# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**RE:** Seinon Outdoor Gear, Inc. – Poseirt Commerce Logistics, LLC: Pre-Signing Issue Identification
**DATE:** [Current Date]

---

## Summary

I have reviewed the Poseirt Master Services Agreement ("MSA"), Order Form No. 1 ("Order Form"), and Service Level Schedule ("SLA"). I also reviewed the Kelvane Textile Labs fabric testing agreement; as noted in Issue 12 below, it does not materially bear on the Poseirt deal. I identify eleven issues requiring negotiation before signing, three of which I recommend be escalated to the client for business judgment before we respond to Poseirt.

---

## Issues Requiring Client Escalation Before We Respond to Poseirt

These three items involve business decisions that go beyond legal drafting and should be confirmed with Seinon's commercial team before we table redlines.

---

### Issue 1: Exclusivity Scope – Order Form Dramatically Expands Beyond MSA

**Where:** MSA § 2.4; Order Form § 4.

**The problem.** MSA § 2.4 limits exclusivity to "direct-to-consumer e-commerce fulfillment of Seinon products shipped to the United States and Canada" and expressly states that nothing restricts Customer from "selling, distributing or fulfilling Products through any other channel or in any other territory." Order Form § 4, however, requires Seinon to use Poseirt as "its exclusive provider of all fulfillment, warehousing and logistics services for all Seinon products in all sales channels worldwide, including direct-to-consumer e-commerce, wholesale distribution and retail-store replenishment," and extends the restriction to Affiliates.

Under MSA § 1.3 (Order of Precedence), the Order Form controls over the MSA in the event of conflict. As drafted, the Order Form sweeps in wholesale distribution, retail-store replenishment, and all territories for the full 60-month Initial Term (Order Form § 2).

**Why it matters.** Seinon would be contractually locked into a single Reno, Nevada facility for *all* fulfillment—DTC, wholesale, retail replenishment—worldwide for five years. Any disruption at the Facility (natural disaster, labor issue, Provider insolvency) would leave Seinon unable to use an alternative 3PL without breaching the contract. This is an existential operational risk for a company whose revenue depends on shipping product to customers.

**Recommended fix.** Conform Order Form § 4 to the MSA § 2.4 scope, or at minimum limit exclusivity to DTC e-commerce fulfillment in North America. If the client's business intent is broader exclusivity, that is a commercial decision the client must make knowingly. Proposed language if we narrow it:

> "During the term of this Order Form, Customer will use Provider as its exclusive provider of direct-to-consumer e-commerce fulfillment of Seinon products shipped to the United States and Canada. Nothing in this Order Form restricts Customer from selling, distributing or fulfilling Products through any other channel or in any other territory, or from engaging any third party to do so."

**Client question:** Does Seinon's business plan actually require single-sourcing *all* fulfillment (wholesale, retail replenishment, international) through Poseirt for five years? If not, we should strike Order Form § 4 and rely on MSA § 2.4.

---

### Issue 2: Security Incident Liability – SLA Overrides MSA Cap Carve-Out

**Where:** MSA § 11.3(b); SLA § 6.3 (second sentence); MSA § 1.3.

**The problem.** MSA § 11.3(b) expressly carves Security Incidents out of both the consequential-damages exclusion (§ 11.1) and the liability cap (§ 11.2). This means that, under the MSA alone, Provider's liability for a Security Incident is uncapped.

SLA § 6.3 then states: "Notwithstanding Section 11.3 of the MSA, Provider's aggregate liability arising out of or relating to Security Incidents shall not exceed the cap set out in Section 11.2 of the MSA."

Because the SLA ranks above the MSA in the order of precedence (MSA § 1.3), the SLA's language controls. The net effect is that Provider's liability for a Security Incident is capped at 12 months of fees—approximately $582,000 in Monthly Platform Fees alone (Order Form § 3.1), plus whatever fulfillment fees were paid in the trailing 12 months.

**Why it matters.** "Shopper Data" (MSA § 1.1(m)) includes names, addresses, emails, phone numbers, order histories, and payment-related data. A breach of that data could trigger: state and federal AG enforcement actions, class-action litigation, PCI fines, credit-monitoring costs for potentially hundreds of thousands of consumers, and reputational damage. The MSA already obligates Provider to reimburse notification, credit-monitoring, and call-center costs (MSA § 8.3(c)), but those reimbursements would be subject to the cap as the SLA reads them. A single significant breach could easily exceed $5–10 million in costs. The $10 million cyber insurance requirement (MSA § 12) is for Provider's own protection; it does not make the insurer directly accessible to Seinon.

