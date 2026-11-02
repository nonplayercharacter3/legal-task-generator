# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Keisaiv Therapeutics, Inc. – Review of Kedoul Specialty Logistics Contract Set: Identified Issues and Recommended Fixes

---

## Summary

I have reviewed the Master Services Agreement ("**MSA**"), Data Processing Addendum ("**DPA**"), GDP Quality Agreement ("**QA**"), Service Level Schedule ("**SLS**"), and the Velnorix Launch Kickoff Meeting Notes ("**Meeting Notes**"). I have identified **twenty-three (23) issues** where Keisaiv's position is weak, unclear, or internally inconsistent within the contract set. They are ordered below from most to least significant. Items requiring client confirmation or additional documents are flagged at the end.

---

## Tier 1 – Critical Issues

### Issue 1: Conflicting Definitions of "Temperature Excursion"

**Where:** MSA § 1.14 vs. QA § 1.9; order of precedence in MSA § 16.4.

**The problem.** The MSA defines "Temperature Excursion" as "any deviation, **of any duration**, outside the 2°C to 8°C labeled storage range." The QA defines it as "any deviation outside the 2°C to 8°C labeled storage range **lasting more than sixty (60) consecutive minutes**, as recorded by a qualified temperature monitoring device." These are materially different standards. A 30-minute excursion is a Temperature Excursion under the MSA but not under the QA.

MSA § 16.4 provides that the QA "shall govern with respect to quality, storage and handling matters." It is therefore likely that the QA's 60-minute definition controls for quality and storage purposes (notification under QA § 5.5, quarantine, the SLS § 3.5 service level). However, MSA § 9.3 (Product Loss) uses the term "Temperature Excursion" without specifying which definition applies. If the QA definition controls there as well, Provider would owe no replacement cost for product compromised by a 30-minute excursion—despite the fact that for a refrigerated biologic, even a brief excursion may render product unusable.

**Why it matters.** Velnorix is a biologic. Protein-based products can denature at temperatures above 8°C even for short periods. If the 60-minute threshold controls, Keisaiv could lose product to a 45-minute excursion with no contractual recourse under § 9.3, no quarantine obligation under QA § 5.5, and no service credit under SLS § 3.5.

**Recommended fix.** Harmonize the definitions. I recommend adopting the MSA's "any duration" standard throughout, or at minimum carving MSA § 9.3 out of the QA's precedence so that the broader MSA definition applies to product loss. Proposed language for MSA § 9.3:

> "For purposes of this Section 9.3, 'Temperature Excursion' has the meaning set out in Section 1.14 of this Agreement."

Alternatively, if the 60-minute threshold is scientifically justified (e.g., stability data shows product is stable for up to 60 minutes at 9–10°C), the QA definition should be used everywhere, but Keisaiv should confirm with its quality and stability teams that 60 minutes is a safe threshold before agreeing.

**Client confirmation needed:** Does Keisaiv's stability data support a 60-minute excursion threshold, or is any deviation from 2–8°C potentially product-impacting?

---

### Issue 2: Summer Temperature Mapping Not Complete Before First Commercial Shipment

**Where:** QA § 4.1; Meeting Notes § 3.1.

**The problem.** QA § 4.1 requires Provider to complete "installation, operational and performance qualification of the refrigerated storage areas," including "a temperature mapping study under **both summer and winter conditions**," before storing Velnorix. The Meeting Notes confirm that only the winter profile is complete; the summer mapping "will be issued after the scheduled summer study." The target first commercial shipment date is April 15, 2024 (Meeting Notes § 2.2).

**Why it matters.** Storing Velnorix at a facility that has not completed full performance qualification is a deviation from the QA and potentially from Applicable GDP Requirements (QA § 1.1, incorporating USP <1079>). If a temperature-related product failure occurs before the summer mapping is complete, Keisaiv could face regulatory scrutiny (FDA may question how the facility was validated for summer conditions) and would have a harder time establishing that Provider breached the QA, since the qualification was still "in progress" per the parties' own meeting.

