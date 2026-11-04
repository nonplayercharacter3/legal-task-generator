# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Daitend Dental Partners, LLC – Gaiport Clinical Systems, Inc. MSA Review: Issues and Recommended Changes

---

## Summary

I reviewed the four documents in the matter folder. The arrangement has several significant problems for Daitend, the most serious being a definitional conflict between the MSA and the DPA that appears to exclude diagnostic images (and possibly other clinical data) from the business associate agreement's protections. In addition, Daitend has an uncapped indemnity obligation that applies even when Gaiport causes the underlying claim, is now locked into a 36-month renewal at a 15% price increase, and has no consent right over assignment of the contract. Details and proposed fixes follow.

---

## Issue 1 (Critical): DPA "Patient Data" Definition Excludes Diagnostic Images and Is Limited to Scheduling/Billing Records

**Where:** DPA § 1.1 (definition of "Patient Data"); MSA § 1.1 (definition of "Patient Data"); MSA § 2.3 (order of precedence).

**Description.** The MSA defines "Patient Data" as "all patient health information, including radiographs, intraoral scans and other diagnostic images" (MSA § 1.1). The DPA defines "Patient Data" as "Protected Health Information relating to patients of Customer or its Clinic Locations that is contained in Customer's scheduling and billing records created, received, maintained or transmitted by Provider through the Platform, **excluding diagnostic images**" (DPA § 1.1). These definitions directly conflict. Under MSA § 2.3, the DPA prevails over the MSA in case of conflict. Therefore, the operative definition of "Patient Data" is the DPA's narrower one.

The practical effect is twofold:

- **Diagnostic images are excluded.** Radiographs, intraoral scans, and other imaging data—despite being PHI under HIPAA—are not "Patient Data" under the DPA. They are "Customer Data" under the MSA (MSA § 1.1) but fall outside the DPA's security requirements (DPA § 5.2), breach notification obligations (DPA § 5.3), individual rights provisions (DPA § 6), and return/deletion terms (DPA § 7).
- **The DPA is limited to "scheduling and billing records."** Even setting aside the image exclusion, the DPA's definition is confined to PHI "contained in Customer's scheduling and billing records." The Platform is described as a "dental practice-management, scheduling, billing and imaging platform" (MSA, Background). It is reasonable to assume the platform also stores treatment plans, clinical notes, and other PHI. Those data types may also fall outside the DPA's scope.

**Why it matters.** The DPA "also serves as the Parties' business associate agreement under HIPAA" (MSA § 1.1, definition of "DPA"; DPA, Background). A BAA must cover all PHI that a business associate creates, receives, maintains, or transmits on behalf of the covered entity (45 C.F.R. § 164.504(e)). If the DPA's "Patient Data" definition is read to exclude diagnostic images and non-scheduling/billing clinical data, then Gaiport is handling PHI outside the BAA's scope. This creates:

- A HIPAA compliance gap for Daitend as the covered entity. Daitend could be exposed to OCR enforcement for failing to have an adequate BAA in place for all its business associates' PHI handling.
- A practical gap: if a breach occurs involving imaging data, the DPA's breach notification, mitigation, and cost-reimbursement provisions (DPA §§ 5.3–5.5) may not apply.
- An indemnification complication: MSA § 10.2 requires Daitend to indemnify Gaiport for "Customer Data Claims," which are defined to include claims "arising out of or relating to any Customer Data." Because "Customer Data" includes all data (MSA § 1.1), Daitend's indemnity obligation extends to diagnostic images even though the DPA's protections do not. Daitend bears the regulatory risk for image-related breaches but lacks the contractual tools (breach notification, mitigation, cost reimbursement) that the DPA provides for other data types.

The Severna Park onboarding makes this concrete: 41,906 radiographs and intraoral scans were migrated to the Platform (Email Thread, Message 8). Those images are now in Gaiport's environment but appear to be outside the DPA's protective framework.

**Recommended fix.** Amend DPA § 1.1 to align with the MSA's definition and to cover all PHI processed through the Platform. Proposed language:

> "**Patient Data**" means all Protected Health Information relating to patients of Customer or its Clinic Locations that is created, received, maintained, or transmitted by Provider or any Subcontractor through the Platform, including but not limited to scheduling records, billing records, clinical notes, treatment plans, radiographs, intraoral scans, and other diagnostic images.

