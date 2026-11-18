# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Baineind Event Rentals, LLC – Software License Agreement with Beipeiv Software, Inc.: Issue Identification and Recommended Fixes

---

## Summary

I have reviewed all eight documents in the matter folder. I identify fifteen issues, ranging from a critical pre-closing consent gap to drafting conflicts that erode the client's service-level protections. The most urgent item is the change-of-control consent problem (Issue 1), which requires action before the expected December 15, 2026 closing.

---

## Issue 1 – Change of Control: Notice Letter Fails to Request Required Consent

**Where:** Software License Agreement § 16.2, § 16.3; Baineind Notice Letter (Nov. 2, 2026) § 3

**The problem:** Section 16.2 provides that any direct or indirect change in Control of Licensee "is deemed an assignment" requiring "Licensor's prior written consent, which Licensor may give or withhold in its sole discretion." The sale of 100% of Baineind's membership interests from Ostrander Holdings LLC to Kestrel Venue Group is unambiguously a change in Control under the § 1.4 definition (ownership of more than 50% of membership interests).

The November 2 notice letter, however, states in § 3: "This letter is provided for Beipeiv's information, and no action is required by Beipeiv in connection with it." It does not request consent. If the closing proceeds on December 15 without Beipeiv's prior written consent, Section 16.3 is triggered: the assignment is void, Beipeiv may terminate immediately, and "all License Fees for the remainder of the Initial Term become immediately due and payable." The Initial Term runs to February 28, 2029; accelerated fees would approximate $372,000–$410,000 (the balance of the 2026–27 annual fee already paid in advance, plus the full 2027–28 and a portion of the 2028–29 annual fee).

**Why it matters:** This is the single most financially dangerous item in the file. The client has structured the notice as informational, but the Agreement treats the event as a consent-requiring assignment. Beipeiv has sole discretion to withhold consent.

**Recommended fix:**
1. Before closing, send a supplemental letter that expressly requests Beipeiv's written consent under § 16.2, identifying the transaction and the expected closing date.
2. Make Beipeiv's written consent a condition to closing in the Ostrander–Kestrel purchase agreement (or obtain a consent letter as a closing deliverable).
3. If Beipeiv signals it may withhold consent, explore whether a side agreement or novation can be negotiated (e.g., Beipeiv consents in exchange for a fee or a commitment from Kestrel).
4. Do not allow the closing to occur without documented consent in hand.

**Can this be resolved from the documents alone?** No. We do not know whether Beipeiv has informally indicated it will consent, or whether Kestrel is aware of the § 16.2 requirement. Confirm with the client.

---

## Issue 2 – Severity 1 Incident Definition: SLS Narrows the Agreement's Broader Definition

**Where:** Software License Agreement § 1.18; Service Level Schedule § 2.1; Agreement § 20.4 (order of precedence); Platform License Term Sheet § 6.2

**The problem:** The Agreement defines a Severity 1 Incident as "any failure of the Platform preventing Licensee from creating, modifying or fulfilling Rental Orders **at any Licensee location**" (emphasis added). The SLS defines it as "the **complete** unavailability of the Platform to **all** Authorized Users at **all** Licensee locations" (emphasis added).

Under § 20.4, for service-level matters the SLS prevails over the body of the Agreement. The SLS's definition therefore controls. The practical effect is that a partial outage—e.g., the Rental Order module down at one of Baineind's multiple warehouses, or the dispatch module unavailable during an event day—would be classified as Severity 2, not Severity 1.

| | Severity 1 (SLS) | Severity 2 (SLS) |
|---|---|---|
| Response | 1 hour, 24×7 | 4 Business Hours |
| Resolution target | 4 hours | 2 business days |
| Service credit trigger | Availability + response | None directly |

For an event rental company whose operations depend on same-day order processing and dispatch at each warehouse, a single-location outage during peak season is operationally equivalent to a total outage.

The term sheet (§ 6.2) used the broader definition, suggesting the SLS's narrower language was introduced during drafting without flagging the discrepancy.

**Why it matters:** The client loses the 24×7 one-hour response commitment and the four-hour resolution target for the most common and operationally damaging failure mode (partial degradation at one or more locations).

**Recommended fix:** Amend SLS § 2.1 to align with the Agreement's definition, or add a proviso: "Notwithstanding the foregoing, a failure of the Rental Order, delivery dispatch or warehouse pick-list module at any single Licensee location shall be treated as a Severity 1 Incident." If Beipeiv resists, negotiate at minimum a Severity 2 response time of 1 hour (rather than 4 Business Hours) for module-level failures affecting Rental Order functionality.

