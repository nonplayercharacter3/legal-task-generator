# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Daitend Dental Partners, LLC – Gaiport Clinical Systems, Inc. MSA Review: Issues and Recommended Actions

---

## Summary

I have reviewed the four documents in the matter folder. I identify eight issues, ordered by significance. The two most urgent are (1) a definitional conflict between the MSA and the DPA that removes diagnostic images from the HIPAA business associate framework, and (2) the fact that Daitend's window to prevent auto-renewal has already closed, locking the client into a 36-month term through December 2029 with a 15% fee increase. Several additional issues make the current arrangement materially one-sided in Gaiport's favor.

I flag three items where the file is incomplete or ambiguous and that require client input before we can finalize recommendations.

---

## Issue 1 – Conflict in the Definition of "Patient Data" Removes Diagnostic Images from the DPA

**Description.** The MSA and the DPA define "Patient Data" inconsistently. The MSA includes diagnostic images; the DPA expressly excludes them. Because the DPA prevails over the MSA in case of conflict, the narrower DPA definition controls, and the entire HIPAA business associate framework in the DPA does not apply to radiographs, intraoral scans, or other diagnostic images.

**Where it appears.**

- MSA § 1.1: *"Patient Data" means all patient health information, including radiographs, intraoral scans and other diagnostic images.*
- DPA § 1.1: *"Patient Data" means Protected Health Information relating to patients of Customer or its Clinic Locations that is contained in Customer's scheduling and billing records created, received, maintained or transmitted by Provider through the Platform, **excluding diagnostic images**.*
- MSA § 2.3 (Order of Precedence): *"the DPA first, then this Agreement, then Statements of Work."*

**Why it matters for Daitend.** Diagnostic images are unambiguously PHI under 45 C.F.R. § 160.103. By excluding them from the DPA's definition of "Patient Data," the following DPA protections do not extend to images:

- The specific security controls in DPA § 5.2 (encryption standards, U.S.-only hosting, role-based access, penetration testing, backup/DR requirements, training).
- Breach notification obligations in DPA § 5.3–5.4.
- Subcontractor flow-down requirements in DPA § 4.1 (a subcontractor handling images need not be bound by DPA-equivalent terms).
- Individual rights support in DPA § 6.
- Return and deletion in DPA § 7.
- Audit rights in DPA § 8.

The images are still "Customer Data" under MSA § 1.1 and remain subject to MSA § 5 (data ownership, limited license) and the general security obligation in MSA § 5.3 ("Provider shall maintain administrative, physical and technical safeguards for the Platform as described in the DPA"). But MSA § 5.3 incorporates the DPA's safeguards "as described in the DPA" — and the DPA's safeguards are scoped to "Patient Data," which excludes images. This creates a circular gap: the MSA points to the DPA for security standards, but the DPA's standards don't cover the images.

The practical exposure is significant. The Severna Park onboarding alone migrated 41,906 radiographs and intraoral scans (Email Thread, Message 8). Across all locations, the volume is likely in the hundreds of thousands. If a breach affects only image storage, Gaiport arguably has no DPA-based obligation to notify Daitend within 10 days, to mitigate, or to reimburse notification costs. Daitend, as the Covered Entity, would still bear the full weight of HIPAA breach notification to patients, HHS, and potentially the media, with no contractual recourse against Gaiport under the DPA.

**Recommended fix.** Amend DPA § 1.1 to conform to the MSA definition. Proposed language:

> "**Patient Data**" means all Protected Health Information relating to patients of Customer or its Clinic Locations that is created, received, maintained or transmitted by Provider through the Platform, including scheduling and billing records, radiographs, intraoral scans and other diagnostic images.

This is a one-line change. If Gaiport resists on the ground that images are handled by a different subsystem, the alternative is to add a sentence:

> For the avoidance of doubt, diagnostic images stored in the Platform's imaging module are Patient Data and are subject to all provisions of this DPA.

**Questions for the client:**

