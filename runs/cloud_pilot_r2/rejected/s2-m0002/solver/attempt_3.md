# MEMORANDUM

**TO:** Supervising Partner
**FROM:** Associate
**DATE:** October 18, 2026
**RE:** Harrowgate Home Goods, Inc. / Bellweather Freight Logistics LLC: Review of Provider-draft MSA, SOW No. 1 and DPA against the Term Sheet and Broker Letter

**Privileged & Confidential / Attorney Work Product**

---

## 1. Summary

I reviewed the five documents in the matter folder, individually and against each other. Citations use these short forms:

- **MSA**: master_services_agreement_draft.md
- **SOW**: sow_no1_warehousing_last_mile.md
- **DPA**: data_processing_addendum.md
- **TS**: term_sheet_signed_2026-09-22.md
- **Broker Letter**: insurance_certificate_cover_letter.md

The Provider drafts are materially more Provider-favorable than the signed Term Sheet. The Term Sheet is non-binding on these points (TS §12.1), so it gives us leverage rather than a legal right. The most serious problems are:

1. **Exclusivity is far broader than the deal.** MSA §3.2 makes Provider exclusive for all warehousing, freight and delivery services nationwide, and bars Harrowgate and its Affiliates from self-performing. The TS limited exclusivity to last-mile home delivery in the NYC metro area (TS §§4.1–4.2).
2. **Liability is one-sided.** Harrowgate's broad indemnity (MSA §10.2) is uncapped and carved out of the exclusion of indirect damages (MSA §11.3). Provider's indemnity (MSA §10.1) is narrow and capped. The cap itself (MSA §11.1) is low and applies to loss of Harrowgate's inventory and to data breaches.
3. **Lock-in.** Harrowgate faces a 2-year initial term, automatic 3-year renewals, and a 15-day non-renewal window (MSA §§14.1–14.2). It has no termination for convenience and no chronic-SLA exit. The TS left renewal open (TS §10.2).
4. **Assignment is asymmetric.** Harrowgate cannot assign, even through a merger or change of control (MSA §17.4). Provider may assign freely without consent (SOW §8.2).
5. **The DPA sets Delaware law and Wilmington courts** (DPA §9.1). The MSA and the TS both call for New York law and New York County courts (MSA §18.1; TS §11). The order of precedence puts the DPA first (MSA §2.3).
6. **Insurance is not yet in place.** The additional-insured endorsements have not been issued. The cyber policy is claims-made and expires July 1, 2027. The actual certificate is not in our folder.
7. **SOW pricing has a steep cliff** between baseline and excess volumes (SOW §§5.1–5.3).

Part 4 lists the points to raise with the client before the next turn of the draft.

---

## 2. Issues in Order of Importance

### Issue 1: Exclusivity is nationwide, covers all logistics services, and binds Affiliates (CRITICAL)

**Where:** MSA §3.2; compare TS §§4.1–4.2; SOW §§1.3, 2.2, 4.1, 9.3; MSA §§1.1, 17.2.

**What the documents say.**
- MSA §3.2 appoints Provider exclusive provider of "all warehousing, freight transportation and delivery services required by Customer and its Affiliates throughout the United States."
- It also prohibits Harrowgate from using any third party, or from performing those services itself.
- TS §4.1 limited exclusivity to "last-mile home delivery within the New York City metropolitan area only."
- TS §4.2 said "No other services are subject to exclusivity" and that Harrowgate "remains free to use other providers, or to perform services itself," for everything else.

**Why it matters.**
- *It is a direct departure from the agreed term.* The Term Sheet is non-binding (TS §12.1), so this is leverage, not a breach.
- *The covered services are not priced or committed.* SOW No. 1 covers one Secaucus facility and the §4.1 Service Area. Line-haul is expressly out of scope (SOW §1.3). Provider would be Harrowgate's exclusive nationwide freight provider with no rates, capacity or service levels.
- *Day-one breach risk.* SOW §2.2 refers to Harrowgate's "current facility." Because §3.2 bars Harrowgate from performing warehousing "itself," the clause could be read to prohibit Harrowgate's own warehousing and store operations from January 1, 2027. It could also breach existing carrier contracts. We need to confirm this with the client.
- *Internal conflict with the SOW.* SOW §9.3 has Harrowgate arrange and pay for inbound transportation to the Facility. MSA §3.2 forbids Harrowgate from using a third party for that freight. Under MSA §2.3 the MSA prevails.
- *Exclusivity ties Harrowgate's hands when Provider fails.* The only relief is the force majeure cover right (MSA §17.2), and only after 15 days. Chronic SLA failures, capacity shortfalls or Provider-side labor disruption do not trigger it, and Harrowgate would keep paying the fixed fee.
- *It reaches Affiliates.* "Affiliate" means more than 50% voting control (MSA §1.1). Harrowgate must "cause" Affiliates to comply even though they are not parties.

