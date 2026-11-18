# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Napais Cold Chain Logistics, LLC — Software License Arrangements with Baivusk Software, Inc. (Acquisition Diligence)

---

## Executive Summary

Napais is the target of a 100% membership interest acquisition by Kelderhorn Cold Freight Holdings, Inc. (per the Equity Purchase Agreement dated October 30, 2025, referenced in Napais's November 14, 2025 non-renewal letter). The Baivusk relationship presents three material issues that could affect the transaction: (1) the non-renewal notice appears to have been sent 14 days after the contractual deadline, risking an involuntary 24-month renewal; (2) the change of control itself triggers a consent requirement under the License Agreement; and (3) the Side Letter's exclusivity clause is dramatically broader than what the parties originally negotiated, and it survives 12 months past termination — creating integration friction for Kelderhorn. Details and recommendations follow.

---

## Issue 1: Non-Renewal Notice Is Likely Late

**Where:** License Agreement § 12.2; Non-Renewal Letter ¶¶ 2.1–2.2.

**The problem.** Section 12.2 provides that the Agreement renews automatically for successive 24-month periods unless "either party gives the other written notice of non-renewal at least 120 days before the end of the then-current term." The Initial Term is 36 months from March 1, 2023, ending **February 28, 2026**. Counting back 120 days from February 28, 2026 lands on **October 31, 2025**. Napais's non-renewal letter is dated **November 14, 2025** — 14 days after the deadline.

**Why it matters.** If Baivusk successfully argues the notice was untimely, the Agreement auto-renews for 24 months (through February 28, 2028). Consequences:

- Napais (now owned by Kelderhorn) is locked into $684,000/year in subscription fees plus any renewal fee increase of up to 5% (§ 5.5), with 150 days' advance notice.
- The Most Favored Pricing protection in Side Letter § 3.1 applies only "During the Initial Term." On renewal, Napais loses its MFN shield.
- The change-of-control consent issue (Issue 2 below) becomes more acute because the Agreement is still in effect at closing.
- Customer data remains in Baivusk's environment for another two years (§ 6.4 triggers only on expiration or termination).

**Recommendation.**

1. Send a supplemental notice immediately, acknowledging the original date and asserting that the November 14 letter constitutes timely notice under § 18.4 (which defines effectiveness as "on receipt"). Argue that the letter was *delivered* via overnight courier and certified mail on or before November 14 and *received* by Baivusk within the 120-day window if the courier date was earlier. Check the certified-mail return receipt for the actual date of receipt.
2. If the receipt date confirms delivery after October 31, negotiate a waiver or amendment with Baivusk as part of the consent process (see Issue 2). Baivusk has an incentive to cooperate: it wants the consent fee or a clean exit, and it does not want to litigate a 14-day discrepancy while its customer is being acquired by a competitor-adjacent entity.
3. In the acquisition agreement, include a specific closing condition or indemnity covering the financial impact of an involuntary renewal (up to ~$1.4M in subscription fees plus lost MFN savings over 24 months).

---

## Issue 2: Change of Control Requires Baivusk's Prior Written Consent

**Where:** License Agreement § 15.1; § 13.2(c); Side Letter § 6.3.

**The problem.** Section 15.1 states:

> "Any change of control of Licensee, whether by sale of equity, merger, consolidation or otherwise, is deemed an assignment requiring Licensor's prior written consent."

The Kelderhorn transaction is a 100% sale of membership interests — squarely a "sale of equity" change of control. Without Baivusk's written consent before closing, the change of control is a "purported assignment in breach" of § 15.1, which is **void** (§ 15.1, last sentence) and triggers Baivusk's right to **terminate immediately** under § 13.2(c).

Section 15.1 does state that consent "shall not be unreasonably withheld," but that is a standard, not a guarantee. Baivusk could condition consent on:

- A fee or premium;
- Acceptance of the Side Letter's exclusivity by Kelderhorn (Side Letter § 6.3 binds "permitted successors and assigns");
- A shorter transition period; or
- Other commercial concessions.

**Why it matters.** If Baivusk terminates under § 13.2(c) post-closing, Kelderhorn loses the Platform immediately, loses transition assistance (which is unavailable where Licensor terminates for non-payment under § 13.2(a), but the § 13.4 carve-out only references 13.2(a) — so transition assistance *should* be available for a 13.2(c) termination, though this is worth confirming), and faces a sudden gap in temperature monitoring for 1,800 trailers and 6 facilities.

**Recommendation.**

1. Request Baivusk's written consent **before** the Kelderhorn closing, ideally as a condition to closing in the Equity Purchase Agreement.
2. In the consent request, offer to have Kelderhorn (or Napais, post-closing) acknowledge the Side Letter's terms. Be prepared for Baivusk to push back on the exclusivity scope (see Issue 3).
3. If Baivusk unreasonably withholds consent, Napais has a claim under § 15.1's reasonableness standard, but litigation in Delaware (License Agreement § 17.2) or New York (Side Letter § 5.2) during a pending acquisition is impractical. Negotiation is the better path.
4. Coordinate timing: if the non-renewal notice is effective (Issue 1), the Agreement expires February 28, 2026. If the Kelderhorn closing occurs before that date, consent is still needed. If closing occurs after expiration, the consent issue is moot (the Agreement is over), but the 12-month post-termination exclusivity tail (Issue 3) still applies.

---

## Issue 3: Exclusivity Clause Is Far Broader Than Negotiated and Survives 12 Months Post-Termination

**Where:** Side Letter § 2.1; Term Sheet §§ 4.1, 4.3; Non-Renewal Letter ¶ 2.2.

**The problem.** The Term Sheet (January 18, 2023) — the document reflecting the parties' commercial negotiation — scoped exclusivity narrowly:

- **Term Sheet § 4.1:** "exclusive provider of **temperature telemetry software** for Napais's **United States refrigerated trailer fleet**."
- **Term Sheet § 4.3:** "Napais and its affiliates are **not restricted** from licensing, developing or using other software outside the agreed scope."

The executed Side Letter (March 1, 2023) expanded this dramatically:

- **Side Letter § 2.1:** "Licensee shall not license, develop or use any **temperature monitoring, warehouse management, yard management or transportation management software** from any provider other than Licensor, **in any jurisdiction worldwide**."

The final clause covers four software categories (not one), applies globally (not just to the US trailer fleet), and binds Affiliates. "Develop" is defined to include internal development or development through a third party.

**Survival.** The exclusivity runs "During the Term, **and for 12 months after** the expiration or termination of the Agreement." If the Agreement expires February 28, 2026, the exclusivity tail runs to **February 28, 2027**.

**Why it matters to Kelderhorn.** Kelderhorn is a cold freight holdings company. It almost certainly operates (or will operate post-closing) a group-wide TMS, WMS, or YMS. If Napais is bound by the Side Letter's exclusivity through February 2027, it **cannot** migrate to Kelderhorn's group technology stack during that window. This creates:

- A 12-month integration delay for the acquirer's technology consolidation strategy;
- A potential breach if Kelderhorn, in its ordinary post-closing integration, causes Napais to "use" a group TMS or WMS (even passively, through shared dashboards or consolidated reporting);
- Leverage for Baivusk in the consent negotiation (Issue 2).

**Recommendation.**

1. As part of the consent request to Baivusk, propose an **exclusivity release or narrowing** in exchange for consent. Offer: (a) a consent fee; (b) a commitment to pay through the expiration date; (c) a reference or case-study right. In return, ask Baivusk to (i) release the 12-month post-termination tail, or (ii) narrow the scope to "temperature monitoring" only (matching the Term Sheet), or (iii) carve out software used by the Licensee's ultimate parent or its Affiliates for group-level operations.
2. If Baivusk will not negotiate, document the Term Sheet as evidence of the parties' original commercial understanding. While this does not rewrite the Side Letter (both parties signed it), it supports a "unreasonable withholding of consent" argument under § 15.1 if Baivusk uses the exclusivity as a pretext to extract excessive concessions.
3. In the Equity Purchase Agreement, include a **specific indemnity or escrow** for any exclusivity-related costs Kelderhorn incurs during the 12-month tail (e.g., dual-running costs, delayed integration savings).
4. Instruct Napais management **not to take any action** that could be construed as "using" or "developing" a competing WMS, YMS, or TMS before the exclusivity period ends, even in planning stages. Side Letter § 2.3 requires prompt notice if Napais "receives a proposal from or enters into discussions with another provider" for covered software. Kelderhorn's integration planning team should be briefed on this restriction.

---

## Issue 4: Split Governing Law and Forum

**Where:** License Agreement § 17.1–17.2; Side Letter §§ 5.1–5.2; License Agreement § 18.3.

**The problem.** The License Agreement is governed by **Delaware** law with exclusive jurisdiction in **New Castle County, Delaware**. The Side Letter is governed by **New York** law with exclusive jurisdiction in **New York County, New York**. Section 18.3 gives the Side Letter **priority** over the License Agreement in case of conflict.

**Why it matters.** Any dispute touching the exclusivity clause (the most commercially significant term for Kelderhorn) will be litigated in New York under New York law, while disputes about the license grant, data, or termination will be in Delaware. This split creates:

- Increased litigation cost and complexity;
- The risk of inconsistent rulings if related claims are split across forums;
- A tactical disadvantage if Baivusk files first in New York (home-court familiarity for a Delaware corporation is less than for a New York forum, but Baivusk's CRO signed both documents and the Side Letter was likely drafted by Baivusk's New York counsel).

**Recommendation.**

1. In any consent or amendment negotiation, ask Baivusk to conform the Side Letter's governing law and forum to Delaware, matching the License Agreement. This is a reasonable ask given that the Side Letter is ancillary to the main Agreement.
2. If Baivusk resists, ensure that any side agreement or consent letter explicitly states which law governs the release or modification of the exclusivity.

---

## Issue 5: Transition Assistance and Customer Data Export

**Where:** License Agreement §§ 6.4, 13.4; Non-Renewal Letter ¶¶ 3.1–3.2, 4.1–4.3; Order Form Part D.

**The problem.** The non-renewal letter requests 90 days of transition assistance under § 13.4 and a comprehensive data export under § 6.4. Both requests are contractually supported *if* the Agreement expires (rather than renews). Key operational considerations:

- **Data export (§ 6.4):** Baivusk must make Customer Data available in "a standard machine-readable format" within 30 days after expiration, then delete within 60 days after the export window. The letter requests shipment records, temperature/humidity readings, location/route data, equipment status data, and alarm history for the full Term. This is a substantial dataset (3 years, 1,800 trailers, 6 facilities, 1,150 driver seats).
- **Transition assistance (§ 13.4):** 90 days at "fee rates then in effect." The letter does not specify whether this means the full $684,000/12 = $57,000/month or a reduced rate. The contract says "fee rates then in effect," which most naturally reads as the full subscription rate.
- **Gateway decommissioning:** 1,800 TG-4 telematics gateways are owned by Napais (Order Form § C.4: "Title to purchased devices passes to Licensee on delivery"). Decommissioning 1,800 gateways across a national trailer fleet in 90 days is a significant logistics project. The Ostrander maintenance agreement (Service Schedule § S.6) provides 3-hour emergency response within 100 miles of Columbus, Indianapolis, or Louisville — but the fleet is national.

**Why it matters.** If the non-renewal notice is ineffective (Issue 1), none of this triggers until February 28, 2028 at the earliest. Even if effective, Kelderhorn needs to plan the migration to its replacement system during the 90-day window. The data export is critical for regulatory compliance (FDA food safety records, FMCSA requirements) and for customer contracts that may require temperature proof-of-delivery.

**Recommendation.**

1. Confirm the non-renewal notice is effective (Issue 1) before investing in transition planning.
2. If effective, immediately engage a migration vendor and begin scoping the replacement platform. The 90-day window starts February 28, 2026 — plan backward from there.
3. Send a detailed data export specification to Baivusk now (format: CSV, Parquet, or API-based; field-level mapping; historical depth). Do not wait for the 30-day post-expiration window to begin the technical conversation.
4. Budget for 90 days of transition fees (~$57,000/month × 3 = ~$171,000) plus professional services for gateway decommissioning at $215/hour (Order Form § C.7).
5. Confirm that the Ostrander agreement (Issue 6 below) remains in place during the transition to maintain reefer uptime.

---

## Issue 6: Ostrander Reefer Maintenance Agreement — Assignment Analysis

**Where:** Ostrander Agreement § 12.2.

**The problem.** Section 12.2 provides:

> "Neither party may assign this Agreement without the other party's prior written consent, which may not be unreasonably withheld. Either party may, however, assign this Agreement without consent to an Affiliate or to a successor to all or substantially all of its business or assets, on written notice to the other party."

The Kelderhorn transaction is a **sale of membership interests** (change of control of Napais), not a sale of Napais's business or assets. Napais remains the same legal entity. Therefore:

- No "assignment" of the Ostrander Agreement occurs. The contract continues with Napais as the party; only Napais's ownership changes.
- The "successor to all or substantially all of its business or assets" carve-out is not needed because there is no assignment to begin with.
- The Ostrander Agreement does **not** contain a change-of-control provision analogous to Baivusk's § 15.1.

**Why it matters.** This is a favorable distinction. The Ostrander relationship (preventive maintenance on reefer units, emergency roadside response) continues uninterrupted through the acquisition. No consent is required. However, if Kelderhorn later restructures Napais (e.g., merges it into a Kelderhorn subsidiary, or sells its assets to a Kelderhorn entity), that *would* trigger the assignment clause.

**Recommendation.**

1. No action required at closing. The Ostrander Agreement survives the change of control without consent.
2. If Kelderhorn plans any post-closing restructuring of Napais's legal entity (merger, asset transfer), obtain Ostrander's consent or rely on the "successor to all or substantially all" carve-out, with written notice per § 12.2.
3. Note that the Ostrander Agreement auto-renews for 12-month periods (Service Schedule § 11.1) unless 60 days' non-renewal notice is given. The initial 24-month term from July 1, 2024 ends **June 30, 2026**. Kelderhorn should decide before **May 1, 2026** (60 days prior) whether to renew or replace Ostrander as part of the group's maintenance strategy.

---

## Issue 7: NDA Confidentiality Obligations Survive

**Where:** NDA §§ 8.1–8.2, 10.3.

**The problem.** The NDA term was 2 years from January 9, 2023, expiring **January 9, 2025** (absent earlier termination). However, § 8.2 provides that confidentiality obligations continue for **3 years after expiration** — i.e., through **January 9, 2028**. Trade secrets are protected indefinitely.

The NDA covers (per § 1.2): Baivusk's product architecture, source code, security documentation, audit reports, product roadmaps, and pricing; and Napais's fleet data, routes, customer identities, shipment volumes, rates, and cost information.

Section 10.3 prohibits assignment without consent, except to a "successor to all or substantially all of its business or assets." As with the Ostrander agreement, a change of control does not constitute an assignment — Napais remains the same entity. The NDA obligations continue to bind Napais (now owned by Kelderhorn).

**Why it matters.** Kelderhorn's deal team and integration team will have access to Napais's confidential operational data (routes, customers, pricing) as part of the acquisition. They must not disclose that data to Baivusk's competitors or use it in a way that breaches the NDA. Conversely, any Baivusk product information Napais received during diligence (architecture, roadmaps, pricing of other customers) remains confidential through January 2028.

**Recommendation.**

1. Include the NDA in Kelderhorn's post-closing confidentiality briefing. Ensure integration team members who access Napais's data are aware of the surviving obligations.
2. No consent or notice to Baivusk is required for the change of control (same analysis as Ostrander).
3. If Kelderhorn plans to share Napais's operational data with other Kelderhorn entities for benchmarking or integration purposes, confirm that those entities qualify as "Representatives" under NDA § 1.3 (affiliates, officers, employees, advisors). Post-closing, Kelderhorn and its subsidiaries will be Napais's parent and Affiliates, so this should be satisfied — but document the need-to-know basis.

---

## Issue 8: Baivusk's Unilateral Assignment Right

**Where:** License Agreement § 15.2.

**The problem.** Section 15.2 allows Baivusk to assign the Agreement (and by § 18.3, the Side Letter) to any Affiliate or successor **without Napais's consent**, on 30 days' notice. This is one-sided: Napais needs consent for a change of control, but Baivusk does not.

**Why it matters.** If Baivusk is acquired by a competitor of Kelderhorn (or by a private equity firm that strips services), the Platform — and the exclusivity obligations — transfer to the new owner. Kelderhorn would be locked into an exclusive relationship with an entity it did not choose.

**Recommendation.**

1. As part of the consent negotiation (Issue 2), request that Baivusk's consent letter include a covenant that, if Baivusk assigns the Agreement under § 15.2, the assignee must assume the Side Letter's exclusivity obligations *only* to the extent they were in effect at the time of assignment, and that Napais/Kelderhorn may terminate the exclusivity (with a pro-rata refund) if the assignee is a direct competitor of Kelderhorn.
2. Monitor Baivusk's corporate developments. If Baivusk announces a sale or merger, assess whether the assignee triggers the § 15.2 notice and whether Kelderhorn wants to negotiate a release.

---

## Summary of Recommended Actions (Priority Order)

| # | Action | Deadline / Timing |
|---|--------|-------------------|
| 1 | Verify certified-mail receipt date of the November 14 non-renewal letter; if received after October 31, 2025, prepare supplemental notice and waiver request to Baivusk | **Immediately** |
| 2 | Request Baivusk's written consent to the change of control under § 15.1, bundled with a proposal to narrow or release the Side Letter exclusivity | **Before Kelderhorn closing** |
| 3 | Add a closing condition to the Equity Purchase Agreement requiring Baivusk consent (or confirming the non-renewal is effective) | **Before Kelderhorn closing** |
| 4 | Brief Kelderhorn integration team on Side Letter § 2.3 notice obligation (do not enter discussions with competing TMS/WMS/YMS vendors without notifying Baivusk) | **Immediately** |
| 5 | Engage migration vendor; scope replacement platform and gateway decommissioning plan for the 90-day transition window | **By January 2026** (to be ready for Feb 28 expiration) |
| 6 | Send data export specification to Baivusk (format, fields, historical depth) to begin technical alignment before the § 6.4 window opens | **By January 2026** |
| 7 | Decide on Ostrander renewal (60-day non-renewal deadline is May 1, 2026) as part of Kelderhorn's group maintenance strategy | **By April 2026** |
| 8 | Include NDA obligations in Kelderhorn's post-closing confidentiality protocol | **At closing** |

---

## Documents Reviewed

| Document | Role in Analysis |
|----------|-----------------|
| Software License Agreement (Mar 1, 2023) | Primary contract; assignment, term, termination, data, liability provisions |
| Side Letter (Mar 1, 2023) | Exclusivity and pricing commitments; NY governing law |
| Term Sheet (Jan 18, 2023) | Evidence of original negotiated scope of exclusivity |
| Non-Renewal Letter (Nov 14, 2025) | Napais's exit notice; timing issue |
| Order Form No. 001 (Mar 1, 2023) | Commercial terms: fees, quantities, service credits, implementation |
| Ostrander Reefer Maintenance Agreement (Jul 1, 2024) | Separate vendor; assignment analysis for change of control |
| Mutual NDA (Jan 9, 2023) | Surviving confidentiality obligations through Jan 2028 |