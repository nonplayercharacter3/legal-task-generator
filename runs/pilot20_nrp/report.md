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
| s20-m0001 | accepted | dev | qwen3-small 0.33 |  |
| s20-m0002 | accepted (unsolved) | train | qwen3-small 0.00 |  |
| s20-m0003 | accepted | train | qwen3-small 1.00 |  |

## Variety

- Industries: orthopedic implants (1), outdoor apparel (1), data center cooling (1)
- Agreement types: asset purchase agreement (1), master services agreement (1), stock purchase agreement (1)
- Issue types: change_of_control_consent (2), liability_cap_carveout (2), defined_term_inconsistency (2), uncapped_indemnity (1), exclusivity_scope (1), auto_renewal (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 163778 | 44510 | 0 |
| drafter | 12 | 193267 | 67087 | 0 |
| fact_extractor | 3 | 78076 | 6878 | 0 |
| fact_matcher | 3 | 4972 | 1182 | 0 |
| instruction_writer | 3 | 4166 | 1100 | 0 |
| issue_verifier | 10 | 217865 | 7559 | 0 |
| judge | 21 | 171105 | 18508 | 0 |
| ledger_writer | 3 | 12178 | 21106 | 0 |
| rubric_writer | 3 | 17203 | 5090 | 0 |
| solver | 151 | 1043377 | 131910 | 0 |
