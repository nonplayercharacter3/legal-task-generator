# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Stutind Solar Installations, LLC – Zikeiv Software License: Issue Identification

---

## Summary

I have reviewed all ten documents in the matter folder. I identify **six critical issues**, **six significant issues**, and **four lower-priority items** requiring attention. The most urgent matter is that Stutind's Notice of Nonconformity (August 24, 2026) appears to be **five business days late** under the SOW, meaning Deliverable D-2 may already be deemed accepted. Several other terms in the executed documents materially depart from what the Term Sheet negotiated, most favorably to Zikeiv.

---

## CRITICAL ISSUES

### 1. Notice of Nonconformity Is Likely Untimely – D-2 May Be Deemed Accepted

**Where:** SOW §5.2; Notice Letter (dated August 24, 2026)

**Issue:** SOW §5.2 requires Licensee to give written notice of Nonconformity "within ten (10) Business Days after the Delivery Date," failing which "Deliverable D-2 is deemed accepted as of the last day of that period." The Delivery Confirmation is dated **August 3, 2026** (a Monday). Counting forward, the 10th Business Day is **Monday, August 17, 2026**. The Notice Letter is dated **August 24, 2026** – five Business Days after the deadline.

**Why it matters:** If D-2 is deemed accepted, Stutind loses:
- The right to reject the Module and demand correction under SOW §5.3;
- The right to terminate under SOW §5.4 (which requires a failed *second* redelivery);
- Leverage over the $148,000 Milestone 2 fee (the Notice Letter's withholding position in §4.1 becomes untenable if acceptance is deemed to have occurred); and
- The warranty remedy under Agreement §13.3, which is triggered by a "breach" of the performance warranty – a harder argument once the deliverable is accepted.

The Notice Letter does not acknowledge or address the timing problem.

**Recommended fix:**
- Immediately confirm with the client whether the notice was in fact *sent* (by email with confirmation of transmission, per Agreement §15.1) on or before August 17, even though the letter is dated August 24. If it was sent earlier, the date on the letter is not dispositive – the SOW requires notice to be *given*, and Agreement §15.1 provides that email notices are effective on receipt.
- If the notice was genuinely first sent on August 24, assess whether Zikeiv's conduct (e.g., continued engagement on the nonconformities, failure to invoice Milestone 2, or course of performance) constitutes a waiver of the deemed-acceptance provision or an equitable estoppel.
- In all events, send a follow-up letter to Zikeiv confirming that Stutind does not accept D-2 and that the August 24 letter (or an earlier transmission, if one exists) constitutes timely notice. Request Zikeiv's written confirmation that it does not treat D-2 as accepted.
- Preserve all evidence of when the notice was transmitted (email headers, courier receipts).

**Flag:** I cannot resolve from the documents alone whether the notice was actually transmitted before August 17. The letter is *dated* August 24, but the transmission date is not stated. **Client confirmation is needed.**

---

### 2. Exclusivity Covenant Dramatically Expanded Beyond Term Sheet

**Where:** Term Sheet §9; Prior Draft §3.4; Final Agreement §3.4; Order Form §4

**Issue:** The negotiated scope of exclusivity was:

| Document | Scope |
|---|---|
| Term Sheet §9 | "Residential rooftop design software only, in Arizona and Nevada. Stutind's commercial, utility-scale and other business lines, and all jurisdictions outside Arizona and Nevada, are not covered." |
| Prior Draft §3.4 | "residential rooftop solar design software for use on residential rooftop installations located in Arizona or Nevada" – expressly excluding commercial, utility-scale, permitting/proposal software, and out-of-state installations |
| **Final Agreement §3.4** | "any solar system design, permitting or proposal software other than the Licensed Software for any installation in the Territory" |
| **Order Form §4** | Territory = "the United States and Canada" |

The final clause is broader in **four** dimensions:
1. **Software category:** "residential rooftop design software" → "any solar system design, permitting or proposal software"
2. **Installation type:** residential rooftop only → "any installation" (including commercial, utility-scale)
3. **Geography:** Arizona and Nevada → United States and Canada
4. **Restricted acts:** "license or procure" → "license, use, develop or procure" (the word "develop" is new)

Additionally, Final Agreement §3.4 adds "shall cause its Affiliates not to," binding Stutind's affiliates to the expanded covenant.

**Why it matters:** Stutind is a "residential and commercial solar installation contractor" (Recital B). Under the final clause, Stutind cannot use *any* competing design, permitting, or proposal software for *any* installation anywhere in the US or Canada for the duration of the Subscription Term (initial 36 months + potential 36-month renewals). This could prohibit Stutind from using a different proposal tool for a commercial project in Texas, or from developing an internal permitting workflow. A breach would constitute a material breach triggering Zikeiv's termination right under Agreement §10.3 and Stutind's indemnity obligation under §11.3.

**Recommended fix:**
- Negotiate a correction to §3.4 restoring the Term Sheet scope (residential rooftop design software, AZ and NV only, excluding commercial/utility-scale and permitting/proposal software).
- If Zikeiv resists, seek at minimum: (a) exclusion of commercial and utility-scale installations; (b) exclusion of permitting and proposal software (leaving only design software); and (c) deletion of "develop" from the restricted acts.
- Document the discrepancy between the Term Sheet and the final agreement as evidence of negotiating history, should the clause be challenged as unconscionable or as a material departure from the parties' agreement (though Agreement §16.4's entire-agreement clause makes this difficult).

