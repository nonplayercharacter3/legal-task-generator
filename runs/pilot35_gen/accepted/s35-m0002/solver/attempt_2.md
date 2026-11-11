# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Proudert Technical Fabrics, Inc. – Vopein Systems LLC Software License: Issue Identification and Recommended Actions

---

## Summary

I have reviewed the five documents in the matter folder: the Software License Agreement (executed March 2, 2026), the Pricing Side Letter (same date), SOW 1 – Implementation (dated March 16, 2026), Amendment No. 1 – Vision Inspection Module (dated September 8, 2026), and a prior draft of Schedule B – Data Security (dated February 20, 2026, marked "Not for execution"). I have identified **twelve issues** that warrant attention, ranging from a potentially inoperable data-security schedule to a redefined "Authorized User" term that materially increases Proudert's cost exposure. Below is each issue with its source, why it matters, and a recommended fix.

---

## Issue 1: Schedule B (Data Security) Appears Not to Have Been Executed

**Where:** Agreement §8.2 references "Schedule B (Data Security)" as a binding component of the Agreement. The only Schedule B in the folder is the prior draft dated February 20, 2026, which is expressly marked *"Draft of February 20, 2026. Circulated for discussion. Not for execution."* The Agreement was executed March 2, 2026.

**Why it matters:** Section 8.2 obligates Vopein to "comply with the data security requirements set out in Schedule B." If no executed Schedule B was attached to the final Agreement, that obligation is inoperable—Vopein has no specific, enforceable data-security requirements beyond the general language in §§8.1–8.4. The prior draft contains meaningful protections (MFA for remote access, U.S.-only data storage, subcontractor consent, annual security questionnaire, SOC 2 report delivery, 72-hour incident notice with content requirements) that Proudert presumably negotiated for. Without an executed Schedule B, Proudert has no contractual basis to demand any of those specifics.

**Recommended fix:**
- Confirm with the client whether an executed Schedule B was attached to the final Agreement signature pages. If it was, obtain a copy and compare it against the prior draft to identify any changes Vopein made.
- If no executed Schedule B exists, this is a material gap. Recommend that Proudert request execution of a Schedule B (the prior draft is a reasonable starting point) as a condition of continuing the relationship, or as part of the next renewal negotiation. In the interim, §8.2's general reference and §8.3's 72-hour incident notice remain, but they are thin.

**Open item:** I cannot resolve from the documents alone whether a final Schedule B was executed. **Need:** a copy of the fully executed Agreement signature pages and any attached schedules.

---

## Issue 2: Expanded "Authorized User" Definition Drastically Increases Cost Exposure

**Where:** Amendment No. 1 §1.1 amends and restates Agreement §1.2. The original definition covered only "a Licensee employee at the Licensed Site issued individual LoomSight login credentials." The amended definition adds:
- (b) "each contractor, consultant or other individual engaged by or on behalf of Licensee who has system access to the Software, whether through individual login credentials, **shared credentials or an interface**"; and
- (c) "each **networked inspection camera or sensor station** at the Licensed Site that captures, transmits or receives data through the Software."

**Why it matters:** This is the single most financially significant issue in the contract set. "Authorized User" drives three cost mechanisms:

1. **Core license tier pricing (Agreement §5.1):** Tiers are 1–75 ($186K), 76–125 ($238K), 126–200 ($304K), 201+ ($304K + $1,400/user). If Proudert has, for example, 60 employees, 15 contractors, and 150 camera/sensor stations, the count is 225—pushing Proudert into Tier 4 at $304,000 + (25 × $1,400) = $339,000, versus $186,000 under the original definition.

2. **Vision Inspection Module Fee (Amendment §2.2):** $145 per Authorized User per month. At 225 users, that is $225,000/year for the module alone.

3. **User true-up (Agreement §5.4):** Annual reporting of the *highest* number of Authorized Users in the preceding 12 months, with retroactive billing.

The inclusion of hardware (cameras, sensor stations) as "Authorized Users" is unusual and effectively converts a per-device hardware cost into a per-user software license cost. The "shared credentials or an interface" language in (b) also means that a single ERP interface or a shared kiosk login could count as an Authorized User.

