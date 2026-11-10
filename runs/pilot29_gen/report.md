# Run report

Backend: `claude_sdk`. Accepted **3 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 3 | 0 | 0 |
| rubric_tests | 3 | 3 | 0 | 0 |
| decontamination | 3 | 3 | 0 | 0 |
| solver_check | 3 | 0 | 0 | 3 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**3 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s29-m0001 | accepted (label pending) | train |  |  |
| s29-m0002 | accepted (label pending) | train |  |  |
| s29-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: marine shipping (1), commercial bakery (1), cold chain logistics (1)
- Agreement types: stock purchase agreement (1), supply agreement (1), master services agreement (1)
- Issue types: liability_cap_carveout (3), uncapped_indemnity (2), defined_term_inconsistency (2), exclusivity_scope (2), expired_notice_window (1), survival_gap (1), missing_assignment_restriction (1), governing_law_mismatch (1), change_of_control_consent (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 182668 | 37556 | 0 |
| drafter | 14 | 233577 | 75512 | 0 |
| fact_extractor | 3 | 84912 | 8788 | 0 |
| fact_matcher | 3 | 5824 | 1346 | 0 |
| instruction_writer | 3 | 4278 | 1075 | 0 |
| issue_verifier | 15 | 363507 | 10619 | 0 |
| judge | 9 | 60331 | 8588 | 0 |
| ledger_writer | 3 | 12607 | 27043 | 0 |
| rubric_writer | 3 | 20457 | 7558 | 0 |
