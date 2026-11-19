"""
Write a review sheet of cases where the agent and the TREC label disagree.

Run:
    python review_agent.py --split 2021

Open notes/agent_review_2021.md and press Cmd+Shift+V.
For each case, decide who is right: the agent, the label, or unclear.
"""
import argparse
import json

import ir_datasets

SPLITS = {
    "2021": "clinicaltrials/2021/trec-ct-2021",
    "2022": "clinicaltrials/2021/trec-ct-2022",
}
LABEL_NAME = {2: "eligible", 1: "excluded", 0: "not_relevant"}

# The disagreements that matter most for ranking, in order
FOCUS = [
    (2, "excluded", "TREC says ELIGIBLE, agent says EXCLUDED (good trial pushed down)"),
    (1, "eligible", "TREC says EXCLUDED, agent says ELIGIBLE (missed an exclusion)"),
]

VERDICT_BOX = """**Who is right?** (mark one)
- [ ] Agent wrong: misread the note or the criterion
- [ ] Agent too strict: e.g. ignored a time window ("within 4 weeks") or a "unless" clause
- [ ] Label looks wrong (like the CPT-11 case)
- [ ] Unclear / needs more info

Notes:
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=SPLITS, default="2021")
    ap.add_argument("--tag", default="")
    args = ap.parse_args()

    suffix = f"_{args.tag}" if args.tag else ""
    dataset = ir_datasets.load(SPLITS[args.split])
    notes = {q.query_id: q.text for q in dataset.queries_iter()}
    labels = {(r.query_id, r.doc_id): r.relevance for r in dataset.qrels_iter()}
    trials = ir_datasets.load("clinicaltrials/2021").docs_store()

    recs = [json.loads(line) for line in open(f"data/agent_{args.split}{suffix}.jsonl")]

    out = f"notes/agent_review_{args.split}{suffix}.md"
    with open(out, "w") as f:
        f.write(f"# Agent vs TREC disagreements: {args.split}{suffix}\n\n")
        for label, verdict, title in FOCUS:
            cases = [r for r in recs if labels.get((r["query_id"], r["doc_id"])) == label
                     and r["verdict"] == verdict]
            f.write(f"# {title}: {len(cases)} cases\n\n")
            for r in cases:
                trial = trials.get(r["doc_id"])
                f.write(f"---\n\n## Patient {r['query_id']} | {r['doc_id']}\n\n")
                f.write(f"**Trial:** {trial.title}\n\n")
                f.write(f"**Agent reason:** {r['reason']}\n\n")
                fails = [c for c in r["criteria"] if c.get("status") == "fail"]
                if fails:
                    f.write("**Criteria the agent marked FAIL:**\n\n")
                    for c in fails:
                        f.write(f"- ({c.get('type')}) {c.get('criterion')}\n")
                        f.write(f"  - evidence: \"{c.get('evidence')}\"\n")
                        f.write(f"  - reasoning: {c.get('reasoning')}\n")
                    f.write("\n")
                f.write(f"<details><summary>Patient note</summary>\n\n{notes[r['query_id']].strip()}\n\n</details>\n\n")
                f.write("<details><summary>Full eligibility criteria</summary>\n\n```\n"
                        f"{(trial.eligibility or '').strip()}\n```\n\n</details>\n\n")
                f.write(VERDICT_BOX + "\n")
        f.write("---\n\n# Tally\n\n| | Agent wrong | Too strict | Label wrong | Unclear |\n"
                "|---|---|---|---|---|\n| Eligible -> excluded | | | | |\n"
                "| Excluded -> eligible | | | | |\n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
