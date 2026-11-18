# MEMORANDUM

**TO:** Partner
**FROM:** Associate
**RE:** Traimand Seed Genetics, Inc. – Figos Analytics, LLC Software License: Issue Identification
**DATE:** [Current]

---

## Issue 1: Non-Renewal Notice Was 11 Days Late; Auto-Renewal Likely Triggered

**Where:** License Agreement § 12.2; Order Form OF-001 § 2.2–2.3; SOW 02 § 8.1–8.2.

**Facts.** The Initial Subscription Term is 36 months from February 1, 2024, ending January 31, 2027 (OF-001 § 2.2). Section 12.2 requires written notice of non-renewal "at least one hundred twenty (120) days before the end of the then-current term." One hundred twenty days before January 31, 2027 is **October 3, 2026**. Traimand delivered its non-renewal notice on **October 14, 2026** (SOW 02 § 8.1) — 109 days before term end, 11 days short. Figos has disputed the notice's effectiveness in writing (SOW 02 § 8.1), and both parties expressly reserved their positions (SOW 02 § 8.2).

**Why it matters.** If the notice is ineffective, OF-001 auto-renews for a 24-month Renewal Term (OF-001 § 2.3) at **Licensor's then-current list pricing** (OF-001 § 2.4), not the contracted Year 3 rate of $493,320. There is no cap, escalation limit, or most-favored-customer provision on renewal pricing. Given that Traimand is in the process of merging with Kestrel and intends to transition its breeding informatics operations (SOW 02, Recital C), an unintended 24-month lock-in at unknown list pricing is a material financial and strategic exposure.

