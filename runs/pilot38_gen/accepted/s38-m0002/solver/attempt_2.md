# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Binond Releasing LLC – Review of Favaiv Digital Cinema Services Supply Agreement Package

---

## Executive Summary

I have reviewed the four documents in the matter folder: the Supply Agreement, the Data Processing Addendum, SOW No. 1, and the Mutual NDA. The package is generally well-drafted and favorable to Customer in many respects (strong content security regime, uncapped liability for security and confidentiality breaches, reasonable acceptance procedures). However, I have identified several material issues that expose Binond to significant risk, one of which (the DPA indemnity) is so one-sided that it should not be signed as drafted. I have also flagged a governing-law conflict between the SOW and the master agreement, an exclusivity structure that may need a business decision, and a gap in the DPA's sub-processor schedule.

Issues are ordered by significance.

---

## 1. DPA Section 9.1 – Customer Indemnifies Supplier for Data Claims "Regardless of Whether Caused in Part by Supplier"

**Where:** Data Processing Addendum, Section 9.1.

**The problem.** The DPA requires Customer to indemnify Supplier for *all* Losses arising from any third-party claim, regulatory investigation, fine, penalty, or Data Subject action relating to Customer Personal Data, **"regardless of whether caused in part by Supplier."** This means that if Supplier's own negligence, a sub-processor failure, or a security breach at Supplier's facility triggers a regulatory fine or a class action by screener recipients, Customer still owes Supplier an indemnity. In practical terms, Customer is insuring Supplier against Supplier's own mistakes.

This is inconsistent with the Supply Agreement, where Section 13.3(a) carves indemnification obligations out of the liability cap, and Section 12.1(b) has Supplier indemnify Customer for unauthorized access to Customer Materials. The DPA effectively inverts that allocation for personal data.

**Why it matters.** A single data breach involving screener recipient information (names, emails, viewing logs, IP addresses – see Annex A) could generate CCPA/CPRA statutory damages of $100–$750 per consumer per incident, plus regulatory penalties. If Supplier's platform is compromised, Binond would face the Data Subject claims *and* owe Supplier an indemnity for the same event.

**Recommended fix.** Delete "regardless of whether caused in part by Supplier" and replace with a fault-based standard. Proposed language:

> **9.1 By Customer.** Customer shall defend, indemnify and hold harmless Supplier and its Affiliates, officers, employees and agents from and against all Losses arising out of or relating to any third-party claim, regulatory investigation, fine or penalty, or Data Subject action relating to Customer Personal Data or its Processing under the Agreement, **to the extent caused by (a) Customer's instructions to Supplier, (b) Customer's failure to obtain required consents or provide required notices to Data Subjects, or (c) Customer's breach of Section 3 of this DPA. This indemnity does not apply to the extent the Losses are caused by Supplier's breach of this DPA, the Agreement, or applicable Data Protection Laws, or by the acts or omissions of any Sub-processor.**

This mirrors the structure of Section 12.1/12.2 in the Supply Agreement and allocates risk to the party whose conduct caused the loss.

---

## 2. Exclusivity Without a Meaningful Exit (Supply Agreement §3.1, §4.2)

**Where:** Supply Agreement, Sections 3.1 (Exclusive Supply), 4.2 (Renewal), 4.3 (Termination for Breach).

**The problem.** Section 3.1 requires Customer to procure *all* Distribution Deliverables – defined in Section 1.6 to encompass theatrical, home entertainment, streaming, VOD, broadcast, airline, and festival deliverables – exclusively from Supplier for the entire world. The Initial Term is three years, and the agreement auto-renews for successive one-year periods unless either party gives 90 days' non-renewal notice (Section 4.2). The only termination rights before the end of a term are for material breach (with a 30-day cure period) or insolvency (Section 4.3–4.4). There is no termination for convenience, no termination for chronic underperformance short of a single "material breach," and no service-level regime that would convert repeated missed deadlines into a terminable event.

**Why it matters.** If Favaiv's quality degrades gradually, or if its capacity is consistently insufficient (see Issue 6 below), Binond may be locked in for three years plus renewals with no practical exit. The breadth of "Distribution Deliverables" means this is not just a DCP mastering relationship – it covers every channel Binond releases into. Losing the ability to source from a second vendor for even one channel (e.g., streaming encodes) could be operationally crippling.

**Business decision needed.** This is primarily a commercial call. Binond should decide:

- Is full exclusivity across all channels and the entire world the right trade for the pricing and relationship it is getting? A narrower exclusivity (e.g., theatrical DCP mastering only, or North America only) would preserve flexibility.
- If Binond accepts full exclusivity, does it want a termination right for chronic failure to meet service levels (e.g., three or more missed delivery deadlines in any rolling six-month period)?
- Does it want a termination for convenience right after year one or year two, perhaps with a break fee?

**Recommended drafting fixes (if exclusivity is retained):**

Add a new Section 3.4:

> **3.4 Termination for Chronic Underperformance.** If Supplier fails to meet the delivery deadlines stated in a Title Order or SOW on three (3) or more occasions in any rolling six-month period, and such failures are not excused by force majeure, Customer may terminate the affected SOW or this Agreement on thirty (30) days' written notice, without penalty and without prejudice to Customer's right to claim damages.

And consider narrowing Section 3.1:

> **3.1 Exclusive Supply.** Notwithstanding anything in any SOW, Customer shall procure all **theatrical DCP mastering and KDM generation** services exclusively from Supplier throughout the Territory during the Term. Customer may procure other Distribution Deliverables from third parties, provided that Supplier remains the exclusive provider of theatrical DCP mastering for the Pictures covered by an SOW.

The scope of exclusivity should match what Binond is actually comfortable locking down.

---

## 3. Governing Law and Forum Conflict: SOW No. 1 vs. Supply Agreement

**Where:** SOW No. 1, Section 9 (New York law / New York County forum) vs. Supply Agreement, Section 19 (Delaware law / New Castle County forum).

**The problem.** The Supply Agreement's order of precedence (Section 2.3) gives SOWs priority "as to the Services, Deliverables and any matters arising under that SOW." Read strictly, this means New York law governs any dispute about SOW No. 1 services, while Delaware law governs everything else (confidentiality, content security, indemnification, data protection). A single dispute – e.g., a missed delivery deadline that also involves a security breach of the DCP in transit – could implicate both regimes, creating threshold litigation over which law and forum applies.

**Why it matters.** This is the kind of ambiguity that generates expensive motions practice and gives the opposing side leverage. It also creates uncertainty for Binond's own risk management: which state's substantive law protects its content security and confidentiality interests?

**Recommended fix.** Conform SOW No. 1, Section 9 to the Supply Agreement. Proposed replacement:

> **9. GOVERNING LAW AND JURISDICTION**
>
> 9.1 This SOW is governed by and construed in accordance with the laws of the State of Delaware, without regard to its conflict of laws principles.
>
> 9.2 The forum provisions of Section 19.2 of the Agreement apply to this SOW.

If Favaiv insists on New York (perhaps because its facility is there), the alternative is to move the master agreement to New York as well, so the entire package is governed by one law. Either way, the documents should be aligned.

---

## 4. DPA Annex C – Sub-Processors Not Identified

**Where:** Data Processing Addendum, Annex C.

**The problem.** The authorized sub-processors are listed only as "Cloud hosting provider (as notified to Customer in writing)" and "Transactional email provider (as notified to Customer in writing)." No entity names are given. Section 6.1 authorizes Customer's consent to the sub-processors "listed in Annex C," but the list is effectively empty.

**Why it matters.** Under CCPA and GDPR, a controller must know who its processors are engaging. If a sub-processor is in a jurisdiction with weak data protection, or has a poor security track record, Binond has no way to assess that risk before data flows begin. The 30-day objection right in Section 6.1 is meaningless if Customer does not know who the initial sub-processors are.

**Recommended fix.** Require Favaiv to populate Annex C with named entities before signing. Proposed language for Annex C:

| Sub-processor | Function | Location |
|---|---|---|
| [Named entity, e.g., Amazon Web Services / Azure / GCP] | Hosting of screener platform and storage | United States |
| [Named entity, e.g., SendGrid / Mailchimp / Customer.io] | Delivery of screener invitations and credentials | United States |

Add a sentence: *"Supplier shall not engage any Sub-processor not listed in this Annex C without complying with Section 6.1."*

**Business decision needed.** Once the names are provided, Binond should vet them (security posture, data residency, breach history) before the relationship goes live.

---

## 5. NDA Section 2.4 – Restriction on Transcoding/Encoding Conflicts with Supply Agreement Operations

**Where:** Mutual NDA, Section 2.4; Supply Agreement, Section 9.5; SOW No. 1, Section 2.1.

**The problem.** NDA Section 2.4 provides that the Receiving Party "shall not copy, screen, transcode, encode or retain any picture or sound materials of the Disclosing Party except as needed for the Purpose (for example, to prepare test encodes or sample packages that the Disclosing Party requests in writing)." The NDA's stated Purpose is to "explore a possible commercial relationship." The NDA has a two-year term from November 17, 2025, so it remains in force until at least November 17, 2027 (and its confidentiality obligations continue five years beyond that).

