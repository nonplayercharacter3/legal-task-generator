# MEMORANDUM

**To:** Partner of Record
**From:** Associate
**Re:** Trouseind Provisioning Group / Reitaisk Aviation Services – Cobbelly Inflight Kitchens Acquisition: Issue Identification Across Deal Package
**Date:** [Current Date]

---

## Summary

I have reviewed all five documents in the matter folder. I identified nine issues requiring attention before we respond to the other side. The three most critical are: (1) the Seller's proposed side letter cutting tax survival to nine months; (2) a definitional mismatch between the SPA and the Escrow Agreement that strips the Extended Holdback of its intended protection for food safety and tax claims; and (3) a provision in the Transition Services Agreement under which Trouseind indemnifies the Seller for the Seller's own ordinary negligence in producing meals. Details and recommended fixes follow, in order of priority.

---

## Issue 1 – Seller Side Letter: Tax Survival Reduced to Nine Months

**Where:** `seller_side_letter_tax_survival.md`, Section 2.1 (proposed replacement for SPA § 9.1(b)).

**What it does:** Deletes the SPA's existing tax survival provision—under which Section 3.14 (Taxes) representations and the Section 9.2(c) Pre-Closing Tax indemnity survive until 60 days after expiration of the applicable statute of limitations—and replaces it with a flat nine-month survival period from the Closing Date.

**Why it matters for Trouseind:**

- The Company has been in the Seller's consolidated federal group since January 1, 2019 (SPA § 3.14(e)). The 2026 consolidated return, which will include the Company through the Closing Date, will not be filed until at least October 2026 (with extension). Any deficiency, allocation dispute, or § 1.1502-6 issue arising from that return would surface after the nine-month period has expired (December 31, 2026 if closing is March 31, 2026).
- Pre-Closing Taxes (SPA § 1.1) include taxes for all periods ending on or before the Closing Date, including Straddle Periods. A state or federal audit of a 2023 or 2024 return could result in an assessment in 2027 or later—well outside a nine-month window.
- The SPA's Pre-Closing Tax indemnity (SPA § 9.2(c)) is uncapped (SPA § 9.5 excludes § 9.2(c) from the 10% Cap). Cutting the survival to nine months effectively neutralizes that uncapped protection.
- The Extended Holdback Amount ($3M) is designated in SPA § 2.4 to secure Pre-Closing Tax claims. If those claims are time-barred at nine months, the Extended Holdback sits in escrow for three years (SPA § 2.4(b)) securing claims that can no longer be brought—reducing it to a pure credit enhancement for Seller with no corresponding protection for Trouseind.

**Recommendation:** Reject the side letter as drafted. This requires a **business decision** from the client: whether to (a) insist on the SPA's original formulation (statute of limitations + 60 days), (b) accept a compromise such as the later of (i) 60 days after expiration of the applicable statute of limitations or (ii) the date the 2026 consolidated return is finally assessed, or (c) in no event accept less than 24 months. I would recommend (a) as the opening position, with (b) as a fallback. The client should also be aware that this issue is interlocked with Issue 2 below.

---

## Issue 2 – Escrow Agreement: "Fundamental Representation Claims" Definition Does Not Match the SPA

**Where:** `escrow_agreement_lanterwick.md`, § 1.1 (definition of "Fundamental Representation Claims"); compare `stock_purchase_agreement_trouseind_reitaisk.md`, § 1.1 (definition of "Seller Fundamental Representations") and § 2.4.

**What it does:** The Escrow Agreement defines "Fundamental Representation Claims" as claims for breach of SPA §§ 3.1, 3.2, and 3.3 only. The SPA defines "Seller Fundamental Representations" to include §§ 3.1, 3.2, 3.3, **3.14 (Taxes)**, and **3.17 (Food Safety and Regulatory Compliance)**. SPA § 2.4 expressly states that the $3M Extended Holdback Amount secures claims for breach of the Seller Fundamental Representations *and* for Pre-Closing Taxes under § 9.2(c). SPA § 9.6(b) provides that claims for breach of Seller Fundamental Representations or under § 9.2(c) are recoverable from the Extended Holdback.

**Why it matters for Trouseind:**

- As drafted, the Escrow Agent is contractually prohibited from disbursing the Extended Holdback for a food safety claim (SPA § 3.17) or a Pre-Closing Tax claim (SPA § 9.2(c)). Escrow Agreement § 5.3(a) states the Extended Holdback "shall be available solely for Fundamental Representation Claims" and "the Escrow Agent shall not disburse any portion of the Extended Holdback Amount to Buyer for any other Claim."
- The General Escrow Amount ($5.64M) is released at 12 months (SPA § 2.4(a); Escrow Agreement § 5.2(b)). A food safety incident that manifests in month 14 (e.g., a latent contamination claim by an airline customer or a regulatory action) would find the General Escrow already released. Under the SPA, Trouseind would look to the Extended Holdback. Under the Escrow Agreement, the Extended Holdback is unavailable for that claim. Trouseind would be forced to pursue Seller directly—a credit risk.
- The same problem applies to Pre-Closing Tax claims that surface after 12 months but before 3 years.