**Recommendation (redline MSA §3.2).**

> "3.2 Exclusivity. During the Term, Customer shall use Provider as its exclusive provider of last-mile home delivery services to end customers located within the Service Area (as defined in Section 4.1 of Statement of Work No. 1). Nothing in this Agreement restricts Customer or its Affiliates from engaging any third party, or performing itself, any other warehousing, freight transportation, line-haul, inbound, store-delivery, customer-pickup or delivery services, including delivery outside the Service Area. The exclusivity in this Section 3.2 shall not apply (a) to the extent Provider fails to perform, or is excused from performing, the Services, including during a force majeure event; (b) for volumes exceeding [capacity commitment]; (c) if Provider fails to meet any service level in [two] of [three] consecutive months; or (d) after notice of termination by either Party. This Section 3.2 does not bind Customer's Affiliates."

**Ask of the counterparty.** Explain the departure from TS §4. If Bellweather wants broader exclusivity, it must offer rates, capacity and service levels for the added scope, and consider an exclusivity exception for Harrowgate's existing carrier relationships.

---

### Issue 2: Indemnity asymmetry and uncapped Customer indemnity (CRITICAL)

**Where:** MSA §§10.1, 10.2, 10.3, 11.3. TS §8.2 left indemnities "to be negotiated" and TS §8.1 contemplated a mutual cap with "customary exceptions."

**What the documents say.**
- *Provider indemnity (MSA §10.1).*
  - It covers only third-party claims "to the extent arising from" (a) bodily injury or property damage caused by Provider's negligence or willful misconduct, (b) violation of law, or (c) personnel wage claims.
  - It is subject to the §11.1 cap, because §11.3 carves out only §10.2.
- *Customer indemnity (MSA §10.2).*
  - It covers any third-party claim "arising out of or relating to" (a) Customer Goods, including defects, (b) any Customer or end-customer premises where Provider performs Services, or (c) "Customer's use of the Services."
  - It is not limited to claims caused by Harrowgate. It is expressly uncapped and uncarved from the damages exclusion (MSA §11.3).

**Why it matters.**
- *Overlap and conflict.* Provider's crews carry furniture into end customers' homes (SOW §§4.2, 4.4). If a crew negligently injures someone or damages a residence, MSA §10.1(a) says Provider indemnifies. MSA §10.2(b) (end-customer premises) and §10.2(a) (Customer Goods) say Harrowgate indemnifies, without limit, and Provider can invoke it. A court would have to reconcile the two clauses.
- *Possible indemnity for Provider's own negligence.* New York courts generally require that an intent to indemnify a party for its own negligence be unmistakably clear. The breadth of "relating to" and the absence of any "except to the extent caused by Provider" qualifier create real uncertainty. We should confirm the current case law before relying on this argument.
- *Uncapped exposure.* Harrowgate's potential liability is unlimited, while Provider's is limited to roughly 12 months of fees, about $2.21 million at the $184,500 monthly fee (SOW §5.1).
- *Gaps in the Provider indemnity.* It does not cover:
  - data and security incidents or DPA breach (only a reimbursement covenant in DPA §5.5);
  - breach of confidentiality;
  - IP infringement by Provider systems or the portal;
  - liens;
  - fines or penalties;
  - taxes.
- *Control of defense (MSA §10.3).* The indemnifying Party gets "sole control" of defense and settlement. Where Provider is the indemnitor, it would control the defense of claims against Harrowgate that affect Harrowgate's brand and end-customer relationships. Settlement consent is required only if the settlement imposes "any obligation or admission."

**Recommendation.**
- Replace §10.2 with a fault-based indemnity:

> "10.2 By Customer. Customer shall defend, indemnify and hold harmless Provider … from third-party claims to the extent arising from (a) an allegation that Customer Goods, as delivered to Provider and excluding any damage or alteration caused by Provider or its personnel, infringe a third party's intellectual property rights or are defective in design or manufacture, or (b) Customer's breach of Section 4.2 (hazardous materials), in each case except to the extent caused by the negligence, willful misconduct or breach of Provider, its personnel or subcontractors."

