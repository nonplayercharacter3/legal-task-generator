# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Proudert Technical Fabrics, Inc. – Vopein Systems LLC Software License: Issue Identification and Recommended Actions

---

## Summary

I have reviewed the five documents in the matter folder. I identify **twenty-three issues** ranging from critical structural gaps to commercially significant one-sided provisions. The most urgent items are: (1) Schedule B (Data Security) appears to have never been executed, leaving Proudert without enforceable data security requirements; (2) Amendment No. 1 redefines "Authorized User" to include cameras and sensor stations, with potentially dramatic fee consequences that were likely not fully appreciated at signing; and (3) the SOW contains a governing law and forum clause that conflicts with the main agreement, creating a split-jurisdiction regime. Details and recommended fixes follow.

---

## Issue 1: Schedule B (Data Security) Was Never Executed

**Where:** Schedule B prior draft, header ("Draft of February 20, 2026. Circulated for discussion. Not for execution."); SLA §8.2 (references "Schedule B (Data Security)").

**Why it matters:** Section 8.2 of the SLA obligates Vopein to "comply with the data security requirements set out in Schedule B." But the only version of Schedule B in the file is an unexecuted draft. If no final Schedule B was signed, Proudert has no enforceable data security requirements beyond the bare-bones provisions in SLA §8 (ownership, 72-hour incident notice, return of data). All the meaningful controls—MFA for remote access, encryption in transit and at rest, U.S.-only data storage, subcontractor consent, background checks, security questionnaire rights, SOC 2 report delivery—are in the draft only and carry no contractual force.

Given that the Vision Inspection Module (added by Amendment No. 1) will generate large volumes of image data from the weaving floor, and that Vopein personnel will have remote access to Proudert's systems for support, this gap is operationally significant.

**Recommended fix:**
- Confirm with the client whether a final Schedule B was executed. If not, negotiate and execute one immediately, using the prior draft as a starting point (it is reasonably protective).
- If Vopein resists, at minimum add to the SLA by amendment: (a) a requirement for MFA on all remote access; (b) encryption of Licensee Data in transit and at rest; (c) U.S.-only storage; and (d) prior written consent for subcontractor access.
- **Open item:** I cannot confirm from the documents alone whether a final Schedule B exists. Need to request the executed agreement package from the client.

---

## Issue 2: "Authorized User" Redefined to Include Cameras and Sensor Stations

**Where:** Amendment No. 1 §1.1 (amends and restates SLA §1.2); SLA §1.2 (original definition).

**Why it matters:** The original definition counted only "a Licensee employee at the Licensed Site issued individual LoomSight login credentials." The Amendment expands this to include:
- (b) "each contractor, consultant or other individual engaged by or on behalf of Licensee who has system access to the Software, whether through individual login credentials, shared credentials or an interface"; and
- (c) "each networked inspection camera or sensor station at the Licensed Site that captures, transmits or receives data through the Software."

This has compounding fee consequences:

1. **Core license tier bump (SLA §5.1):** The tier structure is based on Authorized User count. If Proudert has 70 human users plus 30 cameras, the count is 100, pushing Proudert into Tier 2 ($238,000 vs. $186,000). The true-up provision (SLA §5.4) would catch this within 30 days of each anniversary.

2. **Module Fee multiplication (Amendment §2.2):** The Vision Inspection Module costs $145 per Authorized User per month. If "Authorized User" includes every camera, a plant with 50 cameras pays $145 × 50 × 12 = $87,000/year in Module Fees for hardware alone, before counting any human users.

3. **Double-counting risk:** The same camera that pushes the core license into a higher tier also generates a Module Fee. Proudert pays twice for the same "user."

4. **Usage report mismatch (SLA §6.2 vs. Amendment §2.3):** SLA §6.2 says the usage report "shows the number of active login credentials." Amendment §2.3 says the Module Fee invoice states "the highest number of Authorized Users during each month of the quarter, as shown by the usage report described in Section 6.2." A networked camera does not have a "login credential" in any conventional sense. This creates a fundamental ambiguity about what the usage report actually measures and whether Vopein can unilaterally determine the count.

