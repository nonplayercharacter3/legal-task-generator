# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Daikesk Imaging Holdings / Sorrelux Imaging – Exposure Analysis and Recommended Revisions

---

## Executive Summary

The current document set contains one deal-critical defect and several significant gaps that leave Daikesk exposed at and after closing. The most urgent issue is that the exclusive license to the Company's core detector calibration patents **terminates automatically upon the change of control** that this transaction effects, and no document requires Dr. Ferreol's consent as a condition to closing. In addition, the Transition Services Agreement as drafted covers a materially narrower scope of the business than the LOI contemplated, and its liability provisions override the SPA's indemnification for data-related claims. Details and proposed fixes follow.

---

## 1. Patent License Terminates on Change of Control; No Consent Required as Closing Condition

**Where:**
- Key Employee Agreement § 9.3 (last two sentences): *"The license and all rights of the Company under this Section 9.3 shall terminate automatically upon a Change of Control unless the Company has obtained the Employee's prior written consent to that Change of Control."*
- Key Employee Agreement § 1.1, definition of "Change of Control" (clause (a)): includes *"any sale of a majority of the Company's stock."*
- SPA § 7.2 (Conditions to Buyer's Closing Obligation): no condition requires Dr. Ferreol's consent or any action to preserve the patent license.
- SPA § 3.2 (Seller Closing Deliverables): no deliverable related to the Key Employee Agreement or Dr. Ferreol's consent.
- SPA § 1.1, definition of "Key Employee Agreement": identifies the agreement but does not make it a closing condition or deliverable.

**Why it matters:**
The four Detector Calibration Patents (Exhibit A to the Key Employee Agreement) are the foundational IP for the Company's flat-panel DR detector line. The license is exclusive, royalty-free, and worldwide—but it is the *only* right the Company has in these patents (Dr. Ferreol is sole owner; see Key Employee Agreement § 9.2). If the license terminates at closing, the Company (now Daikesk's subsidiary) loses the right to make, use, sell, or service its core product line. This is not a contingent risk; the termination is automatic upon the change of control that the SPA effects.

The SPA's IP representation (§ 4.9) states the Company "owns, or has a valid and enforceable right to use, all Company Intellectual Property necessary for the conduct of the Business as currently conducted." That representation is true *as of the signing date* but will be false *as of the Closing Date* if Dr. Ferreol has not consented—yet the SPA's bring-down condition (§ 7.2(a)) requires reps to be true "as of the Closing Date." This creates a paradox: the buyer cannot close without the rep being true, but the rep cannot be true at closing without Dr. Ferreol's consent, which is not a required deliverable.

**Recommended fix:**

Add a new closing condition in SPA § 7.2:

> **(g)** Dr. Tamsin Ferreol shall have delivered to Buyer her prior written consent to the Change of Control contemplated by this Agreement, in form and substance reasonably acceptable to Buyer, pursuant to Section 9.3 of the Key Employee Agreement, and the license under the Detector Calibration Patents shall remain in full force and effect as of the Closing Date.

Add a corresponding closing deliverable in SPA § 3.2:

> **(g)** the written consent of Dr. Tamsin Ferreol to the Change of Control, in the form required by Section 9.3 of the Key Employee Agreement.

**Additionally:** Negotiate a new or amended employment/retention agreement with Dr. Ferreol to be effective at or before closing. The current Key Employee Agreement was signed in 2021 and its terms (particularly the Good Reason definition and the 12-month non-compete) may not reflect the post-closing reality. A retention agreement should: (a) confirm her continued employment on acceptable terms; (b) extend the non-compete to align with the 5-year Seller non-compete in SPA § 6.8; and (c) clarify that the patent license survives any future change of control of the Company (i.e., if Daikesk later sells Sorrelux).

**Question for client:** Has Dr. Ferreol been informally approached about the transaction? What is her stated position? If she is not on board, we need to understand whether Seller/Glosiv has any leverage to obtain her consent, and whether the purchase price should be adjusted to reflect the risk.

---

## 2. Transition Services Agreement "Business" Definition Excludes Ultrasound and Field Service

