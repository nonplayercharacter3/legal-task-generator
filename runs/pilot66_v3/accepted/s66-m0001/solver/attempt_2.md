# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current]
**RE:** Rekaind Vertical Services, Inc. – Review of Velert Systems Software License Agreement Package: Issues and Recommended Fixes

---

## Summary

I have reviewed all seven documents in the matter folder: the Software License Agreement (8 pp.), the Service Level Schedule (4 pp.), Order Form No. 001 (4 pp.), Rekaind's Notice of Termination dated October 21, 2026 (4 pp.), the Side Letter dated May 12, 2025 (4 pp.), the Dispatch Center Office Lease (6 pp.), and Velert's Certificate of Insurance dated November 2, 2026 (5 pp.). I identify fourteen issues below, ordered by materiality. The first issue is critical and requires immediate attention.

---

## Issue 1 – Termination Notice Appears 17 Days Outside the Contractual Window

**Where:** Service Level Schedule §4.2; Rekaind Notice Letter §§2.3, 3.1, 4.1

**The problem.** Section 4.2 of the Service Level Schedule requires that a termination notice for Chronic Availability Failure be delivered "within thirty (30) days after delivery of the Service Report for the third consecutive calendar month in which Platform Availability was below 99.5%." The Notice Letter confirms (at §2.3) that the August 2026 Service Report—the report for the third consecutive failing month—was delivered to Rekaind on September 4, 2026. Thirty days after September 4 is October 4, 2026. The Notice Letter is dated and delivered October 21, 2026, which is 47 days after the Service Report delivery—17 days outside the required window.

**Why it matters.** If Velert challenges the termination as procedurally defective, Rekaind risks losing its right to exit Order Form No. 001 for Chronic Availability Failure. The Initial Order Term runs to March 2, 2028 (Order Form §2.1), and the Order Form auto-renews for successive 36-month terms (Agreement §12.2). Losing the termination right would lock Rekaind in for at least another 17 months of subscription fees ($410,400/year) with no remedy short of proving material breach under Agreement §12.4 (which carries its own 30-day cure period and is a higher threshold).

**Mitigating considerations.** Velert delivered a remediation plan on August 19, 2026 (Notice Letter §2.5), and the parties' senior technical representatives met to review it on August 25, 2026. Velert's own Service Reports confirm the three consecutive failing months. One could argue equitable estoppel or waiver if Velert participated in the termination process without timely objecting, but the contractual deadline is unambiguous and no saving provision (such as a "reasonable time" fallback) appears in the SLS.

**Recommended fix.**
- Immediately assess whether Velert has acknowledged the notice or raised a timeliness objection. If Velert has not yet responded, do not draw attention to the date discrepancy.
- Prepare a fallback position under Agreement §12.4 (material breach): the pattern of three consecutive months of sub-standard availability, the missed Severity 1 resolution target on June 16 (SLS §6.2 requires 4-hour resolution; the incident lasted approximately 4 hours and 40 minutes per Notice Letter §2.4(a)), and the failure of the remediation plan to prevent a third failing month collectively constitute a material breach of the Service Level Schedule and Agreement §§5.2 and 11.2(a).
- If Velert contests the termination, consider whether a court would apply equitable tolling given Velert's own knowledge of the Chronic Availability Failure (evidenced by the remediation plan and the August Service Report). This is a weaker position but not without merit.
- Going forward, if Rekaind re-engages Velert or enters a new agreement, negotiate a longer notice window (e.g., 60 days) or a "reasonable time" standard.

---

## Issue 2 – Direct Conflict on Governing Law and Venue

**Where:** Agreement §§15.1–15.2 (Delaware law; Wilmington, Delaware courts) vs. Order Form No. 001 §§7.1–7.2 (Ohio law; Franklin County, Ohio courts)

**The problem.** The Agreement body selects Delaware law and exclusive jurisdiction in Wilmington, Delaware. The Order Form selects Ohio law and exclusive jurisdiction in Franklin County, Ohio. These are irreconcilable. Under the order of precedence in Agreement §15.4, the Order Form controls over the Agreement body, so Ohio law and Franklin County venue govern. However, the conflict itself creates uncertainty and could be the subject of a threshold litigation dispute.

