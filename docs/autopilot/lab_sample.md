# Frozen LAB sample (M3)

Frozen 2026-11-19 by the autopilot. The LAB side of the before/after comparison: 30 LAB tasks drawn by
`scripts/lab_sample.py draw` (seed 46, tasks with at most 200 criteria): 20 from corporate-ma and contracts
(`lab_slice`, the area our tasks resemble) and 10 from other practice areas (`lab_other`). Paths and criteria
counts only, no LAB text. Every LAB score in this project's comparisons uses exactly these 30 tasks, Qwen
`qwen3-small` at `reasoning_effort = low` through LAB's own runner, one Opus SDK judge with LAB's grader prompt,
tag `s1`. The draw is in `runs/lab_sample/sample.json` (local).

| # | set | criteria | task |
|---|---|---|---|
| 1 | lab_slice | 40 | `contracts/commercial-channel-partnerships/strategic-partnership-co-sell-first-turn-redline/scenario-03` |
| 2 | lab_slice | 79 | `contracts/ip-licensing/license-agreement-first-draft/scenario-01` |
| 3 | lab_slice | 57 | `contracts/banking/repo-securities-lending-first-turn-redline/scenario-01` |
| 4 | lab_slice | 76 | `corporate-ma/draft-vendor-due-diligence-report` |
| 5 | lab_slice | 58 | `corporate-ma/draft-tsa-markup` |
| 6 | lab_slice | 31 | `contracts/corporate-ma/stock-purchase-agreement-term-negotiation` |
| 7 | lab_slice | 57 | `corporate-ma/review-outside-counsel-engagement-letter` |
| 8 | lab_slice | 78 | `corporate-ma/compare-ddrl-to-vdr-index/scenario-01` |
| 9 | lab_slice | 59 | `contracts/commercial-vendor-customer/saas-api-subscription-subsequent-turn-redline/scenario-03` |
| 10 | lab_slice | 62 | `corporate-ma/draft-transaction-nda/scenario-01` |
| 11 | lab_slice | 54 | `corporate-ma/draft-data-room-population-plan/scenario-02` |
| 12 | lab_slice | 63 | `contracts/banking/isda-master-pack-subsequent-turn-redline/scenario-01` |
| 13 | lab_slice | 82 | `contracts/banking/isda-master-pack-playbook-escalation/scenario-02` |
| 14 | lab_slice | 41 | `contracts/commercial-channel-partnerships/strategic-partnership-co-sell-counterparty-paper-review/scenario-01` |
| 15 | lab_slice | 114 | `contracts/financing/credit-lending-counterparty-paper-review/scenario-01` |
| 16 | lab_slice | 55 | `corporate-ma/review-material-contract-review` |
| 17 | lab_slice | 41 | `contracts/commercial-channel-partnerships/channel-distribution-first-turn-redline/scenario-02` |
| 18 | lab_slice | 93 | `contracts/commercial-vendor-customer/saas-api-subscription-first-draft/scenario-01` |
| 19 | lab_slice | 58 | `corporate-ma/draft-exit-closing-checklist` |
| 20 | lab_slice | 57 | `contracts/employment-compensation/employment-agreement-playbook-escalation/scenario-01` |
| 21 | lab_other | 45 | `international-trade-sanctions/review-technology-control-plan/scenario-02` |
| 22 | lab_other | 4 | `firm-knowledge/tasks/200` |
| 23 | lab_other | 71 | `corporate-governance/assess-impact-of-new-state-privacy-law-on-multi` |
| 24 | lab_other | 64 | `healthcare-life-sciences/draft-response-to-civil-investigative-demand` |
| 25 | lab_other | 101 | `intellectual-property/extract-license-grant-terms-from-executed-technology-agreements` |
| 26 | lab_other | 101 | `funds-asset-management/draft-compliance-manual` |
| 27 | lab_other | 52 | `emerging-companies-venture-capital/analyze-counterparty-markup-of-bridge-loan-agreement` |
| 28 | lab_other | 86 | `intellectual-property/draft-saas-subscription-agreement` |
| 29 | lab_other | 63 | `intellectual-property/draft-motion-in-limine` |
| 30 | lab_other | 85 | `capital-markets/draft-equity-incentive-plan` |

Total criteria: 1927 (one judge call each).
