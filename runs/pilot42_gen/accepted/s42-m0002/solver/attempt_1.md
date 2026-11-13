# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Timais Outdoor Co. / Pesith Apparel Manufacturing, LLC – Proposed MSA Package: Issue Identification and Recommended Markup

---

## Summary

The package consists of a Master Services Agreement (MSA), a Quality Agreement, a Data Processing Addendum (DPA), and an insurance certificate cover letter from Pesith's broker. Overall, the MSA is reasonably well-drafted and contains several provisions that are favorable to Timais (e.g., zero-tolerance AQL for critical defects, force majeure volume credit, provider bears risk of loss on fulfillment inventory). However, there are several significant issues that need to be addressed before we recommend the client sign. The most critical problems are in the DPA (a one-sided, uncapped indemnity running from Timais to Pesith), the limitation of liability (no carve-out for data breaches), the exclusive remedy clause for nonconforming product, and the term/termination structure (auto-renewal with no post-Initial-Term convenience exit).

---

## Issues (in order of significance)

### 1. DPA Section 8.2 – One-Sided, Uncapped Indemnity from Timais to Pesith

**Where:** DPA, Section 8.2.

**The issue.** Customer (Timais), as Controller, indemnifies Provider (Pesith) for *all* losses, regulatory fines, penalties, and third-party claims "arising out of or relating to any processing of Customer Personal Data performed by Processor on Customer's behalf." The section expressly states this obligation "shall not be subject to any limitation of liability in the Agreement." There is no corresponding indemnity from Pesith to Timais for Pesith's own breach of the DPA.

**Why it matters.** This inverts the standard allocation of data-protection risk. In a typical controller-processor arrangement, the processor indemnifies the controller for losses caused by the processor's breach (e.g., a data breach at the fulfillment center). Here, if Pesith suffers a Security Incident due to its own failure to implement the security measures in Annex 2, and the California Privacy Protection Agency or a class of consumers brings claims against Timais as the "business," Timais would indemnify Pesith for Pesith's own negligence—and that indemnity is uncapped. Meanwhile, Timais's own recovery from Pesith for the same breach is subject to the MSA's 12-month-fee cap (DPA § 8.1 incorporates MSA § 11; MSA § 11.3 does not carve out data-protection obligations).

**Recommended fix.**

- Delete DPA § 8.2 in its entirety, or at minimum limit it to claims arising from Timais's own breach of the DPA or its instructions.
- Add a new § 8.4: "Provider shall defend, indemnify and hold harmless Customer and its Affiliates, officers, directors and employees from and against all losses, damages, regulatory fines and penalties, costs, reasonable attorneys' fees and third-party claims arising out of or relating to (a) a Security Incident caused by Provider's or any Subprocessor's breach of this DPA, (b) Provider's failure to implement or maintain the security measures in Annex 2, or (c) Provider's processing of Customer Personal Data in violation of Section 3.2. This indemnity shall not be subject to the limitation of liability in Section 11 of the Agreement."
- Add "a Party's obligations under the DPA" to the list of exceptions in MSA § 11.3, so that the cap and consequential-damages waiver do not apply to data-protection breaches.

---

### 2. MSA Section 6.2 – Exclusive Remedy for Nonconforming Product

**Where:** MSA, Section 6.2.

**The issue.** Replacement or credit is "Customer's sole and exclusive remedy for Nonconforming Product." Combined with the consequential-damages waiver in § 11.2, Timais cannot recover for lost sales, brand damage, consumer return costs, or expedited re-sourcing costs if a production lot fails.

**Why it matters.** Timais sells technical outdoor apparel (waterproof shells, insulated layers) where quality failures can be severe: a batch of shells that fails the 20,000 mm hydrostatic head spec will generate consumer returns, negative reviews, and potential safety issues. The 24-month warranty in § 6.1 is effectively hollowed out because the only remedy is a credit or replacement—Timais still bears the cost of pulling product from the market, managing consumer complaints, and protecting its brand.

**Recommended fix.**

- Add: "The foregoing shall not limit Customer's rights under Section 13 (Indemnification) or Provider's obligations under the Quality Agreement, and shall not apply where the Nonconformity results from Provider's gross negligence, willful misconduct, or a breach of Section 8.4 (No Unauthorized Production)."
- Alternatively, carve out a scenario-based exception: "Notwithstanding the foregoing, if Provider's failure to conform to Specifications causes Customer to incur (a) consumer return or warranty costs in excess of [threshold], (b) regulatory fines or penalties, or (c) costs of re-sourcing the affected Products, Provider shall be liable for such amounts in addition to the remedies in this Section 6.2."

