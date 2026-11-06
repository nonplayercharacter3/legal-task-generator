# Run report

Backend: `claude_sdk`. Accepted **0 of 3** candidate matters.

## Gates

| Gate | Evaluated | Passed | Failed | Skipped |
| --- | ---: | ---: | ---: | ---: |
| ledger_schema | 3 | 3 | 0 | 0 |
| consistency | 3 | 3 | 0 | 0 |
| issue_check | 3 | 3 | 0 | 0 |
| leak_check | 3 | 3 | 0 | 0 |
| rubric_trace | 3 | 1 | 2 | 0 |
| rubric_tests | 1 | 0 | 1 | 0 |
| decontamination | 0 | 0 | 0 | 0 |
| solver_check | 0 | 0 | 0 | 0 |

Rubric repairs for bundled issue criteria (`gates.check_bundling`): 3 ran, 1 cleared; 2 matter(s) still had bundled clauses in the final rubric.

## Difficulty

Pass rates of the accepted tasks per labelling model. Difficulty is a label, not a filter: whoever trains picks the band that fits their model.

| Model | Tasks | Pass rate: tasks |
| --- | ---: | --- |

## Matters

| Matter | Result | Split | Pass rate per model | Reason |
| --- | --- | --- | --- | --- |
| s13-m0001 | rejected at rubric_tests |  |  | gold_fails: ["C8"] |
| s13-m0002 | rejected at rubric_trace |  |  | errors: ["criterion C1 requires a harm, remedy or provision that issue I1's expected_finding does not name: 'The response must locate the issue in Amendment No. |
| s13-m0003 | rejected at rubric_trace |  |  | errors: ["criterion C3 requires a harm, remedy or provision that issue I3's expected_finding does not name: 'The response locates the issue in the Seller Note ( |

## Variety

- Industries: industrial textiles (1), video game publishing (1), data center cooling (1)
- Agreement types: stock purchase agreement (2), distribution agreement (1)
- Issue types: missing_assignment_restriction (2), defined_term_inconsistency (2), liability_cap_carveout (2), uncapped_indemnity (2), governing_law_mismatch (1), auto_renewal (1), expired_notice_window (1), change_of_control_consent (1), survival_gap (1)
- Party names used in more than one matter: none
- Identical issue sets: none

## Model calls

| Role | Calls | Input tokens | Output tokens | Errors |
| --- | ---: | ---: | ---: | ---: |
| answer_writer | 6 | 221414 | 54107 | 0 |
| drafter | 15 | 305760 | 96037 | 0 |
| fact_extractor | 3 | 105098 | 7218 | 0 |
| fact_matcher | 3 | 3620 | 425 | 0 |
| instruction_writer | 3 | 4291 | 1191 | 0 |
| issue_verifier | 13 | 395346 | 8117 | 0 |
| judge | 3 | 20561 | 2661 | 0 |
| ledger_writer | 3 | 12328 | 29947 | 0 |
| rubric_writer | 6 | 44611 | 10857 | 0 |
