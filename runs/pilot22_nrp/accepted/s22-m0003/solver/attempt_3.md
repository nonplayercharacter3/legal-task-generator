# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Topar Medical Systems / Pritor Healthcare Partners – Seller-Side Risk Assessment of Transaction Documents

---

## Summary

I have reviewed the Stock Purchase Agreement (the "SPA"), the Bill of Sale and Assignment and Assumption Agreement (the "Bill of Sale"), the Ashcombe Escrow Agreement (the "Escrow Agreement"), and the Norrland Liquid Helium Supply Agreement (the "Helium Agreement"). The transaction documents leave Topar exposed on several significant fronts. The most critical issues are: (1) a likely misrepresentation regarding the Okavi software license consent requirement, (2) an uncapped and potentially perpetual indemnity for product liability claims, (3) an ambiguous cap structure that may leave covenant breaches uncapped, and (4) a conflict between the SPA and Escrow Agreement that limits Topar's recovery if Buyer wrongfully withholds escrow release. Details and recommended fixes follow.

---

## Issue 1 – Okavi Assignment Consent: Misrepresentation and Void Assignment

**Where it appears:**
- SPA § 4.4 (No Conflicts; Consents) and Disclosure Schedule, Schedule 4.4 ("None")
- Bill of Sale, Annex A, Item 1 (Okavi Reconstruction Software License Agreement), § 14.2 (Assignment)
- Bill of Sale § 2.1 (Assignment of Assigned Contracts)
- SPA § 6.2 (Pre-Closing Contribution)

**Why it matters to Topar:**

The Okavi agreement § 14.2, as quoted in Annex A to the Bill of Sale, provides:

> "Licensee shall not assign, delegate or otherwise transfer this Agreement or any of its rights or obligations hereunder, whether voluntarily, by operation of law or otherwise, without the prior written consent of Licensor. Any change of control of Licensee, including any transfer of more than fifty percent (50%) of the voting securities of Licensee, shall be deemed a transfer requiring the prior written consent of Licensor. Any purported assignment or transfer in violation of this Section 14.2, including upon any change of control of Licensee, shall be null and void, and Licensor may terminate this Agreement immediately upon written notice."

The Bill of Sale § 2.1 expressly assigns Topar's rights under the Okavi agreement to Celestra. This is an assignment that requires Okavi's prior written consent. Without that consent, the assignment is "null and void" and Okavi may terminate immediately.

Yet Schedule 4.4 to the SPA states "None" — meaning Topar has represented to Buyer that no consents are required under any contract, including the Assigned Contracts. This is directly contradicted by the Okavi agreement's own terms.

The consequences for Topar are severe:

- **Breach of representation (SPA § 4.4).** If Buyer discovers the lack of consent, Topar has made a false representation. Because § 4.4 is not a Fundamental Representation (those are §§ 4.1, 4.2, 4.3, 4.9, 5.1, 5.2), the cap would be the $18.6M Seller Cap under § 9.5(a). But the actual damages from loss of the reconstruction software license could far exceed that amount.
- **Breach of covenant (SPA § 6.2).** Topar covenanted to assign the Assigned Contracts to Celestra before Closing. If the assignment is void, Topar has failed to perform this covenant. As discussed in Issue 3 below, the cap on covenant breaches is ambiguous and may be unlimited.
- **Walk right for Buyer.** If the Okavi agreement is terminated, Celestra loses its core reconstruction software. This would likely constitute a failure of the bring-down condition in SPA § 7.2(a) (other reps true in all material respects) or a material breach giving Buyer termination rights under § 8.1(c).
- **Business criticality.** The Okavi license covers "iterative image reconstruction software" for both CT and MRI systems, including "low-dose CT reconstruction and accelerated MRI reconstruction modules." This appears to be a core technology for the Company's products.

**Recommended fix:**

