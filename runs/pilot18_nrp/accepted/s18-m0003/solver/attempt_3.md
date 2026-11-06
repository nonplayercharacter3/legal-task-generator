# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Vaigaind Data Halls, LLC / Trugeith Thermal Systems, Inc. – Review of Deal Documents

---

## Summary

I have reviewed the Supply Agreement (dated March 2, 2026), SOW No. 2 for Phase 2 Hall C (dated August 24, 2026), the Service Level Schedule, the Data Processing Addendum, and the email thread on Phase 2 freight and rigging (October 27 – November 3, 2026). I identify fifteen issues, prioritized below. The three most urgent are: (1) the unresolved Phase 1 rejection dispute, which likely means Vaigaind has lost its contractual right to reject but retains warranty claims; (2) the DPA's override of the Agreement's data-security liability carve-out, which caps data-breach recovery at 12 months of fees; and (3) the combination of the consequential-damages waiver, the 12-month fee cap, and minimal service credits, which leaves Vaigaind substantially exposed for the core risk of a cooling failure in a live data hall.

---

## Issue 1 – Phase 1 CDU Rejection: Deemed Acceptance Under Section 7.3

**Where:** SOW No. 2, Recital C; Supply Agreement § 7.3, § 7.5, § 9.1.

**Facts.** Phase 1 CDUs were Delivered June 8, 2026. Customer gave written notice of nonconformity (leaking quick-disconnect couplings) on July 10, 2026 – 32 days after Delivery. Section 7.3 allows only 20 days; absent timely notice, Products are "deemed accepted." Supplier has rejected the notice as untimely. The dispute is unresolved.

**Why it matters.**

- Vaigaind has almost certainly lost its right to reject under § 7.3. The 20-day window is unambiguous, and 32 days is 12 days late.
- However, § 7.5 provides that acceptance "does not waive Customer's rights under Section 9." The product warranty in § 9.1 runs 36 months from the *later* of Delivery and completion of commissioning. If commissioning was completed on or before June 8, 2026, the warranty expires June 8, 2029. If commissioning was after delivery, the warranty runs from that later date. Vaigaind should still be able to invoke the warranty for the leaking couplings.
- The same coupling model (TTS-QDC-100) is ordered in Phase 2 (192 sets, SOW No. 2 § 3.1, Item 4). If the Phase 1 leakage is a design or manufacturing defect, Phase 2 is at risk of the same failure.
- The dispute is now a relationship and leverage issue. Proceeding with Phase 2 while Phase 1 is unresolved weakens Vaigaind's negotiating position and could compound exposure if Phase 2 couplings also leak.

**Recommendation.**

1. Confirm the Phase 1 commissioning date to calculate the exact warranty expiry. Request SOW No. 1 (not in the folder) to verify.
2. Send a formal letter to Trugeith asserting the § 9.1 warranty claim for the Phase 1 couplings, expressly reserving rights, and requesting repair or replacement under § 9.3. Do not concede that § 7.3 bars the warranty claim.
3. Before Milestone M2 (January 18, 2027 delivery of Phase 2 products), require Trugeith to provide a written explanation of the Phase 1 root cause and the corrective action taken for the Phase 2 coupling batch. Consider adding a specific commissioning test for Phase 2 couplings beyond what § 8.1(b) already requires (leak inspection under design flow).
4. Evaluate whether to condition further Phase 2 progress (e.g., M3 installation) on resolution of the Phase 1 claim, or at minimum raise it in the weekly project-manager calls.

---

## Issue 2 – DPA Caps Data-Breach Liability, Overriding the Agreement's Carve-Out

**Where:** DPA § 8.2; Supply Agreement § 12.2, § 12.3(b); Supply Agreement § 1.4 (order of precedence).

**Facts.** Agreement § 12.3(b) excludes "breach of Section 14 (Confidentiality and Data Security)" from both the consequential-damages waiver and the liability cap. However, DPA § 8.2 states: "Notwithstanding Section 12.3(b) of the Agreement, each Party's aggregate liability arising out of or relating to this Addendum or any Security Incident … is subject to the limitation of liability in Section 12.2 of the Agreement." Under § 1.4, the DPA has first precedence "as to Personal Data only."

**Why it matters.**