**Why it matters.** Velert is an Ohio LLC headquartered in Columbus (Franklin County). Rekaind is a Pennsylvania corporation headquartered in Philadelphia. The Licensed Units are in Pennsylvania, New Jersey, and Delaware. Ohio is Velert's home forum. Rekaind would be litigating in the counterparty's backyard under the counterparty's home-state law. This increases Rekaind's cost of enforcement and may affect substantive outcomes (e.g., Ohio's approach to liquidated damages, implied covenants, or software license enforceability may differ from Delaware's).

**Recommended fix.**
- If the relationship continues (e.g., transition assistance under Agreement §12.8, or a new agreement), negotiate a conforming amendment selecting Pennsylvania law and Philadelphia venue, or at minimum a neutral forum.
- For the current termination dispute, be prepared to brief the precedence issue. Rekaind's position should be that §15.4 makes the Order Form control, but that the conflict renders both venue clauses ambiguous as to the parties' true intent, inviting application of the forum most closely related to the transaction (Pennsylvania, where Rekaind is headquartered and where the Licensed Units are predominantly located).

---

## Issue 3 – Exclusivity Clause Restricts All of Rekaind's Equipment Worldwide

**Where:** Agreement §3.4 (Exclusivity); §1.16 (definition of "Covered Equipment")

**The problem.** Section 3.4 provides that "Licensee shall not license, use, or develop, and shall cause its Affiliates not to license, use, or develop, any remote-monitoring, condition-monitoring, dispatch or work-order software other than the Platform for any Covered Equipment." Section 1.16 defines "Covered Equipment" as "any equipment serviced by Licensee or any of its Affiliates anywhere in the world, including elevators, escalators, moving walks, dumbwaiters, wheelchair and platform lifts, and their associated controllers, drives, door operators and machine-room components."

This means Rekaind cannot use or develop any competing or complementary monitoring, dispatch, or work-order software for any vertical transportation equipment it services anywhere in the world—not just the 1,140 Licensed Units in PA, NJ, and DE under Order Form No. 001. If Rekaind services 5,000 units total, it is locked into LiftSense for all 5,000.

**Why it matters.** This is an extraordinary non-compete embedded in a software license. It:
- Prevents Rekaind from using a different (potentially better or cheaper) platform for units outside the Order Form territory;
- Prohibits Rekaind from developing its own dispatch or work-order tools, even for internal use;
- Extends to Affiliates; and
- Has no stated duration limit beyond the Term (it applies "during the Term and for any period during which any Order Form remains in effect").

If the termination is upheld, this restriction falls away. But if the termination fails (see Issue 1), Rekaind remains bound for the balance of the term and any renewal terms.

