"""`ltg batch`: a whole batch in one command. For each seed: generate (`ltg run`, resumed until no matter ends in an
error), label (`ltg label`, retried until no task errors), commit the seed's results by the run-output rule; then
export every run folder of the batch and print the labels' spread.

    python -m ltg batch --config configs/pilot_generate_v2.toml --seeds 46-53 --out-pattern 'runs/pilot{seed}_v2'

Waits: a Claude usage limit ("You've hit your session limit · resets 8:40pm") sleeps until that time, else
`--retry-wait` minutes; any other error sleeps `--retry-wait` minutes. An NRP refusal (an HTTP 403 with a body) stops
the batch. One batch at a time per checkout (a lock folder); `touch` the stop file to stop between steps.
Commits go straight to `main` (pull --ff-only first), or with `--branch` to that branch, pushed, with one PR opened.
Every commit runs under `runs/.git-commit.lock`, so two writers never commit at once.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

from . import orchestrator
from .config import load_config

GIT_LOCK = Path("runs/.git-commit.lock")
LIMIT = re.compile(r"hit your .{0,40}limit|usage limit", re.I)
RESETS = re.compile(r"resets\s+(?:[A-Za-z]{3,9}\s+\d{1,2},?\s+)?(\d{1,2})(?::(\d\d))?\s*([ap]m)", re.I)
REFUSED = re.compile(r"HTTP 403: b'[^']")  # a bare 403 (empty body) is NRP's flaky gateway, which the client retries
HEARTBEAT = 600  # a long wait logs a line this often, so a watchdog on the log's age does not take it for a hang


def log(msg: str) -> None:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} batch: {msg}", flush=True)


def parse_seeds(text: str) -> list[int]:
    """'46-53' or '46,48,50-52' -> the seeds in order, no repeats."""
    seeds: list[int] = []
    for part in filter(None, (p.strip() for p in text.split(","))):
        a, _, b = part.partition("-")
        for s in range(int(a), int(b or a) + 1):
            if s not in seeds:
                seeds.append(s)
    return seeds


def limit_wait(text: str, default: float, now: datetime | None = None) -> float | None:
    """Seconds to wait if `text` reports a Claude usage limit (until its reset time plus 2 minutes, else `default`);
    None if it does not."""
    if not LIMIT.search(text):
        return None
    m = RESETS.search(text)
    if not m:
        return default
    now = now or datetime.now()
    hour = int(m[1]) % 12 + (12 if m[3].lower() == "pm" else 0)
    at = now.replace(hour=hour, minute=int(m[2] or 0), second=0, microsecond=0)
    if at <= now:
        at += timedelta(days=1)
    return (at - now).total_seconds() + 120


def error_text(out: Path) -> str:
    """The reasons of matters that ended in an error, and the last line of each pending task's label error."""
    parts = []
    if (out / "report.json").exists():
        parts += [str(m.get("reason") or "") for m in json.loads((out / "report.json").read_text())["matters"]
                  if m.get("failed_gate") == "error"]
    parts += [e.read_text()[-2000:] for e in sorted((out / "accepted").glob("*/label_error.txt"))]
    return "\n".join(parts)


def pending(out: Path) -> int:
    return sum(1 for t in (out / "accepted").glob("*/task.json") if json.loads(t.read_text()).get("label_pending"))


# ------------------------------------------------------------------ git


