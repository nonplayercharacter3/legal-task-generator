# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Timais Outdoor Co. / Pesith Apparel Manufacturing, LLC – MSA Package Review

---

## Summary

The package consists of a Master Services Agreement (MSA), a Quality Agreement, a Data Processing Addendum (DPA), and an insurance certificate cover letter from Pesith's broker. The MSA is reasonably well-drafted overall but contains several provisions that are materially unfavorable to Timais or that leave critical commercial terms unresolved. The DPA contains a significant structural problem: it shifts essentially all data-protection risk onto Timais while capping Pesith's own exposure. Schedules B and C are placeholders, meaning the financial and service-level terms are not yet agreed. I have identified the issues below in order of significance.

---

## Tier 1 – Critical Issues

### 1. DPA Section 8.2: One-Sided, Uncapped Indemnification from Timais to Pesith

**Where:** DPA § 8.2; see also DPA § 8.1 and MSA § 11.

**The issue.** Section 8.2 requires Timais (as Controller) to indemnify Pesith (as Processor) for "all losses, damages, regulatory fines and penalties, costs, reasonable attorneys' fees and third-party claims" arising from "any processing of Customer Personal Data performed by Processor on Customer's behalf." This is not limited to processing that Timais directed or that resulted from Timais's own fault. It covers processing performed by Pesith itself, including processing that results from Pesith's security failures, unauthorized subprocessor use, or negligent handling.

Section 8.2 further provides that Timais's indemnification obligation "shall not be subject to any limitation of liability in the Agreement." By contrast, Section 8.1 subjects Pesith's own liability to Timais to the MSA cap in Section 11 (12 months of fees). The result is a radically asymmetric risk allocation: if Pesith suffers a data breach due to its own failure to patch a vulnerability (contrary to Annex 2(c), which requires patching within 30 days), Timais indemnifies Pesith for the full regulatory fine and consumer claims without cap, while Pesith's own liability to Timais is capped at 12 months of fees.

**Why it matters.** For a DTC apparel brand, consumer data breaches carry significant regulatory exposure (CCPA/CPRA statutory damages of $100–$750 per consumer per incident, plus private right of action for certain breaches), notification costs, and reputational harm. The current drafting means Timais bears the full financial consequence of Pesith's data-security failures, uncapped, while Pesith's downside to Timais is limited to roughly one year of fulfillment fees.

**Recommended fix.**

- Delete or substantially narrow DPA § 8.2. Timais should indemnify Pesith only for third-party claims arising from (a) Timais's own unlawful instructions to Pesith, or (b) Timais's failure to provide required consumer notices under § 2.3.
- Add a reciprocal indemnity from Pesith to Timais for claims arising from Pesith's breach of the DPA (including failure to implement Annex 2 security measures, unauthorized subprocessor use, or failure to meet the § 7.1 notification deadline).
- Remove the "not subject to any limitation of liability" language from § 8.2, or at minimum make the cap mutual. If the parties insist on an uncapped indemnity, it should run both ways.
- Carve data-protection breaches out of the MSA § 11.1 cap by adding a new sub-clause to § 11.3: "(e) a Party's breach of the DPA or its obligations under Applicable Data Protection Laws."

**Proposed language for DPA § 8.2 (replacement):**

> "Customer shall defend, indemnify and hold harmless Processor from and against third-party claims to the extent arising from (a) Customer's written instructions that are unlawful under Applicable Data Protection Laws, or (b) Customer's failure to provide the notices described in Section 2.3. Processor shall defend, indemnify and hold harmless Customer from and against third-party claims, regulatory fines and penalties, and reasonable attorneys' fees to the extent arising from Processor's breach of this DPA, including any failure to implement the security measures in Annex 2 or to comply with Section 7 (Security Incidents)."

---

### 2. MSA Section 14.1: Auto-Renewal with a Narrow 30-Day Notice Window

**Where:** MSA § 14.1.

**The issue.** The agreement auto-renews for successive three-year terms unless a party gives non-renewal notice "no earlier than ninety (90) days and no later than sixty (60) days before the end of the then-current Initial Term or Renewal Term." This creates a 30-day window (from day 90 to day 60 before term end) in which notice must be delivered. If Timais misses the window by even one day—whether because the notice was sent on day 91 or day 59—it is locked in for another three years.

