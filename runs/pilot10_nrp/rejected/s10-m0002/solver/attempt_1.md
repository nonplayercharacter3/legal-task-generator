# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Keisaiv Therapeutics, Inc. – Review of Kedoul Specialty Logistics Contract Set: Issues and Recommended Fixes

---

## Summary

I have reviewed the Master Services Agreement ("**MSA**"), Data Processing Addendum ("**DPA**"), GDP Quality Agreement ("**QA**"), Service Level Schedule ("**SLS**"), and the Velnorix Launch Kickoff Meeting Notes (March 12, 2024) (the "**Meeting Notes**"). Below are the issues I identified, ordered by significance to Keisaiv. Each issue cites the relevant document and section, explains the risk, and proposes a fix.

---

## Issue 1 – Conflicting Definitions of "Temperature Excursion"

**Where:** MSA § 1.14 vs. QA § 1.9

**Problem.** The MSA defines Temperature Excursion as "any deviation, **of any duration**, outside the 2°C to 8°C labeled storage range." The QA defines it as "any deviation outside the 2°C to 8°C labeled storage range **lasting more than sixty (60) consecutive minutes**, as recorded by a qualified temperature monitoring device." These are materially different thresholds.

**Why it matters.** The MSA definition governs financial liability: under MSA § 9.3, Provider bears replacement cost for any Velnorix "subject to a Temperature Excursion while in Provider's custody." The QA definition governs operational obligations: under QA § 5.5, Provider must notify and quarantine only when the 60-minute threshold is met. A 30-minute excursion would therefore trigger Keisaiv's right to replacement cost under the MSA but would *not* trigger Provider's notification or quarantine duties under the QA. In practice, this means a short excursion could go unreported and unquarantined while still giving rise to a financial claim—creating an evidentiary and operational gap. Conversely, Kedoul could argue the QA definition controls (per MSA § 16.4, the QA "shall govern with respect to quality, storage and handling matters") and that no excursion occurred unless it lasted 60+ minutes, defeating the § 9.3 claim.

**Recommended fix.** Harmonize the definitions. For Keisaiv, the broader MSA definition (any duration) is preferable for financial liability, but the 60-minute threshold in the QA is operationally reasonable for triggering quarantine and notification (shorter blips may be within sensor tolerance). I recommend:

> **MSA § 1.14 (revised):** "Temperature Excursion" means any deviation outside the 2°C to 8°C labeled storage range lasting more than thirty (30) consecutive minutes, as recorded by a qualified temperature monitoring device.

> **QA § 1.9 (revised):** Conformed to the same definition.

This sets a single threshold that is sensitive enough to capture meaningful excursions but avoids triggering quarantine for momentary sensor spikes. Alternatively, if Keisaiv prefers the "any duration" standard for financial liability, the MSA should expressly state that § 9.3 applies regardless of the QA's operational threshold, and the QA should add a separate, lower threshold (e.g., 15 minutes) for notification and quarantine.

**Flag for client:** Confirm with Keisaiv Quality whether 30 minutes is an acceptable threshold or whether they require "any duration" for liability purposes.

---

## Issue 2 – Worldwide Exclusivity with No Corresponding Performance Standards Outside the U.S.

**Where:** MSA §§ 1.15, 2.4; SLS § 1.2; QA § 2.1

**Problem.** The MSA defines Territory as "throughout the world" (§ 1.15) and makes Kedoul Keisaiv's *exclusive* provider of logistics, distribution, and hub services for *all* Covered Products (defined as any product "now or in the future," § 1.5) in that Territory (§ 2.4). However, the SLS covers only "U.S. Lanes" (50 states + DC) and U.S.-based Hub Services (§ 1.2), and the QA applies only to Velnorix "distributed solely in the United States" (§ 2.1).

**Why it matters.** If Keisaiv ever seeks to distribute a product internationally—or if a U.S. patient is in a territory the SLS doesn't cover—there are no service levels, no credits, no quality standards, and no regulatory compliance framework. Yet Keisaiv is contractually barred from engaging any other provider. This is a significant lock-in with no performance backstop outside the U.S. Additionally, the exclusivity extends to Affiliates (§ 2.4, last sentence), which could restrict group-wide logistics strategy.

