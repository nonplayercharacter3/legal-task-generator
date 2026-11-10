# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Fatesk Interactive Entertainment, LLC – Drupuv Systems, Inc. Platform License: Issue Identification and Recommended Fixes

---

## Summary

I reviewed the five documents in the matter folder. The office lease (`fatesk_wilmington_studio_office_lease.md`) is not materially relevant to the Drupuv license deal and I have not analyzed it further. The four documents that bear on the license arrangement are the Platform License Agreement, the Statement of Work, the Service Level Schedule, and the Term Sheet. I used the Term Sheet as the benchmark for what the parties had agreed in principle and identified where the definitive documents deviate or create new exposure.

The most serious problems are (1) a definitional conflict that guts Fatesk's primary operational protections, (2) a renewal structure that is materially worse than what was agreed, and (3) an assignment clause that removes a key protection from the Term Sheet. Details and recommended fixes follow, in order of importance.

---

## Issue 1 – Severity 1 Incident Definition Conflict (Critical)

**Where it appears:**
- Agreement §1.11 defines "Severity 1 Incident" as "an incident making matchmaking, login or in-game purchases unavailable to **10% or more of End Users**."
- SLA Schedule §2.1(a) defines "Severity 1 Incident" as "an incident resulting in the **complete unavailability of the Platform to all End Users in all regions**."
- Term Sheet §5.2 tracks the Agreement's broader definition (10%+ of End Users).
- Agreement §17.4 (Order of Precedence) provides that the SLA Schedule prevails "as to … incident classification."

**Why it matters:**
The SLA Schedule's definition is dramatically narrower. Under the precedence rule, the SLA definition controls. This means:

- The 1-hour response, continuous senior engineering, and hourly status update obligations in Agreement §7.2 apply only to a total, global, all-regions outage—essentially a once-in-a-lifetime event.
- The chronic-failure termination right in Agreement §8.4 (three Severity 1 Incidents in a rolling 90-day period) becomes nearly impossible to trigger. A region-wide outage or a single-service outage (e.g., matchmaking down in Europe) would be classified as Severity 2 under the SLA, not Severity 1.
- The Severity 1 escalation path in SLA §3.3 (immediate Level 2, Level 3 at 4 hours) applies only to total outages.

In practical terms, Fatesk has paid for a platform that supports live-service games with millions of players. A 30-minute matchmaking outage in North America affecting 40% of players would be a Severity 2 under the SLA, with a 2-hour response time and a 2-day resolution target, and would not count toward the chronic-failure termination trigger.

**Recommended fix:**
Strike SLA Schedule §2.1(a) and replace with the definition from Agreement §1.11 (or the Term Sheet language): *"Severity 1 Incident means an incident making one or more Core Services unavailable or materially degraded for 10% or more of End Users in any Region."* Alternatively, if Drupuv resists, add a new "Severity 1.5" tier for regional or single-service outages affecting 10%+ of users, with response and resolution times between the current Severity 1 and Severity 2, and include it in the chronic-failure count in §8.4.

---

## Issue 2 – Renewal Term Changed from 1 Year to 3 Years with Narrow Opt-Out Window (Critical)

**Where it appears:**
- Term Sheet §8.2: "The agreement would provide for **one-year renewals**; either party may decline renewal on **90 days' notice** before term end."
- Agreement §12.2: "this Agreement shall renew automatically for successive **three (3) year** Renewal Terms. It shall not renew if either Party gives the other written notice of non-renewal. A notice of non-renewal is effective only if delivered **no earlier than 150 days and no later than 120 days** before the end of the then-current term."

**Why it matters:**
Two changes work against Fatesk:

1. **Duration:** A 3-year auto-renewal locks Fatesk in for up to 6 years (initial + one renewal) before it can walk away, versus 4 years under the Term Sheet structure. Given that the platform is embedded in live-service titles with millions of paying players, the switching cost of a 3-year lock-in is enormous.

2. **Opt-out window:** The non-renewal notice must be delivered in a 30-day window (150 to 120 days before term end). If Fatesk's legal team misses that window by even one day, it is locked in for another 3 years. Compare the Term Sheet's 90-day notice, which gave a much wider decision window.

Additionally, Agreement §5.3 allows Drupuv to increase the fee by up to 9% at each renewal. Over two 3-year renewal cycles, that compounds to roughly 19–20% above the initial fee, and Fatesk would be locked in for the full 3 years at the increased rate.

