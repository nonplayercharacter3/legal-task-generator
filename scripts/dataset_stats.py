"""Dataset statistics: our accepted tasks beside a local copy of LAB, the same measure on both sides, plus the
solver's per-criterion pass rate from the label grades stored in each task's gates.json. No model calls.

    python3 scripts/dataset_stats.py --runs runs/pilot30_gen runs/pilot31_gen --lab ../harvey-labs --out out/

Writes dataset_stats.md and dataset_stats.json. Only counts are written, never LAB text.

LAB layout (harveyai/harvey-labs, `tasks/`): a task is any folder holding a `task.json`, at depth 2 to 4 under
`tasks/` (`<area>/<task>`, `<area>/<task>/scenario-NN`, `contracts/<sub-area>/<task>/scenario-NN`). The first folder
name is the practice area. `task.json` holds `instructions` (the instruction), `criteria` (the rubric; each has an
`id`, `title`, `match_criteria`) and, for most, `work_type` and `deliverables` ({file name: file name}). The matter
documents are the files under the task's `documents/` folder (.docx, .xlsx, .eml, .pptx, .txt, .json). Three groups:
`practice-area` (work_type and deliverables present), `contracts` (neither: the reply is the deliverable) and
`firm-knowledge` (a `docs_dir` pointing at one shared DMS folder, no per-task documents; left out of the folder
rows). A Git LFS pointer file counts as a file but adds no words.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import zipfile
from collections import Counter
from pathlib import Path

LFS = b"version https://git-lfs"
TAG = re.compile(r"<[^>]+>")


def pct(xs: list[float], p: float) -> float:
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, round(p / 100 * (len(xs) - 1))))] if xs else 0


def spread(xs: list[float]) -> dict:
    return {"min": min(xs, default=0), "p10": pct(xs, 10), "median": statistics.median(xs) if xs else 0,
            "p90": pct(xs, 90), "max": max(xs, default=0)}


def words(path: Path) -> int:
    """Word count of one document; 0 for an LFS pointer or a file that cannot be read."""
    try:
        raw = path.read_bytes()
        if raw.startswith(LFS):
            return 0
        ext = path.suffix.lower()
        if ext in (".docx", ".xlsx", ".pptx"):
            with zipfile.ZipFile(path) as z:
                parts = [n for n in z.namelist() if n.endswith(".xml") and (
                    n.startswith(("word/document", "xl/sharedStrings", "ppt/slides/slide"))
                    or n.startswith("xl/worksheets/"))]
                text = " ".join(TAG.sub(" ", z.read(n).decode("utf8", "ignore")) for n in parts)
        else:
            text = raw.decode("utf8", "ignore")
        return len(text.split())
    except (OSError, zipfile.BadZipFile):
        return 0


def names_every_file(instruction: str, files: list[str]) -> bool:
    low = instruction.lower()
    return bool(files) and all(f.lower() in low or Path(f).stem.lower() in low for f in files)


def load_ours(runs: list[Path], model: str) -> list[dict]:
    out = []
    for run in runs:
        for task in sorted(run.glob("accepted/*/task.json")):
            m = task.parent
            t = json.loads(task.read_text())
            files = sorted(p for p in (m / "docs").rglob("*") if p.is_file()) if (m / "docs").is_dir() else []
            ledger = json.loads((m / "ledger.json").read_text()) if (m / "ledger.json").exists() else {}
            gates = json.loads((m / "gates.json").read_text()) if (m / "gates.json").exists() else {}
            rubric = t["rubric"]
            out.append({
                "id": f"{run.name}/{m.name}", "area": t.get("practice_area", "?"),
                "work_type": t.get("work_type", "?"), "n_docs": len(files),
                "words": sum(words(p) for p in files), "formats": [p.suffix.lower() for p in files],
                "kinds": {c["id"]: c.get("kind", "?") for c in rubric}, "n_criteria": len(rubric),
                "instruction": t["instruction"], "names_all": names_every_file(t["instruction"], [p.name for p in files]),
                "deliverable": "reply (memo in the response)", "issues": [i.get("type", "?") for i in ledger.get("issues", [])],
                "held": bool(t.get("hold")), "unsolved": bool(t.get("unsolved")), "attempts": attempts(gates, model),
            })
    return out


def attempts(gates: dict, model: str) -> list[list[str]]:
    """Failed criterion ids of each stored attempt of `model` (empty list: no label grades stored)."""
    for g in gates.get("gates", []):
        if g["name"] == "solver_check":
            runs = g.get("details", {}).get("runs", {})  # older runs stored a plain list, with no model name
            return [r.get("failed_criteria", []) for r in runs.get(model, [])] if isinstance(runs, dict) else []
    return []


def load_lab(lab: Path) -> list[dict]:
    root = lab / "tasks"
    out = []
    for f in sorted(root.rglob("task.json")):
        t = json.loads(f.read_text())
        d = f.parent
        if "docs_dir" in t:
            group = "firm-knowledge"
        elif "work_type" in t:
            group = "practice-area"
        else:
            group = "contracts"
        files = sorted(p for p in (d / "documents").rglob("*") if p.is_file()) if (d / "documents").is_dir() else []
        dels = t.get("deliverables") or {}
        exts = sorted({Path(k).suffix.lower() for k in dels}) if isinstance(dels, dict) else []
        crit = t.get("criteria", [])
        out.append({
            "id": str(d.relative_to(root)), "area": d.relative_to(root).parts[0], "group": group,
            "work_type": t.get("work_type", "not stated"), "n_docs": len(files),
            "words": sum(words(p) for p in files), "formats": [p.suffix.lower() for p in files],
            "n_criteria": len(crit), "instruction": t.get("instructions", ""),
            "names_all": names_every_file(t.get("instructions", ""), [p.name for p in files]),
            "deliverable": "file" if exts else "not stated (reply)", "deliverable_exts": exts, "issues": [],
        })
    return out


def summarise(tasks: list[dict], folders: bool = True) -> dict:
    """One column of the table."""
    n = len(tasks)
    folder = [t for t in tasks if t.get("group") != "firm-knowledge"] if folders else tasks
    iw = [len(t["instruction"].split()) for t in tasks]
    fmt = Counter(e for t in folder for e in t["formats"])
    issues = Counter(i for t in tasks for i in t["issues"])
    s = {
        "tasks": n,
        "documents_per_task": spread([t["n_docs"] for t in folder]),
        "words_per_folder": spread([t["words"] for t in folder]),
        "file_formats": dict(fmt.most_common()),
        "criteria_per_task": spread([t["n_criteria"] for t in tasks]),
        "instruction_words": {"mean": round(statistics.mean(iw), 1) if iw else 0,
                              "median": statistics.median(iw) if iw else 0},
        "instructions_naming_every_file": round(sum(t["names_all"] for t in folder) / len(folder), 3) if folder else 0,
        "deliverable": dict(Counter(t["deliverable"] for t in tasks).most_common()),
        "deliverable_formats": dict(Counter(e for t in tasks for e in t.get("deliverable_exts", [])).most_common()),
        "work_types": dict(Counter(t["work_type"] for t in tasks).most_common()),
        "practice_areas": dict(Counter(t["area"] for t in tasks).most_common()),
    }
    if issues:
        k = [len(t["issues"]) for t in tasks]
        s["issues_per_task"] = {"min": min(k), "median": statistics.median(k), "max": max(k), "total": sum(k)}
        s["issue_types"] = {"distinct": len(issues), "top10": dict(issues.most_common(10))}
    return s


def per_check(ours: list[dict]) -> dict:
    """Share of single criteria passed over all stored attempts, beside the all-pass rate."""
    graded = [t for t in ours if t["attempts"]]

    def rate(ts, kind=None):
        tot = ok = 0
        for t in ts:
            for fails in t["attempts"]:
                for cid, k in t["kinds"].items():
                    if kind and k != kind:
                        continue
                    tot += 1
                    ok += cid not in fails
        return {"criteria_graded": tot, "pass_rate": round(ok / tot, 4) if tot else None}

    runs = [(t, fails) for t in graded for fails in t["attempts"]]
    allp = sum(not [c for c in fails if c in t["kinds"]] for t, fails in runs)
    bins = [("8 to 9", 0, 9), ("10", 10, 10), ("11 to 12", 11, 12), ("13 or more", 13, 999)]
    return {
        "tasks_graded": len(graded), "attempts": len(runs),
        "all_pass_rate": round(allp / len(runs), 4) if runs else None,
        "criteria": rate(graded),
        "by_kind": {k: rate(graded, k) for k in ("issue", "fact", "negative", "format")},
        "by_rubric_size": {name: {"tasks": sum(lo <= t["n_criteria"] <= hi for t in graded),
                                  **rate([t for t in graded if lo <= t["n_criteria"] <= hi])}
                           for name, lo, hi in bins},
    }


def _cell(v) -> str:
    if isinstance(v, dict) and "median" in v and "p10" in v:
        return f"{v['min']} / {v['p10']} / {v['median']} / {v['p90']} / {v['max']}"
    if isinstance(v, dict):
        return ", ".join(f"{k} {n}" for k, n in list(v.items())[:10]) or "none"
    return str(v)


ROWS = [("tasks", "Tasks"), ("documents_per_task", "Documents per task (min / p10 / median / p90 / max)"),
        ("words_per_folder", "Words per folder (same spread)"), ("file_formats", "Files by format"),
        ("criteria_per_task", "Rubric criteria per task (same spread)"),
        ("instruction_words", "Instruction words"),
        ("instructions_naming_every_file", "Share of instructions naming every file"),
        ("deliverable", "Deliverable"), ("deliverable_formats", "Deliverable file formats"),
        ("work_types", "Work types"), ("practice_areas", "Practice areas")]


def markdown(stats: dict, pc: dict) -> str:
    cols = list(stats)
    out = ["# Dataset statistics", "", "| Measure | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols)]
    for key, label in ROWS:
        out.append(f"| {label} | " + " | ".join(_cell(stats[c].get(key, "")) for c in cols) + " |")
    for key, label in (("issues_per_task", "Issues per task"), ("issue_types", "Issue types")):
        out.append(f"| {label} | " + " | ".join(_cell(stats[c].get(key, "n/a")) if key in stats[c] else "n/a"
                                                for c in cols) + " |")
    out += ["", "## Solver per-check pass rate (ours, stored label grades)", "",
            f"Tasks graded: {pc['tasks_graded']}, attempts: {pc['attempts']}. "
            f"All-pass rate {pc['all_pass_rate']}, single criteria passed {pc['criteria']['pass_rate']} "
            f"({pc['criteria']['criteria_graded']} grades).", "", "| Group | Criteria graded | Pass rate |",
            "|---|---|---|"]
    out += [f"| kind: {k} | {v['criteria_graded']} | {v['pass_rate']} |" for k, v in pc["by_kind"].items()]
    out += [f"| rubric size: {k} ({v['tasks']} tasks) | {v['criteria_graded']} | {v['pass_rate']} |"
            for k, v in pc["by_rubric_size"].items()]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", nargs="*", help="run folders (default: every folder under runs/ except fake ones)")
    ap.add_argument("--lab", help="local copy of harveyai/harvey-labs (omit for our side only)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="qwen3-small", help="solver role whose stored grades are used")
    a = ap.parse_args(argv)
    runs = [Path(r) for r in a.runs] if a.runs else sorted(p for p in Path("runs").glob("*/")
                                                           if (p / "accepted").is_dir() and "fake" not in p.name)
    ours = load_ours(runs, a.model)
    stats = {"ours": summarise(ours),
             "ours, held": summarise([t for t in ours if t["held"]]),
             "ours, unsolved": summarise([t for t in ours if t["unsolved"]])}
    stats = {k: v for k, v in stats.items() if v["tasks"]}
    if a.lab:
        lab = load_lab(Path(a.lab))
        stats["LAB, all"] = summarise(lab)
        for g in ("practice-area", "contracts", "firm-knowledge"):
            stats[f"LAB {g}"] = summarise([t for t in lab if t["group"] == g])
    pc = per_check(ours)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "dataset_stats.json").write_text(json.dumps({"stats": stats, "per_check": pc}, indent=2) + "\n")
    (out / "dataset_stats.md").write_text(markdown(stats, pc))
    print(markdown(stats, pc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
