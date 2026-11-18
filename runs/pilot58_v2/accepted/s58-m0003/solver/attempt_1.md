# MEMORANDUM

**TO:** Partner
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Traimand Seed Genetics, Inc. – Figos Analytics, LLC Software License: Issue Identification and Recommended Fixes

---

## Summary

I have reviewed all six documents in the matter folder. I identify **fourteen issues** ranging from critical to moderate. The three most urgent are: (1) Traimand's non-renewal notice was delivered 11 days late, likely triggering an involuntary 24-month renewal; (2) the pending Kestrel merger constitutes a Change of Control requiring Figos's consent, which has not been sought; and (3) a Special Term in the Order Form narrows the uncapped data-security liability to willful disclosure only, leaving negligent breaches subject to a ~$493,000 cap.

---

## Issue 1: Non-Renewal Notice Delivered Late – Involuntary 24-Month Renewal

**Where:** SOW 02, § 8.1; SLA § 12.2; OF-001 § 2.3

**Facts:** The Initial Subscription Term is 36 months from February 1, 2024, expiring January 31, 2027 (OF-001 § 2.2). SLA § 12.2 requires written non-renewal notice "at least one hundred twenty (120) days before the end of the then-current term." Counting back 120 days from January 31, 2027 yields **October 3, 2026**. Traimand delivered its notice on **October 14, 2026** (SOW 02 § 8.1) — 11 days after the deadline. Figos has disputed the notice's effectiveness (SOW 02 § 8.1).

**Why it matters:** If the notice is ineffective, OF-001 auto-renews for a 24-month Renewal Term beginning February 1, 2027, at "Licensor's then-current list pricing" (OF-001 § 2.4). Traimand is in the middle of a planned exit (SOW 02 is a transition/migration SOW) and would be locked in for two more years at potentially higher prices. The SOW 02 recitals make clear that Traimand intends to integrate its informatics operations with Kestrel post-closing and does not plan to continue on the Figos Platform.

**Recommended fix:**
- Immediately send a supplemental non-renewal notice and request that Figos accept it as effective, arguing that the 11-day delay was immaterial and that Figos's own conduct (executing SOW 02, a transition SOW, on October 28, 2026) constitutes a waiver of strict compliance with the 120-day deadline.
- In the alternative, negotiate a mutual termination of OF-001 effective at the end of the Initial Subscription Term (January 31, 2027) as part of a global resolution that also addresses the Change of Control consent (Issue 2) and the transition deliverables.
- If Figos refuses, assess whether the 120-day requirement is a condition precedent or a material term; under New York law (SLA § 15.1), a party's failure to comply with a time provision may be excused if the other party waived it or if strict enforcement would be unconscionable. Figos's execution of SOW 02 after receiving the late notice is strong evidence of waiver.

---

## Issue 2: Pending Kestrel Merger Triggers Change of Control Consent Requirement

**Where:** SLA §§ 1.1 (definition of "Change of Control"), 14.2; SOW 02, Recital C

**Facts:** SLA § 14.2 provides that "A Change of Control of Customer is deemed an assignment" requiring "Licensor's prior written consent." The defined term "Change of Control" includes "the acquisition by any person or group of more than fifty percent (50%) of the Party's voting interests" (SLA § 1.1). SOW 02 Recital C confirms that on September 22, 2026, Traimand entered into an Agreement and Plan of Merger with Kestrel Row Crop Holdings under which Traimand "will become a wholly owned subsidiary of Kestrel." No consent from Figos has been requested or given.

**Why it matters:** When the Kestrel merger closes, a Change of Control will occur. Without Figos's prior written consent, Figos may terminate the entire Agreement on 30 days' notice (SLA § 14.2). This creates several risks:
- If Figos terminates, the SLA § 12.4 fee provisions are ambiguous: they specify that "If Licensor terminates under Section 12.3, Customer shall pay all unpaid Fees for the remainder of the then-current Subscription Term," but § 14.2 is a separate termination right not referenced in § 12.4. Figos could argue Traimand still owes fees for the balance of the term.
- Termination would disrupt the SOW 02 transition, potentially leaving Traimand without the Transition Package it needs for the Kestrel integration.
- Figos could leverage the consent requirement to extract additional fees or concessions.