- Has Daitend ever experienced a security incident or breach that affected only imaging data? If so, how was it handled?
- Does Daitend's own HIPAA compliance program (risk analysis, policies) treat imaging data as within the BAA scope? If Daitend's compliance officers have been operating on the assumption that the DPA covers images, there may be a gap in Daitend's own documentation that should be corrected in parallel.

---

## Issue 2 – Auto-Renewal Window Has Closed; Daitend Is Locked In Through December 2029

**Description.** The MSA provides for automatic 36-month renewals. The only way to prevent renewal is to give written notice of non-renewal within a 30-day window. That window has passed. Gaiport's October 9, 2026 renewal letter confirms the Agreement has renewed and announces a 15% increase in the Platform Fee.

**Where it appears.**

- MSA § 12.1: Initial Term ends December 31, 2026.
- MSA § 12.2: *"Unless either Party gives the other written notice of non-renewal no earlier than 120 and no later than 90 days before the current term ends."*
- Gaiport Renewal Notice Letter, § 2: *"Our records do not show that either Party gave notice of non-renewal. The Agreement has therefore renewed for a 36-month Renewal Term commencing January 1, 2027 and ending December 31, 2029."*

**Calculation of the non-renewal window:**

- Term ends: December 31, 2026
- 120 days before: September 2, 2026
- 90 days before: October 2, 2026
- Window: **September 2 – October 2, 2026** (30 days)

The renewal letter is dated October 9, 2026 — one week after the window closed. Daitend is now contractually committed through December 31, 2029.

**Why it matters for Daitend.**

- The Platform Fee increases from $18,400 to $21,160 per month (a $32,760 annual increase, or approximately $98,280 over the three-year Renewal Term before any further increases).
- The next non-renewal window will be approximately September 2 – October 2, 2029. Daitend needs to calendar this immediately.
- The 30-day window is narrow and easy to miss. There is no requirement that Gaiport remind Daitend of the approaching deadline (the renewal letter is informational, not a warning).
- During the Renewal Term, Daitend has no termination right for convenience. The only exit paths are termination for material breach (§ 12.3) or insolvency (§ 12.4).

**Recommended fix.**

The renewal has already occurred; the immediate action is defensive:

1. **Calendar the next non-renewal window** (September 2 – October 2, 2029) with a reminder set for July 2029.
2. **Negotiate a mid-term exit or price-protection clause** as part of the broader renegotiation recommended below. Proposed language for a future amendment:

> **12.2 (as amended).** Upon expiry of the Initial Term, this Agreement shall automatically renew for successive renewal terms of twelve (12) months each (each, a "Renewal Term"), unless either Party gives the other written notice of non-renewal no earlier than 180 and no later than 120 days before the current term ends.

Shortening the renewal term to 12 months and widening the notice window to 60 days gives Daitend more frequent decision points and more time to respond.

3. **Request that Gaiport confirm in writing** that the Severna Park per-location charges (added via the August 2026 change order) are not subject to the renewal pricing adjustment. The renewal letter states that per-location rates "will continue to be charged at the rates in the applicable Statement of Work," which should protect Severna Park, but given the definitional issues in this file, written confirmation is prudent.

**Questions for the client:**

- Was the non-renewal window identified and considered by Daitend's team before it closed? If not, what process change would prevent a repeat in 2029?
- Is Daitend satisfied with the Gaiport platform, or was the renewal a default rather than a business decision? This affects the leverage analysis for the renegotiation recommended in Issue 3.

---

## Issue 3 – Customer Indemnity in MSA § 10.2 Is One-Sided, Uncapped, and Covers Provider-Caused Losses

**Description.** Daitend must indemnify Gaiport for all "Customer Data Claims" — including HIPAA enforcement actions, civil money penalties, and corrective action plans — *regardless of whether Gaiport's own acts or omissions caused or contributed to the claim*. This indemnity is expressly excluded from the liability cap in MSA § 11.3(b), making it unlimited.

