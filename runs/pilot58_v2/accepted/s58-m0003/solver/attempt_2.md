# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Traimand Seed Genetics, Inc. – Figos Analytics Software License: Issue Identification and Recommended Fixes

---

## Summary

I have reviewed all six documents in the matter folder. I identify **eleven issues** ranging from critical to moderate. The three most consequential are: (1) the Order Form's narrowing of data-security liability to willful disclosure only, (2) the apparently late non-renewal notice that Figos is disputing, and (3) the unaddressed Change of Control consent requirement triggered by the Kestrel merger. Each is detailed below with the specific document and section, the risk to Traimand, and a recommended fix.

---

## Issue 1 – Data-Security Liability Capped for All But Willful Disclosure

**Where:** Order Form No. OF-001, Special Terms §4; read with License Agreement §11.3(b) and §1.3 (Order of Precedence).

**What it says:** License Agreement §11.3(b) carves "Licensor's breach of Section 9 (Data Security and Confidentiality)" out of the liability cap in §11.1, meaning data-security breaches would ordinarily be uncapped. However, Special Terms §4 of the Order Form provides:

> "Section 11.3(b) shall apply only to Licensor's willful disclosure of Customer Data in breach of Section 9. All other breaches of Section 9 by Licensor are subject to the cap in Section 11.1."

Because the Order Form controls over the License Agreement (§1.3), this Special Term prevails. The practical effect is that any negligent or even grossly negligent data-security failure—e.g., a ransomware attack resulting from inadequate patching, a subcontractor breach, failure to maintain encryption—exposes Traimand to a maximum recovery of 12 months of fees (approximately $493,000 based on Year 3 pricing).

**Why it matters:** Traimand's Customer Data includes 15 years of genotypic, phenotypic, pedigree, and germplasm data, plus all Derived Data (GEBVs, relationship matrices, trained models). This data is the core intellectual property of a breeding program. A single significant breach could cause irreparable competitive harm (e.g., disclosure of proprietary GEBVs to a competitor) far exceeding $493,000. The cap effectively transfers the economic risk of Figos's security failures to Traimand.

**Recommended fix:** Negotiate deletion of Special Terms §4 or, at minimum, expand the uncapped category to include (a) any breach of Section 9 caused by Licensor's gross negligence, and (b) any breach resulting in unauthorized access to or disclosure of Customer Data to a third party, regardless of fault. If Figos resists, seek a super-cap (e.g., 3× annual fees) for data-security breaches rather than the general 1× cap.

---

## Issue 2 – Non-Renewal Notice Appears 12 Days Late; Figos Disputes Effectiveness

**Where:** SOW No. 02, §8.1; License Agreement §12.2; Order Form OF-001, §§2.2–2.4.

**What it says:** The Initial Subscription Term is 36 months from February 1, 2024, ending **January 31, 2027**. Section 12.2 requires written notice of non-renewal "at least one hundred twenty (120) days before the end of the then-current term." Counting back 120 days from January 31, 2027 yields a deadline of approximately **October 2 or 3, 2026**. SOW §8.1 states that Traimand delivered its non-renewal notice on **October 14, 2026**—12 to 14 days after the deadline. Figos has disputed the notice's effectiveness in writing.

**Why it matters:** If the notice is ineffective, the Order Form auto-renews for a **24-month** Renewal Term (OF-001 §2.3) beginning February 1, 2027, at "Licensor's then-current list pricing" (§2.4)—an uncapped price increase. Traimand would be locked in through January 31, 2029, during and after the Kestrel integration, with no contractual right to exit. Given that Traimand has already commissioned a full data-migration and transition SOW (SOW 02), the commercial intent to exit is clear, but the legal position is uncertain.

**Recommended fix:**
- **Immediate:** Send a cure or clarification letter arguing that (a) the 120-day period should be measured from the last day of the term (i.e., notice by October 3, 2026 is sufficient, making October 14 only 11 days late), and (b) Figos's contemporaneous performance of SOW 02 (signed October 28, 2026, with §8.3 requiring performance "regardless of the resolution") constitutes a waiver or estoppel against strict enforcement of the notice deadline.
- **Strategic:** If the notice is held ineffective, negotiate a mutual release from the Renewal Term in exchange for Traimand's payment of a breakage fee (e.g., 50% of the first 12 months of renewal fees). This is preferable to being locked in for 24 months at list pricing while also dealing with the CoC issue (Issue 3).
- **Going forward:** Implement a contract-management calendar with 180-day alerts for all auto-renewal notice deadlines.

