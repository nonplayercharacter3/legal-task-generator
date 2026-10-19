# MEMORANDUM

**To:** Partner
**From:** Associate
**Date:** October 18, 2026
**Re:** Marrowind Packaging Corp. / Tessaly Holdings LLC: seller-side review of the deal package (APA, TSA, Bill of Sale, Escrow Agreement)

---

## 1. Scope and Bottom Line

I reviewed all four documents individually and against each other. Abbreviations are APA, TSA, BoS and Escrow Agt.

**Three caveats:**
- The Disclosure Schedule and exhibits are not in the folder. I could not check the schedules cited in APA §§2.1, 2.1(c), 4.4, 4.8 and 6.4, or Escrow Agt Schedule A (blank).
- The APA is dated October 30, 2026, which is after today. I assume it is unsigned, so the APA itself is still open for negotiation, not only the ancillaries.
- New York authorities are cited from general knowledge and need a cite-check before anything goes to the other side.

**Bottom line.** The documents line up on the mechanics:
- The purchase price, the $1,840,000 escrow, and the 18-month survival and escrow release are the same across documents.
- The cross-references I checked are accurate: TSA Recital B to APA §6.6, BoS Recital B to APA §§3.2(a) and 3.3(b), Escrow Recital C to APA §§3.2(c) and 3.3(b), and Escrow Agt §3.6 and TSA §7.3 to APA §§9.6 and 9.5.

They do not line up on substance, in four main ways:
1. The APA's indemnity limits do not work as drafted (Item 1).
2. The BoS defines "Purchased Assets" differently from the APA and conveys assets Marrowind is keeping (Item 2).
3. The TSA uses Delaware law, and it assumes Marrowind still has people, systems and contracts that the APA sells to Tessaly (Items 4, 5 and 6).
4. The consent mechanics conflict across the APA and BoS (Item 3).

---

## 2. Issues, Most Significant First

### Item 1. The indemnity cap and basket do not apply to rep breaches (Critical)
**Where:** APA §9.4(a)–(c), read with §§9.2, 9.1 and 1.1(m).

**Issue.** The basket in §9.4(b) applies only to claims under §9.2(a). Section 9.4(c) then says §9.4(a) and (b) "shall not apply to any claim under Section 9.2(a)." The result:
- The $184,000 basket never operates.
- The 10% cap ($1,840,000) can apply only to §9.2(b) and (c), meaning covenants and Excluded Assets/Liabilities.
- Every rep breach is uncapped, including the flat, unqualified reps in §4.6 (condition and adequacy of assets), §4.9 (non-infringement) and §4.10 (environmental), and the §4.4 consents rep.

It looks like a drafting error. The intended exception was almost certainly the "Fundamental Representations" defined in §1.1(m), a term that is never used in Article IX other than in the §9.1 survival clause.

**Why it matters.** Marrowind's exposure on ordinary reps is unlimited, when the deal economics suggest $1.84M (escrow = cap). The general reps survive 18 months (§9.1).

**Fix.** Redraft §9.4:

> "(a) Seller's aggregate liability under Section 9.2(a), other than for breach of a Fundamental Representation, shall not exceed the Escrow Amount, and the Escrow Funds shall be the sole and exclusive source of recovery for such claims. (b) Seller shall not be liable under Section 9.2(a), other than for breach of a Fundamental Representation, until aggregate Losses exceed $184,000, and then only for Losses in excess of that amount. (c) Seller's aggregate liability under this Article IX shall in no event exceed the Purchase Price. Nothing in this Section 9.4 limits liability for Fraud."

Also revise §9.6, which now says Buyer recovers "first" from escrow "and thereafter directly by Seller," so that it matches the sole-recourse language.

**Related points:**
- **Buyer cap (§9.4(d)).** Make it symmetrical, with an exception for Buyer's own fundamental reps (§§5.1, 5.2, 5.4).
- **Buyer's likely counter.** Buyer will probably want the §9.2(c) Excluded Liabilities claim uncapped. Decide in advance whether to concede that (see Business Decisions).

### Item 2. The BoS defines "Purchased Assets" more broadly than the APA and conveys retained assets (Critical)
**Where:** BoS §§1.1(b), 2.1, 2.3, 4.2; APA §§2.1, 2.2, 10.12.

**Issue.**
- APA §2.1 sells assets "other than the Excluded Assets." APA §2.2 retains cash, the Albany manufacturing facility, and the HOLLIS trademark.
- BoS §1.1(b) redefines the term as "all assets, properties and rights of every kind and nature, whether real, personal or mixed … wherever located." It has no Excluded Asset carve-out.
- BoS §1.1(b)(iv) specifically lists "trademarks, trade names." APA §2.1(d) lists only IP "including customer dies and print plates."
- BoS §2.1 is a present, irrevocable conveyance ("hereby irrevocably sells…"). On its face it transfers the Albany facility, cash and HOLLIS.
- BoS §1.1 says undefined terms take APA meanings, but "Purchased Assets" is defined locally, so the BoS definition governs.
- APA §10.12 says the APA controls over an Ancillary Agreement "except that each Ancillary Agreement controls as to its specific subject matter." The BoS's specific subject matter is the conveyance, so Buyer can argue the BoS definition wins.
- The BoS power of attorney (§2.3) and trust-over clause (§4.2) both run off the same defined term, so they extend to the retained assets too.