**Recommended fix:**
- Negotiate a revised definition that separates "human users" (for core license tiering) from "device connections" (for Module Fee purposes), or cap the number of devices that count toward the fee.
- Clarify in writing what the usage report measures and how device connections are counted. Require that the report distinguish between login credentials and device interfaces.
- Model the total cost impact under various camera/sensor counts and present to the client before the next true-up date (March 2, 2027, i.e., the first anniversary).
- **Open item:** Need to know the actual number of cameras and sensor stations Proudert has installed or plans to install for the Vision Inspection Module.

---

## Issue 3: Conflicting Governing Law and Forum (SOW vs. SLA)

**Where:** SOW 1 §10.1 (Pennsylvania law) and §10.2 (exclusive jurisdiction, Allegheny County, PA); SLA §15.2 (Delaware law) and §15.3 (exclusive jurisdiction, Wilmington, DE); SLA §15.6 (order of precedence: SOWs rank above the SLA).

**Why it matters:** Under the order of precedence in SLA §15.6, the SOW controls over the SLA in the event of a conflict. SOW §10 expressly provides that Pennsylvania law governs and that Allegheny County courts have exclusive jurisdiction for disputes "arising out of or relating to this SOW or the Services." This creates a split regime:
- Implementation disputes → Pennsylvania law, Allegheny County courts.
- License, fee, and data disputes → Delaware law, Wilmington courts.
- Hybrid disputes (e.g., a warranty claim under SLA §10.1 that is triggered by a SOW deliverable) → uncertain.

For Proudert, a Delaware corporation operating in South Carolina, being hauled into Pennsylvania for implementation disputes is inconvenient and likely more expensive than Delaware. It also means two different bodies of law could apply to factually intertwined claims.

**Recommended fix:**
- Amend SOW 1 §10 to conform to SLA §15.2–15.3 (Delaware law, Wilmington forum), or at minimum add a savings clause stating that if a dispute implicates both the SOW and the Agreement, the SLA's governing law and forum provisions control.
- If Vopein insists on Pennsylvania (it is a Pennsylvania company), consider whether a neutral forum or arbitration clause would be preferable for both sides.

---

## Issue 4: Auto-Renewal at "Then-Current List Fees" with a 30-Day Non-Renewal Window

**Where:** SLA §13.2.

**Why it matters:** Two compounding problems:

1. **Uncapped price increases at renewal.** The agreement renews for successive three-year terms "at Licensor's then-current list fees." There is no cap on the increase, no most-favored-nation clause, and no requirement that Vopein provide advance notice of a price change. The 12% Side Letter discount applies "during the Term" (Side Letter §2.4), and "Term" includes Renewal Terms (SLA §13.2), so the discount should survive. But the base fee to which the discount applies can jump to whatever Vopein's list price is at renewal.

2. **Extremely narrow non-renewal notice window.** Notice must be given "not less than 180 days and not more than 210 days before the end of the then-current Initial Term or Renewal Term." That is a 30-day window. Notice given outside that window is "void and of no effect." There is no cure, no grace period, no provision for accidental misdelivery.

For the Initial Term (ending March 1, 2029), the window is approximately **August 12, 2028 through September 1, 2028**. If Proudert's legal team misses it by a day, it is locked in for another three years at whatever Vopein's list price then is.

**Recommended fix:**
- Amend SLA §13.2 to: (a) cap renewal increases at a stated percentage (e.g., CPI or 5%); (b) widen the non-renewal notice window to at least 120 days before term end (with no outside limit); and (c) require Vopein to give Proudert at least 180 days' advance written notice of any fee increase before the renewal date.
- **Immediate action:** Calendar the non-renewal notice window for the Initial Term (August 12 – September 1, 2028) and set internal reminders at 6 months and 3 months before the window opens.

---

## Issue 5: No Uptime or Availability Commitment

