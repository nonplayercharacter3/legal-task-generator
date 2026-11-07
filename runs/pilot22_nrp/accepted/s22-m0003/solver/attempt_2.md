# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Topar Medical Systems / Pritor Healthcare Partners – Seller-Side Issue Identification

---

## Summary

I have reviewed the Stock Purchase Agreement (SPA), the Bill of Sale, the Ashcombe Escrow Agreement, and the Norrland Helium Supply Agreement. I have identified three critical issues that should be resolved before we proceed, several significant exposures, and a number of open questions. The most urgent problem is that the SPA's no-conflicts representation is flatly contradicted by the terms of the Okavi reconstruction software license, which is one of the Assigned Contracts being contributed to Celestra pre-Closing.

---

## 1. CRITICAL: Okavi Consent Requirement Contradicts SPA Representation

**Where:** SPA § 4.4 and Schedule 4.4; Bill of Sale, Annex A, Item 1 (Okavi Algorithms GmbH, § 14.2); SPA § 6.2; Bill of Sale § 2.1.

**The problem.** Section 4.4 of the SPA represents that the transactions do not "require any consent of, or notice to, any Person under any contract to which Seller or the Company is a party, **including the Assigned Contracts**," except as set out in Schedule 4.4. Schedule 4.4 states: "None."

However, the Okavi Reconstruction Software License Agreement (Annex A, Item 1 to the Bill of Sale) contains the following assignment and change-of-control provision (§ 14.2):

> "Licensee shall not assign, delegate or otherwise transfer this Agreement or any of its rights or obligations hereunder, whether voluntarily, by operation of law or otherwise, **without the prior written consent of Licensor**. Any change of control of Licensee, including any transfer of more than fifty percent (50%) of the voting securities of Licensee, **shall be deemed a transfer requiring the prior written consent of Licensor**. Any purported assignment or transfer in violation of this Section 14.2, including upon any change of control of Licensee, **shall be null and void**, and Licensor may terminate this Agreement immediately upon written notice."

Two separate consents are required:

- **(a) Consent to assignment.** The Bill of Sale (§ 2.1) assigns the Okavi contract from Topar to Celestra, effective March 30, 2026. Topar is the "Licensee" under the Okavi agreement. Section 14.2 expressly prohibits assignment without Okavi's prior written consent.
- **(b) Consent to change of control.** After the assignment, Celestra becomes the Licensee. The sale of 100% of Celestra's stock to Pritor at Closing is a "change of control of Licensee" under § 14.2, which is "deemed a transfer requiring the prior written consent of Licensor."

**Why it matters to Topar.**

- If Topar closes without Okavi's consent, it is in immediate breach of § 4.4. Although § 4.4 is not a Fundamental Representation (so the $18.6M cap and $1.86M deductible in § 9.5(a)–(b) would apply), Buyer would have a material-breach termination right under § 8.1(c) and a post-Closing indemnification claim.
- More seriously, Okavi has an express right to declare the assignment "null and void" and to terminate the license immediately. The Okavi license covers "iterative image reconstruction software" for both CT and MRI systems, including "low-dose CT reconstruction and accelerated MRI reconstruction modules." Loss of this license would be operationally devastating to Celestra and would almost certainly constitute a material adverse change that Buyer could exploit.
- The Bill of Sale (§ 5.1) requires joint notice to Okavi within ten business days after the Effective Date (March 30, 2026). That notice would put Okavi on express notice of an unauthorized assignment, accelerating the risk of termination.

**Recommended fix.**

1. **Obtain Okavi's written consent before the Bill of Sale Effective Date and before Closing.** This should be a condition to Closing. I recommend adding to SPA Article VII:

   > **§ 7.2(d)** Buyer's obligation to close is further subject to Seller having delivered to Buyer, at or before the Closing, Okavi's written consent to (i) the assignment of the Okavi Reconstruction Software License Agreement to the Company pursuant to the Bill of Sale and (ii) the change of control of the Company resulting from the transactions under this Agreement.

2. **Amend Schedule 4.4** to state: "Okavi Algorithms GmbH – prior written consent required under § 14.2 of the Reconstruction Software License Agreement dated June 1, 2022, as amended, for (a) assignment of such agreement to the Company and (b) change of control of the Company. Consent sought; status: [to be updated]."

3. **If Okavi refuses or conditions consent**, we need to evaluate whether the Okavi contract can be carved out of the Assigned Contracts (requiring an amendment to the Bill of Sale and SPA) or whether the deal economics change materially. This is a **client decision point** – please confirm whether Topar has already approached Okavi and what Okavi's posture is.