**Flag:** The Term Sheet is expressly non-binding (Term Sheet §15) and is superseded by the final agreement (Agreement §16.4). However, the Prior Draft (January 6, 2026) – which tracked the Term Sheet – was the last draft before execution. The gap between the Prior Draft and the Final on this point is significant and suggests the change was made in Zikeiv's favor without corresponding consideration.

---

### 3. Side Letter Gutted the Limitation-of-Liability Protections

**Where:** Side Letter §2 (amending Agreement §12.2); Agreement §§12.1–12.3; DPA §9

**Issue:** The original Agreement §12.2 excluded from both the liability cap (§12.1) and the consequential-damages waiver (§12.3):
- (a) indemnification obligations under Section 11;
- (b) breach of Section 9 (Data Security) or Section 8 (Confidentiality); and
- (c) gross negligence or willful misconduct.

The Side Letter (June 10, 2026) deleted all of that and replaced §12.2 with a single exclusion:

> "The limitation in Section 12.1 and the exclusion in Section 12.3 do not apply to **Licensor's obligations under Section 11.1 (Infringement Indemnity)**."

**Net effect under the amended provision:**

| Scenario | Original Protection | Post-Side Letter |
|---|---|---|
| Zikeiv data breach exposing homeowner data | Uncapped; consequential damages available | Capped at ~$312K (12 months' fees); consequential damages excluded |
| Zikeiv's gross negligence or willful misconduct | Uncapped; consequential damages available | Capped at ~$312K; consequential damages excluded |
| Zikeiv's breach of confidentiality (e.g., disclosing Stutind's pricing to a competitor) | Uncapped; consequential damages available | Capped at ~$312K; consequential damages excluded |
| Zikeiv's IP infringement indemnity | Uncapped | Uncapped (unchanged) |
| Stutind's indemnity to Zikeiv (§11.3) | Uncapped | Capped at ~$312K; consequential damages excluded |

DPA §9 expressly subjects DPA liability to "the limitations and exclusions of liability in Section 12 of the Agreement." The DPA's security-incident cost reimbursement (§7.4) is therefore also capped.

**Why it matters:** Stutind processes sensitive homeowner data (addresses, property/parcel info, utility account numbers, e-signature records – DPA Annex 1). A data breach could trigger notification costs, credit monitoring, regulatory penalties (under state privacy and breach laws), and class-action exposure easily exceeding $312,000. Under the amended §12.2, Stutind's recovery is capped and it cannot recover consequential damages (lost business, reputational harm) even if Zikeiv's gross negligence caused the breach.

**Recommended fix:**
- Negotiate restoration of the original §12.2 exclusions, or at minimum: (a) breach of Section 9 (Data Security); (b) breach of Section 8 (Confidentiality); and (c) gross negligence or willful misconduct.
- If Zikeiv's position is that the Side Letter was exchanged for the $31,200 Subscription Credit and reference-customer obligations, that consideration is grossly disproportionate to the value of the liability protections removed. Raise this in any renegotiation.
- As a risk-mitigation measure in the interim, confirm that Zikeiv's cyber liability insurance ($5M per claim, Agreement §14.1(c)) is in place and obtain a certificate. Note, however, that the insurance protects Zikeiv, not Stutind directly, and the policy limits may be eroded by other claims.