**Recommended fix.** Delete the second sentence of SLA § 6.3 in its entirety. Restore the MSA § 11.3(b) carve-out so Security Incidents remain uncapped. Alternatively, if the client accepts a cap for Security Incidents, negotiate a super-cap (e.g., 3× the general cap or a fixed dollar amount tied to the cyber insurance limit). Proposed language:

> "Service Credits and Customer's termination right under Section 6.2 are Customer's sole and exclusive remedies for any Service Failure *other than a Security Incident*. In the case of a Security Incident, Customer's remedies are as set out in Section 8.3 and Section 11.3(b) of the MSA."

**Client question:** Is the client prepared to accept a ~$600K–$1M cap on Provider's liability for a data breach of its customers' payment and personal information? If not, we must strike the SLA override.

---

### Issue 3: Governing Law and Venue Conflict

**Where:** MSA §§ 14.1–14.2; Order Form § 8.

**The problem.** MSA § 14.1 selects Delaware law; MSA § 14.2 selects exclusive jurisdiction in Wilmington, Delaware. Order Form § 8 selects New York law and exclusive jurisdiction in New York County. Under MSA § 1.3, the Order Form controls, so New York law and venue would govern.

**Why it matters.** This appears to be a drafting error (Poseirt likely used a New York template for the Order Form without conforming it to the MSA). If left uncorrected, every dispute—including a Chronic Failure termination or a Security Incident claim—would be litigated in New York under New York law, which may not be the jurisdiction the parties intended. Delaware law is generally well-developed for commercial contracts and is the law of both parties' states of incorporation/formation (Seinon is a Delaware corporation; Poseirt is a Nevada LLC, but the MSA selects Delaware). New York venue also imposes significant travel and cost burdens on both parties relative to their home jurisdictions.

**Recommended fix.** Delete Order Form § 8 in its entirety and add: "Governing law and venue are as set out in Section 14 of the Agreement." Alternatively, conform Order Form § 8 to Delaware law and Wilmington venue.

**Client question:** Confirm that Delaware law and venue are acceptable to the client. (They should be, given the MSA already selects them.)

---

## Additional Issues for Negotiation

### Issue 4: Customer Indemnification – "Regardless of Provider Handling"

**Where:** MSA § 10.2.

**The problem.** MSA § 10.2 requires Seinon to indemnify Poseirt against third-party claims "arising out of or relating to the Products or the Customer Materials, *regardless of whether caused in part by Provider handling, storage or shipment of the Products*." The italicized phrase means that if Poseirt drops a box of technical jackets in the warehouse, a consumer receives a damaged product that causes injury, and the consumer sues both Seinon and Poseirt, Seinon must still indemnify Poseirt for its share—even though Poseirt's own negligence contributed to the harm.

**Why it matters.** This effectively shifts Provider's own operational negligence back onto Customer. It undermines the risk-of-loss allocation in MSA § 6.2 (where Provider bears risk of loss and reimburses at landed cost) and the insurance structure in MSA § 12 (where Provider carries warehouse legal liability insurance "full replacement value").

**Recommended fix.** Delete the phrase "regardless of whether caused in part by Provider handling, storage or shipment of the Products." Add: "Customer's indemnification obligation under this Section 10.2 does not extend to claims to the extent caused by Provider's negligence, willful misconduct, or breach of this Agreement."

---

### Issue 5: Auto-Renewal Notice Window Is Only Ten Days Wide

**Where:** MSA § 9.2.

**The problem.** Non-renewal notice must be delivered "no earlier than 100 days and no later than 90 days before the expiration of the then-current term." This creates a 10-day window. If Seinon's notice goes out on day 101 or day 89, it is ineffective, and the Order Form auto-renews for another 60 months.

**Why it matters.** Given the 60-month Initial Term and the broad exclusivity (see Issue 1), an inadvertent missed renewal would lock Seinon in for another five years. The window is unreasonably narrow for a contract of this size and duration.

