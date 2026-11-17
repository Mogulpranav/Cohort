# Cohort: Findings Log

## Results

| Date | Method | Split | nDCG@10 | P@10 | MRR |
|------|--------|-------|---------|------|-----|
| 2026-11-15 | BM25 (title+condition+summary+eligibility) | 2021 dev | 0.3527 | 0.1960 | 0.3801 |

| 2026-11-17 | Dense all-MiniLM-L6-v2 (title+condition+summary) | 2021 dev | 0.3519 | 0.2320 | 0.4588 |
| 2026-11-17 | Hybrid BM25 + MiniLM (RRF, k=60) | 2021 dev | 0.4207 | 0.2573 | 0.4701 |

Rule: tune on 2021, report final numbers on 2022 only once.

## Data observations (Day 1)

- Patient 1 (45M, spinal anaplastic astrocytoma) has 407 judged trials:
  47 eligible, 122 excluded, 238 not relevant. Many trials look right
  but aren't, so search alone isn't enough.
- **Excluded trial NCT00002569:** topic matches, but "No spinal cord tumors"
  and oligodendroglioma (not astrocytoma) rule him out. A single line decides.
- **Not relevant NCT00002806:** shares keywords (glioma, chemo, radiation)
  but wrong grade (I/II vs III), wrong location, and requires no prior chemo.
- **Label noise, NCT00002814:** labeled eligible, but it excludes prior
  topoisomerase I inhibitors, and the patient had CPT-11 (irinotecan), which is one.
  The labels aren't perfect, and the task needs drug knowledge.
- The "condition" field is empty in older trials, so rely on eligibility text.
- Eligibility formatting is inconsistent (bullets vs run-on paragraphs).
- Patient notes contain abbreviations (s/p, h/o, SOB) and de-identified
  dates like [**2148-10-1**].
- Dense ties BM25 on nDCG but ranks eligible trials higher (P@10, MRR).
  Hybrid gives +19% nDCG over BM25: the two methods find different good trials.
- Dense embeds only title+condition+summary (models read ~256 tokens max).

## Ideas to try
- Dense retrieval (sentence-transformers + FAISS), general vs biomedical model
- Hybrid BM25 + dense (Reciprocal Rank Fusion)
- LLM query rewriting from patient notes