4. **Do not deliver the Bill of Sale notice under § 5.1 to Okavi until consent is in hand.**

**Open question:** Has Topar contacted Okavi regarding consent? What is Okavi's typical turnaround and whether it charges a consent fee? If Okavi is uncooperative, what is the business impact of losing the reconstruction license?

---

## 2. CRITICAL: Specified Matters Indemnity Is Uncapped and Effectively Has Indefinite Survival

**Where:** SPA §§ 1.1 (definition of "Specified Matters"), 9.1 (survival), 9.2(c) (indemnification trigger), 9.5(c) (exceptions to cap and deductible).

**The problem.** Section 9.2(c) requires Seller to indemnify Buyer for "any Specified Matters." "Specified Matters" is defined in § 1.1 to include:

> (a) any Product Liability Claim relating to any CT or MRI imaging system, or any component of one, manufactured, sold or serviced by the Company, **whether before or after the Closing Date**, and
> (b) any recall, field safety corrective action or market withdrawal of any such system required by a Governmental Authority or undertaken by the Company in connection with such a Product Liability Claim.

Section 9.5(c) provides that the Seller Cap ($18.6M) and the Deductible ($1.86M) "shall not apply to Losses under Section 9.2(c)." So Topar's exposure for product liability is **uncapped**.

On survival: § 9.1 provides that representations survive 18 months (or longer for Fundamentals) and that "[c]ovenants survive until fully performed." The § 9.2(c) indemnity is a covenant, not a representation. "Until fully performed" for a product liability indemnity that covers claims "whether before or after the Closing Date" is effectively **indefinite** – it runs until every potential product liability claim has been resolved, which for medical devices can be a decade or more given applicable statutes of limitations and discovery rules.

**Why it matters to Topar.**

- Medical imaging devices (CT and MRI) carry significant product liability risk. A single serious injury claim or a recall could generate eight- or nine-figure losses.
- Topar has no cap, no deductible, and no time limit on this exposure.
- The "after the Closing Date" language means Topar is on the hook for defects that Buyer's post-Closing operations may contribute to (e.g., servicing errors by Celestra's post-Closing workforce that Buyer controls).
- The 18-month escrow period (§ 4.1 of the Escrow Agreement) provides no comfort: the escrow is released at 18 months, but the Specified Matters indemnity continues beyond that, meaning Topar faces direct cash exposure after the escrow is gone.

**Recommended fix.**

1. **Cap the Specified Matters indemnity.** I recommend negotiating a separate cap for § 9.2(c) losses, ideally tied to a multiple of the escrow or a fixed dollar amount. Proposed language:

   > **§ 9.5(h) Specified Matters Cap.** Notwithstanding Section 9.5(c), Seller's aggregate liability under Section 9.2(c) shall not exceed $[37,200,000] [i.e., 20% of Purchase Price], provided that this cap shall not apply to Losses arising from fraud by Seller.

2. **Limit the temporal scope.** Strike "whether before or after the Closing Date" and replace with "arising from facts or circumstances existing on or before the Closing Date." Proposed language:

   > "Specified Matters" means (a) any Product Liability Claim relating to any CT or MRI imaging system, or any component of one, manufactured, sold or serviced by the Company **on or before the Closing Date**, to the extent arising from facts or circumstances existing on or before the Closing Date…

3. **Set a survival period.** Add to § 9.1:

   > Seller's indemnification obligations under Section 9.2(c) shall survive the Closing until the later of (i) [36] months after the Closing Date or (ii) the expiration of the applicable statute of limitations for claims arising from facts existing on or before the Closing Date, plus [60] days.

4. **If Buyer will not agree to a cap**, consider requiring Buyer to maintain product liability insurance with Topar named as an additional insured or loss payee for pre-Closing products, and/or negotiating a higher escrow amount dedicated to Specified Matters.

**Open question:** What is Topar's historical product liability loss experience? Are there any pending or threatened claims not reflected in Schedule 4.8 (which we cannot verify because it references the data room index)? What product liability insurance does Celestra currently carry, and will Buyer maintain equivalent coverage post-Closing?

---

## 3. CRITICAL: Escrow Agreement § 8.3 Caps Buyer's Liability for Withholding Escrow Release at $5M

**Where:** Escrow Agreement § 8.3; SPA § 9.5(d)–(e); SPA § 11.9 (order of precedence).