The Supply Agreement (Section 9.5) preserves the NDA for information exchanged before the Effective Date. But the NDA does not contain a supersession clause, and its Section 2.4 restriction on transcoding, encoding, and retaining content could be read to conflict with Supplier's operational right under the Supply Agreement and SOW No. 1 to ingest, encode, package, and archive DCPs.

**Why it matters.** In a dispute over content security or confidentiality, Favaiv could argue that the NDA's narrower permission (test encodes and sample packages "requested in writing") limits its right to hold archived DCPs or perform routine mastering operations, creating an ambiguity that cuts against Binond's ability to enforce the Supply Agreement's security and IP provisions cleanly.

**Recommended fix.** Add a supersession clause to the Supply Agreement. Proposed new sentence at the end of Section 9.5:

> "Except as provided in this sentence, the NDA is superseded in its entirety by this Agreement with respect to all Confidential Information disclosed on or after the Effective Date, and the obligations of Section 2.4 of the NDA shall not apply to the performance of Services under this Agreement or any SOW."

Alternatively, if the parties prefer to keep the NDA in force for pre-existing disclosures, add a carve-out to NDA Section 2.4:

> "…except as needed for the Purpose or as necessary to perform Services under a definitive agreement between the Parties."

---

## 6. Supplier's Capacity Obligation Is Soft (Supply Agreement §3.2)

**Where:** Supply Agreement, Section 3.2.

**The problem.** Supplier must "maintain sufficient personnel, equipment and facility capacity to meet Customer's **reasonably forecast** requirements." Customer's forecast is expressly "non-binding" and rolling quarterly. If Binond's actual release schedule exceeds its forecast (e.g., it acquires an additional title on short notice), Supplier has no contractual obligation to accommodate the overrun. Yet under Section 3.1, Binond cannot go to another vendor.

**Why it matters.** An independent distributor's release slate can shift quickly (acquisition timing, festival acceptance, co-financing conditions). If Favaiv is at capacity and Binond needs a rush DCP, the agreement gives Binond no leverage to compel performance beyond a general "material breach" argument, which is a high bar.

**Recommended fix.** Tighten Section 3.2:

> **3.2 Capacity.** Supplier shall maintain sufficient personnel, equipment and facility capacity to meet Customer's reasonably forecast requirements **and to accommodate up to twenty percent (20%) additional volume above the most recent forecast without surcharge or delay beyond the standard turnaround in the applicable SOW.** Customer shall give Supplier a non-binding rolling quarterly forecast of anticipated releases at least thirty (30) days before the start of each calendar quarter. **If Customer's actual requirements exceed the forecast by more than twenty percent (20%), Supplier shall use commercially reasonable efforts to accommodate the additional volume and shall notify Customer within five (5) business days if it cannot do so, in which case Customer may source the excess volume from a third party without breach of Section 3.1.**

The last sentence is critical: it creates a safety valve that prevents the exclusivity obligation from becoming a trap when Supplier cannot perform.

**Business decision needed.** The 20% buffer is a placeholder. Binond should tell us what percentage over-forecast it realistically needs to accommodate based on its acquisition pipeline.

---

## 7. Liability Cap Is Back-End Loaded (Supply Agreement §13.2)

**Where:** Supply Agreement, Section 13.2.

**The problem.** The cap is "Fees paid or payable by Customer under this Agreement in the twelve (12) months preceding the event giving rise to the claim." In month one of the relationship, if a dispute arises, the cap could be as low as a few thousand dollars (one or two DCP masters at $4,850 each). The cap only grows as fees accumulate.

**Why it matters.** While Sections 13.3(b) and (c) carve out confidentiality and content security breaches (the most critical risks for a film distributor), other significant failures – e.g., chronic missed deadlines that cause Binond to lose a festival slot or a theatrical window – would be subject to the cap. Early in the term, that cap is negligible.

**Recommended fix.** Replace the trailing-12-months formulation with a fixed floor:

> **13.2 Cap.** Except as provided in Section 13.3, each Party's total aggregate liability arising out of or relating to this Agreement shall not exceed the **greater of** (a) the Fees paid or payable by Customer under this Agreement in the twelve (12) months preceding the event giving rise to the claim, or (b) **$[X]**.

Suggest a floor of $250,000–$500,000, calibrated to the value of a single release window to Binond. This is a **business decision**: Binond should tell us what a missed theatrical or festival deadline would cost it, and we can set the floor accordingly.

---

