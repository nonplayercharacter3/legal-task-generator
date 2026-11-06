# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Vaigaind Data Halls, LLC / Trugeith Thermal Systems, Inc. – Review of Deal Documents (SOW No. 2, Phase 2)

---

## Summary

I have reviewed the Supply Agreement (March 2, 2026), SOW No. 2 for Hall C Phase 2 (August 24, 2026), the Service Level Schedule, the Data Processing Addendum, and the October–November 2026 email thread on Phase 2 freight and rigging. I identify **twelve issues**, prioritized below. The three most consequential are: (1) the Phase 1 coupling dispute, where Vaigaind's rejection notice appears time-barred but a warranty claim likely survives; (2) a direct conflict between the DPA and the Agreement on the liability cap for data breaches; and (3) the combination of the exclusivity clause and the broad "Covered Sites" definition, which locks Vaigaind into Trugeith for all U.S. and Canadian facilities for the full Term.

Two referenced documents are missing from the folder (SOW No. 1 and the Design Basis, Exhibit A to SOW No. 2). I flag where their absence limits my analysis.

---

## Issue 1 – Phase 1 Rejection Notice Appears Untimely; Warranty Claim Likely Survives

**Where:** Supply Agreement § 7.3 (20-day rejection window); § 7.5 (acceptance does not waive § 9); § 9.1 (36-month warranty); SOW No. 2, Recital C.

**Facts.** Phase 1 CDUs were Delivered on June 8, 2026. Vaigaind issued its notice of nonconformity (leaking quick-disconnect couplings) on July 10, 2026 — **32 days** after Delivery. Section 7.3 requires notice within 20 days. Trugeith has rejected the notice as untimely. The parties have reserved their positions (SOW No. 2, Recital C).

**Why it matters.** On the plain language, Trugeith is correct that the § 7.3 rejection is time-barred. However, § 7.5 states that "Acceptance of Products does not waive Customer's rights under Section 9." The leaking couplings are a defect in materials or workmanship covered by the 36-month product warranty in § 9.1(b). Vaigaind's remedy under § 9.3 is repair or replacement at Supplier's cost (or a refund if Supplier fails to act within a reasonable time). This is substantively similar to the § 7.4 remedy, but the time window is 36 months rather than 20 days.

**Recommendation.**
- Advise the client that its best route is a **warranty claim under § 9**, not a § 7.3 rejection. The § 7.3 window has passed, but § 7.5 expressly preserves § 9 rights.
- Send Trugeith a formal warranty claim notice under § 9.3 identifying the leaking couplings as a defect in materials/workmanship, demanding repair or replacement at Trugeith's cost.
- Be mindful that the couplings are also listed as Phase 2 Products (SOW No. 2, § 3.1, Item 4: 192 TTS-QDC-100 sets). If the same model is being shipped for Phase 2, Vaigaind should require Trugeith to confirm the Phase 2 couplings incorporate a corrected design before delivery, and should consider adding a specific commissioning test for coupling integrity (SOW No. 2, § 8.1(b) already requires a leak inspection of all QDCs under design flow, which should catch this).
- **Open item:** I do not have SOW No. 1 in the folder. If SOW No. 1 contains a different or shorter warranty period, or different commissioning terms, that could affect the analysis. Please confirm whether SOW No. 1 is available.

---

## Issue 2 – DPA Re-Imposes the Liability Cap for Data Breaches, Overriding the Agreement's Carve-Out

**Where:** Supply Agreement § 12.2 (cap = 12 months of fees); § 12.3(b) (cap does not apply to breach of § 14); DPA § 8.2 ("Notwithstanding Section 12.3(b) of the Agreement, each Party's aggregate liability arising out of or relating to this Addendum or any Security Incident … is subject to the limitation of liability in Section 12.2"); Supply Agreement § 1.4 (order of precedence: DPA first, "as to Personal Data only").

**Why it matters.** The Agreement carves out confidentiality/data-security breaches from the liability cap (§ 12.3(b)). The DPA then expressly negates that carve-out for anything "arising out of or relating to this Addendum or any Security Incident." Because the DPA has first precedence "as to Personal Data only" (§ 1.4), the net effect is:

