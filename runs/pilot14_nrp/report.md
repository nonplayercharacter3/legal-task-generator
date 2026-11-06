# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 1 | 2 | 0 |
| issue_check | 1 | 1 | 0 | 0 |
| leak_check | 1 | 1 | 0 | 0 |
| rubric_trace | 1 | 1 | 0 | 0 |
| rubric_tests | 1 | 1 | 0 | 0 |
| decontamination | 1 | 1 | 0 | 0 |
| solver_check | 1 | 1 | 0 | 0 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 0.33: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s14-m0001 | rejected at consistency |  |  | mismatches: [{"fact": "F5", "key": "Supply Agreement Minimum Annual Commitment", "filename": "gesail_side_letter_minimum_commitment.md", "ledger": "120,000 poun |
| s14-m0002 | rejected at consistency |  |  | mismatches: [{"fact": "F7", "key": "Distribution Agreement liability cap carve-outs", "filename": "term_sheet.md", "ledger": "Supplier indemnity under Section 1 |
| s14-m0003 | accepted | train | qwen3-small 0.33 |  |

## Variety

- Industries: craft brewing (1), architectural glass (1), elevator maintenance (1)
- Agreement types: supply agreement (1), distribution agreement (1), stock purchase agreement (1)
- Issue types: defined_term_inconsistency (2), expired_notice_window (2), change_of_control_consent (1), auto_renewal (1), liability_cap_carveout (1), governing_law_mismatch (1), uncapped_indemnity (1), survival_gap (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 2 | 69786 | 18935 | 0 |
| drafter | 15 | 280189 | 90570 | 0 |
| fact_extractor | 3 | 102135 | 8724 | 0 |
| fact_matcher | 3 | 4168 | 1093 | 0 |
| instruction_writer | 1 | 1452 | 378 | 0 |
| issue_verifier | 4 | 117145 | 3064 | 0 |
| judge | 7 | 67448 | 7329 | 0 |
| ledger_writer | 3 | 12163 | 27863 | 0 |
| rubric_writer | 1 | 6389 | 1309 | 0 |
| solver | 62 | 565738 | 61131 | 0 |
