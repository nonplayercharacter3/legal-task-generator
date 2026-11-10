# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Fatesk / Drupuv Platform License – Issue Identification and Recommended Fixes

---

## Scope Note

The Wilmington office lease (*fatesk_wilmington_studio_office_lease.md*) has no bearing on the Drupuv license arrangement and is excluded from this analysis. All issues below arise from the Platform License Agreement, the Term Sheet, the SOW, and the SLA Schedule.

---

## Tier 1 – Critical Issues

### 1. Severity 1 Definition Conflict: Agreement vs. SLA Schedule

**Where:**
- Agreement § 1.11: "Severity 1 Incident" = "an incident making matchmaking, login or in-game purchases unavailable to **10% or more of End Users**."
- SLA Schedule § 2.1(a): "Severity 1 Incident" = "an incident resulting in the **complete unavailability of the Platform to all End Users in all regions**."
- SLA Schedule § 2.1(b): "Severity 2 Incident" = "an incident that makes one or more Core Services unavailable, or materially degraded, for **some or all** End Users."
- Agreement § 17.4 (Order of Precedence): The SLA Schedule prevails over the Agreement "as to service levels and incident classification."

**Why it matters:**
Because § 17.4 gives the SLA Schedule priority on incident classification, the operative definition of Severity 1 is the SLA Schedule's: total, global outage. This has cascading consequences:

- **Chronic failure termination right (Agreement § 8.4):** Fatesk may terminate only after three or more *Severity 1* Incidents in a rolling 90-day period. Under the SLA Schedule definition, that means three total global outages in 90 days—a near-impossible threshold. Under the Agreement's 10% definition, a significant regional or single-service outage would count.
- **Elevated response obligations (Agreement § 7.2):** The 1-hour response, continuous senior engineering, hourly status updates, and 5-day root cause analysis apply only to Severity 1. A 30%-of-users login outage would be classified as Severity 2 under the SLA Schedule, triggering only a 2-hour response and 8-hour workaround target (SLA Schedule § 4.1).
- **SLA response/resolution targets (SLA Schedule § 4.1):** The 12-hour resolution target for Severity 1 applies only to total global outages. A 20% in-game purchase outage gets a 2-day resolution target (Severity 2).

In short, the SLA Schedule quietly gutted the most important protective provisions in the Agreement.

