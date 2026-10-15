"""Stage 3: gates that try to break a candidate task. Each returns a GateResult.

Cheap deterministic gates run before model-based ones, and the solver check (the most
expensive) runs last, so a broken task is discarded as early as possible.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from . import prompts
from .decontam import BloomIndex
from .models import ModelClient, call_json, render_input
from .schema import Answers, Ledger, MatterSpec, Rubric, validate_answers, validate_ledger, validate_rubric
from .stages import Documents, judge, solve


@dataclass
class GateResult:
    name: str
    passed: bool
    details: dict[str, Any] = field(default_factory=dict)


def _norm(s) -> str:
    s = ("" if s is None else str(s)).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s.strip(" .;,\"'")


# ---------------------------------------------------------------- deterministic


def ledger_schema(ledger: Ledger, spec: MatterSpec) -> GateResult:
    errs = validate_ledger(ledger, spec)
    return GateResult("ledger_schema", not errs, {"errors": errs})


def leak_check(instruction: str, ledger: Ledger) -> GateResult:
    """The instruction must not name an issue or quote its multi-word detect terms."""
    low = instruction.lower()
    hits = []
    for i in ledger.issues:
        for phrase in [i.label, *[t for t in i.detect_terms if " " in t.strip()]]:
            if phrase and phrase.lower() in low:
                hits.append({"issue": i.id, "phrase": phrase})
    passed = bool(instruction.strip()) and not hits
    return GateResult("leak_check", passed, {"hits": hits, "empty": not instruction.strip()})


def rubric_trace(rubric: Rubric, ledger: Ledger, answers: Answers) -> GateResult:
    errs = validate_rubric(rubric, ledger) + validate_answers(answers, ledger)
    return GateResult("rubric_trace", not errs, {"errors": errs, "n_criteria": len(rubric.criteria)})


def decontamination(texts: dict[str, str], index: BloomIndex | None, threshold: float) -> GateResult:
    if index is None:
        return GateResult("decontamination", True, {"skipped": "no reference_dirs configured"})
    scores = {name: round(index.containment(t), 3) for name, t in texts.items()}
    flagged = {k: v for k, v in scores.items() if v >= threshold}
    return GateResult("decontamination", not flagged, {"max": max(scores.values(), default=0.0), "flagged": flagged})


# ---------------------------------------------------------------- model-based


def consistency(client: ModelClient, ledger: Ledger, docs: Documents) -> GateResult:
    """Re-extract every fact from EVERY drafted file, WITHOUT telling the extractor the value.

    A fact's own document must state the ledger value. Any other document may stay silent, but must not
    state a different value unless a planted issue `contradicts` that fact there. Otherwise the drafter
    has planted a conflict the answer key does not know about.
    """
    fname = {d.id: d.filename for d in ledger.documents}
    planted = {(i.contradicts, fname.get(i.doc)) for i in ledger.issues if i.contradicts}
    payload = {
        "documents": [{"filename": n, "content": c} for n, c in docs.items()],
        "queries": [{"id": f"{f.id}@{n}", "key": f.key, "filename": n} for f in ledger.facts for n in docs],
    }
    out = call_json(client, "fact_extractor", prompts.FACT_EXTRACTOR, render_input(payload))
    got = {r["id"]: r.get("value") for r in out.get("facts", []) if "id" in r}
    mismatches = []
    for f in ledger.facts:
        for n in docs:
            v = got.get(f"{f.id}@{n}")
            if _norm(v) == _norm(f.value):
                continue
            if n != fname[f.doc] and (not _norm(v) or (f.id, n) in planted):
                continue  # silent elsewhere, or a deliberate contradiction
            mismatches.append({"fact": f.id, "key": f.key, "filename": n, "ledger": f.value, "document": v})
    return GateResult("consistency", not mismatches, {"mismatches": mismatches, "checked": len(payload["queries"])})


def issue_check(client: ModelClient, ledger: Ledger, docs: Documents, show_terms: bool = False) -> GateResult:
    """Each planted issue must actually be present and findable where the ledger put it.

    Two checks: the drafter was told to use every detect term verbatim, which code verifies for free;
    then a verifier that (by default) is not given those terms judges whether the problem is really there.
    """
    fname = {d.id: d.filename for d in ledger.documents}
    results = []
    for i in ledger.issues:
        content = docs.get(fname[i.doc], "")
        missing_terms = [t for t in i.detect_terms if _norm(t) not in _norm(content)]
        if missing_terms:
            results.append({"issue": i.id, "present": False, "missing_terms": missing_terms})
            continue
        issue = {"label": i.label, "description": i.description, "section": i.section}
        if show_terms:
            issue["detect_terms"] = i.detect_terms
        payload = {"document": {"filename": fname[i.doc], "content": content}, "issue": issue}
        out = call_json(client, "issue_verifier", prompts.ISSUE_VERIFIER, render_input(payload))
        results.append({"issue": i.id, "present": bool(out.get("present")), "evidence": out.get("evidence", "")})
    missing = [r["issue"] for r in results if not r["present"]]
    return GateResult("issue_check", not missing, {"missing": missing, "results": results})


def rubric_tests(client: ModelClient, rubric: Rubric, answers: Answers) -> GateResult:
    """A rubric is code, so unit-test it: gold passes all, blank passes none, flawed fails where it should."""
    gold = judge(client, answers.gold, rubric)
    blank = judge(client, "", rubric)
    flawed = judge(client, answers.flawed, rubric)

    gold_fails = [c for c, ok in gold.items() if not ok]
    graded_on_blank = [c.id for c in rubric.criteria if c.kind != "negative"]  # negatives pass on blank by design
    blank_passes = [c for c in graded_on_blank if blank[c]]
    should_fail = [c.id for c in rubric.criteria if c.kind == "issue" and c.source in answers.flawed_omits]
    flawed_wrongly_passes = [c for c in should_fail if flawed[c]]

    passed = not gold_fails and not blank_passes and bool(should_fail) and not flawed_wrongly_passes
    return GateResult(
        "rubric_tests",
        passed,
        {
            "gold_fails": gold_fails,
            "blank_passes": blank_passes,
            "flawed_should_fail": should_fail,
            "flawed_wrongly_passes": flawed_wrongly_passes,
        },
    )


def solver_check(
    client: ModelClient,
    instruction: str,
    docs: Documents,
    rubric: Rubric,
    attempts: int,
    min_rate: float,
    max_rate: float,
    probe_without_documents: bool,
) -> tuple[GateResult, list[str]]:
    """Run a solver that never sees the ledger. Returns the gate result and the solver's answers."""
    answers: list[str] = []
    details: dict[str, Any] = {}

    if probe_without_documents:
        probe = solve(client, instruction, {})
        probe_grades = judge(client, probe, rubric)
        details["probe_without_documents_passed"] = all(probe_grades.values())
        if details["probe_without_documents_passed"]:
            details["reason"] = "solved without opening any document: the instruction leaks the answer"
            return GateResult("solver_check", False, details), [probe]

    runs = []
    for _ in range(attempts):
        ans = solve(client, instruction, docs)
        grades = judge(client, ans, rubric)
        answers.append(ans)
        runs.append({"passed": all(grades.values()), "failed_criteria": [c for c, ok in grades.items() if not ok]})
    rate = sum(r["passed"] for r in runs) / max(attempts, 1)
    details.update({"pass_rate": round(rate, 3), "runs": runs})
    if rate < min_rate:
        details["reason"] = "no attempt passed: task is probably broken or too hard"
    elif rate > max_rate:
        details["reason"] = "every attempt passed: too easy to carry training signal"
    return GateResult("solver_check", min_rate <= rate <= max_rate, details), answers
