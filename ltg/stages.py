"""Generation stages. Each function builds the payload its role is allowed to see.

Isolation, by construction:
  * instruction_writer never sees the issues, so it cannot leak them.
  * solver (ltg/solver.py) sees only the instruction and the documents, never the ledger or rubric.
  * judge sees only a response and the rubric.
"""

from __future__ import annotations

import math
import random

from . import prompts
from .config import SpecCfg
from .models import ModelClient, call_json, call_text, render_input
from .schema import Answers, Ledger, MatterSpec, Rubric, bundling_errors, split_issue_errors, validate_instruction, validate_ledger, validate_rubric
from .sources import Precedent
from .taxonomy import (
    DISTRACTOR_KINDS,
    INDUSTRIES,
    ISSUE_LIBRARY,
    OVERUSED_NAMES,
    PRACTICE_AREAS,
    SUPPORTING_KINDS,
    WORK_TYPES,
    issue_types_for,
    name_stem,
)

Documents = dict[str, str]  # filename -> content


# ---------------------------------------------------------------- stage 1: plan


def sample_specs(cfg: SpecCfg, n: int, seed: int, used_industries: dict[str, int] | None = None) -> list[MatterSpec]:
    """Matter spec sampler. Draws from our own taxonomy, never from a benchmark's task list.

    `used_industries` counts industries earlier runs used: the least used come first, so a night of rounds does not
    repeat one before all are used (elevator maintenance came up 3 times in rounds 20 to 27)."""
    r = random.Random(seed)
    specs = []
    used_issues: dict[str, int] = {}
    used_stems: set[str] = set()
    industries = r.sample(INDUSTRIES, len(INDUSTRIES))  # every industry once before any repeats
    industries.sort(key=lambda i: (used_industries or {}).get(i, 0))  # stable: no history keeps the seed's order
    for k in range(n):
        area = r.choice(cfg.practice_areas)
        work = r.choice(cfg.work_types)
        n_issues = r.randint(*cfg.n_issues)
        n_docs = r.randint(*cfg.n_documents)
        issue_types = _balanced_sample(r, issue_types_for(area), n_issues, used_issues)
        stems = []
        while len(stems) < 2:
            s = name_stem(r)
            if s not in used_stems:
                used_stems.add(s)
                stems.append(s)
        n_dis = min(cfg.min_distractors, n_docs - 1) if n_docs >= 3 else 0
        n_support = max(n_docs - 1 - n_dis, 0)  # the rest: main agreement and the distractors
        specs.append(
            MatterSpec(
                matter_id=f"s{seed}-m{k + 1:04d}",
                practice_area=area,
                agreement_type=r.choice(PRACTICE_AREAS[area]),
                work_type=work,
                jurisdiction=r.choice(cfg.jurisdictions),
                deliverable=WORK_TYPES[work],
                n_documents=n_docs,
                n_issues=n_issues,
                issue_types=issue_types,
                seed=seed,
                industry=industries[k % len(industries)],
                name_stems=stems,
                supporting_kinds=r.sample(SUPPORTING_KINDS[area], min(n_support, len(SUPPORTING_KINDS[area]))),
                distractor_kind=r.choice(DISTRACTOR_KINDS) if n_docs >= 3 else "",
                min_distractors=max(n_dis, 1) if n_docs >= 3 else 1,
                n_cross_document=min(math.ceil(cfg.cross_document_share * n_issues), n_issues) if n_docs >= 2 else 0,
            )
        )
    return specs


def _balanced_sample(r: random.Random, pool: list[str], k: int, used: dict[str, int]) -> list[str]:
    """Pick k issue types without repeats, favouring types used less often earlier in the run."""
    picked, left = [], list(pool)
    for _ in range(min(k, len(left))):
        t = r.choices(left, weights=[1 / (1 + used.get(x, 0)) ** 2 for x in left])[0]
        picked.append(t)
        left.remove(t)
        used[t] = used.get(t, 0) + 1
    return picked