**Recommended fix.**

1. **Narrow the Territory** to match the actual scope of services. If the initial SOW and near-term plans are U.S.-only, define Territory as "the fifty states of the United States and the District of Columbia" and add a mechanism for expansion by mutual agreement:

> "The Parties may agree in writing to extend the Territory to additional geographies, in which case the Service Level Schedule and Quality Agreement shall be amended to cover such geographies before the extension takes effect."

2. **Add a performance backstop for any future international lanes:** "If the Territory is expanded, the Parties shall negotiate in good faith service levels and quality standards for the expanded geography within [60] days. Until such standards are agreed, Provider shall perform Services in the expanded geography in a professional and workmanlike manner consistent with applicable local GDP requirements."

3. **Carve out Affiliates** or at minimum limit the Affiliate restriction to products that are actually covered by a SOW:

> "Client shall not engage any third party to perform services that are the same as or substantially similar to the Services for any Covered Product for which a Statement of Work has been executed."

**Flag for client:** Confirm whether Keisaiv has any near-term plans for international distribution of Velnorix or other products. If not, narrowing the Territory is low-risk. If yes, the gap is urgent.

---

## Issue 3 – Product Liability Indemnity from Keisaiv to Kedoul

**Where:** MSA § 13.2(a)

**Problem.** Keisaiv indemnifies Kedoul against "product liability claims relating to Velnorix, **except to the extent caused by Provider's handling of Velnorix**." The exception is factual and untested: in any product liability claim where a temperature excursion, shipping error, or storage failure contributed to patient harm, Keisaiv would initially bear the defense cost and indemnity obligation, then have to prove that Provider's handling *caused* the harm to recover.

**Why it matters.** For a refrigerated biologic, handling-related product liability is a realistic risk (e.g., a patient receives a product that was stored above 8°C for an extended period, leading to loss of potency and a adverse event). The "except to the extent" language creates a comparative-fault allocation that would require litigation to resolve. Keisaiv, as the indemnifying party, controls the defense under § 13.3 but bears the cost if the exception is not established.

**Recommended fix.** Strengthen the exception and add a procedural mechanism:

> "Client shall defend, indemnify and hold harmless Provider and its officers, directors and employees from and against all third-party claims, losses, damages and reasonable attorneys' fees arising out of product liability claims relating to Velnorix, **provided that** Provider shall defend, indemnify and hold harmless Client from and against all such claims **to the extent such claims arise from or are contributed to by** (i) a Temperature Excursion in Provider's custody; (ii) Provider's failure to comply with the Quality Agreement; (iii) Provider's negligence or willful misconduct in the storage, handling, packing, or shipping of Velnorix; or (iv) Provider's use of an unqualified shipping configuration or carrier."

This shifts the burden: if any of the listed Provider-side failures contributed, Kedoul bears the indemnity. The word "contributed to" (rather than "caused") lowers Keisaiv's proof threshold.

**Flag for client:** Confirm with Keisaiv's product liability counsel whether this allocation is acceptable and whether additional language is needed for biologics-specific risk (e.g., loss of potency due to cold chain failure).

---

## Issue 4 – Auto-Renewal with a 30-Day Notice Window

**Where:** MSA § 12.2

**Problem.** The Agreement auto-renews for successive three-year terms unless a Party delivers non-renewal notice in a window of 210 to 180 days before expiration—a 30-day window. A notice delivered at any other time "shall be of no force or effect."

**Why it matters.** Combined with the exclusivity clause (Issue 2), a missed window locks Keisaiv in for another three years with no ability to engage an alternative provider. The window is narrow, the consequence of missing it is severe (no cure, no equitable relief suggested), and the obligation falls on Keisaiv's internal team to track. Over a 36-month initial term plus potential renewals, the cumulative lock-in could be 9+ years.

**Recommended fix.**

