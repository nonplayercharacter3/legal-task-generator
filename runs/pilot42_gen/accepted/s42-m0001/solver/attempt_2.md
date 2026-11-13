# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Gaimun Brewing Company, LLC – Breneth Systems Software License: Issue Identification and Recommended Fixes

---

## Summary

I reviewed all five documents in the matter folder. I identified twelve issues, ranging from a critical gap that could expose Gaimun to roughly $930,000 in accelerated fees to drafting conflicts that shift the governing law to Colorado. The four most urgent items are flagged below; the full list follows in priority order.

---

## Issue 1 – Change of Control: No Consent Obtained Despite Known Merger

**Where:** Agreement §14.2; Side Letter, Recital B.

**What the documents say:**

- §14.2 provides that any Change of Control of Customer "shall be deemed an assignment" requiring Breneth's prior written consent. If a Change of Control occurs without consent, Breneth may terminate, and **all Fees for the remainder of the Subscription Term become immediately due and payable.**
- The Side Letter's Recital B acknowledges that Gaimun entered a merger agreement on September 30, 2026 under which it will become a wholly owned subsidiary of Ostrander Beverage Holdings LLC, with closing expected in Q1 2027.
- The Subscription Start Date is January 1, 2027 (Order Form §2.1), and the Initial Term is 60 months (Order Form §2.2).

**Why it matters:** The merger will almost certainly close during the first month or two of the subscription. At $186,000 per year over 60 months, the total contract value is approximately $930,000. If Breneth asserts that the closing constitutes an unconsented Change of Control, it could terminate and demand the full remaining balance immediately. The Side Letter acknowledges the deal but says nothing about consent or waiver. This is the single largest financial exposure in the file.

**Recommended fix:** Before the Ostrander closing, obtain Breneth's written consent to the Change of Control (or a specific waiver of §14.2 as it applies to this transaction). This should be added to the Side Letter or executed as a separate consent letter. If Breneth resists, negotiate at minimum: (a) consent conditioned on Ostrander assuming the Agreement, and (b) elimination of the accelerated-fee consequence, replacing it with a standard termination-and-refund mechanism.

**Confirm with client:** Has any consent or waiver been discussed with Breneth? Is the Ostrander closing date firm, and does it fall after January 1, 2027?

---

## Issue 2 – Governing Law and Forum: Side Letter Overrides New York to Colorado

**Where:** Side Letter §§4.1–4.2; Agreement §§16.1–16.2; Agreement §1.4 (order of precedence).

**What the documents say:**

- Agreement §16.1 selects New York law; §16.2 selects New York County courts.
- Side Letter §4.1 selects Colorado law; §4.2 selects Denver, Colorado courts. The Side Letter's scope language reads: "This Side Letter **and the Agreement as modified hereby** … are governed by the laws of the State of Colorado."
- Agreement §1.4 sets the order of precedence: Side Letter first, then Order Form, then Service Level Schedule, then the body of the Agreement.

**Why it matters:** Because the Side Letter has the highest precedence and expressly purports to govern "the Agreement as modified hereby," a court would likely hold that Colorado law and Denver forum apply to the entire Agreement, not just the pricing terms in the Side Letter. Gaimun is a Kingston, New York brewery. Litigating in Denver under Colorado law is costly and inconvenient, and Colorado law may interpret certain provisions (e.g., the liability cap, the sole-remedy clause) differently than New York law would.

**Recommended fix:** Delete Side Letter §4 in its entirety. The main Agreement's New York governing law and forum clause should control. If Breneth insists on a neutral forum, propose New York (Gaimun's home) or at minimum a provision that the Side Letter's pricing terms are governed by the same law as the rest of the Agreement.

**Confirm with client:** Whether Gaimun has any operational presence in Colorado that would make Denver forum less onerous than it appears.

---

## Issue 3 – Service Credits as Sole Remedy for Data Loss (Precedence Conflict)

**Where:** Schedule B §5.4; Agreement §11.3(b); Agreement §1.4.

**What the documents say:**

- Schedule B §5.4: "Service Credits are Customer's sole and exclusive remedy, and Breneth's sole liability, for any Service failure, including … **loss or corruption of Customer Data arising from or in connection with any Service failure**."
- Agreement §11.3(b): The liability cap does **not** apply to "Breneth's liability for breach of its obligations under Section 8 (Data Security) or Section 9 (Confidentiality), **including liability for any loss or corruption of Customer Data and the costs of restoring it**."
- Under §1.4, the Service Level Schedule has **higher** precedence than the body of the Agreement.

