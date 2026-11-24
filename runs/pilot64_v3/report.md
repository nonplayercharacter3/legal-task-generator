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
| qwen3-small | 3 | 0.00: 3 |

**3 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s64-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s64-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s64-m0003 | accepted (unsolved) | train | qwen3-small 0.00 |  |

## Variety

- Industries: craft brewing (1), organic dairy (1), commercial bakery (1)
- Agreement types: software license agreement (2), asset purchase agreement (1)
- Issue types: expired_notice_window (2), exclusivity_scope (2), defined_term_inconsistency (2), uncapped_indemnity (2), change_of_control_consent (2), liability_cap_carveout (1), governing_law_mismatch (1), missing_assignment_restriction (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 568202 | 48378 | 0 |
| drafter | 16 | 849950 | 195732 | 0 |
| fact_extractor | 3 | 284537 | 10706 | 0 |
| fact_matcher | 2 | 2878 | 641 | 0 |
| instruction_writer | 3 | 3918 | 462 | 0 |
| issue_solo_verifier | 16 | 277482 | 6719 | 0 |
| issue_verifier | 14 | 1226023 | 11845 | 0 |
| judge | 21 | 182135 | 19434 | 0 |
| ledger_writer | 2 | 9549 | 25449 | 0 |
| rubric_writer | 3 | 21479 | 6191 | 0 |
| solver | 436 | 11401914 | 298758 | 2 |
