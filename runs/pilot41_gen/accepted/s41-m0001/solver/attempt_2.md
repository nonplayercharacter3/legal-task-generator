# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Lalais Medical Systems / Trasirt Holdings — Transaction Document Risk Assessment

---

## Summary

I have reviewed the Stock Purchase Agreement (SPA), the Bill of Sale for service tooling, the Transition Services Agreement (TSA), and the prior draft of the Bill of Sale (dated February 24, 2026). I identify twenty-three issues below, ordered by risk to Lalais. The most critical problems are: (1) the absence of the Kestrevo detector supply consent from the SPA's closing conditions; (2) survival periods for product liability and FDA representations that are far too short for a medical device company; (3) the TSA's one-sided assignment right, which lets Trasirt delegate all services—including ERP hosting and remote diagnostics—to any third party without Lalais's consent; and (4) the absence of a defined "net working capital" formula, which will produce a post-closing dispute.

---

## ISSUE 1 — Kestrevo Change-of-Control Consent Missing from Closing Conditions

**Document / Section:** SPA, Schedule 4.6(a)(iii) (disclosing the Kestrevo consent requirement) vs. Schedule 7.2(d) (listing required third-party consents) and Section 7.2(d) (condition to Buyer's closing obligation).

**Explanation:** Schedule 4.6(a)(iii) discloses that Section 14.2 of the Detector Supply Agreement with Kestrevo Sensors GmbH requires Kestrevo's prior written consent to a change of control of the Company, "failing which Kestrevo may terminate the Detector Supply Agreement on written notice." Kestrevo is the **sole source** of flat-panel detectors for the Company's mobile C-arm product line. However, Schedule 7.2(d) lists only one required consent: that of Westbridge Industrial Partners LLC under the Facility Lease. Kestrevo's consent is absent.

Because Section 7.2(d) makes only the consents "listed on Schedule 7.2(d)" a condition to Buyer's closing obligation, and Section 6.4 covenants Seller to obtain only those same listed consents, **Lalais has no contractual right to refuse to close if Kestrevo has not consented, and no covenant requiring Seller to obtain Kestrevo's consent before Closing.** If Kestrevo terminates after Closing, Lalais loses its sole detector supply for the C-arm line with no indemnification trigger (the SPA representation in Section 4.5(c) is already carved out by the Schedule 4.6 disclosure, so its inaccuracy would not give rise to a claim under Section 9.2(a)).

**Recommendation:**
- Add Kestrevo's consent to Schedule 7.2(d) so it becomes a condition to Buyer's closing obligation under Section 7.2(d).
- Add a specific covenant in Section 6.4 (or a new Section 6.4A) requiring Seller to use its best efforts (not merely "commercially reasonable efforts") to obtain Kestrevo's consent before Closing, with a requirement that the consent be in form and substance reasonably satisfactory to Buyer.
- If Kestrevo's consent cannot be obtained as a condition to Closing, negotiate a specific indemnity from Seller for Losses arising from termination of the Detector Supply Agreement, outside the general indemnification cap and deductible.

**Proposed language for Schedule 7.2(d), new item 2:**

> 2. Consent of Kestrevo Sensors GmbH, as supplier under the Detector Supply Agreement dated September 15, 2022, to the change of control of the Company resulting from the transactions contemplated by this Agreement, in form and substance reasonably satisfactory to Buyer.

---

## ISSUE 2 — Product Liability and FDA Representations Survive Only Until the Escrow Release Date (90 Days)

**Document / Section:** SPA, Section 9.1(b) (survival of Sections 4.12 and 4.14 until the Escrow Release Date); Section 2.4(b) (Escrow Release Date is 90 days after Closing).

**Explanation:** Section 9.1(b) provides that the product liability/recall representations (Section 4.12) and the FDA/regulatory compliance representations (Section 4.14) survive only until the Escrow Release Date—90 days after Closing. For a medical device company whose products have been on the market since at least 2019 (510(k) K193318), this is grossly inadequate:

- **Product liability:** Claims from patient injury can arise years after a device is implanted or used. New York's statute of limitations for medical malignment/product liability is three years from discovery (or up to two years from the date of the act/omission under CPLR § 214-c for latent injury). A 90-day survival window means that if a patient is injured by an OV-9 C-arm in month four post-Closing and files suit in month six, Lalais has no indemnification recourse against Seller.
- **FDA regulatory:** The FDA can issue a Form 483, warning letter, or initiate an enforcement action well after 90 days based on pre-Closing quality system deficiencies. Section 4.14(c) represents that no such notice has been received, but if the FDA issues one in month four, the representation has already expired.
- Neither Section 4.12 nor Section 4.14 is a "Fundamental Representation" (defined in Section 1.1 as Sections 4.1, 4.2, 4.3, 4.13, and 4.17), so the longer survival in Section 9.1(c) does not apply.

**Recommendation:**
- Extend survival of Section 4.12 (Product Liability; Recalls) to the full statute of limitations for the underlying claim, plus 60 days (mirroring the Fundamental Representation survival in Section 9.1(c)).
- Extend survival of Section 4.14 (FDA and Regulatory Compliance) to at least 24 months after Closing, or to the expiration of the applicable statute of limitations, whichever is later.
- If Seller resists, at minimum extend both to 18 months (the general survival period in Section 9.1(a)) and increase the escrow holdback period for claims under those sections.

**Proposed language for Section 9.1(b):**

> (b) The representations and warranties in Section 4.12 (Product Liability; Recalls) shall survive the Closing until the expiration of the applicable statute of limitations for the underlying claim, plus sixty (60) days. The representations and warranties in Section 4.14 (FDA and Regulatory Compliance) shall survive the Closing until twenty-four (24) months after the Closing Date.

---

## ISSUE 3 — TSA Allows Provider to Assign or Delegate to Any Person Without Recipient Consent

**Document / Section:** TSA, Section 13.2 (Assignment).

**Explanation:** Section 13.2 provides: "Provider may assign this Agreement, or delegate the performance of any Services, in whole or in part, to any Person without the consent of Recipient." This is profoundly one-sided. The entire purpose of the TSA is continuity: Lalais is paying $410,000 per month for 12 months to have the same people and systems that ran the Business before Closing continue to do so during the transition. Under this provision, Trasirt could:

- Hand the ERP hosting to a third-party cloud provider (potentially one with weaker security);
- Delegate field service dispatch to a staffing agency or a competitor;
- Assign the entire TSA to an Affiliate that is less creditworthy or less capable.

Section 9.3 of the TSA expressly permits Provider to disclose Recipient Confidential Information (which includes service firmware, diagnostic software, Customer site data, and complaint records) to "permitted assignees and delegates under Section 13.2." Combined, these provisions mean Lalais's most sensitive operational data could end up in the hands of an unknown third party with no consent right.

The contrast with the SPA is notable: Section 11.6 of the SPA restricts assignment by either party without the other's consent (with limited exceptions for Buyer's Affiliates and lenders).

