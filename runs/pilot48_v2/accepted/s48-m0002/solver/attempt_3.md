# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Baineind Event Rentals, LLC – Beipeiv Software License Agreement: Issue Identification and Recommended Fixes

---

## Summary

I have reviewed all eight documents in the matter folder. I identify twelve issues ranging from a critical, time-sensitive assignment problem to operational gaps in the service level commitments. Issues 1 and 2 require immediate attention.

---

## Issue 1: Pending Change of Control Triggers Assignment Consent Requirement — Notice Letter Is Procedurally Deficient

**Where it appears:**
- Software License Agreement §16.2 (Change of Control of Licensee), §16.3 (Consequences)
- Baineind Notice Letter dated November 2, 2026, ¶¶2–3

**The problem:**

Section 16.2 provides that any direct or indirect change in Control of Licensee "is deemed an assignment of this Agreement by Licensee" and "requires Licensor's prior written consent, which Licensor may give or withhold in its sole discretion." The defined term "Control" (§1.4) captures ownership of more than 50% of voting equity or membership interests.

The November 2 notice letter discloses that Ostrander Holdings LLC (Baineind's sole member) has agreed to sell 100% of Baineind's membership interests to Kestrel Venue Group, Inc., with closing expected December 15, 2026. This is unambiguously a change in Control under §1.4(b) (power to direct management) and §1.4(a) (100% ownership transfer).

Critically, the letter states in ¶3: "This letter is provided for Beipeiv's information, and no action is required by Beipeiv in connection with it." It does **not** request Licensor's written consent as §16.2 requires.

If Beipeiv withholds consent (which it may do in its sole discretion), §16.3 provides that the change of control "is void as against Licensor" and Beipeiv "may terminate this Agreement immediately." Upon such termination, "all License Fees for the remainder of the Initial Term become immediately due and payable." The Initial Term runs through February 28, 2029. If Beipeiv terminates after the December 15, 2026 closing, Baineind would owe approximately 27 months of accelerated fees (~$418,500) plus any other accrued fees.

**Why it matters:**

Baineind is about to close a transaction that, as currently papered, gives Beipeiv a walk-away right with fee acceleration. The "sole discretion" standard means Baineind has no contractual leverage to compel consent. Kestrel Venue Group, as the incoming owner, would inherit a platform license that Beipeiv can terminate at will.

**Recommended fix:**

1. **Immediately** send a supplemental letter to Beipeiv expressly requesting written consent under §16.2, identifying the transaction, the incoming controller (Kestrel Venue Group), and the expected closing date. Do not rely on the November 2 letter, which frames the matter as informational only.
2. Seek consent **before** closing on December 15. If Beipeiv signals it may withhold consent, explore whether a negotiated side arrangement (e.g., a fee adjustment or a most-favored-nation commitment) can secure it.
3. If consent is a condition to closing, add it as a closing condition in the Kestrel purchase agreement or obtain a bring-down certificate.
4. Consider whether the "sole discretion" standard is challengeable under Delaware law as an implied covenant of good faith issue, but do not rely on this; it is an uncertain argument and Beipeiv could litigate it from a position of strength given the acceleration clause.

**Flag:** I cannot confirm from the documents whether Beipeiv has responded to the November 2 letter or whether any consent has been given. If Beipeiv has already consented in writing, this issue is resolved. Please confirm.

---

## Issue 2: Severity 1 Incident Definition Conflict — SLS Uses a Materially Narrower Definition Than the Agreement and the Term Sheet

**Where it appears:**
- Software License Agreement §1.18 (Definition of "Severity 1 Incident")
- Service Level Schedule §2.1 (Definition of "Severity 1 Incident")
- Platform License Term Sheet §6.2 (Description of intended Severity 1 definition)
- Software License Agreement §20.4(b) (Order of Precedence)

**The problem:**

The Agreement defines Severity 1 as: "any failure of the Platform preventing Licensee from creating, modifying or fulfilling Rental Orders **at any Licensee location**" (§1.18).

The Service Level Schedule defines Severity 1 as: "the **complete unavailability** of the Platform to **all** Authorized Users at **all** Licensee locations" (§2.1).

These are fundamentally different. Under the Agreement definition, a single warehouse losing access to the Rental Order module is a Severity 1 (1-hour response, 24×7, 4-hour resolution target). Under the SLS definition, that same event is a Severity 2 (4 Business Hours response, Business Hours only, 2-business-day resolution target).

The Term Sheet §6.2 used the broader language matching the Agreement, indicating the parties' original commercial understanding was the broader definition. The SLS deviated from that understanding.

Under §20.4(b), the SLS prevails "as to service levels." Since severity classification directly determines the applicable response times, resolution targets, and service credits, the SLS definition almost certainly controls. This means Baineind negotiated a broader protection in the Agreement that the SLS effectively nullifies.

**Why it matters:**

Baineind operates multiple warehouse locations. Event-day operations depend on dispatch and pick-list functions at each site. A partial outage affecting one warehouse on a Saturday during peak season would be classified as Severity 2 under the SLS, meaning:
- Response only during Business Hours (7 a.m.–7 p.m. ET, Mon–Fri) — a Saturday outage might not get a response until Monday morning.
- No 24×7 coverage.
- No continuous-effort obligation (that applies only to Severity 1 under SLS §3.2).
- No hourly status updates.
- No root-cause analysis obligation within 5 business days (SLS §3.3 applies only to Severity 1).

For an event rental company, this is a significant operational risk during peak seasons.

**Recommended fix:**

1. Request an amendment to SLS §2.1 to conform to the Agreement §1.18 definition, or at minimum to provide that a failure preventing Rental Order creation, modification or fulfillment at **any single** Licensee location constitutes a Severity 1 Incident.
2. If Beipeiv resists, propose a middle ground: a "Severity 1A" or modified Severity 2 tier for single-location outages that carries 24×7 response within 2 hours (rather than 1 hour) and a 6-hour resolution target.
3. Cite the Term Sheet §6.2 as evidence of the parties' original agreement on the broader definition.
4. In the interim, ensure Baineind's operations team understands that a single-location outage will be classified as Severity 2 and plan manual workarounds (phone orders, paper pick lists) for peak-season contingencies.

---

## Issue 3: Governing Law and Forum Conflict Between the Side Letter and the Agreement

**Where it appears:**
- Software License Agreement §20.1 (Delaware law), §20.2 (Wilmington, Delaware forum)
- Side Letter §6.1 (New York law), §6.2 (Manhattan, New York forum)
- Platform License Term Sheet §13.1–13.2 (Delaware law and forum, consistent with the Agreement)

**The problem:**

The Side Letter provides that "This Side Letter, **and the Agreement as modified hereby**, are governed by and construed in accordance with the laws of the State of New York" and submits the parties to "exclusive jurisdiction of the state or federal courts located in the Borough of Manhattan, New York" for "any action arising out of or relating to this Side Letter **or the Agreement as modified hereby**."

This creates a direct conflict with the Agreement's Delaware governing law and Wilmington forum. The Side Letter purports to change the governing law and forum for the entire Agreement, not just for Side Letter-specific disputes.

The order of precedence in §20.4(a) gives the Side Letter first priority. One could argue that the Side Letter's governing law clause, as the highest-priority document, controls. But §20.4 is itself a provision of the Agreement, and it is unusual for a side letter to unilaterally change the governing law of the main agreement without express acknowledgment in the main agreement.

**Why it matters:**

- If Baineind needs to enforce peak-season support obligations (e.g., Beipeiv fails to provide the named engineer), the dispute may need to be brought in New York under New York law.
- If Baineind needs to terminate for breach of the main Agreement (e.g., repeated Platform failures), the forum and law may be Delaware.
- A single dispute could implicate both sets of terms, creating jurisdictional complexity, increased litigation costs, and uncertainty about which law's substantive rules apply.
- New York law may interpret certain provisions (e.g., the "sole discretion" standard in §16.2, or the scope of the implied covenant of good faith) differently than Delaware law.

**Recommended fix:**

1. Seek a clarifying amendment stating that the Side Letter's governing law and forum provisions apply **only** to disputes arising exclusively under the Side Letter, and that all other disputes remain governed by Delaware law and the Wilmington forum under §§20.1–20.2.
2. Alternatively, conform the Side Letter to Delaware law and forum for consistency.
3. If no amendment is obtained, flag to the client that any dispute touching both the Side Letter and the Agreement may require parallel or consolidated proceedings in two jurisdictions.

---

## Issue 4: Resolution Targets Are Non-Binding; No Service Credits for Missed Resolution Times

**Where it appears:**
- Service Level Schedule §3.1 (Resolution Targets table), §3.4 (Resolution Targets are "targets"), §5.3–5.4 (Service Credits only for availability and response failures)

**The problem:**

SLS §3.4 states: "The Resolution targets in Section 3.1 are targets. Licensor shall use commercially reasonable efforts to meet them. Service credits are payable only as set out in Section 5."

Section 5 provides credits only for:
- Monthly Availability below 99.9% (§5.3), and
- Missed Severity 1 **Response** times (§5.4).

There are **no** service credits for missed **Resolution** targets. A Severity 1 Incident that is responded to within 1 hour but not resolved for 24 hours (versus the 4-hour target) generates no credit, as long as the total downtime for the month keeps availability above 99.9%.

Given that 99.9% monthly availability permits up to ~43 minutes of downtime per 30-day month (and ~44 minutes per 31-day month), a single 43-minute Severity 1 outage uses the entire monthly allowance. But a 3-hour outage that is responded to on time and resolved in 3 hours (missing the 4-hour target by a hair) would generate no credit if it is the only downtime that month and total downtime stays under 43 minutes. Wait — 3 hours = 180 minutes, which exceeds 43 minutes, so availability would fall below 99.9%. Let me recalculate.

99.9% of a 30-day month (43,200 minutes) allows 43.2 minutes of downtime. So any Severity 1 Incident lasting more than ~43 minutes in a month will trigger at least the 5% availability credit. The resolution target gap matters most for Severity 2 incidents (which don't count toward "Downtime Minutes" under SLS §5.2, since only Severity 1 incidents do). A Severity 2 incident lasting 3 business days (missing the 2-business-day target) generates no credit at all.

**Why it matters:**

For Baineind, the most damaging outages may be partial (single-location, single-module) failures that are classified as Severity 2 under the SLS's narrow Severity 1 definition (see Issue 2). These don't count toward the availability calculation at all, and there are no credits for missed resolution targets. Baineind could experience repeated multi-day partial outages with zero financial remedy.

**Recommended fix:**

1. Negotiate service credits for missed Resolution targets, at least for Severity 1 and Severity 2 incidents. For example: 2% of Monthly Fee for each business day a Severity 2 Resolution target is missed.
2. Alternatively, negotiate that Severity 2 incidents affecting a core module (inventory, quoting, Rental Order, dispatch, pick-list) at a single location during a Peak Season count as Severity 1 for credit purposes.
3. If no amendment is obtained, ensure Baineind's operations team documents the business impact of each missed resolution target to support a potential material breach claim under §15.3(a) if the pattern becomes systemic.

---

## Issue 5: Liability Cap and Consequential Damages Exclusion May Leave Baineind Uncompensated for Business Loss

**Where it appears:**
- Software License Agreement §13.1 (Cap: 12 months' fees = $186,000), §13.2 (Exclusion of indirect/consequential damages, lost profits, revenues), §13.3 (Excluded Claims)

**The problem:**

The liability cap is $186,000 (one year's fees). Consequential damages — including lost profits and lost revenues — are excluded. The Excluded Claims (§13.3) that pierce the cap are limited to: indemnification obligations, confidentiality breaches, gross negligence/fraud/willful misconduct, and fee payment obligations.

A Platform failure or data error that causes Baineind to miss event deliveries, double-book inventory, or lose customers would result in lost revenues that are expressly excluded. Baineind's maximum recovery for any non-excluded claim is $186,000, regardless of actual damages.

**Why it matters:**

A single lost event season or a major customer relationship damaged by a Platform failure could easily exceed $186,000 in lost revenue. The cap and exclusion together mean Baineind bears the economic risk of Platform failures above that threshold.

**Recommended fix:**

1. Negotiate a super-cap (e.g., 2× or 3× annual fees) for claims arising from Platform failures or data errors that cause direct loss to Baineind's operations.
2. Alternatively, seek to add "loss of revenue directly resulting from a Severity 1 Incident" to the Excluded Claims in §13.3, so it is not subject to the cap or the consequential damages waiver.
3. If no amendment is obtained, ensure Baineind maintains its own business interruption insurance that covers technology-dependent revenue loss, and document the causal link between any Platform failure and specific lost revenues to support a gross negligence argument if warranted.

---

## Issue 6: Side Letter Peak-Season Rates Are "Fixed for the Initial Term" Only — Post-Renewal Pricing Is Ambiguous

**Where it appears:**
- Side Letter §3.2 ("These rates are fixed for the Initial Term"), §3.3 (off-peak rates capped at 110% of §3.1 rates)

**The problem:**

The fixed Peak Season rates in §3.1 apply only during the Initial Term (through February 28, 2029). The Side Letter does not state what happens to these rates during Renewal Terms. Section 3.3 provides that off-peak rates "may not exceed the rates in Section 3.1 by more than ten percent (10%)" — but if §3.1 rates are no longer "fixed" after the Initial Term, the cap in §3.3 floats. Beipeiv could argue that after the Initial Term, it may increase the §3.1 rates (subject to the general 5% annual cap in Agreement §5.4, which applies to "License Fees" and may not cover Additional Services rates), and the §3.3 off-peak cap would adjust accordingly.

**Why it matters:**

Baineind's seasonal staffing and event-day support planning depends on predictable costs. If Peak Season rates can increase after the Initial Term without the same 5% cap that applies to License Fees, Baineind faces unbounded cost growth for services it needs most.

**Recommended fix:**

1. Amend Side Letter §3.2 to provide that the §3.1 rates are fixed for the entire Term (Initial + all Renewal Terms), or subject to the same 5% annual cap in Agreement §5.4.
2. Clarify that §3.3's 10% cap references the §3.1 rates as in effect at the start of the applicable contract year, not as adjusted.

---

## Issue 7: On-Site Event-Day Support Has a 10-Business-Day Start Requirement — Operationally Unworkable for Short-Notice Events

**Where it appears:**
- Side Letter §3.2 (second sentence)

**The problem:**

"For on-site event-day support, Licensor shall start within ten (10) business days." This means if Baineind needs a Beipeiv engineer on-site at a warehouse for a specific event day, it must give at least 10 business days' notice (roughly two calendar weeks).

For an event rental company, last-minute changes, additional events, or urgent issues requiring on-site troubleshooting may arise with far less than two weeks' notice. The other services in §3.1 have a 3-business-day start requirement, which is more reasonable but still long for urgent needs.

**Why it matters:**

During Peak Seasons, Baineind's operational tempo is highest. A 10-business-day lead time for on-site support effectively means Baineind must anticipate all on-site needs two weeks in advance, which is impractical for event-day contingencies.

**Recommended fix:**

1. Negotiate a shorter start time for on-site event-day support during Peak Seasons — ideally 3 business days (matching the other services) or 2 business days for events already in the dispatch system.
2. Alternatively, create an "urgent on-site" tier at a premium rate (e.g., 1.5× the $1,600/day rate) with a 48-hour start time.
3. If no amendment is obtained, build the 10-business-day lead time into Baineind's event scheduling process and ensure the Dispatch Manager flags potential on-site support needs at the time events are booked.

---

## Issue 8: Insurance Certificate Does Not Commit Beipeiv to the 30-Day Cancellation Notice Required by the Agreement

**Where it appears:**
- Software License Agreement §14.2 (30-day notice of cancellation or material reduction)
- Beipeiv Certificate of Insurance §8.1 ("notice will be delivered in accordance with the policy provisions"), §1.1 ("confers no rights upon the Certificate Holder")

**The problem:**

The Agreement requires Beipeiv to "notify Licensee within thirty (30) days after any cancellation or material reduction of coverage" (§14.2). The certificate's cancellation clause (§8.1) states only that notice "will be delivered in accordance with the policy provisions" — which typically means the insurer will notify the named insured (Beipeiv), not the certificate holder (Baineind). Standard certificate language (§1.1) disclaims any rights for the certificate holder.

So the certificate does not, and cannot, satisfy Beipeiv's contractual obligation to give Baineind 30-day notice. Baineind's protection depends entirely on Beipeiv independently monitoring its policies and sending notice.

**Why it matters:**

If Beipeiv's Technology E&O or Cyber policy is cancelled or materially reduced (e.g., limits dropped, coverage narrowed) and Beipeiv fails to notify Baineind within 30 days, Baineind could discover the gap only after a claim is denied. The Technology E&O and Cyber policies are claims-made with a retroactive date of March 1, 2019; if the policy lapses, new claims arising after the lapse would not be covered.

**Recommended fix:**

1. Request that Beipeiv's insurance broker (Halloway Ridge) add Baineind as a notice party on the policies, or that Beipeiv obtain a certificate endorsement committing to direct notice to Baineind upon cancellation or material change.
2. Add Baineind as an additional insured on the Technology E&O and Cyber policies, at minimum for claims arising from Baineind's use of the Platform. (The Agreement does not require this, but it would give Baineind a direct right to make a claim.)
3. Calendar an annual request for updated certificates of insurance, aligned with the policy renewal dates (March 1).

---

## Issue 9: Force Majeure and Internet/Utility Failures Are Excluded from Downtime Calculations

**Where it appears:**
- Service Level Schedule §5.6(e) (excludes "events described in Section 19.1 of the Agreement" from Downtime Minutes)
- Software License Agreement §19.1 (includes "failures of public utilities or the internet")

**The problem:**

SLS §5.6(e) excludes from Downtime Minutes any period caused by events in §19.1, which includes "failures of public utilities or the internet." The only carve-back is for "any failure of Licensor's disaster recovery or business continuity measures."

This means if Beipeiv's data center loses internet connectivity due to a carrier outage or a utility failure at the data center, the resulting Platform unavailability does not count toward the 99.9% Monthly Availability calculation and generates no service credits. Beipeiv is not required to have redundant internet connections or backup power as a contractual matter — only that its "disaster recovery or business continuity measures" not fail.

**Why it matters:**

A cloud platform is only as available as its data center's connectivity and power. If the data center's internet provider has an outage, Baineind's platform is down but Beipeiv owes no credits. For an event rental company operating on tight delivery windows, this is a significant gap.

**Recommended fix:**

1. Negotiate a requirement that Beipeiv maintain redundant internet connectivity (multiple carriers) and backup power (UPS + generator) at its data center, and that failures of these redundant systems constitute a failure of "disaster recovery or business continuity measures" (triggering the carve-back in §5.6(e)).
2. Alternatively, narrow the §5.6(e) exclusion to apply only to failures of public internet infrastructure external to Beipeiv's data center perimeter, not to failures of Beipeiv's own connectivity to the internet.
3. Request that Beipeiv identify its data center provider and confirm the provider's SLA, so Baineind can assess the real-world risk.

---

## Issue 10: Service Credit Claim Process Is Misaligned with Annual Prepayment

**Where it appears:**
- Service Level Schedule §5.7 (credits applied against "next invoice"; if no further fees payable, paid within 30 days)
- Software License Agreement §5.1 (fees paid annually in advance)

**The problem:**

License Fees are paid annually in advance (§5.1). The first payment was due within 30 days of March 1, 2026 (i.e., by March 31, 2026). The next payment is not due until March 1, 2027. SLS §5.7 provides that credits are "applied against the next invoice for License Fees." If no further License Fees are payable (i.e., between annual payment dates), Beipeiv "shall pay the credit to Licensee within thirty (30) days."

This means if Baineind earns service credits in, say, June 2026, it must wait until March 2027 to have them applied (or request a cash refund under the second sentence of §5.7). The 30-day claim window (§5.7, first sentence) runs from the end of the month of the failure, so Baineind must file its claim by, e.g., July 30 for a June failure, but won't see the credit for 8+ months.

**Why it matters:**

This creates a cash flow mismatch and administrative burden. Baineind is effectively financing Beipeiv's service failures for up to 11 months.

**Recommended fix:**

1. Amend SLS §5.7 to require cash payment of credits within 30 days of the end of the month in which the failure occurred, rather than application against the next annual invoice.
2. Alternatively, provide that credits are applied as a reduction to the next annual payment, with a corresponding reduction in the invoice amount (so Baineind doesn't overpay and wait for a refund).
3. In the interim, ensure Baineind's finance team tracks all service credits earned and includes them in the calculation of the next annual payment to avoid overpaying.

---

## Issue 11: "Contract Year" Is Undefined in the Side Letter, Creating Ambiguity in Peak Season Modification Timing

**Where it appears:**
- Side Letter §1.2 (60-day notice before "the start of a contract year")
- Software License Agreement §1 (Definitions — no definition of "contract year")

**The problem:**

Side Letter §1.2 allows Licensee to move a Peak Season by up to 14 days "by written notice given at least sixty (60) days before the start of a contract year." The term "contract year" is not defined in the Side Letter or the Agreement. The Agreement uses "Initial Term" (3 years) and "Renewal Term" (1 year each) but never "contract year."

Possible interpretations:
- Each 12-month period starting on the Effective Date anniversary (March 1).
- Each calendar year.
- Each term period (3-year Initial Term, then 1-year Renewal Terms).

If "contract year" means the 12-month period starting March 1, then for the first contract year (March 1, 2026 – February 28, 2027), the 60-day notice deadline was December 31, 2025 — before the Agreement was even in effect. This makes the first-year modification right impossible to exercise.

**Why it matters:**

If Baineind wants to shift a Peak Season (e.g., to accommodate a changed event calendar), it may have already missed the notice deadline, or it may be unclear when the next deadline falls.

**Recommended fix:**

1. Seek a clarifying amendment defining "contract year" as each successive 12-month period starting on the Effective Date, and providing that for the Initial Term, the first notice deadline is 60 days before the start of the second contract year (i.e., by December 31, 2026 for the March 1, 2027 – February 28, 2028 period).
2. In the interim, if Baineind needs to adjust a Peak Season, send notice well in advance and cite the ambiguity to preserve the right.

---

## Issue 12: The Term Sheet Evidences a Different Commercial Understanding on Severity 1 Than the Final SLS

**Where it appears:**
- Platform License Term Sheet §6.2 (Severity 1 defined broadly, matching Agreement §1.18)
- Service Level Schedule §2.1 (Severity 1 defined narrowly)
- Platform License Term Sheet §1.2 (non-binding except for confidentiality, costs, governing law)

**The problem:**

The Term Sheet §6.2 states: "'Severity 1 Incident' will mean any failure of the Platform preventing Licensee from creating, modifying or fulfilling Rental Orders at any Licensee location. Licensee's event-day operations depend on order, dispatch and pick-list functions being available at each warehouse."

This is the same broad definition that appears in Agreement §1.18. The final SLS §2.1 replaced it with the narrow "complete unavailability at all locations" definition. The Term Sheet is non-binding (§1.2), so it cannot be used as a contractual basis for the broader definition. However, it is strong evidence of the parties' original commercial understanding and could be relevant in a parol evidence or reformation argument if the SLS definition were challenged as a scrivener's error or as contrary to the deal the parties actually struck.

**Why it matters:**

This supports Baineind's position in Issue 2. If Beipeiv resists amending the SLS, Baineind can point to the Term Sheet as evidence that the broader definition was the agreed commercial term and that the SLS deviation was not a negotiated change but a drafting error.

**Recommended fix:**

Use the Term Sheet as leverage in the negotiation described in Issue 2. If Beipeiv claims the narrower definition was intentional, request the negotiation history (email threads, draft comparisons) to confirm. If the narrower definition appeared only in the final SLS draft without corresponding negotiation, this strengthens the reformation argument.

**Flag:** The Term Sheet is marked non-binding. Its evidentiary value in a Delaware court would depend on the specific legal theory (reformation, course of dealing, or parol evidence to explain ambiguity). I have not researched the applicable Delaware standards and flag this for further analysis if the issue becomes litigated.

---

## Additional Observations (Lower Priority)

| # | Observation | Where | Note |
|---|---|---|---|
| A | Baineind is not an additional insured on any of Beipeiv's policies | Certificate of Insurance §§3, 5 | Not required by the Agreement, but would provide a direct claim path. See Issue 8. |
| B | The Agreement's warranty remedy (§11.2) provides no fee reduction or credit for the period of non-conformity | Software License Agreement §11.2 | Baineind pays full fees while the Platform is defective, up to 30 days before termination is available. |
| C | Quality Agreement §5.5 requires Licensor to correct disputed Data Errors at Licensee's request while classification is unresolved, but Licensor may later charge if it turns out to be a Licensee Data Error | Quality Agreement §5.5 | This is fair in principle but could create friction; ensure Baineind's Data Quality Contact documents the basis for each dispute. |
| D | The Side Letter §2.3 maintenance restriction (no non-emergency maintenance on weekends/pre-holidays during Peak Season) does not define "non-emergency" | Side Letter §2.3; cf. SLS §5.6(b) (defines "emergency maintenance" narrowly as security vulnerabilities) | If "emergency" is read broadly by Beipeiv, the weekend restriction could be easily circumvented. Consider conforming the Side Letter to the SLS's narrow definition. |
| E | Agreement §15.5 provides transition assistance for up to 90 days at "then-current professional services rates" | Software License Agreement §15.5 | No rate cap. If Baineind needs to exit, transition costs could be significant and are not addressed in the Side Letter's fixed-rate schedule. |

---

## Items I Cannot Resolve From the Documents Alone

1. **Whether Beipeiv has responded to the November 2, 2026 notice letter or given/withheld consent under §16.2.** This is the single most time-sensitive question. If consent has been given, Issue 1 is resolved. If Beipeiv has indicated it will withhold consent, Baineind needs to act before the December 15 closing.

2. **Whether the SLS Severity 1 definition was a negotiated change or a drafting error.** The Term Sheet supports the broader definition, but I cannot determine from the documents whether the narrower definition was proposed and accepted during negotiations. Request the negotiation file (drafts, emails, call notes) from Beipeiv's counsel.

3. **The identity of Beipeiv's data center provider and its own SLA.** This is relevant to Issue 9 (internet/utility failure exclusion) and to assessing real-world availability risk.

4. **Whether Baineind has experienced any Severity 1 or Severity 2 incidents since go-live (targeted April 6, 2026).** If so, the classification disputes in Issue 2 may already be practically significant, and Baineind should review whether any service credits were earned but not claimed (30-day deadline under SLS §5.7).

5. **The current status of the Kestrel Venue Group transaction.** The notice letter says closing is "currently expected" for December 15, 2026, and is "subject to customary closing conditions." If the transaction structure changes (e.g., to an asset sale rather than equity sale), the §16.2 analysis would need to be revisited.

---

## Recommended Next Steps (Priority Order)

1. **Today:** Confirm whether Beipeiv has responded to the November 2 letter. If not, send a supplemental letter requesting §16.2 consent before the December 15 closing.
2. **This week:** Draft a letter to Beipeiv raising Issues 2, 3, and 4 as items for amendment, citing the Term Sheet for Issue 2 and the practical operational impact for Issues 3–4.
3. **Before the next quarterly review (SLS §7.2):** Present Issues 5, 6, 7, 9, and 10 as items for the parties to address in a renewal-term amendment package.
4. **Ongoing:** Ensure Baineind's IT Manager tracks the 30-day service credit claim deadline (SLS §5.7) and the 60-day data export window (Agreement §7.3) on a calendar.