1. **Immediately obtain Okavi's written consent** to the assignment of the Okavi agreement from Topar to Celestra. This should be a condition to the Bill of Sale becoming effective. If Okavi refuses consent, the parties need to renegotiate the deal structure or the scope of Assigned Contracts.
2. **Amend Schedule 4.4** to disclose the Okavi consent requirement and the status of the consent request. Proposed language:

   > "Schedule 4.4 — Consents
   > 1. The Reconstruction Software License Agreement with Okavi Algorithms GmbH (Annex A, Item 1 to the Bill of Sale) requires Licensor's prior written consent to any assignment. Seller has requested such consent as of [date]. Consent is [granted / pending / denied]. If consent is not obtained by the Effective Date of the Bill of Sale, the assignment of this agreement shall be void under its terms, and Seller shall [describe remedy or exclusion from Assigned Contracts]."

3. **Add a condition to Closing** in the SPA that the Okavi consent has been obtained. Proposed addition to § 7.1:

   > "(c) Seller having obtained the prior written consent of Okavi Algorithms GmbH to the assignment of the Reconstruction Software License Agreement identified in Annex A, Item 1 to the Bill of Sale, in form and substance reasonably acceptable to Buyer."

4. **Consider removing the Okavi agreement from the Assigned Contracts** if consent cannot be obtained, and restructuring the deal to address the gap (e.g., a transition services agreement or a new license negotiation between Celestra and Okavi post-closing).

**Open question:** Has Topar already requested Okavi's consent? What is Okavi's response? If Okavi is unwilling to consent, the deal structure needs fundamental rethinking.

---

## Issue 2 – Uncapped, Potentially Perpetual Indemnity for Specified Matters (Product Liability)

**Where it appears:**
- SPA § 1.1 (definition of "Specified Matters")
- SPA § 9.2(c) (indemnification for Specified Matters)
- SPA § 9.5(c) (exceptions to Seller limitations)
- SPA § 9.1 (survival)
- SPA § 9.6 (source of recovery)

**Why it matters to Topar:**

The definition of "Specified Matters" in § 1.1 covers:

> "(a) any Product Liability Claim relating to any CT or MRI imaging system, or any component of one, manufactured, sold or serviced by the Company, **whether before or after the Closing Date**, and (b) any recall, field safety corrective action or market withdrawal of any such system required by a Governmental Authority or undertaken by the Company in connection with such a Product Liability Claim."

Section 9.2(c) requires Topar to indemnify Buyer for "any Specified Matters." Section 9.5(c) expressly excludes Specified Matters from both the $18.6M cap and the $1.86M deductible. The result:

- **No cap.** Topar's exposure for product liability claims is unlimited.
- **No deductible.** Topar is on the hook from the first dollar.
- **No clear survival limit.** Section 9.1 provides survival periods for representations and warranties (18 months general; statute of limitations + 60 days for Fundamental Reps) and for covenants (until fully performed). But the § 9.2(c) indemnity is a standalone obligation that is neither a rep, warranty, nor covenant. Its survival period is not addressed. Given that the definition covers claims "whether before or after the Closing Date," and that product liability statutes of limitations for medical devices can extend many years (and some jurisdictions allow discovery-based tolling), Topar's exposure could effectively be perpetual.
- **Post-closing claims included.** The definition captures Product Liability Claims arising from systems "manufactured, sold or serviced by the Company" at any time. This means even claims arising from products sold years before the transaction, or products sold after the Closing that relate to pre-Closing design or manufacture, are covered.
- **Escrow is insufficient.** The $18.6M escrow (SPA § 2.3) is the first source of recovery under § 9.6, but it is released after 18 months (Escrow Agreement § 4.1). Any Specified Matters claim arising after the escrow period is released, or exceeding the escrow amount, comes directly out of Topar's pocket with no limit.

For a company that designs and manufactures CT and MRI systems — high-value medical devices with inherent product liability risk — this is an existential tail exposure. A single catastrophic product liability event (e.g., a magnet failure causing patient injury, or a software defect leading to misdiagnosis) could generate claims well into the hundreds of millions.

