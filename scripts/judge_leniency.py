"""Judge leniency check (known weakness 1): grade the same saved responses with and without grading hints.

    .venv/bin/python scripts/judge_leniency.py configs/pilot_nrp_solver.toml runs/judge_leniency \\
        runs/cloud_pilot_r5/accepted/s5-m0001 ... [--memos runs/qwen_solver_smoke_low] [--repeats 2]

For every matter folder it judges the solver attempts (solver/attempt_N.md), the gold and flawed answers, and any
extra memos under --memos/<matter>/attempt_N.md, once per condition ("hints", "nohints") and repeat. Then a referee
that sees the ledger regrades every criterion where the two conditions disagree, to say which one was right.
Calls are cached as JSON under the output folder, so a rerun only makes the calls that are missing.
Prints and saves summary.json: pass rates, run-to-run noise, flips between conditions, gold/flawed checks, the
referee's verdicts, and each matter's solver pass rate under each condition.
"""

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ltg import prompts  # noqa: E402
from ltg.config import build_client, load_config  # noqa: E402
from ltg.models import CallLog, call_json, render_input  # noqa: E402

REFEREE = """You check one grading decision on a legal memo. You see one rubric criterion, what the answer key
(the ledger) says the criterion is about, and the memo. Decide strictly whether the memo satisfies the criterion:
for an issue, the memo must identify the same problem in substance (the right document and provision, and why it
matters to the client), not just mention nearby words; for a fact, it must state the value correctly; for a
"negative" criterion, pass means the memo did NOT do the bad thing. Quote the memo passage your decision rests on.

Reply with ONLY a JSON object: {"pass": bool, "quote": str, "reason": str}"""

CONDITIONS = ("hints", "nohints")


def load_matter(folder: Path, memos: Path | None) -> dict:
    rubric = json.loads((folder / "rubric.json").read_text())["criteria"]
    answers = json.loads((folder / "answers.json").read_text())
    responses = {f"solver_{p.stem.split('_')[1]}": p.read_text() for p in sorted((folder / "solver").glob("attempt_*.md"))}
    if memos and (memos / folder.name).is_dir():
        responses |= {f"memo_{p.stem.split('_')[1]}": p.read_text() for p in sorted((memos / folder.name).glob("attempt_*.md"))}
    responses |= {"gold": answers["gold"], "flawed": answers["flawed"]}
    return {
        "name": folder.name,
        "rubric": rubric,
        "ledger": json.loads((folder / "ledger.json").read_text()),
        "flawed_omits": answers["flawed_omits"],
        "responses": responses,
    }


def cached(path: Path, make) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    out = make()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2))
    return out


def judge(client, m: dict, resp: str, cond: str, rep: int, out: Path) -> dict[str, bool]:
    """Same payload as ltg.stages.judge, keeping the judge's reasons."""

    def make():
        payload = {
            "response": m["responses"][resp],
            "criteria": [
                {"id": c["id"], "text": c["text"], "kind": c["kind"], **({"grading_hints": c["hints"]} if cond == "hints" and c.get("hints") else {})}
                for c in m["rubric"]
            ],
        }
        return call_json(client, "judge", prompts.JUDGE, render_input(payload))

    got = cached(out / m["name"] / f"{resp}.{cond}.{rep}.json", make)
    res = {r["id"]: bool(r.get("pass")) for r in got.get("results", []) if "id" in r}
    return {c["id"]: res.get(c["id"], False) for c in m["rubric"]}


