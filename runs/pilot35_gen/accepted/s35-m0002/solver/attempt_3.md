# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Proudert Technical Fabrics, Inc. – Vopein Systems LLC Software License: Issue Identification and Recommended Actions

---

## Executive Summary

I have reviewed the five documents in the matter folder. The contract set contains several provisions that are materially unfavorable to Proudert, at least one direct inter-document conflict, and a significant gap (no executed Schedule B). The most urgent issues are (1) the dramatically expanded "Authorized User" definition in Amendment No. 1, which inflates both the core license tier and the new module fee; (2) the worldwide, post-term exclusive-use covenant in the Side Letter; and (3) the absence of an executed Schedule B despite the SLA's incorporation of it by reference. Details and recommended fixes follow.

---

## Issue 1: No Executed Schedule B in the File

**Where:** SLA § 8.2 (incorporates Schedule B by reference); the only Schedule B document in the folder is a Vopein draft dated February 20, 2026, marked "Not for execution" and "Subject to review by Proudert's information technology and legal teams."

**Why it matters:** Section 8.2 obligates Vopein to "comply with the data security requirements set out in Schedule B." If no executed Schedule B exists, Proudert has no enforceable data-security requirements beyond the general language in SLA §§ 8.1–8.4 and 9. The draft contains meaningful protections that Proudert would lose without an executed schedule: US-only data storage (§ 6.4), subcontractor consent (§ 7.1), remote-access logging (§ 5.2), multi-factor authentication for remote access (§ 4.2), and verification rights including annual security questionnaires and SOC 2 / ISO 27001 report delivery (§ 10). Given that the Vision Inspection Module (Amendment No. 1) involves machine-learning defect detection that may process images in the cloud, data-security terms are critical.

**Recommended fix:** Confirm whether an executed Schedule B was signed. If not, negotiate and execute one promptly, using the Vopein draft as a starting point but insisting on the US-only storage, subcontractor consent, and verification provisions. If Vopein resists, at minimum add a data-security addendum to the SLA.

**Open item:** I cannot determine from the documents alone whether an executed Schedule B exists outside this folder. **Need:** Confirmation from the client whether Schedule B was ever signed, and if so, a copy.

---

## Issue 2: Expanded "Authorized User" Definition (Amendment No. 1)

**Where:** Amendment No. 1, § 1.1 (amends and restates SLA § 1.2 in its entirety).

**Why it matters:** The original definition limited "Authorized User" to a "Licensee employee at the Licensed Site issued individual LoomSight login credentials." The restated definition now includes three categories:

- (a) Licensee employees with individual login credentials (unchanged);
- (b) "each contractor, consultant or other individual engaged by or on behalf of Licensee who has system access to the Software, **whether through individual login credentials, shared credentials or an interface**"; and
- (c) "each networked inspection camera or sensor station at the Licensed Site that captures, transmits or receives data through the Software."

This has two compounding financial effects:

1. **Core license tier escalation (SLA § 5.1).** Tiers are based on Authorized User count. If Proudert deploys, for example, 40 inspection cameras and has 10 contractors with system access, those 50 entities are added to the employee count. A plant with 70 employees plus 50 cameras/contractors = 120 Authorized Users, pushing Proudert from the Base Tier ($186,000) into Tier 2 ($238,000) — a $52,000 annual increase (before the 12% Side Letter discount).

2. **Vision Inspection Module Fee (Amendment § 2.2).** The Module Fee is $145 per Authorized User per month. At 120 Authorized Users, that is $17,400/month or $208,800/year — nearly as much as the entire core license fee. Even at 75 users, the module fee is $131,250/year.

Additionally, the **User True-Up (SLA § 5.4)** reports the "highest number of Authorized Users at any time during the preceding twelve months." A single camera temporarily connected for testing could spike the count and trigger a true-up invoice.

There is also a **measurement problem.** SLA § 6.2 states the usage report "shows the number of active login credentials." But cameras and contractors accessing via "shared credentials or an interface" (Amendment § 1.1(b)) may not generate individual login events. Vopein could argue the true count is higher than what the report shows, creating audit and dispute risk under SLA § 6.3.