- **Personal Data breach (e.g., tenant or employee data):** capped at 12 months of fees.
- **Non-Personal Data confidentiality breach (e.g., facility layouts, cooling designs, pricing):** the § 12.3(b) carve-out still applies, so no cap.

For a colocation operator, a breach of tenant or employee Personal Data could trigger regulatory fines (NJ DPA, NY SHIELD Act), tenant indemnification claims, notification costs, and credit-monitoring obligations. Twelve months of fees under SOW No. 2 alone is approximately $5.4 million ($5,313,450 fixed price + ~$133K in monitoring fees). That may be insufficient to cover a serious breach, particularly if multiple tenants are affected.

**Recommendation.**
- Flag this to the client as a **material risk-allocation gap**. The DPA cap undermines the protection the Agreement's § 12.3(b) was designed to provide.
- In discussions with Trugeith, seek to either (a) raise the DPA cap to a fixed dollar amount (e.g., $10 million, matching the cyber insurance requirement in Agreement § 11(e)), or (b) carve Security Incidents caused by Supplier's gross negligence or willful misconduct out of the DPA cap (consistent with § 12.3(c)).
- Note that the $10 million cyber liability insurance requirement (Agreement § 11(e)) provides some backstop, but insurance is not a guarantee of recovery and does not cover Vaigaind's own downstream tenant obligations.

---

## Issue 3 – Exclusivity Clause Combined with Broad "Covered Sites" Definition Creates a Multi-Facility Lock-In

**Where:** Supply Agreement § 3.1 (exclusive purchasing of all Covered Products for all Covered Sites); SOW No. 2 § 2 (defines "Covered Sites" as "all data center facilities owned, leased or operated by Customer or any of its Affiliates in the United States and Canada"); Supply Agreement § 1.1(d) ("Covered Sites" has the meaning given in the applicable SOW).

**Why it matters.** Vaigaind is contractually barred from soliciting, purchasing, or installing liquid-cooling equipment from any third party at **any** of its U.S. or Canadian facilities for the entire Term (5 years, auto-renewing for successive 5-year terms). This is not limited to the Project Site or Hall C. If Trugeith's products prove unreliable (the Phase 1 coupling issue is an early warning), Vaigaind cannot switch suppliers at its other facilities without breaching the Agreement. The only express escape is § 3.2 (Supplier notifies it cannot meet lead times), which is narrow.

**Recommendation.**
- Discuss with the client whether the exclusivity scope is commercially acceptable. If the client has other facilities with different cooling requirements or existing relationships with other vendors, this clause may be overbroad.
- If the client wishes to narrow it, propose limiting "Covered Sites" to the Project Site (or to facilities where Trugeith equipment is actually installed) rather than all U.S./Canadian facilities.
- At minimum, ensure the client's deal team understands that this commitment runs for 5 years (potentially 10+ with renewal) and covers all Affiliates.

---

## Issue 4 – Service Credits Are Modest Relative to Downstream Colocation Risk

**Where:** Service Level Schedule § 5.1 (credits based on Monthly Remote Monitoring Fee per loop); § 5.4 (monthly maximum = 100% of Monthly Remote Monitoring Fee); SOW No. 2 § 7.4 ($1,850/CDU/month × 6 CDUs = $11,100/month for Phase 2); Supply Agreement § 12.1 (consequential damages excluded).

**Why it matters.** The maximum monthly service credit for Phase 2 is **$11,100** (100% of the monitoring fee). If a cooling outage causes Vaigaind to breach its own SLAs with colocation tenants — which in this market can carry liquidated damages of $50K–$500K+ per incident, or even termination rights — the service credit from Trugeith covers a small fraction of Vaigaind's actual exposure. The consequential damages exclusion (§ 12.1) prevents Vaigaind from recovering those downstream losses from Trugeith.

**Recommendation.**
- This is a structural risk the client should understand before proceeding. The service credit regime compensates for the reduced value of the monitoring service, not for the business impact of a cooling failure.
- Options to discuss with the client:
  - Negotiate a higher credit ceiling or a super-cap for P1 Incidents (e.g., credits for P1 outages calculated as a percentage of the product price, not just the monitoring fee).
  - Ensure the client's tenant agreements allocate cooling-failure risk appropriately (e.g., force majeure or utility-failure carve-outs in tenant SLAs).
  - Confirm that the client's own insurance program (property/business interruption) responds to cooling-failure scenarios.
