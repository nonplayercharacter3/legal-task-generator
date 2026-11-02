# MEMORANDUM

**To:** Partner
**From:** Associate
**Re:** Ziteir Aerial Robotics, Inc. — Contractual Issue Identification (Lakix Supply Agreement; Pellbrook Hangar Lease)
**Date:** [Current]

---

## Issue 1: Change-of-Control Consent Requirement — Supply Agreement § 15.2 vs. October 15, 2026 Letter

**Where:** Supply Agreement, Section 15.2 (Change of Control); Letter to Lakix dated October 15, 2026, Section 2.

**The problem.** Section 15.2 provides that "[a]ny change of control of Supplier, including a merger, consolidation, sale of equity or other transaction in which more than 50% of Supplier's voting equity changes hands, is deemed an assignment of this Agreement" and "requires Lakix's prior written consent." It further states that failure to obtain consent "is a material breach of this Agreement and entitles Lakix to terminate this Agreement by written notice and to recover its damages."

The letter (Section 2) asserts the opposite: "Ziteir will remain the same legal entity after closing … Ziteir will not assign or transfer the Agreement … Accordingly, no consent of Lakix is required in connection with the Transaction." The letter is framed as informational only and does not seek consent.

The described deal structure — a wholly owned Okonvale subsidiary merging with and into Ziteir, with Ziteir surviving as a wholly owned subsidiary of Okonvale and Okonvale acquiring all outstanding equity — is unambiguously a change of control under Section 15.2. The fact that Ziteir remains the same legal entity does not avoid the provision, which is triggered by the change in who holds more than 50% of Ziteir's voting equity, not by a transfer of the contract itself.

**Why it matters.** If Lakix asserts (post-closing or at any time) that Section 15.2 was triggered and that Ziteir failed to obtain consent, Lakix has the right to terminate the entire Supply Agreement and claim damages. The Initial Term runs through February 28, 2027, and the agreement auto-renews for three-year terms (Section 2.2), so the revenue at stake includes the full Platform subscription base, ongoing drone and spare parts sales, and SOW 001 Phase 3 fees. The letter, rather than protecting Ziteir, may be used as evidence that Ziteir proceeded without the required consent while affirmatively representing that none was needed.

**Recommended fix.** Before closing, Ziteir should:

1. Seek Lakix's written consent to the change of control under Section 15.2. The October 15 letter can be supplemented with a consent request. Given the letter has already been delivered, a follow-up letter or email (satisfying § 17.1) requesting consent and explaining the continuity commitments in the original letter would be appropriate.
2. If Lakix consents, obtain a signed consent or a written acknowledgment that constitutes consent under the Agreement.
3. If Lakix refuses or does not respond, assess whether the refusal is reasonable and consider whether to (a) condition the merger closing on obtaining consent, (b) negotiate a waiver, or (c) accept the termination risk and price it into the deal.
4. Revise the October 15 letter's Section 2 language (or issue a corrected letter) to remove the assertion that no consent is required, or at minimum to state that Ziteir is seeking consent in accordance with Section 15.2.

**Flag for partner:** The letter was signed by the CEO and sent before (presumably) this issue was identified. If the deal team believed the letter was sufficient, that assumption is not supported by the contract text. I recommend confirming with the deal team whether any consent request was made separately or whether the letter was intended to serve as that request.

---

## Issue 2: Uncapped Strict-Liability Data Indemnity — DPA § 8.2

**Where:** Data Processing Addendum, Sections 8.1 and 8.2.

**The problem.** Section 8.1 requires Ziteir (as Processor) to defend and indemnify Lakix, its Affiliates, and each Grower against all losses arising from any Security Incident involving Grower Data, including regulatory fines, notification costs, credit monitoring, forensic investigation, and third-party claims. Section 8.2 states this indemnity applies "whether or not caused by Processor's fault" and "shall not be subject to any limitation of liability in the Agreement."

The Supply Agreement's liability cap (§ 11.1) is limited to fees paid in the preceding 12 months. The DPA's order of precedence is highest under Supply Agreement § 18.3, so the uncapped strict-liability indemnity overrides the cap.

