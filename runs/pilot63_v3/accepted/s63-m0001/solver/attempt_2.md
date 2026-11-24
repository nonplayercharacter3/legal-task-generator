# MEMORANDUM

**TO:** [Partner]
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Bisart AgTech Corp. / Bramand Holdings, LLC – Stock Purchase: Buyer-Side Exposure Review

---

## Issues Requiring Immediate Attention

### 1. Kestrune Avionics Autopilot License – No Closing Condition, No Walk Right

**Where:** SPA § 1.1 (definition of "Required Consents"); Disclosure Schedule § 4.6, Item 2; SPA § 7.2(d); SPA § 4.4; SPA § 6.4(b)

**Issue:** The Disclosure Schedule identifies the Autopilot Firmware License Agreement with Kestrune Avionics GmbH as a Material Contract and expressly notes that "Section 12.3 of that agreement provides that the licensor may terminate the license upon written notice upon any change of control of Licensee effected without the licensor's prior written consent." This is the flight-control autopilot firmware installed on **all** Company drone models. Without it, the fleet cannot operate.

However, the defined term "Required Consents" in SPA § 1.1 covers **only** "the consent of the landlord under the Hangar Lease." The Kestrune consent is not a Required Consent, is not a closing condition under § 7.2(d), and is not the subject of the efforts covenant in § 6.4(b). The prior draft contained a drafting note ("Third-party consent deliverables to be added once diligence on Material Contracts is complete") at § 3.2, confirming this was a known open item that was resolved by narrowing the definition rather than adding the consent.

Because the Kestrune consent requirement is disclosed in the Disclosure Schedule, the § 4.4 (No Conflicts) representation is effectively qualified as to this matter. Post-closing, the exclusive remedy provision (§ 9.7) would limit Bisart to indemnification—and the § 4.4 rep is a non-fundamental rep subject to the $4.2M cap (§ 9.5(a)), which is a small fraction of the loss if the entire drone fleet loses its autopilot.

**Why it matters:** Bisart could close, pay $42M, and then have Kestrune terminate the license the following week. The drones would be ground-bound. The indemnification cap would not come close to covering the loss of the core operating asset.

**Recommendation:**
- Add the Kestrune consent to the definition of "Required Consents" in § 1.1, making it a closing condition under § 7.2(d).
- Alternatively, if Seller resists a condition, add a specific covenant requiring Seller to obtain Kestrune's written consent (or a waiver of the termination right) **before** Closing, with failure to do so constituting a breach of a specific covenant (recoverable under § 9.2(b), which is not subject to the cap).
- As a fallback, negotiate a specific indemnity from Seller, outside the cap, for any loss arising from termination or non-renewal of the Kestrune license.

---

### 2. Asymmetric Assignment Right Exposes Earn-Out Information to Third Parties

**Where:** SPA § 11.4; SPA § 2.5(d)

**Issue:** Section 11.4 provides: "Buyer may not assign this Agreement or any of its rights or obligations hereunder, by operation of law or otherwise, without the prior written consent of Seller… **Seller may assign this Agreement or any of its rights hereunder, in whole or in part, without the consent of Buyer.**"

The earn-out information rights in § 2.5(d) require Buyer to deliver to Seller quarterly reports "broken down by customer, by acreage serviced and by product and service line, with the applicable pricing," and to give Seller "reasonable access… to the books, records, customer lists, acreage and application logs, pricing schedules and personnel of the Company." These are rights of Seller under the Agreement.

If Seller assigns the Agreement (or its rights) to a third party—say, a portfolio company, a competitor, or a fund—that assignee steps into Seller's shoes for purposes of the earn-out information rights. The non-compete in § 6.7 is an obligation of Seller, not a right, and would not transfer under an assignment of "rights hereunder." The result: a third party with no non-compete restriction receives Bisart's customer-level pricing and operational data for the entire earn-out period (through December 31, 2027) plus the audit window.

The prior draft does not show this provision (Article XI §§ 11.4–11.7 were marked "[To follow]"), so this appears to have been introduced or accepted in the final turn without flagging the interaction with the earn-out information rights.

**Why it matters:** Bisart is buying a precision-agriculture drone company. Customer identity, acreage serviced, and pricing are the core competitive data. Leaking that to an uncontrolled third party undermines the acquisition's strategic value and could violate customer confidentiality expectations.

