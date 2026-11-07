# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Seinon Outdoor Gear, Inc. – Poseirt Commerce Logistics, LLC: Pre-Signing Issue Identification

---

## Summary

I have reviewed the Poseirt Master Services Agreement ("**MSA**"), Order Form No. 1 ("**Order Form**"), and Service Level Schedule ("**Schedule**"). I also reviewed the Kelvane Fabric Testing Agreement for contextual purposes (see Part E below). The Poseirt documents contain several provisions that materially increase Seinon's risk or restrict its flexibility. The four issues marked **CLIENT DECISION NEEDED** should be raised with the business team before we send a redline to Poseirt, because each involves a commercial trade-off that legal alone cannot resolve.

---

## A. Critical Issues

### Issue 1 – Order Form Exclusivity Is Dramatically Broader Than the MSA

**Where:** Order Form § 4, read against MSA § 2.4.

**What it says:**

- MSA § 2.4 limits exclusivity to "direct-to-consumer e-commerce fulfillment of Seinon products shipped to the United States and Canada" and expressly carves out all other channels and territories.
- Order Form § 4 expands exclusivity to "all fulfillment, warehousing and logistics services for all Seinon products in all sales channels worldwide, including direct-to-consumer e-commerce, wholesale distribution and retail-store replenishment," and adds that Customer "will not engage, and will cause its Affiliates not to engage, any third party to provide those services during the term of this Order Form."

**Why it matters:** Under MSA § 1.3 (Order of Precedence), the Order Form controls over the MSA in the event of a conflict. The Order Form therefore overrides the MSA's narrower exclusivity and locks Seinon into Poseirt as its *sole* global fulfillment provider—for DTC, wholesale, and retail-store replenishment—for the entire 60-month Initial Term (plus any renewal terms). If Poseirt underperforms in a non-DTC channel (e.g., retail-store replenishment), Seinon has no ability to bring in a secondary 3PL without breaching the Order Form. The Affiliate restriction further constrains any group-level logistics strategy.

**Recommended fix:**

> Delete Order Form § 4 in its entirety and replace with: "During the term of this Order Form, Customer will use Provider as its exclusive provider of direct-to-consumer e-commerce fulfillment of Seinon products shipped to the United States and Canada, consistent with Section 2.4 of the Agreement. Nothing in this Order Form restricts Customer from using any other provider for wholesale distribution, retail-store replenishment, or fulfillment in any territory outside the United States and Canada."

**CLIENT DECISION NEEDED:** Confirm with the business team whether the expanded exclusivity (all channels, worldwide, including Affiliates) was a deliberate commercial concession or a drafting error by Poseirt. If it was negotiated, understand what consideration Seinon received in exchange.

---

### Issue 2 – Service Level Schedule Overrides the MSA's Security Incident Protections

**Where:** Schedule § 6.3, read against MSA §§ 11.1, 11.3(b), and 8.3.

**What it says:**

- MSA § 11.3(b) carves Security Incidents out of both the consequential-damages exclusion (§ 11.1) and the liability cap (§ 11.2). MSA § 8.3(c) obligates Provider to reimburse Customer's notification, credit-monitoring, and call-center costs.
- Schedule § 6.3 states: "Service Credits and Customer's termination right under Section 6.2 are Customer's **sole and exclusive remedies** for any Service Failure, **including any Security Incident**." It then adds: "Notwithstanding Section 11.3 of the MSA, Provider's aggregate liability arising out of or relating to Security Incidents **shall not exceed the cap set out in Section 11.2 of the MSA**."

**Why it matters:** A "Security Incident" is defined as a "Service Failure" in Schedule § 2(e). The exclusive-remedy clause therefore converts what the MSA intended to be an uncapped, full-recovery obligation into a regime where Seinon's maximum recovery for a data breach is (a) service credits capped at 25% of the Monthly Platform Fee per month (§ 5.2), plus (b) the 12-month-fee liability cap. For a company processing consumer payment card data, this is a severe exposure gap. If a breach results in PCI fines, class-action defense costs, or regulatory penalties in the tens or hundreds of millions, Seinon's contractual recovery from Poseirt is limited to roughly $600K–$1M (12 months of fees). The "sole and exclusive remedy" language also creates a serious argument that MSA § 8.3(c) (reimbursement of notification/credit-monitoring costs) is subsumed by the service credit regime, leaving Seinon to absorb those costs itself.

