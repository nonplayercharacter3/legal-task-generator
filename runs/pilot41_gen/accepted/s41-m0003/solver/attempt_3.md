# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Nonaisk Event Rentals / Zouduth Logistics – MSA, DPA, and Related Documents: Issue List for Markup and Client Call

---

## Issues Requiring Client Decision

These go to fundamental risk allocation and commercial posture. I'd recommend raising them on the client call before we finalize our markup positions.

### 1. Customer Indemnity Is a Blanket Guarantee of the Rental Inventory — Regardless of Provider Fault

**Where:** MSA § 10.2; compare Term Sheet § 8.2.

**Issue:** The term sheet contemplated mutual negligence-based indemnification ("Each party will indemnify the other against third-party claims arising from its own negligence or willful misconduct"). The MSA instead requires Customer to indemnify Provider for *all* third-party claims "arising from or relating to the Rental Inventory," expressly including bodily injury and property damage "regardless of whether caused in part by Provider's installation or handling of the Rental Inventory."

**Why it matters:** Nonaisk rents furniture to events with hundreds of attendees. If a staging platform collapses because Zouduth's crew misinstalled it, a guest is injured, and the guest sues both Nonaisk and Zouduth — under § 10.2, Nonaisk must indemnify Zouduth for Zouduth's own share of the judgment. Nonaisk effectively becomes the insurer of its own inventory for the entire relationship, with no fault requirement.

**Recommended fix:** Strike the "regardless of whether caused in part by Provider's installation or handling" language. Limit Customer's indemnity to claims arising from the inherent nature or pre-existing condition of the Rental Inventory, or to Customer's own negligence. Restore the mutual negligence standard from the term sheet for all other claims.

**Client decision needed:** Nonaisk should confirm whether it is willing to accept any version of a blanket inventory indemnity, or whether it will hold the line on fault-based allocation. This is the single largest financial exposure in the deal.

---

### 2. Provider Can Assign to Any Successor Without Consent — Including a Competitor

**Where:** MSA § 15.2; compare Term Sheet § 7.1.

**Issue:** The term sheet provided that neither party may assign without consent, except to a successor that is *not* a Competitor. The MSA inverts this: Customer cannot assign without Provider's consent (§ 15.1), but Provider may assign freely to any Affiliate or any successor "whether by merger, sale of stock, sale of assets or otherwise" with no consent right and no competitor restriction (§ 15.2).

**Why it matters:** The MSA defines "Competitor" (§ 1.2) as any entity in the event furniture rental business. If Zouduth is acquired by or merges with a competitor of Nonaisk, that competitor would step into the agreement with full access to Nonaisk's Customer Data (client lists, pricing, venue access information, booking patterns) under the existing confidentiality and data protection terms. Nonaisk has no exit right triggered by the assignment.

**Recommended fix:** Restore the term sheet structure: mutual consent required for assignment, with a carve-out for assignment to a non-Competitor successor. Alternatively, if Provider resists, at minimum add (a) a competitor restriction, and (b) a Customer termination right (without penalty) if Provider assigns to a Competitor.

**Client decision needed:** Confirm Nonaisk's comfort level. If Zouduth is a growth-stage company likely to be acquired, this is a live risk, not a theoretical one.

---

### 3. Customer's Indemnity Obligation Is Uncapped; Provider's Is Capped

**Where:** MSA § 11.1, § 11.3(c); compare Term Sheet § 8.3.

**Issue:** The term sheet stated that limitations of liability "will be mutual." In the MSA, the 12-month-fee cap (§ 11.1) applies to both parties, but § 11.3(c) carves "Customer's obligations under Section 10.2" out of the cap. Provider's indemnity under § 10.1 has no such carve-out and remains subject to the cap.

