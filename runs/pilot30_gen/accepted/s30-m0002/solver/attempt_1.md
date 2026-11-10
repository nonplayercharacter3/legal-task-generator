# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Fatesk / Drupuv Platform License – Issue Identification and Recommended Fixes

---

## Summary

I reviewed all five documents in the matter folder. The office lease bears no material relevance to the license deal and is addressed only briefly at the end. The four documents that matter—the Platform License Agreement, the SOW, the SLA Schedule, and the term sheet—reveal several significant issues, the most critical of which is a definitional conflict that effectively gutts Fatesk's key incident-response and termination protections. I have ordered the issues below by importance to the client.

---

## Issue 1 – Severity 1 Incident Definition Conflict (CRITICAL)

**Where:** Agreement § 1.11 defines "Severity 1 Incident" as "an incident making matchmaking, login or in-game purchases unavailable to **10% or more of End Users**." SLA Schedule § 2.1(a) defines "Severity 1 Incident" as "an incident resulting in the **complete unavailability of the Platform to all End Users in all regions**." Agreement § 17.4 provides that the SLA Schedule prevails "as to service levels and incident classification."

**Why it matters:** The SLA definition is so narrow that virtually no real-world incident would qualify. A matchmaking outage in North America, a login failure affecting 40% of players in Europe, or a storefront crash on PlayStation would all be classified as Severity 2 under the SLA definition. This has cascading consequences:

- **§ 7.2** (1-hour response, continuous senior engineering, hourly status updates) applies only to Severity 1.
- **§ 7.4** (root cause analysis within 5 business days) applies only to Severity 1.
- **§ 8.4** (termination right for 3+ Severity 1 Incidents in a rolling 90-day period) applies only to Severity 1.

Under the SLA definition, Fatesk would lose its chronic-failure termination right and enhanced response obligations for the most common and damaging class of incidents—regional or service-specific outages. A Drupuv platform that has five regional outages in a quarter would trigger no termination right at all.

**Recommended fix:** Delete SLA Schedule § 2.1(a) and conform it to the Agreement's definition, or add language to § 17.4 clarifying that the Agreement's definition of "Severity 1 Incident" controls for purposes of §§ 7.2, 7.4, and 8.4. Alternatively, restructure the SLA severity table so that the Agreement's 10% threshold is the floor for Severity 1, and the "complete unavailability" scenario is a sub-category (e.g., "Severity 1 – Total") with even more aggressive response obligations. At minimum, the chronic-failure termination trigger in § 8.4 should reference incidents meeting the Agreement's broader definition.

---

## Issue 2 – Renewal Terms Deviate Materially from Term Sheet (HIGH)

**Where:** Term Sheet § 8.2: "one-year renewals; either party may decline renewal on 90 days' notice before term end." Agreement § 12.2: automatic renewal for "successive three (3) year Renewal Terms," with non-renewal notice effective only if delivered "no earlier than one hundred fifty (150) days and no later than one hundred twenty (120) days before the end of the then-current term."

**Why it matters:** Two significant changes were made from the negotiated term sheet without apparent client awareness:

1. **Renewal period doubled** from 1 year to 3 years. If Fatesk misses the notice window, it is locked in for three additional years at a fee that can increase up to 9% per renewal (§ 5.3).
2. **Notice window narrowed** from 90 days to a 30-day window (days 150–120 before term end). Missing this window by even one day means Fatesk is bound for another 3 years.

Combined with the 9% annual fee escalation, Fatesk could be locked into a 9-year commitment (initial 3 + two renewals of 3 each) with compounding fee increases and no exit right.

**Recommended fix:** Restore the term sheet position: one-year renewal terms with 90 days' non-renewal notice. If Drupuv insists on multi-year renewals, negotiate (a) a wider notice window (e.g., 120–90 days before term end), (b) a cap on cumulative fee increases over the life of the agreement, and (c) a termination right if Drupuv's platform is acquired by a Fatesk competitor (see Issue 3).

---

## Issue 3 – Loss of Competitor Assignment Protection (HIGH)

**Where:** Term Sheet § 10.2: "Drupuv may not assign to a Fatesk competitor without Fatesk's prior written consent." Agreement § 15.2: "Drupuv may assign or transfer this Agreement, in whole or in part, **without Fatesk's consent** in connection with a Permitted Transfer." Agreement § 1.8 defines "Permitted Transfer" as "any merger, change of control, or sale of all or any part of the business or assets to which this Agreement relates, **to any person**."

