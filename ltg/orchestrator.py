"""Runs matters through all three stages and writes everything to disk.

Output layout (one folder per candidate matter):

    <out>/accepted/<matter_id>/   tasks that passed every gate (has task.json)
    <out>/rejected/<matter_id>/   everything else, kept for debugging
    <out>/report.json, report.md  pass counts per gate, model calls per role
    <out>/calls.jsonl             one line per model call, appended as each call ends
    <out>/tries/<n>/              report.json (if it got that far) and calls.jsonl of the try a --resume followed

Inside a matter folder: spec.json, precedents.json, ledger.json, docs/, instruction.md,
rubric.json, answers.json, stages_done.json, solver/, gates.json. stages_done.json names the generation stages
whose files are complete; a --resume of a matter that ended in an error reuses them and reruns the gates.
"""

from __future__ import annotations

import json
import os
import random
import shutil
import sys
import time
import traceback
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

from . import gates, stages
from .config import Config, GatesCfg, InstructionCfg, build_client
from .decontam import BloomIndex
from .models import CallLog, ModelClient
from .schema import Answers, Ledger, MatterSpec, Rubric
from .sources import load_precedents, select_precedents
from .splits import assign_split

GATE_ORDER = [
    "ledger_schema",
    "consistency",
    "issue_check",
    "leak_check",
    "rubric_trace",
    "rubric_tests",
    "decontamination",
    "solver_check",
]


@dataclass
class MatterResult:
    matter_id: str
    accepted: bool
    failed_gate: str | None = None
    reason: str | None = None
    split: str | None = None
    solver_pass_rate: float | None = None
    unsolved: bool = False  # kept, but no solver attempt passed: a person should check it is not broken
    difficulty: list[dict] = field(default_factory=list)  # per labelling model: model, attempts, passes, pass_rate
    label_pending: bool = False  # accepted with solver_check deferred: no labels and no leak probe until `ltg label`
    labelled_by: dict | None = None  # set by `ltg label`: config, models, probe result
    gates: list[dict] = field(default_factory=list)


class _Rejected(Exception):
    def __init__(self, gate: str, reason: str) -> None:
        super().__init__(reason)
        self.gate, self.reason = gate, reason


def _write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        path.write_text(data, encoding="utf-8")
    else:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def beat(matter_id: str, stage: str) -> None:
    """One line per matter per stage on stderr (the batch log), so a stalled call shows without `sample`."""
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {matter_id} {stage}", file=sys.stderr, flush=True)


def _read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _first_reason(g: gates.GateResult) -> str:
    d = g.details
    for key in ("reason", "errors", "mismatches", "missing", "hits", "html_comments", "instruction_form", "gold_fails", "blank_passes", "flawed_wrongly_passes", "flawed_wrongly_fails", "flagged"):
        if d.get(key):
            v = d[key]
            return v if isinstance(v, str) else f"{key}: {json.dumps(v)[:300]}"
    return "failed"


def solve_and_label(client: ModelClient, g: GatesCfg, folder: Path, instruction: str, docs: dict[str, str], rubric: Rubric,
                    step=lambda stage: None) -> gates.GateResult:
    """Run solver_check and save each attempt under folder/solver/ (other labelling models under their role)."""
    res, solutions = gates.solver_check(client, instruction, docs, rubric, g.solver_attempts, g.probe_without_documents,
                                        g.solver_max_steps, g.solver_page_chars, tuple(g.solver_models), step)
    for role, sols in solutions.items():
        sub = folder / "solver" if role == g.solver_models[0] else folder / "solver" / role
        for k, sol in enumerate(sols, 1):
            _write(sub / f"attempt_{k}.md", sol.answer)
            _write(sub / f"attempt_{k}.trace.json", sol.steps)
    return res


def _take_labels(result: MatterResult, g: gates.GateResult) -> None:
    result.solver_pass_rate = g.details.get("pass_rate")
    result.unsolved = bool(g.details.get("unsolved"))
    result.difficulty = g.details.get("difficulty", [])
    result.label_pending = False