**Recommended fix.**
- If Rekaind renews or re-enters a license with Velert, negotiate to limit the exclusivity to the Licensed Units under the applicable Order Form, not to all Covered Equipment worldwide.
- In any dispute with Velert over the scope of §3.4, argue that the restriction is unreasonably broad as a matter of public policy (it functions as a non-compete on Rekaind's core business tools) and that the definition of "Covered Equipment" in §1.16 was intended for the indemnity and data provisions, not to extend the license exclusivity globally.

---

## Issue 4 – Service Credits Are the Exclusive Remedy for Non-Chronic Availability Failures

**Where:** Agreement §5.4; Service Level Schedule §§3.1–3.3

**The problem.** Agreement §5.4 states: "Service credits and the termination right for Chronic Availability Failure described in the Service Level Schedule are Licensee's remedies for Licensor's failure to meet the Platform Availability service level." This means that if Platform Availability falls below 99.5% in one or two months (but not three consecutive months), Rekaind's only remedy is a service credit of 5–30% of the Monthly Fee (SLS §3.1), capped at 40% of the Monthly Fee (SLS §3.3). There is no right to terminate, no right to consequential damages, and no right to a refund.

**Why it matters.** For a safety-critical application (entrapment alerts, passenger alarms), the financial remedy is disproportionate to the risk. A single month of 98.5% availability yields a 10% credit on $34,200 = $3,420. If that month includes an entrapment alert failure that results in a passenger being trapped for an extended period, the reputational and contractual damage to Rekaind (which owes its own obligations to building owners under maintenance contracts) vastly exceeds $3,420. The §5.4 language effectively immunizes Velert from all liability for short-duration availability failures regardless of severity.

**Recommended fix.**
- In any renegotiation, strike the exclusivity language in §5.4 and preserve Rekaind's right to claim damages for availability failures that cause actual harm (e.g., missed entrapment alerts), subject to the general liability cap in §11.3.
- Alternatively, add a provision that any Severity 1 Incident affecting the alert-delivery Core Function for more than 30 minutes gives rise to a separate termination right (not requiring three consecutive months of sub-99.5% availability).
- For the current termination, emphasize that the Chronic Availability Failure path was available and was exercised (subject to the timing issue in Issue 1).

---

## Issue 5 – Claims-Made Insurance Creates a Gap for the Post-Term Period

**Where:** Agreement §13.1 (insurance required "during the Term and for two (2) years afterward"); Certificate of Insurance §§5, 10.1, 11.1 (Tech E&O and Cyber are claims-made); §10.5 (optional 36-month extended reporting period)

**The problem.** Agreement §13.1 requires Velert to maintain technology E&O and cyber liability insurance "during the Term and for two (2) years afterward." The Termination Date is November 20, 2026, so the obligation runs to approximately November 20, 2028. However, the Tech E&O and Cyber policies are written on a claims-made and reported basis (Certificate §§10.1, 11.1). The current policy period ends April 1, 2027. For a claims-made policy, a claim must be both made and reported during the policy period (or during an extended reporting period) to be covered.

If Velert's claims-made policies expire on April 1, 2027 and are not renewed, or if Velert purchases a new policy with a later retroactive date, there is a coverage gap for claims first made between April 1, 2027 and November 20, 2028 that arise from acts occurring during the original policy period. The optional 36-month extended reporting period (Certificate §10.5) would bridge this gap, but it is optional—Velert must affirmatively purchase it and pay the premium.

**Why it matters.** Rekaind's primary exposure from the Platform is safety-related (entrapment, passenger alarms). A claim could be made well after the termination date—for example, if a passenger alleges they were trapped in August 2026 due to a delayed alert and files suit in 2027 or 2028. If the claims-made policy has lapsed and no ERP was purchased, Velert's insurer has no duty to defend or indemnify, and Rekaind's indemnity rights under Agreement §10 (as modified by the Side Letter) become uncollectable.

**Recommended fix.**
- Require Velert to confirm in writing that it will either (a) renew the claims-made policies through at least November 20, 2028, or (b) purchase the 36-month extended reporting period before the current policy expires on April 1, 2027.
- Request a certificate of insurance evidencing the renewal or ERP before the April 1, 2027 expiration.
- In the Notice Letter's insurance demand (§13.1), specifically reference the claims-made nature and the post-term duration requirement.

---

## Issue 6 – Connected Device Firmware Remains Licensed; Post-Termination Use Unclear

**Where:** Agreement §4.2(c) (title to hardware passes to Licensee; firmware remains part of the Platform and is licensed under §3.1); §12.7(a) (licenses terminate on expiration/termination); Notice Letter §11.1

**The problem.** Section 4.2(c) provides that title to Connected Devices passes to Rekaind upon delivery, but "the firmware and embedded software in those devices remain part of the Platform and are licensed under Section 3.1." Section 3.1 grants the license only "during the Subscription Term of each Order Form." Upon termination, the license ends (§12.7(a)). This means that after November 20, 2026, the firmware in the devices Rekaind owns is technically unlicensed.

The Notice Letter (§11.1) asks Velert not to "remotely disable, wipe or modify any Connected Device" post-termination, but this is a request, not a contractual right. The Agreement does not contain an express post-termination right to continue using the firmware, nor does it prohibit Velert from remotely disabling the devices.

**Why it matters.** If Velert remotely disables the firmware (e.g., by revoking a license key or pushing a "decommission" update), the hardware becomes a paperweight. Rekaind would own the physical devices but could not use them. Given that the devices are installed in 1,140 elevator and escalator units, a mass remote disable would create an immediate safety gap (loss of monitoring) during Rekaind's transition to a replacement platform.

**Recommended fix.**
- Seek a written confirmation from Velert (in response to the Notice Letter) that it will not remotely disable, wipe, or modify any Connected Device firmware post-termination without Rekaind's prior written consent.
- If the relationship continues in any form (e.g., transition assistance), negotiate a post-termination firmware license for the transition period.
- In any new agreement, require that firmware in devices owned by the licensee remain functional for a stated period post-termination (e.g., 12 months) or that the licensor provide the means to install alternative firmware.

---

## Issue 7 – Non-Renewal Window Is Only 15 Days

**Where:** Agreement §1.14 (definition of "Non-Renewal Window"); §12.2 (auto-renewal)

**The problem.** The Non-Renewal Window is defined as "the period beginning not more than seventy-five (75) days and ending not less than sixty (60) days before the expiration of the then-current Initial Order Term or Renewal Term." This creates a window of at most 15 days (75 to 60 days before expiration) in which either party must deliver non-renewal notice. If no notice is given within that 15-day window, the Order Form automatically renews for another full term (36 months, per §12.2).

**Why it matters.** A 15-day window is extremely narrow for a $410,400/year commitment. If Rekaind's contract administrator misses the window by even one day, Rekaind is locked in for another 36 months. This is particularly dangerous given:
- The Initial Order Term expires March 2, 2028;
- The Non-Renewal Window would open December 17, 2027 (75 days before) and close January 1, 2028 (60 days before);
- That is a 15-day window in the holiday season.

**Recommended fix.**
- If Rekaind continues with Velert in any form, negotiate to extend the Non-Renewal Window to at least 90 days before expiration (e.g., 120 to 90 days).
- Implement an internal calendar alert for the Non-Renewal Window opening date, with escalation to General Counsel.
- Note that the current termination (if effective) makes this issue moot for Order Form No. 001, but it would apply to any new Order Form.

---

## Issue 8 – Minimum Unit Commitment of 1,000 Units

**Where:** Order Form No. 001 §1.5; Agreement §2.4(b)

**The problem.** The minimum unit commitment is 1,000 Licensed Units. Rekaind may remove units under Agreement §2.4(b) only "to the extent that the number of Licensed Units after the removal is not less than the minimum unit commitment." With 1,140 units, Rekaind can remove at most 140 units. If Rekaind loses maintenance contracts (e.g., a building owner switches to a competing elevator contractor), it must continue paying the subscription fee for the minimum 1,000 units even if it has fewer actual units to monitor.

**Why it matters.** This creates a fixed-cost floor of $360,000/year (1,000 × $360) regardless of Rekaind's actual portfolio size. In a down market or if Rekaind loses a major account, it cannot reduce its subscription proportionally.

**Recommended fix.**
- If Rekaind re-enters a license with Velert, negotiate a lower minimum (e.g., 80% of the initial unit count) or a step-down schedule.
- Alternatively, negotiate that the minimum applies only during the Initial Order Term and not during Renewal Terms.
- For the current termination, this issue is moot (the minimum falls with the Order Form), but it is relevant if Rekaind pursues transition assistance under Agreement §12.8 (which continues at "the per-unit fees then in effect").

---

## Issue 9 – No Credit Mechanism for Device Delivery Delays After Year 1

**Where:** Order Form No. 001 §3.4 (Year 1 credit only); Agreement §4.2(a) (Licensor supplies devices)

**The problem.** Order Form §3.4 provides a credit of 50% of the prorated per-unit subscription fee for each full month in Year 1 during which a unit is not connected "because of a delay in delivery of Connected Devices attributable to Licensor." No equivalent credit mechanism exists for Year 2 or Year 3. If Velert delays delivery of replacement or additional devices in Year 2 or 3, Rekaind pays the full subscription fee for units that are not yet connected, with no offset.

**Why it matters.** The Notice Letter references an outstanding device order (replenishment of LS-G4 Gateways and LS-ESC Escalator Sensor Packages) placed September 28, 2026 that had not been shipped as of October 21, 2026 (Notice Letter §5.3). While this is now cancelled, the pattern suggests Velert's device logistics may be a recurring issue. In a continuing relationship, delivery delays in Year 2 or 3 would generate unremediated costs.

**Recommended fix.**
- In any new agreement, extend the Year 1 credit mechanism to all years of the Subscription Term.
- Alternatively, add a provision that if device delivery is delayed by more than 30 days beyond the implementation plan date, the subscription fee for the affected units is abated for the delay period.

---

## Issue 10 – Technology E&O and Cyber Policies Written on Surplus Lines Basis

**Where:** Certificate of Insurance §18.1; Agreement §13.1 (requires insurers "rated A- VII or better by A.M. Best")

**The problem.** The certificate discloses that the Technology E&O and Cyber Liability policies (Insurer D, Meridian Specialty Insurance Company) are "written on a surplus lines basis through a licensed Ohio surplus lines broker" and that "policies issued by surplus lines insurers are not protected by the Ohio Insurance Guaranty Association" (Certificate §18.1).

**Why it matters.** If Meridian Specialty becomes insolvent, there is no state guaranty fund to step in and pay claims. The $5,000,000 limits on both the Tech E&O and Cyber policies—Rekaind's primary source of recovery for a data breach or a safety-related software failure—would be uncollectable. The A.M. Best rating (A, Excellent, FSC XIV) satisfies the contractual requirement in §13.1, but rating is not the same as solvency guarantee.

**Recommended fix.**
- Require Velert to confirm that the surplus lines placement was made in compliance with Ohio's surplus lines law (including the eligible surplus lines insurer determination and the Ohio Surplus Lines Disclosure Notice, which is listed at Certificate §17.5).
- Consider requiring Velert to maintain a letter of credit or escrow as additional security for the Tech E&O and Cyber coverage, given the absence of guaranty fund protection.
- In any new agreement, require that the Tech E&O and Cyber policies be written on an admitted (in-force) basis, or that the insurer maintain a trust or letter of credit equal to the policy limits.

---

## Issue 11 – Asymmetric Assignment Rights

**Where:** Agreement §14.1 (Licensee may not assign without consent); §14.2 (Licensor may assign without consent to Affiliates or successors)

**The problem.** Rekaind cannot assign the Agreement or any Order Form without Velert's prior written consent (though consent "shall not be unreasonably withheld"). Velert, by contrast, may assign freely to any Affiliate or to any successor in a merger, asset sale, or change of control, with only 30 days' post-hoc notice.

**Why it matters.** If Velert is acquired by a competitor of Rekaind or by a private equity firm that strips services, Rekaind has no consent right and no termination trigger. The Agreement does not provide Rekaind with a right to terminate upon a change of control of Velert. Rekaind's Customer Data, security posture, and service quality could all change hands without Rekaind's approval.

**Recommended fix.**
- In any new agreement, add a provision giving Rekaind the right to terminate (with pro-rata refund and no early termination charge) if Velert undergoes a change of control to a competitor or to an entity that does not maintain the required insurance and service levels.
- Alternatively, require Rekaind's consent (not to be unreasonably withheld) for any assignment by Velert to a non-Affiliate successor.

---

## Issue 12 – Aggregated Data: Competitive Risk

**Where:** Agreement §8.4; Side Letter §2.2(d) (new §10.1(d))

**The problem.** Section 8.4 permits Velert to "compile statistical and performance data derived from Equipment Data" and "use it to improve the Platform and its predictive models." The restriction is that Velert must de-identify the data so it "does not identify Licensee, any of Licensee's customers, any building, or any individual," and must not "disclose Aggregated Data to third parties in any form that identifies Licensee or permits a third party to determine Licensee's customer portfolio or pricing."

However, nothing prevents Velert from sharing non-identifying aggregate data (e.g., "average door cycles per unit in the Philadelphia metro area," "failure rate for Otis controllers in mid-Atlantic buildings") with Rekaind's competitors who are also Velert customers. A sophisticated competitor could use such data to benchmark Rekaind's service territory, identify underperforming building types, or optimize its own maintenance pricing.

**Why it matters.** Rekaind's competitive advantage in the elevator maintenance industry depends on proprietary knowledge of its customers' equipment, failure patterns, and service costs. The Aggregated Data provision, while facially protective, creates a channel through which competitive intelligence could leak.

**Recommended fix.**
- Negotiate a provision that Velert shall not share Aggregated Data with any entity that is a direct competitor of Rekaind in the elevator or escalator maintenance industry, or that shall obtain Rekaind's prior written consent before sharing Aggregated Data with any third party.
- Define "direct competitor" with reference to the specific markets in which Rekaind operates (PA, NJ, DE vertical transportation maintenance).
- The Side Letter's new §10.1(d) indemnity (for IP infringement arising from Velert's use of Aggregated Data) does not address competitive harm—only IP claims.