---

## Issue 3 – Change of Control (Kestrel Merger) Requires Figos Consent; None Evidenced

**Where:** License Agreement §14.2; SOW No. 02, Recital C.

**What it says:** Section 14.2 provides: "A Change of Control of Customer is deemed an assignment for purposes of this Section 14.2 and requires Licensor's prior written consent. If a Change of Control of Customer occurs without Licensor's prior written consent, Licensor may terminate this Agreement by giving Customer thirty (30) days' written notice." SOW Recital C confirms that on September 22, 2026, Traimand entered into an Agreement and Plan of Merger with Kestrel Row Crop Holdings, Inc., under which Traimand will become a wholly owned subsidiary of Kestrel. No document in the folder evidences that Figos has consented to this Change of Control.

**Why it matters:** If the Kestrel merger closes before the Subscription Term ends (January 31, 2027, or later if the non-renewal notice is ineffective), Figos has the right to terminate the entire Agreement on 30 days' notice. The financial consequences of such a termination are ambiguous: §12.4 expressly addresses termination "under Section 12.3" (for cause) but is silent on termination under §14.2. Figos could argue that all prepaid fees are non-refundable and that Traimand owes any unpaid fees for the remainder of the term. Even if that argument fails, a §14.2 termination would disrupt the SOW 02 transition services at the worst possible time—mid-integration with Kestrel.

Additionally, if Figos is acquired by a competitor of Kestrel (permitted without consent under §14.3), Traimand's data and GEBVs could end up in the hands of a strategic rival, with no contractual remedy.