**Recommended fix.**
- Add a condition precedent to the initial SOW: no Velnorix inventory shall be received at the Memphis Facility until the summer temperature mapping is complete and accepted by Client's Quality Unit.
- Alternatively, if business timing requires earlier receipt, add a specific provision that Provider warrants the winter mapping is sufficient for the April–September period and that any excursion occurring before the summer mapping is complete shall be treated as a Deviation under QA § 8.1 regardless of duration.
- Escalate internally: confirm with Keisaiv Quality whether the winter mapping provides adequate assurance for spring/summer storage.

**Client confirmation needed:** Can Keisaiv delay first receipt until summer mapping is complete, or is the April 15 date immovable? If immovable, what is the risk acceptance?

---

### Issue 3: No Termination for Convenience; Narrow Non-Renewal Window; Exclusivity Lock-In

**Where:** MSA §§ 2.4, 12.1, 12.2, 12.3.

**The problem.** Three features compound to create a significant lock-in risk:

1. **No termination for convenience.** Keisaiv's only exit rights are termination for material breach (30-day cure, § 12.3), insolvency (§ 12.4), and regulatory trigger (§ 12.5). If Provider consistently underperforms but does not commit a "material breach" (e.g., misses service levels but stays within the cure period, or provides sub-par but not negligent service), Keisaiv has no exit.

2. **Auto-renewal with a 30-day notice window.** MSA § 12.2 provides that the agreement auto-renews for successive 3-year terms unless either party gives notice of non-renewal "no earlier than 210 days and no later than 180 days prior to expiration." A notice delivered on day 179 is "of no force or effect." Missing this 30-day window locks Keisaiv in for another three years.

3. **Exclusivity.** MSA § 2.4 makes Provider the exclusive logistics and hub services provider for all Covered Products worldwide during the Term (including renewal terms). Keisaiv cannot engage any alternative provider even if it wanted to run a parallel operation during a transition.

**Why it matters.** For a new product launch, Keisaiv has limited visibility into whether Kedoul will perform well over a 36-month (or longer) horizon. If the product's commercial trajectory changes, if Keisaiv is acquired, or if Kedoul's service quality deteriorates without crossing the "material breach" threshold, Keisaiv is contractually trapped. The exclusivity also prevents Keisaiv from developing a backup logistics capability.

**Recommended fixes.**
- **Add a termination for convenience right** exercisable by Keisaiv on 180 days' written notice after the first 12 months of the Initial Term. Proposed language:

  > "12.8 Termination for Convenience. After the first twelve (12) months of the Initial Term, Client may terminate this Agreement or any Statement of Work for convenience upon one hundred eighty (180) days' prior written notice to Provider. Upon such termination, Client shall pay all undisputed Fees for Services performed through the effective date of termination and any reasonable, documented transition costs incurred by Provider."

- **Widen the non-renewal notice window** to 90–180 days (i.e., notice may be given any time from 180 to 90 days before expiration). This gives Keisaiv a 90-day decision window rather than 30 days.

- **Carve out the exclusivity** to permit Keisaiv to engage an alternative provider if Provider is in uncured material breach, or to permit a limited parallel operation for the purpose of qualifying a successor provider during a transition period.

---

### Issue 4: Recall Costs Not Clearly Allocated When Provider Is at Fault

**Where:** QA § 7.2; MSA §§ 9.3, 13.2(a).

**The problem.** QA § 7.2 provides that "Client shall direct all recalls and market withdrawals" and Provider shall "support" the recall. MSA § 9.3 covers Provider's obligation to bear "replacement cost" of lost, damaged, or excursion-affected product. MSA § 13.2(a) has Client indemnify Provider for product liability claims "except to the extent caused by Provider's handling of Velnorix."

However, the **costs of executing a recall**—consignee notification, reverse logistics, product retrieval, destruction, regulatory reporting support, and potential patient notification—are not explicitly allocated to Provider when the recall is triggered by Provider's error (e.g., shipping in an unqualified configuration, a temperature excursion in Provider's custody, or a serialization failure). MSA § 9.3 covers "replacement cost" of affected units, but a recall involves far more than replacing the units: it includes the operational cost of pulling product from the market, which can be substantial for a specialty biologic distributed to sites of care nationwide.

**Why it matters.** If a recall is necessitated by Provider's handling error, Keisaiv could bear seven- or eight-figure recall execution costs with no clear contractual right to recover them from Provider. The indemnification in § 13.1(a) (breach of the QA) and § 13.1(c) (violation of Applicable Law) may cover third-party claims, but the direct operational costs of the recall itself (internal labor, reverse logistics, destruction) are not "third-party claims."

