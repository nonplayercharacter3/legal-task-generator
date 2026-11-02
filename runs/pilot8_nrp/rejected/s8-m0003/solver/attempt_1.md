# MEMORANDUM

**To:** Partner
**From:** Associate
**Re:** Ziteir Aerial Robotics, Inc. – Pre-Acquisition Contract Review (Lakix and Pellbrook)
**Date:** [Current]

---

## Summary

Ziteir's pending merger with Okonvale Agritech Holdings, Inc. (expected closing November 30, 2026) raises several material issues under its existing contracts. The most urgent is that the Ziteir–Lakix Supply Agreement treats a change of control as a deemed assignment requiring Lakix's prior written consent, and the October 15, 2026 letter to Lakix does not actually request that consent. If Lakix withholds consent or challenges the letter's reasoning, it has the right to terminate the agreement and claim damages. Below are the issues I identified, in order of practical significance.

---

## Issue 1: Change of Control Triggers Consent Right Under Supply Agreement § 15.2; Letter Does Not Request Consent

**Where:** Supply Agreement § 15.2; Letter § 2.

**What the contract says:** Section 15.2 provides that "Any change of control of Supplier, including a merger, consolidation, sale of equity or other transaction in which more than 50% of Supplier's voting equity changes hands, is deemed an assignment of this Agreement. Any such assignment requires Lakix's prior written consent. Failure to obtain that consent is a material breach of this Agreement and entitles Lakix to terminate this Agreement by written notice and to recover its damages."

**What the letter says:** Section 2 of the October 15, 2026 letter states: "Ziteir will remain the same legal entity after closing, and the Agreement will remain with Ziteir. Ziteir will not assign or transfer the Agreement … Accordingly, no consent of Lakix is required in connection with the Transaction. This letter is provided for informational purposes only, and Lakix does not need to take any action in response to it."

**Why it matters:** The transaction structure described in the letter (Okonvale subsidiary merges into Ziteir; Ziteir survives as a wholly owned subsidiary of Okonvale; Okonvale acquires all outstanding equity) is unambiguously a change of control under § 15.2. More than 50% of Ziteir's voting equity changes hands. The clause does not carve out surviving-entity mergers. The letter's argument that no "assignment" occurs because Ziteir survives as the same legal entity is textually inconsistent with the clause, which expressly *deems* a change of control to be an assignment. If Lakix disagrees, it has a colorable argument that it has been materially breached and can terminate the Supply Agreement, the DPA, and (by incorporation) the SOW. Termination would cut off Ziteir/Okonvale's revenue from the Platform subscription, spare parts, and any future drone sales to Lakix, and would trigger the data return/deletion obligations in DPA § 9.

Additionally, the letter does not *request* consent. Even if the "no consent required" position were correct as a matter of law, the safer commercial approach would have been to request consent affirmatively. As drafted, the letter invites a dispute.

**Recommended fix:**

- Before closing, send a supplemental letter to Lakix that (a) acknowledges § 15.2 applies, (b) affirmatively requests Lakix's written consent to the change of control, and (c) offers to negotiate any reasonable conditions Lakix might want (e.g., a commitment to maintain service levels, insurance, or pricing). Frame it as a courtesy and relationship matter.
- If Lakix consents in writing, file the consent with the transaction records.
- If Lakix refuses or does not respond, escalate to the partner for a risk assessment: the worst case is termination at or after closing, which would be a material adverse change in Ziteir's revenue base that Okonvale should price into the deal. Consider whether the merger agreement with Okonvale has a material adverse change or closing condition that would be triggered.
- Flag to the client that the current letter, standing alone, is insufficient to protect Ziteir/Okonvale.

---

## Issue 2: Uncapped, Strict-Liability Data Incident Indemnity in the DPA

**Where:** DPA § 8.1–8.2.

