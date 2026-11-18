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
| solver_check | 3 | 0 | 0 | 3 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

**3 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s47-m0001 | accepted (label pending) | train |  |  |
| s47-m0002 | accepted (label pending) | train |  |  |
| s47-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: independent film distribution (1), commercial laundry services (1), cold chain logistics (1)
- Agreement types: stock purchase agreement (2), asset purchase agreement (1)
- Issue types: defined_term_inconsistency (3), missing_assignment_restriction (3), survival_gap (3), uncapped_indemnity (2), change_of_control_consent (2), expired_notice_window (2), governing_law_mismatch (2), liability_cap_carveout (1)
- Party names used in more than one matter: ostrander in s47-m0001, s47-m0002
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 328088 | 47300 | 0 |
| drafter | 26 | 836957 | 150281 | 0 |
| fact_extractor | 3 | 163278 | 10755 | 0 |
| fact_matcher | 3 | 4531 | 754 | 0 |
| instruction_writer | 3 | 3924 | 502 | 0 |
| issue_solo_verifier | 24 | 223612 | 12736 | 0 |
| issue_verifier | 18 | 855478 | 15685 | 0 |
| judge | 9 | 70013 | 6940 | 0 |
| ledger_writer | 5 | 23569 | 72818 | 0 |
| rubric_writer | 3 | 24402 | 7278 | 0 |