---

## Issue 13 – No Specific Remedy for Missed Resolution Targets

**Where:** Service Level Schedule §6.2 (Response and Resolution Targets); §3 (Service Credits tied only to Platform Availability)

**The problem.** The SLS sets specific Resolution Targets for each Severity Level (e.g., 4 hours for Severity 1, 12 hours for Severity 2). However, the Service Credit mechanism in SLS §3 is triggered only by Platform Availability falling below 99.5% in a Measurement Period. There is no separate credit, penalty, or termination trigger for missing individual Resolution Targets.

The June 16, 2026 incident (Notice Letter §2.4(a)) lasted approximately 4 hours and 40 minutes, exceeding the 4-hour Severity 1 Resolution Target. The only consequence is that the downtime minutes feed into the Platform Availability calculation. If the total monthly downtime remains below the threshold that drops availability under 99.5%, the missed Resolution Target has no independent consequence.

**Why it matters.** A pattern of missed Resolution Targets that individually stay below the availability threshold could degrade Rekaind's operations without triggering any remedy. For a 24/7 dispatch center, a Severity 1 incident that takes 6 hours to resolve (vs. the 4-hour target) means 2 extra hours of manual monitoring for potentially hundreds of units.

**Recommended fix.**
- Negotiate a service credit or penalty for each Severity 1 Incident that exceeds its Resolution Target (e.g., 1% of Monthly Fee per hour over target, up to a cap).
- Alternatively, provide that three or more missed Severity 1 Resolution Targets in any six-month period constitute a material breach giving rise to a termination right.
- In the current termination, cite the missed Resolution Target as part of the pattern of material breach (fallback position under Agreement §12.4 if the Chronic Availability Failure termination is challenged on timing).