**Why it matters:** Read together with the precedence rule, Schedule B §5.4 overrides the §11.3(b) carve-out. The practical effect: if a "Service failure" (defined broadly in Schedule B §1.1(f) as "any failure of the Platform to perform materially in accordance with the Documentation") causes Gaimun's data to be lost or corrupted, Gaimun's maximum recovery is a Service Credit of 10% of the Monthly Fee—approximately **$1,550**—regardless of the actual damage. For a brewery whose Customer Data includes recipes, formulations, TTB filing history, and distributor pricing, a data loss event could cause far greater harm.

**Recommended fix:** Amend Schedule B §5.4 to carve out data loss or corruption caused by Breneth's breach of Section 8 (Data Security) or Section 9 (Confidentiality), so that those claims are not subject to the Service Credit sole-remedy limitation. The carve-out should track the language already in §11.3(b). Alternatively, add a sentence: "Notwithstanding the foregoing, this Section 5.4 does not limit Customer's rights under Section 11.3(b) of the Agreement."

---

## Issue 4 – Auto-Renewal for 60-Month Terms with a 15-Day Opt-Out Window

**Where:** Agreement §3.2; Order Form §2.2.

**What the documents say:**

- The Initial Subscription Term is 60 months (Order Form §2.2).
- §3.2: Upon expiry, the subscription "automatically renews for successive renewal periods, **each equal in length to the Initial Subscription Term**" (i.e., another 60 months).
- Non-renewal notice must be delivered "no earlier than 60 days and no later than 45 days before the end of the then-current … Term." A notice outside that window "shall not be effective."

**Why it matters:** Gaimun has a 15-day window (days 60 through 45 before term end) to prevent a five-year auto-renewal. If it misses that window—because the responsible person is on leave, the calendar reminder fails, or the company is in the middle of a transition—it is locked in for another 60 months at the then-current fee. Given that the Initial Term itself is five years, the first renewal decision will come in January 2032, and the opt-out window will be roughly November–December 2031.

**Recommended fix:** (a) Widen the notice window to "no earlier than 90 days and no later than 30 days before the end of the then-current Term," giving a 60-day window. (b) Reduce the Renewal Term to 12 months so that each renewal is a shorter commitment. (c) Add a requirement that Breneth send a renewal reminder notice at least 90 days before the opt-out window opens. At minimum, Gaimun should put a calendar reminder now for November 2031.

---

## Issue 5 – No Service Level for TTB Report Accuracy

**Where:** Schedule B §§1.1(b), 2.1, 4.3; Agreement §2.4, §10.2.

**What the documents say:**

- The SLA measures **availability** (uptime) and **support response times**. "Available" means users can log in and use core modules "in material conformity with the Documentation" (Schedule B §1.1(b)).
- Agreement §2.4 obligates Breneth to maintain the TTB module so report formats "conform to the TTB forms current as of the date of each update."
- Agreement §10.2 warrants the Platform will perform "materially in accordance with the Documentation."

**Why it matters:** The SLA does not test whether the TTB module actually generates correct or compliant reports. If the module is "Available" (users can log in and click through) but produces a report with a calculation error, a wrong form version, or a misclassified tax category, that is not a "Service failure" under the SLA. Gaimun would have to rely on the general warranty (§10.2) and the limitation of liability (§11), and the "materially" qualifier gives Breneth a defense. For a regulated industry where incorrect TTB filings can trigger penalties, interest, and compliance audits, this gap is significant.

**Recommended fix:** Add a specific obligation in the Agreement (not just the SLA) that Breneth will test and validate TTB report output against the then-current TTB forms and instructions before each regulatory filing cycle, and that material errors in generated reports constitute a breach of the Platform Warranty. Consider adding a service credit or fee abatement for months in which a TTB report error is traced to a Platform defect.

**Confirm with client:** What are Gaimun's actual TTB filing deadlines and the potential penalties for late or inaccurate filings? This will help calibrate the remedy.

---

## Issue 6 – Force Majeure Can Excuse Downtime During TTB Filing Windows

**Where:** Agreement §15.2; Schedule B §2.3(e); Schedule B §3.4.

**What the documents say:**

- §15.2 excuses both parties from performance (other than payment) during force majeure events.
- Schedule B §2.3(e) excludes force majeure events from the Downtime calculation, so they do not count against the 99.5% Availability Commitment.
- Schedule B §3.4 requires Breneth to use "commercially reasonable efforts" to avoid Scheduled Maintenance in the last three Business Days before TTB deadlines—but this applies only to Scheduled Maintenance, not to force majeure outages.

