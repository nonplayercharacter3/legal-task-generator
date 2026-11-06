# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Vaigaind Data Halls, LLC / Trugeith Thermal Systems, Inc. – Review of Deal Documents

---

## Summary

I have reviewed the five documents in the matter folder: the Supply Agreement, SOW No. 2, the Service Level Schedule, the Data Processing Addendum, and the Phase 2 freight/rigging email thread. I identify **nine substantive issues** and **three gaps/incomplete items** that require attention before Vaigaind proceeds further. Issues are prioritized as High, Medium, or Lower.

---

## HIGH-PRIORITY ISSUES

### 1. Phase 1 Coupling Defect – Deemed Acceptance Likely Defeats the Expedited Remedy

**Where:** SOW No. 2, Recital C; Supply Agreement § 7.3, § 7.4, § 7.5, § 9.1, § 9.3.

**Facts.** Phase 1 CDUs were Delivered June 8, 2026. Vaigaind gave written notice of nonconformity (leaking quick-disconnect couplings) on July 10, 2026 – 32 days after Delivery. Section 7.3 provides a 20-day rejection window; the deadline was June 28, 2026. Trugeith has rejected the notice as untimely. The SOW No. 2 recital confirms the dispute is unresolved.

**Why it matters.** Because the notice was 12 days late, the Products are "deemed accepted" under § 7.3. Vaigaind therefore loses the § 7.4 remedy (repair or replace within 15 days at Supplier's cost, with Supplier bearing all freight, removal and reinstallation). Vaigaind's remaining route is the § 9.1 product warranty (36 months from the later of Delivery and commissioning completion), enforced through § 9.3 (repair/replace "promptly," or refund if Supplier fails within a "reasonable time"). The § 9.3 remedy is less structured: there is no fixed deadline, and "reasonable time" is fact-specific. In a data center context where leaking couplings pose a water-damage risk to live IT equipment, the absence of a hard 15-day cure deadline is a material gap.

**Recommendation.**
- Confirm the Phase 1 commissioning completion date (SOW No. 1 is not in the folder – see Gap 1 below) to calculate the warranty expiry.
- Send a formal warranty claim under § 9.1(b) (defect in materials/workmanship) with a specific cure deadline, preserving the argument that the 32-day delay was caused by the latent nature of the leak (couplings may not manifest a leak until pressurized during commissioning or initial operation).
- Consider whether the "deemed acceptance" language in § 7.3 can be challenged on the ground that the defect was not discoverable by reasonable inspection within 20 days (leakage under pressure may only appear after the system is charged). If so, Vaigaind may have an argument that the 20-day period should run from when the defect became known or knowable.
- In any event, document the risk: if the couplings fail again during Phase 2 operation, Vaigaind will want to show a pattern to support a Chronic Failure claim under SLS § 9.1(b) (three or more P1 Incidents from the same root cause within six months).

---

### 2. DPA Caps Data-Breach Liability Where the Agreement Intends It to Be Uncapped

**Where:** Supply Agreement § 12.3(b); DPA § 8.2; Supply Agreement § 1.4 (Order of Precedence).

**Conflict.** Agreement § 12.3(b) provides that the consequential-damages exclusion and the liability cap in § 12.2 do **not** apply to "breach of Section 14 (Confidentiality and Data Security)." Read plainly, a data-security breach is uncapped. However, DPA § 8.2 states: "Notwithstanding Section 12.3(b) of the Agreement, each Party's aggregate liability arising out of or relating to this Addendum or any Security Incident… is subject to the limitation of liability in Section 12.2 of the Agreement."

Under § 1.4, the DPA has first precedence "as to Personal Data only." So for any Security Incident involving Personal Data, the DPA's cap controls, and Vaigaind's recovery is limited to fees paid or payable in the 12 months preceding the event.

**Why it matters.** A breach of Trugeith's monitoring platform could expose badge-access records, employee contact details, and tenant alarm-routing information (DPA § 2.3). For a colocation operator, a data breach can trigger tenant notification obligations, regulatory exposure (NJ DPA, NY SHIELD Act), and reputational harm far exceeding 12 months of monitoring fees (approximately $133,200 for Phase 2 alone, plus Phase 1 fees). The cap effectively shifts most of the data-breach risk to Vaigaind.

**Recommendation.**
- Negotiate a carve-out: DPA § 8.2 should exclude from the cap (i) Supplier's indemnification obligations, (ii) gross negligence or willful misconduct, and (iii) Supplier's failure to maintain the security measures in Annex 1. Alternatively, raise the cap for DPA breaches to a fixed dollar amount (e.g., 3× the 12-month fee cap, or a floor of $5 million).
- At minimum, confirm that the $10 million cyber liability insurance in Agreement § 11(e) is intended to backstop the capped exposure and that Vaigaind is named as an additional insured or loss payee on that policy.

---

### 3. Exclusivity Obligation Is Extraordinarily Broad

**Where:** Supply Agreement § 3.1; SOW No. 2 § 2 (definition of "Covered Sites").

**Issue.** Section 3.1 requires Vaigaind to purchase **all** Covered Products for **all** Covered Sites exclusively from Trugeith for the entire Term (minimum 5 years, auto-renewing in 5-year increments). SOW No. 2 § 2 defines "Covered Sites" as "all data center facilities owned, leased or operated by Customer or any of its Affiliates in the United States and Canada." This captures not just the Secaucus campus but every current and future US/Canadian facility of Vaigaind and its Affiliates.

The only escape valve is § 3.2: if Trugeith notifies Vaigaind in writing that it cannot supply a product within the SOW lead times, Vaigaind may procure the affected quantity from a third party. There is no carve-out for quality failures, price increases, or Trugeith's insolvency (other than the general termination right in § 15.2).

**Why it matters.** If Vaigaind acquires or leases new facilities during the Term, it is locked into Trugeith for all liquid cooling. If Trugeith's product quality deteriorates (as the Phase 1 coupling issue suggests), Vaigaind has no contractual right to source alternatives based on performance – only on delivery delay.

**Recommendation.**
- Narrow "Covered Sites" to facilities identified in an exhibit or schedule, with a process to add new sites by mutual agreement.
- Add a quality/performance carve-out to § 3.2: if the Products fail to meet Specifications or service levels at a facility for a sustained period (e.g., a Chronic Failure under SLS § 9), Vaigaind may procure from a third party for that facility.
- If Trugeith resists, at minimum add a right to terminate the exclusivity obligation (without terminating the Agreement) upon a Chronic Failure at any Covered Site.

---

### 4. Remote Monitoring Fee May Not Be Fixed Beyond SOW Completion

**Where:** Supply Agreement § 5.1; SOW No. 2 § 7.4, § 9.1, § 12.1.

**Ambiguity.** Agreement § 5.1 states: "Prices are fixed for the duration of each SOW." SOW No. 2 § 12.1 provides that the SOW "continues until completion of Milestone M5" (target: April 16, 2027), but § 9.1 extends the Remote Monitoring Services "from Substantial Completion until the end of the Term" (i.e., at least through March 1, 2031, plus any renewal terms). The $1,850/CDU/month rate in § 7.4 is stated in the SOW pricing table.

Read literally, the price is fixed only until M5 (April 2027). After that, the monitoring service continues under § 9.1, but the SOW has "ended." There is no other provision in the Agreement that fixes the monitoring rate for the post-M5 period. Trugeith could argue it is entitled to adjust the rate annually or upon renewal.

**Why it matters.** Over a 5-year monitoring period, even a modest annual increase compounds significantly. For 6 CDUs at $1,850/month, the baseline is $133,200/year. A 5% annual increase would add roughly $36,000 over five years. More importantly, the uncertainty creates a negotiating disadvantage at renewal.

**Recommendation.**
- Amend SOW No. 2 § 7.4 (or add a side letter) to state that the $1,850/CDU/month rate is fixed for the full period of Remote Monitoring Services under § 9.1, i.e., through the end of the Agreement Term.
- Alternatively, cap any post-M5 increase at a defined formula (e.g., CPI or a fixed percentage per year).

---

### 5. Auto-Renewal with a Narrow and Early Non-Renewal Window

**Where:** Supply Agreement § 2.1, § 2.2.

**Issue.** The Initial Term is 5 years from March 2, 2026 (expiring March 1, 2031). The Agreement auto-renews for successive 5-year terms. To prevent renewal, a Party must give notice "during the thirty (30) day period ending two hundred seventy (270) days before the expiration of the then-current Term." For the Initial Term, 270 days before March 1, 2031 is approximately July 5, 2030, so the notice window is roughly **June 5 – July 5, 2030** – 18 months before the Term ends.

**Why it matters.** If Vaigaind's deal team misses this 30-day window (a very short and early deadline), the Agreement locks in for another 5 years – including the exclusivity obligation, the auto-renewal structure, and any fee levels then in effect. Given the breadth of the exclusivity (Issue 3) and the data-breach cap (Issue 2), being locked in for an additional 5 years without renegotiation is a significant commercial risk.

**Recommendation.**
- Calendar the non-renewal deadline immediately (June 5, 2030) and set internal reminders at 12 months, 6 months, and 3 months before the window opens.
- Negotiate to extend the notice window (e.g., 90 days instead of 30) and/or move it later (e.g., 180 days before expiration rather than 270).
- Consider adding a "material adverse change" trigger that allows either party to exit a renewal term if the other party has committed a Chronic Failure or material breach during the preceding Term.

---

## MEDIUM-PRIORITY ISSUES

### 6. Service Credits Are Modest Relative to Vaigaind's Actual Exposure

**Where:** Service Level Schedule § 5.1, § 5.4; Supply Agreement § 12.1.

**Issue.** The maximum monthly service credit is 100% of the Monthly Remote Monitoring Fee (SLS § 5.4). For Phase 2, that is 6 × $1,850 = **$11,100/month**. Even a total cooling failure for an entire month yields only $11,100 in credits. Meanwhile, Agreement § 12.1 excludes consequential damages, lost profits, and indirect losses. For a colocation operator, a cooling outage can trigger tenant SLA penalties, equipment damage claims, and regulatory reporting obligations – costs that dwarf $11,100.

The SLS does preserve "other rights and remedies" (§ 5.6) and the Chronic Failure provision (§ 9) gives a termination right, but there is no damages remedy for a single severe outage short of termination.

**Why it matters.** Vaigaind is effectively self-insuring the gap between the service credit and its actual loss. If Trugeith causes a multi-hour cooling outage that damages tenant equipment, Vaigaind's recovery is limited to the warranty (if the equipment is a "Product") or the indemnity (if it is a third-party claim), both of which are subject to the § 12.2 cap.

**Recommendation.**
- Negotiate a super-cap or carve-out for P1 Incidents that cause physical damage to Customer's or tenants' property: the § 12.2 cap should not apply where a P1 Cooling Outage results in damage to tangible property (this would fall within the § 10.1(b) indemnity, which is already excluded from the cap under § 12.3(a) – confirm this is the intended reading).
- Increase the service credit percentages or add a minimum dollar floor per P1 Incident.
- Confirm that the § 10.1(b) indemnity (bodily injury, property damage caused by the Products or Supplier's negligence) is truly uncapped via § 12.3(a), and that a cooling failure causing water damage to tenant cabinets would fall within it.

---

### 7. Design Basis Referenced as "Attached Separately" – Incorporation Uncertainty

**Where:** SOW No. 2 § 3.2, page 3 (footnote).

**Issue.** Section 3.2 makes the "Hall C Liquid Cooling Design Basis, Revision C, dated April 17, 2026" part of the Specifications and states it is "attached to this SOW as Exhibit A." However, the footnote on page 3 reads: "*Exhibit A: Hall C Liquid Cooling Design Basis, Revision C, dated April 17, 2026 (attached separately).*" The phrase "attached separately" creates ambiguity about whether the Design Basis was physically attached to the executed SOW or is a separate document that must be incorporated by reference. The Design Basis is not in our matter folder.

**Why it matters.** The Design Basis contains the load range, supply temperature setpoints, and facility water conditions against which the CDUs must perform. If it is not properly incorporated, there is a risk that Trugeith could argue the Specifications are limited to its own product data sheets (which Vaigaind does not control). The ±0.5°C supply temperature tolerance in § 3.2 is critical and references the Design Basis for the "full load range."

**Recommendation.**
- Obtain a copy of the Design Basis, Revision C, and confirm it was attached to or incorporated in the executed SOW.
- If it was "attached separately," ensure there is a signature or initialing block on the Design Basis itself referencing SOW No. 2, or a side letter confirming incorporation.
- Add the Design Basis to the matter file.

---

### 8. Liability Cap Lookback May Be Inadequate Early in the Relationship

**Where:** Supply Agreement § 12.2.

**Issue.** The cap is "fees paid or payable by Customer under this Agreement in the 12 months preceding the event giving rise to the claim." In the first 12 months of the relationship, total fees may be relatively low (Phase 1 products + installation + a few months of monitoring). If a significant claim arises in month 6, the cap could be a fraction of the total contract value.

**Why it matters.** This is a standard drafting point, but it is worth flagging because the Phase 1 dispute (Issue 1) arose early in the relationship. If the coupling defect leads to property damage, the cap calculation will reference only the fees paid in the preceding 12 months, which may not reflect the full economic value of the deal.

**Recommendation.**
- Negotiate a fixed-dollar cap (e.g., 2× or 3× the total SOW price) or a cap based on fees paid or payable over the full SOW term rather than a rolling 12-month lookback.
- At minimum, confirm that the § 12.3(a) indemnity carve-out covers property damage claims so the cap is not relevant for the most likely Phase 1 scenario.

---

## LOWER-PRIORITY / HOUSEKEEPING ISSUES

### 9. Milestone M1 Completion Not Evidenced in the Folder

**Where:** SOW No. 2 § 5.1 (M1: September 25, 2026); Email Thread, Message 1 (§ 1.1).

**Issue.** The October 27, 2026 email from Trugeith references "your approval of submittals at M1 on September 25" in past tense, implying M1 was met. However, no submittal approval or M1 completion certificate is in the folder. The 16-week lead time in § 5.2 runs from M1 approval, so confirming the actual M1 date is essential to verifying the M2 delivery date of January 18, 2027.

**Recommendation.** Request from Vaigaind's project team (Dana Whitcombe / Leo Fairbanks) the documentation evidencing M1 submittal approval and the date it was given. Confirm it aligns with September 25, 2026.

---

## GAPS AND ITEMS REQUIRING FURTHER CONTEXT

### Gap 1: SOW No. 1 Not in the Folder

SOW No. 1 (Phase 1) is referenced in SOW No. 2 Recital B but is not provided. Without it, I cannot verify:
- The Phase 1 commissioning completion date (needed to calculate the § 9.1 warranty period and the SLS Service Commencement Date);
- The Phase 1 product list, specifications, and any Phase 1-specific terms;
- Whether the Phase 1 SOW contains any amendments to the Agreement that might affect the Phase 1 dispute.

**Action:** Request SOW No. 1 from the client.

### Gap 2: Design Basis (Exhibit A) Not in the Folder

As noted in Issue 7, the Design Basis is referenced but not provided. It is a key component of the Specifications.

**Action:** Request the Design Basis, Revision C, from the client.

### Gap 3: Supplier Product Data Sheets (Revision 2026-04) Not in the Folder

SOW No. 2 § 3.2 incorporates "Supplier's product data sheets for each listed model, Revision 2026-04" into the Specifications. These are not in the folder. Without them, the full technical Specifications cannot be assessed.

**Action:** Request copies of the product data sheets for all six line items in SOW No. 2 § 3.1.

---

## ITEMS THAT APPEAR IN ORDER (No Action Required)

For completeness, the following items were reviewed and present no apparent issue:

- **Freight and rigging logistics** (Email Thread): The four-truck schedule, the 5-business-day notice requirement, the rigging subcontractor consent (with conditions), and the method-of-procedure timeline (December 4, 2026) are all consistent with SOW No. 2 §§ 6.2, 6.3, 10.2 and Agreement § 8.4. The consent was properly documented in writing via email.
- **Packing lists** (Email Thread, Messages 2.4 and 3.3): Confirmed consistent with Agreement § 6.3 and SOW No. 2 § 6.4.
- **DPA sub-processors** (DPA Annex 2): All three sub-processors are US-based, consistent with DPA § 3.5 (US-only storage/processing).
- **OT segregation** (DPA § 4.3): Monitoring Platform is logically segregated; no inbound connections to Customer's BMS without written approval. Appropriate for a data center environment.
- **Governing law and forum** (Agreement § 18): New York law, New York County courts, jury waiver. Standard and neutral.
- **Insurance** (Agreement § 11): Coverage limits appear adequate for the risk profile, including $10M cyber liability.

---

## Suggested Next Steps for Client Discussion

1. **Immediate:** Resolve the Phase 1 coupling dispute (Issue 1). Determine whether to pursue a warranty claim, negotiate a commercial resolution, or reserve rights while proceeding with Phase 2.
2. **Before M2 (January 18, 2027):** Confirm receipt of the updated certificate of insurance for Hackensack Rigging (due November 13, 2026 per email) and the method of procedure (due December 4, 2026).
3. **Near-term negotiation:** Address Issues 2 (DPA cap), 3 (exclusivity), 4 (monitoring fee fixation), and 5 (renewal window) in a side letter or amendment. These are structural issues that are harder to fix after the relationship is established.
4. **Document collection:** Obtain SOW No. 1, the Design Basis, and the product data sheets (Gaps 1–3).
5. **Calendar:** Set internal deadlines for the non-renewal notice window (June 5, 2030) and for tracking the Phase 1 warranty period.

---

Please let me know if you would like me to draft any of the recommended amendments or to prepare a more detailed analysis of the Phase 1 dispute once SOW No. 1 is available.