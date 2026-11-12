# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Namaith Facade Systems, Inc. – License Package with Lavas Glazing Software, LLC: Issue Identification

---

## Summary

I have reviewed all five documents in the matter folder. The package contains several material issues, the most significant of which are (1) Amendment No. 1's restatement of Section 10.3, which quietly removes Licensor's IP indemnity from the liability-cap exceptions and narrows the confidentiality exception; (2) the Licensee indemnity in Section 9.2, which is far broader and more onerous than the Term Sheet contemplated and is uncapped; and (3) the pending Orvand Partners acquisition of Namaith's parent, which triggers a Licensor termination right that has not been addressed. I have identified 14 issues in total, set out below in roughly descending order of practical importance.

---

## Issue 1: Amendment No. 1 Restates Section 10.3 to Remove Licensor's IP Indemnity from the Cap Exceptions

**Where:** `license_amendment_no_1.md`, Section 2 (restating Section 10.3 of the Agreement); compare `namaith_lavas_software_license_agreement.md`, Section 10.3 (original); `glazecore_license_term_sheet.md`, Item 7.

**Original Section 10.3 exceptions (four):**
- (a) Licensee's indemnification under § 9.2
- (b) **Licensor's indemnification under § 9.1**
- (c) **Either Party's** breach of § 7
- (d) Licensee's obligation to pay fees

**Restated Section 10.3 exceptions (three):**
- (a) Licensee's indemnification under § 9.2
- (b) **Licensee's** breach of § 7
- (c) Licensee's obligation to pay fees

**Why it matters:** Two protections are gone:

1. **Licensor's IP indemnity (§ 9.1) is now subject to the cap.** Under the original agreement, if a third party sued Namaith alleging the GlazeCore software infringed its IP, Lavas's defense and indemnity obligations were uncapped. Now they are capped at "fees paid or payable in the 12 months preceding the claim" (§ 10.1) — approximately $1,405,000 (the $1,240,000 base fee plus the $165,000 ThermaStress module fee). An IP infringement defense in the facade-engineering space could easily exceed that amount in attorneys' fees alone, before any settlement or judgment. Namaith would bear the excess.

2. **Licensor's breach of confidentiality is now capped.** Under the original § 10.3(c), *either* party's breach of § 7 was excluded from the cap. Now only *Licensee's* breach is excluded. If Lavas misuses or discloses Namaith's Licensee Data (project designs, tempering parameters, customer specifications), Namaith's recovery is capped at ~$1.4M regardless of actual harm.

The Term Sheet (Item 7) expressly stated: "Licensor's IP infringement indemnity is excluded from the liability cap (uncapped)." The Amendment reverses that deal point. Because § 16.3 gives the Amendment priority over the Agreement body, and the Agreement supersedes the Term Sheet, Namaith has no contractual basis to assert the Term Sheet position.

