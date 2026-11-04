# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 3 | 0 | 0 |
| rubric_tests | 3 | 2 | 1 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 2 | 1 | 1 | 0 |

## Matters

| Matter | Result | Split | Solver pass rate | Reason |
| --- | --- | --- | ---: | --- |
| s6-m0001 | rejected at solver_check |  | 1.00 | every attempt passed: too easy to carry training signal |
| s6-m0002 | accepted | train | 0.33 |  |
| s6-m0003 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C6"] |

## Variety

- Industries: concert promotion (1), veterinary diagnostics (1), water treatment chemicals (1)
- Agreement types: stock purchase agreement (2), distribution agreement (1)
- Issue types: defined_term_inconsistency (2), governing_law_mismatch (2), liability_cap_carveout (2), change_of_control_consent (1), auto_renewal (1), expired_notice_window (1), exclusivity_scope (1), uncapped_indemnity (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 227580 | 44715 | 0 |
| drafter | 15 | 279050 | 101671 | 0 |
| fact_extractor | 3 | 110602 | 7795 | 0 |
| fact_matcher | 3 | 3572 | 509 | 0 |
| instruction_writer | 3 | 4221 | 1201 | 0 |
| issue_verifier | 12 | 388054 | 7937 | 0 |
| judge | 17 | 164577 | 16001 | 0 |
| ledger_writer | 3 | 10768 | 20656 | 0 |
| rubric_writer | 3 | 16518 | 4550 | 0 |
| solver | 141 | 2156428 | 357776 | 0 |
