# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Rekaind Vertical Services, Inc. – Review of Velert Systems Software License Agreement File: Issues and Recommended Fixes

---

## I. CRITICAL ISSUES

### 1. Termination Notice Appears 17 Days Late

**Where:** Service Level Schedule §4.2; Rekaind Notice Letter §3.1 and §2.3

**Issue:** SLS §4.2 requires Rekaind to deliver written notice of termination for Chronic Availability Failure "within thirty (30) days after delivery of the Service Report for the third consecutive calendar month in which Platform Availability was below 99.5%." The third failing month is August 2026. Velert's Service Report for that month was delivered on September 4, 2026 (confirmed in the Notice Letter at §2.3 and in the table at §2.2). Thirty days after September 4, 2026 is **October 4, 2026**. The Notice Letter is dated **October 21, 2026**—17 days past the deadline.

**Why it matters:** Velert will almost certainly argue the termination is a nullity for non-compliance with the contractual notice period. If the termination is invalid, the Order Form continues in effect (and potentially auto-renews under Agreement §12.2), Rekaind remains bound by the exclusivity clause (§3.4), and Rekaind's refund and service-credit claims lose their termination-triggered basis.

**Recommended fix:**
- **Immediate:** Assess whether an alternative termination ground is available. Agreement §12.4 permits termination for material breach with 30 days' cure notice. Three consecutive months of sub-99.5% availability, including Severity 1 incidents affecting entrapment alerting, likely constitute a material breach of Agreement §5.2 and §11.2(a). If Velert has not already been given a §12.4 cure notice, send one immediately (or argue the Chronic Availability Failure notice itself put Velert on notice of the breach).
- **Argue waiver/estoppel:** Velert delivered a remediation plan on August 19, 2026 (SLS §4.5) and met to review it on August 25, 2026. Velert knew by that date that two consecutive months had failed and that a third was likely. Velert's failure to cure before the August report was delivered, and its participation in the remediation process, support an argument that it waived strict compliance with the 30-day window or is estopped from raising the lateness as a defense.
- **Argue the "required to be reported" language:** SLS §4.1 defines Chronic Availability Failure by reference to months that are "reported, or required to be reported, in the Service Report." One could argue the 30-day clock in §4.2 should run from when the report was *required* to be delivered (SLS §7.1: within 5 Business Days of month-end, i.e., by September 7, 2026 for the August report), not from actual delivery. This buys 3 days but does not cure the 17-day gap.
- **Negotiate:** Given the strength of the underlying performance failure, Velert may prefer to agree to the termination terms rather than litigate the notice issue. Use the lateness as a bargaining chip only if Velert raises it.

---

### 2. Governing Law and Venue Conflict

**Where:** Agreement §15.1 (Delaware law); Agreement §15.2 (Wilmington, Delaware venue); Order Form No. 001 §7.1 (Ohio law); Order Form No. 001 §7.2 (Franklin County, Ohio venue)

**Issue:** The Agreement specifies Delaware governing law and exclusive jurisdiction in Wilmington, Delaware. The Order Form specifies Ohio governing law and exclusive jurisdiction in Franklin County, Ohio. Under the order of precedence in Agreement §15.4, the Order Form controls over the Agreement body. Therefore, the operative governing law is **Ohio** and the operative venue is **Franklin County, Ohio**.

**Why it matters:**
- Rekaind is a Pennsylvania corporation. Neither Delaware nor Ohio is home territory. However, Ohio is Velert's home state (Columbus), which gives Velert a home-field advantage in litigation.
- Ohio and Delaware differ on contract interpretation, the economic loss rule, and the enforceability of certain limitations of liability. For example, Ohio courts have been more willing to enforce consequential-damages waivers in commercial contracts than some Delaware courts.
- If Rekaind needs to sue (e.g., to enforce the refund or service credits), it must do so in Franklin County, Ohio, increasing cost and inconvenience.

