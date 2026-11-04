# Memorandum

**PRIVILEGED AND CONFIDENTIAL. ATTORNEY WORK PRODUCT.**

**To:** Supervising Partner
**From:** Associate
**Date:** November 2, 2026
**Client:** Daitend Dental Partners, LLC ("Daitend")
**Counterparty:** Gaiport Practice Systems, Inc. ("Gaiport")
**Re:** Issues review of the Gaiport relationship and recommended fixes

**Sources reviewed (abbreviations used below):**
- **MSA**: daitend_gaiport_master_services_agreement.md (Effective Date March 1, 2024)
- **DPA**: daitend_gaiport_data_processing_addendum.md (dated March 1, 2024)
- **Letter**: daitend_non_renewal_letter_2026-07-20.md (dated July 20, 2026)
- **Emails**: daitend_internal_imaging_rollout_emails.md (Sept. 2024 to Dec. 2024)

---

## Bottom Line

Daitend's non-renewal notice appears to be **untimely**. Under MSA §12.2 the notice window closed on June 2, 2026, and the Letter is dated July 20, 2026. On that basis the MSA likely **auto-renewed on September 1, 2026 for 36 months, through August 31, 2029**, at $18,400 per month. The MSA has no termination-for-convenience right, so Daitend's exit options are now negotiation or a for-cause argument.

Separately, the DPA does not cover patient health information (PHI), which is the core of what Gaiport hosts. No Business Associate Agreement (BAA) appears in the folder. The risk allocation also runs against Daitend: Daitend indemnifies Gaiport for Customer Data incidents "regardless of whether caused by Gaiport," and that indemnity sits outside the liability cap.

Items 1 through 5 below need action this week.

---

## Priority Summary

| # | Issue | Urgency | Where |
|---|---|---|---|
| 1 | Non-renewal notice untimely; MSA auto-renewed to Aug. 31, 2029 | **Immediate** | MSA §§12.1, 12.2, 13, 16.2, 16.3; Letter §1 |
| 2 | PHI outside DPA protections; no BAA in folder | **Immediate** | MSA §§1.4, 2.3, 7.1, 7.3; DPA §§1.1, 1.3, 1.6, 2.2, 5, 6.1, 8, 9, Annex A |
| 3 | Uncapped Daitend indemnity for Customer Data incidents, including Gaiport-caused; one-sided liability | **High** | MSA §§9.1(a), 9.2, 10.1–10.3 |
| 4 | Data exit gap: no in-term export; legacy image copies decommissioned; Waves 2–3 migration checks undocumented | **Immediate** (request export now) | MSA §§7.4, 13.4; DPA §§9.1–9.3; Letter §3; Emails 4–7 |
| 5 | Payment and suspension exposure during dispute | **Immediate** | MSA §§4.2–4.4, 13.3; Letter §2 |
| 6 | Gaiport may assign the MSA and Customer Data without consent or notice | High | MSA §§1.10, 3.1, 15.3, 15.4 |
| 7 | Subprocessor changes without a meaningful objection right | High | DPA §§7.1–7.3; Annex C |
| 8 | Limited security assurance, audit rights, insurance limits, force majeure | High | DPA §§5.3, 5.4; MSA §§14.1, 16.4; DPA Annex B |
| 9 | Weak service levels and exclusive remedies | Medium | MSA §§3.4, 3.5, 11.2, 13.1 |
| 10 | Fixed fee for 22 locations; no reduction right; Order Forms missing | Medium | MSA §§2.2, 4.1, 12.2 |
| 11 | Daitend hardware and firmware obligations; Documentation can change | Medium | MSA §§1.6, 5.2, 9.1(c); Emails 2, 7 |
| 12 | Oral assurance that DICOM exports keep calibration data | Low–Medium | Email 3; MSA §§7.4, 11.3 |
| 13 | Housekeeping: unsigned copies, notice address, publicity | Low | MSA §§16.2, 16.6, signature pages; DPA signature page; Letter |

---

## Issue 1: Non-Renewal Notice Was Untimely; MSA Likely Renewed Through August 31, 2029

**Where:** MSA §12.1 (Initial Term ends Aug. 31, 2026), §12.2 (renewal and notice window), §13 (termination rights), §16.2 (notice mechanics), §16.3 (amendments in writing); Letter §1.