- The DPA deliberately overrides the Agreement's uncapped treatment of data-security breaches. If Trugeith suffers a Security Incident affecting Vaigaind's employees, badge-access records, tenant contacts, and alarm-routing data (all within scope per DPA §§ 2.2–2.3), Vaigaind's recovery is capped at 12 months of fees.
- In the early months of Phase 2, 12 months of fees could be as low as the Phase 2 Remote Monitoring fees ($1,850 × 6 CDUs × 12 = $133,200) plus any Phase 1 monitoring fees. That is a fraction of the cost of a data breach affecting tenants, regulatory notification, credit monitoring, and forensics.
- The DPA does have a reimbursement provision (§ 5.5) for Security Incident costs "to the extent caused by Supplier's or its Sub-processors' breach of this Addendum," but § 8.2 caps even that recovery.

**Recommendation.**

- Negotiate to delete or narrow DPA § 8.2. At minimum, carve out from the cap any Security Incident caused by Supplier's gross negligence or willful misconduct (which § 12.3(c) already excludes from the cap generally, but § 8.2's "notwithstanding" language may swallow that too).
- Alternatively, raise the cap for DPA claims to a fixed dollar amount (e.g., $5 million or the cyber liability insurance limit in Agreement § 11(e), which is $10 million).
- Confirm that Trugeith's $10 million cyber liability policy (Agreement § 11(e)) is in place and that Vaigaind is named as an additional insured or loss payee for data-breach claims. The Agreement only requires additional-insured status on the general liability policy (§ 11, final sentence), not the cyber policy.

---

## Issue 3 – Liability Cap and Consequential Damages Waiver Inadequate for Data Center Risk

**Where:** Supply Agreement §§ 12.1, 12.2; SLS §§ 5.1–5.4.

**Facts.**

- § 12.1 excludes all indirect, incidental, consequential, special, and punitive damages, including lost profits.
- § 12.2 caps aggregate liability at fees paid or payable in the 12 months preceding the claim.
- The SLS service credits (the primary remedy for cooling failures) max out at 100% of the Monthly Remote Monitoring Fee per loop (SLS § 5.1), with a monthly aggregate cap of 100% of the total Monthly Remote Monitoring Fee (SLS § 5.4). For Phase 2, that is $1,850 × 6 = $11,100 per month.

**Why it matters.**

- Vaigaind is a colocation operator. The principal risk of a cooling failure is damage to tenant IT equipment, SLA breaches to tenants, and business-interruption claims. All of these are consequential damages, which § 12.1 excludes.
- The service credits are a price adjustment on the monitoring fee – they do not compensate for the actual harm of a cooling outage. A 99.5% month (26 minutes of outage) triggers only a 50% credit ($5,550). A total loss of cooling for a month triggers a 100% credit ($11,100). Neither approaches the cost of a single damaged server rack or a tenant SLA penalty.
- The 12-month fee cap in § 12.2 will be low in the early years. If Phase 2 is delivered in January 2027, the "12 months preceding" a claim in, say, March 2027 would capture only a couple of months of monitoring fees plus the Phase 2 product/installation invoice (which was paid in January). The cap would be roughly $5.3 million (the SOW total) plus a few months of monitoring – but only if the product invoice counts as "fees paid or payable under this Agreement." If it does, the cap is adequate for the first year but will grow only as more SOWs are added.

**Recommendation.**

- This is the most structurally important issue in the deal. Vaigaind should consider:
  - (a) A super-cap for cooling-related failures (e.g., 3× the 12-month fee cap or a fixed dollar amount tied to the replacement cost of tenant equipment at risk).
  - (b) Carving out of the consequential-damages waiver any claim arising from a Cooling Outage that causes physical damage to tenant property (arguably a direct damage, but the line is blurry).
  - (c) Requiring Trugeith to maintain a specific "cooling failure" insurance policy or a performance bond for the Phase 2 installation.
- At minimum, ensure the SLS § 5.6 language ("without prejudice to Customer's other rights and remedies") is understood to preserve Vaigaind's right to claim direct damages (e.g., cost of emergency cooling, tenant equipment repair) outside the credit mechanism, subject to the § 12.2 cap.

---

## Issue 4 – Exclusivity Across All US and Canada Facilities

**Where:** Supply Agreement § 3.1; SOW No. 2 § 2.