def reference_index(g: GatesCfg) -> BloomIndex | None:
    """The benchmark index the decontamination gate screens against, or None when no reference folder is set."""
    if not g.reference_dirs:
        return None
    return BloomIndex.from_dirs(g.reference_dirs, bits=g.decontam_bloom_bits, n=g.decontam_ngram,
                                cache_dir=g.decontam_cache_dir or None, group_depth=g.decontam_group_depth)


class Pipeline:
    def __init__(self, cfg: Config, client: ModelClient | None = None, log: CallLog | None = None) -> None:
        self.cfg = cfg
        self.log = log if log is not None else getattr(client, "log", None) or CallLog()
        self.client = client or build_client(cfg, self.log)
        self.precedents = load_precedents(cfg.sources.precedent_dirs or None)
        self.index = reference_index(cfg.gates)

    # ------------------------------------------------------------ one matter

    def run_matter(self, spec: MatterSpec, out: Path, reuse: bool = False) -> MatterResult:
        work = out / "work" / spec.matter_id
        if work.exists():
            shutil.rmtree(work)
        made = _reusable(out / "rejected" / spec.matter_id, work) if reuse else {"stages": []}
        results: list[gates.GateResult] = []
        result = MatterResult(matter_id=spec.matter_id, accepted=False)

        step = lambda stage: beat(spec.matter_id, stage)
        if made["stages"]:
            step("reusing " + ", ".join(made["stages"]))

        def stage(name, make, save, load):
            """Run one generation stage, or load what a completed run of it saved in an errored try."""
            if name in made["stages"]:
                return load()
            step(name)
            value = make()
            save(value)
            made["stages"].append(name)
            tmp = work / "stages_done.json.tmp"  # written after the stage's files, and atomically
            _write(tmp, made)
            os.replace(tmp, work / "stages_done.json")
            return value

        def save_docs(docs):
            for name, content in docs.items():
                _write(work / "docs" / name, content)
            made["docs"] = list(docs)  # in drafting order, which the solver's file list follows

        def save_rubric(value):
            _write(work / "rubric.json", value[0].to_dict())
            made["rubric_repair"] = value[1]

        def check(g: gates.GateResult) -> None:
            results.append(g)
            if not g.passed:
                raise _Rejected(g.name, _first_reason(g))

        try:
            cfg = self.cfg
            _write(work / "spec.json", spec.to_dict())

            # Stage 1: plan the matter
            rng = random.Random(f"{cfg.run.seed}:{spec.matter_id}")
            chosen = select_precedents(self.precedents, spec.agreement_type, cfg.sources.precedents_per_matter, rng)
            _write(work / "precedents.json", [{"id": p.id, "title": p.title} for p in chosen])
            ledger: Ledger = stage("ledger", lambda: stages.write_ledger(self.client, spec, chosen, cfg.sources.precedent_chars),
                                   lambda v: _write(work / "ledger.json", v.to_dict()), lambda: Ledger.from_dict(_read(work / "ledger.json")))
            check(gates.ledger_schema(ledger, spec))

            # Stage 2: build the task from the ledger
            docs = stage("documents", lambda: stages.draft_documents(self.client, ledger, {p.id: p for p in chosen}, cfg.sources.precedent_chars),
                         save_docs, lambda: {n: (work / "docs" / n).read_text(encoding="utf-8") for n in made["docs"]})
            step("consistency")
            check(gates.consistency(self.client, ledger, docs))
            step("issue_check")
            check(gates.issue_check(self.client, ledger, docs, show_terms=cfg.gates.verifier_sees_terms))

            instruction = stage("instruction", lambda: stages.write_instruction(self.client, spec, ledger, cfg.instruction.name_files, cfg.instruction.max_words),
                                lambda v: _write(work / "instruction.md", v), lambda: (work / "instruction.md").read_text(encoding="utf-8"))
            check(gates.leak_check(instruction, ledger, docs, cfg.instruction.name_files, cfg.instruction.max_words))

            rubric, repair = stage("rubric", lambda: stages.write_rubric(self.client, spec, ledger, instruction, cfg.gates.check_bundling),
                                   save_rubric, lambda: (Rubric.from_dict(_read(work / "rubric.json")), made["rubric_repair"]))
            answers = stage("answers", lambda: stages.write_answers(self.client, ledger, instruction, rubric, docs, omit=rng.choice(ledger.issues).id),
                            lambda v: _write(work / "answers.json", v.to_dict()), lambda: Answers(**_read(work / "answers.json")))

            # Stage 3: try to break it. The judge sees exactly the rubric that is exported.
            if not cfg.gates.judge_hints:
                rubric = Rubric([replace(c, hints=[]) for c in rubric.criteria])
            check(gates.rubric_trace(rubric, ledger, answers, cfg.gates.check_bundling, repair))
            step("rubric_tests")
            check(gates.rubric_tests(self.client, rubric, answers))
            texts = {"instruction": instruction, "rubric": "\n".join(c.text for c in rubric.criteria), **{f"docs/{k}": v for k, v in docs.items()}}
            check(gates.decontamination(texts, self.index, cfg.gates.decontam_threshold))

            if cfg.gates.solver_check == "defer":  # `ltg label` runs it later
                results.append(gates.GateResult("solver_check", True, {"skipped": True, "reason": "deferred"}))
                result.label_pending = True
            else:
                g = solve_and_label(self.client, cfg.gates, work, instruction, docs, rubric, step)
                _take_labels(result, g)
                check(g)

            result.accepted = True
            result.split = assign_split(spec.matter_id, cfg.splits.ratios, cfg.splits.salt)
            _write(
                work / "task.json",
                {
                    "task_id": spec.matter_id,
                    "split": result.split,
                    "practice_area": spec.practice_area,
                    "agreement_type": spec.agreement_type,
                    "work_type": spec.work_type,
                    "jurisdiction": spec.jurisdiction,
                    "instruction": instruction,
                    "documents": sorted(docs),
                    "rubric": [{"id": c.id, "text": c.text, "kind": c.kind, "hints": c.hints} for c in rubric.criteria],
                    "solver_pass_rate": result.solver_pass_rate,
                    "unsolved": result.unsolved,
                    "difficulty": result.difficulty,
                    **({"label_pending": True} if result.label_pending else {}),
                },
            )
        except _Rejected as r:
            result.failed_gate, result.reason = r.gate, r.reason
        except Exception as e:  # a model call or parse failed: reject, keep the trace
            result.failed_gate, result.reason = "error", f"{type(e).__name__}: {e}"
            _write(work / "error.txt", traceback.format_exc())

        step("accepted" if result.accepted else f"rejected at {result.failed_gate}")
        result.gates = [asdict(g) for g in results]
        _write(work / "gates.json", asdict(result))  # the full verdict, so --resume can reload it
        for folder in ("accepted", "rejected"):  # a rerun must not leave the previous verdict behind
            shutil.rmtree(out / folder / spec.matter_id, ignore_errors=True)
        dest = out / ("accepted" if result.accepted else "rejected") / spec.matter_id
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(work), str(dest))
        return result

    # ------------------------------------------------------------ a run

    def _settings(self) -> dict:
        """Everything that changes what a matter produces. Run size, concurrency and folder do not."""
        s = json.loads(json.dumps(asdict(self.cfg)))
        for k in ("n_matters", "concurrency", "out_dir"):
            s["run"].pop(k)
        # Keys added after runs began, left out at their default so those runs still resume (pilot28_nrp and later).
        for section, k, default in (("backend", "timeout_retries", 1), ("gates", "solver_check", "inline"), ("spec", "min_distractors", 1)):
            if s[section].get(k) == default:
                s[section].pop(k)
        s["instruction"] = {k: v for k, v in s["instruction"].items() if v != getattr(InstructionCfg, k)}
        if not s["instruction"]:
            s.pop("instruction")
        if not s["spec"].get("cross_document_share"):
            s["spec"].pop("cross_document_share", None)
        # How a reply travels does not change what it says, so runs begun without streaming resume with it on.
        for b in (s["backend"], *s["backend"]["roles"].values()):
            for k in ("stream", "max_seconds"):
                b.pop(k, None)
        return s

    def _finished(self, out: Path, matter_id: str) -> MatterResult | None:
        """A matter with a verdict from an earlier run. Errors don't count: they are retried."""
        for folder in ("accepted", "rejected"):
            f = out / folder / matter_id / "gates.json"
            if f.exists():
                r = MatterResult(**json.loads(f.read_text()))
                return None if r.failed_gate == "error" else r
        return None

    def run(self, n: int | None = None, out_dir: str | None = None, resume: bool = False) -> dict:
        n = n if n is not None else self.cfg.run.n_matters
        out = Path(out_dir or self.cfg.run.out_dir)
        out.mkdir(parents=True, exist_ok=True)
        settings_file = out / "settings.json"
        if resume and settings_file.exists() and json.loads(settings_file.read_text()) != self._settings():
            raise ValueError(f"cannot resume {out}: settings changed since it was started (see {settings_file})")
        if resume and not settings_file.exists() and any((out / f).is_dir() for f in ("accepted", "rejected")):
            raise ValueError(f"cannot resume {out}: it has no settings.json, so its settings are unknown")
        # keep the try this resume follows, errors included; a killed try has no report, only its calls so far
        if resume and any((out / f).exists() for f in ("report.json", "calls.jsonl")):
            tries = out / "tries" / str(len(list((out / "tries").glob("*"))) + 1)
            tries.mkdir(parents=True)
            for f in ("report.json", "calls.jsonl"):
                if (out / f).exists():
                    shutil.copy2(out / f, tries / f)
        _write(settings_file, self._settings())
        self.log.stream_to(str(out / "calls.jsonl"))
        history = out / "industries_before.json"  # kept, so a --resume samples the same specs
        if not (resume and history.exists()):
            _write(history, industries_used_beside(out, self.cfg.backend.kind))
        specs = stages.sample_specs(self.cfg.spec, n, self.cfg.run.seed, json.loads(history.read_text()))
        ids = {s.matter_id for s in specs}
        stale = sorted(p.name for f in ("accepted", "rejected") if (out / f).is_dir() for p in (out / f).iterdir() if p.name not in ids)
        if stale:  # refuse rather than delete: accepted/ must match this run's report
            raise FileExistsError(f"{out} holds matters from another run ({', '.join(stale[:3])}, ...); use a new --out or delete it")
        done = {s.matter_id: r for s in specs if resume and (r := self._finished(out, s.matter_id))}
        pool = ThreadPoolExecutor(max_workers=max(1, self.cfg.run.concurrency))  # matters are independent
        try:
            results = list(pool.map(lambda s: done.get(s.matter_id) or self.run_matter(s, out, reuse=resume), specs))
        finally:  # on Ctrl-C or a crash, finish the matters in flight but start no queued ones
            pool.shutdown(cancel_futures=True)
        shutil.rmtree(out / "work", ignore_errors=True)
        report = build_report(results, self.log, self.cfg.backend.kind, resumed=len(done))
        report["variety"] = variety(out, results)
        _write(out / "report.json", report)
        _write(out / "report.md", render_report(report))
        return report