**Recommended fix.**
- Open immediate negotiations with Figos to either (a) accept the non-renewal notice as effective (arguing substantial compliance or estoppel given Figos's performance under SOW 02 without objection at signing), or (b) agree to a mutually acceptable exit date and transition timeline in exchange for Traimand's payment of the SOW 02 fees.
- If Figos holds firm, evaluate whether to pay the renewal-year fees under protest while preserving the dispute, or to seek a negotiated early-termination fee that is less than 24 months of list pricing.
- In any event, document the 11-day shortfall and the business reason (the Kestrel merger was signed September 22, 2026 — 22 days before the notice — and Traimand likely calculated the deadline from the merger signing rather than the term end). This context may support a good-faith / substantial-compliance argument.

---

## Issue 2: Change of Control to Kestrel Requires Figos Consent; None in the File

**Where:** License Agreement § 1.1 (definition of "Change of Control"), § 14.2; SOW 02 Recital C.

**Facts.** Section 14.2 provides that "a Change of Control of Customer is deemed an assignment" requiring "Licensor's prior written consent." The defined term (License Agreement § 1.1) includes "the acquisition by any person or group of more than fifty percent (50%) of the Party's voting interests." Under the Kestrel merger, Traimand will become a "wholly owned subsidiary of Kestrel" (SOW 02, Recital C) — a 100% acquisition, squarely within the definition. The merger agreement was signed September 22, 2026; the SOW was signed October 28, 2026. **No document in the file evidences Figos's written consent to the Change of Control.**

**Why it matters.** If the Kestrel merger closes without Figos consent, Figos may terminate the entire Agreement on 30 days' written notice (§ 14.2, last sentence). This would cut off Traimand's access to the Platform and, critically, could disrupt the SOW 02 data migration and Transition Package delivery that Traimand needs for the Kestrel integration. Even if the merger has not yet closed, the pending CoC gives Figos significant negotiating leverage on every open issue (non-renewal, pricing, indemnity scope).

**Recommended fix.**
- Before the Kestrel merger closes, obtain Figos's written consent to the Change of Control. Frame it as a condition to closing or a covenant in the merger agreement if possible.
- In the consent request, bundle it with a resolution of Issue 1 (non-renewal) and a transition plan: e.g., "We consent to the CoC; in exchange, the parties agree the subscription ends on [date] and Figos will complete SOW 02 deliverables by [date]."
- If Figos refuses consent, assess whether the 30-day termination right is the worst case (it is, because § 12.4 gives a 60-day export window) and whether the Kestrel integration timeline can absorb a Figos termination.
- Note the asymmetry: § 14.3 permits Figos to assign to any Affiliate or acquirer without Traimand's consent. If Figos is itself acquired, Traimand has no approval right. This should be flagged to the client as a structural imbalance.

---

## Issue 3: Order Form Special Term 4 Guts the Uncapped Data-Security Liability

**Where:** License Agreement § 11.3(b); OF-001 Special Term 4; License Agreement § 1.3 (order of precedence).

**Facts.** License Agreement § 11.3(b) carves out "Licensor's breach of Section 9 (Data Security and Confidentiality)" from both the liability cap (§ 11.1) and the consequential-damages exclusion (§ 11.2). This means that, under the base agreement, a negligent data breach by Figos would expose it to uncapped liability. However, OF-001 Special Term 4 provides: "Section 11.3(b) shall apply **only to Licensor's willful disclosure** of Customer Data in breach of Section 9. **All other breaches of Section 9 by Licensor are subject to the cap in Section 11.1.**" Under the order of precedence (§ 1.3), the Order Form controls over the License Agreement.

**Why it matters.** Traimand's Customer Data includes genotypic, phenotypic, pedigree, and germplasm data — the core intellectual property of a seed company. A negligent breach (misconfigured access, lost laptop, vendor error) would be capped at the 12-month fee amount (~$493,320 in Year 3; potentially higher in a renewal year at list pricing). That cap is almost certainly far below the actual value of the data or the cost of a remediation. Only a *willful* disclosure — a deliberate act — escapes the cap. The practical effect is that Figos's financial exposure for a serious but negligent data breach is limited to roughly one year of subscription fees.

**Recommended fix.**
- Negotiate a restoration of the § 11.3(b) carve-out for at least negligent breaches, or a super-cap (e.g., 3× annual fees) for Section 9 breaches.
- If Figos will not move, ensure the cyber insurance (see Issue 8) is adequate to cover the gap, and consider requiring Figos to purchase a higher-limit policy or a tail policy.
- At minimum, clarify that "willful disclosure" does not include reckless or grossly negligent conduct, and that the § 11.3(c) carve-out for gross negligence still applies to Section 9 breaches (it should, as a separate ground, but confirm there is no ambiguity).

---

## Issue 4: Transition Package Model Specifications Are Licensed Back Under § 2.1, Not Assigned

**Where:** License Agreement § 7.1, § 7.3; SOW 02 § 3.4(c).

**Facts.** SOW 02 § 3.4(c) requires Figos to deliver "model specifications and parameter sets used in those runs, sufficient to permit an independent quantitative geneticist to reproduce the computation outside the Platform." However, License Agreement § 7.3 provides that "Licensor's pre-existing materials incorporated in any deliverable remain Licensor's property and are licensed to Customer on the terms of Section 2.1." Section 2.1 grants a license "to access and use the Platform … for Customer's and its Affiliates' internal plant breeding, research and product development purposes." The model specifications are almost certainly Figos's pre-existing materials (they are the core of the Platform's GEBV Engine).