"Security Incident" is defined broadly (DPA § 1.7) to include "any actual or reasonably suspected unauthorized access to, or acquisition, use, disclosure, alteration, loss or destruction of, Grower Data."

**Why it matters.** This is a significant, uncapped contingent liability that transfers to Ziteir's balance sheet (and therefore to Okonvale post-closing). A single data breach affecting Lakix's grower clients could generate regulatory fines (multiple state data protection laws apply under DPA § 1.2), notification costs for potentially hundreds of growers, credit monitoring, and third-party class claims — all indemnifiable by Ziteir regardless of fault. The insurance in Supply Agreement § 13(c) provides $3M in cyber liability coverage, which may be insufficient for a large-scale incident.

**Recommended fix.**

1. Confirm that Ziteir's current cyber liability policy ($3M minimum under § 13(c)) is actually in force and that the limit is adequate for the scale of data held. Request a copy of the policy and any claims-made endorsements.
2. In the acquisition agreement or a side letter, seek an Okonvale indemnity or escrow for pre-closing data incidents, or at minimum ensure the purchase price reflects this exposure.
3. Post-closing, evaluate whether to negotiate an amendment to DPA § 8.2 to (a) limit the indemnity to incidents caused by Ziteir's breach of its security obligations, or (b) subject it to the cyber insurance limit. This would require Lakix's agreement and may be resisted given the DPA's precedence position.
4. Verify that the security measures in DPA Annex 2 are actually implemented and current (annual pen test, MFA, encryption, etc.), since a failure to maintain those measures would make a "no fault" indemnity claim easier for Lakix to bring.

---

## Issue 3: Conflicting Governing Law and Forum — SOW 001 § 9 vs. Supply Agreement § 18

**Where:** SOW 001, Section 9 (Governing Law and Forum); Supply Agreement, Sections 18.1–18.2 and 18.3 (Order of Precedence).

**The problem.** The Supply Agreement is governed by Delaware law with exclusive jurisdiction in New Castle County, Delaware (§§ 18.1–18.2). SOW 001 is governed by New York law with exclusive jurisdiction in the Borough of Manhattan (§ 9.1–9.2). Under the Supply Agreement's order of precedence (§ 18.3), the SOW ranks above the Supply Agreement. Therefore, for any dispute arising out of the Services under SOW 001, New York law and Manhattan forum control.

**Why it matters.** This creates a split-regime: product warranty, pricing, and platform disputes go to Delaware; services disputes (commissioning, training, season support) go to New York. If a single factual scenario gives rise to claims under both the Supply Agreement and the SOW (e.g., a drone fails during a training flight, implicating both product warranty and the services), the parties could end up litigating in two forums under two bodies of law. This complicates defense strategy and increases cost. It also means Ziteir's New York law exposure for services disputes is governed by a legal regime the deal team may not have fully analyzed.

**Recommended fix.**

1. Flag this to the deal team as a known structural issue. It does not require a fix before closing, but Okonvale's litigation budget and insurance program should account for potential New York forum exposure.
2. Post-closing, consider whether to negotiate a conforming amendment to SOW 001 § 9 to align with the Supply Agreement's Delaware governing law and forum. This is low-priority if Phase 3 is the last active phase and the SOW will wind down by February 28, 2027.

---

## Issue 4: Active Service Obligations at Closing — SOW 001 Phase 3

**Where:** SOW 001, Section 3 (Phases and Schedule), Section 2.6 (Season Support), Section 7.1 (Fees).

**The problem.** Phase 3 (fleet expansion at all Sites, up to 6 additional Drones) has a Services Window of September 1, 2026 to February 28, 2027, and a Season Support Window of October 1, 2026 to November 30, 2026. The expected closing date is November 30, 2026. At closing, Ziteir will be:

- In the final day of the Phase 3 Season Support Window (obligated to provide a dedicated field support engineer 6 a.m.–8 p.m. ET, seven days a week, and on-site support within 24 hours — § 2.6);
- Mid-way through the Phase 3 Services Window (commissioning, training, and Platform configuration for up to 6 additional Drones — §§ 2.2, 2.3, 2.4);
- Accruing season support fees at $9,500/month (§ 7.1) through November 30, 2026.