**Where it appears.**

- MSA § 10.2: *"Customer shall defend, indemnify and hold harmless Provider … from and against any and all claims … arising out of or relating to any Customer Data … including any enforcement action, civil money penalty or corrective action plan under HIPAA or state health privacy law, **whether or not caused or contributed to by any act or omission of Provider**."*
- MSA § 11.3(b): The liability cap does not apply to "amounts payable under Section 10.2."

**Why it matters for Daitend.**

Consider a scenario: Gaiport's hosting provider suffers a ransomware attack that exposes patient scheduling data. HHS imposes a $1.5 million civil money penalty on Daitend (the Covered Entity) for the breach. Under § 10.2, Daitend must indemnify Gaiport for any claim Gaiport faces arising from the same incident — even though Gaiport's subcontractor caused it. Meanwhile, Daitend's own recovery against Gaiport is limited by:

- The liability cap in § 11.1 (12 months of fees = ~$219,120 at the renewed rate), and
- The exclusion of indirect/consequential damages in § 11.2 (which would likely bar recovery of the HHS penalty as a "consequential" loss).

So Daitend could owe Gaiport an uncapped indemnity while Gaiport's exposure to Daitend is capped at roughly $219,000. The asymmetry is severe.

Additionally, the "Customer Data" trigger is broad. It covers any data "uploaded to, entered into or stored on the Platform by or on behalf of Customer." If a patient's data is compromised due to Gaiport's security failure, the claim "arises out of or relating to" that Customer Data, and Daitend's indemnity is triggered.

**Recommended fix.** Amend MSA § 10.2 to carve out Provider-caused losses. Proposed language:

> **10.2 By Customer.** Customer shall defend, indemnify and hold harmless Provider and its Affiliates, officers, directors and employees from and against any and all claims, demands, investigations, regulatory proceedings, fines, penalties, losses, damages, costs and expenses (including reasonable attorneys' fees) arising out of or relating to any Customer Data uploaded to, entered into or stored on the Platform by or on behalf of Customer, including any enforcement action, civil money penalty or corrective action plan under HIPAA or state health privacy law; **provided, however, that Customer shall have no obligation under this Section 10.2 to the extent the claim, demand, investigation, proceeding, fine, penalty, loss, damage, cost or expense is caused by or contributed to by any act or omission of Provider, its Affiliates, or its Subcontractors, including any failure by Provider to comply with its obligations under the DPA or this Agreement.**

This is a standard "to the extent caused by" carve-out. It preserves Daitend's indemnity for claims genuinely arising from its own data or its own misconduct while removing the absurdity of Daitend indemnifying Gaiport for Gaiport's own breaches.

If Gaiport resists the full carve-out, a fallback is to at least subject the indemnity to the liability cap:

> …provided that Customer's aggregate liability under this Section 10.2 shall not exceed the cap set forth in Section 11.1.

This is less protective but still eliminates the uncapped exposure.

---

## Issue 4 – Provider May Assign to Any Successor Without Daitend's Consent

**Description.** Gaiport can assign the entire Agreement (or any SOW) to any "Successor" — defined broadly to include any entity that acquires "all or any part of the Platform business" or "any of Provider's customer contracts" — without Daitend's consent. Daitend receives notice within 30 days *after* the assignment takes effect.

**Where it appears.**

- MSA § 1.1: *"Successor" means any entity that acquires all or any part of the Platform business of Provider, or any of Provider's customer contracts, whether by merger, sale of stock, sale of assets or otherwise.*
- MSA § 15.3: *"Provider may assign this Agreement, or any Statement of Work, in whole or in part, to any Successor without the consent of Customer, by written notice to Customer given within thirty (30) days after the assignment takes effect."*

**Why it matters for Daitend.**

- Daitend has no veto, no termination right, and no price-protection if Gaiport is acquired by or sells its practice management business to a competitor, a distressed buyer, or an entity with inferior security practices.
- The 30-day post-assignment notice means Daitend learns of the change *after* it has already happened.
- The DPA (which prevails over the MSA) does not contain its own assignment restriction. DPA § 10.3 states that the DPA confers no rights on third parties, but is silent on assignment. The MSA's assignment clause therefore governs.
- For a dental group handling sensitive patient data, the identity and security posture of the entity hosting that data is a material consideration. Daitend's patients (and potentially Daitend's own compliance obligations) are affected by who holds the data.