**Recommendation:**
- Require Recipient's prior written consent (not to be unreasonably withheld) for any assignment or delegation by Provider.
- If delegation is permitted (e.g., to a subcontractor for specific tasks), require that the delegatee be bound by confidentiality and data security obligations no less protective than the TSA, and that Provider remains liable for the delegatee's performance.

**Proposed language for Section 13.2 (revised):**

> **13.2 Assignment.** Recipient may not assign its rights or delegate its obligations under this Agreement without Provider's prior written consent, except that Recipient may assign this Agreement to the Company or to any other Affiliate of Recipient. Provider may not assign this Agreement or delegate the performance of any Services without Recipient's prior written consent, not to be unreasonably withheld. Notwithstanding the foregoing, Provider may delegate discrete, non-core tasks (such as courier delivery of parts) to subcontractors, provided that (a) the subcontractor is bound by written confidentiality and data security obligations no less protective than Sections 8.3 and 9 of this Agreement, and (b) Provider remains fully responsible for the subcontractor's performance. Any purported assignment in violation of this Section 13.2 is void.

---

## ISSUE 4 — No Definition of "Net Working Capital" in the SPA

**Document / Section:** SPA, Section 2.3 (Working Capital Adjustment); Article 1 (Definitions) — no definition of "net working capital" or "closing working capital."

**Explanation:** Section 2.3 adjusts the $186.5 million Purchase Price dollar-for-dollar based on the Company's "net working capital" as of Closing, against a Target of $14,200,000. However, the SPA never defines what components are included in or excluded from "net working capital." Common points of dispute include:

- Whether cash and cash equivalents are included (if yes, the target effectively includes a cash balance; if no, the working capital target is higher in practice);
- Whether short-term debt (e.g., current portion of long-term notes, credit facility borrowings) is deducted;
- How to treat prepaids, deferred revenue, and accrued expenses;
- Whether the working capital calculation includes intercompany balances (relevant if the Company has any related-party transactions with Seller or its Affiliates);
- Whether inventory is valued at cost or net realizable value.

Without a definition, the 90-day post-closing true-up under Section 2.3(b) is likely to generate a dispute, and the independent accounting firm mechanism in Section 2.3(b) will be invoked—costing time and money and creating uncertainty about the final Purchase Price.

**Recommendation:**
- Add a definition of "Net Working Capital" in Section 1.1, specifying included and excluded components.
- Alternatively, attach a schedule with a worked example of the calculation.

**Proposed language for Section 1.1 (new definition):**

