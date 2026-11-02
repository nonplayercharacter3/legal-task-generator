# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Ziteir Aerial Robotics, Inc. – Contractual Issues Ahead of Okonvale Acquisition

---

## 1. CRITICAL: Supply Agreement § 15.2 Requires Lakix Consent for the Change of Control; the October 15 Letter Misstates the Requirement

**Where:** Supply Agreement § 15.2; Letter to Lakix (Oct. 15, 2026) § 2.

**The problem.** Section 15.2 provides:

> "Any change of control of Supplier, including a merger, consolidation, sale of equity or other transaction in which more than 50% of Supplier's voting equity changes hands, **is deemed an assignment** of this Agreement. Any such assignment requires Lakix's prior written consent. Failure to obtain that consent is a material breach of this Agreement and entitles Lakix to terminate this Agreement by written notice and to recover its damages."

The described transaction—a merger in which a subsidiary of Okonvale merges with and into Ziteir, with Okonvale acquiring all outstanding equity of Ziteir—falls squarely within the definition of "change of control" in § 15.2. The "deemed an assignment" language is expressly designed to capture transactions where the contractual entity survives but its ownership changes.

The letter, however, states in § 2: "Ziteir will remain the same legal entity after closing… Ziteir will not assign or transfer the Agreement… Accordingly, **no consent of Lakix is required** in connection with the Transaction."

This reasoning is inconsistent with the plain text of § 15.2. The section does not require an actual transfer of the agreement; it deems the change of control itself to be an assignment. The letter's position is, with respect, wrong as a matter of contract interpretation.

**Why it matters.** If Lakix's counsel identifies this discrepancy (and they almost certainly will, either upon reviewing the letter or during their own pre-signing diligence), Lakix could:

- Refuse to give consent;
- Declare Ziteir in material breach;
- Terminate the Supply Agreement, the DPA, and the SOW; and
- Pursue damages.

Given that the Initial Term runs through February 28, 2027 and the agreement auto-renews for three-year periods (§ 2.2), loss of this customer would be material. The letter has already been sent, which compounds the problem: Ziteir has affirmatively told Lakix that consent is not required, which could be characterized as a bad-faith attempt to circumvent the consent right.

**Recommended fix.**