**Why it matters.** Okonvale inherits active performance obligations at closing. If the change-of-control issue (Issue 1) causes Lakix to terminate, Ziteir would need to wind down Phase 3 mid-stream, potentially triggering cure obligations under SOW § 4.2 and the Supply Agreement § 14.3. Even absent termination, the transition of the project team (SOW § 6.1 names specific Project Managers) during an active phase creates operational risk.

**Recommended fix.**

1. Confirm that the Ziteir project team (Priya N. Calloway and her staff) is committed through Phase 3 completion or that a transition plan is in place.
2. Ensure the October 15 letter's representation in Section 3(c) ("Deployment, commissioning and pilot training under Statement of Work No. 001 will continue on the existing schedule, using the same Ziteir project team") is accurate and that Okonvale has not planned any headcount changes that would undermine it.
3. Track the Phase 3 deliverables and acceptance (SOW § 4.2) to confirm the SOW will be fully performed and accepted before the Initial Term ends on February 28, 2027, so that the SOW does not remain open into the Renewal Term.

---

## Issue 5: Automatic Renewal — Supply Agreement § 2.2

**Where:** Supply Agreement, Section 2.2 (Renewal).

**The problem.** The Initial Term ends February 28, 2027. The agreement auto-renews for successive three-year terms unless either party gives written notice of non-renewal at least 30 days before the end of the then-current term. The deadline for Ziteir (or Okonvale, post-closing) to prevent renewal is therefore January 29, 2027.

**Why it matters.** If no notice is given, the agreement locks in for three additional years (through February 28, 2030) on the same fixed pricing (Exhibit B, § 4.2). For the buyer, this is both a revenue asset (committed Platform subscription fees of $1,400/Drone/year, plus drone and spare parts purchases) and a constraint (fixed pricing may become uncompetitive; the change-of-control consent issue could resurface at the renewal boundary if the relationship has deteriorated). For the seller, it is a reason to ensure the consent issue is resolved before the renewal date, not after.

**Recommended fix.**

1. Calendar the January 29, 2027 non-renewal deadline.
2. As part of resolving Issue 1, consider whether to seek Lakix's consent to the change of control on terms that also address the renewal (e.g., a consent that is effective for the Initial Term and any Renewal Term).
3. If Okonvale's strategic plan includes re-pricing or restructuring the Lakix relationship, note that the fixed-pricing provision (§ 4.2) runs for the full Term, including Renewal Terms.

---

## Issue 6: Pellbrook Lease — Permitted Transfer and Notice Obligation

**Where:** Pellbrook Hangar Lease, Section 11.2 (Permitted Transfers).

**The problem (favorable, but action required).** Section 11.2 permits Ziteir to, without Landlord's consent: (a) assign to an affiliate; (b) assign to a merger survivor or asset purchaser; or (c) "undergo any transfer of its equity interests or any change of control, including by merger." The Okonvale transaction falls squarely within 11.2(b) and (c). However, Ziteir must give Landlord written notice within 30 days after the transaction.

**Why it matters.** This is a compliance step, not a risk. Failure to give timely notice could technically constitute a default under § 12.1(b) (failure to perform an obligation within 30 days after written notice), though the practical consequence would be minimal. More importantly, confirming that no consent is needed (unlike the Lakix agreement) gives the deal team comfort that the hangar lease does not present a closing condition or consent risk.

**Recommended fix.**

1. Prepare the notice to Pellbrook Airfield Properties, LLC for delivery within 30 days after closing (by approximately December 30, 2026). The notice should identify the transaction and confirm that Ziteir remains the tenant of record.
2. No consent or amendment is required.

---

## Issue 7: Pellbrook Lease — Extension Option Deadline

**Where:** Pellbrook Hangar Lease, Section 3.2 (Option to Extend).

**The problem.** Ziteir has a one-time option to extend the lease for five additional years. The option must be exercised by written notice given no earlier than 12 months and no later than 9 months before the Expiration Date (January 31, 2029). This creates a narrow window:

- No earlier than: January 31, 2028 (12 months before expiration)
- No later than: April 30, 2028 (9 months before expiration)

If the notice is not given within this window, the option lapses and the lease ends January 31, 2029.

