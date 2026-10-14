"""A deterministic, offline stand-in for a language model.

It reads the same structured payload a real model would receive (the <input> block)
and returns plausible JSON for each role, so the whole pipeline, including every
gate, can run and be tested without any API.

It can also inject faults on purpose, to prove each gate rejects what it should:
  drop_issue             drafter leaves a planted issue out       -> issue_check fails
  wrong_fact             drafter misstates a ledger fact          -> consistency fails
  untraceable_criterion  rubric cites an id not in the ledger     -> rubric_trace fails
  weak_gold              gold answer misses an issue              -> rubric_tests fails

Its "legal knowledge" is the issue library's detect_terms, so the fake solver finds
an issue by spotting those phrases, with probability `solver_skill` per issue.
"""

from __future__ import annotations

import hashlib
import json
import random
import re
from typing import Any

from .models import CallLog, CallRecord, extract_input
from .taxonomy import ISSUE_LIBRARY

FAULTS = ("drop_issue", "wrong_fact", "untraceable_criterion", "weak_gold")

COMPANY_NAMES = [
    "Halvorsen Industrial Supply Co.",
    "Brightwater Analytics, Inc.",
    "Copperline Foods LLC",
    "Northgate Robotics Corp.",
    "Meridian Orchard Holdings, Inc.",
    "Tallis & Reed Logistics LLC",
    "Saffron Peak Software, Inc.",
    "Ironbridge Medical Devices Corp.",
    "Larkspur Renewable Materials LLC",
    "Quillon Freight Systems, Inc.",
]

BOILERPLATE = [
    "Each party shall perform its obligations in a professional and workmanlike manner consistent with industry practice.",
    "Headings are for convenience only and do not affect the interpretation of this document.",
    "This document may be executed in counterparts, each of which is deemed an original.",
    "The parties shall cooperate in good faith to give effect to the purposes of this document.",
    "Invoices are payable in United States dollars by wire transfer to the account designated by the payee.",
]

DISTRACTOR_TEXT = [
    "Thanks for sending the updated delivery schedule. Our team will confirm the loading dock hours by Friday.",
    "Attached are the minutes from the quarterly operations review. Attendance and action items are listed below.",
    "Reminder that the office will be closed on the holiday. Please route urgent shipping questions to the duty manager.",
    "The parking validation process has changed; visitors should check in at the front desk on arrival.",
]


def _rng(*parts: Any) -> random.Random:
    h = hashlib.sha256("|".join(str(p) for p in parts).encode()).hexdigest()
    return random.Random(int(h[:16], 16))


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