## 8. No Consequences for Missed Turnaround Deadlines in SOW No. 1

**Where:** SOW No. 1, Section 4.3–4.4 (Standard and Rush Turnaround); Supply Agreement, Section 5.2 (Time of delivery is of the essence).

**The problem.** Section 5.2 of the Supply Agreement makes time of the essence where the SOW identifies a release date. SOW No. 1 sets specific turnarounds (7 business days standard, 3 business days rush). However, the only remedy for a late delivery is the general breach/termination machinery (30-day cure, then termination) or the force majeure carve-out (15-day threshold). There is no liquidated damages clause, no service credit, and no automatic right to source from a third party for a single late delivery.

**Why it matters.** For a theatrical release, a DCP that arrives one day late can mean missed print-and-distribute deadlines, lost exhibition slots, or contractual penalties from Binond's own downstream agreements with exhibitors. The "time is of the essence" language helps Binond argue material breach, but it does not provide a quick, self-executing remedy.

**Recommended fix.** Add a service credit or liquidated damages provision to SOW No. 1. Proposed new Section 4.7:

> **4.7 Late Delivery.** If Supplier fails to deliver a DCP by the deadline in Section 4.3 or 4.4 (as applicable), and the delay is not excused by force majeure, Supplier shall credit Customer **ten percent (10%) of the applicable mastering fee for each business day of delay, up to a maximum of fifty percent (50%) of that fee.** If the delay causes Customer to miss a theatrical release date or festival deadline identified in the Title Order, Customer may, in addition to the credit, (a) source the affected Deliverable from a third party without breach of Section 3.1 of the Agreement, and (b) recover the reasonable excess cost of such third-party performance from Supplier.

The third-party sourcing right for a single missed release date is the key protection; the credit is secondary.

---

## 9. Force Majeure Threshold Is Too Long (Supply Agreement §16.1)

**Where:** Supply Agreement, Section 16.1.

**The problem.** Customer may source from a third party only if a force majeure event prevents Supplier from performing for **more than fifteen (15) days**. For a theatrical release, 15 days of disruption could be catastrophic (the release window is lost). Yet during those 15 days, Customer is still bound by the exclusivity in Section 3.1 and has no right to engage a backup vendor.

**Recommended fix.** Reduce the threshold:

> "If a force majeure event prevents Supplier from performing for more than **five (5) business days**, Customer may obtain the affected Services from a third party for the duration of the event and may terminate the affected SOW on written notice."

Five business days is still generous for a mastering facility to clear a disruption, but it protects Binond's release schedule.

---

## 10. Supply Agreement Section 4.5(c) – KDM Completion Obligation Post-Termination

**Where:** Supply Agreement, Section 4.5(c).