1. **Widen the window:** "no earlier than twelve (12) months and no later than six (6) months prior to expiration."
2. **Add a cure mechanism:** "If a Party fails to deliver timely notice of non-renewal, the other Party may deliver such notice within thirty (30) days after the expiration of the stated window, and the Agreement shall not renew if either Party delivers notice within that additional period."
3. **Add a performance-based exit:** "Notwithstanding the foregoing, Client may elect not to renew if, in the final twelve (12) months of the then-current term, Provider fails to meet at least three (3) Service Levels in at least four (4) Measurement Periods."

---

## Issue 5 – Split Governing Law and Forum

**Where:** MSA §§ 16.1–16.2 (New York law; New York County forum) vs. DPA §§ 12.1–12.2 (Delaware law; Delaware forum)

**Problem.** The MSA is governed by New York law with exclusive jurisdiction in New York County. The DPA is governed by Delaware law with exclusive jurisdiction in Delaware courts. MSA § 16.4 provides that the DPA "shall govern with respect to Personal Data," but it does not resolve the conflict in governing law or forum for a dispute that involves both Personal Data and non-Personal Data issues (e.g., a data breach that also involves a product liability claim or a service level failure).

**Why it matters.** In a complex dispute (e.g., a security incident that also caused a Temperature Excursion and product loss), Keisaiv could face parallel proceedings in two forums under two bodies of law. This increases cost, creates inconsistent outcomes, and gives Kedoul forum-selection leverage.

**Recommended fix.** Conform the DPA to the MSA:

> **DPA § 12.1 (revised):** "This DPA is governed by and construed in accordance with the laws of the State of New York, without regard to its conflict of laws principles."
>
> **DPA § 12.2 (revised):** "Each Party irrevocably submits to the exclusive jurisdiction of the state or federal courts located in New York County, New York for any action arising out of or relating to this DPA or the Processing of Personal Data."

Alternatively, if Delaware law is preferred for data protection (some argue it has a more developed body of privacy law), conform the MSA to Delaware. But consistency is the priority.

---

## Issue 6 – Summer Temperature Mapping Not Complete Before First Shipment

**Where:** QA § 4.1; Meeting Notes § 3.1

**Problem.** QA § 4.1 requires "installation, operational and performance qualification of the refrigerated storage areas," including "a temperature mapping study under both summer and winter conditions," *before* storing Velnorix. The Meeting Notes confirm that only the winter profile is complete; the summer mapping "will be issued after the scheduled summer study." First inbound shipment is the week of April 1, 2024, and first commercial shipment is April 15, 2024.

**Why it matters.** Storing Velnorix without completed summer mapping is a direct violation of the QA and potentially of GDP requirements. If the FDA inspects and finds that performance qualification was incomplete, Keisaiv (as the BLA holder) could face a Form 483 observation or worse. The QA places the qualification obligation on Provider, but the regulatory risk falls on Keisaiv as the licensed manufacturer.

**Recommended fix.**

1. **Contractual:** Add to QA § 4.1: "Provider shall not accept Velnorix into storage at a Facility until all qualification activities required by this Section 4.1 are complete and the reports have been delivered to and reviewed by Client. If summer mapping cannot be completed before the first inbound shipment, the Parties shall agree in writing on interim risk mitigation measures (e.g., increased monitoring frequency, reduced storage volume) and Client's Quality Unit shall document its acceptance of the residual risk."
2. **Operational:** Confirm with Keisaiv Quality whether the summer study can be accelerated or whether an interim protocol (e.g., continuous monitoring with tighter alarm thresholds) can bridge the gap. Document the decision.

**Flag for client:** This is a time-sensitive operational issue. Confirm with Harriet Lunde-Achebe (VP, QA) whether Keisaiv Quality is comfortable accepting inventory before summer mapping is complete, and if so, what interim controls will be in place.

---

## Issue 7 – Non-Binding Forecasts Still Set the Excuse Threshold

**Where:** MSA § 5.1; SLS § 6.1(c)

**Problem.** MSA § 5.1 requires Keisaiv to provide a "rolling twelve (12) month **non-binding** forecast." SLS § 6.1(c) excuses a Service Level Failure if "an order volume in a Measurement Period exceed[s] 125% of Client's most recent forecast." The forecast is non-binding (Kedoul has no obligation to maintain capacity for it), yet it still operates as the threshold above which Kedoul can excuse itself from service levels.

