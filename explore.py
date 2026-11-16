"""
Day 1: look at the data before building anything.

Run (with your .venv active):
    python explore.py

The first run downloads the trials corpus, which takes a while.
Later runs are fast.
"""
import ir_datasets

dataset = ir_datasets.load("clinicaltrials/2021/trec-ct-2021")  # dev split

# ---------- 1. Three patient notes ----------
queries = list(dataset.queries_iter())
print(f"Total patients: {len(queries)}\n")

for q in queries[:3]:
    print("=" * 80)
    print(f"PATIENT {q.query_id}")
    print("=" * 80)
    print(q.text)
    print()

# ---------- 2. Labels for the first patient ----------
first_id = queries[0].query_id
labels = {}  # doc_id -> 0/1/2
for qrel in dataset.qrels_iter():
    if qrel.query_id == first_id:
        labels[qrel.doc_id] = qrel.relevance

counts = {lbl: sum(1 for v in labels.values() if v == lbl) for lbl in (0, 1, 2)}
print(f"Patient {first_id} has {len(labels)} judged trials: "
      f"{counts[2]} eligible, {counts[1]} excluded, {counts[0]} not relevant\n")

# ---------- 3. One eligible, one excluded, one not-relevant trial ----------
docs = dataset.docs_store()  # first call downloads the corpus
NAMES = {2: "ELIGIBLE", 1: "EXCLUDED", 0: "NOT RELEVANT"}

for label in (2, 1, 0):
    match = next((d for d, v in labels.items() if v == label), None)
    if match is None:
        continue
    trial = docs.get(match)
    print("=" * 80)
    print(f"{NAMES[label]}  |  {trial.doc_id}  |  {trial.title}")
    print("=" * 80)
    print(f"Condition: {trial.condition}\n")
    print("Eligibility criteria (first 1500 chars):")
    print(trial.eligibility[:1500])
    print()