**Facts.** Section 3.1 requires Customer to purchase *all* Covered Products for *all* Covered Sites exclusively from Supplier. SOW No. 2 § 2 defines "Covered Sites" as "all data center facilities owned, leased or operated by Customer or any of its Affiliates in the United States and Canada."

**Why it matters.**

- This is not limited to the Secaucus campus or even to Hall C. It covers every Vaigaind and Affiliate facility in two countries.
- The Term is 5 years plus automatic 5-year renewals (see Issue 5). Vaigaind could be locked in for 10, 15, or 20 years.
- The only escape valve is § 3.2: if Trugeith notifies Vaigaind it cannot supply within the SOW lead time, Vaigaind may procure from a third party "for the affected quantity only." This is narrow – it doesn't cover quality failures, price increases on future SOWs, or Trugeith's insolvency.
- Given the Phase 1 coupling issue, Vaigaind has early evidence that Trugeith's product quality may be below expectations. The exclusivity clause limits Vaigaind's ability to test alternatives.

**Recommendation.**

- Narrow "Covered Sites" to the Project Site (Secaucus campus) or to facilities where Trugeith Products are actually installed.
- Add a quality-based escape: if Trugeith fails to meet the Cooling Availability Service Level for a Chronic Failure (SLS § 9) or if a material warranty claim is unresolved for more than 60 days, Vaigaind may procure from a third party for the affected facility.
- If Trugeith will not move on exclusivity, at least ensure the auto-renewal notice window (Issue 5) is widened so Vaigaind can exit at the end of the Initial Term.

---

## Issue 5 – Auto-Renewal with a 30-Day Notice Window 9 Months Before Expiry

**Where:** Supply Agreement § 2.2.

**Facts.** The Agreement renews automatically for successive 5-year terms. To prevent renewal, a Party must give written notice "during the thirty (30) day period ending two hundred seventy (270) days before the expiration of the then-current Term." For the Initial Term (expiring March 2, 2031), the notice window is approximately June 5 – July 5, 2030.

**Why it matters.**

- The window is only 30 days long and opens roughly 9 months before the term ends. If Vaigaind's legal team misses it, the Agreement renews for another 5 years, and the exclusivity in § 3.1 continues.
- There is no reminder mechanism in the Agreement. The burden is entirely on Vaigaind to calendar and act.
- Combined with Issue 4 (broad exclusivity), a missed renewal notice is a significant business risk.

**Recommendation.**

- Negotiate to extend the notice window to 90 days and/or move it closer to the expiration date (e.g., "during the 90-day period ending 180 days before expiration").
- Internally, calendar the notice deadline immediately (June 5, 2030) with multiple reminders and assign ownership to a specific person.
- Consider adding a provision that if either Party fails to give timely non-renewal notice, the other Party may still prevent renewal by giving notice within 30 days after the original window closes (a "cure" period).

---

## Issue 6 – Full Product Price Due at Delivery, Before Installation

**Where:** SOW No. 2 § 7.2; Supply Agreement § 5.2, § 6.2.

**Facts.** SOW No. 2 § 7.2 provides that Supplier invoices the Phase 2 Products ($4,186,400) "upon Delivery." Delivery is DDP to the loading dock (SOW § 6.1). Risk of loss passes to Customer on Delivery (Agreement § 6.2), though it remains with Supplier until installation is complete if Supplier is installing. Payment terms are net 45 (Agreement § 5.3).

**Why it matters.**

- Vaigaind pays $4.19 million when the equipment arrives at the dock, roughly 3.5 months before Substantial Completion (M4, April 2, 2027) and 5 months before final documentation (M5, April 16, 2027).
- If the Phase 2 products have the same coupling defect as Phase 1, Vaigaind has already paid the full price and must rely on warranty remedies (§ 9.3: repair, replace, or refund) rather than simply withholding payment.
- The "risk of loss remains with Supplier until completion of installation" language in § 6.2 helps with physical damage during installation but does not address latent defects.

**Recommendation.**

- Negotiate to tie a portion of the product price (e.g., 20–30%) to Substantial Completion (M4) rather than Delivery. This is common in data center projects and aligns payment with performance.
- If Trugeith resists, at minimum ensure the § 5.3 dispute-withholding mechanism is used proactively: if Phase 2 couplings show the same leakage pattern during commissioning, withhold the disputed amount immediately with written notice.

---

## Issue 7 – Specifications Referenced but Not in the Folder

**Where:** SOW No. 2 § 3.2.

