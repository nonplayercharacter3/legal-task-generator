# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Trouseind / Reitaisk – Cobbelly Inflight Kitchens Acquisition: Deal Package Issue List

---

## Summary

I have reviewed all five documents in the matter folder. I identify ten issues, ranging from a proposed side letter that would gut the client's tax indemnity protection to a structural mismatch between the SPA and the Escrow Agreement that would strip the Extended Holdback of its intended purpose. The first four items should be resolved before we return to the other side.

---

## Issue 1 (CRITICAL – Business Decision Required)

**Seller Side Letter Would Reduce Tax Survival to Nine Months**

- **Where:** `seller_side_letter_tax_survival.md`, Section 2.1; compare `stock_purchase_agreement_trouseind_reitaisk.md`, Section 9.1(b).
- **What it says:** The Seller's draft letter agreement deletes SPA Section 9.1(b) in its entirety and replaces it with a fixed nine-month survival period for both the Section 3.14 (Taxes) representations and the Section 9.2(c) Pre-Closing Tax indemnity obligation.
- **Why it matters for Trouseind:**
  - The current SPA provides tax survival until 60 days after expiration of the applicable statute of limitations. For federal income tax, that is generally three years (six years for substantial omissions under IRC § 6501(e)), meaning effective survival of approximately 3.5 to 6.5+ years. The Seller's proposal cuts this to nine months.
  - The Company has been in Seller's consolidated federal group since January 1, 2019 (SPA § 3.14(e)). Section 1.1502-6 imputed underpayment exposure can arise from intercompany transactions years after they occur. A nine-month window will almost certainly expire before the 2026 straddle-period return is filed, let alone before any audit of pre-closing years surfaces.
  - The Extended Holdback Amount ($3,000,000) is not released until the third anniversary of the Closing Date (SPA § 2.4(b); Escrow Agreement § 5.3(b)). If tax survival is only nine months, the funds sit in escrow for two more years securing claims that have already expired. The Seller gets its money back at year three with no meaningful tax risk retained.
  - Pre-Closing Taxes are defined broadly in SPA § 1.1 to include taxes of Seller and its affiliated group under § 1.1502-6 and transferee/successor taxes. Nine months is inadequate to cover any of these.
- **Recommendation:** This requires a business decision from the client. In my view, the nine-month period is unacceptable and should be rejected. If the client wishes to negotiate, a reasonable compromise might be survival until the later of (a) 60 days after expiration of the applicable statute of limitations or (b) the Extended Release Date (third anniversary), which would at least align the survival period with the escrow release. Alternatively, the client could accept a shorter period (e.g., 18 months) only if the Extended Holdback release is accelerated accordingly. The client should also consider whether the $3,000,000 Extended Holdback is sufficient to cover realistic consolidated-group tax exposure, given the Company has been in the group since 2019.

---

## Issue 2 (CRITICAL – Drafting Fix)

**Escrow Agreement's Definition of "Fundamental Representation Claims" Omits Tax and Food Safety Reps**

- **Where:** `escrow_agreement_lanterwick.md`, Section 1.1 (definition of "Fundamental Representation Claims"); compare `stock_purchase_agreement_trouseind_reitaisk.md`, Section 1.1 (definition of "Seller Fundamental Representations") and Section 2.4.
- **What it says:** The Escrow Agreement defines "Fundamental Representation Claims" as claims for breach of Sections 3.1, 3.2, and 3.3 only. The SPA defines "Seller Fundamental Representations" as Sections 3.1, 3.2, 3.3, **3.14 (Taxes)**, and **3.17 (Food Safety and Regulatory Compliance)**. SPA Section 2.4 states that the Extended Holdback Amount secures "claims by Buyer Indemnitees for breach of the Seller Fundamental Representations **and** for Pre-Closing Taxes under Section 9.2(c)." SPA Section 9.6(b) provides that claims for breach of Seller Fundamental Representations or under Section 9.2(c) are recoverable from the Extended Holdback.
- **Why it matters for Trouseind:**
  - As drafted, the $3,000,000 Extended Holdback is available *solely* for organization, authority, and capitalization claims (Escrow Agreement § 5.3(a): "The Extended Holdback Amount shall be available solely for Fundamental Representation Claims"). Food safety claims (Section 3.17) and tax claims (Section 3.14 / Section 9.2(c)) cannot be recovered from the Extended Holdback at all, even after the General Escrow is exhausted.
  - For an inflight food production business, food safety is the highest-risk operational area. A major contamination event or recall would likely generate claims under Section 3.17, which would be limited to the $5,640,000 General Escrow and released to Seller at the 12-month Initial Release Date.
  - The SPA's order of recovery (Section 9.6) and the Escrow Agreement's disbursement rules (Section 5.3) are directly inconsistent. SPA Section 11.10 provides that the SPA prevails over other Transaction Documents "except that the Escrow Agreement shall govern the disbursement of the Escrow Funds." This exception likely means the Escrow Agreement's narrow definition controls for disbursement, defeating the SPA's intended protection.