**Why it matters:** The term sheet's competitor protection has been eliminated. Drupuv can now sell the Nimbus business (or even just the Fatesk contract) to any entity—including a direct competitor of Fatesk—without Fatesk's consent. Fatesk's game architecture, player data flows, integration patterns, and operational dependencies would become available to a competitor. Given that the Platform handles Fatesk's entire live-service backend (accounts, matchmaking, commerce), this is a serious competitive risk.

**Recommended fix:** Add to § 15.2: "Notwithstanding the foregoing, Drupuv shall not assign this Agreement to any entity that, at the time of assignment, develops or operates a live-service game backend platform that is directly competitive with the Platform, or that is a publisher of online video games, without Fatesk's prior written consent, not to be unreasonably withheld." Alternatively, grant Fatesk a termination right (with pro-rated refund and transition assistance) if Drupuv assigns to a competitor.

---

## Issue 4 – Split Governing Law and Venue (HIGH)

**Where:** Agreement §§ 17.1–17.2: Delaware law, exclusive jurisdiction in Wilmington, Delaware. SOW §§ 9.1–9.2: California law, exclusive jurisdiction in San Francisco County, California.

**Why it matters:** Implementation services are deeply intertwined with the platform license. A dispute about whether Drupuv's integration work caused a platform outage, or whether a data migration failure breaches the SOW or the Agreement, could plausibly be framed under either document. Split governing law creates:

- Risk of inconsistent legal standards (e.g., California and Delaware differ on implied covenants, duty of good faith, and certain contract interpretation principles).
- Increased litigation cost and complexity (two jurisdictions, two sets of local rules).
- Potential for Drupuv to forum-shop by characterizing a claim as an "Implementation Services" dispute to get California law.

The term sheet (§ 12) contemplated a single governing law and forum for all Definitive Agreements.

**Recommended fix:** Conform SOW § 9 to the Agreement: Delaware law, Wilmington venue. If Drupuv resists, at minimum add a provision that disputes arising out of or relating to both the SOW and the Agreement shall be resolved in a single forum under the Agreement's governing law.

---

## Issue 5 – Data Export Window Shorter Than Transition Period (MEDIUM-HIGH)

**Where:** Agreement § 9.5: Fatesk Data available for export "During the Term and for ninety (90) days afterward." Agreement § 12.5(a): transition period of "up to one hundred eighty (180) days."

**Why it matters:** If Fatesk terminates (e.g., for chronic failure under § 8.4) and elects the full 180-day transition period, its right to export Fatesk Data expires on day 90—halfway through the transition. During days 91–180, Fatesk is still operating on the Platform and generating new Fatesk Data, but Drupuv is no longer obligated to make that data available for export. If the transition then fails or Fatesk needs to migrate to a second successor platform, it may lack access to data generated during the second half of the transition.

**Recommended fix:** Amend § 9.5 to tie the export window to the transition period: "During the Term, for the duration of any transition period under Section 12.5, and for ninety (90) days after the end of such transition period (or after expiration of the Term if no transition period is elected), Drupuv shall make all Fatesk Data available to Fatesk for export."

---

## Issue 6 – Overage Economics Lack a Cap or Obligation to Agree (MEDIUM)

**Where:** Agreement § 2.2: if peak concurrent users exceed Licensed Concurrency, Drupuv "will continue to serve all End Users" and the parties "will meet in good faith to agree an increase." Exhibit B: overage at $96,000 per 50,000-user block per contract year.

**Why it matters:** There is no obligation on either party to actually agree to an increase. "Good faith" meeting language is unenforceable in most jurisdictions. If Fatesk has a breakout title and sustains 1,500,000 concurrent users, the overage would be 15 blocks × $96,000 = $1,440,000 per year—nearly doubling the base fee. More concerning, if the parties cannot agree, it is unclear whether Drupuv can throttle service or whether Fatesk is in breach for exceeding the licensed concurrency. The agreement says Drupuv "will continue to serve all End Users," but does not say for how long or under what terms if no agreement is reached.

**Recommended fix:** Add language clarifying that (a) Drupuv shall continue to serve all End Users at the Exhibit B overage rate until the parties agree on a revised Licensed Concurrency, (b) the overage rate shall not increase during the Initial Term, and (c) if the parties have not agreed on a revised concurrency within 60 days of the overage occurring, Fatesk may terminate the affected title from the agreement without penalty.

---

## Issue 7 – Service Credits Are Modest Relative to Business Impact (MEDIUM)

**Where:** SLA Schedule § 7.1 (availability credits: 5%–30% of Monthly Fee), § 7.2 (performance credits: 3% of Monthly Fee per failed commitment), § 7.4 (monthly cap: 50% of Monthly Fee).