**Recommendation:** Amend Escrow Agreement § 1.1 to define "Fundamental Representation Claims" as claims for breach of any of the Seller Fundamental Representations as defined in SPA § 1.1 (i.e., §§ 3.1, 3.2, 3.3, 3.14, and 3.17), and to include claims under SPA § 9.2(c) (Pre-Closing Taxes). Conform Escrow Agreement § 5.3(a) accordingly. This is a drafting fix, not a business decision, but it should be raised together with Issue 1 because the two are interdependent.

---

## Issue 3 – TSA § 8.1: Trouseind Indemnifies the Provider for the Provider's Own Negligence

**Where:** `transition_services_agreement.md`, § 8.1.

**What it says:** "Recipient shall indemnify, defend and hold harmless Provider, its Affiliates and their respective officers, directors, employees and agents (the 'Provider Indemnitees') from and against all Losses arising out of or relating to the provision or receipt of the Services, **including any negligence of Provider**."

**Why it matters for Trouseind:**

- This means that if the Provider (Seller) is ordinarily negligent in producing meals at the Milwaukee Commissary—for example, a temperature excursion, cross-contamination, or failure to follow allergen protocols—and an airline customer or passenger suffers harm, Trouseind must indemnify the Provider for the Provider's own negligence.
- The Provider's indemnity to Trouseind (§ 8.2) covers only "gross negligence or willful misconduct." Ordinary negligence—the most common basis for food safety liability—is excluded from the Provider's indemnity and affirmatively covered by Trouseind's indemnity to the Provider.
- In a food service business, the realistic risk is ordinary negligence, not gross negligence. As drafted, Trouseind bears essentially all of the operational food safety risk during the transition period, even though the Provider is the one controlling the production environment.
- This indemnity is uncapped (TSA § 9.2 excludes Article VIII from the fee-based cap), so Trouseind's exposure is unlimited.

**Recommendation:** Delete the phrase "including any negligence of Provider" from § 8.1. Replace § 8.1 with a mutual structure: each party indemnifies the other for Losses to the extent arising from the indemnifying party's own negligence, gross negligence, or willful misconduct. Alternatively, at minimum, § 8.1 should be limited to Losses arising from the negligence of Recipient or the Company (i.e., Trouseind's own side), and § 8.2 should be expanded to cover the Provider's ordinary negligence (not just gross negligence/willful misconduct). This is a **business decision** in the sense that the client should confirm it is willing to push back on this, as it is a significant economic term. However, the current drafting is so one-sided that I would expect the client to want it fixed.

---

## Issue 4 – TSA § 12.3: Provider May Assign Without Trouseind's Consent

**Where:** `transition_services_agreement.md`, § 12.3.

**What it says:** "Provider may assign or delegate this Agreement, or any of its rights or obligations hereunder, in whole or in part, to any Person without the consent of Recipient."

**Why it matters for Trouseind:**

- The entire purpose of the TSA is to maintain continuity of meal production during the transition. Trouseind is relying on the Provider's specific food safety program, personnel, airline customer relationships, and regulatory standing at the Milwaukee Commissary.
- The Provider could assign the TSA to an entity with inferior food safety controls, less experienced personnel, or no airline industry track record—without Trouseind's knowledge or consent.
- SPA § 3.11 (Title to and Sufficiency of Assets) represents that, "except for the services to be provided under the Transition Services Agreement," the Company's assets are sufficient to conduct the Business. If the Provider assigns the TSA to an undercapitalized or incompetent successor, that representation's practical value is undermined.
- The non-compete in SPA § 6.2 carves out "performing the Transition Services Agreement." If the Provider assigns the TSA to a third party, it is arguable that the assignee's performance falls within the carve-out, potentially allowing a competitor to operate in the restricted space.

**Recommendation:** Amend § 12.3 to require Provider to obtain Recipient's prior written consent (not to be unreasonably withheld) before assigning or delegating any material obligation under the Agreement, particularly the Meal Production Services. At minimum, any assignee should be required to assume all obligations and maintain equivalent insurance and food safety programs. This is a drafting fix, but the client should be aware that the Seller may resist, in which case it becomes a **business decision** about how much leverage Trouseind wants to retain over the transition provider.

---

