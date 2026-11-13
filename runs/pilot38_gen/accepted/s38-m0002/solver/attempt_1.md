# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Binond Releasing LLC / Favaiv Digital Cinema Services – Review of Supply Agreement, DPA, SOW No. 1 and Mutual NDA

---

## Executive Summary

The document set contains several material issues that expose Binond to significant financial and operational risk. The three most urgent are: (1) a DPA indemnification clause that makes Binond liable for data-protection losses even when Favaiv caused them; (2) a direct governing-law conflict between SOW No. 1 and the Supply Agreement; and (3) a worldwide exclusivity obligation that is already in effect while terms for most of the required services remain unset. Details and proposed fixes follow, in order of significance.

---

## Issue 1 – DPA Indemnification Shifts Fault to Binond

**Where:** Data Processing Addendum, Section 9.1.

**The problem.** Section 9.1 provides:

> "Customer shall defend, indemnify and hold harmless Supplier and its Affiliates, officers, employees and agents from and against all Losses arising out of or relating to any third-party claim, regulatory investigation, fine or penalty, or Data Subject action relating to Customer Personal Data or its Processing under the Agreement, **regardless of whether caused in part by Supplier**."

The italicized language means Binond must indemnify Favaiv for data-protection losses even where Favaiv's own negligence or breach caused the loss. This directly contradicts the architecture of the Supply Agreement, where Section 12.1(b) has Supplier indemnify Customer for unauthorized access to or disclosure of Customer Materials, and Section 13.3(a) carves indemnification obligations out of the liability cap. Because the DPA takes precedence over the Agreement for personal-data matters (Supply Agreement § 2.3(a)), this clause would likely override § 12.1(b) in any data-protection dispute.

**Why it matters.** Favaiv operates the screener platform, holds viewer credentials, IP addresses, and forensic watermark logs (DPA Annex A). A breach of that platform—say, a leak of unreleased screener files tied to identifiable recipients—would trigger regulatory exposure (CCPA, potentially GDPR for international festival attendees) and class-action risk. Under the current drafting, Binond would be on the hook for Favaiv's share of that liability.

**Recommended fix.** Delete "regardless of whether caused in part by Supplier" and replace Section 9.1 with fault-based language:

> "9.1 **By Customer.** Customer shall defend, indemnify and hold harmless Supplier and its Affiliates, officers, employees and agents from and against all Losses arising out of or relating to any third-party claim, regulatory investigation, fine or penalty, or Data Subject action relating to Customer Personal Data or its Processing under the Agreement, to the extent caused by (a) Customer's instructions to Supplier that violate Data Protection Laws, or (b) Customer's failure to obtain required consents or provide required notices to Data Subjects.
>
> 9.2 **By Supplier.** Supplier shall defend, indemnify and hold harmless Customer and its Affiliates, officers, employees and agents from and against all Losses arising out of or relating to any third-party claim, regulatory investigation, fine or penalty, or Data Subject action relating to Customer Personal Data or its Processing under the Agreement, to the extent caused by (a) Supplier's breach of this DPA or Section 7 of the Agreement, (b) a Personal Data Breach resulting from Supplier's failure to maintain the security measures in Annex B, or (c) the acts or omissions of any Sub-processor.
>
> 9.3 **Procedure.** Section 12.3 of the Agreement applies to claims under this Section 9."

This mirrors the supply-side indemnity in Agreement § 12.1 and allocates risk to the party in control of the failure.

**Flag for business decision:** If Favaiv resists a full fault-based split, the minimum acceptable position is to delete "regardless of whether caused in part by Supplier" and insert "to the extent not caused by Supplier's breach of this DPA or the Agreement." Anything less leaves Binond bearing Favaiv's regulatory risk.

---

## Issue 2 – Governing Law and Forum Conflict (SOW No. 1 vs. Supply Agreement)

**Where:** SOW No. 1, Sections 9.1–9.2 (New York law; New York County courts) vs. Supply Agreement, Sections 19.1–19.2 (Delaware law; New Castle County courts).

**The problem.** The two documents specify different governing laws and different exclusive forums. Under the Supply Agreement's order of precedence (§ 2.3(b)), the SOW controls "as to the Services, Deliverables and any matters arising under that SOW." A dispute over a missed DCP delivery deadline, a quality-conformance claim, or a fee disagreement under SOW No. 1 would therefore be governed by New York law and litigated in New York County—while a dispute over content security, confidentiality, or the exclusivity obligation would fall under Delaware law in New Castle County.