> "**Net Working Capital**" means, as of any date of determination, the excess of (a) current assets (excluding cash and cash equivalents, deferred tax assets, and any receivable from Seller or its Affiliates) over (b) current liabilities (excluding current portion of long-term debt, deferred tax liabilities, and any payable to Seller or its Affiliates). Inventory shall be included at the lower of cost or net realizable value. Accrued expenses and deferred revenue shall be included in current liabilities and current assets, respectively.

---

## ISSUE 5 — Bill of Sale Asset Register Not a Closing Deliverable; Scope of Transferred Assets Uncertain

**Document / Section:** Bill of Sale, Schedule A, Part 1, items 5 and 6 (referencing "the asset register delivered by Seller to Buyer before the Closing"); SPA, Section 3.2 (Seller Closing Deliverables) — no reference to an asset register.

**Explanation:** Items 5 and 6 of Schedule A to the Bill of Sale define the service laptops and CT/MRI tooling by reference to "the asset register delivered by Seller to Buyer before the Closing." This asset register:

- Is not attached to the Bill of Sale or the SPA;
- Is not listed as a closing deliverable in SPA Section 3.2;
- Is not a condition to Closing under Article 7;
- Was flagged in the prior draft (February 24, 2026) with the note "Quantities to be confirmed against Seller asset register," indicating the parties had not yet agreed on the definitive list.

If Seller fails to deliver the asset register before Closing, or delivers an incomplete one, the scope of items 5 and 6 is undefined. Lalais could close, pay $186.5 million, and later discover that tooling it believed was included was not on the register. Because the Bill of Sale contains no representations or warranties (see Issue 6 below), and SPA Section 4.8 (Title to Assets; Sufficiency) covers the Company's assets rather than Seller-held assets being transferred, the remedy path is unclear.

**Recommendation:**
- Add the asset register as a specific closing deliverable in SPA Section 3.2 (new item, e.g., 3.2(j)): "a complete and accurate asset register identifying all Transferred Assets described in Schedule A, Part 1, items 5 and 6 of the Bill of Sale."
- Make delivery of the asset register a condition to Closing under Section 7.2 (new item).
- Require that the asset register be delivered at least 10 Business Days before Closing to allow Buyer to verify contents.

---

## ISSUE 6 — Bill of Sale Contains No Representations or Warranties Backed by Indemnification

**Document / Section:** Bill of Sale, Section 6 (Relationship to the Stock Purchase Agreement); SPA, Section 9.2 (Indemnification by Seller).

**Explanation:** Bill of Sale Section 6 states: "The representations, warranties, covenants and indemnities of Seller in the Stock Purchase Agreement are not enlarged or diminished by this Bill of Sale." The Bill of Sale itself contains no representations or warranties from Seller regarding the condition, completeness, or title to the Transferred Assets. Section 1.1 covenants that the transfer is "free and clear of all Encumbrances," but a covenant in a side document is not a "representation or warranty of Seller in this [Stock Purchase] Agreement" and may not trigger indemnification under SPA Section 9.2(a).

SPA Section 9.2(b) covers "any breach of any covenant or obligation of Seller in this Agreement"—but "this Agreement" is the SPA, not the Bill of Sale. While the Bill of Sale is a "Transaction Document" (SPA Section 1.1), the indemnification clause is tied to covenants "in this Agreement."

If the tooling is defective, incomplete, or encumbered, Lalais may find that it has no clear indemnification path: the Bill of Sale disclaims additional reps, the SPA indemnity may not reach the Bill of Sale's covenants, and the general sufficiency representation in SPA Section 4.8 is subject to the deductible and cap.

**Recommendation:**
- Add representations and warranties to the Bill of Sale (or, preferably, to the SPA) covering: (a) Seller's good and marketable title to the Transferred Assets, free and clear of all Encumbrances; (b) the Transferred Assets are in good working order and condition, fit for their intended purpose; (c) Schedule A is complete and accurate; and (d) the transfer does not violate any agreement to which Seller is a party.
- Clarify in SPA Section 9.2 that a breach of any covenant in a Transaction Document (including the Bill of Sale) is indemnifiable.

**Proposed language for SPA Section 9.2 (add at end):**

> For purposes of this Section 9.2, "covenant or obligation of Seller in this Agreement" includes any covenant or obligation of Seller in any other Transaction Document.

---

## ISSUE 7 — TSA Force Majeure Covers Internet and Utility Failure (Core Service Risk)

**Document / Section:** TSA, Section 13.4 (Force Majeure).

**Explanation:** Section 13.4 excuses Provider from liability for delays caused by "widespread utility or internet failure." The Services under Schedule A include ERP hosting (Part 3), remote service platform operation (Part 1), and field service dispatch (Part 2)—all of which depend on network connectivity. A "widespread" internet or utility outage at Provider's data center or dispatch hub would suspend Provider's obligations with no liability and no required timeline for resumption (only "commercially reasonable efforts").