---

## Issue 14 – Insurance Certificate: Additional Insured Status Limited to CGL and Umbrella Only

**Where:** Agreement §13.2 (requires additional insured status under §§13.1(a) CGL and 13.1(d) Umbrella); Certificate §5 (shows "N" for Addl Insd on Tech E&O and Cyber); §13.1 (additional insured under CGL and Umbrella only)

**The problem.** Agreement §13.2 requires Velert to name Rekaind as an additional insured under the CGL and Umbrella policies. The certificate confirms this (Certificate §§5, 13.1–13.2). However, Rekaind is NOT an additional insured under the Technology E&O or Cyber Liability policies (Certificate §5 shows "N" for both). This is technically compliant with §13.2 (which only requires additional insured status under CGL and Umbrella), but it means that if a data breach or software failure causes harm to Rekaind's customers, Rekaind cannot make a direct claim under Velert's Tech E&O or Cyber policies. Rekaind must rely on its contractual indemnity rights under Agreement §10 (as modified by the Side Letter) and then look to Velert to collect from its insurer.

**Why it matters.** In a worst-case scenario (e.g., a data breach exposing customer information, or a software failure causing an entrapment injury), Rekaind's recovery depends entirely on Velert's solvency and willingness to pay. If Velert is undercapitalized or disputes the indemnity claim, Rekaind has no direct right under the insurance policies. The CGL additional insured status helps for bodily injury/property damage, but the Tech E&O and Cyber policies are the ones that cover the specific risks most likely to arise from a software platform (data breach, software failure, network interruption).