**Why it matters.** This creates (a) uncertainty about which law applies to mixed claims, (b) the possibility of parallel or sequential proceedings in two jurisdictions, and (c) a tactical advantage to Favaiv, which can argue that SOW-specific disputes (where Binond is most likely to be the claimant—e.g., late delivery, defective DCP) are governed by New York law, which may differ from Delaware on issues like consequential damages, the economic loss rule, or the enforceability of liquidated damages.

**Recommended fix.** Conform SOW No. 1 § 9 to the Agreement:

> "9.1 This SOW is governed by and construed in accordance with the laws of the State of Delaware, without regard to its conflict of laws principles.
>
> 9.2 Each Party irrevocably submits to the exclusive jurisdiction of the state and federal courts located in New Castle County, Delaware for any action arising under or relating to this SOW, and waives any objection to venue in those courts."

Alternatively, if the New York forum was negotiated deliberately (e.g., Favaiv's mastering facility is in New York), the fix should go the other way: amend Agreement § 19 to New York. But given that Binond is a Delaware LLC and the NDA is also Delaware-law, the cleaner solution is to conform the SOW to Delaware.

**Flag for business decision:** Confirm with the client whether the New York forum in SOW No. 1 was a conscious choice or a drafting carry-over from a Favaiv template. If it was negotiated, understand the rationale before we push to change it.

---

## Issue 3 – Worldwide Exclusivity with Most Services Unpriced

**Where:** Supply Agreement, Sections 1.6, 1.12, and 3.1; SOW No. 1, Section 2.3.

**The problem.** Section 3.1 obligates Binond to procure **all** Distribution Deliverables **exclusively** from Favaiv **throughout the Territory** (defined as "the entire world" in § 1.12) during the Term. "Distribution Deliverables" (§ 1.6) is defined to sweep in theatrical, home entertainment, streaming/VOD, broadcast, cable, airline, and festival deliverables, plus all related mastering, encoding, conforming, packaging, duplication, encryption, and screener services.

Yet SOW No. 1 covers only US/Canada theatrical DCP mastering. Section 2.3 of the SOW expressly excludes KDM generation, drive duplication and shipping, secure watermarked screeners, and all non-theatrical deliverables. No SOWs for those services are in the folder.

**Why it matters.** The exclusivity obligation is effective from the March 2, 2026 Effective Date. That means from day one, Binond cannot use any other vendor for a European festival deliverable, a streaming encode, a drive duplication run, or a screener platform—even though the pricing, SLAs, and specifications for those services have not been agreed. If Favaiv's terms for those services are unfavorable, or if Favaiv lacks capability in a particular format or region, Binond is contractually locked in. The three-year Initial Term plus auto-renewal (§ 4.2) extends this lock-in potentially well beyond five years.

**Recommended fix (drafting):** Add a "most-favored-customer" or "reasonable terms" backstop to Section 3.1:

> "3.1 **Exclusive Supply.** Notwithstanding anything in any SOW, Customer shall procure all Distribution Deliverables exclusively from Supplier throughout the Territory during the Term; **provided that** (a) Supplier shall make such Distribution Deliverables available on terms (including fees, turnaround times and specifications) that are no less favorable than those Supplier offers to similarly situated customers, and (b) if the Parties are unable to agree on the terms of a new SOW for a category of Distribution Deliverables within thirty (30) days after Customer's written request, Customer may procure that category from a third party for so long as the impasse continues, without breach of this Section 3.1."

**Flag for business decision:** The client needs to decide how much exclusivity it is willing to grant. Options, in order of increasing flexibility for Binond:

- **Option A (current):** Full worldwide exclusivity for all Distribution Deliverables. Highest leverage for Favaiv; greatest risk for Binond.
- **Option B (recommended):** Exclusivity limited to the US and Canada (matching SOW No. 1's geographic scope), with the proviso above.
- **Option C:** Exclusivity only for theatrical DCP mastering in the US and Canada, with all other services on a non-exclusive basis.

The client should also confirm whether Favaiv actually has the capability and facilities to serve worldwide (particularly for non-theatrical formats and international territories) before accepting the current scope.

---

## Issue 4 – Consequential Damages Exclusion for Delivery Failures

**Where:** Supply Agreement, Sections 13.1 and 13.3.

**The problem.** Section 13.1 excludes all indirect, incidental, special, consequential, or punitive damages and loss of profits or revenue. Section 13.3 carves out of this exclusion only: (a) indemnification obligations; (b) breach of confidentiality (§ 9); (c) Supplier's breach of content security (§ 7); (d) gross negligence, fraud, or willful misconduct; and (e) payment of undisputed fees.

A failure to deliver a DCP on time for a theatrical release is none of these. It is a breach of the SOW delivery schedule (§ 5.2 of the Agreement; § 4.3 of SOW No. 1), but it is not a § 7 content-security breach. Therefore, if Favaiv misses a release date and Binond loses first-weekend box office, that loss is consequential and excluded. Binond's recovery is limited to direct damages (e.g., the cost of re-mastering elsewhere, if the exclusivity clause even permits it) subject to the § 13.2 cap.

**Why it matters.** For a film distributor, the single most expensive failure mode is a missed or delayed theatrical release. The current drafting means Binond bears that risk.

**Recommended fix.** Add a new carve-out to Section 13.3:

> "(f) Supplier's failure to deliver a Deliverable by the date specified in the applicable SOW where the SOW identifies a release, festival or screening date, in which case Customer's recovery shall include the documented, direct costs incurred as a result of the delay (including expedited re-mastering costs, additional marketing spend, and lost distribution window revenue to the extent such revenue is reasonably quantifiable)."

Alternatively, if Favaiv resists opening the consequential-damages exclusion, negotiate a **liquidated damages** provision in each SOW for missed release dates (e.g., a specified percentage of the mastering fee per day of delay, up to a stated maximum). Liquidated damages are direct damages and would not be caught by § 13.1.

**Flag for business decision:** The client should quantify its typical exposure to a missed release (lost box office, contractual penalties to exhibitors, re-marketing costs) so we can calibrate the liquidated damages figure or the scope of the carve-out.

---

## Issue 5 – Liability Cap Is Low in Early Years

**Where:** Supply Agreement, Section 13.2.

**The problem.** The cap is "Fees paid or payable by Customer under this Agreement in the twelve (12) months preceding the event giving rise to the claim." In the first year, if Binond orders, say, ten DCP masters at $4,850 each (SOW No. 1 § 5.1) plus a few VFs, total fees might be $60,000–$80,000. That is the cap for any non-carved-out claim. A single significant operational failure (e.g., corrupted archive, lost content keys that are not a § 7 "security" issue but a data-integrity issue) could cause losses far exceeding that amount.

**Why it matters.** The cap grows with spend, so it becomes less problematic over time. But in years one and two, when Binond is most dependent on Favaiv establishing reliable workflows, the cap provides thin protection.

**Recommended fix.** Raise the floor:

> "13.2 **Cap.** Except as provided in Section 13.3, each Party's total aggregate liability arising out of or relating to this Agreement shall not exceed the greater of (a) the Fees paid or payable by Customer under this Agreement in the twelve (12) months preceding the event giving rise to the claim, or (b) **$1,000,000**."

**Flag for business decision:** The $1M floor is a starting point. The client should consider what a worst-case non-security, non-data failure would cost and set the floor accordingly.

---

## Issue 6 – Sub-Processors Not Identified

**Where:** Data Processing Addendum, Annex C.

**The problem.** Annex C lists sub-processors as "Cloud hosting provider (as notified to Customer in writing)" and "Transactional email provider (as notified to Customer in writing)." Neither is named. Binond is authorizing Favaiv to process screener viewer data (names, emails, IP addresses, device identifiers, viewing logs—Annex A) through unidentified third parties.

**Why it matters.** Without knowing the sub-processors, Binond cannot assess their security posture, data residency, or compliance history. If a sub-processor is a major cloud provider (AWS, Azure) the risk is manageable; if it is an unknown entity, the risk is not. The "as notified" language suggests Favaiv will identify them later, but Binond is granting authorization now, in the dark.

**Recommended fix.** Require Favaiv to populate Annex C with named sub-processors before the DPA is executed, or add:

> "Supplier shall not engage any Sub-processor until it has identified that Sub-processor to Customer in writing and Customer has had a reasonable opportunity to assess the Sub-processor's data protection measures. The authorization in Section 6.1 is conditional on such prior identification."

**Flag for business decision:** If Favaiv says it will name the sub-processors "soon," the client should decide whether to sign the DPA with placeholders or hold execution until names are provided. Given that the DPA takes precedence over the Agreement for personal-data matters (§ 2.3(a)), signing with unknown sub-processors is a real risk.

---

## Issue 7 – Deemed Acceptance After 10 Business Days

**Where:** Supply Agreement, Section 5.3.

**The problem.** A Deliverable is deemed accepted when the 10-business-day inspection period expires without a notice of non-conformity. For DCPs, this means Binond has 10 business days after delivery to spot encoding errors, audio issues, subtitle timing problems, or packaging defects. If the DCP is delivered 7 business days before release (the standard turnaround in SOW No. 1 § 4.3), Binond has only 7 business days to inspect—and the release is imminent. In practice, the inspection window may close before the DCP has even been loaded on a projection server in a theater.

**Why it matters.** Once a DCP is "accepted" (even by deemed acceptance), the 90-day conformance warranty in § 11.2(b) starts running, and Binond's ability to reject or demand correction is weakened. A latent defect discovered after acceptance but before the theatrical release could be costly to fix.

**Recommended fix.** Add a provision to SOW No. 1 (or amend Agreement § 5.3):

> "Notwithstanding Section 5.3 of the Agreement, for any DCP delivered in connection with a theatrical release, the inspection period shall not expire until five (5) business days after the scheduled opening date of the release, provided that Customer shall use commercially reasonable efforts to complete inspection before that date."

---

## Issue 8 – Auto-Renewal with 90-Day Notice

**Where:** Supply Agreement, Section 4.2.

**The problem.** The Agreement renews automatically for successive one-year terms unless either party gives written notice of non-renewal at least 90 days before the end of the then-current term. Combined with the exclusivity obligation (§ 3.1), a missed 90-day window locks Binond in for another year of exclusive dealing with Favaiv at whatever fees Favaiv sets (subject to the 3% annual increase in SOW No. 1 § 5.4).

**Why it matters.** This is a common trap in supply agreements. The 90-day notice period means Binond must decide by approximately December 1 (for a March 2 year-end) whether to renew. If the client's release slate is not finalized that far in advance, it may renew by default.

**Recommended fix (drafting):** Shorten the notice period to 60 days, or add a "for convenience" termination right:

> "4.7 **Termination for Convenience.** Either Party may terminate this Agreement or any SOW for convenience on ninety (90) days' written notice, provided that Customer pays for all Services properly performed and Deliverables accepted through the effective date of termination."

**Flag for business decision:** The client should decide whether it wants a for-convenience exit. Favaiv will likely resist, given that the exclusivity is its primary commercial benefit. If a for-convenience right is off the table, at minimum calendar the 90-day non-renewal deadline and build it into the client's annual planning cycle.

---

## Issue 9 – SOW No. 1 Excludes Critical Services with No Fallback Terms

**Where:** SOW No. 1, Section 2.3.

**The problem.** KDM generation, drive duplication and shipping, secure watermarked screeners, and all non-theatrical deliverables are excluded from SOW No. 1. The Agreement's exclusivity clause (§ 3.1) requires Binond to source all of these from Favaiv, but no SOWs setting out the terms for those services are in the folder.

**Why it matters.** Binond is bound to use Favaiv for these services but has no agreed pricing, SLAs, security specifications, or delivery timelines. In a dispute, Favaiv could argue that the absence of a SOW means the service is not yet "ordered" and is not subject to the Agreement's performance standards.

**Recommended fix.** Before the Effective Date (or as a condition to it), require Favaiv to deliver draft SOWs for at minimum: (a) KDM generation and distribution; (b) drive duplication and shipping; and (c) secure watermarked digital screeners. Add to the Agreement:

> "3.4 **Pending SOWs.** The Parties shall negotiate in good faith and execute SOWs for the categories of Distribution Deliverables excluded from SOW No. 1 within sixty (60) days after the Effective Date. Until such SOWs are executed, Supplier shall provide those services on terms no less favorable than those set out in SOW No. 1, adjusted for the nature of the service."

---

## Issue 10 – NDA Term Shorter than Agreement Term

**Where:** Mutual NDA, Section 9.1 (2-year term from November 17, 2025, expiring November 17, 2027) vs. Supply Agreement, Section 4.1 (3-year Initial Term from March 2, 2026, expiring March 2, 2029).

**The problem.** The NDA will expire roughly 16 months before the Agreement's Initial Term ends. Supply Agreement § 9.5 preserves the NDA for pre-Effective-Date information, and NDA § 9.2 provides a 5-year post-term tail on obligations. So the practical effect is limited: pre-agreement information remains protected until November 2032. However, the NDA's specific protections for content (e.g., § 2.4's restriction on copying, screening, transcoding, or encoding picture materials) will no longer apply after the NDA term expires, even though the Agreement's § 9 confidentiality clause is broader in some respects but does not contain the same specific content-handling restrictions.

**Why it matters.** Low risk in practice, because the Agreement's § 9 and § 7 provide overlapping protection during the Agreement term. But if the relationship ends and the NDA has already expired, there is a gap for pre-Effective-Date information between the NDA's 5-year tail and any residual Agreement obligations.

**Recommended fix.** Extend the NDA term to match the Agreement, or add to NDA § 9.1:

> "This NDA shall remain in effect for so long as the Supply Agreement between the Parties dated March 2, 2026 (as amended) remains in force, and in any event for no less than two (2) years from the NDA Effective Date."

This is a low-priority fix but easy to include in the next amendment cycle.

---

## Items Incomplete or Missing from the Folder

1. **No SOWs for KDMs, drive duplication, screeners, or non-theatrical deliverables.** As noted in Issue 9, these are required by the exclusivity clause but have no agreed terms. I need these drafts from Favaiv (or we need to request them) before the client can make an informed decision on the overall package.

2. **No Title Order form or template.** SOW No. 1 § 4.1 references "Title Orders" as the mechanism for ordering individual DCP masters, but no form is provided. We should request one to confirm that the order mechanism captures all necessary variables (resolution, versions, release date, special requirements) and that it does not inadvertently modify SOW terms.

3. **No evidence of Favaiv's content security assessment.** SOW No. 1 § 7.3 requires Favaiv to "provide Customer with a summary of its most recent independent content security assessment on request." We should make that request now, before signing, so the client can evaluate Favaiv's actual security posture.

4. **Sub-processor identities.** See Issue 6. We need the names before the DPA is executed.

5. **Favaiv's corporate details.** The Agreement identifies Favaiv as "a corporation" without stating its state of incorporation. This is a minor point but should be corrected for precision (and to confirm it is a valid entity in good standing).

---

## Summary Table

| # | Issue | Document / Section | Severity | Type |
|---|-------|-------------------|----------|------|
| 1 | Customer indemnifies Supplier for data losses regardless of fault | DPA § 9.1 | **Critical** | Drafting |
| 2 | Governing law conflict (NY vs. DE) | SOW No. 1 § 9; Agreement § 19 | **High** | Drafting |
| 3 | Worldwide exclusivity with most services unpriced | Agreement § 3.1; SOW No. 1 § 2.3 | **High** | Business + Drafting |
| 4 | Consequential damages excluded for missed release dates | Agreement § 13.1, 13.3 | **High** | Drafting / Business |
| 5 | Liability cap very low in early years | Agreement § 13.2 | **Moderate** | Drafting |
| 6 | Sub-processors not named | DPA Annex C | **Moderate** | Business + Drafting |
| 7 | Deemed acceptance may close before practical inspection | Agreement § 5.3 | **Moderate** | Drafting |
| 8 | Auto-renewal with 90-day notice | Agreement § 4.2 | **Moderate** | Business |
| 9 | No SOWs for excluded critical services | SOW No. 1 § 2.3 | **High** | Business + Drafting |
| 10 | NDA term shorter than Agreement term | NDA § 9.1 | **Low** | Drafting |

---

## Recommended Next Steps

1. **Before the client decides whether to sign:** Resolve Issues 1, 2, 3, and 9. These go to the fundamental risk allocation and scope of the relationship.
2. **Request from Favaiv:** Named sub-processors; draft SOWs for KDMs, duplication, and screeners; most recent content security assessment summary; Title Order template.
3. **Client business decisions needed:** Exclusivity scope (Option A/B/C from Issue 3); willingness to accept auto-renewal or require a for-convenience exit (Issue 8); quantification of missed-release exposure to calibrate the consequential-damages fix (Issue 4); whether to hold DPA execution until sub-processors are named (Issue 6).
4. **Drafting package:** I can prepare a redline of the Agreement, DPA, and SOW No. 1 incorporating the fixes above once the client confirms its position on the business-decision items.