- Before closing (November 30, 2026), Ziteir should contact Lakix and request written consent under § 15.2, acknowledging that the letter's statement in § 2 was incorrect. A short follow-up letter or email from Ziteir's General Counsel correcting the record and requesting consent is the cleanest approach.
- If Lakix is amenable (the commercial relationship appears stable, and the letter's substantive commitments in § 3—continued supply, same team, same sub-processors—should reassure them), obtain a signed consent or a written acknowledgment that Lakix does not object.
- If Lakix resists or demands concessions (e.g., price protections, term extension, termination rights), Ziteir should assess whether to negotiate or to accept the risk of a post-closing dispute.
- In any event, Ziteir should not proceed to closing without either (a) Lakix's written consent, or (b) a documented legal analysis supporting the position that § 15.2 does not apply, if one can be sustained. I am not able to identify one from the contract language as drafted.

**Ambiguity flag.** It is possible that Ziteir's counsel who drafted the letter relied on a theory that a surviving-entity merger is not a "change of control" because the contractual party does not change. That theory is not supported by the text of § 15.2, which uses the phrase "change of control of Supplier" without limiting it to transactions where the Supplier entity ceases to exist. If Ziteir's deal team has a different understanding of § 15.2 based on negotiations or side letters not in this folder, please provide those.

---

## 2. SOW 001 Governing Law and Forum Differ from the Supply Agreement

**Where:** SOW 001 § 9.1–9.2; Supply Agreement §§ 18.1–18.2; Supply Agreement § 18.3 (Order of Precedence).

**The problem.** The SOW specifies New York governing law and exclusive jurisdiction in Manhattan (SOW § 9.1–9.2). The Supply Agreement specifies Delaware governing law and exclusive jurisdiction in New Castle County (Supply Agreement §§ 18.1–18.2). The order of precedence in Supply Agreement § 18.3 resolves the conflict: "Data Processing Addendum, then Statement of Work, then Supply Agreement." So for disputes relating to the SOW Services, New York law and the Manhattan forum control.

**Why it matters.** This creates a split-regime for what is effectively a single commercial relationship. In a dispute that implicates both the SOW (e.g., quality of training or commissioning) and the Supply Agreement (e.g., product warranty, payment), the parties could litigate in two forums under two bodies of law. Post-acquisition, if Okonvale inherits this relationship, its outside counsel will need to be comfortable working in both Delaware and New York. More practically, if Lakix terminates based on the § 15.2 issue (see Item 1 above), the termination right arises under the Supply Agreement (Delaware law), but any counterclaim for defective Services would arise under the SOW (New York law).

**Recommended fix.** This is a pre-existing drafting issue, not something the acquisition creates. However, if Ziteir negotiates the consent request with Lakix (Item 1), it may be an opportunity to propose a conforming amendment to align the SOW's governing law and forum with the Supply Agreement. If no amendment is practical before closing, flag this to Okonvale in the acquisition diligence so they are not surprised.

---

## 3. DPA § 8.2: Uncapped, Strict-Liability Indemnity for Security Incidents

**Where:** DPA §§ 8.1–8.2; Supply Agreement § 11.1 (cap).

**The problem.** DPA § 8.2 states:

> "Processor's obligations under Section 8.1 apply to each Security Incident, **whether or not caused by Processor's fault**, and **shall not be subject to any limitation of liability in the Agreement**."

This is a strict-liability, uncapped indemnity. If a Security Incident occurs—whether caused by Ziteir, a sub-processor, a cybercriminal, or even Lakix's own personnel—Ziteir must defend and indemnify Lakix, its Affiliates, and each Grower for all resulting losses, including regulatory fines, notification costs, credit monitoring, and third-party claims.

**Why it matters.** This is a contingent liability that Okonvale will inherit at closing. It is not capped by the 12-month-fee limitation in Supply Agreement § 11.1. For a company processing agricultural telemetry data (field boundaries, geolocation, chemical application records, personal data of growers and their personnel), a serious breach could generate eight- or nine-figure exposure. The DPA's survival clause (§ 10.2) keeps this obligation alive as long as any Grower Data is retained.

**Recommended fix.**

- Ensure this exposure is disclosed in the acquisition diligence materials and reflected in any indemnity or escrow arrangements in the merger agreement with Okonvale.
- Confirm that Ziteir's cyber liability insurance (required at $3,000,000 under Supply Agreement § 13(c)) is adequate for this exposure. Given the uncapped nature of the DPA indemnity, $3 million may be insufficient. If Okonvale's risk team agrees, consider negotiating a higher cyber limit or a specific endorsement for the Lakix relationship.
- Post-closing, if Okonvale plans to consolidate data infrastructure or change sub-processors, be aware that any Security Incident during a migration would trigger this indemnity. Coordinate with DPA § 5.2 notice requirements (see Item 5 below).

---

## 4. Pellbrook Lease § 11.2(c): Post-Closing Notice Deadline

**Where:** Pellbrook Lease § 11.2(c); § 15 (Notices).

**The problem.** Section 11.2(c) permits Ziteir to undergo "any transfer of its equity interests or any change of control, including by merger" without Landlord's consent, but requires "written notice to Landlord **within 30 days after the transaction**."

**Why it matters.** This is a hard administrative deadline. If the closing occurs on November 30, 2026, Ziteir must deliver written notice to Pellbrook Airfield Properties, LLC by approximately December 30, 2026. Failure to give timely notice could be characterized as a default under § 12.1(b) (failure to perform an obligation within 30 days after written notice), though the practical consequence would likely be limited to a cure period.

**Recommended fix.** Calendar the notice deadline immediately. Prepare the notice letter now so it can be sent promptly after closing. The notice should go to: Pellbrook Airfield Properties, LLC, 900 Runway View Drive, Middletown, Delaware 19709, Attention: Property Manager (per § 15). No consent is needed—this is purely informational.

---

## 5. DPA § 5.2: Sub-Processor Change Risk Post-Closing

**Where:** DPA § 5.2; Letter to Lakix § 3(d).

**The problem.** The letter commits that "the Sub-processors listed in Annex 3 to the Data Processing Addendum will not change as a result of the Transaction" and that any future change will follow the § 5.2 notice process. Section 5.2 gives Lakix 15 days to object to a new sub-processor on "reasonable data protection grounds." If the objection cannot be resolved within 30 days, "Lakix may terminate the affected Platform subscriptions without penalty."

**Why it matters.** Acquirers frequently rationalize IT and cloud infrastructure post-closing. If Okonvale wants to migrate the ZiteirLink Platform to its own cloud environment, add a new analytics vendor, or consolidate support tooling, each change triggers the § 5.2 process. A single unresolved objection could allow Lakix to walk away from its Platform subscriptions (at $1,400 per Drone per year, per Exhibit B) without penalty, which would undermine the letter's commitment to continuity.

**Recommended fix.**

- Before closing, identify any sub-processor changes Okonvale is planning in the first 12 months post-closing. If any are contemplated, either (a) defer them until after the § 5.2 process has been completed with Lakix, or (b) give the 30-day advance notice to Lakix pre-closing so the objection window runs before the relationship is in flux.
- Brief Okonvale's IT and data teams on this constraint so they do not inadvertently trigger a termination right.

---

## 6. Supply Agreement § 2.2: Auto-Renewal Notice Deadline Falls Shortly After Closing

**Where:** Supply Agreement §§ 2.1–2.2.

**The problem.** The Initial Term ends February 28, 2027. The agreement auto-renews for successive three-year terms unless either party gives written notice of non-renewal at least 30 days before the end of the then-current term. The non-renewal notice deadline is therefore approximately **January 29, 2027**—only about two months after the expected November 30, 2026 closing.

**Why it matters.** If the § 15.2 consent dispute (Item 1) is not resolved amicably, Lakix could use the approaching renewal date as leverage: threaten non-renewal, or condition consent on renewal terms. Conversely, if Ziteir/Okonvale wants to exit the relationship (e.g., if Okonvale has a competing product line), the window to do so cleanly is narrow.

**Recommended fix.** Decide now, as part of the acquisition integration planning, whether Ziteir/Okonvale intends to renew or not. If renewing, resolve the § 15.2 consent issue well before January 29, 2027. If not renewing, calendar the notice deadline and prepare the non-renewal notice. Either way, do not let this date pass by default.

---

## 7. SOW 001 Phase 3 Spans the Closing Date

**Where:** SOW 001 § 3 (Phases table); Letter § 3(c).

**The problem.** Phase 3 (fleet expansion, up to 6 Drones, all Sites) has a Services Window of September 1, 2026 to February 28, 2027, and a Season Support Window of October 1, 2026 to November 30, 2026. The expected closing date—November 30, 2026—is the **last day** of the Phase 3 Season Support Window.

The letter commits that "Deployment, commissioning and pilot training under Statement of Work No. 001 will continue on the existing schedule, using the same Ziteir project team" (§ 3(c)).

**Why it matters.** The transition from Ziteir-as-independent to Ziteir-as-Okonvale-subsidiary occurs at the exact moment Phase 3's active support period ends and its commissioning/expansion work continues into 2027. Any disruption to the project team (Priya N. Calloway, per SOW § 6.1(a)) or to the season support structure (dedicated field engineer, 6 a.m.–8 p.m. ET, seven days a week, per SOW § 2.6) during this window could constitute a failure to perform the SOW. Lakix's acceptance rights under SOW § 4.2 (deemed acceptance if no response within 10 business days of the end-of-phase report) mean that a botched Phase 3 could generate a dispute.

**Recommended fix.** Confirm with Ziteir's deployment team that the Phase 3 project plan accounts for the ownership transition. Ensure the project manager and field support engineer are committed through at least the end of Phase 3's Services Window (February 28, 2027). If Okonvale plans any headcount changes or reorganizations effective at closing, defer them for the Ziteir deployment team until Phase 3 is complete and accepted.

---

## 8. SOW 001 § 10.1: Ambiguous Incorporation of Supply Agreement Provisions

**Where:** SOW 001 § 10.1; Supply Agreement § 15.

**The problem.** SOW § 10.1 states: "This SOW forms part of the Agreement. Sections 11 (Limitation of Liability), 12 (Confidentiality), 16 (Force Majeure) and 17 (Notices) of the Agreement apply to this SOW."

The first sentence makes the SOW part of the Agreement. The second sentence enumerates only four sections as applying to the SOW. Read together, these create ambiguity: does the enumeration mean that *only* those four sections apply to the SOW (excluding, e.g., § 15 Assignment), or is it a non-exhaustive clarification of sections that might otherwise be unclear?

**Why it matters.** This bears directly on Item 1. If § 15.2 does not apply to the SOW (because it is not among the enumerated sections), then the change of control consent requirement attaches only to the Supply Agreement and DPA, not to the SOW. That would narrow—but not eliminate—the consent issue. However, the stronger reading is that the SOW is "part of the Agreement" and therefore all Agreement provisions apply, with the enumeration being illustrative rather than exhaustive.

**Recommended fix.** Flag this ambiguity to Ziteir's deal team. If the consent request to Lakix (Item 1) is being negotiated, be prepared for Lakix's counsel to argue that § 15.2 applies to the entire agreement structure including the SOW. Do not rely on the narrower reading unless Lakix agrees to it.

---

## 9. Supply Agreement § 3.2: Deemed Acceptance of Purchase Orders – Operational Risk During Transition

**Where:** Supply Agreement § 3.2.

**The problem.** "Ziteir will accept or reject each Purchase Order in writing within five business days after receipt. If Ziteir does not respond within that period, the Purchase Order is **deemed accepted**."

**Why it matters.** During the ownership transition, if Ziteir's order-management processes are disrupted (system changes, staff reassignments, attention diverted to integration), there is a risk of inadvertently accepting Purchase Orders by simply failing to respond within five business days. Each deemed-accepted PO creates a binding delivery obligation at fixed prices (Exhibit B).

**Recommended fix.** Ensure that the order-acceptance workflow for Lakix Purchase Orders remains staffed and functional through and after the closing. If any system migration is planned, implement a manual override or extended-response protocol for Lakix POs during the transition period.

---

## 10. Items Requiring Additional Context

The following points could not be fully assessed from the documents in the folder:

| # | Item | What I need |
|---|------|------------|
| 10.1 | **Merger agreement with Okonvale.** The letter describes the transaction structure (subsidiary merges into Ziteir, Ziteir survives). I have not seen the merger agreement itself. If it contains conditions precedent, regulatory approvals, or a different expected closing date, the analysis in Items 1, 4, 6, and 7 may need adjustment. | A copy of the merger agreement or at least the key terms (structure, closing date, conditions). |
| 10.2 | **Whether Ziteir has previously given § 15.2 consent requests or whether Lakix has previously raised the change-of-control issue.** If there is a course of dealing or prior waiver, the analysis changes. | Any prior correspondence with Lakix regarding assignment or change of control. |
| 10.3 | **Okonvale's post-closing integration plans** for IT infrastructure, sub-processors, and personnel. This affects Items 5 and 7. | A summary of Okonvale's 100-day plan or integration roadmap, if available. |
| 10.4 | **Ziteir's current cyber insurance policy.** I noted the contractual minimum ($3M) in Supply Agreement § 13(c), but I have not seen the actual policy. The DPA's uncapped indemnity (Item 3) may exceed the policy limit. | The current cyber liability policy or a broker summary. |
| 10.5 | **Whether the Pellbrook lease has been assigned or noticed in connection with any prior Ziteir corporate event.** If Ziteir has previously undergone a change of control (e.g., a financing round) and given notice under § 11.2, that would confirm the operational process. | Confirmation from Ziteir's facilities or legal team. |

---

## Summary of Recommended Actions (Priority Order)

| Priority | Action | Deadline |
|----------|--------|----------|
| **1** | Seek Lakix's written consent under Supply Agreement § 15.2; correct the October 15 letter's misstatement. | Before November 30, 2026 closing |
| **2** | Confirm Phase 3 project team continuity through February 28, 2027. | Before closing |
| **3** | Calendar and prepare Pellbrook § 11.2(c) notice. | Within 30 days after closing (~Dec. 30, 2026) |
| **4** | Identify any planned sub-processor changes; if any, give DPA § 5.2 notice or defer. | Before or immediately after closing |
| **5** | Calendar Supply Agreement § 2.2 non-renewal decision. | By January 29, 2027 |
| **6** | Confirm PO acceptance workflow remains functional through transition. | Ongoing |
| **7** | Disclose DPA § 8.2 uncapped indemnity in acquisition diligence; assess cyber insurance adequacy. | Before closing |