Additionally, add a sentence to DPA § 2.1:

> "For the avoidance of doubt, Provider's obligations under this DPA extend to all PHI processed through the Platform, regardless of the module or data type."

This should be raised as a condition of the renewal term. If Gaiport resists, Daitend should at minimum require a side letter or amendment confirming that the BAA covers all PHI in the Platform and that the DPA's security and breach provisions apply to diagnostic images.

**Flag:** It is possible Gaiport's position is that diagnostic images are handled under a separate agreement or that the "scheduling and billing records" language was intended to be illustrative rather than limiting. The documents do not support either reading, but we should confirm with the client whether any separate imaging-specific BAA or data agreement exists.

---

## Issue 2 (High): Uncapped Customer Indemnity Applies Even When Provider Causes the Claim

**Where:** MSA § 10.2; MSA § 11.3(b).

**Description.** MSA § 10.2 requires Daitend to indemnify Gaiport for all "Customer Data Claims," which are defined as claims "arising out of or relating to any Customer Data uploaded to, entered into or stored on the Platform by or on behalf of Customer, including any enforcement action, civil money penalty or corrective action plan under HIPAA or state health privacy law, **whether or not caused or contributed to by any act or omission of Provider**." The phrase in bold is the critical problem: Daitend's indemnity obligation is triggered even if Gaiport's own negligence, security failure, or breach of the DPA caused or contributed to the claim.

MSA § 11.3(b) carves out "amounts payable under Section 10.2" from the liability cap in § 11.1. This means Daitend's indemnity exposure is **uncapped**.

**Why it matters.** Consider a scenario: Gaiport suffers a ransomware attack due to a failure to patch a known vulnerability. Patient data is exfiltrated. OCR assesses a civil money penalty against Daitend (as the covered entity) and Gaiport (as the business associate). Gaiport then asserts that Daitend must indemnify it for the OCR penalty under § 10.2, because the claim "arises out of or relates to" Customer Data. The "whether or not caused" language means Gaiport's own failure to patch does not reduce Daitend's indemnity obligation. And because § 11.3(b) removes the cap, Daitend's exposure is unlimited.

Meanwhile, Daitend's own recovery against Gaiport for the breach is subject to the § 11.1 cap (12 months of fees ≈ $220,800 at current rates, or ≈ $253,920 at renewal rates) and the § 11.2 exclusion of consequential damages. So Daitend could owe Gaiport an uncapped indemnity while its own recovery from Gaiport is capped at roughly $250,000.

This is compounded by Issue 1: if diagnostic images are outside the DPA, a breach of image data may not trigger the DPA's mitigation and cost-reimbursement provisions (DPA § 5.5), leaving Daitend without even the limited contractual remedy it would otherwise have.

**Recommended fix.** Amend MSA § 10.2 to exclude claims caused or contributed to by Provider. Proposed language:

> "Customer shall defend, indemnify and hold harmless Provider and its Affiliates, officers, directors and employees from and against any and all Customer Data Claims, **provided that Customer shall have no obligation under this Section 10.2 to the extent a Customer Data Claim is caused or contributed to by any act or omission of Provider, any Subcontractor, or any failure by Provider to comply with the DPA or applicable law** (collectively, the 'Provider Fault Carve-Out'). In the event a Customer Data Claim is caused or contributed to by both Customer and Provider, each Party shall be liable only for the portion of the claim attributable to its own acts or omissions."

Additionally, amend MSA § 11.3(b) to remove the uncapping of § 10.2, or at minimum to cap § 10.2 obligations at a multiple of the liability cap (e.g., 3× or 5× the 12-month fee cap) for claims not falling within the Provider Fault Carve-Out.

**Flag:** The "whether or not caused" language is aggressive and unusual. It may reflect Gaiport's standard form. We should ask the client whether this was negotiated or accepted as-is, and whether there is any side correspondence in which Gaiport acknowledged shared responsibility.

---

## Issue 3 (High): 36-Month Auto-Renewal with No Price Cap; Daitend Is Now Locked In

**Where:** MSA § 12.2; MSA § 4.3; Renewal Notice Letter §§ 2–3.