**Why it matters:**
- MSA §12.2 requires non-renewal notice "not more than one hundred twenty (120) days and not less than ninety (90) days before the end of the then-current Initial Term." For an Aug. 31, 2026 end date, the window was **May 3, 2026 to June 2, 2026**.
- The Letter is dated **July 20, 2026**, which is 42 days before the end date. It missed the last permissible date by about 48 days. Under MSA §16.2 a notice is effective on receipt, so the July 21 receipt date (if overnight delivery was next-day) does not help.
- Absent an effective notice, the MSA renewed on September 1, 2026 for a Renewal Term of 36 months, ending **August 31, 2029**, at the Subscription Fee then in effect (MSA §12.2). The MSA sets $18,400 per month for 22 locations (MSA §4.1) and contains no escalator. Remaining committed fees: 36 months × $18,400 = **$662,400**, less any amounts already paid for September and October 2026 (roughly $625,600 remains as of today if those two months were paid).
- The Letter itself states the Agreement "will expire ... on August 31, 2026." That date has passed. Gaiport will likely rely on §12.2 and treat the Letter as ineffective.
- The MSA has **no termination for convenience**. Daitend's exit routes are limited to for-cause termination for an uncured material breach with 30 days' notice and cure (MSA §13.1), insolvency (§13.2), or a negotiated amendment signed by both parties (§16.3).
- Email is not notice (MSA §16.2). Any earlier emails between May and June 2026 likely do not cure the timing problem.
- Context: the Emails show the Imaging Module is now embedded across all 22 clinics, with legacy servers decommissioned (Emails 5–7). The MSA was not a short-term tool, which makes a forced exit operationally costly.

**Recommended fix:**
1. **Today:** Confirm whether Gaiport has invoiced and Daitend has paid for September, October, and November 2026. Payment or continued use may be treated as acceptance of the renewal.
2. Pull the courier receipt for the Letter and confirm the delivery address. The MSA's notice block lists only "Attn: General Counsel, Gaiport Practice Systems, Inc." with no street address (MSA signature page). Confirm what address was used and whether delivery was signed for.
3. Confirm whether any formal (courier, hand, or certified mail) notice was sent between May 3 and June 2, 2026.
4. Do not characterize the Letter as an effective notice in new correspondence unless we conclude it is. Consider a without-prejudice letter to Gaiport proposing a negotiated early termination or a renewal amendment.
5. Evaluate for-cause arguments under MSA §13.1 (e.g., the BAA and DPA gaps in Issue 2, if they amount to material breach). On the current record (Emails 5–7 report no Severity 1 incidents), this is weak.
6. Use the renewal as leverage. A realistic path is a signed amendment (MSA §16.3) that accepts the renewal in exchange for fixing Issues 2–6 and 9, or a buy-out with a transition period and data export.
7. **Calendar the next window:** non-renewal notice for the current renewal term must be given between **May 3, 2029 and June 2, 2029** (MSA §12.2). Send by courier with a receipt, well before June 2, 2029, and set internal reminders for April 2029.

**Facts we need:** the Letter's delivery receipt and address used; any Gaiport response; invoices and payments since September 1, 2026; the decision record for non-renewal (who decided, when, and whether anyone identified the §12.2 deadline; the Emails stop in December 2024); the business reason for leaving; cost and timeline of any replacement platform; and whether Daitend wants to stay on the platform on better terms.

---

## Issue 2: Patient Health Information Is Outside the DPA; No BAA in the Folder

**Where:** MSA §1.4 (Customer Data includes PHI and radiographic images), §2.3 (DPA controls as to "personal data"), §7.1 (safeguards "as further described in the DPA"), §7.3 (incident notice "in accordance with the DPA"); DPA §1.1 ("Customer Personal Data ... excluding Patient Health Information"), §1.3 (PHI definition), §1.6 (Security Incident limited to Customer Personal Data), §2.2 (scope), §3.1 (documented instructions), §§5.2–5.4 (encryption, pen testing, SOC 2), §6.1 (72-hour notice), §8.1 (individual requests), §9.3 (deletion certificate), Annex A (categories of individuals: staff only).