**Why it matters.** For a three-year initial term ending February 28, 2029, the notice window is December 1, 2028 through January 1, 2029. A single administrative miss (holiday, travel, internal approval delay) extends the commitment to 2032. Given the Minimum Volume Commitment in § 4.4, each additional three-year term carries a recurring shortfall-fee obligation.

**Recommended fix.**

- Widen the window: "no earlier than one hundred eighty (180) days and no later than one hundred twenty (120) days before the end of the then-current term."
- Alternatively, make the renewal opt-in rather than opt-out: "This Agreement shall renew for successive one (1) year terms unless either Party gives written notice of non-renewal at least sixty (60) days before the end of the then-current term."
- Add a reminder obligation: "Provider shall send Customer a written reminder of the upcoming renewal and the non-renewal notice deadline at least one hundred twenty (120) days before the end of the then-current term."

---

### 3. MSA Section 6.2: Sole and Exclusive Remedy for Nonconforming Product

**Where:** MSA § 6.2; Quality Agreement § 1.6 (definition of "Nonconforming Product"); Quality Agreement Appendix A.

**The issue.** Section 6.2 provides that replacement or credit is "Customer's sole and exclusive remedy for Nonconforming Product." "Nonconforming Product" is defined in the Quality Agreement as any product that "fails the visual and workmanship criteria in Appendix A." Appendix A covers stitching, color, labeling, trims, appearance, and packing defects.

This creates two problems:

(a) **Downstream losses are unrecoverable for visual/workmanship defects.** If a shipment of jackets arrives with visible defects (e.g., shade variation, misaligned pockets) that Timais's quality team catches after the 30-day rejection window has passed, or that consumers discover and return, Timais's only remedy is replacement or credit for the defective units. Timais cannot recover the cost of consumer return processing, customer service, restocking, or the margin lost on returned goods.

(b) **Performance-specification failures fall into a gap.** The MSA § 6.1 warranty covers conformance to "Specifications" (defined in MSA § 1.13 to include the performance requirements in Schedule A, e.g., 20,000 mm waterproofing, 15,000 g/m²/24h breathability). A product that passes all visual/workmanship criteria in Appendix A but fails a performance spec (e.g., seam tape delaminates after 15 launderings instead of 20) is not "Nonconforming Product" under the Quality Agreement. It is, however, a breach of the § 6.1 warranty. The § 6.2 exclusive remedy does not apply, so Timais's remedy is the general breach-of-contract framework—subject to the § 11.1 cap and the § 11.2 consequential damages exclusion. In practice, this means Timais may recover direct damages (e.g., cost of rework) but not consequential losses (e.g., consumer returns, brand damage), and the cap limits total recovery to 12 months of fees.

**Why it matters.** Technical outerwear is sold on performance. If a batch of shell jackets fails waterproofing in the field, Timais faces consumer returns, potential product liability exposure (mitigated by the § 13.1 indemnity for third-party claims), and brand damage. The current structure limits Timais's recovery for the business losses it actually suffers.

**Recommended fix.**

- In MSA § 6.2, add: "The remedies in this Section 6.2 are Customer's sole and exclusive remedy for Nonconforming Product *identified during the inspection and rejection period in Section 5.2 of the Quality Agreement*. For Nonconforming Product identified after that period, or for any breach of the warranty in Section 6.1, Customer's remedies shall include those set forth in this Section 6.2 and any other remedies available at law or in equity, subject to Section 11."
- Alternatively, expand the definition of "Nonconforming Product" in Quality Agreement § 1.6 to include any product that fails to conform to the Specifications in Schedule A of the MSA, not just the visual/workmanship criteria in Appendix A.
- Carve out of the § 11.2 consequential damages exclusion any losses arising from a Product safety defect or a failure of a performance Specification in Schedule A.

---

### 4. Schedules B and C Are Placeholders – No Commercial Terms Agreed

**Where:** MSA Schedule B ("as agreed by the Parties in writing"); MSA Schedule C (one sentence of service levels, no credits); MSA § 4.4 (references "per-unit shortfall rate stated in Schedule B"); MSA § 6.3 (references "service level credits stated in Schedule C").