- **Recommendation:** Amend Escrow Agreement Section 1.1 to define "Fundamental Representation Claims" as claims for breach of the "Seller Fundamental Representations" as defined in the Purchase Agreement (i.e., Sections 3.1, 3.2, 3.3, 3.14, and 3.17), and add Pre-Closing Tax claims under Section 9.2(c). Alternatively, conform the definition to track the SPA's defined term directly. This is a drafting fix, not a business decision, though the Seller may resist.

---

## Issue 3 (HIGH – Drafting Fix)

**TSA Section 8.1: Recipient Indemnifies Provider for Provider's Own Negligence**

- **Where:** `transition_services_agreement.md`, Section 8.1; compare Section 8.2.
- **What it says:** Section 8.1 provides that Recipient (Trouseind) "shall indemnify, defend and hold harmless Provider… from and against all Losses arising out of or relating to the provision or receipt of the Services, **including any negligence of Provider**." The only carve-out is for losses where Provider is obligated to indemnify under Section 8.2, which covers only "gross negligence or willful misconduct."
- **Why it matters for Trouseind:**
  - This inverts the normal allocation of risk in a services agreement. If the Provider is ordinarily negligent—for example, a temperature excursion in the cold chain, a cross-contamination event, a labeling error, or a failure to follow the food safety plan—Trouseind would be contractually obligated to indemnify the Provider for the resulting losses (including third-party claims by airlines or passengers).
  - The Provider's own indemnity (Section 8.2) is triggered only by gross negligence or willful misconduct, a significantly higher threshold. Ordinary negligence—the most common failure mode in food production—is not covered by the Provider's indemnity but *is* covered by the Recipient's indemnity.
  - Combined with the TSA liability cap in Section 9.2 (total Fees paid and payable), Trouseind's recovery from the Provider for a significant food safety incident caused by ordinary negligence would be limited to the cap, while Trouseind's indemnity obligation to the Provider for the same incident is uncapped (Article VIII obligations are excluded from the cap per Section 9.2).
- **Recommendation:** Delete "including any negligence of Provider" from Section 8.1. Section 8.1 should be limited to losses arising from Recipient's own acts or omissions (e.g., failure to provide accurate Customer Specifications, failure to pay Fees). Section 8.2 should be expanded to cover Provider's negligence (not just gross negligence), consistent with the standard of care in Section 2.2. This is a significant negotiating point; the Seller will likely resist, but the current drafting is not market for a TSA where the Provider is performing the core operational function (meal production).

---

## Issue 4 (HIGH – Drafting Fix)

**TSA Section 12.3: Provider May Assign or Delegate Without Recipient's Consent**

- **Where:** `transition_services_agreement.md`, Section 12.3.
- **What it says:** "Provider may assign or delegate this Agreement, or any of its rights or obligations hereunder, in whole or in part, to any Person without the consent of Recipient."
- **Why it matters for Trouseind:**
  - The Provider could transfer the Meal Production Services to an unknown third party—potentially a competitor, a lower-cost operator with inferior food safety systems, or an entity with no relevant experience—without any approval right for Trouseind.
  - Section 12.2 restricts production to the Milwaukee Commissary but does not restrict *who* operates it. A new operator could be in place overnight.
  - Airline customers have their own vendor approval and audit requirements. An unapproved substitution could breach airline contracts and trigger customer claims.
  - The non-compete in SPA Section 6.2 carves out "performing the Transition Services Agreement," so if the Seller assigns the TSA to a third party, that third party could arguably produce inflight meals within 150 miles of the Company's facilities without violating the non-compete (since the restriction runs against Seller, not its assignees, and the carve-out is tied to TSA performance).
- **Recommendation:** Amend Section 12.3 to require Recipient's prior written consent (not to be unreasonably withheld) for any assignment or delegation of the Meal Production Services. Support Services could be delegated with notice. Additionally, add a provision requiring that any successor provider meet the insurance, food safety, and personnel requirements of this Agreement.

---

## Issue 5 (MEDIUM – Drafting / Business Decision)

**TSA Insurance Requirements Are Lower Than the Company's Current Program for Key Coverages**