**Description.** MSA § 12.2 provides for automatic renewal for successive 36-month terms unless either party gives written notice of non-renewal "no earlier than 120 and no later than 90 days before the current term ends." The Initial Term ended December 31, 2026. The non-renewal window was therefore **September 2 through October 2, 2026** (120 days before December 31 = September 2; 90 days before = October 2). Gaiport's renewal letter, dated October 9, 2026, confirms that no non-renewal notice was given and that the Agreement renewed for a 36-month term through December 31, 2029.

MSA § 4.3 provides that renewal-term fees are "Provider's then-current rates for the Platform, as notified by Provider to Customer in writing at least sixty (60) days before the start of that Renewal Term." There is **no cap** on the increase. Gaiport's letter (dated October 9, 2026, which is 84 days before January 1, 2027) complies with the 60-day notice requirement and imposes a 15% increase: from $18,400 to $21,160 per month.

**Why it matters.**

- Daitend is contractually bound for 36 months (through December 31, 2029) at the increased rate. The annual cost increase is $33,120 ($2,760/month × 12), or $99,360 over the renewal term.
- At the next renewal (December 31, 2029), Gaiport can again unilaterally set "then-current rates" with no cap. If Gaiport's pricing continues to rise at 15% per cycle, the fee would be approximately $24,334/month by 2030.
- The non-renewal window is only 30 days long (120 to 90 days before term end). For a multi-location dental group, this is an operational trap: if the responsible person is on leave or the notice is missed, Daitend is locked in for another three years.
- Daitend has no termination right for convenience. The only termination rights are for material breach (§ 12.3) or insolvency (§ 12.4).

**Recommended fix.**

- **Near-term (this renewal term):** Negotiate a price cap or most-favored-customer provision for the duration of the current renewal term. If Gaiport will not agree to reduce the 15% increase, seek other concessions (e.g., extended non-renewal notice window, enhanced SLA credits, or a termination-for-convenience right with a reduced buyout).
- **For the next renewal cycle and future agreements:** Amend MSA § 12.2 and § 4.3. Proposed language:

> **§ 4.3 (amended):** "Fees for any Renewal Term shall not exceed the Fees in effect at the end of the then-current Term increased by the lesser of (a) five percent (5%) or (b) the annual increase in the Consumer Price Index for Urban Consumers (CPI-U) for the twelve-month period preceding the Renewal Term. Provider shall provide written notice of any Fee adjustment at least ninety (90) days before the start of the Renewal Term."

> **§ 12.2 (amended):** "Upon expiry of the Initial Term, this Agreement shall automatically renew for successive renewal terms of **twelve (12)** months each, unless either Party gives the other written notice of non-renewal no earlier than **180** and no later than **120** days before the current term ends."

Shortening the renewal term to 12 months and widening the non-renewal window to 60 days (180–120) reduces the lock-in risk substantially.

**Questions for the client:**
- Who was responsible for tracking the non-renewal deadline, and why was it missed? (This is relevant to internal process, not to the legal analysis, but it informs whether Daitend wants to implement a contract-calendar system.)
- Does Daitend have any leverage with Gaiport (e.g., Daitend is a top-10 customer by revenue) that could support a renegotiation?
- Is Daitend comfortable with the 15% increase for the current term, or does it want to push back before the January 2027 invoice?

---

## Issue 4 (High): Provider May Assign Without Customer Consent

**Where:** MSA § 15.3; MSA § 1.1 (definition of "Successor").

**Description.** MSA § 15.3 permits Gaiport to assign the Agreement "to any Successor without the consent of Customer, by written notice to Customer given within thirty (30) days **after** the assignment takes effect." The definition of "Successor" in MSA § 1.1 is broad: "any entity that acquires all or **any part** of the Platform business of Provider, or any of Provider's customer contracts, whether by merger, sale of stock, sale of assets or otherwise."

**Why it matters.**

- Daitend has no consent right. Gaiport could sell the dental practice-management business line (or even a portfolio of customer contracts that includes Daitend) to a competitor, a private equity firm, or a distressed buyer, and Daitend would be bound to the acquirer for the remainder of the term.
- The notice comes **after** the assignment, not before. Daitend learns of the change only after it has happened.
- The "any part" language means Gaiport could spin off the imaging module to one entity and the scheduling/billing module to another, potentially fragmenting Daitend's data across multiple providers.
- For a dental group handling sensitive patient data, the identity and security posture of the data processor matters. Daitend has no contractual mechanism to object to an acquirer with a poor security record or incompatible practices.
- The DPA is assigned along with the MSA (MSA § 15.3: "the Successor shall assume Provider's obligations under this Agreement and the DPA"), but Daitend has no right to terminate upon assignment.