- Delete §10.2(b) and (c).
- Expand §10.1 to add (d) breach of Section 8 or Section 9 or the DPA, (e) Provider's infringement, and (f) Security Incidents caused by Provider or its Subprocessors.
- Revise §10.3 so the indemnified Party may assume its own defense, at the indemnitor's cost, where there is a conflict, regulatory exposure or reputational impact.
- Make the indemnities symmetrical in the §11 carve-outs (see Issue 3).

---

### Issue 3: Liability cap and damages exclusion (CRITICAL)

**Where:** MSA §§11.1, 11.2, 11.3, 6.3, 12.1(c); DPA §5.5; SOW §6.3; TS §8.1.

**What the documents say.**
- The cap is "the fees paid or payable in the 12 months before the claim" (MSA §11.1). "Fees" is not capitalized in the clause, though it is defined as a term in §1.5.
- The only carve-outs are Customer's §10.2 indemnity, fraud, gross negligence, willful misconduct and Customer's payment of Fees (MSA §11.3).

**Why it matters.**
- *Early-term cap is tiny.* A claim in month 2 may yield a cap equal to roughly two months of fees, about $369,000. Even at full run rate the cap is about $2.21 million.
- *Loss of Customer Goods is capped.* Provider is insured for $5,000,000 per occurrence under warehouse legal liability (MSA §12.1(c)), and landed-cost reimbursement is its core obligation (MSA §6.3; SOW §6.3). A cap below that coverage leaves Harrowgate's inventory under-protected. We do not know the inventory value, and the client must tell us.
- *Data breach is capped.* The DPA has no liability clause. "This Agreement" in §11.1 includes the DPA, which "forms part of the Agreement" (DPA preamble). Notification, call center and credit-monitoring costs (DPA §5.5) may also be argued to be "consequential" damages excluded by §11.2. The Provider's cyber coverage is $3,000,000 per claim (MSA §12.1(f)).
- *Lost profits and replacement costs are excluded* (MSA §11.2). A failure to deliver during peak season could cause mostly lost-revenue and cover costs. Harrowgate has no direct remedy for those.
- *The cap is nominally mutual but practically one-way.* Harrowgate's main exposure is uncapped under §10.2, while Provider's main exposures are capped.

**Recommendation (redline MSA §§11.1–11.3).**

> "11.1 … shall not exceed the greater of (a) the Fees paid and payable in the twelve (12) months preceding the event giving rise to the claim (or, if the event occurs in the first twelve months, the Fees projected for the first twelve months) and (b) $[●]."
>
> "11.3 Exceptions. Sections 11.1 and 11.2 shall not apply to: (a) either Party's indemnification obligations under Section 10; (b) Provider's obligation to reimburse loss of or damage to Customer Goods under Section 6.3, which shall be limited only by the greater of $[●] and the limits of insurance required under Section 12.1(c) and (d); (c) breach of Section 8 or Section 9 or the DPA, subject to a separate cap of the greater of $[●] and [●]x annual Fees [or the cyber limit in Section 12.1(f)]; (d) fraud, gross negligence or willful misconduct; (e) Customer's obligation to pay Fees properly due; or (f) amounts covered by insurance required under Section 12."
>
> Add: "The following are direct damages: costs of notification, credit monitoring, forensic investigation and regulatory response arising from a Security Incident; reasonable cover costs; and amounts reimbursed under Section 6.3."

Cap figures need client input on inventory value and the volume of personal data (see Part 4). Baseline volumes imply roughly 78,000 end-customer deliveries per year (SOW §5.2).

---

### Issue 4: Three-year auto-renewal, 15-day opt-out window, and no convenience or chronic-failure exit (CRITICAL)

**Where:** MSA §§14.1, 14.2, 14.3, 14.5, 17.1; SOW §§2.3, 6.2; TS §§5, 10.1, 10.2.

**What the documents say.**
- The Initial Term is 2 years "from the MSA Effective Date" (MSA §14.1). That term is not defined; the MSA defines "Effective Date."
- The Agreement then automatically renews for successive **3-year** Renewal Terms. Non-renewal notice must be delivered "during the fifteen (15) day period ending one hundred twenty (120) days before the expiry." Notice at any other time "shall be of no effect" (MSA §14.2).
- Notices must be hand-delivered, couriered or sent by certified mail (with email copy) and are effective on receipt (MSA §17.1).
- The TS agreed only the 2-year initial term (TS §5). It left "renewal, termination and assignment terms to be negotiated" (TS §10.2).

