# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Marrowind Packaging Corp. / Tessaly Holdings LLC – Seller-Side Review of Ancillary Documents

---

## Summary

I have reviewed the Asset Purchase Agreement (the "APA"), the Bill of Sale and Assignment and Assumption Agreement (the "Bill of Sale"), the Transition Services Agreement (the "TSA"), and the Indemnity Escrow Agreement (the "Escrow Agreement"). The documents are largely consistent, but I have identified one critical drafting error, two significant cross-document inconsistencies, and several lesser issues. The most urgent item is a likely drafting error in the APA's indemnification limitations that, as written, leaves Marrowind's indemnification exposure for representation and warranty breaches **uncapped and without a basket**.

---

## Issue 1 – CRITICAL: Indemnification Cap and Basket Inapplicable to All Rep & Warranty Claims

**Where:** APA § 9.4(c); APA § 1.1(m)

**Problem.** Section 9.4(c) provides:

> "The limitations set forth in Section 9.4(a) and Section 9.4(b) shall not apply to any claim under Section 9.2(a), or to any claim arising from fraud."

Section 9.2(a) covers *all* breaches of Seller's representations and warranties. Read as written, the 10%-of-Purchase-Price cap (§ 9.4(a)) and the $184,000 basket (§ 9.4(b)) apply only to covenant breaches (§ 9.2(b)) and Excluded Asset/Liability claims (§ 9.2(c)). Every rep-and-warranty claim—whether fundamental or ordinary—is uncapped and has no deductible.

The defined term "Fundamental Representations" (APA § 1.1(m)) is defined but **never used anywhere in the Agreement**. This is a strong indicator that the drafter intended § 9.4(c) to carve out only Fundamental Representations (and fraud) from the cap and basket, consistent with market practice.

**Why it matters for Marrowind.** As drafted, a single inaccuracy in any of Seller's 12 representations (e.g., a minor overstatement in the financial statements rep in § 4.7, or a single undisclosed permit in § 4.10) exposes Marrowind to unlimited indemnification with no threshold. The escrow is only $1,840,000, but under § 9.6 Buyer can recover directly from Seller above the escrow. Marrowind's total indemnification exposure is theoretically unlimited.

**Recommended fix.** Amend § 9.4(c) to:

> "(c) *Exceptions.* The limitations set forth in Section 9.4(a) and Section 9.4(b) shall not apply to any claim under Section 9.2(a) arising from a breach of a Fundamental Representation, or to any claim arising from fraud."

This preserves the cap and basket for ordinary rep/warranty claims while leaving Fundamental Representations and fraud uncapped, which is the standard market structure and almost certainly the parties' intent.

---

## Issue 2 – HIGH: Bill of Sale Definition of "Purchased Assets" Broader Than APA and Omits Excluded Assets Carve-Out

**Where:** Bill of Sale § 1.1(b); APA §§ 2.1, 2.2

**Problem.** The APA defines Purchased Assets as "all of Seller's right, title and interest in all assets used or held for use in the Business, **other than the Excluded Assets**" (APA § 2.1). The Excluded Assets are: Seller's cash, the Albany manufacturing facility, and the HOLLIS trademark (APA § 2.2).

The Bill of Sale, however, provides its own definition of "Purchased Assets" in § 1.1(b):

> "all of Seller's right, title and interest in, to and under all assets, properties and rights of every kind and nature, **whether real, personal or mixed, tangible or intangible, wherever located**, used or held for use in the Business."

Two problems:

1. **No Excluded Assets carve-out.** The Bill of Sale's definition does not exclude the Excluded Assets. Because § 1.1 provides that the Bill of Sale's definitions control ("In addition, the following terms have the meanings set forth below"), the Bill of Sale's broader definition overrides the APA's for purposes of the Bill of Sale.

2. **Expressly includes real property and trademarks.** The Bill of Sale's chapeau adds "whether real, personal or mixed" (the APA is silent on real property) and the IP sub-clause (§ 1.1(b)(iv)) adds "trademarks, trade names" (the APA § 2.1(d) says only "intellectual property used or held for use in the Business, including customer dies and print plates"). The Albany manufacturing facility is real property used in the Business; the HOLLIS trademark is a trademark used in the Business. Both are Excluded Assets, but both fall squarely within the Bill of Sale's definition.

