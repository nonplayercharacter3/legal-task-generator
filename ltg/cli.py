"""Command line: `python -m ltg run ...`, `label ...`, `index ...`, `inspect ...` and `export ...`."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from .config import load_config
from .orchestrator import Pipeline, label_runs, reference_index


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


def seed_used_by(out_dir: str, seed: int) -> str | None:
    """Another run folder beside `out_dir` that ran this seed, or None. Matter ids come from the seed, so a reused
    seed drafts the same matter specs again (seeds 8 and 9 were run by both solver streams, see CLAUDE.md)."""
    for s in sorted(Path(out_dir).parent.glob("*/settings.json")):
        if s.parent.resolve() == Path(out_dir).resolve():
            continue  # the same folder: a --resume, or a rerun into it
        try:
            if json.loads(s.read_text()).get("run", {}).get("seed") == seed:
                return str(s.parent)
        except (OSError, ValueError):
            continue
    return None


def cmd_run(args: argparse.Namespace) -> int:
    overrides: dict = {}
    if args.matters is not None:
        overrides.setdefault("run", {})["n_matters"] = args.matters
    if args.seed is not None:
        overrides.setdefault("run", {})["seed"] = args.seed
    if args.out is not None:
        overrides.setdefault("run", {})["out_dir"] = args.out
    cfg = load_config(args.config, overrides)
    if args.seed is not None and not args.allow_seed_reuse and (other := seed_used_by(cfg.run.out_dir, cfg.run.seed)):
        print(f"seed {cfg.run.seed} was already used by {other}: its matter ids and specs would repeat. "
              f"Pick a seed no run folder beside {cfg.run.out_dir} has used, or pass --allow-seed-reuse.", file=sys.stderr)
        return 2
    report = Pipeline(cfg).run(resume=args.resume)
    print(f"accepted {report['accepted']} of {report['candidates']} candidates -> {cfg.run.out_dir}"
          + (f" ({report['resumed']} reloaded from an earlier run)" if report["resumed"] else ""))
    for g, s in report["gates"].items():
        print(f"  {g:<16} evaluated {s['evaluated']:>3}  passed {s['passed']:>3}  failed {s['failed']:>3}  skipped {s['skipped']:>3}")
    if report.get("label_pending"):
        print(f"{report['label_pending']} accepted task(s) wait for labels: run `ltg label` with a solver config on {cfg.run.out_dir}")
    if report["gates"]["decontamination"]["skipped"]:
        print("WARNING: decontamination skipped (no reference_dirs); tasks were not screened against LAB")
    print(f"report: {Path(cfg.run.out_dir) / 'report.md'}")
    return 0


def cmd_label(args: argparse.Namespace) -> int:
    res = label_runs(load_config(args.config), args.runs, args.config)
    print(f"labelled {res['labelled']}, rejected {res['leak']} as leaks, {res['error']} errors"
          + (" (still pending: rerun `ltg label` to retry)" if res["error"] else ""))
    return 1 if res["error"] else 0


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


def cmd_export(args: argparse.Namespace) -> int:
    from .export import export, parse_ratios

    try:
        ratios = parse_ratios(args.ratios) if args.ratios else None
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    if args.model is None and (args.min_pass != 0.0 or args.max_pass != 1.0):
        print("--min-pass and --max-pass select a band of one model's labels: add --model", file=sys.stderr)
        return 2
    res = export(args.runs, args.out, args.model, args.min_pass, args.max_pass, args.include_unsolved, args.include_held,
                 args.include_pending, ratios)
    for tid, paths in res["duplicates"].items():
        print(f"duplicate task id {tid}, kept neither: {', '.join(paths)}", file=sys.stderr)
    sk = res["skipped"]
    print("exported " + ", ".join(f"{s} {n}" for s, n in res["counts"].items()) + f" -> {args.out}"
          + f" (left out: {sk['held']} held, {sk['pending']} waiting for labels, {sk['unsolved']} unsolved, {sk['outside_band']} outside the band)"
          + (f"; splits re-assigned by --ratios, {res['moved']} moved" if ratios else ""))
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
    r.add_argument("--allow-seed-reuse", action="store_true", help="run a --seed another run folder beside --out has already used")
    r.set_defaults(func=cmd_run)

    x = sub.add_parser("index", help="build or load the decontamination reference index (e.g. LAB) and report it")
    x.add_argument("--config", required=True, help="TOML config with gates.reference_dirs")
    x.set_defaults(func=cmd_index)

    lb = sub.add_parser("label", help="run the deferred solver_check on accepted tasks with label_pending")
    lb.add_argument("--config", required=True, help="TOML config with the solver roles, e.g. configs/pilot_nrp_solver.toml")
    lb.add_argument("runs", nargs="+", help="run folders holding accepted/<matter>/")
    lb.set_defaults(func=cmd_label)

    i = sub.add_parser("inspect", help="print one matter folder in readable form")
    i.add_argument("matter_dir")
    i.set_defaults(func=cmd_inspect)

    e = sub.add_parser("export", help="write accepted tasks as JSONL training data, one file per split")
    e.add_argument("--runs", nargs="+", required=True, help="run folders holding accepted/<matter>/")
    e.add_argument("--out", required=True, help="output folder for train.jsonl, dev.jsonl, test.jsonl")
    e.add_argument("--model", help="keep only tasks this model labelled, within the band below (e.g. qwen3-small)")
    e.add_argument("--min-pass", type=float, default=0.0, help="lowest pass rate kept (with --model)")
    e.add_argument("--max-pass", type=float, default=1.0, help="highest pass rate kept (with --model)")
    e.add_argument("--include-unsolved", action="store_true", help="also export tasks no solver attempt passed")
    e.add_argument("--include-held", action="store_true", help="also export tasks a person put on hold (task.json `hold`)")
    e.add_argument("--include-pending", action="store_true", help="also export tasks waiting for `ltg label` (no label, no leak probe yet)")
    e.add_argument("--ratios", metavar="TRAIN,DEV,TEST", help="re-assign every task's split from its matter id, e.g. 0.7,0.15,0.15 (default: the split stored at acceptance)")
    e.set_defaults(func=cmd_export)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