- The Chronic Failure provision (SLS § 9) gives Vaigaind a termination right after repeated underperformance, which is a useful backstop but does not address a single severe outage.

---

## Issue 5 – Auto-Renewal with a Long and Narrow Notice Window

**Where:** Supply Agreement § 2.1 (Initial Term = 5 years from March 2, 2026, i.e., through ~March 2, 2031); § 2.2 (auto-renews for successive 5-year terms; non-renewal notice must be given during the 30-day period ending 270 days before expiration).

**Why it matters.** To prevent the first auto-renewal (which would extend the Agreement to ~March 2, 2036), Vaigaind must deliver written notice during a **30-day window that closes approximately June 5, 2030** (270 days before March 2, 2031). If the client misses that window, it is locked in for another 5 years — and the exclusivity obligation (Issue 3) continues. Combined with the broad Covered Sites definition, a missed notice date has significant commercial consequences.

**Recommendation.**
- Enter the non-renewal notice deadline (and a reminder 90 days prior) into the client's contract-management calendar now.
- Consider whether the 270-day lead time is reasonable or whether it should be shortened in any renegotiation.

---

## Issue 6 – 79% of SOW No. 2 Price Is Due at Delivery, Before Installation or Commissioning

**Where:** SOW No. 2 § 7.1 (Products: $4,186,400; Installation: $912,750; Commissioning/training/docs: $214,300; Total: $5,313,450); § 7.2 (Products invoiced upon Delivery; Installation in two installments at M3 and M4; Commissioning at M5); Supply Agreement § 5.3 (payment in 45 days).

**Why it matters.** Vaigaind will owe $4,186,400 (≈79% of the total) within 45 days of the January 18, 2027 delivery — before any installation, pressure testing, or commissioning has occurred. If the Phase 2 products then fail commissioning (as the Phase 1 couplings failed in service), Vaigaind has already paid the bulk of the price and must rely on the § 7.4 remedy (repair/replace or refund) and the § 9 warranty. The 20-day rejection window (§ 7.3) will start running from Delivery, creating the same timing pressure that caused the Phase 1 dispute.

**Recommendation.**
- Ensure the client's receiving and inspection team is fully prepared to inspect and test the Phase 2 products within 20 days of the January 18, 2027 delivery. Given the Phase 1 experience with couplings, a focused inspection of all 192 QDC sets at the dock is advisable.
- Consider negotiating a payment milestone for products (e.g., 50% at delivery, 50% at Substantial Completion) in any future SOW or change order. For SOW No. 2 as drafted, this is not available without a change order under § 4.2.
- The client should also confirm its cash-flow plan accommodates a ~$4.2M payment in late February / early March 2027.

---

## Issue 7 – Missing Documents: SOW No. 1 and the Design Basis (Exhibit A)

**Where:** SOW No. 2, Recitals B–C (reference SOW No. 1); SOW No. 2 § 3.2 and page 3 (Design Basis "attached separately" as Exhibit A).

**Why it matters.**
- **SOW No. 1:** I cannot verify Phase 1 pricing, schedule, commissioning terms, or whether it contains any terms that differ from SOW No. 2. This limits my ability to assess the Phase 1 dispute (Issue 1) fully and to confirm that the SLS applies to Phase 1 products as intended (SLS § 1.1).
- **Design Basis (Exhibit A):** This document contains the technical specifications against which the Phase 2 products will be judged (SOW No. 2 § 3.2), including the load range for the ±0.5°C supply temperature tolerance. Without it, I cannot confirm that the commissioning tests in SOW No. 2 § 8.1 adequately verify conformance.

**Recommendation.**
- Request both documents from the client. The Design Basis in particular should be reviewed by the client's engineering team to confirm the specifications are appropriate and that the commissioning test plan (SOW No. 2 § 8.1) maps to every critical parameter in the Design Basis.

---