**Recommended fix:**
- Quantify Proudert's actual current and projected Authorized User count under the amended definition (employees + contractors + cameras/sensors + any interface-based access).
- Negotiate an amendment to either (a) exclude cameras and sensor stations from the "Authorized User" count for core license tier purposes (counting them only for the Module Fee, or not at all), or (b) establish a fixed cap or flat fee for the Vision Inspection Module that is not tied to the Authorized User count.
- If Proudert is already in a higher tier than it would be under the original definition, seek a one-time true-up credit or a phased transition.

**Open item:** I need from the client: (1) the number of employees with LoomSight credentials; (2) the number of contractors/consultants with system access; (3) the number of networked cameras and sensor stations deployed or planned; and (4) whether any third-party systems access the Software via interface.

---

## Issue 3: Conflicting Governing Law and Forum Provisions

**Where:**
- Agreement §15.2: Delaware law. §15.3: Exclusive jurisdiction in Wilmington, Delaware.
- SOW 1 §10.1: Pennsylvania law. §10.2: Exclusive jurisdiction in Allegheny County, Pennsylvania.
- Amendment No. 1 §4.2: Incorporates Agreement §§15.2–15.3 (Delaware).
- Side Letter §5.3: Incorporates Agreement §§15.2–15.3 (Delaware).

**Why it matters:** Under the Agreement's order of precedence (§15.6), SOWs rank *above* the main Agreement. This means that for disputes "arising out of or relating to the Services" (i.e., the implementation work under SOW 1), Pennsylvania law and Allegheny County forum govern. For all other disputes (license fees, data security, confidentiality, termination), Delaware law and Wilmington forum govern. Proudert is a Delaware corporation operating in South Carolina; Vopein is a Pennsylvania LLC. This split creates:
- Strategic litigation risk: Vopein could characterize a dispute as "relating to the Services" to forum-shift to Pennsylvania (its home turf).
- Inconsistent legal standards: Pennsylvania and Delaware differ on issues like the economic loss doctrine, consequential damages enforceability, and software license interpretation.
- Practical burden: Proudert would need counsel in two jurisdictions.

**Recommended fix:**
- Negotiate a conforming amendment to SOW 1 §10, deleting the Pennsylvania governing law and forum provisions and replacing them with a reference to Agreement §§15.2–15.3. If the SOW has already been performed and paid in full, this is less urgent but still important for any residual warranty or dispute claims.
- If Vopein resists, at minimum seek a clarification that the SOW forum provision applies only to disputes over the scope, quality, or payment of implementation Services, and not to any claim involving the Software license, data, or confidentiality.

---

## Issue 4: Side Letter Exclusivity Restriction Is Overly Broad

**Where:** Side Letter §3.1: During the Term and for 24 months after expiration or termination, Proudert shall not "license, develop or use any competing manufacturing execution or quality inspection software at **any facility owned or operated by Licensee or any of its Affiliates, anywhere in the world**." Section 3.2 defines "competing" software as anything providing functions "substantially similar" to the Software.

**Why it matters:**
- **Geographic scope:** The restriction covers all Proudert facilities worldwide, not just the Greenville Licensed Site. If Proudert has or acquires other plants (in the U.S. or internationally), they cannot use alternative MES or QI software there for 24 months post-termination.
- **Functional scope:** "Substantially similar" is undefined and could be read broadly. The Software covers production order management, loom scheduling, WIP tracking, defect logging, roll grading, SPC, and CoA generation. A general-purpose ERP with a production module, or a standalone SPC tool, could arguably be "substantially similar."
- **Affiliate restriction:** Proudert must "cause its Affiliates" to comply, extending the restriction to entities Proudert controls.
- **No carve-out for existing software:** There is no exception for software already deployed at other facilities before the Effective Date.
- **Consideration imbalance:** The exclusivity is the "consideration" for a 12% discount (~$22,320/year on the Base Tier). A worldwide, multi-year, post-termination exclusivity is disproportionate to that benefit.

**Recommended fix:**
- Negotiate a narrowing amendment to Side Letter §3.1: limit the restriction to the Licensed Site only (or to facilities where the Software is actually deployed); add a carve-out for software in use as of the Effective Date; and define "competing" more narrowly (e.g., "software whose primary purpose is [specific functions]" rather than "substantially similar").
- If Vopein will not narrow the restriction, consider whether the 12% discount is worth the operational constraint. Model the cost of being locked out of a better or cheaper alternative at another plant for 24 months post-termination.

