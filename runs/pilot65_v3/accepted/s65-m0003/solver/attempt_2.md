# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Trouvar Therapeutics, Inc. – LairalQMS License: Key Issues and Recommended Actions

---

## 1. Exclusivity Clause Significantly Broader Than Term Sheet

**Where:** Order Form No. 1, § 6.1 (executed); Term Sheet, § 5.1 (January 22, 2026, non-binding).

**Issue.** The Term Sheet contemplated exclusivity limited to "no third-party batch-record software at the Raleigh, North Carolina facility during the Initial Term." The executed Order Form § 6.1 expands this to: (a) any facility worldwide (not just Raleigh); (b) any "manufacturing execution, quality-management or batch-record software" (broader than "batch-record software"); (c) the full Term plus 24 months thereafter (i.e., through March 2031, not just March 2029); and (d) it binds Trouvar's Affiliates. Trouvar also covenants not to "develop" competing software, which could restrict internal R&D.

**Why it matters.** If Trouvar opens a second manufacturing site or wants to pilot a different QMS module (e.g., for a non-sterile product line) during the exclusivity window, it would breach the Order Form. The 24-month tail means the restriction outlives the subscription relationship.

**Recommended fix.** Before Trouvar commits to any additional site or product line, negotiate an amendment to § 6.1 that (a) limits the geographic scope to sites actually licensed under an Order Form, (b) carves out non-GxP or non-sterile product lines, and (c) reduces the post-Term tail to 12 months or eliminates it. At minimum, document internally that the Term Sheet language was not carried through, so the business team understands the constraint.

---

## 2. Phase 1 Dispute Creates Deemed-Acceptance Risk for Phase 2

**Where:** License Agreement § 6.3 (deemed acceptance); SOW No. 2, Recital C (dispute) and § 2.9(e) (Phase 1 rework excluded from SOW No. 2 scope).

**Issue.** Trouvar rejected the Phase 1 Deliverables on October 6, 2026. Lairal disputes the rejection. SOW No. 2 (still in draft) contemplates that Phase 2 validation work will proceed "in parallel" with the Phase 1 dispute (Recital E). However, License Agreement § 6.3 provides that a Deliverable is deemed accepted if Licensee "uses it in the production environment for the release of commercial product, other than for testing or validation purposes." The risk is that if Trouvar's validation team begins OQ or PQ execution using the Phase 1 configuration in the validation environment, and that configuration is later deployed to production (as SOW No. 2 § 2.7 contemplates for cutover), Trouvar could argue it was "testing or validation," but the line is thin. More critically, if any Phase 1 configuration is used in a production batch release before the dispute is resolved, deemed acceptance is triggered and Trouvar loses its rejection right under § 6.3 and its second-rejection termination right under § 6.4.

**Why it matters.** Losing the rejection right means Trouvar may be locked into a nonconforming configuration (electronic batch-record review-by-exception workflow, audit-trail configuration, equipment master data) that could compromise GxP compliance and regulatory posture.

**Recommended fix.** (a) Do not deploy any Phase 1 configuration to the production environment until the dispute is resolved or a written agreement carves out the disputed elements from deemed acceptance. (b) In the final SOW No. 2, add an express provision that use of Phase 1 Deliverables in the validation environment for OQ/PQ purposes does not constitute "use in the production environment" under § 6.3, and that the Phase 1 dispute is preserved and unaffected by Phase 2 activities. (c) Consider escalating the Phase 1 dispute under License Agreement § 17.3 (project manager → senior executive) to resolve it before Phase 2 execution begins.

---

## 3. Quality Agreement Overdue

**Where:** License Agreement § 8.3; Term Sheet § 8.3.

**Issue.** Section 8.3 requires the Parties to "negotiate in good faith and enter into a quality agreement" within 60 days after the Effective Date (March 16, 2026), i.e., by May 15, 2026. No quality agreement appears in the folder. The quality agreement is meant to cover change control, deviation management, incident management and supplier audit arrangements.

**Why it matters.** Without an executed quality agreement, there is no agreed framework for how the Parties will handle GxP-critical events (e.g., a configuration change that affects the validated state, a deviation discovered during validation, or a supplier audit finding). This creates ambiguity during exactly the period (Phase 2 validation) when such events are most likely. It also weakens Trouvar's position if a Regulatory Authority asks how the supplier relationship is governed from a quality standpoint.