For a medical device company, loss of ERP access means inability to process orders, manage inventory, or bill service contracts. Loss of the remote service platform means inability to monitor installed devices or respond to field issues. Loss of dispatch means field service engineers cannot be sent to Customer sites.

The term "widespread" is undefined and could be interpreted broadly by Provider.

**Recommendation:**
- Narrow the force majeure carve-out to exclude failures that are within Provider's reasonable control (e.g., failure of Provider's own network infrastructure, data center power, or internet connectivity at Provider's facilities).
- Require Provider to maintain redundant connectivity and backup power at its data center, and to have a disaster recovery plan with a maximum recovery time objective (e.g., 4 hours for ERP, 8 hours for remote service).
- Add a provision that if a force majeure event continues for more than 5 consecutive Business Days, Recipient may terminate the affected Service without penalty and receive a pro-rata refund of fees paid for that Service.

**Proposed language (new Section 13.4A):**

> **13.4A Disaster Recovery; Extended Force Majeure.** Provider shall maintain redundant internet connectivity, backup power, and a documented disaster recovery plan for the Provider Systems. If a force majeure event under Section 13.4 prevents Provider from performing any Service for more than five (5) consecutive Business Days, Recipient may terminate that Service by written notice, and Provider shall refund any pre-paid fees attributable to the terminated Service for the period after the force majeure event began.

---

## ISSUE 8 — TSA Term Is Fixed at 12 Months with No Extension Mechanism

**Document / Section:** TSA, Section 2.1 (Term); SPA, Section 1.1 (definition of "Transition Services Agreement" references "a term of 12 months after the Closing Date").

**Explanation:** The TSA expires 12 months after Closing with no provision for extension. Section 7.3 requires Recipient to use "commercially reasonable efforts to transition each Service to its own systems or a third-party provider before the end of the Term." Standing up an ERP system, a remote service platform, and a field dispatch operation for a medical device company with an installed base of CT and MRI equipment is a significant undertaking that may not be completable in 12 months, particularly if Lalais needs to select and implement new vendors.

If the Term expires before transition is complete, Lalais would need to negotiate a new agreement with Trasirt (or a successor), at which point Trasirt would have significant leverage. There is no right of first refusal, no most-favored-nations pricing, and no obligation on Trasirt to extend.

**Recommendation:**
- Add an extension provision: if either party gives written notice at least 60 days before the end of the Term that transition of one or more Services is not complete, the Term for those Services shall be extended for up to six additional months, with the Monthly Service Fee continuing to apply.
- Alternatively, add a "tail" provision requiring Provider to continue Services on the same terms for up to 90 days after the end of the Term if Recipient is in the process of transitioning, at the same Monthly Service Fee.

**Proposed language (new Section 2.3):**

> **2.3 Extension.** If, at least sixty (60) days before the scheduled expiration of the Term, either party notifies the other in writing that one or more Services have not been fully transitioned, the Term for those Services shall be extended for a period of up to six (6) additional months. During any extension, the Monthly Service Fee and all other terms of this Agreement shall continue to apply. Provider shall not unreasonably withhold cooperation necessary to complete the transition during the extension period.

---

## ISSUE 9 — Non-Compete Does Not Cover CT/MRI Service Business

**Document / Section:** SPA, Section 6.8 (Non-Competition; Non-Solicitation).

**Explanation:** Section 6.8 prohibits Seller from engaging in "the design, manufacture, sale or servicing of mobile C-arm or digital radiography systems anywhere in the United States" for three years post-Closing. The Company's Business, however, includes "providing service for an installed base of computed tomography and magnetic resonance imaging equipment" (Recital B). The non-compete does not restrict Seller from entering the CT or MRI service business.