**Why it matters:**
- MSA §1.4 defines Customer Data to include PHI and radiographic images. Those are the most sensitive data Gaiport holds for Daitend.
- DPA §1.1 expressly excludes PHI from "Customer Personal Data." Nearly all DPA protections are keyed to Customer Personal Data: encryption (§5.2), pen testing (§5.3), SOC 2 access (§5.4), the 72-hour incident notice (§6.1), individual-request handling (§8.1), and the deletion certificate (§9.3).
- Annex A describes only staff as data subjects. Patient data processing is not described at all, so Gaiport's documented instructions (§3.1) do not clearly cover the core processing.
- "Security Incident" requires a **confirmed** breach (DPA §1.6). Suspected incidents do not trigger notice. The MSA's §7.3 notice obligation points back to the DPA and so inherits the same gap.
- Gaiport hosts PHI on behalf of a dental group, which makes Gaiport a business associate. HIPAA generally requires a written BAA with the business associate (45 C.F.R. §§164.502(e), 164.504(e)). **No BAA appears in the folder.** Whether one exists elsewhere is a critical question. This should be confirmed with HIPAA counsel.
- A missing or inadequate BAA also weakens Daitend's position on the exit (Issue 4), because return and deletion obligations for PHI are not clearly defined.

**Recommended fix:**
1. **Immediately** ask Daitend for any BAA or HIPAA addendum with Gaiport. If none exists, require one at once, or amend the DPA, with terms covering all PHI.
2. The BAA or amendment should: (a) cover all PHI and radiographic images; (b) define Security Incident to include suspected incidents; (c) require breach notice to Daitend within a short contractual period (e.g., 72 hours from discovery of a suspected or confirmed incident, with the HIPAA outer limit of 60 days from discovery as a backstop); (d) include individual-request assistance, accounting-of-disclosures support, and return or deletion of PHI with officer certification; and (e) require Gaiport to flow down equivalent terms to subprocessors, including Zendesk, which handles support tickets.
3. Ask Gaiport for its HIPAA compliance documentation, including its risk analysis, and confirm that AWS, Okta, and Zendesk have BAAs with Gaiport.
4. Reconcile MSA §2.3 and DPA §1.1 so that PHI is expressly governed by the DPA or BAA, and the MSA's references to "personal data" are not read to exclude PHI.

**Facts we need:** whether a BAA exists; whether Daitend has completed its own HIPAA risk analysis and whether it covers the Gaiport platform; whether any security incident has occurred; whether support tickets include PHI.

---

## Issue 3: Daitend's Uncapped Indemnity for Customer Data Incidents; One-Sided Risk Allocation

**Where:** MSA §9.1(a) (Daitend indemnifies for Customer Data incidents "regardless of whether caused by Gaiport," including regulatory fines and penalties); §9.1(c) (Daitend breach of §5); §9.2 (Gaiport indemnity limited to U.S. IP claims, excluding Customer Data claims); §10.1 (cap: fees paid in prior 12 months); §10.2 (consequential damages excluded); §10.3(a) (indemnities excluded from the cap and the consequential-damages exclusion); DPA §10.1.

**Why it matters:**
- Daitend would indemnify Gaiport, without limit, for third-party claims and regulatory fines arising from a Gaiport-caused data breach. Under §10.3(a), that exposure is outside the cap.
- Gaiport's own exposure for a data breach it causes is capped at 12 months of fees, which is about **$220,800** at the current rate (MSA §10.1). Its consequential-damages exclusion (§10.2) would likely bar Daitend's patient-notification, forensic, and lost-revenue losses.
- Gaiport's indemnity covers only IP infringement (MSA §9.2). There is no Gaiport indemnity for data breaches, HIPAA violations, or subprocessor failures.
- Result: Gaiport bears little of the breach risk for the data it controls, and Daitend bears most of it.

**Recommended fix:**
1. Limit §9.1(a) to Customer Data incidents to the extent caused by Daitend or its Authorized Users.
2. Add a Gaiport indemnity for losses caused by a Security Incident in Gaiport's or its subprocessors' possession, including regulatory fines to the extent permitted by law.
3. Carve data-protection and confidentiality breaches out of §10.1 with a separate "super-cap," for example a multiple of annual fees or the cyber insurance limit, whichever is higher.
4. Define breach-response costs (notification, call center, credit monitoring, forensics, legal fees) as direct damages recoverable from Gaiport.

