# Run report

Backend: `claude_sdk`. Accepted **1 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 2 | 1 | 0 |
| issue_check | 2 | 2 | 0 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 1 | 1 | 0 |
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
| s19-m0001 | accepted | train | qwen3-small 0.67 |  |
| s19-m0002 | rejected at consistency |  |  | mismatches: [{"fact": "F6", "key": "APA cap carve-outs", "filename": "asset_purchase_agreement.md", "ledger": "Fraud, Fundamental Representations under Section  |
| s19-m0003 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C9"] |

## Variety

- Industries: data center cooling (1), specialty pharmaceuticals (1), concert promotion (1)
- Agreement types: asset purchase agreement (2), stock purchase agreement (1)
- Issue types: governing_law_mismatch (3), change_of_control_consent (2), uncapped_indemnity (2), defined_term_inconsistency (2), survival_gap (1), liability_cap_carveout (1), expired_notice_window (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 150492 | 32148 | 0 |
| drafter | 15 | 301615 | 102871 | 0 |
| fact_extractor | 3 | 112713 | 8296 | 0 |
| fact_matcher | 3 | 4446 | 746 | 0 |
| instruction_writer | 2 | 2816 | 730 | 0 |
| issue_verifier | 7 | 227770 | 5549 | 0 |
| judge | 10 | 81753 | 7301 | 0 |
| ledger_writer | 3 | 12380 | 27379 | 0 |
| rubric_writer | 2 | 11852 | 3250 | 0 |
| solver | 65 | 600419 | 48969 | 0 |