---

## Issue 5: Side Letter Discount May Not Survive Renewal at "List Fees"

**Where:**
- Agreement §13.2: On renewal, the Agreement continues "at Licensor's then-current list fees."
- Side Letter §2.4: The 12% discount "applies to each annual core license fee invoice issued during the Term."
- Agreement §13.2 defines "Term" as the Initial Term plus all Renewal Terms.

**Why it matters:** On its face, the discount should apply during Renewal Terms because the Side Letter uses the defined term "Term." However, the renewal provision says fees reset to "then-current list fees," which could be read as resetting the baseline to which the discount applies. If Vopein increases list prices by, say, 20% at renewal, Proudert pays 20% more before the 12% discount is applied. There is no cap on list-price increases, no most-favored-customer clause, and no price-protection mechanism. Additionally, because the Side Letter is at the *bottom* of the precedence order (Agreement §15.6), any future amendment that modifies the fee structure could inadvertently override or conflict with the discount.

**Recommended fix:**
- Seek a clarification or amendment stating that the 12% discount applies to the list fee in effect at the start of each Renewal Term, and that list-fee increases during any Term shall not exceed a stated percentage (e.g., CPI or 5% per year).
- Alternatively, lock the Base Tier fee for the full Initial Term plus one Renewal Term.

---

## Issue 6: Automatic Renewal with a Narrow Non-Renewal Window

**Where:** Agreement §13.2: The Agreement automatically renews for successive three-year terms. Either Party may prevent renewal only by giving notice "not less than 180 days and not more than 210 days before the end of the then-current Initial Term or Renewal Term." Notice outside that window "shall be void and of no effect."

**Why it matters:** The 30-day window (between day 210 and day 180 before term end) is extremely narrow. For the Initial Term ending March 2, 2029, Proudert must deliver non-renewal notice between September 1, 2028 and October 2, 2028. Missing this window by even one day locks Proudert into another three-year term at Vopein's then-current list fees. There is no cure mechanism, no "reasonable efforts" savings clause, and no requirement that Vopein remind Proudert of the approaching deadline.

**Recommended fix:**
- Calendar the non-renewal notice window immediately (September 1 – October 2, 2028 for the Initial Term) and set internal reminders at T-minus 6 months.
- Negotiate an amendment to (a) widen the window (e.g., 120–270 days), (b) require Vopein to send a written reminder 270 days before term end, and (c) provide that notice given within 30 days after the window closes is effective if Vopein has not sent its reminder.

---

## Issue 7: Limitation of Liability Is Inadequate for a Manufacturing Environment

**Where:** Agreement §12.1 (cap: fees paid/payable in prior 12 months), §12.2 (exclusion of consequential damages including "LOSS OF PRODUCTION"), §12.3 (exceptions: only Licensee's indemnity obligations, Licensee's fee payment, and fraud/willful misconduct).

**Why it matters:** Proudert operates a weaving plant. If the Software fails, is breached, or causes a data incident that halts production, Proudert's actual damages (lost production, spoiled fabric, missed delivery deadlines, customer penalties) will vastly exceed 12 months of fees (~$163,680–$339,000 depending on tier). Section 12.2 expressly bars recovery of "LOSS OF PRODUCTION." The §12.3 exceptions do not carve out:
- Vopein's indemnification obligations under §11.1 (IP infringement),
- Breach of data security obligations (§8.2 / Schedule B),
- Breach of confidentiality (§9),
- Vopein's gross negligence.

This means that if Vopein's data security failure exposes Proudert's production data, or if a Software defect causes a multi-day production stoppage, Proudert's recovery is capped at roughly one year of fees and cannot include lost production.