**Facts we need:** Gaiport's cyber insurance limits (see Issue 8); any incident history; whether Daitend has ever been asked to indemnify Gaiport or has received a claim.

---

## Issue 4: Data Exit Gap; Legacy Image Copies Decommissioned; Migration Checks Undocumented

**Where:** MSA §7.4 (export only for 30 days after expiration or termination, on written request, in DICOM for images); §13.4 (access ends at expiration, subject to §7.4); DPA §§9.1–9.3 (export period, deletion within 60 days after export period, backups up to 180 days, officer certification); Letter §3 (export request); Emails 4 (migration plan and reconciliation), 5 (pilot results), 6 (Wave 2 readiness), 7 (closeout and decommissioning).

**Why it matters:**
- The MSA has **no right to export data during the Term.** Export is available only after expiration or termination. Because the MSA has renewed (Issue 1), the export period has not started, and the Letter's export request (§3) was made before any expiration. The request is at best premature.
- Daitend's legacy imaging servers were decommissioned after a 90-day fallback (Email 4; Email 7 says Wave 1 in early January 2025, Waves 2 and 3 on the same cadence). Gaiport likely holds the **only** copy of historic radiographs, which Daitend needs for patient care and recordkeeping.
- For the pilot, Gaiport ran a record-count reconciliation and Marcus Lindqvist spot-checked 50 charts per clinic (Emails 4, 5). For Waves 2 and 3, the Emails show only "scheduled" migrations and a closeout that says the rollout "went smoothly" (Emails 6, 7). No reconciliation or spot-check results for Waves 2 and 3 appear in the folder.
- Disposal certificates for the legacy servers are promised (Email 7) but are not in the folder.
- Under DPA §9.2, deletion can follow the export period. An exit without a verified complete export is a significant clinical and compliance risk.

**Recommended fix:**
1. **Now:** Send a written request for a complete export of all Customer Data, including DICOM images with calibration data and structured records, as an operational request. Ask for a test export and a data-integrity report. Gaiport has no obligation to provide this during the Term, so frame it as a request.
2. Obtain Waves 2 and 3 reconciliation records and the legacy-server disposal certificates. If they do not exist, ask Gaiport to perform a reconciliation against the legacy-migrated record counts.
3. In any amendment, add: an in-Term export right at any time at no added charge; an exit assistance period of at least 90 to 180 days at then-current fees; and a deletion obligation that does not begin until Daitend confirms receipt and integrity of the export.
4. Confirm internally that Daitend's record-retention obligations (state law and any payer requirements) are met by the export plan.

**Facts we need:** whether Daitend has ever done a test export; the Daitend record-retention schedule; whether Gaiport completed reconciliations for Waves 2 and 3; whether any clinic has encountered missing images since migration.

---

## Issue 5: Payment and Suspension Exposure During the Dispute

**Where:** MSA §4.2 (monthly invoicing in advance; payment within 30 days of undisputed invoices), §4.3 (good-faith withholding requires written notice before due date with reasonable detail), §4.4 (1% monthly interest on undisputed late amounts), §13.3 (Gaiport may suspend access for undisputed amounts unpaid more than 30 days after written notice); Letter §2 (Daitend will pay "for the remaining months of the Initial Term").

**Why it matters:**
- Gaiport runs scheduling and imaging for 22 clinics. Suspension would affect patient care, not just finance.
- The Letter says Daitend will pay only for the "remaining months of the Initial Term." That is inconsistent with the renewal. If Daitend stops paying after August 31, 2026, Gaiport can treat the amounts as undisputed and suspend after notice (§13.3).
- Withholding payment as leverage is risky. Daitend's non-renewal position is weak (Issue 1), so Gaiport would likely argue the withheld amounts are not disputed in good faith.

**Recommended fix:**
1. Confirm the current payment status and whether any invoice is unpaid.
2. If Daitend is paying, continue under a written reservation of rights that the renewal and the notice are disputed. Do not withhold.
3. If Daitend wants to dispute specific invoices, send a §4.3 notice before each due date with reasons. Keep the dispute narrow and documented.
4. Ask for a standstill: Gaiport agrees not to suspend while the parties negotiate, and Daitend keeps paying under reservation. Put any standstill in writing.
5. Brief the clinical leadership and the COO on the suspension risk and a contingency plan (e.g., a manual scheduling and paper-imaging fallback).