**Recommended fix.** Amend MSA § 15.3 to require consent or provide an exit right. Proposed language:

> **15.3 Provider Assignment.** Provider may assign this Agreement, or any Statement of Work, to a Successor only with Customer's prior written consent, not to be unreasonably withheld, conditioned or delayed. **Notwithstanding the foregoing, if Provider proposes to assign this Agreement to a Successor that (a) is a direct competitor of Customer in the provision of dental services, or (b) does not maintain cybersecurity controls substantially equivalent to those described in the DPA, Customer may terminate this Agreement and any affected Statement of Work upon thirty (30) days' written notice, and Provider shall refund prepaid Fees for the unused portion of the Term.**

If Gaiport insists on a free-assignment right (which is common in SaaS), the minimum fallback is:

> …provided that Customer may terminate this Agreement upon sixty (60) days' written notice following receipt of notice of any such assignment, and Provider shall refund prepaid Fees for the unused portion of the Term.

This gives Daitend an exit without requiring consent.

---

## Issue 5 – Renewal Pricing Is Open-Ended With No Cap

**Description.** MSA § 4.3 provides that renewal-term fees are "Provider's then-current rates" with 60 days' notice. There is no cap, no formula, no most-favored-customer clause, and no requirement that the increase be reasonable. The 15% increase in the October 2026 letter is the first instance, but the structure permits unlimited increases at every subsequent renewal.

**Where it appears.**

- MSA § 4.3: *"Fees for any Renewal Term shall be Provider's then-current rates for the Platform, as notified by Provider to Customer in writing at least sixty (60) days before the start of that Renewal Term."*
- Gaiport Renewal Notice Letter, § 3: Platform Fee increases from $18,400 to $21,160 (15%).

**Why it matters for Daitend.**

- At the current 15% increase, the fee reaches $21,160/month. A second 15% increase at the next renewal (2030) would bring it to ~$24,334/month. Compounded over multiple renewal cycles, the fee could double or triple.
- Daitend has no contractual mechanism to challenge the reasonableness of the increase. The only protection is the non-renewal right, which (as noted in Issue 2) requires action within a narrow 30-day window.
- The 60-day notice period is sufficient to inform Daitend of the increase but does not give Daitend meaningful time to negotiate or find an alternative.

**Recommended fix.** Add a pricing cap to MSA § 4.3. Proposed language:

> **4.3 Renewal Pricing.** Fees for any Renewal Term shall not exceed the Fees in effect at the end of the immediately preceding term increased by the lesser of (a) five percent (5%) or (b) the annual increase in the Consumer Price Index for Urban Consumers (CPI-U), as published by the U.S. Bureau of Labor Statistics, for the twelve (12) months preceding the notice of renewal. Provider shall notify Customer of the applicable increase in writing at least ninety (90) days before the start of the Renewal Term.

Extending the notice period from 60 to 90 days also gives Daitend more time to evaluate and respond.

---

## Issue 6 – Service Credits Are the Exclusive Remedy for Availability Failures, With No Termination Right for Chronic Underperformance

**Description.** MSA § 6.2 provides service credits (5% of monthly fee per 0.5% availability shortfall, capped at 25%) as the remedy for failure to meet the 99.5% uptime commitment. The Agreement does not state that service credits are the *exclusive* remedy, but the structure of § 6 (combined with the general limitation of liability in § 11) makes it the only practical remedy for availability issues. There is no provision allowing Daitend to terminate for chronic SLA failures.