**Why it matters.** This is the most direct route by which Marrowind could lose assets it bargained to keep.

**Related gap.** The APA does not carve out the "Marrowind" corporate name. Because "trade names" are conveyed, Marrowind could lose its own name. This is a business decision (see Section 4).

**Fix.**
- BoS §1.1(b): delete the local definition and enumerated list and replace with:
  > "'Purchased Assets' has the meaning given in the Purchase Agreement and expressly excludes the Excluded Assets, including Seller's cash, the Albany manufacturing facility and the HOLLIS trademark."
- Add BoS §5.9:
  > "This Bill of Sale is delivered pursuant to, and is subject to, the Purchase Agreement. Nothing in this Bill of Sale expands, limits, supersedes or merges any provision of the Purchase Agreement, including Article IX. If there is any conflict, the Purchase Agreement controls. Seller makes no representation or warranty in this Bill of Sale."
- APA §10.12: narrow the exception:
  > "…this Agreement controls; provided that the Escrow Agreement governs solely the duties of the Escrow Agent and the administration of the Escrow Account, and the Transition Services Agreement governs solely the Services and Service Fees."
- Expand APA §2.2 to also exclude the Seller corporate name and organizational records, insurance policies, tax refunds, claims relating to Excluded Assets/Liabilities, and rights under the Transaction Documents.

### Item 3. Consents: closing condition, covenant and BoS holding mechanism conflict (High)
**Where:** APA §§3.2(e), 4.4, 6.3, 7.1(d); BoS §3.4.

**Issue.**
- APA §3.2(e) makes delivery of "the third-party consents listed in Section 4.4 of the Disclosure Schedule" a Seller closing delivery. Under §7.1(d), delivery of the §3.2 items is a condition to Buyer's obligation to close.
- But §6.3 requires only "commercially reasonable efforts" to obtain consents, and BoS §3.4 assumes Closing can occur without them.
- The APA has no non-assignable-contract provision of its own, so the real mechanism sits in the BoS, a document Buyer might argue is outside the APA's indemnity and cap framework.
- Any consent not delivered gives Buyer a free walk right or price-renegotiation lever (the outside date is December 31, 2026, §8.1(b)).
- The §4.4 rep ("lists each consent required") is flat and, per Item 1, uncapped.
- BoS §3.4 is open-ended and one-sided:
  - Marrowind holds contracts for Buyer indefinitely.
  - It has no cost reimbursement and no end date.
  - It remains liable to the counterparty while Buyer's performance is only "to the extent" the obligations would have been Assumed Liabilities.
  - It must "continue" its efforts to obtain consents after Closing, with no limit.

**Fix.**
- APA §3.2(e): "…the third-party consents listed in Section 4.4 of the Disclosure Schedule that have been obtained as of the Closing." If Buyer needs certain consents, limit §7.1(d) to a short list of "Required Consents" in a schedule (business decision).
- Add a new APA §6.8 and conform BoS §3.4:
  > "If any Assigned Contract cannot be assigned without a consent not obtained at Closing, the Closing shall proceed and, until the earliest of receipt of the consent, expiration of the contract, and [12] months after Closing, Seller shall provide Buyer the economic benefits of the contract and Buyer shall perform all obligations thereunder arising after Closing at Buyer's cost. Buyer shall indemnify Seller for all Losses arising from the contract or this arrangement. Seller is not required to pay any amount, commence any proceeding, or amend the contract. Seller's post-Closing consent efforts are limited to requests not requiring payment, and Buyer shall bear any consent fee."

### Item 4. TSA uses Delaware law and Delaware courts; every other document uses New York (High)
**Where:** TSA §9.3 (and §9.4); APA §§10.8–10.10; BoS §§5.5–5.6; Escrow Agt §§7.1–7.2.

**Issue.**
- TSA §9.3 selects Delaware law and exclusive Delaware courts for claims "arising out of or relating to this Agreement or the Services." The other three documents select New York law and New York County courts.
- Buyer is a Delaware LLC based in Wilmington (APA §10.2), so the TSA choice favors Buyer's home forum.
- Disputes that straddle the documents are plausible: data ownership under TSA §6.2 turns on what is a "Purchased Asset", and the APA §9.2(b) covenant theory in Item 6 mixes APA and TSA obligations. Those could be litigated in two courts under two bodies of law, with the risk of inconsistent results.
- Marrowind is a New York corporation based in Rochester.
- Statutory support for a New York choice should be available. N.Y. Gen. Oblig. Law §5-1401 permits a New York choice of law for transactions of $250,000 or more. The TSA fee stream is at most about $285,000 if every Service ran its full duration (Schedule A: $18,500×6 + $9,000×3 + $14,000×6 + $4,500×4 + $7,500×6), so it is close to the threshold and falls if Buyer terminates Services early. The TSA is, however, expressly part of the $18.4M transaction (TSA Recitals). Please verify the application.