---

### 3. MSA Sections 11.1–11.3 – Liability Cap Lacks Data Protection and IP Carve-Outs

**Where:** MSA, Section 11.

**The issue.** The cap is 12 months of fees. The exceptions in § 11.3 cover indemnification (§ 13), confidentiality (§ 9), gross negligence/willful misconduct/fraud, and Customer's payment obligations. Notably absent: (a) Provider's breach of the DPA, and (b) Provider's breach of § 8.4 (No Unauthorized Production).

**Why it matters.** A data breach at a fulfillment center handling consumer names, addresses, phone numbers, and order histories could generate regulatory penalties (CCPA allows up to $2,500 per consumer, $7,500 if intentional), consumer notification costs, credit monitoring, and class-action exposure well in excess of 12 months of manufacturing fees. Similarly, if Pesith runs unauthorized overruns of Timais's branded products and sells them, the brand damage and lost revenue could far exceed the cap.

**Recommended fix.**

- Add to § 11.3: "(e) Provider's obligations under the DPA, and (f) Provider's breach of Section 8.4 (No Unauthorized Production)."
- This pairs with the DPA indemnity fix in Issue 1 above.

---

### 4. MSA Section 14.1 – Auto-Renewal for Successive 3-Year Terms with a 30-Day Opt-Out Window

**Where:** MSA, Section 14.1.

**The issue.** After the 3-year Initial Term, the agreement automatically renews for successive 3-year terms. Either party must give notice of non-renewal "no earlier than ninety (90) days and no later than sixty (60) days before the end of the then-current Initial Term or Renewal Term." That is a 30-day window.

**Why it matters.** If Timais's sourcing team misses the window by even one day, it is locked in for another three years with no convenience termination right (see Issue 5). For a fashion-adjacent outdoor brand whose product lines, volume needs, and margin targets shift, a 3-year lock-in with a 30-day opt-out is operationally risky.

**Recommended fix.**

- Extend the notice window: "no earlier than one hundred eighty (180) days and no later than ninety (90) days before the end of the then-current term."
- Alternatively, shorten the renewal term from 3 years to 1 year.
- Add: "Customer may terminate for convenience on one hundred eighty (180) days' notice at the end of any Renewal Term, without penalty, provided Customer has met the Minimum Volume Commitment for the then-current Contract Year."

---

### 5. MSA Section 14.3 – No Convenience Termination After the Initial Term

**Where:** MSA, Section 14.3.