**Why it matters.** Okonvale will need to decide whether to extend. The decision requires knowledge of Ziteir's long-term facility needs, which may not be clear at closing. Missing the window would force Ziteir to relocate its hangar operations (14,200 sq. ft. hangar + 3,800 sq. ft. office/workshop + 6,000 sq. ft. apron) on relatively short notice, with significant disruption to operations and the Lakix SOW (which uses the Dover Base as a Site, though the Pellbrook facility appears to be Ziteir's own operational base).

**Recommended fix.**

1. Calendar the extension window (January 31 – April 30, 2028) as a critical decision point for Okonvale.
2. Begin internal planning in Q3 2027 to assess whether the facility will still meet post-acquisition needs.
3. Note that Extension Term rent is 95% of fair market rent (§ 3.3), determined by the parties or a broker if they cannot agree. This is a reasonable mechanism but should be budgeted.

---

## Issue 8: Pellbrook Lease — Hazardous Materials Restriction

**Where:** Pellbrook Hangar Lease, Section 6.4 (Hazardous Materials).

**The problem.** Section 6.4 prohibits Ziteir from storing or using "agricultural chemicals or pesticides at the Premises, other than sealed sample containers kept in a fire-rated cabinet." Ziteir's business involves spray drones that apply agricultural chemicals. The SOW 001 commissioning process (§ 2.2(c)) requires calibrating the spray system "to the product labels Lakix supplies," and the test flight uses water (§ 2.2(e)), so the SOW as drafted does not require chemical storage at the Pellbrook facility. However, if Ziteir ever wants to conduct chemical application testing, demonstrations, or R&D at the hangar, it is limited to sealed sample containers in the fire-rated cabinet (which Landlord's Work in Exhibit B, item 3, provides: a ~300 sq. ft. fire-rated battery storage room with dedicated ventilation — though this is specified for batteries, not chemicals).

**Why it matters.** This is a use restriction that could constrain Ziteir's operational flexibility at the Pellbrook facility. If Okonvale's integration plan involves consolidating testing or demonstration activities at the hangar, this restriction would need to be addressed.

**Recommended fix.**

1. Confirm with Ziteir operations whether any current or planned activities at Pellbrook involve agricultural chemicals beyond sealed samples.
2. If chemical storage or use beyond samples is needed, negotiate an amendment to § 6.4 before the extension option is exercised (or as a separate matter). Landlord's consent would be required, and the Airfield Rules (Exhibit C) and local fire marshal requirements would also be relevant.

---

## Issue 9: Insurance Obligations — Supply Agreement § 13

**Where:** Supply Agreement, Section 13 (Insurance).

**The problem.** Ziteir is obligated to maintain during the Term: (a) $5M CGL including products liability; (b) $5M aviation liability for Drones while Ziteir personnel operate them; and (c) $3M cyber liability. These are ongoing obligations that survive the acquisition.

**Why it matters.** Okonvale should confirm that Ziteir's current policies meet these minimums and that they will be maintained (or replaced with equivalent coverage) post-closing. A gap in coverage would be a breach of the Supply Agreement and could also undermine the DPA indemnity (Issue 2) if a data incident exceeds the cyber policy limit. The aviation liability requirement is particularly relevant given that Ziteir personnel operate Drones during commissioning and training under SOW 001.

**Recommended fix.**

1. As part of pre-closing diligence, obtain copies of Ziteir's current CGL, aviation liability, and cyber liability policies and confirm limits meet or exceed the contractual minimums.
2. Confirm that the policies will not be cancelled or materially reduced at or after closing.
3. Note that the Pellbrook lease separately requires $2M CGL / $4M aggregate, $5M aviation liability, property insurance, and workers' comp (Lease § 9.1). The Supply Agreement's $5M CGL minimum should satisfy the lease's lower requirement, but the policies should be checked for consistency.

---

## Issue 10: Sub-Processor Change Risk Post-Closing — DPA § 5.2

**Where:** Data Processing Addendum, Section 5.2 (Notice of New Sub-processors); Annex 3 (Authorized Sub-processors).