**Recommended fix.** Amend MSA § 15.3. Proposed language:

> "**15.3 Provider Assignment.** Provider may assign this Agreement to a Successor only with Customer's prior written consent, not to be unreasonably withheld, conditioned or delayed, **provided that Customer's consent shall be deemed withheld if the Successor (a) is a direct competitor of Customer; (b) has, in the two years preceding the assignment, been subject to a HIPAA enforcement action, a material data breach, or a bankruptcy filing; or (c) does not assume in writing all of Provider's obligations under this Agreement and the DPA.** Provider shall give Customer at least sixty (60) days' prior written notice before any assignment. If Customer withholds consent for a reasonable basis, Customer may terminate this Agreement and any affected Statement of Work upon thirty (30) days' written notice, and Provider shall refund prepaid Fees for the unused portion and provide transition assistance under Section 13.2."

At minimum, if Gaiport will not accept a consent requirement, Daitend should insist on (a) prior notice (not after-the-fact), (b) a termination right if the Successor does not meet basic security standards, and (c) a requirement that the Successor execute a direct assumption of the DPA.

---

## Issue 5 (Moderate): Limited SLA Remedies; No Data Integrity Commitment

**Where:** MSA §§ 6.1–6.3.

**Description.** The SLA provides:

- 99.5% monthly availability (MSA § 6.1), excluding scheduled maintenance.
- Service credits of 5% of the monthly Platform Fee per 0.5% shortfall, capped at 25% of the monthly fee (MSA § 6.2).
- Support hours of 7 a.m. to 9 p.m. Eastern on business days, with 24/7 for Severity 1 (MSA § 6.3).

There is **no** service level for data integrity, data loss, or corruption. There is **no** termination right for chronic SLA failures (e.g., missing the availability target in 3 or more consecutive months). The maximum credit in any month is 25% of $21,160 = $5,290. For a multi-location dental practice, a full day of Platform downtime could cost far more in lost production than $5,290.

**Why it matters.** If Gaiport experiences a prolonged outage or a data corruption event (e.g., a failed update corrupts patient records), Daitend's only remedy is a service credit capped at 25% of one month's fee. Daitend cannot terminate for chronic underperformance short of proving "material breach" under § 12.3, which is a high bar.

**Recommended fix.**

- Add a data integrity SLA: "Provider shall ensure that Customer Data is not lost, corrupted, or made unavailable as a result of any Platform update, maintenance activity, or system failure. In the event of data loss or corruption caused by Provider, Provider shall restore the affected data from backup within the recovery time objective set forth in DPA § 5.2(e) and shall provide a service credit equal to fifty percent (50%) of the affected month's Platform Fee."
- Add a chronic failure termination right: "If Provider fails to meet the availability commitment in Section 6.1 in three (3) or more consecutive calendar months, or in five (5) or more calendar months in any twelve-month period, Customer may terminate this Agreement upon thirty (30) days' written notice without penalty, and Provider shall refund prepaid Fees for the unused portion."
- Increase the service credit cap from 25% to 50% of the monthly fee.

---

## Issue 6 (Moderate): Legacy Server Decommissioning Without Documented Secure Disposal

**Where:** Email Thread, Messages 10–11 (September 28, 2026).

**Description.** Priya Venkataraman's go-live email states: "The legacy server can be decommissioned once Daitend's records-retention review is complete." Daniel Reyes-Whitford responded: "We'll start the legacy server retention review next week." As of the last message in the thread (September 28, 2026), there is no indication that the retention review has been completed or that the server has been securely wiped.

The legacy server contained approximately 9 years of patient records and radiographs for the Severna Park practice. If the server is decommissioned without NIST SP 800-88–compliant media sanitization, there is a risk of data recovery and a potential HIPAA breach.

**Why it matters.**

