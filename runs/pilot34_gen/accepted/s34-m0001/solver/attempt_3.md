# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current]
**RE:** Steireis Hospitality Group, LLC – Nesesk Software License: Issue Identification and Recommended Positions

---

## Preliminary Note: Ardmoor Linen Services Agreement

I reviewed `ardmoor_linen_services_agreement.md`. It is a linen and laundry services agreement between Steireis and Ardmoor Linen Services, LLC, effective March 1, 2024. It addresses physical goods (linen supply, laundering, delivery) and has no overlap with the Nesesk software licensing in terms of parties, subject matter, or legal issues. **It has no bearing on this matter.**

---

## Issue 1: Side Letter – Forced Acknowledgment of Auto-Renewal

**Documents:** `nesesk_proposed_side_letter_2026-10-14.md`, Recital B and Section 1.1; `steireis_nesesk_software_license_agreement.md`, Section 3.2; `nesesk_order_form_no1.md`, Section 2.1.

**Facts.** The Initial Term runs from December 1, 2023 to November 30, 2026 (36 months from the Subscription Start Date per Agreement § 3.1 and Order Form § 2.1). Section 3.2 requires written notice of non-renewal at least 90 days before the end of the then-current term. Ninety days before November 30, 2026 is **September 1, 2026**. Steireis's non-renewal notice was dated **September 18, 2026** – 17 days late. Nesesk is therefore correct that the contract auto-renewed for a 36-month First Renewal Term through November 30, 2029.

