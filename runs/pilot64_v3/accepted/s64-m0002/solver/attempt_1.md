# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Kunoux Creamery, Inc. – Tilil Systems Software License: Issue Identification and Recommendations

---

## Summary

I have reviewed all ten documents in the matter folder. The arrangement is broadly well-drafted and favorable to Kunoux in several respects (recall support treated as Severity 1, data ownership, U.S. hosting, fixed pricing for the Initial Term). However, I have identified the following issues, prioritized by urgency and materiality.

---

## Priority 1 – Immediate Action Required

### Issue 1: Change of Control – Termination Right and Fee Acceleration

**Where:** License Agreement § 14.4; § 1 (definition of "Change of Control"); Amendment No. 1, Recital B; Parent Guaranty § 1.1 (definition of "Guaranteed Obligations," clauses (a) and (b)).

**The problem.** Kunoux Holdings, L.P. signed an equity purchase agreement on September 18, 2026 to sell its general partner and operating subsidiaries to Ostrander Dairy Partners III, L.P., with closing expected in Q1 2027 (Amendment No. 1, Recital B). This will constitute a "Change of Control" under § 1 of the License Agreement (transfer of more than 50% of voting equity of an entity controlling Licensee).

Section 14.4 provides that Tilil may terminate on 30 days' notice if Licensee undergoes a Change of Control **without Licensor's prior written consent**, and upon such termination **all Subscription Fees for the remainder of the Initial Term become immediately due and payable**. That is up to approximately $2.4 million in accelerated fees (five years × $486,000, less elapsed time).

Those accelerated amounts are "Guaranteed Obligations" under the Parent Guaranty (§ 1.1(b): "the payment of all amounts that become due and payable under Section 14.4"), meaning Kunoux Holdings would be on the hook as primary obligor.

The Amendment acknowledges the Ostrander transaction in its recitals but contains **no provision** addressing (a) Tilil's consent to the Change of Control, (b) waiver of the termination right, or (c) waiver of fee acceleration.

**Why it matters.** If the Ostrander closing occurs before Kunoux obtains Tilil's written consent, Tilil has a contractual right to terminate the entire agreement and accelerate all remaining subscription fees. Kunoux would lose its traceability platform mid-implementation (Sheboygan Go-Live is January 18, 2027) and face a seven-figure cash outflow.

**Recommended fix.** Before the Ostrander closing:
- Negotiate a written consent or waiver from Tilil under § 14.4, ideally as Amendment No. 2.
- If Tilil resists a full waiver, seek at minimum: (a) a right for Kunoux to assign the Agreement to the Ostrander entity without termination; or (b) a provision that the Change of Control does not trigger fee acceleration so long as the Ostrander entity assumes the Agreement.
- Confirm with Kunoux Holdings' deal team that the Ostrander purchase agreement does not itself require Tilil consent as a closing condition (if it does, that creates leverage).

---

### Issue 2: Exclusivity Scope Broader Than Negotiated

**Where:** Term Sheet § 4.1; License Agreement § 2.6; Order Form § 3.1.

**The problem.** The Term Sheet limited exclusivity to "milk traceability software at the Eau Claire and Sheboygan, Wisconsin plants only" (§ 4.1). The definitive documents are materially broader:

- **Order Form § 3.1** defines "Covered Facilities" as *all* facilities owned, leased or operated by Licensee or any Affiliate, *wherever located*, including facilities acquired or opened after the Order Form date.
- **License Agreement § 2.6** prohibits use of any third-party software *or internally developed software* performing Traceability Functions at *any* Covered Facility.

The combined effect: Kunoux cannot use a competing traceability product (or build its own) at any of its facilities—present or future, domestic or foreign—during the entire Term (five years plus renewals). This is significantly broader than the two-plant, third-party-only limitation in the Term Sheet.

**Why it matters.** If Kunoux acquires another dairy processor, opens a new plant, or wants to pilot an in-house tool at a non-implementation facility, § 2.6 restricts it. The restriction also covers Affiliates (§ 2.6: "shall cause its Affiliates not to").

**Recommended fix.**
- Negotiate an amendment narrowing § 2.6 to the Implementation Sites (Eau Claire and Sheboygan) or to facilities where the Subscription Services are actually in production use.
- Delete or narrow the prohibition on internally developed software, or limit it to the Implementation Sites.
- If Tilil resists, at minimum add a carve-out for facilities where the Subscription Services have not been implemented and for which no Order Form has been executed.

