# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Binond Releasing LLC – Review of Favaiv Digital Cinema Services Supply Agreement Package

---

## Summary

I have reviewed the four documents in the matter folder: the Supply Agreement, the Data Processing Addendum, SOW No. 1, and the Mutual NDA. The package is generally well-drafted from a structural standpoint, but it contains several provisions that create significant exposure for Binond, one direct conflict between documents, and a critical gap between the scope of Binond's exclusivity commitment and the services actually specified. The issues are ranked by significance below.

---

## 1. DPA Indemnification: Customer Indemnifies Supplier Regardless of Fault (Uncapped)

**Where:** DPA § 9.1; Supply Agreement § 13.3(a) and § 2.3(a).

**Issue:** DPA § 9.1 requires Customer to indemnify Supplier for all Losses arising from any third-party claim, regulatory investigation, fine or penalty, or Data Subject action relating to Customer Personal Data, **"regardless of whether caused in part by Supplier."** Read together with Supply Agreement § 13.3(a) (which excludes indemnification obligations under any Addendum from the liability cap) and § 2.3(a) (which gives the DPA precedence over the Agreement body), this means:

- If Supplier's own negligence or a Sub-processor's failure causes a Personal Data Breach, Customer still owes Supplier an indemnity.
- That indemnity is **uncapped**.
- The DPA's precedence rule means this overrides Supply Agreement § 12.1(b), which would otherwise have Supplier indemnifying Customer for unauthorized access to Customer Materials.

**Why it matters:** Binond would bear the financial risk of Supplier's data protection failures. For a company distributing films with high-profile screener recipients (critics, awards voters, studio executives), a breach could trigger regulatory fines (CCPA, GDPR if EU/UK recipients are involved), class actions, and remediation costs. Having to indemnify the party that caused the problem is untenable.

**Recommended fix:** Amend DPA § 9.1 to limit Customer's indemnity to claims arising from Customer's own acts or omissions (e.g., providing unlawful instructions, failing to obtain required consents). Add a corresponding Supplier indemnity for claims arising from Supplier's or its Sub-processors' breach of the DPA. Proposed language:

> **9.1 By Customer.** Customer shall defend, indemnify and hold harmless Supplier and its Affiliates, officers, employees and agents from and against all Losses arising out of or relating to any third-party claim, regulatory investigation, fine or penalty, or Data Subject action to the extent arising from (a) Customer's provision of unlawful or undocumented instructions under Section 4.1, or (b) Customer's failure to obtain a lawful basis, notice or consent required under Section 3.2.
>
> **9.3 By Supplier.** Supplier shall defend, indemnify and hold harmless Customer and its Affiliates, officers, employees and agents from and against all Losses arising out of or relating to any third-party claim, regulatory investigation, fine or penalty, or Data Subject action to the extent arising from (a) a Personal Data Breach caused by Supplier or any Sub-processor; (b) Supplier's breach of this DPA; or (c) Supplier's gross negligence or willful misconduct.
>
> **9.4 Procedure.** Section 12.3 of the Agreement applies to claims under this Section 9.

**Note:** This also requires a conforming edit to Supply Agreement § 13.3(a) so that the Supplier's new DPA indemnity is likewise excluded from the cap (it already is, by the existing language "indemnification obligations under Section 12 or any Addendum").

---

## 2. Exclusivity Scope Far Exceeds Agreed Services

**Where:** Supply Agreement § 3.1 and § 1.6 (definition of "Distribution Deliverables"); SOW No. 1 § 2.3 (Exclusions).

**Issue:** Section 3.1 obligates Customer to procure **all** Distribution Deliverables **exclusively** from Supplier **throughout the Territory** (defined as the entire world, § 1.12) during the Term (three years plus auto-renewals). The definition of "Distribution Deliverables" in § 1.6 sweeps in theatrical, home entertainment, streaming, VOD, broadcast, cable, airline, festival and market deliverables, plus all related mastering, encoding, conforming, packaging, duplication, encryption and screener services.

However, SOW No. 1 covers only **theatrical DCP mastering for the United States and Canada**, and expressly excludes KDM generation, drive duplication, screeners, and all non-theatrical deliverables (§ 2.3). No other SOW is in the folder.