**Why it matters:** If a cyberattack, natural disaster, or other force majeure event takes the Platform offline during a TTB filing window, Gaimun has no SLA credit, no contractual remedy, and may miss a regulatory deadline. The only protection is the maintenance-scheduling courtesy in §3.4, which does not extend to unplanned events.

**Recommended fix:** Add a provision requiring Breneth to maintain disaster-recovery and business-continuity capabilities sufficient to restore the TTB excise reporting module within 24 hours of any force majeure event, or to provide Gaimun with an offline export of pending report data within a specified timeframe. At minimum, clarify that a force majeure event affecting the TTB module triggers the Severity 1 response protocol even if it is excluded from the Availability calculation.

---

## Issue 7 – Subscription Starts Even If Onboarding Is Incomplete

**Where:** Order Form §2.1; Side Letter §§1.2, 2.2; Onboarding Email 3 (timeline).

**What the documents say:**

- The Subscription Start Date is January 1, 2027 (Order Form §2.1).
- The first invoice is due "on or after the Subscription Start Date" (Side Letter §1.2; Order Form §3.2).
- Side Letter §2.2 requires onboarding to be "completed before the Subscription Start Date," but there is no consequence stated if it is not.
- The onboarding timeline (Email 3) shows a go-live readiness check on December 29, 2026—two days before the Start Date.

**Why it matters:** If data migration, TTB configuration, or training is not finished by January 1, 2027, the clock is already running and the first $186,000 invoice is due. There is no provision for a delayed start, a credit, or a termination right if onboarding fails. Given that the timeline is tight (only about 10 weeks from kickoff to go-live) and involves importing years of spreadsheet data, slippage is a real risk.

**Recommended fix:** Add a provision that if onboarding is not complete by the Subscription Start Date due to Breneth's failure to perform, the Subscription Start Date (and the first invoice) are delayed day-for-day, and if the delay exceeds 30 days, Gaimun may terminate without penalty. Alternatively, add a service credit for each week of delay.

**Confirm with client:** How confident is Gaimun that its data (spreadsheets going back to 2019, per Email 2) is in a state that can be imported cleanly? Any known data quality issues?

---

## Issue 8 – Expansion Pricing Terms Are Ambiguous

**Where:** Side Letter §§3.1–3.2; Order Form §5.

**What the documents say:**

- §3.1: Additional Authorized Users at "a price per additional Authorized User no higher than the **per-user rate implied by** the Subscription Fees in Order Form No. 001." That works out to $186,000 ÷ 25 = $7,440 per user per year.
- §3.2: Additional facilities at "a discount of fifteen percent (15%) from Breneth's **then-current list price for a facility of comparable size**."

**Why it matters:** "List price" is not defined in any document. "Comparable size" is subjective. If Gaimun adds a second facility post-merger (the Side Letter Recital B anticipates increased production volumes), Breneth could argue that Gaimun's Kingston facility is not "comparable" to its list-price benchmark, or that "list price" has changed. The implied per-user rate in §3.1 is clearer but still depends on the base fee remaining $186,000, which the price hold ensures only during the Initial Term.

**Recommended fix:** (a) Define "list price" by reference to a specific published rate card or by fixing a dollar amount. (b) Define "comparable size" objectively (e.g., "a facility with production capacity within ±25% of Customer's Kingston facility"). (c) For §3.1, state the dollar amount explicitly: "no higher than $7,440 per additional Authorized User per year, prorated."

---

## Issue 9 – Data Export Request Window Is Only 30 Days Post-Termination

**Where:** Agreement §7.4.

**What the documents say:** Upon expiry or termination, Customer must request data export "within thirty (30) days thereafter." Breneth then has 60 days to delete.

**Why it matters:** If Gaimun terminates (or the term expires) and the team is focused on transition, wind-down, or a merger integration, 30 days is a short window to remember to send the written request. If it is missed, the contractual right to request export lapses, and Gaimun's data (recipes, TTB history, distributor records) could be deleted in 60 days with no recourse.

**Recommended fix:** Extend the request window to 90 days. Alternatively, make export automatic upon termination without requiring a customer request, with deletion following 60 days after the automatic export is made available.

---

## Issue 10 – Backup Retention: "Until Overwritten" Is Indeterminate

**Where:** Agreement §7.4 (last sentence); Agreement §8.2(c).

**What the documents say:**

- §7.4: After the 60-day deletion period, "copies retained in routine backups … shall remain subject to Section 8 until overwritten."
- §8.2(c): Backups are retained "not less than thirty (30) days."

**Why it matters:** The minimum backup retention is 30 days, but "until overwritten" could mean 30 days, 90 days, or longer depending on Breneth's backup rotation cycle. For a brewery whose recipes and formulations are trade secrets, an indeterminate retention period in a third party's systems is a residual confidentiality risk, even though Section 8 obligations technically survive.