**The problem.** The current sub-processors are AWS (cloud hosting), Twilio (SMS/email), and Zendesk (support ticketing), all in the United States. If Okonvale's integration plan involves migrating Ziteir's infrastructure to a different cloud provider, consolidating support functions, or changing communication tools, each change would trigger the 30-day notice requirement in DPA § 5.2. Lakix may object on "reasonable data protection grounds," and if the objection cannot be resolved within 30 days, Lakix may terminate the affected Platform subscriptions without penalty.

**Why it matters.** The October 15 letter (Section 3(d)) represents that the sub-processors "will not change as a result of the Transaction" and that any future change will follow DPA § 5.2. If Okonvale's post-closing integration plan includes infrastructure changes, this representation could be breached or the letter could be used against Ziteir. More practically, losing Lakix's Platform subscriptions would eliminate $1,400/Drone/year in recurring revenue for each affected Drone.

**Recommended fix.**

1. Confirm with Okonvale's IT integration team whether any sub-processor changes are planned in the 12 months post-closing.
2. If changes are planned, build the 30-day notice and potential objection process into the integration timeline.
3. If no changes are planned, the letter's representation is safe and no action is needed.

---

## Summary of Action Items by Priority

| Priority | Issue | Action | Deadline |
|----------|-------|--------|----------|
| **Critical** | #1 — Change of control consent | Obtain Lakix's written consent under § 15.2 before closing | Before Nov 30, 2026 |
| **High** | #2 — Uncapped data indemnity | Confirm cyber insurance adequacy; consider deal protection | Before closing |
| **High** | #4 — Phase 3 active at closing | Confirm project team continuity; plan for transition | Before closing |
| **Moderate** | #5 — Auto-renewal | Calendar Jan 29, 2027 deadline; address in consent negotiation | Jan 29, 2027 |
| **Moderate** | #9 — Insurance | Verify current policies meet contractual minimums | Before closing |
| **Low** | #3 — SOW governing law conflict | Note for litigation planning; consider post-closing amendment | Post-closing |
| **Low** | #6 — Pellbrook notice | Deliver notice to Landlord within 30 days post-closing | By ~Dec 30, 2026 |
| **Low** | #7 — Pellbrook extension option | Calendar decision window; begin planning Q3 2027 | Jan 31 – Apr 30, 2028 |
| **Low** | #8 — Pellbrook hazmat restriction | Confirm no operational conflict | Post-closing |
| **Low** | #10 — Sub-processor changes | Confirm with Okonvale IT team | Post-closing |

---

## Ambiguities and Items Requiring Further Context

1. **Was a consent request made to Lakix separate from the October 15 letter?** The letter is framed as informational. If the deal team intended it to serve as a consent request, that intention is not clear from the text. I need to confirm with the deal team.

2. **What is the structure of the Okonvale merger?** The letter describes a reverse triangular merger (Okonvale sub merges into Ziteir, Ziteir survives). I have not seen the merger agreement. If the structure is different (e.g., a forward merger where Ziteir is the target and disappears), the analysis under § 15.2 could be affected, though the "sale of equity" and "more than 50% of voting equity changes hands" language would likely still be triggered.

3. **Does Ziteir have other customer agreements with similar change-of-control provisions?** The partner's instruction focuses on Lakix and Pellbrook, but if Ziteir has other material contracts with change-of-control or assignment restrictions, those would need similar analysis. I have not been provided with other customer agreements.

4. **Pellbrook lease — is the Dover Base (SOW 001 § 1.3(a)) the same as or related to the Pellbrook facility?** The SOW lists the Dover Base at 1275 Harvest Mill Road, Dover, DE (which is Lakix's own address). The Pellbrook facility is at 900 Runway View Drive, Middletown, DE. These appear to be different locations. I have assumed the Pellbrook hangar is Ziteir's own operational facility (for storage, assembly, maintenance, testing, and training per the Permitted Use in Lease § 1.7) and not a Lakix Site. If Ziteir uses Pellbrook to support SOW 001 Services (e.g., as a staging area or for training), the hazmat restriction (Issue 8) becomes more significant.

5. **Exhibit A to the Supply Agreement is cut off** at "one ground" (page 3). I was unable to read the full list of standard accessories or the complete Platform description. If there are additional service level commitments or product specifications in the remainder of Exhibit A, I have not reviewed them.