**Recommended fix:**
- Negotiate a super-cap (e.g., 2× or 3× the 12-month fee cap) for breaches of §8 (Data Security), §9 (Confidentiality), and §11.1 (Vopein's IP indemnity).
- Carve out "loss of production" from the consequential damages exclusion where the loss is directly caused by Vopein's breach of §8 or §10 (Warranties).
- At minimum, add Vopein's §11.1 indemnification obligation to the §12.3 exceptions so the IP indemnity is not subject to the cap.

---

## Issue 8: Indemnification Is Asymmetric and Lacks a Data-Security Indemnity

**Where:** Agreement §11.1 (Vopein indemnifies only for U.S. IP infringement), §11.2 (Proudert indemnifies for Licensee Data claims *and* combination claims).

**Why it matters:**
- Vopein's indemnity is narrow: IP infringement only, U.S. only. There is no indemnity for Vopein's negligence, data security breach, or violation of confidentiality.
- Proudert's indemnity is broader: it covers any third-party claim arising from Licensee Data (including claims that the data itself infringes someone's rights) *and* any claim arising from combining the Software with Proudert's equipment. The combination indemnity in §11.2(b) could be triggered if a loom controller malfunction is blamed on the Software integration.
- If a data breach occurs due to Vopein's failure to maintain security, Proudert has no indemnity—only a damages claim subject to the §12 cap and the §12.2 consequential damages bar.

**Recommended fix:**
- Add a data-security indemnity: Vopein shall indemnify Proudert against third-party claims and regulatory fines arising from a Security Incident caused by Vopein's breach of §8 or Schedule B.
- Narrow §11.2(b): the combination indemnity should apply only where the claim would not have arisen but for the combination (mirroring the carve-out already in §11.1), and should not apply where the combination was performed in accordance with the Documentation.

---

## Issue 9: Support Exclusion for "Licensee Systems" Creates a Gap for the Vision Inspection Module

**Where:**
- Agreement §4.3(c): Support Services do not cover "failures of Licensee Systems not supplied by Licensor."
- Amendment No. 1 §2.7: "Cameras, lighting, mounting hardware, sensor stations and related network equipment for the Vision Inspection Module are **Licensee Systems**."

**Why it matters:** The Vision Inspection Module is entirely dependent on cameras, lighting, and sensor stations to function. If the module fails because a camera is misaligned, a light source is degraded, or a network switch drops packets, Vopein can point to §4.3(c) and §2.7 to say the failure is a "Licensee Systems" issue outside support. But Proudert may not have the expertise to diagnose whether the problem is in the hardware or the software. This creates a diagnostic gap where neither party is clearly responsible for troubleshooting.

**Recommended fix:**
- Negotiate a "first-response diagnostic" obligation: for any Severity 1 or Severity 2 issue involving the Vision Inspection Module, Vopein shall perform an initial remote or on-site diagnostic to determine whether the root cause is the Software or Licensee Systems, at no additional charge. Only after that diagnostic can the §4.3(c) exclusion be invoked.
- Alternatively, include basic hardware health-checking in the module's support scope.

---

## Issue 10: Deemed Acceptance and Go-Live Trigger Are Aggressive

**Where:**
- SOW 1 §5.3: If Proudert does not respond to a deliverable within the review period plus 5 business days after Vopein's written notice, the deliverable is "deemed accepted." Critically: "Using the Software in production for live production orders is deemed acceptance of Milestone M4."
- SOW 1 §11.2: The 12-month Software warranty period "begins on Go-Live."
- SOW 1 §1.1(a): "Go-Live" is the date Proudert "first uses the Software in production for live production orders."

**Why it matters:** In a manufacturing environment, there is often pressure to go live to meet production schedules. The moment an operator logs a live production order, Milestone M4 is deemed accepted and the warranty clock starts. There is no cure period, no "substantial acceptance" standard, and no distinction between a pilot run and full production. If the Software has latent defects that only manifest under full production load (e.g., during a peak season), Proudert may have already "accepted" M4 and be well into the warranty period before the issue is identified.

**Recommended fix:**
- Negotiate a "stabilization period" of 30–60 days post-Go-Live during which the warranty does not begin to run, or during which deemed acceptance of M4 is suspended.
- Clarify that "first uses the Software in production" means sustained production use (e.g., 5 consecutive production days), not a single test order.
- Add a provision that latent defects not discoverable through reasonable UAT do not trigger deemed acceptance.

---

## Issue 11: No Price Protection or Cap on Future Fee Increases

**Where:** Agreement §5.1 (tiered fees), §13.2 (renewal at "then-current list fees"), Side Letter §2 (12% discount off list).

**Why it matters:** During the Initial Term, fees are fixed by the tier schedule. But there is no cap on how much Vopein can increase "list fees" at renewal. The 12% Side Letter discount is a percentage, not a fixed dollar amount, so it provides no absolute protection. If Vopein raises list fees 30% at the first renewal, Proudert's cost jumps from ~$163,680 (Base Tier, discounted) to ~$212,784—a 30% increase—despite the discount still applying. There is no most-favored-customer clause, no CPI cap, and no right to benchmark against Vopein's other customers.

