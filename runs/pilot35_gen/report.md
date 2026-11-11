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
| solver_check | 3 | 3 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 3 | 0.00: 1, 0.33: 1, 1.00: 1 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s35-m0001 | accepted | train | qwen3-small 1.00 |  |
| s35-m0002 | accepted | test | qwen3-small 0.33 |  |
| s35-m0003 | accepted (unsolved) | test | qwen3-small 0.00 |  |

## Variety

- Industries: outdoor apparel (1), industrial textiles (1), event furniture rental (1)
- Agreement types: software license agreement (2), asset purchase agreement (1)
- Issue types: governing_law_mismatch (3), change_of_control_consent (2), exclusivity_scope (2), uncapped_indemnity (2), missing_assignment_restriction (1), defined_term_inconsistency (1), auto_renewal (1), expired_notice_window (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 167814 | 43514 | 0 |
| drafter | 13 | 202368 | 68211 | 0 |
| fact_extractor | 3 | 77662 | 7425 | 0 |
| fact_matcher | 2 | 2865 | 446 | 0 |
| instruction_writer | 3 | 4232 | 1104 | 0 |
| issue_verifier | 13 | 277415 | 9065 | 0 |
| judge | 21 | 190801 | 28498 | 0 |
| ledger_writer | 3 | 12309 | 21720 | 0 |
| rubric_writer | 3 | 19483 | 8140 | 0 |
| solver | 150 | 1025309 | 138596 | 0 |