**Flag:** The Side Letter was executed (or is in execution) – the signature blocks are blank in the copy provided. **Confirm with the client whether Stutind has signed the Side Letter.** If not signed, it is not effective and the original §12.2 remains in force. If signed, the amendment is binding under Agreement §15.8.

---

### 4. Renewal Terms Changed from 12 to 36 Months with a Narrow Notice Window

**Where:** Term Sheet §5(c); Prior Draft §10.2; Final Agreement §10.2; Order Form §§2.3–2.4

**Issue:**

| Provision | Term Sheet / Prior Draft / Final Agreement | Order Form (controls per §1.3) |
|---|---|---|
| Renewal term length | 12 months | **36 months** |
| Non-renewal notice | 60 days before term end | **Received no earlier than 120 days and no later than 90 days before term end** |

The Order Form prevails over the Agreement under the order of precedence (Agreement §1.3).

**Why it matters:**
- Stutind is locked into a minimum 36-month initial term (February 1, 2026 – January 31, 2029).
- If Stutind misses the non-renewal window, it is locked in for another **36 months** (through January 31, 2032), not 12.
- The notice window is only **30 days wide** (between 120 and 90 days before term end). For the Initial Term ending January 31, 2029, Stutind must deliver notice between approximately **October 3, 2028** and **November 2, 2028**. Missing this window by even one day results in a 36-month extension.
- Renewal fees are at "Licensor's then-current list price" (Order Form §2.3) – no price protection.

**Recommended fix:**
- Calendar the non-renewal notice deadline immediately (October 3, 2028 – November 2, 2028 for the Initial Term) and set internal reminders well in advance.
- Negotiate a correction to Order Form §2.3–2.4: (a) reduce renewal terms to 12 months; (b) widen the notice window (e.g., 60–180 days before term end); and/or (c) add price-protection language (e.g., renewal fees shall not increase by more than CPI or a fixed percentage per year).
- If the 36-month renewal term is non-negotiable, seek a termination-for-convenience right after the Initial Term with a reasonable notice period and pro-rata refund.

---

### 5. Assignment Clause Made One-Way; Change-of-Control Protection Deleted

**Where:** Term Sheet §13; Prior Draft §15.3; Final Agreement §15.3

**Issue:**

| Provision | Term Sheet / Prior Draft | Final Agreement |
|---|---|---|
| Mutual restriction | "Neither party may assign without the other party's prior written consent" | Only **Licensee** is restricted from assigning |
| Consent standard | "which shall not be unreasonably withheld" | No standard – Licensor may withhold consent for any reason |
| Change-of-control termination | If a solar installation provider acquires control of Licensor, Licensee may terminate within 90 days | **Deleted entirely** |

**Why it matters:**
- Zikeiv can assign the agreement (e.g., in an acquisition or asset sale) without Stutind's consent. Stutind could end up with a new licensor it did not choose.
- If a direct competitor of Stutind (a solar installation company) acquires Zikeiv, Stutind has no termination right. The competitor would then have access to Stutind's Licensee Data (subject to confidentiality, but the business relationship continues) and Stutind would be bound by the expanded exclusivity covenant (§3.4) to use the competitor's software.
- Stutind cannot assign the agreement (e.g., in connection with its own M&A) without Zikeiv's consent, which can be withheld arbitrarily.

**Recommended fix:**
- Negotiate restoration of: (a) mutual assignment restriction; (b) "not unreasonably withheld" standard; and (c) a change-of-control termination right for Stutind if Licensor is acquired by a solar installation competitor.
- In the interim, monitor Zikeiv's corporate developments. If a change of control occurs, assess whether it constitutes a material breach of the mutual-warranty provision (§13.1) or a basis for termination under §10.3 (argument is weak but not frivolous if the acquirer is a direct competitor).

---

### 6. Custom Permitting Automation Module Owned by Zikeiv

**Where:** SOW §9; Agreement §7.3; Agreement §3.1

