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
from .solver import Solution, solve
from .stages import Documents, judge


@dataclass
class GateResult:
    name: str
    passed: bool
    details: dict[str, Any] = field(default_factory=dict)


def _norm(s) -> str:
    s = ("" if s is None else str(s)).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s.strip(" .;,\"'")


_PLAIN = str.maketrans({"\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'", "*": None, "_": None})


def _plain(s) -> str:
    """Normalised text with Markdown emphasis and curly quotes removed: '"**Territory**" means' -> '"territory" means'."""
    return _norm(str(s or "").translate(_PLAIN))


# ---------------------------------------------------------------- deterministic


def ledger_schema(ledger: Ledger, spec: MatterSpec) -> GateResult:
    errs = validate_ledger(ledger, spec)
    return GateResult("ledger_schema", not errs, {"errors": errs})


def _words(s: str) -> str:
    """Lowercase words separated by single spaces, so "change_of_control.md" matches "change of control"."""
    return " " + " ".join(re.findall(r"[a-z0-9]+", s.lower())) + " "


def leak_check(instruction: str, ledger: Ledger, docs: Documents) -> GateResult:
    """Nothing the solver sees outside the document text may name an issue or quote its multi-word detect terms.

    That covers the instruction, and the filenames and document kinds, which the ledger writer chose while
    knowing the issues. Documents must not carry HTML comments: drafter notes the solver would read.
    """
    visible = {"instruction": instruction, **{d.filename: f"{d.filename} {d.kind}" for d in ledger.documents}}
    hits = []
    for where, text in visible.items():
        for i in ledger.issues:
            for phrase in [i.label, *[t for t in i.detect_terms if len(t.split()) > 1]]:
                if _words(phrase).strip() and _words(phrase) in _words(text):
                    hits.append({"issue": i.id, "phrase": phrase, "in": where})
    comments = sorted(n for n, c in docs.items() if "<!--" in c)
    passed = bool(instruction.strip()) and not hits and not comments
    return GateResult("leak_check", passed, {"hits": hits, "html_comments": comments, "empty": not instruction.strip()})


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

    Values that differ only after normalisation go to a matcher, which compares the two values (it never
    sees the documents): real drafting says "the laws of the State of New York" where the ledger says
    "State of New York", and only a mismatch in meaning should reject the task.
    """
    fname = {d.id: d.filename for d in ledger.documents}
    planted = {(i.contradicts, fname.get(i.doc)) for i in ledger.issues if i.contradicts}
    payload = {
        "documents": [{"filename": n, "content": c} for n, c in docs.items()],
        "queries": [{"id": f"{f.id}@{n}", "key": f.key, "filename": n} for f in ledger.facts for n in docs],
    }
    out = call_json(client, "fact_extractor", prompts.FACT_EXTRACTOR, render_input(payload))
    got = {r["id"]: r.get("value") for r in out.get("facts", []) if "id" in r}
    # One long call misses values (a real run: 1 of 40 came back empty though its document stated it). Ask again,
    # focused, for each fact its own document seemed not to state; still without telling the extractor the value.
    retry = [{"id": f"{f.id}@{fname[f.doc]}", "key": f.key, "filename": fname[f.doc]}
             for f in ledger.facts if not _norm(got.get(f"{f.id}@{fname[f.doc]}"))]
    if retry:
        names = sorted({q["filename"] for q in retry})
        again = {"documents": [{"filename": n, "content": docs[n]} for n in names], "queries": retry}
        out = call_json(client, "fact_extractor", prompts.FACT_EXTRACTOR, render_input(again))
        got.update({r["id"]: r.get("value") for r in out.get("facts", []) if "id" in r and _norm(r.get("value"))})
    differ = []
    for f in ledger.facts:
        for n in docs:
            v = got.get(f"{f.id}@{n}")
            if _norm(v) == _norm(f.value):
                continue
            if n != fname[f.doc] and (not _norm(v) or (f.id, n) in planted):
                continue  # silent elsewhere, or a deliberate contradiction
            differ.append({"fact": f.id, "key": f.key, "filename": n, "ledger": f.value, "document": v})
    same: set[int] = set()
    worded = [k for k, d in enumerate(differ) if _norm(d["document"])]  # a missing value needs no matcher
    if worded:
        pairs = [{"id": str(k), "fact": differ[k]["key"], "ledger": differ[k]["ledger"], "document": differ[k]["document"]} for k in worded]
        out = call_json(client, "fact_matcher", prompts.FACT_MATCHER, render_input({"pairs": pairs}))
        same = {int(r["id"]) for r in out.get("results", []) if r.get("same") is True and str(r.get("id", "")).isdigit()}
    mismatches = [d for k, d in enumerate(differ) if k not in same]
    return GateResult(
        "consistency",
        not mismatches,
        {"mismatches": mismatches, "reworded": len(same), "checked": len(payload["queries"])},
    )


def issue_check(client: ModelClient, ledger: Ledger, docs: Documents, show_terms: bool = False) -> GateResult:
    """Each planted issue must actually be present and findable where the ledger put it.

    Two checks: the drafter was told to use every detect term verbatim, which code verifies for free
    (ignoring Markdown emphasis and curly quotes); then a verifier that (by default) is not given those terms
    judges whether the problem is really there. It sees the rest of the folder too, since an issue can
    depend on a fact stated elsewhere (a change-of-control clause matters because a letter of intent exists).
    """
    fname = {d.id: d.filename for d in ledger.documents}
    results = []
    for i in ledger.issues:
        content = docs.get(fname[i.doc], "")
        missing_terms = [t for t in i.detect_terms if _plain(t) not in _plain(content)]
        if missing_terms:
            results.append({"issue": i.id, "present": False, "missing_terms": missing_terms})
            continue
        issue = {"label": i.label, "description": i.description, "section": i.section}
        if show_terms:
            issue["detect_terms"] = i.detect_terms
        others = [{"filename": n, "content": c} for n, c in docs.items() if n != fname[i.doc]]
        payload = {"document": {"filename": fname[i.doc], "content": content}, "other_documents": others, "issue": issue}
        out = call_json(client, "issue_verifier", prompts.ISSUE_VERIFIER, render_input(payload))
        results.append({"issue": i.id, "present": bool(out.get("present")), "evidence": out.get("evidence", "")})
    missing = [r["issue"] for r in results if not r["present"]]
    return GateResult("issue_check", not missing, {"missing": missing, "results": results})


def rubric_tests(client: ModelClient, rubric: Rubric, answers: Answers) -> GateResult:
    """A rubric is code, so unit-test it: gold passes all, blank passes none, and the flawed answer fails
    exactly the criteria for the issue it omits (anything else it fails means a criterion is not specific)."""
    gold = judge(client, answers.gold, rubric)
    blank = judge(client, "", rubric)
    flawed = judge(client, answers.flawed, rubric)

    gold_fails = [c for c, ok in gold.items() if not ok]
    graded_on_blank = [c.id for c in rubric.criteria if c.kind != "negative"]  # negatives pass on blank by design
    blank_passes = [c for c in graded_on_blank if blank[c]]
    should_fail = [c.id for c in rubric.criteria if c.kind == "issue" and c.source in answers.flawed_omits]
    flawed_wrongly_passes = [c for c in should_fail if flawed[c]]
    flawed_wrongly_fails = [c for c, ok in flawed.items() if not ok and c not in should_fail]

    passed = not gold_fails and not blank_passes and bool(should_fail) and not flawed_wrongly_passes and not flawed_wrongly_fails
    return GateResult(
        "rubric_tests",
        passed,
        {
            "gold_fails": gold_fails,
            "blank_passes": blank_passes,
            "flawed_should_fail": should_fail,
            "flawed_wrongly_passes": flawed_wrongly_passes,
            "flawed_wrongly_fails": flawed_wrongly_fails,
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
    max_steps: int = 20,
    page_chars: int = 6000,
) -> tuple[GateResult, list[Solution]]:
    """Run a tool-using solver that never sees the ledger. Returns the gate result and the solver's attempts."""
    solutions: list[Solution] = []
    details: dict[str, Any] = {}

    if probe_without_documents:
        probe = solve(client, instruction, {}, max_steps, page_chars)
        probe_grades = judge(client, probe.answer, rubric)
        details["probe_without_documents_passed"] = all(probe_grades.values())
        if details["probe_without_documents_passed"]:
            details["reason"] = "solved without opening any document: the instruction leaks the answer"
            return GateResult("solver_check", False, details), [probe]

    runs = []
    for _ in range(attempts):
        sol = solve(client, instruction, docs, max_steps, page_chars)
        grades = judge(client, sol.answer, rubric)
        solutions.append(sol)
        runs.append(
            {
                "passed": all(grades.values()),
                "failed_criteria": [c for c, ok in grades.items() if not ok],
                "steps": len(sol.steps),
                "files_opened": sol.files_opened(),
            }
        )
    rate = sum(r["passed"] for r in runs) / max(attempts, 1)
    details.update({"pass_rate": round(rate, 3), "runs": runs})
    if rate < min_rate:
        details["reason"] = "no attempt passed: task is probably broken or too hard"
    elif rate > max_rate:
        details["reason"] = "every attempt passed: too easy to carry training signal"
    return GateResult("solver_check", min_rate <= rate <= max_rate, details), solutions