**Recommended fix:**
- Revert to 1-year renewal terms, or at minimum 2-year terms.
- Widen the non-renewal notice window to no earlier than 180 days and no later than 90 days before term end (giving a 90-day decision window).
- Add a requirement that Drupuv's renewal fee increase notice (§5.3) be delivered at least 210 days before the renewal term starts, so Fatesk has full information before the non-renewal window opens.

---

## Issue 3 – Drupuv May Assign to a Fatesk Competitor Without Consent (Critical)

**Where it appears:**
- Term Sheet §10.2: "Drupuv may **not** assign to a **Fatesk competitor** without Fatesk's prior written consent."
- Agreement §15.2: "Drupuv may assign or transfer this Agreement, in whole or in part, **without Fatesk's consent** in connection with a Permitted Transfer."
- Agreement §1.8 defines "Permitted Transfer" as "any merger, change of control, or sale of all or any part of the business or assets to which this Agreement relates, **to any person**."

**Why it matters:**
The Term Sheet gave Fatesk a veto over assignment to a competitor. The definitive agreement removes that protection entirely. Drupuv can sell its business (or the relevant asset line) to any of Fatesk's competitors—say, a rival game publisher that also operates a backend platform—and the competitor would step into Drupuv's shoes with full access to Fatesk's platform usage data, integration architecture, player metrics, and unreleased title information (all of which are "Fatesk Data" or confidential information under the Agreement).

The confidentiality obligations in §11 survive assignment (§15.3: "This Agreement binds and benefits the Parties and their permitted successors and assigns"), but a competitor already in the same market would have a structural incentive and opportunity to exploit the relationship.

**Recommended fix:**
Revise §15.2 to track the Term Sheet: "Drupuv may assign or transfer this Agreement in connection with a Permitted Transfer, provided that Drupuv shall not assign to an entity that is a direct competitor of Fatesk in the online video game publishing market without Fatesk's prior written consent, not to be unreasonably withheld." Define "direct competitor" by reference to entities that publish live-service games in the same genres as the Licensed Titles, or by a scheduled list that Fatesk can update.

---

## Issue 4 – SOW Governed by California Law and Venue (High)

**Where it appears:**
- Agreement §17.1–17.2: Delaware law; exclusive jurisdiction in Wilmington, Delaware.
- SOW §9.1–9.2: **California** law; exclusive jurisdiction in **San Francisco County, California**.
- Agreement §17.4: The SOW prevails "as to Implementation Services."

**Why it matters:**
This creates a split governing law and forum structure. Any dispute over the implementation work—milestone acceptance, scope changes, deliverable ownership, the $420,000 fee—would be litigated in California under California law, while all other disputes (SLA, data, termination, fees) would be in Delaware. This:

- Increases Fatesk's cost and complexity of enforcing its rights (two jurisdictions, two sets of law).
- Was not in the Term Sheet, which specified Delaware law and Wilmington venue for all Definitive Agreements (§12).
- May reflect Drupuv's home-state preference being pushed into the SOW as a drafting afterthought.

**Recommended fix:**
Strike SOW §9 in its entirety. Add: "This SOW is governed by and shall be construed in accordance with the laws of the State of Delaware. The Parties submit to the exclusive jurisdiction of the state and federal courts located in Wilmington, Delaware, as set out in Section 17.2 of the Agreement." This aligns the SOW with the Term Sheet and the main Agreement.

---

## Issue 5 – Data Deletion at 90 Days Conflicts with 180-Day Transition Period (High)

**Where it appears:**
- Agreement §9.5: Drupuv makes Fatesk Data available for export "during the Term and for **ninety (90) days** afterward." After that, Drupuv deletes the data and certifies deletion.
- Agreement §12.5(a): Upon termination, Drupuv continues to provide the Platform for a transition period of up to **one hundred eighty (180) days**.
- Agreement §12.5(c): "Section 9.5 shall apply to the return and deletion of Fatesk Data."

**Why it matters:**
If Fatesk elects the full 180-day transition period, the Platform is still operating and generating Fatesk Data for the first 180 days post-termination. But §9.5 requires deletion at day 90. This creates an internal contradiction: Drupuv is obligated to both operate the Platform (generating and storing data) and delete all Fatesk Data. In practice, Drupuv could argue that its deletion obligation at day 90 supersedes its transition obligation, effectively cutting the transition period to 90 days. Or Fatesk could argue the transition period extends the data availability. Either way, this is a trap.

