"""Generation stages. Each function builds the payload its role is allowed to see.

Isolation, by construction:
  * instruction_writer never sees the issues, so it cannot leak them.
  * solver (ltg/solver.py) sees only the instruction and the documents, never the ledger or rubric.
  * judge sees only a response and the rubric.
"""

from __future__ import annotations

import random

from . import prompts
from .config import SpecCfg
from .models import ModelClient, call_json, call_text, render_input
from .schema import Answers, Ledger, MatterSpec, Rubric, validate_ledger
from .sources import Precedent
from .taxonomy import ISSUE_LIBRARY, PRACTICE_AREAS, WORK_TYPES, issue_types_for

Documents = dict[str, str]  # filename -> content


# ---------------------------------------------------------------- stage 1: plan


def sample_specs(cfg: SpecCfg, n: int, seed: int) -> list[MatterSpec]:
    """Matter spec sampler. Draws from our own taxonomy, never from a benchmark's task list."""
    r = random.Random(seed)
    specs = []
    for k in range(n):
        area = r.choice(cfg.practice_areas)
        work = r.choice(cfg.work_types)
        n_issues = r.randint(*cfg.n_issues)
        pool = issue_types_for(area)
        specs.append(
            MatterSpec(
                matter_id=f"s{seed}-m{k + 1:04d}",
                practice_area=area,
                agreement_type=r.choice(PRACTICE_AREAS[area]),
                work_type=work,
                jurisdiction=r.choice(cfg.jurisdictions),
                deliverable=WORK_TYPES[work],
                n_documents=r.randint(*cfg.n_documents),
                n_issues=n_issues,
                issue_types=r.sample(pool, min(n_issues, len(pool))),
                seed=seed,
            )
        )
    return specs


def write_ledger(client: ModelClient, spec: MatterSpec, precedents: list[Precedent], precedent_chars: int) -> Ledger:
    payload = {
        "spec": spec.to_dict(),
        "issue_types": [{"type": t, "label": ISSUE_LIBRARY[t]["label"], "description": ISSUE_LIBRARY[t]["description"]} for t in spec.issue_types],
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
        }
        docs[d.filename] = call_text(client, "drafter", prompts.DRAFTER, render_input(payload))
    return docs


def write_instruction(client: ModelClient, spec: MatterSpec, ledger: Ledger) -> str:
    client_party = ledger.parties[0]
    payload = {
        "matter": {
            "client": client_party.name,
            "client_role": client_party.role,
            "counterparties": [p.name for p in ledger.parties[1:]],
            "practice_area": spec.practice_area,
            "agreement_type": spec.agreement_type,
            "jurisdiction": spec.jurisdiction,
            "deliverable": spec.deliverable,
        },
        "files": [{"filename": d.filename, "kind": d.kind} for d in ledger.documents],
    }
    return call_json(client, "instruction_writer", prompts.INSTRUCTION_WRITER, render_input(payload)).get("instruction", "")


def write_rubric(client: ModelClient, spec: MatterSpec, ledger: Ledger, instruction: str) -> Rubric:
    payload = {"ledger": ledger.to_dict(), "instruction": instruction, "deliverable": spec.deliverable}
    return Rubric.from_dict(call_json(client, "rubric_writer", prompts.RUBRIC_WRITER, render_input(payload)))


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
    payload = {
        "response": response,
        "criteria": [{"id": c.id, "text": c.text, "kind": c.kind, **({"grading_hints": c.hints} if c.hints else {})} for c in rubric.criteria],
    }
    out = call_json(client, "judge", prompts.JUDGE, render_input(payload))
    got = {r["id"]: bool(r.get("pass")) for r in out.get("results", []) if "id" in r}
    return {c.id: got.get(c.id, False) for c in rubric.criteria}  # a criterion the judge skipped counts as failed