**Facts.** The Specifications are defined as "Supplier's product data sheets for each listed model, Revision 2026-04, together with Customer's Hall C Liquid Cooling Design Basis, Revision C, dated April 17, 2026." The Design Basis is referenced as Exhibit A but the SOW states it is "attached separately." Neither the data sheets nor the Design Basis is in the matter folder.

**Why it matters.**

- We cannot verify the technical requirements Vaigaind is purchasing against. The ±0.5°C supply temperature tolerance is stated in § 3.2, but the full load range, flow rates, pressure ratings, and other performance criteria are in the missing documents.
- The commissioning tests in SOW § 8.1 reference "the Specifications" and "the Design Basis." If those documents are ambiguous or incomplete, disputes over whether commissioning was passed become harder to resolve.
- The Phase 1 coupling failure may be traceable to a specification gap (e.g., no explicit requirement for dry-break verification under thermal cycling). Without the data sheets, we cannot assess this.

**Recommendation.**

- Request from the client: (a) the Design Basis (Exhibit A), (b) the Trugeith product data sheets Rev. 2026-04 for all six line items, and (c) SOW No. 1 in full.
- Review the data sheets for the TTS-QDC-100 coupling in particular, given the Phase 1 issue. Confirm whether the Phase 2 specification includes any additional testing or certification requirement for couplings.

---

## Issue 8 – SOW No. 1 Not in the Folder

**Where:** SOW No. 2, Recitals B and C.

**Facts.** SOW No. 1 is referenced but not provided. We do not have its delivery date, commissioning date, pricing, or specific terms.

**Why it matters.**

- We cannot confirm the Phase 1 commissioning date, which is needed to calculate the § 9.1 warranty expiry (Issue 1).
- We cannot verify whether SOW No. 1 had different or additional terms (e.g., different payment milestones, different specifications) that might affect the Phase 1 dispute.
- The Service Level Schedule applies to Phase 1 Products from their Service Commencement Date (SLS § 1.1). We don't know when that was.

**Recommendation.** Request SOW No. 1 from the client. Also request the Phase 1 commissioning report (required by Agreement § 7.2) and the Phase 1 notice of nonconformity and Trugeith's response.

---

## Issue 9 – Service Credits Are Inadequate as the Primary SLA Remedy

**Where:** SLS §§ 5.1–5.4; SOW No. 2 § 7.4.

**Facts.** The Monthly Remote Monitoring Fee for Phase 2 is $1,850 × 6 CDUs = $11,100. The maximum service credit for any month is 100% of that fee (SLS § 5.4). Even a total loss of cooling for an entire month yields a $11,100 credit.

**Why it matters.**

- For a colocation facility, the cost of a cooling failure is measured in tenant SLA penalties, equipment damage, and emergency mitigation – not in a $11,100 monitoring fee credit.
- SLS § 5.6 states credits are "without prejudice to Customer's other rights and remedies," which preserves warranty and termination claims. But in practice, the credit mechanism signals that the Parties view the monitoring fee as the measure of the service's value, not the value of the cooling itself.
- The Chronic Failure provision (SLS § 9) is the real teeth: it constitutes a material breach triggerable under Agreement § 15.1. But the threshold is high (3 months in 12, or 3 P1s from same root cause in 6 months).

**Recommendation.**

- This ties back to Issue 3. The structural fix is to increase the liability cap or add a super-cap for cooling failures.
- In the short term, ensure the SLS § 9 Chronic Failure threshold is understood and that Vaigaind's project team is tracking P1 Incidents and SLA misses in a way that would support a Chronic Failure declaration if the pattern emerges.
- Consider negotiating a "liquidated damages" provision for Cooling Outages that is separate from and in addition to the service credits, calibrated to a reasonable estimate of Vaigaind's actual loss per hour of outage.

---

## Issue 10 – Single-Day Delivery of All Phase 2 Products

**Where:** Email Thread, Message 1, § 1.2; SOW No. 2 § 6.3.

**Facts.** All Phase 2 Products (6 CDUs, 96 rear-door heat exchangers, 16 manifolds, 192 coupling sets, 16 leak detection kits, 1 spare parts kit) are scheduled for delivery on four trucks on January 18, 2027, within the 7:00 a.m. – 3:00 p.m. dock window.

**Why it matters.**

