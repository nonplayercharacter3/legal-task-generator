# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Breneth Systems / Gaimun Brewing – Software License Agreement: Issue Identification and Recommended Fixes

---

## Summary

I reviewed the Software License and Subscription Agreement (the "Agreement"), Schedule B (Service Level Schedule), the Side Letter, Order Form No. 001, and the onboarding email thread. I identified **fifteen issues**, ranging from a critical unaddressed change-of-control exposure to drafting conflicts and practical gaps. The three most urgent items are: (1) the pending Ostrander merger triggers a fee-acceleration clause that the Side Letter acknowledges but does not resolve; (2) the Side Letter silently moves governing law and forum from New York to Colorado; and (3) the Service Level Schedule makes service credits the exclusive remedy for data loss caused by a service failure, which likely conflicts with the main Agreement's uncapped data-security liability carve-out.

---

## Issue 1 – Change of Control: Fee Acceleration Without Consent

**Where:** Agreement §14.2; Side Letter, Recital B.

**What it says:** Section 14.2 provides that any Change of Control of Customer "shall be deemed an assignment" requiring Breneth's prior written consent. If it occurs without consent, Breneth may terminate and **all Fees for the remainder of the Subscription Term become immediately due and payable.** The Initial Subscription Term is 60 months at $186,000/year, so the acceleration exposure is up to **$930,000**.

Side Letter Recital B states that Breneth was told about the September 30, 2026 merger agreement with Ostrander Beverage Holdings LLC (closing expected Q1 2027). However, no operative section of the Side Letter grants consent, waives the acceleration, or modifies §14.2.

**Why it matters:** The merger is expected to close in Q1 2027—after the Subscription Start Date of January 1, 2027. At closing, Gaimun will be a wholly owned subsidiary of Ostrander, which is a Change of Control under §1.1(c)(i) ("Customer becomes a subsidiary of another entity"). Unless Breneth consents in writing before closing, Breneth can terminate and demand the full remaining term's fees.

**Recommended fix:** Add an operative section to the Side Letter (or a new side letter) that:
- Constitutes Breneth's prior written consent to the specific Change of Control described in Recital B;
- Confirms that the Change of Control will not trigger termination or fee acceleration under §14.2; and
- Clarifies whether the consent extends to future changes of control of Ostrander or is limited to this transaction.

**Note for client:** We need to confirm with Gaimun whether the Ostrander merger has closed or is still pending, and whether Ostrander itself might undergo a change of control in the near term.

---

## Issue 2 – Governing Law and Forum: Direct Conflict Between Agreement and Side Letter

**Where:** Agreement §16.1–16.2 (New York law; New York County courts); Side Letter §4.1–4.2 (Colorado law; Denver courts).

**What it says:** The main Agreement selects New York law and exclusive jurisdiction in New York County. The Side Letter selects Colorado law and exclusive jurisdiction in Denver. Under Agreement §1.4, the Side Letter has the **highest order of precedence**.

**Why it matters:** The Side Letter's clause covers "the Agreement as modified hereby," which is broad enough to argue that the entire relationship is now governed by Colorado law and must be litigated in Denver—Breneth's home forum. Gaimun is a Kingston, New York company. Losing home-court advantage on a $186,000/year, 5-year contract is a meaningful disadvantage, particularly for the pricing and expansion terms that live in the Side Letter.

Even if a court reads the Side Letter's forum clause as applying only to Side Letter-specific disputes, the ambiguity itself creates litigation risk and increases the cost of any enforcement action.

**Recommended fix:** Conform the Side Letter's governing law and forum to New York, matching the main Agreement. If Breneth resists, at minimum carve out the Side Letter's pricing provisions from the Colorado forum clause and confirm that the main Agreement's New York forum governs all other disputes.

---

## Issue 3 – Service Credits as "Sole and Exclusive Remedy" for Data Loss Conflicts with Uncapped Data-Security Liability

