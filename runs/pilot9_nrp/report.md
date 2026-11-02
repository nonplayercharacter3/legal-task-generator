# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 2 | 0 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 2 | 0 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 2 | 2 | 0 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s9-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F8", "key": "Stock Purchase Agreement indemnity cap carve-outs", "filename": "escrow_agreement.md", "ledger": "Fraud, breaches of Fundame |
| s9-m0002 | accepted | dev | 0.33 |  |
| s9-m0003 | accepted | train | 0.33 |  |

## Variety

- Industries: commercial laundry services (1), architectural glass (1), dental clinics (1)
- Agreement types: stock purchase agreement (1), supply agreement (1), master services agreement (1)
- Issue types: expired_notice_window (3), change_of_control_consent (2), survival_gap (1), governing_law_mismatch (1), liability_cap_carveout (1), exclusivity_scope (1), auto_renewal (1), defined_term_inconsistency (1), missing_assignment_restriction (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 105784 | 32800 | 0 |
| drafter | 13 | 204550 | 70194 | 0 |
| fact_extractor | 3 | 79519 | 7933 | 0 |
| fact_matcher | 3 | 3854 | 898 | 0 |
| instruction_writer | 2 | 2758 | 805 | 0 |
| issue_verifier | 8 | 171236 | 5047 | 0 |
| judge | 14 | 130815 | 15342 | 0 |
| ledger_writer | 3 | 10757 | 24535 | 0 |
| rubric_writer | 2 | 10062 | 3055 | 0 |
| solver | 90 | 609030 | 117521 | 0 |
