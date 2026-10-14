"""Our own task taxonomy and issue library.

This is deliberately NOT LAB's list of practice areas or its rubric wording. It is a
starting point for contract review only.

DRAFT: the issue library has not been reviewed by anyone with legal training. Every
entry should be approved (or rewritten) by a lawyer before generated tasks are used
for training. `planted_text` is used only by the fake model; real models draft their own.
"""

from __future__ import annotations

PRACTICE_AREAS: dict[str, list[str]] = {
    "commercial_contracts": [
        "supply agreement",
        "master services agreement",
        "software license agreement",
        "distribution agreement",
    ],
    "mergers_acquisitions": [
        "stock purchase agreement",
        "asset purchase agreement",
    ],
}

WORK_TYPES: dict[str, str] = {
    "issue_spotting_memo": (
        "a memo to the supervising partner that lists each issue, where it appears "
        "(document and section), why it matters for the client, and a recommended fix"
    ),
    "risk_table": (
        "a table with one row per issue: document and section, the problem, risk level "
        "(high, medium, low) and proposed replacement language"
    ),
}

JURISDICTIONS = ["Delaware", "New York"]

# Supporting documents a matter folder can contain besides the main agreement.
SUPPORTING_KINDS = ["amendment", "disclosure schedule", "side letter", "board consent"]
DISTRACTOR_KINDS = ["email thread", "prior draft", "unrelated vendor agreement", "meeting notes"]

ISSUE_LIBRARY: dict[str, dict] = {
    "change_of_control_consent": {
        "label": "change of control consent",
        "applies_to": "any",
        "description": "A counterparty consent right is triggered by the transaction or a change of control and has not been obtained or addressed.",
        "detect_terms": ["change of control", "prior written consent"],
        "planted_text": "Any change of control of the Customer shall be deemed an assignment requiring the Supplier's prior written consent.",
        "finding": "the change of control clause requires the counterparty's prior written consent, which the deal does not address",
    },
    "liability_cap_carveout": {
        "label": "liability cap carve-out conflict",
        "applies_to": "any",
        "description": "A later document narrows or removes a carve-out from the limitation of liability, so the cap now covers losses it should not.",
        "detect_terms": ["limitation of liability", "notwithstanding"],
        "planted_text": "Notwithstanding anything to the contrary, the limitation of liability applies to all claims, including claims for breach of confidentiality.",
        "finding": "a clause extends the limitation of liability to confidentiality breaches, removing the usual carve-out",
    },
    "expired_notice_window": {
        "label": "expired notice window",
        "applies_to": "any",
        "description": "A notice or exercise deadline has already passed relative to the dates in the matter.",
        "detect_terms": ["written notice", "days prior to"],
        "planted_text": "Either party may terminate by giving written notice no fewer than ninety (90) days prior to the end of the then-current term.",
        "finding": "the termination notice window may already have passed given the term dates, so the client may be locked into the current term",
    },
    "auto_renewal": {
        "label": "automatic renewal",
        "applies_to": "commercial_contracts",
        "description": "The agreement renews automatically for a long term unless a short opt-out window is used.",
        "detect_terms": ["automatically renew", "successive"],
        "planted_text": "This Agreement shall automatically renew for successive three (3) year terms unless terminated as provided herein.",
        "finding": "the agreement automatically renews for successive three-year terms, locking the client in",
    },
    "governing_law_mismatch": {
        "label": "governing law mismatch",
        "applies_to": "any",
        "description": "Two documents in the same matter choose different governing law or forums.",
        "detect_terms": ["governed by the laws of", "exclusive jurisdiction"],
        "planted_text": "This letter shall be governed by the laws of the State of California, and the parties submit to the exclusive jurisdiction of its courts.",
        "finding": "one document selects California law and courts, conflicting with the governing law of the main agreement",
    },
    "uncapped_indemnity": {
        "label": "uncapped indemnity",
        "applies_to": "any",
        "description": "An indemnity obligation is excluded from any cap, exposing the client to unlimited liability.",
        "detect_terms": ["indemnify", "without limit"],
        "planted_text": "The Customer shall indemnify the Supplier against all losses arising from third-party claims, without limit as to amount.",
        "finding": "the client's indemnity is uncapped, exposing it to unlimited liability",
    },
    "exclusivity_scope": {
        "label": "overbroad exclusivity",
        "applies_to": "commercial_contracts",
        "description": "An exclusivity or non-compete clause is broader in scope or territory than the deal requires.",
        "detect_terms": ["exclusively", "worldwide"],
        "planted_text": "During the Term the Customer shall purchase the Products exclusively from the Supplier on a worldwide basis.",
        "finding": "the exclusivity clause is worldwide and covers all purchases, which is broader than the commercial deal",
    },
    "survival_gap": {
        "label": "indemnity survival gap",
        "applies_to": "mergers_acquisitions",
        "description": "Representations or indemnities survive for too short a period to make claims practical.",
        "detect_terms": ["shall survive", "six (6) months"],
        "planted_text": "The representations and warranties of the Seller shall survive the Closing for six (6) months only.",
        "finding": "the seller's representations survive only six months after closing, too short to discover most breaches",
    },
    "defined_term_inconsistency": {
        "label": "defined term inconsistency",
        "applies_to": "any",
        "description": "A defined term is used inconsistently across documents, changing the scope of an obligation.",
        "detect_terms": ["as defined in", "affiliates"],
        "planted_text": "For purposes of this schedule, \"Company\" as defined in the Agreement shall include all Affiliates of the Company.",
        "finding": "a supporting document redefines \"Company\" to include all affiliates, widening the obligations beyond the main agreement",
    },
    "missing_assignment_restriction": {
        "label": "unrestricted assignment",
        "applies_to": "any",
        "description": "The counterparty may assign the agreement freely, including to a competitor.",
        "detect_terms": ["may assign", "without the consent"],
        "planted_text": "The Supplier may assign this Agreement, in whole or in part, without the consent of the Customer.",
        "finding": "the counterparty may assign the agreement without consent, including to a competitor of the client",
    },
}


def issue_types_for(practice_area: str) -> list[str]:
    return [
        k
        for k, v in ISSUE_LIBRARY.items()
        if v["applies_to"] in ("any", practice_area)
    ]