- Daitend, as the covered entity, bears ultimate responsibility for the security of its PHI, including data on legacy systems that are being retired.
- The DPA's return/deletion provisions (DPA § 7) apply to data in Gaiport's environment, not to Daitend's own legacy hardware. Daitend is on its own for the secure disposal of the Severna Park server.
- If the server is discarded or repurposed without proper sanitization, and the data is later recovered, Daitend could face a reportable breach under HIPAA.
- There is no documentation in the file confirming that the server was securely destroyed.

**Recommended fix / action items:**

- Confirm with the client whether the Severna Park legacy server has been securely wiped or destroyed. If not, ensure it is sanitized in accordance with NIST SP 800-88 (Clear or Purge method, depending on whether the hardware will be reused or disposed).
- Document the disposal: date, method, person responsible, and certificate of destruction if applicable.
- Confirm that the records-retention review is complete and that Daitend's retention policy (and any Maryland-specific dental records retention requirements) has been satisfied before the server is decommissioned.
- If Daitend has other acquired practices with legacy systems, implement a standard decommissioning checklist that includes secure media sanitization.

**Questions for the client:**
- Has the Severna Park legacy server been decommissioned yet? If so, what method was used?
- What is Daitend's records retention policy for dental records? Does Maryland law impose a specific retention period (e.g., Maryland Health Occupations Article § 5-501 or Board of Dentistry regulations)?
- Are there other acquired practices with legacy systems pending decommissioning?

---

## Issue 7 (Moderate): No Routine Audit Right

**Where:** DPA § 8.3.

**Description.** Daitend's right to audit Gaiport's compliance with the DPA is limited to two triggers: (a) Gaiport suffers a Breach of Unsecured PHI, or (b) a regulator requires it. There is no right to conduct a routine or periodic audit. Daitend can request a SOC 2 Type II report once per year (DPA § 8.1) and send one security questionnaire per year (DPA § 8.2), but these are self-reported or limited-scope instruments, not a full audit.

**Why it matters.** For a multi-location dental group relying on a single platform for all clinical, scheduling, billing, and imaging operations, the absence of a routine audit right means Daitend has no contractual mechanism to verify Gaiport's compliance between breaches. If Gaiport's security posture degrades gradually (e.g., access controls are weakened, subcontractors are added without proper flow-downs, patching cadence slows), Daitend would not discover the problem until a breach occurs.

**Recommended fix.** Amend DPA § 8.3 to add a routine audit right:

> "In addition to the audit rights set forth above, Customer or its independent auditor, bound by confidentiality obligations, may conduct one (1) on-site or remote audit of Provider's compliance with this DPA in each twelve-month period, upon at least sixty (60) days' written notice, during normal business hours, and in a manner that does not unreasonably disrupt Provider's operations. The audit shall be at Customer's expense, provided that if the audit reveals a material compliance failure, Provider shall reimburse Customer's reasonable audit costs."

---

## Issue 8 (Moderate): Transition Assistance at Provider's Rates; 90-Day Window May Be Insufficient

**Where:** MSA § 13.2.

**Description.** Upon expiry or termination, Gaiport provides 90 days of read-only access and will export Customer Data "at Provider's then-current Professional Services rates." The export format is "an industry-standard, non-proprietary format (including DICOM format for diagnostic images)."

**Why it matters.**

- **Cost uncertainty.** "Then-current Professional Services rates" are not specified. If Daitend terminates at the end of the 2029 renewal term, Gaiport could set export fees at a level that makes transition prohibitively expensive, effectively holding Daitend's data hostage.
- **90 days may be insufficient.** For a multi-location dental group with years of imaging data (the Severna Park migration alone involved 41,906 images), 90 days of read-only access plus a paid export may not be enough to complete a migration to a new platform, particularly if the new vendor requires its own implementation timeline.
- **Format ambiguity.** The word "including" before "DICOM format for diagnostic images" is ambiguous. It could mean DICOM is one example of an acceptable format, or it could be read as the only format specifically guaranteed. If Gaiport exports clinical data in a proprietary format, Daitend may need to pay for conversion.

**Recommended fix.** Amend MSA § 13.2:

> "For up to **one hundred eighty (180)** days after expiry or termination, Provider shall continue to provide read-only access to the Platform and shall, on Customer's request, export Customer Data in the following formats: (a) diagnostic images in DICOM; (b) scheduling and billing data in CSV or a mutually agreed open format; and (c) all other Customer Data in a format reasonably requested by Customer. Provider's fees for transition assistance shall not exceed **$[X] per Clinic Location** (or such other fixed rate as the Parties agree), and shall be set forth in the applicable Statement of Work."

