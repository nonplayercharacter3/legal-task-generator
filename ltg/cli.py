"""Command line: `python -m ltg run ...`, `python -m ltg index ...` and `python -m ltg inspect ...`."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from .config import load_config
from .orchestrator import Pipeline, reference_index


def cmd_index(args: argparse.Namespace) -> int:
    """Build (or load) the reference index on its own, e.g. when a cloud session starts, so runs find it ready."""
    g = load_config(args.config).gates
    if not g.reference_dirs:
        print("no gates.reference_dirs in this config: nothing to index")
        return 1
    t0 = time.time()
    idx = reference_index(g)
    print(f"reference index ready: {idx.count:,} n-grams from {g.reference_dirs}, "
          f"false positive rate {idx.false_positive_rate():.2%}, {time.time() - t0:.0f} s, saved under {g.decontam_cache_dir}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    overrides: dict = {}
    if args.matters is not None:
        overrides.setdefault("run", {})["n_matters"] = args.matters
    if args.seed is not None:
        overrides.setdefault("run", {})["seed"] = args.seed
    if args.out is not None:
        overrides.setdefault("run", {})["out_dir"] = args.out
    cfg = load_config(args.config, overrides)
    report = Pipeline(cfg).run(resume=args.resume)
    print(f"accepted {report['accepted']} of {report['candidates']} candidates -> {cfg.run.out_dir}"
          + (f" ({report['resumed']} reloaded from an earlier run)" if report["resumed"] else ""))
    for g, s in report["gates"].items():
        print(f"  {g:<16} evaluated {s['evaluated']:>3}  passed {s['passed']:>3}  failed {s['failed']:>3}  skipped {s['skipped']:>3}")
    if report["gates"]["decontamination"]["skipped"]:
        print("WARNING: decontamination skipped (no reference_dirs); tasks were not screened against LAB")
    print(f"report: {Path(cfg.run.out_dir) / 'report.md'}")
    return 0


def cmd_inspect(args: argparse.Namespace) -> int:
    d = Path(args.matter_dir)
    if not (d / "gates.json").exists():
        print(f"not a matter folder: {d}", file=sys.stderr)
        return 1
    g = json.loads((d / "gates.json").read_text())
    print(f"# {d.name}: {'ACCEPTED' if g['accepted'] else 'REJECTED at ' + str(g['failed_gate'])}")
    if g.get("reason"):
        print(f"reason: {g['reason']}")
    if (d / "instruction.md").exists():
        print("\n## Instruction\n" + (d / "instruction.md").read_text())
    if (d / "docs").exists():
        print("\n## Documents")
        for f in sorted((d / "docs").iterdir()):
            print(f"- {f.name} ({len(f.read_text().split())} words)")
    if (d / "ledger.json").exists():
        led = json.loads((d / "ledger.json").read_text())
        print("\n## Planted issues (answer key)")
        for i in led.get("issues", []):
            print(f"- {i['id']} [{i['type']}] {i['doc']} s.{i['section']}: {i['expected_finding']}")
    if (d / "rubric.json").exists():
        print("\n## Rubric")
        for c in json.loads((d / "rubric.json").read_text())["criteria"]:
            print(f"- {c['id']} ({c['kind']}{', ' + c['source'] if c.get('source') else ''}): {c['text']}")
    print("\n## Gates")
    for gate in g["gates"]:
        print(f"- {gate['name']}: {'pass' if gate['passed'] else 'FAIL'}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="ltg", description="Ledger-first generator for LAB-style legal agent tasks.")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="generate and filter candidate tasks")
    r.add_argument("--config", help="TOML config (default: fake backend, built-in settings)")
    r.add_argument("--matters", type=int, help="number of candidate matters")
    r.add_argument("--seed", type=int)
    r.add_argument("--out", help="output folder")
    r.add_argument("--resume", action="store_true", help="keep matters already finished in the output folder; retry errors")
    r.set_defaults(func=cmd_run)

    x = sub.add_parser("index", help="build or load the decontamination reference index (e.g. LAB) and report it")
    x.add_argument("--config", required=True, help="TOML config with gates.reference_dirs")
    x.set_defaults(func=cmd_index)

    i = sub.add_parser("inspect", help="print one matter folder in readable form")
    i.add_argument("matter_dir")
    i.set_defaults(func=cmd_inspect)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