**Why it matters.** If Keisaiv provides a conservative forecast (reasonable, given it is non-binding), Kedoul can excuse performance failures when actual volume exceeds 125% of that conservative number. During launch, volume is likely to exceed initial forecasts. This means Kedoul could systematically miss service levels during the highest-volume period and claim the forecast exception.

**Recommended fix.**

1. **Raise the threshold:** "exceeding 150% of Client's most recent forecast" (giving more headroom for launch growth).
2. **Add a notice requirement:** "Provider shall notify Client in writing at least ten (10) Business Days before the applicable Measurement Period if it anticipitates that order volume will exceed the threshold in this Section 6.1(c), and shall propose a capacity plan. If Provider does not give such notice, the exception shall not apply."
3. **Alternative:** Tie the threshold to a fixed volume rather than a moving forecast: "exceeding [X] orders per month, as set out in the applicable Statement of Work."

---

## Issue 8 – No Service Level for Inbound Receipt Processing

**Where:** SLS (entire); QA § 5.2

**Problem.** The SLS covers outbound order fulfillment, shipping, delivery, inventory accuracy, and hub services. It does not cover inbound receipt: the time from Provider's acceptance of an inbound shipment to completion of receipt verification and release from quarantine (QA § 5.2). If Kedoul is slow to process inbound product, Velnorix sits in quarantine, reducing available inventory and potentially causing stock-outs at the point of care.

**Why it matters.** At launch, inbound volume will be concentrated. A delay in receipt processing directly impacts product availability and patient access. There is currently no remedy.

**Recommended fix.** Add a new service level:

> **SLS § 3.10 – Inbound Receipt Processing.** Provider shall complete receipt verification (including in-transit temperature data review, physical inspection, and DSCSA verification) for each inbound shipment within two (2) Business Days of the shipment's arrival at the Facility, provided Client's advance shipping notice was received at least three (3) Business Days prior to arrival. Measurement: the number of inbound shipments with receipt completed within two (2) Business Days, divided by total inbound shipments in the Measurement Period. Service Level: 95%. Service Credit: 2% of Monthly Fees.

---

## Issue 9 – Subprocessor Identification is Deferred to the SOW

**Where:** DPA Annex C; DPA § 6.1

**Problem.** Annex C lists two subprocessors: "Kedoul Specialty Logistics, LLC Affiliates (as identified in the initial Statement of Work)" and "Cloud hosting provider (as identified in the initial Statement of Work)." Neither is specifically named. DPA § 6.1 requires Client's prior written consent for any Subprocessor, and Annex C is supposed to list those approved "as of the Effective Date."

**Why it matters.** If the SOW (which is not in the review folder) does not specifically identify the cloud hosting provider and the relevant Affiliates, then technically no subprocessors have been approved, and any use of a subprocessor would require individual written consent. This creates operational friction and potential compliance risk. Additionally, without knowing the identity of the cloud hosting provider, Keisaiv cannot assess data location compliance (DPA § 8.1) or security posture.

**Recommended fix.**

1. **Name the subprocessors specifically in Annex C** (or in a schedule to the DPA), including legal entity name, location, and specific services.
2. **Add a change process:** "Provider may propose additional or replacement Subprocessors by written notice to Client, including the Subprocessor's identity, location, services, and data protection terms. Client shall not unreasonably withhold consent. If Client does not respond within fifteen (15) Business Days, consent shall be deemed granted, provided the Subprocessor is located in the United States and the data protection terms meet the requirements of Section 6.2."
3. **Confirm with client:** Lena Marchetti (Associate Director, Privacy) should confirm the identity of the cloud hosting provider and whether it has any non-U.S. remote access capabilities.

**Flag for client:** The SOW is not in the review folder. Please provide it so I can confirm whether the subprocessors are specifically identified.

---

## Issue 10 – "Equivalent Regulatory Action" Undefined in Regulatory Termination Right