def referee(client, m: dict, resp: str, crit: dict, out: Path) -> bool:
    led = m["ledger"]
    source = next((x for x in led.get("issues", []) + led.get("facts", []) if x.get("id") == crit.get("source")), None)
    payload = {"criterion": crit["text"], "kind": crit["kind"], "ledger_entry": source, "memo": m["responses"][resp]}
    got = cached(out / m["name"] / f"{resp}.referee.{crit['id']}.json", lambda: call_json(client, "referee", REFEREE, render_input(payload)))
    return bool(got.get("pass"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("out")
    ap.add_argument("matters", nargs="+")
    ap.add_argument("--memos", help="folder of extra memos: <memos>/<matter>/attempt_N.md")
    ap.add_argument("--repeats", type=int, default=2)
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()

    cfg = load_config(a.config)
    client = build_client(cfg, CallLog())
    out = Path(a.out)
    matters = [load_matter(Path(p), Path(a.memos) if a.memos else None) for p in a.matters]

    jobs = [(m, r, c, k) for m in matters for r in m["responses"] for c in CONDITIONS for k in range(1, a.repeats + 1)]
    with ThreadPoolExecutor(a.workers) as pool:
        grades = list(pool.map(lambda j: judge(client, *j, out), jobs))
    g = {(j[0]["name"], j[1], j[2], j[3]): x for j, x in zip(jobs, grades)}

    # A criterion's grade under a condition is settled when every repeat agrees; otherwise it is noise.
    rows = []
    for m in matters:
        for r in m["responses"]:
            for c in m["rubric"]:
                by = {cond: {g[(m["name"], r, cond, k)][c["id"]] for k in range(1, a.repeats + 1)} for cond in CONDITIONS}
                rows.append({"matter": m["name"], "resp": r, "crit": c, "by": by})

    flips = [x for x in rows if all(len(v) == 1 for v in x["by"].values()) and x["by"]["hints"] != x["by"]["nohints"]]
    with ThreadPoolExecutor(a.workers) as pool:
        verdicts = list(pool.map(lambda x: referee(client, next(m for m in matters if m["name"] == x["matter"]), x["resp"], x["crit"], out), flips))

    def rate(cond, kind=None, resp_pred=lambda r: True):
        xs = [g[(m["name"], r, cond, k)][c["id"]] for m in matters for r in m["responses"] if resp_pred(r)
              for c in m["rubric"] if kind in (None, c["kind"]) for k in range(1, a.repeats + 1)]
        return round(sum(xs) / max(len(xs), 1), 3)

    def all_pass_rate(m, cond, prefix):
        rs = [r for r in m["responses"] if r.startswith(prefix)]
        return [round(sum(all(g[(m["name"], r, cond, k)].values()) for r in rs) / len(rs), 3) for k in range(1, a.repeats + 1)] if rs else None

    def flawed_omitted_passed(cond):
        n = t = 0
        for m in matters:
            for c in m["rubric"]:
                if c.get("source") in m["flawed_omits"]:
                    for k in range(1, a.repeats + 1):
                        t += 1
                        n += g[(m["name"], "flawed", cond, k)][c["id"]]
        return f"{n} of {t}"

    is_attempt = lambda r: r.startswith(("solver_", "memo_"))  # noqa: E731
    summary = {
        "matters": len(matters),
        "responses": sum(len(m["responses"]) for m in matters),
        "criterion_grades_per_condition": len(rows) * a.repeats,
        "pass_rate_attempts": {cond: rate(cond, resp_pred=is_attempt) for cond in CONDITIONS},
        "pass_rate_attempts_by_kind": {k: {cond: rate(cond, k, is_attempt) for cond in CONDITIONS} for k in sorted({c["kind"] for m in matters for c in m["rubric"]})},
        "gold_criteria_passed": {cond: rate(cond, resp_pred=lambda r: r == "gold") for cond in CONDITIONS},
        "flawed_omitted_issue_criteria_passed": {cond: flawed_omitted_passed(cond) for cond in CONDITIONS},
        "noise_unsettled_grades": {cond: sum(len(x["by"][cond]) > 1 for x in rows) for cond in CONDITIONS},
        "flips": {
            "total": len(flips),
            "hints_pass_nohints_fail": sum(True in x["by"]["hints"] for x in flips),
            "nohints_pass_hints_fail": sum(True in x["by"]["nohints"] for x in flips),
            "referee_sides_with_hints": sum((True in x["by"]["hints"]) == v for x, v in zip(flips, verdicts)),
            "referee_sides_with_nohints": sum((True in x["by"]["nohints"]) == v for x, v in zip(flips, verdicts)),
            "detail": [
                {"matter": x["matter"], "resp": x["resp"], "crit": x["crit"]["id"], "kind": x["crit"]["kind"],
                 "hints": True in x["by"]["hints"], "referee": v}
                for x, v in zip(flips, verdicts)
            ],
        },
        "solver_pass_rate_per_repeat": {
            m["name"]: {cond: {p: all_pass_rate(m, cond, p) for p in ("solver_", "memo_") if all_pass_rate(m, cond, p)} for cond in CONDITIONS}
            for m in matters
        },
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps({k: v for k, v in summary.items() if k != "flips"} | {"flips": {k: v for k, v in summary["flips"].items() if k != "detail"}}, indent=2))


if __name__ == "__main__":
    main()