**Recommended fix:**

1. **Negotiate a cap on Specified Matters.** Even if Buyer resists, Topar should push for a cap tied to a multiple of the escrow amount or a fixed dollar figure. Proposed amendment to § 9.5(c):

   > "(c) *Exceptions to Seller Limitations.* The cap in Section 9.5(a) and the deductible in Section 9.5(b) shall not apply to Losses arising from fraud by Seller. Losses under Section 9.2(c) shall be subject to a cap of [$X], which shall be [three times the Escrow Amount / a stated dollar figure], and to a deductible of [$Y]."

2. **Limit the temporal scope of "Specified Matters."** The current definition captures claims "whether before or after the Closing Date." Topar should argue that it should only cover claims arising from products manufactured or sold before the Closing Date (i.e., pre-closing product risk), not post-closing products that Buyer/Company will manufacture going forward. Proposed amendment to § 1.1:

   > "**Specified Matters**" means (a) any Product Liability Claim relating to any CT or MRI imaging system, or any component of one, **manufactured or sold by the Company before the Closing Date**, and (b) any recall, field safety corrective action or market withdrawal of any such system **manufactured or sold before the Closing Date** required by a Governmental Authority or undertaken by the Company in connection with such a Product Liability Claim.

   This would exclude post-closing products (which Buyer will control) and post-closing servicing (which Buyer will perform).

3. **Establish a survival period.** Add to § 9.1:

   > "The indemnification obligation under Section 9.2(c) shall survive the Closing until the expiration of the longest applicable statute of limitations for Product Liability Claims under the laws of the jurisdiction in which the relevant product was sold, plus sixty (60) days."

4. **Require Buyer to maintain product liability insurance.** Add a covenant requiring the Company (and thus Buyer post-closing) to maintain product liability insurance with limits no less than [$X] for a period of [Y] years post-closing, with Topar named as an additional insured or loss payee for pre-closing products. This would provide a funding source for Specified Matters claims that reduces Topar's direct exposure.

5. **Carve out known claims.** Ensure Schedule 4.8 is comprehensive and that any claims listed there are excluded from the Specified Matters indemnity (or addressed via a specific purchase price adjustment). The current Schedule 4.8 refers to "the data room index delivered to Buyer" — Topar should confirm exactly what is listed and ensure no material claims are omitted.

**Open question:** What is the Company's actual product liability history? How many CT and MRI systems are in the field? What is the nature and extent of any pending or threatened claims? This information is critical to assessing the real magnitude of the Specified Matters exposure and to negotiating an appropriate cap.

---

## Issue 3 – Ambiguous Cap Structure: Covenant Breaches May Be Uncapped

**Where it appears:**
- SPA § 9.2(b) (indemnification for covenant breaches)
- SPA § 9.5(a) (Seller Cap)
- SPA § 9.5(c) (exceptions)

**Why it matters to Topar:**

Section 9.5(a) provides:

> "The aggregate liability of Seller under **Section 9.2(a)** shall not exceed $18,600,000, except that Seller's aggregate liability for breaches of Fundamental Representations, together with all other amounts paid by Seller under this Article IX, shall not exceed the Purchase Price."

The cap is drafted to apply only to "Section 9.2(a)" — breaches of representations and warranties. Section 9.2(b) (breaches of covenants) is not referenced. Section 9.5(c) excludes only § 9.2(c) (Specified Matters) and fraud from the cap and deductible; it is silent on § 9.2(b).

Read literally, Topar's exposure for breach of any covenant (e.g., § 6.1 Conduct of Business, § 6.2 Pre-Closing Contribution, § 6.4 Regulatory Filings, § 6.5 Confidentiality) is **uncapped**. The only potential limit is the $186M Purchase Price cap, but that is triggered only "for breaches of Fundamental Representations, together with all other amounts paid by Seller under this Article IX" — meaning it applies as an overall ceiling only when a Fundamental Reps breach is also present.

