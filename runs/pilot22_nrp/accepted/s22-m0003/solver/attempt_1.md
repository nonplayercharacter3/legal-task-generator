# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Topar Medical Systems / Pritor Healthcare Partners – Seller-Side Exposure Analysis

---

## Summary

I have reviewed the Stock Purchase Agreement (the "SPA"), the Bill of Sale, the Ashcombe Escrow Agreement (the "Escrow Agreement"), and the Norrland Helium Supply Agreement. Below are the issues that create the most significant exposure for Topar as Seller, in descending order of severity.

---

## 1. CRITICAL: Okavi Algorithms Assignment Requires Consent That Has Not Been Obtained or Disclosed

**Where:** Bill of Sale, Annex A, Item 1 (Okavi Reconstruction Software License Agreement, Section 14.2); SPA, Section 4.4 and Schedule 4.4.

**The Problem:**

The Okavi license agreement (Item 1 of Annex A to the Bill of Sale) contains the following assignment restriction:

> "Licensee shall not assign, delegate or otherwise transfer this Agreement or any of its rights or obligations hereunder, whether voluntarily, by operation of law or otherwise, without the prior written consent of Licensor. Any change of control of Licensee, including any transfer of more than fifty percent (50%) of the voting securities of Licensee, shall be deemed a transfer requiring the prior written consent of Licensor. Any purported assignment or transfer in violation of this Section 14.2, including upon any change of control of Licensee, shall be null and void, and Licensor may terminate this Agreement immediately upon written notice."

Two separate consent triggers are implicated:

- **Trigger 1 – Assignment to Celestra.** Section 2.1 of the Bill of Sale assigns the Okavi contract from Topar to Celestra, effective March 30, 2026. The Okavi contract prohibits assignment without Licensor's prior written consent. There is no evidence in the matter folder that Okavi has consented.
- **Trigger 2 – Change of Control of Celestra.** After the assignment, Celestra is the Licensee. The sale of 100% of Celestra's stock to Pritor is a "transfer of more than fifty percent (50%) of the voting securities of Licensee," which the Okavi contract deems a transfer requiring consent. Again, no consent is documented.

**Why It Matters to Topar:**

- SPA Section 4.4 represents that the transactions do not "require any consent of, or notice to, any Person under any contract to which Seller or the Company is a party, including the Assigned Contracts." Schedule 4.4 states "None." If Okavi's consent is in fact required, this representation is false as of the signing date.
- Because Section 4.4 is not a Fundamental Representation, it is subject to the 18-month survival period and the $18.6M cap / $1.86M deductible. However, a breach here could also constitute a breach of the Section 6.2 covenant (pre-closing contribution), which survives until fully performed and is not subject to the cap or deductible under Section 9.5(c) (which carves out only Section 9.2(c) Specified Matters and fraud from the limitations—covenant breaches under 9.2(b) are subject to the cap).
- More critically, if the assignment is "null and void" under the Okavi contract, Celestra never validly received the license. Post-closing, Pritor (as owner of Celestra) could lack the right to use the reconstruction software in its CT and MRI systems. This could give rise to a product liability or regulatory claim that falls within "Specified Matters" (SPA Section 1.1), which are **uncapped** under Section 9.5(c).
- Okavi also has the right to "terminate this Agreement immediately upon written notice," which could disrupt Celestra's product line post-closing.

**Recommended Fix:**

- **Immediately confirm with the client** whether Okavi's written consent to (a) the assignment to Celestra and (b) the change of control of Celestra has been obtained. If not, this must be resolved before Closing.
- If consent has not been obtained, add the Okavi contract to Schedule 4.4 with a description of the consent requirement and the status of the consent request.
- Consider adding a condition to Closing in the SPA that Okavi's written consent to both the assignment and the change of control has been delivered.
- If Okavi refuses consent, evaluate whether the Okavi contract should be removed from Annex A (i.e., not assigned to Celestra) and instead licensed directly to Celestra by Okavi, or whether the deal structure needs to change.

**Open Question:** Has Topar requested or received Okavi's consent? The documents do not indicate.

---