**Recommended fix:**
Amend §9.5 to provide: "During the Term, any transition period under Section 12.5, and for ninety (90) days after the later of the end of the Term or the end of any transition period, Drupuv shall make all Fatesk Data available to Fatesk for export…" This aligns the data retention period with the actual operational period.

---

## Issue 6 – Deemed Acceptance of SOW Milestones (High)

**Where it appears:**
- SOW §4.2: Fatesk has 10 business days to accept or reject a milestone. If Fatesk does not respond, Drupuv may give a reminder. If Fatesk does not respond within 5 business days after the reminder, "the milestone is **deemed accepted**."

**Why it matters:**
Acceptance of a milestone triggers payment (SOW §5.2). If Fatesk's team is busy with a launch or a Severity 1 incident and misses the 10-day window, and then misses the 5-day reminder window, the milestone is deemed accepted and the associated invoice becomes payable. For M2 ($126,000) and M3 ($126,000), this is significant. The deemed acceptance mechanism effectively shifts the risk of Fatesk's internal delays onto Fatesk's wallet.

**Recommended fix:**
Delete the deemed acceptance language. Replace with: "If Fatesk does not respond within the ten (10) business day period, Drupuv may give a reminder notice. If Fatesk does not respond within ten (10) business days after the reminder, either Party may escalate the issue under Section 6.4. A milestone shall not be deemed accepted by silence." Alternatively, if Drupuv insists on a time limit, extend the initial period to 15 business days and the reminder period to 10 business days, and require that the reminder notice specifically identify the deliverables at issue.

---

## Issue 7 – Upfront SOW Payment Deviates from Term Sheet (Moderate)

**Where it appears:**
- Term Sheet §3.2: "The implementation fee would be a $420,000 fixed fee. It would be **payable against milestones**, with no additional time-and-materials charges for the agreed scope."
- SOW §5.2: $84,000 (20%) is invoiced on the "SOW Effective Date"—before any work is performed.

**Why it matters:**
The Term Sheet contemplates milestone-based payment only. The SOW adds an upfront payment of $84,000. While 20% is not unusual in services agreements, it was not agreed in the Term Sheet and gives Drupuv leverage before any deliverable is produced. If the implementation goes poorly, Fatesk has already paid $84,000 with no accepted milestone to point to.

**Recommended fix:**
Either (a) move the $84,000 to M1 (Design Approval) so it is payable only after Fatesk accepts the integration design documents and project plan, or (b) reduce the upfront payment to $42,000 (10%) and add $42,000 to M2. If Drupuv resists, at minimum add a condition that the upfront payment is refundable if Fatesk terminates for Drupuv's material breach before M2.

---

## Issue 8 – "Commercially Reasonable Efforts" Standard for Milestones (Moderate)

**Where it appears:**
- SOW §3.1: "Drupuv shall use **commercially reasonable efforts** to achieve the following milestones by the target dates set out in the approved project plan."

**Why it matters:**
This is a best-efforts-adjacent standard, not a firm deadline. If Drupuv misses a milestone target date, Fatesk cannot claim breach unless it can show Drupuv did not use "commercially reasonable efforts." That is a high bar to meet in litigation. Combined with the absence of a termination right for implementation delay (see Issue 9), Fatesk has limited recourse if the implementation slips.

**Recommended fix:**
Change to: "Drupuv shall achieve the following milestones by the target dates set out in the approved project plan." If Drupuv resists a firm commitment, add: "If Drupuv fails to achieve a milestone by its target date for reasons other than Fatesk's failure to perform its responsibilities under Section 7, Fatesk may (a) extend the target date by the period of delay plus five (5) business days, or (b) if the delay exceeds thirty (30) days, terminate this SOW and the Agreement and receive a pro-rata refund of fees paid for unaccepted milestones."

---

## Issue 9 – No Termination Right for Implementation Delay (Moderate)

**Where it appears:**
- SOW: No termination right for Fatesk if Drupuv chronically misses milestones.
- Agreement §12.3: Termination for material breach with 30-day cure. But a single missed milestone may not rise to "material breach," especially given the "commercially reasonable efforts" qualifier (Issue 8).
- Agreement §8.4: Chronic failure termination applies only to Severity 1 Incidents (operational), not to implementation delays.

**Why it matters:**
If Drupuv's implementation drags on for months—pushing back Fatesk's launch dates for its titles—Fatesk may have no clean exit. It would need to argue that the delay constitutes a "material breach" of the SOW, which is fact-intensive and uncertain, especially with the "commercially reasonable efforts" language.