**What the contract says:** Section 8.1 requires Ziteir (as Processor) to defend, indemnify and hold harmless Lakix, its Affiliates, and *each Grower* from all losses arising out of any Security Incident involving Grower Data, including regulatory fines, notification costs, credit monitoring, forensics, and third-party claims. Section 8.2 states this indemnity applies "whether or not caused by Processor's fault" and "shall not be subject to any limitation of liability in the Agreement."

**Why it matters:** This is a strict-liability, uncapped indemnity that extends to Lakix's own customers (the Growers). If a data breach occurs in the Platform—whether caused by Ziteir, a sub-processor, or even a third-party hacker—Ziteir/Okonvale bears unlimited financial exposure. The Supply Agreement's liability cap (§ 11.1: 12 months of fees) and consequential damages waiver (§ 11.2) are expressly overridden for this indemnity. Given that the Platform holds sensitive agronomic data, geolocation data, and personal data of growers and their personnel (DPA § 1.4, Annex 1), a breach could generate significant regulatory and class-action exposure. Okonvale inherits this obligation at closing.

**Recommended fix:**

- For the transaction: Ensure Okonvale's deal team prices this exposure. Request Ziteir's most recent penetration test report, security audit, and cyber insurance policy (the $3M cyber policy required by Supply Agreement § 13(c) may be insufficient for an uncapped indemnity).
- Going forward: In any renewal or amendment negotiation with Lakix, seek to (a) make the indemnity fault-based rather than strict liability, (b) cap it at a multiple of annual fees or the cyber insurance limit, and (c) limit the class of indemnitees to Lakix and its Affiliates (remove individual Growers).
- Confirm that Ziteir's cyber insurance policy names Lakix (and potentially Growers) as additional insureds or at least provides a direct payment mechanism for the indemnity.

---

## Issue 3: Governing Law and Forum Conflict Between SOW and Supply Agreement

**Where:** SOW § 9.1–9.2; Supply Agreement § 18.1–18.2; Supply Agreement § 18.3 (Order of Precedence).

**What the contracts say:** The Supply Agreement specifies Delaware law and exclusive jurisdiction in New Castle County, Delaware. SOW 001 specifies New York law and exclusive jurisdiction in the Borough of Manhattan. Supply Agreement § 18.3 provides that in case of conflict, the SOW prevails over the Supply Agreement.

**Why it matters:** Any dispute arising from the Services (commissioning, training, season support) will be governed by New York law and litigated in Manhattan, while disputes about the Products (drones, spare parts, Platform subscription) will be governed by Delaware law and litigated in New Castle County. This creates: (a) a higher cost base (New York counsel plus Delaware counsel); (b) potential for inconsistent outcomes if related claims are split; and (c) strategic complexity if Lakix brings a termination claim under § 15.2 (which is in the Supply Agreement, governed by Delaware law) alongside a services-quality claim (governed by New York law).

**Recommended fix:**

- This is a legacy drafting issue that is difficult to fix unilaterally. Flag it to the client as a risk factor.
- In any future SOW or amendment, conform the governing law and forum to Delaware to match the master agreement.
- For the pending transaction, ensure the deal team understands that a Lakix challenge to the change of control would likely be brought in Delaware (because § 15.2 is in the Supply Agreement), not New York.

---

## Issue 4: Ambiguity on Whether Supply Agreement § 15.2 Applies to the SOW

**Where:** SOW § 10.1; Supply Agreement § 15.2, § 18.3.

**What the contracts say:** SOW § 10.1 states: "This SOW forms part of the Agreement. Sections 11 (Limitation of Liability), 12 (Confidentiality), 16 (Force Majeure) and 17 (Notices) of the Agreement apply to this SOW." It specifically enumerates four sections of the Supply Agreement that apply. Section 15 (Assignment) is not listed. However, the SOW also says it "forms part of the Agreement," which could mean all terms of the Agreement apply unless displaced by the SOW's own terms.

