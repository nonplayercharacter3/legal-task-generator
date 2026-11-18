# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

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
| solver_check | 2 | 0 | 0 | 2 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**2 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s60-m0001 | accepted (label pending) | train |  |  |
| s60-m0002 | rejected at issue_check |  |  | missing: ["I2"] |
| s60-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: industrial textiles (1), battery recycling (1), cold chain logistics (1)
- Agreement types: supply agreement (1), stock purchase agreement (1), software license agreement (1)
- Issue types: expired_notice_window (3), defined_term_inconsistency (3), liability_cap_carveout (2), missing_assignment_restriction (2), change_of_control_consent (2), governing_law_mismatch (2), auto_renewal (1), survival_gap (1), uncapped_indemnity (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 151634 | 34013 | 0 |
| drafter | 24 | 654754 | 127738 | 0 |
| fact_extractor | 3 | 142174 | 10931 | 0 |
| fact_matcher | 3 | 4504 | 758 | 0 |
| instruction_writer | 2 | 2613 | 350 | 0 |
| issue_solo_verifier | 20 | 138202 | 8252 | 0 |
| issue_verifier | 18 | 720281 | 16170 | 0 |
| judge | 6 | 46365 | 4856 | 0 |
| ledger_writer | 4 | 19374 | 59687 | 0 |
| rubric_writer | 2 | 14950 | 4866 | 0 |