**Recommended fix:**

> Amend Schedule § 6.3 to read: "Service Credits and Customer's termination right under Section 6.2 are Customer's sole and exclusive remedies for a Service Failure **other than a Security Incident**. In the case of a Security Incident, Customer's remedies include, in addition to Service Credits and the termination right under Section 6.2, all rights and remedies available under Sections 8.3 and 11.3 of the MSA. **Delete** the sentence beginning 'Notwithstanding Section 11.3 of the MSA…' in its entirety."

If Poseirt resists full deletion, a fallback would be to raise the Security Incident cap to the Provider's cyber insurance limit ($10M under MSA § 12) and expressly preserve § 8.3(c) reimbursement obligations outside the exclusive-remedy clause.

**CLIENT DECISION NEEDED:** Confirm the volume and sensitivity of Shopper Data (cardholder data, SSNs, etc.) that will flow through the Platform. This determines whether the uncapped MSA position is non-negotiable or whether a super-cap (e.g., $10M, matching the cyber policy) is an acceptable business risk.

---

### Issue 3 – Customer Indemnity Extends to Claims Caused in Part by Provider

**Where:** MSA § 10.2, first sentence.

**What it says:** "Customer will defend Provider … against any third-party claim arising out of or relating to the Products or the Customer Materials, **regardless of whether caused in part by Provider handling, storage or shipment of the Products**."

**Why it matters:** This language means that if Poseirt mishandles a product (e.g., stores waterproof garments in a non-climate-controlled area, causing mold; or ships a product with a defective seam tape that was fine on receipt), and an end consumer is injured or brings a product liability claim, Seinon must still indemnify Poseirt. The "regardless of whether caused in part by Provider" clause effectively makes Seinon the insurer of Poseirt's operational errors. This is particularly concerning given that the Order Form's expanded exclusivity (Issue 1) means all of Seinon's products—across all channels—will be in Poseirt's hands.

**Recommended fix:**

> Delete the phrase "regardless of whether caused in part by Provider handling, storage or shipment of the Products." Replace with: "Customer will defend Provider … against any third-party claim arising out of or relating to the Products or the Customer Materials, **to the extent such claim is not caused by Provider's negligence, willful misconduct, or breach of this Agreement**."

---

### Issue 4 – Governing Law and Venue Conflict Between MSA and Order Form

**Where:** Order Form § 8, read against MSA § 14.1–14.2.

**What it says:**

- MSA § 14.1: Delaware law. MSA § 14.2: exclusive jurisdiction in Wilmington, Delaware.
- Order Form § 8: New York law; exclusive jurisdiction in New York County, New York.

**Why it matters:** Under the MSA's own order of precedence (§ 1.3), the Order Form controls. So the effective governing law is New York and the effective venue is New York County. This is likely a drafting error (Poseirt may have used a New York template for the Order Form), but as written it creates: (a) uncertainty about which state's contract law applies to interpretation of the MSA's general provisions; (b) a split where some claims might be characterized as "arising out of" the MSA (Delaware) versus the Order Form (New York); and (c) a less favorable forum for Seinon, a Delaware corporation, which would have to litigate in New York.

**Recommended fix:**

> Delete Order Form § 8 in its entirety. Add: "Governing law and venue are as set forth in Section 14 of the Agreement."

---

## B. Significant Issues

### Issue 5 – Auto-Renewal for Successive 60-Month Terms

**Where:** MSA § 9.2; Order Form § 2.

**What it says:** The Initial Term is 60 months. Each Order Form "renews automatically … for a successive renewal term equal in length to its Initial Term." Non-renewal notice must be given "no earlier than 100 days and no later than 90 days before the expiration of the then-current term."

**Why it matters:** If Seinon misses the narrow 10-day notice window (between 100 and 90 days pre-expiration), it is locked in for another 60 months. Over time, this could extend the relationship indefinitely. Combined with the broad exclusivity (Issue 1), a missed notice deadline means Seinon cannot use any other fulfillment provider worldwide for five more years.

