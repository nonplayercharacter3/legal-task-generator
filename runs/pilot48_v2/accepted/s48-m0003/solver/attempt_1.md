# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Zeisein Lift Services, Inc. – Bruben Elevator Components Supply Agreement: Issue Identification

I have reviewed all seven documents in the matter folder. Below are the issues I identified, ordered by urgency and severity.

---

## 1. Zeisein's Price Objection Is 18 Days Late – Increase Is Deemed Accepted

**Documents:** `zeisein_letter_2026-09-14.md` ¶¶1–2; `supply_agreement_zeisein_bruben.md` § 5.3

Section 5.3 requires Customer to deliver a notice of objection "within 30 days after receipt of a Price Adjustment Notice." The letter states the July Notice was "delivered to our King of Prussia offices by courier the same day" (July 28, 2026). Thirty days after July 28 is **August 27, 2026**. The objection letter is dated **September 14, 2026** – 48 days after receipt, or 18 days past the deadline.

Section 5.3 is unambiguous: "If Customer does not deliver a notice of objection within that period, the adjusted prices are deemed accepted by Customer and take effect on the date stated in the Price Adjustment Notice." The 14% increase takes effect October 1, 2026.

**Why it matters:** Zeisein is now contractually bound to the increased prices. The letter's substantive arguments (no cost justification, above PPI movement, fixed-price downstream contracts) are irrelevant to the deemed-acceptance mechanism. Zeisein's paragraph 3 statement that it "will continue to issue Purchase Orders… at the unit prices stated in Section 1.3" is a breach of the Agreement as it now stands.

**Recommendation:**
- Advise the client immediately that the objection is likely ineffective as a matter of contract.
- Explore whether Bruben can be argued to have waived the deadline (e.g., if Bruben's account manager acknowledged receipt of the letter and engaged in negotiation without raising the timeliness issue). Check the file for any Bruben response.
- If no waiver argument is available, negotiate a commercial resolution: Zeisein could offer to accept a reduced increase (e.g., 5–7%) in exchange for Bruben withdrawing the deemed-acceptance position, or accept the full increase in exchange for an extended price-protection period (e.g., 24 months instead of 12) under Order Form § 3.2.
- Going forward, implement an internal calendar with a 20-day alert for any Price Adjustment Notice so the 30-day window is never missed again.

---

## 2. Order Form Site Indemnity Is Overbroad and Uncapped

**Documents:** `order_form_mid_atlantic_program.md` § 6.1; `supply_agreement_zeisein_bruben.md` §§ 11.2, 12.1–12.2, 18.2

Order Form § 6.1 requires Zeisein to indemnify Bruben for **all** claims "arising from site conditions at any Program Site, or from the installation, adjustment, testing, start-up or operation of Products at any Program Site," including claims by Bruben's own employees, agents, and subcontractors. There is no fault requirement – Zeisein indemnifies even for events caused by Bruben's product defect or Bruben's own negligence.

This provision **overrides** the Agreement's balanced indemnity in § 11.2 (which limits Customer's indemnity to "the negligence or willful misconduct of Customer or its personnel in installing or servicing the Products") because § 18.2 gives the Order Form priority over the Agreement body.

Worse, § 12.2(b) excludes "a Party's obligations under any Order Form" from the liability cap in § 12.1. Zeisein's site indemnity is therefore **uncapped**.

**Why it matters:** If a Bruben-supplied controller board malfunctions and causes a fire at a Program Site, Zeisein could be liable to indemnify Bruben for Bruben's own employees' injury claims, even though the root cause was a product defect for which Bruben would otherwise indemnify Zeisein under Agreement § 11.1(a). The two indemnities could collide, and the Order Form provision wins on precedence.

