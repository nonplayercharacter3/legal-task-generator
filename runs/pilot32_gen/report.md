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
| qwen3-small | 3 | 0.33: 1, 0.67: 1, 1.00: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s32-m0001 | accepted | train | qwen3-small 1.00 |  |
| s32-m0002 | accepted | train | qwen3-small 0.67 |  |
| s32-m0003 | accepted | test | qwen3-small 0.33 |  |

## Variety

- Industries: marine shipping (1), regional airline catering (1), specialty pharmaceuticals (1)
- Agreement types: software license agreement (1), master services agreement (1), asset purchase agreement (1)
- Issue types: governing_law_mismatch (2), liability_cap_carveout (2), exclusivity_scope (1), auto_renewal (1), missing_assignment_restriction (1), expired_notice_window (1), uncapped_indemnity (1), defined_term_inconsistency (1), change_of_control_consent (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 175988 | 49408 | 0 |
| drafter | 14 | 257588 | 73193 | 0 |
| fact_extractor | 3 | 84344 | 8608 | 0 |
| fact_matcher | 3 | 4442 | 874 | 0 |
| instruction_writer | 3 | 4266 | 1108 | 0 |
| issue_verifier | 12 | 268725 | 9563 | 0 |
| judge | 21 | 190837 | 20801 | 0 |
| ledger_writer | 3 | 12254 | 23295 | 0 |
| rubric_writer | 3 | 19306 | 6963 | 0 |
| solver | 151 | 1200048 | 148670 | 0 |