**Issue:** SOW §9 provides that "Section 7.3 of the Agreement applies to the Module and all other Deliverables." Agreement §7.3 states: "Licensor owns all modifications and enhancements to the Licensed Software, including any developed under an SOW." The Module "forms part of the Licensed Software and is licensed to Licensee under Section 3.1 of the Agreement for the Subscription Term at no additional subscription fee."

**Why it matters:**
- Stutind is paying $250,000 (SOW §6.1) for a Module that is custom-configured for Stutind's specific jurisdictions (Schedule A: 12 AHJs in AZ and NV), including jurisdiction-specific rule sets, validation logic, and form population mappings.
- Zikeiv owns the Module. It can license the same jurisdiction-specific configurations to Stutind's competitors.
- If the agreement terminates (for any reason), Stutind loses the Module. The $250,000 investment yields no residual IP or data asset.
- The Module's license is co-terminous with the Subscription Term (§3.1). There is no perpetual license, no source-code escrow, and no right to a transition period.

**Recommended fix:**
- Negotiate one or more of the following:
  - A perpetual, irrevocable license to the Module (or at least the jurisdiction-specific configurations) surviving termination;
  - Source-code escrow for the Module, releasable on Zikeiv's insolvency or material breach;
  - A non-compete or field-of-use restriction preventing Zikeiv from offering the same jurisdiction-specific Module to Stutind's direct competitors in AZ/NV for a defined period;
  - A transition-services obligation requiring Zikeiv to support the Module for a defined period post-termination.
- At minimum, ensure that the Licensee Data (including the jurisdiction-specific rule parameters Stutind configured) is fully exportable under Agreement §7.5.

---

## SIGNIFICANT ISSUES

### 7. DPA Governing Law and Forum Conflict with Main Agreement

**Where:** DPA §§11.1–11.2; Agreement §§16.1–16.2

**Issue:** The Agreement specifies Delaware law and New Castle County, Delaware forum. The DPA specifies **California law** and **San Francisco County, California** forum. DPA §11.1–11.2 appear to be boilerplate that was not conformed to the main agreement.

The order of precedence (Agreement §1.3) gives the DPA priority "as to Personal Data." This creates an ambiguous split: a dispute involving both personal data processing and, say, a service-level failure might be subject to two different governing laws and forums.

**Why it matters:** If a data breach occurs, Stutind would need to litigate in California under California law for the DPA claims, but in Delaware under Delaware law for any related Agreement claims (e.g., the security obligations in §9, the warranty in §13.2(c)). This increases cost, complexity, and the risk of inconsistent outcomes.

**Recommended fix:** Amend DPA §11 to conform to the Agreement (Delaware law, New Castle County forum), or add a provision that all disputes under the transaction documents are consolidated in a single forum.

---

### 8. Subprocessors Not Identified by Name

**Where:** DPA Annex 3; DPA §6.1

**Issue:** Annex 3 lists subprocessors by function only ("Primary cloud hosting provider," "Secondary cloud hosting provider," "Transactional email service," "E-signature service," "Customer support ticketing service"). No company names are given.

**Why it matters:**
- Stutind cannot assess the security posture, financial stability, or compliance history of its actual subprocessors.
- The objection right in DPA §6.3 (object to a *new* subprocessor on reasonable data protection grounds) is less meaningful when the baseline subprocessors are anonymous.
- If a subprocessor is involved in a security incident, Stutind may not know which entity to pursue or whether it is covered by Zikeiv's insurance.

**Recommended fix:** Require Zikeiv to populate Annex 3 with the actual legal names of all authorized subprocessors. Add a covenant that Zikeiv will identify subprocessors by name in any §6.2 notice of a new subprocessor.

---

### 9. No Price Protection at Renewal

**Where:** Order Form §2.3

**Issue:** "Fees for each Renewal Term are charged at Licensor's then-current list price for the Licensed Software and the number of installer seats in effect at the end of the preceding term."

**Why it matters:** Combined with the 36-month auto-renewal (Issue 4), Stutind faces unbounded price escalation at each renewal. If Zikeiv raises list prices by 20% per year, Stutind's $312,000 annual fee becomes $374,400 at the first renewal and $449,280 at the second – with no contractual cap.

**Recommended fix:** Negotiate a price-protection mechanism: e.g., renewal fees shall not increase by more than the lesser of (a) 5% per year or (b) CPI-U. Alternatively, fix the per-seat rate for the duration of the Subscription Term including renewals.