**Where:** MSA § 12.5

**Problem.** Keisaiv may terminate immediately if Provider "receives a warning letter or **equivalent regulatory action** relating to its handling of pharmaceutical products." "Equivalent regulatory action" is not defined.

**Why it matters.** In a dispute, Kedoul could argue that only a formal FDA warning letter triggers this right, and that a Form 483, a state board of pharmacy citation, or an FDA inspection observation is not "equivalent." This would narrow Keisaiv's termination right significantly.

**Recommended fix.**

> "Client may terminate this Agreement immediately by written notice if Provider (a) loses any license required to perform the Services; (b) receives an FDA warning letter, consent decree, or injunction; (c) receives a final adverse determination from a state board of pharmacy or equivalent state regulatory authority relating to its handling of pharmaceutical products; (d) is the subject of an FDA Form 483 with any observation classified as 'critical' or 'major' that is not corrected to FDA's satisfaction within the time allowed; or (e) breaches Section 6.5."

---

## Issue 11 – Liability Cap May Underprotect Against Non-Indemnity DPA Claims

**Where:** DPA § 11.3; MSA § 14.2

**Problem.** DPA § 11.3 provides that "Each Party's liability under this DPA is subject to Section 14 of the Agreement." MSA § 14.2 caps aggregate liability at 24 months of fees, with carve-outs for §§ 9.3, 10, 13, and gross negligence/willful misconduct. DPA § 11.3 also states that "Provider's obligations under Section 13.1 of the Agreement apply to claims arising out of this DPA," which pulls data breach claims into the indemnity (and thus out of the cap). However, a DPA claim that does not rise to a third-party indemnifiable event—e.g., Provider's failure to maintain encryption, failure to conduct annual risk assessments, or failure to remediate audit findings—would be subject to the 24-month fee cap.

**Why it matters.** If Kedoul systematically fails to maintain required security measures but no breach occurs, Keisaiv's remedy is limited to the cap (and likely to service credits or termination). The cap may be insufficient to cover the cost of remediation, regulatory fines (if HHS imposes a penalty on Keisaiv as the covered entity due to Kedoul's failure), or the cost of implementing compensating controls.

**Recommended fix.** Add to DPA § 11.3:

> "Notwithstanding Section 14.2 of the Agreement, Provider's liability for (a) regulatory fines or penalties imposed on Client as a result of Provider's breach of this DPA, and (b) Client's reasonable costs of implementing compensating security measures following Provider's material breach of Section 4 of this DPA, shall not be subject to the cap in Section 14.2 of the Agreement."

---

## Issue 12 – Transition Assistance Lacks Specificity

**Where:** MSA § 12.6

**Problem.** Upon expiration or termination, Provider shall "for up to one hundred eighty (180) days at Client's request and at the rates then in effect, continue to perform the Services and cooperate in the orderly transfer of Client inventory, records and patient cases to Client or its designee." Several gaps:

- No obligation to train a successor provider.
- No specification of what "cooperate" entails (e.g., data format, system access, personnel availability).
- "At the rates then in effect" could be disputed if fees were adjusted in the final year.
- No obligation to maintain service levels during the transition period.
- The 180-day period is a maximum, not a guaranteed minimum—Provider could argue that 30 days of transition is sufficient.

**Why it matters.** For a specialty biologic with a complex cold chain and patient support program, transition is high-risk. An inadequate transition could result in product loss, patient disruption, and regulatory exposure.

**Recommended fix.**

> "Upon expiration or termination for any reason, Provider shall, for a period of up to one hundred eighty (180) days (the 'Transition Period'), at Client's request: (a) continue to perform the Services at the rates in effect for the final Measurement Period before expiration or termination; (b) meet all Service Levels; (c) cooperate in good faith in the orderly transfer of Client inventory, records, and patient cases to Client or its designee, including providing system access, data in agreed formats, and reasonable personnel availability; (d) train Client's designee on all procedures, systems, and protocols used to perform the Services; and (e) maintain all licenses, registrations, and insurance required to perform the Services throughout the Transition Period."

---