**Recommended fix:**
Conform the SLA Schedule definition to the Agreement, or at minimum to the Term Sheet (which tracks the Agreement's 10% threshold). Proposed language for SLA Schedule § 2.1(a):

> "Severity 1 Incident" means an incident making any Core Service unavailable or materially degraded to ten percent (10%) or more of End Users in any Region, or resulting in complete unavailability of the Platform to all End Users in all Regions.

If Drupuv resists, an alternative is to add a new "Severity 1A" or "Severity 1.5" tier for 10%+ incidents with the same response obligations as current Severity 1, and to amend Agreement § 8.4 to count both tiers toward the chronic failure termination trigger.

---

### 2. Renewal Term Changed from 1-Year to 3-Year Auto-Renewal with Narrow Notice Window

**Where:**
- Term Sheet § 8.2: "The agreement would provide for **one-year renewals**; either party may decline renewal on **90 days' notice** before term end."
- Agreement § 12.2: "this Agreement shall renew automatically for successive **three (3) year** Renewal Terms. It shall not renew if either Party gives the other written notice of non-renewal. A notice of non-renewal is effective only if delivered **no earlier than one hundred fifty (150) days and no later than one hundred twenty (120) days** before the end of the then-current term."

**Why it matters:**
The negotiated deal was 1-year renewals with a generous 90-day non-renewal window. The definitive agreement locks Fatesk into 3-year auto-renewals with a 30-day window (days 150–120 before term end). If Fatesk misses that window by even one day, it is committed for another 3 years at a fee that can increase up to 9% (Agreement § 5.3). Over two missed windows, Fatesk could be locked in for 9 years with compounding fee increases on a platform it may no longer want.

**Recommended fix:**
Restore the Term Sheet structure: 1-year renewal terms with 90 days' non-renewal notice. If Drupuv insists on 3-year renewal terms as a commercial condition, at minimum:
- Widen the non-renewal notice window to 180 days before term end (with no outside date, or an outside date of 90 days); and
- Cap the renewal fee increase at the lesser of 9% or CPI for the preceding 12 months.

---

### 3. SOW Governed by California Law and San Francisco Venue – Direct Conflict with Agreement

**Where:**
- Agreement § 17.1: Delaware governing law.
- Agreement § 17.2: Exclusive jurisdiction in Wilmington, Delaware.
- SOW § 9.1: "governed by the laws of the State of **California**."
- SOW § 9.2: Exclusive jurisdiction in **San Francisco County, California**.
- Agreement § 17.4: The SOW prevails over the Agreement "as to Implementation Services."

**Why it matters:**
Any dispute arising from the Implementation Services—including acceptance of milestones, payment of the Implementation Fee, ownership of Deliverables, or performance of the data migration—will be litigated in California under California law, while all other disputes (SLA failures, data security, IP infringement, termination) go to Delaware. This creates:
- Split proceedings and inconsistent outcomes;
- A higher-cost forum for Fatesk (travel, local counsel);
- Potential for Drupuv to forum-shop by characterizing a dispute as "implementation-related" to pull it to California.

The Term Sheet (§ 12) contemplated a single Delaware forum for all Definitive Agreements. This appears to be a drafting error or a concession that was not flagged.

**Recommended fix:**
Delete SOW § 9 in its entirety and add: "This SOW is governed by and subject to the dispute resolution provisions of Section 17 of the Agreement." If Drupuv's California counsel inserted this for their own convenience, push back: the SOW is an ancillary document to the Agreement and should not have a different governing law.

---

### 4. Drupuv Assignment Rights Expanded – Competitor Protection Dropped

**Where:**
- Term Sheet § 10.2: "Drupuv may **not** assign to a **Fatesk competitor** without Fatesk's prior written consent."
- Agreement § 15.2: "Drupuv may assign or transfer this Agreement, in whole or in part, **without Fatesk's consent** in connection with a Permitted Transfer."
- Agreement § 1.8: "Permitted Transfer" = "any merger, change of control, or sale of all or any part of the business or assets to which this Agreement relates, **to any person**."

**Why it matters:**
Drupuv can sell the Platform business (or the relevant assets) to any of Fatesk's competitors—e.g., another game publisher or a rival backend provider—and Fatesk has no consent right. The competitor would then have access to Fatesk's Fatesk Data (subject to § 9), integration details, player metrics, and unreleased title information (subject to § 11, but confidentiality obligations bind the assignee only if the assignment is effective). More practically, Fatesk's live-service titles would be running on infrastructure owned by a direct competitor, creating competitive intelligence risk and potential conflicts in service prioritization.

**Recommended fix:**
Restore the Term Sheet protection. Amend Agreement § 15.2:

> Drupuv may assign or transfer this Agreement in connection with a Permitted Transfer, provided that (a) the assignee is not a direct competitor of Fatesk in the publication or operation of online video games, and (b) Drupuv gives Fatesk at least thirty (30) days' prior written notice of the proposed assignment. If the proposed assignee is a competitor, Fatesk may terminate this Agreement on written notice within thirty (30) days after receiving the assignment notice, and Drupuv shall refund all prepaid fees for the period after the termination date.

---

## Tier 2 – Significant Issues

### 5. Data Return Window (90 Days) Shorter Than Transition Period (180 Days)

**Where:**
- Agreement § 9.5: "During the Term and for **ninety (90) days** afterward, Drupuv shall make all Fatesk Data available to Fatesk for export… After that period, Drupuv shall delete the Fatesk Data."
- Agreement § 12.5(a): Transition period of up to **one hundred eighty (180) days**.
- Agreement § 12.5(c): "Section 9.5 shall apply to the return and deletion of Fatesk Data."

**Why it matters:**
If Fatesk elects the full 180-day transition, Drupuv is contractually entitled to delete all Fatesk Data at day 90—while Fatesk is still operating the Platform on Drupuv's infrastructure for another 90 days. This creates an impossible situation: Fatesk is running live titles on data that Drupuv has deleted, or Drupuv is in breach of § 12.5(a) by continuing to operate the Platform without the underlying data.

**Recommended fix:**
Amend § 9.5 to tie the data retention period to the transition period:

> During the Term, for the duration of any transition period under Section 12.5(a), and for ninety (90) days after the end of the transition period (or, if no transition period is elected, ninety (90) days after the end of the Term), Drupuv shall make all Fatesk Data available…

---

### 6. SOW Deemed Acceptance Mechanism

**Where:**
- SOW § 4.2: If Fatesk does not respond within 10 business days of a milestone completion notice, Drupuv may send a reminder. If Fatesk does not respond within 5 business days after the reminder, "the milestone is **deemed accepted**."

**Why it matters:**
Fatesk's engineering team is managing platform-holder certifications, launch preparations, and potentially multiple titles simultaneously. A 15-business-day total window (10 + 5) to review and respond is aggressive. If Fatesk misses the window, it loses the right to reject the milestone, trigger correction, or withhold the associated payment ($126,000 for M2 or M3). Deemed acceptance also triggers the ownership transfer of Deliverables under SOW § 8.2 (payment in full), potentially accelerating Fatesk's financial exposure.

**Recommended fix:**
- Extend the initial response period to 20 business days and the post-reminder period to 10 business days; and/or
- Add: "Deemed acceptance shall not apply if Fatesk has identified and notified Drupuv of a specific non-conformity in writing before the expiration of the response period, even if the notice was informal or incomplete."
- Clarify that deemed acceptance of a milestone does not waive Fatesk's right to claim a breach of warranty under Agreement § 13.2(b) for defects discovered later.

---

### 7. Liability Cap May Be Inadequate for Platform-Level Failures

**Where:**
- Agreement § 14.5: Cap = "total fees paid and payable under this Agreement in the twelve (12) months preceding the event giving rise to the claim" = approximately **$1,840,000**.
- Agreement § 14.6: Carve-outs for indemnification, breach of § 9 (Data/Security), breach of § 11 (Confidentiality), gross negligence, willful misconduct.

**Why it matters:**
The cap applies to Drupuv's SLA failures, service outages that don't rise to gross negligence, and implementation service failures. If a prolonged Sev 2 outage (e.g., 2-day matchmaking failure) causes Fatesk to lose significant revenue from in-game purchases or player churn, Fatesk's recovery is capped at ~$1.84M. The service credits (capped at 50% of Monthly Fee ≈ $76,667 per month) are the primary monetary remedy for SLA failures, which is modest relative to the revenue at risk.

The § 14.6 carve-outs help for data breaches and IP claims, but a pure performance failure (no data loss, no IP issue, no gross negligence) is subject to the cap.

**Recommended fix:**
- Raise the cap to 24 months of fees (~$3.68M), or
- Add a super-cap: "Notwithstanding Section 14.5, Drupuv's aggregate liability for failures to meet the service levels in the SLA Schedule shall not exceed [X]% of the annual license fee for the contract year in which the failure occurred."
- At minimum, confirm that the chronic failure termination right (§ 8.4) provides a full refund of prepaid fees (it does) and that Fatesk's termination is not treated as a breach that would trigger Fatesk's own indemnity to Drupuv.

---

### 8. Service Credit Cap and Structure

**Where:**
- SLA Schedule § 7.4: "Total service credits in any Service Month shall not exceed **50% of the Monthly Fee**."
- SLA Schedule § 7.1: Availability credits range from 5% to 30% of Monthly Fee per Core Service.
- SLA Schedule § 7.2: Performance credits = 3% of Monthly Fee per failed commitment.
- SLA Schedule § 1.2(d): Monthly Fee = $1,840,000 / 12 ≈ **$153,333**.

**Why it matters:**
Maximum monthly credit ≈ $76,667. In a bad month where all four Core Services are degraded across multiple regions and all four performance targets are missed, Fatesk recovers at most $76,667 against a $1.84M annual commitment. For a live-service game where a 4-hour matchmaking outage during a major event could cost millions in lost purchases and player trust, the credit structure is a weak deterrent. The Term Sheet (§ 5.1) correctly states that "Service credits would not be Fatesk's exclusive remedy," and Agreement § 8.3 confirms this, but the practical remedy for non-chronic SLA failures is still just the credit.

**Recommended fix:**
- Increase the monthly credit cap to 100% of Monthly Fee;
- Add a "consecutive month" multiplier: if the same Core Service misses the availability target in three consecutive months, the credit for the third month is tripled;
- Confirm in the SLA Schedule that service credits are in addition to (not in lieu of) Fatesk's right to terminate under § 8.4 or to claim damages for breach (subject to the cap in § 14.5).

---

## Tier 3 – Moderate Issues

### 9. Overage Mechanism Lacks a Dispute Resolution Path

**Where:**
- Agreement § 2.2: If peak concurrent users exceed Licensed Concurrency, "Drupuv will continue to serve all End Users. The Parties will then **meet in good faith to agree an increase** to the Licensed Concurrency at the overage rate set out in Exhibit B."
- Exhibit B: Overage priced at $96,000 per 50,000-user block per contract year.

**Why it matters:**
There is no consequence if Fatesk declines to agree to the overage increase. Drupuv must continue to serve, but the agreement is silent on whether the overage fee is automatically billed or whether Fatesk is in breach for "exceeding" the licensed concurrency. This ambiguity could be exploited by Drupuv to claim Fatesk is in material breach (triggering § 12.3) or to assert a right to bill the overage unilaterally.

**Recommended fix:**
Add to § 2.2:

> If the Parties are unable to agree on an increase within thirty (30) days after the overage occurs, the overage fee set forth in Exhibit B shall apply automatically for the remainder of the contract year in which the overage occurred, and Fatesk shall not be in breach for the overage. Drupuv shall not suspend, throttle, or degrade service to any End User on account of the overage.

---

### 10. SLA Exclusion for "Fatesk Code" Defects – Risk of Disputes

**Where:**
- SLA Schedule § 7.5(b): Downtime and performance failures are excluded if caused by "defects in Licensed Title code that is **not** Drupuv integration code delivered under the Statement of Work."

**Why it matters:**
In a live-service game, the boundary between "Fatesk code" and "Drupuv integration code" can be blurry. Drupuv could argue that a matchmaking failure was caused by Fatesk's game logic (e.g., a bug in Fatesk's player state management) rather than the Platform, thereby excluding the incident from SLA calculations. Given the SOW's scope (Drupuv integrates SDKs into Fatesk's builds), there will be extensive code intermingling.