**Why it matters:** The Monthly Fee is approximately $153,333 ($1,840,000 ÷ 12). Even in a catastrophic month where every Core Service in every Region falls below 99.0% availability, Fatesk would receive at most 50% of the Monthly Fee (~$76,667) in credits. For a live-service game generating significant monthly revenue, a week of degraded matchmaking or login could cost Fatesk far more in player churn and lost purchases than $76,667. The credits are a floor, not a ceiling on remedies (§ 8.3 preserves other rights), but in practice they will be the primary near-term remedy because proving consequential damages from a platform outage is difficult.

**Recommended fix:** (a) Increase the availability credit tiers (e.g., 10% / 25% / 50% / 75%); (b) raise or eliminate the 50% monthly cap; (c) add a specific credit multiplier for outages during launch windows (the current 2× in § 7.3 is good but could be increased to 3×); and (d) clarify that the § 8.4 chronic-failure termination right is the primary structural remedy and that service credits are supplemental.

---

## Issue 8 – Broad SLA Exclusions for Platform Holder and Fatesk Code Issues (MEDIUM)

**Where:** SLA Schedule § 7.5(b): excludes downtime caused by "defects in Licensed Title code that is not Drupuv integration code delivered under the Statement of Work." § 7.5(c): excludes "the unavailability of a first-party platform holder's network, identity service or storefront, where the Platform is otherwise operating normally."

**Why it matters:**

- **§ 7.5(b):** The line between "Licensed Title code" and "Drupuv integration code" will be disputed in every incident. If Fatesk's game sends a malformed request that causes the matchmaking service to crash, Drupuv will argue the exclusion applies. Fatesk will argue the platform should be resilient to client errors. This exclusion could swallow the availability commitment.

- **§ 7.5(c):** For a multi-platform title (PC, PlayStation, Xbox, Nintendo, iOS, Android), first-party platform outages are not rare. If PlayStation's authentication service is down for 4 hours, Drupuv can exclude that from its availability calculation even though Fatesk's PlayStation players cannot log in. The "where the Platform is otherwise operating normally" qualifier helps, but it puts the burden on Fatesk to show the Platform itself was at fault.

**Recommended fix:** (a) Narrow § 7.5(b) to exclude only downtime caused by Fatesk code that is *outside the scope of the integration* and *not interacting with a Drupuv API in the documented manner*; (b) in § 7.5(c), require Drupuv to implement reasonable fallback or degradation (e.g., offline queue, cached authentication) so that a platform-holder outage does not result in complete service unavailability, and exclude from the SLA only the portion of downtime directly attributable to the platform holder's failure.

---

## Issue 9 – SOW Milestone Standard Is "Commercially Reasonable Efforts" With No Specific Remedy for Delay (MEDIUM)

**Where:** SOW § 3.1: "Drupuv shall use **commercially reasonable efforts** to achieve the following milestones by the target dates." SOW § 3.2: only extends dates for Fatesk-caused delays.

**Why it matters:** There is no liquidated damages provision, no termination right specific to milestone failure, and no service credit for late delivery. If Drupuv misses M4 (Launch Readiness) by two months, Fatesk's only recourse is to argue material breach under Agreement § 12.3 (30-day cure period). For a game with a fixed launch date and platform-holder certification deadlines, a two-month delay could be catastrophic and the general material-breach remedy is slow and uncertain.

**Recommended fix:** Add to SOW § 3: (a) a liquidated damages provision of a specified amount per week of delay beyond the target date (e.g., $10,000/week), representing Fatesk's estimated costs of delayed launch; (b) a termination right for Fatesk if any milestone is delayed by more than 30 days for reasons not attributable to Fatesk, with refund of fees paid for unaccepted milestones; and (c) clarify that "commercially reasonable efforts" includes dedicating the named lead solutions architect (SOW § 6.2) throughout the delay.

---

## Issue 10 – Liability Cap May Be Inadequate for Platform-Critical Failure (MEDIUM)

**Where:** Agreement § 14.5: cap at "total fees paid and payable under this Agreement in the twelve (12) months preceding the event giving rise to the claim" (approximately $1,840,000 plus any overage and implementation fees).

**Why it matters:** The Platform is the backbone of Fatesk's live-service games. A prolonged failure or a data breach could result in player churn, lost in-game purchase revenue, platform-holder penalties, and regulatory exposure far exceeding $1.84M. The cap does not apply to data breaches (§ 14.6 carves out § 9), which is good, but it does apply to service failures, implementation failures, and IP indemnity shortfalls (though IP indemnity is also carved out). For a service failure that causes, say, 30 days of degraded gameplay across multiple titles, Fatesk's actual losses could be many multiples of the cap.