**Where it appears.**

- MSA § 6.1: 99.5% monthly availability commitment.
- MSA § 6.2: Service credits as the stated remedy.
- MSA § 12.3: Termination for material breach with 30-day cure period (the only general termination right).

**Why it matters for Daitend.**

- The maximum service credit is 25% of one month's fee (~$5,290 at the renewed rate). If Gaiport's platform is down for an entire day (a ~6.5% monthly availability failure), Daitend's recovery is ~$10,580. The actual operational cost of a full day of downtime across multiple dental clinics (lost patient appointments, staff idle time, patient dissatisfaction) likely far exceeds this.
- Those operational costs are "indirect" or "consequential" damages, which are excluded by § 11.2.
- If Gaiport chronically misses the SLA (e.g., 99.0% availability every month for six consecutive months), Daitend's only path is to argue this constitutes a "material breach" under § 12.3. That is a factual and legal argument, not a clean contractual right, and Gaiport would have 30 days to "cure" (presumably by improving uptime for one month).
- For a dental practice, platform downtime directly affects patient care (scheduling, billing, access to records and images). The stakes are higher than for a typical SaaS deployment.

**Recommended fix.** Add a chronic-failure termination right. Proposed language:

> **6.4 Chronic Failure.** If Provider fails to meet the availability commitment in Section 6.1 in four (4) or more calendar months during any consecutive twelve-month period, Customer may terminate this Agreement or the affected Statement of Work upon thirty (30) days' written notice, and Provider shall refund prepaid Fees for the unused portion of the Term.

Also consider adding a sentence to § 6.2:

> Service credits are Customer's sole monetary remedy for failure to meet the availability commitment in Section 6.1, **except as provided in Section 6.4**.

This makes clear that the credit is the exclusive *monetary* remedy (preventing Gaiport from arguing Daitend waived other claims by accepting credits) while preserving the termination right.

---

## Issue 7 – Transition Assistance Is Priced at Provider's Then-Current Rates and Limited to 90 Days

**Description.** Upon termination or expiry, Gaiport provides 90 days of read-only access and will export Customer Data "at Provider's then-current Professional Services rates." There is no fixed rate, no obligation to provide assistance beyond 90 days, and no requirement that the export be complete or verified.

**Where it appears.**

- MSA § 13.2: *"For up to ninety (90) days after expiry or termination, Provider shall continue to provide read-only access to the Platform and shall, on Customer's request, export Customer Data in an industry-standard, non-proprietary format (including DICOM format for diagnostic images), at Provider's then-current Professional Services rates."*
- DPA § 7.1: Return of Patient Data in industry-standard format during the transition period.
- DPA § 7.2: Deletion within 30 days after the transition period.

**Why it matters for Daitend.**

- "Then-current Professional Services rates" are not defined in the file (the initial SOW is not provided). Gaiport could set a high hourly rate for data export, creating a financial disincentive for Daitend to leave.
- 90 days may be insufficient for a multi-location dental group to migrate years of patient records and diagnostic images to a new platform. The Severna Park migration alone (6,812 records, 41,906 images) took approximately 8 weeks from initial request to go-live, and that was a *new* onboarding, not a full exit migration.
- The DPA's deletion clock (30 days after the transition period) means that if Daitend needs more than 90 days to complete its migration, it risks losing data that Gaiport is obligated to delete.
- "Read-only access" is helpful but does not allow Daitend to perform billing, scheduling, or other operational functions during the transition.

**Recommended fix.** Amend MSA § 13.2. Proposed language:

> **13.2 Transition Assistance.** For up to one hundred eighty (180) days after expiry or termination, Provider shall continue to provide read-only access to the Platform and shall, on Customer's request, export Customer Data in an industry-standard, not-proprietary format (including DICOM format for diagnostic images) at a fixed rate of $[X] per hour, not to exceed $[Y] in the aggregate. Provider shall use commercially reasonable efforts to complete the export within sixty (60) days of Customer's request. If Customer requires additional transition assistance beyond one hundred eighty (180) days, the Parties shall negotiate in good faith to extend the transition period, and Provider shall not delete any Customer Data pending resolution.