**Why it matters.**
- *Narrow window.* For an Initial Term ending around December 31, 2028 / January 1, 2029, the window would run roughly August 19 to September 3, 2028. The exact dates turn on how the end of the Initial Term is read. A missed or late notice locks Harrowgate in for three more years.
- *Cost of missing it.* Three more years at the fixed fee is at least $6,642,000 (36 × $184,500), before excess volumes. The Initial Term commitment is $4,428,000 (24 × $184,500).
- *No other exit.* There is no termination for convenience for Harrowgate, no right to terminate for chronic SLA failure, and no right to terminate on a Provider change of control. Service credits are capped at 10% of the monthly fee (SOW §6.2). The only exit is a material breach with a 30-day cure (MSA §14.3).
- *Compounding with exclusivity.* Issue 1 means Harrowgate could be exclusively tied for up to five years with no price protection. The SOW does not freeze fees for the term.

**Recommendation.**
- Redline MSA §14.1 to "two (2) years from the Effective Date" (fix the defined term).
- Redline MSA §14.2:

> "… automatically renew for successive renewal terms of one (1) year each, unless either Party gives written notice of non-renewal at least sixty (60) days before expiry of the then-current term. Provider shall give Customer written reminder notice not more than one hundred fifty (150) and not less than ninety (90) days before expiry; if Provider fails to do so, the Agreement shall not renew beyond the then-current term unless Customer so elects in writing."

- Add Customer termination rights:
  - for convenience on [90] days' notice;
  - for chronic SLA failure (for example, any service level missed in 3 of 6 months, or any level missed by more than a stated margin);
  - on Provider's change of control or assignment.
- Add a fee freeze for the Initial Term and a cap on increases in any Renewal Term.
- Add an email-notice option for non-renewal in §17.1.

---

### Issue 5: One-way assignment restrictions; SOW lets Provider assign without consent (HIGH)

**Where:** MSA §17.4 vs. SOW §8.2; MSA §§2.3, 7.2; DPA §6.1; TS §10.2.

**What the documents say.**
- MSA §17.4 bars only *Customer* from assigning "by operation of law, by merger or change of control or otherwise" without Provider's consent.
- SOW §8.2 allows Provider to "assign, delegate or otherwise transfer this SOW, and any of its rights and obligations under this SOW and under the Agreement, in whole or in part, to any third party, without Customer's consent," with notice within 30 days *after* it becomes effective.
- MSA §2.3 puts the MSA above the SOW. But because MSA §17.4 is silent on Provider assignment, the two arguably do not "conflict," so SOW §8.2 may control.

**Why it matters.**
- *Harrowgate's M&A and financing flexibility is restricted.* A change of control is itself an assignment requiring Provider consent. That gives Provider hold-up leverage in any sale or restructuring, and a cash-flow lever if it wants to renegotiate.
- *Provider could hand off its obligations.* It could transfer Harrowgate's goods, data and operations to an unknown, unrated or competitor-owned entity, with notice after the fact. That undercuts the subcontractor consent right in MSA §7.2, SOW §8.1 and DPA §6.1. These are consent rights that a transfer to a third party would circumvent.
- *Insurance and data risks.* Policies and Subprocessor approvals are tied to Bellweather (Broker Letter §2.1; DPA Annex 3).

**Recommendation.**
- Delete SOW §8.2.
- Redline MSA §17.4:

> "Neither Party shall assign … without the other Party's prior written consent, not to be unreasonably withheld, except that Customer may assign this Agreement without consent to an Affiliate or to a successor to all or substantially all of the business to which this Agreement relates, whether by merger, change of control, sale of assets or otherwise, on written notice. Provider's assignment, or a change of control of Provider, shall entitle Customer to terminate on thirty (30) days' notice."

---

### Issue 6: DPA sets Delaware governing law and forum, and the DPA is first in precedence (HIGH)

**Where:** DPA §9.1; MSA §§2.3, 18.1, 18.2; TS §11; DPA §10.1.

**What the documents say.**
- DPA §9.1 states Delaware law governs "any dispute relating to the Processing of Personal Data or any Security Incident," with exclusive jurisdiction in the state and federal courts in Wilmington, Delaware.
- MSA §18.1 selects New York law and New York County courts. TS §11 says the Definitive Agreements "will be governed by New York law, with disputes resolved in the state and federal courts in New York County."
- MSA §2.3 puts the DPA first in the order of precedence.

