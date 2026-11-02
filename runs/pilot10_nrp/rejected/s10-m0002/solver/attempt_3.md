# MEMORANDUM

**To:** Partner of Record
**From:** Associate
**Re:** Keisaiv Therapeutics, Inc. – Review of Kedoul Specialty Logistics Contract Set: Issues and Recommended Fixes
**Date:** [Current Date]

---

## Summary

I have reviewed the Master Services Agreement ("MSA"), Data Processing Addendum ("DPA"), GDP Quality Agreement ("QA"), Service Level Schedule ("SLS"), and the Velnorix launch kickoff meeting notes (March 12, 2024). Below are the issues I identified, ordered by significance. Each issue cites the relevant document and section, explains the risk to Keisaiv, and proposes a fix.

---

## Issue 1 – Conflicting Definitions of "Temperature Excursion" Create a Coverage Gap

**Where:** MSA §1.14 vs. QA §1.9; implicated by MSA §9.3, QA §5.5, SLS §3.5, and MSA §16.4 (order of precedence).

**Problem.** The MSA defines "Temperature Excursion" as "any deviation, of any duration, outside the 2°C to 8°C labeled storage range" (MSA §1.14). The Quality Agreement defines it as "any deviation outside the 2°C to 8°C labeled storage range lasting more than sixty (60) consecutive minutes, as recorded by a qualified temperature monitoring device" (QA §1.9). These are irreconcilable.

Under MSA §16.4, the Quality Agreement "shall govern with respect to quality, storage and handling matters." A temperature excursion is squarely a storage/handling matter, so the QA definition (60-minute threshold) likely controls. The practical consequence:

- A 30-minute excursion is **not** a "Temperature Excursion" under the QA, so Provider has **no notification obligation** (QA §5.5), **no quarantine obligation** (QA §5.5), and **no service credit trigger** (SLS §3.5, which cross-references QA §5.5).
- However, MSA §9.3 (product loss) uses the term "Temperature Excursion" without specifying which definition applies. If the QA definition controls, a 30-minute excursion that damages product would **not** trigger Provider's replacement cost obligation. If the MSA definition controls, it would. This ambiguity cuts against Keisaiv because the party that drafted the narrower definition (the QA, which Kedoul's quality team signed) will argue it governs.

**Why it matters.** Velnorix is a refrigerated biologic. Even short excursions can compromise product integrity. Keisaiv needs a clear, low threshold that triggers notification, quarantine, and cost recovery.

**Recommended fix.** Harmonize the definitions. I recommend adopting the MSA definition (any duration) across all documents, or if a de minimis threshold is acceptable for operational reasons, setting it at a lower duration (e.g., 15 minutes) and making it explicit in all three documents. Proposed language for QA §1.9:

> "Temperature Excursion" means any deviation outside the 2°C to 8°C labeled storage range lasting more than fifteen (15) consecutive minutes, as recorded by a qualified temperature monitoring device. Any deviation lasting fifteen minutes or less shall be recorded in Provider's temperature logs and reported in the monthly performance report, but shall not trigger the notification and quarantine obligations of Section 5.5.

Add a conforming note in MSA §1.14: *See Quality Agreement §1.9 for the operative definition.*

Also add to MSA §9.3: "For purposes of this Section 9.3, 'Temperature Excursion' has the meaning set out in the Quality Agreement, and any deviation outside the labeled storage range that results in product damage or loss shall be treated as a Temperature Excursion regardless of duration."

---

## Issue 2 – Worldwide Exclusivity with U.S.-Only Quality and Service Level Protections

**Where:** MSA §2.4 (exclusivity), MSA §1.15 (Territory = "throughout the world"), QA §2.1 (scope: "distributed solely in the United States"), SLS §1.2 (scope: "U.S. Lanes" and Hub Services for patients/HCPs "located in the United States").