**Recommended fix:** Negotiate a further amendment restoring § 10.3(b) (Licensor's § 9.1 indemnity excluded from cap) and changing § 10.3(b) (as restated) from "Licensee's breach of § 7" back to "either Party's breach of § 7." If Lavas resists, at minimum seek a super-cap (e.g., 3× or 5× the annual fees) for Licensor's IP indemnity obligations.

---

## Issue 2: Section 9.2 Licensee Indemnity Is Extraordinarily Broad and Uncapped

**Where:** `namaith_lavas_software_license_agreement.md`, § 9.2; compare `glazecore_license_term_sheet.md`, Item 7.

**What the Agreement says:** Namaith must "defend, indemnify and hold harmless" Lavas against "any and all third-party claims" arising from "any building, curtain wall or structure incorporating glass products fabricated, tempered or processed using the Licensed Software." This expressly includes claims "alleging that the Licensed Software, any engineering output it generated or any tempering parameter it applied was defective or erroneous."

**What the Term Sheet said:** "Licensee will indemnify Licensor against third-party claims. Licensee's indemnity is limited to claims from Licensee's negligence or modifications; subject to liability cap."

**Why it matters:** Three problems compound:

1. **Scope.** The Agreement indemnity is not limited to Namaith's negligence or modifications. It covers *all* claims from buildings using the products, including claims that the *software itself* generated a defective tempering parameter. If GlazeCore's TemperControl module outputs an incorrect soak time and a lite spontaneously breaks in a completed curtain wall, Namaith must indemnify Lavas for the resulting property damage, personal injury, or death claims. This effectively makes Namaith Lavas's product-liability insurer.

2. **Uncapped.** Under both the original and restated § 10.3(a), this indemnity is excluded from the liability cap. Namaith's exposure is theoretically unlimited.

3. **No fault requirement.** The section does not require that Namaith be at fault. The trigger is that a claim "aris[es] out of or relat[es] to" a building incorporating the products. Even if the glass failure was caused entirely by a software defect, Namaith still indemnifies Lavas.

**Recommended fix:** This is the single most dangerous provision in the package. Negotiate to: (a) limit the indemnity to claims caused by Namaith's negligence, willful misconduct, or unauthorized modifications; (b) exclude claims to the extent caused by defect or error in the Licensed Software or its outputs (i.e., make it a mutual fault-based indemnity); and (c) subject it to the liability cap or at minimum a super-cap. If Lavas will not move on scope, insist on a cap.

---

## Issue 3: Pending Orvand Partners Acquisition Triggers Licensor Termination Right; Amendment Acknowledges But Does Not Consent

**Where:** `namaith_lavas_software_license_agreement.md`, §§ 1.4 (Control), 14.1–14.2; `license_amendment_no_1.md`, Recital D and § 5.

**Facts:** Amendment Recital D states: "Licensee has informed Licensor that Namaith Holdings Corp., the parent company of Licensee, has signed a definitive agreement under which Namaith Holdings Corp. will be acquired by Orvand Partners Fund III, L.P."

Section 1.4 defines a change of Control of a Party to include "any change in the ownership or Control of any entity that Controls that Party." Namaith Holdings Corp. controls Namaith. Its acquisition by Orvand Partners is therefore a change of Control of Namaith.

Section 14.2 provides that such a change "shall be deemed an assignment of this Agreement by Licensee requiring Licensor's prior written consent." Without consent, "Licensor may terminate this Agreement by written notice to Licensee given at any time within one hundred twenty (120) days after Licensor becomes aware of the change of Control."

Section 5 of the Amendment states: "Nothing in this Amendment is a waiver of, or a consent under, any provision of the Agreement."

**Why it matters:** The Amendment records that both parties know about the pending acquisition, yet the Amendment does *not* grant the consent that § 14.2 requires. When the Orvand Partners deal closes, Licensor will have a 120-day window to terminate the entire agreement — including the newly added ThermaStress module. Namaith is increasing its operational dependence on the software (adding a module, paying an additional $165,000/year) while sitting in a known termination trigger. This gives Lavas significant negotiating leverage post-closing.

**Recommended fix:** Before the Orvand Partners acquisition closes, obtain Licensor's written consent to the change of Control under § 14.2, or negotiate a side letter or further amendment that (a) consents to the specific transaction, and (b) confirms the Agreement (including the ThermaStress module) will continue on unchanged terms. Do not allow the closing to occur without this protection.

---

## Issue 4: Parent Guaranty Is Subject to the Same Liability Cap as Licensor

**Where:** `lavas_parent_guaranty.md`, § 3.2.

**What it says:** "Guarantor's liability for any Guaranteed Obligation is no greater than Licensor's liability for that obligation under the License Agreement, including Section 10 of the License Agreement."

**Why it matters:** The entire purpose of a parent guaranty is to provide Namaith with a deeper pocket than the operating subsidiary. But § 3.2 makes the guaranty only as broad as Licensor's own liability. Since the cap is ~$1,405,000 (and since, per Issue 1, Licensor's IP indemnity is now *inside* that cap), the guaranty effectively caps Namaith's recovery from the parent at the same amount. If Lavas Glazing Software, LLC is undercapitalized (as LLC subsidiaries of holding companies often are), the guaranty adds little real security.

Additionally, § 3.1 allows the Guarantor to assert any defense Licensor could assert (other than insolvency-based defenses), further eroding the "unconditional" character of the guaranty.

**Recommended fix:** Negotiate to delete or modify § 3.2 so that the Guarantor's liability is not limited by § 10 of the License Agreement, or at minimum so that the Guarantor's liability for the Guaranteed Obligations listed in § 1.3(a)–(e) is uncapped. If Lavas resists, consider whether the guaranty provides enough comfort given the subsidiary's capitalization, and whether additional security (a letter of credit, escrow, or parent financial covenants) is warranted.

---

## Issue 5: Parent Guaranty Governed by New York Law; License Agreement Governed by Delaware Law