---

## Issue 3 – Governing Law and Forum Conflict Between the Agreement and the Side Letter

**Where:** Software License Agreement §§ 20.1–20.2; Side Letter §§ 6.1–6.2; Platform License Term Sheet § 13.2

**The problem:** The Agreement specifies Delaware law and exclusive jurisdiction in Wilmington, Delaware. The Side Letter specifies New York law and exclusive jurisdiction in Manhattan. Under § 20.4, the Side Letter has first priority, and its § 6.2 covers disputes arising from "this Side Letter **or the Agreement as modified hereby**."

This creates an ambiguous split: a dispute that touches any Side Letter provision (e.g., peak-season support, seasonal user credentials, off-peak rate cap) is governed by New York law in Manhattan, while a purely Agreement-based dispute (e.g., a data security claim under § 8) is governed by Delaware law in Wilmington. The term sheet (§ 13.2) contemplated Delaware law for the Agreement, indicating the New York provisions in the Side Letter were likely inserted by Beipeiv's counsel without the client's informed consent to the forum shift.

**Why it matters:** The client is a Delaware LLC headquartered in Wilmington. Litigating in Manhattan under New York law increases cost and removes the home-forum advantage. The ambiguity also creates threshold jurisdictional disputes in any litigation.

**Recommended fix:** Amend Side Letter § 6 to conform to the Agreement (Delaware law, Wilmington forum), or at minimum clarify that § 6.2 applies only to disputes arising exclusively under the Side Letter and not to the Agreement generally. If Beipeiv insists on New York law for the Side Letter, ensure the client's litigation budget and counsel selection account for the dual-forum risk.

---

## Issue 4 – Licensee Indemnity (§ 12.2(b)) Sweeps In Platform-Caused Third-Party Claims

**Where:** Software License Agreement § 12.2(b); Quality Agreement §§ 1.2(b)–(c), 5.3–5.5

**The problem:** Section 12.2(b) requires Baineind to indemnify Beipeiv against "any claims by event customers, venues or other third parties arising from Rental Orders processed through the Platform." This is not limited to claims caused by Baineind's own acts or omissions. If a Platform Data Error (e.g., a double-booking caused by a synchronization defect) results in a venue or customer claim, Baineind must still indemnify Beipeiv under § 12.2(b), even though the Quality Agreement (§ 5.3) requires Beipeiv to correct Platform Data Errors at no charge and the Agreement (§ 17.2) makes that correction Licensor's obligation.

The indemnity runs one way: Baineind protects Beipeiv from Rental Order claims, but Beipeiv has no corresponding obligation to indemnify Baineind for third-party claims caused by Platform defects.

**Why it matters:** In the event of a Platform-caused data error that leads to a customer dispute (missed delivery, double-allocated inventory, incorrect pricing on a Rental Order), Baineind faces the customer claim *and* must indemnify Beipeiv if Beipeiv is also named. The Quality Agreement's correction mechanism addresses the data, not the downstream third-party liability.

**Recommended fix:** Add a carve-out to § 12.2(b): "Licensee's obligation under this clause (b) shall not extend to claims to the extent arising from or caused by a Platform Data Error as defined in the Quality Agreement, or from Licensor's breach of this Agreement." Alternatively, add a reciprocal indemnity from Beipeiv for third-party claims caused by Platform defects.

---

## Issue 5 – Liability Cap Is Inadequate Relative to Client's Exposure

**Where:** Software License Agreement § 13.1; Service Level Schedule § 5.5

**The problem:** The aggregate liability cap is $186,000 (fees paid or payable in the 12 months before the claim). Service credits are capped at 30% of the Monthly Fee per month, i.e., $4,650. For a company whose entire order-processing, inventory and dispatch operations run through the Platform, a prolonged outage or a data breach exposing customer PII could generate losses (lost revenue, customer termination, regulatory fines, reputational harm) that dwarf the cap.

The Excluded Claims (§ 13.3) do not include data breaches, service failures, or warranty breaches—only indemnity obligations, confidentiality breaches, gross negligence/fraud/willful misconduct, and payment obligations escape the cap.

**Why it matters:** In a worst-case scenario (e.g., a 48-hour total outage during the November 15–December 31 Peak Season), the client's recoverable damages are limited to $186,000 minus any service credits already applied (per § 13.4, credits count toward the cap). The client's actual lost revenue during that window could be substantially higher.