## 2. CRITICAL: Specified Matters Indemnity Is Uncapped and Survival Is Unclear (Potentially Indefinite)

**Where:** SPA, Sections 1.1 (definition of "Specified Matters"), 9.2(c), 9.5(c), and 9.1.

**The Problem:**

Section 9.2(c) requires Topar to indemnify Buyer for "any Specified Matters." The definition of Specified Matters (Section 1.1) covers:

> "(a) any Product Liability Claim relating to any CT or MRI imaging system, or any component of one, manufactured, sold or serviced by the Company, **whether before or after the Closing Date**, and (b) any recall, field safety corrective action or market withdrawal of any such system required by a Governmental Authority or undertaken by the Company in connection with such a Product Liability Claim."

Section 9.5(c) provides that the Seller Cap ($18.6M) and the Deductible ($1.86M) **do not apply** to Losses under Section 9.2(c).

**Survival ambiguity:** Section 9.1 provides survival periods for (i) representations and warranties (18 months, or statute of limitations + 60 days for Fundamental Reps) and (ii) covenants (until fully performed). Section 9.2(c) is neither a representation nor a covenant—it is a freestanding indemnity obligation. The survival provision does not expressly address it. The most natural reading is that it survives until the underlying claims are resolved, which for product liability (especially latent injury claims from medical devices) could be **many years** after Closing.

**Why It Matters to Topar:**

- Topar is giving Pritor an **uncapped, potentially perpetual** indemnity for all product liability claims relating to Celestra's CT and MRI systems, including claims that arise entirely after Closing.
- For a medical device manufacturer, product liability exposure can be severe (personal injury, death, recalls). A single catastrophic recall or a class action could far exceed the $18.6M escrow.
- Because the escrow is the first source of recovery (Section 9.6), the $18.6M escrow would be exhausted quickly in a major product liability event, and Topar would be directly liable for the remainder with no cap.
- This is effectively a product liability insurance policy that Topar is writing for Pritor's benefit, at no premium, with no limit.

**Recommended Fix:**

- **Cap the Specified Matters indemnity.** Propose that Section 9.5(c) be amended so that the Seller Cap applies to Section 9.2(c) as well, or alternatively that a separate (higher) cap applies—e.g., 2x or 3x the escrow amount.
- **Limit the look-back.** If Buyer insists on post-closing product liability coverage, negotiate a time limit (e.g., claims arising from products manufactured before the Closing Date only, or a survival period of 3–5 years after Closing).
- **Clarify survival.** Add express language in Section 9.1 stating that the indemnity under Section 9.2(c) survives for a defined period (e.g., the applicable statute of limitations for product liability claims in the jurisdictions where the Company sells, plus 60 days).
- **Require Buyer to maintain product liability insurance.** Add a covenant requiring the Company (and thus Buyer post-closing) to maintain product liability insurance with limits adequate to cover Specified Matters, with Topar named as an additional insured or with a loss-payable clause, so that insurance proceeds reduce Topar's exposure.

**Proposed Language (cap on Specified Matters):**

> Section 9.5(c) is deleted in its entirety and replaced with: "The cap in Section 9.5(a) shall apply to Losses under Section 9.2(c), except that Seller's aggregate liability for Specified Matters shall not exceed $[37,200,000] (two times the Escrow Amount). The deductible in Section 9.5(b) shall not apply to Losses under Section 9.2(c). The cap in Section 9.5(a) and the deductible in Section 9.5(b) shall not apply to Losses arising from fraud by Seller."

**Proposed Language (survival for Specified Matters):**

> Add to Section 9.1: "The indemnification obligation of Seller under Section 9.2(c) shall survive the Closing until the expiration of the applicable statute of limitations (including any tolling or extension) for the Product Liability Claim or Specified Matter giving rise to the Losses, plus sixty (60) days."

---

## 3. HIGH: Escrow Agreement Caps Buyer's Liability for Withholding Release Instructions at $5M, Overriding the SPA Carve-Out

**Where:** Escrow Agreement, Section 8.3; SPA, Sections 9.5(d), 9.5(e)(iii), and 11.9.

**The Problem:**