## Issue 8 – Consequential Damages Exclusion Is Broad and One-Way in Effect

**Where:** Supply Agreement § 12.1 (mutual exclusion of indirect, incidental, consequential, special, punitive damages and lost profits); § 12.2 (cap at 12 months of fees).

**Why it matters.** Although the exclusion is mutual in form, in practice it operates primarily against Vaigaind. Trugeith's main revenue is the product and service fees; its "lost profits" from a terminated contract are modest. Vaigaind's "lost profits" or consequential damages from a cooling failure — tenant SLA penalties, lost revenue, reputational harm, regulatory exposure — are potentially enormous. The cap (§ 12.2) further limits Vaigaind's recovery to 12 months of fees.

**Recommendation.**
- This is standard in equipment supply agreements and difficult to change. The practical mitigations are:
  - Ensure the client's tenant agreements and insurance program address the downstream risk (see Issue 4).
  - The § 12.3 exclusions (indemnification, § 14 breach [partially, see Issue 2], gross negligence/fraud, undisputed fees) provide some carve-outs. Confirm the client understands these are the only scenarios in which the cap and consequential damages exclusion do not apply.

---

## Issue 9 – Rigging Route Passes Live Phase 1 Rows: Operational and Liability Risk

**Where:** SOW No. 2 § 6.3 (work must follow change-management and method-of-procedure requirements for live Phase 1 rows); Email Thread, Message 2 § 2.2 (route from dock to staging passes live Phase 1 rows; requires floor protection, weight verification, and MoP).

**Why it matters.** The Phase 2 CDU moves (6 units, each a 1.2 MW in-row CDU on a skid) will traverse the aisle past the live Phase 1 CDUs. If a rigging incident damages Phase 1 equipment or disrupts Phase 1 cooling, the following issues arise:
- Who bears the cost? Under SOW No. 2 § 4.1(b), rigging is a Phase 2 Service, and Supplier is responsible for its subcontractors (Agreement § 8.4). So Trugeith should be liable for damage caused by its rigging operations.
- However, if the Phase 1 damage is related to the existing coupling defect (Issue 1), there could be a dispute over causation.
- The method of procedure (due December 4, 2026 per Email Thread, Message 3 § 3.2) is the critical risk-mitigation document. It should address floor loading, path clearance, emergency stop procedures, and coordination with Phase 1 operations.

**Recommendation.**
- Confirm that the MoP is submitted by December 4, 2026 and is reviewed by the client's facilities and safety teams before approval.
- Ensure the MoP includes a specific provision for damage to Phase 1 equipment, clarifying that Trugeith (and its rigging subcontractor) bears all cost of repair and any resulting cooling disruption.
- Verify that Hackensack Rigging's certificate of insurance (due November 13, 2026 per Email Thread, Message 3 § 3.1) names Vaigaind as an additional insured or confirms adequate coverage for operations at the Project Site.

---

## Issue 10 – SLS Section 4.5 Spare Parts Location: Confirm Feasibility

**Where:** Service Level Schedule § 4.5 (Supplier must maintain critical spare parts "at or within a two-hour drive of the Project Site"); § 4.2 (P1 on-site attendance within 4 hours; P2 within 8 hours).

**Why it matters.** The Project Site is in Secaucus, NJ. A two-hour drive radius covers most of the NYC metro area, northern NJ, southern NY, and parts of PA and CT. This is feasible for a supplier with a regional warehouse, but if Trugeith's nearest parts depot is at the edge of that radius, the 4-hour P1 on-site attendance target becomes tight (travel + diagnosis + parts retrieval + repair).

**Recommendation.**
- Ask Trugeith to confirm in writing the location of its Phase 2 spare parts stock and the expected travel time to the Project Site.
- Verify that the spare parts list (pumps, controllers, sensors, seals, QDC couplings per SLS § 4.5) is sufficient for the Phase 2 equipment models. Given the Phase 1 coupling issue, confirm that the spare QDC couplings in stock are the corrected design.

---

## Issue 11 – DPA Sub-Processor List and Change Mechanism

**Where:** DPA § 6.1 (authorized sub-processors in Annex 2); § 6.2 (30-day prior notice for new sub-processors; Customer may object on reasonable data-protection grounds).