- The CDUs are 1.2 MW units – large, heavy equipment. Unloading and rigging six of them, plus 96 heat exchangers and all ancillary items, in 8 hours is aggressive.
- The route passes the live Phase 1 rows (Email Thread, Message 2, § 2.2). Any spill, drop, or incident in that corridor risks the Phase 1 equipment, which already has a known coupling issue.
- If any truck is delayed (traffic, mechanical failure, customs if applicable), the entire schedule compresses. The SOW does not provide for split deliveries.
- The SOW § 5.1 schedule shows M2 (Delivery) as a single date: January 18, 2027. There is no flexibility built in.

**Recommendation.**

- Confirm with the client's facilities team (Leo Fairbanks) that the single-day plan is realistic given the dock capacity, crane availability, and the path-of-travel constraints.
- If there is any risk of delay, consider negotiating a split delivery (e.g., CDUs on Day 1, heat exchangers and ancillaries on Day 2) via a change order under SOW § 11 / Agreement § 4.2.
- Ensure the method of procedure (due December 4, 2026 per Email Thread, Message 3, § 3.2) specifically addresses the proximity to live Phase 1 rows and includes contingency for a CDU rigging failure mid-move.

---

## Issue 11 – Order of Precedence Places SOW Last

**Where:** Supply Agreement § 1.4.

**Facts.** The precedence order is: (1) DPA (as to Personal Data), (2) Agreement body, (3) SLS, (4) SOW.

**Why it matters.**

- If a SOW term conflicts with the Agreement, the Agreement controls. This is the reverse of what many clients expect: they sign a SOW with specific project terms and assume those terms "override" the master agreement.
- For example, if a future SOW tried to extend the § 7.3 rejection period beyond 20 days, it would be ineffective unless it expressly identified § 7.3 and was signed by an authorized officer of each Party (per § 1.2). The SOW must "expressly identify the Section of this Agreement to be amended."
- SOW No. 2 § 1.1 states: "This SOW does not amend any Section of the Agreement." So all SOW terms are subordinate.

**Recommendation.**

- Be aware that any project-specific protection Vaigaind wants (e.g., extended rejection period, different payment terms, additional warranties) must be drafted as an express amendment to the Agreement under § 1.2, not merely as a SOW term.
- For Phase 2, if the client wants a longer rejection window given the Phase 1 experience, it would need to amend § 7.3 of the Agreement (or add a SOW-specific provision that expressly identifies § 7.3 as amended).

---

## Issue 12 – Hackensack Rigging Certificate of Insurance Not Confirmed

**Where:** Email Thread, Message 2, § 2.3(b); Message 3, § 3.1.

**Facts.** Vaigaind's consent to use Hackensack Rigging was conditional on Trugeith providing "an updated certificate of insurance showing Hackensack Rigging's general liability coverage for work at the Project Site." Marcus committed to sending it by November 13, 2026. No confirmation of receipt is in the folder.

**Why it matters.**

- The consent is conditional. If the COI was not delivered, the consent may not be effective, and Hackensack Rigging's presence on site on January 18 could be a breach of § 8.4 (no subcontracting without consent).
- Even if the COI was delivered, we should verify the coverage limits are adequate for the rigging work (heavy equipment moves in a live data hall).

**Recommendation.** Confirm with the client whether the updated COI was received by November 13, 2026. If not, send a reminder to Trugeith and flag that the consent remains conditional. Verify the COI shows adequate general liability limits (at least $5 million, consistent with Agreement § 11(a)) and names Vaigaind as an additional insured.

---

## Issue 13 – Method of Procedure Not in the Folder

**Where:** Email Thread, Message 2, § 2.2(c); Message 3, § 3.2.

**Facts.** Trugeith committed to submit the rigging method of procedure through Vaigaind's change-management process by December 4, 2026. It is not in the folder.

**Why it matters.**

- The method of procedure must address the path of travel past live Phase 1 rows, floor loading, and safety. Without reviewing it, we cannot confirm it is adequate.
- SOW § 6.3 requires work in the Phase 2 Area to follow Vaigaind's change-management and method-of-procedure requirements for the live Phase 1 rows. If the MoP is deficient and an incident occurs, Vaigaind could face arguments that it approved an inadequate plan.

**Recommendation.** Request the method of procedure from the client. Review it for: (a) floor-protection specifications, (b) CDU skid weights vs. Design Basis floor loading, (c) emergency stop procedures, and (d) coordination with Phase 1 operations.