**Why it matters:** If § 15.2 does *not* apply to the SOW, then even if Lakix successfully terminates the Supply Agreement for the change of control, the SOW (and the services being performed under Phase 3) might survive. Conversely, if § 15.2 *does* apply to the SOW (because the SOW "forms part of" the Agreement), termination of the Supply Agreement could cascade to the SOW. The ambiguity cuts both ways and creates uncertainty about what Okonvale actually acquires at closing.

**Recommended fix:**

- Seek a clarifying side letter from Lakix confirming that the SOW continues in effect regardless of any dispute over the Supply Agreement, or that Lakix consents to the change of control as it applies to both documents.
- In the supplemental consent request (see Issue 1), expressly reference the SOW and ask for consent to the change of control "as it relates to the Agreement, the DPA, and all Statements of Work hereunder."

---

## Issue 5: SOW Phase 3 Is Actively in Performance at Closing

**Where:** SOW § 3 (Phase 3: September 1, 2026 to February 28, 2027; Season Support Window: October 1, 2026 to November 30, 2026); Letter § 3(c).

**Why it matters:** At the expected closing date (November 30, 2026), Phase 3 commissioning is ongoing and the fall season support window is in its final week. Ziteir has committed to a dedicated field support engineer (6 a.m.–8 p.m. ET, seven days a week) and 24-hour on-site response. If Lakix terminates the agreement post-closing (under Issue 1), Ziteir/Okonvale would be mid-performance, with potential claims for work performed but not yet invoiced, and the obligation to transition out of active operations at three sites. The letter (Section 3(c)) represents that Phase 3 will continue "on the existing schedule, using the same Ziteir project team"—a representation Okonvale would inherit.

**Recommended fix:**

- Confirm that all Phase 3 invoices through November 30, 2026 are sent and paid before closing, or that the merger agreement allocates pre-closing receivables appropriately.
- Ensure the Ziteir project team (Priya N. Calloway and staff) is contractually committed through at least the end of Phase 3 (February 28, 2027) or that Okonvale has a retention/transition plan.
- If the consent issue (Issue 1) is not resolved before closing, consider whether to delay closing until Phase 3's season support window ends (November 30, 2026—coincidentally the same date) or until Phase 3 commissioning is complete (February 28, 2027).

---

## Issue 6: Fixed Pricing Locked In for Up to Eight Years

**Where:** Supply Agreement § 4.2; § 2.1–2.2.

**What the contract says:** "The prices set out in Exhibit B are fixed for the duration of the Term." The Term is the Initial Term (through February 28, 2027) plus successive three-year Renewal Terms. If both parties allow renewal to occur (no non-renewal notice given 30 days before term end), the Term could extend to February 28, 2033.

**Why it matters:** Drone hardware costs (components, lithium batteries, radar modules) and Platform infrastructure costs (AWS, personnel) are likely to increase over an eight-year period. Ziteir/Okonvale is contractually locked into the Exhibit B prices ($38,500 per drone; $1,400 per drone per year for Platform; spare parts at listed prices) for the entire Term. This is a margin compression risk that Okonvale should model.

**Recommended fix:**

- Model the revenue and cost trajectory under fixed pricing through 2033.
- In any renewal negotiation (the first non-renewal window opens around January 29, 2027—30 days before February 28, 2027), seek to reset pricing or add a cost-of-living/component-cost escalator.
- Note that Lakix also has the right to prevent renewal on the same 30-day notice, so Ziteir/Okonvale cannot unilaterally extend the pricing lock.

---

## Issue 7: Pellbrook Lease – Post-Closing Notice Obligation

**Where:** Pellbrook Lease § 11.2(c).

**What the contract says:** Tenant may "undergo any transfer of its equity interests or any change of control, including by merger" without Landlord's consent, but must give "written notice to Landlord within 30 days after the transaction."

**Why it matters:** This is favorable—no consent is needed, unlike the Lakix agreement. But the notice obligation is affirmative and time-limited (30 days post-closing). If missed, it could technically constitute a default under § 12.1(b) (failure to perform an obligation within 30 days after written notice), though the practical consequence would be minimal.

