# MEMORANDUM

**To:** Partner
**From:** Associate
**Date:** [Current Date]
**Re:** Pakairt Outdoor Apparel, Inc. – Sairan Threadline License: Issue Identification and Recommendations

---

## Executive Summary

Pakairt has signed a five-year, $1.14M-per-year license for Sairan's Threadline PLM platform and, on May 4, 2026, exercised its right to elect out of the Phase 2 (wholesale and retail) modules, reducing the annual fee to $855,000. The transaction documents are generally well-drafted, but I have identified ten issues that range from critical to moderate. The most urgent is a structural conflict between the exclusivity covenant and the Phase 2 Election that, as the documents currently read, places Pakairt in automatic breach the moment it uses any other system for wholesale order management or retail merchandising.

---

## Issue 1 – Exclusivity Covenant Is Inconsistent with the Phase 2 Election

**Documents and Sections:**
- Software License Agreement, § 2.5
- SOW, § 1.2 (definition of "Covered Functions")
- Side Letter, § 3.4 (effect of Phase 2 Election)
- Agreement, § 1.4 (order of precedence)

**Explanation:**
Section 2.5 of the Agreement provides: "During the Term, Licensee shall use the Licensed Software as its exclusive solution for the Covered Functions. Licensee shall not, and shall cause its Affiliates not to, license, develop or use any other software that performs any Covered Function."

The SOW (§ 1.2) defines "Covered Functions" to include, among others, "(c) wholesale order management" and "(d) retail point-of-sale and e-commerce merchandising."

The Side Letter (§ 3.4) provides that upon a valid Phase 2 Election, "the licenses to the Phase 2 Modules under Section 2.2 of the SOW shall not take effect." It does not amend, qualify, or carve out the exclusivity obligation in § 2.5.

Because the Side Letter ranks first in the order of precedence (Agreement § 1.4), it governs over the Agreement where they conflict. But the Side Letter is silent on § 2.5. Silence is not a conflict—the Side Letter simply does not address the exclusivity covenant. As a result, the full text of § 2.5 remains in force.

Pakairt delivered its Phase 2 Election notice on May 4, 2026 (Notice Letter, ¶ 2). From that date, it no longer holds licenses to the wholesale or retail modules. Yet § 2.5 still prohibits it from "licens[ing], develop[ing] or us[ing] any other software that performs" wholesale order management or retail POS/e-commerce merchandising. Pakairt must use *some* system for those functions. Any such use is a breach of § 2.5.

This is not a theoretical risk. Pakairt is an outdoor apparel company that sells through wholesale and retail channels. It will inevitably use other tools for those functions. Each day it does so after May 4, 2026, it is in continuing breach, exposing it to Sairan's termination right under § 12.3(a) (material breach, 30-day cure) and potentially to a damages claim (subject to the § 10.1 cap).

**Recommendation:**
Amend the Side Letter (or execute a short amendment to the Agreement) to provide that, following a valid Phase 2 Election, § 2.5 applies only to Covered Functions for which Licensee holds an active module license under the SOW. Alternatively, redefine "Covered Functions" in the Side Letter to exclude the Phase 2 functions upon election. This should be done before Pakairt's next wholesale season or retail planning cycle to avoid any gap in compliance.

---

## Issue 2 – Renewal Term Is 60 Months, Not 12 Months

**Documents and Sections:**
- Term Sheet, § 7.2
- Agreement, § 12.2
- SOW, § 4.1 (Order Term = 60 months)

**Explanation:**
The Term Sheet (§ 7.2) stated: "After the initial term, the license will continue for successive **12-month** renewal terms, unless either party gives notice of non-renewal before the end of the then-current term."

The final Agreement (§ 12.2) provides: "this Agreement shall renew automatically for successive renewal terms, each equal in length to the **Order Term** (each a 'Renewal Term')." The Order Term is 60 months (SOW § 4.1).

The Term Sheet is non-binding (Term Sheet § 15.1), so it cannot be enforced. But the discrepancy is material: the Term Sheet gave Pakairt an annual exit opportunity; the Agreement locks it in for five years at a time. The non-renewal notice window is narrow—only 30 days, opening 120 days before term expiry (Agreement § 12.2). If Pakairt misses that window, it is committed for another 60 months at a fee that can increase up to 3% per year (SOW § 4.3).

**Recommendation:**
This is now baked into a signed agreement and cannot be unilaterally fixed. Going forward, Pakairt should:
1. Calendar the non-renewal notice deadline (120 days before the end of the Initial Term, i.e., approximately 120 days before the Phase 1 Acceptance Date + 60 months = roughly September 2031).
2. In any future SOW or amendment, negotiate to shorten the Renewal Term to 12 months or to add a mid-term break right.
3. Consider whether the 60-month Renewal Term, combined with the fee-escalation right, makes the long-term cost of the license materially higher than the Term Sheet contemplated, and factor this into any business case for continued use.

