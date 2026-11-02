# MEMORANDUM

**PRIVILEGED & CONFIDENTIAL: ATTORNEY WORK PRODUCT**

**To:** Supervising Partner
**From:** Associate
**Date:** November 2, 2026
**Re:** Daitend Dental Partners, LLC / Gaiport Practice Systems, Inc.: Issues, Exposure and Recommended Actions

Sources reviewed: Master Services Agreement dated March 1, 2024 ("MSA"); Data Processing Addendum of the same date ("DPA"); Daitend non-renewal letter dated July 20, 2026 ("Letter"); internal Imaging Module rollout emails, September 9 to December 13, 2024 ("Emails," cited by number).

---

## Bottom Line

1. **The non-renewal notice was probably late, so the MSA likely auto-renewed on September 1, 2026 for a 36-month Renewal Term ending August 31, 2029 (MSA §12.2).** Remaining fee exposure is about $662,400 (36 × $18,400), before any negotiated change. We have no facts after July 20, 2026, so this must be confirmed immediately.
2. **Patient data is the most time-sensitive operational risk.** If the agreement did expire, the DPA deletion clock could run out around November 29, 2026. Gaiport is likely the only remaining complete copy of the historic radiographs.
3. **The contract leaves patient health information (PHI) largely outside the DPA's protections.** Daitend also carries uncapped indemnity exposure for data incidents, even where Gaiport caused them, while Gaiport's liability is capped.

Items marked **[PROMPT]** need action this week.

---

## Issues, in Order of Importance

### 1. Non-renewal notice was untimely; agreement likely renewed to August 31, 2029 **[PROMPT]**

- **Where:** MSA §12.1 (Initial Term ends August 31, 2026); MSA §12.2 (renewal unless notice given "not more than 120 days and not less than 90 days" before the end of the Initial Term); Letter §1 (dated July 20, 2026); MSA §16.2 (notice effective on receipt); MSA §16.3 (amendment only by signed writing; no waiver by delay).
- **Why it matters:**
  - The notice window was **May 3 to June 2, 2026**, counting back 120 and 90 days from August 31, 2026.
  - The Letter is dated **42 days** before expiration and was sent **48 days after** the window closed. Actual receipt is later still.
  - Under §16.3, a party's delay does not waive a right, but a late notice also cannot change the term. Unless Gaiport agreed in a signed writing, the MSA should have renewed on September 1, 2026 at the then-current Subscription Fee of $18,400/month (§12.2, §4.1).
  - The Letter says Daitend "expects" services through August 31, 2026 and will pay "for the remaining months of the Initial Term" (Letter §2). Gaiport may cite this to show Daitend understood the term ran to that date. It does not extend the window.
  - No convenience termination right exists (see Issue 8), so Daitend cannot exit early by notice alone.
- **Recommended fix:**
  - Treat renewal as the base case until we confirm the facts in the list at the end of this memo, especially any invoices and payments since September 1, 2026.
  - Confirm whether any notice was sent between May 3 and June 2, 2026. If one was, it changes the analysis entirely.
  - Confirm the delivery date and proof of delivery for the Letter. The signature-page notice address (MSA signature page) lists only "Attn: General Counsel" with no street address, so check that the courier delivered to an address Gaiport designated under §16.2.
  - Find out whether Gaiport responded or acknowledged expiration. Any written acceptance of the Letter would be the strongest argument for a mutual termination, and it should be pursued.
  - Send a reservation-of-rights letter now. Propose a negotiated exit with a signed amendment under §16.3 that sets an end date, export and deletion terms, and transition support. Alternatively, negotiate new terms that include an exit right.
  - Do not stop paying undisputed invoices. Suspension is available to Gaiport after 30 days' notice of non-payment (MSA §13.3), and interest accrues at 1% per month (§4.4). Suspension would stop clinic scheduling and imaging at 22 locations.
  - If Daitend wants to contest any invoice, it must give written notice before the due date with reasonable detail (MSA §4.3).

### 2. Patient data return and deletion clock; Gaiport may hold the only complete image archive **[PROMPT]**

