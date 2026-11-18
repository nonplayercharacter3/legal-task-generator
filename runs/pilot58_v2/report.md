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
| s58-m0001 | accepted (label pending) | train |  |  |
| s58-m0002 | accepted (label pending) | test |  |  |
| s58-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: orthopedic implants (1), organic dairy (1), seed genetics (1)
- Agreement types: software license agreement (2), stock purchase agreement (1)
- Issue types: liability_cap_carveout (3), expired_notice_window (2), missing_assignment_restriction (2), uncapped_indemnity (2), defined_term_inconsistency (2), auto_renewal (1), exclusivity_scope (1), governing_law_mismatch (1), survival_gap (1), change_of_control_consent (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 242950 | 47733 | 0 |
| drafter | 20 | 486174 | 106683 | 0 |
| fact_extractor | 3 | 120365 | 10484 | 0 |
| fact_matcher | 3 | 4515 | 516 | 0 |
| instruction_writer | 3 | 3936 | 434 | 0 |
| issue_solo_verifier | 20 | 162932 | 9532 | 0 |
| issue_verifier | 16 | 536947 | 12605 | 0 |
| judge | 9 | 68385 | 6586 | 0 |
| ledger_writer | 3 | 14261 | 41534 | 0 |
| rubric_writer | 3 | 23228 | 6841 | 0 |