**Recommended fix:**
- Request Figos's written consent to the Change of Control immediately, well before the merger closes. Frame it as a condition to the global resolution of the non-renewal dispute (Issue 1).
- Negotiate that consent be conditioned only on (a) Traimand's assumption of all existing obligations and (b) Kestrel's acknowledgment of the Agreement, rather than on any payment premium.
- If Figos withholds consent, confirm that the SOW 02 services (including the Transition Package) will be completed regardless (SOW 02 § 8.3 so provides), and document that Traimand has done everything in its power to obtain consent.
- Consider whether the merger agreement with Kestrel contains any provisions regarding notification to or consent from software vendors; if so, ensure consistency.

---

## Issue 3: Special Term 4 Narrows Uncapped Data-Security Liability to Willful Disclosure Only

**Where:** OF-001, Special Terms § 4; SLA §§ 11.1, 11.3(b)

**Facts:** SLA § 11.3(b) excludes "Licensor's breach of Section 9 (Data Security and Confidentiality)" from both the liability cap (§ 11.1) and the consequential-damages exclusion (§ 11.2). However, OF-001 Special Term 4 provides: "Section 11.3(b) shall apply only to Licensor's **willful disclosure** of Customer Data in breach of Section 9. All other breaches of Section 9 by Licensor are subject to the cap in Section 11.1." Under SLA § 1.3, the Order Form controls over the License Agreement in the event of conflict.

**Why it matters:** Traimand's Customer Data includes genotypic, phenotypic, pedigree, trial, environmental, and germplasm data (SLA § 1.1) — the core intellectual property of a seed genetics company. If Figos suffers a negligent Security Incident (e.g., a ransomware attack, misconfigured access controls, or a subcontractor breach), Traimand's recovery is capped at 12 months of fees (~$493,320 based on Year 3 pricing in OF-001 § 4.1). The actual harm to Traimand from a germplasm data leak could be orders of magnitude greater (loss of proprietary breeding lines, competitive disadvantage, obligations to cooperator growers and germplasm licensors). Only a *willful* disclosure by Figos triggers uncapped liability.

**Recommended fix:**
- Negotiate to delete or amend Special Term 4 to restore the full SLA § 11.3(b) carve-out for all Section 9 breaches, or at minimum to include "gross negligence" and "failure to maintain the security program required by Section 9.1" as uncapped events.
- If Figos resists, seek a super-cap for data-security breaches (e.g., 3× the 12-month fee cap, or a fixed dollar amount tied to the sensitivity of the data).
- Confirm that Figos's Technology E&O / Cyber insurance (currently $5M per claim, per the Certificate of Insurance § 5.3) would respond to a negligent Security Incident, and request that Traimand be added as an additional insured or loss payee on that policy (see Issue 8).

---

## Issue 4: Renewal Pricing at Unconstrained List Price

**Where:** OF-001 § 2.4

**Facts:** "Subscription Fees for each Renewal Term are charged at Licensor's then-current list pricing for the Platform Modules and user seats subscribed at the time of renewal." There is no cap, formula, or most-favored-customer provision.

**Why it matters:** If Issue 1 results in an involuntary renewal, Traimand would be locked in for 24 months at whatever Figos's list price happens to be in February 2027. Given that the initial term carried only ~3% annual escalators ($465K → $478.95K → $493.32K), a shift to "list pricing" could represent a substantial increase, particularly if Figos has raised prices for new customers or if the market has shifted.

**Recommended fix:**
- As part of the global resolution, negotiate that any renewal (whether voluntary or involuntary) be priced at no more than a stated percentage increase (e.g., CPI + 2%) over the Year 3 rate, or at the rates in a mutually agreed price schedule.
- If the non-renewal is ultimately upheld, this issue becomes moot, but it should be addressed in any settlement to prevent re-litigation.

---

## Issue 5: Model Specifications in Transition Package May Be Licensed Only During Subscription Term

**Where:** SLA §§ 7.1, 7.3, 2.1; SOW 02 § 3.4(c)