**Recommended fix:**
- **Immediate:** Request written consent from Figos to the Kestrel Change of Control as a condition of closing. Frame it as a mutual benefit: Figos retains a paying customer (now backed by Kestrel's balance sheet) and avoids the administrative burden of a termination and data migration it is already performing under SOW 02.
- **If consent is withheld or conditioned:** Negotiate a side letter specifying that (a) a §14.2 termination will not trigger payment of remaining-term fees (i.e., Traimand pays only for services rendered through the termination date), (b) the 60-day data-export period in §12.4 applies, and (c) SOW 02 continues to completion regardless.
- **Regarding §14.3 (Licensor assignment):** Seek to add a requirement that any assignment by Figos to a competitor of Customer or Customer's Affiliates triggers Customer's right to terminate without penalty.

---

## Issue 4 – Conflicting Definitions of "Customer Data" Create a Protection Gap for Derived Data

**Where:** License Agreement §1.1 (definition of "Customer Data"); Quality Agreement §2.1 (definition of "Customer Data"); License Agreement §1.3 (Order of Precedence).

**What it says:** The License Agreement defines Customer Data broadly to include "all Derived Data generated from it by the Platform," expressly listing GEBVs, marker-effect estimates, genomic relationship matrices, prediction accuracies, and trained models. The Quality Agreement, however, redefines Customer Data narrowly as "the raw data files uploaded by Customer to the Platform, including genotype call files, marker panels, phenotypic trial records, pedigree files and associated metadata, **in the form in which Customer or its Authorized Users upload them**."

Under §1.3, the Quality Agreement controls for "quality and data-handling matters." The Quality Agreement's core obligations—segregation (§4.2), permitted use (§5.1), no-training-for-other-customers (§5.2), retention and deletion (§§5.4–5.6), and deletion certification (§5.7)—all reference "Customer Data" as defined in §2.1. Read literally, these obligations do not extend to Derived Data.

**Why it matters:** Derived Data (GEBVs, relationship matrices, calibrated models) is arguably the most sensitive and valuable output. If Figos's obligation not to use Customer Data to train models for other customers (§5.2) applies only to raw uploaded files, Figos could potentially use Traimand's GEBVs and relationship matrices to improve its platform for other seed companies. Similarly, the deletion certification requirement (§5.7) would not cover Derived Data, leaving Traimand without a contractual assurance that its GEBVs are destroyed post-termination.

**Recommended fix:** Amend Quality Agreement §2.1 to conform to the License Agreement's broader definition, or add an express sentence: "For purposes of this Quality Agreement, 'Customer Data' has the meaning given in Section 1.1 of the License Agreement, including all Derived Data." If Figos resists, at minimum add a sentence to §5.2: "The restrictions in this Section 5.2 apply equally to all Derived Data."

---

## Issue 5 – Uncapped Customer Indemnity for 15 Years of Legacy Trial Data

**Where:** SOW No. 02, §7.1; License Agreement §11.3(a).

**What it says:** SOW §7.1 requires Traimand to indemnify Figos against any third-party claim "arising from the Legacy Trial Data or from Licensor's receipt, processing, loading or transfer of the Legacy Trial Data in accordance with this Statement of Work." The indemnity expressly covers claims that the data "was collected, used or transferred in breach of grower agreements, cooperator trial agreements, third-party germplasm licenses, material transfer agreements or other obligations owed by Customer to any third party." Because §11.3(a) excludes indemnification obligations from the liability cap, this indemnity is **uncapped**.

The Legacy Trial Data spans **2009 through 2023** (15 years) and includes data from cooperator sites operated by growers and data relating to in-licensed germplasm (SOW §1, definition of "Legacy Trial Data"; Exhibit A).

**Why it matters:** Traimand is assuming unlimited financial exposure for the provenance of 15 years of trial data, much of which was collected under grower and cooperator agreements that may be difficult to locate or verify after a decade or more. A single grower or germplasm licensor could bring a claim (e.g., alleging that phenotypic data was shared without authorization, or that in-licensed germplasm data was used beyond the scope of the license) and Traimand would bear the full cost of defense and any judgment. The risk is heightened by the Kestrel integration, which may involve combining Traimand's data with Kestrel's, potentially triggering additional third-party claims.

**Recommended fix:**
- Negotiate a cap on the SOW §7 indemnity (e.g., limited to the SOW Fees of $186,500, or a multiple thereof).
- Narrow the scope: limit the indemnity to claims arising from Traimand's **knowing** breach of a third-party agreement, and exclude claims that could have been discovered through reasonable pre-migration diligence.
- Add a time limitation: the indemnity should not extend to claims arising from data collected more than X years before the SOW Effective Date, or should require Traimand to have had actual notice of the underlying agreement.
- Require Figos to give Traimand the opportunity to settle or control the defense of any claim that implicates Traimand's relationships with growers or germplasm licensors (currently §7.3 incorporates License Agreement §10.4, which gives the indemnifying party—Traimand—sole control, which is acceptable, but confirm this in practice).

---

## Issue 6 – Technology E&O / Cyber Insurance Is Claims-Made with No Evidenced Tail

**Where:** Certificate of Insurance (2026), §5.3; License Agreement §13.1.

**What it says:** The $5,000,000 Technology E&O / Network Security and Privacy Liability policy is written on a **claims-made** form with a policy period of **February 1, 2026 – February 1, 2027** and a retroactive date of January 1, 2019. No extended reporting period (tail) or successor-policy commitment is evidenced in the certificate.

**Why it matters:** Under a claims-made policy, coverage is triggered only if a claim is **made** (not merely if the wrongful act occurs) during the policy period. If a data breach occurs in December 2026 but is not discovered or reported until March 2027 (after the policy expires), Figos's insurer has no obligation to respond—unless Figos has purchased a tail or the new policy picks up the prior retroactive date. Combined with Issue 1 (data-security liability capped at ~$493K for non-willful breaches), Traimand faces a scenario where: (a) a negligent breach causes significant harm, (b) Traimand's contractual recovery is capped at $493K, and (c) Figos's insurance does not respond because the claim was made after the policy period. Traimand would bear the loss.

Additionally, License Agreement §13.1 requires Figos to maintain insurance "during the term of this Agreement, and for one (1) year after it ends." If the Subscription Term ends January 31, 2027, insurance must be in place through January 31, 2028. The current certificate only evidences coverage through February 1, 2027—a gap of approximately one year.

**Recommended fix:**
- Require Figos to provide evidence of (a) a renewal policy for the period February 1, 2027 – January 31, 2028 (or later, if the term is extended), with the same or better limits and the same or earlier retroactive date, or (b) a 12-month extended reporting period (tail) on the current policy.
- Add a contractual requirement that the claims-made policy include a minimum 12-month extended reporting period upon non-renewal or cancellation, at Figos's expense.
- Make continued compliance with §13.1 a condition precedent to Figos's right to invoke the liability cap in §11.1 (i.e., if Figos is not properly insured, the cap does not apply).

---

## Issue 7 – Renewal Fees at Uncapped "Then-Current List Pricing"

**Where:** Order Form OF-001, §2.4.

**What it says:** "Subscription Fees for each Renewal Term are charged at Licensor's then-current list pricing for the Platform Modules and user seats subscribed at the time of renewal."

**Why it matters:** If the non-renewal notice is held ineffective (Issue 2), Traimand enters a 24-month Renewal Term at a price it cannot predict. "List pricing" is not defined in any document in the folder and could reflect any increase Figos implements in the intervening period. For a company in the middle of a merger integration with fixed budget commitments to Kestrel, an unpredictable fee increase is a material financial risk.

**Recommended fix:** Negotiate a price-protection provision: renewal fees shall not exceed the prior year's fee by more than a stated percentage (e.g., CPI + 2%) or a fixed cap (e.g., 5% per year). Alternatively, if the non-renewal dispute is resolved in Figos's favor, negotiate a fixed renewal price as part of the settlement.

---

## Issue 8 – One-Sided Assignment Rights

**Where:** License Agreement §§14.2 and 14.3.

**What it says:** Customer may not assign without Licensor's consent, and a Change of Control is deemed an assignment (§14.2). Licensor may assign "in whole or in part, without Customer's consent to any Affiliate or any successor or acquirer of all or part of its business or assets to which this Agreement relates" (§14.3), with only 30 days' post-hoc notice.

**Why it matters:** The asymmetry means that if Figos is acquired by—or sells its genomic selection business to—a direct competitor of Traimand or Kestrel, Traimand has no right to object, terminate, or renegotiate. Its proprietary breeding data and GEBVs would transfer to the acquirer's control (subject to the confidentiality and data-use restrictions, but those are only as strong as the acquirer's compliance). In the seed industry, where a handful of large firms dominate, this is a realistic scenario.

