# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 2 | 1 | 0 |
| consistency | 2 | 1 | 1 | 0 |
| issue_check | 1 | 1 | 0 | 0 |
| leak_check | 1 | 1 | 0 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 0 | 0 | 1 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**1 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s59-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F6", "key": "MSA liability cap", "filename": "gaisirt_beputh_master_services_agreement.md", "ledger": "Fees paid or payable in the 12 mon |
| s59-m0002 | accepted (label pending) | train |  |  |
| s59-m0003 | rejected at ledger_schema |  |  | errors: ["issue I3 contradicts F6 inside D1, the document that states it; a contradiction needs the fact stated in a different document, otherwise leave it out" |

## Variety

- Industries: medical imaging equipment (1), video game publishing (1), elevator maintenance (1)
- Agreement types: master services agreement (1), asset purchase agreement (1), distribution agreement (1)
- Issue types: governing_law_mismatch (3), missing_assignment_restriction (2), expired_notice_window (2), change_of_control_consent (2), uncapped_indemnity (2), defined_term_inconsistency (2), liability_cap_carveout (1), survival_gap (1), auto_renewal (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 108774 | 17813 | 0 |
| drafter | 18 | 539291 | 98527 | 0 |
| fact_extractor | 2 | 109731 | 8788 | 0 |
| fact_matcher | 3 | 5009 | 760 | 0 |
| instruction_writer | 1 | 1320 | 137 | 0 |
| issue_solo_verifier | 8 | 73157 | 3470 | 0 |
| issue_verifier | 6 | 281575 | 5424 | 0 |
| judge | 3 | 25828 | 2541 | 0 |
| ledger_writer | 4 | 19281 | 58549 | 0 |
| rubric_writer | 1 | 8269 | 2583 | 0 |
