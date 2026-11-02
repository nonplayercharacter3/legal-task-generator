# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters (2 stopped by errors).

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 2 | 1 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 2 | 0 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 0 | 0 | 0 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s11-m0001 | rejected at error |  |  | ModelError: solver: HTTP 403: b'' |
| s11-m0002 | rejected at issue_check |  |  | missing: ["I3", "I4", "I5"] |
| s11-m0003 | rejected at error |  |  | ModelError: solver: HTTP 403: b'' |

## Variety

- Industries: commercial laundry services (1), used car auctions (1), school bus operations (1)
- Agreement types: software license agreement (1), asset purchase agreement (1), distribution agreement (1)
- Issue types: defined_term_inconsistency (2), liability_cap_carveout (2), uncapped_indemnity (1), expired_notice_window (1), change_of_control_consent (1), survival_gap (1), governing_law_mismatch (1), missing_assignment_restriction (1), exclusivity_scope (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 111824 | 34102 | 0 |
| drafter | 13 | 203019 | 68100 | 0 |
| fact_extractor | 3 | 77304 | 7166 | 0 |
| fact_matcher | 3 | 3741 | 594 | 0 |
| instruction_writer | 2 | 2697 | 820 | 0 |
| issue_verifier | 12 | 269359 | 9609 | 0 |
| judge | 6 | 45338 | 4710 | 0 |
| ledger_writer | 3 | 11149 | 20918 | 0 |
| rubric_writer | 2 | 10270 | 3067 | 0 |
| solver | 14 | 0 | 0 | 14 |