**Facts:** SOW 02 § 3.4(c) requires the Transition Package to include "the model specifications and parameter sets used in those runs, sufficient to permit an independent quantitative geneticist to reproduce the computation outside the Platform." SLA § 7.3 provides that SOW deliverables "become Customer's property upon payment in full," but "Licensor's pre-existing materials incorporated in any deliverable remain Licensor's property and are licensed to Customer on the terms of Section 2.1." Section 2.1 grants a license only "during the Subscription Term."

**Why it matters:** The model specifications (e.g., ssGBLUP parameter sets, marker QC thresholds, relationship matrix blending weights) are almost certainly Figos's pre-existing intellectual property embedded in the Platform (SLA § 7.1). Once the Subscription Term ends, Traimand's license to those specifications would expire, even though the Transition Package as a whole is Traimand's property. This would undermine the entire purpose of the transition — enabling Traimand (or its Kestrel integration team) to reproduce GEBV computations independently.

**Recommended fix:**
- Negotiate a perpetual, irrevocable, royalty-free license to the model specifications and parameter sets included in the Transition Package, surviving expiration or termination of the Agreement. This should be documented either in SOW 02 (as a modification to the default in SLA § 7.3) or in a side letter.
- Alternatively, require Figos to deliver the model specifications in a form that is fully documented and self-contained (i.e., not requiring access to the Platform or any Figos-proprietary software to interpret), and confirm in writing that such documentation is a "deliverable created specifically for Customer" rather than a "pre-existing material."

---

## Issue 6: Broad Customer Indemnity for Legacy Trial Data

**Where:** SOW 02 § 7.1; SLA §§ 3.2, 6.1, 10.3

**Facts:** SOW 02 § 7.1 requires Traimand to indemnify Figos against any third-party claim "arising from the Legacy Trial Data or from Licensor's receipt, processing, loading or transfer of the Legacy Trial Data in accordance with this Statement of Work," including claims that the data "was collected, used or transferred in breach of grower agreements, cooperator trial agreements, third-party germplasm licenses, material transfer agreements or other obligations owed by Customer to any third party." The Legacy Trial Data spans 2009–2023 and includes data from cooperator sites and in-licensed germplasm (SOW 02 § 1, Exhibit A).

**Why it matters:** The indemnity is very broad. It covers not only claims about the data itself but also claims about Figos's *processing* of the data, so long as Figos acts "in accordance with" the SOW. Given the age and volume of the data (6.4 million plot records across three systems, plus ~3,800 spreadsheet workbooks), there is a real risk that some cooperator agreements or germplasm licenses from 2009–2014 contain data-use restrictions that were not carried forward. A single grower or licensor claim could trigger the indemnity. The exclusion in § 7.2 (claims arising from Figos's unauthorized use or disclosure) is narrow.