**Recommended fix:** Specify a maximum backup retention period (e.g., 90 days) after which backups containing Customer Data must be irrecoverably deleted or cryptographically erased.

---

## Issue 11 – 72-Hour Security Incident Notification May Be Tight for Regulatory Response

**Where:** Agreement §8.3.

**What the documents say:** Breneth must notify Gaimun "without undue delay, and in any event within seventy-two (72) hours" of becoming aware of a Security Incident.

**Why it matters:** If the incident involves TTB excise data or distributor information, Gaimun may have its own notification obligations (e.g., to the TTB, to affected distributors under contract, or under state data-breach statutes). Seventy-two hours to receive notice, then assess, then act, is a compressed timeline. The clause also says "after becoming aware"—if Breneth's detection is delayed, the 72-hour clock starts late.

**Recommended fix:** Shorten to 48 hours. Add a requirement that the notice include (to the extent known) the nature of the incident, the categories of data affected, and the number of records involved, so Gaimun can begin its own regulatory assessment immediately.

---

## Issue 12 – Fees Are Non-Cancellable and Non-Refundable (General Rule)

**Where:** Agreement §4.1; partially mitigated by §13.3(c) and §12.4.

**What the documents say:**

- §4.1: "Fees are non-cancellable and non-refundable."
- §13.3(c): If Customer terminates for cause (§13.1) or insolvency (§13.2), Breneth refunds prepaid Fees for the post-termination period.
- §12.4: If the Platform is subject to an IP infringement claim that cannot be resolved, Breneth may terminate and refund prepaid Fees for the unused portion.

**Why it matters:** There is no convenience termination right. If Gaimun wants to leave the Agreement for a business reason (e.g., the Ostrander integration makes BrewOps redundant, or Gaimun switches to a different platform), it must pay the full remaining term. The only refund scenarios are Breneth's breach, insolvency, or an unresolvable IP claim. Combined with the 60-month term and auto-renewal (Issue 4), this is a very sticky commitment.

**Recommended fix:** Negotiate a termination-for-convenience right after year two or year three, with a declining early-termination fee (e.g., 50% of remaining fees if terminated in year 3, 25% if terminated in year 4). Alternatively, tie a convenience exit to the Change of Control: if Ostrander decides post-closing to consolidate brewing operations and drop Gaimun as a separate entity, Gaimun should be able to exit without the full-term penalty.

**Confirm with client:** Does Ostrander's integration plan contemplate any scenario in which Gaimun's standalone brewing operations would be reduced or eliminated? If so, the Change of Control consent (Issue 1) should be conditioned on a corresponding exit right.

---

## Items I Could Not Resolve From the Documents Alone

| # | Question | Why it matters | What to confirm |
|---|---|---|---|
| A | Has Breneth informally agreed to the Change of Control? The Side Letter acknowledges the merger but grants no consent. | Determines whether Issue 1 is a live risk or already handled. | Ask client whether any verbal or email assurance was given. |
| B | What is Breneth's "list price" for a facility of comparable size? | Needed to evaluate Issue 8. | Request Breneth's current rate card. |
| C | What are Gaimun's specific TTB filing deadlines and the penalty exposure for late/inaccurate filings? | Calibrates the severity of Issues 5 and 6. | Ask Jess Okafor (Compliance Coordinator) for the 2027 calendar and applicable penalty provisions. |
| D | Is the Ostrander closing date confirmed, and will it fall after January 1, 2027? | Determines timing of the Change of Control relative to the subscription. | Ask client for the expected closing date. |
| E | What is the current state of Gaimun's data (spreadsheets from 2019 onward)? | Affects onboarding risk (Issue 7) and data-migration quality. | Ask Elena Ruiz whether the data is clean and in a consistent format. |

---

## Suggested Next Steps (Priority Order)

1. **Before Ostrander closing:** Secure written consent to the Change of Control (Issue 1). This is time-sensitive.
2. **Before next billing cycle (January 2027):** Resolve the governing law conflict (Issue 2) and the data-loss sole-remedy problem (Issue 3) via an amendment or revised Side Letter.
3. **Before onboarding completes (December 2026):** Address the onboarding-completion condition (Issue 7) and the TTB accuracy gap (Issue 5).
4. **Calendar the auto-renewal opt-out window** (Issue 4): set a reminder for no later than September 2031 (90 days before the first opt-out window opens in November 2031).
5. **Address remaining items** (Issues 6, 8–12) in a comprehensive amendment or at the first renewal negotiation.