**Recommended fix:**
Add to SOW §3.2: "If any milestone is delayed by more than thirty (30) days for reasons attributable to Drupuv (other than Fatesk's failure under Section 7), Fatesk may terminate this SOW and the Agreement upon written notice. Upon such termination, Drupuv shall refund all fees paid for unaccepted milestones and shall provide transition assistance under Section 12.5 of the Agreement."

---

## Issue 10 – Service Credit Cap (Moderate)

**Where it appears:**
- SLA §7.4: "Total service credits in any Service Month shall not exceed **50% of the Monthly Fee**."
- Monthly Fee = $1,840,000 ÷ 12 ≈ $153,333. Maximum monthly credits ≈ $76,667.

**Why it matters:**
If the platform has a bad month—say, 99.4% availability on two Core Services in two Regions, plus performance failures on all four commitments—the credits could theoretically exceed 50% of the Monthly Fee, but the cap limits Fatesk's recovery. More importantly, the cap means that even in a catastrophic month, Fatesk recovers at most ~$76,667 against a $1.84M annual fee. The credits are a modest remedy.

That said, Agreement §8.3 and SLA §7.6 both state that service credits do not limit Fatesk's other rights and remedies. So the cap is on the credit mechanism itself, not on Fatesk's ability to claim breach or terminate. The practical issue is that for sub-catastrophic but persistent underperformance, the credits are the primary remedy and they are capped low.

**Recommended fix:**
Increase the cap to 100% of the Monthly Fee. Alternatively, add a "chronic underperformance" trigger: if in any three consecutive Service Months the total availability of any Core Service in any Region falls below 99.5%, Fatesk may terminate under §8.4 (treating it as equivalent to chronic Severity 1 failure).

---

## Issue 11 – Overage Rate Lower Than Base Rate (Open Question)

**Where it appears:**
- Agreement §5.1: Annual license fee of $1,840,000 for 750,000 peak concurrent users (effective rate: ~$2.45/user/year).
- Exhibit B: Overage blocks of 50,000 users at $96,000/block/year (effective rate: $1.92/user/year).