---

### Issue 3: Parent Guaranty – Breadth and Subordination

**Where:** Parent Guaranty §§ 1.1, 2.1, 2.2, 3.1, 4.3; License Agreement § 16.8.

**The problem.** The Guaranty is unusually broad:

1. **Guaranty of payment AND performance** (§ 2.1): Kunoux Holdings guarantees not just fees but "the full and punctual performance of all Guaranteed Obligations," including all covenants (§ 1.1(f)). If Kunoux Creamery fails to, say, maintain its site safety rules for Tilil personnel (§ 4.4 of the License Agreement), the parent is liable.
2. **Absolute and unconditional** (§ 3.1): Not affected by amendments, insolvency, set-off, or any other circumstance that would normally discharge a guarantor.
3. **Subordination** (§ 4.3): All indebtedness of Kunoux Creamery to Kunoux Holdings is subordinated to the Guaranteed Obligations. While Tilil has a demand outstanding (or during a Licensee insolvency), the parent cannot collect intercompany payables from the subsidiary.
4. **Continuing and self-executing** (§ 2.4, § 3.1(a)): Extends to future obligations without further action by the Guarantor.

The Amendment (§ 6.2) has the Guarantor confirming the guaranty continues to cover the amended Agreement, including the increased Implementation Fees ($334,500 vs. $312,000).

**Why it matters.** In a downside scenario (e.g., Tilil terminates for Change of Control under Issue 1, or Kunoux Creamery has a payment dispute that escalates), Kunoux Holdings faces uncapped, unconditional exposure for all of the subsidiary's contractual obligations, and cannot recover intercompany debt while the guaranty is live.

**Recommended fix.**
- Seek to narrow the guaranty to payment obligations only (delete § 1.1(f) and the performance language in § 2.1).
- Add a cap on the Guarantor's aggregate exposure (e.g., limited to the then-outstanding Subscription Fees and Implementation Fees, excluding consequential or accelerated amounts).
- Carve out the § 14.4 fee acceleration from the Guaranteed Obligations, or at minimum make it conditional on Tilil not having terminated for its own breach.
- Limit the subordination in § 4.3 to the period of an actual demand, and exclude ordinary-course intercompany charges (the current carve-out for "ordinary course distributions, intercompany charges or repayments" is helpful but could be broadened).

---

## Priority 2 – Significant Risk

### Issue 4: Service Credits as Sole Monetary Remedy for Availability Failures

**Where:** License Agreement § 5.6; Exhibit A, §§ A.1–A.4.

**The problem.** Section 5.6 makes service credits Kunoux's "sole monetary remedy" for failure to meet the 99.9% availability commitment. The maximum credit is 30% of the monthly Subscription Fee (i.e., ~$12,150/month). The chronic failure termination right (§ A.4) requires availability below 99.0% in three separate months within a rolling 12-month period.

If the platform is down during a recall, a spring flush peak, or a regulatory inspection, and the downtime does not trigger the chronic failure threshold, Kunoux's only monetary recovery is a modest credit. Operational losses (milk rejected, product held, recall delayed) are excluded as consequential damages under § 12.1.

**Why it matters.** For a dairy processor, a multi-hour outage during milk receiving can mean rejected loads, spoiled product, and missed delivery windows. The financial impact can far exceed $12,150, but the contract channels all monetary recovery into the credit mechanism.

**Recommended fix.**
- Negotiate a carve-out from § 5.6 for outages that prevent milk receiving or product release for more than a specified duration (e.g., 4 hours in a day), allowing Kunoux to claim direct damages in addition to credits.
- Alternatively, increase the service credit percentages or add a "super credit" for Severity 1 outages exceeding a threshold duration.
- At minimum, confirm that the § 12.1 exclusion of indirect damages does not swallow claims for direct, out-of-pocket costs incurred during an outage (e.g., cost of rejected milk, expedited shipping).

---

### Issue 5: Fee Acceleration on Licensor Termination for Licensee Breach

**Where:** License Agreement § 14.5(d); Parent Guaranty § 1.1(b).

**The problem.** If Tilil terminates for Kunoux's material breach (§ 14.3(a)), "all Subscription Fees for the remainder of the then-current Initial Term or Renewal Term shall become due and payable" (§ 14.5(d)). These accelerated amounts are Guaranteed Obligations.