**Recommended fix:** Amend §14.3 to provide that Customer may terminate the Agreement without penalty if Licensor assigns to (a) a direct competitor of Customer or its Affiliates, or (b) an entity that is subject to conflicting obligations under a competing platform license. Alternatively, require Customer's prior written consent for any assignment by Licensor (matching the standard in §14.2).

---

## Issue 9 – Deemed Acceptance Triggered by Operational Use

**Where:** SOW No. 02, §5.3.

**What it says:** "A Deliverable is deemed accepted if Customer does not notify Licensor of a material nonconformity within the review period, **or if Customer uses the Deliverable in its Production Environment for operational selection decisions**."

**Why it matters:** The second prong creates an inadvertent-acceptance risk. If a data engineer loads a migrated dataset into the Production Environment for a routine GEBV run before the formal 10-business-day review period expires, the deliverable is deemed accepted and Traimand loses the right to reject it for nonconformity. In a breeding operation with 40 authorized users, the risk of someone using migrated data operationally before formal sign-off is non-trivial.

**Recommended fix:** Delete the second prong of §5.3, or limit it to use by the designated project lead (Dr. Ostrander) with documented intent to accept. At minimum, add: "Deemed acceptance under this second prong shall not apply if Customer notifies Licensor of a material nonconformity within five (5) business days after the use."

---

## Issue 10 – Validation Report Acceptance Deadline Precedes Circulation of Meeting Minutes

**Where:** Meeting Notes (August 19, 2026), §§5.1, 5.5; Quality Agreement §7.3.

**What it says:** Validation Report VR-2026-03 was delivered to Dr. Ostrander on August 12, 2026. Quality Agreement §7.3 requires Customer to accept or reject within 10 business days, i.e., by **August 26, 2026**. The quarterly review meeting at which the results were discussed took place on **August 19, 2026** (business day 5 of the 10-day window). The minutes were not circulated until **August 28, 2026**—two days after the acceptance deadline.

**Why it matters:** While Dr. Ostrander had access to the Validation Report and the presentation at the meeting, the formal written record (minutes with the results table, the confirmation of no protocol deviations, and the discussion of the MAF threshold impact) was not available until after the deadline. If a dispute later arises about what was presented or agreed at the meeting, Traimand would be relying on its own recollection rather than the circulated minutes. More practically, if Traimand's internal approval process required the minutes (e.g., for a multi-person sign-off), the deadline was effectively impossible to meet.