**Why it matters for Marrowind.** The Bill of Sale is the operative conveyance instrument. If a dispute arises over whether the Albany facility or the HOLLIS trademark was conveyed, Buyer could point to the Bill of Sale's unambiguous (if overbroad) definition and the absence of any Excluded Assets reference in the conveyance clause (§ 2.1). While APA § 10.12 (Order of Precedence) provides that the APA controls in case of conflict, relying on a precedence clause to undo an operative conveyance is litigation risk, not a substitute for clear drafting.

**Recommended fix.** Amend Bill of Sale § 1.1(b) to track the APA:

> "(b) 'Purchased Assets' means all of Seller's right, title and interest in all assets used or held for use in the Business, other than the Excluded Assets. This includes: [existing sub-clauses (i) through (vii), with sub-clause (iv) revised to read: 'all intellectual property used or held for use in the Business, including customer dies and print plates, other than the HOLLIS trademark.']"

Alternatively, if the parties prefer to keep the broader chapeau, add at the end of § 1.1(b): "The Purchased Assets do not include the Excluded Assets."

---

## Issue 3 – HIGH: TSA Governed by Delaware Law; All Other Documents Governed by New York Law

**Where:** TSA § 9.3; APA § 10.8; Bill of Sale § 5.5; Escrow Agreement § 7.1

**Problem.** The TSA selects Delaware law and exclusive Delaware jurisdiction (§ 9.3). The APA, Bill of Sale, and Escrow Agreement all select New York law and New York County jurisdiction. The partner's instructions confirm the deal is governed by New York law.

**Why it matters for Marrowind.**

- **Interpretive risk.** The TSA is an Ancillary Agreement under APA § 1.1(b), and APA § 10.12 provides that the APA controls in case of conflict. But if a dispute arises under the TSA (e.g., over the standard of performance in § 3.2, the liability cap in § 7.2, or the data ownership provision in § 6.2), a Delaware court applying Delaware law might interpret key terms differently than a New York court would. For example, Delaware and New York differ on the enforceability of certain liability limitations and on the scope of "substantial compliance."
- **Forum fragmentation.** Marrowind could face simultaneous proceedings in New York (under the APA or Escrow Agreement) and Delaware (under the TSA) arising from the same factual circumstances, increasing cost and creating the risk of inconsistent outcomes.
- **Cross-reference problem.** TSA § 7.3 incorporates the APA's claims procedure (§ 9.5) "with necessary changes." If a Delaware court is applying the TSA, it must interpret a New York-law procedure provision, adding complexity.

**Recommended fix.** Amend TSA § 9.3 to:

> "9.3 Governing Law; Jurisdiction. This Agreement, and all claims or causes of action arising out of or relating to this Agreement or the Services, shall be governed by and construed in accordance with the Laws of the State of New York, without giving effect to any choice or conflict of law provision or rule that would cause the application of the laws of any other jurisdiction. Each Party irrevocably submits to the exclusive jurisdiction of the State and federal courts located in New York County, New York for any action arising out of or relating to this Agreement or the Services. Each Party waives any objection to venue in those courts, including any objection based on inconvenient forum."

---

## Issue 4 – MEDIUM: Bill of Sale Conveyance Clause Does Not Reference Excluded Assets

**Where:** Bill of Sale § 2.1

**Problem.** Section 2.1 states: "Seller hereby irrevocably sells, assigns, transfers, conveys and delivers to Buyer, and Buyer hereby accepts, all of the Purchased Assets." It does not state that the Excluded Assets are not conveyed. Combined with Issue 2 (the overbroad definition), this creates ambiguity at the operative moment of transfer.

**Why it matters for Marrowind.** Even if the definition issue (Issue 2) is fixed, best practice is to state the exclusion in the conveyance clause itself so that the four corners of the Bill of Sale are unambiguous.

**Recommended fix.** Add to Bill of Sale § 2.1:

> "The Excluded Assets are not conveyed by this Bill of Sale and remain the property of Seller."

---

## Issue 5 – MEDIUM: TSA Liability Cap Is One-Way

**Where:** TSA § 7.2

