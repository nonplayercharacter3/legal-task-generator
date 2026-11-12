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
| solver_check | 2 | 1 | 0 | 1 |

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 1 | 1.00: 1 |

**1 accepted task(s) wait for `ltg label`: solver_check was deferred, so they have no difficulty label and no leak probe yet.**

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s38-m0001 | accepted | train | qwen3-small 1.00 |  |
| s38-m0002 | accepted (label pending) | train |  |  |
| s38-m0003 | rejected at rubric_tests |  |  | gold_fails: ["C9", "C10"] |

## Variety

- Industries: organic dairy (1), independent film distribution (1), seed genetics (1)
- Agreement types: software license agreement (1), supply agreement (1), master services agreement (1)
- Issue types: liability_cap_carveout (2), change_of_control_consent (2), governing_law_mismatch (2), expired_notice_window (1), auto_renewal (1), exclusivity_scope (1), uncapped_indemnity (1), defined_term_inconsistency (1), missing_assignment_restriction (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 168564 | 49202 | 0 |
| drafter | 12 | 175198 | 67059 | 0 |
| fact_extractor | 3 | 77896 | 6120 | 0 |
| fact_matcher | 3 | 5686 | 983 | 0 |
| instruction_writer | 3 | 4170 | 985 | 0 |
| issue_verifier | 12 | 274814 | 7855 | 0 |
| judge | 23 | 116342 | 13206 | 9 |
| ledger_writer | 3 | 12289 | 22335 | 0 |
| rubric_writer | 3 | 18964 | 7556 | 0 |
| solver | 142 | 459301 | 68192 | 0 |