**Recommended fix.**
- In any new agreement, require that Rekaind be named as an additional insured (or at minimum a loss payee) under the Tech E&O and Cyber policies, to the extent those policies permit additional insured status.
- If the insurers will not add Rekaind as an additional insured on the claims-made policies (which is common), require Velert to maintain the policies with a "primary and non-contributory" endorsement in favor of Rekaind and to provide Rekaind with direct notice of any claim that could implicate the policies.
- For the current situation, the Notice Letter's insurance demand (§13.1) should specifically request confirmation that the Tech E&O and Cyber policies will remain in force (or be replaced with equivalent coverage) through the two-year post-term period.

---

## Additional Observations (Lower Materiality)

**A. SLS §2.3 Proportional Downtime Calculation.** Downtime affecting fewer than 25% of Licensed Units counts only in proportion. For 1,140 units, a regional outage affecting 273 units (24%) for 4 hours counts as only ~57.6 minutes of downtime rather than 240 minutes. This makes it harder to reach the Chronic Availability Failure threshold and could mask significant regional outages. Recommend negotiating a lower threshold (e.g., 10%) or a flat count for any Severity 1 Incident.

**B. Order Form §4.6 Spare Device Replenishment.** Velert must replenish spare devices within 5 Business Days. The Notice Letter references a replenishment order placed September 28, 2026 that had not shipped as of October 21, 2026 (23 Business Days later). If spares were used, this appears to be a breach of the replenishment obligation. Preserve this as a separate claim for damages.