**The issue.** The convenience termination right (180 days' notice) is available only "During the Initial Term." After year 3, Timais has no right to exit except for cause under § 14.2.

**Why it matters.** This compounds the auto-renewal issue. If Timais wants to transition to a different manufacturer or bring fulfillment in-house after the Initial Term, it must either (a) wait for the narrow non-renewal window or (b) prove a material breach. There is no "walk-away" right.

**Recommended fix.**

- Make the convenience termination right available throughout the Term, not just the Initial Term. If Pesith resists, at minimum allow convenience termination at the end of each Renewal Term (paired with the expanded opt-out window in Issue 4).
- Reduce the notice period from 180 to 120 days, and clarify that the raw-material buyout obligation in § 14.3 is limited to materials with a shelf life of less than 12 months (to avoid Timais paying for fabric that Pesith can use for other customers).

---

### 6. MSA Section 5.4 – Inadequate Remedy for Late Delivery

**Where:** MSA, Section 5.4.

**The issue.** If Provider is more than 10 days late, Customer's only options are (a) expedited freight at Provider's cost or (b) cancellation of the late portion. There is no service credit, no liquidated damages, and no right to source elsewhere and charge back the differential.

**Why it matters.** Outdoor apparel is seasonal. A 120-day lead time (Section 4.3) means a delay of even 3–4 weeks can push delivery past the peak selling window. The 10-day grace period before any remedy kicks in is generous, and the available remedies (expedited freight or partial cancellation) do not compensate Timais for lost revenue or the cost of air-freighting a replacement from an alternate supplier.

**Recommended fix.**

- Add a service credit: "For each day of delay beyond the tenth (10th) day, Provider shall pay Customer a service credit equal to [0.5%–1%] of the Fees for the affected Purchase Order, up to a maximum of [10%–15%] of such Fees."
- Add: "If the delay exceeds thirty (30) days, Customer may, in addition to the foregoing, source the affected Products from an alternate supplier and charge Provider the difference between the alternate cost and the Fees under the affected Purchase Order."

---

### 7. Quality Agreement Section 5.2 – 30-Day Rejection Period May Be Too Short for Latent Defects

**Where:** Quality Agreement, Section 5.2.

**The issue.** Customer must reject Nonconforming Product within 30 days after delivery (or after recording into fulfillment inventory). The MSA warranty in § 6.1 runs for 24 months, but the rejection mechanism in the Quality Agreement is the operative procedure for identifying and returning nonconforming goods.

**Why it matters.** Some defects in technical outerwear are latent: seam tape delamination, DWR failure, or membrane pinholes may not be apparent until after 30 days of wear or laundering. The Specifications in MSA Schedule A (e.g., "no delamination or lifting after twenty (20) home launderings," "minimum spray rating of 80 after twenty (20) home launderings") imply performance over time, not just at delivery. A strict 30-day rejection window undercuts the 24-month warranty.

**Recommended fix.**

- Add: "Notwithstanding the foregoing, Customer may reject Product at any time during the warranty period in Section 6.1 of the MSA if the Nonconformity is a latent defect that could not reasonably have been discovered within thirty (30) days after delivery, including defects relating to waterproofing, breathability, seam tape adhesion, or DWR performance as specified in Schedule A of the MSA."
- Alternatively, extend the general rejection period to 60 days and add the latent-defect carve-out.

---

### 8. Schedule B and Schedule C – Incomplete / Placeholder

**Where:** MSA, Schedule B (page 4) and Schedule C (page 5).

**The issue.** Schedule B states that "Unit pricing, Fulfillment Services rates, minimum annual unit volumes per Product category and the per-unit shortfall rate are set out in the pricing table attached to this Schedule B, as agreed by the Parties in writing." No table is attached. Schedule C provides only two service levels (99% ship-out within 2 business days; 99.5% inventory accuracy) and does not specify the service level credits referenced in MSA § 6.3.

**Why it matters.** Without the actual numbers, we cannot assess: (a) the financial exposure under the Minimum Volume Commitment (§ 4.4), (b) whether the pricing is competitive, (c) what the shortfall rate is, or (d) what the service level credits for fulfillment are. MSA § 6.3 promises "service level credits stated in Schedule C," but Schedule C contains none.

**Recommended fix.**

- Before signing, require the completed Schedule B pricing table and minimum volume commitments. Flag to the client that the shortfall fee is a real financial obligation and should be negotiated with reference to Timais's actual demand forecast.
- Add to Schedule C: a table of service levels with corresponding credits (e.g., if ship-out accuracy falls below 99%, credit of $X per order; if inventory accuracy falls below 99.5%, credit of $Y per discrepancy). This gives § 6.3 teeth.

---

### 9. MSA Section 4.4 – Minimum Volume Commitment and Shortfall Fee

**Where:** MSA, Section 4.4.

**The issue.** Customer must issue POs for not fewer than the minimum annual unit volumes per Product category, or pay a shortfall fee (units short × per-unit rate in Schedule B) within 45 days after the Contract Year ends.

**Why it matters.** This is a take-or-pay obligation. If Timais's sales underperform or it pivots its product mix, it still owes the shortfall. The force majeure provision (§ 15.1) protects Timais only if *Provider* is the one hit by FM. There is no corresponding protection if Timais's own demand is disrupted (e.g., a retail partner cancels, a weather pattern shifts demand).

**Recommended fix.**

- Negotiate the minimum volumes to be well below Timais's expected demand (e.g., 60–70% of forecast) to build in a buffer.
- Add: "The Minimum Volume Commitment shall be reduced by any volumes that Customer was unable to order due to (a) Provider's failure to deliver within the agreed lead time, (b) a force majeure event affecting Customer's sales channels, or (c) Provider's breach of the Quality Agreement that results in rejection of more than [X]% of a Lot."
- Consider a cap on the shortfall fee (e.g., not to exceed [X]% of the annual Fees).

---

### 10. Insurance Certificate – Property Coverage "As Scheduled"

**Where:** Broker cover letter, Section 2.1 (row for MSA § 12.1(b)); MSA, Section 12.1(b).

**The issue.** The MSA requires property insurance covering Customer's goods "at full replacement value." The certificate states "Full replacement value, as scheduled." We have not seen the schedule.

**Why it matters.** If the scheduled amount is less than the actual value of Timais's inventory in Pesith's fulfillment center (which could be substantial for a DTC brand holding weeks of stock), there is an underinsurance gap. In a fire or flood, Timais could lose inventory that is not fully covered.

**Recommended fix.**

- Request the property insurance schedule and confirm the stated value equals or exceeds the expected peak inventory value at the fulfillment center.
- Add to MSA § 12.2: "Provider shall notify Customer in writing if the scheduled value of property insurance falls below the then-current replacement value of Customer's goods in Provider's care, custody or control, and shall increase coverage to full replacement value within thirty (30) days."

---

### 11. MSA Section 3.5 / Quality Agreement Section 8.3 – Audit Rights

**Where:** MSA, Section 3.5; Quality Agreement, Section 8.3.

**The issue.** Timais may audit Provider's facilities "on reasonable notice during normal business hours." The Quality Agreement cross-references this for quality system audits. There is no specification of how much notice is "reasonable," no cap on the number of audits per year, and no right to audit during a suspected quality crisis on shorter notice.

**Why it matters.** If Timais receives a spike in consumer returns suggesting a systemic quality issue, it needs to get on the floor quickly. "Reasonable notice" is ambiguous and could be stretched by Provider.

**Recommended fix.**

- Add: "Notwithstanding the foregoing, Customer may audit on forty-eight (48) hours' notice if Customer has reasonable grounds to suspect a material quality issue, Security Incident, or compliance violation. Customer may conduct up to two (2) routine audits per Contract Year on ten (10) business days' notice, and additional audits as reasonably necessary following a failed FRI, a rejected Lot, or a Security Incident."

---

### 12. DPA Section 7.1 – 48-Hour Security Incident Notification

**Where:** DPA, Section 7.1.

**The issue.** Provider must notify Customer "without undue delay, and in any event within forty-eight (48) hours" of becoming aware of a Security Incident.

**Why it matters.** 48 hours is acceptable but on the longer end. CCPA and several state breach-notification laws require prompt notification to the affected business. If Pesith discovers a breach on a Friday evening and waits until Monday morning (48 hours), Timais's own clock to notify consumers and regulators may already be running.

**Recommended fix.**

- Tighten to 24 hours: "Provider shall notify Customer without undue delay, and in any event within twenty-four (24) hours, after becoming aware of a Security Incident or reasonable suspicion of a Security Incident."
- Add "or reasonable suspicion" so that Provider cannot delay notification while it determines whether an event qualifies as a "Security Incident."

---

## Open Questions / Additional Facts Needed

1. **Schedule B pricing table.** We need the actual unit prices, fulfillment rates, minimum volumes, and shortfall rate to complete the economic analysis. Is there a draft or term sheet from Pesith?

2. **Expected inventory value in fulfillment.** What is Timais's projected peak inventory value (in units and dollars) that will sit in Pesith's fulfillment center? This drives the insurance schedule review (Issue 10) and the property insurance adequacy question.

3. **Demand forecast and Minimum Volume Commitment.** What is Timais's 12-month demand forecast by product category? We need this to assess whether the minimum volume commitment (once Schedule B is populated) is realistic and to model the shortfall fee exposure.

4. **Current fulfillment arrangement.** Is Timais currently using a different 3PL or in-house fulfillment? If so, what are the current service levels and costs? This gives us a benchmark for the Schedule C service levels and credits.

5. **Data volume.** Approximately how many consumer orders per month will flow through Pesith's fulfillment center? This helps calibrate the data-breach risk and the adequacy of the $2M cyber policy limit.

6. **PFAS / chemical restrictions.** Schedule A, Section A.4 references "applicable PFAS restrictions." Does Timais have a specific PFAS-free commitment (e.g., no PFC-based DWR) that should be spelled out in the Specifications or the Quality Agreement? The current language is generic and may not give Timais a clear rejection right if Provider uses a restricted chemistry.

7. **Subprocessor list (DPA Annex 3).** The annex references a "subprocessor table attached" but no table is provided. We need the actual list of carriers, WMS vendors, and hosting providers to assess data-flow risk.