class FakeModel:
    def __init__(
        self,
        seed: int = 0,
        solver_skill: float = 0.85,
        fault: str = "",
        fault_rate: float = 0.0,
        log: CallLog | None = None,
    ) -> None:
        if fault and fault not in FAULTS:
            raise ValueError(f"unknown fault {fault!r}; choose from {FAULTS}")
        self.seed = seed
        self.solver_skill = solver_skill
        self.fault = fault
        self.fault_rate = fault_rate
        self.log = log if log is not None else CallLog()
        self._solver_attempts: dict[str, int] = {}

    # ------------------------------------------------------------ plumbing

    def fault_for(self, matter_id: str) -> str:
        if self.fault:
            return self.fault
        if self.fault_rate > 0:
            r = _rng(self.seed, "fault", matter_id)
            if r.random() < self.fault_rate:
                return r.choice(FAULTS)
        return ""

    def complete(self, role: str, system: str, user: str) -> str:
        payload = extract_input(user)
        handler = getattr(self, f"_{role}", None)
        if handler is None:
            raise ValueError(f"FakeModel has no behaviour for role {role!r}")
        out = json.dumps(handler(payload))
        self.log.add(
            CallRecord(
                role=role,
                model="fake",
                seconds=0.0,
                input_tokens=(len(system) + len(user)) // 4,
                output_tokens=len(out) // 4,
            )
        )
        return out

    # ------------------------------------------------------------ roles

    def _ledger_writer(self, p: dict) -> dict:
        spec = p["spec"]
        r = _rng(self.seed, "ledger", spec["matter_id"])
        client, counterparty = r.sample(COMPANY_NAMES, 2)
        is_ma = spec["practice_area"] == "mergers_acquisitions"
        roles = ("Buyer", "Seller") if is_ma else ("Customer", "Supplier")

        n_docs = spec["n_documents"]
        n_distractors = 1 if n_docs >= 3 else 0
        precedent_id = p["precedents"][0]["id"] if p.get("precedents") else None
        documents = [
            {
                "id": "D1",
                "filename": _slug(spec["agreement_type"]) + ".md",
                "kind": "main agreement",
                "distractor": False,
                "precedent": precedent_id,
            }
        ]
        support = ["amendment", "disclosure schedule", "side letter", "board consent"]
        for k in range(n_docs - 1 - n_distractors):
            kind = support[k % len(support)]
            documents.append({"id": f"D{len(documents) + 1}", "filename": f"{_slug(kind)}_{k + 1}.md", "kind": kind, "distractor": False, "precedent": None})
        for k in range(n_distractors):
            kind = ["email thread", "meeting notes"][k % 2]
            documents.append({"id": f"D{len(documents) + 1}", "filename": f"{_slug(kind)}.md", "kind": kind, "distractor": True, "precedent": None})

        year = 2025 + r.randint(0, 1)
        amount = r.randint(12, 95) * 100_000
        facts = [
            {"id": "F1", "key": "Effective Date", "value": f"{year}-0{r.randint(1, 9)}-1{r.randint(0, 9)}", "doc": "D1", "section": "1.1"},
            {"id": "F2", "key": "Purchase Price" if is_ma else "Annual Fee", "value": f"${amount:,}", "doc": "D1", "section": "3.1"},
            {"id": "F3", "key": "Governing Law", "value": f"State of {spec['jurisdiction']}", "doc": "D1", "section": "12.1"},
            {"id": "F4", "key": "Liability Cap", "value": f"${amount // 2:,}", "doc": "D1", "section": "9.1"},
            {"id": "F5", "key": "Initial Term", "value": f"{r.randint(2, 5)} years", "doc": "D1", "section": "2.1"},
        ]
        if len(documents) > 1 and not documents[1]["distractor"]:
            facts.append({"id": "F6", "key": "Amendment Date", "value": f"{year + 1}-0{r.randint(1, 9)}-0{r.randint(1, 9)}", "doc": "D2", "section": "1"})

        live_docs = [d["id"] for d in documents if not d["distractor"]]
        issues = []
        for idx, itype in enumerate(spec["issue_types"]):
            lib = ISSUE_LIBRARY[itype]
            issues.append(
                {
                    "id": f"I{idx + 1}",
                    "type": itype,
                    "label": lib["label"],
                    "description": lib["description"],
                    "doc": live_docs[idx % len(live_docs)],
                    "section": f"{idx + 5}.2",
                    "detect_terms": list(lib["detect_terms"]),
                    "expected_finding": lib["finding"],
                }
            )
        return {
            "matter_id": spec["matter_id"],
            "summary": f"{client} is party to a {spec['agreement_type']} with {counterparty}.",
            "parties": [
                {"id": "P1", "name": client, "role": roles[0]},
                {"id": "P2", "name": counterparty, "role": roles[1]},
            ],
            "facts": facts,
            "documents": documents,
            "issues": issues,
        }

    def _drafter(self, p: dict) -> dict:
        ledger, doc = p["ledger"], p["document"]
        fault = self.fault_for(ledger["matter_id"])
        r = _rng(self.seed, "draft", ledger["matter_id"], doc["id"])
        parties = ledger["parties"]
        title = doc["kind"].title()
        lines = [f"# {title}", "", f"**Between** {parties[0]['name']} (\"{parties[0]['role']}\") and {parties[1]['name']} (\"{parties[1]['role']}\")", ""]
        if doc.get("precedent"):
            lines += [f"<!-- structure adapted from precedent {doc['precedent']} -->", ""]

        if doc["distractor"]:
            lines += r.sample(DISTRACTOR_TEXT, 2)
            return {"filename": doc["filename"], "content": "\n\n".join(lines) + "\n"}

        facts = [f for f in ledger["facts"] if f["doc"] == doc["id"]]
        issues = [i for i in ledger["issues"] if i["doc"] == doc["id"]]
        if fault == "drop_issue" and issues and issues[0]["id"] == ledger["issues"][0]["id"]:
            issues = issues[1:]
        first_fact = ledger["facts"][0]["id"]

        for f in facts:
            value = f["value"]
            if fault == "wrong_fact" and f["id"] == first_fact:
                value = "to be confirmed"
            lines += [f"## {f['section']}. {f['key']}", "", f"{f['key']}: {value}", "", r.choice(BOILERPLATE), ""]
        for i in issues:
            lines += [f"## {i['section']}. General Provisions", "", ISSUE_LIBRARY[i["type"]]["planted_text"], "", r.choice(BOILERPLATE), ""]
        return {"filename": doc["filename"], "content": "\n".join(lines)}

    def _fact_extractor(self, p: dict) -> dict:
        docs = {d["filename"]: d["content"] for d in p["documents"]}
        out = []
        for q in p["queries"]:
            content = docs.get(q["filename"], "")
            m = re.search(rf"^{re.escape(q['key'])}: (.+)$", content, re.M)
            out.append({"id": q["id"], "value": m.group(1).strip() if m else None})
        return {"facts": out}

    def _issue_verifier(self, p: dict) -> dict:
        content = p["document"]["content"]
        terms = p["issue"].get("detect_terms", [])
        present = bool(terms) and all(t.lower() in content.lower() for t in terms)
        evidence = next((ln for ln in content.splitlines() if terms and terms[0].lower() in ln.lower()), "")
        return {"present": present, "evidence": evidence, "reason": "all detect terms found" if present else "detect terms missing"}

    def _instruction_writer(self, p: dict) -> dict:
        m, files = p["matter"], p["files"]
        listing = ", ".join(f["filename"] for f in files)
        text = (
            f"Our client, {m['client']}, is reviewing its {m['agreement_type']} ahead of a board meeting next week "
            f"and wants to know where it stands. The matter folder has {len(files)} files ({listing}). "
            f"Please review all of them under {m['jurisdiction']} law and prepare {m['deliverable']}. "
            "Keep it practical: the client needs to decide what to raise with the counterparty."
        )
        return {"instruction": text}

    def _rubric_writer(self, p: dict) -> dict:
        ledger = p["ledger"]
        fault = self.fault_for(ledger["matter_id"])
        crit = []
        for i in ledger["issues"]:
            crit.append({"id": f"C{len(crit) + 1}", "kind": "issue", "source": i["id"], "text": f"Identifies that {i['expected_finding']}.", "hints": list(i["detect_terms"])})
        for f in ledger["facts"][:2]:
            crit.append({"id": f"C{len(crit) + 1}", "kind": "fact", "source": f["id"], "text": f"States the {f['key']} as {f['value']}.", "hints": [f["value"]]})
        crit.append({"id": f"C{len(crit) + 1}", "kind": "format", "source": None, "text": "Cites the document and section for each issue identified.", "hints": ["section"]})
        crit.append({"id": f"C{len(crit) + 1}", "kind": "negative", "source": None, "text": "Does not cite case law or statutes that do not appear in the matter documents.", "hints": []})
        if fault == "untraceable_criterion":
            crit.append({"id": f"C{len(crit) + 1}", "kind": "issue", "source": "I99", "text": "Identifies the missing escrow provision.", "hints": ["escrow"]})
        return {"criteria": crit}

    def _answer_writer(self, p: dict) -> dict:
        ledger = p["ledger"]
        fault = self.fault_for(ledger["matter_id"])
        docs = {d["filename"]: d["content"] for d in p["documents"]}
        fname = {d["id"]: d["filename"] for d in ledger["documents"]}

        def finding(i: dict) -> str:
            content = docs.get(fname[i["doc"]], "")
            quote = next((ln for ln in content.splitlines() if i["detect_terms"][0].lower() in ln.lower()), "; ".join(i["detect_terms"]))
            return f"- {fname[i['doc']]}, Section {i['section']}: {i['expected_finding']}. The clause reads: \"{quote}\""

        facts = "\n".join(f"- {f['key']}: {f['value']}" for f in ledger["facts"])
        issues = ledger["issues"]
        gold_issues = issues[1:] if fault == "weak_gold" else issues
        gold = "MEMORANDUM\n\nIssues identified:\n" + "\n".join(finding(i) for i in gold_issues) + "\n\nKey facts:\n" + facts
        omit = issues[-1]
        flawed = "MEMORANDUM\n\nIssues identified:\n" + "\n".join(finding(i) for i in issues if i["id"] != omit["id"]) + "\n\nKey facts:\n" + facts
        return {"gold": gold, "flawed": flawed, "flawed_omits": [omit["id"]]}

    def _judge(self, p: dict) -> dict:
        resp = p["response"]
        low = resp.lower()
        results = []
        for c in p["criteria"]:
            if c["kind"] == "negative":
                ok = not re.search(r"\bv\.\s|U\.S\.C\.|F\.\s?\d?d\b", resp)
            else:
                hints = c.get("grading_hints") or []
                ok = bool(resp.strip()) and bool(hints) and all(h.lower() in low for h in hints)
            results.append({"id": c["id"], "pass": ok, "reason": "hint match" if ok else "missing"})
        return {"results": results}

    def _solver(self, p: dict) -> dict:
        key = p["instruction"] + "|" + str(len(p["documents"]))
        attempt = self._solver_attempts.get(key, 0)
        self._solver_attempts[key] = attempt + 1
        if not p["documents"]:
            return {"answer": "I cannot assess the agreement without the documents in the matter folder."}
        r = _rng(self.seed, "solve", key, attempt)

        findings, facts = [], []
        for d in p["documents"]:
            section = "?"
            for ln in d["content"].splitlines():
                head = re.match(r"^##\s+([\d.]+)\.", ln)
                if head:
                    section = head.group(1)
                    continue
                fm = re.match(r"^([A-Z][A-Za-z ]+): (.+)$", ln)
                if fm:
                    facts.append(f"- {fm.group(1)}: {fm.group(2)}")
                for itype, lib in ISSUE_LIBRARY.items():
                    if all(t.lower() in ln.lower() for t in lib["detect_terms"]) and r.random() < self.solver_skill:
                        findings.append(f"- {d['filename']}, Section {section}: this clause is a problem for the client: \"{ln}\"")
        answer = "MEMORANDUM\n\nIssues identified:\n" + ("\n".join(findings) or "- None found.") + "\n\nKey facts:\n" + "\n".join(facts)
        return {"answer": answer}
