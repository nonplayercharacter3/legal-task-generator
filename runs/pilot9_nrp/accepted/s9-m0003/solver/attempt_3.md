# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Daitend Dental Partners / Gaiport Clinical Systems – Contract Review and Recommended Changes

---

## Summary

I have reviewed the four documents in the matter folder. The relationship is governed by a Master Services Agreement (MSA) and Data Processing Addendum (DPA), both effective January 1, 2024, with an initial 36-month term that has now auto-renewed through December 31, 2029. Gaiport's October 9, 2026 renewal letter confirms the renewal and a 15% fee increase. A change order added the Severna Park location in August 2026.

I have identified nine issues, ordered by significance. The two most critical are (1) a definitional gap that removes diagnostic images from the DPA's HIPAA protections, and (2) an unlimited customer indemnity that covers Gaiport's own negligence. Both create substantial legal and financial exposure for Daitend.

---

## Issue 1: Diagnostic Images Excluded from the DPA's Definition of "Patient Data"

**Description.** The MSA and the DPA define "Patient Data" incompatibly. The MSA (Section 1.1) defines Patient Data as "all patient health information, **including** radiographs, intraoral scans and other diagnostic images." The DPA (Section 1.1) defines Patient Data as "Protected Health Information relating to patients of Customer or its Clinic Locations that is contained in Customer's scheduling and billing records created, received, maintained or transmitted by Provider through the Platform, **excluding diagnostic images**."

Under MSA Section 2.3 (Order of Precedence), the DPA prevails over the MSA. Therefore, the operative definition is the DPA's narrower one, which carves diagnostic images out of the DPA entirely.

**Where it appears.**
- MSA § 1.1 (definition of "Patient Data" – inclusive)
- DPA § 1.1 (definition of "Patient Data" – exclusive)
- MSA § 2.3 (order of precedence giving DPA priority)

**Why it matters.** Radiographs and intraoral scans are unambiguously PHI under HIPAA (45 C.F.R. § 160.103). By excluding them from the DPA's definition of "Patient Data," the following DPA protections do not apply to the images:

- Security safeguards (DPA § 5.1–5.2): encryption, access controls, penetration testing, backup requirements
- Breach notification (DPA § 5.3–5.4): the 10-day breach reporting obligation
- Mitigation and cost reimbursement (DPA § 5.5)
- Individual rights support (DPA § 6.1–6.4)
- Return and deletion (DPA § 7.1–7.4)
- Audit rights (DPA § 8.3)
- Termination for DPA violation (DPA § 9.2)

The Platform stores these images (the MSA references DICOM format in § 13.2; the Severna Park onboarding migrated 41,906 radiographs and intraoral scans per Email Thread, Message 8). Daitend is the Covered Entity and remains legally responsible for all PHI, including images, under HIPAA. If a breach affects the images, Daitend faces regulatory exposure without the contractual protections the DPA was supposed to provide.

Additionally, the DPA serves as the parties' Business Associate Agreement (DPA Background; MSA § 1.1 definition of "DPA"). A BAA that does not cover all PHI the Business Associate creates, receives, maintains, or transmits is deficient under 45 C.F.R. § 164.504(e). This could itself be a compliance failure for Daitend as the Covered Entity.

**Recommendation.** This must be corrected before or at the start of the Renewal Term. Proposed amendment to DPA § 1.1:

> "**Patient Data**" means all Protected Health Information relating to patients of Customer or its Clinic Locations that is created, received, maintained or transmitted by Provider or any Subcontractor through the Platform, including but not limited to scheduling records, billing records, clinical notes, radiographs, intraoral scans and other diagnostic images.

This aligns the DPA's definition with the MSA's and with the scope of a valid BAA. We should also confirm with the client whether Gaiport will agree, and if not, whether Daitend should treat this as a material compliance risk requiring escalation.