The carve-out for "performance of the Transition Services Agreement" means Seller can provide CT/MRI service during the 12-month TSA term. After the TSA expires, Seller is free to compete in CT/MRI service—potentially using the service manuals, calibration phantoms, and customer relationships it accessed during the TSA (subject to the TSA's confidentiality provisions, which survive for five years or indefinitely for trade secrets).

**Recommendation:**
- Expand the non-compete to cover "the servicing of computed tomography or magnetic resonance imaging equipment" in the geographic areas where the Company's installed base is located, for the same three-year period.
- At minimum, add a non-solicitation of Customers (not just employees) for CT/MRI service contracts for three years.

**Proposed language for Section 6.8(a) (revised):**

> (a) engage in the design, manufacture, sale or servicing of mobile C-arm or digital radiography systems anywhere in the United States, or the servicing of computed tomography or magnetic resonance imaging equipment in any state in which the Company's installed base includes equipment as of the Closing Date, other than through the performance of the Transition Services Agreement;

---

## ISSUE 10 — Bill of Sale Permits Seller to Retain Electronic Service Manuals Indefinitely

**Document / Section:** Bill of Sale, Section 3.2 (Electronic Materials); compare prior draft Section 3.2.

**Explanation:** The current Bill of Sale Section 3.2 requires Seller to deliver complete copies of electronic service manuals to the Company but then permits Seller to "retain only such copies as Seller needs to perform the Transition Services Agreement or to comply with applicable Law." There is no requirement that Seller delete or return retained copies after the TSA term ends, no restriction on use beyond TSA performance, and no audit right for the Company.

The prior draft (February 24, 2026) contained no such retention right—it simply required delivery. The addition of the retention right appears to have been negotiated to support the TSA, but the "or to comply with applicable Law" language is open-ended and could be used to justify indefinite retention.

Service manuals contain proprietary technical information (calibration procedures, fault codes, component specifications) that is competitively sensitive. While the TSA's confidentiality provisions (Section 9) protect Recipient Confidential Information, the Bill of Sale is a separate document and does not incorporate the TSA's confidentiality obligations.

**Recommendation:**
- Limit the retention right to the duration of the TSA Term plus 30 days.
- Require Seller to certify in writing that it has deleted all retained copies (except those required by Law, identified specifically) within 30 days after the TSA Term ends.
- Incorporate the TSA's confidentiality and data security obligations into the Bill of Sale for any retained electronic materials.

**Proposed language for Bill of Sale Section 3.2 (revised):**

> **3.2 Electronic Materials.** For service manuals and related documentation held in electronic form, Seller shall do the following on the Effective Date:
>
> (a) deliver complete copies to the Company in their native format; and
>
> (b) after delivery, retain only such copies as Seller reasonably needs to perform the Transition Services Agreement, provided that Seller shall delete all such retained copies within thirty (30) days after the later of (i) the expiration or termination of the Transition Services Agreement and (ii) the date on which Seller no longer needs the copies to comply with a specific, identified Legal requirement. Seller shall certify deletion in writing to the Company within ten (10) Business Days after completing it.
>
> Seller's use of any retained copies shall be subject to the confidentiality and data security obligations of the Transition Services Agreement.

---

## ISSUE 11 — TSA Contains No Service Level Agreement or Uptime Commitments

**Document / Section:** TSA, Section 3.2 (Standard of Performance); Schedule A (Services).

**Explanation:** The only performance standard is Section 3.2(b): "substantially the same scope, priority, quality, timeliness and level of care as the corresponding services were provided to the Business during the 12 months before the Closing Date." This is a backward-looking, subjective standard with no objective metrics. There are no:

- Uptime percentages for the ERP or remote service platform;
- Maximum response times for the technical support hotline;
- Service ticket resolution targets;
- Dispatch turnaround times for field service;
- Consequences (service credits, fee reductions) for failure to meet standards.

The only remedy for underperformance is termination for material breach (Section 12.1), which is a high bar and impractical for a company that depends on these services daily.

**Recommendation:**
- Add an SLA schedule (Schedule B) specifying: (a) minimum uptime for ERP and remote service platform (e.g., 99.5% measured monthly); (b) hotline response times (e.g., first response within 30 minutes during business hours); (c) field dispatch turnaround (e.g., engineer on-site within 4 business days for standard requests, 24 hours for urgent); and (d) service credits (e.g., 5% of Monthly Service Fee for each full percentage point below 99.5% uptime).
- Clarify that chronic SLA failures (e.g., three consecutive months below target) constitute a material breach entitling Recipient to terminate.

---

## ISSUE 12 — TSA Does Not Require Provider to Maintain Insurance

**Document / Section:** TSA — no insurance provision.

**Explanation:** The TSA imposes no obligation on Provider to maintain any form of insurance, including:

- Commercial general liability (for damage to Customer property or bodily injury at Customer sites during field service);
- Professional liability / errors and omissions (for faulty diagnostics or service);
- Cyber liability (for data breaches of Recipient Data);
- Workers' compensation (for Provider's field service personnel).

While Section 11.1 provides indemnification for third-party claims caused by Provider's gross negligence, willful misconduct, breach of data security, or violation of Applicable Law, indemnification is only as good as Provider's balance sheet. If Provider is undercapitalized or becomes insolvent (see Section 12.2, which allows termination for insolvency), Lalais's recovery may be limited.

**Recommendation:**
- Add a requirement that Provider maintain, at its own cost: (a) commercial general liability of not less than $5,000,000 per occurrence; (b) professional liability of not less than $5,000,000 per claim; (c) cyber liability of not less than $10,000,000; and (d) workers' compensation as required by Law.
- Require Provider to name Recipient and the Company as additional insureds on the CGL and professional liability policies.
- Require Provider to deliver certificates of insurance before the Effective Date and upon each renewal.

