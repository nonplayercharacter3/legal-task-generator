# Run report

Backend: `claude_sdk`. Accepted **2 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 2 | 1 | 0 |
| consistency | 2 | 2 | 0 | 0 |
| issue_check | 2 | 2 | 0 | 0 |
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
| s507-m0001 | rejected at ledger_schema |  |  | errors: ["fact F5 is 21 words; make it one short value (at most 20 words) and split compound facts"] |
| s507-m0002 | accepted (label pending) | train |  |  |
| s507-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: orthopedic implants (1), architectural glass (1), event furniture rental (1)
- Agreement types: supply agreement (2), stock purchase agreement (1)
- Issue types: change_of_control_consent (2), exclusivity_scope (2), missing_assignment_restriction (2), expired_notice_window (2), uncapped_indemnity (1), liability_cap_carveout (1), defined_term_inconsistency (1), auto_renewal (1), survival_gap (1), governing_law_mismatch (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 155802 | 26219 | 0 |
| drafter | 13 | 310526 | 70577 | 0 |
| fact_extractor | 2 | 77645 | 6857 | 0 |
| fact_matcher | 2 | 3779 | 651 | 0 |
| instruction_writer | 2 | 2711 | 293 | 0 |
| issue_solo_verifier | 12 | 92186 | 5445 | 0 |
| issue_verifier | 9 | 293175 | 6918 | 0 |
| judge | 6 | 38790 | 4191 | 0 |
| ledger_writer | 4 | 19194 | 48446 | 0 |
| rubric_writer | 2 | 14192 | 3944 | 0 |