**Facts we need:** invoices and payments since September 1, 2026; any Gaiport notice of non-payment; whether the COO authorized the Letter and its payment statement.

---

## Issue 6: Gaiport Can Assign the MSA and Customer Data Without Consent or Notice

**Where:** MSA §1.10 ("Permitted Assignee" includes any acquirer of assets or business, and any lender, investor, or financing party, including their agents), §15.3 (Daitend's assignment requires consent, not to be unreasonably withheld), §15.4 (Gaiport may assign to any Permitted Assignee "together with any associated rights, obligations and Customer Data ... without Customer's consent and without notice"), §3.1 (non-transferable license).

**Why it matters:**
- Gaiport can transfer Daitend's PHI and operational data to a buyer, including a competitor, a sponsor-owned entity, or a financing party's agent, without telling Daitend.
- The asymmetry is notable. Daitend cannot assign the MSA even to a buyer of its clinics without Gaiport's consent (§15.3), while Gaiport can move the MSA freely.
- The DPA's subprocessor-change notice (§7.2) does not clearly reach an assignee that takes over the whole business.

**Recommended fix:**
1. Require at least 60 days' prior written notice of any assignment or change of control of Gaiport, and the right to terminate without penalty and receive a pro-rata refund if the assignee is a competitor or fails a security review.
2. Require any assignee to assume the DPA and any BAA in writing.
3. Delete or narrow §1.10(c) so that financing parties cannot receive Customer Data.
4. Make the assignment right reciprocal: Daitend may assign to an Affiliate (§2.4) or to a buyer of all or substantially all of its clinics without consent.

**Facts we need:** whether Daitend expects a transaction (sale, acquisition, financing) that would require an assignment; whether Gaiport has disclosed any ownership change; Daitend's growth plans, since new clinics require new Order Forms.

---

## Issue 7: Subprocessor Changes Without a Meaningful Objection Right

**Where:** DPA §7.1 (general authorization), §7.2 (30 days' notice; objection leads only to good-faith discussion), §7.3 (flow-down of DPA terms; Gaiport remains responsible), Annex C (Amazon Web Services, Okta, Zendesk); MSA §15.2.

**Why it matters:**
- Daitend's only remedy for an objectionable new subprocessor is a discussion. There is no right to refuse, no termination right, and no refund.
- Zendesk handles support tickets (Annex C). Support tickets can contain patient information. The folder does not show whether a BAA covers Zendesk.
- The flow-down in §7.3 requires "data-protection obligations," not BAA terms.

**Recommended fix:**
1. Give Daitend a right to object on reasonable grounds, with a right to terminate affected Services with a pro-rata refund if the objection is not resolved within 30 days.
2. Require flow-down of BAA-equivalent terms to all subprocessors handling PHI.
3. Require Gaiport to confirm, at least annually, the current subprocessor list and the data categories each handles.
4. Ask Gaiport to confirm what patient data Zendesk receives and whether it is restricted or redacted.

**Facts we need:** whether Daitend has received any subprocessor-change notice; the data included in support tickets.

---

## Issue 8: Limited Security Assurance, Audit Rights, Insurance Limits, and Force Majeure

**Where:** DPA §5.3 (annual third-party penetration test; results not requested), §5.4 (one SOC 2 Type II report per year, on request; report is Gaiport confidential information), Annex B (controls, including MFA, 12-month logs, annual incident-response testing, and geographically separate backups); MSA §14.1 (cyber liability insurance "customary" limits; certificates "on reasonable request"), §16.4 (force majeure, including "beyond its reasonable control" and telecommunications failures), §3.5 (outages from §16.4 events excluded from availability).

**Why it matters:**
- Daitend has no audit right, only one SOC 2 report per year, and no right to penetration-test summaries. Daitend cannot independently verify the controls that protect its PHI.
- Insurance is required but without minimum limits. Certificates are available only "on reasonable request."
- Force majeure could be argued to cover a cyberattack or telecommunications failure as an event "beyond reasonable control." That would excuse Gaiport's availability performance (§§3.5, 16.4).
- Annex B controls apply to Customer Personal Data (staff data), not PHI (Issue 2).

**Recommended fix:**
1. Require annual delivery of the SOC 2 Type II report and the penetration-test executive summary, plus a bridge letter covering any gap period, without the once-per-year limit on request.
2. Add an audit right triggered by a security incident or regulator request.
3. Require cyber insurance with stated minimum limits (for example, a figure tied to the records held), a certificate annually, and notice of cancellation or material change.
4. Carve cyberattacks and security incidents out of §16.4, and require Gaiport to maintain and test business continuity and disaster recovery at least annually (Annex B item 7 already requires BCP; add testing).

**Facts we need:** the date and exceptions in Gaiport's latest SOC 2 report; penetration-test results; current insurance certificates and limits; the number of patient records Gaiport holds for Daitend.

---

## Issue 9: Weak Service Levels and Exclusive Remedies

**Where:** MSA §3.4 (support 7:00 a.m. to 8:00 p.m. ET on business days; Severity 1 support 24/7 "in accordance with the Documentation"; Severity 1 is not defined in the MSA), §3.5 (99.5% availability on a "commercially reasonable efforts" basis; no credits), §11.2 (correction within 30 days as exclusive warranty remedy), §13.1 (30-day cure); Email 5 (support "covers our clinic hours").

**Why it matters:**
- Availability is an efforts obligation, not a guarantee. There are no service credits and no termination right for chronic failure.
- The warranty remedy in §11.2 is exclusive. Gaiport has 30 days to correct, and the fallback is termination of the affected Services with a refund of prepaid fees for the "then-current term." That is a weak remedy for a platform used by 22 clinics.
- Email 5's statement that support hours cover clinic hours is an assumption. The folder does not contain clinic hours. If any clinic opens on Saturdays or after 8:00 p.m., support does not cover it.
- Severity definitions depend on the Documentation, which is not in the folder and can change (MSA §1.6).

**Recommended fix:**
1. Replace "commercially reasonable efforts" with a firm 99.5% commitment, with service credits (e.g., a percentage of the monthly fee per shortfall) and a termination right for chronic failure (e.g., three misses in six months).
2. Define Severity 1 and 2 in the MSA, with response and resolution times.
3. Extend support to the clinic hours of every location, and confirm 24/7 telephone support for Severity 1 issues.
4. Make the §11.2 remedy non-exclusive and add a refund of unused fees plus a transition period.

**Facts we need:** clinic operating hours; outage and ticket history since December 2024; any Severity 1 events since the rollout.

---

## Issue 10: Fixed Fee for 22 Locations; No Reduction Right; Order Forms Missing

**Where:** MSA §4.1 ($18,400 per month for 22 Clinic Locations; additional locations or modules per Order Form), §2.2 (Order Forms incorporated), §1.3 (Clinic Location must be listed in an Order Form), §1.11 (Platform includes the Imaging Module), §12.2 (renewal at fees then in effect).

**Why it matters:**
- The fee is tied to 22 locations. If any clinic closes or is sold, the MSA has no mechanism to reduce fees.
- The Order Forms are not in the folder. We cannot confirm whether the Imaging Module carries a separate fee, whether the 22 locations are the ones listed, or whether any Order Form has different terms.
- The renewal rate is "then in effect," which could be read to allow Order Form changes to flow into the renewal price.

**Recommended fix:**
1. Obtain all Order Forms and invoices since March 2024.
2. Add a right to remove a Clinic Location on notice, with a corresponding fee reduction.
3. Confirm no escalator applies to the renewal term, or cap any increase.

**Facts we need:** all Order Forms; invoice history; any planned clinic closures or sales.

---

## Issue 11: Daitend Hardware and Firmware Obligations; Documentation Can Change

**Where:** MSA §1.6 (Documentation is "then-current" and Gaiport-controlled), §5.2 (Daitend maintains compatible hardware per the Documentation), §9.1(c) (Daitend indemnifies for breach of §5), §10.3(a) (indemnity uncapped); Email 2 (14 workstations below minimum RAM; two panoramic units need manufacturer firmware; three clinics need sensor driver updates); Email 7 (workstations and driver updates installed on schedule).

**Why it matters:**
- Daitend's hardware obligations depend on a Gaiport document that can change. A future specification change could put Daitend in breach of §5.2, and a §5.2 breach triggers the uncapped indemnity in §9.1(c).
- Email 7 confirms workstations and driver updates were completed. It does not confirm that the two panoramic-unit firmware updates were completed (Email 2 says service visits were requested).

**Recommended fix:**
1. Confirm completion of the panoramic-unit firmware updates in writing.
2. Obtain the Documentation version in effect at signing and the current version.
3. Require that changes to hardware specifications be made with at least 90 days' notice and do not require replacement of hardware Daitend has already purchased, unless a Gaiport-caused defect requires it.
4. Limit §9.1(c) to Daitend breaches of §5 that cause the third-party claim.

**Facts we need:** completion status of the panoramic firmware updates; current workstation and sensor inventory against the current spec.

---

## Issue 12: Oral Assurance on DICOM Calibration Data

**Where:** Email 3 (exports "are in DICOM format and keep the calibration data," confirmed "with Gaiport support"); MSA §7.4 (export in DICOM format); §11.3 (disclaimer of other warranties).

**Why it matters:** Measurement accuracy in exported radiographs matters clinically. The assurance was given informally by support staff and is not in the contract. Under §11.3 it is not a warranty.

**Recommended fix:** Obtain written confirmation from Gaiport that exports preserve calibration and measurement metadata. Add that requirement to §7.4. Run a test export and compare measurements before relying on it.

**Facts we need:** whether any clinic has used exported images for measurement.

---

## Issue 13: Housekeeping Items

- **Unsigned copies.** The signature blocks of the MSA and DPA are blank in the folder copies, and the Letter's signature line is blank. Obtain fully executed copies. If the MSA was not executed, our analysis of the renewal and the notice changes.
- **Notice address.** The MSA's notice block gives "Attn: General Counsel" with no street address (MSA signature page). Confirm the correct address for future notices under §16.2, and ask Gaiport to provide it in writing.
- **Publicity.** MSA §16.6 bars either party from using the other's name in marketing without consent. Confirm Gaiport has not used Daitend's name in marketing.
- **Internal emails.** The Emails are business communications and are likely discoverable. Route further discussion of the dispute through counsel and mark it as privileged where appropriate.
- **Governing law and forum.** MSA §16.1 selects Delaware law and exclusive Delaware courts. Note this for any dispute strategy; we have not analyzed Delaware law for this memo.

---

## Consolidated Facts We Need from the Client

1. Whether a BAA or HIPAA addendum with Gaiport exists, and any HIPAA risk analysis Daitend has done.
2. The courier receipt for the July 20 Letter, the address used, and the delivery date.
3. Any notice or correspondence with Gaiport between May 3 and November 2, 2026, including any response to the Letter.
4. All invoices and payment records since March 2024, especially from September 1, 2026.
5. Who decided on non-renewal, when, and whether anyone identified the §12.2 deadline. Also the business reasons and whether Daitend would still leave on better terms.
6. All Order Forms, the Documentation version in effect at signing, and the current Documentation.
7. Fully executed copies of the MSA, DPA, and any amendments.
8. Records of the Waves 2 and 3 migration reconciliations and the legacy-server disposal certificates.
9. Any test export history and Daitend's record-retention schedule.
10. Any security incident, unauthorized access, or patient complaint related to the platform.
11. Gaiport's SOC 2 Type II report, most recent penetration-test summary, and insurance certificates.
12. Clinic operating hours for all 22 locations.
13. Current subprocessor notices received, and the data categories included in support tickets.
14. Whether any clinic is closing, being sold, or planned for change, and Daitend's growth plans.
15. Whether Daitend has an alternative platform in view, its cost, and the time needed to migrate 22 clinics.
16. Completion status of the panoramic-unit firmware updates (Email 2).

---

## Limits of This Review

This memo relies solely on the four documents in the matter folder. We have not reviewed the Order Forms, the Documentation, any BAA, any Gaiport SOC 2 or penetration-test report, insurance certificates, invoices, or any correspondence after the Letter. The HIPAA observations are preliminary and should be confirmed by privacy counsel. We have not researched Delaware law on the enforceability of the renewal, the notice timing, or the indemnity provisions; that research should follow before we advise Daitend on litigation positions.