**Flag:** It is unclear whether this exclusion was deliberate (perhaps Gaiport's imaging module is a separate product with its own data terms) or a drafting error. The MSA's definition, the Platform's described functionality (imaging module, DICOM support), and the onboarding emails all treat images as part of the Platform. I would not assume intent without asking the client.

---

## Issue 2: Unlimited Customer Indemnity Covers Gaiport's Own Negligence

**Description.** MSA § 10.2 requires Daitend to indemnify Gaiport for "any and all claims, demands, investigations, regulatory proceedings, fines, penalties, losses, damages, costs and expenses" arising from Customer Data, "including any enforcement action, civil money penalty or corrective action plan under HIPAA or state health privacy law, **whether or not caused or contributed to by any act or omission of Provider**."

Critically, MSA § 11.3(b) carves this indemnity out of the liability cap in § 11.1. Daitend's exposure under § 10.2 is therefore **uncapped**.

**Where it appears.**
- MSA § 10.2 (customer indemnity, "whether or not caused or contributed to by any act or omission of Provider")
- MSA § 11.3(b) (exclusion of § 10.2 amounts from the liability cap)

**Why it matters.** If Gaiport suffers a security failure—misconfigured access controls, an unpatched vulnerability, a subcontractor breach—and that failure leads to a HIPAA enforcement action or patient class action, Daitend must indemnify Gaiport for the full amount, with no cap. HIPAA civil money penalties can reach $2,134,831 per violation category per year (adjusted for inflation). A single breach affecting multiple clinic locations could easily produce eight-figure exposure.

The "whether or not caused or contributed to by Provider" language is particularly aggressive. It means Daitend bears the risk of Gaiport's own data protection failures. This is the inverse of the risk allocation one would expect: the party controlling the security (Gaiport, as Business Associate) should bear the risk of its own security failures.

**Recommendation.** Amend MSA § 10.2 to exclude claims caused or contributed to by Provider's or its Subcontractors' breach of the DPA or negligence. Proposed language:

> "Customer shall defend, indemnify and hold harmless Provider and its Affiliates, officers, directors and employees from and against any and all claims, demands, investigations, regulatory proceedings, fines, penalties, losses, damages, costs and expenses (including reasonable attorneys' fees) arising out of or relating to any Customer Data uploaded to, entered into or stored on the Platform by or on behalf of Customer, including any enforcement action, civil money penalty or corrective action plan under HIPAA or state health privacy law, **provided that Customer shall have no obligation under this Section 10.2 to the extent any such claim arises from or is contributed to by (a) Provider's or any Subcontractor's breach of the DPA, (b) Provider's negligence or willful misconduct, or (c) a security failure in the Platform for which Provider is responsible under Section 5 of the DPA** (collectively, 'Customer Data Claims')."

At a minimum, the "whether or not caused or contributed to by any act or omission of Provider" language must be struck.

---

## Issue 3: Auto-Renewal Has Locked Daitend In for 36 Months at a 15% Higher Fee

**Description.** MSA § 12.2 provides for automatic 36-month renewals unless either party gives non-renewal notice "no earlier than 120 and no later than 90 days before the current term ends." The Initial Term ended December 31, 2026. The non-renewal window therefore ran from **September 2, 2026** (120 days before) to **October 2, 2026** (90 days before). Gaiport's renewal letter is dated **October 9, 2026**—after the window closed—and confirms that no non-renewal notice was given.

The renewal increases the Platform Fee from $18,400 to $21,160 per month (a 15% increase, or $2,760/month). Over the 36-month Renewal Term (January 1, 2027 – December 31, 2029), this represents an additional $99,360 in fees compared to the prior rate.

**Where it appears.**
- MSA § 12.2 (auto-renewal and non-renewal notice window)
- MSA § 4.3 (renewal pricing at Provider's then-current rates)
- Renewal Letter § 2 (confirmation of renewal)
- Renewal Letter § 3 (fee increase to $21,160/month)

**Why it matters.** Daitend is now contractually committed through December 31, 2029. The only exit routes are:
- Termination for material breach (MSA § 12.3) – requires Gaiport to have materially breached and failed to cure
- Termination for insolvency (MSA § 12.4)
- Termination for DPA violation (DPA § 9.2) – if Gaiport violates a material DPA term and fails to cure

There is no convenience termination right. The 15% increase is justified in the letter by "infrastructure, security and imaging-storage investments" but Daitend receives no corresponding service level improvement or additional commitment (Renewal Letter § 4 states service levels and security controls "remain unchanged").

**Recommendation.**
1. **Immediate:** Confirm with the client that they are aware of the locked-in status and the financial impact. If the client was unaware, assess whether there is any argument that the notice window was not properly triggered (e.g., if Gaiport failed to give adequate advance warning of the renewal—though the MSA does not require Gaiport to remind Daitend of the window).
2. **Negotiation leverage:** Use the diagnostic image gap (Issue 1) and the indemnity problem (Issue 2) as leverage to negotiate concessions in exchange for Daitend's continued commitment. For example, seek a price hold or reduction in exchange for fixing the DPA definition.
3. **Future planning:** Calendar the next non-renewal window (for the term ending December 31, 2029, the window will be approximately September 2 – October 2, 2029). Set a reminder 6 months in advance.
4. **Contract fix for future renewals:** Propose adding a cap on renewal increases (e.g., "Fees for any Renewal Term shall not increase by more than five percent (5%) over the Fees in effect for the immediately preceding term") to MSA § 4.3.

---

## Issue 4: Gaiport May Assign to Any Successor Without Daitend's Consent

**Description.** MSA § 15.3 permits Gaiport to assign the Agreement to any "Successor" without Daitend's consent, defined in MSA § 1.1 as "any entity that acquires all or any part of the Platform business of Provider, or any of Provider's customer contracts, whether by merger, sale of stock, sale of assets or otherwise." Gaiport need only give written notice within 30 days **after** the assignment takes effect.

**Where it appears.**
- MSA § 1.1 (definition of "Successor")
- MSA § 15.1 (general consent requirement)
- MSA § 15.3 (Provider's unilateral assignment right)

**Why it matters.** Daitend is entrusting a new entity—potentially one it has never vetted—with the PHI of its patients across all clinic locations. The assignment can happen without prior notice, without consent, and without giving Daitend a termination right. The only protection is that the Successor "shall assume Provider's obligations" (§ 15.3), but:
- There is no requirement that the Successor have equivalent financial strength, security posture, or HIPAA compliance infrastructure.
- Daitend has no right to terminate upon assignment.
- The notice comes after the fact (up to 30 days later).
- The definition of "Successor" is extremely broad—"any part of the Platform business" could mean a small subsidiary or a distressed asset purchase.

For a dental group handling sensitive patient data, this is a significant continuity and compliance risk.

**Recommendation.** Amend MSA § 15.3 to require prior written consent (not to be unreasonably withheld) and to give Daitend a termination right:

> "Provider may assign this Agreement, or any Statement of Work, in whole or in part, to a Successor only with Customer's prior written consent, which consent shall not be unreasonably withheld where the Successor demonstrates (a) financial capacity equivalent to or greater than Provider's, (b) a security program that meets or exceeds the requirements of the DPA, and (c) written assumption of all of Provider's obligations under this Agreement and the DPA. If Customer withholds consent or if the proposed Successor does not meet the foregoing criteria, Customer may terminate this Agreement upon thirty (30) days' written notice without penalty and receive a refund of prepaid Fees for the unused portion."

---

## Issue 5: Transition Assistance Is Limited, Paid, and May Be Insufficient

**Description.** MSA § 13.2 provides only 90 days of read-only access post-termination, and data export is at "Provider's then-current Professional Services rates." For a multi-location dental group with years of accumulated records (Severna Park alone has ~9 years of data per Email Thread, Message 1), 90 days of read-only access may be insufficient to migrate to a replacement platform, and paying Gaiport's rates to retrieve one's own data creates a hold-up risk.

**Where it appears.**
- MSA § 13.2 (transition assistance, 90-day read-only, export at Provider's rates)
- DPA § 7.1 (return in industry-standard format)
- DPA § 7.2 (deletion within 30 days after transition period)

**Why it matters.** If the relationship ends (for cause, by operation of DPA § 9.2, or at the end of the Renewal Term), Daitend needs to extract all patient data—including 40,000+ images per location—without losing access to active patient care. Ninety days of read-only access means no new entries, no scheduling, no billing. For a group that has already demonstrated growth (Severna Park acquisition), this window may be too short. The requirement to pay for export adds cost and gives Gaiport leverage.

**Recommendation.** Amend MSA § 13.2:

> "For up to one hundred eighty (180) days after expiry or termination, Provider shall continue to provide read-only access to the Platform and shall, on Customer's request, export Customer Data in an industry-standard, non-proprietary format (including DICOM format for diagnostic images) **at no charge to Customer**. If Customer requires transition assistance beyond the export (including data mapping, format conversion or loading into a replacement system), Provider shall provide such assistance at Provider's then-current Professional Services rates, not to exceed $[X] per hour."

---

## Issue 6: Liability Cap Is Inadequate Relative to Data Risk

**Description.** MSA § 11.1 caps each party's aggregate liability at "the fees paid by Customer in the 12 months preceding the claim." At the renewed rate of $21,160/month, this cap is approximately $253,920 (plus any per-location charges). However, a single HIPAA breach at a multi-location dental group could generate notification costs, credit monitoring, regulatory penalties, and patient litigation well in excess of this amount.

**Where it appears.**
- MSA § 11.1 (12-month fee cap)
- MSA § 11.2 (exclusion of indirect damages)
- MSA § 11.3 (carve-outs: payment obligations, § 10.2 indemnity, fraud/willful misconduct)

**Why it matters.** If Gaiport's security failure causes a breach affecting Daitend's patients, Daitend's recovery from Gaiport is capped at ~$254,000, while Daitend's own exposure to patients and regulators is uncapped. The § 11.2 exclusion of indirect damages further limits recovery (e.g., lost revenue from clinic closures during a breach response would likely be characterized as consequential).

**Recommendation.** Add a super-cap for data protection failures:

> "Notwithstanding Section 11.1, Provider's aggregate liability for claims arising from a Breach of Unsecured PHI or a Security Incident caused by Provider's or a Subcontractor's failure to comply with Section 5 of the DPA shall not exceed $[5,000,000] (the 'Data Protection Cap'). The Data Protection Cap is in addition to, and not limited by, the cap in Section 11.1."

This should be negotiated in tandem with fixing Issue 2 (the indemnity), so the overall risk allocation is coherent.

---

## Issue 7: Service Credits Are the Exclusive Remedy for Availability Failures

**Description.** MSA § 6.2 provides service credits of 5% of the monthly Platform Fee for each 0.5% availability shortfall, capped at 25% of the monthly fee. There is no stated right to terminate for chronic service level failures.

**Where it appears.**
- MSA § 6.1 (99.5% monthly availability)
- MSA § 6.2 (service credits, 25% cap)

**Why it matters.** A dental clinic cannot see patients if the scheduling and billing platform is down. The maximum credit is 25% of $21,160 = $5,290/month. If Gaiport chronically misses the availability target (e.g., 99.0% every month for a year), Daitend's total recovery is ~$63,480—hardly compensating for lost patient revenue and operational disruption. There is no "three consecutive months" or "six months in a 12-month period" termination trigger.

**Recommendation.** Add a chronic failure termination right to MSA § 6.2:

> "If Provider fails to meet the availability commitment in Section 6.1 for three (3) consecutive calendar months, or for five (5) or more calendar months in any rolling twelve-month period, Customer may terminate this Agreement or the affected Statement of Work upon thirty (30) days' written notice, without penalty and with a refund of prepaid Fees for the unused portion."

---

## Issue 8: Legacy Data Decommissioning Lacks a Contractual Protocol

**Description.** The Severna Park onboarding involved migrating ~9 years of patient records from a locally hosted legacy server (Email Thread, Messages 1 and 3). Priya's go-live email (Message 10) states: "The legacy server can be decommissioned once Daitend's records-retention review is complete." No contractual provision governs the secure destruction of the legacy system or the data it contains.

**Where it appears.**
- Email Thread, Message 1 (description of legacy system: "locally hosted server with a desktop practice-management package and a separate imaging bridge. Roughly 9 years of patient records and radiographs.")
- Email Thread, Message 10 (decommissioning contingent on "records-retention review")
- No corresponding MSA or DPA provision addresses legacy data held by Customer

**Why it matters.** While the legacy server is Daitend's own infrastructure (not Gaiport's), the absence of a documented, compliant decommissioning protocol creates risk. If the legacy server is simply wiped or discarded without following NIST SP 800-88 or equivalent, the residual data could be recovered, creating a breach that Daitend would be responsible for reporting under HIPAA. The DPA's deletion standard (NIST SP 800-88, DPA § 7.2) applies only to data held by Provider, not to Customer's own legacy systems.

**Recommendation.** This is primarily an operational matter for Daitend, but we should:
1. Advise the client to document the decommissioning of the legacy server using NIST SP 800-88 methods (clear, purge, or destroy as appropriate for the media type).
2. Recommend that the client obtain written certification of destruction from whoever performs the decommissioning.
3. Confirm the client's records retention schedule (Maryland and federal requirements for dental records—typically 7 years for adults, until age of majority + 7 for minors).
4. Flag that the 41,906 images now in Gaiport's Platform are subject to the DPA's deletion provisions only upon termination; there is no obligation on Gaiport to delete the legacy copies (which are Daitend's responsibility).

---

## Issue 9: Ambiguities and Missing Items

**9a. The initial Statement of Work is not in the file.** The MSA references rates "set out in the applicable Statement of Work" (MSA § 4.1, § 4.2), and the Severna Park change order incorporates "the per-location, Authorized User and module rates in the initial Statement of Work" (Email Thread, Message 2). Without the initial SOW, I cannot verify what the per-location rate is, whether the Severna Park charges are consistent, or what the total monthly commitment actually is (the $18,400/$21,160 Platform Fee covers only the "Clinic Locations in the initial Statement of Work" per MSA § 4.1; additional locations are charged separately).

**9b. The executed Severna Park change order is referenced but not in the file.** Email Thread, Message 5 references an attached PDF ("Gaiport_Daitend_Change_Order_SevernaPark.pdf"). I have not reviewed the actual change order language.

**9c. The DPA's "Patient Data" definition references "scheduling and billing records" specifically.** DPA § 1.1 limits Patient Data to PHI "contained in Customer's scheduling and billing records." Clinical notes, treatment plans, and other clinical documentation that may be entered into the Platform are not clearly captured by this language, even setting aside the diagnostic image exclusion. This is a second, independent gap in the DPA's scope.

**9d. No SLA for data migration or Professional Services.** The MSA warrants that Professional Services will be performed "in a professional and workmanlike manner" (MSA § 9.2(b)), but there are no deadlines, milestones, or remedies specific to implementation services. The Severna Park timeline (Email Thread, Message 2) was set by email, not by contract.

**9e. The renewal letter states that the DPA continues "on their existing terms" (Renewal Letter § 2).** This means the diagnostic image gap (Issue 1) carries forward for the entire Renewal Term unless affirmatively fixed.

---

## Questions for the Client

1. **Diagnostic images:** Is Daitend aware that the DPA's definition of "Patient Data" excludes diagnostic images? Has any internal compliance or privacy officer flagged this? Are there any existing side letters, emails, or representations from Gaiport that the images are covered by the BAA?

2. **Renewal awareness:** Was the non-renewal window (September 2 – October 2, 2026) discussed internally? Was the decision to renew deliberate, or was the window missed? Is the 15% price increase acceptable, or does the client want to negotiate?

3. **Initial SOW:** Can the client provide the initial Statement of Work (executed January 2024) and the Severna Park change order (executed August 2026)? I need to verify the per-location rates and confirm the total monthly commitment.

4. **Legacy server:** What is Daitend's records retention schedule for the Severna Park legacy data? Has the decommissioning been performed yet? If so, by whom and using what method?

5. **Growth plans:** Does Daitend anticipate additional acquisitions or new locations in the next 12–24 months? This affects the financial modeling of the locked-in renewal and the urgency of negotiating better terms.

6. **Incident history:** Has Daitend experienced any security incidents, near-misses, or patient data complaints related to the Gaiport Platform since go-live? This affects risk assessment and negotiation posture.

7. **Insurance:** Does Daitend carry its own cyber liability or privacy insurance? If so, what are the limits and does the policy address the gap created by the DPA's exclusion of diagnostic images?

---

## Suggested Next Steps

1. **Urgent:** Draft a letter to Gaiport raising the DPA definition issue (Issue 1) as a compliance matter, requesting an amendment before the Renewal Term begins January 1, 2027. Frame it as a mutual interest (Gaiport also wants a valid BAA).
2. **High priority:** Prepare a redline of the MSA addressing Issues 2, 4, 5, 6, and 7 for use in the "account review" Gaiport has proposed (Renewal Letter § 5).
3. **Client follow-up:** Send the questions above to Renata Okonkwo-Hale and Daniel Reyes-Whitford. Request the initial SOW and the executed Severna Park change order.
4. **Calendar:** Set a reminder for Q2 2029 to begin planning for the next renewal/non-renewal decision (window opens ~September 2029).