**Recommended fix:**

- Negotiate a carve-out so that cameras/sensor stations are excluded from the core-license tier count (they should count only toward the Module Fee, which is already per-device).
- Alternatively, cap the number of cameras/sensors included in the tier calculation or convert them to a flat per-site fee.
- Clarify in the Amendment that the usage report in § 6.2 will be updated to separately identify (i) employee logins, (ii) contractor/interface access, and (iii) camera/sensor connections, so the true-up in § 5.4 is transparent and not subject to dispute.
- Confirm with the client the actual or planned number of cameras and contractors to model the financial exposure.

**Open item:** I cannot determine from the documents how many cameras Proudert has deployed or plans to deploy. **Need:** Client to provide the current and planned camera/sensor count and the number of third-party contractors with system access.

---

## Issue 3: Worldwide, Post-Term Exclusive-Use Covenant (Side Letter)

**Where:** Side Letter, § 3.1 (exclusive use) and § 3.2 (scope of "competing" software).

**Why it matters:** The covenant prohibits Proudert and its Affiliates from licensing, developing, or using any competing MES or quality-inspection software at **any facility owned or operated by Licensee or any Affiliate, anywhere in the world**, during the Term **and for 24 months after expiration or termination**. The scope of "competing" software (§ 3.2) is defined functionally and broadly: any software providing "production order management, machine or loom scheduling, work-in-process tracking, defect logging, product grading, statistical process control or automated inspection functions that are substantially similar."

This is a non-compete that is wildly disproportionate to the licensed relationship, which covers a single plant in Greenville, SC. It would prevent Proudert from:

- Deploying a different MES at any other current or future facility;
- Developing in-house scheduling or quality tools;
- Using a competitor's inspection software at a plant acquired by an Affiliate;
- Even evaluating or piloting alternative software (the covenant says "license, develop or use").

The 24-month tail means the restriction outlasts the relationship by two years. If Proudert terminates for cause under SLA § 13.3 because of Vopein's breach, it is still locked out of competing software for two years.

**Recommended fix:**