**Recommended fix:**
- Before delivering the Legacy Trial Data, conduct a targeted review of cooperator trial agreements and germplasm in-license agreements for data-sharing restrictions, particularly for the 2009–2014 period. Document the review.
- Negotiate to narrow the indemnity in § 7.1 to claims arising from the *content* of the Legacy Trial Data (i.e., Traimand's lack of rights in the data itself), excluding claims arising from Figos's *methods* of processing, even if those methods are "in accordance with" the SOW.
- Confirm that the indemnity is subject to the SLA § 10.4 procedure (it is, per § 7.3) and that Figos's obligation to give prompt notice and allow Traimand control of the defense applies.

---

## Issue 7: Restrictive Use Limitation on Building Competing Products

**Where:** SLA § 3.1(e)

**Facts:** Customer shall not "use the Platform to build a competing genomic selection product."

**Why it matters:** Traimand is a breeding company that may wish to develop in-house genomic selection capabilities, particularly as part of the Kestrel integration. While the restriction on its face applies only to "using the Platform," it could be argued to extend to using knowledge, methodologies, or workflows learned through the Platform to build an internal tool. This is especially concerning in the context of the Transition Package (SOW 02 § 3.4(c)), which is designed to enable independent reproduction of GEBV computations.

**Recommended fix:**
- Seek a clarification or amendment confirming that the restriction in § 3.1(e) applies only to the Figos Platform software itself (i.e., Traimand may not resell or redistribute the Platform) and does not restrict Traimand from developing its own genomic selection tools using Customer Data, Derived Data, or the Transition Package.
- This clarification should be documented in writing, ideally as an amendment to the SLA or a provision in the SOW 02.

---

## Issue 8: Traimand Not Additional Insured on Technology E&O / Cyber Policy

**Where:** Certificate of Insurance §§ 5.3, 6.3; SLA § 13.2

**Facts:** SLA § 13.2 requires Figos to name Traimand as an additional insured "under the commercial general liability policy." The Certificate of Insurance confirms Traimand is additional insured on the CGL policy (§ 6.3). However, the Technology E&O / Network Security and Privacy Liability policy (§ 5.3, $5M per claim) does not list Traimand as an additional insured.

**Why it matters:** In a data breach or Security Incident, the CGL policy is unlikely to respond (CGL typically excludes data breaches and electronic data loss). The relevant coverage would be the Technology E&O / Cyber policy. Because Traimand is not an additional insured on that policy, it cannot directly claim under it. Traimand must rely on (a) its own cyber insurance, (b) Figos's indemnification obligations under the SLA, and (c) the liability provisions (which, per Issue 3, are capped for negligent breaches).

**Recommended fix:**
- Request that Figos add Traimand as an additional insured (or at minimum as a "loss payee" or "interested party") on the Technology E&O / Cyber policy. If the policy form does not permit additional insured status for cyber coverage (which is common), request that Figos provide a direct obligation to pay any settlement or judgment to Traimand as an intended beneficiary.
- As an alternative, negotiate a provision requiring Figos to maintain a "tail" or extended reporting period on the cyber policy for at least 3 years after termination of the Agreement, to cover latent data breaches.

---

## Issue 9: Claims-Made Cyber Policy Without Extended Reporting Period

**Where:** Certificate of Insurance § 5.3

**Facts:** The Technology E&O / Cyber policy is a **claims-made** form with a policy period of February 1, 2026 – February 1, 2027 and a retroactive date of January 1, 2019. No extended reporting period (tail) is indicated.

**Why it matters:** Under a claims-made policy, a claim must be *made* (not just the incident must occur) during the policy period. If a Security Incident occurs in January 2027 but is not discovered or reported until March 2027 (after the policy expires), Figos may have no insurance coverage to respond to Traimand's claim. This is particularly relevant given the 72-hour notification requirement in SLA § 9.2 — if Figos is slow to detect or notify, the claim could fall outside the policy window.

**Recommended fix:**
- Request that Figos provide evidence of a "tail" or extended reporting period of at least 3 years following policy expiration, or confirm that the next policy year will maintain the same retroactive date (January 1, 2019) so there is no gap.
- Include this as a condition in any renewal or extension negotiation.

---

## Issue 10: Weak Platform Warranty Remedy

**Where:** SLA § 8.2

**Facts:** If the Platform does not perform materially in accordance with the Documentation, Figos "shall use commercially reasonable efforts to correct the nonconformity." If Figos cannot do so within 30 days, "Customer may terminate the affected Order Form and receive a refund of prepaid Fees for the remainder of the Subscription Term." There is no service-credit regime for the warranty (the service credits in OF-001 § 6.3 apply only to availability, not to functional non-conformance).

**Why it matters:** If the Platform produces incorrect GEBVs due to a software defect (as opposed to a data integrity deviation, which is covered by the Quality Agreement), Traimand's only remedy is to terminate and get a refund. There is no right to damages for selection decisions made in reliance on incorrect GEBVs, no service credits, and no obligation on Figos to re-run computations at no charge (contrast with QA § 6.3, which applies to data integrity deviations). For a breeding company making multi-million-dollar selection decisions, this is an inadequate remedy.

**Recommended fix:**
- Negotiate an amendment to SLA § 8.2 to add: (a) a service-credit mechanism for functional non-conformance (analogous to the availability credits in OF-001 § 6.3); (b) an obligation for Figos to re-run affected computations at no charge (mirroring QA § 6.3); and (c) a clarification that the warranty covers material accuracy of GEBV outputs, not just conformance to Documentation.
- In the interim, ensure that the Quality Agreement's data integrity provisions (QA § 6) are being strictly enforced, as they provide a more robust remedy for the most common failure mode.

---

## Issue 11: One-Sided Assignment Provisions

**Where:** SLA §§ 14.2, 14.3

**Facts:** Customer may not assign without Licensor's consent, and a Change of Control of Customer is *deemed* an assignment requiring consent (§ 14.2). Licensor may assign to any Affiliate or to "any successor or acquirer of all or part of its business or assets to which this Agreement relates" without Customer's consent (§ 14.3).

**Why it matters:** The asymmetry is significant. Traimand cannot be acquired (or merge, as with Kestrel) without Figos's consent, but Figos can be acquired by a competitor of Traimand (or by a private equity firm that might raise prices) without Traimand's consent. Given that Traimand's Customer Data includes highly sensitive germplasm information, an assignment to a competitor would be particularly concerning.

**Recommended fix:**
- Negotiate a mutual assignment provision: Licensor may assign to an Affiliate without consent, but may assign to a third-party acquirer only with Customer's consent (not to be unreasonably withheld), or only if the acquirer agrees in writing to be bound by the data protection and confidentiality provisions.
- At minimum, add a right for Customer to terminate without penalty if Licensor assigns to a direct competitor of Customer.

---

## Issue 12: Pending Validation Report Acceptance – No Deemed Acceptance but No Consequence of Silence

**Where:** Meeting Notes § 5.5, Action Item 1; QA § 7.3

**Facts:** Validation Report VR-2026-03 was delivered to Dr. Ostrander on August 12, 2026. QA § 7.3 requires Customer to "accept or reject the Validation Report in writing within ten (10) business days after receipt" — i.e., by August 26, 2026. The meeting notes (circulated August 28, 2026) confirm that Dr. Ostrander stated Traimand's review "is under way" and that written acceptance or rejection would be delivered by August 26, 2026. We have no document in the file confirming that Traimand actually delivered its response by that date.

**Why it matters:** QA § 7.3 does not contain a deemed-acceptance provision (unlike SOW 02 § 5.3, which deems SOW deliverables accepted if not rejected within the review period). If Traimand failed to respond by August 26, the Validation Report is in a limbo state: neither accepted nor rejected. Figos may argue that silence constitutes acceptance or that it is entitled to proceed with deployment on November 10, 2026 (the date confirmed in the meeting notes, § 4.3). However, QA § 7.1 states that Figos "shall not deploy a Model Change to the Production Environment until it has been validated in accordance with this Section 7," and § 7.3 requires Customer acceptance. Strictly read, Figos cannot deploy without Traimand's written acceptance.

**Recommended fix:**
- Confirm immediately whether Dr. Ostrander delivered written acceptance or rejection by August 26, 2026. If not, deliver acceptance (the validation results in the meeting notes show all criteria were met) to avoid any argument that Traimand is in breach of its QA obligations or that its silence constitutes acceptance of terms it hasn't reviewed.
- If there are any scientific reservations, deliver a conditional acceptance or a rejection with specific comments, as QA § 7.3 permits rejection "if an acceptance criterion is not met or the Validation Protocol was not followed in a material respect."
- Document the acceptance in the Change Control Record (QA § 7.4) to create a clear audit trail.

---

## Issue 13: Usage Allowance Exceedance Has No Enforcement Mechanism

**Where:** OF-001 § 3.3

**Facts:** The subscription includes "up to 250,000 genotyped lines per contract year and up to 60,000 SNP markers per line." If Traimand exceeds the allowance, "Licensor will notify Customer. The Parties will then discuss in good faith an increase in the allowance at the rates in Section 4.3." Section 4.3 sets the overage rate at $0.85 per line per contract year.

**Why it matters:** There is no mechanism for what happens if the parties cannot agree on an increase. Figos could argue that Traimand is in breach of the usage limitation and potentially suspend service. Conversely, Traimand might argue that the overage rate in § 4.3 is the default and that the "good faith discussion" is merely to confirm it. The ambiguity could become acute if Traimand's Kestrel integration significantly increases the number of lines being genotyped.

**Recommended fix:**
- Negotiate a clarification that overage usage is automatically billed at the § 4.3 rate without requiring a separate agreement, and that Figos may not suspend or restrict access for overage usage so long as Traimand pays the overage fees within 30 days of invoice.
- If Traimand anticipates significant growth post-Kestrel integration, proactively negotiate a higher allowance or a volume discount for the next contract year.

---

## Issue 14: SOW 02 Transition Package Acceptance and Deemed Acceptance Risk

**Where:** SOW 02 § 5.3

**Facts:** SOW 02 § 5.3 provides: "A Deliverable is deemed accepted if Customer does not notify Licensor of a material nonconformity within the review period, **or if Customer uses the Deliverable in its Production Environment for operational selection decisions**."

**Why it matters:** The second prong of deemed acceptance is particularly dangerous in the transition context. If Traimand loads any portion of the Transition Package into its new system (or Kestrel's system) and uses it for selection decisions before formally reviewing and accepting it, the deliverable is deemed accepted. This could foreclose Traimand's ability to raise quality issues with the Transition Package after the fact. Given that the Transition Package is the critical deliverable for the Kestrel integration, this is a significant risk.

**Recommended fix:**
- Implement an internal protocol requiring that no component of the Transition Package be used for operational selection decisions until it has been formally reviewed and accepted in writing by Dr. Ostrander (or his designee).
- If any component is used on a trial or exploratory basis before formal acceptance, document that use as "evaluation" rather than "operational selection decisions" to avoid triggering deemed acceptance.
- Consider negotiating a deletion of the second prong of § 5.3 as it applies to the Transition Package (Deliverable 4), or a longer review period for that deliverable given its complexity.

---

## Summary Table

| # | Issue | Document / Section | Severity |
|---|-------|-------------------|----------|
| 1 | Late non-renewal notice; involuntary 24-mo renewal | SOW 02 § 8.1; SLA § 12.2; OF-001 § 2.3 | **Critical** |
| 2 | Change of Control consent not obtained | SLA §§ 1.1, 14.2; SOW 02 Recital C | **Critical** |
| 3 | Data-security liability capped except for willful disclosure | OF-001 ST § 4; SLA §§ 11.1, 11.3(b) | **Critical** |
| 4 | Renewal pricing at unconstrained list price | OF-001 § 2.4 | High |
| 5 | Model specs licensed only during Subscription Term | SLA §§ 7.1, 7.3, 2.1; SOW 02 § 3.4(c) | High |
| 6 | Broad indemnity for Legacy Trial Data | SOW 02 § 7.1 | High |
| 7 | Restriction on building competing product | SLA § 3.1(e) | Medium |
| 8 | No additional insured on E&O/Cyber policy | COI §§ 5.3, 6.3; SLA § 13.2 | Medium |
| 9 | Claims-made cyber policy; no tail | COI § 5.3 | Medium |
| 10 | Weak platform warranty remedy | SLA § 8.2 | Medium |
| 11 | One-sided assignment | SLA §§ 14.2, 14.3 | Medium |
| 12 | Validation Report acceptance status unclear | Meeting Notes § 5.5; QA § 7.3 | Medium |
| 13 | Usage overage – no enforcement mechanism | OF-001 § 3.3 | Low |
| 14 | Deemed acceptance risk for Transition Package | SOW 02 § 5.3 | Medium |

---

## Recommended Next Steps (Priority Order)

1. **Confirm whether Traimand delivered written acceptance of VR-2026-03 by August 26, 2026.** If not, deliver it immediately (Issue 12).
2. **Open a dialogue with Figos on the non-renewal notice and Change of Control consent as a package.** Propose: (a) Figos accepts the non-renewal notice as effective (or the parties agree to a mutual termination at the end of the Initial Term); (b) Figos consents to the Kestrel Change of Control; (c) in exchange, Traimand completes SOW 02 and pays all SOW fees (Issue 1, Issue 2).
3. **Request a global amendment** addressing Special Term 4 (data security cap), the model specifications license (perpetual), the assignment symmetry, and the Transition Package deemed-acceptance provision (Issues 3, 5, 11, 14).
4. **Conduct the cooperator/licensor agreement review** before delivering Legacy Trial Data under SOW 02 (Issue 6).
5. **Request updated insurance documentation** confirming additional insured status on the cyber policy or an alternative protection mechanism (Issues 8, 9).