**Recommended fix:**
1. Negotiate a "super-cap" of 2×–3× annual fees for data security breaches and for failures of the Platform during a Peak Season.
2. Alternatively, clarify that the client may pursue Beipeiv's insurance directly (see Issue 15) for cyber and E&O claims, effectively raising the practical recovery limit to the $5M policy limits.
3. At minimum, confirm that the § 13.4 provision (credits count toward the cap) does not mean the client is *double-counted*—i.e., that service credits reduce the cap dollar-for-dollar.

---

## Issue 6 – Claims-Made Insurance Policies: Retroactive Date and Renewal Risk

**Where:** Beipeiv Certificate of Insurance §§ 5.4, 5.5; Software License Agreement § 14

**The problem:** Both the Technology E&O ($5M) and Cyber Liability ($5M) policies are claims-made with a retroactive date of March 1, 2019. The policy period runs March 1, 2026 to March 1, 2027. If Beipeiv changes carriers, lets the policy lapse, or renegotiates terms at renewal, a claim filed after March 1, 2027 for an incident that occurred during the policy period may be uncovered unless (a) the new policy maintains the same or earlier retroactive date, or (b) tail/extended reporting coverage is purchased.

The Agreement (§ 14.2) requires Beipeiv to notify Baineind within 30 days of any "cancellation or material reduction of coverage," but does not require Beipeiv to maintain the retroactive date or to provide evidence of continuous claims-made coverage throughout the Term.

**Why it matters:** The Initial Term runs to February 28, 2029—two policy renewals. If Beipeiv switches to a new carrier with a later retroactive date at either renewal, coverage for incidents occurring under the prior policy could be compromised.

**Recommended fix:**
1. Request a contractual commitment (via amendment or side letter) that Beipeiv will maintain claims-made policies with a retroactive date no later than March 1, 2019 for the entire Term.
2. Require Beipeiv to provide a new certificate of insurance at each annual renewal (not just "on request").
3. Ask Beipeiv's broker to confirm in writing whether the policies include automatic extended reporting periods or whether tail coverage would be triggered by non-renewal.

**Can this be resolved from the documents alone?** No. We would need to see the actual policy forms to confirm the terms of the claims-made provisions and any extended reporting period.

---

## Issue 7 – Peak Season Begins Before Go-Live

**Where:** Implementation Kickoff Meeting Notes §§ 3.1–3.2; Side Letter § 1.1(a)

**The problem:** The first Peak Season begins April 1, 2026, but the go-live date is April 6, 2026. During April 1–5, the Side Letter's Peak Season obligations (named support engineer available 6 a.m.–10 p.m. ET seven days a week under § 2.1; maintenance restrictions under § 2.3) technically apply, but the Platform is not yet operational. The meeting notes acknowledge the gap and agree to keep the legacy system in read-only mode, but do not address whether the Side Letter's support engineer is obligated to be available during the gap or what "support" means when the Platform is not live.

**Why it matters:** Low financial impact, but creates ambiguity about whether Beipeiv is in breach if the named engineer is not available April 1–5, and whether Baineind can claim Peak Season rates for Additional Services ordered during that window.

**Recommended fix:** Obtain a brief written confirmation from Beipeiv that Side Letter Peak Season obligations are effective from the go-live date (April 6, 2026) for the first contract year, or that the April 1–5 period is treated as part of implementation services under § 4.1 of the Agreement.

---

## Issue 8 – Data Export Window (60 Days) Is Shorter Than Transition Assistance Period (90 Days)

**Where:** Software License Agreement §§ 7.3, 15.5

**The problem:** Section 7.3 gives Baineind 60 days after termination to export Licensee Data, after which Beipeiv deletes it. Section 15.5 provides up to 90 days of transition assistance at Beipeiv's professional services rates. If Baineind uses the full 90-day transition period, it may still need access to data (e.g., to verify migration to a replacement platform) after the 60-day export window has closed.

**Why it matters:** In a contested termination or a complex migration, the client could lose access to its own inventory records, customer data and Rental Order history before the transition is complete.

**Recommended fix:** Amend § 7.3 to extend the export window to 90 days (aligning with § 15.5), or add language stating that the export period is tolled during any transition assistance engagement.

---

## Issue 9 – SLS Resolution Targets Are Non-Binding

**Where:** Service Level Schedule § 3.4

