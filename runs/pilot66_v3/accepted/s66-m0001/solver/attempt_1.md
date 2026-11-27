# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Rekaind Vertical Services, Inc. – Review of Velert Systems Software License Agreement File: Issues and Recommended Fixes

---

## I. CRITICAL: Termination Notice Appears 17 Days Outside the Contractual Window

**Where:** Service Level Schedule § 4.2; Rekaind Notice Letter §§ 2.3, 3.1 (dated October 21, 2026)

**Issue:** Section 4.2 of the Service Level Schedule requires Rekaind to deliver written notice of termination for Chronic Availability Failure "within thirty (30) days after delivery of the Service Report for the third consecutive calendar month in which Platform Availability was below 99.5%." The August 2026 Service Report—the third consecutive failing month—was delivered on **September 4, 2026** (Notice Letter § 2.3; confirmed by the table in § 2.2). Thirty days after September 4 is **October 4, 2026**. The termination notice is dated and was delivered on **October 21, 2026**, which is 47 days after delivery of the August Service Report—17 days beyond the contractual deadline.

**Why it matters:** If Velert challenges the termination as untimely, a court applying the plain language of § 4.2 could hold that Rekaind's termination right has lapsed. This would leave Rekaind locked into the Order Form through at least March 2, 2028 (end of the Initial Order Term), with no refund of prepaid Year 2 fees and no avoidance of the 7% renewal-pricing mechanism. Given that the Order Form's governing-law clause points to Ohio (see Issue II below), the question would be decided under Ohio contract-interpretation principles, which generally enforce express time limits strictly.

**Recommended fix:**
- Immediately assess whether Velert has acknowledged or objected to the notice. If Velert has not yet responded, consider whether a practical or estoppel argument is available (e.g., Velert's own remediation plan of August 19, 2026 acknowledged the chronic failure; Velert's operational contacts were copied on the notice).
- In parallel, prepare a fallback termination under **SLA § 12.4** (material breach with 30-day cure). The three consecutive months of sub-99.5% availability, including repeated Severity 1 incidents affecting alert delivery, constitute a material breach of SLA § 2.1 and SLS § 2.1. A § 12.4 notice would require a new 30-day cure period, pushing any effective termination to approximately mid-December 2026, but it would not be subject to the § 4.2 timing constraint.
- If Velert disputes timeliness, the governing-law conflict (Issue II) becomes a threshold litigation issue. Rekaind should be prepared to argue that the SLS timing requirement is a condition precedent to the § 12.6 remedy but not to the § 12.4 remedy.

---

## II. Conflict in Governing Law and Venue: Ohio vs. Delaware

**Where:** Order Form § 7.1–7.2 (Ohio law; Franklin County, Ohio venue) vs. SLA § 15.1–15.2 (Delaware law; Wilmington, Delaware venue); SLA § 15.4 (Order of Precedence)

**Issue:** The Order Form and the SLA body specify different governing laws and forums. Under the Order of Precedence in SLA § 15.4, the Order Form ranks above the Agreement body, so **Ohio law and Franklin County venue** should control. However, the SLA was drafted with Delaware as the intended forum, and the Side Letter (which ranks highest in the precedence order) is silent on governing law. The result is an avoidable ambiguity that will generate a threshold motion in any dispute.

**Why it matters:** Every dispute—including the timeliness of the termination notice, the refund calculation, and any indemnification claim—will require a court to decide which law and forum apply first. This delays resolution and increases costs. For Rekaind (a Pennsylvania corporation), neither Ohio nor Delaware is home, but Ohio is where Velert is headquartered, making service and discovery somewhat more practical.

**Recommended fix:**
- In any correspondence with Velert regarding the termination, Rekaind should not concede the governing-law question but should proceed on the assumption that Ohio law applies (per the Order of Precedence).
- If the relationship were to continue (e.g., if the termination is held invalid), negotiate an amendment or side letter that harmonizes the governing-law and venue provisions across all documents. A single forum—preferably Pennsylvania or Delaware—would reduce future friction.

---

## III. Exclusivity Clause Covers All of Rekaind's Equipment Worldwide, Not Just the 1,140 Licensed Units

**Where:** SLA § 3.4 (Exclusivity); SLA § 1.6 (definition of "Covered Equipment"); Order Form § 1.1 (Licensed Units limited to PA, NJ, DE)

