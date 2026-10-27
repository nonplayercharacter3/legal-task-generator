"""Solver-only smoke test: run the configured solver on the accepted cloud pilot tasks, with no judging and no Claude calls.

    .venv/bin/python scripts/solve_only.py configs/pilot_nrp_solver.toml runs/qwen_solver_smoke

Run from the repo root (the task paths are relative). Saves attempt_N.md, attempt_N.trace.json and attempt_N.calls.json
(every raw solver reply and whether it parsed) per task, and summary.json. Use it to check a new solver model follows
the tool protocol and finishes its memo before spending a round on it.
"""

import json
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ltg.config import build_client, load_config  # noqa: E402
from ltg.models import CallLog, parse_json  # noqa: E402
from ltg import prompts  # noqa: E402
from ltg.solver import solve  # noqa: E402

TASKS = [
    "runs/cloud_pilot_r2/accepted/s2-m0003",
    "runs/cloud_pilot_r3/accepted/s3-m0001",
    "runs/cloud_pilot_r5/accepted/s5-m0001",
    "runs/cloud_pilot_r5/accepted/s5-m0002",
]
ATTEMPTS = 3

cfg = load_config(sys.argv[1])
out_root = Path(sys.argv[2])
log = CallLog()
client = build_client(cfg, log)


class Spy:
    """Records every raw solver reply so protocol slips hidden by call_json's silent retry show up."""

    def __init__(self):
        self.calls = []

    def complete(self, role, system, user):
        t = time.time()
        out = client.complete(role, system, user)
        rec = {"system": system[:40], "seconds": round(time.time() - t, 1), "chars_in": len(user), "reply": out}
        try:
            obj = parse_json(out)
            rec["parsed"] = isinstance(obj, dict)
            rec["strict_json"] = out.strip().startswith("{")
        except Exception as e:  # noqa: BLE001
            rec["parsed"], rec["error"] = False, str(e)
        self.calls.append(rec)
        return out


def run(task: str, k: int) -> dict:
    t = Path(task)
    docs = {p.name: p.read_text() for p in sorted((t / "docs").iterdir())}
    instruction = (t / "instruction.md").read_text()
    out = out_root / t.name
    out.mkdir(parents=True, exist_ok=True)
    spy, t0 = Spy(), time.time()
    row = {"task": t.name, "attempt": k}
    try:
        sol = solve(spy, instruction, docs, cfg.gates.solver_max_steps, cfg.gates.solver_page_chars)
        (out / f"attempt_{k}.md").write_text(sol.answer)
        (out / f"attempt_{k}.trace.json").write_text(json.dumps(sol.steps, indent=2))
        row.update(steps=len(sol.steps), memo_words=len(sol.answer.split()), files_opened=sol.files_opened(), n_docs=len(docs))
    except Exception as e:  # noqa: BLE001
        row["error"] = f"{type(e).__name__}: {e}"
        (out / f"attempt_{k}.error.txt").write_text(traceback.format_exc())
    (out / f"attempt_{k}.calls.json").write_text(json.dumps(spy.calls, indent=2))
    step_calls = [c for c in spy.calls if c["system"] == prompts.SOLVER_STEP[:40]]
    row.update(
        minutes=round((time.time() - t0) / 60, 1),
        calls=len(spy.calls),
        unparsed=sum(not c["parsed"] for c in spy.calls),
        not_bare_json=sum(c.get("parsed") and not c.get("strict_json") for c in step_calls),
    )
    print(json.dumps(row), flush=True)
    return row


jobs = [(task, k) for task in TASKS for k in range(1, ATTEMPTS + 1)]
with ThreadPoolExecutor(6) as pool:  # NRP allows 8 simultaneous requests for qwen3-small
    rows = list(pool.map(lambda j: run(*j), jobs))
(out_root / "summary.json").write_text(json.dumps(rows, indent=2))
solver_calls = [r for r in log.records if r.role == "solver"]
print(f"{len(solver_calls)} calls, {sum(not r.ok for r in solver_calls)} failed, "
      f"{sum(r.input_tokens or 0 for r in solver_calls):,} in / {sum(r.output_tokens or 0 for r in solver_calls):,} out tokens")