**Recommended fix:**
Add: "For purposes of this exclusion, 'Drupuv integration code' includes all code, configuration, and API calls made by the Platform SDKs and APIs as integrated under the Statement of Work, and the exclusion applies only to the extent Fatesk can demonstrate, with reasonable specificity, that the defect originated in Fatesk's game code independent of the Platform SDKs. In the event of a good-faith dispute as to causation, the incident shall be counted toward the service level calculation pending resolution."

---

### 11. Upfront SOW Payment with No Performance Milestone

**Where:**
- SOW § 5.2: $84,000 (20% of the Implementation Fee) is invoiced at the "SOW Effective Date"—before any work is performed.

**Why it matters:**
Fatesk pays $84,000 on day one with no deliverable in hand. If the project stalls or Drupuv underperforms, this amount is at risk (subject to the general cap and remedies). The Term Sheet (§ 3.2) contemplated payment "against milestones" without specifying an upfront component.

**Recommended fix:**
Either (a) eliminate the upfront payment and make the first invoice contingent on acceptance of M1 (Design Approval), or (b) reduce the upfront payment to $42,000 (10%) and add: "If Drupuv fails to achieve M1 within [60] days of the SOW Effective Date for reasons not attributable to Fatesk, Fatesk may terminate this SOW and receive a full refund of all amounts paid."