**Fix.** Replace TSA §9.3 with the APA §§10.8–10.9 text:
> "…governed by the Laws of the State of New York… exclusive jurisdiction of the State and federal courts located in New York County, New York."

This is a likely first-round concession ask, so decide whether it is a hold point (see Business Decisions).

### Item 5. The TSA assumes Marrowind still has the people, systems and contracts that the APA transfers (High)
**Where:** TSA §3.1, §3.2, Schedule A (Services 1–5); APA §§2.1(b)–(d), 2.1(g), 6.4.

**Issue.**
- **Employees.** Service 5 (Customer Service) uses "Seller's existing customer service personnel." Service 1 relies on Seller finance staff. Service 2 covers "transferred employees." APA §6.4 has Buyer offering employment "effective on the Closing Date" to the Schedule 6.4 employees. If those employees go to Buyer, Marrowind cannot staff the Services. TSA §3.2(a) nonetheless sets a standard of "quality consistent with how Seller provided the Service" in the prior 12 months. I could not check Schedule 6.4.
- **Systems.** Service 3 has Seller hosting "Seller's ERP, email and order-management systems." Under APA §2.1 Buyer buys "all assets used or held for use in the Business" and all IP, which would include those systems unless listed as retained.
- **Contracts.** Service 4 has Seller buying linerboard, medium and starch "under Seller's existing supplier arrangements." If those are Assigned Contracts, Marrowind no longer holds them.
- **Credit and funding.** Marrowind would be buying materials on its own credit for Buyer, and invoices go monthly in arrears with 30-day payment terms (TSA §5.2). That means up to 60+ days of working-capital exposure. Payroll under Service 2 has the same funding problem.
- **Customer-facing exposure.** Under Service 5, Marrowind is taking Buyer's customer orders. The TSA does not say Marrowind acts only as Buyer's service provider, in Buyer's name.

**Why it matters.** Marrowind could be in breach of the TSA on day one for something it cannot control. Its exposure is capped (TSA §7.2) but still real.

**Fix.**
- Run a service-by-service feasibility check against Schedules 2.1 and 6.4 with the client's operations team.
- Add new TSA §3.7:
  > "Seller is not required to provide a Service, and is not liable for any failure or delay, to the extent it depends on any employee, system, software, contract or other asset transferred to Buyer under the Purchase Agreement. Buyer shall make such Buyer Resources available to Seller as reasonably necessary to provide the Services."
- Revise Schedule A so that "using Seller's existing customer service personnel" reads "using personnel made available by Buyer."
- Add a prefunding mechanic:
  > "Buyer shall fund pass-through costs and payroll in cleared funds at least [two] Business Days before Seller is required to pay them."
- Add: "Seller acts solely as service provider and in the name of Buyer. Buyer bears all liability to customers for orders, products and pricing."

### Item 6. TSA performance can be pulled into the APA indemnity, bypassing the TSA liability cap (High)
**Where:** APA §§6.6, 9.2(b), 9.6, 9.8; TSA §§7.2, 7.3; Escrow Agt §3.1.

**Issue.**
- APA §6.6 says Seller and Buyer "shall enter into the Transition Services Agreement, under which Seller shall provide certain services to Buyer for a term of six months." That is a covenant in the APA.
- APA §9.2(b) covers "any breach of any covenant or agreement of Seller in this Agreement." Buyer can argue a TSA service failure is also an APA §6.6 breach.
- If so, Buyer could avoid the TSA's limits (the §7.2 fee-based cap, the consequential-damages waiver, and the gross negligence/willful misconduct indemnity standard in §7.3) and claim against the escrow under Escrow Agt §3.1, which covers any claim "under Section 9.2."
- APA §9.8 makes Article IX the exclusive remedy for breach of APA covenants. That strengthens Buyer's argument that the TSA breach belongs there.

**Fix.** Add to APA §6.6:
> "Seller's obligations with respect to the Services are solely as set forth in the Transition Services Agreement. No breach or alleged breach of the Transition Services Agreement constitutes a breach of this Agreement or gives rise to any claim under Article IX or against the Escrow Funds, and the remedies in the Transition Services Agreement are the sole and exclusive remedies for any such breach."

Add a mirror sentence to Escrow Agt §3.1.

### Item 7. Escrow release mechanics favor Buyer (High)
**Where:** Escrow Agt §§3.1–3.4, 4.1, 4.2, 7.4; APA §§9.5, 10.2.