**Recommended fix.** Add a specific recall cost allocation provision. Proposed language as a new QA § 7.4:

> "7.4 Recall Costs. If a recall or market withdrawal is initiated as a result of Provider's breach of this Quality Agreement, negligence, or violation of Applicable Law, Provider shall bear or reimburse Client for all reasonable and documented costs of the recall, including but not limited to: (a) reverse logistics and freight; (b) product destruction or reprocessing; (c) consignee and patient notification; (d) regulatory reporting support; and (e) Client's internal labor costs directly attributable to the recall. This obligation is in addition to, and not in lieu of, Provider's obligations under Section 9.3 of the Agreement."

---

## Tier 2 – Significant Issues

### Issue 5: Service Credit Cap of 10% of Monthly Fees Is Inadequate

**Where:** SLS § 5.3.

**The problem.** Total service credits in any month are capped at 10% of Monthly Fees. For a specialty biologic where a single shipping configuration failure (SLS § 3.4) or adverse event forwarding failure (SLS § 3.9) could result in product loss, patient harm, or regulatory action, 10% of monthly logistics fees is a modest financial remedy. While SLS § 5.4 and MSA § 3.2 preserve Keisaiv's right to claim material breach, the practical effect is that for non-material failures, Keisaiv's automatic remedy is limited.

**Why it matters.** The cap creates an asymmetry: Provider's financial exposure for poor performance is limited, while Keisaiv's exposure (product loss, regulatory risk, patient harm) is not. This weakens the incentive for Provider to invest in performance.

**Recommended fix.** Increase the cap to 20–25% of Monthly Fees, or remove the cap for the most critical service levels (Shipping Configuration Compliance § 3.4, Temperature Excursion Notification § 3.5, and Adverse Event Forwarding § 3.9). Proposed language:

> "5.3 Cap. The total service credits for any Measurement Period shall not exceed twenty-five percent (25%) of Monthly Fees for the affected month. Notwithstanding the foregoing, no cap shall apply to service credits under Sections 3.4, 3.5 or 3.9 of this Schedule."

---

### Issue 6: Forecast-Based SLA Exclusion Creates a Perverse Incentive

**Where:** SLS § 6.1(c); MSA § 5.1.

**The problem.** A Service Level Failure is "excused" if order volume in a month exceeds 125% of Client's most recent forecast, unless Provider agreed in writing to support that volume. MSA § 5.1 makes the forecast "non-binding."

For a new product launch, volume forecasting is inherently uncertain. If Velnorix launches successfully and demand exceeds forecast by even 25%, Provider's service levels are excused for the entire month. This means that in the best-case scenario for Keisaiv (high demand), Provider has no contractual incentive to meet service levels.

**Why it matters.** Keisaiv could see its most critical growth period coincide with a period of excused underperformance. Patients and providers would experience delayed shipments, missed calls, and slow benefits verification precisely when volume is highest.

**Recommended fix.** Raise the threshold to 150% or 200%, or limit the exclusion to specific service levels (e.g., Order Fulfillment § 3.1) rather than all service levels. Alternatively, require that the forecast be updated monthly (as MSA § 5.1 already provides) and that the exclusion apply only if the volume exceeds 125% of the **most recently updated** forecast (not the original launch forecast). Proposed language:

> "6.1(c) an order volume in a Measurement Period exceeding one hundred fifty percent (150%) of Client's most recently updated forecast under Section 5.1 of the Agreement, unless Provider agreed in writing to support that volume."

---

### Issue 7: Governing Law and Jurisdiction Conflict Between MSA and DPA

**Where:** MSA §§ 16.1–16.2 (New York law; New York County courts) vs. DPA §§ 12.1–12.2 (Delaware law; Delaware courts).

**The problem.** The MSA is governed by New York law with exclusive jurisdiction in New York County. The DPA is governed by Delaware law with exclusive jurisdiction in Delaware courts. MSA § 16.4 provides that the DPA "shall govern with respect to Personal Data." This creates a split: a dispute involving both data protection and logistics performance (e.g., a data breach caused by a logistics system failure) could implicate both regimes, and the parties could litigate in different forums under different laws.