**Recommended fix:**

> Amend MSA § 9.2 to: (a) reduce the renewal term to 12 months (rather than equal to the Initial Term); and (b) widen the non-renewal notice window to "no earlier than 180 days and no later than 60 days before expiration." Alternatively, add: "Customer may terminate any Order Form for convenience on twelve (12) months' written notice, without penalty, after the first twenty-four (24) months of the Initial Term."

**CLIENT DECISION NEEDED:** The business team should confirm whether a 60-month initial commitment is acceptable given that the Platform and fulfillment integration will be deeply embedded in Seinon's operations. If yes, the auto-renewal term length and notice window are the key negotiating points.

---

### Issue 6 – Service Credits Capped at 25% of Monthly Platform Fee

**Where:** Schedule § 5.2.

**What it says:** "The total Service Credits for any Measurement Period will not exceed twenty-five percent (25%) of the Monthly Platform Fee for that Measurement Period."

**Why it matters:** 25% of $48,500 = $12,125 per month. If the Storefront is down for an entire month (0% availability), Seinon's maximum recovery is $12,125—while potentially losing hundreds of thousands in sales. The credit structure compensates for a sliver of the Monthly Platform Fee, not for actual losses. This is standard in the industry but is particularly thin here because the exclusive-remedy clause (Issue 2) prevents Seinon from claiming actual damages.

**Recommended fix:**

> Increase the cap to 50% of the Monthly Platform Fee, or (preferably) provide that the cap does not apply where the Service Failure results in the Storefront being unavailable for more than four (4) consecutive hours in a Measurement Period.

---

### Issue 7 – Liability Cap at 12 Months of Fees

**Where:** MSA § 11.2.

**What it says:** "Each party's aggregate liability … will not exceed the fees paid or payable in the 12 months preceding the claim."

**Why it matters:** In the first year, total fees are approximately $582,000 in platform fees plus variable fulfillment fees. If monthly fulfillment volume is, say, $200,000, the 12-month cap is roughly $2.98M. While not trivial, this is low relative to the revenue at risk if the Storefront is down or inventory is lost at scale. The cap is mutual, but in practice most claims will be brought by Seinon against Poseirt.

**Recommended fix:**

> Increase the cap to the greater of (a) fees paid or payable in the 24 months preceding the claim, or (b) $5,000,000. Preserve the existing carve-outs in § 11.3 (indemnification, confidentiality breach, Security Incidents, gross negligence/willful misconduct).

---

### Issue 8 – Transition Assistance Limited to 90 Days

**Where:** MSA § 9.5.

**What it says:** Provider will provide transition assistance "for up to ninety (90) days, at the rates in effect under that Order Form."

**Why it matters:** If the expanded exclusivity (Issue 1) is accepted, Seinon may need to transition *all* global fulfillment—DTC, wholesale, retail replenishment—off Poseirt's platform and out of its Reno warehouse. Ninety days is likely insufficient to (a) migrate the Storefront to a new platform, (b) physically move inventory, and (c) re-integrate a new 3PL for wholesale and retail channels. After 90 days, Poseirt has no contractual obligation to assist, and could leverage that to extract higher transition fees or hold inventory hostage.

**Recommended fix:**

> Extend transition assistance to one hundred eighty (180) days. Add: "Provider will not charge any premium or surge rate for transition assistance beyond the rates in effect under the Order Form immediately preceding expiration or termination. Provider will cooperate in good faith to ensure an orderly transition and will not interpose any obstacle to Customer's engagement of a replacement provider."

---

### Issue 9 – Broad Exception to Service Credits for Customer Breach

**Where:** Schedule § 5.4(c).

**What it says:** No Service Credit is due "to the extent the failure is caused by … Customer's breach of Section 4 of the MSA, including late or inaccurate advance shipping notices."

**Why it matters:** MSA § 4 imposes three obligations on Customer: (a) deliver products properly packaged with accurate ASNs; (b) ensure product compliance with law; and (c) provide timely cooperation. The "including" language suggests the exception is not limited to ASNs but extends to any § 4 breach. If Seinon is slightly late on a cooperation request (§ 4.3) and that coincides with a ship-timeliness miss, Poseirt could argue no credit is owed. This gives Poseirt a broad, easy-to-invoke escape from its service level commitments.