---

## ISSUE 13 — Data Breach Notification Period of 48 Hours Is Too Long

**Document / Section:** TSA, Section 8.3 (Data Security).

**Explanation:** Section 8.3 requires Provider to notify Recipient "within 48 hours after becoming aware of any unauthorized access to, or loss or disclosure of, Recipient Data." For a medical device company, Recipient Data includes Customer site data, equipment configuration, and service history. While this is not patient health information (PHI) in the HIPAA sense, a breach could expose commercially sensitive information and disrupt regulatory compliance.

Forty-eight hours is longer than best-practice standards (many contracts now require 24 hours or even 12 hours). Additionally, "becoming aware" is subjective—Provider could argue its security team did not "become aware" until after an internal investigation.

**Recommendation:**
- Reduce the notification period to 24 hours.
- Define "aware" to mean the earlier of (a) the time Provider's security systems detect the incident, or (b) the time any Provider employee or agent knows or should reasonably know of the incident.

**Proposed language for Section 8.3 (last sentence, revised):**

> Provider shall notify Recipient within twenty-four (24) hours after the earlier of (a) Provider's security systems detecting any unauthorized access to, or loss or disclosure of, Recipient Data, or (b) any employee or agent of Provider knowing or reasonably believing that such unauthorized access, loss or disclosure has occurred.

---

## ISSUE 14 — TSA Liability Cap May Be Inadequate for Service Failures

**Document / Section:** TSA, Section 11.4 (Cap); Section 11.5 (Exceptions).

**Explanation:** Section 11.4 caps each party's aggregate liability at "the total Monthly Service Fees paid and payable under this Agreement"—approximately $4,920,000 over the 12-month Term. The exceptions in Section 11.5 carve out: (a) indemnification obligations under Sections 11.1/11.2; (b) breach of confidentiality (Section 9); and (c) fraud, gross negligence, or willful misconduct.

However, many realistic service failures would fall within the cap:
- Provider negligently (but not grossly negligently) misconfigures the ERP, causing lost orders or billing errors;
- Provider's dispatch system fails for a week due to ordinary negligence in maintenance;
- Provider's remote service platform has a bug that causes incorrect diagnostics to be sent to field engineers.

In each case, the failure is not "gross negligence" or "willful misconduct," so the cap applies. A $4.92 million cap may not cover the downstream costs to Lalais (lost revenue, Customer contract penalties, regulatory exposure from delayed service).

**Recommendation:**
- Increase the cap to the greater of (a) total Monthly Service Fees paid and payable, or (b) $10,000,000.
- Add an exception to the cap for Provider's failure to meet SLA commitments (if SLAs are added per Issue 11), so that service credits and consequential losses from service outages are not capped.

---

## ISSUE 15 — SPA Escrow Release at 90 Days Provides No Security for Key Risks

**Document / Section:** SPA, Section 2.4(b) (Escrow Release Date); Section 9.1(b) (survival of product liability and FDA reps).

**Explanation:** The $18,650,000 escrow (10% of the Purchase Price) is released 90 days after Closing, less pending claims. Because the product liability and FDA representations (the most important regulatory protections for a medical device buyer) also expire at 90 days (see Issue 2), the escrow provides no security for those risks. After the Escrow Release Date:

- The escrow is gone;
- The product liability and FDA reps have expired;
- Lalais's only recourse for those matters would be a direct claim against Seller (subject to the cap in Section 9.4(b)), with no collateral.

This structure effectively tells Lalais: "You have 90 days to discover any product liability or FDA problems. After that, you're on your own."

**Recommendation:**
- This issue is inextricably linked to Issue 2. If survival periods are extended, the escrow release should be tied to the later of (a) 90 days after Closing, or (b) the expiration of the survival period for the representations secured by the escrow.
- Alternatively, split the escrow: release 70% at 90 days and hold 30% until 18 months (or the extended survival period for FDA/product liability reps).

---

## ISSUE 16 — SPA Section 4.8 Sufficiency Representation Is Subject to Deductible and Cap

**Document / Section:** SPA, Section 4.8 (Title to Assets; Sufficiency); Section 9.4(a) (Deductible of $932,500); Section 9.4(b) (Cap of $18,650,000 for non-Fundamental Reps).

**Explanation:** Section 4.8 represents that the Company's assets, together with the Bill of Sale assets and TSA services, are "sufficient for the continued conduct of the Business after the Closing in substantially the same manner as conducted before the Closing." This is a critical representation for Lalais—it is the contractual assurance that the deal delivers a functioning business.

However, Section 4.8 is not a Fundamental Representation, so any claim based on it is subject to:
- The $932,500 deductible (Section 9.4(a))—Lalais absorbs the first $932,500 of losses;
- The $18,650,000 cap (Section 9.4(b));
- The 18-month survival period (Section 9.1(a)).