**The problem:** Section 3.4 states: "The Resolution targets in Section 3.1 are targets. Licensor shall use commercially reasonable efforts to meet them. Service credits are payable only as set out in Section 5." Service credits under § 5 are triggered only by (a) Monthly Availability falling below 99.9% (§ 5.3) or (b) a missed Severity 1 Response time (§ 5.4). There is no credit for missing a Resolution target.

This means if the Platform is completely down for 12 hours (exceeding the 4-hour Severity 1 resolution target), the client's only remedy is the availability credit under § 5.3. If the 12-hour outage brings Monthly Availability to, say, 99.7%, the credit is only 5% of the Monthly Fee ($775). The client has no direct remedy for the resolution delay itself.

**Why it matters:** The resolution target is the metric most closely tied to the client's operational pain. Making it non-binding with no associated credit significantly weakens the SLA.

**Recommended fix:** Add a resolution credit: for each Severity 1 Incident not Resolved within the § 3.1 target, Licensee receives a credit of 5% of the Monthly Fee per 4-hour block of delay (capped at 25% of the Monthly Fee per incident). Alternatively, make the resolution target a hard commitment with termination rights if missed repeatedly.

---

## Issue 10 – IP Indemnity Limited to United States

**Where:** Software License Agreement § 12.1

**The problem:** The IP indemnity covers only "United States patent, copyright or trademark" infringement and trade secret misappropriation. If Baineind serves events or customers in Canada or elsewhere, or if the Platform is accessed from outside the US, there is no indemnity for foreign IP claims.

**Why it matters:** The documents do not specify Baineind's geographic footprint beyond Delaware. If the client operates multi-state or cross-border, this gap is material.

**Recommended fix:** Confirm the client's operational geography. If it extends beyond the US, negotiate to expand § 12.1 to cover the relevant jurisdictions, or at minimum add Canada.

**Can this be resolved from the documents alone?** No. We need to confirm Baineind's operational footprint.

---

## Issue 11 – Quality Agreement § 5.5: Client May Be Charged for Corrections Made During a Classification Dispute

**Where:** Quality Agreement § 5.5

**The problem:** When the parties disagree on whether a Data Error is a Platform Data Error or a Licensee Data Error, § 5.5 requires Licensor to correct the data if Licensee asks. But if the error is "later agreed or determined to be a Licensee Data Error, Licensor may charge for that correction under Section 5.4."

For urgent corrections (event date within 7 days, requiring 1-business-day turnaround under § 5.3), Baineind may be pressured to request immediate correction to avoid missing an event, only to later receive a bill if Beipeiv ultimately classifies the error as a Licensee Data Error.

**Why it matters:** Creates a hold-up problem during time-sensitive situations. The client may either (a) pay for a correction that might be Beipeiv's responsibility, or (b) refuse to request correction and risk missing an event.

**Recommended fix:** Amend § 5.5 to provide that corrections requested and performed during the pendency of a classification dispute are at Licensor's cost regardless of ultimate classification, or that the dispute must be resolved (under § 7.2 escalation) before any charge is made, with the 1-business-day urgent deadline running from the resolution of the dispute.

---

## Issue 12 – Baineind Is Not an Additional Insured on Beipeiv's Policies

**Where:** Beipeiv Certificate of Insurance § 1.3; Software License Agreement § 14

**The problem:** The certificate confirms that Baineind is the "Certificate Holder" but does not show it as an additional insured on any policy. Section 1.3 of the certificate expressly states that additional insured status requires an endorsement. The Agreement (§ 14) does not require Beipeiv to name Baineind as an additional insured.

**Why it matters:** In a data breach or Platform failure, Baineind cannot make a direct claim under Beipeiv's cyber or E&O policies. It must sue Beipeiv, and Beipeiv's insurers will control the defense. This slows recovery and gives Beipeiv leverage in settlement negotiations.

**Recommended fix:** Request that Beipeiv add Baineind as an additional insured on the CGL and Cyber Liability policies, or at minimum negotiate a direct-access provision allowing Baineind to make claims under the cyber policy for data breach response costs without first obtaining a judgment against Beipeiv.

---

## Issue 13 – Side Letter § 3.3: Off-Peak Rate Cap Is Structurally Odd

**Where:** Side Letter § 3.3

**The problem:** Section 3.3 provides that outside Peak Seasons, Additional Services rates "may not exceed the rates in Section 3.1 by more than ten percent (10%)." Read literally, this permits off-peak rates to be *higher* than peak rates (by up to 10%). The apparent intent is to cap off-peak rates so they don't spike above peak-season pricing, but the drafting allows a 10% premium off-peak.