**Where:**
- TSA § 1.1: *"Business" means the manufacture of digital radiography detectors as conducted by Recipient as of the Closing Date.*
- SPA § 1.1: *"Business" means the design, manufacture, sale and servicing of digital radiography and ultrasound imaging systems.*
- LOI § 5: contemplates transition services for (a) IT/ERP, (b) field-service operations (dispatch, service-ticketing, spare-parts logistics, installed-base records), (c) ultrasound operations (shared transducer sourcing, regulatory and complaint-handling, distributor order processing), (d) supply chain for DR detectors, and (e) payroll/benefits/finance.
- TSA Schedule A: lists only IT, Data Migration, Detector Supply Chain, Procurement, Payroll/Benefits, and Finance/Accounting. No field-service or ultrasound services appear.

**Why it matters:**
The TSA's narrow "Business" definition has two compounding effects:

First, the services actually listed in Schedule A cover only the DR detector manufacturing supply chain and back-office functions. The field-service organization (dispatch, ticketing, spare parts, installed-base records) and the ultrasound line (transducer sourcing, complaint handling, distributor order processing) are absent. These are operations the Company performs today and that Daikesk will need support for at least through the transition.

Second, the "Omitted Services" safety valve in TSA § 2.3 only works for services "reasonably necessary to operate the Business"—and "Business" is defined as DR detector manufacture only. So even if Daikesk identifies a missing ultrasound or field-service item within 90 days post-closing, it cannot add it under § 2.3 because it falls outside the defined Business.

**Recommended fix:**

Amend TSA § 1.1 to align with the SPA:

> "**Business**" has the meaning given in the Purchase Agreement.

Then add to TSA Schedule A (or as a new schedule) the services described in LOI § 5(b) and 5(c):

| No. | Service | Description | Fees |
|---|---|---|---|
| 7 | Field Service Operations | Access to dispatch and service-ticketing systems; spare-parts logistics coordination; access to installed-base service records; support for field-service technician scheduling and routing. | Fully loaded cost, invoiced monthly |
| 8 | Ultrasound Operations | Shared transducer sourcing and purchase-order processing; regulatory complaint-handling system access; distributor order processing for ultrasound products. | Fully loaded cost, invoiced monthly |

**Question for client:** Does Daikesk have its own field-service infrastructure and ultrasound supply chain in place at closing, or will it be fully dependent on Seller for these functions during the transition? If dependent, the gap is operationally critical, not just a paper issue.

---

## 3. TSA Liability Cap Overrides SPA Indemnification for Data Claims

**Where:**
- TSA § 10.2 (second sentence): *"Notwithstanding anything to the contrary in the Purchase Agreement, any claim arising from the use or disclosure by Provider or its Affiliates of Company Data or Confidential Information in connection with the Services is subject to, and limited by, this Section 10.2."*
- TSA § 10.2 (cap): Provider's aggregate liability is limited to *"the Fees paid by Recipient under this Agreement in the six months preceding the event giving rise to the claim."*
- SPA § 9.4(b): breaches of § 6.7 (Confidentiality) are excluded from the 10% cap and have a cap equal to the full Purchase Price.
- SPA § 1.1, "Company Data": includes *"protected health information processed by or for the Company."*

**Why it matters:**
During the 12-month transition, Seller (as Provider) will have access to Company Data, which expressly includes PHI. If Seller or its personnel mishandle that data—a breach, an improper disclosure, a failure to maintain security safeguards—the maximum recovery under the TSA is six months of transition fees. For an $186.5M company handling medical imaging data for hospital customers, a single HIPAA breach could generate penalties, customer claims, and remediation costs far exceeding six months of back-office transition fees (which are likely in the low seven figures at most).

The "notwithstanding" language in TSA § 10.2 expressly trumps the SPA's broader confidentiality indemnification (SPA § 9.4(b), which caps at the full Purchase Price for confidentiality breaches). This is a significant asymmetry that favors Seller.

**Recommended fix:**

Delete the second sentence of TSA § 10.2 in its entirety. If Seller resists, propose:

> Notwithstanding the foregoing, this Section 10.2 shall not apply to (a) Provider's breach of Section 7 (Confidentiality and Data Protection), or (b) Provider's gross negligence or willful misconduct. Claims under clauses (a) and (b) shall be subject to the indemnification and limitation provisions of Article IX of the Purchase Agreement.