---

### 10. Canadian Customer Data in US-Only Data Centers

**Where:** DPA §5.2; Order Form §4; DPA §1 (Applicable Data Protection Laws)

**Issue:** DPA §5.2 restricts storage and processing of Personal Data to US data centers. The Territory includes Canada (Order Form §4). The DPA defines "Applicable Data Protection Laws" to include "all Canadian federal and provincial laws." Canadian customers' Personal Data (names, addresses, property info, utility accounts) will be stored in the US.

**Why it matters:** Under PIPEDA and provincial privacy laws (e.g., BC PIPA, Quebec Law 25), cross-border data transfers require the organization to remain accountable for the data and to ensure a comparable level of protection abroad. The DPA does not address the cross-border transfer mechanism (e.g., contractual clauses, impact assessment). If a Canadian regulator inquires, Stutind (as controller) may need to demonstrate that the US-based processing meets Canadian standards.

**Recommended fix:** Add a provision to the DPA addressing cross-border transfers to the US, including: (a) Zikeiv's commitment to maintain protections comparable to those required by Canadian law; (b) a data protection impact assessment for the cross-border transfer; and (c) cooperation with Stutind in responding to any Canadian regulator inquiry.

---

### 11. "Develop" Added to Exclusivity Restrictions

**Where:** Final Agreement §3.4 (compare Term Sheet §9 and Prior Draft §3.4)

**Issue:** The final clause prohibits Stutind from "develop[ing]" competing software. Neither the Term Sheet nor the Prior Draft included this word.

**Why it matters:** Read broadly, "develop" could restrict Stutind from building internal tools, automations, or workflows that touch solar design, permitting, or proposal generation – even if those tools are not offered to third parties and are not "competing products" in any market sense. For a tech-forward installation company, this could impede internal innovation.

**Recommended fix:** Delete "develop" from §3.4, or narrow it to "develop... for offer to third parties." At minimum, add an express carve-out for internal business processes and tools not made available outside Stutind and its Affiliates.

---

### 12. Service Credits Are the Sole Monetary Remedy for Availability Failures

**Where:** Agreement §4.2; Quality Agreement §5.6

**Issue:** "Service credits under the Quality Agreement are Licensee's sole monetary remedy for availability failures." Maximum credit is 50% of the monthly fee (Quality Agreement §5.3), i.e., ~$13,000 per month.

**Why it matters:** If HelioPlan is down for an extended period during peak permitting season, Stutind may lose significant revenue (inability to generate proposals, submit permits, or close sales). Its only monetary recovery is a credit of at most $13,000 per month – a fraction of likely lost business. The consequential-damages waiver (Agreement §12.3) independently bars recovery of lost profits.

**Recommended fix:** This is a standard SaaS provision and difficult to change. Mitigations:
- Ensure the Chronic Failure threshold (Quality Agreement §6.1) is calibrated to Stutind's operational needs. The current threshold (99.5% in 3 of 6 months, or 95% in any single month, or 4 Sev-1 incidents in 90 days) may be too lenient for a business that depends on the platform daily.
- Negotiate a higher service-credit ceiling (e.g., 100% of monthly fee) for sustained outages.
- Confirm that the Chronic Failure termination right (which triggers a refund of prepaid fees under §10.5(c)) is adequately protective.

---

## LOWER-PRIORITY / WATCH ITEMS

### 13. SOW Target Dates Are Estimates with No Remedy for Delay

**Where:** SOW §6.5

**Issue:** "Target dates are estimates. The Project Managers shall update them as the project progresses." There is no liquidated-damages provision, no outside date, and no termination right for schedule delay short of material breach.

**Why it matters:** If Zikeiv's development of the Module slips significantly (e.g., into 2027), Stutind's only recourse is to argue material breach under Agreement §10.3, which requires a 30-day cure period and is a high bar. Stutind is paying $312,000/year for a platform whose key value-add (the Module) has no firm delivery deadline.

**Recommended fix:** Negotiate an outside date for Milestone 3 (e.g., December 31, 2026) with a termination right and full refund if Zikeiv misses it without cause. Alternatively, add liquidated damages for delay.

### 14. Permitting Content Updates Are "Commercially Reasonable Efforts" Only