---

### 12. Renewal Fee Increase of 9% per Renewal Term

**Where:**
- Agreement § 5.3: "Drupuv may increase the annual license fee by up to **nine percent (9%)** over the annual license fee in effect for the final contract year of the preceding term."

**Why it matters:**
Combined with the 3-year auto-renewal (Issue 2), the fee trajectory could be:
- Year 1–3: $1,840,000
- Year 4–6 (if renewed): up to $2,005,600 (+9%)
- Year 7–9 (if renewed again): up to $2,186,104 (+9% compounded)

Over 9 years, that's a ~19% increase on the base fee, or ~$346,000/year in additional cost by the final term.

**Recommended fix:**
Cap the increase at the lesser of 9% or the Consumer Price Index (CPI-U) increase for the trailing 12 months. Alternatively, if the renewal term is restored to 1 year (per Issue 2), the 9% cap is less concerning because Fatesk can walk after any single year.

---

## Open Questions for the Client

| # | Question | Why it matters |
|---|---|---|
| 1 | What is Fatesk's projected peak concurrent user count for *Ironveil: Frontier* at launch and for *Project Halcyon*? | Determines whether the 750,000 Licensed Concurrency is adequate or whether overage is likely in Year 1. If overage is expected, the overage pricing and mechanism (Issue 9) become more urgent. |
| 2 | Does Fatesk have existing backend infrastructure that it would need to migrate away from if the Drupuv relationship ends? | Affects the practical value of the 180-day transition period and the data return window (Issue 5). If Fatesk has a legacy system it could fall back on, the 90-day window is less critical. |
| 3 | What is Fatesk's expected launch date for *Project Halcyon*? | The SOW covers implementation for all three titles, but *Project Halcyon* is a working title. If its launch is more than 12–18 months out, the SOW timeline and milestone structure may need adjustment. Also affects which launch windows (4 per year) will be used. |
| 4 | Has Fatesk identified any specific competitors that Drupuv might be acquired by, or that might acquire Drupuv? | Informs how aggressively to push on the assignment restriction (Issue 4). If there is a known strategic buyer in Fatesk's competitive set, the risk is more concrete. |
| 5 | What is Fatesk's internal process and timeline for reviewing SOW milestones? | Determines whether the 10-business-day acceptance window (Issue 6) is workable. If Fatesk's review process requires cross-team sign-off (engineering, QA, live ops), 10 days may be unrealistic. |

---

## Summary of Recommended Negotiating Priorities

| Priority | Issue | Ask |
|---|---|---|
| 1 | Sev 1 definition | Conform SLA Schedule to 10% threshold (or add intermediate tier) |
| 2 | Renewal term | Restore 1-year renewals / 90-day notice; if 3-year, widen notice window to 180 days |
| 3 | SOW governing law | Delete SOW § 9; conform to Delaware / Wilmington |
| 4 | Assignment | Add competitor carve-out and termination right |
| 5 | Data return vs. transition | Extend data retention to cover full transition period + 90 days |
| 6 | Deemed acceptance | Extend windows; add carve-out for identified non-conformities |
| 7 | Liability cap | Raise to 24 months or add SLA-specific super-cap |
| 8 | Service credits | Raise monthly cap to 100%; add consecutive-month multiplier |