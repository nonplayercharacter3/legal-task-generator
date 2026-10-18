"""Data shapes that pass between stages.

Everything is plain JSON on disk, so any stage can be rerun or inspected by hand.
Validation returns a list of human-readable errors; an empty list means valid.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any

_SAFE_FILENAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,120}$")


def _pick(cls, d: dict[str, Any]):
    """Build a dataclass from a dict, ignoring extra keys a model may add."""
    names = cls.__dataclass_fields__.keys()
    return cls(**{k: v for k, v in d.items() if k in names})


@dataclass
class MatterSpec:
    matter_id: str
    practice_area: str
    agreement_type: str
    work_type: str
    jurisdiction: str
    deliverable: str
    n_documents: int
    n_issues: int
    issue_types: list[str]
    seed: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "MatterSpec":
        return cls(**d)


@dataclass
class Party:
    id: str
    name: str
    role: str


@dataclass
class Fact:
    """A fact that must read the same in every document that states it."""

    id: str
    key: str  # human label, e.g. "Closing Date"
    value: str
    doc: str  # DocumentPlan.id where it is stated
    section: str


@dataclass
class DocumentPlan:
    id: str
    filename: str
    kind: str  # e.g. "main agreement", "amendment", "email"
    distractor: bool = False
    precedent: str | None = None  # id of the precedent it adapts, if any


@dataclass
class Issue:
    """A planted problem. The rubric is written from these, never from the documents."""

    id: str
    type: str  # key into taxonomy.ISSUE_LIBRARY
    label: str
    description: str
    doc: str
    section: str
    detect_terms: list[str]
    expected_finding: str
    contradicts: str | None = None  # fact id this issue deliberately states differently in its document


@dataclass
class Ledger:
    matter_id: str
    summary: str
    parties: list[Party]
    facts: list[Fact]
    documents: list[DocumentPlan]
    issues: list[Issue]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Ledger":
        return cls(
            matter_id=d["matter_id"],
            summary=d.get("summary", ""),
            parties=[_pick(Party, p) for p in d.get("parties", [])],
            facts=[_pick(Fact, f) for f in d.get("facts", [])],
            documents=[_pick(DocumentPlan, x) for x in d.get("documents", [])],
            issues=[_pick(Issue, i) for i in d.get("issues", [])],
        )

    def doc_by_id(self, doc_id: str) -> DocumentPlan | None:
        return next((d for d in self.documents if d.id == doc_id), None)

    def ids(self) -> set[str]:
        return {x.id for x in [*self.parties, *self.facts, *self.documents, *self.issues]}


CRITERION_KINDS = ("issue", "fact", "format", "negative")
MAX_FACT_WORDS = 20


@dataclass
class Criterion:
    id: str
    text: str
    kind: str  # one of CRITERION_KINDS
    source: str | None = None  # ledger id for "issue" and "fact"; None otherwise
    hints: list[str] = field(default_factory=list)  # grading hints for the judge


@dataclass
class Rubric:
    criteria: list[Criterion]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Rubric":
        return cls(criteria=[_pick(Criterion, c) for c in d.get("criteria", [])])


@dataclass
class Answers:
    gold: str
    flawed: str
    flawed_omits: list[str]  # issue ids the flawed answer deliberately misses

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------- validation


def _dupes(ids: list[str]) -> list[str]:
    seen, out = set(), []
    for i in ids:
        if i in seen:
            out.append(i)
        seen.add(i)
    return out


def validate_ledger(ledger: Ledger, spec: MatterSpec) -> list[str]:
    errs: list[str] = []
    all_ids = [x.id for x in [*ledger.parties, *ledger.facts, *ledger.documents, *ledger.issues]]
    for d in _dupes(all_ids):
        errs.append(f"duplicate id {d}")

    doc_ids = {d.id for d in ledger.documents}
    filenames = [d.filename for d in ledger.documents]
    for f in _dupes(filenames):
        errs.append(f"duplicate filename {f}")
    for f in filenames:
        if not _SAFE_FILENAME.match(f):
            errs.append(f"unsafe filename {f!r} (use letters, digits, '.', '_' and '-')")
    if len(ledger.documents) != spec.n_documents:
        errs.append(f"expected {spec.n_documents} documents, got {len(ledger.documents)}")
    if len(ledger.issues) != spec.n_issues:
        errs.append(f"expected {spec.n_issues} issues, got {len(ledger.issues)}")
    if spec.n_documents >= 3 and not any(d.distractor for d in ledger.documents):
        errs.append("no distractor document")
    if len(ledger.parties) < 2:
        errs.append("fewer than two parties")
    if not ledger.facts:
        errs.append("no facts")

    for f in ledger.facts:
        if f.doc not in doc_ids:
            errs.append(f"fact {f.id} points to unknown document {f.doc}")
        if not str(f.value).strip():
            errs.append(f"fact {f.id} has an empty value")
        elif len(str(f.value).split()) > MAX_FACT_WORDS:  # a clause, not a value: extraction and matching break
            errs.append(f"fact {f.id} is {len(str(f.value).split())} words; make it one short value (at most {MAX_FACT_WORDS} words) and split compound facts")

    issue_docs = set()
    for i in ledger.issues:
        doc = ledger.doc_by_id(i.doc)
        if doc is None:
            errs.append(f"issue {i.id} points to unknown document {i.doc}")
        elif doc.distractor:
            errs.append(f"issue {i.id} is planted in distractor document {i.doc}")
        if i.type not in spec.issue_types:
            errs.append(f"issue {i.id} has type {i.type!r}, not one requested by the spec")
        if not i.detect_terms:
            errs.append(f"issue {i.id} has no detect_terms")
        if not i.expected_finding.strip():
            errs.append(f"issue {i.id} has no expected_finding")
        fact = next((f for f in ledger.facts if f.id == i.contradicts), None)
        if i.contradicts and fact is None:
            errs.append(f"issue {i.id} contradicts unknown fact {i.contradicts}")
        elif fact and fact.doc == i.doc:
            errs.append(f"issue {i.id} contradicts {fact.id} inside {fact.doc}, the document that states it; "
                        "a contradiction needs the fact stated in a different document, otherwise set contradicts to null")
        issue_docs.add(i.doc)
    if spec.n_issues >= 2 and len(issue_docs) < 2:
        errs.append("all issues sit in one document; spread them across documents")
    return errs


def _words(s: str) -> str:
    return " " + " ".join(re.findall(r"[a-z0-9]+", s.lower())) + " "


def validate_rubric(rubric: Rubric, ledger: Ledger) -> list[str]:
    """Every criterion must trace back to the ledger, and every issue must be graded."""
    errs: list[str] = []
    for d in _dupes([c.id for c in rubric.criteria]):
        errs.append(f"duplicate criterion id {d}")
    issue_ids = {i.id for i in ledger.issues}
    fact_ids = {f.id for f in ledger.facts}
    for c in rubric.criteria:
        if not c.text.strip():
            errs.append(f"criterion {c.id} has no text")
        if c.kind not in CRITERION_KINDS:
            errs.append(f"criterion {c.id} has unknown kind {c.kind!r}")
        elif c.kind == "issue" and c.source not in issue_ids:
            errs.append(f"criterion {c.id} cites {c.source!r}, which is not a ledger issue")
        elif c.kind == "fact" and c.source not in fact_ids:
            errs.append(f"criterion {c.id} cites {c.source!r}, which is not a ledger fact")
    # A negative criterion about a distractor punishes thoroughness: real documents always hold points a careful
    # reviewer may raise, and the ledger cannot say they are wrong (the 2026-10-18 pilot lost two tasks this way).
    for c in rubric.criteria:
        if c.kind != "negative":
            continue
        for d in ledger.documents:
            names = {_words(d.filename.rsplit(".", 1)[0]), _words(d.kind.split("(")[0])}
            if d.distractor and any(n.strip() and n in _words(c.text) for n in names):
                errs.append(f"negative criterion {c.id} is about distractor {d.id}; grade only wrong conclusions")
    graded = {c.source for c in rubric.criteria if c.kind == "issue"}
    for missing in sorted(issue_ids - graded):
        errs.append(f"issue {missing} has no criterion")
    return errs


def validate_answers(answers: Answers, ledger: Ledger) -> list[str]:
    errs: list[str] = []
    issue_ids = {i.id for i in ledger.issues}
    if not answers.gold.strip():
        errs.append("empty gold answer")
    if not answers.flawed.strip():
        errs.append("empty flawed answer")
    if not answers.flawed_omits:
        errs.append("flawed answer omits no issue")
    for i in answers.flawed_omits:
        if i not in issue_ids:
            errs.append(f"flawed_omits names unknown issue {i}")
    return errs