def write_ledger(client: ModelClient, spec: MatterSpec, precedents: list[Precedent], precedent_chars: int) -> Ledger:
    payload = {
        "spec": spec.to_dict(),
        "issue_types": [{"type": t, "label": ISSUE_LIBRARY[t]["label"], "description": ISSUE_LIBRARY[t]["description"]} for t in spec.issue_types],
        "avoid_names": OVERUSED_NAMES,
        "precedents": [{"id": p.id, "title": p.title, "excerpt": p.excerpt(min(precedent_chars, 2000))} for p in precedents],
    }
    user = render_input(payload)
    ledger = Ledger.from_dict(call_json(client, "ledger_writer", prompts.LEDGER_WRITER, user))
    errs = validate_ledger(ledger, spec)
    if errs:  # one repair attempt with the validator's complaints
        repair = user + "\n\nYour previous ledger had these problems; fix all of them:\n- " + "\n- ".join(errs)
        ledger = Ledger.from_dict(call_json(client, "ledger_writer", prompts.LEDGER_WRITER, repair))
    ledger.matter_id = spec.matter_id
    return ledger


# ---------------------------------------------------------------- stage 2: build


def draft_documents(client: ModelClient, ledger: Ledger, precedents: dict[str, Precedent], precedent_chars: int) -> Documents:
    docs: Documents = {}
    for d in ledger.documents:
        prec = precedents.get(d.precedent or "")
        payload = {
            "ledger": ledger.to_dict(),
            "document": {"id": d.id, "filename": d.filename, "kind": d.kind, "distractor": d.distractor, "precedent": d.precedent},
            "precedent": {"id": prec.id, "title": prec.title, "text": prec.excerpt(precedent_chars)} if prec else None,
            # earlier drafts, so cross-references, part numbers and defined terms stay consistent across the folder
            "drafted": [{"filename": n, "content": c} for n, c in docs.items()],
        }
        docs[d.filename] = call_text(client, "drafter", prompts.DRAFTER, render_input(payload))
    return docs


def write_instruction(client: ModelClient, spec: MatterSpec, ledger: Ledger, name_files: bool = True, max_words: int = 0) -> str:
    client_party = ledger.parties[0]
    payload = {
        "matter": {
            "client": client_party.name,
            "client_role": client_party.role,
            # Only the deal's counterparty (P2, by the name-stem rule): every other ledger party was listed as
            # "involved", including a non-party licensor and the buyer in a planted issue (s16-m0003, s25-m0001).
            "counterparty": ledger.parties[1].name if len(ledger.parties) > 1 else "",
            "practice_area": spec.practice_area,
            "agreement_type": spec.agreement_type,
            "deliverable": spec.deliverable,
        },
        "files": [{"filename": d.filename, "kind": d.kind} for d in ledger.documents],
    }
    if not name_files:  # the writer gets no file names to repeat
        payload["files"] = len(ledger.documents)
        payload["name_no_file"] = True
    if max_words:
        payload["max_words"] = max_words
    user = render_input(payload)
    text = call_json(client, "instruction_writer", prompts.INSTRUCTION_WRITER, user).get("instruction", "")
    errs = validate_instruction(text, ledger, name_files, max_words)
    if errs:  # one repair attempt; leak_check rejects what is still wrong
        repair = user + "\n\nYour previous instruction had these problems; fix all of them:\n- " + "\n- ".join(errs)
        text = call_json(client, "instruction_writer", prompts.INSTRUCTION_WRITER, repair).get("instruction", "")
    return text