- Narrow the geographic scope to the Licensed Site only (or to facilities where the Software is actually deployed).
- Eliminate or shorten the post-term tail (e.g., 6 months, or zero if termination is for Vopein's cause).
- Add a carve-out for software used at facilities not running the Software.
- Clarify that "develop" does not prohibit internal R&D that is not deployed commercially or at a competing facility.
- If Vopein will not move, consider whether the 12% discount (worth ~$22,320/year on the Base Tier) is adequate consideration for a worldwide non-compete with a 24-month tail. It almost certainly is not.

**Open item:** I cannot determine from the documents whether Proudert operates or plans to operate other facilities, or whether any Affiliate operates facilities. **Need:** Client to confirm its current and planned facility footprint and whether the covenant impairs any business plans.

---

## Issue 4: Governing Law and Forum Conflict (SOW 1 vs. SLA)

**Where:** SOW 1, § 10.1–10.2 (Pennsylvania law; Allegheny County, PA forum) vs. SLA §§ 15.2–15.3 (Delaware law; Wilmington, DE forum).

**Why it matters:** Under the order of precedence in SLA § 15.6, SOWs rank above the SLA. Therefore, for disputes arising out of the implementation services, Pennsylvania law and the Allegheny County forum govern. For all other disputes (license, support, data, indemnification), Delaware law and the Wilmington forum govern. This creates:

- **Split jurisdiction risk.** A single implementation failure that causes a data breach or production loss could generate claims that implicate both the SOW (services) and the SLA (license, data security, indemnification), potentially requiring litigation in two forums or at minimum a threshold fight over which court has jurisdiction.
- **Inconsistent substantive law.** Pennsylvania and Delaware may differ on issues like the enforceability of the consequential-damages waiver, the standard for material breach, or the interpretation of "reasonable efforts."
- **Increased cost.** Proudert (a Delaware corporation operating in South Carolina) now has potential exposure in two out-of-state forums.

**Recommended fix:** Amend SOW 1 § 10 to conform to SLA §§ 15.2–15.3 (Delaware law, Wilmington forum), or alternatively move both to South Carolina (Proudert's operational home) if Vopein will agree. At minimum, add a provision that disputes implicating both the SOW and the SLA shall be resolved in a single forum.

---

## Issue 5: Auto-Renewal at "List Fees" with a Narrow Non-Renewal Window (SLA § 13.2)

**Where:** SLA § 13.2.

**Why it matters:** At the end of the three-year Initial Term (March 2, 2029), the Agreement automatically renews for successive three-year terms "at Licensor's then-current list fees." The non-renewal notice window is **180 to 210 days** before the end of the then-current term. A notice given on day 179 or day 211 is "void and of no effect."

Two problems:

1. **Uncontrolled price increase.** "Then-current list fees" means Vopein can raise its list price by any amount at renewal. The Side Letter 12% discount applies (Side Letter § 2.4 says it applies "during the Term," and "Term" includes Renewal Terms per SLA § 13.2), but the base on which the discount is calculated is whatever Vopein's list price happens to be. There is no cap on the increase.

2. **Extremely narrow notice window.** The 30-day window (210 to 180 days before term end) is easy to miss. For the Initial Term ending March 2, 2029, Proudert must give non-renewal notice between September 1, 2028 and October 1, 2028. If the responsible person is on leave or the notice is drafted on September 30 and delivered by courier on October 2, the notice is void and Proudert is locked in for another three years.

**Recommended fix:**

- Add a renewal price cap (e.g., no increase greater than CPI or 5% per renewal).
- Widen the non-renewal notice window (e.g., 120 to 270 days) or, better, make the notice effective if given at any time more than 120 days before term end (eliminating the "too early" problem).
- Add a requirement that Vopein send a renewal reminder notice at least 270 days before term end.
- Calendar the notice deadline immediately: **September 1 – October 1, 2028** for the Initial Term.

---

## Issue 6: Deemed Acceptance of Go-Live (SOW 1, § 5.3)

**Where:** SOW 1, § 5.3 (Deemed Acceptance).

**Why it matters:** The provision states: "Using the Software in production for live production orders is deemed acceptance of Milestone M4." Milestone M4 is "Training completed and Go-Live" and represents 25% of the Implementation Fee ($53,625). More critically, acceptance of M4 likely:

- Triggers the start of the 12-month software warranty period (SOW 1, § 11.2 confirms the warranty begins on Go-Live);
- Limits Proudert's ability to later claim that the implementation was deficient, because acceptance is deemed to have occurred the moment production use begins;
- Is irreversible — there is no cure period or right to reject after deemed acceptance.

In a manufacturing environment, the pressure to go live (to avoid production downtime during a planned cutover window) may mean Proudert starts using the Software before it is fully satisfied. The moment it does, M4 is accepted.

The same section also deems any deliverable accepted if Proudert fails to respond within 5 business days after Vopein's written notice. Combined with the 10-business-day review period in § 5.1, Proudert has very little time to identify and communicate issues.

**Recommended fix:**

- Delete or narrow the production-use deemed acceptance for M4. Replace with: M4 is accepted only upon written sign-off by Licensee's Project Manager after the Hypercare Period close-out report is delivered.
- Extend the review periods (e.g., 15 business days for deliverables, 10 business days after notice for deemed acceptance).
- Add a provision that deemed acceptance does not waive Proudert's rights under the warranty (SLA § 10.1) or for latent defects not discoverable during UAT.

---

## Issue 7: Consequential Damages Waiver Includes "Loss of Production" (SLA § 12.2)

**Where:** SLA § 12.2 (Exclusion of Consequential Damages), read with § 12.1 (Cap) and § 12.3 (Exceptions).

**Why it matters:** Section 12.2 expressly excludes "LOSS OF PRODUCTION" from recoverable damages. For a weaving plant running conveyor belting, geotextiles, and filtration media, a software outage that stops the looms is the single most likely and most costly failure scenario. The liability cap in § 12.1 is limited to fees paid in the prior 12 months (approximately $163,680–$208,800 depending on tier and module fees). The exceptions in § 12.3 do not help Proudert: they carve out only (a) Licensee's own indemnification obligations, (b) Licensee's payment of fees, and (c) fraud or willful misconduct.

So if Vopein's software fails, stops production for a week, and Proudert loses $500,000 in output, Proudert's maximum recovery is roughly $164,000–$209,000 (the fee cap), and it cannot recover the lost production at all.

**Recommended fix:**

- Carve "loss of production directly caused by Software failure or Licensor's breach of Support Services obligations" out of the consequential damages waiver, subject to a super-cap (e.g., 2x or 3x the annual fees).
- Alternatively, add service credits for Severity 1 outages exceeding the 2-hour response time (e.g., 5% of monthly fees per hour of delay).
- At minimum, ensure the insurance requirement in SLA § 14.1 (technology E&O / cyber, $5M per claim) is backed by a provision requiring Vopein to name Proudert as an additional insured or to provide a direct right of recovery under the policy.

---

## Issue 8: No Service Credits or Remedies for Missed Support SLAs (SLA § 4)

**Where:** SLA § 4.2 (Severity Levels and Response Times).

**Why it matters:** The Agreement specifies response times (2 hours for Severity 1, 8 business hours for Severity 2, 2 business days for Severity 3) but provides no consequence if Vopein misses them. There are no service credits, no termination right for chronic failure to meet response times, and no escalation mechanism beyond the general material-breach provision in § 13.3 (which requires a 30-day cure period).

For a production environment, a missed Severity 1 response means the plant is down with no contractual lever to compel faster action.

**Recommended fix:**

- Add a service-credit schedule: e.g., if Vopein misses the Severity 1 response time, Proudert receives a credit of 5% of the monthly equivalent of the annual core license fee for each hour of delay, up to a maximum of 50% of the monthly fee.
- Add a termination right if Vopein misses Severity 1 response times on more than three occasions in any 90-day period.
- Add an escalation path: if Vopein's Project Manager or support team does not respond within the stated time, the issue escalates automatically to Vopein's CTO or VP of Engineering.

---

## Issue 9: Feedback Provision (SLA § 7.4)

**Where:** SLA § 7.4.

**Why it matters:** "Licensor may use any suggestions or feedback that Licensee provides about the Software, without obligation to Licensee, provided that it does not disclose Licensee's Confidential Information." In a manufacturing context, Proudert will inevitably suggest configuration changes, process workflows, defect codes, and quality thresholds that reflect its proprietary production methods. While the "Confidential Information" limitation provides some protection, the line between "feedback about the Software" and "proprietary process information" is blurry. Vopein could argue that a suggestion like "add a defect code for crosshatch pattern at 300 meters" is software feedback, not Confidential Information, and use it for other textile customers.

**Recommended fix:**

- Narrow § 7.4 to feedback that does not incorporate or reflect Licensee's production processes, product specifications, or quality standards.
- Add: "Licensor shall not use any feedback to develop features specifically targeted at Licensee's competitors without Licensee's prior written consent."
- Alternatively, require that all feedback be submitted in writing and marked, with a presumption that oral feedback in the context of implementation services is Confidential Information.

---

## Issue 10: Transition Assistance Is Limited and Uncapped in Cost (SLA § 13.6)

**Where:** SLA § 13.6, read with § 8.4.

**Why it matters:** If the relationship ends (whether by expiration, non-renewal, or termination), Proudert is entitled to only 90 days of transition assistance, at Vopein's "then-current professional services rates" with no cap. For an MES system deeply integrated with loom controllers and an ERP (SOW 1, § 2.4), 90 days may be insufficient to extract data, reconfigure integrations, and stand up a replacement system. The data return obligation in § 8.4 requires Vopein to "cooperate in exporting Licensee Data in a standard, machine-readable format" but does not specify a timeline, a format standard, or a fee cap.

**Recommended fix:**

- Extend transition assistance to 180 days.
- Cap transition-assistance rates at the rates in effect on the date of the termination notice (or at SOW 1 § 8.4 hourly rates, whichever is lower).
- Specify in § 8.4 that data export shall be completed within 30 days of the termination effective date, in CSV, JSON, or a format mutually agreed, at no additional charge beyond a reasonable administrative fee.
- Add an obligation for Vopein to provide integration documentation (API specs, interface mappings) as part of transition assistance.

---

## Issue 11: Side Letter Is at the Bottom of the Precedence Order (SLA § 15.6)

**Where:** SLA § 15.6 (Order of Precedence): "Amendments, then Statements of Work, then the Software License Agreement, then side letters."

**Why it matters:** The Side Letter is the lowest-priority document. If any term in the Side Letter conflicts with the SLA, the SLA controls. While I have not identified a direct conflict at this time, the structure means that:

- The 12% discount could be overridden if the SLA is later amended in a way that changes the fee structure.
- The exclusive-use covenant (which is in the Side Letter) could be argued to be subordinate to any SLA provision that implicitly permits multi-vendor strategies.
- In any interpretive dispute, the Side Letter gets the least weight.

**Recommended fix:**

- Amend SLA § 15.6 to elevate the Side Letter above the SLA (at least for pricing and commercial terms), or incorporate the Side Letter's key terms (discount, exclusive use) directly into the SLA as a schedule.
- Alternatively, add a sentence to the Side Letter: "In the event of a conflict between this Side Letter and the Agreement, this Side Letter shall control with respect to pricing, discounts, and the commitments in Section 3."

---

## Issue 12: SOW 1 Schedule Uses "Reasonable Efforts" with No Delay Remedy (SOW 1, § 4.1)

**Where:** SOW 1, § 4.1.

**Why it matters:** The target schedule (Go-Live by October 5, 2026) is subject only to "reasonable efforts." There is no liquidated damage for delay, no termination right if Go-Live is pushed beyond a certain date, and no service credit. The only mechanism is the delay-notice provision in § 4.2, which extends dates if the delay is caused by Licensee. If Vopein causes the delay, Proudert has no remedy short of proving material breach (a high bar given the "reasonable efforts" standard).

For a manufacturing plant that has planned production around a go-live date, an unremedied delay has real operational cost (extended use of legacy systems, training schedule disruption, potential quality gaps).

**Recommended fix:**

- Add a longstop date: if Go-Live has not occurred by [date, e.g., December 31, 2026] due to Licensor's failure to perform, Licensee may terminate the SOW and receive a refund of fees paid for unaccepted milestones.
- Add liquidated damages for delay beyond the longstop date (e.g., $5,000 per week of delay, capped at 10% of the Implementation Fee).
- Clarify that "reasonable efforts" includes Vopein's obligation to staff the project with the minimum team in § 6.2 throughout the schedule.

---

## Issue 13: Module Fee Invoicing Relies on a Usage Report That May Not Capture All Authorized Users (Amendment § 2.3; SLA § 6.2)

**Where:** Amendment No. 1, § 2.3 (invoicing based on "the usage report described in Section 6.2"); SLA § 6.2 (usage report "shows the number of active login credentials").

**Why it matters:** The Module Fee is invoiced quarterly based on the highest number of Authorized Users "as shown by the usage report." But the usage report tracks "active login credentials." Under the expanded definition (Amendment § 1.1), Authorized Users include cameras and sensor stations that "capture, transmits or receive data through the Software" — these devices likely do not have "login credentials" in the traditional sense. Similarly, contractors accessing "through an interface" may not generate login events.

This creates two risks:

1. **Underbilling dispute.** Vopein could later argue that the usage report understates the true number of Authorized Users (because cameras don't "log in") and bill the difference retroactively, potentially with audit-cost recovery under SLA § 6.3 if the shortfall exceeds 10%.
2. **Overbilling risk.** Conversely, if the report does capture device connections but labels them ambiguously, Proudert may be paying for "users" it did not intend to include.

**Recommended fix:**

- Amend the usage-report requirement (SLA § 6.2) to specify that the report shall separately identify and count: (i) employee logins, (ii) contractor/interface sessions, and (iii) camera/sensor device connections.
- Clarify in the Amendment that the Module Fee applies only to cameras/sensors actually in production use (not in testing or staging), and that a camera in a test environment does not count.
- Add a dispute mechanism: if Proudert disputes the user count on a Module Fee invoice, it may do so under SLA § 5.3 (withhold disputed amount, 30-day resolution period) without penalty.

---

## Issue 14: Audit Rights May Be Used to Enforce the Expanded User Count (SLA § 6.3)

**Where:** SLA § 6.3 (Audit), read with Amendment § 1.1.

**Why it matters:** Vopein may audit once per 12 months on 30 days' notice to verify compliance with "Authorized User limits." With the expanded definition, an audit could reveal that Proudert has more cameras or contractor connections than it reported, triggering:

- A true-up payment (SLA § 5.4);
- Audit-cost reimbursement if the shortfall exceeds 10% of fees paid (SLA § 6.3).

The audit right is broad: it covers "records and use of the Software." Vopein could inspect network logs to identify all devices communicating with the Software, potentially finding connections Proudert did not consider "Authorized Users."

**Recommended fix:**

- Limit the audit scope to employee login credentials and explicitly exclude camera/sensor device counts from the audit (those should be governed by the Module Fee invoicing process in Amendment § 2.3).
- Add a requirement that any audit findings be subject to the dispute mechanism in SLA § 5.3 before payment is demanded.
- Cap the look-back period for true-ups at 12 months (the current language in § 5.4 already does this, but confirm it applies to audit-driven true-ups as well).

---

## Issue 15: Insurance Requirements May Be Inadequate for the Risk Profile (SLA § 14.1)

**Where:** SLA § 14.1.

**Why it matters:** Vopein must maintain $5M in technology E&O / cyber liability. Given that:

- The Software controls production at a weaving plant;
- The Vision Inspection Module processes images that may include proprietary product data;
- A data breach could expose Licensee Data (production records, quality records, specifications per SLA § 1.6);
- The liability cap in § 12.1 is only ~$164K–$209K;

...the $5M insurance is the primary source of recovery for a catastrophic event. However, the SLA does not require Vopein to name Proudert as an additional insured, does not require notice of cancellation, and does not give Proudert a direct right to make a claim under the policy.

**Recommended fix:**

- Require Vopein to name Proudert as an additional insured on the technology E&O / cyber policy.
- Add a requirement for 30 days' notice of cancellation or material change to the policy.
- Add a provision that Proudert may make a direct claim under Vopein's insurance policy to the extent of Vopein's liability under the Agreement.
- Consider increasing the cyber limit to $10M given the Vision Inspection Module's data-processing role.

---

## Summary of Items I Cannot Resolve From the Documents Alone

| # | Open Item | What I Need |
|---|-----------|------------|
| 1 | Whether an executed Schedule B exists | Client to confirm and provide copy if it does |
| 2 | Number of cameras/sensors deployed or planned | Client to provide current and planned device count |
| 3 | Number of third-party contractors with system access | Client to provide list or estimated count |
| 4 | Whether Proudert operates or plans other facilities (relevant to Side Letter § 3.1) | Client to confirm facility footprint and expansion plans |
| 5 | Whether the Side Letter was actually countersigned by Proudert (signature block is blank in the file) | Client to confirm execution status |
| 6 | Current status of the SOW 1 implementation (are milestones on track? Has Go-Live occurred?) | Client to provide project status |
| 7 | Whether Vopein has raised its list fees since the Effective Date (relevant to renewal exposure) | Market research or client inquiry |

---

## Recommended Priority Actions

1. **Immediately:** Calendar the non-renewal notice window for the Initial Term (September 1 – October 1, 2028). Set internal reminders for 270 days out.
2. **This week:** Confirm with the client whether Schedule B was executed and whether the Side Letter was countersigned. If Schedule B was never executed, escalate as a gap.
3. **Next 30 days:** Open a negotiation with Vopein on the top three issues: (a) Authorized User definition / camera count treatment, (b) exclusive-use covenant scope, (c) execution of Schedule B. Package these as a single amendment or letter of agreement.
4. **Before Go-Live (if not yet occurred):** Negotiate the deemed-acceptance fix (Issue 6) and the service-credit provision (Issue 8) as a SOW change order or side letter.
5. **Ongoing:** Track camera deployments and contractor access to model the Module Fee and tier-escalation exposure under the current (unfavorable) terms, so the client understands its run-rate cost.