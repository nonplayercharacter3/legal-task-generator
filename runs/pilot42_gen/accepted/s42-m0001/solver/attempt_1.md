# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Gaimun Brewing Company, LLC – Breneth Systems Software License: Issue Identification and Recommended Fixes

---

## Summary

I reviewed the Software License and Subscription Agreement (the "Agreement"), Schedule B (Service Level Schedule), the Side Letter, Order Form No. 001, and the onboarding email thread. I identify **ten issues** ranging from critical (requiring action before the Ostrander merger closes in Q1 2027) to lower-priority items worth negotiating or monitoring. The two most urgent are: (1) the Side Letter acknowledges Gaimun's pending Change of Control but does not grant the consent required by Agreement §14.2, exposing Gaimun to termination and fee acceleration; and (2) the Side Letter's Colorado governing-law and forum clause overrides the Agreement's New York provisions for the entire deal, likely in error.

---

## Issue 1 – Change of Control: Consent Not Granted Despite Pending Merger

**Where:** Agreement §14.2; Side Letter, Recital B.

**What the documents say:**

- Agreement §14.2 provides that any Change of Control of Customer "shall be deemed an assignment" requiring Breneth's prior written consent. If a Change of Control occurs without consent, Breneth may terminate and "all Fees for the remainder of the Subscription Term become immediately due and payable."
- Side Letter, Recital B states that Gaimun informed Breneth on September 30, 2026 of a merger agreement under which Gaimun will become a wholly owned subsidiary of Ostrander Beverage Holdings LLC, with closing expected in Q1 2027.
- The Side Letter addresses only pricing, onboarding, and expansion terms. It does not grant consent, waive §14.2, or carve out the Ostrander transaction.

**Why it matters to Gaimun:**

The Initial Subscription Term is 60 months starting January 1, 2027 (Order Form §2.2). If the Ostrander closing occurs in Q1 2027 without Breneth's written consent under §14.2, Breneth can terminate the Agreement and accelerate all remaining Fees. At $186,000 per year, that is roughly $774,000 for the remaining ~4.5 years. Even if Breneth does not terminate, the acceleration clause gives it significant leverage.

The fact that Breneth acknowledged the merger in Recital B but did not grant consent is either an oversight or a deliberate omission. Either way, Gaimun is exposed at closing.

**Recommended fix:**

Before the Ostrander closing, obtain a written consent from Breneth to the Change of Control, either by:
- Adding a provision to the Side Letter (or a new side letter) stating that Breneth consents to the Ostrander merger and that §14.2 shall not apply to it; or
- Executing a standalone consent letter referencing §14.2.

If Breneth resists, negotiate at minimum a provision that (a) the Ostrander merger does not trigger fee acceleration, and (b) Breneth's remedy for an unconsented Change of Control is termination with a pro-rata refund rather than acceleration.

**Confirmation needed with client:** What is the expected closing date for the Ostrander merger? Has any consent or waiver been discussed with Breneth outside the Side Letter?

---

## Issue 2 – Governing Law and Forum: Side Letter Overrides Agreement in Favor of Colorado

**Where:** Agreement §§16.1–16.2 (New York law; New York County forum); Side Letter §§4.1–4.2 (Colorado law; Denver forum); Agreement §1.4 (order of precedence).

**What the documents say:**

- Agreement §16.1 selects New York law. §16.2 selects exclusive jurisdiction in New York County.
- Side Letter §4.1 selects Colorado law for "this Side Letter and the Agreement as modified hereby." §4.2 selects exclusive jurisdiction in Denver for "any action arising out of or relating to this Side Letter or the Agreement as modified hereby."
- Agreement §1.4 establishes the order of precedence: Side Letter ranks first.

**Why it matters to Gaimun:**

Because the Side Letter has the highest priority and its governing-law clause expressly covers "the Agreement as modified hereby" (i.e., the entire Agreement), the Colorado law and Denver forum provisions almost certainly override the New York provisions. This means:

- Any dispute (including a data-breach claim, a service-level dispute, or a termination dispute) would be litigated in Denver under Colorado law.
- Gaimun, a New York company with its operations in Kingston, NY, would have to defend or pursue claims in a distant forum under unfamiliar law.
- Colorado and New York differ on several points relevant to this deal (e.g., enforceability of certain limitation-of-liability clauses, statutory interest rates, and the treatment of consequential damages waivers in adhesion contexts).

This appears to be a drafting error by Breneth's counsel (the Side Letter is about pricing, not dispute resolution), but as written it controls.

**Recommended fix:**

Delete Side Letter §§4.1 and 4.2 in their entirety, or replace them with a provision stating that the governing law and forum provisions of Agreement §16 apply to the Side Letter as well. If Breneth insists on Colorado law for the Side Letter alone, limit the scope to "disputes arising solely from the pricing terms in Sections 1 and 3 of this Side Letter" and confirm that all other disputes remain governed by Agreement §16.

**Confirmation needed with client:** None required from the client; this is a document-internal conflict. However, confirm whether Gaimun's deal team discussed governing law during Side Letter negotiations.

---

## Issue 3 – Service Credits as Exclusive Remedy for Data Loss

**Where:** Schedule B §5.4; Agreement §11.3(b); Agreement §1.4.

**What the documents say:**

- Schedule B §5.4 states that Service Credits are "Customer's sole and exclusive remedy, and Breneth's sole liability, for any Service failure, including any failure to meet the Availability Commitment or the response times in Section 4.3, **and including loss or corruption of Customer Data arising from or in connection with any Service failure**."
- Agreement §11.3(b) carves out from the liability cap "Breneth's liability for breach of its obligations under Section 8 (Data Security) or Section 9 (Confidentiality), including liability for any loss or corruption of Customer Data and the costs of restoring it."
- Under Agreement §1.4, the Service Level Schedule has priority over the body of the Agreement.

**Why it matters to Gaimun:**

Customer Data is defined (Agreement §1.1(e)) to include "recipes and formulations, batch and brew records, production volumes, inventory records, excise and tax reporting data, and distributor, customer and pricing information." Per the onboarding email (Message 2), Gaimun's recipe and batch history goes back to 2019 in spreadsheet form. This is core intellectual property and operational history.

If a Service failure (e.g., a platform outage, a bad update, a support error) causes loss or corruption of that data, Schedule B §5.4 limits Gaimun's remedy to a Service Credit of at most 10% of the Monthly Fee. The Monthly Fee is $186,000 ÷ 12 = $15,500. The maximum credit is therefore **$1,550** per month of failure. That is an absurdly inadequate remedy for the loss of a brewery's recipe database.

The conflict with §11.3(b) is resolved by the order of precedence: Schedule B wins. So the uncapped data-loss remedy in §11.3(b) is effectively gutted for any data loss "arising from or in connection with any Service failure."

**Recommended fix:**

Amend Schedule B §5.4 to carve out data loss from the exclusive-remedy provision. Suggested language: "Service Credits are Customer's sole and exclusive remedy for failure to meet the Availability Commitment or the response times in Section 4.3. This Section 5.4 shall not limit Customer's rights under Section 11.3(b) of the Agreement or any remedy for loss or corruption of Customer Data."

Alternatively, if Breneth resists a full carve-out, negotiate a higher cap specific to data loss (e.g., 3× annual Fees) and require Breneth to maintain off-site backups with a defined restoration SLA.

**Confirmation needed with client:** What is the approximate business value of Gaimun's recipe and formulation data? Are there any recipes that exist only in the Platform (i.e., not also in spreadsheets or other systems)? This helps frame the negotiating position.

---

## Issue 4 – Auto-Renewal for 60-Month Terms with a 15-Day Notice Window

**Where:** Agreement §3.2; Order Form §2.2.

**What the documents say:**

- The Initial Subscription Term is 60 months (Order Form §2.2).
- Upon expiry, the subscription "shall automatically renew for successive renewal periods, each equal in length to the Initial Subscription Term" (Agreement §3.2). So each Renewal Term is also 60 months.
- Non-renewal notice must be delivered "no earlier than 60 days and no later than 45 days before the end of the then-current Initial Subscription Term or Renewal Term." A notice outside that 15-day window "shall not be effective."

**Why it matters to Gaimun:**