**Problem.** Keisaiv has granted Kedoul exclusive rights to provide 3PL, specialty distribution, and hub services for all Covered Products (defined as "any pharmaceutical product commercialized by Client or its Affiliates, now or in the future," MSA §1.5) in a worldwide territory. But the quality agreement and service level schedule apply only to U.S. distribution. If Keisaiv later launches Velnorix (or any future product) in Canada, Europe, or elsewhere, it is contractually locked to Kedoul globally but has no quality framework, no service levels, and no defined facilities for those geographies.

**Why it matters.** This is a strategic trap. The exclusivity runs for the Initial Term (36 months) plus auto-renewing 3-year terms (MSA §12.2). Keisaiv could be locked in for 9+ years with no exit right short of material breach, while having no leverage to negotiate international terms because the contract framework doesn't cover them.

**Recommended fix.** Either (a) narrow the Territory to the United States (matching the QA and SLS scope), or (b) if worldwide exclusivity is a commercial concession Keisaiv has already made, add a provision that requires the parties to negotiate in good faith a quality agreement and service level schedule for any new geography before Keisaiv is obligated to use Kedoul there. Proposed language:

> "If Client elects to distribute a Covered Product outside the United States during the Term, the Parties shall negotiate in good faith a quality agreement and service level schedule applicable to such distribution within sixty (60) days of Client's written notice of its intent to do so. Until such documents are executed, Client shall not be required to use Provider for distribution in such geography, and Section 2.4 shall not apply to that geography."

**Confirm with client:** Does Keisaiv have any near-term plans for international distribution of Velnorix or pipeline products? If not, this is lower urgency but should still be fixed before the auto-renewal window.

---

## Issue 3 – DPA First-Party Breach Costs May Be Subject to the MSA Liability Cap