**Why it matters.** In a Security Incident involving both a HIPAA breach and a product handling failure, Keisaiv could face the cost and complexity of parallel proceedings in two jurisdictions. The split also creates interpretive uncertainty: which law governs the interaction between the DPA's liability provisions and the MSA's limitation of liability?

**Recommended fix.** Conform the DPA to the MSA's governing law and forum (New York). If Kedoul insists on Delaware (perhaps for its own corporate reasons), at minimum add a provision that in the event of a conflict, the MSA's forum selection clause controls for integrated disputes. Proposed language for DPA § 12:

> "12.1 This DPA is governed by and construed in accordance with the laws of the State of New York, without regard to its conflict of laws principles.
> 12.2 Each Party irrevocably submits to the exclusive jurisdiction of the state or federal courts located in New York County, New York for any action arising out of or relating to this DPA or the Processing of Personal Data."

---

### Issue 8: 30-Day Cure Period Inappropriate for Product Safety Breaches

**Where:** MSA § 12.3.

**The problem.** Termination for material breach requires 30 days to cure. For breaches involving product safety (e.g., repeated temperature excursions, failure to quarantine, shipping in unqualified configurations), a 30-day cure period means Keisaiv must continue to allow Provider to handle its biologic product for up to 30 days after discovering a material safety failure before it can terminate.

**Why it matters.** If Provider has a systemic cold chain failure, every day of continued performance risks additional product loss and potential patient harm. Keisaiv should be able to terminate immediately for product safety breaches.

**Recommended fix.** Carve out product safety breaches from the cure period. Proposed language:

> "12.3 Termination for Cause. Either Party may terminate this Agreement or any Statement of Work by written notice if the other Party materially breaches this Agreement and fails to cure the breach within thirty (30) days after receiving written notice describing it; **provided that no cure period shall apply to a material breach involving (a) a Temperature Excursion that results in product loss or patient harm, (b) Provider's failure to quarantine product as required by the Quality Agreement, or (c) Provider's shipment of Velnorix in an unqualified shipping configuration.**"

---

### Issue 9: DPA Liability Cap May Undercover Data Breach Costs

**Where:** DPA § 11.3; MSA §§ 14.1–14.2.

**The problem.** DPA § 11.3 states that "Each Party's liability under this DPA is subject to Section 14 of the Agreement." MSA § 14.2 caps aggregate liability at 24 months of fees, with exclusions for §§ 9.3, 10, 13, and gross negligence/willful misconduct. MSA § 13.1(d) indemnifies Client for "any unauthorized use or disclosure of Personal Data in Provider's possession or control," which is uncapped.

However, § 13.1 is framed as indemnification for "third-party claims." If HHS OCR imposes a civil monetary penalty on Keisaiv for a HIPAA violation caused by Provider's data breach, that penalty is arguably a "third-party claim" (the regulator being the third party). But if the cost is Keisaiv's own internal remediation (e.g., re-platforming its data systems, enhanced monitoring for its own patients) that is not triggered by a third-party claim, it may fall within the 24-month cap.

**Why it matters.** A major data breach involving patient PHI could result in regulatory fines, class action exposure, and internal remediation costs well in excess of 24 months of logistics fees. The current structure may leave Keisaiv bearing the excess.

**Recommended fix.** Add DPA-specific liability carve-outs. Proposed language as a new DPA § 11.4:

> "11.4 Uncapped Liability. Notwithstanding Section 14 of the Agreement, Provider's liability shall not be subject to any cap or exclusion for: (a) regulatory fines, penalties or assessments imposed on Client as a result of Provider's breach of this DPA or Data Protection Laws; (b) Client's reasonable costs of remediation, re-platforming, or enhanced monitoring necessitated by a Security Incident caused by Provider or its Subprocessors; or (c) Provider's gross negligence or willful misconduct in connection with the Processing of Personal Data."

---

### Issue 10: Approved Subprocessors Not Specifically Identified in DPA

**Where:** DPA Annex C; MSA § 7.2.

**The problem.** Annex C lists subprocessors as "Kedoul Specialty Logistics, LLC Affiliates **(as identified in the initial Statement of Work)**" and "Cloud hosting provider **(as identified in the initial Statement of Work)**." No actual entity names appear in the DPA. The initial SOW is not in the matter folder.