---

## Issue 3 – Asymmetric Assignment Rights

**Documents and Sections:**
- Agreement, § 15.2 (Licensee assignment)
- Agreement, § 15.3 (Licensor assignment)

**Explanation:**
Section 15.2 prohibits Pakairt from assigning the Agreement without Sairan's prior written consent. Section 15.3 permits Sairan to assign "in whole or in part, to any person without Licensee's consent," subject only to 30 days' after-the-fact notice.

This means Sairan could sell the business, merge with a competitor, or transfer the contract to an affiliate or acquirer, and Pakairt would have no veto. Pakairt's only protections are the confidentiality and data-protection covenants, which bind successors under § 15.4, and the insurance requirements, which also bind successors. But if Sairan is acquired by a company with a weaker security posture, fewer resources, or a history of data breaches, Pakairt is stuck.

Conversely, if Pakairt undergoes a corporate reorganization, merger, or change of control, it cannot assign the Agreement without Sairan's consent—giving Sairan leverage in any such transaction.

**Recommendation:**
Negotiate an amendment to § 15.3 to require Sairan to obtain Pakairt's consent (not to be unreasonably withheld) before assigning to a direct competitor of Pakairt or to an entity that does not assume Sairan's obligations in writing. At minimum, add a provision that permits Pakairt to terminate without penalty if Sairan assigns to a party whose security posture (as evidenced by SOC 2 or equivalent) is materially inferior.

---

## Issue 4 – No Data Protection Indemnity from Sairan

**Documents and Sections:**
- DPA, § 9 (Customer indemnifies Processor)
- Agreement, § 9.1 (IP indemnity only)
- Agreement, § 9.4 (Licensee indemnifies for Customer Data)
- Agreement, § 10.1 (liability cap)

**Explanation:**
The DPA contains a one-way indemnity: Section 9 requires *Pakairt* to indemnify *Sairan* for losses arising from (a) Processing in accordance with Pakairt's instructions, or (b) Pakairt's failure to provide notices or obtain consents from Data Subjects. There is no reciprocal provision requiring Sairan to indemnify Pakairt for losses arising from Sairan's own breach of the DPA (e.g., a security incident caused by Sairan's failure to maintain the Annex 2 measures).

The Agreement's general indemnity (§ 9.1) covers only third-party IP infringement claims. Section 9.4 has Pakairt indemnifying Sairan for Customer Data claims. So the net effect is:

- If Sairan suffers a security breach through its own negligence and a regulator or class of consumers sues Pakairt (as the CCPA "business"), Pakairt's remedy against Sairan is a breach-of-contract claim subject to the § 10.1 cap (12 months' fees ≈ $855,000 post-election) and the § 10.2 exclusion of indirect damages (which could exclude regulatory fines and consumer damages as "consequential").
- The § 10.3 carve-outs (indemnification obligations, confidentiality breach, gross negligence/wilful misconduct, payment) do not clearly cover a simple DPA breach by Sairan that is not grossly negligent.

This leaves Pakairt potentially bearing the full cost of a Sairan-caused data incident, capped at ~$855K, while Sairan is indemnified by Pakairt for its own compliant Processing.

**Recommendation:**
Add a reciprocal indemnity in the DPA: Sairan shall indemnify Pakairt against losses, regulatory fines, and third-party claims arising from Sairan's breach of the DPA (other than breach caused by Pakairt's instructions or failure to obtain consents). Clarify in § 10.3 that this indemnity is carved out from the cap and the indirect-damages exclusion, consistent with how the IP indemnity is treated.

---

## Issue 5 – Liability Cap May Be Inadequate for a Data-Centric Platform