There is no corresponding provision requiring Tilil to refund the value of services not yet received or to offset Kunoux's damages against the accelerated fees.

**Why it matters.** A dispute over, e.g., an overage charge or a SOW acceptance issue that escalates to a material breach finding could trigger acceleration of up to ~$2.4 million, backed by the parent guaranty.

**Recommended fix.**
- Negotiate a provision that, on Licensor termination for Licensee breach, the accelerated fees are reduced by (a) the value of services actually provided through the termination date, and (b) any damages Licensor is entitled to for the breach (so the acceleration is not in addition to damages but in lieu of continued subscription).
- Alternatively, cap the acceleration at the fees for the remainder of the then-current Subscription Year (not the full Initial Term).

---

### Issue 6: DPA – Licensee Indemnity Is Uncapped

**Where:** DPA §§ 8.1–8.2.

**The problem.** Section 8.1 requires Kunoux to indemnify Tilil for all losses arising from Licensee Data or Kunoux's processing instructions, including claims by Data Subjects, regulators or third parties. Section 8.2 expressly states this indemnity is **not subject to any limitation of liability**, including the § 12 cap.

Kunoux's obligations under DPA § 2.4 include ensuring its instructions comply with Data Protection Laws and providing all necessary notices and consents to Data Subjects, "including the collection of location data from drivers and haulers through the mobile applications."

**Why it matters.** If a driver or farm supplier brings a privacy claim (e.g., over GPS location tracking) and Kunoux is found to have failed in its consent or notice obligations, Kunoux's indemnity to Tilil is unlimited. The parent guaranty may also be implicated if the indemnity is characterized as an obligation "under the Agreement."

**Recommended fix.**
- Negotiate a cap on the DPA indemnity (e.g., the same 12-month fees cap as § 12.2), or at minimum a cap tied to the applicable statutory maximum for the relevant Data Protection Law.
- Clarify that the indemnity does not apply where the claim arises from Tilil's own processing in breach of the DPA.
- Review Kunoux's driver and supplier consent forms to ensure they adequately cover GPS location data collection (DPA § 2.4, Schedule 1 ¶ 5).

---

## Priority 3 – Operational and Governance Issues

### Issue 7: Peak Season May Not Align with Actual Operational Peaks

**Where:** Amendment No. 1 § 2.2 (new License Agreement § 5.7); Kickoff Minutes § 5.3; Term Sheet § 7.5.

**The problem.** The Amendment defines "Peak Season" as April 1 through June 30 (the spring flush). However, the Kickoff Minutes record the VP of Operations stating that "Kunoux wants the plant to be stable on DairyLedger before **late-summer** receiving volumes increase" (§ 5.3). If Kunoux experiences a second volume peak in late summer (July–September), the enhanced support protections of § 5.7 (no scheduled maintenance during receiving hours, named support engineer, weekly review calls, capacity review) would not apply.

**Why it matters.** During a volume peak without the § 5.7 protections, Tilil could schedule maintenance during receiving hours (subject only to the general "commercially reasonable efforts" in § 5.3) and Kunoux would not be entitled to the named support engineer or weekly review.

**Recommended fix.**
- Confirm with Kunoux operations whether there is a meaningful late-summer peak. If so, negotiate to extend the Peak Season (e.g., April 1 – September 30) or add a second "shoulder season" period.
- If the late-summer concern is specific to Eau Claire (which went live in August), consider whether the first few months of production use warrant enhanced support beyond the Hypercare Period.

---

### Issue 8: Deemed Acceptance – 10 Business Day Window

**Where:** SOW § 6.5; License Agreement § 4.5.

**The problem.** If Kunoux neither signs the Acceptance Certificate nor provides written notice of nonconformity within 10 Business Days, the deliverable is **deemed accepted**. This applies to all milestones and deliverables. During spring flush or other busy periods, the project team may miss the window.

Once deemed accepted, the milestone payment becomes due (SOW § 9.1), and Kunoux loses leverage to require correction of issues it has not yet identified.

**Why it matters.** A missed 10-day window on a major milestone (e.g., M4 at $93,600) locks in acceptance and triggers payment, even if defects later surface.