If it emerges that the Business cannot be conducted "in substantially the same manner" because of missing tooling, inadequate service manuals, or insufficient transition support, Lalais must absorb nearly a million dollars before recovering anything.

**Recommendation:**
- Consider elevating Section 4.8 to a Fundamental Representation (which would remove the deductible and extend survival to the statute of limitations plus 60 days). If Seller resists, at minimum negotiate a separate, lower deductible (e.g., $100,000) for breaches of Section 4.8.

---

## ISSUE 17 — Prior Draft Comparison: Copyrights in Service Manuals Were Unresolved

**Document / Section:** Prior draft Bill of Sale, Section 1.3 (note: "Treatment of copyrights in service manuals under discussion"); Current Bill of Sale, Section 1.3 (adds "all copyrights and other rights in the service manuals included in the Transferred Assets").

**Explanation:** The February 24, 2026 draft explicitly flagged the treatment of copyrights in service manuals as an open item. The current draft resolves this in Lalais's favor by including "all copyrights and other rights in the service manuals" in the Transferred Assets. However, because the prior draft shows this was actively disputed, there is a risk that Seller may attempt to reopen the issue or that the inclusion was a drafting oversight rather than a negotiated resolution.

**Recommendation:**
- Confirm with the client that the inclusion of copyrights was expressly negotiated and agreed with Seller. If it was not, raise it before signing.
- Ensure that the service manuals identified in Schedule A, Part 3 are the definitive list and that Seller has no right to withhold any manual on the ground that it is "proprietary" or subject to a third-party license.

---

## ISSUE 18 — TSA Regulatory Support: Recipient Remains Responsible for FDA Submissions

**Document / Section:** TSA, Section 3.3 (Regulatory Support), last sentence: "Recipient remains responsible for all regulatory determinations and submissions relating to Company Products."

**Explanation:** During the 12-month TSA term, Provider logs complaints and service events and forwards them to Recipient (within 1 Business Day, or 24 hours for potentially reportable events). However, all regulatory determinations (e.g., whether a complaint triggers a Medical Device Report under 21 C.F.R. Part 803) and submissions to the FDA remain Recipient's responsibility.

This creates a timing risk: if Provider delays forwarding a complaint (even by one day), and that delay causes Recipient to miss an MDR reporting deadline (30 days for death/serious injury under Part 803), Recipient is in violation of FDA regulations with no recourse against Provider (short of arguing gross negligence).

**Recommendation:**
- Add a provision making Provider liable for Losses arising from its failure to forward complaints or service events within the timeframes specified in Section 3.3, regardless of whether the failure rises to gross negligence.
- Require Provider to maintain a backup forwarding mechanism (e.g., automated system alert) so that a single personnel absence does not delay forwarding.

**Proposed language (new sentence in Section 3.3):**

> Provider shall be liable for Losses incurred by Recipient or the Company resulting from Provider's failure to forward any complaint, service event or report within the timeframes specified in this Section 3.3, including any regulatory penalties or fines resulting from delayed reporting.

---

## ISSUE 19 — SPA Section 4.5 Cross-Reference Ambiguity

**Document / Section:** SPA, Section 4.5(c) ("except as set forth on Schedule 4.6"); Section 4.6 (Material Contracts).

**Explanation:** Section 4.5(c) carves out from the "no conflicts" representation any matter "set forth on Schedule 4.6." Schedule 4.6 is the Material Contracts schedule, which lists specific contracts (the Facility Lease, the Detector Supply Agreement) and their change-of-control provisions. The cross-reference works, but it is imprecise: Schedule 4.6(a) lists the contracts, while the change-of-control consent requirements are described in the narrative text of the schedule, not in a separate "consents" sub-schedule.

This is a minor drafting issue, but in the context of Issue 1 (Kestrevo), it highlights that the SPA's consent framework relies entirely on what is listed in the schedules, and the Kestrevo consent simply was not added to Schedule 7.2(d).

**Recommendation:** No standalone fix needed; addressed by the Schedule 7.2(d) addition recommended in Issue 1.

---

## ISSUE 20 — TSA: No Requirement for Provider to Maintain Business Continuity Plan

**Document / Section:** TSA — no business continuity or disaster recovery provision (other than the force majeure clause in Section 13.4).

**Explanation:** The TSA requires Provider to host the ERP, operate the remote service platform, and manage field dispatch for 12 months. There is no requirement that Provider maintain a business continuity plan, test its disaster recovery capabilities, or meet any recovery time objective. If Provider's data center is destroyed by fire (which is listed as a force majeure event in Section 13.4), Provider is excused from performance with no obligation to restore services within any specific timeframe.

