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
| qwen3-small | 2 | 0.67: 1, 1.00: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s17-m0001 | accepted | train | qwen3-small 0.67 |  |
| s17-m0002 | accepted | train | qwen3-small 1.00 |  |
| s17-m0003 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C9", "C10"] |

## Variety

- Industries: boutique hotels (1), independent film distribution (1), concert promotion (1)
- Agreement types: asset purchase agreement (1), software license agreement (1), stock purchase agreement (1)
- Issue types: defined_term_inconsistency (2), change_of_control_consent (2), survival_gap (1), uncapped_indemnity (1), liability_cap_carveout (1), auto_renewal (1), expired_notice_window (1), missing_assignment_restriction (1)
- Party names used in more than one matter: ostrander in s17-m0002, s17-m0003
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 175166 | 47645 | 0 |
| drafter | 14 | 241963 | 75801 | 0 |
| fact_extractor | 3 | 83985 | 7587 | 0 |
| fact_matcher | 3 | 4711 | 724 | 0 |
| instruction_writer | 3 | 4172 | 1119 | 0 |
| issue_verifier | 10 | 238898 | 7840 | 0 |
| judge | 17 | 138094 | 14592 | 0 |
| ledger_writer | 3 | 12155 | 26799 | 0 |
| rubric_writer | 3 | 17831 | 4818 | 0 |
| solver | 100 | 791669 | 122504 | 0 |
