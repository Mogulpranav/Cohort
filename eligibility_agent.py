"""
Week 2: criterion-by-criterion eligibility agent.

For each patient, take the top-K trials from the best retrieval run
(4-way hybrid), ask gpt-oss to check each eligibility criterion
against the ORIGINAL patient note, then:
  1. Re-rank: eligible > excluded > not relevant (ties keep retrieval order)
  2. Measure: nDCG@10 / P@10 / MRR before vs after, on the same patients
  3. Measure: verdict accuracy vs TREC labels, and whether the
     quoted evidence really appears in the patient note

Setup:
    export GROQ_API_KEY="..."

Pilot run (10 patients x top 10 trials = 100 LLM calls):
    python eligibility_agent.py --split 2021 --patients 10 --top 10 --show-fails 3

Every decision is cached in data/agent_<split>.jsonl, so you can stop
any time and rerun the same command to continue. Increase --patients
later to scale up without repeating finished calls.
"""
import argparse
import json
import os
import re
import time
from collections import Counter

import ir_datasets
import ir_measures
from groq import Groq
from ir_measures import nDCG, P, RR

SPLITS = {
    "2021": "clinicaltrials/2021/trec-ct-2021",
    "2022": "clinicaltrials/2021/trec-ct-2022",
}
METRICS = [nDCG @ 10, P(rel=2) @ 10, RR(rel=2)]
VERDICT_SCORE = {"eligible": 2, "excluded": 1, "not_relevant": 0}
LABEL_NAME = {2: "eligible", 1: "excluded", 0: "not_relevant"}
MAX_CRITERIA_CHARS = 6000  # a few trials have extremely long criteria

PROMPT = """You are a clinical research coordinator screening a patient for a clinical trial.

PATIENT NOTE:
{note}

TRIAL TITLE: {title}

ELIGIBILITY CRITERIA:
{criteria}

Instructions:
1. Decide whether this trial targets the patient's condition at all.
2. Check the criteria that matter for this patient. For each one, set "status":
   - "pass": the note shows the patient satisfies this rule
     (for an exclusion rule, "pass" means the patient does NOT have the excluding condition)
   - "fail": the note shows the patient breaks this rule
   - "unknown": the note does not say
   Skip administrative rules (consent, contraception, willingness to comply) unless the note addresses them.
   List at most 20 criteria, but always include every criterion with status "fail".
3. For "pass" and "fail", copy the exact supporting words from the PATIENT NOTE into "evidence".
   Never put anything in "evidence" that is not written in the note.
   Use medical knowledge to connect evidence to the rule (for example, irinotecan is a
   topoisomerase I inhibitor) and explain the link in "reasoning".
4. Final verdict:
   - "not_relevant": the trial is not for the patient's condition
   - "excluded": the trial is relevant, but at least one criterion is "fail"
   - "eligible": the trial is relevant and no criterion is "fail" ("unknown" is allowed)

Return only a JSON object in this format:
{{"criteria": [{{"type": "inclusion or exclusion", "criterion": "...", "status": "pass, fail, or unknown", "evidence": "...", "reasoning": "..."}}],
  "verdict": "eligible, excluded, or not_relevant",
  "reason": "one sentence"}}"""


# ---------------------------------------------------------------- helpers
def load_ranked(path):
    by_q = {}
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            by_q.setdefault(r["query_id"], []).append((r["score"], r["doc_id"]))
    return {q: [d for _, d in sorted(v, reverse=True)] for q, v in by_q.items()}


def norm(text):
    return re.sub(r"\s+", " ", (text or "").lower()).strip()


def grounded(evidence, note):
    """True if every piece of the quote appears in the note.
    Handles quotes the model shortened with '...' between real fragments."""
    parts = [norm(p).strip(" .,;:\"'") for p in re.split(r"\.\.\.|\u2026", evidence)]
    parts = [p for p in parts if p]
    return bool(parts) and all(p in norm(note) for p in parts)


class DailyLimitReached(Exception):
    pass