**Why it matters.**
- *The DPA overrides the MSA's forum clause.* Data disputes would be litigated in Delaware under Delaware law. A single data incident could also produce MSA claims in New York, split proceedings and inconsistent results. The jury waiver, escalation process and injunction language in MSA §§18.2–18.4 may not neatly apply.
- *The agreement is otherwise New York-centric.* Harrowgate is a New York corporation, the DPA relies on New York's SHIELD Act (DPA §§1.1, 4.1), and the TS expressly agreed New York.
- *Nothing in the DPA supports Delaware.* Neither party's connection to Delaware is described, and Bellweather's state of organization is not stated anywhere in the folder.

**Recommendation.**
- Replace DPA §9.1:

> "9.1 Governing Law and Forum. This DPA is governed by the law and subject to the dispute resolution provisions of Section 18 of the Agreement."

- Narrow MSA §2.3 so that the DPA prevails only on the processing and security of Personal Data:

> "… the Data Processing Addendum (solely as to the Processing and security of Personal Data), then this Agreement, then the Statement of Work."

- Raise this with Bellweather as a conformity to the Term Sheet.

---

### Issue 7: Insurance. Coverage is not yet effective, and the Broker Letter does not close the gaps (HIGH)

**Where:** Broker Letter §§1.2, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1; MSA §§12.1, 12.2; SOW Schedule A; TS §8.3.

**What the documents show.** Every limit in the Broker Letter matches the MSA §12.1 minimum exactly:

| Coverage | MSA §12.1 | Broker Letter §2.1 |
|---|---|---|
| CGL | $2M / $4M | $2M / $4M |
| Auto | $5M CSL | $5M CSL |
| Warehouse legal liability | $5M | $5M |
| Motor truck cargo | $250K per vehicle | $250K per vehicle |
| Employer's liability | $1M | $1M |
| Cyber | $3M per claim | $3M per claim |

All insurer ratings meet A- VII. The issues are structural.

**(a) Additional-insured status is not in place.**
- Broker Letter §3.1 says the endorsements "will be issued … on execution of the Agreement," and the Certificate "names" Harrowgate as additional insured. A certificate cannot confer coverage. The Broker Letter itself says the Certificate is "issued as a matter of information only" (§5.1).
- Copies of the endorsements are to follow "once issued," with no deadline.
- The 30-day cancellation notice is also prospective ("will be endorsed," §3.2).
- Under MSA §12.2 certificates are due "before the start date of the first Statement of Work" (January 15, 2027). Schedule A has the initial inventory transfer on January 14, 2027, one day *before* go-live and, if the January 11 target slips, possibly before any proof of coverage.

**(b) The enclosed Certificate is not in our folder.** We have only the cover letter. We cannot verify the named insured, the additional-insured wording, the certificate-holder box, policy forms or exclusions.

**(c) The cyber policy is claims-made and expires mid-Term.** The policy period is July 1, 2026 to July 1, 2027 (Broker Letter §2.1). Broker Letter §4.2 promises a renewal certificate only "on or before that expiry date." MSA §12.1 requires coverage for the Term plus one year but says nothing about retroactive dates or extended reporting periods, so a lapse or a change of retroactive date could leave a gap.

**(d) Limited additional-insured and no loss-payee protection.** MSA §12.2 requires additional-insured status only on CGL and auto. Harrowgate's goods are insured only through warehouse legal liability and motor truck cargo. Those policies pay for Provider's legal liability and are not named for Harrowgate's benefit. The MSA does not require primary and non-contributory wording or waiver of subrogation, and no excess/umbrella coverage is required.

**(e) The broker is Provider's broker.** Quillmore acts for Bellweather (Broker Letter §1.1) and measured the Certificate against the Provider's own draft (§1.2). Its statements of compliance (§2.2) are not an independent review and owe nothing to Harrowgate. The copy of the Broker Letter in our folder is also unsigned (signature line blank).

**(f) Sufficiency of limits.** The limits were set by Provider's draft and match exactly, with no cushion. They should be tested against inventory value (client input). The cargo limit of $250,000 per vehicle should be checked against typical truckload values for furniture.

**Recommendation.**
- Request from Bellweather the full Certificate and copies of all policies and endorsements. We also need each cyber policy's retroactive date and extended-reporting terms.
- Redline MSA §12.2:

