# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 2 | 0 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 1 | 1 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 0 | 1 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s7-m0001 | rejected at rubric_trace |  |  | errors: ["criterion C5 cites 'I1', which is not a ledger fact"] |
| s7-m0002 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s7-m0003 | rejected at consistency |  |  | mismatches: [{"fact": "F7", "key": "Stock Purchase Agreement forum", "filename": "stock_purchase_agreement.md", "ledger": "exclusive jurisdiction of state or fe |

## Variety

- Industries: cold chain logistics (1), solar panel installation (1), precision agriculture drones (1)
- Agreement types: master services agreement (1), asset purchase agreement (1), stock purchase agreement (1)
- Issue types: change_of_control_consent (2), governing_law_mismatch (2), uncapped_indemnity (2), missing_assignment_restriction (2), expired_notice_window (1), liability_cap_carveout (1), survival_gap (1), defined_term_inconsistency (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 136854 | 32999 | 0 |
| drafter | 14 | 256255 | 95591 | 0 |
| fact_extractor | 3 | 104614 | 6814 | 0 |
| fact_matcher | 3 | 4108 | 1067 | 0 |
| instruction_writer | 2 | 2793 | 789 | 0 |
| issue_verifier | 7 | 211402 | 4222 | 0 |
| judge | 7 | 69773 | 7665 | 0 |
| ledger_writer | 3 | 10685 | 21182 | 0 |
| rubric_writer | 2 | 10243 | 3257 | 0 |
| solver | 68 | 817450 | 60525 | 0 |
