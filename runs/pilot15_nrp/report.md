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

Bundled issue criteria (`gates.check_bundling`): 1 matter(s) flagged in the final rubric; 0 repair(s) ran, 0 cleared.

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |
| qwen3-small | 2 | 0.33: 1, 0.67: 1 |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s15-m0001 | accepted | train | qwen3-small 0.67 |  |
| s15-m0002 | accepted | train | qwen3-small 0.33 |  |
| s15-m0003 | rejected at rubric_tests |  |  | flawed_wrongly_fails: ["C8", "C9"] |

## Variety

- Industries: regional airline catering (1), commercial bakery (1), boutique hotels (1)
- Agreement types: stock purchase agreement (1), distribution agreement (1), asset purchase agreement (1)
- Issue types: governing_law_mismatch (2), change_of_control_consent (2), defined_term_inconsistency (1), expired_notice_window (1), liability_cap_carveout (1), exclusivity_scope (1), missing_assignment_restriction (1), auto_renewal (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 182082 | 47532 | 0 |
| drafter | 12 | 188442 | 76601 | 0 |
| fact_extractor | 3 | 87234 | 6900 | 0 |
| fact_matcher | 3 | 4101 | 494 | 0 |
| instruction_writer | 3 | 4138 | 1128 | 0 |
| issue_verifier | 11 | 278643 | 8812 | 0 |
| judge | 17 | 141712 | 14529 | 0 |
| ledger_writer | 3 | 12266 | 22803 | 0 |
| rubric_writer | 3 | 17292 | 5365 | 0 |
| solver | 108 | 857340 | 109171 | 0 |