- **Where:** `transition_services_agreement.md`, Section 7.1; compare `insurance_certificate_cover_letter_cobbelly.md`, Section 2 (Policies 1, 2, and 3).
- **What it says:** The TSA requires the Provider to maintain:
  - Product contamination and recall: **$2,000,000** (TSA § 7.1(b))
  - Umbrella liability: **$10,000,000** (TSA § 7.1(d))

  The Company's current program (which covers the same operational risk during the pre-closing period) carries:
  - Product contamination and recall: **$5,000,000** (Policy 2)
  - Commercial umbrella: **$15,000,000** (Policy 3)

- **Why it matters for Trouseind:** During the transition period, the Provider at the Milwaukee Commissary is producing the same meals for the same airline customers. The risk profile is essentially identical to the Company's own production. Yet the TSA requires $3M less in product contamination coverage and $5M less in umbrella coverage. A significant contamination event or recall could exhaust the lower TSA limits, leaving Trouseind/Company exposed for the shortfall.
- **Recommendation:** Increase TSA § 7.1(b) to $5,000,000 and § 7.1(d) to $15,000,000 to match the Company's current program. If the client views the current program levels as a business floor rather than a target, this is a business decision; however, from a drafting perspective, the TSA should not require less insurance than the company currently carries for the same activity.

---

## Issue 6 (MEDIUM – Drafting Fix)

**Governing Law and Jurisdiction Conflict Between SPA and Escrow Agreement**

- **Where:** `stock_purchase_agreement_trouseind_reitaisk.md`, Sections 11.8–11.9 (New York law; New York County courts); `escrow_agreement_lanterwick.md`, Section 10.2 (Delaware law; Court of Chancery).
- **What it says:** The SPA is governed by New York law with exclusive jurisdiction in New York County. The Escrow Agreement is governed by Delaware law with exclusive jurisdiction in the Delaware Court of Chancery.
- **Why it matters for Trouseind:**
  - A dispute about whether a claim is valid (which the Escrow Agreement routes to Delaware) may turn on the interpretation of SPA representations and the survival periods (governed by New York law). Splitting the governing law and forum across documents creates the risk of inconsistent interpretations and potentially parallel or sequential litigation in two jurisdictions.
  - SPA Section 11.10 provides that the SPA prevails over other Transaction Documents except that the Escrow Agreement "shall govern the disbursement of the Escrow Funds." This carve-out is limited to disbursement mechanics and should not extend to the governing law for interpreting the underlying claims.
- **Recommendation:** Conform Escrow Agreement Section 10.2 to New York law and New York County jurisdiction, consistent with the SPA. If the Escrow Agent (Lanterwick) prefers Delaware for administrative reasons, an alternative is to keep Delaware law for purely ministerial escrow administration but provide that any dispute regarding the validity, amount, or survival of a Claim shall be governed by New York law and heard in the New York forums specified in the SPA.

---

## Issue 7 (MEDIUM – Consider)

**TSA Section 12.7: Company Is Not a Third-Party Beneficiary**

- **Where:** `transition_services_agreement.md`, Section 12.7.
- **What it says:** "The Company may receive Services but is not a third-party beneficiary."
- **Why it matters for Trouseind:** After the Closing, Trouseind owns the Company. The Company is the entity whose airline customers are receiving meals, whose food safety program is at stake, and whose operations depend on the Services. If the Company is not a third-party beneficiary, it cannot directly enforce the TSA (e.g., to compel incident notice under Section 2.4, to demand access under Section 5.2, or to terminate for breach under Section 11.2). Only Trouseind, as Recipient, has standing.
  - In practice, because Trouseind owns the Company, this is manageable. However, if there is any period of operational separation or if the Company is later restructured, the lack of direct enforcement rights could be problematic.
- **Recommendation:** This is a lower-priority item. If the client wants belt-and-suspenders protection, add the Company as a third-party beneficiary with respect to Sections 2.2 (Standard of Performance), 2.3 (Food Safety Program), 2.4 (Incident Notice), 5.2 (Access), and 11.2 (Termination for Breach). Otherwise, note it as an accepted risk given Trouseind's ownership of the Company.

---

## Issue 8 (LOW-MEDIUM – Business Decision)

**TSA Extension Is Limited to a Single Three-Month Period**

