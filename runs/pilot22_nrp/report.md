# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 3 | 0 | 0 |
| rubric_tests | 3 | 2 | 1 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 2 | 2 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 2 | 0.00: 1, 0.33: 1 |

**1 accepted task(s) are marked unsolved (no attempt passed): check they are not broken.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s22-m0001 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C7"] |
| s22-m0002 | accepted | test | qwen3-small 0.33 |  |
| s22-m0003 | accepted (unsolved) | train | qwen3-small 0.00 |  |

## Variety

- Industries: event furniture rental (1), solar panel installation (1), medical imaging equipment (1)
- Agreement types: stock purchase agreement (2), software license agreement (1)
- Issue types: expired_notice_window (2), liability_cap_carveout (2), uncapped_indemnity (2), missing_assignment_restriction (1), auto_renewal (1), exclusivity_scope (1), defined_term_inconsistency (1), governing_law_mismatch (1), change_of_control_consent (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 210122 | 50719 | 0 |
| drafter | 13 | 219771 | 91295 | 0 |
| fact_extractor | 3 | 99512 | 7119 | 0 |
| fact_matcher | 3 | 5084 | 679 | 0 |
| instruction_writer | 3 | 4204 | 1268 | 0 |
| issue_verifier | 12 | 355832 | 10042 | 0 |
| judge | 17 | 147926 | 16948 | 0 |
| ledger_writer | 3 | 12335 | 26491 | 0 |
| rubric_writer | 3 | 18315 | 5314 | 0 |
| solver | 114 | 949132 | 125944 | 0 |