**Recommendation:**
- Amend Order Form § 6.1 to (a) exclude claims to the extent arising from a defect in the Products or from Bruben's negligence or willful misconduct, and (b) limit the indemnity to claims for which Zeisein is legally responsible.
- Alternatively, add a carve-out: "This Section 6.1 does not apply to the extent a claim arises from a breach of Supplier's warranty under Section 9 of the Agreement or from Supplier's negligence or willful misconduct."
- If Bruben resists, at minimum negotiate to bring the site indemnity within the § 12.1 cap by removing "obligations under any Order Form" from § 12.2(b) or adding a specific cap for the site indemnity.

---

## 3. Hydraulic Power Units Are Not "Critical Parts" – No Emergency Order Available

**Documents:** `service_level_schedule.md` Annex 1; `order_form_mid_atlantic_program.md` § 1.3; `supply_agreement_zeisein_bruben.md` § 1.4

The entire Mid-Atlantic program is a **hydraulic elevator modernization** program. The three hydraulic power units (Lines 1–3 in the Order Form, priced $14,850–$19,975 each) are the most expensive and most mission-critical components. Yet none of them appears in Annex 1 (Critical Parts). Only solenoid coils, one valve size, controller boards, and a contactor are listed.

Because "Critical Part" is defined by reference to Annex 1 (SLS § 1.2), a failed hydraulic power unit cannot be ordered as an Emergency Order. Zeisein must place a Standard Order, which is subject to the 95% on-time delivery metric (SLS § 4.2) and the 3-Business-Day stocked-item shipping standard (SLS § 4.4) – not the 4-hour dispatch / 8-hour delivery standard in SLS § 3.1.

**Why it matters:** If a hydraulic power unit fails at a Program Site and passengers are trapped or the elevator is out of service, Zeisein has no contractual right to emergency dispatch. The building owner experiences a multi-day outage. Zeisein's service credits for late Standard Orders (3% of Monthly Fees per percentage point missed, SLS § 5.2) are trivial compared to the cost of a trapped-passenger incident or a building owner's claim.

**Recommendation:**
- Amend Annex 1 to add all three hydraulic power units (BEC-HPU-15S, BEC-HPU-20S, BEC-HPU-30S) and the 2" main valve assembly (BEC-MV-200) as Critical Parts.
- If Bruben resists adding the 30 HP unit (which is not a "stocked item" per the Order Form), at minimum add the 15 HP and 20 HP units, which are stocked.
- Negotiate a minimum stock quantity appropriate for the program (e.g., 2 per stocking location for the 15 HP, 1 for the 20 HP).

---

## 4. BEC-ST-075 Is a Critical Part With No Price in the Order Form

**Documents:** `service_level_schedule.md` Annex 1, item 6; `order_form_mid_atlantic_program.md` § 1.3

Annex 1 lists "Pump motor starter contactor, 3-pole, 75A" (BEC-ST-075) as a Critical Part with a minimum stock of 4 per location. However, this part does not appear anywhere in the Order Form's product table (§ 1.3). There is no unit price, no "stocked item" designation, and no specification reference.

