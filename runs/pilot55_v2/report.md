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
| qwen3-small | 3 | 0.00: 2, 0.33: 1 |

**2 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s55-m0001 | accepted | dev | qwen3-small 0.33 |  |
| s55-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s55-m0003 | accepted (unsolved) | test | qwen3-small 0.00 |  |

## Variety

- Industries: marine shipping (1), regional airline catering (1), outdoor apparel (1)
- Agreement types: master services agreement (1), stock purchase agreement (1), software license agreement (1)
- Issue types: exclusivity_scope (2), defined_term_inconsistency (2), expired_notice_window (2), uncapped_indemnity (2), governing_law_mismatch (1), liability_cap_carveout (1), change_of_control_consent (1), survival_gap (1), auto_renewal (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 257558 | 45896 | 0 |
| drafter | 23 | 588543 | 114879 | 0 |
| fact_extractor | 3 | 131550 | 11229 | 0 |
| fact_matcher | 3 | 4313 | 630 | 0 |
| instruction_writer | 3 | 3931 | 536 | 0 |
| issue_solo_verifier | 20 | 154163 | 7149 | 0 |
| issue_verifier | 14 | 521627 | 10832 | 0 |
| judge | 21 | 182644 | 17943 | 0 |
| ledger_writer | 4 | 18907 | 62400 | 0 |
| rubric_writer | 3 | 21662 | 6341 | 0 |
| solver | 264 | 2708958 | 215848 | 0 |