At minimum, carve out HIPAA/PHI-related claims from the cap.

---

## 4. TSA Permits Provider to Assign Without Recipient Consent

**Where:**
- TSA § 12.4: *"Provider may assign this Agreement, or delegate the performance of any of the Services, in whole or in part, to any Person without the consent of Recipient."*
- Contrast: *"Recipient may not assign this Agreement, in whole or in part, without the prior written consent of Provider."*

**Why it matters:**
Daikesk is paying for transition services from a known counterparty (Glosiv) with known personnel and systems. If Glosiv can unilaterally assign the TSA to any Person—potentially a competitor, a shell entity, or a party with weaker security controls—Daikesk loses control over who has access to its Company Data (including PHI) and who is performing critical operational services. The one-sidedness is particularly concerning given that the TSA involves access to the Company's ERP, manufacturing execution system, and customer data.

**Recommended fix:**

Amend TSA § 12.4:

> Neither Party may assign this Agreement, in whole or in part, without the prior written consent of the other Party, such consent not to be unreasonably withheld. Provider may delegate the performance of any Service to a subcontractor, provided that (a) Provider remains fully responsible for the subcontractor's performance, (b) the subcontractor is bound by confidentiality and data protection obligations no less protective than those in this Agreement, and (c) Provider gives Recipient at least 30 days' prior written notice of any such delegation.

---

## 5. TSA Governed by New York Law; Inconsistent with SPA

**Where:**
- TSA § 13.2: governed by New York law; exclusive jurisdiction in Manhattan.
- SPA § 11.8: governed by Delaware law.
- SPA § 11.9: exclusive jurisdiction in Delaware (Chancery/Superior/Federal).
- NDA § 10.7: governed by Delaware law.
- Key Employee Agreement § 11.7: governed by Delaware law.

**Why it matters:**
While not fatal, the mismatch creates practical problems. If a dispute arises at the intersection of the TSA and the SPA (e.g., whether a data breach claim is governed by the TSA cap or the SPA indemnification), the parties could end up litigating in two forums under two bodies of law. The "notwithstanding" language in TSA § 10.2 makes this intersection more likely, not less.

**Recommended fix:**

Amend TSA § 13.2 to conform to the SPA:

> This Agreement and all claims arising out of or relating to it are governed by the laws of the State of Delaware, without regard to conflict-of-laws principles. Each Party irrevocably submits to the exclusive jurisdiction of the Court of Chancery of the State of Delaware (or, if that court lacks subject-matter jurisdiction, the Superior Court of the State of Delaware or the United States District Court for the District of Delaware) for any action arising out of or relating to this Agreement or the Services.

---

## 6. Key Employee "Good Reason" Definition Creates Post-Closing Retention Risk

**Where:**
- Key Employee Agreement § 1.1, "Good Reason": includes *"a material diminution in her title, authority or duties."*
- Key Employee Agreement § 7.2: if a qualifying termination (without Cause or for Good Reason) occurs within 12 months after a Change of Control, Dr. Ferreol receives 18 months' salary, 1.5× target bonus, and full equity acceleration.
- Key Employee Agreement § 9.3: the patent license terminates on Change of Control absent her consent (see Issue 1 above).

**Why it matters:**
Post-closing, Daikesk will almost certainly integrate Sorrelux into its own organizational structure. If Dr. Ferreol's reporting line, title, or scope of authority changes—even modestly—she can claim Good Reason, resign, and collect enhanced severance. Worse, if the patent license has already terminated (per Issue 1), her departure removes any remaining personal connection to the Company and makes enforcement of her 12-month non-compete (§ 10.1) the only protection against her joining a competitor.

The combination of (a) automatic license termination, (b) a low threshold for Good Reason, (c) enhanced severance, and (d) a short non-compete creates a scenario where Daikesk could lose the core IP *and* the CTO *and* pay a seven-figure severance package, all within 12 months of closing.

**Recommended fix:**