**Where:** DPA §5.4 (Provider reimburses Client's breach response costs), DPA §11.3 ("Each Party's liability under this DPA is subject to Section 14 of the Agreement"), MSA §14.2 (cap = 24 months of fees, with exceptions for §§9.3, 10, 13, and gross negligence/willful misconduct).

**Problem.** DPA §5.4 obligates Provider to reimburse Keisaiv's "reasonable costs" of a security incident, including forensics, notification, call center, and 24 months of credit monitoring. This is a direct contractual obligation of Provider to Client, not a third-party indemnification claim. DPA §11.3 subjects "each Party's liability under this DPA" to MSA §14. MSA §14.2's cap exceptions cover §13 (indemnification), §10 (confidentiality), §9.3 (product loss), and gross negligence/willful misconduct—but not a standalone reimbursement obligation under the DPA.

So if a data breach occurs that is negligent but not grossly negligent, Keisaiv's recovery of its own breach response costs (which for a pharmaceutical company handling patient PHI could easily exceed $5M–$10M) would be capped at 24 months of fees.

**Why it matters.** The cyber insurance requirement is $10M per claim (MSA §15.1(d)), suggesting the parties contemplated significant data breach exposure. Capping Keisaiv's first-party recovery below that level undermines the protection.

**Recommended fix.** Add DPA §5.4 to the list of cap exceptions in MSA §14.2. Proposed amendment to MSA §14.2:

> "Except for liability under Sections 9.3, 10, 13, **Section 5.4 of the DPA**, or arising from a Party's gross negligence or willful misconduct…"

Alternatively, add a standalone sentence in DPA §11.3: "Notwithstanding the foregoing, Provider's obligations under Section 5.4 of this DPA shall not be subject to the limitation of liability in Section 14.2 of the Agreement."

---

## Issue 4 – Auto-Renewal with a 30-Day Notice Window Combined with Exclusivity Creates Lock-In Risk

**Where:** MSA §12.2 (auto-renewal for successive 3-year terms; non-renewal notice must be delivered "no earlier than 210 days and no later than 180 days prior to expiration"), MSA §2.4 (exclusivity).

**Problem.** The non-renewal window is only 30 days wide (between 210 and 180 days before term end). If Keisaiv misses this window, it is locked in for another 3 years with worldwide exclusivity (see Issue 2). There is no termination right for convenience. The only exits are: material breach with 30-day cure failure (§12.3), insolvency (§12.4), or regulatory termination (§12.5).

**Why it matters.** For a company in launch mode, operational demands make it easy to miss a calendar deadline. The consequence of missing it is severe: 3 more years of exclusivity with no quality/service level framework outside the U.S.

**Recommended fix.** Two options (or both):

(a) Widen the notice window: "no earlier than 270 days and no later than 150 days prior to expiration" (a 120-day window).

(b) Add a termination for convenience right after the Initial Term: "Client may terminate this Agreement for convenience upon twelve (12) months' written notice, provided that Client pays all Fees for Services performed through the effective date of termination and reasonable transition costs."

I recommend (b) as the stronger protection, with (a) as a fallback if Kedoul resists.

**Confirm with client:** Does Keisaiv's contract management team have a calendar/tracking system that will flag the 210-day mark? If not, this is an operational risk as well as a contractual one.

---

## Issue 5 – Summer Temperature Mapping Not Complete Before First Product Receipt

**Where:** QA §4.1 (qualification required "before storing Velnorix at a Facility," including "a temperature mapping study under both summer and winter conditions"); Meeting Notes §3.1 (summer mapping "will be issued after the scheduled summer study"); Meeting Notes §2.2 (first commercial shipment target: April 15, 2024); Meeting Notes §4.1 (first inbound shipment: week of April 1, 2024).

**Problem.** The Memphis facility has completed IQ/OQ and winter temperature mapping, but summer mapping is outstanding. QA §4.1 requires both before storing Velnorix. The first inbound shipment is planned for the week of April 1, 2024, and first commercial shipment is April 15, 2024. Summer mapping cannot realistically be completed before summer.

This means Keisaiv will be storing a refrigerated biologic in a facility that has not completed the full qualification required by the Quality Agreement. If a temperature issue arises, Kedoul could argue the facility was not fully qualified and that Keisaiv accepted the risk by proceeding with shipments.

**Why it matters.** Beyond the contractual gap, this is a regulatory risk. FDA expects qualified storage for biologics. If an inspection occurs before summer mapping is complete, Keisaiv (as NDA holder) could receive observations.

**Recommended fix.** Add a conditional provision or interim safeguard. Proposed language (as an addendum or SOW condition):

> "The Parties acknowledge that summer temperature mapping at the Memphis Facility will be completed by [date, e.g., September 30, 2024]. Until such mapping is complete and accepted by Client's Quality Unit, Provider shall (a) limit storage to the winter-qualified temperature range of 3°C to 7°C; (b) increase monitoring frequency to [e.g., every 15 minutes instead of every 30]; and (c) provide Client with a written risk assessment confirming that the winter-qualified conditions are sufficient for year-round storage pending summer validation."

**Confirm with client:** (1) Has the summer mapping been scheduled with a firm date? (2) Is Keisaiv's Quality team comfortable with the interim risk mitigation above, or does it require a different approach? (3) Were the IQ/OQ and winter mapping reports actually delivered by the March 19 deadline (Meeting Notes, Action Item #1)?

---

## Issue 6 – Split Governing Law and Jurisdiction (New York vs. Delaware)

**Where:** MSA §16.1 (New York law), MSA §16.2 (New York County courts), DPA §12.1 (Delaware law), DPA §12.2 (Delaware courts), MSA §16.4 (DPA governs "with respect to Personal Data").

**Problem.** The contract set is governed by two different state laws with two different exclusive forums. A dispute involving both data protection and, say, product loss or service levels could implicate both jurisdictions. This creates:

- Litigation strategy complexity (which forum to file in, which law applies to which claim).
- Potential for inconsistent rulings if parallel proceedings arise.
- Increased legal costs.

**Why it matters.** While not a day-to-day operational issue, it becomes critical in a dispute. For a company that wants to move quickly (e.g., to enjoin a data breach or recover product loss), split jurisdiction creates delay.

**Recommended fix.** Conform the DPA to the MSA's governing law and forum. Proposed amendment to DPA §12:

> "12.1 This DPA is governed by and construed in accordance with the laws of the State of New York, without regard to its conflict of laws principles.
> 12.2 Each Party irrevocably submits to the exclusive jurisdiction of the state or federal courts located in New York County, New York for any action arising out of or relating to this DPA or the Processing of Personal Data."

If Kedoul resists (Delaware is its home state), an alternative is to use a single forum for all disputes under the contract set, even if the substantive law differs by topic. But unified forum is the minimum ask.

---

## Issue 7 – Forecast-Based Service Level Excuse During Launch Ramp

**Where:** SLS §6.1(c) (service level failure excused if "an order volume in a Measurement Period exceeding 125% of Client's most recent forecast"), MSA §5.1 (forecast is "non-binding").

**Problem.** During a product launch, order volumes are highly volatile and often exceed initial forecasts as patient enrollment ramps. If actual volumes exceed 125% of Keisaiv's most recent monthly forecast, Kedoul is excused from **all** service levels for that month—including the 100% standards for shipping configuration compliance (SLS §3.4), temperature excursion notification (SLS §3.5), and adverse event forwarding (SLS §3.9).

This is particularly dangerous because SLS §7.2 makes repeated failures of §3.4, §3.5, or §3.9 a material breach. If launch volumes trigger the 125% exclusion in multiple months, Keisaiv loses even its material breach termination right for the most critical service levels.

**Why it matters.** The entire purpose of the 100% standards for shipping configuration, excursion notification, and AE forwarding is patient safety. Excusing them during the highest-volume (and highest-risk) launch period defeats that purpose.

**Recommended fix.** Carve the critical service levels out of the volume exclusion. Proposed amendment to SLS §6.1:

> "Section 6.1(c) shall not apply to Service Levels 3.4, 3.5, or 3.9."

Additionally, consider lowering the threshold from 125% to 150% for the remaining service levels, or requiring that the forecast be updated at least monthly (which MSA §5.1 already contemplates) so that the baseline tracks actual ramp.

---

## Issue 8 – DPA Annex C Does Not Name Specific Subprocessors

**Where:** DPA Annex C; Meeting Notes §7.1.

**Problem.** Annex C lists two categories of approved subprocessors: "Kedoul Specialty Logistics, LLC Affiliates (as identified in the initial Statement of Work)" and "Cloud hosting provider (as identified in the initial Statement of Work)." Neither is a named entity. The DPA incorporates them by reference to the initial SOW, which is not in the matter folder.

DPA §6.1 requires Client's "prior written consent" for any subprocessor not on Annex C. If the SOW names specific entities, that's sufficient. But if the SOW uses the same vague language ("as identified in the SOW"), then the approved subprocessor list is effectively empty, and Kedoul could argue that any affiliate or cloud provider it uses is pre-approved.

**Why it matters.** Subprocessor identity is critical for data protection. Keisaiv needs to know exactly which entities will have access to patient PHI and where their systems are located.

**Recommended fix.** Amend DPA Annex C to name each approved subprocessor by legal entity name, with its location and the specific data it will process. Proposed format:

| Subprocessor (Legal Name) | Service | Location | Data Categories |
|---|---|---|---|
| [Entity Name] | Hub call center | Memphis, TN | Patient ID, case management notes |
| [Entity Name] | Cloud hosting | [City, State] | All Personal Data in case management platform |

**Confirm with client:** Please provide the initial Statement of Work so I can verify whether it names the specific subprocessor entities referenced in Annex C.

---

## Issue 9 – No Service Levels for Prior Authorization, Case Management, or Patient Shipment Coordination

**Where:** SLS §3 (service levels listed); MSA §1.8 (Hub Services defined to include "benefits verification, prior authorization support, co-pay program administration, patient intake and case management, and coordination of shipments to patients and sites of care").

**Problem.** The SLS sets service levels for benefits verification turnaround (SLS §3.7: 95% within 2 business days) and call answer rate (SLS §3.8: 90% within 30 seconds), but there are no service levels for:

- Prior authorization submission and follow-up turnaround
- Case management response to patient inquiries (beyond the call answer rate)
- Coordination and on-time delivery of shipments to patients (as distinct from the warehouse-to-consignee on-time delivery in SLS §3.3)
- Co-pay program administration accuracy

For a specialty biologic with a patient support hub, prior authorization delays can mean patients don't receive their medication. Shipment coordination failures mean cold-chain product sits uncollected.

**Why it matters.** These are the services patients interact with directly. Failures here drive patient dissatisfaction, potential adverse events from delayed treatment, and regulatory scrutiny of the patient support program.

**Recommended fix.** Add the following service levels to SLS §3:

> **3.10 Prior Authorization Turnaround.** Provider shall submit prior authorization requests within one (1) Business Day of receiving complete clinical documentation, and shall follow up until a determination is received. Measurement: percentage of prior authorizations submitted within 1 Business Day of complete documentation receipt. Target: 95%.

> **3.11 Patient Shipment Coordination.** Provider shall confirm patient shipment delivery within one (1) Business Day of the scheduled delivery date. Measurement: percentage of patient shipments with confirmed delivery within 1 Business Day of scheduled date. Target: 98%.

> **3.12 Case Management Response.** Provider shall respond to patient case management inquiries within four (4) Business Hours during hub operating hours. Measurement: percentage of inquiries responded to within 4 Business Hours. Target: 95%.

Assign appropriate service credits (I suggest 2% for each) and add them to the SLS §5.1 table.

---

## Issue 10 – "Fully Burdened Cost of Goods" Is Undefined

**Where:** MSA §9.3 ("Replacement cost means Client's fully burdened cost of goods for the affected units plus reasonable costs of investigation, quarantine and destruction").

**Problem.** "Fully burdened cost of goods" is not defined in the MSA or any related document. It could mean:
- Direct manufacturing cost (API + formulation + fill-finish + packaging)
- Manufacturing cost + overhead allocation
- Manufacturing cost + overhead + SG&A allocation
- Manufacturing cost + overhead + profit margin

The difference between these can be 30–100% of the unit cost. In a dispute over product loss, this ambiguity will be litigated.

**Why it matters.** If Kedoul loses or damages a pallet of Velnorix, the replacement cost calculation directly determines the dollar amount Kedoul owes. A narrower interpretation favors Kedoul.

**Recommended fix.** Define the term in MSA §1 or in §9.3 itself. Proposed language:

> "For purposes of Section 9.3, 'fully burdened cost of goods' means Client's internal cost accounting charge for the affected units, including direct materials, direct labor, manufacturing overhead, and allocated corporate overhead, but excluding selling, general and administrative expenses and profit margin. In the event of a dispute regarding this calculation, Client's controller or designee shall provide the cost breakdown to Provider within ten (10) Business Days of request."

**Confirm with client:** What does Keisaiv's finance team consider "fully burdened cost of goods" in its internal accounting? I want to make sure the contractual definition matches their actual cost structure so the provision is workable.

---

## Issue 11 – Material Breach Trigger Limited to Three Service Levels; 30-Day Cure Period Applies Even to Critical Failures

**Where:** SLS §7.2 (only failures of SLS §§3.4, 3.5, 3.9 in 3 of 12 months = material breach), MSA §12.3 (30-day cure period for material breach).

**Problem.** First, only three of the nine service levels can trigger material breach through repeated failure. If, for example, Order Accuracy (SLS §3.2, target 99.8%) fails every month for a year—meaning 0.2% of order lines are wrong (wrong product, wrong lot, wrong consignee)—that is not a material breach under SLS §7.2, and Keisaiv has no termination right based on it.

Second, even for the three critical service levels, MSA §12.3 requires a 30-day cure period before termination. If Kedoul fails to notify Keisaiv of a temperature excursion (SLS §3.5) in three separate months within a year, that's a material breach—but Keisaiv must then give 30 days to cure before terminating. For a cold-chain product, 30 days of continued risk is significant.

**Why it matters.** Keisaiv's primary leverage for operational failure is the termination right. If that right is narrow and slow, Keisaiv is stuck with a underperforming logistics partner for a refrigerated biologic.

**Recommended fix.** Two changes:

(a) Expand SLS §7.2 to include Order Accuracy and On-Time Delivery:

> "A Service Level Failure of Section 3.2, 3.4, 3.5, 3.9, or 3.3 in any three (3) Measurement Periods within a rolling twelve (12) month period constitutes a material breach for purposes of Section 12.3 of the Agreement."

(b) Add a short-circuit for safety-critical failures. New SLS §7.3:

> "7.3 Immediate Termination Right. Notwithstanding Section 12.3 of the Agreement, Client may terminate the Agreement immediately upon written notice if Provider fails to notify Client of a Temperature Excursion as required by Section 3.5 of this Schedule and such failure results in the distribution of Velnorix to a consignee without Quarantine."

---

## Issue 12 – One-Way Fee Adjustment

**Where:** MSA §4.4 (Provider may adjust fees once per contract year, up to lesser of 3% or CPI-U).

**Problem.** Only Provider can increase fees. There is no corresponding right for Client to request a fee reduction if volumes decrease, if Provider achieves efficiency gains, or if market rates decline. Over a 3-year term (plus renewals), this ratchets costs upward with no offset.

**Why it matters.** In the specialty logistics market, rates can shift. If Keisaiv's volumes are lower than projected (e.g., slower launch uptake), it still pays increasing fees with no mechanism to reset.

**Recommended fix.** Add a mutual adjustment right or a volume-based true-up. Proposed language:

> "4.4 [existing text]… Notwithstanding the foregoing, if Client's actual order volume in any contract year is less than seventy-five percent (75%) of Client's forecast for such year (as updated under Section 5.1), Client may request a proportional Fee reduction for the remaining months of such contract year, effective upon thirty (30) days' written notice."

---

## Issue 13 – Transition Assistance at "Rates Then in Effect" with No Successor Qualification Obligation

**Where:** MSA §12.6 (transition assistance for up to 180 days "at the rates then in effect"); QA §4.1 (qualification required before storing at a new facility); MSA §2.5 (no relocation without Client consent and qualification).

**Problem.** If Keisaiv terminates or the agreement expires, Kedoul must provide transition assistance for up to 180 days. However:

- The rates are "then in effect," which could include the most recent fee increase under §4.4. There's no discount or cap for transition services.
- There is no obligation on Kedoul to cooperate with the **qualification** of a successor provider's facility. For a cold-chain product, the successor must complete IQ/OQ/PQ and temperature mapping before it can store Velnorix (QA §4.1). If Kedoul controls the product during transition and the successor can't be qualified quickly, there's a gap.
- 180 days may not be sufficient to qualify a new cold-chain facility (temperature mapping alone requires summer and winter cycles, per QA §4.1).

**Why it matters.** The entire value of this contract is the cold chain. If transition is botched, product is at risk.

**Recommended fix.**

(a) Cap transition rates: "at the rates in effect on the date of the termination notice, without increase."

(b) Add a successor cooperation obligation: "Provider shall cooperate in good faith with the qualification of a successor provider's facilities, including providing access to temperature mapping data, qualification protocols, and historical performance records reasonably necessary for the successor to complete qualification under the Quality Agreement."

(c) Extend the transition period: "up to two hundred seventy (270) days," to account for the time needed to complete seasonal temperature mapping at a new facility.

---

## Issue 14 – "Regulatory Termination" Trigger Is Vague

**Where:** MSA §12.5 (Client may terminate if Provider "receives a warning letter or equivalent regulatory action relating to its handling of pharmaceutical products").

**Problem.** "Equivalent regulatory action" is not defined. Does it include:
- An FDA untitled letter (generally considered less severe than a warning letter)?
- A consent decree?
- A state board of pharmacy action (suspension of a state WD license)?
- An FDA Form 483 with observed deficiencies that are not repeated in a warning letter?

If the trigger is too narrow, Keisaiv loses a quick exit right when it most needs one.

**Recommended fix.** Expand the definition:

> "12.5 Regulatory Termination. Client may terminate this Agreement immediately by written notice if Provider (a) loses any license required to perform the Services; (b) receives a warning letter, consent decree, or equivalent formal regulatory action from the U.S. Food and Drug Administration, a state board of pharmacy, or any other regulatory authority having jurisdiction over Provider's handling of pharmaceutical products; or (c) breaches Section 6.5."

---

## Issue 15 – Open Action Items from Kickoff Meeting: Completion Status Unknown

**Where:** Meeting Notes §9 (Action Items table).

**Problem.** Several items were due in March 2024 and are prerequisites for safe operation:

| # | Item | Due | Status (per documents) |
|---|---|---|---|
| 1 | IQ/OQ and winter mapping reports to Keisaiv Quality | March 19 | Not confirmed |
| 2 | Business continuity plan | March 22 | Not confirmed |
| 3 | 24-hour alarm contact + Keisaiv on-call number | March 19 | Not confirmed |
| 6 | SOC 2 Type II report | March 29 | Not confirmed |
| 7 | Security incident contact confirmation | March 19 | Not confirmed |

If any of these are incomplete, Keisaiv is operating (or about to operate) without the safeguards the contracts require. The SOC 2 report, in particular, is Keisaiv's primary assurance that Kedoul's security controls are adequate (DPA §4.4).

**Recommended fix.** No contractual fix needed, but we should confirm completion before Keisaiv receives product or patient data.

**Confirm with client:** (1) Were all March action items completed? (2) Has Keisaiv received and reviewed the SOC 2 Type II report? (3) Has the business continuity plan been reviewed and accepted by Keisaiv Quality? (4) Is the 24-hour alarm call tree confirmed and tested?

---

## Issue 16 – DPA Security Incident Notification Requires Identity of "Each Affected Individual" Within 48 Hours

**Where:** DPA §5.1(a)–(e), specifically §5.1(c): notice must include "the identity of each affected individual" within 48 hours of discovery.

**Problem.** In a significant breach (e.g., a ransomware event affecting the case management platform), identifying "each affected individual" within 48 hours may be impractical. Forensic analysis to determine exactly whose data was accessed often takes weeks. If Kedoul cannot comply with §5.1(c) within 48 hours, it is in breach of the DPA—even though the delay is due to the nature of the investigation, not negligence.

This creates a perverse incentive: Kedoul might provide an incomplete initial notice (omitting individual identities) to avoid technical breach, then supplement later. Or it might argue the 48-hour deadline is excused, creating a dispute.

**Why it matters.** Keisaiv needs timely, complete information to make its own regulatory notification decisions (HHS OCR, state AGs). If the initial notice is incomplete, Keisaiv's own compliance clock is at risk.

**Recommended fix.** Modify DPA §5.1 to distinguish initial notice from supplemental detail:

> "Provider shall notify Client in writing of any Security Incident without undue delay, and in any event within forty-eight (48) hours after Provider discovers it. The initial notice shall include, to the extent then known: (a) the nature of the Security Incident; (b) the categories and approximate number of individuals and records affected; (c) the likely consequences; and (d) the measures taken or proposed to contain and remediate it. Provider shall provide the identity of each affected individual (item (c) of the original draft) as soon as such identification is reasonably possible, and in any event within ten (10) Business Days of the initial notice, unless Client agrees to a longer period."

---

## Issue 17 – No Obligation on Provider to Maintain Specific Redundancy or Failover for Hub Systems

**Where:** DPA Annex B, item 6 ("Documented incident response, business continuity and disaster recovery plans, tested at least annually"); MSA §16.7 (force majeure carve-out for temperature storage but not for hub systems); Meeting Notes §3.2 (backup generator tested, contingency storage qualified).

**Problem.** The contracts require backup power and contingency storage for the **physical facility** (QA §4.5), and require a business continuity plan (DPA Annex B ¶6). But there is no specific requirement for:

- Redundant hub case management platform (e.g., if the primary cloud instance goes down, is there a failover?)
- Maximum allowable downtime for the patient support phone line
- Redundant SFTP/data feed channels (Meeting Notes §7.4 references an "encrypted SFTP channel" for daily patient status files—what happens if it's down?)

The hub is the patient-facing interface. If it goes down for a day, patients can't get their medications, can't reach case managers, and prior authorizations stall.

**Recommended fix.** Add to the SLS or the initial SOW:

> "Hub Platform Availability. The hub case management platform and patient support phone line shall be available at least 99.5% during hub operating hours, measured monthly. Excluded: scheduled maintenance windows (no more than 4 hours per month, with 72 hours' prior notice to Client) and force majeure events. Service credit: 2% of Monthly Fees for each percentage point below 99.5%."

---

## Issue 18 – MSA §6.1 Standard of Performance References "Leading" Providers

**Where:** MSA §6.1 ("consistent with good distribution practices and the standards of care generally observed by leading specialty pharmaceutical logistics providers in the United States").

**Problem.** The word "leading" is subjective and could be disputed. If Kedoul argues it is not a "leading" provider (or that the relevant peer group is narrower), the standard of care drops. In a negligence claim, this language could be used to lower the benchmark below what Keisaiv expects.

**Recommended fix.** Replace with an objective standard:

> "Provider shall perform the Services in a professional and workmanlike manner, consistent with good distribution practices, Applicable GDP Requirements, and the standards of care observed by specialty pharmaceutical third-party logistics providers serving refrigerated biologic products in the United States."

This ties the standard to a specific product category (refrigerated biologics) rather than an ambiguous quality descriptor ("leading").

---

## Items Requiring Client Confirmation

The following cannot be resolved from the documents alone and require input from Keisaiv:

1. **International plans:** Does Keisaiv anticipate distributing Velnorix or any pipeline product outside the U.S. during the contract term? (Bears on Issue 2.)
2. **Initial SOW contents:** Please provide the executed initial Statement of Work. I need to verify: (a) whether it names the specific subprocessor entities referenced in DPA Annex C (Issue 8); (b) the minimum remaining shelf life requirement (referenced in Meeting Notes §4.3); (c) hub operating hours (referenced in SLS §3.8); (d) the specific data logger model/specification (referenced in Meeting Notes §5.2).
3. **Cost accounting:** What does Keisaiv's finance team mean by "fully burdened cost of goods"? (Issue 10.)
4. **Action item completion:** Were the March 2024 action items from the kickoff meeting completed? Specifically: IQ/OQ reports, business continuity plan, SOC 2 report, alarm contact, and security incident contact. (Issue 15.)
5. **Summer mapping timeline:** When is the summer temperature mapping scheduled? Has a date been confirmed? (Issue 5.)
6. **Affiliate structure:** Does Keisaiv have any affiliates that commercialize pharmaceutical products and might independently seek logistics services? (Bears on MSA §2.4.)
7. **Forecast accuracy:** How accurate has Keisaiv's launch volume forecast been to date? If volumes are tracking well above forecast, the SLS §6.1(c) exclusion is an immediate operational risk. (Issue 7.)

---

## Items I Could Not Resolve from the Documents

1. **The initial Statement of Work** is referenced throughout but not included in the matter folder. Several provisions (subprocessor names, shelf life minimums, hub hours, data logger specs, alarm contacts) are delegated to it. I have flagged where this creates gaps.
2. **Whether the contracts have been amended** since execution. The documents are dated March 1, 2024, and the meeting notes are dated March 12, 2024. If any side letters or amendments were exchanged, they are not in the folder.
3. **Kedoul's actual insurance certificates.** MSA §15.1 requires specific coverages and limits, but I have not seen certificates confirming compliance.

---

*End of memo.*