**Recommended fix:**
- For the current termination dispute, the conflict likely does not change the outcome (the SLS §4.2 deadline is clear regardless of governing law), but it affects procedural strategy.
- If Rekaind re-negotiates or enters a new agreement with Velert (or a replacement vendor), insist on Pennsylvania law and Philadelphia venue, or at minimum neutral territory.
- If the termination is challenged, be prepared to litigate in Ohio. Retain Ohio counsel now.

---

### 3. Insurance Coverage Gap for Post-Termination Period

**Where:** Agreement §13.1 (insurance required "during the Term and for two (2) years afterward"); Certificate of Insurance §5 (all policies expire April 1, 2027); Certificate of Insurance §10.1 and §11.1 (Technology E&O and Cyber are claims-made)

**Issue:** The Termination Date is November 20, 2026. Agreement §13.1 requires Velert to maintain the specified insurance for two years after the Term ends—i.e., through **November 20, 2028**. The current policies (all four insurers) expire **April 1, 2027**, leaving a gap of approximately **19.5 months**.

The problem is acute for the Technology E&O and Cyber policies because they are written on a **claims-made** basis (Certificate §10.1, §11.1). A claims-made policy only covers claims that are both made and reported during the policy period (or an extended reporting period). If a third party sues Rekaind in, say, mid-2027 for an entrapment alert failure that occurred in October 2026, the claim would fall outside the April 1, 2027 policy expiration and would not be covered unless:
- Velert purchased the optional 36-month extended reporting period (Certificate §10.5), or
- Velert bound a new claims-made policy with a retroactive date no later than January 1, 2019 (the current retroactive date).

**Why it matters:** The entire purpose of the post-termination insurance requirement is to protect Rekaind against delayed-manifesting claims (e.g., a passenger injured in an entrapment that was not alerted in time, where the injury claim is filed months later). If the claims-made policies lapse without tail coverage, Rekaind's indemnification right under Agreement §10.1/10.2 (as modified by the Side Letter) becomes unsecured—Velert would owe the indemnity but have no insurance to back it.

**Recommended fix:**
- Demand written confirmation from Velert, before the Termination Date, that it has either (a) bound renewal policies for the period April 1, 2027 through November 20, 2028, or (b) purchased the 36-month extended reporting period on both the E&O and Cyber policies.
- Request a revised certificate of insurance evidencing the extended coverage.
- If Velert refuses or is unable to provide tail coverage, consider requiring a letter of credit or escrow of funds sufficient to cover the indemnification obligation for the uncovered period.
- Note that the Notice Letter §13.1 already requests a current certificate; Velert's response (the November 2, 2026 certificate) does not address the post-April 2027 gap. Follow up specifically.

---

## II. SIGNIFICANT ISSUES

### 4. Overly Broad Exclusivity Clause

**Where:** Agreement §3.4; Agreement §1.6 (definition of "Covered Equipment")

**Issue:** Section 3.4 prohibits Rekaind from licensing, using, or developing any other remote-monitoring, condition-monitoring, dispatch, or work-order software "for any Covered Equipment." "Covered Equipment" is defined in §1.6 as "any equipment serviced by Licensee or any of its Affiliates **anywhere in the world**." This is not limited to the 1,140 Licensed Units in Pennsylvania, New Jersey, and Delaware.