def write_rubric(client: ModelClient, spec: MatterSpec, ledger: Ledger, instruction: str, bundling: str = "warn") -> tuple[Rubric, dict]:
    """The rubric, and what was done about bundled issue criteria (`gates.check_bundling`).

    With `bundling == "repair"`, a rubric whose only faults are clauses demanding a harm, remedy or provision the
    expected finding does not name goes back to its writer once, with those clauses, for a corrected rubric. Past
    rubrics show this is common in sound tasks (6 of 9 accepted matters), so it is repaired, not rejected; the gate
    rejects only if the correction still fails. Any other fault skips the repair and rejects at `rubric_trace`.
    """
    payload = {"ledger": ledger.to_dict(), "instruction": instruction, "deliverable": spec.deliverable}
    rubric = Rubric.from_dict(call_json(client, "rubric_writer", prompts.RUBRIC_WRITER, render_input(payload)))
    repair: dict = {"ran": False}
    split = split_issue_errors(rubric, ledger)
    flagged = split + (bundling_errors(rubric, ledger) if bundling == "repair" else [])
    if flagged and not validate_rubric(rubric, ledger, bundling=False):
        again = {**payload, "previous_rubric": rubric.to_dict(), "problems": flagged,
                 "task": "Your previous rubric is attached. Fix only the criteria listed under problems: keep the finding and "
                         "where it is, and ask that the response explains why the issue matters and recommends a fix, without "
                         "naming the harm, the remedy or a supporting provision. An issue with several criteria gets ONE: merge its parts "
                         "(finding, where, why it matters, fix) into a single criterion. Return the whole corrected rubric."}
        rubric = Rubric.from_dict(call_json(client, "rubric_writer", prompts.RUBRIC_WRITER, render_input(again)))
        repair = {"ran": True, "flagged": flagged, "cleared": not split_issue_errors(rubric, ledger) and not (bundling_errors(rubric, ledger) if bundling == "repair" else [])}
    return rubric, repair


def write_answers(client: ModelClient, ledger: Ledger, instruction: str, rubric: Rubric, docs: Documents, omit: str) -> Answers:
    """Gold and flawed answers, one call each. The pipeline picks the omitted issue, so it is always a real id."""
    payload = {
        "ledger": ledger.to_dict(),
        "instruction": instruction,
        "rubric": rubric.to_dict(),
        "documents": [{"filename": f, "content": c} for f, c in docs.items()],
    }
    gold = call_text(client, "answer_writer", prompts.ANSWER_WRITER, render_input({**payload, "write": "gold"}))
    flawed = call_text(client, "answer_writer", prompts.ANSWER_WRITER, render_input({**payload, "write": "flawed", "omit_issue": omit}))
    return Answers(gold=gold, flawed=flawed, flawed_omits=[omit])


# ---------------------------------------------------------------- used by gates


def judge(client: ModelClient, response: str, rubric: Rubric) -> dict[str, bool]:
    return judge_with_reasons(client, response, rubric)[0]


def judge_with_reasons(client: ModelClient, response: str, rubric: Rubric) -> tuple[dict[str, bool], dict[str, str]]:
    """Each criterion's grade, and the judge's reason for it ("" when it gave none)."""
    payload = {
        "response": response,
        "criteria": [{"id": c.id, "text": c.text, "kind": c.kind, **({"grading_hints": c.hints} if c.hints else {})} for c in rubric.criteria],
    }
    out = call_json(client, "judge", prompts.JUDGE, render_input(payload))
    rows = [r for r in out.get("results", []) if "id" in r]
    negative = {c.id for c in rubric.criteria if c.kind == "negative"}
    # Round 15: the judge set `pass` on a negative criterion against its own reason ("does not make this claim").
    # It now reports only whether the claim is made, and code turns that into the grade; no `claim_made` fails.
    got = {r["id"]: r.get("claim_made") is False if r["id"] in negative else bool(r.get("pass")) for r in rows}
    why = {r["id"]: str(r.get("reason") or "") + (" (no claim_made in the judge's reply)" if r["id"] in negative and "claim_made" not in r else "") for r in rows}
    grades = {c.id: got.get(c.id, False) for c in rubric.criteria}  # a criterion the judge skipped counts as failed
    return grades, {c.id: why.get(c.id, "skipped by the judge" if c.id not in got else "") for c in rubric.criteria}