- SPA Section 9.5(e)(iii) carves out from the Buyer Cap ($5M) "Buyer's obligations to deliver joint written instructions to the Escrow Agent for the release of Escrow Funds under Section 2.3 and the Escrow Agreement." This means the SPA intends that Buyer's obligation to co-sign release instructions is **uncapped**.
- Escrow Agreement Section 8.3 provides: "The aggregate liability of Buyer to Seller arising under or in connection with this Escrow Agreement or Article IX of the Purchase Agreement, **including with respect to release of Escrow Funds**, shall not exceed the Buyer Cap, except for fraud."
- SPA Section 11.9 (Order of Precedence) states: "In the event of any conflict between this Agreement and the Escrow Agreement, **the Escrow Agreement shall prevail with respect to releases of Escrow Funds and the limitations of liability stated therein**."

Read together, the Escrow Agreement's $5M cap on Buyer's liability "with respect to release of Escrow Funds" prevails over the SPA's carve-out in Section 9.5(e)(iii).

**Why It Matters to Topar:**

- At the end of the 18-month Escrow Period, Section 4.2 of the Escrow Agreement requires Buyer and Seller to deliver Joint Written Instructions releasing the remaining Escrow Funds to Seller. If Buyer wrongfully refuses to sign (e.g., asserting a colorable but meritless claim to hold the funds), Topar's damages claim against Buyer for that refusal is capped at $5M.
- The Escrow Amount is $18.6M. If Buyer withholds its signature, Topar could be locked out of up to $18.6M with only a $5M remedy.
- The same issue arises during the Escrow Period if Buyer files a Claim Notice and then refuses to agree to release undisputed portions.

**Recommended Fix:**

- Amend Escrow Agreement Section 8.3 to add a carve-out mirroring SPA Section 9.5(e)(iii):

> "The aggregate liability of Buyer to Seller arising under or in connection with this Escrow Agreement or Article IX of the Purchase Agreement shall not exceed the Buyer Cap, except for (a) fraud, and (b) Buyer's obligation to deliver Joint Written Instructions for the release of Escrow Funds to Seller under Sections 3.2, 3.4 and 4.2 of this Escrow Agreement."

- Alternatively, add to SPA Section 11.9 a clarification that the Escrow Agreement's precedence does not apply to the extent it would reduce Seller's remedies below those provided in SPA Section 9.5(e).

---

## 4. HIGH: Materiality Scrape Expands Topar's Indemnification Exposure

**Where:** SPA, Section 9.5(f).

**The Problem:**

Section 9.5(f) provides: "For purposes of calculating Losses only, materiality qualifiers in the representations and warranties shall be disregarded."

This means that even though Topar's representations are qualified by materiality (e.g., Section 4.5: financial statements "fairly present **in all material respects**"; Section 4.7: compliance "in **all material respects**"; Section 4.6: "neither the Company nor, to Seller's knowledge, any counterparty is in **material** breach"), those qualifiers are stripped out when calculating whether a breach occurred and the amount of Losses.

**Why It Matters to Topar:**

- A technically accurate but immaterial inaccuracy in the financial statements, a minor regulatory compliance gap, or a de minimis contract breach could all give rise to an indemnification claim.
- Combined with the 18-month survival period and the fact that the deductible is only $1.86M, this materially increases the likelihood that small issues will aggregate past the deductible and trigger payments from the escrow.
- The materiality scrape is one-way in effect: it only helps Buyer in calculating Losses against Seller. There is no reciprocal scrape for Buyer's representations (though in practice Buyer's reps are fewer and less detailed).

**Recommended Fix:**

- Delete Section 9.5(f) in its entirety, or limit it so that it applies only to Fundamental Representations (where the bring-down standard is already "in all respects" under Section 7.2(a), making the scrape less impactful).
- If Buyer insists on retaining the scrape, negotiate a higher deductible (e.g., 2% of the Purchase Price = $3.72M) to offset the increased claim frequency.

---

## 5. MEDIUM: $12M Deferred Payment Is Unsecured

**Where:** SPA, Sections 2.4 and 5.3.

**The Problem:**

