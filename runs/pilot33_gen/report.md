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
| s33-m0001 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s33-m0002 | accepted | train | qwen3-small 0.33 |  |
| s33-m0003 | accepted | train | qwen3-small 0.33 |  |

## Variety

- Industries: veterinary diagnostics (1), pet food manufacturing (1), organic dairy (1)
- Agreement types: distribution agreement (2), asset purchase agreement (1)
- Issue types: change_of_control_consent (3), governing_law_mismatch (2), missing_assignment_restriction (1), defined_term_inconsistency (1), auto_renewal (1), liability_cap_carveout (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 178156 | 39187 | 0 |
| drafter | 13 | 203605 | 74770 | 0 |
| fact_extractor | 3 | 83008 | 5943 | 0 |
| fact_matcher | 2 | 3072 | 390 | 0 |
| instruction_writer | 3 | 4179 | 951 | 0 |
| issue_verifier | 10 | 243080 | 6646 | 0 |
| judge | 21 | 157566 | 20639 | 0 |
| ledger_writer | 3 | 12227 | 20894 | 0 |
| rubric_writer | 3 | 18454 | 6514 | 0 |
| solver | 143 | 996062 | 127160 | 0 |
