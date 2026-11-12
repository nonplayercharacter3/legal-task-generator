# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Bredeix Organic Creamery, LLC – Risk Review of Laipeisk Systems Software Package

---

## Executive Summary

I have reviewed the four documents in the matter folder: the Software License and Services Agreement (the "Agreement"), Statement of Work No. 2 – Phase 2 Implementation (the "SOW"), the Data Processing Addendum (the "DPA"), and the Halverston Risk Partners insurance certificate cover letter dated October 26, 2026 (the "Cover Letter"). I identify twelve issues below, ordered by materiality to Bredeix. Three issues are flagged as requiring a call with the client before we respond to Laipeisk.

---

## Issue 1 – Change of Control Gives Laipeisk a Termination Right That Collides with the Northfold Transaction

**Document / Section:** Agreement § 16.2; SOW § 1.2(b)–(c)

**What it says:** Section 16.2 provides that any "direct or indirect change in control of Licensee, including any change in control of any entity that directly or indirectly controls Licensee" is deemed an assignment requiring Licensor's prior written consent. Without consent, Laipeisk may terminate the Agreement on 30 days' written notice. The SOW § 1.2(b) expressly acknowledges that the sole owner of Bredeix Dairy Holdings (Bredeix's parent) signed a Unit Purchase Agreement with Northfold Provisions Group, with closing expected in Q1 2027. SOW § 1.2(c) then states: "Nothing in this SOW constitutes Licensor's consent under Section 16.2 of the Agreement."

**Why it matters:** Phase 2 go-live is scheduled for April 19, 2027 (SOW § 5.1), with hypercare covering two semi-monthly pay cycles thereafter (SOW § 3.2(h)). The Northfold closing is expected in Q1 2027. If the transaction closes before go-live, Laipeisk can terminate the entire Agreement—including the Phase 2 SOW—on 30 days' notice. Bredeix would lose the platform mid-implementation, forfeit its $412,000 Phase 2 investment (to the extent milestones are not yet accepted), and be without a payment-processing system during a corporate transition. Even if the closing occurs after go-live, the termination right creates leverage that Laipeisk can exploit in any subsequent negotiation.

**Recommended fix:** We need Laipeisk's written consent to the Northfold change of control as a condition of closing, or an amendment to § 16.2 that carves out this specific transaction. Proposed language:

> "Notwithstanding the foregoing, Licensor hereby consents to the change in control of Bredeix Dairy Holdings, LLC resulting from the Unit Purchase Agreement dated August 28, 2026 between the sole owner of Bredeix Dairy Holdings, LLC and Northfold Provisions Group, and any subsequent integration of Bredeix Organic Creamery, LLC into the Northfold Provisions Group corporate structure resulting from that transaction. This consent is irrevocable and shall not be conditioned on any further action by Licensee."

Alternatively, if the client prefers a broader fix:

> "A Change of Control of Licensee shall not require Licensor's consent if, following the Change of Control, the surviving or acquiring entity (a) is not a direct competitor of Licensor in the dairy software market, and (b) assumes Licensee's obligations under this Agreement in writing."

**⚠️ CALL WITH CLIENT BEFORE RESPONDING:** This is the single most urgent issue. We need to confirm (a) the expected closing date for the Northfold transaction, (b) whether the deal team has addressed the Laipeisk consent as a condition or covenant, and (c) the client's risk tolerance for proceeding without consent. If closing is imminent, we may need to escalate this to Laipeisk immediately rather than bundling it with other negotiation points.

---

## Issue 2 – DPA Overrides the Agreement's Uncapped Data-Security Liability

**Document / Section:** DPA § 8.1; Agreement § 11.3(c)

**What it says:** Agreement § 11.3(c) provides that the liability cap in § 11.2 does **not** apply to "a Party's breach of Section 9 (Confidentiality and Data Security)." This is a critical protection: it means a data security breach by Laipeisk is uncapped. However, DPA § 8.1 states: "Notwithstanding Section 11.3(c) of the Agreement, each party's aggregate liability arising out of or relating to this Addendum, including any Personal Data Breach, shall be subject to the Cap." The "Cap" is defined in Agreement § 11.2 as Fees paid in the 12 months preceding the claim.

**Why it matters:** The DPA has order of precedence over the Agreement for Personal Data matters (Agreement § 1.3). So DPA § 8.1 controls. The net effect is that if Laipeisk suffers a breach exposing farmer-supplier bank account numbers, routing numbers, taxpayer identification numbers, and payment records (all listed in DPA Annex 1), Bredeix's recovery is capped at roughly 12 months of subscription fees. For an organic dairy processor with hundreds of small-farm suppliers, a breach of this data could trigger SHIELD Act notification obligations, regulatory exposure, consumer claims, and reputational harm that far exceed the cap. The cap also applies to the breach-cost reimbursement in DPA § 7.5 (forensics, credit monitoring, call-center, notification costs).

**Recommended fix:** Strike DPA § 8.1 in its entirety, or replace with:

> "8.1 **Cap.** Section 11 of the Agreement applies to liability arising out of or relating to this Addendum. For the avoidance of doubt, the exclusions in Section 11.3 of the Agreement (including the exclusion for breach of Section 9) apply to this Addendum. The Cap shall not limit Licensor's obligations under Section 7.5 (Costs) of this Addendum."

If Laipeisk resists full uncapping, a fallback is a super-cap for data breaches:

> "Notwithstanding the foregoing, Licensor's aggregate liability for a Personal Data Breach shall not exceed [3× the Cap / $X,000,000], provided that this super-cap shall not limit Licensor's indemnification obligations under Section 10 of the Agreement."

**⚠️ CALL WITH CLIENT BEFORE RESPONDING:** We should confirm with the client (a) the approximate number of farmer-suppliers whose data is in the system, (b) whether any of those suppliers are subject to additional contractual confidentiality obligations that Bredeix has assumed, and (c) the client's view on what an acceptable super-cap would be. This will help us calibrate the ask.

---

## Issue 3 – Insurance Does Not Meet the Contractual Rating Threshold; Broker Made a False Certification

**Document / Section:** Agreement § 12.1; Cover Letter § 2.1 (table) and § 2.2

**What it says:** Agreement § 12.1 requires Licensor to maintain insurance "with insurers rated A- VII or better by A.M. Best." The Cover Letter table shows:

| Insurer | Rating shown |
|---|---|
| Ashmore Mutual (CGL) | A VIII |
| Corvane Specialty (Tech E&O / Cyber) | A XI |
| Pell Harbor Casualty (Workers' Comp) | A- VIII |

On the A.M. Best scale, the Roman numerals within a letter grade run from I (highest) to XI (lowest). "A- VII or better" therefore means A- I through A- VII. All three insurers fall **below** the required threshold: A- VIII and A- XI are worse than A- VII.

Despite this, Cover Letter § 2.2 states: "Each insurer listed above holds an A.M. Best rating of A- VII or better." This is a false representation.

**Why it matters:** First, Laipeisk is in technical breach of § 12.1 as of the Effective Date (or at least as of the current policy period beginning July 1, 2026). Second, the broker's false certification undermines the reliability of the entire insurance package. Third, if a major claim arises (e.g., a data breach triggering the $5M cyber policy), the financial strength of the insurer matters. An A- XI-rated insurer is at the lowest tier of the "Good" category and may have less capacity to pay a large claim.

**Recommended fix:**

1. Demand that Laipeisk either (a) replace the non-compliant insurers with carriers rated A- VII or better, or (b) provide evidence that the ratings shown are in error and the actual ratings meet the threshold.
2. Send a written notice to Laipeisk identifying the discrepancy and demanding cure within 30 days, preserving Bredeix's rights under § 14.3 (termination for material breach) if not cured.
3. Request that the broker issue a corrected cover letter.

Proposed notice language:

> "We write in response to the certificate of insurance and cover letter dated October 26, 2026. Section 12.1 of the Agreement requires insurers rated A- VII or better by A.M. Best. The cover letter at § 2.2 represents that all listed insurers meet this threshold. However, the ratings shown in the § 2.1 table (A- VIII for Ashmore Mutual and Pell Harbor Casualty; A- XI for Corvane Specialty) do not meet the required standard. Please provide either (a) corrected certificates showing compliant ratings, or (b) evidence that the ratings in the table are in error, within thirty (30) days."

---

## Issue 4 – Phase 1 Deemed Acceptance Dispute

**Document / Section:** SOW § 2.2; Agreement § 6.2

**What it says:** Delivery of the Phase 1 Deliverable was made on July 20, 2026 (SOW § 2.1). Bredeix's Rejection Notice is dated August 7, 2026 (SOW § 2.2)—18 days after Delivery. Agreement § 6.2 requires a Rejection Notice within 10 days; otherwise the Deliverable is "deemed accepted." Laipeisk contends the notice was late and Phase 1 is accepted. Bredeix disputes this and "reserves all rights."

The identified defects are material to Bredeix's operations: (a) duplicate producer records in the master file, (b) component test results (butterfat, protein, somatic cell count) posting to the wrong producer account, and (c) incorrect organic premium rates for producers with certification renewals in the current pay period.

**Why it matters:** If Phase 1 is deemed accepted, Bredeix has lost its contractual right to require correction under § 6.3 and its right to terminate under § 6.4 for repeated failure. The Phase 1 milestone fee becomes unconditionally payable. More practically, the defects described—particularly misapplied organic premiums and misposted quality results—directly affect producer pay accuracy. If these defects persist into Phase 2 (which builds on the Phase 1 data foundation), they will compound.

**Recommended fix:**

1. **Short-term:** Press Laipeisk to confirm in writing that it will remediate the three items as part of Phase 2 data-readiness (SOW § 2.3 already contemplates this), with a specific deadline and acceptance criteria tied to D2-1.
2. **Medium-term:** Negotiate a stipulation that the Phase 1 milestone fee is held in abeyance (or that Bredeix's payment is conditioned on remediation) until the three defects are verified as corrected.
3. **Preserve the dispute:** Ensure Bredeix's reservation of rights in SOW § 2.2 is not inadvertently waived by proceeding with Phase 2 without a side letter.

Proposed side-letter language:

> "The Parties acknowledge the dispute regarding the timeliness of Licensee's Rejection Notice dated August 7, 2026. Without prejudice to either Party's position, Licensor shall remediate the items identified in SOW § 2.2(a)–(c) as part of the Data Readiness activities under SOW § 3.2(a), and such remediation shall be a condition to acceptance of Deliverable D2-1. The Phase 1 milestone fee shall be held in abeyance until D2-1 is accepted."

**⚠️ CALL WITH CLIENT BEFORE RESPONDING:** We need to understand (a) whether the Phase 1 defects are still present in the live system and, if so, whether they have caused any actual producer pay errors; (b) whether Bredeix has already paid the Phase 1 milestone fee; and (c) the client's commercial appetite to hold the Phase 1 fee as leverage versus accepting a remediation commitment and moving forward.

---

## Issue 5 – Claims-Made Policies Create a Coverage Gap Around Go-Live

**Document / Section:** Cover Letter § 2.1 (policy period), § 2.3; SOW § 5.1 (go-live date)

**What it says:** The Tech E&O and Cyber Liability policies are written on a **claims-made** basis. The current policy period runs July 1, 2026 to July 1, 2027. Phase 2 go-live is April 19, 2027, and hypercare covers two semi-monthly pay cycles (SOW § 3.2(h)), extending roughly to mid-to-late June 2027. The retroactive date is January 1, 2019 (Cover Letter § 2.3), which is acceptable.

**Why it matters:** A claims-made policy only covers claims **made** during the policy period (or during an extended reporting period, if purchased). If a data breach or software defect occurs during go-live or hypercare (April–June 2027) but the claim is not made until after July 1, 2027, the current policy will not respond. Given that data breaches are often discovered weeks or months after the initial intrusion, and that payment errors may not surface until a producer disputes a settlement statement, this gap is real.

**Recommended fix:**

1. Require Laipeisk to purchase a 60- to 90-day extended reporting period (tail coverage) on the claims-made policies at the July 1, 2027 renewal, at Laipeisk's cost, as a condition of the Phase 2 SOW.
2. Alternatively, require the renewed policies (effective July 1, 2027) to maintain the same or earlier retroactive date and the same or greater limits, with evidence provided to Bredeix before the current policies expire.
3. Add to the SOW:

> "Licensor shall maintain the Technology Errors and Omissions and Cyber Liability policies (or equivalent coverage) in force throughout the hypercare period and for at least ninety (90) days thereafter, with limits no less than those set forth in Section 12.1 of the Agreement. Licensor shall provide evidence of such coverage to Licensee before the expiration of the current policy period."

---

## Issue 6 – Bredeix Is Not an Additional Insured on the Tech E&O or Cyber Policies

**Document / Section:** Cover Letter § 3.1; Agreement § 12.2

**What it says:** Agreement § 12.2 requires Bredeix to be "named as an additional insured on the commercial general liability policy." The Cover Letter confirms this for the CGL policy only (§ 3.1). There is no additional insured status on the Tech E&O or Cyber Liability policies.

**Why it matters:** If a software defect causes a payment error that results in a third-party claim against Bredeix (e.g., a producer sues Bredeix for underpayment), or if a data breach triggers a class action against Bredeix as the data controller, Bredeix cannot directly claim under Laipeisk's Tech E&O or Cyber policies. Bredeix would have to sue Laipeisk contractually and then rely on Laipeisk's insurance—subject to the liability cap and any insolvency risk.

**Recommended fix:** Amend Agreement § 12.2 to add:

> "Licensee shall be named as an additional insured on the technology errors and omissions policy and the cyber liability and network security policy, or, if the insurers do not permit additional insured status on those policies, Licensor shall provide a direct-claim endorsement or a loss-payable clause in favor of Licensee."

If Laipeisk resists, at minimum require that the Tech E&O and Cyber policies name Bredeix as a "certified holder" with direct notice of any claim, cancellation, or material change.

---

## Issue 7 – Auto-Renewal for Five-Year Terms with a Narrow Notice Window

**Document / Section:** Agreement § 14.2

**What it says:** After the 3-year Initial Term, the Agreement auto-renews for successive **five-year** terms unless either party gives non-renewal notice between 120 and 90 days before the end of the then-current term.

**Why it matters:** A five-year renewal is an extremely long commitment for a software platform, particularly one that is still in implementation. The notice window (90–120 days) is narrow and easy to miss. If Bredeix is integrated into the Northfold structure and the new parent wants to consolidate onto a different platform, a five-year lock-in is a significant constraint. Combined with the change-of-control termination right (Issue 1), Bredeix is in a bind: it can either get consent and be locked in for five years, or refuse consent and risk termination.

**Recommended fix:** Amend § 14.2:

> "On expiry of the Initial Term, this Agreement shall renew automatically for successive one (1) year Renewal Terms unless either Party gives the other written notice of non-renewal at least ninety (90) days before the end of the then-current term."

Or, if Laipeisk insists on longer terms:

> "…successive two (2) year Renewal Terms… unless either Party gives written notice of non-renewal at least one hundred twenty (120) days before the end of the then-current term."

---

## Issue 8 – No Service Credits or Remedies for Downtime

**Document / Section:** Agreement § 4.2

**What it says:** Licensor shall use "commercially reasonable efforts" to make the Software available 99.5% of the time per calendar month. There is no service credit, no termination right for chronic unavailability, and no other remedy specified for failure to meet the 99.5% threshold.

**Why it matters:** 99.5% monthly availability permits up to ~3.6 hours of downtime per month. For a system that processes semi-monthly producer payments, an outage during a pay-cycle window could delay payments to hundreds of farmers. "Commercially reasonable efforts" is a low standard and provides no enforceable remedy.

**Recommended fix:** Add a service-credit schedule:

> "If the Software's availability in any calendar month falls below 99.5%, Licensor shall credit Licensee the following percentage of that month's pro rata subscription fee: 99.0%–99.5%: 10%; 98.0%–98.9%: 25%; below 98.0%: 50%. If availability falls below 95% in two consecutive months, Licensee may terminate this Agreement under Section 14.3 without cure period and receive a pro rata refund of prepaid fees."

---

## Issue 9 – Schedule Uses "Commercially Reasonable Efforts" Without Consequences for Delay

**Document / Section:** SOW § 5.1

**What it says:** "Licensor shall use commercially reasonable efforts to give Delivery of each Phase 2 Deliverable by the following target dates." There is no liquidated damages clause, no termination right for material delay, and no definition of what constitutes a material delay.

**Why it matters:** The Phase 2 schedule is tightly coupled to the Northfold integration timeline (SOW § 1.2(c)). If go-live slips past Q1 2027, Bredeix may be entering a corporate transition without its payment system fully operational. "Commercially reasonable efforts" gives Laipeisk wide latitude to miss dates without consequence.

**Recommended fix:**

> "The target dates in Section 5.1 are firm. If Licensor fails to deliver any Deliverable by its target date for reasons other than Licensee's failure to meet its responsibilities under Section 7, Licensor shall pay Licensee liquidated damages of $[X] per calendar day of delay, up to a maximum of [Y]% of the applicable milestone fee. If any Deliverable is delayed by more than thirty (30) days, Licensee may terminate this SOW under Section 14.3 of the Agreement without cure period."

---

## Issue 10 – "Acceptance Upon Use" Creates Inadvertent Acceptance Risk

**Document / Section:** Agreement § 6.5

**What it says:** "Licensee's use of a Deliverable in a live production environment for its business purposes, other than for testing, constitutes acceptance of that Deliverable."

**Why it matters:** During go-live (D2-6), the system will be in production. If a defect is discovered after the first pay cycle but before formal acceptance testing is complete, Bredeix's use of the system in production could be construed as acceptance, waiving its right to reject under § 6.2. This is particularly risky for D2-2 (Payment Module), where the parallel testing requirement (SOW § 4.3) is meant to catch errors before production use.

**Recommended fix:** Amend § 6.5:

> "Licensee's use of a Deliverable in a live production environment constitutes acceptance only if (a) the Deliverable has been formally delivered under Section 6.1, and (b) the applicable rejection period under Section 6.2 has expired without a Rejection Notice. Use of a Deliverable in a production environment prior to formal Delivery shall not constitute acceptance."

Alternatively, add to the SOW:

> "For Deliverable D2-6 (Production Go-Live), acceptance shall occur only upon completion of the hypercare period in Section 3.2(h) and written confirmation by Licensee's project manager that no material defects remain open."

---

## Issue 11 – Software Warranty Provides No Remedy for Operational Loss

**Document / Section:** Agreement § 8.2

**What it says:** The Software warranty's exclusive remedy is for Licensor to correct the nonconformity within 30 days, failing which Licensee may terminate and receive a pro rata refund of prepaid subscription fees. There is no damages remedy for losses caused by software failure.

**Why it matters:** If the payment module miscalculates organic premiums or misdirects ACH payments (the same types of errors already identified in Phase 1), Bredeix faces direct financial losses: overpayments to producers that may be unrecoverable, underpayments that trigger producer disputes and potential regulatory complaints (dairy payment regulations), and the cost of manual correction. The exclusive-remedy clause means Bredeix's only recourse is to get the bug fixed or walk away—no compensation for the losses already suffered.

**Recommended fix:** Carve out payment-accuracy failures from the exclusive remedy:

> "Notwithstanding the foregoing, if the Software's payment calculation modules produce results that deviate from the Specifications by more than [X]% in aggregate for any pay cycle, Licensee's remedy shall include, in addition to correction, reimbursement of documented out-of-pocket costs incurred to manually correct producer payments, up to the Cap."

---

## Issue 12 – General Liability Cap May Be Inadequate for a Payment-Processing Platform

**Document / Section:** Agreement § 11.2

**What it says:** Each party's aggregate liability is capped at "Fees paid by Licensee in the 12 months preceding the claim."

**Why it matters:** The first-year subscription fee is not stated in the Agreement (Schedule A refers to an "order form countersigned by Licensee," which is not in the folder). The Phase 2 fixed fee is $412,000. If the annual subscription is, say, $200,000–$300,000, the cap is roughly $600,000–$700,000. A single payment-cycle error affecting hundreds of producers could exceed this. A data breach (subject to the DPA cap issue in Issue 2) could easily exceed it as well.

**Recommended fix:** Increase the cap to at least 2× annual fees, or set a fixed dollar floor:

> "…shall not exceed the greater of (a) the Fees paid by Licensee in the twelve (12) months preceding the claim, or (b) $[2,000,000]."

---

## Summary of Items Requiring a Client Call Before We Respond to Laipeisk

| # | Issue | Why a call is needed |
|---|---|---|
| 1 | Change of control / Northfold closing | Need closing timeline, deal-team awareness, and client's strategic position |
| 2 | DPA liability cap override | Need data-volume context and client's risk appetite for a super-cap |
| 4 | Phase 1 deemed acceptance | Need to confirm whether defects are still live, whether the fee was paid, and the client's leverage assessment |

---

## Additional Observations (Lower Priority)

- **Agreement § 10.1 (IP Indemnity):** Limited to U.S. patents, copyrights, trademarks, and trade secrets. If Bredeix operates in Canada or is subject to foreign producer claims, the indemnity may not reach. Low risk given the domestic focus, but worth confirming.

- **DPA § 6.3 (New Subprocessors):** 30-day notice and objection right, with termination as the sole remedy for an unresolved objection. This is reasonable but note that termination of "affected Services" could fragment the platform if a subprocessor issue arises.

- **SOW § 3.3 (Out of Scope):** Historical producer pay data before January 1, 2025 is excluded. If Bredeix needs audit trails or year-over-year comparisons for organic certification or cooperative reporting, this gap should be addressed by change order before go-live.

- **Cover Letter § 5.2:** The broker offers to add entities as certificate holders "with Laipeisk's instructions." If the Northfold transaction closes and Bredeix becomes a subsidiary, the parent or the new holding entity may want certificate-holder status. Flag for the deal team.

---

*Prepared from the four documents in the matter folder. Schedule A (subscription fee amount) and SOW Exhibit 1 (Phase 2 Functional Requirements v1.3) were referenced but not provided in the folder; my analysis assumes their terms are consistent with the body of the Agreement and SOW as written.*