**Issues.**
1. **Deemed acceptance and a short clock (§§3.2, 3.3).** If the Escrow Agent receives no Objection Notice within 30 days of Seller's receipt of a Claim Notice, it pays Buyer the full amount claimed on the fifth Business Day. There is no check on the claim and no confirmation from Seller.
2. **Actual-receipt rule (§7.4).** Notices to the Escrow Agent are "effective only on actual receipt." Marrowind's objection must therefore physically reach Corbel inside 30 days. Seller bears the transmission risk.
3. **No email addresses (APA §10.2).** The notice provision permits email notice, deemed given "when sent by email with confirmation of transmission," but lists only street addresses. Seller's address is "Attention: Chief Executive Officer," with no copy to counsel. A Claim Notice could therefore be deemed delivered without reaching anyone in a position to act.
4. **No tie to APA limits (§3.1).** A Claim Notice need only state an amount and "the provision of the Purchase Agreement" relied on. It need not account for the basket, the cap or survival. An uncontested notice pays out automatically even if the claim is below the basket or time-barred.
5. **Unlimited holdback (§§4.1, 3.5).** The Pending Claims Amount at the Release Date is "the aggregate amount of all claims stated in Claim Notices." A single inflated or unliquidated estimate could lock up the entire escrow past the 18-month release.
6. **No cooperation covenant.** Resolving a disputed claim requires Joint Written Instructions or a Final Order (§3.4). Nothing obliges Buyer to sign instructions once a claim is agreed or lost.

**Fix.**
- §3.1: add:
  > "Buyer shall deliver a Claim Notice only for a claim as to which, after giving effect to Section 9.4 of the Purchase Agreement, Buyer reasonably and in good faith believes it is entitled to recover from the Escrow Funds, and any estimated amount shall be Buyer's reasonable good-faith estimate."
- §3.2: extend the period to 45 days, running from delivery in accordance with §7.4, and add:
  > "An Objection Notice sent to the Escrow Agent by email and overnight courier within the period is timely, and the Escrow Agent shall promptly acknowledge receipt."
- §3.3: add:
  > "Buyer shall certify to the Escrow Agent in each Claim Notice the date and manner of delivery to Seller. The Escrow Agent shall not pay any claim until this certification is delivered."
- §4.1: limit the Pending Claims Amount to "the reasonable good-faith estimate of the Losses claimed, not exceeding the amount stated, for claims that have not been objected to or finally determined."
- Add:
  > "Within three Business Days after any amount is agreed or finally determined, Seller and Buyer shall sign Joint Written Instructions to the Escrow Agent."
- APA §10.2: add email addresses and a copy line to outside counsel for each side.

### Item 8. "Fraud" is undefined, and there is no entire-agreement or non-reliance clause (High)
**Where:** APA §§9.4(c), 9.8, Article X (no integration clause), Article IV.

**Issue.**
- Fraud claims sit outside both the cap (§9.4(c)) and the exclusive remedy (§9.8), yet "fraud" is undefined.
- The APA, like the three ancillaries, has no entire-agreement clause and no non-reliance language.
- Under New York law, a specific disclaimer of reliance is what bars fraud claims based on extra-contractual statements (*Danann Realty Corp. v. Harris*, 5 N.Y.2d 317 (1959)). Without one, statements in management presentations or data rooms could support uncapped fraud claims.
- The APA is also silent on sandbagging. New York law generally lets a buyer recover for a breached warranty it relied on even if it had doubts (*CBS Inc. v. Ziff-Davis Publishing Co.*, 75 N.Y.2d 496 (1990)). A buyer that closes with knowledge of the breach from the seller's disclosure may be barred unless it expressly preserves its rights (*Galli v. Metz*, 973 F.2d 145 (2d Cir. 1992)).

**Fix.** Add a definition and new provisions:
> "'Fraud' means actual and intentional common-law fraud under New York law in the making of an express representation in Article IV or V, committed with actual knowledge of its falsity and intent to induce reliance, and excludes constructive fraud, negligent misrepresentation, and recklessness."
>
> "Entire Agreement; Non-Reliance. This Agreement, the Ancillary Agreements and the Disclosure Schedule are the entire agreement of the Parties on their subject matter. Buyer acknowledges that, except for the representations in Article IV, Seller has made no representation or warranty, and Buyer has not relied on any other statement, projection or information, including in any data room or management presentation."
>
> "Seller shall have no liability for any breach of which Buyer had actual knowledge before the Closing."

Make the same cross-reference to the APA in each ancillary (see Item 2).

### Item 9. Working capital adjustment is incomplete, and "assumed payables" depends on it (High)
**Where:** APA §§2.3(b), 2.7, 2.4.

**Issues.**
- **No definition.** "Net working capital" is not defined (no components, accounting principles or sample calculation). The $2,150,000 target is a bare number. Buyer prepares the statement alone.
- **Circular reference.** §2.3(b) has Buyer assume trade payables "reflected in the Closing statement under Section 2.7." But the §2.7 statement is a net working capital statement delivered up to 60 days *after* Closing. Any payable not reflected remains an Excluded Liability that Marrowind must pay (§2.4).
- **Procedural gaps.**
  - It is unclear when Seller's 30 days to object begin.
  - There is no default if Buyer is late.
  - There is no right of access to Buyer's workpapers.
  - There is no tie-breaker if the Parties cannot agree on the accounting firm.
  - There is no allocation of the firm's fees.
  - There is no payment deadline.
  - There is no cap or collar.
  - It does not say the adjustment cannot be paid from the escrow, or that Buyer cannot set it off against other amounts.