**Recommended fix:**
- Negotiate a fee-increase cap for Renewal Terms (e.g., not to exceed the greater of 3% or CPI per year).
- Add a most-favored-customer provision: if Vopein offers a lower effective rate to a similarly situated textile manufacturer, Proudert is entitled to the same rate.
- Alternatively, lock fees for the Initial Term plus one Renewal Term in exchange for a longer commitment or a larger upfront payment.

---

## Issue 12: Transition Assistance Is Limited and One-Sided

**Where:** Agreement §13.6: "At Licensee's request, and for up to ninety (90) days after expiration or termination, Licensor shall provide reasonable transition assistance at its then-current professional services rates." Section 8.4: Vopein shall "cooperate in exporting Licensee Data in a standard, machine-readable format" and then delete it.

**Why it matters:**
- 90 days may be insufficient for a full MES transition in a continuous-manufacturing environment. Reweaving production workflows, retraining operators, and validating quality data in a new system can take 6–12 months.
- "Reasonable transition assistance" is undefined. Vopein is not obligated to provide API documentation, data dictionaries, configuration files, or training for the replacement vendor's personnel.
- "At its then-current professional services rates" means Proudert pays full price for transition work—no discount, no capped rate.
- The data export obligation in §8.4 is limited to "cooperate in exporting" and "standard, machine-readable format." There is no obligation to export in a format compatible with a specific replacement system, no obligation to provide historical data beyond a certain period, and no service-level for the export.

**Recommended fix:**
- Extend the transition assistance period to 180 days.
- Define "reasonable transition assistance" to include: data export in CSV/JSON/XML with full data dictionary, configuration file delivery, up to 40 hours of knowledge-transfer sessions for the replacement vendor, and reasonable cooperation with data validation.
- Cap transition assistance rates at the rates in SOW 1 §8.4 (or a stated fixed rate).
- Add an obligation to retain data for a specified period (e.g., 12 months post-termination) to allow for post-transition data reconciliation.

---

## Issues Requiring Additional Information

| # | Issue | What I Need |
|---|---|---|
| 1 | Executed Schedule B | Copy of the fully executed Agreement with all attached schedules, or confirmation that no Schedule B was attached. |
| 2 | Authorized User count | Current and projected numbers: employees with credentials, contractors with access, cameras/sensor stations deployed or planned, and any interface-based access. |
| 3 | SOW 1 status | Has SOW 1 been fully performed and accepted? Are all milestones paid? This affects the urgency of the governing-law conflict (Issue 3) and the deemed-acceptance issue (Issue 10). |
| 4 | Renewal date tracking | Confirm the Initial Term end date (March 2, 2029) and whether any internal calendar has been set for the non-renewal notice window. |
| 5 | Other facilities | Does Proudert operate or plan to operate MES/QI software at any facility other than Greenville? This is critical to assessing the Side Letter exclusivity risk (Issue 4). |
| 6 | Vision Inspection Module deployment | How many cameras/sensor stations are currently deployed or planned? When was first production use (triggering the 12-month warranty under Amendment §2.6)? |

---

## Priority Ranking for Client Discussion

| Priority | Issue | Reason |
|---|---|---|
| **1** | Issue 2 – Authorized User expansion | Direct, ongoing financial impact. Could be adding $100K–$200K+/year in unanticipated fees. |
| **2** | Issue 1 – Missing Schedule B | Fundamental data-security protection gap. Regulatory and operational risk. |
| **3** | Issue 7 – Liability cap / consequential damages bar | Limits Proudert's recovery in the worst-case scenarios (data breach, production stoppage). |
| **4** | Issue 6 – Renewal notice window | Time-sensitive. If missed, Proudert is locked in for 3 more years. |
| **5** | Issue 4 – Exclusivity scope | Operational constraint on Proudert's freedom to deploy technology at other sites. |
| **6** | Issue 3 – Governing law conflict | Creates litigation strategy complications; moderate urgency depending on SOW 1 status. |
| **7** | Issues 5, 8, 9, 10, 11, 12 | Important but addressable in the next amendment or renewal cycle. |

---

*End of memo.*