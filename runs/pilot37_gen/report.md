# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 2 | 1 | 0 |
| leak_check | 2 | 2 | 0 | 0 |
| rubric_trace | 2 | 2 | 0 | 0 |
| rubric_tests | 2 | 2 | 0 | 0 |
| decontamination | 2 | 2 | 0 | 0 |
| solver_check | 2 | 0 | 0 | 2 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**2 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s37-m0001 | accepted (label pending) | train |  |  |
| s37-m0002 | accepted (label pending) | train |  |  |
| s37-m0003 | rejected at issue_check |  |  | missing: ["I2"] |

## Variety

- Industries: architectural glass (1), marine shipping (1), orthopedic implants (1)
- Agreement types: stock purchase agreement (2), software license agreement (1)
- Issue types: change_of_control_consent (2), governing_law_mismatch (2), defined_term_inconsistency (2), expired_notice_window (2), survival_gap (2), liability_cap_carveout (1), uncapped_indemnity (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 125166 | 27766 | 0 |
| drafter | 13 | 233956 | 85675 | 0 |
| fact_extractor | 3 | 94198 | 7622 | 0 |
| fact_matcher | 3 | 4528 | 676 | 0 |
| instruction_writer | 2 | 2836 | 719 | 0 |
| issue_verifier | 12 | 319276 | 10674 | 0 |
| judge | 6 | 41005 | 4148 | 0 |
| ledger_writer | 3 | 12285 | 26544 | 0 |
| rubric_writer | 2 | 14311 | 3959 | 0 |