**Recommended fix:** Negotiate a super-cap for service-level failures: e.g., "Notwithstanding Section 14.5, Drupuv's aggregate liability for failure to meet the service levels in the SLA Schedule shall not exceed [2× or 3×] the annual license fee." Alternatively, add the chronic-failure termination right (§ 8.4) as a structural protection and accept the cap for non-termination scenarios, but ensure the cap is at least 2× annual fees.

---

## Issue 11 – Deemed Acceptance Window May Be Insufficient (LOWER)

**Where:** SOW § 4.2: Fatesk has 10 business days to accept or reject a milestone. If Fatesk does not respond, Drupuv may send a reminder, and the milestone is "deemed accepted" if Fatesk does not respond within 5 business days after the reminder. Total window: 15 business days (3 calendar weeks).

**Why it matters:** For M2 (Integration Complete), acceptance requires all test cases to pass with no open Severity 1 or 2 defects. For M3 (Migration Complete), the reconciliation report must show no unresolved discrepancies in entitlements or virtual currency balances. These are complex validations that may require Fatesk's QA team to run extended test cycles. 15 business days may not be sufficient, and deemed acceptance could lock in a migration with subtle data errors that surface later.

**Recommended fix:** Extend the initial acceptance period to 15 business days and the post-reminder period to 10 business days (total 25 business days). Add a proviso that deemed acceptance does not waive Fatesk's right to reject a milestone if a material defect is discovered within 30 days after deemed acceptance.

---

## Issue 12 – Scheduled Maintenance Allowance Is Generous (LOWER)

**Where:** SLA Schedule § 9.1: up to 8 hours of Scheduled Maintenance per Service Month, excluded from availability calculations.

**Why it matters:** 8 hours per month × 12 months = 96 hours per year of excluded maintenance. While maintenance must be in the 2–6 a.m. window and cannot fall in a launch window, 8 hours is substantial. If Drupuv uses the full allowance every month, Fatesk's players experience planned downtime roughly twice a month (at 4 hours each, say). For a competitive live-service game, even 4 hours of maintenance can impact player sentiment.

**Recommended fix:** Reduce to 4 hours per month, or require that no more than 2 hours occur in any single 7-day period. Add a requirement that Drupuv provide Fatesk with a 30-day maintenance calendar in advance so Fatesk can plan around it.

---

## Open Questions (Facts Needed from Client)

1. **Current concurrent user baseline.** What are Fatesk's current peak concurrent users across *Ironveil: Frontier* and its mobile companion? If current usage is already near 750,000, the overage risk (Issue 6) is immediate rather than hypothetical. If it is well below, the 750,000 cap may be adequate for the Initial Term.

2. **Project Halcyon launch date.** Is there a confirmed or target launch date for *Project Halcyon*? If it is expected to launch within the first 12 months, the SOW milestone timeline and launch window designations become urgent, and any delay in implementation has direct business impact.

3. **Competitive landscape.** Does Fatesk have identified competitors who might acquire Drupuv or who operate competing backend platforms? This affects how aggressively we should push on Issue 3 (assignment to competitors).

4. **Data sensitivity and regulatory exposure.** Does Fatesk handle any regulated data (e.g., minor player data under COPPA, GDPR data for European players) that would make the data export and deletion provisions (Issue 5) more critical?

5. **Platform-holder certification timelines.** Are there fixed certification deadlines from Sony, Microsoft, Nintendo, or Apple that Fatesk must meet? If so, the SOW milestone risk (Issue 9) is more acute because a delay could cause Fatesk to miss a platform release window entirely.

---

## Note on the Office Lease

The Wilmington office lease (through March 31, 2032, with a 5-year renewal option) has no direct bearing on the Drupuv license deal. The only tangential observation: if Fatesk is locked into the platform through successive 3-year renewals (Issue 2), it could be committed to Drupuv beyond the lease term, at which point the office would need to be re-evaluated. This is not a license issue but worth flagging for the client's broader planning.

---

## Suggested Negotiating Priorities for the Call

| Priority | Issue | Ask |
|----------|-------|-----|
| 1 | Severity 1 definition conflict | Conform SLA to Agreement definition; non-negotiable |
| 2 | Renewal terms | Restore 1-year renewals with 90-day notice; fallback: 30-day wider window + fee cap |
| 3 | Competitor assignment | Add competitor consent right or termination right |
| 4 | Split governing law | Conform SOW to Delaware |
| 5 | Data export / transition | Extend export window to cover full transition |
| 6 | SOW milestone remedy | Add liquidated damages + termination for prolonged delay |