- **Where:** `transition_services_agreement.md`, Section 3.2.
- **What it says:** Recipient may extend the Service Period for any Service by up to three months, "on one occasion," with 30 days' prior notice.
- **Why it matters for Trouseind:** If the client's integration plan requires more than the base Service Period plus three months (e.g., if a replacement kitchen is delayed, or an airline customer contract requires a longer transition), there is no contractual mechanism to extend further. The client would be forced to either (a) negotiate a new agreement with the Seller under time pressure, or (b) find an alternative provider on short notice.
- **Recommendation:** Business decision. The client should confirm its internal integration timeline and determine whether the base Service Periods (in Schedule A, which I have not seen) plus one three-month extension are sufficient. If not, negotiate for two extension rights or a longer single extension. I note that Schedule A is referenced but not included in the matter folder—**I need to see Schedule A and Schedule B to assess the base Service Periods and fee levels.**

---

## Issue 9 (LOW – Planning Item)

**Company's Insurance Policies Expire July 1, 2026 – Three Months After Closing**

- **Where:** `insurance_certificate_cover_letter_cobbelly.md`, Section 2 (all policy periods end July 1, 2026) and Section 3.2.
- **What it says:** All seven policies in the Company's current program expire on July 1, 2026. The broker states it will "start renewal marketing for the July 1, 2026 renewal in the ordinary course" and will "coordinate with the Company, and after closing with the buyer, as directed."
- **Why it matters for Trouseind:** The certificates confer no rights on the holder (Section 4.1). The broker has no contractual obligation to secure renewals. If the client does not actively engage in the renewal process, there is a risk of a coverage gap on July 1, 2026. For a food production business with airline customers, a lapse in product liability or contamination coverage would be operationally and reputationally damaging.
- **Recommendation:** Business/planning item. The client should (a) confirm with the broker that renewal marketing will begin promptly after closing, (b) decide whether to retain the current carriers or re-market the program, and (c) calendar the July 1, 2026 expiration as a hard deadline. No drafting change is needed in the deal documents, but the client should be aware of this timing.

---

## Issue 10 (LOW – Verify in Diligence)

**Tax Sharing Agreement Termination and Consolidated Group Exposure**

- **Where:** `stock_purchase_agreement_trouseind_reitaisk.md`, Sections 3.14(f) and 6.8(e).
- **What it says:** Section 3.14(f) represents that the Company "is not a party to any Tax sharing, allocation or indemnification agreement that will survive the Closing." Section 6.8(e) provides that all such agreements "shall be terminated as of the Closing Date."
- **Why it matters for Trouseind:** The Company has been in Seller's consolidated group since January 1, 2019 (Section 3.14(e)). In a consolidated group, intercompany tax allocations are common. If there is an existing tax sharing or allocation agreement that has not been identified, the termination in Section 6.8(e) may not address outstanding intercompany balances. The representation in 3.14(f) is limited to agreements that "will survive the Closing"—an agreement that is technically terminated at closing but has unresolved intercompany balances would not be captured.
- **Recommendation:** Confirm in diligence that (a) all tax sharing/allocation agreements have been identified, (b) intercompany tax balances are settled or addressed in the Closing Statement, and (c) the Seller Group's consolidated return for the 2026 straddle period will properly allocate any Section 1.1502-6 imputed underpayment. If the side letter in Issue 1 is accepted (even in modified form), this diligence becomes even more critical because the survival window will be shorter.

---

## Open Items / Questions

1. **Schedules to the TSA.** I have not seen Schedule A (Services, Service Periods, Airline Customers) or Schedule B (Fees). I need these to assess whether the base Service Periods are adequate and whether the fee structure is reasonable. Please provide.

2. **Disclosure Schedules.** The SPA references numerous Disclosure Schedules (Sections 3.4, 3.8, 3.9, 3.10, 3.15, 3.16, 3.17(d), 3.18). I have not reviewed these. In particular, I need to see:
   - Section 3.17(d) (foodborne illness incidents since 2021)
   - Section 3.18 (insurance policies)
   - Section 3.4 (consents required)
   - Section 3.8 (Material Contracts, including airline customer agreements)

3. **Closing Statement.** SPA Section 2.3 requires Seller to deliver a Closing Statement at least five Business Days before Closing. I have not seen it. The Indebtedness and Transaction Expenses figures will affect the net proceeds and should be verified.

4. **Client's integration timeline.** For Issue 8, I need to know the client's expected timeline for standing up its own production capability or engaging a replacement provider, so I can assess whether the TSA term (plus one 3-month extension) is sufficient.

5. **Consolidated tax exposure quantification.** For Issue 1, it would be helpful to have a rough sense of the Company's historical taxable income and intercompany transactions within the Seller Group to assess whether the $3,000,000 Extended Holdback is adequate for tax purposes, independent of the survival period question.