**Why it matters.** Section 1.1 of the Side Letter requires Steireis to "acknowledge and agree" that the renewal occurred. Signing would:
- Concede the renewal as a matter of contract, foreclosing any argument (e.g., that Nesesk's own conduct tolled or waived the notice period, or that the 90-day window was unreasonable);
- Lock Steireis in for 36 additional months with no exit right other than for cause;
- Continue the expanded exclusivity obligations (see Issue 3) for the full Renewal Term.

The 8% discount (saving approximately $13,158 per year, ~$39,474 over three years) is a modest sweetener that does not compensate for the loss of negotiating leverage or the continued lock-in.

**Recommendation.**
- **Do not sign the Side Letter as drafted.** The renewal has already occurred as a matter of law; Steireis does not need to "acknowledge" it to be bound.
- **Negotiating position:** Respond that Steireis does not dispute the mechanical operation of the auto-renewal but reserves all rights and arguments regarding the reasonableness of the notice period and any waiver or estoppel arising from Nesesk's conduct. Offer to discuss commercial terms for the Renewal Term (pricing, exclusivity scope, termination rights) in a separate amendment, without the acknowledgment language.
- **If the client wants out entirely,** investigate whether Nesesk's course of performance, any representations about renewal terms, or the disparity between the Term Sheet and the final Agreement give rise to a claim of unenforceability of the auto-renewal provision under New York law (cf. *TeleCheck Services, Inc. v. The First National Bank of Ariz.*, 20 N.Y.3d 460 (2013), on unconscionability of automatic renewal). This is a weaker position but worth preserving.
- **Client flag:** Confirm the exact date and method of delivery of the September 18, 2026 letter. If it was sent by email only (which Agreement § 15.6 provides does not constitute notice), the situation is worse. If it was sent by overnight courier on September 18, the 17-day lateness is clear. We need to know whether any earlier informal communication (e.g., a phone call or email to Nesesk's account manager) could support a waiver or estoppel argument.

---

## Issue 2: Side Letter – Narrowing of Uncapped Data Security Liability

**Documents:** `nesesk_proposed_side_letter_2026-10-14.md`, Section 2.1; `steireis_nesesk_software_license_agreement.md`, Sections 9, 11.2, and 12.3.

**Facts.** Currently, Agreement § 12.3(a) carves out *all* of Licensor's breaches of Section 9 (Data Security) from both the consequential damages exclusion (§ 12.1) and the liability cap (§ 12.2). The Side Letter proposes to replace this with a carve-out limited to breaches "resulting from Licensor's **gross negligence or willful misconduct**."

**Why it matters.** This is the single most dangerous provision in the Side Letter. Steireis processes Guest Data that includes payment card data, identification documents, and reservation history for 232 rooms across seven properties (Agreement § 1.6; Order Form § 1.2). A data breach caused by Nesesk's ordinary negligence (e.g., a misconfigured server, a failed patch, a social engineering attack on Nesesk staff) would:

1. **Cap Steireis's recovery** at 12 months of fees (~$151,314 under the discounted rate) under § 12.2, even if actual damages (regulatory fines under NY SHIELD Act, class action defense costs, guest notification and credit monitoring, PCI DSS non-compliance penalties) run into the millions.
2. **Simultaneously trigger Steireis's uncapped indemnity** to Nesesk under § 11.2 (which is itself excluded from the cap by § 12.3(b)). If guests or regulators pursue Steireis for the breach, Steireis must indemnify Nesesk for those claims – uncapped – even though Nesesk's own negligence caused the breach and Steireis's recovery from Nesesk is capped.

The result is an inverted risk allocation: the party that caused the breach (Nesesk) has limited exposure, while the party that did not (Steireis) bears uncapped downstream liability.

**Recommendation.**
- **Reject Section 2.1 of the Side Letter in its entirety.** Do not accept any qualifier on the § 12.3(a) carve-out.
- **Fallback position (if Nesesk insists on a qualifier):** Accept "gross negligence" but not "willful misconduct" as the threshold, and add a **super-cap** for data security breaches (e.g., 3× the annual fees or the limit of Nesesk's cyber insurance, whichever is greater). Rationale: the current Agreement already contemplates that data security breaches are a distinct and severe risk category (hence the original uncapped carve-out, the specific PCI DSS obligation in § 9.2, the 72-hour notification in § 9.4, and the $5M cyber insurance requirement in § 13.1(b)).
- **Additionally:** Push back on the interaction with § 11.2. If a data breach is caused by Nesesk's negligence, Steireis should not be required to indemnify Nesesk for resulting guest or regulatory claims. Propose adding to § 11.2: "Licensee's obligations under this Section 11.2 shall not apply to the extent any claim arises from or is attributable to Licensor's breach of Section 9."

---

## Issue 3: Exclusivity – Dramatic Expansion Beyond the Term Sheet

**Documents:** `nesesk_order_form_no1.md`, Section 5; `steireis_nesesk_term_sheet.md`, Sections 4.1–4.2; `steireis_nesesk_software_license_agreement.md`, Section 1.3.

**Facts.** The Term Sheet (October 20, 2023) agreed to a narrow exclusivity:
- § 4.1: "Exclusivity will apply to the **property management module only**, at the **seven Hudson Valley properties** listed in the term sheet."
- § 4.2: "Steireis remains free to license, use and evaluate third-party software for **guest messaging, point-of-sale, revenue management** and any other function. Steireis is also free to use **any property management system at any property not listed** in Section 2.2, including properties it acquires, opens or brings under management after the date of the Definitive Agreements."

The executed Order Form (November 15, 2023) contains a vastly broader exclusivity:
- § 5.1: Prohibits competing software at **all Covered Properties** (defined in Agreement § 1.3 as *any* property owned, managed, or franchised by Steireis or its Affiliates, *at any location*, *including future acquisitions*).
- § 5.2: Defines "competing hospitality software" to include **four categories**: property management, point-of-sale (food, beverage, spa, retail), revenue management and rate optimization, and guest messaging and communications.
- § 5.3: Requires newly acquired properties using competing software to **transition to Nesesk within 180 days**.
- § 5.4: Deems breach a **material breach** supporting **injunctive relief**.

**Why it matters.** This transforms a limited PMS exclusivity at seven properties into a comprehensive technology lock-in across Steireis's entire current and future portfolio, in four software categories. For a growing boutique hotel group, this means:
- Steireis cannot adopt a better or cheaper POS system at any property;
- Steireis cannot use a dedicated revenue management tool (e.g., a Best Rate Guarantee optimizer);
- Steireis cannot pilot or evaluate any competing guest messaging platform;
- Any future acquisition (even a single-property deal) triggers a 180-day forced migration to Nesesk;
- Breach gives Nesesk injunctive relief, creating existential operational risk.

The Order of Precedence (Agreement § 15.4) places the Order Form above the Agreement, and the Term Sheet is non-binding (§ 8.1). So the broader Order Form language controls. However, the disparity between the Term Sheet and the Order Form is so significant that it raises questions about whether the Order Form reflects the parties' actual agreement.

**Recommendation.**
- **Primary position:** Demand that Order Form § 5 be conformed to the Term Sheet. Exclusivity should be limited to (a) the PMS module only, and (b) the seven properties listed in Order Form § 1.2. Delete § 5.3 (forced transition of acquired properties) and narrow § 5.2 to property management only.
- **Fallback position:** If Nesesk insists on broader exclusivity, limit it to the PMS module at all Covered Properties (accepting the broader property scope but not the category expansion). Strike the POS, revenue management, and guest messaging categories. Delete § 5.3 or extend the transition period to 365 days with a right to pay a fee in lieu of transition.
- **Additional protection:** Add a carve-out permitting Steireis to use third-party software for functions not offered by Nesesk (e.g., if Nesesk does not offer a spa management module, Steireis should be free to use a third-party spa system).
- **Client flag:** Confirm with Steireis management whether the broader exclusivity was discussed and accepted during negotiations, or whether it appeared in the final Order Form without flagging. If the latter, this strengthens the argument that it does not reflect the parties' agreement.

---

## Issue 4: No Termination for Convenience

**Documents:** `steireis_nesesk_software_license_agreement.md`, Section 14; `nesesk_order_form_no1.md`, Section 6.3.

**Facts.** The Agreement provides termination only for: (a) material breach with 30-day cure period (§ 14.1); (b) insolvency (§ 14.2); and (c) chronic PMS availability failure below 98% in three of six rolling months (Order Form § 6.3, which triggers § 14.1). There is no termination for convenience.

**Why it matters.** Combined with the 36-month auto-renewal (§ 3.2) and the broad exclusivity (Issue 3), Steireis has no exit ramp. If Nesesk's product stagnates, if Steireis's business model changes (e.g., a shift to extended-stay where a different PMS is better suited), or if a superior platform emerges, Steireis is locked in for the full term with no ability to walk away. The only "exit" is to prove material breach – a high bar.

**Recommendation.**
- **Ask for a termination for convenience** with 180 days' notice and a break fee (e.g., 50% of remaining annual fees). This is common in enterprise SaaS for multi-year commitments.
- **Fallback:** If Nesesk resists, negotiate a **right to terminate at the end of any contract year** (rather than only at the end of the full 36-month term) with 120 days' notice. This gives Steireis an annual checkpoint.
- **Alternative:** Negotiate a **performance-based termination right** – e.g., if Nesesk fails to deliver a specified number of material product enhancements or new features during the term, Steireis may terminate without penalty.

---

## Issue 5: Fees Accrue Before Go-Live

**Documents:** `nesesk_order_form_no1.md`, Section 2.3; `steireis_nesesk_software_license_agreement.md`, Section 4.1.

**Facts.** Order Form § 2.3 states: "Subscription Fees accrue from the Subscription Start Date **whatever the go-live date of any property**." The go-live target is February 29, 2024 (nearly 3 months after the December 1, 2023 start). If implementation is delayed, Steireis pays for software it cannot use.

**Why it matters.** There is no service credit, fee abatement, or termination right tied to delayed go-live. The only remedy is the general warranty in Agreement § 10.2(b) (implementation performed in a "professional and workmanlike manner"), for which the exclusive remedy is correction or termination of the affected Order Form with a refund of prepaid fees. But the "exclusive remedy" language in § 10.2 is tied to clause (a) (software performance), not clause (b) (services). Even if it applied, termination of the Order Form would end the entire subscription, not just abate fees for the delay period.

**Recommendation.**
- **Add a go-live deadline with consequences:** If any Initial Deployment Property has not gone live by [date + 60 days], the Subscription Fees for that property are abated for the delay period, or Steireis may terminate the Order Form for that property without penalty.
- **At minimum:** Clarify that the § 10.2 warranty applies to both clauses (a) and (b), and that the exclusive remedy for delayed implementation includes a pro-rata fee abatement for the delay period (not just full termination).

---

## Issue 6: Service Credits Limited to PMS Module

**Documents:** `nesesk_order_form_no1.md`, Section 6.1; `steireis_nesesk_software_license_agreement.md`, Section 4.3.

**Facts.** Service credits apply only if "monthly availability of **Nesesk PMS** falls below the 99.5% target." There are no service credits for Nesesk GuestConnect or Nesesk Channel Bridge, despite both being subscribed modules with dedicated fees ($32,016 and $37,800 annually, respectively).

**Why it matters.** Channel Bridge is a two-way interface to OTA and booking-engine channels. Downtime directly causes **lost reservations and revenue** – arguably more damaging than PMS downtime (which affects operational efficiency but not the booking funnel). GuestConnect downtime degrades the guest experience (no mobile check-in, no pre-arrival communications) and could trigger guest complaints and reviews. Steireis is paying for these modules but has no contractual remedy if they are unavailable.

**Recommendation.**
- **Extend the SLA and service credit structure to all three modules.** At minimum, add a 99.5% availability target for Channel Bridge with the same credit schedule. For GuestConnect, a 99.0% target with a lower credit schedule (e.g., 5% / 10%) would be reasonable given its lower revenue impact.
- **Add a chronic failure provision** (similar to Order Form § 6.3) for Channel Bridge: if availability falls below 98% in three of six rolling months, Steireis may treat it as a material breach.

---

## Issue 7: Force Majeure Includes Internet Failures

**Documents:** `steireis_nesesk_software_license_agreement.md`, Section 15.7.

**Facts.** The force majeure clause excuses non-performance caused by "failures of public utilities or the internet."

**Why it matters.** Nesesk is a cloud-based software provider. Internet connectivity is the **core infrastructure** through which it delivers its service. If the internet fails (at Nesesk's data center, at a carrier level, or at Steireis's properties), Nesesk could invoke force majeure to avoid liability for non-availability – effectively nullifying the SLA in § 4.3 and the service credits in Order Form § 6. The clause does not distinguish between internet failures at Steireis's properties (where force majeure might be appropriate) and failures in Nesesk's own infrastructure or its upstream carriers (where Nesesk should bear the risk as the party in the business of providing cloud services).

**Recommendation.**
- **Narrow the force majeure clause** to exclude "failures of the internet or network connectivity to the extent such failure is within Licensor's control or is a risk inherent in Licensor's business of providing cloud-based software." Alternatively, provide that force majeure does not relieve Licensor of its SLA obligations unless the failure affects more than [X]% of Licensor's customer base.
- **At minimum:** Clarify that scheduled maintenance (already excluded from the SLA under § 4.3) is not force majeure, and that force majeure does not extend the Subscription Term or relieve Steireis of its obligation to pay fees (it already doesn't, per the "other than payment obligations" language, but the interaction with SLA credits should be explicit).

---

## Issue 8: Guest Data Indemnity is One-Sided and Uncapped

**Documents:** `steireis_nesesk_software_license_agreement.md`, Sections 11.2 and 12.3(b).

**Facts.** Section 11.2 requires Steireis to indemnify Nesesk for "any and all third-party claims, actions, regulatory investigations, losses, damages, fines, penalties, costs and expenses (including reasonable attorneys' fees) arising out of or relating to **Guest Data processed through the Licensed Software**." Section 12.3(b) excludes this indemnity from the liability cap, making it **uncapped**.

**Why it matters.** The indemnity is triggered by claims "arising out of or relating to Guest Data processed through the Licensed Software" – not by Steireis's fault. If a guest's data is breached at Nesesk's data center and the guest sues Steireis (the hotel, as the data controller), Steireis must indemnify Nesesk for the guest's claims against Nesesk. The language does not require that Steireis be at fault. Combined with Issue 2 (the proposed narrowing of the data security carve-out), this creates the inverted risk allocation described above.

**Recommendation.**
- **Add a fault qualifier:** Steireis's indemnity should apply only to claims "arising out of or relating to Guest Data **to the extent caused by or resulting from** Licensee's breach of this Agreement or Licensee's negligence or willful misconduct."
- **Add a carve-out for Nesesk-caused breaches:** "Licensee's obligations under this Section 11.2 shall not apply to the extent any claim arises from or is attributable to Licensor's breach of Section 9 or Licensor's negligence or willful misconduct."
- **Cap the indemnity** (remove it from § 12.3(b)) or at minimum set a super-cap (e.g., 3× annual fees or the cyber insurance limit).

---

## Issue 9: Support Obligations Are Underspecified

**Documents:** `steireis_nesesk_software_license_agreement.md`, Section 4.2.

**Facts.** Section 4.2 provides support "in accordance with its **standard support policy**," with a floor of 24/7 coverage for Severity 1 incidents. The "standard support policy" is not attached to the Agreement and is not defined. It could change unilaterally.

**Why it matters.** For a hotel group running seven properties, support responsiveness for non-Sev-1 issues (e.g., a channel bridge sync error, a folio posting bug, a guest messaging template issue) directly affects operations. A floating reference to a policy that Nesesk can update at any time gives Steireis no contractual protection for response times, escalation paths, or support hours for lower-severity issues.

**Recommendation.**
- **Attach Nesesk's current support policy as an exhibit** to the Order Form, with a provision that material changes require Steireis's consent.
- **Specify minimum response and resolution times** for at least Severity 1 and Severity 2 (e.g., Sev 1: response within 1 hour, resolution target 4 hours; Sev 2: response within 4 business hours, resolution target 2 business days).
- **Define severity levels** in the Agreement or Order Form so the parties are not relying on Nesesk's unilateral classification.

---

## Issue 10: No Transition Assistance on Termination

**Documents:** `steireis_nesesk_software_license_agreement.md`, Section 9.6 and Section 14.3.

**Facts.** Section 9.6 requires Nesesk to make data available for export in "standard machine-readable format" within 30 days of termination and to delete it within 90 days after that. There is no obligation to provide transition assistance, parallel running, or cooperation with a successor vendor.

**Why it matters.** A PMS holds reservations, guest profiles, open folios, housekeeping status, and channel connections. Migrating this to a new system without vendor cooperation is operationally disruptive – potentially causing double-bookings, lost reservations, and guest confusion during the transition. The 30-day export window may be insufficient for a multi-property migration, and "standard machine-readable format" does not guarantee compatibility with a successor system.

**Recommendation.**
- **Add a transition assistance obligation:** For up to 90 days post-termination (at Steireis's expense, at a pre-agreed daily rate), Nesesk shall provide reasonable cooperation to facilitate migration, including data mapping assistance, API access, and parallel running of the legacy and new systems.
- **Extend the export window** to 60 days and specify that the format shall be CSV or a format reasonably requested by Steireis.
- **Add a data integrity warranty:** Nesesk warrants that exported data will be complete and accurate as of the export date.

---

## Issue 11: Asymmetric Termination Consequences

**Documents:** `steireis_nesesk_software_license_agreement.md`, Section 14.3.

**Facts.** Section 14.3 provides: "If Licensee terminates under Section 14.1, Licensor shall refund any prepaid Fees for the period after the termination date. If Licensor terminates under Section 14.1, Licensee shall pay any unpaid Fees for the remainder of the then-current term."

**Why it matters.** The second sentence means that if Nesesk terminates for Steireis's material breach, Steireis owes the **full remaining term fees** – not just through the cure period, but for the entire 36-month term (or Renewal Term). This is effectively a liquidated damages clause that could expose Steireis to ~$493,416 (3 × $164,472) or ~$453,943 (3 × $151,314 discounted) for a single material breach. While this is somewhat standard (it reflects the lost revenue Nesesk would have earned), it is harsh when combined with the broad exclusivity (Issue 3) – a single unauthorized evaluation of a competing POS system at one property could trigger this.

**Recommendation.**
- **Limit the acceleration to the remainder of the then-current contract year** (not the full term). Rationale: Nesesk's actual lost revenue from a mid-term termination is the current year's fees, not the full 36 months (which would not have been earned but for the breach).
- **Alternatively:** Convert to a break fee of a fixed percentage (e.g., 50%) of remaining fees, which is more proportionate.

---

## Issue 12: IP Indemnity Limited to United States

**Documents:** `steireis_nesesk_software_license_agreement.md`, Section 11.1.

**Facts.** The IP indemnity covers only "United States patent, copyright, trademark or trade secret" claims.

**Why it matters.** Steireis's guests include international travelers, and the software processes data that may be subject to foreign IP claims (e.g., if a foreign patent covers a feature of the software and is enforced against Steireis in a US court on extraterritorial grounds, or if Steireis expands internationally). The risk is low for a Hudson Valley boutique group but non-zero.

**Recommendation.** Low priority. If Steireis has any plans to expand internationally or franchise abroad, request that the indemnity be extended to "any jurisdiction in which Licensee operates." Otherwise, accept as-is.

---

## Summary of Recommended Actions (Priority Order)

| Priority | Issue | Action |
|----------|-------|--------|
| 1 | Side Letter – Renewal acknowledgment | Do not sign as drafted; reserve rights; negotiate separate amendment |
| 2 | Side Letter – § 12.3(a) narrowing | Reject; demand super-cap or no qualifier |
| 3 | Exclusivity scope (Order Form § 5) | Demand conformance to Term Sheet; at minimum, limit to PMS module |
| 4 | Guest Data indemnity (§ 11.2) | Add fault qualifier and Nesesk-breach carve-out |
| 5 | No termination for convenience | Negotiate annual exit right or break fee |
| 6 | Fees before go-live (Order Form § 2.3) | Add abatement or termination right for delay |
| 7 | Service credits – PMS only (Order Form § 6.1) | Extend to Channel Bridge at minimum |
| 8 | Force majeure – internet (Agreement § 15.7) | Narrow to exclude cloud provider's core infrastructure risk |
| 9 | Support underspecified (Agreement § 4.2) | Attach policy; specify response times |
| 10 | No transition assistance (Agreement § 9.6) | Add 90-day cooperation obligation |
| 11 | Asymmetric termination (Agreement § 14.3) | Limit fee acceleration to current contract year |
| 12 | IP indemnity US-only (Agreement § 11.1) | Low priority; address if international expansion planned |

---

## Items Requiring Client Input

1. **September 18, 2026 notice:** Exact date of dispatch, method of delivery (courier vs. email), and whether any prior informal communication with Nesesk regarding non-renewal occurred. This determines whether we have any waiver/estoppel argument.
2. **Exclusivity negotiations:** Was the broader exclusivity in Order Form § 5 discussed with Nesesk during the negotiation phase? Did Steireis's team flag the discrepancy with the Term Sheet before signing? This affects our leverage and any potential reformation argument.
3. **Business plans:** Does Steireis anticipate acquiring or opening additional properties in the next 36 months? Does it use or plan to use third-party POS, revenue management, or guest messaging tools? This determines how critical the exclusivity fix is.
4. **Risk appetite on the Side Letter:** Is the client willing to accept the renewal (and negotiate from that position) or does it want to litigate the validity of the auto-renewal? The former is pragmatic; the latter is high-risk and costly.
5. **Data breach history:** Has Nesesk experienced any security incidents during the Initial Term? If so, this strengthens our position on the § 12.3(a) amendment.