**Fix.**
- Add a definition: Net Working Capital means the inventory and accounts receivable included in the Purchased Assets, less the trade payables assumed under §2.3(b), calculated under GAAP consistently applied with the audited 12/31/2025 balance sheet and the illustrative calculation in Exhibit [__], excluding cash, income taxes and Excluded Assets/Liabilities.
- §2.3(b): "…trade accounts payable of the Business incurred in the ordinary course to the extent included as a current liability in Net Working Capital as finally determined under Section 2.7."
- §2.7: Seller's objection period runs 30 days from receipt of the statement and Buyer's supporting records. If Buyer fails to deliver in 60 days, Seller's good-faith statement controls. If the Parties cannot agree on the firm within 10 days, [name] serves. The firm's fees are allocated in inverse proportion to success. Payment is due within five Business Days of final determination. The adjustment is not payable from the Escrow Funds and no party may set off.
- Consider a collar or cap (see Business Decisions).

### Item 10. Non-compete conflicts with the retained Albany manufacturing facility (Medium-High)
**Where:** APA §§6.5, 2.2, 10.7, 10.11.

**Issue.**
- §6.5 bars Marrowind from "the manufacture or sale of corrugated packaging products within the United States" for three years, "except through the ownership of the Excluded Assets in a manner that does not compete with the Business."
- The Excluded Assets include a *manufacturing facility* and the HOLLIS trademark. The exception is circular. If Albany makes anything corrugated, whether it "competes with the Business" is a fight waiting to happen, and §10.11 gives Buyer injunctive relief.
- The clause is silent on Marrowind Affiliates, passive investments, and the TSA services, which are themselves support for a competitor's business.
- Nationwide scope and three years are likely defensible in a sale-of-business setting under New York's reasonableness standard, but the vagueness is the problem.

**Fix.** Replace the exception with:
> "…provided that nothing in this Section 6.5 restricts Seller or its Affiliates from (a) owning and operating the Albany manufacturing facility and the HOLLIS business in the fields described in Schedule 6.5; (b) passive ownership of up to 5% of any class of public securities; or (c) performing the Services."

The fields in Schedule 6.5 need client input (see Business Decisions).

### Item 11. The BoS power of attorney is irrevocable, broad, and not in the APA (Medium-High)
**Where:** BoS §2.3; APA §6.7.

**Issue.**
- §2.3 gives Buyer, "and its successors and assigns," an irrevocable power of attorney "coupled with an interest" with full substitution. Buyer can sue in Marrowind's name and endorse Marrowind checks.
- It is not limited to the APA-defined assets (see Item 2), has no time limit, no notice requirement, no cost allocation, and no limit on binding Marrowind to settlements or admissions.
- The APA contemplates only reasonable mutual further assurances (§6.7).

**Fix.** Add to §2.3:
> "This power is limited to Purchased Assets as defined in the Purchase Agreement (excluding all Excluded Assets), is exercisable only after Buyer has requested Seller's action under Section 4.1 and Seller has failed to act within 10 Business Days, is at Buyer's sole cost and subject to Buyer's indemnification of Seller, does not authorize Buyer to bind Seller to any liability, make any admission, or settle any claim on Seller's behalf, and expires [two] years after the Closing Date."

### Item 12. Conveyance takes effect at 12:01 a.m. before payment (Medium)
**Where:** APA §3.1; BoS §2.1; APA §2.6.

**Issue.** Title passes "effective as of 12:01 a.m. Eastern Time on the Closing Date" and the BoS conveys "irrevocably." Payment is by wire later that day. If the funds do not arrive, Marrowind has already conveyed.

**Fix.** Revise APA §3.1 and BoS §2.1: "The BoS and other Closing deliveries are held in escrow by counsel and are released upon Seller's confirmation of receipt of the payments under Section 2.6(b) and the Escrow Agent's written confirmation of receipt of the Escrow Amount." The 12:01 a.m. time can remain as the effective time for accounting and proration.

### Item 13. Title rep and "permitted liens" (Medium)
**Where:** APA §§1.1(m), 2.1, 4.5, 9.1; BoS §2.1.

**Issues.**
- "Permitted liens" is not defined in Article I. It appears only as "permitted liens listed in Section 2.1 of the Disclosure Schedule" (§2.1) and, lower-case and undefined, in §4.5.
- §4.5 is a Fundamental Representation. It survives to the statute of limitations plus 60 days and, per Item 1, sits outside the cap and basket.
- The BoS repeats "free and clear of all liens" (§2.1). Buyer could treat that as an independent title warranty outside the APA's survival, cap and §9.8 exclusive remedy.
- The APA contains no lien payoff or release deliverable, although §2.1 requires title free and clear. This is a Marrowind covenant with nothing yet in the Closing mechanics supporting it.

**Fix.**
- Define "Permitted Liens" in Article I to include liens listed in Schedule 2.1, statutory liens for taxes not yet due, mechanics' and similar liens arising in the ordinary course, and liens released at Closing.
- Use the defined term in §4.5 and the BoS.
- Add a payoff-letter mechanism: payoff amounts are paid from the closing payment and lien releases are delivered at Closing.
- Add to BoS §2.1: "Seller makes no representation or warranty in this Bill of Sale. Buyer's sole remedies in respect of title are those under the Purchase Agreement."

### Item 14. Survival and statute-of-limitations drafting (Medium)
**Where:** APA §9.1.

