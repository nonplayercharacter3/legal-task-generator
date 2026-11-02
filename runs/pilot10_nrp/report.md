# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters (1 stopped by errors).

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
| solver_check | 1 | 0 | 1 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s10-m0001 | rejected at issue_check |  |  | missing: ["I4"] |
| s10-m0002 | rejected at solver_check |  | 0.00 | no attempt passed: task is probably broken or too hard |
| s10-m0003 | rejected at error |  |  | ModelError: solver: HTTP 403: b'' |

## Variety

- Industries: veterinary diagnostics (1), specialty pharmaceuticals (1), independent film distribution (1)
- Agreement types: asset purchase agreement (2), master services agreement (1)
- Issue types: missing_assignment_restriction (2), defined_term_inconsistency (2), governing_law_mismatch (2), uncapped_indemnity (1), change_of_control_consent (1), liability_cap_carveout (1), auto_renewal (1), exclusivity_scope (1), expired_notice_window (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 126928 | 30209 | 0 |
| drafter | 13 | 221961 | 77728 | 0 |
| fact_extractor | 3 | 86747 | 7664 | 0 |
| fact_matcher | 3 | 4152 | 1372 | 0 |
| instruction_writer | 2 | 2756 | 763 | 0 |
| issue_verifier | 13 | 320566 | 8568 | 0 |
| judge | 11 | 96107 | 10119 | 0 |
| ledger_writer | 3 | 11208 | 21623 | 0 |
| rubric_writer | 2 | 10926 | 3694 | 0 |
| solver | 90 | 648224 | 59122 | 7 |