## Issue 13 – Force Majeure / Product Loss Interaction

**Where:** MSA §§ 16.7, 9.3

**Problem.** MSA § 16.7 provides that force majeure "does not excuse Provider's obligations to maintain temperature-controlled storage, backup power and business continuity measures required by the Quality Agreement." MSA § 9.3 makes Provider liable for replacement cost of Velnorix lost or subject to a Temperature Excursion "while in Provider's custody," with exceptions only for Client negligence or pre-existing product defect. There is no force majeure exception in § 9.3.

**Why it matters.** As drafted, this is actually favorable to Keisaiv: even if a hurricane destroys the warehouse, Provider is still liable for product loss. However, the interaction is not explicit, and Kedoul may argue that § 16.7's carve-out (which preserves storage/backup power obligations) implies that if those obligations are met but the facility is still destroyed, force majeure excuses the resulting product loss. The current text doesn't resolve this.

**Recommended fix.** Add to MSA § 9.3:

> "For the avoidance of doubt, a force majeure event under Section 16.7 does not limit or excuse Provider's obligations under this Section 9.3."

This makes Keisaiv's position explicit and forecloses the argument.

---

## Issue 14 – Data Location: Remote Access Risk

**Where:** DPA § 8.1; DPA Annex C

**Problem.** DPA § 8.1 prohibits remote access to Personal Data from outside the United States without Client's prior written consent. Annex C identifies a "Cloud hosting provider" without naming it. If that provider (e.g., AWS, Azure, or a specialty health data host) has global support engineers who can remotely access systems, this could be a violation.

**Why it matters.** A violation of § 8.1 would be a DPA breach, potentially triggering the indemnity and termination rights. But more practically, if the cloud provider's standard terms allow global remote access, Keisaiv may be in continuous breach of its own compliance posture without knowing it.

**Recommended fix.**

1. **Name the cloud provider in Annex C** and confirm in writing that it does not permit remote access from outside the United States, or if it does, obtain Keisaiv's written consent and document the specific controls.
2. **Add to DPA § 8.1:** "Provider shall confirm in writing, at least annually and upon any change to its Subprocessor arrangements, that no remote access to Personal Data is made from outside the United States except as expressly consented to in writing by Client."

**Flag for client:** Confirm with Lena Marchetti the identity of the cloud hosting provider and whether its standard operations include non-U.S. remote access.

---

## Issue 15 – No Right to Terminate for Chronic Underperformance Below the Material Breach Threshold

**Where:** MSA § 12.3; SLS § 7.2

**Problem.** Termination for cause requires a "material breach" that is not cured within 30 days (MSA § 12.3). SLS § 7.2 defines when a service level failure constitutes a material breach: only for SLS §§ 3.4, 3.5, or 3.9 (shipping configuration, temperature excursion notification, adverse event forwarding), and only after failure in three Measurement Periods within a rolling twelve-month period. For all other service levels (order fulfillment, accuracy, on-time delivery, inventory, benefits verification, call answer rate), there is no path to termination for chronic underperformance short of arguing that the aggregate failures constitute a material breach of the MSA as a whole.

**Why it matters.** If Kedoul consistently misses the 98% same-day shipment standard or the 95% benefits verification standard for 11 of 12 months, Keisaiv has no contractual right to terminate. It can only claim service credits (capped at 10% of monthly fees per SLS § 5.3) and await the auto-renewal window.

**Recommended fix.** Add to SLS § 7:

> **7.3 – Chronic Underperformance.** If Provider fails to meet any Service Level (other than those in Sections 3.4, 3.5, or 3.9) in five (5) or more Measurement Periods within a rolling twelve (12) month period, Client may terminate the affected Statement of Work or this Agreement on thirty (30) days' written notice, without prejudice to any other remedy."

---

## Issue 16 – "Fully Burdened Cost of Goods" Undefined

**Where:** MSA § 9.3

**Problem.** Replacement cost is defined as "Client's fully burdened cost of goods for the affected units plus reasonable costs of investigation, quarantine and destruction." "Fully burdened cost of goods" is not defined. It could mean COGS only, or COGS plus allocated manufacturing overhead, R&D amortization, quality costs, etc.