> "Provider shall deliver, before any Customer Goods are tendered to Provider (including under the implementation plan in SOW Schedule A), certificates and copies of the additional-insured and notice-of-cancellation endorsements. Customer shall be named as additional insured on the policies in Sections 12.1(a) and (b) (including products-completed operations coverage), and as loss payee, to the extent of its interest in Customer Goods, on the policies in Sections 12.1(c) and (d). Such coverage shall be primary and non-contributory, with waiver of subrogation in favor of Customer. For claims-made coverage, Provider shall maintain a retroactive date no later than the Effective Date and an extended reporting period of at least [3] years after the Term. Renewal certificates shall be delivered at least thirty (30) days before expiry."

- Add an umbrella/excess requirement of $[●] if the client's inventory values warrant.
- Add a Customer right to delay the Start Date or terminate if coverage is not evidenced.

---

### Issue 8: SOW pricing cliff between the fixed fee and excess-volume rates (HIGH, business input required)

**Where:** SOW §§5.1, 5.2, 5.3, 9.4; TS §§6.1, 6.2.

**What the documents say.**
- The fixed Monthly Service Fee of $184,500 covers storage and up to 2,400 inbound pallets, 9,000 e-commerce orders and 6,500 deliveries (of which no more than 1,500 are White Glove) (SOW §§5.1–5.2). This matches TS §6.1.
- Excess volumes are billed at $9.50/pallet, $4.25/order, and $68/$89/$129 per delivery (SOW §5.3).

**Why it matters.**
- *Implied pricing mismatch.* At the excess unit rates, baseline volume alone would cost at least $503,050 per month before any storage charge (2,400 × $9.50 = $22,800; 9,000 × $4.25 = $38,250; 6,500 × $68 = $442,000 at the lowest delivery rate). The fixed fee implies a baseline delivery cost of under $29. Excess deliveries therefore cost 2.4x to 4.5x as much per delivery as baseline ones. For a furniture retailer with seasonal peaks, this is a significant cost exposure above the baseline.
- *No downside protection.* There is no volume true-down, so Harrowgate pays the full fixed fee whatever its volume. There are also no tiered rates or peak-season terms.
- *Ambiguity on the White Glove cap.* SOW §5.2(c) limits White Glove deliveries to 1,500 within baseline. It does not say whether White Glove deliveries above that number are billed at $129 when total deliveries are below 6,500.
- *Item size and disassembly assumption.* The fees assume no item over 350 lbs and none "requires disassembly" (SOW §9.4). Items outside that range go to a change order with no pre-agreed price. For furniture, this could capture a meaningful share of volume.
- *Haul-away.* The $45 haul-away rate (SOW §5.3) refers to existing furniture, while SOW §1.2(d) refers to packaging. It is unclear what is included in the fixed fee.

**Recommendation.** Confirm with the client whether the fixed fee was intended as a heavily discounted baseline. Then request:
- tiered or step-down excess pricing;
- a peak-season volume allowance;
- a pre-agreed rate card for items over 350 lbs or requiring disassembly;
- a clarification that White Glove deliveries above 1,500 are excess only if total deliveries exceed 6,500;
- a fee freeze for the Initial Term.

---

### Issue 9: Service level remedies, force majeure and transition (MEDIUM-HIGH)

**Where:** SOW §§6.1–6.2; MSA §§3.3, 14.3, 15.1–15.2, 17.2, 5.4, 6.1.

- *Credit cap is modest.* Credits are 2% of the fee per missed service level, to a maximum of 10% (SOW §6.2), i.e., a maximum of $18,450 a month. There is no termination right for repeated misses (see Issue 4).
- *Credits only against the "next invoice"* (MSA §3.3). Credits owed at expiry or termination are lost unless the clause provides for cash payment.
- *Force majeure (MSA §17.2).*
  - The list is non-exhaustive and does not exclude Provider's own labor disputes, subcontractor failures, cyber events, or facility/utility failures.
  - Payment obligations remain in force, so Harrowgate could pay the full fixed fee for Services not delivered.
  - Harrowgate's cover right arises only after 15 days, and for "the duration of the event," which conflicts with MSA §3.2 exclusivity.
- *Transition (MSA §15.2).* Provider gives "reasonable transition assistance for up to 90 days." It does not say that Services continue at existing rates or that Provider keeps performing during that period. Release of goods is not conditioned on payment (MSA §15.1), but there is no express bar on withholding goods or data in a dispute.
- *Liens.* MSA §6.1 preserves any lien "that cannot be waived under applicable law." Because the Secaucus facility is in New Jersey and goods will be held there, we should confirm whether warehouse-lien rights apply and ensure they cannot be asserted against disputed amounts.
- *Provider's warehouse receipts, bills of lading and tariffs.* The MSA does not state that these documents cannot limit Provider's liability. Federal carrier liability rules may also apply to interstate movements (New York to New Jersey). We should verify and add an express override.