The fixed rate and aggregate cap eliminate the hold-up risk. The 180-day period (doubled from 90) provides realistic time for a multi-location migration. The "shall not delete pending resolution" language protects against data loss if the transition runs long.

**Question for the client:** What are the current Professional Services rates in the initial SOW? (The SOW is not in the file.) This is needed to assess whether the "then-current rates" language is already a problem or whether the rates are reasonable.

---

## Issue 8 – Audit Rights Are Limited to Post-Breach or Regulator-Driven Audits

**Description.** Daitend may audit Gaiport's DPA compliance only if (a) a Breach of Unsecured PHI has occurred, or (b) a regulator requires it. There is no routine or periodic audit right. The annual SOC 2 Type II report (DPA § 8.1) and the limited questionnaire right (DPA § 8.2, one per 12 months) are the only proactive assurance mechanisms.

**Where it appears.**

- DPA § 8.1: Annual SOC 2 Type II report on written request.
- DPA § 8.2: One security questionnaire per 12 months (additional permitted after a Breach).
- DPA § 8.3: *"If Provider suffers a Breach of Unsecured PHI within the Patient Data, or if a regulator requires it, Customer or an independent auditor bound by confidentiality obligations may audit Provider's compliance with this DPA."*

**Why it matters for Daitend.**

- Daitend, as a Covered Entity, has a regulatory obligation under 45 C.F.R. § 164.308(b)(1) to obtain satisfactory assurance from its Business Associate that the BA will implement appropriate safeguards. A SOC 2 report is helpful but is a point-in-time assessment; it does not give Daitend visibility into day-to-day operations.
- If Gaiport's security posture degrades gradually (without a discrete "Breach" triggering the audit right), Daitend has no contractual mechanism to detect or address the decline until a breach occurs.
- The one-questionnaire-per-year limit is reasonable, but combined with the absence of a routine audit right, Daitend's oversight is thin.

**Recommended fix.** Add a routine audit right. Proposed language:

> **8.4 Routine Audit.** Once in each twelve-month period, upon sixty (60) days' written notice, Customer or its independent auditor (bound by confidentiality obligations no less protective than Section 8 of the Agreement) may audit Provider's compliance with this DPA, including inspection of relevant policies, procedures, system configurations and logs. The audit shall take place during normal business hours and in a manner that does not unreasonably disrupt Provider's operations. Provider shall provide reasonable access to personnel and documentation. The costs of the audit shall be borne by Customer, **except that if the audit reveals a material compliance failure, the costs shall be borne by Provider.**

This gives Daitend a periodic check without being burdensome on Gaiport. The cost-shifting for material failures creates an incentive for Gaiport to maintain compliance.

---

## Additional Observations and Ambiguities

### A. Initial Statement of Work Not in File

The MSA references an "initial Statement of Work" throughout (e.g., § 2.2, § 4.1, § 4.2), and the Severna Park change order incorporates rates "in the initial Statement of Work." However, the initial SOW is not in the matter folder. Without it, I cannot confirm:

- The number of Clinic Locations in the initial SOW (and therefore the scope of the $18,400/month Platform Fee).
- The per-location, per-user, and per-module rates that apply to Severna Park and any future additions.
- The Professional Services rates that govern data migration, training, and (under Issue 7) transition assistance.

**Action:** Request the initial SOW and any subsequent SOWs from the client.

### B. Severna Park and the Renewal Pricing

The Severna Park change order was executed in August 2026, before the renewal. The renewal letter states that per-location rates "will continue to be charged at the rates in the applicable Statement of Work." This should mean Severna Park's charges are not affected by the 15% Platform Fee increase. However, the renewal letter is a unilateral notice, not a bilateral amendment. If the initial SOW's per-location rates are structured as a percentage of the Platform Fee (rather than fixed dollar amounts), the renewal could indirectly affect Severna Park's charges. This cannot be confirmed without the SOW.