- **Where:** MSA §7.4 (30-day export window after expiration or termination, on written request, DICOM for images); MSA §13.4 (access ends, subject to §7.4); DPA §9.1 (export during the §7.4 period); DPA §9.2 (production deletion within 60 days after the export period; backups within rotation, not exceeding 180 days); DPA §9.3 (officer's certificate on request); DPA §9.4 (legal retention); Letter §3 (export request made before expiration); Emails 4 (October 1, 2024) and 7 (December 13, 2024) (legacy servers to be decommissioned after a 90-day fallback period, with Waves 2 and 3 to follow).
- **Why it matters:**
  - **If the agreement expired August 31, 2026:** the export window ran to about September 30, 2026. Production deletion would be due by about **November 29, 2026**. Backups must be deleted within rotation, not to exceed 180 days, with the measuring start unclear in DPA §9.2.
  - The Letter asked for export "promptly after expiration" (Letter §3). That was sent before expiration and may not satisfy §7.4's "on Customer's written request" requirement. We should assume Gaiport could argue no valid export request was made.
  - **Daitend may have no other complete copy.** The legacy servers were decommissioned under the Emails' plan in early 2025 (Email 7). Daitend's records and radiographs may exist only on Gaiport's platform, which creates retention and clinical-continuity risk.
  - **Migration verification is thin.** The only documented spot-check was Wave 1, 50 charts per clinic (Email 4; Email 5). Waves 2 and 3 show a scheduled migration (Email 6) and the closeout reports "Wave 3 went smoothly" (Email 7), but there is no documented reconciliation or confirmation that all records migrated. Disposal certificates were promised but are not in the folder.
  - Gaiport may invoke DPA §9.4 to keep data under unspecified legal requirements.
- **Recommended fix:**
  - Send a fresh written export request under MSA §7.4 and DPA §9.1 now, regardless of whether renewal or expiration applies. Request a full DICOM export with calibration data (Email 3 relies on Gaiport's oral confirmation of this point), plus charts, billing, scheduling, audit logs, and a data dictionary.
  - Demand written confirmation that no deletion will occur before export is complete and accepted, and that Gaiport will preserve data if a dispute arises.
  - Ask Gaiport to identify in writing any legal requirement it relies on under DPA §9.4.
  - Ask Gaiport for its reconciliation records for all three waves, and confirm whether Daitend has any remaining local copies. Request the disposal certificates. If migration was incomplete before the legacy servers were destroyed, that is a potential claim, subject to the limits in Issue 6.
  - Confirm Daitend's record-retention obligations under state dental-records rules (outside the folder; verify).

### 3. Payment posture and suspension risk **[PROMPT]**

- **Where:** MSA §4.2 (monthly invoices, due in 30 days); §4.3 (good-faith disputes must be noticed before the due date); §4.4 (1% monthly interest); §13.3 (suspension after 30 days' notice of non-payment); §13.4 (fees accrued through termination are payable).
- **Why it matters:** The Letter commits Daitend to pay through August 31, 2026 and does not address invoices after that date. If Gaiport has invoiced September and October 2026 and Daitend has not paid, interest and suspension risk is already running. Suspension would be the most disruptive outcome for a 22-clinic practice.
- **Recommended fix:** Pull the invoice and payment ledger for September 2026 forward. Decide with the client whether to pay under reservation of rights or to dispute properly under §4.3 before the next due date. Do not allow a suspension notice to pass unanswered.

### 4. PHI is largely outside the DPA's protections; breach-notice timing does not apply to patient data **[HIGH]**

- **Where:**
  - MSA §1.4 (Customer Data includes PHI, radiographs and treatment records).
  - DPA §1.1 (Customer Personal Data is defined "excluding Patient Health Information").
  - DPA §1.3 (PHI is defined but has no operative provisions in the DPA).
  - DPA §1.6 (Security Incident means a "confirmed" breach).
  - DPA §6.1 (72-hour notice only for Security Incidents "affecting Customer Personal Data").
  - DPA §5.1 (security measures apply to Customer Personal Data).
  - DPA Annex A (categories of individuals are staff only; patients and PHI are omitted).
  - MSA §7.1 (security "as further described in the DPA"); MSA §7.3 (incident notice "in accordance with the DPA").
  - The MSA and DPA contain no reference to HIPAA or a business associate agreement.
- **Why it matters:**
  - Read together, the documents leave PHI with no defined breach-notice deadline, no defined security standard beyond MSA §8.2's "reasonable care," and no defined subprocessor-change rights. The 72-hour clock in DPA §6.1 does not reach patient data, and "confirmed" breaches exclude suspected incidents.
  - Daitend is the covered entity and Gaiport is handling PHI on its behalf. **[Outside the folder; verify.]** HIPAA generally requires a business associate agreement with breach-reporting, safeguard and subcontractor terms (45 C.F.R. §§ 164.502(e), 164.504(e), 164.410). If no BAA exists, that is a compliance gap for Daitend as well as a contract gap.
  - Annex A's omission of patients creates a documentation inconsistency with MSA §1.4 and the actual processing (Email 1 and Email 5 describe patient charts and radiographs).
- **Recommended fix:**
  - Confirm whether Daitend has an executed BAA. If not, require one now as a condition of any renewal or negotiated exit. Amendments need a signed writing (MSA §16.3; DPA §10.3).
  - Amend the DPA to include PHI in scope. Cover suspected as well as confirmed incidents. Set a short notice period for PHI incidents (for example, 24 to 72 hours from awareness, with rolling updates). Require cooperation and reimbursement of notification costs.
  - Correct Annex A to list patients and PHI categories and Annex C to identify subprocessors touching PHI (see Issue 9).

### 5. Daitend's uncapped indemnity for Customer Data incidents, including incidents Gaiport caused **[HIGH]**

- **Where:** MSA §9.1(a) (Customer indemnifies Gaiport for claims, regulatory fines and penalties arising from Customer Data "regardless of whether caused by Gaiport"); MSA §10.3(a) (indemnities are excluded from the liability cap and exclusions); MSA §9.2 (Gaiport's only indemnity covers IP infringement).
- **Why it matters:** Daitend would bear uncapped exposure, including regulatory penalties, for a breach in Gaiport's systems. Gaiport has no reciprocal data-breach indemnity. This is the single largest contractual imbalance in the folder.
- **Recommended fix:** Limit Daitend's data indemnity to incidents caused by Daitend, its Authorized Users or its breach of §5.1. Add a Gaiport indemnity for breaches caused by Gaiport or its Subprocessors, carved out of the cap or subject to a super-cap (Issue 6).

### 6. Gaiport's liability cap and consequential-damages exclusion will limit recovery for a data breach **[HIGH]**

- **Where:** MSA §10.1 (cap equals fees paid in the prior 12 months, roughly $220,800 at full fee); MSA §10.2 (no consequential damages or lost profits); MSA §10.3 (exceptions only for indemnities, Fees and gross negligence, fraud or willful misconduct); DPA §10.1 (DPA liability subject to MSA §10).
- **Why it matters:** Daitend's likely losses from a patient-data incident (notification, forensic, credit monitoring, lost revenue from clinic downtime) may be argued to be consequential or simply exceed the cap. Gaiport's exposure is therefore limited, while Daitend's indemnity is not.
- **Recommended fix:** Negotiate a data-breach super-cap (for example, a multiple of annual fees or the cyber policy limit, whichever is greater). Define breach-response costs as direct damages. Carve out gross negligence and violations of the DPA or BAA.

### 7. Gaiport may assign the MSA and Customer Data to acquirers and lenders without consent or notice **[HIGH to MEDIUM]**

- **Where:** MSA §15.4 (assignment to any Permitted Assignee "without Customer's consent and without notice"); MSA §1.10 (Permitted Assignee includes any acquirer, and any lender, investor or financing party and its agents); MSA §15.3 (Daitend cannot assign without consent).
- **Why it matters:** Daitend's patient data could move to a new owner, a financing party or an affiliate of unknown security practices. The DPA contains no assignment restriction, and Daitend would have no termination right. Daitend's own assignment is restricted, which is asymmetric.
- **Recommended fix:** Require notice and an opportunity to object for assignment to anyone other than an Affiliate. Require the assignee to assume the DPA and any BAA in writing. Limit lender and investor access to security interests without access to Customer Data. Give Daitend a termination right with a pro-rata refund on assignment to a competitor or to an assignee that does not meet the security standards.

### 8. No exit right and limited remedies; leverage is weaker than it looks **[MEDIUM to HIGH]**

- **Where:** MSA §12 (fixed terms, no convenience termination); MSA §13.1 (termination for uncured material breach); MSA §11.2 (warranty remedy is the exclusive remedy: fix within 30 days, then termination with refund of prepaid fees); MSA §9.2 (IP termination); MSA §3.5 (99.5% availability on a commercially reasonable efforts basis, with no credits); Emails 5 to 7 (pilot and rollout went well, with no Severity 1 incidents).
- **Why it matters:** The client's own emails undercut any claim that Gaiport materially breached the MSA. Without a breach, Daitend's only exit paths are a negotiated amendment or a late-notice argument. Gaiport has leverage.
- **Recommended fix:** Decide with the client whether it wants to exit or stay on better terms. For an exit, negotiate a termination fee, transition assistance and data-migration support. For a stay, negotiate a convenience-termination right after a set period, SLA credits, and tighter availability commitments. Pull uptime and ticket data for the full term to see whether any §11.2 or §13.1 claim exists.

### 9. Subprocessor changes give no termination right; Zendesk may receive patient data **[MEDIUM]**

- **Where:** DPA §7.1 (general authorization); DPA §7.2 (30 days' notice; objections discussed in good faith, with no termination right); DPA Annex C (AWS, Okta, Zendesk); DPA §7.3 (Gaiport remains responsible); MSA §15.2.
- **Why it matters:** Zendesk handles support tickets, which may contain PHI, but Annex C is tied to Customer Personal Data, which excludes PHI (Issue 4). Daitend cannot refuse a new subprocessor or exit if it objects.
- **Recommended fix:** Add a termination right with a pro-rata refund if an objection is not resolved. Confirm in writing whether Zendesk or any other vendor receives PHI. Request Gaiport's current SOC 2 Type II report now under DPA §5.4, since the 12-month request window is available and the report should be reviewed before any renewal.

### 10. Insurance is undefined; no certificate in the file **[MEDIUM]**

- **Where:** MSA §14.1 (cyber, errors and omissions and general liability insurance with "limits customary for providers of comparable services"; certificate on reasonable request).
- **Why it matters:** Gaiport's cyber coverage is the practical source of recovery for a breach, given the cap in Issue 6. The MSA sets no dollar figure.
- **Recommended fix:** Request certificates now under §14.1. Confirm cyber and E&O limits, retention, notice-of-cancellation terms and whether Daitend can be named as additional insured. Use the answer to size the super-cap in Issue 6.

### 11. Executed copies, Order Forms and the Imaging Module fee are not in the folder **[MEDIUM; obtain now]**

- **Where:** MSA signature page (blank signature, name and title lines); DPA signature page (blank); Letter signature block (blank in our copy); MSA §2.2 and §4.1 (Order Forms govern Clinic Locations and additional modules); MSA §1.8 and §1.11 (Imaging Module is part of the Platform); Email 1 (rollout of all 22 clinics to the Imaging Module in late 2024).
- **Why it matters:** We cannot confirm that the MSA and DPA were signed as produced, whether an Order Form for the Imaging Module added fees, whether all 22 clinics are listed as Clinic Locations (MSA §1.3), or whether the Letter was signed as sent. The Imaging Module may also have its own term or fee.
- **Recommended fix:** Obtain fully executed MSA, DPA, all Order Forms, any SOWs or amendments, and the as-sent Letter with its courier receipt. Confirm the fee and clinic count before any renewal analysis is finalized.

### 12. Support hours, undefined Severity 1 and efforts-based availability **[MEDIUM to LOW]**

- **Where:** MSA §3.4 (support 7:00 a.m. to 8:00 p.m. ET on business days; Severity 1 defined only "in accordance with the Documentation"); MSA §3.5 (efforts-based 99.5% availability); MSA §16.4 (force majeure, including telecommunications failures, which may be argued to cover cloud or network outages); Email 5 (support desk "covers our clinic hours").
- **Why it matters:** Email 5 says support covers clinic hours, but MSA §3.4 covers business days only. If any clinic opens on Saturdays or after 8:00 p.m., the gap is real. The availability commitment is weak and there are no credits.
- **Recommended fix:** Confirm clinic hours with the client. Require weekend coverage for clinic days, a defined Severity 1 standard, uptime reporting and service credits. Narrow force majeure so it does not excuse cyber events affecting availability.

### 13. Delaware exclusive forum **[LOW]**

- **Where:** MSA §16.1 (Delaware law; exclusive jurisdiction in Delaware courts).
- **Why it matters:** Any dispute over renewal or data must be litigated in Delaware, which may matter for a practice group operating in other states.
- **Recommended fix:** Consider whether to seek a neutral or home-state forum in any amendment, or accept Delaware as a trade-off for other terms.

### 14. Daitend's own compliance history on hardware and sensors **[LOW; document, do not ignore]**

- **Where:** MSA §5.2 (customer maintains compatible hardware at each clinic); Email 2 (14 workstations below minimum RAM; three clinics with older sensors needing driver updates; two panoramic units needing manufacturer firmware); Email 7 (workstations and driver updates installed on schedule).
- **Why it matters:** Gaiport could raise these points as a Daitend breach under §5.2 if a dispute arises. The record shows they were cured before Wave 3, which is helpful.
- **Recommended fix:** Keep the installation and purchase records for these items.

### 15. Daitend's own assignment limits and clinic scope **[LOW; ask]**

- **Where:** MSA §15.3 (Daitend cannot assign without consent); MSA §1.3 and §2.4 (Clinic Locations and Affiliates); MSA §2.2 (new locations require an Order Form).
- **Why it matters:** If the client plans to acquire or sell clinics, the Services may not follow those clinics without consent or an Order Form.
- **Recommended fix:** Ask whether any acquisitions or disposals are planned. Address this in any renewal or exit amendment.

### 16. Preserve internal emails **[LOW; prompt if a dispute is likely]**

- **Where:** The Emails (non-lawyer internal correspondence, no counsel copied).
- **Why it matters:** These emails are likely not privileged and may be discoverable in a dispute over migration, data retention or service quality. They describe the migration and the legacy-server disposal plan.
- **Recommended fix:** Issue a preservation notice to the working group and the COO. Route further discussion of the contract position through counsel.

---

## Facts We Need From the Client

**Renewal and notice**
1. Was any notice of non-renewal or other written communication sent to Gaiport between May 3 and June 2, 2026?
2. How and when was the July 20 Letter delivered? Do we have the signed, as-sent copy and the courier's proof of delivery and date?
3. Has Gaiport responded in writing or orally? Did it acknowledge expiration or say the agreement would renew?
4. What invoices has Gaiport issued since September 1, 2026, and what has Daitend paid? Is there any suspension notice?
5. Has Daitend been using the Imaging Module continuously through today?
6. What is the client's objective: exit, or stay on renegotiated terms?

**Data**
7. Has Daitend sent any written export request since August 31, 2026? Has any export begun?
8. Does Daitend hold any copy of historic radiographs or charts outside Gaiport? Were the legacy servers actually decommissioned, and were disposal certificates produced?
9. Who verified migration for Waves 2 and 3, and what reconciliation records exist?
10. Has Daitend ever received notice of a security incident, or observed any suspicious activity?
11. Does Daitend have a BAA with Gaiport? Does Zendesk or any other vendor receive patient information?

**Documents**
12. Fully executed MSA, DPA, all Order Forms, SOWs and amendments.
13. Any Imaging Module Order Form and the fee it sets.
14. Gaiport's certificates of insurance, SOC 2 report and uptime or ticket reports.

**Operations**
15. Do any clinics open on Saturdays or outside 7:00 a.m. to 8:00 p.m. ET?
16. Are there any planned acquisitions, disposals or new locations?
17. What are Daitend's record-retention obligations under applicable state rules, and what does its patient privacy notice say about processing by vendors?

---

## Scope and Limits

- This memo relies only on the four documents in the matter folder. I did not review invoices, Order Forms, correspondence after July 20, 2026, or any Gaiport communications.
- The copies of the MSA, DPA and Letter in the folder have blank signature blocks. I have assumed they were executed in this form, but that must be confirmed.
- Points marked "outside the folder" (HIPAA business associate requirements and state dental-records retention) reflect general legal knowledge and should be verified before advice goes to the client.
- Date calculations use the MSA's stated terms and count days as calendar days. Day counts assume a 30-day export period beginning August 31, 2026, and a 60-day deletion period beginning September 30, 2026. Both should be checked against the facts once the client confirms the timeline.