def call_llm(client, model, prompt, effort=None, retries=5):
    extra = {"reasoning_effort": effort} if effort else {}
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                response_format={"type": "json_object"},
                **extra,
            )
            usage = {
                "prompt_tokens": resp.usage.prompt_tokens,
                "completion_tokens": resp.usage.completion_tokens,
            }
            out = json.loads(resp.choices[0].message.content)
            if out.get("verdict") not in VERDICT_SCORE:
                raise ValueError(f"bad verdict: {out.get('verdict')!r}")
            return out, usage
        except Exception as e:  # rate limits, bad JSON, network
            msg = str(e)
            # A daily quota won't reset in a few minutes: stop cleanly instead of retrying
            if "per day" in msg or "(TPD)" in msg or "(RPD)" in msg:
                raise DailyLimitReached(msg)
            wait = 10 * 2 ** attempt
            print(f"    retrying in {wait}s ({type(e).__name__}: {msg[:160]})")
            time.sleep(wait)
    return None, None


def evaluate(name, run, qrels, n):
    agg = ir_measures.calc_aggregate(METRICS, qrels, run)
    print(f"\n{name} ({n} patients)")
    for m in METRICS:
        print(f"  {str(m):<16} {agg[m]:.4f}")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=SPLITS, default="2021")
    ap.add_argument("--run", default="runs/hybrid_all4_{split}.jsonl")
    ap.add_argument("--llm", default="openai/gpt-oss-120b")
    ap.add_argument("--patients", type=int, default=10)
    ap.add_argument("--top", type=int, default=10, help="trials checked per patient")
    ap.add_argument("--sleep", type=float, default=0.0, help="pause between calls (rate limits)")
    ap.add_argument("--show-fails", type=int, default=0, help="print N example exclusions")
    ap.add_argument("--tag", default="", help="separate cache for an experiment, e.g. --tag low")
    ap.add_argument("--effort", choices=["low", "medium", "high"], default=None,
                    help="gpt-oss reasoning effort; 'low' uses far fewer tokens")
    args = ap.parse_args()

    dataset = ir_datasets.load(SPLITS[args.split])
    notes = {q.query_id: q.text for q in dataset.queries_iter()}
    qrels = list(dataset.qrels_iter())
    labels = {(r.query_id, r.doc_id): r.relevance for r in qrels}
    run = load_ranked(args.run.format(split=args.split))
    qids = [q for q in notes if q in run][: args.patients]
    trials = ir_datasets.load("clinicaltrials/2021").docs_store()

    # ---- load cache
    cache_path = f"data/agent_{args.split}{'_' + args.tag if args.tag else ''}.jsonl"
    os.makedirs("data", exist_ok=True)
    done = {}
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            for line in f:
                r = json.loads(line)
                done[(r["query_id"], r["doc_id"])] = r

    # ---- run the agent on (patient, trial) pairs not yet done
    client = Groq()
    pairs = [(q, d, rank) for q in qids for rank, d in enumerate(run[q][: args.top], start=1)]
    todo = [p for p in pairs if (p[0], p[1]) not in done]
    print(f"{len(pairs)} pairs, {len(pairs) - len(todo)} cached, {len(todo)} to run")

    for n, (qid, did, rank) in enumerate(todo, 1):
        trial = trials.get(did)
        prompt = PROMPT.format(
            note=notes[qid],
            title=trial.title,
            criteria=(trial.eligibility or "")[:MAX_CRITERIA_CHARS],
        )
        t0 = time.time()
        try:
            out, usage = call_llm(client, args.llm, prompt, effort=args.effort)
        except DailyLimitReached as e:
            print(f"\nDaily Groq limit reached. Progress is saved in {cache_path}.")
            print("Rerun the same command after the limit resets to continue.")
            print(f"Groq said: {str(e)[:400]}")
            break
        if out is None:
            print(f"  [{n}/{len(todo)}] {qid} | {did} | FAILED, will retry on next run")
            continue
        rec = {
            "query_id": qid,
            "doc_id": did,
            "rank": rank,
            "verdict": out.get("verdict"),
            "reason": out.get("reason"),
            "criteria": out.get("criteria", []),
            "usage": usage,
            "latency_s": round(time.time() - t0, 2),
            "model": args.llm,
        }
        with open(cache_path, "a") as f:
            f.write(json.dumps(rec) + "\n")
        done[(qid, did)] = rec
        label = LABEL_NAME.get(labels.get((qid, did)), "unjudged")
        print(f"  [{n}/{len(todo)}] patient {qid} | {did} | agent: {rec['verdict']:<12} | TREC: {label}")
        if args.sleep:
            time.sleep(args.sleep)

    # ---- only evaluate patients whose top-K are all finished
    evaluated = [q for q in qids if all((q, d) in done for d in run[q][: args.top])]
    if not evaluated:
        print("\nNo patient fully processed yet; rerun to continue.")
        return
    ev = set(evaluated)
    sub_qrels = [r for r in qrels if r.query_id in ev]

    base_run, agent_run = [], []
    for q in evaluated:
        for rank, d in enumerate(run[q], start=1):
            base_run.append(ir_measures.ScoredDoc(q, d, float(-rank)))
            if rank <= args.top:
                v = VERDICT_SCORE.get(done[(q, d)]["verdict"], 1)
                score = v * 1000 + (1000 - rank)  # verdict first, retrieval order breaks ties
            else:
                score = float(-rank)  # unchecked tail stays below checked trials
            agent_run.append(ir_measures.ScoredDoc(q, d, float(score)))

    print("\n" + "=" * 70)
    evaluate("Retrieval only (4-way hybrid)", base_run, sub_qrels, len(evaluated))
    evaluate(f"Retrieval + eligibility agent (re-rank top {args.top})", agent_run, sub_qrels, len(evaluated))

    # ---- verdict accuracy on judged pairs
    recs = [done[(q, d)] for q in evaluated for d in run[q][: args.top]]
    judged = [(labels[(r["query_id"], r["doc_id"])], r["verdict"]) for r in recs
              if (r["query_id"], r["doc_id"]) in labels]
    conf = Counter(judged)
    names = ["eligible", "excluded", "not_relevant"]
    print(f"\nVerdict vs TREC label ({len(judged)} judged of {len(recs)} checked pairs)")
    print(f"  {'TREC label':<14}" + "".join(f"{v:>14}" for v in names))
    for lbl in (2, 1, 0):
        print(f"  {LABEL_NAME[lbl]:<14}" + "".join(f"{conf[(lbl, v)]:>14}" for v in names))
    correct = sum(conf[(lbl, LABEL_NAME[lbl])] for lbl in (2, 1, 0))
    if judged:
        print(f"  Exact agreement: {correct}/{len(judged)} = {correct / len(judged):.1%}")

    # ---- is the evidence really in the note?
    for status in ("fail", "pass"):
        items = [(r["query_id"], c) for r in recs for c in r["criteria"]
                 if c.get("status") == status and c.get("evidence")]
        found = sum(grounded(c["evidence"], notes[q]) for q, c in items)
        if items:
            print(f"  Evidence quoted verbatim from note ({status}): {found}/{len(items)} = {found / len(items):.1%}")

    # ---- cost and speed
    pt = [r["usage"]["prompt_tokens"] for r in recs]
    ct = [r["usage"]["completion_tokens"] for r in recs]
    lat = sorted(r["latency_s"] for r in recs)
    print(f"\nPer trial check: ~{sum(pt) / len(pt):.0f} prompt + {sum(ct) / len(ct):.0f} completion tokens, "
          f"median latency {lat[len(lat) // 2]:.1f}s")
    print(f"Total tokens so far: {sum(pt) + sum(ct):,}")

    # ---- examples to read
    shown = 0
    for r in recs:
        if shown >= args.show_fails:
            break
        fails = [c for c in r["criteria"] if c.get("status") == "fail"]
        if r["verdict"] != "excluded" or not fails:
            continue
        shown += 1
        label = LABEL_NAME.get(labels.get((r["query_id"], r["doc_id"])), "unjudged")
        print("\n" + "-" * 70)
        print(f"Patient {r['query_id']} | {r['doc_id']} | {trials.get(r['doc_id']).title}")
        print(f"Agent: excluded | TREC label: {label}\nReason: {r['reason']}")
        for c in fails:
            print(f"  FAIL ({c.get('type')}): {c.get('criterion')}")
            print(f"    evidence:  \"{c.get('evidence')}\"")
            print(f"    reasoning: {c.get('reasoning')}")


if __name__ == "__main__":
    main()