**Issue:** Section 3.4 prohibits Rekaind from licensing, using, or developing any other remote-monitoring, condition-monitoring, dispatch, or work-order software "for any **Covered Equipment**." "Covered Equipment" is defined in § 1.6 as "any equipment serviced by Licensee or any of its Affiliates **anywhere in the world**." This is not limited to the 1,140 Licensed Units in the Order Form. If Rekaind services, for example, 4,000 units across the Mid-Atlantic, it is contractually barred from using any competing monitoring platform for the other 2,860 units—even though those units generate no fee to Velert and are not part of the subscription.

The restriction continues "during the Term and for any period during which any Order Form remains in effect." Because the Order Form remains in effect until the Termination Date (November 20, 2026), Rekaind is currently bound by this worldwide exclusivity.

**Why it matters:** This clause effectively gives Velert exclusive-dealing rights over Rekaind's entire maintenance business, not just the subset of units under the LiftSense subscription. It prevents Rekaind from piloting or deploying an alternative platform for any unit in its portfolio during the remaining term, which severely constrains transition planning. If the termination is held invalid (see Issue I), this restriction could bind Rekaind for another 17+ months.

**Recommended fix:**
- Before November 20, 2026, Rekaind should avoid any act that could be characterized as "licens[ing], us[ing], or develop[ing]" alternative monitoring software for any unit in its portfolio, even in a proof-of-concept or evaluation capacity.
- If the termination is challenged, negotiate a carve-out or standstill: Velert agrees not to enforce § 3.4 as to units outside the Licensed Units in exchange for Rekaind's agreement to the Termination Date.
- In any replacement agreement, ensure the exclusivity (if any) is limited to the specific units under subscription, not the licensor's entire customer base.

---

## IV. TEO and Cyber Policies Do Not Name Rekaind as Additional Insured; Claims-Made Expiration Creates a Coverage Gap After April 1, 2027

**Where:** SLA § 13.1(b)–(c) (required coverages); SLA § 13.2 (additional insured only under §§ 13.1(a) and (d)); Certificate of Insurance § 5 (TEO: Addl Insd "N"; Cyber: Addl Insd "N"); Certificate § 10.2, § 11.2 (claims-made; policy period 04/01/2026–04/01/2027); SLA § 13.1 (two-year post-termination insurance obligation)

**Issue (a) – No additional insured status under TEO/Cyber:** The SLA requires Velert to name Rekaind as additional insured only under the CGL (§ 13.1(a)) and Umbrella (§ 13.1(d)) policies. The certificate confirms this: CGL and Umbrella show "Y" for additional insured; TEO and Cyber show "N." For a software platform, the most probable claims scenarios—failure to deliver alerts, data breach, business interruption—fall under the TEO and Cyber policies, not the CGL. Rekaind therefore has no direct right to make a claim under the policies most likely to respond to a Platform failure.

**Issue (b) – Claims-made expiration:** Both the TEO and Cyber policies are claims-made. The current policy period ends **April 1, 2027**. The SLA requires Velert to maintain insurance for two years after termination, i.e., through **November 20, 2028**. If Velert does not renew the claims-made policy or purchase the optional 36-month extended reporting period (ERP) (Certificate § 10.5; endorsement MSI-ERP-36 listed in § 17.5), any claim first asserted after April 1, 2027—even if arising from the June–August 2026 incidents—would be uninsured. A building owner could sue Rekaind in 2027 or 2028 for an entrapment that occurred during the August 2026 alert-delivery failure; Rekaind would then seek indemnification from Velert under SLA § 10.2 (as renumbered by the Side Letter), but Velert's insurance would not respond.

**Why it matters:** Rekaind's practical recovery for the most serious incidents (alert failures, data breaches) depends on Velert's TEO and Cyber insurance. If that insurance lapses or has no ERP, Velert's ability to indemnify Rekaind is limited to its own balance sheet. The $100,000 retention on each TEO/Cyber claim (Certificate §§ 10.2, 11.2) further reduces the insurance available for smaller claims.