def sh(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(list(args), capture_output=True, text=True)


def run_files(out: Path) -> list[Path]:
    """The run-output rule: report.md, report.json, settings.json, accepted/ without solver traces, and spec.json,
    ledger.json and gates.json of each rejected matter. Never calls.jsonl, traces or logs."""
    keep = [out / f for f in ("report.md", "report.json", "settings.json") if (out / f).exists()]
    keep += sorted(p for p in (out / "accepted").rglob("*")
                   if p.is_file() and not p.name.endswith(".trace.json") and p.name != "label_error.txt")
    for m in sorted((out / "rejected").glob("*")) if (out / "rejected").is_dir() else []:
        keep += [m / f for f in ("spec.json", "ledger.json", "gates.json") if (m / f).exists()]
    return keep


def describe(out: Path, m: dict) -> str:
    folder = out / ("accepted" if m["accepted"] else "rejected") / m["matter_id"]
    try:
        spec = json.loads((folder / "spec.json").read_text())
        what = f"{spec.get('agreement_type', '?')}, {spec.get('industry', '?')}"
    except (OSError, ValueError):
        what = "spec missing"
    if not m["accepted"]:
        return f"- {m['matter_id']} ({what}): rejected at {m['failed_gate']}: {str(m.get('reason') or '')[:400]}"
    n_docs = len(list((folder / "docs").glob("*"))) if (folder / "docs").is_dir() else 0
    try:
        n_issues = len(json.loads((folder / "ledger.json").read_text())["issues"])
    except (OSError, ValueError, KeyError):
        n_issues = "?"
    labels = ", ".join(f"{d['model']} {d['pass_rate']:.2f}" for d in m.get("difficulty") or []) or "label pending"
    return (f"- {m['matter_id']} ({what}, {m.get('split')}, {n_docs} documents, {n_issues} issues), {labels}"
            + (", unsolved" if m.get("unsolved") else ""))


def message(out: Path, seed: int, config: str, first: bool) -> str:
    """Commit message: the round's numbers and every rejection's cause (the first commit of a run folder), or
    "Labels for seed N" (a later commit, after labelling)."""
    r = json.loads((out / "report.json").read_text())
    calls = r.get("model_calls", {})
    tot = lambda k: sum(v.get(k, 0) for v in calls.values())
    acc = [m for m in r["matters"] if m["accepted"]]
    rej = [m for m in r["matters"] if not m["accepted"]]
    left = r.get("label_pending", 0)
    head = (f"Round {seed}: {len(acc)} of {r['candidates']} accepted (seed {seed}, {config})" if first
            else f"Labels for seed {seed} ({config})")
    lines = [head, ""]
    if acc:
        lines += ["Accepted:"] + [describe(out, m) for m in acc] + [""]
    if rej:
        lines += ["Rejected (causes as the gates recorded them; not yet read by a person):"]
        lines += [describe(out, m) for m in rej] + [""]
    lines += [f"{tot('calls')} calls, ~{tot('input_tokens') / 1e6:.2f}M input and ~{tot('output_tokens') / 1e3:.0f}k output "
              f"tokens, {r.get('errors', 0)} matters in error, {left} task(s) waiting for labels.", "",
              "Committed by `ltg batch`."]
    return "\n".join(lines)


class Git:
    """Commits a run folder's results, straight to main or to `branch` (pushed, one PR opened)."""

    def __init__(self, author: str | None, branch: str | None) -> None:
        self.cfg: list[str] = []
        if author:
            m = re.fullmatch(r"\s*(.+?)\s*<([^>]+)>\s*", author)
            if not m:
                raise ValueError(f"--author must look like 'Name <email>', not {author!r}")
            self.cfg = ["-c", f"user.name={m[1]}", "-c", f"user.email={m[2]}"]
        self.branch = branch

    def start(self) -> str | None:
        """Check out the branch to commit to. An error message if the checkout is not fit to commit from."""
        head = sh("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        if sh("git", "diff", "--cached", "--quiet").returncode != 0:
            return "the git index already holds staged changes"
        if not self.branch:
            return None if head == "main" else f"commits go to main, but the checkout is on {head!r} (use --branch)"
        if head != self.branch:
            r = sh("git", "checkout", self.branch) if sh("git", "rev-parse", "--verify", "-q", self.branch).returncode == 0 \
                else sh("git", "checkout", "-b", self.branch)
            if r.returncode != 0:
                return f"cannot check out {self.branch}: {r.stderr.strip()}"
        return None

    def commit(self, out: Path, msg: str) -> bool:
        if not take_lock(GIT_LOCK):
            log(f"{GIT_LOCK} still held after 30 minutes; {out} not committed")
            return False
        try:
            if not self.branch and (p := sh("git", "pull", "-q", "--ff-only")).returncode != 0:
                log(f"git pull --ff-only failed, {out} not committed: {p.stderr.strip()}")
                return False
            add = sh("git", "add", "-f", "--", *map(str, run_files(out)))
            if add.returncode == 0:  # then deletions: a leak moves its task out of accepted/
                add = sh("git", "add", "-u", "--", str(out))
            if add.returncode != 0:
                log(f"git add failed, {out} not committed: {add.stderr.strip()}")
                sh("git", "reset", "-q")
                return False
            if sh("git", "diff", "--cached", "--quiet").returncode == 0:
                log(f"{out}: nothing new to commit")
                return False
            if (c := sh("git", *self.cfg, "commit", "-q", "-m", msg)).returncode != 0:
                log(f"git commit failed: {c.stderr.strip()}")
                sh("git", "reset", "-q")
                return False
            push = sh("git", "push", "-q", "-u", "origin", self.branch) if self.branch else sh("git", "push", "-q")
            log(f"committed {sh('git', 'rev-parse', '--short', 'HEAD').stdout.strip()} "
                + ("and pushed" if push.returncode == 0 else "but the push failed: " + push.stderr.strip()))
            if self.branch and push.returncode == 0:  # every push: an earlier PR may have been merged since
                open_pr(self.branch, msg.splitlines()[0])
            return True
        finally:
            GIT_LOCK.rmdir()


def open_pr(branch: str, first_title: str) -> bool:
    """Open a PR from `branch` into main unless one is open. True once one exists."""
    if not shutil.which("gh"):
        log("gh not found: open the pull request by hand")
        return False
    if sh("gh", "pr", "view", branch, "--json", "state", "-q", ".state").stdout.strip() == "OPEN":
        return True
    r = sh("gh", "pr", "create", "--base", "main", "--head", branch, "--title", f"Batch results: {branch}",
           "--body", f"Results committed by `ltg batch`, one commit per seed and labelling pass. First: {first_title}.")
    log("opened " + r.stdout.strip() if r.returncode == 0 else "gh pr create failed: " + r.stderr.strip())
    return r.returncode == 0


def take_lock(path: Path, wait: float = 1800) -> bool:
    end = time.time() + wait
    while True:
        try:
            path.mkdir()
            return True
        except FileExistsError:
            if time.time() > end:
                return False
            time.sleep(5)


# ------------------------------------------------------------------ the batch


def run_batch(args, sleep=time.sleep) -> int:
    """0: every seed done; 1: a seed gave up after --max-tries or stopped; 2: NRP refused; 4: another batch runs."""
    seeds, stop, lock = parse_seeds(args.seeds), Path(args.stop_file), Path(args.lock)
    lock.parent.mkdir(parents=True, exist_ok=True)
    try:
        lock.mkdir()
    except FileExistsError:
        log(f"another batch holds {lock}; exiting")
        return 4
    # A `kill` (SIGTERM) would otherwise end Python without running `finally`, leaving a stale lock.
    old = signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))
    try:
        return _batch(args, seeds, stop, sleep)
    finally:
        lock.rmdir()
        signal.signal(signal.SIGTERM, old)


