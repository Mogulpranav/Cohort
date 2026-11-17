"""
Week 1, Days 3-4: dense retrieval (sentence-transformers + FAISS) and hybrid (RRF).

Setup (inside your .venv):
    pip install sentence-transformers faiss-cpu

Run:
    python dense_retrieval.py --split 2021
    python dense_retrieval.py --split 2021 --model pritamdeka/S-PubMedBert-MS-MARCO

The first run embeds all 375,580 trials and saves them in chunks under
index/dense/<model>/. If you stop it (Ctrl+C) or the laptop sleeps,
just run the same command again: finished chunks are skipped.

If runs/bm25_<split>.jsonl exists, the script also scores a
BM25 + dense hybrid using Reciprocal Rank Fusion.
"""
import os

# faiss and torch each ship OpenMP on macOS; this stops the
# "OMP: Error #15" crash. Must be set before importing them.
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

import argparse
import json
import math
from collections import defaultdict

import faiss
import ir_datasets
import ir_measures
import numpy as np
import torch
from ir_measures import nDCG, P, RR
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

SPLITS = {
    "2021": "clinicaltrials/2021/trec-ct-2021",
    "2022": "clinicaltrials/2021/trec-ct-2022",
}
METRICS = [nDCG @ 10, P(rel=2) @ 10, RR(rel=2)]


def trial_text(doc) -> str:
    """Short, topical fields only. Models read ~256 tokens at most,
    so long eligibility text would get cut off anyway."""
    parts = [doc.title, doc.condition, doc.summary]
    return "\n".join(p for p in parts if p)


def pick_device() -> str:
    if torch.backends.mps.is_available():
        return "mps"  # Apple Silicon GPU
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def embed_corpus(model, model_slug, chunk_size):
    out_dir = f"index/dense/{model_slug}"
    os.makedirs(out_dir, exist_ok=True)

    corpus = ir_datasets.load("clinicaltrials/2021")
    doc_ids, texts = [], []
    for doc in tqdm(corpus.docs_iter(), total=corpus.docs_count(), desc="Loading trials"):
        doc_ids.append(doc.doc_id)
        texts.append(trial_text(doc))

    n_chunks = math.ceil(len(texts) / chunk_size)
    for i in range(n_chunks):
        path = f"{out_dir}/chunk_{i:03d}.npy"
        if os.path.exists(path):
            continue
        print(f"\nEmbedding chunk {i + 1}/{n_chunks}")
        emb = model.encode(
            texts[i * chunk_size:(i + 1) * chunk_size],
            batch_size=64,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=True,
        )
        np.save(path, emb.astype(np.float32))

    embs = np.vstack([np.load(f"{out_dir}/chunk_{i:03d}.npy") for i in range(n_chunks)])
    assert embs.shape[0] == len(doc_ids), "Chunk count mismatch: delete the folder and rerun"
    return doc_ids, embs


def evaluate(name, run, qrels, n_queries):
    agg = ir_measures.calc_aggregate(METRICS, qrels, run)
    print(f"\n{name} ({n_queries} patients)")
    for m in METRICS:
        print(f"  {str(m):<16} {agg[m]:.4f}")


def save_run(run, path):
    os.makedirs("runs", exist_ok=True)
    with open(path, "w") as f:
        for d in run:
            f.write(json.dumps(d._asdict()) + "\n")
    print(f"Run saved to {path}")


def load_ranked(path):
    """jsonl run -> {query_id: [doc_id, ...] best first}"""
    by_q = defaultdict(list)
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            by_q[r["query_id"]].append((r["score"], r["doc_id"]))
    return {q: [d for _, d in sorted(v, reverse=True)] for q, v in by_q.items()}


def rrf(ranked_runs, k=60):
    """Reciprocal Rank Fusion: score(d) = sum over runs of 1 / (k + rank)."""
    fused = defaultdict(lambda: defaultdict(float))
    for run in ranked_runs:
        for qid, docs in run.items():
            for rank, doc_id in enumerate(docs, start=1):
                fused[qid][doc_id] += 1.0 / (k + rank)
    return [
        ir_measures.ScoredDoc(qid, doc_id, score)
        for qid, scores in fused.items()
        for doc_id, score in scores.items()
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=SPLITS, default="2021")
    ap.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    ap.add_argument("--k", type=int, default=100)
    ap.add_argument("--chunk-size", type=int, default=25_000)
    args = ap.parse_args()

    device = pick_device()
    model = SentenceTransformer(args.model, device=device)
    model_slug = args.model.split("/")[-1]
    print(f"Model: {args.model} | device: {device} | max tokens: {model.max_seq_length}")

    doc_ids, embs = embed_corpus(model, model_slug, args.chunk_size)

    index = faiss.IndexFlatIP(embs.shape[1])  # inner product = cosine (vectors normalized)
    index.add(embs)

    dataset = ir_datasets.load(SPLITS[args.split])
    queries = list(dataset.queries_iter())
    qrels = list(dataset.qrels_iter())

    q_embs = model.encode(
        [q.text for q in queries], normalize_embeddings=True, convert_to_numpy=True
    ).astype(np.float32)
    scores, idxs = index.search(q_embs, args.k)

    run = [
        ir_measures.ScoredDoc(q.query_id, doc_ids[i], float(s))
        for q, row_i, row_s in zip(queries, idxs, scores)
        for i, s in zip(row_i, row_s)
    ]
    evaluate(f"Dense {model_slug} on TREC CT {args.split}", run, qrels, len(queries))
    dense_path = f"runs/dense_{model_slug}_{args.split}.jsonl"
    save_run(run, dense_path)

    bm25_path = f"runs/bm25_{args.split}.jsonl"
    if os.path.exists(bm25_path):
        hybrid = rrf([load_ranked(bm25_path), load_ranked(dense_path)])
        evaluate(f"Hybrid BM25 + {model_slug} (RRF)", hybrid, qrels, len(queries))
        save_run(hybrid, f"runs/hybrid_{model_slug}_{args.split}.jsonl")
    else:
        print(f"\n(No {bm25_path} found; run bm25_baseline.py first for the hybrid score.)")


if __name__ == "__main__":
    main()
