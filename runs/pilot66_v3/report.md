# Run report

Backend: `claude_sdk`. Accepted **3 of 3** candidate matters.
1 matters were reloaded from an earlier run; model calls below cover this run only.

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
| qwen3-small | 3 | 0.00: 2, 0.67: 1 |

**2 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s66-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s66-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s66-m0003 | accepted | test | qwen3-small 0.67 |  |

## Variety

- Industries: elevator maintenance (1), marine shipping (1), video game publishing (1)
- Agreement types: software license agreement (1), distribution agreement (1), asset purchase agreement (1)
- Issue types: exclusivity_scope (2), missing_assignment_restriction (2), liability_cap_carveout (2), expired_notice_window (2), governing_law_mismatch (2), uncapped_indemnity (2), change_of_control_consent (2), auto_renewal (1), defined_term_inconsistency (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 309022 | 36343 | 0 |
| drafter | 13 | 503472 | 159889 | 0 |
| fact_extractor | 2 | 152314 | 6359 | 0 |
| instruction_writer | 2 | 2645 | 289 | 0 |
| issue_solo_verifier | 12 | 166131 | 5084 | 0 |
| issue_verifier | 12 | 846532 | 9830 | 0 |
| judge | 18 | 195601 | 17897 | 0 |
| rubric_writer | 2 | 15534 | 4889 | 0 |
| solver | 406 | 8794101 | 366152 | 0 |