- If Gaimun misses the 15-day window, it is locked in for another five years.
- The window is unreasonably narrow for a small brewery. A single scheduling oversight, a key person on leave, or a mail delay could trigger an unintended five-year commitment.
- Combined with the Change of Control issue (Issue 1), Gaimun may be entering a five-year term as a subsidiary of Ostrander without having negotiated the term with full knowledge of its post-merger operations.

**Recommended fix:**

- Extend the non-renewal notice window to at least 90 days before term end (i.e., notice may be given any time between 120 and 90 days before expiry).
- Alternatively, add a requirement that Breneth send a renewal reminder notice at least 120 days before the end of the then-current term.
- Consider shortening the Renewal Term to 12 months (rather than matching the 60-month Initial Term) to reduce lock-in.

**Confirmation needed with client:** Does Gaimun (or Ostrander post-merger) intend to use BrewOps long-term, or is there a possibility of migrating to a different platform? This affects how aggressively to negotiate the renewal terms.

---

## Issue 5 – TTB Module: No Accuracy SLA and Ambiguous Update Obligation

**Where:** Agreement §2.4; Agreement §5.3; Schedule B §1.1(b) (definition of "Available"); Schedule B §4.3 (Severity 1 includes TTB module unavailability).

**What the documents say:**

- Agreement §2.4: "Breneth shall maintain the reporting module so that its report formats conform to the TTB forms current as of the date of each update."
- Schedule B defines "Available" as the ability to use core functions "in material conformity with the Documentation." A TTB module that generates a report with an incorrect tax calculation or a mislabeled field is technically "Available" – it is up, users can log in, and it produces output.
- There is no SLA metric for report accuracy. No Service Credit applies if the TTB module generates a wrong number.
- The §2.4 obligation is tied to "the date of each update," which could be read to mean Breneth only has to conform to TTB forms when it pushes a platform update, not when TTB unilaterally changes a form.

**Why it matters to Gaimun:**

TTB compliance is non-discretionary. A wrong excise return can result in penalties, interest, and in severe cases, loss of the brewery's federal permit. Gaimun's compliance coordinator (Jess Okafor) specifically asked in the onboarding thread (Message 4) for test reports from imported 2026 data to validate accuracy before the first live filing. Breneth agreed (Message 5), but that is a one-time onboarding courtesy, not an ongoing contractual obligation.

If TTB revises a form or a calculation methodology and Breneth is slow to update the module, Gaimun could file a non-conforming return. The Agreement puts the responsibility for "reviewing, approving and submitting" on Gaimun (§2.4), but if the module's output is systematically wrong due to a stale format, Gaimun is caught between its TTB obligations and Breneth's update timeline.

**Recommended fix:**

- Amend §2.4 to state that Breneth shall update the TTB module to conform to any change in TTB forms or regulations within a specified period (e.g., 30 days) after the change takes effect, regardless of whether Breneth is otherwise pushing a platform update.
- Add a specific SLA: if the TTB module generates a report that does not conform to the then-current TTB form, that is a Severity 1 Incident (not just a general "Incident"), triggering the 1-hour response and 8-hour resolution targets.
- Clarify that Gaimun's obligation to "review and approve" (§2.4) does not extend to validating the module's conformance to TTB format changes – that is Breneth's responsibility under its update obligation.