**Why it matters.** DPA § 6.1 requires Client's prior written consent for subprocessors, and Annex C is supposed to list those approved as of the Effective Date. If the entities aren't named, it is unclear who is actually approved. This creates ambiguity about whether Provider is in compliance with the subprocessor consent requirement. It also makes it harder to assess the security posture of the actual entities processing Keisaiv's patient data.

**Recommended fix.** Require that Annex C be amended to name the specific legal entities (including full legal names, locations, and the specific data they will process). If the SOW identifies them, incorporate that identification by reference with the specific names stated. Additionally, require 30 days' prior written notice (rather than just consent) for any proposed change to the subprocessor list, with a right of objection.

**Additional document needed:** The initial Statement of Work to confirm which entities are actually identified.

---

## Tier 3 – Moderate Issues

### Issue 11: No Service Level for Inbound Receipt or Quarantine Turnaround

**Where:** SLS § 1.2 (scope); QA § 5.2.

**The problem.** The SLS covers outbound shipments and Hub Services but has no service level for inbound receipt processing or the time from receipt to quarantine release. QA § 5.2 requires product to remain in Quarantine until receipt is complete and Client releases the Lot. If Provider's receipt processing is slow, product sits in quarantine longer, reducing available inventory for outbound shipment—yet no SLA captures this.

**Recommended fix.** Add a service level for inbound receipt: e.g., "Provider shall complete receipt verification (including DSCSA checks and in-transit temperature review) within two (2) Business Days of physical receipt of a shipment." Service credit: 1% of Monthly Fees.

---

### Issue 12: No Service Level for Temperature Monitoring System Uptime

**Where:** QA § 4.3; SLS (no corresponding provision).

**The problem.** QA § 4.3 requires "continuous" temperature monitoring. But if the monitoring system is offline for 4 hours, there is no specific SLA violation, no service credit, and it is unclear whether the gap constitutes a "Deviation" under QA § 1.4. The SLS has no uptime standard for monitoring systems.

**Recommended fix.** Add to the SLS: "Temperature Monitoring Uptime. Provider shall maintain temperature monitoring systems with at least 99.5% uptime per calendar month, measured as the percentage of hours in which all storage area sensors are actively recording and transmitting data. Downtime exceeding 4 consecutive hours shall be reported to Client's Quality Unit within 1 hour of restoration." Service credit: 2% of Monthly Fees.

---

### Issue 13: Vague Standard of Performance

**Where:** MSA § 6.1.

**The problem.** Provider's standard of performance is "a professional and workmanlike manner, consistent with good distribution practices and the standards of care generally observed by **leading specialty pharmaceutical logistics providers** in the United States." The reference to "leading" providers is subjective and would be difficult to prove in a dispute.

**Recommended fix.** Replace with an objective benchmark: "consistent with the standards set forth in the Quality Agreement, the GDP requirements identified in Section 1.1 of the Quality Agreement, and the service levels in the Service Level Schedule." This ties the standard to specific, measurable obligations rather than an amorphous peer group.

---

### Issue 14: "Emergency Change" Exception Undefined

**Where:** QA § 8.3.

**The problem.** Provider may implement an "Emergency Change" immediately with notice within 1 Business Day. There is no definition of what constitutes an emergency. Provider could characterize a non-urgent change (e.g., switching carriers, modifying a shipping configuration) as an "emergency" to bypass the 60-day advance notice and Client approval requirement.

**Recommended fix.** Define "Emergency Change" narrowly: "A Change that, if not implemented immediately, would create an imminent risk of loss of, or damage to, Velnorix in Provider's custody, or would cause a Facility to operate outside its qualified parameters." Require that Provider document the emergency rationale and provide it to Client with the post-implementation notice.

---

### Issue 15: Fee Adjustment Without Corresponding Exit Right

**Where:** MSA § 4.4.

**The problem.** Provider may increase fees annually by up to the lesser of 3% or CPI, on 90 days' notice. If Keisaiv disagrees with the increase, it has no right to terminate. It must either accept the increase or risk being in breach for non-payment.

**Recommended fix.** Add: "If Client does not accept a Fee adjustment under this Section 4.4, Client may terminate the affected Statement of Work upon sixty (60) days' written notice, effective as of the date the adjustment would otherwise take effect, without penalty."

