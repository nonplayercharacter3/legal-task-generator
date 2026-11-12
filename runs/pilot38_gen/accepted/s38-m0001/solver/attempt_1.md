# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Bredeix Organic Creamery, LLC – Risk Review of Laipeisk Systems Software Package

---

## Summary

I have reviewed the Software License and Services Agreement (the "Agreement"), Statement of Work No. 2 (the "SOW"), the Data Processing Addendum (the "DPA"), and the insurance certificate cover letter from Halverston Risk Partners (the "Cover Letter"). I identify eleven issues, ordered by materiality to Bredeix. Three issues require a call with the client before we respond to Laipeisk (flagged below).

---

## Issues Requiring a Client Call Before We Respond to Laipeisk

> **⚠️ ISSUES 1, 2, AND 3 below should be discussed with Bredeix's COO and General Counsel before we send any response to Laipeisk.** Issue 1 in particular is time-sensitive: the Northfold closing is expected in Q1 2027, and Phase 2 go-live is April 19, 2027.

---

## Issue 1 – Change of Control Gives Laipeisk a Termination Right at the Worst Possible Moment

**Documents and Sections:**
- Agreement § 16.2 (Assignment; Change of Control)
- SOW § 1.2(b)–(c) (Background – Northfold transaction)

**The Problem.** Agreement § 16.2 provides that any direct or indirect change in control of Licensee, "including any change in control of any entity that directly or indirectly controls Licensee," is deemed an assignment requiring Laipeisk's prior written consent. If a change of control occurs without consent, Laipeisk may terminate the Agreement on thirty (30) days' written notice.