**Problem.** Section 7.2 caps *Seller's* aggregate liability at total Service Fees (approximately $285,000 over the Term, excluding pass-throughs). It does not impose a corresponding cap on *Buyer's* liability. If Buyer's personnel cause damage to Seller's ERP systems (a realistic risk given § 4.2 grants Buyer access to Seller's IT systems), or if Buyer wrongfully terminates and refuses to pay accrued fees, Seller's recovery is uncapped (subject only to the consequential-damages waiver).

**Why it matters for Marrowind.** The services involve Buyer personnel accessing Seller's live production systems (ERP, email, order management). A security breach or data corruption caused by Buyer's personnel could result in significant losses to Seller that exceed the Service Fees.

**Recommended fix.** Add to TSA § 7.2:

> "Buyer's aggregate liability under this Agreement shall not exceed the total Service Fees paid and payable under this Agreement, except in the case of gross negligence, willful misconduct, or breach of Section 6."

---

## Issue 6 – MEDIUM: Escrow Agent Indemnification Imposes Joint and Several Liability on Seller

**Where:** Escrow Agreement § 5.4

**Problem.** "Seller and Buyer, jointly and severally, shall indemnify the Escrow Agent against any loss, liability, claim or expense, including reasonable attorneys' fees, arising out of its performance under this Escrow Agreement, except to the extent caused by its gross negligence or willful misconduct."

While the next sentence allocates the indemnification 50/50 "as between" the parties, the joint and several obligation means the Escrow Agent can collect the full amount from Marrowind alone if Buyer is insolvent or uncooperative.

**Why it matters for Marrowind.** The practical exposure is limited (the Escrow Agent's duties are ministerial, and its own liability is capped at gross negligence/willful misconduct under § 5.3), but the joint and several structure is unnecessary given that the fees are already split 50/50 under § 5.5.

**Recommended fix.** Amend the first sentence of § 5.4 to:

> "Seller and Buyer, severally and not jointly, shall indemnify the Escrow Agent…"

The existing 50/50 allocation sentence can remain to confirm the split.

---

## Issue 7 – LOWER: TSA Permits Only Buyer to Terminate Individual Services for Convenience

**Where:** TSA § 2.2

**Problem.** Buyer may terminate any Service on 30 days' notice. Seller has no corresponding right. If Buyer's integration proceeds faster than expected and it no longer needs, say, the IT hosting service (Service 3, $14,000/month), it can terminate. But if Seller's own operations change (e.g., the Albany facility is repurposed and the ERP system is migrated), Seller cannot unilaterally end a service it can no longer provide at the agreed standard.

**Why it matters for Marrowind.** Seller is contractually committed to providing services "substantially" at the same quality and scope as the prior 12 months (§ 3.2). If Seller's own business changes during the 6-month Term, it may be unable to meet the standard without incurring breach.

**Recommended fix.** Add to TSA § 2.2:

> "Seller may terminate any Service, in whole or in part, by giving Buyer at least 30 days' written notice if Seller determines in good faith that it can no longer provide the Service at the standard required by Section 3.2 without material disruption to Seller's remaining operations. The Service Fees for a terminated Service end on the effective date of termination."

*Flag for business decision:* The client should confirm whether it is comfortable with the current one-sided termination right or whether it wants to negotiate this point.

---

## Issue 8 – LOWER: Non-Compete Exception for Excluded Assets Is Vague

**Where:** APA § 6.5

**Problem.** The non-compete carves out use of the Excluded Assets "in a manner that does not compete with the Business." The Business is defined broadly (APA Recital A: "designs, manufactures, converts and sells corrugated packaging products, including corrugated sheets, boxes, displays and protective inserts"). If Marrowind uses the Albany facility to manufacture corrugated packaging for a different customer segment, or uses the HOLLIS trademark on a product line that overlaps with the sold Business, Buyer could argue this "competes."

**Why it matters for Marrowind.** The Excluded Assets are Marrowind's principal remaining operating assets post-closing. A vague carve-out creates ongoing uncertainty about what Marrowind can and cannot do with its own retained assets for three years.

**Recommended fix.** Amend the exception in § 6.5 to:

> "…except through the ownership and operation of the Excluded Assets, including the manufacture and sale of corrugated packaging products at the Albany manufacturing facility under the HOLLIS trademark, so long as such activities do not target customers that were customers of the Business as of the Closing Date."

*Flag for business decision:* The client should define the scope of post-closing operations it intends to conduct at the Albany facility so we can calibrate the carve-out appropriately.

---

## Issue 9 – LOWER: Escrow Agreement Schedule A Incomplete

**Where:** Escrow Agreement, Schedule A

**Problem.** Schedule A (Authorized Representatives and Wire Instructions) is a placeholder: "[To be completed by Seller and Buyer before the Closing…]." Without completed wire instructions and authorized signatories, the Escrow Agent cannot process the deposit at Closing or make any disbursement.

**Why it matters for Marrowind.** This is a closing checklist item, not a drafting issue, but it must be completed before November 20, 2026.

**Recommended action.** Prepare and circulate Schedule A for Marrowind's signature well in advance of the Closing Date.

---

## Issue 10 – LOWER: TSA Service Fees at Cost Without Markup

**Where:** TSA § 5.1; Schedule A

**Problem.** The Service Fees are expressly "intended to reflect Seller's fully loaded cost of providing the Services, without markup." Total fees over the Term are approximately $285,000. Marrowind is providing six months of financial, payroll, IT, procurement, and customer-service support to Buyer at no profit.

**Why it matters for Marrowind.** This is a real economic cost to Marrowind. If the client's business plan assumed a revenue contribution from transition services, this is a missed opportunity.

*Flag for business decision:* If the client wants to negotiate a markup (e.g., 10–15%), this should be raised before the next round of drafts. However, given that the documents appear to be in near-final form, this may be a point that has already been traded for other terms.

---

## Issue 11 – LOWER: APA § 9.4(d) Buyer Cap Applies Only to Rep & Warranty Breaches

**Where:** APA § 9.4(d)

**Problem.** "The aggregate liability of Buyer under Section 9.3(a) shall not exceed 10% of the Purchase Price." This caps only Buyer's liability for breaches of its representations and warranties. It does not cap Buyer's liability for covenant breaches (§ 9.3(b)) or Assumed Liabilities (§ 9.3(c)). This is the mirror image of the (erroneous) structure in § 9.4(c) for Seller, but in Buyer's favor: Buyer's rep/warranty exposure is capped, while its covenant and Assumed Liability exposure is not.

**Why it matters for Marrowind.** If Buyer breaches a covenant (e.g., fails to offer employment to the listed employees under § 6.4) or an Assumed Liability claim arises, Marrowind's indemnification claim against Buyer is uncapped. This is actually favorable to Marrowind, so no fix is recommended. I flag it only for completeness and to confirm the asymmetry is intentional.

---

## Issue 12 – LOWER: Transfer Taxes Split Equally

**Where:** APA § 10.1

**Problem.** "Transfer taxes arising from the transfer of the Purchased Assets shall be borne equally by Seller and Buyer." In many New York asset deals, the buyer bears transfer taxes as part of the assumption of the asset. Splitting 50/50 is a compromise.

*Flag for business decision:* The client should confirm whether this allocation was a negotiated trade-off or whether it is open for discussion. If the Purchased Assets include significant tangible personal property subject to New York's MTA (Mortgage Recording Tax does not apply, but the New York City and State transfer taxes on certain assets may), the dollar amount could be material.

---

## Items Requiring Business Decisions from the Client

| # | Item | Document / Section | Question for Client |
|---|------|--------------------|--------------------|
| A | Non-compete carve-out scope | APA § 6.5 | What post-closing operations does Marrowind intend to conduct at the Albany facility? What products under the HOLLIS trademark? |
| B | TSA termination right | TSA § 2.2 | Does the client want a mutual convenience-termination right, or is the current one-sided structure acceptable? |
| C | TSA fee markup | TSA § 5.1 / Schedule A | Does the client want to negotiate a markup on transition services, or is at-cost acceptable? |
| D | Transfer tax allocation | APA § 10.1 | Was the 50/50 split a deliberate trade, or is it open? |
| E | Escrow Agent fees | Escrow Agreement § 5.5 / Schedule C | Confirm the client is comfortable with ~$7,250 in escrow agent fees (Seller's share) over the 18-month term. |

---

## Closing Checklist Items (Non-Drafting)

1. Complete Escrow Agreement Schedule A (authorized reps, specimen signatures, wire instructions) before Closing.
2. Confirm Disclosure Schedule Sections 2.1(c), 2.1, 4.4, 4.8, and 6.4 are finalized and attached.
3. Confirm Board and shareholder resolutions are prepared for the APA § 3.2(d) certificate.
4. Confirm third-party consents listed in Disclosure Schedule § 4.4 have been obtained or are on track for the Closing Date.
5. Confirm Marrowind's wire instructions for the APA § 2.6(b) balance payment are delivered at least two Business Days before Closing.