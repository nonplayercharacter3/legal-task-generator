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
| s43-m0001 | accepted (label pending) | test |  |  |
| s43-m0002 | accepted (label pending) | train |  |  |
| s43-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: video game publishing (1), water treatment chemicals (1), battery recycling (1)
- Agreement types: asset purchase agreement (2), supply agreement (1)
- Issue types: change_of_control_consent (2), liability_cap_carveout (2), missing_assignment_restriction (2), defined_term_inconsistency (2), uncapped_indemnity (1), expired_notice_window (1), auto_renewal (1), exclusivity_scope (1), governing_law_mismatch (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 227910 | 48503 | 0 |
| drafter | 14 | 274758 | 99686 | 0 |
| fact_extractor | 3 | 108711 | 6932 | 0 |
| fact_matcher | 3 | 4598 | 701 | 0 |
| instruction_writer | 3 | 4281 | 1351 | 0 |
| issue_verifier | 13 | 424008 | 9124 | 0 |
| judge | 9 | 69569 | 7450 | 0 |
| ledger_writer | 3 | 12495 | 23556 | 0 |
| rubric_writer | 3 | 20235 | 6882 | 0 |