This creates a dangerous scenario: if Topar breaches a non-fundamental covenant (such as failing to properly assign the Okavi agreement under § 6.2, or violating the conduct of business covenant under § 6.1), its indemnification exposure could be unlimited, with no cap and no deductible.

**Recommended fix:**

1. **Amend § 9.5(a) to make the cap apply to all of Section 9.2**, not just § 9.2(a). Proposed language:

   > "(a) *Seller Cap.* The aggregate liability of Seller under **Section 9.2** shall not exceed $18,600,000, except that (i) Seller's aggregate liability for breaches of Fundamental Representations, together with all other amounts paid by Seller under this Article IX, shall not exceed the Purchase Price, and (ii) the foregoing cap shall not apply to Losses under Section 9.2(c) or to Losses arising from fraud by Seller, as provided in Section 9.5(c)."

2. **Alternatively, if Buyer insists on the current structure, negotiate a separate (higher) cap for covenant breaches.** For example:

   > "The aggregate liability of Seller under Section 9.2(b) shall not exceed [$25,000,000]."

3. **Clarify the interaction with the $186M overall cap.** Add language making clear that, regardless of the type of breach, Topar's total aggregate liability under Article IX shall not exceed the Purchase Price ($186M).

---

## Issue 4 – Conflict Between SPA and Escrow Agreement on Buyer's Liability for Escrow Release

**Where it appears:**
- SPA § 9.5(d)–(e) (Buyer Cap and exceptions)
- SPA § 11.9 (Order of Precedence)
- Escrow Agreement § 8.3 (Liability of Buyer)

**Why it matters to Topar:**

SPA § 9.5(e) provides that the Buyer Cap ($5M) does **not** apply to:

> "(iii) Buyer's obligations to deliver joint written instructions to the Escrow Agent for the release of Escrow Funds under Section 2.3 and the Escrow Agreement."

This means that under the SPA, if Buyer wrongfully refuses to deliver Joint Written Instructions to release escrow funds to Topar (e.g., at the end of the escrow period under Escrow Agreement § 4.2), Buyer's liability is **uncapped** — Topar could recover the full $18.6M.

However, Escrow Agreement § 8.3 provides:

> "The aggregate liability of Buyer to Seller arising under or in connection with this Escrow Agreement or Article IX of the Purchase Agreement, **including with respect to release of Escrow Funds**, shall not exceed the Buyer Cap, except for fraud."

This directly contradicts the SPA. It expressly includes "release of Escrow Funds" within the $5M cap.

SPA § 11.9 resolves the conflict:

> "In the event of any conflict between this Agreement and the Escrow Agreement, **the Escrow Agreement shall prevail with respect to releases of Escrow Funds and the limitations of liability stated therein**."

Under this precedence clause, the Escrow Agreement's $5M cap controls. The practical effect: if Buyer wrongfully withholds Joint Written Instructions to release the $18.6M escrow to Topar, Topar's maximum recovery from Buyer is $5M. Topar would be out $13.6M.

This is a significant asymmetry. The escrow exists to protect Buyer against Seller's indemnification obligations, but the release mechanism requires Buyer's cooperation (Joint Written Instructions). If Buyer acts in bad faith to delay or prevent release, Topar's remedy is severely limited.

**Recommended fix:**

1. **Amend Escrow Agreement § 8.3** to carve out the Joint Written Instructions obligation, consistent with the SPA. Proposed language:

   > "8.3 *Liability of Buyer.* The aggregate liability of Buyer to Seller arising under or in connection with this Escrow Agreement or Article IX of the Purchase Agreement shall not exceed the Buyer Cap, except for (a) fraud, and (b) Buyer's obligation to deliver Joint Written Instructions for the release of Escrow Funds to Seller under Sections 3.2, 3.4 and 4.2 of this Escrow Agreement."