**Why it matters:** Binond is contractually locked to Favaiv as its sole worldwide provider for every category of distribution deliverable for at least three years (and potentially longer with renewals), but has no agreed pricing, specifications, service levels or delivery terms for any of those other services. If Binond needs, say, a 4K HDR master for a streaming platform or drive duplication for a festival in Europe, it must use Favaiv, but the commercial terms for that work are undefined. This gives Favaiv significant leverage to dictate terms on future SOWs, and it prevents Binond from using a potentially better or cheaper vendor for those services during the Term.

**Business decision needed:** This is primarily a commercial question. Does Binond want to commit to worldwide exclusivity for all deliverable types before it has evaluated Favaiv's capability and pricing for non-theatrical, international, and screener work? If the answer is yes, the exclusivity should be narrowed to match the SOWs actually in place, or at minimum to the services Favaiv has demonstrated it can perform. If the answer is no, § 3.1 should be deleted or substantially limited.

**Recommended fix (if exclusivity is retained but narrowed):**

> **3.1 Exclusive Supply.** During the Term, Customer shall procure from Supplier exclusively the Services and Deliverables specified in one or more SOWs in effect under this Agreement. For the avoidance of doubt, this Section 3.1 does not obligate Customer to procure any category of Distribution Deliverable for which no SOW has been executed.

Alternatively, if the business decision is to maintain broad exclusivity, add a most-favored-customer or price-parity clause for future SOWs so that Favaiv cannot exploit the locked-in position to charge premium rates for services that were not priced at signing.

---

## 3. Governing Law Conflict Between SOW No. 1 and the Supply Agreement

**Where:** SOW No. 1 § 9.1–9.2 (New York law; New York County forum); Supply Agreement § 19.1–19.2 (Delaware law; New Castle County forum); Supply Agreement § 2.3 (order of precedence).

**Issue:** SOW No. 1 selects New York governing law and a New York forum for "any dispute arising under or relating to this SOW." The Supply Agreement selects Delaware for the Agreement generally. Section 2.3 gives SOWs precedence over the Agreement body "as to the Services, Deliverables and any matters arising under that SOW." The result is a split: disputes about the quality or delivery of a DCP are governed by New York law in New York courts, while disputes about confidentiality, IP ownership, indemnification or termination of the Agreement are governed by Delaware law in Delaware courts.

**Why it matters:** This creates practical and strategic problems. A single dispute (e.g., a defective DCP that also raises a confidentiality question about leaked content) could implicate both regimes. It complicates litigation strategy, increases costs (two potential forums), and creates interpretive uncertainty about which law applies to mixed claims. For a Delaware LLC, having its primary commercial agreement governed by Delaware law is natural and convenient; importing New York law for the SOW layer is unnecessary and disadvantageous.

**Recommended fix:** Delete SOW No. 1 § 9 in its entirety and add the following:

> **9. GOVERNING LAW AND JURISDICTION**
>
> 9.1 This SOW is governed by and construed in accordance with the laws of the State of Delaware, without regard to its conflict of laws principles.
>
> 9.2 Each Party irrevocably submits to the exclusive jurisdiction of the state and federal courts located in New Castle County, Delaware for any action arising under or relating to this SOW, and waives any objection to venue in those courts.

This aligns the SOW with the Agreement and eliminates the split.

---

## 4. Liability Cap Is Tied to Trailing 12-Month Fees (Potentially Nominal Early in Term)

**Where:** Supply Agreement § 13.2.

**Issue:** The cap is "the Fees paid or payable by Customer under this Agreement in the twelve (12) months preceding the event giving rise to the claim." In the first 12 months of the relationship, if Binond orders only a handful of DCP masters at $4,850 each (SOW 1 § 5.1), the cap could be as low as $20,000–$50,000. A single moderate security incident or a defective master that delays a release could easily exceed that.

**Why it matters:** While § 13.3 carves out content security breaches (§ 7), confidentiality breaches (§ 9), and indemnification obligations from the cap, many other claims (e.g., a Supplier failure to meet a delivery deadline that causes a missed release window, a warranty claim under § 11.2, or a general breach of § 5) would be subject to the cap. In the early months, that cap is too low to be meaningful.