**Recommended fix.** Treat execution of the quality agreement as a precondition to finalizing SOW No. 2. If Lairal resists, at minimum document in writing that Trouvar has repeatedly requested the quality agreement and that its absence is a material gap in GxP governance.

---

## 4. Liability Cap Applies to the Kessmont Guaranty

**Where:** License Agreement § 12.2 (cap); Kessmont Parent Guaranty § 2.5 (extent of liability).

**Issue.** Section 12.2 caps each Party's aggregate liability at "the fees paid or payable in the 12 months preceding the claim" (approximately $1.24M for the subscription, plus any SOW fees). Guaranty § 2.5 expressly provides that "any limitation or exclusion of Licensor's liability under Section 12 of the License Agreement applies to the Guarantor's liability for the corresponding Guaranteed Obligation to the same extent." So Kessmont's guarantee is subject to the same cap.

**Why it matters.** If Lairal suffers a data loss, security breach, or chronic service failure that causes Trouvar to incur regulatory fines, product recall costs, or lost production, Trouvar's recovery from either Lairal or Kessmont is capped at roughly $1.24M (plus SOW fees). For a sterile injectables manufacturer, a single FDA 483 observation or product recall could cost multiples of that. The carve-outs in § 12.3 (confidentiality/data security breach, gross negligence, fraud, willful misconduct) help but are fact-specific and may not cover all scenarios (e.g., ordinary negligence in hosting that causes data corruption is not clearly carved out unless it rises to the level of a § 10 breach).

**Recommended fix.** (a) Ensure Trouvar's own cyber and product liability insurance covers the gap. (b) If Trouvar has leverage (e.g., during SOW No. 2 negotiation), seek to raise the cap for data-loss and GxP-compliance failures to at least 2× or 3× annual fees, or to an uncapped amount for § 12.4 (data restoration) obligations. (c) Confirm that the § 12.3(b) carve-out for "breach of Section 10" is broad enough to cover a hosting failure that results in data loss (it should, given that § 10.5–10.8 address data ownership, security and incidents, but the point should be confirmed in writing).

---

## 5. SOW No. 2 Assumptions at Risk Due to Phase 1 Dispute

**Where:** SOW No. 2 § 11.1 (assumptions), particularly (d) and (e); § 11.2 (variance).

**Issue.** SOW No. 2's fixed fees of $380,000 and target schedule assume: (d) the go-live version will match the validation-environment version with only patch-level updates during execution; and (e) Licensor personnel will be on site for no more than 40 person-days. If resolving the Phase 1 dispute requires reconfiguration of the batch-record workflow or audit-trail settings (the specific nonconformities Trouvar identified), the version deployed at go-live may differ materially from the version in the validation environment, violating assumption (d). Additional on-site time for rework would violate assumption (e). Under § 11.2, either Party may then submit a change request, which could increase fees and delay the schedule.

**Why it matters.** Trouvar has budgeted $380,000 for Phase 2. If the Phase 1 dispute triggers change orders, costs could escalate and the go-live timeline could slip, with knock-on effects for Trouvar's manufacturing schedule and regulatory commitments.

**Recommended fix.** (a) Resolve the Phase 1 dispute before executing SOW No. 2, so that the validation-environment configuration is stable. (b) If the Parties proceed in parallel as contemplated, add a provision to SOW No. 2 that configuration corrections arising from the Phase 1 dispute will be performed at no additional charge and will not count against the 40 person-day assumption, because they are Lairal's responsibility under SOW No. 1. (c) Cap the total fee exposure for Phase 2 (e.g., no more than 10% above $380,000 without Trouvar's written approval).

---

## 6. Storage Limit May Be Insufficient

**Where:** Order Form No. 1 § 7.5.

**Issue.** The Annual Subscription Fee includes only 5 TB of storage for Licensee Data. Additional storage is $4,800 per TB per Subscription Year, but only if Trouvar agrees in writing. For a sterile injectables manufacturer generating electronic batch records, audit trails, deviation records, CAPA documentation and training records for 240 execution users, 95 reviewers/approvers and 75 read-only users, 5 TB may be reached within the first year or two, depending on record volume and retention requirements.