2. **Alternatively, amend SPA § 11.9** to narrow the precedence clause so it does not apply to limitations of liability that are more restrictive than the SPA. Proposed language:

   > "In the event of any conflict between this Agreement and the Escrow Agreement, the Escrow Agreement shall prevail with respect to the mechanics of releases of Escrow Funds. **With respect to limitations of liability, the more favorable provision to the affected party shall control.**"

3. **Add a default release mechanism.** If Buyer fails to deliver Joint Written Instructions within a specified period after the Escrow Period ends (or after a claim is resolved), the Escrow Agent should be directed to release the funds to Seller automatically. Proposed addition to Escrow Agreement § 4.2:

   > "If Buyer fails to deliver its portion of the Joint Written Instructions within five (5) Business Days after the end of the Escrow Period (or within five (5) Business Days after resolution of any Pending Claim, as applicable), Seller may deliver a certificate of an officer of Seller stating that Buyer has failed to deliver such instructions, whereupon the Escrow Agent shall release the applicable Escrow Funds to Seller within two (2) Business Days after receipt of such certificate, without further action by Buyer."

---

## Issue 5 – Deemed Acceptance of Escrow Claims if Seller Fails to Object Within 30 Days

**Where it appears:**
- Escrow Agreement § 3.2 (Response)

**Why it matters to Topar:**

Section 3.2 provides:

> "Within 30 days after receiving a Claim Notice, Seller may deliver to Buyer and the Escrow Agent a written objection to all or part of the claimed amount (an 'Objection Notice'). **If the Escrow Agent receives no Objection Notice within that 30-day period, Buyer and Seller shall, within five Business Days after the period ends, deliver Joint Written Instructions to release the claimed amount to Buyer.**"

If Topar misses the 30-day window, it is contractually obligated to join in releasing the funds to Buyer. This is effectively a deemed waiver of any defense to the claim. Given that the escrow is $18.6M and claims can be complex (particularly product liability claims that may involve ongoing litigation), 30 days may be insufficient to investigate and formulate a response.

**Recommended fix:**

1. **Extend the objection period.** Proposed amendment:

   > "Within **forty-five (45) days** after receiving a Claim Notice, Seller may deliver to Buyer and the Escrow Agent a written objection..."

2. **Add a cure mechanism for late objections.** Proposed addition:

   > "If Seller fails to deliver an Objection Notice within the period stated above but delivers one within fifteen (15) days after the end of that period, the Objection Notice shall be effective unless Buyer demonstrates that the delay caused it material prejudice."

3. **Internal process.** Regardless of the contractual fix, Topar should implement an internal protocol to ensure that any Claim Notice received by the General Counsel's office is escalated immediately and that a response is prepared well within the deadline.

---

## Issue 6 – Escrow Earnings Taxed to Buyer

**Where it appears:**
- Escrow Agreement § 2.4 (Ownership for Tax Purposes)

**Why it matters to Topar:**

Section 2.4 provides:

> "For income tax purposes, **Buyer shall be treated as the owner of the Escrow Funds** and shall report all earnings on them, until the Escrow Funds are distributed."

The escrow represents $18.6M of the Purchase Price that is economically Topar's money (absent valid claims). Yet Buyer receives the tax benefit of any earnings on that $18.6M over the 18-month escrow period. At current money market yields, this could represent several hundred thousand dollars of tax-free earnings accruing to Buyer rather than Topar.

**Recommended fix:**

1. **Amend § 2.4** to treat Seller as the owner for tax purposes, or to split the earnings. Proposed language:

   > "For income tax purposes, **Seller shall be treated as the owner of the Escrow Funds** and shall report all earnings on them, until the Escrow Funds are distributed to Buyer under this Escrow Agreement. Buyer shall be treated as the owner of any Escrow Funds distributed to Buyer. The Escrow Agent shall issue IRS Forms 1099 or other required tax reports for earnings on the Escrow Funds to Seller."

2. **Alternatively**, if Buyer insists on being treated as owner for tax purposes (which may be their position given that the funds are at risk for their indemnification claims), negotiate a side payment or purchase price adjustment to compensate Topar for the lost tax benefit.