**Where:** `lavas_parent_guaranty.md`, § 12.1–12.2; `namaith_lavas_software_license_agreement.md`, § 15.1–15.2.

**Why it matters:** If Namaith needs to enforce both the Agreement and the Guaranty (the likely scenario if Lavas defaults), it must file in two different jurisdictions under two different bodies of law. Delaware and New York can reach different results on interpretation of "material breach," "cure," "indemnity scope," and "guaranty enforceability." This creates cost, delay, and the risk of inconsistent rulings. It also complicates any effort to consolidate proceedings.

**Recommended fix:** Amend the Guaranty to conform its governing law and forum to Delaware / Wilmington, matching the Agreement. If Lavas insists on New York law for the Guaranty (perhaps for tax or regulatory reasons), at minimum negotiate a provision allowing Namaith to join a Guarantor as a party in any Delaware action on the Agreement, or to file in Delaware notwithstanding the Guaranty's forum clause.

---

## Issue 6: Insurance Rating Certification Appears Inaccurate

**Where:** `lavas_insurance_certificate_cover_letter.md`, § 2 (table) and § 3(c); `namaith_lavas_software_license_agreement.md`, § 11.1.

**The requirement:** § 11.1 requires insurers rated "A- VII or better by A.M. Best."

**What the certificate shows:**
- Bastrop Mutual Casualty Company (CGL): **A XII**
- Meridian Specialty Insurance Company (Tech E&O): **A+ XV**

**The broker's certification (§ 3(c)):** "each insurer is rated A- VII or better by A.M. Best."

**Why it matters:** A.M. Best's loss-paying capacity scale runs from I (best) to XV (worst). "VII or better" means a Roman numeral of VII or lower (i.e., I through VII). XII and XV are both *worse* than VII. On the face of the certificate, neither insurer meets the contractual requirement, yet the broker affirmatively certifies that they do. If this is correct, Licensor is in breach of § 11.1 from day one, and the insurance "backstop" for Licensor's obligations is weaker than Namaith was led to believe.

**Caveat:** I am flagging this based on my reading of the A.M. Best scale. The partner should verify the rating interpretation with a broker or risk specialist before raising it with Lavas, in case the combined rating is being read differently than I assume.

**Recommended fix:** (1) Verify the A.M. Best rating interpretation. (2) If the insurers do not meet the § 11.1 threshold, demand compliant policies or a waiver with appropriate protection (e.g., increased limits, a higher-rated insurer, or a parent letter of credit as substitute security). (3) Reserve the right to treat the non-compliant insurance as a material breach under § 13.1.

---

## Issue 7: Technology E&O Policy Is Claims-Made; Gap Risk Over a 5-Year Term

**Where:** `lavas_insurance_certificate_cover_letter.md`, § 2 (table: "claims-made form," retroactive date March 1, 2019); `namaith_lavas_software_license_agreement.md`, § 11.1 ("During the Term and for two (2) years afterward").

**Why it matters:** A claims-made policy only covers claims *made* during the policy period. The current policy runs March 1, 2026 – March 1, 2027. The Agreement requires coverage for the full 5-year Term plus 2 years (7 years total). If:
- the policy is not renewed,
- the insurer non-renews or materially changes terms,
- there is a lapse between policies, or
- a claim arises from a software error in Year 3 but is not discovered or reported until Year 4 (after a policy change),

Namaith could find that the insurance does not respond, even though Licensor was contractually required to maintain coverage. The 30-day cancellation notice (§ 11.2) helps but does not close the gap.

The CGL policy is occurrence-form (covers events that occur during the policy period regardless of when the claim is filed), so it does not have this problem. The Tech E&O is where the risk concentrates — and that is the policy most likely to respond to software-failure claims.

**Recommended fix:** (1) Require Licensor to maintain a claims-made Tech E&O policy with a retroactive date no later than March 1, 2019 (or earlier) for the entire Term plus the 2-year tail, and to provide evidence of continuous coverage. (2) Add a requirement that Licensor purchase a "tail" or "extended reporting period" endorsement at the end of the Term covering the 2-year post-term period. (3) Consider requiring Licensor to notify Namaith not only of cancellation but of any change in policy terms, insurer, or limits at renewal.

---

## Issue 8: No Service Credits or Liquidated Damages for Missed SLA Targets

**Where:** `namaith_lavas_software_license_agreement.md`, Schedule B.3; § 8.2.