**Where:** SLA §4 (Support Services) — response times are provided for Severity 1/2/3 issues, but there is no percentage uptime guarantee, no service level, and no service credits.

**Why it matters:** For a weaving plant running production 24/7 across multiple shifts, a software outage stops the line. The only remedy for a Severity 1 issue (production stopped) is that Vopein must *respond* within 2 hours (SLA §4.2). There is no obligation to *resolve* within any timeframe, no credit for downtime, and—critically—the consequential damages waiver in SLA §12.2 bars recovery for "LOSS OF PRODUCTION." So if the software is down for three days and Proudert loses $500,000 in production, Proudert's recovery is capped at the 12-month fee amount (SLA §12.1) and cannot include the lost production itself.

**Recommended fix:**
- Negotiate an uptime SLA (e.g., 99.5% monthly availability for the production environment) with service credits (e.g., 5% of monthly fee per hour of downtime beyond the threshold).
- Carve "loss of production" out of the consequential damages waiver for failures caused by Vopein's breach of the uptime SLA.
- At minimum, add a resolution-time target for Severity 1 issues (e.g., 8 hours) with escalating remedies.

---

## Issue 6: Consequential Damages Waiver Is Particularly Harsh for a Manufacturing Licensee

**Where:** SLA §12.2 (excludes "LOST PROFITS, LOST REVENUE OR LOSS OF PRODUCTION"); SLA §12.1 (cap at 12-month fees).

**Why it matters:** As noted in Issue 5, the combination of (a) a cap equal to roughly $163,680–$304,000 (depending on tier and timing) and (b) an express exclusion of lost production means that for the most likely and most damaging failure scenario—a software defect or outage that stops the weaving line—Proudert's maximum recovery is a fraction of its actual losses. The waiver is mutual, but the asymmetry in practical impact is stark: Vopein's maximum loss from a Proudert breach is unpaid fees; Proudert's maximum loss from a Vopein breach is a cap that may not cover a single day of downtime.

**Recommended fix:**
- Carve out of the consequential damages waiver: (a) Vopein's breach of data security obligations (SLA §8, Schedule B); (b) Vopein's indemnification obligations (SLA §11.1); and (c) any uptime SLA that is negotiated (see Issue 5).
- Increase the liability cap for Vopein's breaches to at least 2× or 3× the 12-month fee amount, or tie it to the total contract value over the remaining Term.

---

## Issue 7: Indemnification Asymmetry for the Vision Inspection Module