**Recommended fix.**
- Operationally: Calendar the 10 Business Day deadline for each acceptance submission and assign a single owner (the Project Manager) to track it.
- Contractually (if renegotiating): Extend the window to 15 Business Days, or provide that deemed acceptance does not apply to Severity 1 or 2 defects that are discovered after the window but within 30 days of Go-Live.
- Ensure the Project Manager is empowered to issue a short "hold" notice within the window to preserve rights while the team completes testing.

---

### Issue 9: Escalation Contact – Same Person at Levels 1 and 2

**Where:** Kickoff Minutes § 4.4; SOW § 7.5.

**The problem.** Marcus Lindqvist is both Kunoux's Project Manager (Level 1 escalation) and the Director of Plant Systems (Level 2 escalation). The minutes note this and say Kunoux will "consider whether to nominate a different Level 1 contact after Go-Live at the Eau Claire Plant," but no change has been made.

**Why it matters.** If a dispute arises between the Project Managers (Level 1), there is no true internal escalation within Kunoux before jumping to the VPs (Level 3). This weakens Kunoux's position in operational disagreements.

**Recommended fix.**
- Designate a different Level 1 contact (e.g., the quality assurance lead or IT integration lead for the relevant site) so that Level 2 (Lindqvist) can escalate independently.
- Issue the written notice contemplated by SOW § 7.5 to update the escalation contacts.

---

### Issue 10: No General Exclusivity Release if Tilil Withdraws a Module

**Where:** Term Sheet § 4.3; License Agreement § 2.6, § 13.4(c), § 14.6.

**The problem.** The Term Sheet provided that exclusivity "will cease to apply to any module that Tilil withdraws or is unable to continue to provide" (§ 4.3). The License Agreement only releases exclusivity in two narrow circumstances:
- IP infringement termination of affected services (§ 13.4(c)); and
- During a post-termination transition period (§ 14.6).

There is no general provision releasing exclusivity if Tilil simply discontinues a module (e.g., sunsets the Organic Certification module or the Consumer Complaints module) without an IP claim.

**Why it matters.** If Tilil withdraws a module that Kunoux needs for compliance (e.g., organic certification tracking), Kunoux would be locked into § 2.6 and unable to use a replacement at the affected facility until the entire Agreement terminates.

**Recommended fix.**
- Add a provision to § 2.6 (or § 5.4) stating that if Tilil discontinues or materially degrades a subscribed module and does not restore or replace it within 60 days, § 2.6 ceases to apply with respect to the Traceability Functions performed by that module at the affected facility.

---

## Priority 4 – Lower-Risk / Housekeeping Items

### Issue 11: Press Release Now Outdated

**Where:** Press Release § 4 (Rollout Plan); Amendment No. 1 § 3.1.

**The problem.** The press release (dated March 10, 2026) states Sheboygan Go-Live is "targeted for later in 2026." The Amendment moved it to January 18, 2027. If the press release is still circulating (e.g., on Kunoux's website or in trade publications), the outdated timeline could create confusion with suppliers, regulators or customers.

**Recommended fix.** Issue a brief update or remove the press release from Kunoux's public-facing channels. Not a contractual issue, but a reputational one.

---

### Issue 12: Hardware Replacement Costs and Title

**Where:** Order Form § 7.3, § 7.4.

**The problem.** Title to all hardware (sensors, probes, gateways) remains with Tilil (§ 7.3). Kunoux bears risk of loss on delivery. Replacement for lost, damaged (by misuse, accident or collision) hardware is at Kunoux's cost: $640 per in-tanker sensor, $520 per in-silo probe, $1,850 per gateway. With 48 in-tanker sensors on independent haulers' tankers, the risk of loss or damage in transit is non-trivial.

**Why it matters.** A single tanker accident could generate a $640 replacement charge. Over a five-year term with 48 sensors on the road daily, cumulative replacement costs could be meaningful. The costs are not included in the Subscription Fee.

**Recommended fix.**
- Confirm that Kunoux's tanker insurance (or the haulers' insurance) covers damage to third-party equipment.
- Consider negotiating a bulk replacement rate or a cap on annual hardware replacement charges.
- Clarify in the supplier/hauler agreements that the hauler bears responsibility for sensor damage caused by its negligence (the License Agreement places risk of loss on Kunoux, but Kunoux should pass this down contractually).

---

### Issue 13: SOW – INT-5 Test Environment Gap

**Where:** Kickoff Minutes § 7.2.