**Confirmation needed with client:** What TTB filing deadlines apply to Gaimun (monthly Brewer's Report of Operations? quarterly excise returns? annual)? Are there any known TTB form changes on the horizon for 2027?

---

## Issue 6 – Chronic Failure: No Termination Right

**Where:** Schedule B §6.1.

**What the documents say:**

If Availability falls below 98.0% in two consecutive months or three months in a rolling twelve-month period, the Parties' representatives meet, Breneth presents a remediation plan, and "Breneth shall implement the agreed remediation plan." That is the entire provision. There is no consequence if the remediation plan fails, no second meeting, no termination right, and no enhanced Service Credits.

**Why it matters to Gaimun:**

A brewery that cannot access its production, inventory, or compliance tools for extended periods faces real operational and regulatory risk. If Breneth chronically underperforms and its remediation plans are ineffective, Gaimun has no contractual exit short of a material-breach termination under Agreement §13.1 (which requires a 30-day cure period and a finding of "material breach" – a high bar for persistent sub-98% availability that Breneth could argue is not "material" if the platform is technically up most of the time).

**Recommended fix:**

Add to Schedule B §6.1: "If, after implementation of the remediation plan, Availability again falls below 98.0% in any two consecutive calendar months or three calendar months within a rolling twelve-month period, Customer may terminate this Agreement by written notice, and Breneth shall refund any prepaid Fees for the period after the effective date of termination."

---

## Issue 7 – Data Return: 30-Day Request Window and Indefinite Backup Retention

**Where:** Agreement §7.4.

**What the documents say:**

Upon expiry or termination, Gaimun must request data export "within thirty (30) days thereafter." Breneth then has 60 days to delete, "except for copies retained in routine backups, which shall remain subject to Section 8 until overwritten." No specific timeline is given for backup overwriting.

**Why it matters to Gaimun:**

- The 30-day window is short. If the Agreement terminates unexpectedly (e.g., Breneth invokes §14.2 after the Ostrander closing), Gaimun's team may be in crisis mode and could miss the deadline, forfeiting the contractual right to export.
- "Until overwritten" is indefinite. If Breneth's backup rotation is quarterly, Gaimun's data (including recipes) could persist in Breneth's systems for months or longer after the 60-day deletion period.

**Recommended fix:**

- Extend the request window to 90 days.
- Add a specific backup-overwrite deadline (e.g., "no later than ninety (90) days after the deletion deadline in this Section 7.4").
- Add a requirement that Breneth certify in writing upon completion of deletion (including backups).

**Confirmation needed with client:** Does Gaimun maintain independent backups of its recipe and production data outside the Platform? If yes, the risk is lower. If the Platform is the system of record, this is more urgent.

---

## Issue 8 – Force Majeure Excludes TTB-Deadline Downtime from SLA

**Where:** Agreement §15.2; Schedule B §2.3(e); Schedule B §3.4.

**What the documents say:**

- Force majeure events are Excluded Downtime (Schedule B §2.3(e)), so they do not count against the 99.5% Availability Commitment and do not trigger Service Credits.
- Schedule B §3.4 requires Breneth to use "commercially reasonable efforts" to avoid scheduling maintenance in the last 3 Business Days before TTB deadlines, but this applies only to Scheduled Maintenance, not to force majeure events or unplanned outages.

**Why it matters to Gaimun:**

If a force majeure event (e.g., a regional internet outage, a natural disaster affecting Breneth's data center) causes downtime during a TTB filing window, Gaimun has no SLA remedy and may miss a regulatory deadline. The "commercially reasonable efforts" standard in §3.4 is aspirational and does not create a liability hook.

**Recommended fix:**

This is harder to fix contractually because force majeure is a standard allocation of risk. However, consider:
- Requiring Breneth to maintain a geographically redundant failover so that a single-region force majeure event does not take down the Platform.
- Adding a provision that if a force majeure event causes the Platform to be unavailable on a TTB filing deadline, Breneth shall provide emergency manual export of the relevant data within a specified timeframe (e.g., 4 hours) to allow Gaimun to file manually.

**Confirmation needed with client:** What are Gaimun's actual TTB filing deadlines and the consequences of a late filing? (Penalties? Permit risk?) This determines how much to push on this point.

---

## Issue 9 – Expansion Pricing: "Then-Current List Price" Is Undefined

**Where:** Side Letter §3.2.

**What the documents say:**

If Gaimun adds a facility post-merger, Breneth shall offer the Platform "at a discount of fifteen percent (15%) from Breneth's then-current list price for a facility of comparable size."

**Why it matters to Gaimun:**

- "Then-current list price" is not defined anywhere in the Agreement Documents. Breneth could argue its list price has increased by the time Gaimun needs to add a facility, and the 15% discount would be off a higher base.
- "Comparable size" is vague. What metrics determine comparability (tank capacity, production volume, number of users)?
- The Side Letter's price hold (§1.1) covers only the modules and user count in Order Form No. 001. It does not lock in the list price for future expansion.

**Recommended fix:**

- Define "list price" by reference to Breneth's published price sheet as of the Effective Date, or cap the increase at a specified percentage per year (e.g., CPI or 5%).
- Define "comparable size" with objective criteria (e.g., "a facility with production capacity within ±25% of Gaimun's Kingston facility").
- Alternatively, lock in a fixed per-facility price for the Initial Subscription Term.

**Confirmation needed with client:** Post-merger, does Ostrander plan to integrate Gaimun with other breweries onto the Platform? If so, how many additional facilities are anticipated and on what timeline?

---

## Issue 10 – Support Hours May Not Align with Brewery Operations

**Where:** Schedule B §1.1(c) (Business Hours definition); Schedule B §4.1; Onboarding email, Message 5.

**What the documents say:**

- Business Hours are 7:00 a.m. to 7:00 p.m. ET, Monday through Friday, excluding federal holidays.
- Only Severity 1 Incidents receive 24/7 support.
- A Severity 2 Incident (material degradation of a core module, workaround available) reported on a Saturday gets an initial response within "4 Business Hours" – i.e., not before Monday 7:00 a.m. at the earliest.

**Why it matters to Gaimun:**

Craft breweries frequently run production on weekends and may have packaging or distribution activities outside standard business hours. If a Severity 2 issue (e.g., the inventory module shows incorrect tank levels, but the system is technically "up") arises on a Saturday during a brew day, Gaimun has no contractual right to a response until Monday. The workaround requirement for Severity 2 classification means Breneth could argue the issue is "not severe enough" for 24/7 coverage.

**Recommended fix:**

- Expand 24/7 support to include Severity 2 Incidents affecting the Batch and Recipe Tracking or TTB Excise Reporting modules (the two most operationally critical).
- Alternatively, extend Business Hours to include Saturday 7:00 a.m. to 3:00 p.m. ET.
- At minimum, clarify in the Severity definitions that any issue preventing Gaimun from recording a brew batch or generating a TTB report is Severity 1, regardless of whether a "workaround" exists.

**Confirmation needed with client:** Does Gaimun brew or package on weekends? Are there specific days or times when Platform availability is operationally critical beyond standard business hours?

---

## Items I Could Not Resolve From the Documents Alone

| Item | What's unclear | What to confirm |
|---|---|---|
| Ostrander closing date | Recital B says "expected in the first quarter of 2027" but gives no specific date. The Subscription Start Date is January 1, 2027. If closing occurs before January 1, the Change of Control happens before the term even begins. | Exact expected closing date; whether the merger agreement has any conditions that could delay or cancel closing. |
| Breneth's list price | Side Letter §3.2 references "then-current list price" but no price list is attached or referenced. | Request Breneth's current list price for a facility of comparable size to Gaimun's Kingston operation. |
| Backup overwrite cycle | Agreement §7.4 says backups remain "until overwritten" but no retention schedule is specified. | Ask Breneth what its backup rotation cycle is (daily, weekly, monthly). |
| Whether the Side Letter was fully negotiated | The governing-law clause (Issue 2) looks like a template carry-over. It's possible Gaimun's deal team did not flag it. | Confirm with the client who drafted the Side Letter and whether the Colorado clause was discussed. |

---

## Priority Summary

| Priority | Issue | Action Needed By |
|---|---|---|
| **Critical** | 1 – Change of Control consent | Before Ostrander closing (Q1 2027) |
| **Critical** | 2 – Governing law / forum conflict | Before closing; amend Side Letter |
| **High** | 3 – Data loss exclusive remedy | Before Subscription Start Date (Jan 1, 2027) |
| **High** | 4 – Auto-renewal / 60-month lock-in | Before Subscription Start Date |
| **Medium** | 5 – TTB module accuracy / update obligation | Before first live TTB filing in 2027 |
| **Medium** | 6 – Chronic failure: no termination right | Next amendment cycle |
| **Medium** | 7 – Data return 30-day window / backup retention | Next amendment cycle |
| **Lower** | 8 – Force majeure and TTB deadlines | Next amendment cycle |
| **Lower** | 9 – Expansion pricing ambiguity | Before any facility addition |
| **Lower** | 10 – Support hours vs. brewery operations | Before Subscription Start Date |

---

*End of memo.*