---

## Issue 14 – "Two-Hour Drive" Spare Parts Standard Is Vague

**Where:** SLS § 4.5.

**Facts.** Supplier must maintain critical spare parts "at or within a two-hour drive of the Project Site."

**Why it matters.**

- "Two-hour drive" is not defined. Is it under normal traffic? In winter conditions? By the fastest route or the route actually available? Secaucus is in the NJ Turnpike corridor; two hours in normal traffic could be significantly more in winter or during an incident (when roads may be congested).
- The P1 on-site attendance requirement is 4 hours (SLS § 4.2). If the spare parts depot is at the outer edge of the two-hour drive, and the rigging/access to the hall takes additional time, the 4-hour on-site target could be at risk during winter months.

**Recommendation.** Negotiate to specify the depot location (or require it to be within a stated mileage/radius) and to clarify that the two-hour standard is measured under normal winter driving conditions. Alternatively, require Trugeith to identify the specific depot and confirm it by name and address in the SLS or a side letter.

---

## Issue 15 – 30-Day Cure Period for Material Breach May Be Too Long

**Where:** Supply Agreement § 15.1.

**Facts.** Either Party may terminate for material breach only if the breaching Party "fails to cure the breach within thirty (30) days after written notice."

**Why it matters.**

- In a live data center, a material breach (e.g., failure to respond to a P1 Incident, failure to maintain the monitoring platform) could cause ongoing harm for 30 days before Vaigaind can terminate.
- The SLS escalation path (§ 10.2) and Chronic Failure provision (§ 9) provide some interim protection, but they do not shorten the cure period.
- The force majeure termination right (Agreement § 16) requires 60 days of continuation – even longer.

**Recommendation.**

- Negotiate a shorter cure period for breaches that affect cooling availability or data security (e.g., 5 business days), with the 30-day period applying to other breaches.
- Alternatively, add a provision that if a P1 Incident remains unresolved beyond the § 4.2 resolution time (8 hours) for more than 48 consecutive hours, it constitutes an incurable material breach (no cure period).

---

## Items Requiring Further Context from the Client

| # | Item | Why Needed |
|---|---|---|
| A | SOW No. 1 (full text) | Verify Phase 1 delivery date, commissioning date, and terms; calculate warranty expiry |
| B | Phase 1 commissioning report | Confirm commissioning date for § 9.1 warranty calculation |
| C | Phase 1 notice of nonconformity (July 10, 2026) and Trugeith's response | Assess the strength of Vaigaind's position in the Phase 1 dispute |
| D | Design Basis (Exhibit A to SOW No. 2) | Verify technical specifications, floor loading, and design parameters |
| E | Trugeith product data sheets, Rev. 2026-04 (all six models) | Verify specifications; assess Phase 2 coupling risk |
| F | Confirmation whether Hackensack Rigging COI was received by Nov. 13, 2026 | Verify consent conditions were satisfied |
| G | Method of procedure (due Dec. 4, 2026) | Review for adequacy re: live Phase 1 rows |
| H | Current status of Phase 1 couplings – have they been repaired? Is Phase 1 in service? | Assess operational risk during Phase 2 rigging |
| I | Vaigaind's tenant SLA structure (what does Vaigaind owe tenants for cooling failure?) | Calibrate the adequacy of the liability cap and service credits |

---

## Priority Summary for Client Discussion

| Priority | Issue | Key Action |
|---|---|---|
| **1** | Phase 1 rejection / warranty (Issue 1) | Assert warranty claim; require root-cause explanation before M2 |
| **2** | DPA liability cap override (Issue 2) | Negotiate DPA § 8.2; confirm cyber insurance |
| **3** | Liability cap / consequential damages (Issues 3, 9) | Negotiate super-cap or liquidated damages for cooling failures |
| **4** | Exclusivity + auto-renewal (Issues 4, 5) | Narrow Covered Sites; widen renewal notice window; calendar deadline |
| **5** | Payment at delivery (Issue 6) | Negotiate milestone-based payment |
| **6** | Missing documents (Issues 7, 8, 12, 13) | Request from client; verify before M2 |
| **7** | Delivery logistics (Issues 10, 14, 15) | Confirm MoP, COI, and depot location; consider split delivery |