**Why it matters.** In a product loss event, the difference between a narrow and broad interpretation of "fully burdened" could be significant for a specialty biologic with high manufacturing costs. Keisaiv would want the broader definition; Kedoul would want the narrower one.

**Recommended fix.**

> "Replacement cost means Client's internal fully loaded cost to manufacture or acquire the affected units, including direct materials, direct labor, manufacturing overhead, and quality assurance costs, plus reasonable costs of investigation, quarantine, and destruction, as documented in Client's cost accounting records."

**Flag for client:** Confirm with Keisaiv's finance team what components are included in their "fully burdened cost of goods" for Velnorix so the definition matches their actual cost structure.

---

## Issue 17 – MSA § 16.4 Order of Precedence Does Not Address the SLS

**Where:** MSA § 16.4

**Problem.** The order of precedence states: "the Quality Agreement shall govern with respect to quality, storage and handling matters; the DPA shall govern with respect to Personal Data; and otherwise this Agreement shall govern, followed by the Service Level Schedule, followed by the Statements of Work." The SLS is placed *below* the MSA in the hierarchy. However, the SLS is incorporated into the MSA (MSA § 2.3: "The Service Level Schedule forms part of this Agreement"). If a SLS provision conflicts with an MSA provision, the MSA controls. This is generally fine, but it means that if the SLS is more favorable to Keisaiv than the MSA on a particular point, the MSA would override it.

**Why it matters.** For example, if the SLS provided a broader definition of service level failure or a higher credit percentage, but the MSA's general limitation of liability (§ 14) capped the remedy, the MSA would control. This is not necessarily a problem, but it's worth being aware of when negotiating SLS amendments.

**Recommended fix.** No change needed if the current hierarchy is acceptable. However, add a clarifying sentence: "Where the Service Level Schedule sets out specific remedies or standards that are more favorable to Client than the general provisions of this Agreement, the Service Level Schedule shall control with respect to those specific remedies or standards."

---

## Items Requiring Client Confirmation

| # | Item | Contact |
|---|---|---|
| 1 | Acceptable temperature excursion threshold (any duration vs. 30 min vs. 60 min) | Harriet Lunde-Achebe (VP, QA) |
| 2 | Near-term plans for international distribution of Velnorix or other products | Miriam Okonjo-Hale (CCO) |
| 3 | Comfort level with accepting inbound product before summer temperature mapping is complete; interim controls | Harriet Lunde-Achebe (VP, QA) |
| 4 | Identity of cloud hosting provider in DPA Annex C; whether it permits non-U.S. remote access | Lena Marchetti (Privacy) |
| 5 | Components of "fully burdened cost of goods" for Velnorix | Finance / Controller |
| 6 | Whether the initial SOW specifically names the subprocessors in DPA Annex C | Priya Venkataraman (Trade Ops) |
| 7 | Acceptability of the product liability indemnity split (Issue 3) | General Counsel / Product Liability Counsel |
| 8 | Whether Keisaiv wants a performance-based exit right (Issue 15) given the exclusivity lock-in | Miriam Okonjo-Hale (CCO) |

---

## Items I Could Not Resolve from the Documents Alone

1. **The initial Statement of Work** is referenced throughout but is not in the review folder. It likely contains: facility addresses, specific subprocessor names, hub operating hours, minimum shelf-life requirements, shipping configuration details, and fee schedules. Several issues above (particularly Issues 9 and 14) cannot be fully assessed without it.

2. **Kedoul's SOC 2 Type II report** (due March 29, 2024 per Meeting Notes § 7.2) would allow assessment of whether the security controls in DPA Annex B are actually implemented. Not available for review.

3. **The business continuity plan** (due March 22, 2024 per Meeting Notes § 3.2) would allow assessment of whether the 72-hour backup power requirement (QA § 4.5) and contingency storage arrangements are adequate. Not available for review.

4. **Kedoul's insurance certificates** (MSA § 15.1) would confirm that the required coverages are actually in place. Not available for review.

---

*End of memo.*