**Where:** Schedule B §5.4; Agreement §11.3(b).

**What it says:** Schedule B §5.4 states that Service Credits are Customer's "sole and exclusive remedy, and Breneth's sole liability, for any Service failure, including … loss or corruption of Customer Data arising from or in connection with any Service failure." The maximum monthly credit is 10% of the Monthly Fee (§5.3), which works out to roughly **$1,550 per month**.

Agreement §11.3(b) carves out from the general liability cap "Breneth's liability for breach of its obligations under Section 8 (Data Security) … including liability for any loss or corruption of Customer Data and the costs of restoring it."

**Why it matters:** If a platform outage (a "Service failure") causes data loss or corruption, §5.4 appears to cap Gaimun's recovery at ~$1,550, while §11.3(b) appears to leave data-security liability uncapped. These provisions are in direct tension. Because the Service Level Schedule ranks below the main Agreement in the order of precedence (§1.4), one could argue §11.3(b) controls. But the specific language in §5.4 ("including loss or corruption of Customer Data arising from or in connection with any Service failure") is hard to ignore, and Breneth will likely argue it is the more specific provision.

For a brewery whose Customer Data includes proprietary recipes and formulations (defined in §1.1(e)), a data loss event could be devastating, and a $1,550 cap is inadequate.

**Recommended fix:** Amend Schedule B §5.4 to expressly exclude from the "sole and exclusive remedy" language any loss or corruption of Customer Data resulting from a breach of Section 8 (Data Security) or Section 9 (Confidentiality). Alternatively, add a sentence: "Notwithstanding the foregoing, this Section 5.4 does not limit Customer's rights under Section 11.3(b) of the Agreement."

---

## Issue 4 – No Termination Right for Chronic Service Failure; Narrow Non-Renewal Window

**Where:** Schedule B §6.1; Agreement §3.2; Order Form §2.2.

**What it says:** Schedule B §6.1 requires a meeting and a remediation plan if availability drops below 98% in two consecutive months or three months in a rolling year. But it gives Gaimun **no right to terminate** if the problem persists. The only termination rights in the Agreement are for material breach (§13.1, with a 30-day cure period) or insolvency (§13.2).

Meanwhile, §3.2 auto-renews for successive 60-month terms, and the non-renewal notice window is only **15 days wide** (between 60 and 45 days before term end). Missing that window locks Gaimun in for another five years.

**Why it matters:** Gaimun could be stuck in a 5-year (or 10-year) term with a platform that chronically underperforms, with no contractual exit short of proving material breach and waiting out a 30-day cure period. The 15-day non-renewal window is a trap for a small business without a contract-management function.

**Recommended fix:**
- Add to Schedule B §6.1: if the chronic failure continues for an additional 60 days after the remediation plan is agreed, Customer may terminate the affected subscription without penalty and receive a pro-rata refund of prepaid Fees.
- Widen the non-renewal notice window in §3.2 to at least 90 days before term end (e.g., "no earlier than 120 days and no later than 90 days").

---

## Issue 5 – TTB Reporting Module: No Accuracy SLA; "Conform at Each Update" Is Insufficient

**Where:** Agreement §2.4; Schedule B §1.1(b), §4.3 (Severity 1 definition).

**What it says:** Section 2.4 obligates Breneth to maintain the TTB module so that report formats "conform to the TTB forms current as of the date of each update." This means if TTB revises a form and Breneth does not push an update for several months, the module may be non-conforming during that gap. There is no SLA metric for report accuracy.

A Severity 1 Incident (the most serious) requires that a core module be "unusable, with no workaround." If the TTB module is accessible but generates a report in the wrong format, it may only qualify as Severity 2 (target resolution: 2 Business Days), with a service credit of at most 2% of the Monthly Fee (~$310).