**Why it matters:** Combined with Issue 1, Nonaisk faces uncapped exposure for Rental Inventory claims (including those caused by Provider's own negligence), while Zouduth's indemnity for its negligence, IP infringement, or vehicle accidents is capped at roughly $1.85 million (12 months of fees). In a serious event injury claim, the gap between uncapped Customer exposure and capped Provider recovery could be millions of dollars.

**Recommended fix:** If Issue 1 is resolved to a fault-based standard, § 11.3(c) should be deleted so that both parties' indemnities are subject to the same cap. If Nonaisk accepts any form of broad inventory indemnity, it should at minimum be subject to the cap, or the cap should be elevated for indemnity obligations (e.g., 2× or 3× annual fees).

**Client decision needed:** Tied directly to Issue 1. Nonaisk should decide its maximum acceptable uncapped exposure.

---

## High-Priority Drafting Issues

### 4. DPA Governing Law and Forum Conflict with MSA

**Where:** DPA § 12.1–12.2; compare MSA § 16.1–16.2 and Term Sheet § 10.

**Issue:** The MSA and term sheet both specify Delaware law and Wilmington, Delaware forum. The DPA specifies New York law and New York County courts.

**Why it matters:** A data breach dispute could implicate both the MSA (e.g., the security obligations in § 8.3, the liability cap in § 11) and the DPA (e.g., breach notification in § 6, subprocessor liability in § 5.3). Split governing law and forum creates the risk of inconsistent interpretations, parallel proceedings, and added cost. It also gives Provider a home-turf argument in New York for data disputes.

**Recommended fix:** Conform DPA § 12 to Delaware law and Wilmington forum, matching MSA § 16.

---

### 5. DPA "Customer Data" Definition Is Narrower Than MSA Definition — Creating a Protection Gap

**Where:** DPA § 1.3; compare MSA § 1.4.

**Issue:** MSA § 1.4 defines Customer Data as "all data Provider receives from or collects for Customer in performing Services," expressly including "venue access information, delivery sign-offs, and any data entered into or generated by the Dispatch Platform." DPA § 1.3 defines Customer Data as only "Personal Data *uploaded by Customer* to the Zouduth Dispatch Platform." Data that Provider's crews *collect* on site (e.g., a delivery sign-off with a guest's name, a venue access code photographed by a crew member) is Customer Data under the MSA but not under the DPA.

**Why it matters:** Because MSA § 2.3 gives the DPA priority "for Personal Data matters only," and the DPA's narrower definition controls for those matters, Personal Data collected by Provider in the field falls outside the DPA's specific protections: the 48-hour breach notification (§ 6.1), subprocessor flow-down requirements (§ 5.3), security incident cost allocation (§ 6.4), data subject request handling (§ 7), and audit rights (§ 9). It would be governed only by the general MSA confidentiality and security provisions (§§ 7–8), which are less specific.

**Recommended fix:** Conform DPA § 1.3 to the MSA § 1.4 definition, or add language capturing Personal Data "collected by Provider or its personnel in the course of performing the Services."

---

### 6. DPA Liability Subject to MSA Cap and Consequential Damages Waiver

**Where:** DPA § 11.1; MSA § 11.1–11.2.

**Issue:** DPA § 11.1 subordinates all DPA liability to the MSA's 12-month-fee cap and the consequential damages exclusion. A data breach involving event client names, addresses, and phone numbers could trigger regulatory notification obligations, consumer class actions, and reputational harm — all of which are "consequential" or "indirect" damages that § 11.2 excludes.

**Why it matters:** Nonaisk's maximum recovery for a Provider-caused data breach would be approximately $1.85 million (12 months of fees), and only for direct damages. If the breach affects thousands of event clients and triggers state AG enforcement or a class action, Nonaisk's actual costs could far exceed the cap, and the most significant costs (regulatory fines, class settlement, notification to data subjects) are likely to be characterized as consequential.

**Recommended fix:** Add a carve-out in MSA § 11.3 for Provider's obligations under the DPA (or at minimum for Security Incidents resulting from Provider's or its Subprocessors' breach). Alternatively, negotiate a super-cap for data protection liability (e.g., 2× the general cap).