**Recommended fix:**

- Calendar the notice deadline: no later than December 30, 2026 (30 days after the expected November 30, 2026 closing).
- Prepare the notice now so it can be sent promptly at or after closing.
- Confirm the notice address: Pellbrook Airfield Properties, LLC, 900 Runway View Drive, Middletown, Delaware 19709, Attention: Property Manager (Lease § 15).

---

## Issue 8: Pellbrook Lease – Extension Option Deadline

**Where:** Pellbrook Lease § 3.2.

**What the contract says:** Tenant may extend for one additional five-year term by written notice "no earlier than 12 months and no later than nine months before the Expiration Date." The Expiration Date is January 31, 2029.

**Why it matters:** The exercise window is **February 1, 2028 through April 30, 2028**. If Ziteir/Okonvale wants the option to remain the hangar (which houses the test corridor, battery charging infrastructure, RTK base station, and the dedicated 400-amp electrical service built under Landlord's Work in Exhibit B), it must act within that window. Missing it means the lease ends January 31, 2029, and Ziteir/Okonvale would need to relocate or re-negotiate.

**Recommended fix:**

- Calendar the extension window now (February 1, 2028 – April 30, 2028).
- Begin internal decision-making by Q4 2027: does Okonvale's strategic plan for Ziteir include continued use of the Pellbrook facility?
- If exercising, note that Extension Term rent is 95% of fair market rent (Lease § 3.3), to be agreed or determined by a broker. Begin market research in 2027 to understand the likely number.

---

## Issue 9: DPA Sub-Processor Change Restrictions Could Constrain Post-Acquisition Integration

**Where:** DPA § 5.1–5.2; Letter § 3(d).

**What the contract says:** Ziteir generally authorizes existing sub-processors (AWS, Twilio, Zendesk—DPA Annex 3). New sub-processors require 30 days' prior written notice to Lakix, who may object on "reasonable data protection grounds." If the objection cannot be resolved within 30 days, Lakix may terminate the affected Platform subscriptions without penalty.

The letter represents that sub-processors "will not change as a result of the Transaction" and that any post-closing change will follow § 5.2.

**Why it matters:** Post-acquisition, Okonvale may want to consolidate Ziteir's cloud infrastructure onto Okonvale's own AWS account, change the customer support platform, or integrate the telemetry data into a broader Okonvale data lake. Each of these could constitute a "new sub-processor" or a material change in processing that triggers the notice-and-objection right. If Lakix objects and the parties cannot resolve it, Lakix can walk away from the Platform subscription without penalty—removing a recurring revenue stream.

**Recommended fix:**

- Before closing, identify any sub-processor changes Okonvale plans in the first 12–18 months post-closing.
- If changes are anticipated, either (a) delay them until after the renewal cycle, or (b) proactively notify Lakix under § 5.2 well in advance and be prepared to address reasonable concerns.
- Ensure the letter's representation (no sub-processor change "as a result of the Transaction") is accurate as of closing. If Okonvale's integration plan would change the AWS account structure, that may be a "change" even if the sub-processor entity remains AWS.

---

## Issue 10: Deemed Acceptance of Purchase Orders (Operational Risk During Transition)

**Where:** Supply Agreement § 3.2.

**What the contract says:** "If Ziteir does not respond [to a Purchase Order] within five business days after receipt, the Purchase Order is deemed accepted."

**Why it matters:** During the transition period (Q4 2026 – Q1 2027), Ziteir's operations team may be distracted by integration activities. If a Purchase Order sits unresponded for five business days, Ziteir is contractually bound to fulfill it. This is a low-probability but high-impact operational risk: an unintended commitment to deliver drones or spare parts at fixed prices.

**Recommended fix:**

- Brief Ziteir's sales/operations team before closing: all Lakix Purchase Orders must be affirmatively accepted or rejected within five business days, without exception, during the transition period.
- If possible, implement an automated acknowledgment workflow.

---

## Issue 11: Insurance Obligations Survive and Are Inherited by Okonvale

**Where:** Supply Agreement § 13; Pellbrook Lease § 9.1.

**What the contracts say:** Ziteir must maintain (under the Supply Agreement) $5M CGL, $5M aviation liability, and $3M cyber liability. Under the Pellbrook Lease, Ziteir must maintain $2M/$4M CGL, $5M aviation liability, property insurance at full replacement cost, and workers' comp, with Landlord named as additional insured.

**Why it matters:** These are ongoing obligations that Okonvale inherits at closing. The combined aviation liability requirement ($5M under both contracts) and the cyber liability requirement ($3M, which may be inadequate for the uncapped DPA indemnity in Issue 2) need to be confirmed in Okonvale's insurance program. If Okonvale's existing policies do not cover Ziteir's operations or do not meet these thresholds, there is an immediate compliance gap at closing.

**Recommended fix:**

- Confirm with Ziteir's broker that all required policies are in force through at least the first renewal date post-closing.
- Verify that Okonvale's insurance program (or Ziteir's, if maintained separately) meets both the Supply Agreement and Lease requirements simultaneously.
- For the DPA indemnity (Issue 2), assess whether the $3M cyber policy is adequate or whether additional coverage is needed.