def label_runs(cfg: Config, run_dirs: list[str], config_path: str | None = None) -> dict:
    """`ltg label`: run solver_check on every accepted task with label_pending, `cfg.run.concurrency` at a time, with
    the solver roles and attempts of `cfg` (a solver config). A task that errors stays pending for the next call.
    Appends calls to each run's calls.jsonl and refreshes its report."""
    pending, clients = [], {}
    for r in map(Path, run_dirs):
        found = [t.parent for t in sorted((r / "accepted").glob("*/task.json")) if _read(t).get("label_pending")]
        if found:
            log = CallLog(path=str(r / "calls.jsonl"))  # appends: the run's own calls stay
            clients[r] = (build_client(cfg, log), log)
            pending += [(r, m) for m in found]

    def one(item) -> str:
        run, m = item
        try:
            return label_task(clients[run][0], cfg.gates, m, config_path)
        except Exception as e:  # stays pending; rerunning `ltg label` retries it
            beat(f"{run.name}/{m.name}", f"label error, still pending: {type(e).__name__}: {e}")
            _write(m / "label_error.txt", traceback.format_exc())
            return "error"

    pool = ThreadPoolExecutor(max_workers=max(1, cfg.run.concurrency))
    try:
        outcomes = list(pool.map(one, pending))
    finally:
        pool.shutdown(cancel_futures=True)
    for run, (_, log) in clients.items():
        refresh_report(run, log)
    return {k: outcomes.count(k) for k in ("labelled", "leak", "error")}