**Open question:** What is the expected yield on the escrow funds over 18 months, and what is Topar's marginal tax rate? This will determine the dollar magnitude of the issue and whether it is worth negotiating.

---

## Issue 7 – Strict Bring-Down Standard for Fundamental Representations

**Where it appears:**
- SPA § 7.2(a) (Conditions to Buyer's Obligations)

**Why it matters to Topar:**

Section 7.2(a) requires that at Closing:

> "the Fundamental Representations of Seller being true and correct **in all respects**, and the other representations and warranties of Seller being true and correct in all material respects, in each case as of the Closing Date."

The "in all respects" standard for Fundamental Representations (organization, capitalization, authority, brokers) means that **any** inaccuracy — no matter how trivial — gives Buyer the right to refuse to close. While these are typically "clean" reps, the risk is not zero. For example:

- If any officer or director of the Company has a minor compliance issue (e.g., a late-filed registration in a foreign jurisdiction), the organization rep (§ 4.1) could be technically inaccurate.
- If any broker fee obligation exists that was not disclosed, the brokers rep (§ 4.9) is breached.

The practical risk is that Buyer could use a technical inaccuracy as leverage to renegotiate price or terms at the 11th hour.

**Recommended fix:**

1. **Change "in all respects" to "in all material respects"** for Fundamental Representations. Proposed amendment to § 7.2(a):

   > "the Fundamental Representations of Seller being true and correct **in all material respects**, and the other representations and warranties of Seller being true and correct in all material respects, in each case as of the Closing Date."

2. **If Buyer resists**, add a materiality qualifier specific to the organization rep: "except where the failure to qualify would not be material to the Company" (which is already in § 4.1 but could be reinforced in the bring-down).

3. **Ensure the Disclosure Schedule is airtight** for all Fundamental Reps before signing. Any gap is a potential walk-right for Buyer at closing.

---

## Issue 8 – Materiality Scrape for Loss Calculation

**Where it appears:**
- SPA § 9.5(f) (Materiality Scrape)

**Why it matters to Topar:**

Section 9.5(f) provides:

> "For purposes of calculating Losses only, materiality qualifiers in the representations and warranties shall be disregarded."

This means that if a representation is qualified by "material" or "material respect" (e.g., § 4.5: financial statements "fairly present **in all material respects**"; § 4.7: compliance "in **all material respects**"), the materiality qualifier is stripped out when calculating the amount of loss. In practice, this can expand the loss calculation in two ways:

1. **Breach determination:** A matter that is immaterial (and thus not a breach of a materiality-qualified rep) could still generate a "loss" for calculation purposes if the scrape is applied at the loss-calculation stage. (Though arguably the scrape applies only to loss quantification, not to whether a breach occurred — the drafting is ambiguous.)
2. **Loss quantification:** Even if a breach is established, the loss is calculated as if the rep were absolute. For example, if the financial statements rep is breached because a $50K item was misstated (immaterial to the Company), the loss calculation ignores the "material" qualifier and Topar owes the full $50K (subject to the deductible).

**Recommended fix:**

1. **Limit the scrape to loss quantification only, not breach determination.** Add clarifying language:

   > "(f) *Materiality Scrape.* For purposes of **calculating the amount of Losses** (and not for purposes of determining whether a representation or warranty has been breached), materiality qualifiers in the representations and warranties shall be disregarded."

2. **Alternatively, delete the materiality scrape entirely** or limit it to specific reps where Topar is comfortable with the exposure.

---

## Issue 9 – Norrland Helium Agreement: Minimum Volume Commitment and Pre-Closing Breach Risk

**Where it appears:**
- Helium Agreement § 2.2 (Minimum Annual Volume)
- SPA § 4.6 (Material Contracts representation)
- SPA § 6.1 (Conduct of Business)

**Why it matters to Topar:**

The Helium Agreement requires Celestra to purchase at least 60,000 liquid liters of helium per contract year. If Celestra purchases less, it owes a shortfall payment equal to 25% of the then-current price per liter multiplied by the shortfall (Helium Agreement § 2.2).

The SPA § 4.6 represents that each material contract (which would include the Helium Agreement, given the volume commitment) is "in full force and effect" and that "neither the Company nor, to Seller's knowledge, any counterparty is in material breach of any listed contract."

If Celestra has been failing to meet the 60,000-liter minimum in any contract year (2025 or 2026 to date), the Company is in breach, and Topar's representation in § 4.6 is inaccurate. This would trigger indemnification under § 9.2(a), subject to the $18.6M cap and $1.86M deductible.

Additionally, under SPA § 6.1, Topar must cause the Company to operate in the ordinary course between signing and closing. If "ordinary course" includes meeting helium purchase commitments, a failure to do so pre-closing would be a covenant breach (potentially uncapped per Issue 3).

**Recommended fix:**

1. **Confirm with the client** whether Celestra has met the 60,000-liter minimum in each contract year since January 1, 2025. If not, quantify the shortfall and assess whether it constitutes a "material breach" under the Helium Agreement.
2. **If a shortfall exists**, disclose it on Schedule 4.6 and consider a purchase price adjustment or specific indemnity for the shortfall amount.
3. **Ensure the conduct of business covenant (§ 6.1) is understood** to include compliance with the Helium Agreement's minimum volume commitment, so that Topar is not inadvertently in breach between signing and closing.

**Open question:** Has Celestra met the Minimum Annual Volume in contract year 2025 and for the period January 1 through the expected Closing Date in 2026? What is the current helium purchase run-rate?

---

## Issue 10 – Escrow Agent Fee Split and Administrative Burden

**Where it appears:**
- SPA § 11.1 (Expenses)
- Escrow Agreement § 7.1 (Fees)
- Escrow Agreement, Schedule 3 (Fee Schedule)

**Why it matters to Topar:**

Topar pays half of the Escrow Agent's fees. Per Schedule 3, these include:
- Acceptance fee: $5,000 (at Closing)
- Annual administration fee: $7,500 (at Closing and each anniversary while the account is open)
- Disbursement fees: $50 per wire transfer
- Out-of-pocket expenses: at cost

Over the 18-month escrow period, Topar's share would be approximately: $2,500 (acceptance) + $3,750 (one anniversary fee, since the period is 18 months) + disbursement fees + half of any out-of-pocket expenses. This is modest in absolute terms but worth noting.

More importantly, the Escrow Agreement requires Topar to actively participate in the claims process (responding to Claim Notices within 30 days, negotiating disputed claims for 30 days, delivering Joint Written Instructions). This creates an ongoing administrative and legal burden for 18 months post-closing.

**Recommended fix:**

This is a lower-priority item. The fee split is standard. However, Topar should ensure it has internal resources (or outside counsel on retainer) to handle escrow claims promptly. Consider adding to the SPA a requirement that Buyer provide Topar with at least [5] Business Days' advance notice of any anticipated Claim Notice before the end of the escrow period, to allow for orderly wind-down.

---

## Issue 11 – Order of Precedence: Escrow Agreement Prevails on "Limitations of Liability"

**Where it appears:**
- SPA § 11.9 (Order of Precedence)

**Why it matters to Topar:**

As noted in Issue 4, the precedence clause in § 11.9 gives the Escrow Agreement control over "the limitations of liability stated therein." This is a broad grant of precedence that could swallow other SPA protections. For example, if the Escrow Agreement contained a provision limiting Seller's liability (not just Buyer's), the Escrow Agreement would control over the SPA's cap structure.