---

### Issue 16: Transition Assistance Period May Be Insufficient

**Where:** MSA § 12.6.

**The problem.** Transition assistance is limited to 180 days. For a specialty biologic requiring cold chain qualification, shipping configuration validation, hub staff retraining, and data migration, 180 days may be insufficient—particularly if Keisaiv must qualify a new provider's facility from scratch (IQ/OQ/PQ, temperature mapping, carrier qualification).

**Recommended fix.** Extend to 270 days, or provide that the period shall be such as is reasonably necessary to complete transition, not to exceed 365 days. Also specify that transition rates shall not exceed the rates in effect during the last 6 months of the Term (to prevent Provider from inflating transition pricing).

---

### Issue 17: Exclusivity Binds Affiliates Without Affiliate Consent

**Where:** MSA § 2.4.

**The problem.** "Client shall cause its Affiliates to comply with this Section 2.4 as if they were parties to this Agreement." If Keisaiv acquires a company that has its own logistics arrangements, that affiliate is immediately bound by Keisaiv's exclusivity to Kedoul. This could create integration challenges in M&A and limits commercial flexibility.

**Recommended fix.** Limit the affiliate obligation to Affiliates that are "under common control with Client as of the Effective Date" or add: "provided that Client shall not be required to cause an Affiliate acquired after the Effective Date to comply with this Section 2.4 if such Affiliate had an existing logistics arrangement in place prior to acquisition, for a transition period of up to twelve (12) months."

---

### Issue 18: No Fallback for Data Return Format Disagreement

**Where:** DPA § 10.1(a).

**The problem.** Upon termination, Personal Data is returned "in a mutually agreed format." If the parties cannot agree, there is no mechanism to resolve the deadlock. This could delay transition of patient data to a successor hub vendor.

**Recommended fix.** Add: "If the Parties cannot agree on a format within fifteen (15) days of Client's request, Provider shall return the data in the format in which it is currently stored, together with a data dictionary sufficient for Client or its designee to interpret the data."

---

### Issue 19: MSA § 9.3 "Defect in Velnorix" Exclusion Is Overbroad

**Where:** MSA § 9.3.

**The problem.** Provider's product loss obligation is excluded to the extent loss "results from... a defect in Velnorix existing at the time Provider accepted delivery." This could be invoked by Provider to argue that product degradation (e.g., protein aggregation) is an inherent "defect" rather than the result of Provider's handling, particularly if the Temperature Excursion definition conflict (Issue 1) means shorter excursions don't trigger the QA's quarantine protocol.

**Recommended fix.** Narrow the exclusion: "a defect in Velnorix **that is identified in Client's Lot release documentation or that is confirmed by Client's Quality Unit to have existed at the time of acceptance**." This prevents Provider from unilaterally characterizing product degradation as a pre-existing defect.

---

### Issue 20: SLS § 7.2 Material Breach Trigger Requires Three Failures in 12 Months

**Where:** SLS § 7.2.

**The problem.** A Service Level Failure of the most critical standards (Shipping Configuration § 3.4, Temperature Excursion Notification § 3.5, Adverse Event Forwarding § 3.9) constitutes a material breach only if it occurs in "any three (3) Measurement Periods within a rolling twelve (12) month period." This means Provider could fail to notify a temperature excursion in January, fail again in March, and fail again in May—and still not be in material breach until the third failure. In the interim, Keisaiv has no termination right.

**Recommended fix.** For SLS § 3.5 (Temperature Excursion Notification) and § 3.9 (Adverse Event Forwarding), reduce the threshold to two (2) failures in a rolling twelve-month period. Alternatively, provide that any single failure of § 3.4 (Shipping Configuration Compliance) that results in confirmed product loss or patient harm constitutes an immediate material breach.

---

### Issue 21: No Provision Addressing Provider's Financial Distress Short of Insolvency

**Where:** MSA § 12.4.

**The problem.** Termination for financial distress is available only upon insolvency, assignment for benefit of creditors, or bankruptcy/receivership. If Provider is experiencing severe financial difficulty (e.g., missing vendor payments, reducing staff, delaying equipment maintenance) but has not yet filed for bankruptcy, Keisaiv has no contractual trigger to act.