**Recommended fix:**

> Narrow § 5.4(c) to: "Customer's failure to deliver Products in accordance with Section 4.1(a) (improper packaging, labeling, or advance shipping notices), **and only to the extent such failure is the direct and proximate cause of the Service Level miss**."

---

### Issue 10 – One-Way Feedback License

**Where:** MSA § 13.3.

**What it says:** "Provider may use any suggestions that Customer provides about the Platform without obligation."

**Why it matters:** Over a 60-month term, Seinon's operations team will inevitably suggest Platform improvements (new reporting features, integration workflows, packaging logic, etc.). This clause gives Poseirt a perpetual, royalty-free right to use those suggestions for its other customers. For a company whose competitive edge may partly reside in its e-commerce operational workflows, this is an IP leak.

**Recommended fix:**

> Amend to: "Provider may use general, non-proprietary suggestions that Customer provides about the Platform, provided that such suggestions do not incorporate or reveal Customer's Confidential Information, trade secrets, or proprietary business processes. Provider will not use any suggestion that is specifically identified by Customer in writing as proprietary."

---

## C. Moderate Issues

### Issue 11 – Assignment Without Consent to a Successor

**Where:** MSA § 15.2.

**What it says:** Either party may assign "without consent to a successor to all or substantially all of its business or assets, if it gives written notice."

**Why it matters:** If Poseirt is acquired by a competitor of Seinon, or by a company with a poor security track record, the agreement (including all Shopper Data and Customer Materials) transfers automatically. Seinon has no right to object or terminate.

**Recommended fix:**

> Add: "Notwithstanding the foregoing, Customer may terminate the affected Order Form without penalty within ninety (90) days after receiving notice of an assignment by Provider, if the assignee is a direct competitor of Customer or if the assignment results in a material diminution of Provider's security program as described in Section 8.2."

---

### Issue 12 – Limited Verification Rights

**Where:** Schedule § 4.4.

**What it says:** Customer may have Provider's measurements verified by an independent third party "no more than once per contract year."

**Why it matters:** Over a 60-month term, that is only five verification opportunities. If Seinon suspects systematic under-reporting of service failures (e.g., the WMS is configured to exclude certain order types from the SL-5 ship-timeliness calculation), it cannot independently confirm for up to 12 months.

**Recommended fix:**

> Increase to "no more than once per quarter" or "upon reasonable suspicion of material misreporting, no more than twice per contract year."

---

### Issue 13 – Fee Escalation After Month 24

**Where:** Order Form § 3.5.

**What it says:** After the first 24 months, Provider may increase fulfillment fees once per 12-month period, up to 3%, on 60 days' notice.

**Why it matters:** Over the remaining 36 months of the Initial Term, Seinon faces up to three 3% increases (~9.3% cumulative). This is modest but compounds with the long term. More importantly, the Monthly Platform Fee ($48,500) is *not* subject to the 3% cap—only "fulfillment fees in Section 3.2" are. The Platform Fee could theoretically be increased by amendment (MSA § 15.5 requires mutual written agreement, so this is less of a risk, but worth confirming).

**Recommended fix:**

> Clarify that the Monthly Platform Fee is fixed for the entire Initial Term. If Poseirt insists on escalation rights, cap the Platform Fee increase at the same 3% and require 90 days' notice (rather than 60).

---

### Issue 14 – "Standard API" Limitation for ERP Integration

**Where:** Order Form § 5.1(c).

**What it says:** Integration of the Platform with Customer's ERP is "through Provider's standard API."

**Why it matters:** If Seinon's ERP requires custom fields, non-standard data formats, or bidirectional synchronization beyond what the "standard API" supports, Poseirt has no obligation to accommodate. This could create operational friction or force Seinon to build workarounds.

**Recommended fix:**

> Add: "If Customer's ERP integration requires functionality beyond Provider's standard API, Provider will perform such custom integration at Provider's then-standard professional services rates, to be agreed in a change order under Section 2.5 of the Agreement. Provider will use commercially reasonable efforts to accommodate Customer's integration requirements."