**Client decision needed:** Nonaisk should assess its data breach risk exposure (volume of event client data, types of data, state laws implicated) and decide whether to push for a carve-out or accept the cap with the understanding that its cyber insurance (if any) is the backstop.

---

### 7. Cargo Insurance Limit May Be Inadequate

**Where:** MSA § 12.1(c).

**Issue:** Cargo and inland marine insurance is required at only $500,000 per conveyance. A single truckload of staging, tenting furniture, and banquet sets for a large corporate event or wedding can easily exceed that value.

**Why it matters:** If a truck is totaled in an accident, Provider's insurance pays at most $500K per conveyance. The shortfall is Provider's responsibility under § 3.3 (reimbursement for replacement value), but Provider's ability to pay is limited, and its liability is capped at 12 months of fees under § 11.1. Nonaisk could be left absorbing the difference.

**Recommended fix:** Increase the per-conveyance cargo limit to reflect Nonaisk's actual truckload values (client to confirm typical load values). Alternatively, require Provider to carry a higher aggregate cargo limit or to name Nonaisk as additional insured on the cargo policy (currently § 12.2 only requires additional insured status on GL and auto policies).

---

## Moderate-Priority Issues

### 8. No Termination for Convenience; Three-Year Lock-In with Escalating Costs

**Where:** MSA §§ 5.2, 5.5, 14.1–14.3.

**Issue:** Customer is committed to $1.85M per year for three years ($5.55M total), with rate increases of up to 3% per year after year one. There is no termination for convenience. The only exits are for material breach (§ 14.3, with a 30-day cure period) or Provider insolvency (§ 14.4).

**Why it matters:** If Nonaisk's business shrinks, pivots, or if Provider chronically underperforms below the material-breach threshold (e.g., misses service levels twice in six months rather than three times), Nonaisk remains locked in and owes the annual minimum. The 3% annual escalator compounds the commitment.

**Recommended fix:** Add a termination for convenience right exercisable after the first Contract Year on 120 days' notice, with a declining buyout (e.g., 50% of remaining annual minimums in year 2, 25% in year 3). Alternatively, tie the annual minimum to a volume floor that adjusts if Provider's service levels are missed more than a de minimis number of times.

**Client decision needed:** Nonaisk should confirm its revenue visibility over three years and whether a lock-in of this size is acceptable given its growth trajectory.

---

### 9. Press Release Is Dated as If the Deal Is Already Signed and Contains Unapproved Characterizations

**Where:** Press Release, entire document; MSA § 9.3; Term Sheet § 11.

**Issue:** The press release is dated March 4, 2026, two days after the MSA effective date, and uses past-tense language ("today announced," "have entered into a data processing addendum"). MSA § 9.3 requires that any announcement be "mutually approved." The term sheet similarly contemplates a "mutually approved joint announcement" only "on signing."

**Why it matters:** If this release goes out before Nonaisk has signed, it creates public expectations and potential estoppel arguments. Even if the deal closes, Nonaisk should review and approve the language. Specific concerns: (a) § 2 states crews "will work to Nonaisk's handling and installation standards" — this publicly affirms a standard that could be cited in a future performance dispute; (b) § 4 states data "is stored within the United States" as a present fact, which could be problematic if a subprocessor change later moves data.

**Recommended fix:** Do not allow the press release to distribute until (a) the MSA is executed, and (b) Nonaisk has approved the final text. Add a sentence to MSA § 9.3 clarifying that no announcement (including dated drafts) may be circulated without written approval.

---

### 10. Transition Assistance Period May Be Insufficient for a Seasonal Business

**Where:** MSA § 14.5.

**Issue:** Provider is required to provide transition assistance for only 90 days post-termination. For an event rental business with peak seasons (spring/summer weddings, fall corporate events), 90 days may not span a full season, making it difficult to onboard a replacement without a service gap.