**Recommendation.**
- Raise the credit cap (e.g., 20–25% of the monthly fee) and add "earn-back" only if the client prefers.
- Pay credits in cash on termination.
- Add a chronic-failure termination right.
- Redraft §17.2 to exclude Provider's own labor disputes and subcontractor failures, and to abate Fees for Services not performed.
- Provide a cover right for any prolonged non-performance.
- Add: "Provider shall continue the Services at the then-current Fees during transition, shall not withhold Customer Goods or Customer Data on account of any dispute, and waives any warehouse lien to the extent permitted by law. No terms in any bill of lading, warehouse receipt, delivery receipt, tariff or similar document shall limit Provider's liability under this Agreement."

---

### Issue 10: Data protection points (MEDIUM)

**Where:** DPA §§1.1, 2.3, 4.1, 5.1, 5.5, 6.1, 7.3, Annex 3; MSA §§8.3, 9, 13.2, 15.4.

- **Annex 3 (Approved Subprocessors) is blank**, to be "completed by Provider … before the Start Date." The last-mile delivery model commonly uses subcontract drivers. Harrowgate should not approve the blank, and should require the Subprocessor list before signing.
- **Incident notice is 48 hours** (DPA §5.1), measured from Provider "becoming aware." The TS said "promptly" (TS §9). Consider shortening to 24 hours. At minimum, make clear the clock runs from the first indication of a suspected incident (the definition already includes "reasonably suspected," DPA §1.4).
- **Reimbursement is limited to incidents "caused by a breach of this DPA"** (DPA §5.5). Extend to any incident arising from Provider's or its Subprocessors' acts or omissions. Add regulatory fines and penalties, forensic costs and legal fees.
- **MSA §8.3 exclusions** (publicly available, previously known, etc.) could be argued to apply to Customer Data. Carve Personal Data and Customer Data out of §8.3.
- **Customer Data ownership does not survive.** MSA §13.2 (Customer owns Customer Data and reports) is not in the survival clause (MSA §15.4); only §13.1 survives. See Issue 11.
- **The DPA does not address Provider's cyber insurance** or tie reimbursement to it. Cross-refer to MSA §12.1(f).
- The 30-day return of Customer Data (DPA §8.1) is acceptable, but should run *concurrently* with transition assistance and must not be held back pending payment.

---

### Issue 11: Drafting errors, gaps and housekeeping (MEDIUM / LOW)

| # | Where | Point | Fix |
|---|---|---|---|
| 11.1 | MSA §14.1 | "MSA Effective Date" is undefined. | Use "Effective Date." |
| 11.2 | MSA §15.4 | Survival list omits §6.3 (loss/damage claims), §9 and the DPA, §12 (insurance tail), §13.2 (data and report ownership), and accrued service credits. | Add them. |
| 11.3 | MSA §11.1 | "fees" is lower-case and undefined in the clause. | Use the defined term "Fees." |
| 11.4 | MSA signature page / §17.1 | Notice addresses are blank, and no email addresses are specified though §17.1 requires an email copy. | Complete before signing. |
| 11.5 | MSA preamble | Bellweather is described only as "a limited liability company." No jurisdiction of organization is given, though §16.1(a) represents good standing "under the laws of its jurisdiction of organization." | Insert state of organization. Request good-standing certificate and financial information. Consider a parent guaranty. |
| 11.6 | MSA §16.2(a) | Motor carrier authority is represented but not identified. | Request USDOT/MC numbers and permits and verify. |
| 11.7 | MSA (no entire-agreement clause) | There is no merger clause. The Term Sheet remains a separate document with binding confidentiality and costs terms that survive for two years (TS §§12.2–12.3). | Add an integration clause that supersedes non-binding Term Sheet terms. Expressly preserve or fold the confidentiality terms into MSA §8. The client should know that, once integrated, the Term Sheet will no longer help to interpret the deal. |
| 11.8 | TS signature blocks | Signed copy shows "/s/ Authorized Signatory" with signatory name and title lines blank. | Confirm the executed copy and the signatories' authority. |
| 11.9 | SOW §3.6(b) vs. §2.2 and Schedule A | An annual physical inventory is required "during January of each year," but the initial transfer is only reconciled January 14, 2027. | Clarify that the first physical count follows the initial reconciliation. |
| 11.10 | MSA §10.3 | Notice-delay protection is only to the extent of "material" prejudice. | Acceptable, but confirm client comfort. |
| 11.11 | MSA §5.4 / §3.3 | No express set-off right for credits or indemnity amounts. | Add a right to set off undisputed amounts owed by Provider. |
| 11.12 | SOW §6.3 | Loss/damage claims must be paid within 30 days of written claim, but there is no claim-filing deadline. | Acceptable. Note it is helpful to Harrowgate. |