The Deferred Payment of $12,000,000 is due 12 months after Closing. While Section 5.3 contains a representation of sufficient funds, and Section 9.5(e)(ii) carves the Deferred Payment out of the Buyer Cap (so Topar's claim for non-payment is not limited to $5M), there is **no security** for the Deferred Payment—no letter of credit, no guarantee, no pledge of assets, and no right to accelerate upon a credit event.

**Why It Matters to Topar:**

- Topar is extending $12M of unsecured credit to a private equity buyer. If Pritor experiences financial distress within the 12-month window (e.g., the portfolio company underperforms, or Pritor's fund faces redemption pressure), Topar would be an unsecured creditor in any bankruptcy.
- The interest provision (prime + 2%) compensates for time value but does not address credit risk.

**Recommended Fix:**

- Request a **parent guarantee** or **letter of credit** from Pritor's sponsor or fund for the Deferred Payment amount.
- Alternatively, negotiate a **security interest** in the Shares (or in a portion of the escrow) as collateral for the Deferred Payment, to be released upon payment.
- Add an **acceleration trigger**: if Buyer breaches any representation or covenant, or if Buyer's net worth falls below a specified threshold, the Deferred Payment becomes immediately due.

**Proposed Language:**

> "The Deferred Payment shall be secured by an irrevocable letter of credit issued by a nationally recognized bank in an amount equal to the Deferred Payment, delivered to Seller at the Closing. The letter of credit shall remain in effect until the Deferred Payment has been paid in full."

---

## 6. MEDIUM: 30-Day Claim Response Deadline in Escrow Agreement Creates Procedural Risk

**Where:** Escrow Agreement, Section 3.2.

**The Problem:**

If Buyer delivers a Claim Notice, Topar has only **30 days** to deliver an Objection Notice. If Topar misses the deadline, the parties are obligated to deliver Joint Written Instructions releasing the claimed amount to Buyer within five Business Days.

**Why It Matters to Topar:**

- Product liability and regulatory claims can be complex. Thirty days may be insufficient to investigate, assess merit, and prepare a reasoned objection—particularly for claims involving technical issues (e.g., whether a particular MRI system defect caused an injury).
- The consequence of missing the deadline is severe: deemed acceptance of the claim and mandatory release of funds.
- The SPA's claims procedure (Section 9.4) requires only "prompt written notice" from the Indemnified Party and does not impose a similar 30-day response deadline on the Indemnifying Party. The Escrow Agreement's deadline is stricter and applies specifically to escrow claims.

**Recommended Fix:**

- Extend the response period from 30 days to **45 or 60 days**, with one automatic 15-day extension if Topar delivers a written request stating that additional time is needed for a complex claim.
- Add a provision that if the Claim Notice does not include sufficient detail to evaluate the claim (e.g., no identification of the specific product, patient, or regulatory action), the 30-day period does not begin to run until Buyer supplements the notice.

**Proposed Language:**

> "Within forty-five (45) days after receiving a Claim Notice that includes the information required by Section 3.1, Seller may deliver an Objection Notice. If the Claim Notice does not describe the claim in reasonable detail as required by Section 3.1, the response period shall not commence until Buyer delivers a supplemented Claim Notice that does so."

---

## 7. MEDIUM: SPA Section 4.4 Representation May Be Breached by the Norrland Agreement (Lower Risk)

**Where:** SPA, Section 4.4; Helium Supply Agreement, Section 14.1.

**The Problem:**

The Norrland Helium Supply Agreement is a contract of Celestra (the Company), not an Assigned Contract. Section 14.1 provides that "A change in the ownership or control of either Party is not an assignment under this Section 14.1 and does not require the consent of the other Party."

This means the stock sale does not trigger a consent requirement under the Norrland agreement. **This is not an issue.** I flag it only to confirm that, unlike the Okavi contract, the Norrland agreement does not create a consent problem.

However, note that the Norrland agreement contains a Minimum Annual Volume commitment (60,000 liters/year, Section 2.2) and a price adjustment mechanism (Section 5.2). These are ongoing commercial obligations of Celestra that Buyer inherits. They do not create direct exposure for Topar post-closing, but they are relevant to the valuation and to whether Buyer's "sufficiency of funds" representation (Section 5.3) is well-founded.

**No action required** on this point, but be prepared for Buyer to raise the Norrland minimum volume commitment in post-closing disputes if Celestra's MRI production declines.

---

## 8. LOWER: Escrow Agent Fee Allocation and Tax Treatment

**Where:** Escrow Agreement, Sections 2.4 and 7.1; SPA, Section 11.1.

**The Problem:**

- Escrow Agent fees are split 50/50 between Buyer and Seller (Escrow Agreement Section 7.1; SPA Section 11.1). The fees are modest ($5,000 acceptance + $7,500/year + $50/wire), so this is not a significant economic issue.
- Section 2.4 of the Escrow Agreement provides that **Buyer** is treated as the owner of the Escrow Funds for income tax purposes and reports all earnings. The earnings become part of the Escrow Funds and are ultimately released to Seller. This means Buyer bears the tax on earnings that economically benefit Seller (if the funds are released to Seller) or Buyer (if used to pay claims).

**Why It Matters:**

- If the escrow earns, say, $200,000 in interest over 18 months and that amount is released to Seller at the end, Seller receives tax-free income (because Buyer already reported it). This is a modest benefit to Topar.
- Conversely, if the earnings are used to pay a claim against Topar, Topar effectively bears the economic cost of Buyer's tax on those earnings. This is a minor point.

**Recommended Fix:** None needed. The structure is favorable to Topar in the base case (full release at end of escrow period).

---

## 9. OPEN QUESTIONS REQUIRING CLIENT INPUT

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Has Topar obtained Okavi's written consent to (a) the assignment of the Okavi license to Celestra and (b) the change of control of Celestra? If not, has a consent request been made, and what is Okavi's response? | Determines whether Schedule 4.4 is accurate and whether the assignment is valid. If consent is refused, the deal structure may need to change. |
| 2 | What product liability claims, recalls, or field corrections are listed in the data room index referenced by Schedule 4.8? | The Specified Matters indemnity (Section 9.2(c)) covers all such claims, whether before or after Closing. Understanding the known exposure is essential to negotiating a cap or insurance requirement. |
| 3 | Does Topar have product liability insurance that would cover Specified Matters arising from pre-Closing products? If so, what are the limits and does the policy include a "buy-side" or "seller-side" provision? | If insurance is available, it could serve as the primary source of recovery for Specified Matters, reducing Topar's out-of-pocket exposure. Section 9.5(g) already provides that Losses are calculated net of insurance proceeds, but only for insurance "actually received by the Indemnified Party" (i.e., Buyer/Company). Topar's own insurance may not be credited. |
| 4 | What is the expected Closing Date? The SPA allows termination if Closing has not occurred by July 31, 2026 (Section 8.1(b)). | If HSR review or other conditions delay Closing beyond July 31, either party can walk. Topar should be aware of the timeline risk. |
| 5 | Are there any other contracts of Topar (not listed in Annex A) that contain change-of-control or assignment restrictions that could be triggered by the sale of Celestra's stock? | The SPA Section 4.4 representation covers contracts "to which Seller or the Company is a party." If Topar has other contracts with change-of-control provisions (e.g., credit facilities, key supplier agreements), those could also require disclosure. |

---

## Priority Action Items

1. **Resolve the Okavi consent issue before Closing.** This is the most urgent item. If consent has not been obtained, the SPA representation in Section 4.4 is inaccurate, the assignment may be void, and Topar faces uncapped Specified Matters exposure if the software license is terminated post-closing.
2. **Negotiate a cap and survival limit on the Specified Matters indemnity (Section 9.2(c)).** As drafted, Topar is writing an uncapped, potentially perpetual product liability indemnity. This is the single largest financial exposure in the transaction documents.
3. **Fix the Escrow Agreement cap conflict (Section 8.3 vs. SPA Section 9.5(e)(iii)).** Ensure that Buyer's obligation to co-sign release instructions is not subject to the $5M Buyer Cap.
4. **Address the materiality scrape (Section 9.5(f))** or, at minimum, increase the deductible to compensate.
5. **Secure the Deferred Payment** with a letter of credit or equivalent.