**C. Side Letter §3.5 Firmware Validation.** The requirement that Velert validate firmware against "each controller make and model identified in the unit register" before deployment is strong protection. The July 2026 alert delay was associated with "a particular LS-G4 Gateway firmware version" (Notice Letter §2.4(b)). If Velert deployed that firmware without validating against all controller types in the register, this would be a breach of the Side Letter. Request Velert's validation records for the July 2026 firmware deployment.

**D. Dispatch Center Lease – Permitted Use.** The lease at 1700 Spring Garden Street (the dispatch center) permits "operation of a 24-hour elevator and escalator maintenance dispatch and call center" (Lease §1.1). This is consistent with Rekaind's use of the Platform. No issue identified, but note that the lease runs to September 30, 2030, with a renewal option exercisable between March 31, 2029 and September 30, 2029 (Lease Exhibit C, ¶4). If Rekaind's business model changes significantly post-termination, the 7-year lease commitment (plus potential 5-year renewal) is a fixed cost to consider.

**E. Notice Letter §15.1 – Reservation of Rights.** The Notice Letter expressly reserves Rekaind's rights under Agreement §10 for any Third-Party Claim arising from the Incidents. This is appropriate and should be maintained. If any building owner or passenger makes a claim related to the June–August 2026 outages, Rekaind should notify Velert promptly under the indemnity procedure (renumbered §10.5 per the Side Letter) and preserve the 15-day defense-assumption right added by Side Letter §2.5(c).

---

## Recommended Immediate Actions

1. **Monitor Velert's response to the October 21 Notice Letter.** If Velert raises a timeliness objection to the termination, escalate immediately. Prepare the material breach fallback (Agreement §12.4) with supporting evidence of the missed Resolution Target, the failed remediation plan, and the pattern of Severity 1 Incidents.

2. **Demand written confirmation of insurance continuity** through November 20, 2028, specifically addressing the claims-made policies and the extended reporting period (Issue 5).

3. **Request Velert's firmware validation records** for the July 2026 deployment to assess potential Side Letter §3.5 breach (Observation C).

4. **Preserve all monitoring logs, incident tickets, and Service Reports** for the June–November 2026 period. The Notice Letter (§12.2) already requests preservation; follow up if Velert does not confirm.

5. **Implement internal calendar alerts** for any future contractual notice windows (Non-Renewal Window, data export deadline under §8.7, transition assistance request window under §12.8).

6. **Assess Connected Device decommissioning plan.** Confirm that Rekaind's replacement monitoring solution can be deployed before November 20, 2026, or that Rekaind is prepared to invoke transition assistance under Agreement §12.8 (available for up to 90 days post-termination, requestable within 30 days).