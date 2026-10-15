"""Runs matters through all three stages and writes everything to disk.

Output layout (one folder per candidate matter):

    <out>/accepted/<matter_id>/   tasks that passed every gate (has task.json)
    <out>/rejected/<matter_id>/   everything else, kept for debugging
    <out>/report.json, report.md  pass counts per gate, model calls per role
    <out>/calls.jsonl             one line per model call

Inside a matter folder: spec.json, precedents.json, ledger.json, docs/, instruction.md,
rubric.json, answers.json, solver/, gates.json.
"""

from __future__ import annotations

import json
import random
import shutil
import traceback
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

from . import gates, stages
from .config import Config, build_client
from .decontam import BloomIndex
from .models import CallLog, ModelClient
from .schema import Ledger, MatterSpec, Rubric
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


def _first_reason(g: gates.GateResult) -> str:
    d = g.details
    for key in ("reason", "errors", "mismatches", "missing", "hits", "html_comments", "gold_fails", "blank_passes", "flawed_wrongly_passes", "flawed_wrongly_fails", "flagged"):
        if d.get(key):
            v = d[key]
            return v if isinstance(v, str) else f"{key}: {json.dumps(v)[:300]}"
    return "failed"


class Pipeline:
    def __init__(self, cfg: Config, client: ModelClient | None = None, log: CallLog | None = None) -> None:
        self.cfg = cfg
        self.log = log if log is not None else getattr(client, "log", None) or CallLog()
        self.client = client or build_client(cfg, self.log)
        self.precedents = load_precedents(cfg.sources.precedent_dirs or None)
        g = cfg.gates
        self.index = BloomIndex.from_dirs(g.reference_dirs, bits=g.decontam_bloom_bits, n=g.decontam_ngram) if g.reference_dirs else None

    # ------------------------------------------------------------ one matter

    def run_matter(self, spec: MatterSpec, out: Path) -> MatterResult:
        work = out / "work" / spec.matter_id
        if work.exists():
            shutil.rmtree(work)
        results: list[gates.GateResult] = []
        result = MatterResult(matter_id=spec.matter_id, accepted=False)

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
            ledger: Ledger = stages.write_ledger(self.client, spec, chosen, cfg.sources.precedent_chars)
            _write(work / "ledger.json", ledger.to_dict())
            check(gates.ledger_schema(ledger, spec))

            # Stage 2: build the task from the ledger
            docs = stages.draft_documents(self.client, ledger, {p.id: p for p in chosen}, cfg.sources.precedent_chars)
            for name, content in docs.items():
                _write(work / "docs" / name, content)
            check(gates.consistency(self.client, ledger, docs))
            check(gates.issue_check(self.client, ledger, docs, show_terms=cfg.gates.verifier_sees_terms))

            instruction = stages.write_instruction(self.client, spec, ledger)
            _write(work / "instruction.md", instruction)
            check(gates.leak_check(instruction, ledger, docs))

            rubric = stages.write_rubric(self.client, spec, ledger, instruction)
            _write(work / "rubric.json", rubric.to_dict())
            answers = stages.write_answers(self.client, ledger, instruction, rubric, docs, omit=rng.choice(ledger.issues).id)
            _write(work / "answers.json", answers.to_dict())

            # Stage 3: try to break it. The judge sees exactly the rubric that is exported.
            if not cfg.gates.judge_hints:
                rubric = Rubric([replace(c, hints=[]) for c in rubric.criteria])
            check(gates.rubric_trace(rubric, ledger, answers))
            check(gates.rubric_tests(self.client, rubric, answers))
            texts = {"instruction": instruction, "rubric": "\n".join(c.text for c in rubric.criteria), **{f"docs/{k}": v for k, v in docs.items()}}
            check(gates.decontamination(texts, self.index, cfg.gates.decontam_threshold))

            g, solver_answers = gates.solver_check(
                self.client,
                instruction,
                docs,
                rubric,
                cfg.gates.solver_attempts,
                cfg.gates.solver_min_pass_rate,
                cfg.gates.solver_max_pass_rate,
                cfg.gates.probe_without_documents,
            )
            for k, a in enumerate(solver_answers, 1):
                _write(work / "solver" / f"attempt_{k}.md", a)
            result.solver_pass_rate = g.details.get("pass_rate")
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
                },
            )
        except _Rejected as r:
            result.failed_gate, result.reason = r.gate, r.reason
        except Exception as e:  # a model call or parse failed: reject, keep the trace
            result.failed_gate, result.reason = "error", f"{type(e).__name__}: {e}"
            _write(work / "error.txt", traceback.format_exc())

        result.gates = [asdict(g) for g in results]
        _write(work / "gates.json", {"accepted": result.accepted, "failed_gate": result.failed_gate, "reason": result.reason, "gates": result.gates})
        for folder in ("accepted", "rejected"):  # a rerun must not leave the previous verdict behind
            shutil.rmtree(out / folder / spec.matter_id, ignore_errors=True)
        dest = out / ("accepted" if result.accepted else "rejected") / spec.matter_id
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(work), str(dest))
        return result

    # ------------------------------------------------------------ a run

    def run(self, n: int | None = None, out_dir: str | None = None) -> dict:
        n = n if n is not None else self.cfg.run.n_matters
        out = Path(out_dir or self.cfg.run.out_dir)
        out.mkdir(parents=True, exist_ok=True)
        specs = stages.sample_specs(self.cfg.spec, n, self.cfg.run.seed)
        ids = {s.matter_id for s in specs}
        stale = sorted(p.name for f in ("accepted", "rejected") if (out / f).is_dir() for p in (out / f).iterdir() if p.name not in ids)
        if stale:  # refuse rather than delete: accepted/ must match this run's report
            raise FileExistsError(f"{out} holds matters from another run ({', '.join(stale[:3])}, ...); use a new --out or delete it")
        results = [self.run_matter(s, out) for s in specs]
        shutil.rmtree(out / "work", ignore_errors=True)
        report = build_report(results, self.log, self.cfg)
        _write(out / "report.json", report)
        _write(out / "report.md", render_report(report))
        self.log.dump(str(out / "calls.jsonl"))
        return report


