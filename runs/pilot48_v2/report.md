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
| s48-m0001 | accepted (label pending) | train |  |  |
| s48-m0002 | accepted (label pending) | train |  |  |
| s48-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: solar panel installation (1), event furniture rental (1), elevator maintenance (1)
- Agreement types: software license agreement (2), supply agreement (1)
- Issue types: expired_notice_window (2), governing_law_mismatch (2), exclusivity_scope (2), uncapped_indemnity (2), defined_term_inconsistency (2), auto_renewal (1), missing_assignment_restriction (1), liability_cap_carveout (1), change_of_control_consent (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 248270 | 43972 | 0 |
| drafter | 25 | 585728 | 111720 | 0 |
| fact_extractor | 3 | 126481 | 11016 | 0 |
| fact_matcher | 3 | 4624 | 848 | 0 |
| instruction_writer | 3 | 3917 | 462 | 0 |
| issue_solo_verifier | 14 | 93219 | 7457 | 0 |
| issue_verifier | 14 | 516352 | 10201 | 0 |
| judge | 9 | 64978 | 6509 | 0 |
| ledger_writer | 3 | 13597 | 32567 | 0 |
| rubric_writer | 3 | 21386 | 7701 | 0 |