**Recommended fix.** Add: "Client may terminate this Agreement if Provider (a) fails to pay its employees or critical vendors for thirty (30) or more days, (b) receives a material adverse change notice from its lenders, or (c) otherwise demonstrates an inability to perform the Services, in each case as determined by Client in good faith based on reasonable evidence."

---

### Issue 22: Meeting Notes Reveal Open Items That Undermine Launch Readiness

**Where:** Meeting Notes § 9 (Action Items).

**The problem.** As of the March 12 kickoff, the following items remained open with due dates before or around the April 15 launch:
- Summer temperature mapping (no due date stated; will be after launch)
- Business continuity plan delivery (due March 22)
- 24-hour alarm contact confirmation (due March 19)
- SOC 2 Type II report delivery (due March 29)
- Security incident contact confirmation (due March 19)
- Disposition decision request template (due March 22)

If any of these were not completed by the launch date, Keisaiv would be operating with incomplete quality infrastructure. The contracts do not impose specific consequences for failure to complete these pre-launch items.

**Recommended fix.** Confirm status of each action item. For any that were not completed by April 15, document the gap and require a remediation timeline. Consider adding a "Launch Readiness" exhibit to the initial SOW that lists required preconditions and provides that failure to meet them constitutes a Deviation under the QA.

---

### Issue 23: MSA § 16.7 Force Majeure Carve-Out Is Narrow

**Where:** MSA § 16.7.

**The problem.** Force majeure "does not excuse Provider's obligations to maintain temperature-controlled storage, backup power and business continuity measures required by the Quality Agreement." This is appropriate in principle, but the carve-out is limited to obligations "required by the Quality Agreement." If Provider's MSA obligations (e.g., serialization under § 6.3, adverse event forwarding under § 6.4) are interrupted by a force majeure event, those obligations are excused. For a DSCSA-compliant supply chain, a serialization gap during a force majeure event could create compliance exposure for Keisaiv.

**Recommended fix.** Expand the carve-out: "Force majeure does not excuse Provider's obligations under Sections 6.3, 6.4, 9.2, 9.3, 9.4, or any obligation under the Quality Agreement or the DPA that relates to the safety, identity, or traceability of Velnorix or the protection of Personal Data."

---

## Items Requiring Client Confirmation or Additional Documents

| # | Item | Reason |
|---|---|---|
| A | **Initial Statement of Work** | Not in the matter folder. Needed to confirm: (1) named subprocessors (Issue 10); (2) hub operating hours; (3) minimum remaining shelf life at shipment; (4) specific facilities; (5) order channels and cut-off times. |
| B | **Stability data supporting the 60-minute excursion threshold** | Needed to resolve Issue 1. If Keisaiv's data shows product is compromised at <60 minutes, the QA definition is unsafe. |
| C | **Affiliate structure** | Needed to assess the impact of MSA § 2.4 (Issue 17). Does Keisaiv have or expect to acquire Affiliates with existing logistics arrangements? |
| D | **Risk acceptance on summer mapping gap** | Needed for Issue 2. Can Keisaiv's Quality organization accept the risk of storing Velnorix before summer mapping is complete? |
| E | **Recall cost history/benchmark** | Needed to calibrate the recommended recall cost provision (Issue 4). What are typical recall execution costs for a specialty biologic of this profile? |
| F | **Status of Meeting Notes action items** | Needed for Issue 22. Which items were completed by their due dates? |
| G | **Keisaiv's insurance program** | MSA § 15.1 requires Provider to carry $10M cyber and $5M CGL. Confirm whether Keisaiv's own insurance program has subrogation rights or gaps that the contract should address. |

---

## Suggested Priority for Negotiation with Kedoul

1. **Must-fix before relying on the agreement:** Issues 1 (Temperature Excursion definition), 2 (summer mapping), 4 (recall costs), 8 (cure period for safety breaches).
2. **High priority:** Issues 3 (termination for convenience / non-renewal window), 5 (service credit cap), 6 (forecast exclusion), 9 (DPA liability).
3. **Should-fix:** Issues 7 (governing law), 10 (subprocessors), 14 (emergency change), 19 (defect exclusion), 20 (material breach threshold).
4. **Nice-to-have / housekeeping:** Issues 11–13, 15–18, 21–23.