Setting a fixed transition fee in the SOW eliminates the "then-current rates" uncertainty.

---

## Issue 9 (Lower): Platform Update Standard Measured Against Effective Date Documentation

**Where:** MSA § 2.6.

**Description.** Gaiport may update the Platform "provided that no update materially reduces the functionality, security or availability of the Platform **as described in the Documentation at the Effective Date**." The Effective Date is January 1, 2024.

**Why it matters.** The baseline for comparing updates is frozen at January 2024. If Gaiport's Documentation has evolved since then (new modules, enhanced features, improved security), a 2027 update that removes a feature added in 2025 would not be a "material reduction" measured against the 2024 baseline. This gives Gaiport broad latitude to degrade the Platform relative to its current state, so long as it remains at or above its January 2024 level.

**Recommended fix.** Amend MSA § 2.6:

> "Provider may update the Platform from time to time, provided that no update materially reduces the functionality, security or availability of the Platform **as described in the Documentation then in effect immediately prior to the update**. Provider shall give Customer at least thirty (30) days' prior written notice of any update that removes or materially modifies a feature, and Customer may object in writing if the update would materially reduce functionality for Customer's use case."

---

## Issue 10 (Lower): Aggregated Data Rights May Be Broader Than Intended

**Where:** MSA § 5.4; DPA § 3.3.

**Description.** MSA § 5.4 permits Gaiport to "compile de-identified, aggregated statistics about use of the Platform, provided that such statistics do not identify Customer, any Clinic Location or any individual and are de-identified in accordance with 45 C.F.R. § 164.514." DPA § 3.3 permits de-identification "solely to compile the aggregated statistics permitted by Section 5.4 of the Agreement."

**Why it matters.** The de-identification standard (45 C.F.R. § 164.514) is appropriate, and the prohibition on identifying Customer or individual patients is a useful safeguard. However, the scope of "aggregated statistics about use of the Platform" is undefined. In a dental market, usage patterns (e.g., procedure mix, patient volume by geography, imaging frequency) could be commercially sensitive. If Gaiport sells or licenses these analytics to third parties (e.g., dental product manufacturers, real estate investors targeting underperforming clinics), Daitend's operational data could be exposed in aggregate form.

Additionally, because of Issue 1, it is unclear whether the de-identification requirement in § 5.4 applies to data derived from diagnostic images (which are not "Patient Data" under the DPA). The MSA's definition of "Customer Data" includes all data, so § 5.4's de-identification requirement should apply, but the interaction with the DPA's narrower scope creates uncertainty.

**Recommended fix.** Clarify MSA § 5.4:

> "Provider may compile de-identified, aggregated statistics about use of the Platform, provided that (a) such statistics do not identify Customer, any Clinic Location, any individual, or any patient; (b) such statistics are de-identified in accordance with 45 C.F.R. § 164.514; and (c) **Provider does not sell, license, or otherwise make such statistics available to any third party without Customer's prior written consent.**"

If Gaiport's business model depends on selling analytics, this may be a significant ask. A fallback would be to limit the use to "internal product improvement" and require notice to Customer before any external sharing.

---

## Ambiguities and Gaps Flagged

| # | Item | Where | Nature of Ambiguity |
|---|------|-------|--------------------|
| A1 | "Patient Data" definition conflict | MSA § 1.1 vs. DPA § 1.1 | Direct contradiction; DPA prevails per MSA § 2.3, but the practical consequence (BAA gap) may not have been intended. |
| A2 | DPA "Patient Data" limited to "scheduling and billing records" | DPA § 1.1 | Unclear whether clinical notes, treatment plans, and other PHI in the practice-management module are covered. |
| A3 | "Industry-standard, non-proprietary format (including DICOM format for diagnostic images)" | MSA § 13.2 | "Including" is ambiguous—DICOM may be the only guaranteed format or merely an example. |
| A4 | No initial Statement of Work in the file | MSA § 4.1 references it | We do not have the SOW that sets per-location, per-user, and per-module rates. The Severna Park change order references "the initial Statement of Work" rates, but we cannot verify what those rates are. |
| A5 | No DocuSign change order PDF in the file | Email Thread, Message 5 | The change order is referenced and described in the email, but the actual signed document is not in the matter folder. We cannot verify its terms beyond what Priya summarized. |
| A6 | "Severity 1" not defined in the MSA | MSA § 6.3 | The 24/7 emergency support obligation is tied to "Severity 1 issues," but the MSA does not define what constitutes Severity 1. It is presumably in the Documentation, which we do not have. |
| A7 | DPA § 5.3(b) carve-out for "unsuccessful attempts" | DPA § 5.3(b) | The list (pings, port scans, denied log-in attempts, DoS attacks) is illustrative, not exhaustive. Unclear where the line is between an "unsuccessful attempt" and a "Security Incident" that requires reporting. |
| A8 | Renewal letter signed by CRO, not General Counsel | Renewal Letter | The MSA was also signed by the CRO (Marcus Ellery). This is not a legal defect, but it raises a question about whether Gaiport's legal team reviewed the renewal pricing. The cc to General Counsel suggests awareness, but the signatory is a revenue officer. |