**Where:** Quality Agreement §8.2

**Issue:** Zikeiv must use "commercially reasonable efforts to update" jurisdiction-specific permitting content within 30 days of an AHJ publishing a change. This is not a hard obligation.

**Why it matters:** If an AHJ changes its requirements and Zikeiv fails to update the templates, Stutind may generate non-compliant permit packages. The disclaimer in Agreement §13.4 ("Licensor does not warrant that permit submissions... will be approved") shifts the risk to Stutind. A "commercially reasonable efforts" standard is difficult to enforce.

**Recommended fix:** Seek to convert this to a firm obligation ("Licensor shall update... within thirty (30) days") or, at minimum, add a service credit for failure to update within the stated period.

### 15. Side Letter Reference-Customer Obligations

**Where:** Side Letter §§3.1–3.2

**Issue:** Stutind agreed to one written case study (with approval rights) and up to four reference calls with prospective Zikeiv customers through January 31, 2027.

**Why it matters:** Low risk, but Stutind should ensure that (a) the case study draft is actually reviewed before publication, and (b) reference calls do not inadvertently disclose Confidential Information. The Side Letter states Stutind is "not required to disclose its pricing, Licensee Data or other Confidential Information," but verbal misstatements in a call could create issues.

**Recommended fix:** Brief the personnel who will participate in reference calls on the boundaries. Track completion of the case study obligation to close it out.

### 16. Suspension Right for Non-Payment

**Where:** Agreement §6.5

**Issue:** Zikeiv may suspend access to the entire Licensed Software if "undisputed amounts remain unpaid more than thirty (30) days after Licensee receives written notice of non-payment."

**Why it matters:** If Zikeiv characterizes a disputed amount as "undisputed" (e.g., by arguing the dispute is not in "good faith" under §6.4), it could suspend the platform. For a solar installer in peak season, a suspension is operationally devastating.

**Recommended fix:** Negotiate a carve-out preventing suspension while a good-faith dispute is pending under §6.4. Alternatively, require 60 days' notice (rather than 30) before suspension and a right to cure by posting the disputed amount in escrow.

---

## ITEMS REQUIRING CLIENT CONFIRMATION (CANNOT RESOLVE FROM DOCUMENTS ALONE)

| # | Question | Why It Matters |
|---|---|---|
| A | Has Stutind **signed** the Side Letter? The signature blocks are blank in the copy provided. | If unsigned, the §12.2 amendment is not effective and the original (more protective) liability framework remains in force. This changes the analysis of Issue 3 entirely. |
| B | Was the Notice of Nonconformity **transmitted** (email sent / courier dispatched) on or before August 17, 2026, even though the letter is dated August 24? | Determines whether D-2 is deemed accepted (Issue 1). |
| C | Does Stutind have any **Affiliates** that currently use or might need to use competing solar design/permitting/proposal software? | Determines the practical impact of the expanded exclusivity (Issue 2). |
| D | Does Stutind currently serve customers in **Canada**? | Determines the practical significance of the data-location issue (Issue 10). |
| E | What is Stutind's **peak season** and how operationally critical is daily platform availability? | Informs the adequacy of service-level protections (Issue 12) and the risk of suspension (Issue 16). |
| F | Has Zikeiv **invoiced** the Milestone 2 fee ($148,000)? | If invoiced, the dispute clock under Agreement §6.4 is running. If not invoiced, Stutind's withholding position in the Notice Letter is precautionary. |

---

## RECOMMENDED NEXT STEPS (Priority Order)

1. **Immediately** confirm with the client the transmission date of the Notice of Nonconformity (Item B above). If late, prepare a follow-up letter and assess waiver/estoppel arguments.
2. **Immediately** confirm whether the Side Letter was signed (Item A above).
3. Prepare a proposed amendment package addressing Issues 2, 3, 4, 5, and 6 for submission to Zikeiv.
4. Calendar the non-renewal notice deadline (October 3 – November 2, 2028) and set internal reminders at 6-month, 3-month, and 1-month intervals.
5. Request from Zikeiv: (a) named subprocessors for DPA Annex 3; (b) confirmation of cyber insurance certificate; (c) written correction plan and target redelivery date for the Module (as requested in the Notice Letter §3.3).