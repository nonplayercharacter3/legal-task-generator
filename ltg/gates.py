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
from .schema import Answers, Ledger, MatterSpec, Rubric, bundling_errors, validate_answers, validate_ledger, validate_rubric
from .solver import Solution, solve
from .stages import Documents, judge, judge_with_reasons


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


def rubric_trace(rubric: Rubric, ledger: Ledger, answers: Answers, bundling: str = "warn", repair: dict | None = None) -> GateResult:
    """Deterministic trace of rubric and answers to the ledger.

    `bundling` is `gates.check_bundling`: bundled clauses still present reject under "repair" (the writer already had
    its one chance, recorded in `repair` by `stages.write_rubric`), are only listed under `bundled` with "warn", and
    are not checked with "off".
    """
    errs = validate_rubric(rubric, ledger, bundling=False) + validate_answers(answers, ledger)
    bundled = bundling_errors(rubric, ledger) if bundling != "off" else []
    if bundling == "repair":
        errs += bundled
    details = {"errors": errs, "n_criteria": len(rubric.criteria), "bundled": bundled, "repair": repair or {"ran": False}}
    return GateResult("rubric_trace", not errs, details)


def decontamination(texts: dict[str, str], index: BloomIndex | None, threshold: float) -> GateResult:
    if index is None:
        return GateResult("decontamination", True, {"skipped": "no reference_dirs configured"})
    scores = {name: round(index.containment(t), 3) for name, t in texts.items()}
    flagged = {k: v for k, v in scores.items() if v >= threshold}
    return GateResult("decontamination", not flagged, {"max": max(scores.values(), default=0.0), "flagged": flagged})


# ---------------------------------------------------------------- model-based


def _numbers(s) -> set[str]:
    return set(re.findall(r"\d+(?:\.\d+)?", str(s or "").replace(",", "")))


def _stated_change(ledger_value: str, found, descriptions: list[str]) -> bool:
    """An issue description in the document states the value found there: all of it, or every number it adds to the
    ledger value. s14-m0001's side letter reset a minimum commitment to 100,000 lbs, and its issue said "resets the
    Minimum Annual Commitment to 100,000 pounds", but the ledger writer listed only another fact in `contradicts`."""
    # ponytail: a changed number named by an issue in that document counts; a coincidental number there would pass too
    found_words, added = _words(_plain(found)), _numbers(found) - _numbers(ledger_value)
    return bool(found_words.strip()) and any(
        found_words in _words(_plain(d)) or (added and added <= _numbers(d)) for d in descriptions)


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
    # Each query names the instrument the fact belongs to: an NDA in the folder has its own "Effective Date", and
    # reading that as the supply agreement's Effective Date rejected a sound task (2026-10-18 pilot).
    owner = {d.id: f"{d.kind} ({d.filename})" for d in ledger.documents}
    planted = {(fid, fname.get(i.doc)) for i in ledger.issues for fid in i.contradicted()}
    # An issue whose own description quotes a fact's value, word for word, is about that fact in its document even
    # when the ledger writer left `contradicts` empty (round 9: an escrow agreement that cut the SPA's cap carve-outs).
    # Short values ("30 days") turn up in descriptions by chance, so only values of 5 words or more count.
    planted |= {(f.id, fname.get(i.doc)) for i in ledger.issues for f in ledger.facts
                if f.doc != i.doc and len(_words(_plain(f.value)).split()) >= 5 and _words(_plain(f.value)) in _words(_plain(i.description))}
    payload = {
        "documents": [{"filename": n, "content": c} for n, c in docs.items()],
        "queries": [{"id": f"{f.id}@{n}", "key": f.key, "of": owner[f.doc], "filename": n} for f in ledger.facts for n in docs],
    }
    out = call_json(client, "fact_extractor", prompts.FACT_EXTRACTOR, render_input(payload))
    got = {r["id"]: r.get("value") for r in out.get("facts", []) if "id" in r}
    # One long call misses values (a real run: 1 of 40 came back empty though its document stated it). Ask again,
    # focused, for each fact its own document seemed not to state; still without telling the extractor the value.
    retry = [{"id": f"{f.id}@{fname[f.doc]}", "key": f.key, "of": owner[f.doc], "filename": fname[f.doc]}
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
            if n == fname[f.doc] and _words(_plain(f.value)).strip() and _words(_plain(f.value)) in _words(_plain(v)):
                continue  # its own document states the value word for word, with drafting around it (a fallback court)
            if n == fname[f.doc] and _words(_plain(v)).strip() and _words(_plain(v)) in _words(_plain(f.value)) \
                    and _words(_plain(f.value)) in _words(_plain(docs[n])):
                continue  # the extractor trimmed it ("exclusive jurisdiction of" dropped, round 7); the text has it all
            # The extractor can drop a qualifier the document states ("exclusively" in a forum clause, 2026-11-02 pilot).
            # ponytail: 4+ words only, so a short value ("45 days") stated for something else in the document cannot pass
            if n == fname[f.doc] and len(_words(_plain(f.value)).split()) >= 4 and _words(_plain(f.value)) in _words(_plain(docs[n])):
                continue
            if n != fname[f.doc] and (not _norm(v) or (f.id, n) in planted):
                continue  # silent elsewhere, or a deliberate contradiction
            if n != fname[f.doc] and _stated_change(f.value, v, [i.description for i in ledger.issues if fname.get(i.doc) == n]):
                continue  # an issue in this document says it changes the value (a side letter's reset, round 14)
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
    # Whether an issue hurts the client depends on which side the client is on: a narrower indemnity carve-out
    # helps a supplier that gives most of the indemnities (round 5 planted one as a supplier's problem).
    party = {"name": ledger.parties[0].name, "role": ledger.parties[0].role}
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
        payload = {"client": party, "document": {"filename": fname[i.doc], "content": content}, "other_documents": others, "issue": issue}
        out = call_json(client, "issue_verifier", prompts.ISSUE_VERIFIER, render_input(payload))
        # The reason goes to gates.json too: round 12's s12-m0002 was rejected here and its grounds were not on disk.
        results.append({"issue": i.id, "present": bool(out.get("present")), "evidence": out.get("evidence", ""), "reason": out.get("reason", "")})
    missing = [r["issue"] for r in results if not r["present"]]
    return GateResult("issue_check", not missing, {"missing": missing, "results": results})


def rubric_tests(client: ModelClient, rubric: Rubric, answers: Answers) -> GateResult:
    """A rubric is code, so unit-test it: gold passes all, blank passes none, and the flawed answer fails
    exactly the criteria for the issue it omits (anything else it fails means a criterion is not specific)."""
    gold, gold_why = judge_with_reasons(client, answers.gold, rubric)
    blank = judge(client, "", rubric)
    flawed, flawed_why = judge_with_reasons(client, answers.flawed, rubric)

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
            # Why the judge failed gold or passed the flawed answer: round 13's gold failure (s13-m0001 C8) had none on disk.
            "judge_reasons": {"gold": {c: gold_why[c] for c in gold_fails}, "flawed": {c: flawed_why[c] for c in flawed_wrongly_passes}},
        },
    )