**Why it matters:** If the relationship ends in, say, April, the 90-day transition window closes in July — mid-peak. Nonaisk would need to have a replacement fully operational before the transition period expires to avoid a gap during its busiest months.

**Recommended fix:** Extend transition assistance to 120 days, or provide that the period runs through the end of the next full event season (as defined in the applicable SOW), whichever is shorter.

---

### 11. Subprocessor Objection Remedy Is Unclear

**Where:** DPA § 5.2.

**Issue:** If Customer objects to a new subprocessor and the parties cannot resolve the objection within 30 days, Customer may "terminate the affected Services without penalty." The phrase "affected Services" is undefined, and "without penalty" does not clearly address whether the annual minimum commitment is reduced or whether Customer can terminate the entire MSA.

**Why it matters:** If the objected-to subprocessor hosts the Dispatch Platform (per Annex C), "affected Services" could arguably be all Services, but Provider will likely argue it is only the specific function the subprocessor performs. The annual minimum question is critical: if Customer terminates "affected Services" but still owes the $1.85M minimum, the remedy is illusory.

**Recommended fix:** Clarify that "affected Services" means the Services that cannot be performed without the objected-to subprocessor, and that "without penalty" includes a pro-rata reduction of the Annual Minimum for the terminated Services.

---

### 12. Customer Must Ensure Inventory Is "Suitably Packaged" — Potential Shifting of Loading Risk

**Where:** MSA § 4.3; compare § 3.2–3.3.

**Issue:** § 4.3 requires Customer to ensure Rental Inventory is "in serviceable condition and suitably packaged for transport." § 3.3 makes Provider responsible for damage "while in Provider's care, custody or control." The boundary between Customer's packaging obligation and Provider's loading/transport responsibility is not clearly drawn.

**Why it matters:** If furniture is damaged in transit, Provider will have an argument that the damage resulted from inadequate packaging (a Customer obligation under § 4.3) rather than from Provider's handling. This could lead to disputes over which party bears the loss, particularly for items that are inherently fragile or irregularly shaped.

**Recommended fix:** Add language to § 3.3 clarifying that Provider's responsibility attaches from the moment it takes physical possession of the Rental Inventory at Customer's facility, regardless of packaging condition, unless the damage is solely attributable to packaging that was visibly deficient at the time of loading.

---

## Summary Table

| # | Issue | Document / Section | Type | Priority |
|---|-------|-------------------|------|----------|
| 1 | Blanket Customer indemnity for all inventory claims | MSA § 10.2 | Client decision | Critical |
| 2 | Provider free assignment, no competitor restriction | MSA § 15.2 | Client decision | Critical |
| 3 | Customer indemnity uncapped; Provider indemnity capped | MSA § 11.3(c) | Client decision | Critical |
| 4 | DPA governed by NY law; MSA by DE law | DPA § 12 | Drafting | High |
| 5 | DPA "Customer Data" narrower than MSA | DPA § 1.3 vs. MSA § 1.4 | Drafting | High |
| 6 | Data breach liability subject to cap + consequential waiver | DPA § 11.1; MSA § 11 | Client decision / Drafting | High |
| 7 | Cargo insurance $500K/conveyance may be too low | MSA § 12.1(c) | Drafting | High |
| 8 | No termination for convenience; 3-yr lock-in | MSA §§ 5.2, 14 | Client decision | Moderate |
| 9 | Press release premature; unapproved language | Press Release; MSA § 9.3 | Client decision | Moderate |
| 10 | 90-day transition may not cover a season | MSA § 14.5 | Drafting | Moderate |
| 11 | Subprocessor objection remedy unclear | DPA § 5.2 | Drafting | Moderate |
| 12 | Packaging obligation may shift loading risk | MSA §§ 4.3, 3.3 | Drafting | Low |