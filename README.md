# Cohort: LLM Clinical Trial Matching

Cohort matches patients to clinical trials they may qualify for. Given a patient's admission note, it retrieves candidate trials from 375,580 ClinicalTrials.gov records using hybrid search, then (in progress) uses an LLM agent to check each eligibility criterion and explain its decision.

**Status:** Week 1 (retrieval) complete. Week 2 (eligibility agent) in progress.

## Why this problem

Fewer than 5% of adult cancer patients enroll in clinical trials, and many trials close early for lack of participants. Part of the bottleneck is that eligibility criteria are long free text: a single trial can list 30+ rules, and one line ("No spinal cord tumors") can rule a patient out. Checking one patient against dozens of trials by hand takes coordinators hours.

## Benchmark

[TREC Clinical Trials Track](https://www.trec-cds.org/) 2021 and 2022, loaded with [`ir_datasets`](https://ir-datasets.com/clinicaltrials.html):

- **Corpus:** April 2021 snapshot of ClinicalTrials.gov (375,580 trials)
- **Patients:** synthetic admission notes (75 in 2021, 50 in 2022)
- **Labels:** 2 = eligible, 1 = excluded, 0 = not relevant

All tuning happens on **2021**. **2022 is held out** for final reporting.

## Results (TREC CT 2021, 75 patients)

| Method | nDCG@10 | P@10 (eligible) | MRR (eligible) |
|---|---|---|---|
| BM25 (original note) | 0.3527 | 0.1960 | 0.3801 |
| Dense, all-MiniLM-L6-v2 | 0.3519 | 0.2320 | 0.4588 |
| Dense, S-PubMedBert-MS-MARCO | 0.2574 | 0.1427 | 0.4168 |
| Hybrid BM25 + MiniLM (RRF) | 0.4207 | 0.2573 | 0.4701 |
| BM25 with LLM keywords (gpt-oss-120b) | 0.4055 | 0.2827 | 0.4872 |
| **Hybrid, original + LLM-rewritten queries (4-way RRF)** | **0.4894** | **0.3213** | **0.5793** |

**What I learned**

- **Keyword and semantic search find different good trials.** Fusing them gave +19% nDCG@10 over BM25.
- **A biomedical embedding model did worse than a general one.** PubMedBERT (tuned on short MS MARCO queries) trailed MiniLM by ~0.09 nDCG on long patient notes, and took ~6x longer to embed.
- **LLM query rewriting helped most when combined with the original note.** Rewrites add synonyms and expand abbreviations; the original keeps details the LLM drops. The best setup reaches +39% nDCG@10 over BM25.
- **Rewrites are not always faithful.** In manual review, the LLM sometimes listed diagnostic tests as treatments or overstated certainty. Rewrites are used only for *finding* trials; eligibility decisions will be checked against the original note.
- **The labels contain noise.** In one case a trial labeled "eligible" excludes prior topoisomerase I inhibitors, and the patient had received irinotecan (CPT-11), which is one.

## Run it

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python bm25_baseline.py --split 2021
python dense_retrieval.py --split 2021              # embeds the corpus once (~20 min on an M-series Mac)
export GROQ_API_KEY="..."
python query_rewrite.py --split 2021 --show 3
```

| File | Purpose |
|---|---|
| `explore.py` | Print sample patients and labeled trials |
| `bm25_baseline.py` | BM25 retrieval + evaluation |
| `dense_retrieval.py` | sentence-transformers + FAISS, plus RRF hybrid |
| `query_rewrite.py` | gpt-oss query rewriting via Groq, 4-way fusion |
| `review_rewrites.py` | Side-by-side review sheet for LLM rewrites |
| `notes/findings.md` | Running log of results and observations |

## Data and privacy

Uses only public benchmark data (TREC topics are synthetic patient notes) and public ClinicalTrials.gov records. No real patient data is used anywhere in this project.

## Roadmap

- [x] Week 1: Retrieval baselines, dense and hybrid search, LLM query rewriting
- [ ] Week 2: Criterion-by-criterion eligibility agent with explanations
- [ ] Week 3: Fine-tune a small open model (QLoRA) for criterion checking; compare cost and accuracy with gpt-oss-120b
- [ ] Week 4: vLLM serving, FastAPI, AWS deployment, CI evaluation gates
- [ ] Final numbers on the held-out 2022 set