**Issue.**
- Fundamental Reps survive "until 60 days after the expiration of the applicable statute of limitations." That is open-ended and relies on a court to compute the limitation period.
- In New York a rep breach claim generally accrues when the rep is made, at Closing, regardless of discovery (*ACE Securities Corp. v. DB Structured Products, Inc.*, 25 N.Y.3d 581 (2015)), and the contract limitation period is six years (CPLR 213(2)). Please verify the cite.
- The 18-month survival for general reps works as a contractual limitation only if the clause says so clearly. A pre-accrual agreement to *extend* a limitation period is not enforceable under N.Y. Gen. Oblig. Law §17-103(3), so a "survival" longer than the statutory period may not do what Buyer wants. That is a point we can leave for later.

**Fix.** State the survival periods as fixed periods and add:
> "The Parties intend the survival periods in this Section 9.1 to replace any otherwise applicable statute of limitations, and no claim may be brought after the applicable period (other than a claim noticed within the period in accordance with this Section)."

### Item 15. Indemnity scope: Losses, Buyer indemnity, and mitigation (Medium)
**Where:** APA §§1.1(n), 9.3, 9.4(e), 9.5.

**Issues.**
- **Losses.** The definition includes "penalties, fines" and puts no limit on consequential damages, lost profits, diminution in value, or multiples-based damages. It contains no mitigation duty and no double-recovery language. §9.4(e) nets insurance only if "actually received."
- **Missing Buyer indemnity.** Buyer indemnifies only for its reps, covenants and Assumed Liabilities (§9.3). It does not indemnify for Buyer's post-Closing operation of the Business or ownership of the Purchased Assets (post-Closing product, environmental and employment liabilities). The Excluded Liabilities definition (§2.4) covers only "liabilities of Seller," so it is not obvious that post-Closing Buyer liabilities fall anywhere.
- **Direct claims.** Under §10.6, the indemnitees (Buyer's Affiliates, officers, managers) can enforce Article IX directly.

**Fix.**
- Add an exclusion of punitive, exemplary and consequential damages, diminution in value and multiple-based damages, except to the extent actually paid to a third party.
- Add duties to mitigate and no double recovery.
- Add §9.3(d) for "Buyer's ownership or operation of the Business or the Purchased Assets after the Closing."
- Require that indemnitee claims be brought only through Buyer.

### Item 16. Escrow Agent indemnity is joint and several (Medium)
**Where:** Escrow Agt §§5.4, 5.5; Schedule C; APA §10.1.

**Issue.**
- Seller and Buyer indemnify Corbel "jointly and severally" (§5.4). The 50/50 split is only "as between Seller and Buyer." If Buyer is unable or unwilling to pay, Corbel can collect 100% from Marrowind.
- Fees are split 50/50 (§5.5), including a $2,500 acceptance fee and $4,000 per year (Schedule C), while APA §10.1 is silent on who bears escrow costs.

**Fix.**
- Ask for several (not joint) liability, each for one-half.
- Fallback: keep joint and several to Corbel, but add "Buyer shall reimburse Seller on demand for any amount Seller pays in excess of its share."
- Settle the fee allocation (see Business Decisions).

### Item 17. Escrow tax treatment (Medium)
**Where:** Escrow Agt §2.4; APA §§2.8, 9.9; Escrow Agt §§4.1, 2.1.

**Issue.**
- §2.4 treats Buyer as owner of the Escrow Funds for tax purposes until distributed, citing Prop. Treas. Reg. §1.468B-8, and has earnings reported to Buyer on Form 1099. Yet the earnings are released to Marrowind under §4.1 ("Escrow Funds" includes earnings). Buyer will likely ask for a tax distribution or reimbursement, and the documents say nothing about it.
- The owner characterization also affects whether Marrowind can use installment-sale reporting (IRC §453) for escrowed proceeds. The APA does not address this either.

**Fix.** Refer to the client's tax adviser (see Business Decisions). If the Buyer-as-owner treatment stands, address Buyer's tax on earnings expressly, and add an installment-method covenant to APA §2.8.

### Item 18. Escrow Agreement, other mismatches and gaps (Medium-Low)
- **W-9 timing.** Escrow Agt §2.4 requires each of Seller and Buyer to deliver a W-9 to the Escrow Agent "before the Closing Date." APA §3.2(f) has Seller delivering its W-9 to Buyer "at the Closing." Align them.
- **Corbel's signature.** The APA requires only Seller and Buyer to deliver the executed Escrow Agreement (§§3.2(c), 3.3(b)). Corbel is not a party to the APA, and nothing conditions Closing on Corbel's signature, its KYC clearance (Escrow Agt §6.1), completed Schedule A (blank), or its confirmation of receipt (§2.1). Add Corbel's execution and written receipt confirmation as a condition in APA §7.2.
- **Duplicate definition.** "Escrow Amount" is defined both in APA §2.6(a) and Escrow Agt §2.1. Use the APA definition by reference.
- **"Escrow Amount" vs "Escrow Funds."** APA §9.7 releases "the remaining Escrow Amount" while Escrow Agt §4.1 releases "Escrow Funds" (principal plus earnings). Conform the APA to the Escrow Agreement.
- **Hard-wired dates.** Each ancillary is dated November 20, 2026, but APA §3.1 allows Closing on another date. Use "as of the Closing Date" or a bracket.

### Item 19. TSA commercial terms (Medium-Low)
**Where:** TSA §§2.2, 2.3, 5.1–5.5, 7.2, 7.3, 8.1.

- **No suspension right.** If Buyer stops paying, Marrowind must keep serving through a 15-day cure period (§2.3). Disputed invoices carry no interest (§5.5 covers undisputed amounts only) and no suspension right exists. Add the right to suspend Services on 10 days' notice for non-payment of undisputed fees, and interest on disputed amounts later found due.
- **Stranded costs.** Buyer can terminate any Service on 30 days' notice (§2.2). Fees are at fully loaded cost with no markup (§5.1). Dedicated staff and licenses then become stranded costs. Consider a minimum notice period or a wind-down cost reimbursement. This is also a pricing decision (see Business Decisions).
- **Buyer indemnity.** §7.3 covers only third-party claims caused by *gross negligence or willful misconduct*. There is no Buyer indemnity for third-party claims arising from Buyer's operation of the Business, Buyer's instructions or Buyer-provided data. Add one.
- **Section 6 carve-out.** §7.2 removes the consequential-damages waiver for breach of Section 6. Because Marrowind holds all the data, this exposure is mostly Marrowind's. Delete the Section 6 carve-out or limit it to willful breach.
- **Assignment mismatch.** TSA §9.6 and APA §10.4 differ on Buyer's assignment rights: TSA allows assignment only to an Affiliate that acquires substantially all the Purchased Assets, while APA also allows collateral assignment to lenders. The BoS has no assignment clause at all (§5.1). Conform them. For the TSA, Marrowind should require that any assignee be creditworthy.

### Item 20. TSA data and records vs. Marrowind's retention needs (Medium)
**Where:** TSA §§1.1(c), 2.4(b), 6.2; APA §§2.1(g), 2.4.

**Issues.**
- "Service Recipient Data" is "all data and records relating to the Business that Seller processes, stores or generates." TSA §6.2 says it is "owned by Buyer as part of the Purchased Assets," and Marrowind must return or destroy it "at Buyer's election" within 30 days after the Term (§6.2(c)).
- APA §2.1(g) conveys "all books, records…relating to the Business."
- Marrowind keeps pre-Closing tax liabilities and pre-Closing employment liabilities (APA §2.4), and it must defend claims and satisfy the escrow process. Nothing in the APA or TSA lets it keep copies.
- The ERP data set will also mix Business data with data about the Excluded Assets (Albany, HOLLIS) and Marrowind's own corporate and tax records. The TSA definition does not exclude them. Buyer personnel with systems access (§4.2) will see Marrowind's non-Business data.
- §2.4(b) (deliver data on termination of a Service) and §6.2(c) (return or destroy after the Term) use different mechanics.

**Fix.**
- Narrow the definition to data "solely relating to the Business, and excluding data relating to the Excluded Assets, Excluded Liabilities or Seller's corporate, tax and employee records."
- Add to APA §2.1(g) and TSA §6.2:
  > "Seller may retain copies of Service Recipient Data and Business books and records (i) as required by law, regulation or bona fide document-retention policy, and (ii) as reasonably necessary for tax matters, Excluded Liabilities, and the defense or prosecution of any claim, subject to Section 6.1. Buyer shall give Seller reasonable access to the records it has acquired for [seven] years."
- Add data segregation and access limits in TSA §4.2.

### Item 21. Employees, WARN and employee-related gaps (Medium)
**Where:** APA §§6.4, 2.4.

**Issues.**
- Buyer need only offer employment to Schedule 6.4 employees on "substantially comparable in the aggregate" terms. Unlisted employees, and listed employees who decline, stay with Marrowind.
- The APA does not allocate WARN Act exposure, accrued PTO, bonuses or severance. Employment liabilities arising "before the Closing" are Excluded Liabilities, but a plant-closing or mass layoff triggered by the sale could be argued to be Marrowind's problem.

**Fix.** Add a Buyer covenant to assume WARN responsibility for post-Closing employment losses of employees Buyer hires or declines to hire, and to honor accrued PTO for transferred employees (with a working-capital credit). Make this a conversation with the client first (see Business Decisions).

### Item 22. Allocation and tax mechanics (Medium-Low)
**Where:** APA §§2.8, 10.1.

**Issues.**
- Buyer prepares the §1060 allocation in 90 days, "reasonably acceptable to Seller," with no dispute mechanism, no consistent-reporting covenant, and no timing. Allocation drives Marrowind's ordinary income and capital gains mix.
- Transfer taxes are shared 50/50 (§10.1). Marrowind should confirm whether sales tax applies to the tangible assets and what the client expects to bear.
- New York bulk sale rules (N.Y. Tax Law §1141(c)) require a purchaser to notify the Department of Taxation at least 10 days before taking possession or paying. With a November 20 Closing, that is about November 10. If Buyer is late, Marrowind faces delay or a holdback. The APA has no bulk-sale covenant. Please verify the current requirements.

**Fix.**
- Add an objection/dispute mechanism to §2.8 using the accounting firm, plus a consistent-filing covenant (Form 8594).
- Add a mutual bulk-sale cooperation covenant and a timetable.

### Item 23. Smaller drafting points (Low)
- **BoS missing boilerplate.** The BoS has no jury waiver (compare APA §10.10, TSA §9.4, Escrow Agt §7.3), no venue-waiver language (APA §10.9), and no assignment clause (see Item 19).
- **BoS one-sided covenants (§§4.1, 4.2).** Further assurances run only from Seller, "without further consideration," at Buyer's request, with no expense reimbursement. The APA version (§6.7) is mutual and "reasonably required." Payment turnover is one-way: Seller holds payments in trust for Buyer and remits within 10 Business Days, with no reciprocal duty for Buyer to remit payments on Excluded Assets and no set-off right. Make §§4.1 and 4.2 mutual, with out-of-pocket expense reimbursement.
- **MAE (APA §1.1(o), §7.1(c)).** Add exclusions for the announcement of the deal, loss of customers or employees because of it, actions Buyer requests, and failure to meet projections.
- **Financial statements rep (APA §4.7).** The unaudited 9/30/2026 balance sheet should be "subject to normal year-end adjustments and the absence of footnotes."
- **Disclosure Schedule.** There is no right to update the Disclosure Schedule between signing and Closing, while §7.1(a) brings reps down to Closing. Add one.
- **Corporate approval.** APA §3.2(d) contemplates shareholder resolutions. N.Y. Bus. Corp. Law §909 requires shareholder approval for a sale of substantially all assets outside the ordinary course, with dissenters' rights under §910. Confirm the vote required and obtain approval at or before signing, not at Closing.

---

## 3. Facts and Issues to Confirm with the Client

These affect the analysis above and are not answered by the documents:
1. **Where is the equipment?** APA §2.1(b) sells the corrugators and converting equipment, while §2.2 keeps the Albany facility. If the equipment sits in Albany, nothing in the APA, BoS (§2.2 delivers possession "at the locations where those assets are located") or TSA gives Buyer access or a removal period, and nothing compensates Marrowind for hosting it. Unless Albany is empty, Marrowind may be an unpaid warehouse and landlord. A lease, access agreement or removal covenant is probably needed.
2. **Which systems, contracts and people are included?** Schedules 2.1, 2.1(c) and 6.4 control Items 3 and 5.
3. **Broker or banker.** §4.12 (Brokers) is a Fundamental Representation. Confirm no engagement exists, or schedule it.

---

## 4. Items Requiring Business Decisions (separate from drafting)

1. **Indemnity economics (Item 1).** Is the 10% / $1,840,000 cap the deal? Is escrow to be the sole recourse for general reps? What is the cap for Fundamental Representations (Purchase Price is typical)? Should Excluded Liabilities (§9.2(c)) stay capped (current text) or be conceded as uncapped? Is the 18-month survival firm?
2. **Retained assets and name (Items 2, 10).** What does Marrowind intend to do at Albany and under HOLLIS (this defines the non-compete carve-out in Schedule 6.5)? Will Marrowind keep using its corporate name or give a transitional license?
3. **Consent risk (Item 3).** Which consents (if any) will Marrowind accept as closing conditions? For how long, and at whose cost, will Marrowind hold contracts for Buyer?
4. **Governing law (Item 4).** Is New York for the TSA a hold point, or tradeable?
5. **TSA scope and pricing (Items 5, 19).** Can Marrowind staff the Services after employees transfer? Is cost-only, no-markup pricing acceptable, with Marrowind carrying credit risk, stranded costs and 60+ days' float? Should Buyer prefund payroll and pass-through costs?
6. **Fraud and sandbagging (Item 8).** How hard to push the definition of Fraud, non-reliance and an anti-sandbagging clause (the last is typically resisted).
7. **Working capital (Item 9).** Does the client want a collar or cap on the post-Closing adjustment? Confirm the $2,150,000 target against historical working capital.
8. **Escrow fees and tax (Items 16, 17).** Who bears escrow fees, and who is the tax owner of the escrow (tax adviser input; installment method)?
9. **Employees (Item 21).** Severance, WARN and PTO positions for employees who do not transfer.
10. **Post-Closing structure.** Marrowind is the only obligor for up to six years on Fundamental Representations (§9.1). Will it distribute the proceeds or dissolve? Buyer may ask for a guaranty, a holdback, or a covenant to maintain existence.
11. **Shareholder approval (Item 23).** Confirm the vote, timing, and dissenters' rights.

---

## 5. Suggested Next Steps

1. Obtain the Disclosure Schedule and exhibits, and the client's answers to Sections 3 and 4.
2. Prepare a mark-up of the APA first (Items 1, 3, 6, 8, 9, 10, 12–15, 21, 22), then conform the three ancillaries to it (Items 2, 4, 5, 7, 11, 16–20, 23).
3. Cite-check the New York authorities flagged above before anything goes to the other side.