## Issue 5 – Escrow Agreement Governing Law and Jurisdiction Inconsistent with SPA

**Where:** `escrow_agreement_lanterwick.md`, § 10.2 (Delaware law; Delaware Court of Chancery exclusive jurisdiction); compare `stock_purchase_agreement_trouseind_reitaisk.md`, § 11.8 (New York law) and § 11.9 (New York County courts).

**Why it matters for Trouseind:**

- A dispute about whether a Claim is valid (e.g., whether a food safety rep was breached) would be governed by Delaware law and heard in the Court of Chancery under the Escrow Agreement, while the underlying indemnification obligation in the SPA is governed by New York law. The same factual predicate could be analyzed under different substantive standards.
- SPA § 11.10 provides that the Escrow Agreement "shall govern the disbursement of the Escrow Funds" in the event of inconsistency. This means the Delaware forum and law would control the escrow mechanics, but a party might argue that the validity of the underlying claim is a SPA matter (New York). This creates litigation strategy complexity and potential for inconsistent rulings.
- The Court of Chancery is an equity court. Its jurisdiction over a claim for indemnification (a legal remedy) may be questionable, potentially forcing a transfer to the Superior Court or federal court under the Escrow Agreement's own fallback provision.

**Recommendation:** Conform Escrow Agreement § 10.2 to New York law and New York County jurisdiction, consistent with the SPA. Alternatively, if the parties want Delaware for the escrow mechanics (which is common for escrow agreements), add a provision that the validity and scope of any Claim under the SPA shall be determined under New York law, and that the Escrow Agent shall disburse in accordance with such determination. This is a drafting fix, but the client should be aware that the Seller's counsel may have chosen Delaware deliberately (perhaps because the Seller is more comfortable in that forum or because the Escrow Agent is a national bank with a Delaware presence).

---

## Issue 6 – TSA § 7.2: Company Not Named as Additional Insured on Product Contamination Policy

**Where:** `transition_services_agreement.md`, § 7.2; compare `insurance_certificate_cover_letter_cobbelly.md`, § 2 (Policy 2: Product Contamination and Recall, $5M).

**What it says:** § 7.2 requires the Provider to name Recipient and the Company as additional insureds only under the CGL policy (§ 7.1(a)) and the umbrella policy (§ 7.1(d)). The product contamination and recall policy (§ 7.1(b), minimum $2M) is not included.

**Why it matters for Trouseind:**

- During the transition, meals are produced at the Provider's Milwaukee Commissary for the Company's airline customers. If a product contamination event occurs (e.g., undeclared allergen, bacterial contamination), the primary coverage would be the product contamination policy.
- The Company's own product contamination policy ($5M, per the insurance certificate) covers the Company's three flight kitchen facilities. It is unclear whether it extends to product produced at the Provider's Milwaukee Commissary. The policy likely covers products "manufactured, sold or distributed" by the named insured, which could include product made by a contractor, but this depends on the policy language (not in the folder).
- The Provider's product contamination policy ($2M minimum under the TSA) would respond for the Provider, but the Company is not an additional insured. If the Company is sued by an airline customer or passenger for a contamination event at the Milwaukee Commissary, the Company may not have direct access to the Provider's product contamination coverage.
- The CGL policy often excludes product contamination (which is precisely why a separate product contamination policy exists). So the additional insured status on the CGL (§ 7.1(a)) may not help for a contamination claim.

**Recommendation:** Amend TSA § 7.2 to require the Provider to name Recipient and the Company as additional insureds under **all** policies in § 7.1, including the product contamination and recall policy (§ 7.1(b)). Additionally, consider whether the minimum limit for product contamination coverage should be increased from $2M to match or exceed the Company's own $5M product contamination policy, given that the Provider will be handling the Company's product during the transition. This is a **business decision** on the limit question; the additional insured requirement is a drafting fix.

---

## Issue 7 – Gap Between General Escrow Release (12 Months) and General Rep Survival (18 Months)

**Where:** `stock_purchase_agreement_trouseind_reitaisk.md`, § 2.4(a) (General Escrow released at 12 months); § 9.1(a) (general reps survive 18 months).

**Why it matters for Trouseind:**

- For the six-month period between month 12 and month 18, Trouseind has valid indemnification rights for breach of non-fundamental representations (e.g., Material Contracts, Undisclosed Liabilities, Financial Statements, Employee Benefit Matters) but no escrow security. Recovery depends entirely on Seller's creditworthiness and willingness to pay.
- If Seller is a holding company with limited assets outside the Shares (which have been sold), Trouseind's practical recovery for a claim in months 13–18 could be limited.