**Why it matters:** If Zeisein needs to place an Emergency Order for this part (e.g., a contactor fails and an elevator won't start), there is no agreed price. Bruben could assert that the part is outside the scope of the Order Form and charge a list price, or refuse to supply it under the Agreement at all. The Emergency Order pricing protection in SLS § 3.5 ("charged at the prices set out in the applicable Order Form") is inoperable because no price is set.

**Recommendation:**
- Add BEC-ST-075 to the Order Form product table with a unit price and a "Stocked Item: Yes" designation.
- Confirm that the part is included in the Specifications reference in Order Form § 1.4.

---

## 5. Exclusivity Prohibition on Refurbishing Is Overly Broad

**Documents:** `supply_agreement_zeisein_bruben.md` § 3.1

Section 3.1(c) prohibits Customer and its Affiliates from "refurbish[ing], rebuild[ing] or remanufactur[ing] Elevator Components for resale or for installation at any customer site, in each case other than Products supplied by Supplier under this Agreement."

**Why it matters:** Zeisein is an elevator maintenance and modernization contractor. A core part of its business is likely the in-house repair and refurbishment of components (e.g., rewinding a motor, replacing contacts in a starter, rebuilding a valve). The clause as drafted prohibits Zeisein from refurbishing **any** Elevator Component for installation at any customer site, even components originally manufactured by a different OEM (e.g., a Otis or Schindler part in a building Zeisein maintains). The definition of "Elevator Components" (§ 1.2) is all-encompassing: "elevator and lift parts, assemblies and components of every kind."

This could prevent Zeisein from performing routine maintenance work on non-Bruben equipment, which is a significant portion of any elevator contractor's business.

**Recommendation:**
- Amend § 3.1(c) to limit the prohibition to Bruben Products only: "refurbish, rebuild or remanufacture **Products** for resale or for installation at any customer site."
- Alternatively, add a carve-out: "provided that Customer may refurbish, rebuild or remanufacture Elevator Components that were not originally supplied by Supplier under this Agreement."
- Clarify that routine maintenance and repair (as distinct from refurbishment for resale) is not prohibited.

---

## 6. Parent Guaranty Is Subject to the Agreement's Liability Cap

**Documents:** `bruben_parent_guaranty.md` § 2.3; `supply_agreement_zeisein_bruben.md` § 12.1

Guaranty § 2.3 states: "The Guarantor's liability under this Guaranty is equal to, and no greater than, Supplier's liability under the Agreement." The Agreement caps each party's liability at "the fees paid or payable in the 12 months preceding the claim" (§ 12.1).

**Why it matters:** If Zeisein's annual spend is, say, $2 million, the maximum recovery under the guaranty for most claims is $2 million. For a catastrophic product failure (e.g., a defective hydraulic power unit causes a multi-story elevator drop), the actual losses could far exceed 12 months of fees. The guaranty was obtained as a condition of the deal (Guaranty Recital C: "Customer would not have entered into the Agreement without this Guaranty"), presumably to protect against exactly this kind of large loss. The cap undermines that purpose.

Note that § 12.2 excludes indemnification obligations, Order Form obligations, confidentiality breaches, gross negligence/fraud/willful misconduct, and payment of Fees from the cap. So the guaranty is uncapped for those items. But for ordinary breach of contract (e.g., failure to supply, warranty breach not rising to gross negligence), the cap applies.

**Recommendation:**
- Negotiate an amendment to Guaranty § 2.3 to state that the Guarantor's liability is not subject to the cap in Agreement § 12.1, or to set a separate, higher cap (e.g., 3× trailing 12-month fees, or a fixed dollar amount).
- At minimum, confirm that the exclusions in § 12.2 are clearly incorporated into the guaranty so there is no argument that the cap applies to indemnification or Order Form obligations.

---

## 7. Service Credit Cap May Be Inadequate for Emergency Failures

**Documents:** `service_level_schedule.md` §§ 5.1, 5.3

The total service credits in any month are capped at 20% of Monthly Fees (§ 5.3). The per-incident credit for a late Emergency Dispatch is 25% or 50% of the part price plus $750 (§ 5.1).

**Why it matters:** For a solenoid coil priced at $168, a 50% credit is $84 + $750 = $834. For a main valve at $2,640, it's $1,320 + $750 = $2,070. If Zeisein's crew is on standby at a building with trapped passengers for 12 hours, the labor cost alone (two technicians at $75/hour = $1,800) exceeds the credit for a solenoid coil failure. The 20% monthly cap means that if multiple emergencies fail in one month, Zeisein's total recovery is limited regardless of actual damages.

Furthermore, SLS § 5.5 states that service credits are "not Customer's only remedy" and preserve termination rights under Agreement § 15.3. But § 15.3 requires the **same** service level to be missed in **three** months within a rolling twelve-month period. If Bruben misses the emergency dispatch standard in January, the on-time delivery standard in February, and the order accuracy standard in March, Zeisein cannot terminate.

**Recommendation:**
- Increase the per-incident standby credit from $750 to a figure that reflects actual crew cost (e.g., $1,500–$2,000).
- Raise the monthly credit cap from 20% to 30–40% of Monthly Fees, or remove the cap for Emergency Order failures specifically.
- Amend Agreement § 15.3 to allow termination if Supplier fails to meet **any** service level (not just the same one) in three months within a rolling twelve-month period, or to add a separate termination right for repeated Emergency Order failures (e.g., two missed Emergency Dispatches in any 60-day period).

---

## 8. Warranty Period "Whichever Ends First" Can Shorten Coverage

**Documents:** `supply_agreement_zeisein_bruben.md` § 9.1

The product warranty runs "for eighteen (18) months after delivery or twelve (12) months after installation, **whichever ends first**."

**Why it matters:** If Zeisein receives a hydraulic power unit in January but does not install it until September (8 months later), the warranty expires 18 months from delivery = July of the following year, which is only 10 months after installation. Zeisein gets less than 12 months of post-installation coverage. For a modernization program where components may be staged at a central warehouse before being deployed to individual sites, this could systematically shorten the effective warranty.

**Recommendation:**
- Change "whichever ends first" to "whichever ends **last**." This gives Zeisein the benefit of the longer period and is a standard formulation in supply agreements where the buyer controls the timing of installation.
- Alternatively, set a fixed warranty period of 24 months from installation, with no delivery-based trigger.

---

## 9. NDA Expires Before the Agreement's Initial Term Ends

**Documents:** `mutual_nda_zeisein_bruben.md` § 7.1; `order_form_mid_atlantic_program.md` § 2.1

The NDA has a 3-year term from January 12, 2026, expiring **January 12, 2029**. The Agreement's Initial Term is 36 months from March 2, 2026, ending **March 2, 2029**. The NDA expires approximately 2 months before the Agreement's initial term ends.

**Why it matters:** The NDA contains a broader definition of Confidential Information than Agreement § 13, specifically calling out "customer, building owner and site information, including the identity and location of elevators maintained or modernized by Zeisein" (NDA § 1.2(d)). After the NDA expires (and its 3-year survival period ends in January 2032), Zeisein's customer list and site data would be protected only under Agreement § 13, which uses the less specific phrase "customer information." While § 13.4 provides that it applies "in addition to" the NDA, the NDA's more detailed enumeration and its specific reference to building owner identity and location provide stronger evidentiary support in a dispute.

**Recommendation:**
- Amend the NDA term to match the Agreement term plus the same survival period, or simply extend the NDA term to 5 years.
- Alternatively, add a sentence to Agreement § 13.1 that expressly incorporates the NDA's definition of Confidential Information (including the customer/building owner/site information category) for the duration of the Agreement.

---

## 10. Volume Rebate Threshold Is Likely Unattainable

**Documents:** `order_form_mid_atlantic_program.md` §§ 3.3, 4.1

The rebate triggers when aggregate purchases in a Contract Year exceed $1,500,000. Zeisein's own estimate is approximately 90 elevators over 36 months (§ 4.1). Based on the product mix in § 1.3, a typical elevator modernization might require one HPU (~$15,000–$20,000), one main valve (~$2,600–$3,200), one controller (~$3,400), one door operator interface (~$1,300), and solenoid coils (~$336) – roughly $22,000–$28,000 per elevator. At 30 elevators per year, annual spend would be approximately $660,000–$840,000, well below the $1.5M threshold.

**Why it matters:** The rebate is effectively illusory based on the stated program scope. It creates an expectation of a financial benefit that Zeisein is unlikely to realize, and it may have influenced the pricing negotiation (i.e., Zeisein may have accepted higher unit prices in part reliance on the rebate).

**Recommendation:**
- Lower the threshold to a level consistent with the program estimate (e.g., $750,000 or $1,000,000 per Contract Year).
- Or restructure as a tiered rebate: 2% above $1M, 4% above $1.5M.
- If Bruben refuses to move, document that the rebate was a material inducement and use it as leverage in other negotiations (e.g., the Critical Parts list or the site indemnity).

---

## 11. Guarantor Has 10 Business Days to Cure After Supplier Default

**Documents:** `bruben_parent_guaranty.md` § 2.2

If Supplier fails to perform a Guaranteed Obligation, the Guarantor has "ten (10) Business Days after Customer's written demand" to pay or perform. For a supply failure, the Guarantor may "procure performance by Supplier or another Affiliate" or "pay Customer the losses."

**Why it matters:** Ten Business Days is two calendar weeks. If Bruben fails to deliver a Critical Part for an emergency entrapment situation, Zeisein cannot wait two weeks for the parent to step in. During that time, the elevator remains out of service, building owner relationships are damaged, and Zeisein may face its own contractual liability to the building owner.

**Recommendation:**
- Shorten the cure period to 3 Business Days for payment obligations and 5 Business Days for performance obligations.
- Add a provision that for failures involving Critical Parts or Emergency Orders, the Guarantor's obligation to perform (not just pay) arises immediately, and Zeisein may procure substitute performance and charge the Guarantor.

---

## 12. No Insurance Requirement Protects Against Zeisein's Site Indemnity Exposure

**Documents:** `supply_agreement_zeisein_bruben.md` § 14; `order_form_mid_atlantic_program.md` § 6.1

Section 14 requires only Supplier to maintain insurance. There is no requirement that Supplier maintain (or that Zeisein be named on) any policy that would respond to claims Zeisein must indemnify under Order Form § 6.1.

**Why it matters:** Zeisein's uncapped site indemnity (Issue 2 above) exposes it to potentially significant liability. If a site condition causes injury to a Bruben employee, Zeisein indemnifies Bruben, but Bruben's workers' comp (which covers its own employees) may not respond if the claim is framed as a third-party claim against Zeisein. There is no contractual mechanism ensuring that Bruben's insurance responds to these claims.

**Recommendation:**
- Add a provision requiring Supplier to maintain (or confirm that its existing policies cover) liability for claims arising from its employees' presence at Program Sites, and that Zeisein is not required to indemnify Supplier for claims that are or should be covered by Supplier's workers' compensation or CGL insurance.
- Alternatively, narrow the site indemnity (see Issue 2) so it does not extend to Supplier's own employees.

---

## Summary Table

| # | Issue | Document(s) | Severity |
|---|-------|-------------|----------|
| 1 | Late price objection – 14% increase deemed accepted | Zeisein letter; Agreement § 5.3 | **Critical** |
| 2 | Uncapped, overbroad site indemnity | Order Form § 6.1; Agreement §§ 12.2(b), 18.2 | **High** |
| 3 | HPUs not Critical Parts – no emergency dispatch | SLS Annex 1; Order Form § 1.3 | **High** |
| 4 | BEC-ST-075 in Annex 1 but no price in Order Form | SLS Annex 1; Order Form § 1.3 | **High** |
| 5 | Exclusivity bars all refurbishing, not just Bruben parts | Agreement § 3.1(c) | **High** |
| 6 | Guaranty subject to 12-month fee cap | Guaranty § 2.3; Agreement § 12.1 | **Medium-High** |
| 7 | Service credit cap and per-incident amounts too low | SLS §§ 5.1, 5.3; Agreement § 15.3 | **Medium** |
| 8 | Warranty "whichever ends first" shortens coverage | Agreement § 9.1 | **Medium** |
| 9 | NDA expires before Agreement initial term | NDA § 7.1; Order Form § 2.1 | **Low-Medium** |
| 10 | Volume rebate threshold unattainable | Order Form §§ 3.3, 4.1 | **Low** |
| 11 | 10-Business-Day guarantor cure period too long | Guaranty § 2.2 | **Medium** |
| 12 | No insurance backstop for Zeisein's site indemnity | Agreement § 14; Order Form § 6.1 | **Medium** |

---

*Please let me know if you would like me to draft proposed amendment language for any of the above.*