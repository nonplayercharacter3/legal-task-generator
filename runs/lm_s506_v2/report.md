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
| s506-m0001 | accepted (label pending) | train |  |  |
| s506-m0002 | accepted (label pending) | train |  |  |
| s506-m0003 | accepted (label pending) | test |  |  |

## Variety

- Industries: seed genetics (1), concert promotion (1), battery recycling (1)
- Agreement types: asset purchase agreement (2), software license agreement (1)
- Issue types: uncapped_indemnity (3), expired_notice_window (2), missing_assignment_restriction (2), liability_cap_carveout (2), change_of_control_consent (2), survival_gap (1), defined_term_inconsistency (1), governing_law_mismatch (1), exclusivity_scope (1), auto_renewal (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 290292 | 49395 | 0 |
| drafter | 26 | 720509 | 131529 | 0 |
| fact_extractor | 3 | 145857 | 10527 | 0 |
| fact_matcher | 3 | 4127 | 385 | 0 |
| instruction_writer | 3 | 4059 | 412 | 0 |
| issue_solo_verifier | 20 | 153853 | 8638 | 0 |
| issue_verifier | 16 | 668006 | 12100 | 0 |
| judge | 9 | 69387 | 7076 | 0 |
| ledger_writer | 4 | 19251 | 54096 | 0 |
| rubric_writer | 3 | 24598 | 6925 | 0 |