**Recommended fix.** Widen the window and add a reminder mechanism. Proposed language:

> "An Order Form will not renew if either party delivers written notice of non-renewal to the other party no earlier than 180 days and no later than 60 days before the expiration of the then-current term. Provider will send a written reminder to Customer 200 days before each renewal date."

---

### Issue 6: Fee Adjustment – Monthly Platform Fee Not Addressed After Month 24

**Where:** Order Form § 3.5; MSA § 1.1(e).

**The problem.** Order Form § 3.5 states: "Fees are fixed for the first twenty-four (24) months of the Initial Term. After that, Provider may increase the fulfillment fees in Section 3.2 once in any twelve (12) month period, on at least sixty (60) days' prior written notice. No increase may exceed three percent (3%) over the fees then in effect."

"Fees" is defined in MSA § 1.1(e) as "the fees set out in an Order Form"—which includes the Monthly Platform Fee (§ 3.1). So all fees are fixed for 24 months. But after month 24, the adjustment right is limited to "fulfillment fees in Section 3.2." The Monthly Platform Fee ($48,500/month) is in Section 3.1 and is not covered by the adjustment mechanism. This creates ambiguity: can Provider increase the Monthly Platform Fee after month 24? The silent answer is probably yes (no restriction stated), but it could also be read as frozen for the full term.

**Why it matters.** The Monthly Platform Fee is the largest single line item ($582,000/year). If it is subject to uncapped increases after month 24, Seinon's cost base could drift significantly over the 60-month term.

**Recommended fix.** Clarify the treatment of the Monthly Platform Fee. If the client wants it fixed for the full term:

> "The Monthly Platform Fee is fixed for the entire Initial Term and each Renewal Term. After the first twenty-four (24) months of the Initial Term, Provider may increase the fulfillment fees in Section 3.2 once in any twelve (12) month period, on at least sixty (60) days' prior written notice. No increase may exceed three percent (3%) over the fees then in effect."

If the client accepts increases to the platform fee, add the same 3% cap and 60-day notice to Section 3.1 fees.

---

### Issue 7: Transition Assistance – Time-Limited and At Provider's Rates

**Where:** MSA § 9.5.

**The problem.** Transition assistance is limited to "up to ninety (90) days" and is provided "at the rates in effect under that Order Form." There is no obligation on Provider to cooperate beyond 90 days, no service-level commitment for the transition, and no penalty for Provider's failure to complete the transition within that window.

**Why it matters.** Migrating a DTC storefront, inventory, and ERP integrations from a single facility can easily take more than 90 days, particularly if the exclusivity scope (Issue 1) means moving wholesale and retail replenishment as well. If Provider drags its feet, Seinon has no contractual lever to compel faster transition.

**Recommended fix.** Add: (a) a requirement that Provider use commercially reasonable efforts to complete transition within 60 days; (b) a daily liquidated damage or fee-credit for each day transition extends beyond 90 days due to Provider's failure to perform; and (c) an obligation to provide daily (not monthly) inventory reports during the transition period. Proposed language:

> "Provider will use commercially reasonable efforts to complete all transition assistance within sixty (60) days. If transition is not complete within ninety (90) days due to Provider's failure to perform, Provider will credit Customer $[X] per day for each additional day until completion is achieved."

---

### Issue 8: Service Credit Exceptions – Customer ERP Failures

**Where:** SLA § 5.4(d).

**The problem.** A Service Level failure does not generate a credit if caused by "failures of Customer's enterprise resource planning system or other Customer-controlled systems." Order Form § 5.1(c) requires integration of the Platform with Seinon's ERP "through Provider's standard API." If the API is Provider's component but the failure is attributed to the ERP side, Provider could argue the exception applies.

**Why it matters.** This exception could be invoked frequently in the early months while integrations are being stabilized. It effectively makes Seinon bear the cost of any interface problem that Provider can attribute to the ERP side, even if the root cause is a defect in Provider's API.

**Recommended fix.** Narrow the exception to failures that are solely and directly caused by Customer's systems, and add a burden-of-proof requirement:

> "(d) failures of Customer's enterprise resource planning system or other Customer-controlled systems, *solely and directly causing the Service Level failure, as demonstrated by Provider through diagnostic data made available to Customer*."

---

### Issue 9: Assignment Without Consent on Change of Control