def label_task(client: ModelClient, g: GatesCfg, m: Path, config_path: str | None = None) -> str:
    """Label one pending task in place; a leak (solved without documents) moves it to rejected/."""
    task, result = _read(m / "task.json"), MatterResult(**_read(m / "gates.json"))
    names = _read(m / "stages_done.json")["docs"] if (m / "stages_done.json").exists() else sorted(task["documents"])
    docs = {n: (m / "docs" / n).read_text(encoding="utf-8") for n in names}  # drafting order, as the inline solver saw it
    step = lambda stage: beat(f"{m.parent.parent.name}/{m.name}", stage)
    step("label")
    shutil.rmtree(m / "solver", ignore_errors=True)
    res = solve_and_label(client, g, m, task["instruction"], docs, Rubric.from_dict({"criteria": task["rubric"]}), step)
    _take_labels(result, res)
    result.labelled_by = {"config": config_path, "models": [getattr(client, "model_for", lambda r: "")(r) or r for r in g.solver_models],
                          "probe_without_documents_passed": res.details.get("probe_without_documents_passed")}
    result.gates = [x for x in result.gates if x["name"] != "solver_check"] + [asdict(res)]
    (m / "label_error.txt").unlink(missing_ok=True)
    if not res.passed:
        result.accepted, result.failed_gate, result.reason, result.split = False, "solver_check", _first_reason(res), None
        _write(m / "gates.json", asdict(result))
        (m / "task.json").unlink()
        dest = m.parent.parent / "rejected" / m.name
        shutil.rmtree(dest, ignore_errors=True)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(m), str(dest))
        step("rejected at solver_check (leak)")
        return "leak"
    _write(m / "gates.json", asdict(result))
    task.pop("label_pending", None)
    task.update(solver_pass_rate=result.solver_pass_rate, unsolved=result.unsolved, difficulty=result.difficulty, labelled_by=result.labelled_by)
    _write(m / "task.json", task)  # last: label_pending stays set until everything else is written
    step("labelled " + ", ".join(f"{d['model']} {d['pass_rate']:.2f}" for d in result.difficulty))
    return "labelled"