**Where:** SLA §11.1 (Licensor's IP indemnity excludes claims arising from "combination of the Software with Licensee Systems or other items not supplied by Licensor, where the claim would not have arisen but for the combination"); SLA §11.2(b) (Licensee indemnifies for "use of the Software in combination with Licensee equipment, looms, loom controllers or third-party systems, including Licensee Systems"); Amendment §2.7 (cameras, lighting, sensor stations are "Licensee Systems").

**Why it matters:** The Vision Inspection Module is fundamentally a hardware-software integration. It is designed to work with cameras and sensor stations that are, by definition, "Licensee Systems" (Amendment §2.7). If a third party asserts that the combination of Vopein's ML defect-detection algorithms with Proudert's camera hardware infringes a patent:
- Vopein can argue §11.1(ii) excludes the claim because it "would not have arisen but for the combination" with Licensee Systems.
- Proudert is affirmatively indemnifying Vopein under §11.2(b) for that same combination.

This creates a scenario where Proudert is on the hook for an IP claim arising from the core function of the module it licensed, while Vopein has no indemnity obligation. The original software (MES Core, Quality, Connect, Reports) is less affected because the "combination" with loom controllers is more incidental. But for the Vision Inspection Module, the hardware *is* the point.

**Recommended fix:**
- Amend SLA §11.1 to add: "For the Vision Inspection Module, the exclusion in clause (ii) shall not apply to claims arising from the combination of the Software with cameras, lighting, or sensor stations that are specified or recommended by Licensor in the Documentation or in a Statement of Work."
- Alternatively, narrow §11.2(b) to exclude claims arising from the Software's intended function as described in the Documentation.

---

## Issue 8: No SOW or Change Order for Vision Inspection Module Implementation

**Where:** SOW 1 §2.9 (out of scope: "modules not listed in Schedule A of the Agreement"); Amendment §3.1 ("Any installation, configuration, model training, integration or other Services that Licensor performs for the Vision Inspection Module shall be described in a Statement of Work or in a change order").

**Why it matters:** The Amendment adds the Vision Inspection Module to Schedule A and licenses it, but it does not itself commission any implementation services. SOW 1 was signed before the Amendment and expressly excludes modules not then in Schedule A. No SOW 2 or change order for the Vision Inspection Module is in the matter folder. This means:
- There is no agreed scope, schedule, deliverables, or acceptance criteria for installing and configuring the module.
- There is no agreed fee for implementation (model training, camera integration, etc.).
- There is no defined Go-Live for the module (which would trigger the 12-month warranty under Amendment §2.6).
- Proudert is paying the Module Fee ($145/user/month from the Amendment Date, i.e., September 8, 2026) for a module that may not yet be installed or functional.

**Recommended fix:**
- Confirm with the client whether a SOW 2 or change order for the Vision Inspection Module has been negotiated or is in progress. If not, prepare one immediately, covering: scope (camera integration, model training, UAT), schedule, deliverables, acceptance criteria, fees, and a defined Go-Live trigger for the warranty.
- Until implementation is complete and accepted, consider whether Proudert should be paying the full Module Fee. The Amendment does not provide for a free trial or reduced rate during the implementation period.

---

## Issue 9: Deemed Acceptance Provisions Are Aggressive for a Manufacturing Environment

**Where:** SOW §5.3.

**Why it matters:** Two deemed acceptance triggers:
1. **Document deliverables:** If Proudert doesn't approve or comment within 10 business days, and doesn't respond to Vopein's follow-up notice within 5 more business days, the deliverable is deemed accepted. For technical documents (solution design, integration specs, data migration mapping), 10 business days is tight when the review requires input from production, quality, and IT teams across shifts.
2. **Go-Live (M4):** "Using the Software in production for live production orders is deemed acceptance of Milestone M4." In a manufacturing plant, there may be operational pressure to go live (e.g., a production schedule that can't wait for all UAT issues to be resolved). The moment an operator logs a live production order, M4 is accepted, the 25% milestone payment ($53,625) becomes due, and the 12-month warranty clock starts.

**Recommended fix:**
- Amend SOW §5.3 to require that deemed acceptance of M4 applies only if the Software has been in continuous production use for a minimum period (e.g., 10 business days) with no open Severity 1 issues.
- Extend the document review period from 10 to 15 business days for the solution design document and integration specifications.
- Add a proviso that deemed acceptance does not waive Proudert's right to claim a breach of warranty under SLA §10.1 for defects that were not reasonably discoverable during UAT.

---

## Issue 10: Exclusivity Restriction Is Overly Broad in Scope and Duration

**Where:** Side Letter §3.1 (exclusive use during Term + 24 months); §3.2 (definition of "competing" software).

**Why it matters:**
- **Geographic scope:** "any facility owned or operated by Licensee or any of its Affiliates, anywhere in the world." Proudert is a Delaware corporation; if it has or acquires facilities in other states or countries, they are all covered.
- **Functional scope:** "competing" includes software providing "production order management, machine or loom scheduling, work-in-process tracking, defect logging, product grading, statistical process control or automated inspection functions that are substantially similar to those of the Software." This is broad enough to capture a new ERP module, a standalone quality tracking tool, or even an in-house Python script for SPC charts, if it is "substantially similar."
- **Duration:** The Term auto-renews for 3-year periods (SLA §13.2). If Proudert misses the non-renewal window (see Issue 4), the Term extends, and the exclusivity extends with it. The 24-month tail then runs from the end of whatever the then-current Term is. In the worst case, Proudert could be locked into exclusivity for 5+ years from any given renewal.
- **Affiliate reach:** The restriction binds "its Affiliates" (defined as entities under common >50% control, SLA §1.1). If Proudert is acquired or forms a joint venture, the scope could shift.

**Recommended fix:**
- Narrow the geographic scope to the Licensed Site (or, at most, facilities where the Software is actually deployed).
- Narrow the functional scope by requiring that the competing software be deployed in a textile weaving environment and provide the same combination of functions, rather than any single overlapping function.
- Cap the total exclusivity period (e.g., no more than 36 months from the Effective Date, regardless of renewals).
- Add a carve-out for software that is already deployed at a Proudert facility as of the Effective Date.

---

## Issue 11: Data Export Obligations Are Weak

**Where:** SLA §8.4.

**Why it matters:** Upon expiration or termination, Vopein shall "cooperate in exporting Licensee Data in a standard, machine-readable format." Problems:
- "Cooperate" is not "shall export" or "shall provide." Vopein could argue it has met its obligation by making a contact available, without actually performing the export.
- "Standard, machine-readable format" is undefined. Is CSV standard? JSON? A proprietary export that happens to be readable by a machine?
- There is no timeframe for the export.
- There is no cost allocation. Will Vopein charge professional services rates for the export?
- For a weaving plant with years of quality records, production data, and (post-Amendment) vision inspection images, the data is a critical asset. If the export is messy or incomplete, Proudert loses institutional knowledge.

**Recommended fix:**
- Amend SLA §8.4 to: (a) require Vopein to *perform* the export (not merely cooperate); (b) specify the format (e.g., CSV for tabular data, original file format for images); (c) set a deadline (e.g., within 30 days of termination); (d) state that the export is included in transition assistance at no additional charge; and (e) require Vopein to provide a data completeness certification.

---

## Issue 12: Transition Assistance Is Limited and Uncapped in Price

**Where:** SLA §13.6.

**Why it matters:** Transition assistance is limited to 90 days and is provided at Vopein's "then-current professional services rates." For a manufacturing plant with loom integrations, ERP interfaces, and quality workflows embedded in the software, 90 days may be insufficient to migrate to a replacement system. And "then-current rates" means Vopein can set whatever rate it wants at that time, with no cap.

**Recommended fix:**
- Extend the transition assistance period to 180 days.
- Cap the rates at those in effect on the date of termination (or at the SOW 1 hourly rates, whichever is lower).
- Require Vopein to provide a transition plan within 30 days of notice of non-renewal or termination.

---

## Issue 13: Feedback Clause Allows Vopein to Use Proudert's Process Improvements for Competitors

**Where:** SLA §7.4.

**Why it matters:** "Licensor may use any suggestions or feedback that Licensee provides about the Software, without obligation to Licensee, provided that it does not disclose Licensee's Confidential Information." During implementation and ongoing use, Proudert will provide extensive feedback about how the software should handle conveyor belting, geotextiles, and filtration media—processes that are competitively sensitive. Vopein can use that feedback to improve LoomSight for other textile manufacturers (Proudert's competitors) with no compensation, no restriction, and no obligation to Proudert. The only guardrail is that Vopein can't disclose "Confidential Information," but process suggestions made in the course of a support call or a SOW workshop may not be marked as confidential and may not meet the "reasonably understood to be confidential" threshold in SLA §1.3.

**Recommended fix:**
- Amend SLA §7.4 to exclude from the feedback license any suggestions that relate to Licensee's specific manufacturing processes, product specifications, or quality standards, or that are identified by Licensee as confidential at the time of disclosure.
- Alternatively, require that feedback be in writing and marked "Feedback – Subject to Section 9" to bring it within the confidentiality regime.

---

## Issue 14: Support Exclusion for Licensee Systems Creates a Gap for the Vision Inspection Module

**Where:** SLA §4.3(c) (support excludes "failures of Licensee Systems not supplied by Licensor"); Amendment §2.7 (cameras, lighting, sensor stations are Licensee Systems).

**Why it matters:** If a camera fails to transmit images and the Vision Inspection Module stops detecting defects, Vopein can argue the issue is a "failure of Licensee Systems not supplied by Licensor" and is excluded from support. But the module is *designed* to work with those cameras. If the camera integration is faulty (wrong protocol, incompatible firmware, misconfigured network), the root cause may be in Vopein's integration work, not in the camera hardware. The exclusion as written gives Vopein an easy out.

**Recommended fix:**
- Amend SLA §4.3(c) to add: "This exclusion shall not apply to failures caused by the integration of the Software with Licensee Systems where the integration was designed, configured, or implemented by Licensor under a Statement of Work."
- In the SOW for the Vision Inspection Module (see Issue 8), define the interface specifications and acceptance criteria for camera integration so that "failure" can be objectively determined.

---

## Issue 15: Module Fee Is Not Covered by the Side Letter Discount

**Where:** Side Letter §2.1–2.3 (discount applies to "the annual core license fee payable under Section 5.1"); Amendment §2.2 (Module Fee is "payable in addition to the annual core license fee").

**Why it matters:** The 12% discount reduces the core license fee but does not apply to the Module Fee. As the Vision Inspection Module scales (more cameras, more sensor stations, more human users interacting with it), the Module Fee will grow as a proportion of total licensing cost, and none of it receives the discount. If the Module Fee eventually exceeds the core fee, Proudert is paying a discounted rate on the smaller amount and full rate on the larger amount.

**Recommended fix:**
- Negotiate to extend the 12% discount to the Module Fee, or at minimum to the portion of the Module Fee attributable to human Authorized Users (as opposed to device connections).
- Alternatively, negotiate a volume discount on the Module Fee that kicks in at a stated number of Authorized Users.

---

## Issue 16: Audit Rights Are Risky Given the Expanded "Authorized User" Definition

**Where:** SLA §6.3 (audit once per 12 months, 30 days' notice; if shortfall >10%, Proudert pays audit costs); Amendment §1.1 (expanded definition).

**Why it matters:** With cameras and sensor stations now counting as "Authorized Users," the line between a "user" and a "device" becomes fact-intensive. An audit could reveal that Proudert has, say, 47 cameras but Vopein's usage report shows 52 "active" device connections (perhaps due to network retries, test units, or decommissioned cameras still on the network). If the discrepancy exceeds 10% of fees, Proudert pays the audit cost. The audit scope ("records and use of the Software") is broad enough to cover how devices are connected and whether they should be counted.

**Recommended fix:**
- Before the first audit window opens, implement an internal process to reconcile the camera/sensor inventory with the usage report monthly.
- Negotiate a de minimis threshold (e.g., 5% rather than 10%) before Proudert bears audit costs.
- Clarify in the SLA or by side letter that decommissioned devices that are no longer actively transmitting data do not count as "Authorized Users."

---

## Issue 17: Warranty Start Date for the Vision Inspection Module Is Ambiguous

**Where:** Amendment §2.6 (warranty begins "on the date Licensee first uses the Vision Inspection Module in production at the Licensed Site"); SOW §1.2(a) (Go-Live defined as "confirmed in writing by both Parties' Project Managers"); SLA §10.1 (warranty runs 12 months "after go-live").

**Why it matters:** The base software warranty starts at Go-Live, which requires written confirmation by both Project Managers. The Vision Inspection Module warranty starts when Proudert "first uses" the module "in production"—with no confirmation requirement. This creates two problems:
1. Vopein could argue the warranty started on the first day a camera was connected and an image was captured, even if the module was still in testing or configuration.
2. There is no objective milestone or sign-off that marks the start of the warranty period, making it easy to dispute.

**Recommended fix:**
- Amend Amendment §2.6 to require that the warranty period begins on a date confirmed in writing by both Parties' Project Managers, consistent with the Go-Live definition in SOW §1.2(a).
- In the SOW for the Vision Inspection Module implementation (see Issue 8), define a specific milestone (e.g., "Vision Module Go-Live") with acceptance criteria.

---

## Issue 18: Insurance Does Not Survive Termination

**Where:** SLA §13.7 (survival list does not include Section 14); SLA §14 (insurance requirements).

**Why it matters:** Section 14 requires Vopein to maintain $5M in technology E&O / cyber liability insurance during the Term. But Section 14 is not in the survival list. After termination, Vopein still has Proudert's data during the export and deletion period (SLA §8.4), and may still be providing transition assistance (SLA §13.6). If a data breach occurs during that post-termination window, Vopein's insurance obligation has lapsed.

**Recommended fix:**
- Add Section 14 to the survival list in SLA §13.7, with a proviso that the insurance requirement continues for 12 months after expiration or termination (to cover the data return and transition period).

---

## Issue 19: Section 8.2 (Data Security Compliance) Does Not Survive Termination

**Where:** SLA §13.7 (survival list includes §8.4 but not §8.2).

**Why it matters:** Section 8.2 requires Vopein to comply with Schedule B data security requirements "whenever it accesses Licensee Systems or Licensee Data." After termination, Vopein will still be accessing Licensee Data to perform the export (SLA §8.4) and transition assistance (SLA §13.6). But §8.2 does not survive, so the data security requirements (to the extent they are in effect at all—see Issue 1) technically end at termination. Vopein could handle Proudert's data during the transition without any contractual security obligations.

**Recommended fix:**
- Add Section 8.2 to the survival list, applicable for so long as Vopein retains or accesses any Licensee Data post-termination.

---

## Issue 20: SOW Milestone M3 Acceptance Allows Severity 2 Issues with Workarounds

**Where:** SOW §5.2 (M3 accepted when Software passes UAT "with no open Severity 1 or Severity 2 issues"); SLA §4.2 (Severity 2 = "material function impaired with no reasonable workaround").

**Why it matters:** The acceptance criterion is "no open Severity 1 or Severity 2 issues." But Severity 2 is defined as a material function impairment *with no reasonable workaround*. If a material function is impaired but a workaround exists, it is not Severity 2—it is Severity 3 ("minor function impaired or workaround available"). This means a material defect in, say, the statistical process control module that can be "worked around" by manually entering data would not block M3 acceptance. For a quality-critical application in technical textiles (where certificates of analysis are generated by the software), this is an inadequate acceptance standard.

**Recommended fix:**
- Amend SOW §5.2 to require that M3 acceptance also requires no open issues that affect the accuracy of quality records, certificates of analysis, or statistical process control outputs, regardless of severity classification.
- Alternatively, add a project-specific severity definition in the SOW that is stricter than the general SLA definitions for quality-related functions.

---

## Issue 21: Reference Customer Obligation Lacks a Right to Refuse

**Where:** Side Letter §3.3.

**Why it matters:** Proudert "agrees to act as a reference customer" and "will take part in no more than four (4) reference calls or site visits per year, scheduled at mutually agreed times." The phrase "mutually agreed times" suggests scheduling flexibility, but the opening language is an agreement to participate. There is no express right to decline a specific reference request. For a manufacturing company, a site visit by a prospective Vopein customer (who may be a competitor) raises security and competitive concerns. Even a phone reference call could reveal production volumes, quality metrics, or process details.

**Recommended fix:**
- Amend Side Letter §3.3 to give Proudert the right to decline any specific reference request on reasonable grounds (e.g., the prospective customer is a direct competitor, or the request would require disclosure of production volumes or quality data).
- Limit reference calls to a discussion of general satisfaction with the Software, without specific performance metrics.

---

## Issue 22: Order of Precedence Places Side Letter Last, Undermining the Exclusivity Quid Pro Quo

**Where:** SLA §15.6 (precedence: Amendments > SOWs > SLA > Side Letters); Side Letter §3.1 (exclusivity is given "in consideration of" the discount in §2.1).

**Why it matters:** The Side Letter is structured as a quid pro quo: Proudert gives exclusivity (§3) in exchange for the 12% discount (§2). But under the order of precedence, the Side Letter is the lowest-priority document. If any provision in the SLA, a SOW, or an Amendment is arguably inconsistent with the Side Letter, the Side Letter yields. For example, if a future SOW or amendment implicitly contemplates the use of a third-party tool for a function that Side Letter §3.2 defines as "competing," the SOW/amendment would control and the exclusivity restriction would be overridden. This inverts the commercial bargain: Proudert gives up exclusivity but may not get to rely on the discount if a conflict arises.

**Recommended fix:**
- Amend SLA §15.6 to provide that the Side Letter ranks above the SLA (but below Amendments and SOWs), or to provide that in the event of a conflict between the Side Letter and any other document, the Side Letter controls with respect to the pricing and exclusivity provisions.
- Alternatively, move the key Side Letter provisions (discount, exclusivity) into the SLA itself or into an Amendment, where they would have higher precedence.

---

## Issue 23: No Termination Right for Proudert Based on Repeated Support Failures

**Where:** SLA §13.3 (termination for material breach with 30-day cure); SLA §4 (Support Services).

**Why it matters:** The only termination-for-cause right is for "material breach" with a 30-day cure period. If Vopein chronically misses Severity 1 response times (e.g., responds in 4 hours instead of 2, repeatedly), it is hard to argue this rises to "material breach" of the agreement as a whole, especially given the consequential damages waiver and the lack of an uptime SLA. Proudert has no right to terminate for a pattern of sub-par support short of a complete failure to provide support at all.

**Recommended fix:**
- Add a termination right for Proudert if Vopein fails to meet Severity 1 response times in more than [X] instances in any [Y]-month period, or if the overall support satisfaction score (measured quarterly) falls below a stated threshold for two consecutive quarters.
- Alternatively, tie chronic support failures to the warranty: if the Software is not performing "materially in accordance with the Documentation" (SLA §10.1) due to repeated unresolved issues, Proudert should be able to invoke the warranty termination right without waiting 30 days for a cure that may not come.

---

## Items Requiring Additional Information

| # | Open Item | What I Need |
|---|-----------|-------------|
| 1 | Was a final Schedule B executed? | Request the fully executed agreement package from the client. If only the prior draft exists, this is the highest-priority gap to close. |
| 2 | How many cameras/sensor stations are installed or planned? | Need the count to model the fee impact of the expanded "Authorized User" definition (Issue 2). |
| 3 | Has a SOW 2 or change order for the Vision Inspection Module been negotiated? | Need to confirm status. If not, this is urgent (Issue 8). |
| 4 | What is the current Authorized User count (human + device)? | Needed to determine whether Proudert is already in a higher tier than the Base Tier and whether the next true-up (March 2, 2027) will trigger a fee increase. |
| 5 | Has the base software reached Go-Live? | SOW milestone M4 targeted October 5, 2026. Need to confirm actual Go-Live date to determine when the 12-month warranty expires and when the first true-up occurs. |
| 6 | Are there any other Proudert facilities where LoomSight or competing software is deployed? | Relevant to the exclusivity restriction (Issue 10) and the "Licensed Site" limitation. |

---

## Suggested Priority for Client Discussion

1. **Immediate (this week):** Confirm Schedule B status; model the Authorized User fee impact; calendar the non-renewal notice window (Aug–Sep 2028).
2. **Near-term (next 30 days):** Open negotiations on a SOW for the Vision Inspection Module; propose amendments to the governing law conflict, the data export clause, and the indemnification asymmetry.
3. **Medium-term (next 90 days):** Negotiate an uptime SLA, revised liability cap, and narrowed exclusivity. Bundle these as a "Proudert protection package" in a single Amendment No. 2.
4. **Ongoing:** Implement internal processes for Authorized User tracking, data export readiness, and support-level monitoring.