**The problem.** Kunoux does not have a separate test instance of its supplier payroll and premium system (INT-5). The proposed workaround is a "file-based staging area" with "controlled production validation during user acceptance testing." This means INT-5 will be tested against production data during UAT, which carries a risk of corrupting live payroll records.

**Recommended fix.**
- Ensure the Test Plan (DEL-7) documents specific safeguards for the INT-5 production validation (e.g., read-only access, rollback procedure, time-boxed testing window).
- Confirm with the payroll system vendor whether a test instance can be provisioned before UAT begins.

---

### Issue 14: Quality Agreement – Annual Review Obligation

**Where:** Quality Agreement § 13.4.

**The problem.** The Quality Representatives must review the Quality Agreement "at least once each Subscription Year, and following any change in Applicable Food Laws that affects the Food Safety Functions." If federal or state food traceability rules change (e.g., FDA's Food Traceability Rule under FSMA 204), the Quality Agreement may need amendment to reflect new record-keeping requirements.

**Why it matters.** The FDA's Food Traceability Rule (21 C.F.R. Part 1, Subpart S) is being phased in and may impose new traceability record requirements on dairy processors. If the rule changes the types of records Kunoux must maintain, the Quality Agreement's retention periods (Schedule 2) and Food Safety Functions (Schedule 1) may need updating.

**Recommended fix.**
- Calendar the annual Quality Agreement review.
- Monitor FDA/FSMA 204 implementation guidance and the Wisconsin DATCP for changes affecting dairy traceability records.
- If new requirements emerge, raise a change request under § 13.4 before the next Subscription Year begins.

---

## Summary Table

| # | Issue | Document(s) | Risk Level | Action |
|---|---|---|---|---|
| 1 | Change of Control / fee acceleration | LA § 14.4; Amend. Recital B; Guaranty § 1.1 | **Critical** | Obtain Tilil consent/waiver before Ostrander closing |
| 2 | Exclusivity broader than Term Sheet | LA § 2.6; OF § 3.1; TS § 4.1 | **High** | Amend to limit to Implementation Sites |
| 3 | Parent Guaranty breadth | Guaranty §§ 2.1, 3.1, 4.3 | **High** | Narrow to payment; add cap; limit subordination |
| 4 | Service credits sole remedy | LA § 5.6; Ex. A | **High** | Carve-out for prolonged outages |
| 5 | Fee acceleration on breach termination | LA § 14.5(d) | **Medium-High** | Offset or cap acceleration |
| 6 | DPA indemnity uncapped | DPA §§ 8.1–8.2 | **Medium-High** | Add cap; verify driver consents |
| 7 | Peak Season timing | Amend. § 2.2; Minutes § 5.3 | **Medium** | Confirm actual peaks; extend if needed |
| 8 | Deemed acceptance (10 BD) | SOW § 6.5 | **Medium** | Operational calendar; consider extension |
| 9 | Escalation contact overlap | Minutes § 4.4; SOW § 7.5 | **Low-Medium** | Designate alternate Level 1 |
| 10 | No module withdrawal release | TS § 4.3; LA § 2.6 | **Medium** | Add sunset/discontinuation carve-out |
| 11 | Press release outdated | Press Release § 4 | **Low** | Update or remove |
| 12 | Hardware replacement risk | OF §§ 7.3–7.4 | **Low** | Verify insurance; pass down to haulers |
| 13 | INT-5 test environment gap | Minutes § 7.2 | **Low** | Document safeguards in Test Plan |
| 14 | Quality Agreement annual review | QA § 13.4 | **Low** | Calendar; monitor FSMA 204 |

---

## Recommended Next Steps

1. **Immediately** (before Ostrander closing): Engage Tilil on Issue 1. This is time-critical. If the closing is expected in Q1 2027, consent should be sought now.
2. **Before Sheboygan Go-Live (January 18, 2027):** Resolve Issues 8 and 9 operationally. Confirm the network readiness date (Amendment § 3.3) is achievable.
3. **Next amendment cycle** (or as a condition of the Change of Control consent): Package Issues 2, 3, 4, 5, 6, and 10 into a single Amendment No. 2 negotiation.
4. **Ongoing:** Calendar the Peak Season capacity review request (due 30 days before April 1, 2027, per Amendment § 2.2(d)), the annual Quality Agreement review, and the monthly SLA reports.