Currently, the Escrow Agreement does not impose additional limits on Seller's liability (it only addresses Buyer's liability in § 8.3 and the Escrow Agent's liability in § 8.1). But the broad precedence language creates risk if the Escrow Agreement is amended later (which requires all three parties' consent under § 10.3, but Buyer and the Escrow Agent could agree to an amendment that adversely affects Topar if Topar is not attentive).

**Recommended fix:**

1. **Narrow the precedence clause** in SPA § 11.9 to address only the specific conflict at issue (mechanics of escrow release), not "limitations of liability" broadly. Proposed language:

   > "In the event of any conflict between this Agreement and the Escrow Agreement, the Escrow Agreement shall prevail with respect to the **mechanics and procedures for** releases of Escrow Funds. **In all other respects, this Agreement shall prevail.**"

2. **Require Topar's consent to any amendment of the Escrow Agreement** that affects Topar's rights or obligations. (This is already required by Escrow Agreement § 10.3, which mandates all three parties sign any amendment, but it is worth confirming the client understands this.)

---

## Issue 12 – Confidentiality Covenant Survives Closing and Is Potentially Broad

**Where it appears:**
- SPA § 6.5 (Confidentiality)

**Why it matters to Topar:**

Section 6.5 requires that "After the Closing, Seller shall keep confidential all non-public information about the Company, except as required by law." This is a post-closing covenant that survives until "fully performed" (SPA § 9.1). There is no stated time limit.