**Recommended fix:** This is a one-time procedural issue, but going forward: (a) request that Figos circulate draft minutes within 48 hours of the meeting (rather than the 10 business days permitted by QA §3.2) when a validation acceptance deadline falls within the same window; or (b) negotiate to extend the acceptance period in QA §7.3 to 15 business days to accommodate the quarterly review cycle.

---

## Issue 11 – Insurance Certificate Does Not Evidence Post-Term Coverage

**Where:** Certificate of Insurance (2026), §5 (all coverages); License Agreement §13.1.

**What it says:** All policies shown on the certificate have a policy period of **February 1, 2026 – February 1, 2027**. License Agreement §13.1 requires Figos to maintain the specified insurance "during the term of this Agreement, and for **one (1) year after it ends**."

**Why it matters:** If the Subscription Term ends January 31, 2027 (assuming the non-renewal notice is effective), Figos must maintain insurance through at least **January 31, 2028**. The certificate evidences coverage only through February 1, 2027—essentially no post-term coverage. If the non-renewal notice is ineffective and the term extends to January 31, 2029, the gap is even larger. In either scenario, Traimand has no assurance that Figos will be insured for claims arising in the post-termination period (e.g., a data breach discovered 6 months after termination).

**Recommended fix:** Require Figos to deliver a certificate (or binder) evidencing insurance coverage for the full post-term period before the Subscription Term ends. Make this a condition of Traimand's obligation to pay any post-termination amounts. If Figos cannot or will not provide post-term coverage, negotiate a reduction in the data-security liability cap (Issue 1) to reflect the increased risk Traimand is bearing.

---

## Cross-Cutting Observation: Interaction of Issues 2, 3, and 6

The three critical issues are interrelated and should be addressed as a package:

- If the non-renewal notice is **effective**, the term ends January 31, 2027. The Kestrel merger may close before or after that date. If before, Figos can terminate under §14.2 (but the term is ending anyway, so the practical impact is limited to the 60-day export window and any SOW 02 completion). If after, the relationship has ended and the CoC is moot.
- If the non-renewal notice is **ineffective**, the term renews to January 31, 2029. The Kestrel merger will almost certainly close during the renewed term, giving Figos a §14.2 termination right at a time of Traimand's choosing (or not). Traimand would be paying list-price fees for 24 months while also potentially facing a Figos termination.
- In both scenarios, the claims-made insurance gap (Issue 6/11) means that if a data breach occurs near or after the term end, Traimand's recovery is limited by both the contractual cap (Issue 1) and the absence of insurance.

**Recommended approach:** Engage Figos in a single negotiation addressing all three issues simultaneously: (a) confirm the non-renewal (or settle the dispute with a breakage fee), (b) obtain CoC consent (or a side letter limiting the consequences of a §14.2 termination), and (c) secure evidence of post-term insurance. Leverage SOW 02 (which Figos is already performing) as the natural forum: Figos has a financial interest in completing the migration and being paid $186,500, which gives Traimand negotiating capital.

---

## Table of Issues at a Glance

| # | Issue | Document / Section | Severity |
|---|-------|-------------------|----------|
| 1 | Data-security liability capped for non-willful breaches | OF-001, Special Terms §4; LA §11.3(b), §1.3 | **Critical** |
| 2 | Non-renewal notice 12+ days late; disputed | SOW 02 §8.1; LA §12.2; OF-001 §2.3–2.4 | **Critical** |
| 3 | CoC (Kestrel) consent not obtained | LA §14.2; SOW 02 Recital C | **Critical** |
| 4 | Derived Data excluded from QA protections | LA §1.1; QA §2.1; LA §1.3 | High |
| 5 | Uncapped indemnity for 15 yrs of legacy data | SOW 02 §7.1; LA §11.3(a) | High |
| 6 | Claims-made cyber policy; no tail evidenced | COI §5.3; LA §13.1 | Moderate |
| 7 | Renewal fees at uncapped list pricing | OF-001 §2.4 | Moderate |
| 8 | One-sided assignment (Licensor free to assign) | LA §§14.2–14.3 | Moderate |
| 9 | Deemed acceptance by operational use | SOW 02 §5.3 | Low–Moderate |
| 10 | Minutes circulated after acceptance deadline | Meeting Notes §§5.1, 5.5; QA §7.3 | Low |
| 11 | No post-term insurance evidenced | COI §5; LA §13.1 | Moderate |