**Why it matters:** Gaimun's compliance coordinator (Jess Okafor) confirmed in the email thread that TTB filing deadlines are fixed and non-negotiable. A misformatted report discovered close to a deadline could create excise tax exposure for Gaimun. The current structure gives Breneth little incentive to fix format errors quickly.

**Recommended fix:**
- Amend §2.4 to require the module to conform to TTB forms as in effect on any given date, not just as of the last update, and to commit to a maximum lag (e.g., 30 days) after a TTB form change before the module is updated.
- Add a specific SLA: if the TTB module generates a report that does not conform to the then-current TTB form, it is a Severity 1 Incident regardless of whether a workaround exists.

---

## Issue 6 – Onboarding Delay: No Consequence if Platform Is Not Ready by Subscription Start Date

**Where:** Side Letter §2.2; Order Form §2.1; onboarding email thread (Message 3, proposed timeline).

**What it says:** The Side Letter says onboarding services are "to be completed before the Subscription Start Date" (January 1, 2027). The email thread shows a go-live readiness check targeted for December 29, 2026—two days before the start date. There is no provision addressing what happens if onboarding is incomplete on January 1.

**Why it matters:** The Subscription Term (and the 60-month clock, and the first $186,000 annual invoice) begins on January 1 regardless. If onboarding slips, Gaimun pays for a full year while the platform is not yet operational. There is no free-look period, no abatement, and no termination right for late onboarding.

**Recommended fix:** Add to the Side Letter: if onboarding is not completed by the Subscription Start Date, the Subscription Start Date (and the first invoicing date) shall be delayed day-for-day until onboarding is complete, up to a maximum of 60 days. If onboarding is not complete within 60 days of the original Subscription Start Date, Gaimun may cancel Order Form No. 001 without penalty.

**Note for client:** We should confirm with Gaimun whether the onboarding timeline in the email thread is still on track and whether any data-migration issues have arisen.

---

## Issue 7 – Suspension for Late Payment Excluded from Downtime Calculation

**Where:** Agreement §4.4; Schedule B §2.3(d).

**What it says:** If an undisputed amount is more than 30 days past due after written notice, Breneth may suspend access (§4.4). Schedule B §2.3(d) expressly excludes such suspension from the Downtime calculation, so it does not count against the 99.5% availability commitment and generates no service credit.

**Why it matters:** A billing error or a disputed-amount disagreement that goes slightly awry could result in a suspension that hits during production or filing season. Gaimun would have no SLA remedy for the resulting downtime.

**Recommended fix:** Amend §4.4 to require Breneth to give at least 15 days' written notice before suspending, and to limit suspension to the specific module or function related to the disputed amount (rather than the entire Platform). Alternatively, amend Schedule B §2.3(d) to provide that if a suspension later determines to have been in error (i.e., the amount was not actually owed), the suspension period counts as Downtime.

---

## Issue 8 – Data Deletion: Backup Exception Extends Retention Beyond 60 Days

**Where:** Agreement §7.4; §8.2(c).

**What it says:** Upon termination, Breneth must delete Customer Data within 60 days, "except for copies retained in routine backups, which shall remain subject to Section 8 until overwritten." Section 8.2(c) requires daily backups with a retention period of "not less than thirty (30) days."

**Why it matters:** In practice, this means Customer Data (including recipes and formulations) could persist in Breneth's backup systems for up to 90 days after termination (60-day deletion + 30-day backup retention), and potentially longer if backup cycles overlap. For a craft brewery whose recipes are a core competitive asset, extended retention with a third party is a real risk.

**Recommended fix:** Amend §7.4 to require that backup copies be deleted or irreversibly anonymized within 30 days after the initial 60-day deletion period (i.e., 90 days maximum from termination), and that Breneth certify completion in writing.

---

## Issue 9 – Annual Prepayment with Limited Refund Rights

**Where:** Order Form §3.1; Agreement §13.3(c); §4.1.