**Why it matters:**
The marginal cost of additional users is *lower* than the base rate. This is unusual—overage rates are typically at a premium to incentivize capacity planning. This could be:
- A drafting error (the parties may have intended $96,000 per 50,000 to be a premium, but miscalculated); or
- Intentional (Drupuv's marginal cost of serving additional users is low, and it is offering a volume incentive).

If it is a drafting error, Drupuv may later argue for a correction. If it is intentional, it is favorable to Fatesk.

**Open question for client:** Was the $96,000/50,000 overage rate discussed and agreed at the Term Sheet stage? The Term Sheet (§4.3) references "the overage rate in Section 4.3" but does not state the dollar amount, so we cannot confirm from the Term Sheet whether this rate was in the original commercial discussion. I recommend confirming with the client whether this rate was negotiated or whether it appeared for the first time in the definitive documents.

**Recommended fix (if confirmed as intentional):** Add language to Exhibit B: "The overage rate set forth herein is agreed by the Parties to be the applicable rate for the full Term and shall not be subject to adjustment except by mutual written agreement."

---

## Issue 12 – Launch Window Constraints (Moderate)

**Where it appears:**
- Agreement §6.3: Up to 4 launch windows per contract year, each up to 14 days, with 30 days' advance notice.
- Term Sheet §5.5: "Fatesk could designate up to four launch windows per contract year." (No 14-day or 30-day limit stated.)

**Why it matters:**
Fatesk has three Licensed Titles (one of which, Project Halcyon, is a multi-platform launch across PC, PlayStation, Xbox, and Nintendo). A multi-platform launch with staggered platform-holder certification timelines could easily require more than 14 days of maintenance-free window. Additionally, 30 days' notice is a long lead time for a company that may need to adjust launch dates based on platform-holder certification or marketing decisions.

The 4-window limit also does not account for major content updates, seasonal events, or re-launches after a Severity 1 incident.

**Recommended fix:**
- Increase to 6 launch windows per contract year.
- Extend each window to 21 days.
- Reduce advance notice to 14 days (with 7 days for the first two windows in a contract year to allow for planning).
- Add: "If a Licensed Title requires a re-launch following a Severity 1 Incident, the re-launch window shall not count against the annual limit."

---

## Issue 13 – SLA Exclusion for Fatesk Code Defects – Boundary Ambiguity (Moderate)

**Where it appears:**
- SLA §7.5(b): Downtime is excluded if caused by "defects in Licensed Title code that is **not** Drupuv integration code delivered under the Statement of Work."

**Why it matters:**
In a live-service game, the boundary between "Fatesk's game code" and "Drupuv's integration code" can be blurry. For example, if a bug in Fatesk's matchmaking logic causes excessive API calls that degrade platform performance, is that a "defect in Licensed Title code" (excluded) or a platform capacity issue (not excluded)? Drupuv will have the incentive to characterize performance issues as Fatesk code defects to avoid SLA credits.

**Recommended fix:**
Add: "The Parties shall jointly investigate any incident for which Drupuv asserts this exclusion. If the investigation is inconclusive within five (5) business days, the incident shall not be excluded from service level calculations." Also clarify: "For purposes of this exclusion, 'Drupuv integration code' means all code delivered by Drupuv under the SOW, including SDK configuration, API integration layers, and any custom code written by Drupuv for the Licensed Titles."

---

## Issue 14 – No MFN or Price Protection Clause (Low)

**Where it appears:**
- Agreement §5.3: Drupuv may increase the annual license fee by up to 9% at each Renewal Term.
- No most-favored-nation clause or reference to Drupuv's pricing for other customers.

**Why it matters:**
Over a 3-year initial term plus two 3-year renewals (9 years total), Fatesk could face cumulative increases of up to ~36% if Drupuv raises fees at the maximum rate every renewal. There is no mechanism to benchmark Fatesk's pricing against what Drupuv charges other customers of similar scale.

**Recommended fix:**
Add: "Drupuv shall not charge Fatesk an annual license fee (including overage) that is greater than the fee charged by Drupuv to any other licensee with a Licensed Concurrency of 500,000 or more peak concurrent users, as in effect on the date of the applicable fee increase." Alternatively, cap cumulative increases over the full Term at 15%.

---

## Issue 15 – Force Majeure Carve-Out is Favorable but Ambiguous (Low)

**Where it appears:**
- Agreement §17.5: Force majeure "does not include failures of Drupuv's subcontractors or hosting providers that Drupuv's business continuity and redundancy measures would **reasonably have prevented**." Also: "Any such event does not excuse Drupuv's obligations under Section 7.2 or Section 9."

**Why it matters:**
The carve-out for subcontractor/hosting provider failures is good for Fatesk—it prevents Drupuv from hiding behind a cloud provider outage. The "reasonably have prevented" standard introduces some ambiguity (what would a reasonable BCP prevent?), but the overall structure is protective. The explicit preservation of §7.2 (Severity 1 response) and §9 (data security) obligations during force majeure is strong.

No change needed, but be aware that if the Severity 1 definition is fixed (Issue 1), this provision becomes even more valuable because it means Drupuv cannot use force majeure to avoid its enhanced response obligations.

---

## Open Questions for the Client

1. **Overage rate (Issue 11):** Was the $96,000/50,000 rate negotiated, or did it appear for the first time in the definitive documents? Please confirm.

2. **Launch window needs (Issue 12):** How many launch windows does Fatesk realistically expect to need per year across all three Licensed Titles, including potential re-launches and major updates? This will inform how aggressively to push on the 4-window/14-day limit.

3. **Competitor definition (Issue 3):** Does Fatesk have a specific list of competitors it wants to exclude from receiving an assignment? Or should we use a functional definition (e.g., "any entity that publishes a live-service game in the same genre as a Licensed Title")?

4. **SOW California venue (Issue 4):** Was the California governing law/venue in the SOW a Drupuv position that was negotiated, or did it appear in the draft without discussion? This affects how hard we push.

5. **Transition period needs (Issue 5):** If the deal breaks down, how long does Fatesk realistically need to migrate off the platform? 90 days? 180 days? This informs the data retention fix.

---

## Office Lease Note

The Wilmington office lease (`fatesk_wilmington_studio_office_lease.md`) runs from April 1, 2025 through March 31, 2032, with a 5-year extension option. It is not referenced by or relevant to the Drupuv license arrangement. I have not identified any interaction between the lease and the platform deal. If the client's question about the lease relates to a separate matter (e.g., whether the studio space is adequate for the implementation team, or whether the lease term aligns with the license term), please let me know and I can revisit.