def _batch(args, seeds: list[int], stop: Path, sleep) -> int:
    git = Git(args.author, args.branch) if args.commit else None
    if git and (problem := git.start()):
        log(f"cannot commit: {problem}; exiting")
        return 3
    label_config = None if args.no_label else (args.label_config or args.config)
    name = Path(args.config).stem if args.config else "fake backend"
    log(f"start: seeds {seeds}, config {args.config}, labels {label_config or 'deferred'}, "
        f"commits {'to ' + (args.branch or 'main') if git else 'off'}")
    outs, code = [], 0
    for seed in seeds:
        out = Path(args.out_pattern.format(seed=seed))
        outs.append(out)
        if stop.exists():
            log(f"stop file {stop} found before seed {seed}")
            code = 1
            break
        status = _generate(args, seed, out, stop, sleep)
        if status == "refused":
            return 2
        if status != "done":
            code = 1
            if status == "stopped":
                break
            continue
        committed = git is not None and _committed(out)
        if git and not committed:
            git.commit(out, message(out, seed, f"{name}, " + ("labels next" if label_config else "labels deferred"), True))
        if label_config and pending(out):
            status = _label(args, label_config, out, stop, sleep)
            if git:
                git.commit(out, message(out, seed, Path(label_config).stem, False))
            if status == "refused":
                return 2
            if status != "done":
                code = 1
                if status == "stopped":
                    break
    _summary(outs, args.export_out)
    log(f"end (exit {code})")
    return code


def _committed(out: Path) -> bool:
    return sh("git", "cat-file", "-e", f"HEAD:{out / 'report.json'}").returncode == 0


def _generate(args, seed: int, out: Path, stop: Path, sleep) -> str:
    """'done' (no matter in error), 'refused', 'stopped', 'skipped' (seed used elsewhere) or 'gave up'."""
    from .cli import seed_used_by

    rep = out / "report.json"
    if rep.exists() and json.loads(rep.read_text()).get("errors") == 0:
        log(f"seed {seed}: {out} already finished")
        return "done"
    if not (out / "settings.json").exists() and (other := seed_used_by(str(out), seed)):
        log(f"seed {seed} was already used by {other}; skipped")
        return "skipped"
    for t in range(1, args.max_tries + 1):
        resume = (out / "settings.json").exists()
        log(f"seed {seed} try {t}" + (" (resume)" if resume else ""))
        cfg = load_config(args.config, {"run": {"seed": seed, "out_dir": str(out)}})
        try:
            report = orchestrator.Pipeline(cfg).run(resume=resume)
            text = "" if report["errors"] == 0 else error_text(out)
            log(f"seed {seed}: accepted {report['accepted']} of {report['candidates']}, {report['errors']} in error")
        except Exception as e:  # noqa: BLE001  a crashed try is retried like an errored one
            text = f"{type(e).__name__}: {e}"
            log(f"seed {seed}: try crashed: {text[:300]}")
        if not text:
            return "done"
        status = _wait(args, text, stop, sleep, f"seed {seed}")
        if status:
            return status
    log(f"seed {seed}: still errors after {args.max_tries} tries; going on")
    return "gave up"


