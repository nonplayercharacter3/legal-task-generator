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
| s61-m0001 | accepted (label pending) | train |  |  |
| s61-m0002 | accepted (label pending) | train |  |  |
| s61-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: pet food manufacturing (1), concert promotion (1), architectural glass (1)
- Agreement types: stock purchase agreement (2), asset purchase agreement (1)
- Issue types: survival_gap (3), uncapped_indemnity (2), defined_term_inconsistency (2), governing_law_mismatch (2), change_of_control_consent (2), liability_cap_carveout (2), expired_notice_window (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 301576 | 45527 | 0 |
| drafter | 20 | 551592 | 138735 | 0 |
| fact_extractor | 3 | 148266 | 8936 | 0 |
| fact_matcher | 3 | 4027 | 290 | 0 |
| instruction_writer | 3 | 3928 | 451 | 0 |
| issue_solo_verifier | 20 | 190829 | 9167 | 0 |
| issue_verifier | 15 | 650593 | 11271 | 0 |
| judge | 9 | 66600 | 6872 | 0 |
| ledger_writer | 4 | 19142 | 52715 | 0 |
| rubric_writer | 3 | 22489 | 7017 | 0 |