In the new retention agreement (see Issue 1), negotiate:
- A narrower Good Reason definition that requires the diminution to be "material and adverse" and that excludes routine integration changes made in good faith;
- An extension of the non-compete to 3 years post-termination (matching or approaching the Seller's 5-year non-compete in SPA § 6.8);
- An express provision that the Detector Calibration Patent license survives any Change of Control of the Company (i.e., is not terminable by reference to ownership changes above the Company level);
- A commitment to maintain her title and direct reporting to the CEO (or equivalent) for a minimum period (e.g., 3 years).

---

## 7. Indemnification Survival Period May Be Insufficient for Regulatory and IP Reps

**Where:**
- SPA § 9.1: general representations and warranties survive 18 months post-closing.
- SPA § 4.9 (IP), § 4.10 (FDA/Regulatory), § 4.11 (Data Privacy/HIPAA): all subject to the 18-month survival.

**Why it matters:**
FDA enforcement actions, HIPAA breach notifications, and IP infringement claims often have long latency. An FDA 510(k) clearance issue or a quality system deficiency may not surface for 2–3 years. A patent infringement claim by a third party could be filed well after closing. An 18-month survival means Daikesk would bear these risks with no recourse against Seller.

**Recommended fix:**

Propose in SPA § 9.1:

> The representations and warranties in this Agreement survive the Closing for 18 months, except that (a) the Fundamental Representations survive until 60 days after expiration of the applicable statute of limitations, (b) the representations in Sections 4.9 (Intellectual Property), 4.10 (Regulatory Compliance) and 4.11 (Data Privacy) survive for 36 months, and (c) covenants survive until fully performed.

If Seller resists 36 months, 24 months is a reasonable fallback for the regulatory and IP reps.

---

## 8. Indemnification Cap (10%) and Escrow (5%) Are Low for This Transaction

**Where:**
- SPA § 9.4(a): Seller's aggregate liability for rep/warranty breaches capped at 10% of Purchase Price = $18,650,000.
- SPA § 2.2(a): Escrow Amount = $9,325,000 (5% of Purchase Price).
- LOI § 4(a): Buyer proposed a 10% cap—so this matches the LOI.

**Why it matters:**
For an $186.5M acquisition of a medical device company, a $18.65M cap means Daikesk is self-insuring the top $167.85M of any pre-closing problem. If the IP representation is breached (e.g., a third party asserts the Company's products infringe its patents), defense costs and potential damages could easily exceed $18.65M. The escrow of $9.325M provides only a partial source of recovery; the remainder must be collected from Seller directly, which raises credit risk.

This is less urgent than Issues 1–6 (because the cap is at least consistent with the LOI), but it is worth flagging.

**Recommended fix:**

If the client is comfortable with the 10% cap as a business matter, consider:
- Increasing the escrow to 10% ($18,650,000) to match the cap, so the full cap is secured;
- Alternatively, adding a specific indemnity (outside the cap) for pre-closing IP infringement claims and FDA regulatory liabilities, with survival tied to the applicable statute of limitations.

**Question for client:** Is the 10% cap a business decision the client has already accepted, or is there room to push for a higher cap or a specific indemnity?

---

## 9. Only One Third-Party Consent Identified on Schedule 4.5

**Where:**
- SPA Schedule 4.5: lists only the Meridian Health Purchasing Alliance consent.
- SPA § 4.8: defines Material Contracts to include group purchasing arrangements, IP licenses, employment agreements with officers, and non-compete restrictions.
- SPA § 7.2(e): makes obtaining all Schedule 4.5 consents a condition to closing.

**Why it matters:**
A medical imaging company with an installed base served through field-service contracts, hospital GPO arrangements, and distributor relationships is likely to have multiple contracts with change-of-control or assignment provisions. The fact that only one consent is identified suggests either (a) the other contracts genuinely lack such provisions, or (b) the schedule is incomplete. If the schedule is incomplete, Daikesk could close and later discover that a material customer or supplier contract was terminated for lack of consent.

**Recommended fix:**

Before closing, confirm with Seller (and through our own diligence) that Schedule 4.5 is complete. Add a representation in the SPA that:

> Schedule 4.5 identifies all consents, approvals, waivers or authorizations required under any Material Contract in connection with the transactions contemplated by this Agreement.

If additional consents are identified, add them to the schedule and to the closing conditions.

---

## 10. TSA Lacks Specific Service Levels or Service Credits

**Where:**
- TSA § 2.2: Service Standard is "at least the same degree of care, priority, volume and timeliness" as the prior 12 months.
- TSA § 10.3: remedy for failure is re-performance at no charge.
- No service credits, no specific uptime requirements, no response-time metrics.

**Why it matters:**
The Service Standard is a baseline, not a target. If Seller's IT team is simultaneously supporting its own operations and the transition, "same degree of care" is hard to verify and even harder to enforce. For critical services like the ERP and detector supply chain, even brief outages can halt production. Without service credits or specific SLA metrics, Daikesk's only remedy is to argue that the Service Standard was not met—a fact-intensive dispute.

**Recommended fix:**

Add a schedule of service-level metrics for the most critical services (IT/ERP uptime, supply chain order-processing turnaround, data migration milestones). Provide for service credits (e.g., 5–10% of the monthly fee for the affected service) for failure to meet those metrics. This gives Daikesk a practical, low-friction remedy without needing to litigate whether the "degree of care" was sufficient.

---

## 11. SPA Does Not Require Key Employee Agreement as a Closing Deliverable

**Where:**
- SPA § 3.2: lists closing deliverables but does not include the Key Employee Agreement or any confirmation of its continued effectiveness.
- SPA § 1.1: defines "Ancillary Agreements" to include the Key Employee Agreement, but this definition is not operationalized in the closing conditions or deliverables.

**Why it matters:**
Related to Issue 1. Even if Dr. Ferreol consents to the Change of Control, Daikesk should receive confirmation at closing that the Key Employee Agreement remains in full force and effect, that no termination or amendment has been executed, and that Dr. Ferreol's employment is continuing. Without this, there is a gap between the representation (SPA § 4.8, which covers employment agreements with officers) and the actual state of affairs at closing.

**Recommended fix:**

Add to SPA § 3.2:

> **(h)** a certificate of an officer of Seller confirming that the Key Employee Agreement is in full force and effect, that no notice of termination or non-renewal has been given or received, and that the Key Employee is actively employed as of the Closing Date.

---

## Items I Cannot Resolve from the Documents Alone

| # | Item | What I Need |
|---|---|---|
| A | Whether Dr. Ferreol has been informed of the transaction and what her position is | Client confirmation / call with Dr. Ferreol's counsel |
| B | Whether the $14.2M Target Working Capital reflects the "normalized" level agreed during diligence | Diligence workpapers / prior correspondence with Seller |
| C | Whether Daikesk has standalone IT, field-service, and ultrasound supply-chain capabilities at closing | Client operational assessment |
| D | Whether there are additional contracts with change-of-control provisions not on Schedule 4.5 | Diligence contract review |
| E | The financial magnitude of the transition fees (to assess the TSA liability cap) | TSA fee schedule / Seller's cost allocation |
| F | Whether the Meridian GPO consent has been requested and what its status is | Seller confirmation |

---

## Suggested Priorities for Next Call with Client

1. **Confirm Dr. Ferreol's position.** If she is not supportive, we need to decide whether to make her consent a condition to closing (giving us walk-away rights) or to adjust the purchase price to reflect the IP risk. This is the single most important open item.

2. **Decide on the TSA scope.** If Daikesk needs field-service and ultrasound transition support, we must expand Schedule A before the TSA is finalized. The current draft is not sufficient for the business as described in the LOI.

3. **Negotiate the TSA liability cap carve-out.** The "notwithstanding" language in § 10.2 is a significant concession to Seller that should be revisited.

4. **Confirm working capital target.** Validate the $14.2M figure against diligence.

5. **Decide whether to push on survival periods and the indemnification cap.** These are less critical than items 1–3 but worth raising if we have negotiating capital.

---

*All section references are to the documents as currently drafted. The TSA remains in draft form (effective date blank), so items 2–5 and 10 are negotiable before execution. The SPA appears to be in final form (dated August 14, 2026), so amendments to the SPA would require Seller's agreement.*