**Recommended fix:**
- In the response to the notice letter (or in a separate letter), require Velert to confirm in writing, within 10 Business Days, that it will either (a) renew the TEO and Cyber policies through at least November 20, 2028, or (b) purchase the 36-month ERP under endorsement MSI-ERP-36 effective April 1, 2027, and deliver a certificate evidencing the ERP.
- Request that Velert add Rekaind as additional insured under the TEO and Cyber policies for the remainder of the required insurance period. If Velert resists, negotiate a provision requiring Velert to maintain the policies with a "cut-through" or "direct action" endorsement permitting Rekaind to claim directly.
- Consider whether the $100,000 retention is consistent with the indemnification obligation. The SLA indemnity is not subject to the insurance retention; Velert must indemnify Rekaind even for the first $100,000 of a claim. Confirm this understanding in writing.

---

## V. Refund Calculation in Notice Letter Overstates by One Day

**Where:** Rekaind Notice Letter § 6.2

**Issue:** The notice letter calculates the unexpired portion of Year 2 as "the 103 days from November 21, 2026 to March 2, 2027" and derives a refund of $115,811.51. The correct count is **102 days**:

| Month | Days |
|---|---|
| November 21–30 | 10 |
| December 1–31 | 31 |
| January 1–31 | 31 |
| February 1–28 (2027) | 28 |
| March 1–2 | 2 |
| **Total** | **102** |

The annual billing period is 365 days (March 3, 2026 – March 2, 2027). The correct refund is $410,400 × 102/365 = **$114,687.12**, not $115,811.51. The overstatement is $1,124.39.

**Why it matters:** While the dollar amount is modest, an arithmetic error in a formal notice of termination undermines Rekaind's credibility and gives Velert an easy point of contention. If Velert disputes the refund, it will start with the number that is wrong.

**Recommended fix:**
- Send a supplemental letter or email correcting the day count to 102 and the refund to $114,687.12, with the reconciliation reserved for units added or removed under SLA § 2.4 (as the original letter already provides). Do not wait for Velert to raise the error.

---

## VI. Limitation of Liability and Exclusion of Consequential Damages Cap Rekaind's Recovery for Business Loss

**Where:** SLA § 11.3 (12-month fee cap); SLA § 11.5 (consequential damages exclusion); SLS § 3.3 (maximum service credits 40% of Monthly Fee)

