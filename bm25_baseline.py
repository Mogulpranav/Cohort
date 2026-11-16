"""
Week 1, Step 1: BM25 baseline on TREC Clinical Trials.

Setup:
    pip install ir_datasets bm25s ir_measures tqdm

Run:
    python bm25_baseline.py --split 2021   # dev set (75 patients): tune here
    python bm25_baseline.py --split 2022   # test set (50 patients): report this

The first run downloads the corpus (375,580 trials) and builds an index.
That takes a while; later runs reuse the saved index.
"""
import argparse
import json
import os

import bm25s
import ir_datasets
import ir_measures
from ir_measures import nDCG, P, RR
from tqdm import tqdm

INDEX_DIR = "index/bm25"
DOC_IDS_PATH = "index/doc_ids.json"
SPLITS = {
    "2021": "clinicaltrials/2021/trec-ct-2021",
    "2022": "clinicaltrials/2021/trec-ct-2022",
}


def trial_text(doc) -> str:
    """Fields used for retrieval. Experiment with this: it matters a lot."""
    parts = [doc.title, doc.condition, doc.summary, doc.eligibility]
    return "\n".join(p for p in parts if p)


def build_or_load_index():
    if os.path.exists(INDEX_DIR) and os.path.exists(DOC_IDS_PATH):
        print("Loading saved index...")
        with open(DOC_IDS_PATH) as f:
            return bm25s.BM25.load(INDEX_DIR), json.load(f)

    print("Building index (first run only)...")
    corpus = ir_datasets.load("clinicaltrials/2021")
    doc_ids, texts = [], []
    for doc in tqdm(corpus.docs_iter(), total=corpus.docs_count()):
        doc_ids.append(doc.doc_id)
        texts.append(trial_text(doc))

    retriever = bm25s.BM25()
    retriever.index(bm25s.tokenize(texts, stopwords="en"))

    os.makedirs("index", exist_ok=True)
    retriever.save(INDEX_DIR)
    with open(DOC_IDS_PATH, "w") as f:
        json.dump(doc_ids, f)
    return retriever, doc_ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=SPLITS, default="2021")
    ap.add_argument("--k", type=int, default=100)
    args = ap.parse_args()

    retriever, doc_ids = build_or_load_index()
    dataset = ir_datasets.load(SPLITS[args.split])
    queries = list(dataset.queries_iter())

    results, scores = retriever.retrieve(
        bm25s.tokenize([q.text for q in queries], stopwords="en"), k=args.k
    )

    run = [
        ir_measures.ScoredDoc(q.query_id, doc_ids[idx], float(s))
        for q, idxs, ss in zip(queries, results, scores)
        for idx, s in zip(idxs, ss)
    ]

    # Labels: 2 = eligible, 1 = excluded, 0 = not relevant
    metrics = [nDCG @ 10, P(rel=2) @ 10, RR(rel=2)]
    agg = ir_measures.calc_aggregate(metrics, dataset.qrels_iter(), run)

    print(f"\nBM25 on TREC CT {args.split} ({len(queries)} patients)")
    for m in metrics:
        print(f"  {str(m):<16} {agg[m]:.4f}")

    os.makedirs("runs", exist_ok=True)
    out = f"runs/bm25_{args.split}.jsonl"
    with open(out, "w") as f:
        for d in run:
            f.write(json.dumps(d._asdict()) + "\n")
    print(f"Run saved to {out}")


if __name__ == "__main__":
    main()