**Documents and Sections:**
- Agreement, § 10.1 (cap = 12 months' fees)
- Agreement, § 10.2 (indirect damages excluded)
- Agreement, § 10.3 (carve-outs)
- SOW, § 4.2 / Side Letter, § 3.2 (Annual License Fee = $855,000 post-election)

**Explanation:**
The cap is the fees "paid or payable in the 12 months preceding the claim." Post-election, that is $855,000. The carve-outs in § 10.3 preserve uncapped liability for: indemnification obligations, confidentiality breaches, gross negligence/wilful misconduct, and payment obligations.

However, the following scenarios fall *within* the cap:
- Sairan's failure to meet service levels resulting in lost business (e.g., a multi-day outage during a critical ordering window). The service credits (max 35% of Monthly Fee per month, per SLS § 4.3) are the primary remedy, and any additional damages would be capped and potentially excluded as indirect.
- Loss or corruption of Customer Data that does not rise to the level of a "Security Incident" under the DPA (e.g., a software bug that overwrites tech packs). This would be a warranty breach (§ 8.2) or ordinary negligence, subject to the cap.
- Sairan's failure to maintain the security measures in DPA Annex 2, short of gross negligence, resulting in a data incident.

For a platform holding unreleased product designs, supplier pricing, and (potentially) consumer data, an $855K cap is low. A single lost product line or a supplier price leak could cost Pakairt far more.

**Recommendation:**
Negotiate a super-cap for data-related claims (e.g., 2× or 3× the 12-month fees) or a carve-out from the cap for Sairan's breach of § 5 (Customer Data) or DPA § 5 (Security). At minimum, clarify that "loss of Customer Data" is not an "indirect" or "consequential" damage excluded by § 10.2, but a direct loss recoverable up to the cap.

---

## Issue 6 – Insurance: No Proactive Notification Obligation

**Documents and Sections:**
- Agreement, § 11.1 (coverage requirements)
- Agreement, § 11.2 (certificates "on request")
- Insurance Certificate Cover Letter, § 4 ("on request")

**Explanation:**
Section 11.2 requires Sairan to provide certificates "on request." The cover letter confirms this: "Licensor will provide updated certificates after each renewal **on request**." There is no obligation on Sairan to:
- Notify Pakairt if a policy is cancelled or non-renewed;
- Notify Pakairt if coverage limits are reduced;
- Notify Pakairt if an insurer's A.M. Best rating falls below A-; or
- Provide certificates proactively at each renewal.

If Sairan's cyber policy lapses between renewals and a data breach occurs, Pakairt would discover the gap only after the fact, when it seeks to make a claim.

**Recommendation:**
Amend § 11.2 to require Sairan to (a) deliver updated certificates within 30 days after each policy renewal without request, and (b) provide prompt written notice (and in any event within 10 days) of any cancellation, material reduction in coverage, or downgrade in insurer rating below the required threshold.

---

## Issue 7 – Additional Seat Pricing Is Uncapped

**Documents and Sections:**
- SOW, § 2.3

**Explanation:**
Pakairt is licensed for 350 named-user seats. Additional seats are available "in blocks of twenty-five (25) at Licensor's **then-current list price**, pro-rated to the next anniversary of the Phase 1 Acceptance Date."

The fee-adjustment cap in SOW § 4.3 (lesser of CPI-U or 3%) applies to the "Annual License Fee," not to the per-seat price for additional seats. Sairan could, in theory, double its list price for new seats at any time. If Pakairt's headcount grows and it needs 100+ additional seats, the cost could escalate significantly without contractual protection.

**Recommendation:**
Amend SOW § 2.3 to cap the per-seat price increase at the same CPI-U / 3% limit that applies to the Annual License Fee, or to fix the per-seat price for the duration of the Order Term.

---

## Issue 8 – Deemed Acceptance Risk

**Documents and Sections:**
- SOW, § 5.5

**Explanation:**
Section 5.5 provides that a Phase is "Accepted" on the *earlier* of (a) signing the Acceptance Certificate or (b) first use in production "for live business operations, other than for testing or hypercare."

This means that if any Pakairt user begins entering live orders, processing real designs, or running production workflows before the formal Acceptance Certificate is signed, acceptance is deemed to have occurred. The consequences are significant:
- The Order Term (60 months) starts running (SOW § 4.1).
- The Annual License Fee becomes due (Agreement § 4.1).
- The 45-day Phase 2 Election window starts (Side Letter § 2.1).

In this engagement, Phase 1 was formally accepted on March 2, 2026 (Notice Letter, ¶ 1), so the risk has passed. But the same mechanism will apply to any future Phase or SOW. Pakairt's teams must be instructed not to use new modules in a production capacity until the Acceptance Certificate is signed.

**Recommendation:**
For any future SOW, negotiate to remove the deemed-acceptance trigger or to require that production use must be "general and sustained" (e.g., more than 5 business days) before acceptance is deemed. In the interim, issue an internal guidance memo to all project teams clarifying that production use of any new module before formal acceptance will trigger contractual consequences.

---

## Issue 9 – Sub-Processor Termination Remedy Is Ambiguous for Infrastructure Providers

**Documents and Sections:**
- DPA, § 6.2
- DPA, Annex 3 (AWS listed as cloud hosting for all modules)

**Explanation:**
If Sairan proposes a new or replacement sub-processor and Pakairt objects on data-protection grounds, and the parties cannot resolve the objection within 30 days, Pakairt may "terminate the affected module by written notice and receive a pro-rata refund of prepaid fees for that module" (DPA § 6.2).

The current sub-processor list (Annex 3) includes Amazon Web Services for "Cloud hosting infrastructure." AWS underpins *all* modules. If Sairan proposed replacing AWS with a different cloud provider and Pakairt objected, the "affected module" is arguably every module. Terminating all modules would be equivalent to terminating the entire Agreement, but the DPA remedy is framed as terminating "the affected module" (singular) with a pro-rata refund "for that module." This creates ambiguity about whether Pakairt can terminate the entire engagement or only a single module (and which one).

**Recommendation:**
Clarify in the DPA that where a sub-processor provides infrastructure supporting multiple or all modules, the "affected module" for purposes of § 6.2 means all modules that depend on that sub-processor, and the refund applies to the full Annual License Fee (or the applicable portion). Alternatively, provide that in such a case, Pakairt may terminate the Agreement in its entirety with a pro-rata refund of all prepaid fees.

---

## Issue 10 – Term Sheet Exclusivity Language Was Broadened in the Final Agreement

**Documents and Sections:**
- Term Sheet, § 8
- Agreement, § 2.5
- SOW, § 1.2

**Explanation:**
The Term Sheet (§ 8) provided: "Pakairt will use Threadline as its exclusive solution for **PLM software for apparel and footwear design only**. Pakairt remains free to select and use other systems for all other business functions."

The final Agreement (§ 2.5) uses the defined term "Covered Functions," which the SOW (§ 1.2) expands to include not only PLM/design but also demand planning, wholesale order management, and retail POS/e-commerce merchandising.

Although the Term Sheet is non-binding, the broadening represents a significant shift from the commercial deal as initially understood. Combined with Issue 1 (the Phase 2 Election making the wholesale/retail exclusivity impossible to perform), this suggests the exclusivity provision was not carefully tailored to the final scope of the license.

**Recommendation:**
This reinforces the fix recommended in Issue 1. The exclusivity covenant should be conformed to the modules actually licensed. If Pakairt elects out of Phase 2, the exclusivity obligation should narrow accordingly. If Pakairt later re-adds Phase 2 modules (Side Letter § 4), the obligation should expand to cover those functions at that point.

---

## Additional Observations (Lower Priority)

| # | Observation | Document / Section | Comment |
|---|---|---|---|
| A | Service Level termination notice window is 90 days | SLS § 5.2 | Pakairt must monitor monthly reports closely; missing the window forfeits the right. Recommend an internal process to review SLS § 6.1 reports within 30 days of receipt. |
| B | SOC 2 report and audit rights limited to once per 12 months | DPA §§ 5.3, 8.3 | If multiple security concerns arise in a year, Pakairt is limited to one formal verification. Consider negotiating a second audit right triggered by a Severity 1 Security Incident. |
| C | SOW § 4.2 still states the fee "covers the Phase 2 Modules" | SOW § 4.2 | Inconsistent with the Side Letter reduction. The Side Letter prevails (§ 1.4), but the SOW text should be conformed to avoid confusion in future disputes. |
| D | Blackout period notice was action-itemed for Feb 13, 2026 for a March 16 event | Kickoff Minutes, Action Item 8; SLS § 2.4 | 31 days' notice—meets the 30-day requirement by one day. Confirm the notice was actually delivered on or before Feb 13. |
| E | Force majeure excludes payment obligations but not service obligations | Agreement § 17.2 | Standard, but note that Sairan could invoke force majeure to suspend hosting during, e.g., a natural disaster, with no service credit consequence (SLS § 2.3(e) excludes force majeure from availability calculation). |

---

## Priority Action Items

| Priority | Action | Deadline / Trigger |
|---|---|---|
| **Critical** | Execute amendment to Side Letter or Agreement to conform § 2.5 exclusivity to licensed modules post-Phase 2 Election | Before next wholesale order cycle or retail planning period |
| **High** | Negotiate reciprocal data protection indemnity in DPA | Next amendment cycle or renewal negotiation |
| **High** | Negotiate super-cap or carve-out for data loss / DPA breach in § 10 | Same |
| **Medium** | Add proactive insurance notification obligation in § 11.2 | Same |
| **Medium** | Cap additional seat pricing in SOW § 2.3 | Before next seat purchase |
| **Medium** | Calendar the 120-day non-renewal notice deadline for the Initial Term | ~September 2031 (120 days before 60-month expiry from March 2, 2026) |
| **Low** | Conform SOW § 4.2 language to reflect reduced fee | Housekeeping |
| **Low** | Confirm blackout period notice was delivered by Feb 13, 2026 | Immediate verification |

---

*This memorandum is based solely on the ten documents in the matter folder. It does not address tax, accounting, or business-strategy considerations. All recommendations should be reviewed by the responsible partner before being communicated to the client or the counterparty.*