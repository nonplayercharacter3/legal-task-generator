# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Bredeix Organic Creamery, LLC – Review of Laipeisk Systems Software Package: Risk Issues and Recommended Fixes

---

## Summary

I have reviewed the four documents in the matter folder. The package contains several material risks for Bredeix, three of which I believe require a call with the client before we respond to Laipeisk (flagged below). The most pressing issues are: (1) Laipeisk's express reservation of its right to terminate upon the pending Northfold change of control; (2) the DPA's cap on data-breach liability, which overrides the Agreement's otherwise-uncapped treatment of data-security breaches; and (3) the likely loss of Bredeix's right to reject the Phase 1 Deliverable due to a missed 10-day rejection window.

---

## Issues Requiring a Call with the Client Before We Respond to Laipeisk

### 1. Change of Control – Laipeisk's Express Non-Consent and Termination Right

**Document and Section:** Software License Agreement § 16.2; SOW Phase 2 § 1.2(b) and § 1.2(c)

**Issue.** Section 16.2 provides that any direct or indirect change in control of Licensee, "including any change in control of any entity that directly or indirectly controls Licensee," is deemed an assignment requiring Licensor's prior written consent. If it occurs without consent, Licensor may terminate on 30 days' notice.

SOW § 1.2(b) acknowledges that on August 28, 2026, the sole owner of Bredeix Dairy Holdings, LLC (Bredeix's parent) signed a Unit Purchase Agreement with Northfold Provisions Group, with closing expected in Q1 2027. SOW § 1.2(c) then states: "Nothing in this SOW constitutes Licensor's consent under Section 16.2 of the Agreement."

**Why it matters.** The Northfold closing will almost certainly constitute a change in control of an entity that directly controls Licensee. Laipeisk has put Bredeix on written notice that it does not consent and reserves its termination right. If the deal closes and Laipeisk terminates, Bredeix (or Northfold) loses the HerdLedger platform mid-Phase 2 implementation, with no refund of the remaining Phase 2 fixed fee ($412,000 less milestones already paid) and no transition assistance beyond what § 14.5 provides at Laipeisk's then-current rates. The acquisition is the single most important corporate event for Bredeix in the next 12 months, and this clause gives Laipeisk a de facto veto or, at minimum, significant leverage to extract better economic terms.

**Recommended fix.** Before the Northfold closing, negotiate a side letter or amendment in which Laipeisk:
- consents in advance to the specific change of control described in SOW § 1.2(b);
- waives its termination right under § 16.2 for that transaction; and
- confirms that the Agreement and all SOWs remain in full force and effect post-closing.

**Proposed language (side letter):**

> "Licensor hereby consents to the change in control of Bredeix Dairy Holdings, LLC contemplated by the Unit Purchase Agreement dated August 28, 2026 between the sole owner of Bredeix Dairy Holdings, LLC and Northfold Provisions Group (the 'Transaction'). Licensor waives its right to terminate the Agreement under Section 16.2 by reason of the Transaction. The Agreement and all Statements of Work shall remain in full force and effect following closing of the Transaction. For the avoidance of doubt, nothing in this letter constitutes consent to any other change in control."

**Client call needed to confirm:** (a) whether Northfold is aware of this issue and expects it to be resolved pre-closing; (b) whether the client is willing to give Laipeisk any economic concession (e.g., a fee bump or extended term) in exchange for consent; and (c) the expected closing date, so we can time the negotiation.

---

### 2. DPA Caps Data-Breach Liability – Overrides the Agreement's Uncapped Treatment

**Document and Section:** DPA § 8.1; Agreement § 11.3(c); Agreement § 1.3 (order of precedence)

**Issue.** Agreement § 11.3(c) provides that the liability cap in § 11.2 does *not* apply to "a Party's breach of Section 9 (Confidentiality and Data Security)." This would leave data-breach exposure uncapped. However, DPA § 8.1 states: "Notwithstanding Section 11.3(c) of the Agreement, each party's aggregate liability arising out of or relating to this Addendum, including any Personal Data Breach, shall be subject to the Cap."

Under Agreement § 1.3, the DPA has priority "as to Personal Data." Therefore, DPA § 8.1 controls, and all data-breach liability is capped at the Fees paid in the 12 months preceding the claim.

**Why it matters.** Annex 1 to the DPA identifies the Personal Data at issue as including farmer-supplier bank account numbers, routing numbers, taxpayer identification numbers, and payment records. A breach of this data set would expose Bredeix to: (a) SHIELD Act penalties (up to $5,000 per knowing or reckless violation, with no cap); (b) Vermont breach-notification obligations; (c) costs of forensics, notification, call-center support, and 24 months of credit monitoring for every affected farmer-supplier; (d) potential class-action litigation; and (e) reputational harm with the organic farming community. The Cap (12 months of subscription fees, which per Schedule A is set by the order form and not stated in the documents we have) is almost certainly a small fraction of a realistic worst-case breach cost.

**Recommended fix.** Strike DPA § 8.1 in its entirety, or amend it to carve out Personal Data Breaches from the Cap, consistent with Agreement § 11.3(c).

**Proposed language (amended DPA § 8.1):**

> "8.1 **Cap.** Section 11 of the Agreement applies to liability arising out of or relating to this Addendum. For the avoidance of doubt, the exclusions in Section 11.3 of the Agreement, including Section 11.3(c) (breach of Section 9), apply in full to liability under this Addendum."

Alternatively, if Laipeisk insists on a cap for data breaches, negotiate a super-cap of no less than $5,000,000 (matching the cyber insurance limit) specifically for Personal Data Breach claims.

**Client call needed to confirm:** (a) the actual annual subscription fee (to calculate the current Cap); (b) the number of farmer-suppliers whose data is in the system (to model worst-case breach cost); and (c) the client's risk tolerance – whether it will accept a super-cap in lieu of full uncapped liability.

---

### 3. Phase 1 Deliverable – Missed Rejection Window and Deemed Acceptance

**Document and Section:** Agreement § 6.2, § 6.5; SOW Phase 2 § 2.1, § 2.2, § 2.3

**Issue.** SOW § 2.1 states that Delivery of the Phase 1 Deliverable occurred on July 20, 2026. SOW § 2.2 states that Bredeix's Rejection Notice is dated August 7, 2026 – 18 days after Delivery. Agreement § 6.2 provides a 10-day rejection window and deems the Deliverable accepted if no Rejection Notice is delivered in time. Laipeisk has asserted deemed acceptance.

Compounding this, Agreement § 6.5 provides that "Licensee's use of a Deliverable in a live production environment for its business purposes, other than for testing, constitutes acceptance." The Phase 1 Deliverable included the procurement module and the producer-intake interface for Bredeix's receiving stations. If Bredeix has been using either of these in production (which is likely, given that milk receipts are daily), Laipeisk could argue acceptance under § 6.5 even earlier than the § 6.2 deadline.

The identified defects are operationally significant:
- (a) duplicate producer records in the master file;
- (b) component test results (butterfat, protein, somatic cell count) posting to the wrong producer account; and
- (c) incorrect organic premium rates for producers whose certification renewal falls within the pay period.

Defect (c) directly affects Bredeix's organic premium obligations to farmers and could result in underpayment (creating a liability to producers and potential organic-certification issues) or overpayment (a financial loss).

SOW § 2.3 provides that Laipeisk will "investigate" these items as part of Phase 2 data-readiness work (SOW § 3.2(a)), but this is framed as a Phase 2 service, not a warranty correction under § 8.2 or a § 6.3 remediation obligation.

**Why it matters.** If the Phase 1 Deliverable is deemed accepted, Bredeix:
- owes the Phase 1 milestone fee (amount not stated in the documents we have, but it was a separate SOW);
- loses the right to compel correction under § 6.3;
- loses the § 6.4 repeated-failure termination right; and
- is left with only the § 8.2 software warranty (fix-or-terminate, no damages) for any ongoing nonconformity.

Given that the defects affect daily milk-receipt operations and organic premium calculations, this is not a theoretical risk.

**Recommended fix.** This is a fact-intensive dispute. Before pushing back on Laipeisk, we need to confirm:
- the exact date Bredeix first used the Phase 1 Deliverable in production (if at all, and if so, which components);
- whether the Rejection Notice was sent by email, courier, or hand delivery, and when it was actually received by Laipeisk (the 10-day clock runs from "Delivery," defined in § 1.1(e) as Licensor's written notice that the Deliverable is "ready for acceptance testing" – we need to confirm the date of that notice, which may differ from the date the files were loaded into the test environment); and
- whether the Phase 1 milestone fee has been paid or is in dispute.

If the facts support it, argue that:
- "Delivery" under § 1.1(e) requires Licensor's *written notice* of readiness, and if that notice postdates July 20, the 10-day window may not have run by August 7; or
- at minimum, Bredeix should not be deemed to have "used" the Deliverable in production under § 6.5 if the known defects (wrong premium rates, misposted component results) made production use impracticable or if Bredeix was running its legacy system in parallel.

If the deemed-acceptance position is strong, negotiate a commercial resolution: a credit or fee reduction against Phase 2 milestones in exchange for Bredeix's agreement that the Phase 1 Deliverable is accepted, coupled with a binding commitment that Laipeix will correct the three identified defects at its own cost within a specified timeframe (e.g., 30 days) as a condition of Phase 2 go-live.

**Client call needed to confirm:** (a) the date of Laipeisk's written Delivery notice for Phase 1; (b) whether and when Bredeix used any Phase 1 component in production; (c) whether the Phase 1 milestone fee has been paid; and (d) the client's commercial position – whether it prefers to litigate the acceptance issue or trade it for a Phase 2 concession.

---

## Additional Issues (in descending order of importance)

### 4. Five-Year Automatic Renewal with Narrow Non-Renewal Window

**Document and Section:** Agreement § 14.1, § 14.2

**Issue.** The Initial Term is 3 years. On expiry, the Agreement renews automatically for successive **five-year** terms unless either party gives notice of non-renewal between 90 and 120 days before the end of the then-current term.

**Why it matters.** If Bredeix misses the 90–120 day window at the end of the Initial Term (April 1, 2028), it is locked in until at least April 1, 2033. For a company undergoing a change of control, the acquirer (Northfold) may have its own systems strategy and may not want a 5-year commitment to HerdLedger. The asymmetry is notable: the Initial Term is 3 years, but renewals jump to 5 years.

**Recommended fix.** Shorten the renewal term to 1 year, or at minimum 3 years, to match the Initial Term. Alternatively, extend the non-renewal notice window to 180 days.

**Proposed language (amended § 14.2):**

> "On expiry of the Initial Term, this Agreement shall renew automatically for successive one (1) year Renewal Terms unless either Party gives the other written notice of non-renewal not more than one hundred eighty (180) days nor fewer than one hundred twenty (120) days before the end of the then-current term."

---

### 5. Bredeix Is Not an Additional Insured on the Technology E&O or Cyber Policies

**Document and Section:** Insurance Certificate Cover Letter § 3.1; Agreement § 12.2

**Issue.** The cover letter confirms that Bredeix is named as an additional insured only on the commercial general liability policy (Ashmore Mutual). It is not an additional insured on the Technology E&O policy (Corvane Specialty) or the Cyber Liability policy (Corvane Specialty).

Agreement § 12.2 requires Bredeix to be named as an additional insured on the CGL policy but is silent on the E&O and Cyber policies.

**Why it matters.** The most likely claims against Laipeisk in this relationship are technology failures (E&O) and data breaches (Cyber). If Bredeix suffers a loss from a software defect or a data breach, it must sue Laipeisk and rely on Laipeisk's insurance responding. As an additional insured on those policies, Bredeix could make a direct claim against the insurer, bypassing any dispute over Laipeisk's liability or solvency. Without that status, Bredeix's recovery depends entirely on Laipeisk's willingness (and ability) to pay.

**Recommended fix.** Amend Agreement § 12.2 to require Bredeix to be named as an additional insured on the Technology E&O and Cyber Liability policies as well.

**Proposed language (amended § 12.2, added sentence):**

> "Licensee shall be named as an additional insured on the commercial general liability policy and on the technology errors and omissions and cyber liability policies, to the extent such policies permit additional insured status."

---

### 6. Claims-Made Insurance Policies – Coverage Gap Risk

**Document and Section:** Insurance Certificate Cover Letter § 2.1, § 2.3

**Issue.** The Technology E&O and Cyber Liability policies are written on a claims-made basis. The current policy period is July 1, 2026 to July 1, 2027. The retroactive date is January 1, 2019.

**Why it matters.** A claims-made policy only covers claims *made* during the policy period (or within any extended reporting period). Phase 2 go-live is targeted for April 19, 2027, with hypercare covering two semi-monthly pay cycles thereafter (potentially into June 2027). If a defect in the Phase 2 payment module causes an error that is not discovered until after July 1, 2027 (e.g., a subtle miscalculation that only surfaces in a quarterly cooperative audit), no claim can be made under the current policy. The cover letter states an updated certificate will be sent at renewal, but there is no contractual obligation on Laipeisk to maintain continuous claims-made coverage with a retroactive date no later than January 1, 2019.

**Recommended fix.** Add to Agreement § 12.1 a requirement that claims-made policies maintain a retroactive date no later than the Effective Date of the Agreement (April 1, 2025) or, preferably, January 1, 2019, and that there be no gap in coverage between policy periods.

**Proposed language (added to § 12.1):**

> "To the extent any required coverage is written on a claims-made basis, Licensor shall maintain a retroactive date no later than April 1, 2025, and shall not permit any gap in coverage between successive policy periods."

---

### 7. Software Warranty – Exclusive Remedy Is Fix-or-Terminate, No Damages

**Document and Section:** Agreement § 8.2

**Issue.** The exclusive remedy for breach of the software warranty is: (a) Licensor corrects the nonconformity within 30 days; or (b) if it does not, Licensee may terminate and receive a pro rata refund of prepaid subscription fees. There is no right to consequential damages, even for a software failure that causes Bredeix to miss a pay cycle, mispay farmers, or lose production data.

**Why it matters.** For a dairy processor on a semi-monthly pay cycle, a software failure during a pay period could mean: delayed payments to hundreds of farmers (creating goodwill damage and potential breach of producer contracts), incorrect payments (creating a cash-flow problem to correct), or system downtime during milk-receipt operations. The fix-or-terminate remedy does not compensate for any of this.

**Recommended fix.** Add a service-credit mechanism for availability failures and a carve-out from the exclusive-remedy language for failures that cause Bredeix to miss a producer pay deadline.

**Proposed language (new § 8.6):**

> "8.6 **Pay-Cycle Protection.** If a failure of the Software causes Licensee to be unable to process a producer pay cycle by the scheduled pay date, Licensor shall (a) use all available personnel to restore the Software within twenty-four (24) hours; and (b) reimburse Licensee for any additional costs incurred to process the pay cycle through alternative means (e.g., manual processing, temporary staffing), up to a maximum of $[X] per occurrence."

---

### 8. Availability SLA Is Weak – "Commercially Reasonable Efforts" and 99.5%

**Document and Section:** Agreement § 4.2

**Issue.** The availability commitment is 99.5% per calendar month, achieved through "commercially reasonable efforts," excluding scheduled maintenance with 48 hours' notice. 99.5% permits approximately 3.6 hours of downtime per month. There is no service-credit or remedy for missing the target.

**Why it matters.** Bredeix operates milk-receiving stations in New York and Vermont. Downtime during receiving hours means producers cannot check in, component tests cannot be recorded, and the daily milk flow is disrupted. A 3.6-hour monthly allowance, with no financial consequence, gives Laipeisk little incentive to prioritize availability.

**Recommended fix.** (a) Raise the target to 99.9%; (b) replace "commercially reasonable efforts" with a firm obligation; (c) add service credits for missed availability.

**Proposed language (amended § 4.2):**

> "4.2 **Availability.** Licensor shall make the Software available 99.9% of the time in each calendar month, excluding scheduled maintenance notified to Licensee at least seventy-two (72) hours in advance. If availability in any calendar month falls below 99.9%, Licensee shall be entitled to a credit of [X]% of the monthly subscription fee for each full 0.1% below the target, up to a maximum credit of [Y]% of the monthly fee. Credits shall be applied against the next invoice."

---

### 9. "Acceptance Upon Use" Is Overly Broad

**Document and Section:** Agreement § 6.5

**Issue.** "Licensee's use of a Deliverable in a live production environment for its business purposes, other than for testing, constitutes acceptance of that Deliverable." This is not limited to use of the specific Deliverable in question – it could be argued that using *any* part of the Software in production accepts *all* Deliverables.

**Why it matters.** In a phased implementation, Bredeix will inevitably use earlier-phase components (e.g., the Phase 1 procurement module) in daily operations while later-phase Deliverables are still being tested. Laipeisk could argue that production use of any component constitutes acceptance of all Deliverables, gutting the § 6.1–6.4 acceptance process.

**Recommended fix.** Limit § 6.5 to the specific Deliverable in question and require that the use be for the business purpose the Deliverable was designed to serve.

**Proposed language (amended § 6.5):**

> "6.5 **Acceptance Upon Use.** Licensee's use of a specific Deliverable in a live production environment for the business purpose for which that Deliverable was designed, other than for testing, constitutes acceptance of that Deliverable only. Use of other components of the Software does not constitute acceptance of a Deliverable that has not yet been delivered or tested."

---

### 10. Schedule Has No Consequence for Late Delivery

**Document and Section:** SOW Phase 2 § 5.1

**Issue.** The target dates are governed by "commercially reasonable efforts." There are no liquidated damages, service credits, or termination rights for missed target dates. The only schedule protection is § 5.2, which extends dates if *Licensee* is delayed.

**Why it matters.** The Production Go-Live (D2-6) is targeted for April 19, 2027. If this slips, Bredeix must continue running its legacy payment system in parallel, incurring dual-system costs and risk of errors. There is no financial incentive for Laipeisk to hit the date.

**Recommended fix.** Add a liquidated-damages or fee-credit provision for missed target dates.

**Proposed language (new SOW § 5.3):**

> "5.3 **Late Delivery.** If Licensor fails to give Delivery of any Phase 2 Deliverable by its target date in Section 5.1, and the delay is not attributable to Licensee's failure to meet its responsibilities under Section 7, the applicable milestone fee shall be reduced by [X]% for each week of delay, up to a maximum reduction of [Y]%. If the delay exceeds thirty (30) days, Licensee may terminate this SOW under Section 14.3 of the Agreement without further liability."

---

### 11. Historical Data Migration (Pre-2025) Is Out of Scope

**Document and Section:** SOW Phase 2 § 3.3(b)

**Issue.** Migration of "historical producer pay data from before January 1, 2025" is expressly out of scope.

**Why it matters.** Dairy processors are subject to cooperative reporting, checkoff deductions, and state agricultural tax filings that may require multi-year historical data. Organic certification audits may also look at historical premium payments. If Bredeix needs pre-2025 data in HerdLedger for any of these purposes, it will have to pay for a change order at the hourly rates in SOW § 6.3 ($195–$245/hour).

**Recommended fix.** Confirm with the client whether pre-2025 data is needed. If so, either include it in the SOW scope or negotiate a fixed-fee change order before signing.

---

### 12. Transition Assistance Is Uncapped and at Laipeisk's Rates

**Document and Section:** Agreement § 14.5

**Issue.** On termination, Laipeisk shall provide "reasonable transition assistance for up to ninety (90) days at its then-current professional services rates." There is no cap on the cost, and "then-current rates" could be higher than the rates in the SOW.

**Why it matters.** If the relationship sours (e.g., after the change of control or a Phase 1 dispute), Bredeix may need extensive transition help to migrate off HerdLedger. At $195–$245/hour, 90 days of meaningful transition support could cost six figures.

**Recommended fix.** Cap transition assistance at a fixed fee or at a multiple of the remaining contract-value.

**Proposed language (amended § 14.5, last sentence):**

> "On Licensee's request, Licensor shall provide reasonable transition assistance for up to ninety (90) days at a not-to-exceed fee of $[X], inclusive of all personnel and expenses."

---

### 13. Licensee Responsibility Deadlines Are Tight

**Document and Section:** SOW Phase 2 § 7(b), § 7(c)

**Issue.** Bredeix must provide producer contracts, premium schedules, and organic certification records by **October 15, 2026** (less than one month after the SOW Effective Date of September 15, 2026), and must arrange for its bank and milk-testing lab to provide file specifications and test environments by **November 2, 2026**. Under § 5.2, any delay by Bredeix extends the target dates.

**Why it matters.** These are third-party dependencies (the bank, the lab) that are outside Bredeix's direct control. If the bank or lab is slow to respond, the entire Phase 2 schedule slips, and Bredeix bears the risk of downstream delays (e.g., missing the April 2027 go-live).

**Recommended fix.** (a) Build in a longer window (e.g., 30 days for bank/lab specs); (b) clarify that if the delay is caused by the third party's unreasonableness rather than Bredeix's failure to "arrange" the specification, the schedule should not extend; (c) require Laipeisk to provide a template or data-specification request that Bredeix can forward to the bank and lab immediately.

---

### 14. Subprocessor Termination Right Is Vague

**Document and Section:** DPA § 6.3

**Issue.** If Bredeix objects to a new subprocessor and the parties cannot resolve the objection, "Licensee may terminate the affected Services on written notice." The term "affected Services" is not defined. If the subprocessor in question is AWS (the cloud hosting provider), "affected Services" could arguably encompass the entire hosted platform.

**Why it matters.** Bredeix needs certainty that a subprocessor dispute over, say, a new email vendor (Twilio/SendGrid) does not give it the right – or the risk – of losing the entire platform.

**Recommended fix.** Define "affected Services" to mean only those Services that directly involve the objected-to subprocessor.

**Proposed language (amended DPA § 6.3, last sentence):**

> "…Licensee may terminate only those Services that directly involve the objected-to Subprocessor (the 'Affected Services'). Licensee shall then receive a refund of any prepaid Fees for the Affected Services covering the period after termination. Termination of Affected Services shall not affect Licensee's right to continue using the remainder of the Software and Services."

---

## Non-Issues / Items That Are Acceptable

- **Governing law and jurisdiction (Agreement § 15.1, § 15.3):** New York law and New York County courts. Appropriate given Bredeix is a New York LLC.
- **Order of precedence (Agreement § 1.3):** DPA > Agreement > SOW. Standard and appropriate, though it is what causes Issue #2 above.
- **Fee adjustment cap (Agreement § 5.5):** Limited to the lesser of 3% or CPI. Reasonable.
- **Security measures (DPA Annex 2):** SOC 2 Type II, MFA, AES-256, TLS 1.2+, annual pen testing, 15-day patch SLA for critical vulnerabilities. These are solid.
- **Data location (DPA § 6.4; Agreement § 4.1):** U.S.-only processing. Appropriate.
- **Breach notification (DPA § 7.1; Agreement § 9.6):** 48 hours. Reasonable.
- **Breach cost reimbursement (DPA § 7.5):** Covers notification, call center, 24-month credit monitoring, forensics. Good – but subject to the cap in Issue #2.

---

## Suggested Next Steps

1. **Call with the client** to discuss Issues #1, #2, and #3 (the three flagged above). We need facts on the Phase 1 delivery notice date, production use, and milestone fee status, as well as the client's commercial position on the Northfold consent and the data-breach cap.
2. **Request the order form** referenced in Schedule A to confirm the actual annual subscription fee (needed to calculate the Cap and to assess the economics of a super-cap negotiation).
3. **Request the Phase 1 SOW (SOW No. 1)** to confirm the Phase 1 milestone fee amount and the exact Delivery definition used.
4. **Draft a response letter to Laipeisk** addressing the issues above, prioritizing the change-of-control consent and the DPA cap, with the Phase 1 acceptance dispute handled separately (it may be better resolved commercially than through a formal dispute).