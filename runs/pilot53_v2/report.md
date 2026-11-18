# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

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
| solver_check | 1 | 0 | 0 | 1 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**1 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s53-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F7", "key": "Stock Purchase Agreement definition of 'Losses'", "filename": "stock_purchase_agreement.md", "ledger": "excludes punitive an |
| s53-m0002 | accepted (label pending) | dev |  |  |
| s53-m0003 | rejected at issue_check |  |  | missing: ["I2"] |

## Variety

- Industries: architectural glass (1), regional airline catering (1), video game publishing (1)
- Agreement types: stock purchase agreement (2), master services agreement (1)
- Issue types: expired_notice_window (2), defined_term_inconsistency (2), uncapped_indemnity (2), liability_cap_carveout (2), change_of_control_consent (1), missing_assignment_restriction (1), governing_law_mismatch (1), auto_renewal (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 92750 | 14625 | 0 |
| drafter | 24 | 674102 | 139824 | 0 |
| fact_extractor | 3 | 151896 | 10097 | 0 |
| fact_matcher | 2 | 3574 | 833 | 0 |
| instruction_writer | 1 | 1321 | 153 | 0 |
| issue_solo_verifier | 12 | 89964 | 6423 | 0 |
| issue_verifier | 9 | 378103 | 7157 | 0 |
| judge | 3 | 22098 | 2727 | 0 |
| ledger_writer | 3 | 13548 | 37298 | 0 |
| rubric_writer | 1 | 7485 | 2197 | 0 |