As the former parent of the Company, Topar may have ongoing business interests (e.g., other product lines, competitive intelligence) that could be implicated by information it learned about Celestra during the pre-closing period. An unlimited confidentiality obligation could restrict Topar's use of general business knowledge.

**Recommended fix:**

1. **Add a time limit.** Proposed amendment:

   > "6.5 *Confidentiality.* After the Closing, Seller shall keep confidential all non-public information about the Company, except as required by law or except for information that becomes publicly available through no fault of Seller. **This obligation shall survive for three (3) years after the Closing Date.**"

2. **Add standard carve-outs** for information independently developed, already known, or received from a third party without restriction (similar to Helium Agreement § 11.2).

---

## Open Questions Requiring Client or Counterparty Input

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Has Topar requested Okavi's consent to the assignment? What is Okavi's response? | Determines whether Issue 1 is a live breach or a manageable pre-closing condition. |
| 2 | What is the Company's full product liability history (pending claims, recalls, field corrections)? | Determines the realistic magnitude of the Specified Matters exposure (Issue 2). |
| 3 | Has Celestra met the 60,000-liter helium minimum in 2025 and YTD 2026? | Determines whether there is a pre-closing breach of the Helium Agreement and a potential inaccuracy in SPA § 4.6 (Issue 9). |
| 4 | What is the expected yield on the $18.6M escrow over 18 months, and what is Topar's marginal tax rate? | Determines the dollar value of the escrow earnings tax issue (Issue 6). |
| 5 | Does Buyer consider the § 9.5(a) cap to apply only to § 9.2(a) intentionally, or is it a drafting oversight? | Determines whether Issue 3 is a negotiation point or a confirmed risk. |
| 6 | Are there any other contracts of the Company (beyond those in Annex A to the Bill of Sale) that contain change-of-control or assignment consent provisions that could be triggered by the stock sale? | The SPA § 4.4 representation covers all contracts of the Company, not just the Assigned Contracts. A change of control of Celestra could trigger consent requirements in other Company contracts. |
| 7 | What is the status of the HSR filing (SPA § 6.4)? Has early termination been requested? | Affects the timing of Closing and the outside date (July 31, 2026). |

---

## Recommended Priority of Action

1. **Immediately:** Confirm Okavi consent status. If not yet requested, request consent now. The Bill of Sale Effective Date is March 30, 2026 — if consent is not in hand by then, the assignment is void.
2. **Before signing any amendment:** Negotiate fixes for Issues 2 (Specified Matters cap/scope), 3 (covenant cap), and 4 (escrow release conflict). These are the highest-dollar, highest-probability risks.
3. **Before Closing:** Resolve Issues 1 (schedule disclosure), 5 (objection period), 7 (bring-down standard), and 9 (helium minimums).
4. **At or after Closing:** Implement internal processes for escrow claims (Issue 5) and monitor the Helium Agreement compliance (Issue 9).