### C. Legacy Server Decommissioning

Email Thread, Message 10: *"The legacy server can be decommissioned once Daitend's records-retention review is complete."* The legacy server held 9 years of patient records and radiographs for the Severna Park practice. Once the data has been migrated to Gaiport's platform, the legacy server is Daitend's own system, not Gaiport's. The DPA's return/deletion provisions (§ 7) do not apply to it. Daitend is responsible for the secure disposal of the legacy server in accordance with its own HIPAA policies and any applicable state records-retention laws. This is not a contract issue with Gaiport, but it is a compliance task the client should not lose track of.

**Question for the client:** Has the records-retention review for the Severna Park legacy server been completed? If the server is decommissioned before the review is done, there is a risk of premature destruction of records subject to Maryland's medical records retention requirements (Md. Code, Health-General § 4-306, which requires retention for at least 10 years for adult patients).

### D. DPA Survival Clause Is Narrow

DPA § 9.3 provides that only Sections 5.5 (mitigation and cooperation), 6.5 (books and records for HHS), 7 (return and deletion), and 10 (general) survive. Sections 5.1–5.4 (security safeguards, specific controls, reporting, breach report contents) do not survive. This is logical for an ongoing relationship (you don't need security controls for data you no longer hold), but it means that if a breach is *discovered* after the DPA has terminated (e.g., during the backup overwrite period in DPA § 7.4, which allows up to 90 days), the breach notification and reporting obligations in § 5.3–5.4 may not apply. The data in backup is still "subject to this DPA" per § 7.4, which provides some protection, but the survival clause creates an arguable gap.

**Recommended fix (low priority):** Add Section 5 to the survival list in DPA § 9.3, or add a sentence to § 7.4:

> Any Breach of Unsecured PHI discovered during the backup overwrite period shall be reported in accordance with Section 5.3 and 5.4 as if this DPA were still in full effect.

### E. MSA § 2.6 (Updates) Is One-Sided

Provider may update the Platform so long as no update "materially reduces the functionality, security or availability of the Platform as described in the Documentation at the Effective Date." The baseline is frozen at the Effective Date (January 1, 2024). If the Documentation has been updated since then (which is likely, given the "expanded DICOM storage capacity and enhanced disaster recovery environment" referenced in the renewal letter), the baseline for the "materially reduces" test is arguably still the January 2024 documentation. This could allow Gaiport to make changes that reduce functionality relative to the *current* documentation but not relative to the *original* documentation.

This is a lower-priority issue but worth noting if Daitend renegotiates.

---

## Summary of Recommended Actions (Priority Order)

| Priority | Action | Timing |
|---|---|---|
| 1 | Calendar the next non-renewal window (Sept 2 – Oct 2, 2029) | Immediate |
| 2 | Request the initial SOW and any amendments from the client | This week |
| 3 | Send Gaiport a letter identifying the Patient Data definitional conflict and requesting an amendment to DPA § 1.1 | Within 30 days |
| 4 | Propose a comprehensive amendment package to Gaiport covering Issues 1, 3, 4, 5, 6, 7, and 8 | Within 60 days, ideally before the January 2027 renewal takes full effect |
| 5 | Confirm in writing that Severna Park per-location charges are not affected by the renewal pricing | With the amendment package |
| 6 | Complete the Severna Park legacy server records-retention review | Per Maryland law (10-year retention) |
| 7 | Review Daitend's internal HIPAA compliance documentation to ensure it is not operating on the incorrect assumption that the DPA covers diagnostic images | In parallel with #3 |

---

*This is a first draft for internal discussion. I have not verified the Maryland records-retention citation or the specific HHS enforcement posture for the scenarios described. The proposed contract language is a starting point for negotiation, not a final position.*