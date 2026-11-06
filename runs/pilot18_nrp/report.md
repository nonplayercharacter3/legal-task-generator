# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 3 | 0 | 0 |
| rubric_tests | 3 | 1 | 2 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 1 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 1.00: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s18-m0001 | rejected at rubric_tests |  |  | gold_fails: ["C9", "C10"] |
| s18-m0002 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C11"] |
| s18-m0003 | accepted | dev | qwen3-small 1.00 |  |

## Variety

- Industries: pet food manufacturing (1), craft brewing (1), data center cooling (1)
- Agreement types: master services agreement (1), stock purchase agreement (1), supply agreement (1)
- Issue types: auto_renewal (2), expired_notice_window (2), liability_cap_carveout (2), governing_law_mismatch (1), defined_term_inconsistency (1), missing_assignment_restriction (1), change_of_control_consent (1), survival_gap (1), uncapped_indemnity (1), exclusivity_scope (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 186874 | 48022 | 0 |
| drafter | 13 | 220894 | 79319 | 0 |
| fact_extractor | 3 | 87985 | 7279 | 0 |
| fact_matcher | 2 | 3445 | 530 | 0 |
| instruction_writer | 3 | 4181 | 1161 | 0 |
| issue_verifier | 13 | 326726 | 9492 | 0 |
| judge | 13 | 101511 | 9872 | 0 |
| ledger_writer | 3 | 12405 | 25052 | 0 |
| rubric_writer | 3 | 18659 | 5830 | 0 |
| solver | 58 | 543867 | 52142 | 0 |