**Where:** MSA § 15.2.

**The problem.** Either party may assign the Agreement without consent to "a successor to all or substantially all of its business or assets." If Poseirt is acquired by a competitor of Seinon or by a company with inferior operational capabilities, the acquirer steps into the contract automatically.

**Why it matters.** Combined with the 60-month term and broad exclusivity (Issue 1), an involuntary change of control at Poseirt could hand Seinon's entire fulfillment operation to an unknown or adverse party.

**Recommended fix.** Add a termination right for Customer upon Provider's change of control:

> "Notwithstanding the foregoing, if Provider undergoes a change of control (including a merger, acquisition, or sale of substantially all assets), Customer may terminate any and all Order Forms on written notice delivered within ninety (90) days after the change of control, without payment of any termination fee. Section 9.5 (Transition Assistance) applies to any such termination."

---

### Issue 10: Go-Live Target Is Non-Binding

**Where:** Order Form § 6.2.

**The problem.** The parties "target" go-live within 90 days. The word "target" is aspirational, not obligatory. There is no consequence—no service credit, no termination right, no fee abatement—if Provider misses the 90-day mark.

**Why it matters.** Seinon is presumably migrating off an existing storefront. Every week of delay means either (a) running two systems in parallel (cost) or (b) operating without the new Platform (lost sales, degraded customer experience). If Provider's implementation is slow, Seinon has no remedy.

**Recommended fix.** Convert to a binding obligation with a remedy:

> "Provider will achieve Storefront go-live and commencement of fulfillment at the Facility no later than ninety (90) days after the Order Form Effective Date (the 'Go-Live Date'). If Provider fails to achieve go-live by the Go-Live Date, the Monthly Platform Fee will be abated by fifty percent (50%) for each week (or portion thereof) of delay, and Customer may terminate this Order Form without penalty if go-live is not achieved within one hundred twenty (120) days after the Order Form Effective Date."

---

### Issue 11: Independent Verification Limited to Once Per Contract Year

**Where:** SLA § 4.4.

**The problem.** Customer may have Provider's service-level measurements verified by an independent third party "no more than once per contract year." Over a 60-month term, that is five verifications total.

**Why it matters.** If Provider systematically under-reports service failures (e.g., misclassifying outages as "Scheduled Maintenance" or attributing failures to Customer's ERP under SLA § 5.4), Seinon would not be able to independently confirm for up to 12 months at a time.

**Recommended fix.** Increase to once per quarter, or allow verification whenever Customer has a good-faith basis to believe measurements are inaccurate:

> "Customer may have Provider's measurements verified by an independent third party no more than once per calendar quarter, or at any time if Customer has a good-faith, reasonable basis to believe that Provider has understated a Service Failure. If verification shows that Provider understated a Service Failure, Provider will bear the reasonable cost of verification."

---

## Note on the Kelvane Fabric Testing Agreement

### Issue 12: Kelvane Agreement – No Material Bearing on the Poseirt Deal

**Where:** seinon_kelvane_fabric_testing_agreement.md (entire document).

The Kelvane agreement governs independent fabric and garment testing (waterproofing, abrasion, breathability). It is a separate vendor relationship with no overlap in scope, parties, or subject matter with the Poseirt engagement. I do not identify any provision in the Kelvane agreement that creates a conflict, gap, or additional exposure in the Poseirt deal.

One structural observation for the client's awareness: the Kelvane agreement uses a more favorable auto-renewal structure (2-year initial term, 1-year renewals, 60-day non-renewal notice window that is 60 days wide). The Poseirt MSA's 10-day-wide renewal window (Issue 5) is markedly less forgiving by comparison. If the client is comfortable with the Kelvane renewal structure, that is a useful benchmark to cite when pushing back on MSA § 9.2.

---

## Recommended Next Steps

1. **Escalate Issues 1–3 to the client** for business decisions before we table redlines with Poseirt.
2. Prepare a redline of the Order Form and SLA addressing Issues 4–11.
3. Request that Poseirt confirm in writing whether the governing-law conflict (Issue 3) was intentional or a template error.
4. If the client accepts any form of Security Incident cap (Issue 2), require that the cap be no less than the Provider's cyber insurance limit ($10M per MSA § 12) and that Seinon be named as an additional insured or loss payee on that policy.