**Recommendation:**
- Delete or narrow the second sentence of § 11.4. At minimum, provide that Seller may not assign any right to receive information under § 2.5(d) without Buyer's prior written consent.
- Alternatively, add a proviso: "Notwithstanding the foregoing, no assignment by Seller shall transfer any right to receive information or access under Section 2.5(d), and any purported assignment of such rights shall be void."

---

### 3. Survival Period for Non-Fundamental Representations Is Only ~5.5 Months Post-Closing

**Where:** SPA § 9.1; Escrow Agreement § 1.1 (definition of "Escrow Release Date")

**Issue:** SPA § 9.1 provides that non-fundamental representations "shall survive the Closing until 11:59 p.m. New York time on the Escrow Release Date." The Escrow Agreement § 1.1 defines "Escrow Release Date" as "the date that is twelve (12) months after the date of this Escrow Agreement." The Escrow Agreement is dated March 2, 2026—the same date as the SPA. The Escrow Release Date is therefore **March 2, 2027**.

The Closing is scheduled for **September 15, 2026** (SPA § 3.1). The survival period for non-fundamental reps is thus approximately **5 months and 2 weeks after Closing**.

For comparison, the Fundamental Representations (§§ 4.1, 4.2, 4.3, 4.12-as-originally-numbered) survive until 60 days after expiration of the applicable statute of limitations—years longer. But all other reps (financial statements, IP, taxes, environmental, employees, material contracts, product liability, etc.) die on March 2, 2027.

**Why it matters:** Many of the most important reps in an acquisition of an operating business do not manifest until the buyer has been running the company for several months. Tax issues (e.g., unrecorded liabilities, sales tax exposure on drone leases), environmental issues (e.g., fuel or battery storage at the Salina hangar), product warranty claims, and IP chain-of-title gaps typically surface 6–18 months post-closing. Bisart will have no indemnification recourse for these after March 2, 2027.

Compounding the problem: the Escrow Release Date is also when the escrow is disbursed to Seller (Escrow Agreement § 5.1). After that date, even if a claim were somehow still alive, the escrow—Bisart's primary source of recovery under § 9.6(a)—would be gone.

**Recommendation:**
- Amend Escrow Agreement § 1.1 to define "Escrow Release Date" as the date that is twelve (12) months after the **Closing Date** (not the date of the Escrow Agreement). This would push the release to approximately September 15, 2027, giving Bisart a full 12 months post-closing.
- If Seller resists extending the escrow hold, at minimum extend the survival period in SPA § 9.1 to 18 months post-Closing for the reps in §§ 4.5 (Financial Statements), 4.7 (IP), 4.12/4.13 (Taxes, as renumbered), and 4.13/4.14 (Environmental, as renumbered), with a corresponding extension of the escrow for those specific claims.

---

## Other Significant Issues

### 4. Uncapped Buyer Indemnification for Seller Guarantees

**Where:** SPA § 9.3(c); § 9.5(b); § 6.8; Disclosure Schedule § 4.16

**Issue:** Section 9.3(c) requires Buyer to indemnify Seller for "any Seller Guarantee, including any payment, performance or other obligation of Seller or its Affiliates under any Seller Guarantee, whether arising before or after the Closing." The Seller Guarantee is Bramand's guaranty of the Company's $7.3M Fleet Financing Agreement with Fallowgate Equipment Finance LLC.