**The problem.** SPA § 9.5(e)(iii) carves out from the Buyer Cap ($5M) "Buyer's obligations to deliver joint written instructions to the Escrow Agent for the release of Escrow Funds under Section 2.3 and the Escrow Agreement." This was presumably negotiated to protect Topar: if Buyer wrongfully refuses to co-sign the release of the $18.6M escrow at the end of the 18-month period, Topar should be able to recover the full amount.

However, Escrow Agreement § 8.3 states:

> "The aggregate liability of Buyer to Seller arising under or in connection with this Escrow Agreement or Article IX of the Purchase Agreement, **including with respect to release of Escrow Funds**, shall not exceed the Buyer Cap, except for fraud."

And SPA § 11.9 provides:

> "In the event of any conflict between this Agreement and the Escrow Agreement, **the Escrow Agreement shall prevail with respect to releases of Escrow Funds and the limitations of liability stated therein**."

Read together, the Escrow Agreement's $5M cap on Buyer's liability for escrow-release issues **overrides** the SPA's carve-out in § 9.5(e)(iii). If Buyer wrongfully withholds its signature on the Joint Written Instructions needed to release the remaining escrow to Topar at month 18, Topar's maximum recovery is $5M – not the full $18.6M.

**Why it matters to Topar.**

- The escrow is Topar's primary post-Closing security for the first 18 months. If Buyer can block release of up to $18.6M and Topar's recovery is capped at $5M, Buyer has a powerful (and arguably unfair) leverage tool.
- This is particularly concerning given that the Escrow Agreement (§ 3.2) requires Joint Written Instructions for any release – neither party can unilaterally access the funds.

**Recommended fix.**

Amend Escrow Agreement § 8.3 to carve out the escrow-release obligation, mirroring SPA § 9.5(e)(iii). Proposed language:

> **§ 8.3 Liability of Buyer.** The aggregate liability of Buyer to Seller arising under or in connection with this Escrow Agreement or Article IX of the Purchase Agreement shall not exceed the Buyer Cap, except for (a) fraud and (b) Buyer's obligation to deliver Joint Written Instructions for the release of Escrow Funds to Seller under Section 4.2 or Section 4.3 of this Escrow Agreement.

Alternatively, if Buyer resists, add to SPA § 11.9 a clarifying sentence:

> "For the avoidance of doubt, Section 9.5(e)(iii) of this Agreement is not a 'limitation of liability stated in' the Escrow Agreement and shall not be overridden by the preceding sentence of this Section 11.9."

---

## 4. SIGNIFICANT: No Security for the $12M Deferred Payment

**Where:** SPA § 2.4.

**The problem.** Topar will not receive $12M until 12 months post-Closing. The Deferred Payment is unsecured. There is no letter of credit, bank guarantee, parent guarantee, or pledge of assets. Topar's sole protection is:

- The interest rate on late payment (prime + 2%, § 2.4);
- The exclusion from Buyer Cap in § 9.5(e)(ii) (so Topar can sue for the full $12M if Buyer doesn't pay);
- The exclusive-remedy carve-out in § 9.8 (so Topar can bring a payment claim outside the indemnification framework).

**Why it matters to Topar.**

- Pritor Healthcare Partners is an LLC. If it is a purpose-entity or thinly capitalized fund vehicle, Topar's $12M receivable is only as good as Pritor's balance sheet 12 months from now.
- SPA § 5.3 (Sufficiency of Funds) is a representation that Buyer "will have" sufficient funds when the Deferred Payment is due, but it is not a Fundamental Representation, so it is subject to the 18-month survival period and the materiality standard. More importantly, a representation is not a guarantee – if Buyer lacks funds at month 12, Topar has a breach-of-rep claim but no security to execute against.

**Recommended fix.**

1. **Require a letter of credit or bank guarantee** in the amount of the Deferred Payment, issued at Closing and running for 12 months plus a grace period. Proposed addition to § 2.4:

   > At the Closing, Buyer shall deliver to Seller an irrevocable letter of credit in the amount of $12,000,000 issued by a federally insured bank with a minimum short-term debt rating of A- (or equivalent) from S&P or Moody's, in form and substance reasonably acceptable to Seller, to secure Buyer's obligation to make the Deferred Payment. The letter of credit shall expire [15] days after the due date of the Deferred Payment.

2. **Alternatively, require a parent guarantee** from Pritor's ultimate parent entity, or a pledge of specific assets.

3. **At minimum, add a default/acceleration trigger:** if Buyer fails to make the Deferred Payment when due, the entire remaining Purchase Price (if any) accelerates and bears default interest at prime + 5%.

**Open question:** What is Pritor's capitalization and ownership structure? Is there a creditworthy parent that would agree to a guarantee? What is Topar's risk appetite for an unsecured $12M receivable?

---

## 5. SIGNIFICANT: Materiality Scrape Increases Exposure on Representation Breaches

**Where:** SPA § 9.5(f).

**The problem.** Section 9.5(f) provides: "For purposes of calculating Losses only, materiality qualifiers in the representations and warranties shall be disregarded."

This means that if, for example, § 4.5 (Financial Statements) says the financials "fairly present in all material respects" the Company's position, and there is a $200K error that is arguably immaterial, the materiality qualifier is scraped out for damages calculation purposes. The full $200K (plus any downstream losses) counts toward the deductible and cap without the "materiality" filter.

**Why it matters to Topar.**

- The scrape converts what would be non-actionable immaterial inaccuracies into actionable ones for purposes of computing Losses.
- Combined with the $1.86M deductible (which is a true deductible, not a tipping basket – § 9.5(b)), the scrape means that even small, individually immaterial breaches across multiple representations can accumulate past the deductible and trigger recovery.
- This is a buyer-favorable provision that is common in PE deals but worth pushing back on given the other uncapped exposures Topar already carries (Specified Matters).

**Recommended fix.**

- **Preferred:** Delete § 9.5(f) in its entirety.
- **Fallback:** Limit the scrape so it does not apply to the deductible calculation: "For purposes of calculating Losses in excess of the Deductible only, materiality qualifiers in the representations and warranties shall be disregarded." This preserves the scrape for quantum but prevents immaterial breaches from counting toward the threshold.
- **Alternative fallback:** Carve out specific representations (e.g., § 4.5 Financial Statements) from the scrape.

---

## 6. SIGNIFICANT: Escrow Earnings Taxed to Buyer

**Where:** Escrow Agreement § 2.4.

**The problem.** Section 2.4 provides: "For income tax purposes, **Buyer** shall be treated as the owner of the Escrow Funds and shall report all earnings on them, until the Escrow Funds are distributed."

The escrow is $18.6M invested in a U.S. Treasury money market fund (§ 2.3). At current short-term rates (~4–5%), that generates roughly $750K–$930K in earnings over the 18-month escrow period. All of that income is taxable to Buyer, not Topar.

**Why it matters to Topar.**

- Topar is economically the owner of the escrow (it is deferred purchase price that will be released to Topar absent valid claims). Having Buyer receive the tax benefit of the earnings is a transfer of value from Topar to Buyer.
- While the dollar amount is modest relative to the deal size, it is an unnecessary concession that was likely not the focus of negotiation.

**Recommended fix.**

Amend Escrow Agreement § 2.4 to provide that earnings are allocated to Seller for tax purposes, or at minimum that the parties will cooperate to ensure the tax treatment reflects economic substance. Proposed language:

> **§ 2.4 Ownership for Tax Purposes.** For income tax purposes, Seller shall be treated as the owner of the Escrow Funds and shall report all earnings on them, until the Escrow Funds are distributed to Seller. If Buyer is required by applicable law to report any such earnings, Buyer shall be entitled to a corresponding offset against amounts otherwise payable to Seller under the Purchase Agreement.

**Open question:** Confirm with Topar's tax advisors whether the current allocation creates any adverse tax consequences for Topar (e.g., if Topar is in a different tax bracket or has different deduction needs).

---

## 7. MODERATE: 30-Day Claim Response Window Creates Operational Burden

**Where:** Escrow Agreement § 3.2.

**The problem.** If Buyer delivers a Claim Notice and Topar does not deliver an Objection Notice within 30 days, the parties "shall" deliver Joint Written Instructions to release the claimed amount to Buyer. This is a deemed-consent mechanism.

**Why it matters to Topar.**

- 30 days is a tight window to investigate a product liability or regulatory claim, assess exposure, and decide whether to object.
- The obligation to co-sign release if Topar stays silent is a strong incentive to object to everything, which could poison the relationship and lead to more disputes going to litigation (and legal fees).
- Given the uncapped Specified Matters exposure (Issue 2 above), a single large product liability claim could arrive with a 30-day clock.

**Recommended fix.**

- Extend the response period to 45 days: "Within **45 days** after receiving a Claim Notice, Seller may deliver…"
- Add a tolling provision: "The period shall be tolled while Seller is awaiting information reasonably necessary to evaluate the claim that is in Buyer's or the Company's possession."
- Change "shall" to "may" for the deemed release: "If the Escrow Agent receives no Objection Notice within that period, Buyer and Seller **may** (but are not obligated to) deliver Joint Written Instructions…"

---

## 8. MODERATE: Outside Date May Be Insufficient Given HSR and Okavi Consent

**Where:** SPA §§ 6.4, 8.1(b).

**The problem.** The SPA is dated March 16, 2026. HSR filings are due within 10 business days (§ 6.4), i.e., by approximately March 30, 2026. The standard HSR waiting period is 30 days, putting the earliest possible closing around late April 2026. The outside date is July 31, 2026 (§ 8.1(b)), leaving roughly three months of buffer.

However, if Okavi consent (Issue 1) requires negotiation, and if HSR results in a second request (which can add 6–12 months), the outside date could be at risk.

**Recommended fix.**

- Extend the outside date to **September 30, 2026** to provide additional buffer, particularly given the Okavi consent issue.
- Add a provision that the outside date is automatically extended by the length of any HSR second request investigation, up to a maximum of [180] additional days.

---

## 9. MODERATE: Conduct-of-Business Restriction on Material Contracts

**Where:** SPA § 6.1(d).

**The problem.** Between signing and Closing, the Company may not "enter into or terminate any contract required to be listed on Schedule 4.6" without Buyer's consent. Schedule 4.6 covers contracts with annual payments over $500K. The Norrland helium agreement (60,000+ liters annually) almost certainly meets this threshold.

If the helium agreement needs to be amended (e.g., to add a new Facility location under Schedule A, or to negotiate a price adjustment under § 5.2), the Company would need Buyer's consent during the pre-Closing period.

**Why it matters to Topar.**

- This could delay necessary operational decisions and give Buyer leverage over routine business matters.
- The "not to be unreasonably withheld" standard helps, but any consent requirement is a friction point.

**Recommended fix.**

- Add an exception for amendments that do not increase the Company's annual payment obligation by more than [10%] or that are required by law.
- Alternatively, confirm that no amendments to the helium agreement are anticipated during the pre-Closing period.

**Open question:** Are there any anticipated amendments to the Norrland helium agreement or other Schedule 4.6 contracts before Closing?

---

## 10. OPEN QUESTIONS (Cannot Be Resolved from the Documents Alone)

| # | Question | Why It Matters |
|---|----------|---------------|
| A | Has Topar contacted Okavi for consent? What is Okavi's response? | Determines whether Issue 1 is fixable before Closing or whether the deal structure needs to change. |
| B | What is in the data room index referenced by Schedules 4.6 and 4.8? | We cannot verify that all material contracts and product liability claims are properly disclosed. An undisclosed claim or contract could give Buyer a post-Closing indemnification claim. |
| C | What is Pritor's ownership structure and creditworthiness? | Directly relevant to the $12M unsecured Deferred Payment (Issue 4). |
| D | What is Celestra's historical product liability loss experience and current insurance tower? | Informs the negotiation of the Specified Matters cap (Issue 2). |
| E | Are there any pending or threatened FDA actions, recalls, or field corrections not reflected in Schedule 4.8? | Would implicate both § 4.7 (Regulatory Compliance) and the Specified Matters definition. |
| F | What is Topar's tax position on the escrow earnings allocation? | Determines whether Issue 6 is worth pursuing. |
| G | Is the Norrland helium agreement listed in the data room index under Schedule 4.6? | If not, § 4.6 may be inaccurate. |

---

## Summary of Recommended Actions (Priority Order)

1. **Immediately contact Okavi** to request written consent to both the assignment and the change of control. Do not execute or deliver the Bill of Sale until consent is in hand. Amend Schedule 4.4 and add a Closing condition.
2. **Open negotiation on Specified Matters** – push for a cap, a temporal limit ("pre-Closing facts only"), and a defined survival period.
3. **Fix the Escrow Agreement § 8.3 / SPA § 9.5(e)(iii) conflict** so that Buyer's obligation to co-sign escrow release is not subject to the $5M Buyer Cap.
4. **Request security for the Deferred Payment** (letter of credit or parent guarantee).
5. **Negotiate the materiality scrape** – delete or limit § 9.5(f).
6. **Address the escrow earnings tax allocation** in Escrow Agreement § 2.4.
7. **Extend the outside date** and add an HSR second-request tolling provision.
8. **Extend the escrow claim response period** from 30 to 45 days.

I am available to draft the specific amendment language for any of the above upon your instruction.