**Why it matters:**
- During the Subscription Term, Rekaind cannot use any competing monitoring platform for any elevator or escalator it services globally, even units it does not want to put on LiftSense (e.g., units in other states, units with building owners who require a specific vendor's platform, or units where LiftSense is technically unsuitable).
- The clause also bars Rekaind from *developing* its own monitoring software, which could stifle internal innovation.
- The prohibition on procuring monitoring hardware "designed to transmit data to any platform other than the Platform" (§3.4, second sentence) is particularly restrictive.
- Although the exclusivity ends when the Order Form terminates (because it applies "during the Term and for any period during which any Order Form remains in effect"), if the termination is found invalid (see Issue 1), the exclusivity continues.

**Recommended fix:**
- If the termination is upheld, this issue resolves itself.
- If Rekaind renegotiates or enters a replacement agreement, narrow "Covered Equipment" to the Licensed Units under the applicable Order Form, and add carve-outs for: (a) units where the building owner contractually requires a specific platform; (b) units in jurisdictions where the Platform is not available; and (c) Rekaind's internal R&D.
- In the current dispute, if Velert argues Rekaind is in breach of §3.4 for beginning to evaluate replacement monitoring solutions, the answer is that §3.4 applies "during the Term," and Rekaind has given notice of termination. Even if the notice is late, Rekaind is in the process of exercising its contractual right, and evaluating alternatives in anticipation of a valid termination is reasonable.

---

### 5. Technology E&O and Cyber Policies Do Not Name Rekaind as Additional Insured

**Where:** Agreement §13.2; Certificate of Insurance §5 (Summary of Coverages table)

**Issue:** Agreement §13.2 requires Velert to name Rekaind and its Affiliates as additional insureds under the policies in §13.1(a) (CGL) and §13.1(d) (Umbrella). The certificate confirms additional insured status under CGL and Umbrella (marked "Y"). However, the Technology E&O and Cyber policies are marked **"N"** for additional insured status.

The Agreement does not require additional insured status under the E&O or Cyber policies (§13.1(b) and (c)), so Velert is technically in compliance. But the practical effect is that if a technology failure or data breach gives rise to a third-party claim naming Rekaind (e.g., a building owner sues both Velert and Rekaind for a missed entrapment alert), Rekaind cannot go directly to Velert's E&O or Cyber insurer. Rekaind must rely solely on the contractual indemnification in Agreement §10.1/10.2 (as modified by the Side Letter).

**Why it matters:** The indemnification is Rekaind's only direct protection for technology-related third-party claims. While it is uncapped (excluded from the §11.3 limitation by §11.4(a)), it is only as good as Velert's ability to pay. If Velert's E&O insurer denies a claim (e.g., arguing the loss is not "technology services" but a "product" defect, or that the retention applies), Rekaind has no direct right under the policy.

**Recommended fix:**
- In any renewed or replacement agreement, require additional insured status under the Technology E&O and Cyber policies, or at minimum require that those policies name Rekaind as a "loss payee" or provide that the insurer will not deny coverage to Rekaind without first exhausting the policy limits.
- For the current situation, the indemnification (uncapped per §11.4(a)) is the primary protection. Ensure Velert's acknowledgment of the termination notice includes confirmation that it will honor its indemnification obligations for any claims arising from the June–August 2026 incidents.

---

### 6. Surplus Lines Status of E&O and Cyber Insurer

**Where:** Certificate of Insurance §18.1; Agreement §13.1

**Issue:** The Technology E&O and Cyber policies are issued by Meridian Specialty Insurance Company (Insurer D) on a **surplus lines** basis. Certificate §18.1 expressly states: "Policies issued by surplus lines insurers are not protected by the Ohio Insurance Guaranty Association."

**Why it matters:** If Meridian Specialty becomes insolvent, there is no state guaranty fund to step in and pay claims. The E&O and Cyber policies are the most relevant coverages for a software platform failure. Rekaind's protection against a Velert technology failure that causes bodily injury or a data breach rests substantially on these policies. The absence of guaranty fund protection is a meaningful credit risk.

The insurer meets the Agreement's rating requirement (A- VII or better; Meridian is rated A, Financial Size Category XIV—Certificate §4), so Velert is in technical compliance. But the surplus lines status is a qualitative risk factor the Agreement does not address.

**Recommended fix:**
- For the current period, the risk is manageable given the insurer's rating. Monitor Meridian Specialty's financial condition.
- In any future agreement, require that the E&O and Cyber policies be written on an admitted (in-state) basis, or require a higher minimum Financial Size Category (e.g., XV or above), or require a bond or letter of credit to backstop the surplus lines exposure.

---

### 7. Minimum Unit Commitment Locks In 1,000 Units

**Where:** Order Form No. 001 §1.5; Agreement §2.4(b)

**Issue:** The minimum unit commitment is 1,000 Licensed Units. Rekaind started with 1,140 units, meaning it can remove no more than 140 units without breaching the minimum. Furthermore, Agreement §2.4(b) provides that "Fees for a removed unit cease from the start of the next annual billing period after the removal takes effect"—so even a valid removal does not reduce fees immediately.

**Why it matters:** If Rekaind loses maintenance contracts (e.g., building owners cancel due to service disruptions caused by the Platform failures), it cannot correspondingly reduce its subscription footprint below 1,000 units. This creates a fixed-cost floor that is disproportionate if Rekaind's actual portfolio shrinks.

**Recommended fix:**
- In the current termination, this is moot (the Order Form is ending).
- In any replacement agreement, negotiate a lower minimum (e.g., 75% of the initial unit count) or eliminate the minimum entirely, and provide that fee reductions for removed units are effective immediately (prorated) rather than deferred to the next billing period.

---

### 8. Fees Payable for Unconnected Units from Day One

**Where:** Order Form No. 001 §3.4

**Issue:** "Fees for Licensed Units that are not yet connected to the Platform on the Order Effective Date are nonetheless payable from the Order Effective Date." The only mitigation is a 50% credit for units not connected in Year 1 due to a delay "attributable to Licensor."

**Why it matters:** The implementation plan targeted go-live in three phases (June 30, September 30, and December 31, 2025—Order Form §5.1). This means units in Phases 2 and 3 were not connected for 6–10 months after the Order Effective Date, yet Rekaind paid full fees for them. The 50% credit only applies if the delay is "attributable to Licensor"—a fact-specific determination that could be disputed.

**Recommended fix:**
- This is a past-cost issue for Year 1. If Rekaind believes some Phase 2 or Phase 3 delays were attributable to Velert (e.g., late device deliveries), it should quantify the 50% credit it was entitled to and assert it as an offset against the refund or as a separate claim.
- In any future agreement, tie subscription fees to actual connection date, not Order Effective Date.

---

### 9. Refund Calculation Off by One Day

**Where:** Rekaind Notice Letter §6.2

**Issue:** The Notice Letter calculates the unexpired portion of Year 2 as "103 days from November 21, 2026 to March 2, 2027." The correct count is **102 days**:
- November 21–30: 10 days
- December: 31 days
- January: 31 days
- February: 28 days (2027 is not a leap year)
- March 1–2: 2 days
- Total: 102 days

The letter's refund figure of $115,811.51 is calculated as $410,400 × 103/365. The correct figure is $410,400 × 102/365 = **$114,632.88**.

**Why it matters:** The overstatement is $1,178.63. While small, it undermines the precision of Rekaind's claims and gives Velert an easy (if minor) point of dispute. More importantly, it signals that the calculation should be double-checked before any settlement discussion.

**Recommended fix:** Correct the refund figure to $114,632.88 (or recalculate once the final unit count is confirmed, since the letter notes the figure is subject to reconciliation for units added/removed under §2.4). Send a corrected schedule to Velert.

---

### 10. Asymmetric Assignment Rights

**Where:** Agreement §14.1 (Licensee cannot assign without consent); Agreement §14.2 (Licensor may assign freely to Affiliates or successors)

**Issue:** Velert can assign the Agreement to any Affiliate or to any successor in a merger, asset sale, or change of control without Rekaind's consent. Rekaind cannot assign without Velert's consent (though consent "shall not be unreasonably withheld").

**Why it matters:** If Velert is acquired by a competitor of Rekaind or by a company with a weaker financial profile, Rekaind is stuck with the new counterparty. The Platform could be deprioritized, service levels could effectively degrade, and Rekaind's data could end up in the hands of a competitive entity. The only protection is the confidentiality clause (§9), which survives assignment.

**Recommended fix:**
- In any future agreement, require Rekaind's consent for assignment to a direct competitor, or at minimum require that the assignee assume all obligations in writing and that Rekaind may terminate without penalty if the assignee is a competitor.
- For the current situation, monitor Velert's corporate developments. If a change of control occurs before the Termination Date, Rekaind may have grounds to argue the assignment affects the contract's performance.

---

## III. MODERATE ISSUES

### 11. Building Power Exclusion from Downtime

**Where:** Service Level Schedule §2.4(d)

**Issue:** "Unavailability of an individual Licensed Unit caused by loss of building power" is Excluded Downtime. In a portfolio of 1,140 units across occupied buildings, power outages are not uncommon (storms, grid maintenance, building electrical faults). Each such event removes that unit from the Downtime calculation, making it easier for Velert to meet the 99.5% availability target.

**Why it matters:** If a significant number of units experience power loss in a given month (e.g., a regional storm), the availability percentage is calculated as if those units were still "up," artificially inflating the metric. This makes it harder for Rekaind to establish a Chronic Availability Failure or claim service credits.

**Recommended fix:** In a future SLS, exclude building power events only if the Connected Device has a battery backup that should have kept it online, or cap the total Excluded Downtime from this category at a set number of minutes per month.

---

### 12. Proportional Counting for Partial Outages (25% Threshold)

**Where:** Service Level Schedule §2.3

**Issue:** Downtime affecting fewer than 25% of Licensed Units counts only proportionally. For example, if an outage affects 10% of units for 4 hours, it counts as 24 minutes of Downtime for the month, not 4 hours.

**Why it matters:** The 1,140-unit portfolio means 25% is 285 units. A regional failure affecting, say, 200 units (17.5%) for 3 hours counts as only 52.5 minutes of Downtime. This dilution makes it significantly harder to drop below 99.5% (which allows only about 3.6 hours of Downtime per 30-day month). Rekaind may experience operationally significant outages that do not register meaningfully in the availability metric.

**Recommended fix:** Lower the threshold from 25% to 10%, or eliminate proportional counting entirely for Severity 1 incidents (where any alert-delivery failure should count in full regardless of the number of units affected).

---

### 13. Limitation of Liability Cap and Consequential Damages Exclusion

**Where:** Agreement §11.3 (cap at 12 months' Fees ≈ $410,400); Agreement §11.5 (exclusion of consequential damages)

**Issue:** For any claim that is not an indemnification, confidentiality breach, data security breach, fraud, or payment obligation, Velert's total liability is capped at approximately $410,400, and Rekaind cannot recover lost profits, lost revenue, or loss of goodwill.

**Why it matters:** If a Platform failure causes Rekaind to lose a building maintenance contract (e.g., a building owner cancels after repeated missed entrapment alerts), Rekaind's lost contract revenue is a consequential damage and is unrecoverable. The only remedies are service credits (capped at 40% of Monthly Fee per month—SLS §3.3) and the termination right. For a company with 1,140 units generating significant maintenance revenue, this is a substantial gap.

**Recommended fix:** In a future agreement, either (a) raise the cap to 24 or 36 months' Fees, (b) carve out lost building contracts from the consequential damages exclusion where the loss is directly caused by a Severity 1 alert-delivery failure, or (c) require Velert to maintain a higher E&O limit specifically to backstop this exposure.

---

### 14. Cancellation of Pending Device Order

**Where:** Rekaind Notice Letter §5.3; Agreement (no express provision)

**Issue:** The Notice Letter cancels a device replenishment order placed September 28, 2026 that had not yet shipped. The Agreement does not contain an express right to cancel pending purchase orders upon termination for Chronic Availability Failure. Section 12.7(b) requires payment of "all undisputed Fees accrued through the effective date of termination." One could argue the device order fees "accrued" when the order was placed and accepted.

**Why it matters:** Velert may assert that the device order is a binding obligation and that Rekaind must pay for the devices (or accept delivery and return them). The devices in question are LS-G4 Gateways and LS-ESC Escalator Sensor Packages—potentially a significant cost.

**Recommended fix:**
- Argue that the device order was placed in anticipation of continued performance under the Order Form, and that termination for Chronic Availability Failure (with refund of prepaid Fees under §12.6) unwinds all forward-looking obligations. The devices were not delivered, so no fee has "accrued."
- If Velert disputes, the devices are Rekaind's property once delivered (§4.2(c)), so Rekaind's worst case is paying for and then reselling or storing them.
- In any future agreement, include an express provision that all pending orders are cancelled upon termination for cause.

---

### 15. Dispatch Center HVAC Costs for 24-Hour Operation

**Where:** Office Lease §8.1(a) (Building Hours: 7 a.m.–7 p.m. weekdays, 8 a.m.–1 p.m. Saturdays); §8.2 (after-hours HVAC at $65/hour per floor zone)

**Issue:** Rekaind operates a 24-hour dispatch center (Lease §7.2; Permitted Use in §1.1). Building Hours HVAC covers only 12 hours on weekdays and 5 hours on Saturdays. Rekaind must pay $65/hour per floor zone for the remaining ~20 hours per day, 7 days per week.

**Why it matters:** At $65/hour × 20 hours/day × 365 days = approximately **$474,500/year** in after-hours HVAC charges (assuming one floor zone). This is a significant ongoing cost that is not reflected in the base rent. If the dispatch center expands to multiple floor zones, the cost multiplies.

**Recommended fix:**
- Negotiate with the landlord to include 24-hour HVAC in the base Operating Expenses, or at minimum reduce the after-hours rate.
- Alternatively, evaluate whether the supplemental cooling system for the server room (§8.3, §3.5(a)) can be extended to cover the dispatch area, potentially reducing reliance on the Building HVAC.
- Track actual charges and include them in the total cost of occupancy when evaluating whether to renew the lease (option notice window: March 31–September 30, 2029, per Lease §4.4 and Exhibit C).

---

### 16. Emergency Generator Dependency Without Service Level

**Where:** Office Lease §9.4

**Issue:** The dispatch center relies on the Building's emergency generator for up to 150 kW of standby power. The lease requires the landlord to maintain the generator, test it monthly, and keep 48 hours of fuel on site. However, there is no service level, no penalty for generator failure, and no requirement for the landlord to provide alternative power if the generator is down for an extended period.

**Why it matters:** If the generator fails during a commercial power outage, the dispatch center loses power. Without power, Rekaind cannot receive or respond to entrapment alerts, potentially endangering building occupants. The lease's rent abatement provision (§8.6) only applies if the premises are "untenantable for more than three consecutive business days"—a high threshold for a dispatch center that needs power 24/7.

**Recommended fix:**
- Negotiate a generator uptime commitment (e.g., 99.9% availability) with a rent credit or abatement for failures.
- Install or expand Rekaind's own UPS system (§9.5 permits this) to bridge short generator start-up times.
- Consider a backup generator or fuel cell dedicated to the dispatch center, independent of the Building's system.

---

## IV. ADDITIONAL OBSERVATIONS

### 17. Side Letter Broadens Exclusions to All IP Indemnity Sub-Sections

**Where:** Side Letter §2.5(a); Agreement §10.3 (as renumbered to §10.4)

**Issue:** The original Agreement §10.3 exclusions applied only to "Section 10.1(a)" (the IP indemnity). The Side Letter changes this to "Section 10.1" (the entire IP indemnity, now including the new sub-sections on open-source compliance, report/dashboard IP, and Aggregated Data IP). This means, for example, the "combination" exclusion (§10.3(b)) now applies to the open-source indemnity as well.

**Why it matters:** The Side Letter also adds a carve-out to the combination exclusion for "elevator or escalator controllers, drives or other unit equipment on which Connected Devices are installed in accordance with the Documentation" (Side Letter §2.5(a), second sentence). This carve-out is critical for Rekaind's use case but is narrow—it only covers the specific unit equipment, not, e.g., a building management system that interfaces with the elevator controller.

**Recommended fix:** No immediate action required. Be aware of this if an IP claim arises from a combination with non-unit equipment (e.g., a BMS integration).

---

### 18. Order Form §6.3 References Dispatch Center at a Different Address

**Where:** Order Form No. 001 §6.3; Office Lease §1.1 (Premises: 1700 Spring Garden Street, Suite 300); Agreement preamble (Rekaind's principal place of business: 2401 Walnut Street, Suite 600)

**Issue:** The Order Form identifies Rekaind's "primary dispatch center" as being at "Licensee's dispatch operations premises in Philadelphia, Pennsylvania" without specifying the address. The lease is for 1700 Spring Garden Street. Rekaind's registered address (used in the Agreement and for notices) is 2401 Walnut Street. The Notice Letter §8.2 references "Rekaind's dispatch center" for manual monitoring.

**Why it matters:** If the dispatch center relocates (e.g., if Rekaind does not renew the Spring Garden lease after 2030), the alert routing could be affected. The unit register (Order Form §1.3(e)) specifies dispatch contacts per unit, so a relocation would require updating the register. There is no express obligation on Rekaind to notify Velert of a dispatch center address change, though §6.3 and the unit register imply it.

**Recommended fix:** Ensure the unit register and all dispatch contact information are current. If the Spring Garden lease is not renewed, plan the transition of dispatch operations well in advance and update the unit register and Velert's alert routing configuration.

---

### 19. Agreement §15.14 – Bankruptcy Code §365(n) Protection

**Where:** Agreement §15.14

**Issue:** The Agreement expressly provides that the licenses granted are "intellectual property" licenses under §365(n) of the Bankruptcy Code, and Rekaind may exercise all rights and elections under that section.

**Why it matters:** If Velert files for bankruptcy, Rekaind can elect to retain its license to the Platform and require Velert (or its trustee) to perform. This is a valuable protection. However, §365(n) does not preserve indemnification rights or service level commitments—those are contractual obligations that may be rejected by the trustee. Rekaind's protection in a Velert bankruptcy would be limited to the license to use the software, not to the support services, SLAs, or indemnities.

**Recommended fix:** No action required now. Be aware that in a Velert bankruptcy scenario, the practical value of the Platform may diminish significantly even though the license survives.

---

### 20. Service Level Schedule §10.2 – No Reduction of Service Levels

**Where:** Service Level Schedule §10.2

**Issue:** "Licensor shall not reduce the service levels, Response or Resolution targets, Service Credits or recovery objectives in this Schedule for any Order Form during its Subscription Term, except by an amendment signed by both Parties."

**Why it matters:** This is a strong protection for Rekaind. Velert cannot unilaterally degrade the SLA during the term. Combined with the order of precedence (§15.4: Agreement controls over SLS), this means Velert cannot use a general Agreement amendment to reduce SLS commitments—it must specifically amend the SLS with Rekaind's signature.

**Recommended fix:** No action required. This is a favorable provision. Ensure any future amendment discussions do not inadvertently include SLS reductions.

---

## V. SUMMARY OF RECOMMENDED IMMEDIATE ACTIONS

| Priority | Action | Deadline |
|---|---|---|
| 1 | Assess and document arguments for validity of late termination notice (waiver, estoppel, material breach alternative) | Before next communication with Velert |
| 2 | Send follow-up to Velert demanding confirmation of post-April 2027 insurance (tail coverage or renewal policies) through November 20, 2028 | Immediately |
| 3 | Correct refund calculation from $115,811.51 to $114,632.88 and send revised schedule | Before settlement discussions |
| 4 | Retain Ohio litigation counsel in anticipation of venue in Franklin County | Within 2 weeks |
| 5 | Quantify any Year 1 50% device-delay credits Rekaind was entitled to under Order Form §3.4 | Within 2 weeks |
| 6 | Confirm dispatch center power redundancy (generator + UPS) is operational through the transition period | Before November 20, 2026 |