**Why it matters:** Schedule B.3 sets "Response" and "Workaround or Fix Target" times for each severity level. For Severity 1 (production stoppage or tempering-control failure), the target is 1-hour response and 8-hour workaround/fix. These are labeled "targets," not guarantees. There is no service-credit mechanism, no liquidated-damages provision, and no termination right for chronic SLA failures (short of a "material breach" argument under § 13.1, which would require 30 days' notice and cure).

For a facade manufacturer running tempering furnaces, a Severity 1 event that is not resolved within 8 hours means lost production, potentially missed delivery dates to general contractors, and possible liquidated-damages exposure to Namaith's own customers. Namaith's only contractual remedy is to argue the failure constitutes a breach of the § 8.2 performance warranty — but the § 8.2 remedy is correction (or termination + pro rata refund if correction fails within 60 days), not damages for lost production. And lost profits are excluded by § 10.2.

**Recommended fix:** Negotiate a service-credit schedule (e.g., a percentage of the monthly license fee credited for each hour the Severity 1 fix target is missed) and a termination right if Severity 1 targets are missed more than [X] times in any [Y]-month period. Alternatively, add a provision that chronic SLA failure constitutes a material breach excusing the 30-day cure period.

---

## Issue 9: 90-Day Post-Termination Transition Period May Be Inadequate

**Where:** `namaith_lavas_software_license_agreement.md`, § 13.4(a)–(b).

**Why it matters:** Upon termination (for any reason, including Licensor's termination right under § 14.2 for the Orvand Partners change of control), Namaith has 90 days to "complete fabrication of orders then in progress" and export its data. Curtain-wall and insulating-glass projects typically have multi-month fabrication and delivery schedules. A 90-day window may not be sufficient to complete all in-progress orders, particularly large unitized-facade projects. If the window expires before an order is complete, Namaith must cease use of the software mid-project, potentially delivering non-conforming product or breaching its own customer contracts.

**Recommended fix:** Extend the transition period to 180 days, or tie it to the completion date of the last in-progress order (whichever is earlier). Alternatively, negotiate a "run-off" license at a reduced fee for the transition period.

---

## Issue 10: Performance Warranty Remedy Does Not Compensate for Lost Production

**Where:** `namaith_lavas_software_license_agreement.md`, § 8.2, § 10.2.

**Why it matters:** If the software fails to perform in accordance with the Documentation, Namaith's exclusive remedy is for Lavas to fix it. If Lavas cannot fix it within 60 days, Namaith may terminate and receive a pro rata refund of prepaid fees. There is no right to damages for the period of non-performance. Combined with the § 10.2 consequential-damages exclusion (lost profits, lost revenue), Namaith bears the full economic cost of downtime — lost production, idle labor, missed customer delivery dates — with no recovery from Lavas.

**Recommended fix:** Carve out of the § 10.2 consequential-damages exclusion any damages resulting from Licensor's failure to meet the § 8.2 performance warranty or the Schedule B service levels. At minimum, negotiate a service-credit mechanism (see Issue 8) that provides some monetary remedy short of full consequential damages.

---

## Issue 11: License Is Non-Transferable and Change of Control Requires Consent — Limits M&A Flexibility

**Where:** `namaith_lavas_software_license_agreement.md`, § 2.1, § 14.1–14.2.

**Why it matters:** Beyond the specific Orvand Partners issue (Issue 3), the non-transferability and change-of-control consent requirement mean that in any future sale of Namaith (or its parent), the acquirer cannot simply step into the license. Licensor has a veto. This is a standard provision in software licenses, but combined with the 5-year initial term and auto-renewal, it creates a significant encumbrance on Namaith's corporate flexibility. If Namaith is sold and Licensor withholds consent, the buyer loses the software (and the 90-day transition period applies).

**Recommended fix:** If the Orvand Partners deal is proceeding, address this now (see Issue 3). For future flexibility, consider negotiating a provision that permits assignment to an acquirer in a change-of-control transaction without consent, so long as the acquirer assumes the Agreement in writing.

---

## Issue 12: Guaranty Lacks Financial Covenants

**Where:** `lavas_parent_guaranty.md`, § 8.

**Why it matters:** The only ongoing financial obligations on the Guarantor are (a) to deliver annual consolidated financial statements within 120 days of fiscal year-end, *on request*, and (b) to give notice if it ceases to own a majority of Licensor. There are no minimum net-worth covenants, no leverage limits, no requirement to maintain a certain level of liquidity. If Lavas Technologies Holdings, Inc. takes on significant debt or its financial condition deteriorates, Namaith has no early-warning trigger or right to demand additional security. The "on request" language for financial statements also means Namaith must remember to ask; there is no automatic delivery.

**Recommended fix:** Add a covenant requiring automatic (not on-request) delivery of annual financial statements, and consider a material-adverse-change provision that would allow Namaith to demand additional security or terminate the Agreement if the Guarantor's financial condition deteriorates below a specified threshold.

---

## Issue 13: Amendment No. 1 – ThermaStress Module Delivery and Implementation Deadlines

**Where:** `license_amendment_no_1.md`, §§ 1.3, 3.3.

**Why it matters:** The Amendment (effective September 14, 2026) required delivery of the ThermaStress module within 10 business days (by approximately September 28, 2026) and completion of implementation within 45 days (by approximately October 29, 2026). I have no document in the file confirming that delivery or implementation has occurred. If these deadlines have passed without performance, Namaith may have a breach claim.

**Recommended fix:** Verify whether the ThermaStress module has been delivered and implemented. If not, send a notice of breach under § 13.1 and demand cure. If implementation is in progress, document the status and hold Lavas to the Schedule B.1A deadline.

---

## Issue 14: Section 5.3 Feedback Provision – Broad Grant to Licensor

**Where:** `namaith_lavas_software_license_agreement.md`, § 5.3.

**Why it matters:** "Licensor may use any suggestions Licensee provides about the Licensed Software without obligation, provided Licensor does not disclose Licensee Data or Licensee's Confidential Information." This means if Namaith's engineers suggest a feature or workflow improvement (which is likely during implementation and ongoing use), Lavas can incorporate that suggestion into the software and license it to Namaith's competitors. The only protection is that Lavas cannot disclose Namaith's data or confidential information — but the *idea* itself (e.g., a new method of calculating thermal stress for a specific edge condition) is not necessarily "Confidential Information" unless marked as such or obviously confidential.

**Recommended fix:** Amend § 5.3 to exclude from the "suggestions" grant any feedback that constitutes or incorporates Namaith's Confidential Information or proprietary engineering methods, or to require Namaith's prior written consent before Lavas uses any suggestion that is specific to Namaith's processes.

---

## Items Flagged as Ambiguous or Incomplete

1. **Schedules A and B are incorporated by reference but only the Schedule A module list and Schedule B service levels appear at the end of the Agreement document.** I have not seen a separate execution copy or confirmation that the Schedules were attached and initialed. Verify that the executed Agreement includes the Schedules as shown.

2. **The insurance certificate itself is not in the file** — only the broker's cover letter summarizing it. The cover letter states "Copies of the policy endorsements are available on request through Lavas" (§ 6). I have not seen the actual policy forms, endorsements, or the certificate of insurance. The broker's summary may not capture all exclusions (e.g., the Tech E&O policy may exclude certain types of claims, or contain sub-limits for cyber events). Request the full policy forms.

3. **The Term Sheet is dated January 22, 2026, and references a "mutual non-disclosure agreement"** (Item 12) that is not in the file. If Namaith wishes to assert that the Term Sheet reflects the parties' intent (e.g., on the scope of the Licensee indemnity), it may be useful to have the NDA for context, though the Term Sheet is expressly non-binding.

4. **No document addresses what happens to the ThermaStress Module Fee if the Agreement is terminated mid-year.** § 8.2 provides a pro rata refund of "prepaid Annual License Fees" but does not expressly include the ThermaStress Module Fee. Given that § 4.7 (added by the Amendment) is part of Section 4, one could argue it is included in "fees due under Section 4," but the refund language in § 8.2 specifically says "Annual License Fees." Clarify whether the ThermaStress Module Fee is refundable on termination.

---

## Questions for the Partner

1. Do you want me to draft a letter to Lavas raising Issues 1–3 (the Section 10.3 restatement, the § 9.2 indemnity scope, and the change-of-control consent) as a package, or should we sequence them?
2. On the insurance rating issue (Issue 6), do you have a risk specialist I should loop in to confirm the A.M. Best scale interpretation before we raise it?
3. Is the Orvand Partners acquisition expected to close before or after the next contract-year anniversary (March 3, 2027)? This affects urgency on Issue 3.
4. Has Namaith received the ThermaStress module? I need to know before I can assess Issue 13.