---

## 3. Consistency Check: Points Where the Documents Align

For completeness, the following items cross-check correctly:
- **Dates.** Effective Date of January 1, 2027 and SOW start of January 15, 2027 (MSA preamble; SOW §2.1; TS §5), and the 2-year initial term (MSA §14.1; TS §5).
- **Fees and payment terms.** $184,500 per month, monthly invoicing in arrears, 45-day payment and good-faith withholding (SOW §5.1; MSA §§5.3–5.4; TS §§6.1, 6.3).
- **Facility and goods.** The Secaucus facility (SOW §3.1; TS §3.1), title in Harrowgate and landed-cost reimbursement (MSA §§6.1, 6.3; SOW §6.3; TS §7).
- **Data location.** US-only processing (DPA §3.5; TS §9).
- **Service levels.** The five SLA categories track TS §3.3.
- **Insurance minimums.** The Broker Letter limits and ratings meet MSA §12.1 (Issue 7).
- **Internal cross-references.** The section cross-references I checked between the MSA, SOW and DPA are accurate, apart from the defined-term error in MSA §14.1.
- **Service area.** SOW §4.1 lists the five boroughs plus Nassau, Suffolk, Westchester, Rockland and four New Jersey counties. This is broader than "NYC metropolitan area" as the TS describes it (TS §§3.2, 4.1) but is not inconsistent. The TS term "NYC metropolitan area" is undefined, so any exclusivity should be tied to the SOW's defined Service Area (Issue 1).

---

## 4. Items to Raise with the Client Before the Next Turn

1. **Exclusivity.** Does Harrowgate (or any Affiliate) currently self-perform warehousing, freight or delivery, or hold carrier contracts that would be breached on January 1, 2027? Would it accept any exclusivity beyond the NYC-area last-mile delivery in the Term Sheet?
2. **Peak volumes and forecasts.** What are realistic monthly and peak-season volumes compared with the baselines (2,400 pallets, 9,000 orders, 6,500 deliveries)? Is the fixed fee intended as a discounted baseline (Issue 8)? How many items exceed 350 lbs or need disassembly?
3. **Inventory value at the Secaucus facility** and the expected maximum value in a single truck. This drives the cap and the WLL, cargo and excess insurance requirements (Issues 3, 7).
4. **Personal data volumes and breach-cost exposure**, and whether Harrowgate carries its own cyber coverage that interacts with the Provider's $3M cyber policy.
5. **Transaction or financing plans.** Any anticipated sale, merger, financing or affiliate reorganization within the next five years (Issue 5).
6. **Term and exit appetite.** Is a 2-year term with 1-year renewals acceptable? Does the client want convenience termination, or at least a chronic-failure exit (Issue 4)?
7. **Reliance on Provider's insurance broker.** Confirm Harrowgate has not accepted the Broker Letter as satisfying diligence. We should request the Certificate, endorsements and policies (Issue 7).
8. **Existing communications.** Whether Bellweather made any commitments or representations outside the documents (for example, on exclusivity scope, pricing or insurance), since the MSA has no integration clause (Issue 11.7).
9. **Bellweather's credit and operations.** Whether the client has diligence on Bellweather's financial standing, state of organization, motor carrier authority and subcontractor use, which are not addressed in the folder.

---

## 5. Limits of This Review

- I reviewed only the five files in the matter folder. The **Certificate of Liability Insurance** the Broker Letter says is enclosed was not in the folder. Schedule A is the only schedule to the SOW, and DPA Annex 3 is blank.
- I have not reviewed any other agreements, Harrowgate's existing carrier or warehouse contracts, or the policies themselves.
- Statements of New York law above are general. In particular, the standard for indemnifying a party for its own negligence, the treatment of non-binding term sheets, and the interaction of federal carrier liability rules and warehouse liens should be confirmed by research before we cite them to the counterparty.
- Dollar figures are my arithmetic from the SOW's stated fees and rates. Dates for the non-renewal window are approximate and depend on how the end of the Initial Term is read.

I can turn these recommendations into a full redline of the MSA, SOW and DPA, plus a short issues list for Bellweather's counsel, once you have confirmed the priorities.