**Recommendation:** This is a **business decision**. Options include: (a) extend the General Escrow release to 18 months to match the survival period; (b) accept the current structure if the client is comfortable with the credit risk of pursuing Seller directly; or (c) negotiate a shorter survival period (e.g., 12 months) to align with the escrow release. I would recommend (a) as the first ask, with (c) as a fallback if the Seller resists holding funds longer.

---

## Issue 8 – TSA § 12.7: Company Is Not a Third-Party Beneficiary

**Where:** `transition_services_agreement.md`, § 12.7.

**What it says:** "The Company may receive Services but is not a third-party beneficiary."

**Why it matters for Trouseind:**

- The Company (which Trouseind will own) is the entity actually receiving meals and bearing operational risk. If the Company suffers a loss from a Provider breach (e.g., a delivery failure that causes the Company to miss an airline customer's deadline), only Trouseind as Recipient can enforce the TSA. The Company cannot sue the Provider directly.
- This adds a procedural layer: the Company must report the loss to Trouseind, and Trouseind must bring the claim. In a fast-moving operational context (e.g., a missed flight delivery), this could delay response.
- It also means the Company's own insurance (which may subrogate against the Provider) could be complicated by the contractual structure.

**Recommendation:** Consider adding the Company as a third-party beneficiary with respect to the Provider's obligations under Articles II (Services), VII (Insurance), and VIII (Indemnification). Alternatively, if the client prefers to keep the TSA bilateral, ensure that the Company's internal reporting lines to Trouseind are clear and that the indemnity in § 8.2 (as revised per Issue 3) expressly covers Losses of the Company. This is a lower-priority drafting point.

---

## Issue 9 – Company Insurance Policies Expire July 1, 2026 (Three Months Post-Closing)

**Where:** `insurance_certificate_cover_letter_cobbelly.md`, § 2 (all policies: July 1, 2025 – July 1, 2026) and § 3.2.

**Why it matters for Trouseind:**

- All seven policies in the Company's current program expire on the same date—July 1, 2026, approximately three months after the target Closing Date.
- The broker states that renewal marketing will begin "in the ordinary course" and that it will "coordinate with the Company, and after closing with the buyer, as directed." This is a soft commitment, not a guarantee of renewal on equivalent terms.
- In the interim, Trouseind will need to ensure that (a) the policies are renewed or replaced, (b) the transition period's insurance needs (per the TSA) are coordinated with the Company's own program, and (c) there is no gap in coverage.
- The product contamination policy ($5M) and the aviation ground liability policy ($25M) are particularly important given the nature of the business. If the insurer non-renews or materially increases premiums at the July 2026 renewal, Trouseind will face a cost increase or coverage gap shortly after closing.

**Recommendation:** This is a **business decision** and an operational item. I recommend that the client: (a) request the full policy forms and five-year loss runs from the data room (as offered in § 3.3 of the broker's letter) before closing, to assess renewal risk; (b) require as a closing condition or post-closing covenant that the Provider/Seller cooperate in the renewal process; and (c) begin its own insurance marketing for the July 2026 renewal no later than April 2026. No drafting change to the deal documents is strictly required, but the client should be aware of the timing.

---

## Questions for the Client / Partner

1. **On Issue 1 (Tax Survival Side Letter):** What is the client's risk tolerance on pre-closing tax exposure? The Company was in a consolidated group for seven years. Are there any known tax audits, disputes, or unusual positions (e.g., transfer pricing, state apportionment) that would make the nine-month period particularly dangerous? I would want to review the Disclosure Schedules (not yet in the folder) for any tax-related disclosures before finalizing our position.

2. **On Issue 3 (TSA Indemnity):** Is the client aware that as drafted, it would be indemnifying the Seller for the Seller's own negligence in producing meals? I suspect this may be a drafting error by the Seller's counsel (perhaps a carryover from a template where the Recipient is the service provider), but if it is intentional, the client needs to understand the magnitude of the exposure before we negotiate.

3. **On the Disclosure Schedules:** The SPA references Disclosure Schedules throughout (e.g., §§ 3.4, 3.8, 3.9, 3.10, 3.15, 3.16, 3.17(d), 3.18), but they are noted as "to be delivered by Seller" and are not in the folder. Several of the issues above (particularly tax and food safety) cannot be fully assessed without reviewing the Schedules. Can we get those before we respond to the Seller?

4. **On the Milwaukee Commissary:** The TSA contemplates that the Provider will continue producing meals at its own facility (the Milwaukee Commissary) during the transition. Is this facility subject to a lease that the Company also uses? If so, the termination of intercompany arrangements under SPA § 6.6 may interact with the TSA in ways we need to understand. The lease is presumably listed in the Disclosure Schedules (SPA § 3.10).