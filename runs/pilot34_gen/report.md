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
| qwen3-small | 2 | 1.00: 2 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s34-m0001 | accepted | train | qwen3-small 1.00 |  |
| s34-m0002 | accepted | train | qwen3-small 1.00 |  |
| s34-m0003 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C10"] |

## Variety

- Industries: boutique hotels (1), orthopedic implants (1), cold chain logistics (1)
- Agreement types: asset purchase agreement (2), software license agreement (1)
- Issue types: survival_gap (2), missing_assignment_restriction (2), governing_law_mismatch (2), expired_notice_window (1), liability_cap_carveout (1), uncapped_indemnity (1), exclusivity_scope (1), defined_term_inconsistency (1), change_of_control_consent (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 191392 | 51807 | 0 |
| drafter | 14 | 249435 | 77662 | 0 |
| fact_extractor | 3 | 89861 | 7563 | 0 |
| fact_matcher | 3 | 4635 | 503 | 0 |
| instruction_writer | 3 | 4313 | 1305 | 0 |
| issue_verifier | 12 | 309582 | 8096 | 0 |
| judge | 17 | 153011 | 22272 | 0 |
| ledger_writer | 3 | 12294 | 24887 | 0 |
| rubric_writer | 3 | 19836 | 8130 | 0 |
| solver | 100 | 661967 | 90209 | 2 |
