"""
Write a side-by-side review file: original patient note vs. LLM rewrite.

Run:
    python review_rewrites.py --split 2021 --n 10

Then open notes/rewrite_review_2021.md in VS Code and press
Cmd+Shift+V to see it formatted. Fill in the checklist for each patient.
"""
import argparse
import json

import ir_datasets

SPLITS = {
    "2021": "clinicaltrials/2021/trec-ct-2021",
    "2022": "clinicaltrials/2021/trec-ct-2022",
}

CHECKLIST = """**Checklist** (mark [x] if there's a problem, and note what it is):
- [ ] Invented a fact not in the note:
- [ ] Changed certainty ("consistent with" became "diagnosed with"):
- [ ] Wrong field (e.g. a test listed as a treatment):
- [ ] Dropped something important:
- [ ] Age or sex wrong:
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=SPLITS, default="2021")
    ap.add_argument("--n", type=int, default=10)
    args = ap.parse_args()

    rewrites = json.load(open(f"data/rewrites_{args.split}.json"))
    queries = list(ir_datasets.load(SPLITS[args.split]).queries_iter())[: args.n]

    out = f"notes/rewrite_review_{args.split}.md"
    with open(out, "w") as f:
        f.write(f"# Rewrite review: TREC CT {args.split} (first {len(queries)} patients)\n\n")
        for q in queries:
            r = rewrites[q.query_id]
            f.write(f"---\n\n## Patient {q.query_id}\n\n")
            f.write(f"### Original note\n\n{q.text.strip()}\n\n")
            f.write("### LLM rewrite\n\n")
            f.write(f"- **Age / sex:** {r.get('age')} / {r.get('sex')}\n")
            f.write(f"- **Primary diagnosis:** {r.get('primary_diagnosis')}\n")
            f.write(f"- **Other conditions:** {', '.join(r.get('other_conditions') or [])}\n")
            f.write(f"- **Prior treatments:** {', '.join(r.get('prior_treatments') or [])}\n")
            f.write(f"- **Summary:** {r.get('summary')}\n")
            f.write(f"- **Keywords:** {r.get('keywords')}\n\n")
            f.write(CHECKLIST + "\n")
        f.write("---\n\n## Tally\n\nPatients with at least one problem: __ / "
                f"{len(queries)}\n\nMost common problem: \n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