**Recommended fix:** Replace the trailing-12-months formula with a fixed floor. Proposed language:

> **13.2 Cap.** Except as provided in Section 13.3, each Party's total aggregate liability arising out of or relating to this Agreement shall not exceed the greater of (a) the Fees paid or payable by Customer under this Agreement in the twelve (12) months preceding the event giving rise to the claim, or (b) $500,000.

The dollar floor should be a business decision for the client, but $500,000 is a reasonable starting point given the value of a single theatrical release to an independent distributor.

---

## 5. Sub-Processors Not Actually Identified in Annex C

**Where:** DPA Annex C.

**Issue:** Annex C lists two sub-processors by generic function only: "Cloud hosting provider (as notified to Customer in writing)" and "Transactional email provider (as notified to Customer in writing)." The actual entity names are not provided. DPA § 6.1 states that Customer "authorizes" the sub-processors listed in Annex C, but the list is effectively empty.

**Why it matters:** Binond is purporting to authorize data processing by entities it cannot identify. If a breach occurs at an unknown cloud host, Binond may later argue it never actually authorized that processor, but the DPA language could be read as a blanket authorization. Additionally, for CCPA "service provider" compliance, Binond needs to know who is processing the data to verify that the sub-processor is bound by equivalent restrictions (DPA § 6.2 addresses this, but only if we know who the sub-processor is).

**Recommended fix:** Require Favaiv to populate Annex C with the actual legal names, addresses, and data protection contact details of each sub-processor before signing. If Favaiv resists, add the following to DPA § 6.1:

> For the avoidance of doubt, Customer's authorization in this Section 6.1 is limited to the specific Sub-processors identified by name in Annex C. Generic or functional descriptions do not constitute an authorization.

---

## 6. No Remedy if Supplier Fails to Maintain Capacity

**Where:** Supply Agreement § 3.2.

**Issue:** Section 3.2 requires Supplier to "maintain sufficient personnel, equipment and facility capacity to meet Customer's reasonably forecast requirements," but the forecast is expressly non-binding. There is no stated consequence if Supplier fails to maintain adequate capacity. The only related protection is the force majeure clause (§ 16.1), which allows Customer to source from a third party only after a force majeure event persists for 15 days.

**Why it matters:** If Favaiv's facility is overcommitted to other customers (which § 3.3 expressly permits) and cannot meet Binond's release schedule, Binond has no contractual remedy short of arguing material breach under § 4.3 (which requires a 30-day cure period—often longer than the window between a missed mastering deadline and a theatrical release). The non-binding forecast means Favaiv has no obligation to plan for Binond's pipeline.

**Recommended fix:** Add a service-level commitment and a remedy. Proposed language to add to § 3.2:

> If Supplier is unable to accept a Title Order or meet a delivery deadline under an SOW due to insufficient capacity, Supplier shall notify Customer in writing within two (2) business days of becoming aware of the capacity constraint. If Supplier cannot resolve the constraint within five (5) business days, Customer may (a) source the affected Services from a third party without breach of Section 3.1, and (b) terminate the affected SOW under Section 4.3 without the 30-day cure period.

**Business decision needed:** The client should confirm whether it is comfortable with the 2-business-day / 5-business-day trigger or whether shorter windows are appropriate given typical release scheduling.

---

## 7. Auto-Renewal with 90-Day Notice Creates a Lock-In Trap

**Where:** Supply Agreement § 4.2.

**Issue:** The Agreement renews automatically for successive one-year terms unless either Party gives notice of non-renewal at least 90 days before the end of the then-current term. Combined with the broad exclusivity in § 3.1 (see Issue 2 above), missing the 90-day window locks Binond in for another year with no ability to source from competitors.

**Why it matters:** For a company whose release slate may shift, whose needs may outgrow or shrink relative to Favaiv's capacity, or who may identify a better vendor, a 90-day non-renewal notice is a meaningful administrative risk. If the client's contract management process does not calendar this date, the renewal is automatic.

**Recommended fix:** Reduce the notice period to 60 days and add a reminder mechanism:

> **4.2 Renewal.** After the Initial Term, this Agreement renews automatically for successive one-year periods unless either Party gives written notice of non-renewal at least sixty (60) days before the end of the then-current term. Supplier shall send Customer a written reminder of the upcoming renewal date and the non-renewal deadline no fewer than one hundred twenty (120) days before the end of the then-current term.

Alternatively, eliminate auto-renewal entirely and require affirmative renewal by both parties.

---

## 8. Insurance: No Additional Insured or Loss Payee Requirement

**Where:** Supply Agreement § 14.1.

**Issue:** Section 14.1 requires Supplier to maintain CGL ($2M), E&O ($3M), cyber ($3M), and property insurance, and to provide certificates on request. It does not require Supplier to name Customer as an additional insured on the CGL or E&O policies, nor does it require Customer to be named as loss payee on the property policy covering Customer Materials.

**Why it matters:** If a fire or water damage event destroys duplicated drives in Favaiv's facility, the property insurance pays Favaiv (the named insured), not Binond. Without a loss payee endorsement, Binond would need to rely on Favaiv's solvency to pass through the insurance proceeds. Similarly, if a third party sues Binond alleging that a DCP caused harm (however unlikely), the CGL additional insured endorsement would allow Binond to be covered directly under Favaiv's policy.

**Recommended fix:** Add to § 14.1:

> Supplier shall name Customer as an additional insured on the commercial general liability and errors and omissions policies, and shall name Customer as loss payee on the property insurance covering Customer Materials in Supplier's custody. Certificates of insurance shall evidence the foregoing.

---

## 9. SOW Archiving: Vague "Then-Standard Transfer Rates" for Retrieval

**Where:** SOW No. 1 § 6.2.

**Issue:** Section 6.1 requires Supplier to archive DCPs at no charge during the SOW term. Section 6.2 allows Customer to request delivery of archived DCPs "at Supplier's then-standard transfer rates." No rate is specified, and "then-standard" gives Favaiv unilateral pricing power for retrieval.

**Why it matters:** If Binond needs to pull an archived DCP for a re-release, a festival submission, or a platform delivery, it faces an unknown cost. For a distributor managing a catalog, this could add up.

**Recommended fix:** Either specify a maximum rate in the SOW or make retrieval free for a stated period (e.g., 24 months after the original delivery). Proposed language:

> **6.2** On Customer's written request, Supplier shall deliver archived DCPs to Customer or to a destination Customer designates. Retrieval and transfer of archived DCPs requested within twenty-four (24) months of the original delivery date shall be at no charge. Thereafter, Supplier shall charge its then-standard transfer rate, which shall not exceed $[X] per DCP.

**Business decision needed:** Client to confirm whether 24 months is the right window and whether a per-DCP cap is appropriate.

---

## 10. NDA Term and Interaction with Supply Agreement

**Where:** Mutual NDA § 9.1 (2-year term); Supply Agreement § 9.5 (pre-Effective Date information remains subject to the NDA).

**Issue:** The NDA was signed November 17, 2025 and has a 2-year term, expiring November 17, 2027. The Supply Agreement is effective March 2, 2026. Section 9.5 of the Agreement preserves the NDA for pre-Effective Date information. However, the NDA's own confidentiality obligations run for 5 years after the NDA term ends (§ 9.2), so obligations for pre-March 2026 information would run until approximately November 2032. This is workable but creates a layered structure where two different agreements govern confidentiality depending on when information was disclosed, with different definitions, different exclusions, and different procedural requirements.

**Why it matters:** In practice, this is unlikely to cause a dispute, but if a confidentiality claim arises involving information shared during the NDA period (e.g., Favaiv's facility capabilities, pricing proposals, or test encodes), the NDA's terms would apply rather than the Agreement's § 9. The NDA's definition of Confidential Information (§ 1.2) is broader in some respects (it expressly includes "the fact that the Parties are discussing the Purpose") and the care standard is slightly different. This is a low-risk item but worth being aware of.

**Recommended fix:** No change required, but I would recommend that the client's contract management team calendar the NDA expiration (November 17, 2027) and confirm whether the NDA should be terminated early (it can be ended on 30 days' notice under § 9.1) once the Supply Agreement is in full effect, to simplify the confidentiality framework. This is optional.

