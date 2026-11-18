# MINUTES: QUARTERLY QUALITY REVIEW AND GEBV MODEL VALIDATION MEETING

**Meeting Date:** August 19, 2026
**Time:** 1:00 p.m. – 3:15 p.m. U.S. Central Time
**Format:** Video conference
**Prepared by:** Figos Analytics, LLC (Scientific Quality)
**Circulated:** August 28, 2026
**Reference:** Quality Agreement dated January 15, 2024, Sections 3.2 and 7; Order Form No. OF-001, Special Terms Sections 1 to 3

---

## 1. ATTENDEES

| **Name** | **Organization** | **Role** |
|---|---|---|
| Dr. Samuel K. Ostrander | Traimand Seed Genetics, Inc. | Director of Breeding Informatics; Customer Quality Representative |
| Dr. Lena M. Achterberg | Traimand Seed Genetics, Inc. | Senior Quantitative Geneticist, Corn |
| Marcus J. Telford | Traimand Seed Genetics, Inc. | Lead Data Engineer, Breeding Informatics |
| Dr. Priya N. Halvorsen | Figos Analytics, LLC | Director, Scientific Quality; Licensor Quality Representative |
| Dr. Tomas E. Ekberg | Figos Analytics, LLC | Named Account Scientist (Order Form Special Terms Section 3) |
| Rachel T. Lindqvist | Figos Analytics, LLC | VP, Customer Accounts |

## 2. AGENDA

1. Open data integrity deviations
2. Planned Model Changes
3. Validation Report VR-2026-03 (Marker QC and Relationship Matrix Update)
4. Security Incidents
5. Other business and action items

## 3. OPEN DATA INTEGRITY DEVIATIONS

3.1 Dr. Halvorsen reported one deviation closed since the Q2 review. Deviation DV-2026-02 was notified to Customer on May 6, 2026 under Quality Agreement Section 6.2. It concerned a duplicated environment identifier in the 2025 soybean Maturity Group II trial set. That duplication caused two locations to be pooled in the May 4 production run.

3.2 Figos re-ran the affected computations under Quality Agreement Section 6.3 and delivered corrected GEBVs on May 11, 2026. The written corrective and preventive action plan was delivered on May 29, 2026. The plan added a uniqueness check on location-year identifiers to the automated validation rules under Quality Agreement Section 6.1(b).

3.3 Mr. Telford confirmed that Traimand reviewed the corrected results and that no selection decisions were made on the uncorrected run. **DV-2026-02 is closed.**

3.4 No deviations are open.

## 4. PLANNED MODEL CHANGES

4.1 Dr. Ekberg presented one planned Model Change, MC-2026-03, with two components:

(a) **Marker QC thresholds.** The call-rate threshold rises from 0.90 to 0.95. The minor allele frequency threshold falls from 0.05 to 0.02 for corn only. Soybean remains at 0.05.

(b) **Relationship matrix blending.** The default blending weight between the genomic (G) and pedigree (A) relationship matrices in ssGBLUP changes from 0.95/0.05 to 0.90/0.10. The change is intended to reduce inflation of GEBVs for lines with sparse genotyping.

4.2 The Validation Protocol, VP-2026-03, was delivered to Dr. Ostrander on July 8, 2026. Traimand provided written comments on July 17, 2026, requesting that results be broken out separately for corn Relative Maturity groups 95–105 and 106–115. Figos incorporated the comments. Traimand approved the revised protocol on July 22, 2026.

4.3 Ms. Lindqvist confirmed that Figos will not deploy MC-2026-03 to the Production Environment during the breeding season change freeze under Order Form Special Terms Section 1. **The proposed deployment date is November 10, 2026,** subject to acceptance of the Validation Report.

4.4 No other Model Changes are planned for the remainder of 2026.

## 5. VALIDATION REPORT VR-2026-03

5.1 Figos delivered Validation Report VR-2026-03 to Dr. Ostrander on August 12, 2026. Validation was executed in the Validation Environment using Traimand's historical datasets held on the Platform. The design was the forward-validation scheme specified in VP-2026-03: training on trial seasons through 2023 and validating on 2024 and 2025 phenotypes.

5.2 Dr. Ekberg summarized results against the acceptance criteria:

| **Metric** | **Acceptance Criterion** | **Corn RM 95–105** | **Corn RM 106–115** | **Soybean (all MGs)** |
|---|---|---|---|---|
| Change in predictive ability (proposed minus current) | ≥ -0.01 | +0.03 | +0.02 | +0.01 |
| Rank correlation of GEBVs, current vs. proposed | ≥ 0.90 | 0.96 | 0.95 | 0.97 |
| Regression bias (slope of phenotype on GEBV) | 0.90 – 1.10 | 0.98 | 0.96 | 1.02 |
| Top-10% retention | ≥ 80% | 88% | 86% | 91% |

5.3 All acceptance criteria were met for every crop and maturity grouping. No deviations from VP-2026-03 were recorded.

5.4 Dr. Achterberg asked whether the reduction in the corn minor allele frequency threshold increased the number of markers retained for the doubled-haploid inbred panels. Dr. Ekberg confirmed that roughly 4,200 additional markers per line are retained on average in corn. He also confirmed that the computation time impact is within the Platform's normal run window. Both points are described in Appendix C of the Validation Report.

5.5 Dr. Ostrander noted that Traimand's review is under way. He confirmed that Traimand will deliver written acceptance or rejection within the ten (10) business days provided in Quality Agreement Section 7.3, that is, **by August 26, 2026**.

5.6 Dr. Halvorsen confirmed that the current model version will be retained for at least twelve (12) months after deployment under Quality Agreement Section 7.5. She also confirmed that Traimand may request comparison re-runs under that version during that period.

## 6. SECURITY INCIDENTS

6.1 No Security Incidents have been notified under License Agreement Section 9.2 since the previous quarterly review.

6.2 Ms. Lindqvist noted that Figos completed its annual SOC 2 Type II examination in June 2026. The report is available to Traimand on request under License Agreement Section 9.6.

## 7. OTHER BUSINESS

7.1 Mr. Telford asked whether the quarterly user-access review under Quality Agreement Section 4.3 had been completed for Q3. Dr. Halvorsen confirmed it was completed on August 3, 2026, and that two Figos support accounts were deprovisioned. Figos will provide the access review summary with these minutes.

7.2 There is no change to the subcontractor list provided to Traimand in February 2026.

7.3 The Q4 quarterly review is tentatively scheduled for November 18, 2026, after the planned deployment of MC-2026-03.

## 8. ACTION ITEMS

| **No.** | **Action** | **Owner** | **Due** |
|---|---|---|---|
| 1 | Deliver written acceptance or rejection of VR-2026-03 | S. Ostrander | August 26, 2026 |
| 2 | Circulate Q3 user-access review summary with these minutes | P. Halvorsen | August 28, 2026 |
| 3 | On acceptance, update Change Control Record for MC-2026-03 and confirm deployment window | T. Ekberg | September 4, 2026 |
| 4 | Provide SOC 2 Type II report on Traimand's request | R. Lindqvist | On request |
| 5 | Issue calendar invitation for Q4 quarterly review | R. Lindqvist | September 30, 2026 |

---

*These minutes are circulated under Quality Agreement Section 3.2. Please send any corrections to Dr. Priya N. Halvorsen within five (5) business days after receipt.*