def solver_check(
    client: ModelClient,
    instruction: str,
    docs: Documents,
    rubric: Rubric,
    attempts: int,
    probe_without_documents: bool,
    max_steps: int = 20,
    page_chars: int = 6000,
    roles: tuple[str, ...] = ("solver",),
) -> tuple[GateResult, dict[str, list[Solution]]]:
    """Run tool-using solvers that never see the ledger. Returns the gate result and each role's attempts.

    Rejects only a leak: a task solved without opening any document. Each role in `roles` (routed to its own model
    by the config) makes `attempts` attempts; its pass rate is recorded under `difficulty` as a label, never judged
    (decision of 2026-11-04): a task every attempt passes is kept, and one no model passes at all is kept with
    `unsolved: true` so a person can check it is not broken.
    """
    solutions: dict[str, list[Solution]] = {}
    details: dict[str, Any] = {}

    if probe_without_documents:
        probe = solve(client, instruction, {}, max_steps, page_chars, roles[0])
        probe_grades = judge(client, probe.answer, rubric)
        details["probe_without_documents_passed"] = all(probe_grades.values())
        if details["probe_without_documents_passed"]:
            details["reason"] = "solved without opening any document: the instruction leaks the answer"
            return GateResult("solver_check", False, details), {roles[0]: [probe]}

    difficulty, runs = [], {}
    for role in roles:
        model = getattr(client, "model_for", lambda r: "")(role) or role
        runs[model], solutions[role] = [], []
        for _ in range(attempts):
            sol = solve(client, instruction, docs, max_steps, page_chars, role)
            grades = judge(client, sol.answer, rubric)
            solutions[role].append(sol)
            runs[model].append(
                {
                    "passed": all(grades.values()),
                    "failed_criteria": [c for c, ok in grades.items() if not ok],
                    "steps": len(sol.steps),
                    "files_opened": sol.files_opened(),
                }
            )
        passes = sum(r["passed"] for r in runs[model])
        difficulty.append({"model": model, "attempts": attempts, "passes": passes, "pass_rate": round(passes / max(attempts, 1), 3)})
    details.update({
        "pass_rate": difficulty[0]["pass_rate"],  # the default solver's, kept for older readers of gates.json
        "unsolved": not any(d["passes"] for d in difficulty),
        "difficulty": difficulty,
        "runs": runs,
    })
    return GateResult("solver_check", True, details), solutions