def refresh_report(out: Path, label_log: CallLog) -> None:
    """Rebuild report.json and report.md from the matters' gates.json; model calls add the labelling calls."""
    old = _read(out / "report.json") if (out / "report.json").exists() else {}
    results = sorted((MatterResult(**_read(f)) for d in ("accepted", "rejected") for f in (out / d).glob("*/gates.json")),
                     key=lambda r: r.matter_id)
    rep = build_report(results, label_log, old.get("backend") or _read(out / "settings.json")["backend"]["kind"], old.get("resumed", 0))
    calls = old.get("model_calls", {})
    for role, s in rep["model_calls"].items():
        calls[role] = {k: calls.get(role, {}).get(k, 0) + v for k, v in s.items()}
    rep["model_calls"] = calls
    rep["variety"] = variety(out, results)
    _write(out / "report.json", rep)
    _write(out / "report.md", render_report(rep))


def _reusable(prev: Path, work: Path) -> dict:
    """The generation stages an errored try of this matter completed. Its folder becomes the work folder again,
    without the old verdict and solver output, so only the gates rerun. Anything else starts from scratch."""
    try:
        made = _read(prev / "stages_done.json")
        if _read(prev / "gates.json")["failed_gate"] != "error":
            return {"stages": []}
    except (OSError, ValueError, KeyError):
        return {"stages": []}
    work.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(prev), str(work))
    for f in ("gates.json", "error.txt", "task.json"):
        (work / f).unlink(missing_ok=True)
    shutil.rmtree(work / "solver", ignore_errors=True)
    return made