**The problem.** On termination, Supplier must "complete any KDM issuance already scheduled for exhibitions booked before the termination date, unless Customer instructs otherwise." This is reasonable on its face, but it creates an operational dependency: if the relationship ends acrimoniously (e.g., for Supplier's breach), Customer may still need Supplier to issue KDMs for already-booked exhibitions. There is no SLA on how quickly those KDMs must be issued post-termination, and no requirement that Supplier maintain key management system access for a transition period.

**Recommended fix.** Add to Section 4.5:

> "(d) For a period of **ninety (90) days** following the effective date of termination, Supplier shall maintain its key management system and shall issue any KDMs requested by Customer in connection with exhibitions booked before the termination date, within **two (2) business days** of request, at the rates set out in the applicable SOW. After such ninety-day period, Supplier shall, at Customer's request, transfer all content keys and KDM generation capabilities to Customer or its designee."

---

## 11. DPA Section 6.1 – Sub-Processor Objection Standard Is Narrow

**Where:** Data Processing Addendum, Section 6.1.

**The problem.** Customer may object to a new or replacement sub-processor only on "reasonable **data protection** grounds." If the proposed sub-processor is, for example, a hosting provider with adequate data protection but a poor physical security track record, or one located in a jurisdiction that raises business concerns (e.g., national security laws allowing government access), Customer may not have a valid objection under this standard.

**Recommended fix.** Broaden the objection standard:

> "Customer may object on reasonable **data protection, security, or business** grounds within that period."

This gives Binond flexibility to reject a sub-processor that is technically compliant but operationally risky.

---

## 12. Minor / Housekeeping Items

| # | Where | Issue | Fix |
|---|---|---|---|
| 12a | Supply Agreement §1.6 | "Distribution Deliverables" is extremely broad (all channels, all formats). If Binond accepts exclusivity, this definition determines the scope of the lock-in. | Narrow to match the business decision in Issue 2. |
| 12b | SOW No. 1 §5.4 | 3% annual price increase is reasonable, but there is no cap on the *number* of increases over the life of the SOW (which tracks the Agreement's term, including renewals). Over 5+ years, compounding 3% increases add up. | Add: "…by no more than three percent (3%) **per annum, provided that the cumulative increase over the Term shall not exceed ten percent (10%)**." |
| 12c | Supply Agreement §15.1 | Audit is limited to once per 12 months (except post-incident). Given the sensitivity of pre-release content, annual may be insufficient if Binond has multiple high-profile releases. | Add: "…not more than **twice** in any twelve-month period (except following a security incident)…" |
| 12d | NDA §9.1 | NDA term is 2 years from Nov 17, 2025 (expires Nov 17, 2027). Supply Agreement Initial Term is 3 years from Mar 2, 2026 (expires Mar 2, 2029). The NDA will expire *before* the Supply Agreement. This is fine because the Supply Agreement has its own confidentiality regime, but it means that after Nov 2027, the NDA's indefinite protection for "picture and sound materials, unreleased Pictures, content keys and security credentials" (NDA §9.2) no longer applies, and only the Supply Agreement's Section 9.6 protection remains. The two are substantively similar, but the gap should be confirmed. | No drafting fix needed if Issue 5 (supersession) is resolved. Otherwise, extend the NDA term to match the Supply Agreement or add a survival bridge. |
| 12e | DPA Annex A | "Duration" is listed as "The Term, plus any period of return or deletion under Section 11." This is circular – Section 11's return/deletion obligation is triggered by the end of the Term, so the duration of processing is coextensive with the Term. Not wrong, but imprecise. | Clarify: "The Term of the Agreement, plus fifteen (15) days for return or deletion under Section 11." |

---

## Items Incomplete or Needed from Client

1. **Sub-processor identities (DPA Annex C).** Favaiv has not named its cloud hosting or email providers. We need those names to complete the data protection analysis and to advise Binond on whether any present jurisdictional or security concerns.

2. **Title Order template.** SOW No. 1 references "Title Orders" (Section 4.1) as the mechanism for ordering individual DCP masters, but no template or form is in the folder. We should request one to confirm that the Title Order mechanism does not introduce terms that override the SOW or the Agreement (e.g., different acceptance criteria, shortened cure periods, or expanded exclusivity).

3. **Binond's release pipeline for the next 12–18 months.** To calibrate the capacity buffer (Issue 6), the liability floor (Issue 7), and the late-delivery remedy (Issue 8), we need to understand volume and timing. A rough count of titles and release dates would suffice.

4. **Downstream exhibitor agreements.** If Binond has agreements with exhibitors that impose penalties on *it* for late DCP delivery, we should know the quantum so we can assess whether the proposed service credit in Issue 8 is adequate or whether we need a pass-through indemnity from Favaiv for Binond's downstream liabilities.

5. **Insurance certificates.** Section 14.1 requires Favaiv to maintain CGL ($2M), E&O/media liability ($3M), cyber ($3M), and property insurance. We should request current certificates to confirm coverage is in place before signing, and to verify that the cyber policy covers first-party data breach costs (forensics, notification, credit monitoring) that would otherwise fall on Binond under the DPA indemnity as currently drafted.

---

## Summary of Recommended Negotiating Positions

| Priority | Issue | Ask |
|---|---|---|
| **Must fix** | DPA §9.1 indemnity | Delete "regardless of whether caused in part by Supplier"; replace with fault-based standard |
| **Must fix** | SOW §9 / Agreement §19 governing law conflict | Conform to single jurisdiction (Delaware preferred) |
| **Must fix** | DPA Annex C unnamed sub-processors | Require named entities before signing |
| **Strong preference** | Exclusivity scope + exit rights | Narrow §3.1 or add §3.4 chronic underperformance termination |
| **Strong preference** | Capacity / over-forecast safety valve | Add 20% buffer + third-party sourcing right in §3.2 |
| **Strong preference** | Late delivery remedy in SOW | Add §4.7 service credit + third-party sourcing for missed release dates |
| **Moderate** | Force majeure threshold | Reduce from 15 days to 5 business days |
| **Moderate** | Liability cap floor | Add fixed dollar minimum |
| **Moderate** | NDA §2.4 conflict | Add supersession or carve-out |
| **Housekeeping** | Items 12a–12e | Clean-up in redline |

I am available to prepare a full redline once you and the client have had a chance to weigh in on the business decisions flagged above (exclusivity scope, capacity buffer percentage, liability floor, and sub-processor vetting).