def build_report(results: list[MatterResult], log: CallLog, cfg: Config) -> dict:
    gate_stats = {g: {"evaluated": 0, "passed": 0, "failed": 0, "skipped": 0} for g in GATE_ORDER}
    for r in results:
        for g in r.gates:
            s = gate_stats[g["name"]]
            s["evaluated"] += 1
            s["skipped" if g["details"].get("skipped") else "passed" if g["passed"] else "failed"] += 1
    errors = sum(1 for r in results if r.failed_gate == "error")
    return {
        "backend": cfg.backend.kind,
        "candidates": len(results),
        "accepted": sum(r.accepted for r in results),
        "errors": errors,
        "gates": gate_stats,
        "matters": [
            {"matter_id": r.matter_id, "accepted": r.accepted, "failed_gate": r.failed_gate, "reason": r.reason, "split": r.split, "solver_pass_rate": r.solver_pass_rate}
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
    lines += ["", "## Matters", "", "| Matter | Result | Split | Solver pass rate | Reason |", "| --- | --- | --- | ---: | --- |"]
    for m in rep["matters"]:
        res = "accepted" if m["accepted"] else f"rejected at {m['failed_gate']}"
        rate = "" if m["solver_pass_rate"] is None else f"{m['solver_pass_rate']:.2f}"
        reason = (m["reason"] or "").replace("|", "/")[:160]
        lines.append(f"| {m['matter_id']} | {res} | {m['split'] or ''} | {rate} | {reason} |")
    lines += ["", "## Model calls", "", "| Role | Calls | Input tokens | Output tokens | Errors |", "| --- | ---: | ---: | ---: | ---: |"]
    for role, s in sorted(rep["model_calls"].items()):
        lines.append(f"| {role} | {s['calls']} | {s['input_tokens']} | {s['output_tokens']} | {s['errors']} |")
    return "\n".join(lines) + "\n"
