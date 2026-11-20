# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 1 | 2 | 0 |
| leak_check | 1 | 1 | 0 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 1 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 0.67: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s50-m0001 | accepted | train | qwen3-small 0.67 |  |
| s50-m0002 | rejected at issue_check |  |  | missing: ["I6"] |
| s50-m0003 | rejected at issue_check |  |  | missing: ["I1"] |

## Variety

- Industries: battery recycling (1), industrial textiles (1), organic dairy (1)
- Agreement types: stock purchase agreement (1), supply agreement (1), asset purchase agreement (1)
- Issue types: expired_notice_window (2), missing_assignment_restriction (2), change_of_control_consent (2), liability_cap_carveout (2), defined_term_inconsistency (1), governing_law_mismatch (1), uncapped_indemnity (1), auto_renewal (1), exclusivity_scope (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 75394 | 12240 | 0 |
| drafter | 23 | 610020 | 126448 | 0 |
| fact_extractor | 3 | 139395 | 10277 | 0 |
| fact_matcher | 3 | 4313 | 759 | 0 |
| instruction_writer | 1 | 1313 | 156 | 0 |
| issue_solo_verifier | 18 | 141719 | 10091 | 0 |
| issue_verifier | 14 | 537182 | 10632 | 0 |
| judge | 7 | 50979 | 4949 | 0 |
| ledger_writer | 4 | 18418 | 47284 | 0 |
| rubric_writer | 1 | 6537 | 2305 | 0 |
| solver | 71 | 663888 | 59685 | 0 |
