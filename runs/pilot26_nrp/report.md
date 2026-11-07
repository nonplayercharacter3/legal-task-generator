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
| qwen3-small | 3 | 0.00: 1, 0.33: 2 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s26-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s26-m0002 | accepted | train | qwen3-small 0.33 |  |
| s26-m0003 | accepted | test | qwen3-small 0.33 |  |

## Variety

- Industries: outdoor apparel (1), regional airline catering (1), data center cooling (1)
- Agreement types: master services agreement (1), software license agreement (1), stock purchase agreement (1)
- Issue types: governing_law_mismatch (2), liability_cap_carveout (2), expired_notice_window (2), change_of_control_consent (2), exclusivity_scope (1), auto_renewal (1), uncapped_indemnity (1), missing_assignment_restriction (1), defined_term_inconsistency (1), survival_gap (1)
- Party names used in more than one matter: ostrander in s26-m0002, s26-m0003
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 185398 | 52714 | 0 |
| drafter | 13 | 209171 | 76708 | 0 |
| fact_extractor | 3 | 85756 | 6396 | 0 |
| fact_matcher | 2 | 2858 | 272 | 0 |
| instruction_writer | 3 | 4219 | 1179 | 0 |
| issue_verifier | 14 | 351565 | 9174 | 0 |
| judge | 21 | 197291 | 22469 | 0 |
| ledger_writer | 3 | 12406 | 28653 | 0 |
| rubric_writer | 3 | 19606 | 5344 | 0 |
| solver | 148 | 1130023 | 183922 | 0 |
