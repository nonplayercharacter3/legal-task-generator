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
| s502-m0001 | accepted (label pending) | train |  |  |
| s502-m0002 | rejected at issue_check |  |  | missing: ["I3"] |
| s502-m0003 | accepted (label pending) | train |  |  |

## Variety

- Industries: marine shipping (1), craft brewing (1), school bus operations (1)
- Agreement types: supply agreement (1), software license agreement (1), stock purchase agreement (1)
- Issue types: change_of_control_consent (2), defined_term_inconsistency (2), governing_law_mismatch (2), uncapped_indemnity (2), missing_assignment_restriction (1), liability_cap_carveout (1), auto_renewal (1), exclusivity_scope (1), expired_notice_window (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 4 | 213698 | 30800 | 0 |
| drafter | 25 | 751296 | 134289 | 0 |
| fact_extractor | 3 | 150876 | 11198 | 0 |
| fact_matcher | 3 | 4082 | 292 | 0 |
| instruction_writer | 2 | 2711 | 292 | 0 |
| issue_solo_verifier | 16 | 130330 | 7047 | 0 |
| issue_verifier | 13 | 544663 | 8865 | 0 |
| judge | 6 | 43517 | 3971 | 0 |
| ledger_writer | 3 | 14299 | 39043 | 0 |
| rubric_writer | 2 | 14408 | 4310 | 0 |
