# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 1 | 1 | 0 |
| leak_check | 1 | 1 | 0 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 0 | 1 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s8-m0001 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s8-m0002 | rejected at issue_check |  |  | missing: ["I3"] |
| s8-m0003 | rejected at consistency |  |  | mismatches: [{"fact": "F4", "key": "Supply Agreement forum", "filename": "ziteir_lakix_master_supply_agreement.md", "ledger": "state and federal courts located  |

## Variety

- Industries: medical imaging equipment (1), dental clinics (1), precision agriculture drones (1)
- Agreement types: stock purchase agreement (1), asset purchase agreement (1), supply agreement (1)
- Issue types: change_of_control_consent (2), defined_term_inconsistency (2), governing_law_mismatch (2), liability_cap_carveout (2), uncapped_indemnity (2), missing_assignment_restriction (1), survival_gap (1), expired_notice_window (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 88466 | 19344 | 0 |
| drafter | 15 | 296813 | 98111 | 0 |
| fact_extractor | 3 | 108780 | 8082 | 0 |
| fact_matcher | 3 | 3776 | 1202 | 0 |
| instruction_writer | 1 | 1427 | 397 | 0 |
| issue_verifier | 10 | 324107 | 5865 | 0 |
| judge | 7 | 84831 | 8279 | 0 |
| ledger_writer | 3 | 10932 | 26374 | 0 |
| rubric_writer | 1 | 5601 | 1539 | 0 |
| solver | 86 | 1784980 | 367805 | 0 |