SOW § 1.2(b) records that the sole owner of Bredeix Dairy Holdings, LLC (Bredeix's parent) signed a Unit Purchase Agreement with Northfold Provisions Group on August 28, 2026, with closing expected in Q1 2027. SOW § 1.2(c) then states: *"Nothing in this SOW constitutes Licensor's consent under Section 16.2 of the Agreement."*

In other words, Laipeisk negotiated the Phase 2 schedule with full knowledge of the pending transaction (the SOW was signed September 15, 2026, weeks after the Unit Purchase Agreement), built the go-live date (April 19, 2027) around it, and yet expressly reserved its right to terminate when the deal closes.

**Why It Matters to Bredeix.** Bredeix is a dairy processor running semi-monthly producer pay cycles. If Laipeisk terminates the Agreement upon the Northfold closing:

- The license to HerdLedger ends (§ 14.5), cutting off access to the procurement, payment, quality-tracking, and logistics modules.
- Phase 2 go-live (D2-6, targeted April 19, 2027) could be interrupted or voided.
- Bredeix would be forced to migrate payment processing, quality tracking, and logistics to a new platform mid-implementation, with 90 days of transition assistance at Laipeisk's professional services rates (§ 14.5) – expensive and operationally disruptive.
- The farmer-supplier relationships and payment obligations do not pause for a software transition.

**Recommendation.** Before the Northfold closing, Bredeisk must obtain Laipeisk's written consent under § 16.2, or negotiate an amendment that:

- Carves out the Northfold transaction from the change-of-control termination right; or
- Provides that a change of control of Licensee does not give rise to a termination right so long as the acquirer assumes the Agreement in writing; or
- At minimum, extends the transition-assistance period and reduces the termination notice to 180 days to allow for an orderly migration.

**Proposed language (for an amendment or side letter):**

> *Notwithstanding Section 16.2 of the Agreement, the contemplated acquisition of Bredeix Dairy Holdings, LLC by Northfold Provisions Group (the "Northfold Transaction") shall not constitute a Change of Control requiring Licensor's consent, provided that (a) the surviving or acquiring entity assumes Licensee's obligations under the Agreement in writing no later than the closing of the Northfold Transaction, and (b) Licensee provides written notice of the closing to Licensor within five (5) business days thereafter.*

**Client call needed:** Confirm the expected closing date with Northfold's deal team, and whether the Unit Purchase Agreement contains any covenants about vendor contract consents. We need to know if we have leverage (e.g., Northfold as a condition to closing) or if Bredeix must approach Laipeisk unilaterally.

---

## Issue 2 – DPA Caps Data Breach Liability, Overriding the Agreement's Broader Protection

**Documents and Sections:**
- DPA § 8.1 (Cap)
- Agreement § 11.2 (Cap), § 11.3(c) (Exclusions from Cap)
- DPA Annex 1 (Categories of Personal Data – includes bank account numbers, routing numbers, TINs)
- DPA § 7.5 (Breach Costs)

**The Problem.** Agreement § 11.3(c) excludes "a Party's breach of Section 9 (Confidentiality and Data Security)" from both the indirect-damages waiver and the liability cap. This was presumably negotiated to give Bredeix uncapped recovery for a data security failure.

However, DPA § 8.1 states: *"Notwithstanding Section 11.3(c) of the Agreement, each party's aggregate liability arising out of or relating to this Addendum, including any Personal Data Breach, shall be subject to the Cap."*

The DPA has priority over the Agreement for Personal Data matters (Agreement § 1.3, Order of Precedence). The result: if Laipeisk suffers a breach of farmer-supplier bank account numbers, routing numbers, or taxpayer identification numbers – all of which are in the system per DPA Annex 1 – Bredeix's recovery is capped at the Fees paid in the 12 months preceding the claim.

**Why It Matters to Bredeix.** The Phase 2 SOW adds the farmer-supplier payment module, ACH file generation, and positive-pay files (SOW § 3.2(b)–(c)). The data at risk includes:

- Bank account and routing numbers for every producer (DPA Annex 1)
- Taxpayer identification numbers (DPA Annex 1)
- Payment, premium, and deduction records (DPA Annex 1)

A breach exposing this data would trigger:
- NY SHIELD Act notification obligations (potentially to thousands of individual farmers)
- Vermont breach notification (9 V.S.A. § 2435) for Vermont-based producers
- Credit monitoring for affected data subjects (24 months per DPA § 7.5(c))
- Forensic investigation
- Regulatory fines
- Reputational damage with the farmer-supplier base

The costs of a serious breach of this data could easily exceed $1–2 million, while the 12-month fee cap is likely a fraction of that (the Phase 2 fixed fee alone is $412,000; the subscription fee is in Schedule A but referenced only as "as set out in Licensor's order form").

**Recommendation.** Strike DPA § 8.1 or replace it with language that preserves the Agreement's uncapped treatment for data security breaches:

> *Section 8.1 is deleted in its entirety. Section 11 of the Agreement applies to liability arising out of or relating to this Addendum, including Section 11.3(c), without modification.*

If Laipeisk resists full uncapped liability, a fallback:

> *Notwithstanding Section 11.2 of the Agreement, each Party's aggregate liability arising from a Personal Data Breach caused by such Party's or its Subprocessors' failure to implement the Security Measures described in Annex 2 shall not exceed [three (3) times] the Cap.*

**Client call needed:** Confirm with Bredeix how many farmer-suppliers are in the system and whether any are in Vermont (which triggers the Vermont breach statute in addition to NY SHIELD). This affects the potential exposure calculation we'll use to justify pushing back on the cap.

---

## Issue 3 – Phase 1 Rejection Notice Likely Time-Barred; Live Dispute Over Deemed Acceptance

**Documents and Sections:**
- SOW § 2.1–2.3 (Phase 1 Status)
- Agreement § 6.2 (Rejection Period – 10 days), § 6.5 (Acceptance Upon Use)

**The Problem.** The Phase 1 Deliverable was delivered on July 20, 2026 (SOW § 2.1). Bredeix's Rejection Notice is dated August 7, 2026 (SOW § 2.2) – eighteen (18) days after Delivery. Agreement § 6.2 provides a ten (10) day rejection period, after which the Deliverable is "deemed accepted."

Laipeisk has asserted deemed acceptance. Bredeix disputes it and "reserves all rights" (SOW § 2.2). The identified defects are:
- (a) Duplicate producer records from data migration
- (b) Component test results (butterfat, protein, somatic cell count) posting to the wrong producer account
- (c) Incorrect organic premium rates for producers whose certification renewal dates fall within the current pay period

**Why It Matters to Bredeix.** If deemed acceptance stands:

- Bredeix owes the Phase 1 milestone fee (amount in SOW No. 1, not before us, but presumably material).
- The defects become Bredeix's problem to work around operationally. Defect (b) – mis-posted component test results – directly affects milk-quality payments and could mean Bredeix is over- or under-paying producers. Defect (c) – incorrect organic premiums – means Bredeix is either over-paying (cost) or under-paying (producer relations and potential organic certification audit issues) producers who are in the middle of a certification renewal window.
- SOW § 2.3 provides that Laipeisk will "investigate" the items as part of Phase 2 data-readiness, but this is framed as a Phase 2 service, not a warranty correction. It does not acknowledge a breach or create an obligation to fix at no charge.

**Compounding risk – Agreement § 6.5 (Acceptance Upon Use).** If Bredeix has been using the Phase 1 Deliverable in its live production environment (e.g., processing pay cycles through the producer-intake interface), § 6.5 provides that such use "constitutes acceptance." This is independent of the 10-day period and may be Laipeisk's stronger argument.

**Recommendation.**

1. **Immediate:** Confirm with Bredeix whether the Phase 1 Deliverable has been used in a live production environment. If yes, § 6.5 is likely triggered and the deemed-acceptance argument under § 6.2 becomes moot. We need to assess whether there is any equitable argument (e.g., use was in reliance on Laipeisk's representations, or use was limited and not for "business purposes" in the full sense).

2. **Negotiating position:** Even if acceptance is deemed to have occurred, the defects described in SOW § 2.2 are material and ongoing. We should:
   - Demand that SOW § 2.3 be recharacterized as a warranty correction obligation under Agreement § 8.2 (Software Warranty), with the 30-day correction period running from the date of the SOW (September 15, 2026) rather than being subsumed into Phase 2 data-readiness activities.
   - Seek a credit or reduction against the Phase 1 milestone fee proportional to the cost of remediating the defects.
   - Add a specific acceptance criterion in the Phase 2 data-readiness deliverable (D2-1) that the Phase 1 defects are resolved and verified.

3. **Process fix going forward:** The 10-day rejection period in § 6.2 is too short for a complex dairy implementation. Negotiate an extension to 30 days, or at minimum tie the period to the completion of parallel testing (which for D2-2 is two full pay cycles per SOW § 4.3).

**Proposed language (for SOW amendment):**

> *Section 2.3 is amended to read: "Licensor shall correct the nonconformities identified in Section 2.2 within thirty (30) days of the SOW Effective Date, at no additional charge, in accordance with Section 8.2 of the Agreement. Correction of these items is a precondition to acceptance of Deliverable D2-1. If Licensor fails to correct any item within the thirty (30) day period, Licensee may withhold the milestone fee for D2-1 until correction is complete."*

**Client call needed:** We must confirm (a) whether the Phase 1 system is in live production use, (b) the amount of the Phase 1 milestone fee, and (c) whether any producer payments have already been affected by defects (b) or (c). If producers have been mis-paid, there may be regulatory or contractual exposure to Bredeix independent of the software dispute.

---

## Issue 4 – "Acceptance Upon Use" Creates a Trap for Production Environments

**Documents and Sections:**
- Agreement § 6.5 (Acceptance Upon Use)

**The Problem.** § 6.5 provides: *"Licensee's use of a Deliverable in a live production environment for its business purposes, other than for testing, constitutes acceptance of that Deliverable."*

**Why It Matters to Bredeix.** Bredeix runs semi-monthly producer pay cycles. If a new module (e.g., the payment module in D2-2) is partially deployed and Bredeix uses it to process even one pay cycle to meet a deadline, that use constitutes acceptance – even if the module has unresolved defects. There is no cure period, no right to reject after the fact, and no distinction between "we used it because we had to" and "we evaluated it and found it conforming."

This is particularly dangerous for the Phase 2 payment module: if the ACH file interface (D2-3) has a bug but Bredeix uses it to cut a pay cycle, the module is accepted, and Bredeix bears the cost of fixing any incorrect payments to producers.

**Recommendation.** Amend § 6.5 to:

> *Licensee's use of a Deliverable in a live production environment for its business purposes, other than for testing, constitutes acceptance of that Deliverable only if such use continues for more than fifteen (15) consecutive days without Licensee providing written notice of a material nonconformity. If Licensee provides such notice within the fifteen (15) day period, the acceptance testing procedures in Sections 6.1 and 6.2 shall apply.*

Alternatively, add a "forced use" exception:

> *For the avoidance of doubt, Licensee's use of a Deliverable in production solely to meet a regulatory or contractual deadline (including a producer pay deadline) shall not constitute acceptance if Licensee notifies Licensor in writing within five (5) business days after such use of the specific nonconformity that necessitated the use.*

---

## Issue 5 – Five-Year Auto-Renewal with a Narrow Non-Renewal Window

**Documents and Sections:**
- Agreement § 14.1 (Initial Term – 3 years), § 14.2 (Renewal – successive 5-year terms)

**The Problem.** The Initial Term is 3 years (April 1, 2025 – March 31, 2028). Thereafter, the Agreement renews automatically for successive **five (5) year** terms unless either party gives notice of non-renewal between 90 and 120 days before the end of the then-current term.

**Why It Matters to Bredeix.**

- If the Northfold transaction closes and Bredeix (now a Northfold subsidiary) wants to exit or renegotiate, it is locked in for five years from April 1, 2028 through March 31, 2033, unless it gives notice between December 1, 2027 and January 30, 2028 (90–120 days before March 31, 2028).
- That notice window falls just after the expected Northfold closing (Q1 2027) and during the Phase 2 implementation. Bredeix's post-acquisition integration team may not be aware of the deadline.
- A five-year renewal is a long commitment for software that may be superseded by Northfold's enterprise systems.

**Recommendation.**

- Shorten the renewal term from 5 years to 1 year (auto-renewing annually).
- Widen the non-renewal notice window to 180 days.
- Add a termination right for convenience upon a change of control of Licensee (to complement the fix for Issue 1).

**Proposed language:**

> *Section 14.2 is amended to read: "On expiry of the Initial Term, this Agreement shall renew automatically for successive one (1) year Renewal Terms unless either Party gives the other written notice of non-renewal at least one hundred eighty (180) days before the end of the then-current term. Notwithstanding the foregoing, following a Change of Control of Licensee, Licensee may terminate this Agreement for convenience on one hundred eighty (180) days' written notice, with a pro rata refund of prepaid Fees for the period after termination."*

---

## Issue 6 – No Service Credits or Liquidated Damages for Late Delivery or Downtime

**Documents and Sections:**
- SOW § 5.1 ("commercially reasonable efforts" to meet target dates)
- Agreement § 4.2 (99.5% availability, no service credits specified)
- Agreement § 16.4 (Force Majeure – 60-day termination of affected SOW only)

**The Problem.**

- The SOW schedule uses "target dates" and "commercially reasonable efforts" (SOW § 5.1). There is no liquidated damages clause, no service credit, and no termination right if a target date is missed by more than a de minimis period. The only remedy for late delivery is the general material-breach/termination path in Agreement § 14.3 (30-day cure period).
- The 99.5% availability SLA (Agreement § 4.2) permits approximately 3.6 hours of downtime per month. There are no service credits for failure to meet the SLA. For a dairy processor, 3.6 hours of downtime that hits a pay-cycle cutoff is operationally catastrophic, yet the only remedy is to argue material breach after the fact.

**Why It Matters to Bredeix.** Phase 2 go-live is April 19, 2027. If it slips by even a few weeks, Bredeix may miss a pay cycle or be forced to run parallel systems (old and new) simultaneously, increasing error risk. The milk-quality module flags antibiotic-residue and somatic-cell thresholds (SOW § 3.2(d)); downtime during a lab-results window could mean non-compliant milk is not flagged in time.

**Recommendation.**

1. Add service credits for availability:

> *If the Software is available less than 99.5% in any calendar month, Licensor shall credit Licensee [1]% of the monthly subscription fee for each 0.1% below 99.5%, up to a maximum credit of [10]% of the monthly fee. If the Software is available less than 99.0% in any calendar month, Licensee may terminate the affected module license on written notice and receive a pro rata refund.*

2. Add a longstop date for Phase 2 go-live:

> *If Delivery of D2-6 (Production Go-Live) has not occurred by May 31, 2027 (the "Longstop Date"), Licensee may terminate this SOW on written notice and receive a refund of all milestone fees paid for undelivered Deliverables, without prejudice to Licensee's other rights under the Agreement.*

3. Convert "target dates" to firm dates with a defined cure period, or at minimum add: *"If any target date is delayed by more than fifteen (15) days for reasons within Licensor's control, Licensee may reduce the applicable milestone fee by [5]% for each week of delay, up to a maximum reduction of [20]%."*

---

## Issue 7 – Software Warranty Provides No Remedy for Consequential Losses from Payment Errors

**Documents and Sections:**
- Agreement § 8.2 (Software Warranty – exclusive remedy is correction or termination + pro rata refund)
- Agreement § 11.1 (Exclusion of indirect/consequential damages, lost profits)

**The Problem.** The Software Warranty (§ 8.2) makes correction (or termination with pro rata refund) the *exclusive* remedy for software that fails to perform in accordance with the Documentation and Specifications. Combined with the indirect-damages exclusion in § 11.1, Bredeix has no contractual remedy for:

- Incorrect producer payments that Bredeix must reissue out of pocket
- Lost revenue from downtime during a processing window
- Costs of reconciling mis-posted quality data
- Fines or penalties from organic certification auditors if quality records are inaccurate

**Why It Matters to Bredeix.** The Phase 2 payment module calculates base price, component pricing, quality premiums, deductions, organic premiums, hauling charges, and cooperative/checkoff deductions (SOW § 3.2(b)). An error in any of these calculations, if not caught in the parallel testing phase, would result in incorrect payments to producers. Bredeix would bear the cost of correcting those payments, and potentially face producer disputes or cooperative audit findings.

**Recommendation.** Carve payment-accuracy errors out of the exclusive-remedy and consequential-damages provisions:

> *Notwithstanding Sections 8.2 and 11.1, if the Software calculates producer pay in a manner that does not conform to the Specifications in Exhibit 1 to the applicable Statement of Work, and Licensee issues payments to producers based on such nonconforming calculations, Licensor shall reimburse Licensee for the reasonable costs of correcting such payments (including reissue of payments, producer communication, and reconciliation), up to an amount equal to [two (2) times] the Cap. This reimbursement is in addition to, and not in lieu of, Licensor's obligation to correct the Software under Section 8.2.*

---

## Issue 8 – Bredeix Is Not an Additional Insured on the Most Relevant Policies

**Documents and Sections:**
- Cover Letter § 3.1 (Additional insured on CGL only)
- Agreement § 12.1 (Required coverage includes Tech E&O and Cyber)
- Cover Letter § 2.1 (Policy table – Tech E&O and Cyber are claims-made)

**The Problem.** Bredeix is named as an additional insured only on the Commercial General Liability policy (Cover Letter § 3.1). It has no additional insured status on the Technology E&O policy or the Cyber Liability policy – the two coverages most relevant to a software and data-processing relationship.

Additionally, both the Tech E&O and Cyber policies are **claims-made** (Cover Letter § 2.3). This means a claim must be *made* during the policy period (July 1, 2026 – July 1, 2027) to be covered. If a data breach occurs in June 2027 but is not discovered (and no claim is made) until August 2027, after the policy has expired and before the renewal takes effect, there may be a coverage gap.

**Why It Matters to Bredeix.** If Laipeisk causes a data breach or a software failure that results in a third-party claim (e.g., a producer sues Bredeix for incorrect payments, or a regulator fines Bredeix for a data security failure), Bredeix's recovery depends on:

1. Its contractual rights against Laipeisk (subject to the cap – see Issue 2), and
2. Laipeisk's insurance.

But Bredeix cannot directly claim under Laipeisk's Tech E&O or Cyber policies because it is not an additional insured. If Laipeisk is insolvent or the insurer denies the claim, Bredeix has no direct path to the insurance proceeds.

**Recommendation.**

1. Require Bredeix to be named as an additional insured on the Tech E&O and Cyber policies, or at minimum as a "loss payee" or "certificate holder with direct claim rights."
2. Require tail coverage: the claims-made policies should include a six-month extended reporting period after cancellation or non-renewal.
3. Require notice of any change in the claims-made policy (including retroactive date changes) at least 60 days in advance.

**Proposed language (for an insurance rider or amendment to § 12.2):**

> *Licensor shall cause the Technology Errors and Omissions policy and the Cyber Liability policy to name Licensee as an additional insured, or to provide that Licensee may make a direct claim under such policies for losses for which Licensor is obligated to indemnify or reimburse Licensee under this Agreement. Such policies shall include an extended reporting period of not less than six (6) months following cancellation or non-renewal. Licensor shall provide at least sixty (60) days' prior written notice of any change to the retroactive date, limits, or terms of such policies.*

---

## Issue 9 – Insurance Policy Period Does Not Align with Agreement Term

**Documents and Sections:**
- Cover Letter § 2.1 (Policies run July 1, 2026 – July 1, 2027)
- Agreement § 12.1 (Coverage required "During the Term and for two (2) years afterward")
- Agreement § 14.1 (Initial Term: 3 years from April 1, 2025 = through March 31, 2028)

**The Problem.** The Agreement requires Laipeisk to maintain insurance "during the Term and for two (2) years afterward" – i.e., through at least March 31, 2030 (and longer if the agreement renews). The current policies expire July 1, 2027. The Cover Letter (§ 4.2) states that an updated certificate will be sent at renewal, but there is no contractual guarantee that the renewal will maintain the same limits, the same claims-made structure, or the same insurers.

**Why It Matters to Bredeix.** If the policies are not renewed on equivalent terms, or if the insurer changes to one with a weaker rating, Bredeix's indirect protection (through Laipeisk's insurance) diminishes at exactly the time when Phase 2 is going live and the data footprint is expanding.

**Recommendation.**

- Add to Agreement § 12.2: *"Licensor shall provide evidence of renewal coverage no later than thirty (30) days before the expiration of any policy required under Section 12.1. Renewal coverage shall maintain limits no lower than those required by Section 12.1 and insurers with A.M. Best ratings no lower than A- VII. If Licensor fails to provide such evidence, Licensee may, at its option, (a) terminate the affected Services on written notice, or (b) require Licensor to post a letter of credit in an amount equal to the applicable policy limit."*
- Calendar the July 1, 2027 renewal date and follow up for the updated certificate.

---

## Issue 10 – Indemnity Exception for "Licensee Data" Is Overly Broad

**Documents and Sections:**
- Agreement § 10.2(c) (Indemnity exception for claims arising from Licensee Data)
- Agreement § 10.4 (Licensee indemnity to Licensor for Licensee Data submitted in violation of law)

**The Problem.** Section 10.2(c) provides that Laipeisk has no IP indemnity obligation to the extent a claim arises from "Licensee Data." Given the breadth of the "Licensee Data" definition (Agreement § 1.1(h): "all data and information, including Personal Data, that Licensee or its Users submit to, or that is generated from Licensee's use of, the Software"), this exception could swallow the indemnity.

For example, if a third party claims that the *output* of the payment module (which is "generated from Licensee's use of the Software" and thus "Licensee Data") infringes a patent, Laipeisk could argue the exception applies. Or if the ACH file format that the Software generates is accused of infringing, Laipeisk could say the file is "Licensee Data."

**Why It Matters to Bredeix.** The payment module generates ACH files and positive-pay files (SOW § 3.2(c)). These are functional outputs of the Software, not raw data submitted by Bredeix. If an IP claim arises from the way the Software structures or formats these files, Bredeix should have the benefit of Laipeisk's indemnity.

**Recommendation.** Narrow § 10.2(c):

> *Section 10.2(c) is amended to read: "Licensee Data that was submitted by Licensee independently of the Software and that does not incorporate any Software functionality, configuration, or output format."*

Or, more simply:

> *The exception in Section 10.2(c) shall not apply to any claim to the extent it arises from the Software's processing, formatting, calculation, or output of Licensee Data.*

---

## Issue 11 – Subprocessor List Is Thin and the Objection Mechanism Is Weak

**Documents and Sections:**
- DPA Annex 3 (Authorized Subprocessors: AWS, Zendesk, Twilio/SendGrid)
- DPA § 6.3 (New Subprocessors – 30-day notice, objection, termination of "affected Services")

**The Problem.**

- The subprocessor list includes only three entities. Given that the Software handles ACH payment files, positive-pay files, and ERP interfaces (SOW § 3.2(c), (f)), it is likely that additional subprocessors are involved (e.g., a payment processor, an identity-verification service, a backup provider other than AWS). The list may be incomplete.
- DPA § 6.3 allows Bredeix to object to a new subprocessor on "reasonable data protection grounds," but the remedy for an unresolved objection is termination of only the "affected Services" – not the entire Agreement. For a payment module, "affected Services" could be interpreted narrowly (e.g., only the email notification subprocessor), leaving the core data processing intact with the objectionable subprocessor still in the chain.
- There is no right to audit subprocessors directly; the audit right in DPA § 10.2 is limited to Licensor.

**Why It Matters to Bredeix.** Farmer-supplier bank account data and TINs are flowing through this subprocessor chain. If an unlisted or objectionable subprocessor gains access to that data, Bredeix's ability to respond is limited.

**Recommendation.**

1. Require Laipeisk to confirm in writing that the Annex 3 list is complete as of the SOW Effective Date and that no other entity processes Personal Data on Bredeix's behalf.
2. Strengthen the objection remedy:

> *If the Parties cannot resolve Licensee's objection to a new Subprocessor within the period specified in Section 6.3, Licensee may (a) terminate the affected Services, or (b) require Licensor to remove the objected-to Subprocessor from the processing chain for Licensee's Personal Data within thirty (30) days, failing which Licensee may terminate this Addendum and the Agreement.*

3. Add: *"Licensor shall provide Licensee with a list of all Subprocessors, including any Subprocessor's Subprocessors (downstream processors), that have access to Licensee's Personal Data, and shall update such list within ten (10) days of any change."*

---

## Additional Observations (Lower Priority)

| # | Observation | Document / Section | Note |
|---|---|---|---|
| A | Support hours are 6 a.m.–8 p.m. ET, 7 days/week (Agreement § 4.3). Severity-1 response is 2 hours. | Agreement § 4.3 | Acceptable for a dairy operation, but confirm what constitutes "severity one" – if a pay-cycle failure is severity one, the 2-hour response is critical. No definition of severity levels is provided. |
| B | Fee adjustment capped at lesser of 3% or CPI (Agreement § 5.5). | Agreement § 5.5 | Reasonable. No action needed. |
| C | Transition assistance is 90 days at "then-current professional services rates" (Agreement § 14.5). | Agreement § 14.5 | Rates are not defined in the Agreement. The SOW lists rates for Phase 2 ($195–$245/hr), but "then-current" could be higher. Consider fixing a rate or capping transition fees. |
| D | The SOW excludes migration of historical producer pay data from before January 1, 2025 (SOW § 3.3(b)). | SOW § 3.3(b) | Confirm with Bredeix whether it needs historical data in the new system for audit, cooperative reporting, or producer disputes. If yes, this should be added by change order before go-live. |
| E | Training is limited to six half-day sessions (SOW § 3.2(g)). | SOW § 3.2(g) | For a system that replaces manual pay calculation across procurement, field-service, and accounts-payable staff, six half-days may be insufficient. Consider whether additional training should be included in the fixed fee or priced at a discounted rate. |

---

## Recommended Next Steps

1. **Call with Bredeix** (before responding to Laipeisk) to discuss Issues 1, 2, and 3. Specifically:
   - Confirm the Northfold closing timeline and whether the Unit Purchase Agreement addresses vendor consents.
   - Confirm whether Phase 1 is in live production use (triggers § 6.5).
   - Quantify the number of farmer-suppliers and whether any are in Vermont.
   - Confirm whether historical pay data pre-2025 is needed.

2. **Prepare a markup** of the Agreement, SOW, and DPA incorporating the proposed language above.

3. **Send a draft response to Laipeisk** prioritizing:
   - Change-of-control consent / amendment (Issue 1) – time-critical
   - DPA cap override (Issue 2)
   - Phase 1 dispute resolution (Issue 3)
   - Acceptance-upon-use fix (Issue 4)
   - Service credits / longstop date (Issue 6)

4. **Calendar** the July 1, 2027 insurance renewal and the December 1 – January 30, 2028 non-renewal notice window.