**Recommendation:**
- Require Provider to maintain a written business continuity plan, tested at least annually, with a maximum recovery time of 24 hours for the ERP and 48 hours for the remote service platform.
- Require Provider to maintain backup systems at a geographically separate location.

---

## ISSUE 21 — SPA: No Specific Performance Carve-Out for Buyer's Right to Walk Away

**Document / Section:** SPA, Section 11.11 (Specific Performance); Section 10.1 (Termination).

**Explanation:** Section 11.11 provides that "each party shall be entitled to specific performance of the terms of this Agreement." This is mutual, meaning Seller could potentially seek specific performance to compel Buyer to close even if a condition in Section 7.2 is not satisfied (arguing that Buyer should have waived the condition). While Section 7.2 conditions are for Buyer's benefit and Buyer can waive them, the specific performance clause could be invoked by Seller to pressure Buyer into waiving conditions (e.g., the Kestrevo consent, if added per Issue 1).

**Recommendation:**
- Add a clarification that specific performance does not compel either party to waive a closing condition in Article 7.

**Proposed language (add to Section 11.11):**

> Nothing in this Section 11.11 shall be construed to require either party to waive any condition set forth in Article 7.

---

## ISSUE 22 — TSA: Monthly Service Fee Proration and No Early Termination Fee

**Document / Section:** TSA, Section 4.1 (proration for partial months); Section 12 (Termination).

**Explanation:** If Recipient terminates for Provider's material breach (Section 12.1), Section 12.3(a) requires Recipient to pay "all fees accrued for Services performed through the effective date of termination." There is no early termination fee or wind-down payment. This is favorable to Lalais. However, the proration provision in Section 4.1 means that if the TSA is terminated mid-month, Lalais pays only for the days of service actually rendered. No issue here—this is working in Lalais's favor. I flag it only to confirm the client is aware.

**Recommendation:** None. This is acceptable as drafted.

---

## ISSUE 23 — SPA: HSR Filing Deadline May Have Passed

**Document / Section:** SPA, Section 6.3 (Regulatory Filings): "Each party shall, within ten Business Days after the date of this Agreement, file any notification required under the HSR Act."

**Explanation:** The SPA is dated March 3, 2026. Ten Business Days from March 3, 2026 is approximately March 17, 2026. If the HSR filing has not been made by that date, both parties are in breach of Section 6.3. The HSR waiting period (typically 30 days) would then not have expired, making Section 7.1(a) (HSR expiration) a blocking condition to Closing.

**Recommendation:**
- Confirm with the client immediately whether the HSR notification has been filed and whether the waiting period has expired or early termination has been granted. If the filing was not made by the deadline, assess whether this constitutes a material breach giving rise to a termination right under Section 10.1(b) or (c), and whether the deadline should be extended by amendment.

---

## Items Requiring Client Input Before Responding to Trasirt

1. **HSR status:** Has the HSR notification been filed? Has the waiting period expired or has early termination been granted? (Issue 23.)

2. **Kestrevo relationship:** Does Lalais have any existing relationship with Kestrevo? Is Lalais willing to negotiate directly with Kestrevo for consent, or does it want Seller to handle the request? What is the commercial importance of the detector supply to the deal model? (Issue 1.)

3. **Transition timeline:** Does Lalais have a realistic plan to stand up ERP, remote service, and dispatch capabilities within 12 months? If not, how long does it need? This will inform the extension negotiation (Issue 8) and the SLA requirements (Issue 11).

4. **Asset register:** Has Seller delivered the asset register referenced in Bill of Sale Schedule A, items 5 and 6? If so, has Lalais reviewed it for completeness? (Issue 5.)

5. **Copyrights in service manuals:** Was the inclusion of copyrights in the current Bill of Sale (Section 1.3) expressly negotiated with Seller, or did it appear between drafts without discussion? (Issue 17.)

6. **CT/MRI service competitive landscape:** Does Lalais understand the competitive dynamics in CT/MRI service in the relevant geographies? This will inform how aggressively to push on the non-compete expansion (Issue 9).

7. **Insurance:** Does Lalais have a minimum insurance requirement it wants imposed on Trasirt for the TSA period? (Issue 12.)

---

## Items I Could Not Resolve From the Documents Alone

- The contents of the Disclosure Schedule beyond the excerpts provided (e.g., whether other contracts with change-of-control provisions exist).
- The actual asset register referenced in the Bill of Sale.
- The status of the HSR filing.
- Whether the Kestrevo consent was discussed and deliberately excluded from Schedule 7.2(d) or simply overlooked.
- The pre-Closing service levels actually delivered by Trasirt (the TSA's performance standard in Section 3.2(b) is measured against this baseline, but the documents do not specify what that baseline is).
- Whether any side letters or term sheets exist that modify the documents as drafted.