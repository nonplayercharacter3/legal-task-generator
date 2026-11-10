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
| qwen3-small | 3 | 0.00: 1, 1.00: 2 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s30-m0001 | accepted | test | qwen3-small 1.00 |  |
| s30-m0002 | accepted | train | qwen3-small 1.00 |  |
| s30-m0003 | accepted (unsolved) | train | qwen3-small 0.00 |  |

## Variety

- Industries: organic dairy (1), video game publishing (1), commercial bakery (1)
- Agreement types: software license agreement (2), stock purchase agreement (1)
- Issue types: missing_assignment_restriction (2), governing_law_mismatch (2), defined_term_inconsistency (2), survival_gap (1), uncapped_indemnity (1), change_of_control_consent (1), expired_notice_window (1), auto_renewal (1), exclusivity_scope (1), liability_cap_carveout (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 184194 | 43127 | 0 |
| drafter | 14 | 229018 | 78270 | 0 |
| fact_extractor | 3 | 89116 | 7809 | 0 |
| fact_matcher | 3 | 3944 | 320 | 0 |
| instruction_writer | 3 | 4281 | 1222 | 0 |
| issue_verifier | 13 | 325179 | 8837 | 0 |
| judge | 21 | 158697 | 18813 | 0 |
| ledger_writer | 3 | 12338 | 26126 | 0 |
| rubric_writer | 3 | 20151 | 6364 | 0 |
| solver | 149 | 997389 | 130230 | 0 |