def _label(args, label_config: str, out: Path, stop: Path, sleep) -> str:
    lcfg = load_config(label_config)
    for t in range(1, args.max_tries + 1):
        log(f"{out}: labelling {pending(out)} task(s), try {t}")
        try:
            res = orchestrator.label_runs(lcfg, [str(out)], label_config)
            log(f"{out}: labelled {res['labelled']}, {res['leak']} leaks, {res['error']} errors")
            text = error_text(out) if res["error"] else ""
        except Exception as e:  # noqa: BLE001
            text = f"{type(e).__name__}: {e}"
            log(f"{out}: labelling crashed: {text[:300]}")
        if not text:
            return "done"
        status = _wait(args, text, stop, sleep, str(out))
        if status:
            return status
    log(f"{out}: label errors after {args.max_tries} tries; tasks stay pending")
    return "gave up"


def _wait(args, text: str, stop: Path, sleep, what: str) -> str | None:
    if REFUSED.search(text):
        log(f"{what}: NRP refused (HTTP 403); stopping the batch: {REFUSED.search(text).group(0)}")
        return "refused"
    if stop.exists():
        log(f"{what}: stop file {stop} found")
        return "stopped"
    wait = limit_wait(text, args.retry_wait * 60)
    log(f"{what}: " + ("usage limit" if wait is not None else "errors") + f", waiting {(wait or args.retry_wait * 60) / 60:.0f} min")
    left = wait if wait is not None else args.retry_wait * 60
    while left > 0:
        sleep(min(left, HEARTBEAT))
        left -= HEARTBEAT
        if stop.exists():
            log(f"{what}: stop file {stop} found")
            return "stopped"
        if left > 0:
            log(f"{what}: still waiting, {left / 60:.0f} min left")
    return None


def _summary(outs: list[Path], export_out: str | None) -> None:
    acc = labels = 0
    rates: dict[float, int] = {}
    for out in outs:
        for t in (out / "accepted").glob("*/task.json"):
            acc += 1
            for d in json.loads(t.read_text()).get("difficulty") or []:
                labels += 1
                rates[round(d["pass_rate"], 2)] = rates.get(round(d["pass_rate"], 2), 0) + 1
    log(f"batch: {acc} accepted task(s) in {len(outs)} run folder(s); pass rates "
        + (", ".join(f"{r:.2f}: {n}" for r, n in sorted(rates.items())) or "none yet"))
    if export_out:
        from .export import export

        res = export([str(o) for o in outs if o.exists()], export_out, include_unsolved=True)
        log("exported " + ", ".join(f"{s} {n}" for s, n in res["counts"].items()) + f" -> {export_out}")


def add_parser(sub) -> None:
    b = sub.add_parser("batch", help="generate, label, commit and export a batch of seeds in one command")
    b.add_argument("--config", help="generation config (default: fake backend)")
    b.add_argument("--seeds", required=True, help="e.g. 46-53 or 46,48,50-52")
    b.add_argument("--out-pattern", default="runs/pilot{seed}_v2", help="run folder per seed (default %(default)s)")
    b.add_argument("--label-config", help="solver config for `ltg label` (default: --config)")
    b.add_argument("--no-label", action="store_true", help="leave labels for later (`ltg label`)")
    b.add_argument("--commit", action=argparse.BooleanOptionalAction, default=True,
                   help="commit each seed's results by the run-output rule (default on)")
    b.add_argument("--author", help="commit author, 'Name <email>' (default: git config)")
    b.add_argument("--branch", help="commit to this branch, push it and open a PR, instead of committing to main")
    b.add_argument("--max-tries", type=int, default=12, help="tries per seed, and per labelling (default %(default)s)")
    b.add_argument("--retry-wait", type=float, default=30, help="minutes between tries without a reset time (default %(default)s)")
    b.add_argument("--export-out", help="after the batch, export its run folders here (unsolved included)")
    b.add_argument("--lock", default="runs/.batch.lock", help="lock folder (default %(default)s)")
    b.add_argument("--stop-file", default="runs/.batch.stop", help="touch it to stop between steps (default %(default)s)")
    b.set_defaults(func=lambda a: run_batch(a))