**Why it matters:** Minor, but if Beipeiv's "then-current rates" under § 5.3 of the Agreement increase, the client could end up paying more for off-peak services than during the Peak Season, which is counterintuitive and likely not the commercial deal the parties struck.

**Recommended fix:** Amend § 3.3 to provide that off-peak rates "shall not exceed the rates set forth in Section 3.1" (i.e., peak rates are the ceiling for all periods), or clarify that the 10% is a maximum *discount* off-peak, not a maximum *premium*.

---

## Issue 14 – Auto-Renewal and the 90-Day Non-Renewal Notice Window

**Where:** Software License Agreement §§ 15.2, 5.4

**The problem:** The Agreement auto-renews for successive one-year terms unless either party gives 90 days' written notice of non-renewal. The Initial Term ends February 28, 2029, so the first non-renewal notice is due by November 30, 2028. Additionally, § 5.4 allows Beipeiv to increase fees by up to 5% per renewal with 90 days' notice.

If the Kestrel acquisition closes and the new ownership wants to evaluate whether to continue the Platform, it needs to be aware of this deadline. There is no termination-for-convenience right in the Agreement.

**Why it matters:** Missing the 90-day window locks the client in for another year at up to 5% higher fees. Post-acquisition, the new parent may have different technology strategies.

**Recommended fix:** Calendar the non-renewal notice deadline (November 30, 2028 for the first renewal). If the client wants flexibility, negotiate a one-time termination-for-convenience right after the Initial Term, with a 6-month notice period and payment of fees through the effective date of termination.

---

## Issue 15 – Insurance Limits: "Customary" Standard Is Unverifiable

**Where:** Software License Agreement § 14.1; Beipeiv Certificate of Insurance § 5

**The problem:** Section 14.1 requires Beipeiv to maintain policies with "limits customary for providers of cloud software of comparable scope." The certificate shows $1M CGL per occurrence / $2M aggregate, $5M E&O, and $5M Cyber. Whether these are "customary" for a platform serving enterprise event-rental clients is a market question we cannot answer from the documents.

**Why it matters:** If a loss exceeds the policy limits, the excess falls on Beipeiv (subject to the § 13.1 liability cap of $186,000), which may be insufficient to satisfy a judgment. The "customary" standard provides a contractual hook to argue the limits are inadequate, but it is fact-intensive and would require industry benchmarking.

**Recommended fix:** Obtain a market survey of technology E&O and cyber limits for comparable cloud platforms. If the current limits are below market, raise the issue with Beipeiv before the next policy renewal. At minimum, document the client's reliance on the § 14.1 "customary" standard in case a loss tests the limits.

**Can this be resolved from the documents alone?** No. Requires external market data.

---

## Items Requiring Client Confirmation

| # | Question | Why It Matters |
|---|---|---|
| A | Has Beipeiv responded to the November 2 notice letter? If so, what did it say? | Determines whether Issue 1 is already in crisis mode. |
| B | Is Beipeiv's written consent a condition to closing in the Ostrander–Kestrel purchase agreement? | If not, the client is exposed to § 16.3 upon closing. |
| C | Does Baineind operate in any jurisdiction outside the United States? | Determines materiality of Issue 10. |
| D | How many warehouse/showroom locations does Baineind currently operate? | Affects the practical impact of Issue 2 (partial outages at "any location"). |
| E | Has the go-live occurred as planned on April 6, 2026? Are there any open implementation issues? | Context for Issues 7 and 11. |
| F | Does the client have its own cyber liability or technology E&O insurance? | Affects the practical significance of Issues 5 and 12. |

---

## Priority Summary

| Priority | Issue | Action Required | Deadline |
|---|---|---|---|
| **Critical** | 1 – Change of Control consent | Send supplemental consent request; make consent a closing condition | Before Dec. 15, 2026 |
| **High** | 2 – Severity 1 definition | Propose SLS amendment | Next renewal or upon next SLA dispute |
| **High** | 4 – Indemnity scope | Propose § 12.2(b) carve-out | Before next renewal |
| **Medium** | 3 – Governing law conflict | Propose Side Letter § 6 amendment | Before any dispute arises |
| **Medium** | 5 – Liability cap | Negotiate super-cap or insurance access | Before next renewal |
| **Medium** | 6 – Claims-made renewal risk | Request retroactive date commitment | Before March 1, 2027 renewal |
| **Low** | 7–15 | Address in next amendment cycle | As convenient |