---

## Questions for the Client

1. **Diagnostic images / BAA gap (Issue 1):** Is Daitend aware that the DPA excludes diagnostic images from its definition of "Patient Data"? Has Daitend's compliance officer or privacy counsel flagged this? Does Daitend have any other BAAs (e.g., with imaging labs, PBM vendors) that cover diagnostic images separately?

2. **Indemnity (Issue 2):** Was the "whether or not caused" language in § 10.2 negotiated, or was it in Gaiport's standard form? Did Daitend's counsel flag it at signing?

3. **Renewal (Issue 3):** Who was responsible for tracking the non-renewal deadline (September 2 – October 2, 2026)? Does Daitend want to push back on the 15% increase before the January 2027 invoice, or accept it and focus on the next renewal cycle?

4. **Severna Park legacy server (Issue 6):** Has the legacy server been decommissioned? If so, what sanitization method was used? Is the records-retention review complete?

5. **Initial SOW (Gap A4):** Can the client provide the initial Statement of Work? We need it to verify per-location and per-user rates, Professional Services rates, and the scope of modules.

6. **Change Order (Gap A5):** Can the client provide the executed Severna Park change order (the PDF referenced in the email thread)?

7. **Documentation (Gap A6):** Can the client provide Gaiport's current Documentation (user guides, technical specifications)? We need it to understand the Severity 1 definition and the current feature set (relevant to the § 2.6 update analysis).

8. **SOC 2 report (DPA § 8.1):** Has Daitend requested and received Gaiport's most recent SOC 2 Type II report? If so, can we review it?

9. **Subcontractors (DPA § 4.3):** Has Daitend requested Gaiport's current list of subcontractors that host or have access to Patient Data? If Gaiport uses a hosting provider (e.g., AWS, Azure), we should understand the data flow.

10. **Scale:** How many Clinic Locations and Authorized Users does Daitend currently have? This affects the financial exposure analysis for Issues 2, 3, and 5.

---

## Suggested Next Steps

1. **Immediately:** Confirm status of the Severna Park legacy server (Issue 6). If it has not been securely sanitized, this is a potential unreported breach.
2. **Before January 1, 2027:** Send Gaiport a letter acknowledging the renewal but raising the DPA definition issue (Issue 1) as a material compliance concern and requesting an amendment. Frame it as a HIPAA compliance matter, not a commercial negotiation—this increases Gaiport's incentive to fix it quickly.
3. **Q1 2027:** Open a broader renegotiation covering Issues 2, 3, 4, 5, 7, 8, 9, and 10. Use the renewal as the natural inflection point. If Gaiport resists, evaluate whether the BAA gap (Issue 1) alone justifies a termination-for-material-breach analysis under MSA § 12.3 (arguably, a BAA that does not cover all PHI is a material breach of the DPA's own terms and of HIPAA).
4. **Internal:** Implement a contract-obligations calendar to track renewal notice windows, audit rights, and SOW expirations.

---

*This is a first draft. I have not independently verified the HIPAA regulatory citations beyond what appears in the documents, and I have not reviewed Gaiport's Documentation, the initial SOW, or the executed change order. My analysis of the "Patient Data" definitional conflict (Issue 1) is based on the four documents provided; if there is a side agreement or amendment not in the file, the analysis may need to be revisited.*