**What it says:** Fees are $186,000 per year, invoiced annually in advance. Section 13.3(c) provides a refund of prepaid Fees only if **Customer** terminates for cause under §13.1 or §13.2. There is no refund provision if the Agreement terminates for other reasons (e.g., Breneth's breach that Gaimun does not elect to treat as a termination trigger, or a mutual agreement to end early).

**Why it matters:** Gaimun is putting $186,000 at risk each year upfront. If the relationship sours and the parties want to part ways amicably mid-year, the contract does not clearly provide for a pro-rata refund. Section 4.1 states Fees are "non-cancellable and non-refundable" except as expressly provided, and the only express refund is in §13.3(c).

**Recommended fix:** Amend §13.3(c) to provide a pro-rata refund of prepaid Fees for the unused portion of the subscription year upon any termination, regardless of which Party triggers it or for what reason (other than Customer's uncured material breach).

---

## Issue 10 – 99.5% Availability Commitment Is Modest for a Production-Critical System

**Where:** Schedule B §2.1.

**What it says:** The Availability Commitment is 99.5% per calendar month, which permits approximately **3 hours and 37 minutes** of Downtime in a 30-day month without any service credit.

**Why it matters:** BrewOps handles batch tracking, inventory, TTB reporting, and distributor ordering. An unplanned 3.5-hour outage on a production day could halt brewing operations or delay distributor orders. The service credit for the first tier of shortfall (99.0–99.5%) is only 2% of the Monthly Fee (~$310), which is negligible against the operational cost of a downtime event.

**Recommended fix:** Negotiate a higher commitment (99.7% or 99.9%) or, at minimum, increase the first-tier service credit to 5% of the Monthly Fee. Also consider adding a "consecutive downtime" threshold: any single Downtime event exceeding 4 hours should automatically qualify as a Severity 1 Incident regardless of monthly availability percentage.

---

## Issue 11 – "Competing Product" Restriction Is Overbroad

**Where:** Agreement §2.3(d).

**What it says:** Customer shall not "use the Platform to build a competing product."

**Why it matters:** "Competing product" is not defined. Read broadly, this could restrict Gaimun from developing its own internal production tools, dashboards, or analytics that overlap with BrewOps functionality—especially relevant if Ostrander (post-merger) wants to build proprietary systems across its portfolio. Gaimun could argue it is not "using the Platform" to build the tool, but the line is blurry.

**Recommended fix:** Narrow §2.3(d) to prohibit using the Platform's source code, architecture, or proprietary algorithms to create a product offered commercially to third parties as a brewery-management platform. Add: "This restriction does not apply to Customer's development of internal business tools or systems for Customer's own use."

---

## Issue 12 – Expansion Pricing: "List Price" and "Comparable Size" Undefined

**Where:** Side Letter §3.2.

**What it says:** Additional facilities are offered at "a discount of fifteen percent (15%) from Breneth's then-current list price for a facility of comparable size."

**Why it matters:** Neither "list price" nor "comparable size" is defined in any document. If Gaimun (or Ostrander post-merger) adds a facility, Breneth could assert a high list price or characterize the new facility as larger than "comparable," undermining the 15% discount.

**Recommended fix:** Define "list price" as the price set forth in Breneth's then-current standard pricing schedule for the BrewOps Platform, or attach the current list price as an exhibit. Define "comparable size" by reference to a specific metric (e.g., annual barrel production capacity within ±25% of the Kingston facility).

---

## Issue 13 – Gap Period Between Effective Date and Subscription Start Date

**Where:** Agreement preamble (Effective Date: November 2, 2026); Order Form §2.1 (Subscription Start Date: January 1, 2027).

**What it says:** The Agreement is effective November 2, 2026, but the Subscription Term does not begin until January 1, 2027. During this ~2-month gap, the Agreement is in force (confidentiality, data security, and onboarding obligations apply), but the Platform subscription has not started.

**Why it matters:** It is unclear whether the Service Level Schedule applies during onboarding (it references the "Subscription Term" and "Monthly Fee," which do not yet exist). If Gaimun uploads data during onboarding and Breneth suffers a security incident in December 2026, §8.3 applies (the Agreement is in effect), but there is no SLA framework for response times or service credits. The warranty in §10.2 also applies only "during the Subscription Term."

**Recommended fix:** Add a sentence to the Side Letter or a new section confirming that (a) the data security obligations in §8 apply to Customer Data from the moment it is transmitted to Breneth (including during onboarding), and (b) the support response times in Schedule B §4.3 apply to any Incident arising from the onboarding environment, even though formal service credits do not accrue.

---

## Issue 14 – Aggregated Data: "Production Information" Not Defined

**Where:** Agreement §7.3; §1.1(e).

**What it says:** Breneth may generate de-identified, aggregated usage statistics provided they "do not identify Customer or disclose any recipe, formulation, pricing, distributor or production information of Customer." The term "Customer Data" in §1.1(e) explicitly includes "production volumes."

**Why it matters:** "Production information" in §7.3 is not a defined term. It likely encompasses "production volumes" from the Customer Data definition, but the mismatch in language creates an argument that Breneth could publish aggregate statistics revealing Gaimun's scale of production (e.g., "customers in the 50,000–100,000 barrel range increased output by 12%") without "disclosing production information" in a narrow sense. Post-merger, Ostrander may be sensitive about revealing portfolio-level production data.

**Recommended fix:** Replace "production information" in §7.3 with "Customer Data" (the defined term), so the restriction clearly covers all data categories listed in §1.1(e), including production volumes, batch records, and inventory records.

---

## Issue 15 – Security Incident Notification: 72 Hours From "Awareness" May Be Too Late for Regulatory Response

**Where:** Agreement §8.3.

**What it says:** Breneth must notify Gaimun "without undue delay, and in any event within seventy-two (72) hours, after becoming aware of" a Security Incident.

**Why it matters:** The 72-hour clock starts when Breneth becomes aware, not when the incident occurred. If Breneth discovers a breach that happened two weeks earlier, Gaimun gets notice up to 2 weeks + 72 hours after the actual event. If the breached data includes distributor or customer information subject to state data-breach notification laws (New York's SHIELD Act, for example), Gaimun's own notification clock may already be running or close to running.

**Recommended fix:** Shorten to 48 hours, and add: "Breneth shall include in its notice the date or approximate date the Security Incident occurred, the categories of Customer Data affected, and the number of records involved, to the extent known."

---

## Items Requiring Client Confirmation

| # | Question | Why it matters |
|---|----------|---------------|
| 1 | Has the Ostrander merger closed, and if so, when? | Determines whether the §14.2 exposure is live or still prospective. |
| 2 | Does Gaimun anticipate adding facilities or users in the near term (e.g., as part of Ostrander integration)? | Affects the importance of Issues 12 and the Side Letter expansion terms. |
| 3 | Is the onboarding timeline still on track for a January 1 go-live? | Affects Issue 6 urgency. |
| 4 | What is Gaimun's risk tolerance for the 99.5% availability level given production and filing deadlines? | Affects whether to push on Issue 10. |
| 5 | Does Gaimun have any existing data-breach notification obligations (e.g., under distributor agreements or state law) that would be triggered by a Security Incident? | Affects Issue 15 and the importance of the notification timeline. |

---

## Suggested Priority for Negotiation

1. **Before the Ostrander closing:** Resolve Issue 1 (change-of-control consent) and Issue 2 (governing law). These are binary—either fixed or not—and the closing date creates natural urgency.
2. **Before the Subscription Start Date (January 1, 2027):** Resolve Issues 3, 4, 5, and 6. These affect the operational framework Gaimun will be living under from day one.
3. **In a cleanup amendment (can be addressed in the same negotiation round):** Issues 7–15.

I am happy to draft proposed redlines for any of these once you've had a chance to review and prioritize.