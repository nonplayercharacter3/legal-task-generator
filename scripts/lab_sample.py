"""Draw the LAB sample and ours, run them through lab_run.py (4 at a time), and write summary.json.

    runs/lab_venv/bin/python scripts/lab_sample.py draw   # prints the draw and the judge-call projection, writes sample.json
    runs/lab_venv/bin/python scripts/lab_sample.py run    # runs every task in sample.json without a scores.json yet

LAB root is runs/lab_root of the main checkout (see lab_run.py); the sample, logs and summary.json go to
runs/lab_sample/. The draw is fixed by SEED: 20 LAB tasks from corporate-ma and contracts (the slice ours resemble),
10 from the other areas, and 20 of ours, 5 per qwen3-small label where the pool has them.
"""

import json
import os
import random
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "scripts"))
from ltg.export import difficulty, task_id  # noqa: E402
import to_lab_format  # noqa: E402

MAIN = Path("/Users/shesirui/Projects/legal-task-generator")
LAB = Path("/Users/shesirui/Projects/harvey-labs/tasks")
ROOT, OUT = MAIN / "runs/lab_root", MAIN / "runs/lab_sample"
SEED, TAG, WORKERS = 46, "s1", 4
LABELS = (0.0, 0.333, 0.667, 1.0)


def lab_tasks() -> dict[str, int]:
    return {str(p.parent.relative_to(LAB)): len(json.loads(p.read_text())["criteria"]) for p in sorted(LAB.rglob("task.json"))}


def ours() -> dict[float, list[Path]]:
    pool: dict[float, dict[str, Path]] = {l: {} for l in LABELS}
    for t in sorted(MAIN.glob("runs/*/accepted/*/task.json")):
        m, task = t.parent, json.loads(t.read_text())
        if task.get("hold") or task.get("label_pending"):
            continue
        mine = [d for d in difficulty(task, {}) if d["model"] == "qwen3-small"]
        if mine:
            pool[min(LABELS, key=lambda l: abs(l - mine[0]["pass_rate"]))].setdefault(task_id(m), m)
    return {l: list(v.values()) for l, v in pool.items()}


def draw() -> dict:
    rng, tasks = random.Random(SEED), lab_tasks()
    slice_ = [t for t in tasks if t.split("/")[0] in ("corporate-ma", "contracts")]
    rest = [t for t in tasks if t not in slice_]
    rows = [{"task": t, "set": "lab_slice", "criteria": tasks[t]} for t in rng.sample(slice_, 20)]
    rows += [{"task": t, "set": "lab_other", "criteria": tasks[t]} for t in rng.sample(rest, 10)]
    pool = ours()
    picked = {l: rng.sample(v, min(5, len(v))) for l, v in pool.items()}
    spare = [(l, m) for l, v in pool.items() for m in v if m not in picked[l]]
    short = 20 - sum(map(len, picked.values()))
    chosen = [(l, m) for l, v in picked.items() for m in v] + (rng.sample(spare, short) if short > 0 else [])
    for l, m in chosen:
        name = to_lab_format.convert(m, ROOT / "tasks")
        n = len(json.loads((ROOT / "tasks" / name / "task.json").read_text())["criteria"])
        rows.append({"task": name, "set": "ours", "label": l, "matter": str(m), "criteria": n})
    return {"seed": SEED, "pool_sizes": {str(l): len(v) for l, v in pool.items()}, "rows": rows,
            "judge_calls_projected": sum(r["criteria"] for r in rows)}


def run_one(row: dict) -> None:
    d = ROOT / "results" / row["task"] / f"qwen3-small-low/{TAG}"
    if (d / "scores.json").exists():
        return
    env = {**os.environ, "PATH": "/opt/homebrew/bin:" + os.environ["PATH"]}
    with open(OUT / "logs" / (row["task"].replace("/", "_") + ".log"), "w") as f:
        subprocess.run([str(MAIN / "runs/lab_venv/bin/python"), str(REPO / "scripts/lab_run.py"), row["task"], "--tag", TAG],
                       stdout=f, stderr=subprocess.STDOUT, env=env)


def summarise(rows: list[dict]) -> dict:
    out = []
    for r in rows:
        d = ROOT / "results" / r["task"] / f"qwen3-small-low/{TAG}"
        if not (d / "scores.json").exists():
            out.append({**r, "error": "no scores.json"})
            continue
        s, m, j = (json.loads((d / f).read_text()) for f in ("scores.json", "metrics.json", "judge_calls.json"))
        out.append({**r, "n_criteria": s["n_criteria"], "n_passed": s["n_passed"], "all_pass": s["all_pass"],
                    "grading_errors": s["n_grading_errors"], "turns": m["turn_count"], "input_tokens": m["input_tokens"],
                    "output_tokens": m["output_tokens"], "seconds": m["wall_clock_seconds"], "finish": m["finish_reason"],
                    "judge_calls": j["calls"], "wrote_output": any((d / "output").iterdir())})
    sets = {}
    for name in ("lab_slice", "lab_other", "ours"):
        g = [o for o in out if o["set"] == name and "n_criteria" in o]
        if g:
            sets[name] = {"tasks": len(g), "all_pass": sum(o["all_pass"] for o in g) / len(g),
                          "criterion_pass_pooled": sum(o["n_passed"] for o in g) / sum(o["n_criteria"] for o in g),
                          "criterion_pass_macro": sum(o["n_passed"] / o["n_criteria"] for o in g) / len(g),
                          "no_output": sum(not o["wrote_output"] for o in g), "judge_calls": sum(o["judge_calls"] for o in g),
                          "input_tokens": sum(o["input_tokens"] for o in g), "output_tokens": sum(o["output_tokens"] for o in g),
                          "agent_minutes": round(sum(o["seconds"] for o in g) / 60), "grading_errors": sum(o["grading_errors"] for o in g)}
    return {"sets": sets, "tasks": out}


if __name__ == "__main__":
    (OUT / "logs").mkdir(parents=True, exist_ok=True)
    if sys.argv[1] == "draw":
        s = draw()
        (OUT / "sample.json").write_text(json.dumps(s, indent=1))
        print(json.dumps({k: v for k, v in s.items() if k != "rows"}))
        for r in s["rows"]:
            print(f"{r['set']:9} {r['task']} {r.get('label', '')} {r['criteria']}")
    else:
        rows = json.loads((OUT / "sample.json").read_text())["rows"]
        with ThreadPoolExecutor(WORKERS) as pool:
            list(pool.map(run_one, rows))
        (OUT / "summary.json").write_text(json.dumps(summarise(rows), indent=1))