The cap in § 9.5(b) applies only to "claims under Section 9.3(a)" (Buyer's rep breaches). It does **not** apply to § 9.3(c). The Seller Guarantee indemnity is therefore **uncapped**.

Section 6.8 requires Buyer to use "commercially reasonable efforts" to obtain Seller's release from the guarantee by offering a replacement. The Board Consent (§ 5.2) limits the replacement guarantee to "the outstanding principal balance under that financing at the time of delivery, together with interest, fees and costs of enforcement." If Fallowgate will not accept a limited guarantee and insists on the full original terms (including future draws), the Seller Guarantee may remain outstanding post-Closing, and Bisart's uncapped indemnity in § 9.3(c) would be triggered by any default by the Company.

**Why it matters:** If the Company defaults on the Fleet Financing Agreement post-Closing (e.g., due to integration issues, working capital strain, or a crop-failure-driven revenue drop), Fallowgate could call the guarantee. If Seller's guarantee is still in place, Bisart must indemnify Seller for the full amount—potentially $7.3M plus interest and fees—with no cap.

**Recommendation:**
- Negotiate a cap on the § 9.3(c) indemnity equal to the outstanding principal balance under the Fleet Financing Agreement as of the Closing Date (plus accrued interest).
- Make the release of the Seller Guarantee (or delivery of an acceptable replacement) a **condition to Closing** rather than a post-closing "commercially reasonable efforts" covenant.
- Confirm with Fallowgate before Closing that they will accept the limited replacement guarantee described in the Board Consent.

---

### 5. Remote ID Retrofit Not an Express Closing Condition

**Where:** Side Letter § 4(d); SPA § 7.2(b); Side Letter Annex 1, Part C

**Issue:** Side Letter § 4(d) requires Seller to cause the Company to complete installation of remote identification broadcast modules on 14 FL-S20 aircraft "Before the Closing." However, this is a covenant, not an express closing condition. The only relevant closing condition is § 7.2(b), which requires Seller to have "performed and complied **in all material respects** with all covenants required by this Agreement to be performed or complied with by it before or at the Closing."

If one or two of the 14 aircraft are not retrofitted by Closing, Seller could argue the failure is not "material" (14 demo/leased aircraft out of an entire fleet). Bisart would then close with non-compliant aircraft in the fleet, creating FAA enforcement risk and potential liability under the new § 4.12(f) representation (as inserted by the Side Letter).

**Why it matters:** Operating aircraft without compliant Remote ID violates 14 C.F.R. Part 89. The FAA could issue enforcement action against the Company (now Bisart's subsidiary). The new FAA representation (§ 4.12) would be breached at Closing, but the survival period issue (Problem 3 above) means Bisart may have very little time to pursue a claim.

**Recommendation:**
- Add the completion of the Remote ID retrofit as an express item in § 7.2(f) (Deliverables) or as a standalone closing condition in § 7.2.
- At minimum, require delivery of the officer's certificate contemplated by Side Letter § 4(d) as a § 3.2 Seller Closing Deliverable.

---

### 6. Bill of Sale – Contributor IP Chain of Title Is Efforts-Based Only

**Where:** Bill of Sale § 4.2; SPA § 4.7(a)–(b)

**Issue:** Bill of Sale § 4.2 provides that if a contributor "has not assigned all of its rights," Seller shall "use commercially reasonable efforts, at its own expense, to obtain a written assignment of those rights directly to the Company." This is an efforts standard, not a guarantee. There is no representation in the Bill of Sale or the SPA that **all** contributors have in fact assigned their rights.

SPA § 4.7(a) represents that the Company "owns, or has a valid and enforceable right to use, all intellectual property used in or necessary for the conduct of the Business." But this is qualified by the Disclosure Schedule, and the survival period issue (Problem 3) limits how long Bisart can pursue a claim if a gap is discovered.

**Why it matters:** If a former contractor or consultant who wrote a significant portion of the FieldPath flight-planning software or the telemetry ingestion service never signed an assignment, a competitor (or the contributor themselves) could assert ownership or licensing rights. For a software-heavy business, this could impair the core product.

**Recommendation:**
- Require Seller to deliver, as a Closing deliverable, a complete list of all contributors with evidence of assignment (or a representation that all contributors have assigned).
- Add a specific representation in the Bill of Sale that all contributors to the Company Software have executed valid assignments of their IP rights to Seller or the Company, with exceptions disclosed in a schedule.
- Make the § 4.2 efforts covenant a condition to Closing (i.e., Seller must have made the efforts and reported results before Bisart is obligated to close).

---

### 7. Knowledge Transfer Limited to 40 Hours Per Person

**Where:** Bill of Sale § 3.4

**Issue:** Post-Closing, Seller's employees and contractors with "material knowledge of the design, architecture, build process or deployment of the Company Software" must be made available for 90 days, but "This assistance is limited to no more than forty (40) hours per individual."

The Company Software includes the FleetView telemetry dashboard (web + mobile + services), the GCS-series ground station firmware (handheld + vehicle-mount), and ancillary tools. This is a substantial embedded systems and software platform. Forty hours per person (roughly one work week) may be insufficient to transfer build environments, signing keys, deployment procedures, and architectural decisions—particularly if the key engineers are the only ones who understand certain subsystems.

**Why it matters:** If a critical engineer departs after the 90-day window (or uses up their 40 hours early on non-essential questions), Bisart could face a knowledge gap that delays product releases or creates maintenance burdens. The SPA § 10.1 employee covenant (12-month salary protection) reduces the incentive for engineers to leave immediately, but does not prevent departures after month 12.

**Recommendation:**
- Increase the cap to 80 hours per individual, or eliminate the cap for the first 30 days post-Closing.
- Require Seller to identify, before Closing, the specific individuals with critical knowledge and confirm their availability for the full 90-day period.
- Add a requirement that Seller deliver complete build documentation, CI/CD pipeline documentation, and deployment runbooks as part of the Contributed Materials (Bill of Sale § 1, definition of "Contributed Materials" already includes "build scripts" but not explicitly "deployment runbooks" or "operational procedures").

---

### 8. NDA Clean Team Restrictions May Impede Pre-Closing Integration Planning

**Where:** NDA §§ 4.1–4.3; NDA § 10.2; SPA (no corresponding provision)

**Issue:** The NDA (effective October 6, 2025, term: 2 years, i.e., through October 6, 2027) restricts Bisart's access to "Clean Team Information" (customer-specific pricing, margins, acreage data, dealer terms, bid information, product roadmaps) to a narrow "Clean Team" of outside advisors and specifically approved employees who "do not have direct responsibility for pricing, sales, marketing or dealer relations for products or services that compete with those of Furrowline" (NDA § 4.2).

NDA § 10.2 provides that the NDA continues to apply post-Definitive Agreement "to the extent [the Definitive Agreement] addresses those obligations." The SPA does not address Clean Team restrictions. Therefore, the NDA's Clean Team limitations continue to apply during the ~6-month interim period between signing (March 2, 2026) and Closing (September 15, 2026).

**Why it matters:** Bisart's integration planning team (which will include commercial, sales, and product personnel) cannot access Furrowline's customer pricing, dealer terms, or product roadmap during the interim period. This hampers Bisart's ability to plan synergies, identify integration risks, and prepare for Day 1 operations. The Board Consent (§ 1.3(f)) references a "management's integration plan for Furrowline" that was presented to the Board—but the team that built it may have been constrained by Clean Team rules.

**Recommendation:**
- Negotiate a waiver or amendment to the NDA's Clean Team restrictions effective upon execution of the SPA, or at a specified date post-signing (e.g., 30 days after signing).
- Alternatively, add a provision to the SPA (or a side letter) stating that, from and after the signing date, the Clean Team restrictions in the NDA no longer apply to Bisart's integration planning personnel, provided they are bound by the SPA's confidentiality provisions (§ 6.6 applies to Seller; Buyer's obligations are in § 11.1 and general fiduciary duties).

---

## Moderate / Administrative Issues

### 9. 12-Month Salary and Benefit Lock for Continuing Employees

**Where:** SPA § 10.1

**Issue:** For 12 months post-Closing, Buyer must cause the Company to maintain each Continuing Employee's base salary "no less favorable than that in effect immediately before the Closing" and provide "employee benefits that are substantially comparable in the aggregate to those provided to similarly situated employees of Buyer."

**Why it matters:** If Bisart's post-closing integration plan includes workforce rationalization (overlapping roles, office consolidation, etc.), it cannot reduce salaries or benefits for a full year. This limits cost synergies in the first 12 months.

**Recommendation:** Acceptable as a market-standard provision, but ensure the integration plan and financial model account for the 12-month lock. Consider negotiating a carve-out for employees whose positions are eliminated due to functional overlap with existing Bisart roles (with severance in lieu).

---

### 10. Board Consent – Broad Officer Authority with Self-Policing Standard

**Where:** Board Consent § 3.2(b)–(c); § 7.1–7.2

**Issue:** The Board Consent authorizes the CEO, CFO, and General Counsel (each an "Authorized Officer") to approve changes to the Purchase Agreement and Escrow Agreement that the officer "determines to be necessary, appropriate or advisable and not materially adverse to the Corporation," with the officer's execution being "conclusive evidence of that determination" (§ 3.2(c)). The only hard limits are: no increase in Base Purchase Price, no increase in Maximum Earn-Out Payment, no reduction in Escrow Amount (§ 3.2(d)).

There is no limit on: reducing survival periods, expanding Buyer's indemnification obligations, adding new covenants with significant cost, narrowing closing conditions, or modifying the working capital target. The "not materially adverse" determination is self-policed.

**Why it matters:** If additional side letters or amendments are negotiated between now and Closing, the officers can agree to them without further Board approval so long as they don't cross the three bright-line limits. A provision that is arguably "not materially adverse" in isolation (e.g., shortening the survival period by 3 months, or adding a Buyer covenant to fund a specific pre-closing capex item) could cumulatively erode Bisart's position.

**Recommendation:**
- Ensure the General Counsel's reporting obligation under § 7.2(c) ("shall report each such amendment, waiver or consent to the Committee at its next meeting") is calendared and tracked.
- Consider whether the Board should add a fourth bright-line limit to § 3.2(d): no reduction in the survival period for any representation or warranty.

---

### 11. Escrow Tax Treatment – Bisart Taxed on Escrow Earnings

**Where:** Escrow Agreement § 6.1; § 6.2

**Issue:** Bisart is treated as the tax owner of the Escrow Fund and must report all earnings on it (§ 6.1). Section 6.2 provides for quarterly distributions of 40% of earnings to fund Bisart's tax liability, but the distribution is only "upon Buyer's written request" and "No such distribution may reduce the Escrow Fund below the Escrow Amount."

**Why it matters:** If the money market fund earns, say, 5% on $4.2M, that's ~$210K of taxable income to Bisart per year. The 40% distribution (~$84K) may not fully cover the tax depending on Bisart's marginal rate. The net economics are minor but should be modeled.

**Recommendation:** Ensure the CFO's team requests the quarterly tax distributions promptly. Confirm the tax model accounts for the earnings inclusion.

---

### 12. SPA § 6.1(c) – Pre-Closing Draws Increase Buyer's Effective Cost

**Where:** SPA § 6.1(c); § 2.2(b); Disclosure Schedule § 4.16

**Issue:** Between signing and Closing, the Company may draw up to $500,000 additional under the Fleet Financing Agreement. These draws are "Indebtedness" that Buyer pays off at Closing under § 2.2(b). The working capital calculation (§ 2.4(e)) excludes Indebtedness from current liabilities, so the additional debt does not reduce the working capital credit. The net effect is that Buyer funds up to $500K of additional debt on top of the Base Purchase Price.

**Why it matters:** Minor economic point (~$500K), but it means the effective purchase price is up to $500K higher than the $42M Base Purchase Price if Seller causes maximum draws before Closing.

**Recommendation:** Confirm in the financial model that the $42M Base Purchase Price is net of the expected debt payoff. If the $42M was negotiated assuming a specific debt balance, consider adding a proviso that draws in excess of a stated amount reduce the Base Purchase Price dollar-for-dollar.

---

## Summary Table

| # | Issue | Document / Section | Severity |
|---|-------|-------------------|----------|
| 1 | Kestrune consent not a closing condition | SPA § 1.1; DS § 4.6(2); § 7.2(d) | **Critical** |
| 2 | Seller can assign earn-out info rights to third parties | SPA § 11.4; § 2.5(d) | **Critical** |
| 3 | Non-fundamental rep survival only ~5.5 months post-Closing | SPA § 9.1; Escrow Agt § 1.1 | **Critical** |
| 4 | Uncapped Buyer indemnity for Seller Guarantees | SPA § 9.3(c); § 9.5(b) | Significant |
| 5 | Remote ID retrofit not express closing condition | Side Letter § 4(d); SPA § 7.2(b) | Significant |
| 6 | Contributor IP chain of title is efforts-based only | Bill of Sale § 4.2; SPA § 4.7 | Significant |
| 7 | Knowledge transfer capped at 40 hrs/person | Bill of Sale § 3.4 | Significant |
| 8 | NDA Clean Team restrictions impede integration planning | NDA §§ 4.1–4.3, 10.2 | Moderate |
| 9 | 12-month salary/benefit lock | SPA § 10.1 | Moderate |
| 10 | Board officer authority is self-policed | Board Consent §§ 3.2, 7.1–7.2 | Moderate |
| 11 | Bisart taxed on escrow earnings | Escrow Agt §§ 6.1–6.2 | Minor |
| 12 | Pre-closing draws increase effective cost | SPA §§ 6.1(c), 2.2(b) | Minor |

---

*Items 1–3 should be raised with Seller before the next drafting turn. Items 4–7 are important but may be addressable through a combination of closing deliverables, specific indemnities, and escrow adjustments. Items 8–12 are lower priority but should be noted in the integration plan.*