def variety(out: Path, results: list[MatterResult]) -> dict:
    """How much the run's matters differ: industries, agreement types, issue types, and anything repeated.

    Read from each matter's saved spec and ledger, so it also covers matters reloaded by --resume."""
    industries, agreements, issues, combos, names = Counter(), Counter(), Counter(), Counter(), {}
    for r in results:
        folder = next((out / f / r.matter_id for f in ("accepted", "rejected") if (out / f / r.matter_id).is_dir()), None)
        if folder is None or not (folder / "spec.json").exists():
            continue
        spec = json.loads((folder / "spec.json").read_text())
        industries[spec.get("industry") or "(none)"] += 1
        agreements[spec["agreement_type"]] += 1
        issues.update(spec["issue_types"])
        combos[" + ".join(sorted(spec["issue_types"]))] += 1
        if (folder / "ledger.json").exists():
            for p in json.loads((folder / "ledger.json").read_text()).get("parties", []):
                word = (p.get("name") or "").split(" ")[0].strip(",.").lower()
                if word:
                    names.setdefault(word, set()).add(r.matter_id)
    return {
        "industries": dict(industries.most_common()),
        "agreement_types": dict(agreements.most_common()),
        "issue_types": dict(issues.most_common()),
        "repeated_names": {w: sorted(ms) for w, ms in sorted(names.items()) if len(ms) > 1},
        "repeated_issue_sets": {c: n for c, n in combos.items() if n > 1},
    }


def industries_used_beside(out: Path, backend_kind: str) -> dict[str, int]:
    """How often each industry was used by the other run folders beside `out` with the same backend kind (so fake
    runs neither see nor shape real ones), from their matters' saved specs."""
    used: Counter = Counter()
    for settings in out.parent.glob("*/settings.json"):
        run = settings.parent
        if run.resolve() == out.resolve():
            continue
        try:
            if json.loads(settings.read_text()).get("backend", {}).get("kind") != backend_kind:
                continue
            used.update(json.loads(p.read_text()).get("industry", "") for p in run.glob("*/*/spec.json"))
        except (OSError, ValueError):
            continue
    used.pop("", None)
    return dict(used)


def build_report(results: list[MatterResult], log: CallLog, backend: str, resumed: int = 0) -> dict:
    gate_stats = {g: {"evaluated": 0, "passed": 0, "failed": 0, "skipped": 0} for g in GATE_ORDER}
    for r in results:
        for g in r.gates:
            s = gate_stats[g["name"]]
            s["evaluated"] += 1
            s["skipped" if g["details"].get("skipped") else "passed" if g["passed"] else "failed"] += 1
    errors = sum(1 for r in results if r.failed_gate == "error")
    traces = [g["details"] for r in results for g in r.gates if g["name"] == "rubric_trace"]
    repairs = {"ran": sum(1 for d in traces if d.get("repair", {}).get("ran")),
               "cleared": sum(1 for d in traces if d.get("repair", {}).get("cleared")),
               "bundled_after": sum(1 for d in traces if d.get("bundled"))}  # matters whose final rubric still has bundled clauses
    spread: dict[str, dict] = {}  # per labelling model: how many accepted tasks sit at each pass rate
    for r in results:
        for d in r.difficulty if r.accepted else []:
            m = spread.setdefault(d["model"], {"tasks": 0, "pass_rates": {}})
            m["tasks"] += 1
            m["pass_rates"][f"{d['pass_rate']:.2f}"] = m["pass_rates"].get(f"{d['pass_rate']:.2f}", 0) + 1
    return {
        "backend": backend,
        "candidates": len(results),
        "accepted": sum(r.accepted for r in results),
        "errors": errors,
        "resumed": resumed,
        "gates": gate_stats,
        "rubric_repairs": repairs,
        "unsolved": sum(1 for r in results if r.accepted and r.unsolved),
        "label_pending": sum(1 for r in results if r.accepted and r.label_pending),
        "difficulty": {m: {"tasks": v["tasks"], "pass_rates": dict(sorted(v["pass_rates"].items()))} for m, v in sorted(spread.items())},
        "matters": [
            {"matter_id": r.matter_id, "accepted": r.accepted, "failed_gate": r.failed_gate, "reason": r.reason, "split": r.split,
             "solver_pass_rate": r.solver_pass_rate, "unsolved": r.unsolved, "difficulty": r.difficulty,
             "label_pending": r.label_pending}
            for r in results
        ],
        "model_calls": log.by_role(),
    }