---

### Issue 15 – 25-User Limit with No Overflow Pricing

**Where:** Order Form § 3.1.

**What it says:** The Monthly Platform Fee includes "access for up to twenty-five (25) named Customer users."

**Why it matters:** There is no stated fee for additional users. If Seinon's operations team grows beyond 25 users (e.g., adding warehouse staff, customer service reps, or Affiliate users), the commercial terms are silent. This could become a billing dispute.

**Recommended fix:**

> Add: "Access for additional named users beyond twenty-five (25) will be provided at $[X] per user per month, or at no additional charge for users who are employees or contractors of Customer's Affiliates and who require access solely for fulfillment operations."

---

## D. Additional Observations

| # | Item | Location | Comment |
|---|------|----------|---------|
| 16 | Warehouse legal liability insurance = "Full replacement value of Products at the Facility" | MSA § 12 | Vague. "Replacement value" is not defined. Should be tied to a specific dollar amount or to Customer's declared inventory value. |
| 17 | Force majeure does not excuse "Provider's business continuity obligations" | MSA § 15.3 | The MSA does not actually contain a business continuity obligation. This reference is to a section that doesn't exist, creating ambiguity. |
| 18 | No SLA for data migration / go-live | Order Form § 6.2 | Go-live is "targeted" for 90 days but there is no service level, credit, or termination right if the target is missed. |
| 19 | MSA § 3.2 requires monthly performance reporting | MSA § 3.2 | Consistent with Schedule § 4.3 (10 Business Days). No issue, but confirm the report format is specified. |
| 20 | No audit right for security | MSA § 8.2 | Provider must "maintain" a security program but Customer has no right to audit or request SOC 2 / ISO 27001 reports. |

**Recommended fix for Item 20:** Add to MSA § 8.2: "Provider will make available to Customer, upon reasonable request no more than once per year, its most recent SOC 2 Type II report or equivalent independent security assessment. Provider will notify Customer promptly of any material change to its security program."

---

## E. Note on the Kelvane Fabric Testing Agreement

The Kelvane agreement is a separate vendor relationship (textile testing) and does not create any direct legal obligation or right that affects the Poseirt deal. However, two contrasts are worth flagging to the client as negotiating context:

1. **Termination for convenience.** The Kelvane agreement permits either party to terminate on 30 days' notice (§ 13.2). The Poseirt MSA has no termination-for-convenience right for Customer. Given that Seinon is comfortable with short-notice exit in its other vendor relationships, the absence of any convenience exit in the Poseirt agreement (combined with 60-month auto-renewals) is a significant structural difference the business team should understand.

2. **Indemnity standard.** Under Kelvane § 10, each party's indemnity obligation is limited to claims arising from its "gross negligence or willful misconduct." Under Poseirt MSA § 10.2, Customer's indemnity to Provider is not fault-limited at all—it covers any claim "arising out of or relating to the Products" regardless of Provider's role. This is a much less favorable position for Seinon.

These points do not require changes to the Kelvane agreement but should inform the client's risk tolerance discussion regarding the Poseirt deal.

---

## F. Items Requiring Client Input Before We Respond to Poseirt

| Priority | Issue | Question for Client |
|----------|-------|--------------------|
| 1 | Exclusivity scope (Issue 1) | Was the worldwide, all-channels exclusivity a deliberate business decision? What is the strategic cost of being locked to a single 3PL for wholesale and retail replenishment? |
| 2 | Security Incident remedy (Issue 2) | What is the estimated value of Shopper Data at risk (record count, payment card data, PII)? Is a $10M super-cap acceptable, or is uncapped liability non-negotiable given regulatory exposure (PCI DSS, state breach laws, CCPA)? |
| 3 | Term and renewal (Issue 5) | Is a 60-month initial term with 60-month auto-renewals acceptable? Would the business team prefer a 36-month initial term with 12-month renewals? |
| 4 | Transition planning (Issue 8) | How long would it realistically take to transition all fulfillment (DTC + wholesale + retail) to a new provider? This determines whether 90 or 180 days is sufficient. |

---

*Prepared for internal discussion. Not a legal opinion.*