**Why it matters.** Annex 2 lists three sub-processors: Northwall Cloud Services (hosting, Ashburn VA / Columbus OH), Relayline Communications (SMS/voice alarms), and Kestrel Desk Software (ticketing). All are U.S.-based, consistent with § 3.5 (data stored/processed only in the U.S.). The 30-day objection mechanism in § 6.2 is reasonable but note that if an objection is not resolved, the DPA simply says "Supplier shall not use that Sub-processor" — it does not provide a termination right or a service-credit remedy if Supplier is then unable to perform.

**Recommendation.**
- Low risk at present. Monitor the sub-processor list. If Trugeith proposes a new sub-processor (e.g., a cloud migration), the client should evaluate the data-protection implications before the 30-day window closes.
- Consider adding a provision that if Supplier cannot perform because a sub-processor change is blocked, the affected service levels are suspended rather than breached (or, conversely, that Supplier remains fully responsible).

---

## Issue 12 – Drafting Imprecision in SOW No. 2 § 4.1(b) Cross-Reference

**Where:** SOW No. 2 § 4.1(b) ("receipt, unloading and rigging … in accordance with Section 6.1 of the Agreement").

**Why it matters.** Section 6.1 of the Agreement addresses Delivery terms (DDP) and states that Supplier is responsible for "freight, unloading and rigging to the designated staging area, unless the applicable SOW provides otherwise." The more specific rigging obligations (5-business-day notice, truck count, rigging plan) are in SOW No. 2 § 6.2. The cross-reference in § 4.1(b) to "Section 6.1 of the Agreement" is not wrong, but it omits the SOW's own § 6.2, which contains the operational detail. In the email thread, both parties are working from SOW § 6.2, so this is not creating confusion in practice.

**Recommendation.**
- Minor. If a change order is negotiated for any other reason, correct the cross-reference to "Section 6.1 of the Agreement and Section 6.2 of this SOW."

---

## Items Requiring Further Context from the Client

| # | Item | Reason |
|---|------|--------|
| A | **SOW No. 1** (Phase 1) | Needed to verify Phase 1 terms, pricing, commissioning date, and whether the SLS Service Commencement Date for Phase 1 has passed. Directly relevant to Issue 1. |
| B | **Design Basis, Exhibit A to SOW No. 2** (Hall C Liquid Cooling Design Basis, Rev. C, April 17, 2026) | Needed to verify technical specifications and confirm commissioning test coverage. Relevant to Issues 1 and 7. |
| C | **Client's tenant SLA structure** for Hall C | Needed to assess the downstream financial exposure from a cooling outage (Issue 4). |
| D | **Status of Hackensack Rigging COI** (due November 13, 2026) | Confirm receipt and adequacy (Issue 9). |
| E | **Status of Method of Procedure** (due December 4, 2026) | Confirm submission and approval through change management (Issue 9). |
| F | **Client's insurance program** (property, business interruption, cyber) | To confirm coverage for cooling-failure scenarios and data breach (Issues 4, 8). |

---

## Suggested Priority for Client Discussion

| Priority | Issue | Action |
|----------|-------|--------|
| **1** | Phase 1 warranty claim (Issue 1) | Send formal § 9.3 warranty notice to Trugeith; require corrected QDC design for Phase 2 |
| **2** | DPA liability cap (Issue 2) | Raise in next negotiation; seek higher cap or gross-negligence carve-out |
| **3** | Exclusivity / Covered Sites (Issue 3) | Confirm commercial acceptance; consider narrowing if client has other facilities |
| **4** | Service credit adequacy (Issue 4) | Review tenant SLA exposure; consider negotiating P1-specific credits |
| **5** | Auto-renewal calendar (Issue 5) | Enter deadline (~June 2030) in contract management system |
| **6** | Payment timing / inspection readiness (Issue 6) | Prepare receiving team for 20-day inspection window; confirm cash flow |
| **7** | Rigging / live-row risk (Issue 9) | Track MoP submission (Dec 4) and COI (Nov 13); review MoP before approval |
| **8** | Missing documents (Issue 7) | Request SOW No. 1 and Design Basis from client |