---

## Items Flagged as Ambiguous or Requiring Additional Context

1. **Merger agreement terms.** I have not seen the Ziteir–Okonvale merger agreement. Key questions: Does it have a condition that all material contracts be assigned or consented to? Does it define "material contract" in a way that captures the Lakix Supply Agreement? Is there a MAC clause that could be triggered if Lakix terminates? I would need to review this to assess whether the § 15.2 consent issue is a closing risk or a post-closing risk.

2. **Lakix's response to the October 15 letter.** I do not have any response from Lakix. If Lakix has already objected or requested consent, the analysis changes. If Lakix has remained silent, the silence is not consent (the letter explicitly says no action is required, which may be read as waiving the consent right—but that is an aggressive position).

3. **Ziteir's current insurance policies.** I have not seen the actual policies or certificates. The contractual requirements are clear, but I cannot confirm compliance without the policies.

4. **Whether the Pellbrook lease notice has been or will be coordinated with the Lakix consent process.** If Ziteir sends the Pellbrook notice (required within 30 days post-closing) before resolving the Lakix consent issue, it may publicly signal the change of control to a third party (the landlord) while the Lakix dispute is unresolved. This is a minor tactical consideration.

5. **Exhibit A to the Supply Agreement (service levels).** The 99.5% monthly availability commitment with a 10% service credit is referenced but the full Exhibit A text was cut off in the matter folder (page 3 ends mid-sentence on "one ground"). I would want to confirm the full service level terms and any liquidated damages or termination rights tied to chronic service level failures.

---

## Priority Action Items for the Client

| # | Action | Deadline | Owner |
|---|--------|----------|-------|
| 1 | Send supplemental letter to Lakix requesting written consent under § 15.2 | Before November 30, 2026 closing | Ziteir GC / outside counsel |
| 2 | Calendar Pellbrook lease notice (30 days post-closing) | By December 30, 2026 | Ziteir GC |
| 3 | Confirm insurance program meets all contractual requirements at and after closing | Before closing | Ziteir CFO / broker |
| 4 | Calendar Pellbrook extension option window | February 1 – April 30, 2028 | Ziteir GC / Facilities |
| 5 | Brief operations team on Purchase Order deemed-acceptance risk | Immediately | Ziteir COO |
| 6 | Identify any planned sub-processor changes in first 12 months post-closing | Before closing | Ziteir CTO / Okonvale IT |
| 7 | Model fixed-pricing margin through 2033 | Before closing (for Okonvale deal team) | Ziteir CFO |