**Issue:** Rekaind's total recovery for Velert's failure to meet the availability commitment is limited to:
- Service credits of up to 40% of the Monthly Fee per month (i.e., up to $13,680/month); plus
- The § 11.3 liability cap of $410,400 (12 months' fees) for any other damages; with
- Consequential damages (lost profits, lost contracts, reputational harm) excluded under § 11.5, except for the narrow § 11.4 exceptions (indemnification, confidentiality/data-security breach, fraud/willful misconduct).

If the Platform's unavailability causes Rekaind to lose a building maintenance contract (e.g., a building owner terminates because of repeated entrapment-monitoring gaps), that lost revenue is a consequential damage and is not recoverable. Rekaind's maximum recovery for the June–August 2026 failures, absent a third-party bodily-injury claim, is approximately $13,680 × 3 months + $410,400 cap = roughly $451,440, and only if the losses are direct rather than consequential.

**Why it matters:** For a dispatch-and-monitoring platform on which Rekaind's entire operational model depends, the remedy structure is misaligned with the risk. The service credits are a small fraction of the annual fee ($13,680 max vs. $34,200 Monthly Fee), and the consequential-damages exclusion means Rekaind bears the business-risk of Platform failure.

**Recommended fix:**
- In the current termination posture, this issue is largely moot for the June–August period (Rekaind is exiting). However, if Rekaind enters a replacement agreement or renegotiates with Velert, it should:
  - Negotiate a higher service-credit ceiling (e.g., 100% of Monthly Fee for availability below 97%);
  - Carve out "loss of contracts with building owners directly attributable to Platform unavailability" from the consequential-damages exclusion;
  - Increase the § 11.3 cap to 24 months' fees or a fixed dollar amount tied to the size of the Licensed Unit portfolio.
- For the current termination, ensure the notice letter (which it does, in § 15.1) expressly reserves rights under § 10 for third-party claims, because the § 11.4(a) exception removes the cap and consequential-damages exclusion for indemnification obligations.

---

## VII. Potential Breach of Side Letter Firmware Validation Requirement

**Where:** Side Letter § 3.5; Notice Letter § 2.4(b) (July 2026: "delay in alert delivery for Licensed Units running a particular LS-G4 Gateway firmware version")

**Issue:** Side Letter § 3.5 requires that "Licensor shall not deploy any firmware update to Connected Devices installed on Licensed Units unless the update has first been validated in Licensor's test environment against each controller make and model identified in the unit register." The July 2026 Service Report records a delay in alert delivery specifically tied to "a particular LS-G4 Gateway firmware version." If the delayed firmware was deployed without validation against all controller makes and models in the unit register, Velert breached § 3.5.

**Why it matters:** A breach of the Side Letter's firmware validation requirement is independent of the availability failure. It could:
- Support an argument that the Chronic Availability Failure was caused by Velert's own non-compliance, strengthening Rekaind's position if the § 4.2 timing is challenged;
- Constitute a separate material breach under SLA § 12.4, providing an alternative termination ground not subject to the § 4.2 30-day window;
- Support a claim that Velert's conduct was willful or reckless, which would fall within the § 11.4(c) exception to the liability cap and consequential-damages exclusion.

**Recommended fix:**
- Request from Velert, under the document-preservation demand in Notice Letter § 12.2, the firmware deployment logs, validation test records, and change-management tickets for all LS-G4 firmware updates deployed between January 1, 2026 and the Termination Date.
- If the records confirm deployment without full validation, issue a supplemental notice of material breach under SLA § 12.4, citing Side Letter § 3.5, with a 30-day cure period. This creates a second, independent termination right that is not subject to the SLS § 4.2 timing constraint.

---

## VIII. Lease: Security Deposit Formula Produces a Different Figure Than the Stated Amount

**Where:** Dispatch Center Office Lease § 1.1 (stated Security Deposit: $33,330.83); § 6.1 (formula)

**Issue:** Section 6.1 defines the Security Deposit as "one month of Base Rent at the Lease Year 7 rate plus an additional amount equal to one half of one month of Base Rent at the Lease Year 1 rate." Using the figures in § 1.2:
- Lease Year 7 monthly Base Rent: $23,197.10
- ½ × Lease Year 1 monthly Base Rent: ½ × $19,997.50 = $9,998.75
- Formula result: $23,197.10 + $9,998.75 = **$33,195.85**

The stated Security Deposit in § 1.1 is **$33,330.83**, a difference of $134.98.

**Why it matters:** This is a minor discrepancy, but if the lease is ever the subject of a dispute (e.g., at surrender, when the deposit is returned under § 6.3), the formula and the stated amount will produce different results. The § 1.1 summary provision states that "if a basic lease provision conflicts with another provision of this Lease, the other provision governs"—so § 6.1 (the formula) would control over § 1.1 (the stated figure). Rekaind may have overpaid the deposit by $134.98.

**Recommended fix:**
- Confirm with the property manager whether the actual deposit collected was $33,330.83 or $33,195.85. If the former, request a credit or refund of the $134.98 difference. This is low-priority but easy to raise in the next lease-related communication.

---

## IX. Aggregated Data: Competitive Risk from Velert's Use of Rekaind's Equipment Data

**Where:** SLA § 8.4 (Aggregated Data); SLA § 1.7 (Customer Data definition)

**Issue:** Section 8.4 permits Velert to compile and use statistical and performance data derived from Equipment Data to "improve the Platform and its predictive models." The restriction is that the data must be de-identified and aggregated so it "does not identify Licensee, any of Licensee's customers, any building, or any individual," and Velert "shall not disclose Aggregated Data to third parties in any form that identifies Licensee or permits a third party to determine Licensee's customer portfolio or pricing."

In the elevator maintenance industry, the number of independent contractors with portfolios of 1,000+ units in the Mid-Atlantic is small. Even de-identified and aggregated data—fault rates by unit type, door-cycle frequencies by region, entrapment rates by controller manufacturer—could reveal Rekaind's portfolio characteristics to Velert's other customers (some of which may be Rekaind's competitors). The predictive models Velert builds using Rekaind's data will make the Platform more effective for those competitors.

**Why it matters:** Rekaind is paying $410,400/year for the Platform while simultaneously providing the training data that makes the Platform better for Velert's other clients. The § 8.4 restrictions are narrow (no identification, no portfolio/pricing disclosure) but do not prevent Velert from using the data to improve product features that benefit competitors.

**Recommended fix:**
- In the data-return and deletion process (Notice Letter § 9), expressly confirm that Velert will delete all raw Equipment Data and Customer Data and will not retain any dataset from which Rekaind's portfolio could be reverse-engineered, even in aggregated form.
- If Rekaind enters a replacement agreement with another vendor, negotiate a data-use provision that is more restrictive than § 8.4—for example, prohibiting the vendor from using the data to improve predictive models for other customers in the same geographic market or equipment segment.
- Consider whether the § 8.4 Aggregated Data right survives termination. Section 12.9 (Survival) does not list § 8.4, and § 8.7 requires deletion after the 60-day return window. The Side Letter is silent. Rekaind should confirm in writing that Velert's right to use Aggregated Data ends at the Termination Date and that no Aggregated Data derived from Rekaind's Equipment Data will be used after that date.

---

## X. Unit Removal: Minimum Commitment and Fee-Cessation Timing Limit Flexibility

**Where:** SLA § 2.4(b); Order Form § 1.5 (minimum 1,000 units)

**Issue:** Two constraints limit Rekaind's ability to reduce its unit count:
1. **Minimum commitment:** Rekaind cannot remove units below 1,000 (Order Form § 1.5). With 1,140 Licensed Units, Rekaind can remove at most 140 units.
2. **Fee cessation timing:** Even for permitted removals, "Fees for a removed unit cease from the start of the next annual billing period after the removal takes effect" (SLA § 2.4(b)). If Rekaind removes a unit in June 2026, it continues to pay for that unit until March 3, 2027—the start of the next annual billing period.

**Why it matters:** During the Initial Order Term, Rekaind is effectively locked in at 1,000+ units with annual-in-advance billing. If Rekaind loses building contracts mid-year, it cannot reduce its fee obligation until the next billing anniversary. This is a cash-flow and flexibility concern, though it is less acute now that Rekaind is terminating the Order Form.

**Recommended fix:**
- For the current termination, this issue is moot (the entire Order Form is ending). For any replacement agreement, negotiate:
  - A lower minimum commitment or no minimum;
  - Monthly (not annual) fee cessation for removed units;
  - A right to remove units on 30 days' notice without waiting for the next billing period.

---

## XI. Cyber Policy: 8-Hour Waiting Period for Network/Business Interruption

**Where:** Certificate of Insurance § 11.2 (Waiting Period: 8 hours)

**Issue:** The Cyber Liability policy includes a **8-hour waiting period** for Network and Business Interruption coverage. This means that if a cyber event (e.g., ransomware, DDoS) causes the Platform to be unavailable for less than 8 hours, Velert's cyber insurance will not respond to the business-interruption loss. The June 16, 2026 data-ingestion node failure lasted approximately 4 hours and 40 minutes (Notice Letter § 2.4(a)). Had that been caused by a cyber event rather than a hardware/software fault, the cyber policy would not have covered the interruption.

**Why it matters:** For a dispatch platform monitoring passenger elevators, even a 4-hour interruption is operationally severe. The 8-hour waiting period creates a gap in Velert's insurance that could reduce its ability to indemnify Rekaind for shorter interruption events. However, the TEO policy (which covers "failure to perform") does not appear to have the same waiting period, so the gap may be narrower than it first appears.

**Recommended fix:**
- Confirm with Velert's broker (Scioto Risk Partners) whether the TEO policy's "failure to perform" coverage responds to interruption events of less than 8 hours duration. If it does, the cyber waiting period is less concerning.
- In any replacement agreement, require the vendor's cyber policy to have a waiting period of no more than 1 hour for network interruption, or no waiting period at all for the alert-delivery function.

---

## XII. Surplus Lines Status of TEO and Cyber Insurer

**Where:** Certificate of Insurance § 18.1; § 4 (Insurer D: Meridian Specialty Insurance Company, A.M. Best A, FSC XIV)

**Issue:** The TEO and Cyber policies are written on a **surplus lines** basis through an Ohio surplus lines broker. Surplus lines policies are **not protected by the Ohio Insurance Guaranty Association** (or any state guaranty fund). If Meridian Specialty becomes insolvent, policyholders have no guaranty-fund backstop.

**Why it matters:** While Meridian is currently rated A (Excellent) with Financial Size Category XIV (total assets of approximately $1–2 billion), the absence of guaranty-fund protection means that in a worst-case insurer-insolvency scenario, Velert's $5M TEO and $5M Cyber coverage could be impaired. This is a secondary risk (insurer insolvency on top of a Platform failure) but worth noting given that these are the policies most relevant to Rekaind's claims.

**Recommended fix:**
- Monitor Meridian Specialty's A.M. Best rating annually. If the rating drops below A- or the FSC drops below X, require Velert to replace the insurer or add an admitted carrier.
- This is a low-priority item given the current rating, but it should be on the risk-management checklist for the two-year post-termination insurance period.

---

## XIII. Notice Letter: Cancellation of Outstanding Device Order Lacks Express Contractual Basis

**Where:** Notice Letter § 5.3; SLA § 4.2(c) (title passes on delivery); SLA § 12.7 (effect of termination)

**Issue:** The notice letter cancels Velert's undelivered replenishment order for LS-G4 Gateways and LS-ESC Escalator Sensor Packages (placed September 28, 2026). The SLA does not contain an express provision addressing the status of pending device orders upon termination. Section 12.7 lists the effects of termination (license termination, fee payment, return of Confidential Information, deactivation) but does not mention open purchase orders for hardware.

Rekaind's position rests on § 4.2(c) (title passes on delivery) and the general principle that a termination ends the contractual basis for future performance. However, Velert could argue that the September 28 order was a separate, binding commitment that survives termination as an accrued obligation.

**Why it matters:** The undelivered devices represent a six-figure exposure (at the Order Form § 4.2 prices: even 100 gateways at $485 + 50 sensor packages at $615 = $79,250). If Velert ships the devices and invoices Rekaind, Rekaind will be in a dispute over whether it must accept and pay.

**Recommended fix:**
- The notice letter already states that Rekaind will return any in-transit devices "unopened at Velert's cost." This is reasonable. If Velert objects, Rekaind should respond by citing § 4.2(c) (no title passed because no delivery occurred) and the general effect-of-termination provision (§ 12.7), and by noting that the Order Form is the source of the pricing and the order was placed under it.
- If the devices are already in transit, arrange for interception or refusal at the warehouse (4100 Robbins Avenue) and document the refusal.

---

## XIV. Side Letter: Expanded IP Indemnification Now Covers Canada, EU, UK, and Hosting/Manufacturing Jurisdictions

**Where:** Side Letter § 2.2(a) (replacing SLA § 10.1(a))

**Issue:** The original SLA § 10.1(a) covered IP infringement "in the United States." The Side Letter expands this to "the United States, Canada, the European Union, the United Kingdom or any jurisdiction in which any component of the Platform is hosted or any Connected Device is manufactured."

**Why it matters:** This is favorable to Rekaind and should be cited in any IP-related dispute. However, it also means that if a Connected Device is manufactured in, say, Mexico or China, Velert's IP indemnification extends to those jurisdictions. This broadens Velert's exposure and may make Velert more risk-averse in future negotiations. For Rekaind's current purposes, the key point is that the indemnification is broader than the original SLA, and any analysis of Velert's indemnification obligations should use the Side Letter version, not the original.

**Recommended fix:** No action required. This is a benefit. Ensure that any internal summary of the indemnification provisions references the Side Letter's expanded scope, not the original SLA text.

---

## XV. SLA § 5.7 / SLS § 6.1: Severity 1 Classification of Alert-Defect Incidents

**Where:** SLA § 5.7; SLS § 6.1 (Severity 1 definition); SLS § 2.4 (last paragraph: alert-delivery Downtime is not Excluded Downtime under § 2.4(a))

**Issue:** The agreement provides strong protections for alert-delivery failures:
- Any defect preventing or delaying entrapment/passenger-alarm alerts is automatically a **Severity 1** (SLA § 5.7; SLS § 6.1 last sentence).
- Downtime of the alert-delivery Core Function is **not** Excluded Downtime even during Scheduled Maintenance, unless Velert maintains the secondary alert-routing path (SLS § 2.4, last paragraph).
- The secondary alert-routing path (SMS + automated voice) must be tested quarterly (SLS § 5.3).

The August 2026 incidents (two occasions of >30 minutes' alert-delivery Downtime affecting ≥5% of units) triggered both the standard availability service credit and the additional alert-delivery credit under SLS § 3.2. The notice letter correctly claims both.

**Why it matters:** These provisions confirm that the most serious failures (alert delivery) receive the highest severity classification and are carved out of exclusions. This supports Rekaind's position that the June–August 2026 failures were not marginal or excusable. If Velert argues that some of the Downtime should be excluded (e.g., as Scheduled Maintenance or Force Majeure), the SLS § 2.4 carve-out for alert-delivery Downtime is Rekaind's strongest rebuttal.

**Recommended fix:** No action required for the current termination. In any dispute over Excluded Downtime, cite SLS § 2.4 (last paragraph) and § 5.3.

---

## XVI. Order Form § 3.4: Year 1 Credit for Delayed Connected Devices – Potential Unclaimed Amount

**Where:** Order Form § 3.4 (last sentence)

**Issue:** The Order Form provides that if a Licensed Unit is not connected to the Platform in Year 1 "because of a delay in delivery of Connected Devices attributable to Licensor," Velert must issue a credit of 50% of the prorated per-unit subscription fee for each full month of delay. The notice letter does not reference any such credit. If there were device-delivery delays in Year 1 (March 2025 – March 2026) attributable to Velert, Rekaind may be entitled to an additional credit that has not been claimed.

**Why it matters:** The per-unit fee is $360/year = $30/month. A 50% credit = $15/unit/month. If, for example, 100 units were delayed by an average of 3 months due to Velert's device-delivery failures, the unclaimed credit would be 100 × $15 × 3 = $4,500. The actual amount depends on the implementation record.

**Recommended fix:**
- Review the implementation status reports (required by Side Letter § 5.1) and the delivery records for Year 1 to identify any units that were not connected due to Velert-attributable delays.
- If any are found, include a claim for the § 3.4 credit in the reconciliation with Velert (the notice letter already reserves the right to reconcile under § 6.2).
- This is a secondary claim and should not delay the primary termination and refund process.

---

## XVII. Lease: 24-Hour Access and Dispatch Center Resilience Are Adequate but Cost-Intensive

**Where:** Office Lease § 7.2 (24-hour access); § 8.2 (after-hours HVAC at $65/hr/zone); § 9.4 (generator connection, 150 kW, $450/month + fuel)

**Issue:** The lease supports Rekaind's 24/7 dispatch operations with:
- Unrestricted after-hours access to the Premises, garage, and elevators (§ 7.2);
- A 150 kW emergency generator connection (§ 9.4);
- Supplemental cooling for the server/telecom room (§ 8.3);
- Redundant telecom entrances (§ 3.5(c)).

However, the after-hours HVAC cost is significant. Building Hours end at 7:00 p.m. weekdays and 1:00 p.m. Saturdays. The dispatch center operates 24/7. After-hours HVAC is needed approximately 63 hours per week at $65/hour = **$4,095/week ≈ $17,800/month**. This is a fixed operational cost that will continue regardless of the Velert termination.

**Why it matters:** This is not a legal defect, but it is a material cost consideration for Rekaind's transition planning. The dispatch center lease runs to September 30, 2030 (with a 5-year renewal option). Rekaind is committed to this space and its associated after-hours costs for at least four more years. The transition to a new monitoring platform must be planned within the constraints of this existing infrastructure.

**Recommended fix:**
- No legal action required. Flag to Rekaind's operations team that the after-hours HVAC cost is a fixed transition-period expense and should be included in the budget for the replacement platform's implementation.
- The 150 kW generator connection should be verified as sufficient for the replacement platform's dispatch-center load. If the new system requires more power, a lease amendment under § 10.1 (alterations) would be needed.

---

## XVIII. SLA § 12.8: Transition Assistance Available but Not Yet Requested

**Where:** SLA § 12.8; Notice Letter § 10.1

**Issue:** Section 12.8 provides up to 90 days of transition assistance (continued Platform access at prorated fees, data export help, Connected Device protocol information) if Rekaind requests it "before or within thirty (30) days after expiration or termination." The notice letter (§ 10.1) states that Rekaind "does not currently request" transition assistance but "may still make a request."

The 30-day window after the November 20, 2026 Termination Date closes on **December 20, 2026**.

**Why it matters:** If Rekaind's phased regional cutover (described in Notice Letter § 8.2) is not complete by November 20, it may need the Platform to remain active for certain regions. Without a § 12.8 request, Velert is entitled to deactivate all Platform services on the Termination Date (§ 12.7(d)). If any region is not yet cut over, those units would lose monitoring.

**Recommended fix:**
- If any regional cutover is not confirmed complete by November 15, 2026, Rekaind should submit a written § 12.8 request before December 20, 2026, specifying the Licensed Units that require continued coverage and the anticipated transition period (up to 90 days).
- The notice letter's phased-cutover protocol (§ 8.2) requires Velert not to deactivate any region until Rekaind confirms in writing that the cutover is complete. This should be sufficient protection through the Termination Date, but a § 12.8 request provides a contractual safety net for the period after.

---

## XIX. SLA § 14.2: Velert May Assign Without Rekaind's Consent

**Where:** SLA § 14.2

**Issue:** Velert may assign the Agreement (and all Order Forms) without Rekaind's consent to an Affiliate or to a successor in a merger, asset sale, or change of control. Rekaind receives only 30 days' notice after the assignment takes effect. There is no right to terminate upon assignment.

**Why it matters:** If Velert is acquired by a competitor of Rekaind's other software vendors, or by a company with a different service-quality culture, Rekaind has no contractual exit. The assignment could also complicate the insurance analysis (Issue IV): the new entity would need to assume the insurance obligations, and the claims-made policies may not automatically follow the assignment.

**Recommended fix:**
- In the current termination posture, this is of limited practical importance (the Order Form is ending). However, if the termination is held invalid and the Order Form continues, monitor for any change-of-control event at Velert. If one occurs, assess whether the new owner's financial condition and insurance program satisfy the SLA § 13 requirements.
- For any replacement agreement, negotiate a termination right upon assignment to a competitor or upon a change of control, or at minimum a right to require the assignee to provide evidence of equivalent insurance and financial capacity.

---

## XX. Certificate of Insurance: Notice of Cancellation Is 30 Days, But 10 Days for Non-Payment

**Where:** Certificate § 15.1

**Issue:** The insurers will give Rekaind 30 days' notice of cancellation, non-renewal, or material reduction—except for cancellation for **non-payment of premium**, where notice is only **10 days**. SLA § 13.2 requires Velert to give Rekaind "at least thirty (30) days' prior written notice of any cancellation, non-renewal or material reduction of the required coverage."

**Why it matters:** If Velert fails to pay its insurance premium and the insurer cancels with only 10 days' notice, Velert may be unable to meet its 30-day notice obligation to Rekaind under § 13.2. In that scenario, Rekaind could learn of the coverage gap on short notice, leaving it vulnerable during the two-year post-termination period.

**Recommended fix:**
- In the insurance-confirmation letter (see Issue IV), ask Velert to confirm that it will maintain sufficient premium reserves or a premium-payment arrangement that eliminates the risk of non-payment cancellation. Alternatively, require Velert to notify Rekaind immediately (not waiting for the insurer's 10-day notice) if it becomes aware of any premium delinquency.

---

## Summary of Priority Actions

| Priority | Issue | Action | Deadline |
|---|---|---|---|
| **1** | Late termination notice (Issue I) | Assess Velert's response; prepare § 12.4 fallback | Immediate |
| **2** | Insurance gap – claims-made expiration (Issue IV) | Demand written confirmation of renewal/ERP | 10 Business Days |
| **3** | Refund calculation error (Issue V) | Send correcting supplemental letter | 5 Business Days |
| **4** | Firmware validation breach (Issue VII) | Request deployment logs; prepare § 12.4 notice if confirmed | 10 Business Days |
| **5** | Exclusivity constraint (Issue III) | Cease all evaluation of alternative platforms for any unit | Immediate |
| **6** | Transition assistance window (Issue XVIII) | Monitor cutover progress; submit § 12.8 request if needed | By Dec 20, 2026 |
| **7** | Aggregated Data survival (Issue IX) | Confirm in writing that § 8.4 rights end at termination | With data-deletion confirmation |
| **8** | Governing law conflict (Issue II) | Proceed on Ohio-law assumption; do not concede | Ongoing |