**The issue.** The two schedules that carry the economic substance of the agreement are essentially blank. Schedule B is supposed to contain unit pricing, fulfillment rates, minimum annual volumes by product category, and the per-unit shortfall rate. Schedule C is supposed to contain the site table, detailed service levels, and service level credits. As drafted, Timais would be signing an agreement with:

- No agreed pricing (so "Fees" in § 1.5 has no referent);
- No minimum volume commitment numbers (so § 4.4's shortfall fee is unquantifiable);
- No service level credit mechanism (so § 6.3's reference to "service level credits stated in Schedule C" is empty).

**Why it matters.** Without these terms, the agreement is not commercially operable. More importantly, the absence of service level credits means that if Pesith misses the 99% ship-out or 99.5% inventory accuracy targets in Schedule C, Timais has no monetary remedy—only the general warranty in § 6.3 (re-performance at no charge), which is of limited value for a fulfillment operation where the cost of a missed ship date is a consumer receiving a late package.

**Recommended fix.**

- Do not circulate the MSA for signature until Schedules B and C are fully populated and agreed.
- Schedule C should include a service level credit table, for example:

| Metric | Target | Credit if missed |
|---|---|---|
| Order ship-out (monthly) | ≥ 99% within 2 business days | 1% of monthly fulfillment fees per 0.5% below target, capped at 10% of monthly fees |
| Inventory accuracy (monthly) | ≥ 99.5% | 2% of monthly fulfillment fees per 0.25% below target, capped at 15% of monthly fees |
| Returns processing (monthly) | ≥ 98% processed within 5 business days | 1% of monthly fulfillment fees per 0.5% below target |

- Schedule B should specify the minimum volume commitment per product category (e.g., "Technical Waterproof Shell Jackets: 50,000 units per Contract Year") and the shortfall rate (e.g., "$X per unit below the minimum").

---

## Tier 2 – Significant Issues

### 5. MSA Section 7.4: Price Escalation with "Not Unreasonably Withheld" Approval

**Where:** MSA § 7.4.

**The issue.** After the first Contract Year, Pesith may propose a price adjustment once per year, supported by "documented changes in raw material or labor costs." The adjustment "takes effect only on Customer's written approval, which shall not be unreasonably withheld." The "shall not be unreasonably withheld" standard means that if Pesith provides adequate documentation, Timais is contractually obligated to approve the increase. Over a three-year initial term (plus renewals), this could compound significantly, particularly for technical outerwear inputs (membranes, seam tapes, down) that are subject to volatile commodity pricing.

**Why it matters.** Timais's margins on DTC apparel are thin. An uncontrolled escalation mechanism erodes the pricing advantage that the first-year fixed prices were meant to lock in.

**Recommended fix.**

- Replace "shall not be unreasonably withheld" with a cap: "Any adjustment shall not exceed the lesser of (a) the percentage change in the [BLS Producer Price Index for textiles and apparel] over the preceding twelve months, or (b) three percent (3%) per Contract Year."
- Add: "If Customer does not approve a proposed adjustment, the existing prices shall remain in effect for the remainder of the then-current Contract Year, and either Party may terminate the affected Purchase Orders on sixty (60) days' notice without penalty."

---

### 6. MSA Section 14.3: Termination for Convenience Limited to Initial Term; Raw Material Payment Obligation

**Where:** MSA § 14.3.

**The issue.** Two problems:

(a) The right to terminate for convenience exists only "During the Initial Term." If Timais is locked into a Renewal Term (see Issue 2 above), it has no for-convenience exit short of the 30-day non-renewal window.

(b) On termination, Timais must pay for "raw materials purchased by Provider specifically for those Purchase Orders that cannot reasonably be cancelled, returned or used for other customers." The phrase "cannot reasonably be" is subjective. For custom-dyed fabrics, specialty membranes, or branded trims, virtually all raw materials could be argued to fall in this category. There is no verification mechanism, no cap, and no requirement that Provider mitigate by attempting to resell.

**Why it matters.** If Timais needs to exit the relationship during a Renewal Term (e.g., performance issues, strategic shift), it has no clean exit. And even during the Initial Term, the raw material payment obligation could be substantial and difficult to verify.

**Recommended fix.**

- Extend the for-convenience termination right to Renewal Terms: "Customer may terminate this Agreement for convenience during any Contract Year on not less than one hundred eighty (180) days' written notice."
- Add verification and mitigation requirements to the raw material clause: "Provider shall provide Customer with itemized invoices and supplier purchase orders for such raw materials within thirty (30) days after termination. Provider shall use commercially reasonable efforts to mitigate losses by cancelling supplier orders, returning materials, or reselling them to other customers. Customer's payment obligation shall be limited to the net cost after mitigation."
- Add a cap: "Customer's total payment obligation under this Section 14.3 shall not exceed [X]% of the Fees paid in the preceding Contract Year."

---

### 7. Quality Agreement: "Nonconforming Product" Definition Excludes Performance Failures

**Where:** Quality Agreement § 1.6; MSA Schedule A §§ A.2–A.3 (performance specs); MSA § 1.13 (definition of "Specifications").

**The issue.** As noted in Issue 3, the Quality Agreement defines "Nonconforming Product" by reference to "visual and workmanship criteria in Appendix A." The performance specifications in MSA Schedule A (waterproofing, breathability, DWR durability, seam tape adhesion, fill power, down-proof construction) are not part of Appendix A. A product that is visually perfect but fails the 20,000 mm waterproofing test is not "Nonconforming Product" under the Quality Agreement.

This means the Quality Agreement's inspection, rejection, CAP, and escalation machinery does not apply to performance failures. Timais would need to rely on the MSA § 6.1 warranty and general breach principles, which are weaker and subject to the consequential damages exclusion.

**Why it matters.** Performance failures in technical outerwear are the most damaging type of quality issue for a brand. A shell jacket that leaks is a product recall scenario, not a cosmetic defect. The current structure gives Timais less procedural leverage (no automatic FRI failure trigger, no CAP requirement, no joint re-inspection right) for exactly the type of failure that matters most.

**Recommended fix.**

- Amend Quality Agreement § 1.6 to: "'Nonconforming Product' means any Product, or any unit of a Product, that (a) fails the visual and workmanship criteria in Appendix A, or (b) fails to conform to the Specifications set out in Schedule A of the MSA, as determined by inspection under Section 4, Section 5, or laboratory testing under Section 4.2."
- Add to Quality Agreement § 7.1: "Provider shall deliver a CAP… (d) any laboratory test report or field data indicating a Product has failed to meet a performance Specification in Schedule A of the MSA."

---

### 8. MSA Section 5.4: No Liquidated Damages for Late Delivery

**Where:** MSA § 5.4.

**The issue.** If Pesith is more than 10 days late, Timais's options are (a) expedited freight at Pesith's cost, or (b) cancellation of the late portion. There is no liquidated daily penalty. For a DTC brand with seasonal launches, a 30-day delay on a fall shell jacket line could mean missing peak selling season entirely. Expedited freight mitigates the delay but does not compensate for the lost revenue or the cost of air-freighting a full container.

**Why it matters.** The 120-day standard lead time (§ 4.3) means that a delay of even 2–3 weeks can push delivery past a seasonal window. The current remedy (expedited freight) addresses the logistics problem but not the commercial problem.

**Recommended fix.**

- Add a liquidated delay charge: "If Provider fails to deliver Products within ten (10) days after the agreed delivery date for reasons not attributable to Customer, Provider shall pay Customer a delay charge of [0.5]% of the Fees for the affected Purchase Order for each day of delay beyond ten (10) days, up to a maximum of [10]% of such Fees. This delay charge is in addition to, and not in lieu of, the remedies in this Section 5.4."
- Lower the trigger from 10 days to 5 days for seasonal products (Technical Waterproof Shell Jackets) if the delivery date falls within 60 days of a stated retail launch date.

---

### 9. Insurance: Property Coverage "As Scheduled" May Not Match Actual Inventory Value

**Where:** Insurance certificate § 2.1 (row for MSA § 12.1(b)); MSA § 12.1(b).

**The issue.** The MSA requires property insurance covering "Customer's goods in Provider's care, custody or control at full replacement value." The certificate evidences "Commercial property, including property of others in Pesith's care, custody or control" with limits stated as "Full replacement value, as scheduled." The phrase "as scheduled" means the policy has a schedule of insured values, and coverage is limited to the amounts stated in that schedule. If Timais's actual inventory value at Pesith's facility exceeds the scheduled amount (e.g., during peak season buildup), there is a coverage gap.

**Why it matters.** MSA § 5.3 makes Pesith bear risk of loss for fulfillment inventory. If a fire or water damage event destroys $3M of Timais's inventory but the property policy schedule only covers $2M, Timais bears the $1M gap—and its claim against Pesith would be subject to the § 11.1 liability cap (12 months of fees), which may not cover the loss.

**Recommended fix.**

- Require Pesith to provide the property policy schedule and confirm that the "property of others" sub-limit equals or exceeds Timais's maximum anticipated inventory value at the facility (e.g., $5M or the actual peak-season value).
- Add to MSA § 12.2: "Provider shall notify Customer in writing if the scheduled value of property insurance covering Customer's goods falls below [110]% of the average value of Customer's goods in Provider's care, custody or control over the preceding six (6) months, and shall increase the scheduled value within thirty (30) days."
- Consider requiring a waiver of subrogation in favor of Timais on the property policy, so the insurer cannot seek recovery from Timais after paying a claim.

---

## Tier 3 – Moderate Issues

### 10. MSA Section 4.4: Minimum Volume Commitment Financial Risk

**Where:** MSA § 4.4; MSA § 15.1 (force majeure carve-out).

**The issue.** Timais must meet minimum annual volumes or pay a shortfall fee. The actual numbers are in the (empty) Schedule B. The force majeure provision in § 15.1 helps: if Pesith is unable to perform for more than 45 days due to force majeure, Timais can source elsewhere and those volumes "shall count toward the Minimum Volume Commitment." However, this carve-out only applies to force majeure events affecting Pesith. It does not protect Timais from its own demand shortfall (e.g., a product underperforms in the market, or a broader economic downturn reduces consumer spending).

**Why it matters.** If the minimum volume is set aggressively (e.g., based on optimistic growth projections), Timais could face a significant shortfall payment in a soft year. The payment is due within 45 days after year-end, which creates a cash flow hit on top of the lost revenue.

**Recommended fix.**

- Negotiate the minimum volume at a conservative level (e.g., 80% of projected volume) to build in a buffer.
- Add a "material adverse change" carve-out: "The Minimum Volume Commitment shall not apply to any Contract Year in which Customer's consolidated revenue decreases by more than [20]% year-over-year, provided Customer gives Provider written notice within [30] days after year-end."
- Extend the payment deadline from 45 to 90 days to align with Timais's internal budgeting cycle.

---

### 11. Quality Agreement Appendix A: Critical Defects Do Not Include Chemical/Safety Issues

**Where:** Quality Agreement Appendix A § A.2; MSA Schedule A § A.4 (references Prop 65 and PFAS restrictions).

**The issue.** The three Critical Defects (zero AQL) are: broken needle, missing/incorrect regulatory labels, and wrong trademark. There is no critical defect category for chemical safety failures (e.g., detectable PFAS above regulatory limits, lead in zipper pulls, phthalates in coatings). A chemical safety issue would likely be classified as a Major Defect (AQL 2.5) at best, meaning up to 2.5% of a lot could have the issue and still pass inspection.

**Why it matters.** MSA Schedule A § A.4 requires compliance with "applicable product safety, labeling and chemical restriction laws, including California Proposition 65 and applicable PFAS restrictions." A PFAS contamination issue in a waterproof shell jacket could trigger regulatory action, consumer class actions, and brand damage. Classifying it as merely "Major" (rather than "Critical") reduces the inspection rigor and weakens Timais's rejection rights.

**Recommended fix.**

- Add to Appendix A § A.2: "(d) Presence of any chemical substance in excess of the limits set by applicable product safety or chemical restriction laws, including California Proposition 65, EU REACH, or applicable PFAS restrictions, as identified by laboratory testing under Section 4.2."
- Add to MSA § 13.1 (Provider indemnity): "(e) any claim arising from the presence of a prohibited or restricted chemical substance in a Product in excess of applicable legal limits, to the extent not caused by Customer Materials."

---

### 12. DPA Annex 2: Security Measures Lack Specificity and Verification

**Where:** DPA Annex 2; DPA § 9.4 (audit rights).

**The issue.** The security measures in Annex 2 are a reasonable baseline but lack specificity in several areas:

- No requirement for SOC 2 Type II (or equivalent) certification, or a defined schedule to obtain it.
- No penetration testing frequency (only "regular vulnerability scanning").
- No specific requirement for encryption key management, logging of data access by named individuals, or network segmentation between the fulfillment WMS and other systems.
- The "patching of critical vulnerabilities within thirty (30) days" standard is industry-average but may be too slow for a system processing consumer PII.

**Why it matters.** Given the one-sided indemnity in § 8.2 (Issue 1), the security measures are the primary protection Timais has against Pesith's data-handling failures. Vague standards make it difficult to demonstrate a breach of the DPA if an incident occurs.

**Recommended fix.**

- Add to Annex 2: "(h) Provider shall maintain a current SOC 2 Type II report (or ISO 27001 certification) and shall make it available to Customer upon request. Provider shall conduct penetration testing of its fulfillment systems at least annually by an independent third party and shall remediate any critical findings within fifteen (15) days."
- Tighten the patching standard: "patching of critical vulnerabilities within fifteen (15) days and high-severity vulnerabilities within thirty (30) days."
- Add: "Provider shall implement network segmentation such that systems processing Customer Personal Data are logically separated from Provider's general corporate networks."

---

### 13. MSA Section 3.4: "Material Part" of Fulfillment Services – Ambiguous Subcontracting Threshold

**Where:** MSA § 3.4.

**The issue.** Pesith cannot subcontract "the manufacture of any Product, or any material part of the Fulfillment Services" without consent. The phrase "material part" is undefined. Does it mean a particular step (e.g., returns processing)? A particular volume threshold (e.g., more than 20% of order volume)? A particular function (e.g., all pick-and-pack)?

**Why it matters.** Fulfillment operations commonly use third-party carriers (already addressed in the DPA as subprocessors) and may outsource returns processing or overflow capacity. Without a clear threshold, Timais either (a) has to consent to every minor subcontractor engagement (administrative burden), or (b) loses visibility into who is actually handling its consumer data and inventory (risk).

**Recommended fix.**

- Define "material part" as: "any subcontracting of more than [20]% of the volume of any single Fulfillment Service step (receipt, storage, pick, pack, labeling, shipping, or returns processing), or any subcontracting of a step that involves access to Customer Personal Data, in each case without Customer's prior written consent."
- Cross-reference the DPA subprocessor regime: "Subcontracting of any activity that involves Processing of Customer Personal Data is also subject to Section 6 of the DPA."

---

## Open Questions

The following items require additional facts from Timais before the analysis can be completed:

1. **Minimum volumes and pricing.** What are Timais's projected unit volumes for each product category in Year 1? What is the target per-unit cost? This is needed to assess whether the Minimum Volume Commitment (once populated in Schedule B) is achievable and whether the shortfall rate is commercially reasonable.

2. **Inventory value at Pesith's facility.** What is Timais's anticipated peak-season inventory value held at Pesith's fulfillment center? This determines whether the "as scheduled" property insurance limit is adequate (Issue 9).

3. **Tech packs and lab testing frequency.** Which tech packs have been approved or are in development? What lab testing frequency do they specify (Quality Agreement § 4.2)? Without this, we cannot assess whether the testing regime is sufficient to catch performance failures before shipment.

4. **Data volume and sensitivity.** Approximately how many consumer orders per month will Pesith process? Are there any states with data breach notification laws that impose specific timing requirements stricter than the 48-hour notice in DPA § 7.1? (e.g., some states require notice within 30 days of discovery, which 48 hours satisfies, but the internal investigation timeline matters.)

5. **Existing insurance program.** Does Timais carry its own product liability or cyber insurance? If so, what are the limits and subrogation provisions? This affects whether the additional insured status and the property insurance gap (Issue 9) are material.

6. **Strategic flexibility.** Does Timais anticipate potentially moving manufacturing or fulfillment to another provider within the Initial Term? If so, the termination-for-convenience and raw material payment issues (Issue 6) become more pressing, and we should consider adding a "right to first refusal" or transition-assistance enhancement.

---

*Prepared for internal use in framing markup and client call. All section references are to the documents as received in the matter folder.*