---

## 11. DPA Precedence Over Supply Agreement Creates Asymmetry

**Where:** Supply Agreement § 2.3(a); DPA § 9.1.

**Issue:** The order of precedence gives the DPA control "as to the processing of personal data." Because the DPA's indemnification (§ 9.1) is broader and more one-sided than the Agreement's (§ 12), and because the DPA prevails in the area of personal data processing, the DPA's customer-favorable indemnity effectively overrides the Agreement's supplier indemnity for any claim that touches personal data. This compounds Issue 1 above.

**Why it matters:** Even if we fix DPA § 9.1 as recommended in Issue 1, we should confirm that the precedence rule is not creating unintended overrides in other areas. For example, the DPA's 24-hour breach notification (§ 7.1) is consistent with the Agreement's § 7.4, so no conflict there. But the point is that the DPA's precedence is a double-edged sword: it protects Customer on data issues (e.g., the sub-processor termination right in § 6.1) but the current indemnification structure turns that precedence against Customer.

**Recommended fix:** Addressed through the fix in Issue 1. No separate change to § 2.3 is needed.

---

## Items Requiring Client Business Decisions

| # | Decision | Context |
|---|----------|---------|
| A | **Exclusivity scope** | Does Binond want to commit to Favaiv as sole worldwide provider for all distribution deliverable types, or should exclusivity be limited to services actually specified in executed SOWs? (Issue 2) |
| B | **Liability cap floor** | What minimum cap is appropriate for the first 12 months? I have suggested $500,000 as a starting point. (Issue 4) |
| C | **Capacity remedy timing** | Are 2-business-day notice and 5-business-day cure windows appropriate for capacity failures, or does the client need shorter windows given release scheduling? (Issue 6) |
| D | **Archival retrieval window** | How long should free retrieval of archived DCPs last? I have suggested 24 months. (Issue 9) |
| E | **Auto-renewal** | Does the client prefer a 60-day notice period with a Supplier reminder obligation, or elimination of auto-renewal entirely? (Issue 7) |

---

## Gaps and Open Items

1. **No SOWs for screeners, KDMs, or drive duplication.** The Agreement contemplates these services (the recitals, § 1.6, and § 7.3 all reference them), and the DPA is built around screener data processing, but no SOW specifies the actual service, pricing, or delivery terms for screeners or KDMs. If the client intends to use Favaiv for screeners (which the DPA strongly implies), a SOW for that service needs to be negotiated before or concurrently with signing. **I would need to see a draft screener SOW if one exists, or confirm whether it will be a later deliverable.**

2. **Favaiv's jurisdiction of organization is not stated.** The Agreement identifies Favaiv as "a corporation" without specifying the state of incorporation. This is a minor point but relevant for the § 11.1(a) representation (duly organized and in good standing). I would recommend confirming Favaiv's state of incorporation and adding it to the preamble.

3. **No SLA or service credits.** The Agreement and SOW contain delivery deadlines and a deemed-acceptance mechanism, but there are no service-level credits or liquidated damages for late delivery. Given that "time of delivery is of the essence" (§ 5.2) for release dates, the client's only remedy for a late DCP is a breach claim subject to the (potentially low) liability cap. **Business decision:** Does the client want to negotiate service credits (e.g., 5% of the affected DCP fee per day of delay, capped at 25%)?

4. **DPA Annex A lists "Customer personnel" as a Data Subject category.** This is unusual and potentially overbroad. If Favaiv is processing Binond employee data (e.g., for portal access to review DCPs), that should be specified. If it is not, the category should be deleted to avoid scope creep. **I would need to confirm with the client whether Favaiv will have any access to Binond employee personal data.**

---

## Conclusion

The two items that I would treat as deal-breakers if not resolved are **(1)** the DPA indemnification structure and **(2)** the mismatch between the exclusivity commitment and the actual SOW scope. The governing law conflict (Issue 3) is a clear drafting error that should be corrected before signing. The remaining items are important but can be addressed in a negotiation round without threatening the deal.

I am available to draft the specific redlines for any of the above upon your instruction.