**Why it matters.** Traimand's stated purpose for the Transition Package is to support integration with Kestrel's breeding informatics systems (SOW 02, Recital C). If those systems are not "the Platform" (i.e., not Figos's hosted software), Traimand's use of the model specifications to configure or validate a third-party system may fall outside the § 2.1 license. Figos could argue that reproducing its GEBV computation in a non-Figos environment is not "access[ing] and us[ing] the Platform." This creates a risk that Traimand pays $48,000 for the Transition Package (SOW 02 § 9.1) and then cannot legally use the model specs for their intended purpose.

**Recommended fix.**
- Before the Transition Package is delivered, negotiate a specific license grant in the SOW or a side letter: the model specifications and parameter sets in the Transition Package are licensed to Traimand (and its Affiliates, including Kestrel post-closing) for use in any breeding informatics system for internal plant breeding, research, and product development purposes, in perpetuity or for a defined term.
- Alternatively, request that Figos deliver the model specs in a form that is genuinely "sufficient to permit an independent quantitative geneticist to reproduce the computation" (per the SOW's own language) and that this sufficiency standard implies a license to use them independently of the Platform. Put this interpretation in writing in the SOW change order.

---

## Issue 5: Broad Customer Indemnity for Legacy Trial Data

**Where:** SOW 02 § 7.1; License Agreement § 3.2, § 6.1.

**Facts.** SOW 02 § 7.1 requires Traimand to indemnify Figos against any third-party claim "arising from the Legacy Trial Data or from Licensor's receipt, processing, loading or transfer of the Legacy Trial Data in accordance with this Statement of Work," including claims that the data "was collected, used or transferred in breach of grower agreements, cooperator trial agreements, third-party germplasm licenses, material transfer agreements or other obligations owed by Customer to any third party." The Legacy Trial Data explicitly includes "data generated at cooperator sites operated by growers under agreements with Customer, and data relating to germplasm that Customer has in-licensed from third parties" (SOW 02 § 1, definition of "Legacy Trial Data").

**Why it matters.** Traimand's trial network involves numerous cooperator growers and in-licensed germplasm from third parties. If any cooperator agreement or germplasm license contains a data-use restriction (e.g., "data shall not be provided to third parties without prior written consent"), the act of uploading that data to Figos's Platform could trigger a breach for which Traimand indemnifies Figos. The indemnity is uncapped (it falls within § 11.3(a) of the License Agreement, which excludes indemnification obligations from the cap). The volume is large: approximately 6.4 million plot records and 3,800 spreadsheet files spanning 2009–2023 (SOW 02, Exhibit A).

**Recommended fix.**
- Before data extraction begins (SOW 02 § 6.2 gives Traimand 20 business days after Migration Specification approval), conduct a targeted review of the cooperator grower agreements and germplasm in-licensing agreements to identify any data-sharing restrictions.
- If restrictions exist, either (a) obtain consents from the affected third parties, (b) exclude the affected data from the migration scope via a change order, or (c) negotiate a limitation on SOW 02 § 7.1 to exclude claims arising from data that Traimand identified in writing to Figos as potentially restricted, provided Figos proceeds with the migration after receiving that notice.
- Confirm that the § 7.2 exclusion (claims arising from Figos's use "other than as permitted") adequately protects Traimand if Figos mishandles the data.

---

## Issue 6: Breeding Season Freeze Does Not Cover All Model Changes

**Where:** OF-001 Special Term 1; Quality Agreement § 2.2 (definition of "Model Change"), § 7.5.

**Facts.** Special Term 1 freezes only "Updates that change GEBV calculation methodology or default model parameters" between August 1 and October 31. The Quality Agreement defines "Model Change" more broadly to include changes to "marker quality-control thresholds, imputation methods or the relationship matrices used in GEBV computation" (QA § 2.2). QA § 7.5 states that "Licensor shall schedule deployments of Model Changes in accordance with Special Terms Section 1 of Order Form No. OF-001."

**Why it matters.** The language of Special Term 1 does not explicitly prohibit deployment of marker QC threshold changes, imputation method changes, or relationship matrix changes during the freeze window. A narrow reading would permit Figos to deploy those changes in, e.g., September, even though they are "Model Changes" under the QA and even though QA § 7.5 references Special Term 1 for scheduling. In the August 19, 2026 meeting, Figos voluntarily committed not to deploy MC-2026-03 (which included both marker QC and relationship matrix changes) during the freeze (Meeting Notes § 4.3), but that is a statement of intent, not a contractual obligation. Future Model Changes may not receive the same courtesy.

**Recommended fix.**
- Amend Special Term 1 (or add a clarifying sentence) to provide: "For purposes of this Special Term 1, 'GEBV calculation methodology or default model parameters' includes all changes that constitute a Model Change as defined in Section 2.2 of the Quality Agreement." This closes the gap without requiring a full restatement.
- Alternatively, add to QA § 7.5: "No Model Change of any type shall be deployed to the Production Environment between August 1 and October 31 without Customer's prior written approval."

---

## Issue 7: Cyber/TEO Insurance Is Claims-Made; No Evidence of Tail Coverage

**Where:** Certificate of Insurance § 5.3; License Agreement § 13.1.

**Facts.** The Technology E&O / Network Security and Privacy Liability policy (Meridian Specialty Insurance Company, Policy No. MSI-TEO-0938841-06) is a **claims-made** form with a retroactive date of January 1, 2019 and a policy period of February 1, 2026 – February 1, 2027. Claims-made policies cover only claims first made during the policy period (or during an extended reporting period) for incidents occurring after the retroactive date. License Agreement § 13.1 requires Figos to maintain insurance "during the term of this Agreement, and for one (1) year after it ends."

**Why it matters.** If the Agreement terminates (whether by effective non-renewal, by Figos's CoC termination right, or by mutual agreement) and Figos does not renew the claims-made policy or purchase a tail, a data breach that occurred during the subscription but is discovered and claimed after the policy expires would be uninsured. Given that Traimand's data will be in Figos's possession for the duration of the SOW 02 migration and that the deletion certification (QA § 5.7) occurs only after the export period, there is a window in which a latent breach could surface after coverage ends. The $5,000,000 aggregate limit (shared between TEO and cyber coverage) is also modest for a breach affecting genomic data of a major seed company.

**Recommended fix.**
- Require Figos to confirm in writing that it will either (a) renew the claims-made policy for at least one year after the Agreement ends (satisfying § 13.1), or (b) purchase a tail / extended reporting period covering at least one year post-termination.
- Request a copy of the policy (or at minimum the declarations page and the extended reporting period provisions) to confirm the terms.
- Consider whether the $5M aggregate is adequate given the sensitivity of the data; if not, negotiate an increase or require Figos to evidence additional coverage.

---

## Issue 8: Validation Report Acceptance Deadline — Status Unclear

**Where:** Quality Agreement § 7.3; Meeting Notes § 5.5, Action Item 1.

**Facts.** Validation Report VR-2026-03 was delivered to Dr. Ostrander on August 12, 2026 (Meeting Notes § 5.1). QA § 7.3 requires Customer to "accept or reject the Validation Report in writing within ten (10) business days after receipt." The deadline was **August 26, 2026** (Meeting Notes § 5.5, Action Item 1). No document in the file confirms that Traimand delivered a written acceptance or rejection by that date.

**Why it matters.** The QA does not contain a deemed-acceptance provision for Validation Reports (unlike SOW 02 § 5.3, which deems SOW deliverables accepted if Customer does not object within the review period). However, if Traimand is silent and Figos proceeds to deploy MC-2026-03 on November 10, 2026 (Meeting Notes § 4.3), Figos may argue that Traimand's failure to reject constitutes acceptance, or at minimum that Traimand waived its right to object. Conversely, if Traimand intended to reject but missed the deadline, it may lose leverage. The deployment is scheduled for November 10, 2026 — only two weeks after the SOW Effective Date (October 28, 2026) — creating a compressed timeline in which the model changes and the data migration will overlap.

**Recommended fix.**
- Confirm immediately whether Dr. Ostrander or another Traimand representative delivered a written response by August 26, 2026. If not, send a written response now (acceptance or rejection with specific grounds) and note the delay.
- If the Validation Report is accepted, ensure the Change Control Record is updated (Meeting Notes, Action Item 3) and that the deployment is not accelerated ahead of the SOW 02 migration milestones.
- If there are grounds for rejection (e.g., the forward-validation design did not adequately test the interaction between the marker QC change and the relationship matrix blending), raise them in writing and invoke the QA § 3.3 escalation process.

---

## Issue 9: Asymmetric Assignment Rights

**Where:** License Agreement § 14.2 vs. § 14.3.

**Facts.** Section 14.2 prohibits Customer from assigning without Licensor's consent and deems a Change of Control to be an assignment. Section 14.3 permits Licensor to assign "without Customer's consent to any Affiliate or any successor or acquirer of all or part of its business or assets to which this Agreement relates," with only 30 days' post-closing notice.

**Why it matters.** Traimand is locked in: it cannot be acquired, merge, or reorganize without Figos's permission, but Figos can be acquired by a competitor or an entity with different security practices, and Traimand's data would transfer with the agreement. Given the sensitivity of genomic selection data (which reveals a seed company's breeding pipeline), this is a significant risk. There is no right to terminate if Figos assigns to a competitor.

**Recommended fix.**
- Negotiate a mutual assignment provision: Customer may assign to an Affiliate or in connection with a Change of Control upon notice (not consent), and Licensor may assign only to a non-competitor or with Customer's consent (not to be unreasonably withheld).
- At minimum, add a termination right for Customer if Licensor assigns to a direct competitor of Customer (i.e., another genomic selection platform provider).
- If Figos resists, consider whether the CoC consent (Issue 2) can be traded: "We consent to your assignment to [X]; in exchange, you consent to our CoC to Kestrel."

---

## Issue 10: No Consequential-Damages Carve-Out for Breeding-Season Disruption

**Where:** License Agreement § 11.2, § 8.4; OF-001 § 6.3.

**Facts.** Section 11.2 excludes all indirect, consequential, and special damages, including "lost profits or revenues." Section 8.4 disclaims any warranty that GEBVs will achieve particular genetic gain or field performance. The only remedy for Platform unavailability is the service credit in OF-001 § 6.3: 5% of the monthly fee per 0.5% shortfall, capped at 25% of the monthly fee. For a $493,320 annual fee, the monthly equivalent is ~$41,110; the maximum monthly credit is ~$10,278.

**Why it matters.** If the Platform is unavailable or produces incorrect GEBVs during a critical breeding decision window (e.g., cross planning for the upcoming season), Traimand's actual losses (delayed selection decisions, suboptimal crosses, lost genetic gain over multiple seasons) could be substantial. The contractual remedy is a service credit of at most ~$10,000 per month, and the disclaimer in § 8.4 forecloses any claim that Figos warranted a particular outcome. The § 11.2 exclusion of lost profits means Traimand cannot recover the economic value of delayed or impaired selection decisions.

**Recommended fix.**
- This is a structural limitation that is difficult to change in a renewal negotiation, but consider: (a) a super-cap or carve-out for Platform unavailability exceeding a threshold (e.g., more than 48 hours in a breeding-critical period); (b) a termination right with full refund if availability falls below a floor (e.g., 95%) for two consecutive months; or (c) a specific service-level remedy tied to the breeding calendar (e.g., if the Platform is down during the cross-planning window in Q3, Traimand may terminate the affected module without penalty).
- At minimum, document the business impact of any outage to preserve the record for a bad-faith or willful-misconduct claim under § 11.3(c), which is not subject to the consequential-damages exclusion.

---

## Summary Table

| # | Issue | Primary Documents | Severity |
|---|-------|------------------|----------|
| 1 | Non-renewal notice 11 days late; auto-renewal at list pricing likely | LA § 12.2; OF-001 § 2.3–2.4; SOW 02 § 8.1 | **Critical** |
| 2 | Kestrel CoC requires Figos consent; none obtained | LA § 14.2; SOW 02 Recital C | **Critical** |
| 3 | Data-security liability capped for all but willful breaches | LA § 11.3(b); OF-001 ST 4 | **High** |
| 4 | Transition Package model specs licensed under § 2.1 only | LA § 7.3; SOW 02 § 3.4(c) | **High** |
| 5 | Uncapped indemnity for Legacy Trial Data third-party claims | SOW 02 § 7.1 | **High** |
| 6 | Breeding-season freeze gap for non-methodology Model Changes | OF-001 ST 1; QA § 2.2, § 7.5 | **Moderate** |
| 7 | Claims-made cyber policy; no tail coverage confirmed | Cert. of Ins. § 5.3; LA § 13.1 | **Moderate** |
| 8 | VR-2026-03 acceptance deadline (Aug 26, 2026) — status unknown | QA § 7.3; Meeting Notes § 5.5 | **Moderate** |
| 9 | Asymmetric assignment rights | LA § 14.2 vs. § 14.3 | **Moderate** |
| 10 | No meaningful remedy for breeding-season disruption | LA § 11.2, § 8.4; OF-001 § 6.3 | **Moderate** |

---

*All section references are to the documents as they appear in the matter folder. "LA" = Software License Agreement; "OF-001" = Order Form No. OF-001; "QA" = Quality Agreement; "SOW 02" = Statement of Work No. 02; "Meeting Notes" = Minutes of August 19, 2026 Quarterly Quality Review; "Cert. of Ins." = Certificate of Liability Insurance dated November 4, 2026.*