**Why it matters.** If storage is exhausted and Trouvar has not agreed to additional storage in writing, Licensor could argue it is not obligated to accept further data, which would disrupt batch record creation and GxP compliance.

**Recommended fix.** (a) Conduct an internal data-volume assessment now, using historical paper-batch-record volumes as a proxy, to project storage needs over the 3-year Initial Term. (b) If the projection exceeds 5 TB, negotiate an increase in included storage (or a pre-agreed additional allocation) as part of the SOW No. 2 or a side letter, so that the "agreement in writing" requirement in § 7.5 is satisfied in advance. (c) Add a provision that Licensor will not reject or suspend data ingestion due to storage limits without 60 days' prior written notice.

---

## 7. Confidentiality Duration: NDA vs. License Agreement

**Where:** NDA § 10.2(b) (Trouvar's batch records protected "as long as that information remains confidential"); License Agreement § 10.11 (5-year tail, except trade secrets and Licensee Data "for as long as that information remains a trade secret or is held by the Recipient").

**Issue.** The NDA provides perpetual protection for Trouvar's batch records, manufacturing processes, product formulations and regulatory submissions. The License Agreement's § 10.11 provides a 5-year general tail, with a longer period only for trade secrets and Licensee Data "as long as … held by the Recipient." Once Licensor deletes Licensee Data under § 14.6 (90 days post-termination), the "as long as held" qualifier ends, and the 5-year clock governs. If the 5-year period expires before Trouvar's GxP record retention obligations are satisfied (which for sterile injectables can be product shelf life plus one year, or longer under FDA expectations), there is a gap.

**Why it matters.** If Lairal retains any copies of Trouvar's Confidential Information (e.g., in backup systems under § 10.10(b)) beyond the 5-year tail, the contractual protection weakens. In a regulatory inspection, Trouvar would want to be able to demand that Lairal maintain confidentiality of its records indefinitely.

**Recommended fix.** Add a sentence to § 10.11 (or confirm in the quality agreement) that obligations with respect to Licensee Data that constitutes GxP records continue for so long as Licensee is required to retain those records under applicable law or Regulatory Authority expectation, regardless of whether Licensor still holds them. This aligns the License Agreement with the NDA's stronger standard for batch records.

---

## 8. Minor / Administrative Items

| # | Issue | Where | Fix |
|---|-------|-------|-----|
| 8a | SOW No. 2 is unsigned and in draft. Trouvar should not begin any Phase 2 activities (including protocol review) until it is executed, to avoid creating course-of-dealing expectations. | SOW No. 2, header | Hold all Phase 2 work until execution. |
| 8b | Order Form § 6.4 gives a one-time $12,400 early-payment credit if Subscription Year 1 is paid within 15 days. Confirm whether Trouvar took advantage of this; if not, the window has passed. | Order Form No. 1 § 6.4 | Verify with AP. |
| 8c | The Wilmington lease permits "quality management functions" at the Suite 1800 premises (§ 7.1). Ensure that any on-site validation activities or quality-unit work related to the LairalQMS implementation are conducted within that scope and do not drift into "manufacturing" or "compounding" (prohibited). | Lease § 7.1 | Brief the quality team on permitted use. |
| 8d | License Agreement § 17.14 (non-solicitation) runs for 12 months after completion of each SOW. If the Phase 1 dispute delays SOW No. 1 "completion," the non-solicitation period for Phase 1 personnel may still be running. | License Agreement § 17.14 | Track SOW completion dates; do not solicit Lairal project staff until the period has clearly expired. |

---

## Priority Actions (Next 30 Days)

1. **Escalate Phase 1 dispute** under § 17.3 to senior executives. Do not allow production use of disputed configuration.
2. **Demand the quality agreement** in writing; make it a condition to executing SOW No. 2.
3. **Circulate SOW No. 2 redlines** addressing items 2, 5 and the deemed-acceptance carve-out.
4. **Run storage-volume assessment** and pre-negotiate additional TB allocation.
5. **Confirm insurance coverage** (cyber, product liability) is adequate to bridge the liability-cap gap.