"""
Week 1, Day 5: LLM query rewriting.

Patient notes are long and noisy. gpt-oss (on Groq) pulls out the key
facts and writes two clean queries:
  - "keywords" -> used for BM25
  - "summary"  -> used for dense retrieval (MiniLM)
Then we measure whether retrieval improves.

Setup (inside your .venv):
    pip install groq
    export GROQ_API_KEY="your-key-here"     # never commit this

Run:
    python query_rewrite.py --split 2021 --show 3

Rewrites are cached in data/rewrites_<split>.json, so the LLM is only
called once per patient. Delete that file to regenerate.
Needs bm25_baseline.py and dense_retrieval.py in the same folder,
and their 2021 runs already saved in runs/.
"""
import os

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

import argparse
import json
import time

import bm25s
import faiss
import ir_datasets
import ir_measures
import numpy as np
from groq import Groq
from sentence_transformers import SentenceTransformer

from bm25_baseline import SPLITS, build_or_load_index
from dense_retrieval import embed_corpus, evaluate, load_ranked, pick_device, rrf, save_run

DENSE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DENSE_SLUG = "all-MiniLM-L6-v2"

PROMPT = """You help search for clinical trials a patient might be eligible for.
Read the patient note and return a JSON object with these keys:
- "age": number or null
- "sex": "male", "female", or null
- "primary_diagnosis": the main condition the patient would enroll in a trial for, in standard medical terms
- "other_conditions": list of other relevant diagnoses
- "prior_treatments": list of drugs, therapies, or procedures, using full generic names (expand abbreviations)
- "keywords": one string of 10-25 medical search terms for the primary condition, including synonyms
- "summary": one sentence describing the patient's main condition and situation
Only use facts stated in the note. Do not invent anything.

Patient note:
{note}"""


def rewrite(client, model, note, retries=4):
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": PROMPT.format(note=note)}],
                temperature=0,
                response_format={"type": "json_object"},
            )
            return json.loads(resp.choices[0].message.content)
        except Exception as e:  # rate limits, bad JSON, network
            wait = 5 * 2 ** attempt
            print(f"  retrying in {wait}s ({type(e).__name__}: {e})")
            time.sleep(wait)
    raise RuntimeError("Rewrite failed after retries")


def as_text(value) -> str:
    if isinstance(value, list):
        return " ".join(str(v) for v in value)
    return str(value or "")


def get_rewrites(queries, split, model):
    path = f"data/rewrites_{split}.json"
    os.makedirs("data", exist_ok=True)
    cache = json.load(open(path)) if os.path.exists(path) else {}

    client = Groq()  # reads GROQ_API_KEY
    todo = [q for q in queries if q.query_id not in cache]
    for n, q in enumerate(todo, 1):
        print(f"Rewriting patient {q.query_id} ({n}/{len(todo)})")
        cache[q.query_id] = rewrite(client, model, q.text)
        with open(path, "w") as f:  # save after each call so nothing is lost
            json.dump(cache, f, indent=2)
    return cache


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=SPLITS, default="2021")
    ap.add_argument("--llm", default="openai/gpt-oss-120b")
    ap.add_argument("--k", type=int, default=100)
    ap.add_argument("--show", type=int, default=0, help="print N example rewrites")
    args = ap.parse_args()

    dataset = ir_datasets.load(SPLITS[args.split])
    queries = list(dataset.queries_iter())
    qrels = list(dataset.qrels_iter())

    rewrites = get_rewrites(queries, args.split, args.llm)

    for q in queries[: args.show]:
        print("\n" + "=" * 80)
        print(f"PATIENT {q.query_id}\n--- original ---\n{q.text}\n--- rewrite ---")
        print(json.dumps(rewrites[q.query_id], indent=2))

    # Fall back to the original note if the LLM left a field empty
    kw_texts = [as_text(rewrites[q.query_id].get("keywords")) or q.text for q in queries]
    sum_texts = [as_text(rewrites[q.query_id].get("summary")) or q.text for q in queries]

    # --- BM25 with keywords ---
    retriever, bm25_ids = build_or_load_index()
    res, sc = retriever.retrieve(bm25s.tokenize(kw_texts, stopwords="en"), k=args.k)
    bm25_rw = [
        ir_measures.ScoredDoc(q.query_id, bm25_ids[i], float(s))
        for q, row_i, row_s in zip(queries, res, sc)
        for i, s in zip(row_i, row_s)
    ]
    bm25_rw_path = f"runs/bm25_rewrite_{args.split}.jsonl"
    save_run(bm25_rw, bm25_rw_path)

    # --- Dense with summary ---
    model = SentenceTransformer(DENSE_MODEL, device=pick_device())
    doc_ids, embs = embed_corpus(model, DENSE_SLUG, 25_000)  # reuses saved chunks
    index = faiss.IndexFlatIP(embs.shape[1])
    index.add(embs)
    q_embs = model.encode(sum_texts, normalize_embeddings=True, convert_to_numpy=True)
    scores, idxs = index.search(q_embs.astype(np.float32), args.k)
    dense_rw = [
        ir_measures.ScoredDoc(q.query_id, doc_ids[i], float(s))
        for q, row_i, row_s in zip(queries, idxs, scores)
        for i, s in zip(row_i, row_s)
    ]
    dense_rw_path = f"runs/dense_rewrite_{args.split}.jsonl"
    save_run(dense_rw, dense_rw_path)

    # --- Compare ---
    n = len(queries)
    orig_bm25 = load_ranked(f"runs/bm25_{args.split}.jsonl")
    orig_dense = load_ranked(f"runs/dense_{DENSE_SLUG}_{args.split}.jsonl")
    rw_bm25, rw_dense = load_ranked(bm25_rw_path), load_ranked(dense_rw_path)

    evaluate("BM25 (LLM keywords)", bm25_rw, qrels, n)
    evaluate("Dense MiniLM (LLM summary)", dense_rw, qrels, n)

    hybrid_rw = rrf([rw_bm25, rw_dense])
    evaluate("Hybrid, rewritten queries only", hybrid_rw, qrels, n)
    save_run(hybrid_rw, f"runs/hybrid_rewrite_{args.split}.jsonl")

    hybrid_all = rrf([orig_bm25, orig_dense, rw_bm25, rw_dense])
    evaluate("Hybrid, original + rewritten (4 runs)", hybrid_all, qrels, n)
    save_run(hybrid_all, f"runs/hybrid_all4_{args.split}.jsonl")


if __name__ == "__main__":
    main()