def render_report(rep: dict) -> str:
    lines = [
        "# Run report",
        "",
        f"Backend: `{rep['backend']}`. Accepted **{rep['accepted']} of {rep['candidates']}** candidate matters"
        + (f" ({rep['errors']} stopped by errors)." if rep["errors"] else "."),
        *([f"{rep['resumed']} matters were reloaded from an earlier run; model calls below cover this run only."] if rep["resumed"] else []),
        "",
        "## Gates",
        "",
        "| Gate | Evaluated | Passed | Failed | Skipped |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for g, s in rep["gates"].items():
        lines.append(f"| {g} | {s['evaluated']} | {s['passed']} | {s['failed']} | {s['skipped']} |")
    if rep["gates"]["decontamination"]["skipped"]:
        lines += ["", "**Decontamination was skipped (no `reference_dirs`): these tasks were NOT screened against LAB.**"]
    rr = rep.get("rubric_repairs") or {}
    if rr.get("ran") or rr.get("bundled_after"):
        lines += ["", f"Bundled issue criteria (`gates.check_bundling`): {rr['bundled_after']} matter(s) flagged in the final rubric; "
                  f"{rr['ran']} repair(s) ran, {rr['cleared']} cleared."]
    lines += ["", "## Difficulty", "", "Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever "
              "trains picks the band that fits their model.", "", "| Model | Tasks | Pass rate: tasks |", "| --- | ---: | --- |"]
    for model, d in rep.get("difficulty", {}).items():
        lines.append(f"| {model} | {d['tasks']} | " + ", ".join(f"{k}: {n}" for k, n in d["pass_rates"].items()) + " |")
    if rep.get("unsolved"):
        lines += ["", f"**{rep['unsolved']} accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**"]
    if rep.get("label_pending"):
        lines += ["", f"**{rep['label_pending']} accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no "
                  "difficulty label and no leak probe yet.**"]
    lines += ["", "## Matters", "", "| Matter | Result | Split | Pass rate per model | Reason |", "| --- | --- | --- | --- | --- |"]
    for m in rep["matters"]:
        res = (("accepted (label pending)" if m.get("label_pending") else "accepted (unsolved)" if m.get("unsolved") else "accepted")
               if m["accepted"] else f"rejected at {m['failed_gate']}")
        rate = ", ".join(f"{d['model']} {d['pass_rate']:.2f}" for d in m.get("difficulty") or [])
        reason = (m["reason"] or "").replace("|", "/")[:160]
        lines.append(f"| {m['matter_id']} | {res} | {m['split'] or ''} | {rate} | {reason} |")
    v = rep.get("variety")
    if v:
        counts = lambda d: ", ".join(f"{k} ({n})" for k, n in d.items()) or "none"
        lines += ["", "## Variety", "", f"- Industries: {counts(v['industries'])}", f"- Agreement types: {counts(v['agreement_types'])}",
                  f"- Issue types: {counts(v['issue_types'])}"]
        rn = "; ".join(f"{w} in {', '.join(ms)}" for w, ms in v["repeated_names"].items())
        lines += [f"- Party names used in more than one matter: {rn or 'none'}",
                  f"- Identical issue sets: {counts(v['repeated_issue_sets'])}"]
    lines += ["", "## Model calls", "", "| Role | Calls | Input tokens | Output tokens | Errors |", "| --- | ---: | ---: | ---: | ---: |"]
    for role, s in sorted(rep["model_calls"].items()):
        lines.append(f"| {role} | {s['calls']} | {s['input_tokens']} | {s['output_tokens']} | {s['errors']} |")
    return "\n".join(lines) + "\n"
