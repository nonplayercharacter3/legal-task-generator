# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Date]
**Re:** Marrowind Packaging Corp. / Tessaly Holdings LLC – Seller-Side Review of Ancillary Documents

---

## Summary

I reviewed the Asset Purchase Agreement (the "APA"), the Bill of Sale and Assignment and Assumption Agreement (the "Bill of Sale"), the Transition Services Agreement (the "TSA"), and the Indemnity Escrow Agreement (the "Escrow Agreement"). I identified three significant cross-document inconsistencies, two moderate issues, and several minor items. The most urgent problem is that the Bill of Sale's definition of "Purchased Assets" omits the Excluded Assets carve-out, meaning the conveyance document could be read to transfer the HOLLIS trademark, the Albany manufacturing facility, and Seller's cash to Buyer.

---

## Issue 1 – Bill of Sale Conveys Excluded Assets (Critical)

**Documents and Sections:**
- APA § 2.1 (defines "Purchased Assets" as assets "other than the Excluded Assets")
- APA § 2.2 (Excluded Assets: Seller's cash, the Albany manufacturing facility, and the HOLLIS trademark)
- Bill of Sale § 1.1(b) (independently defines "Purchased Assets")
- Bill of Sale § 2.1 (conveyance of "all of the Purchased Assets")

**Explanation:**
The Bill of Sale provides its own definition of "Purchased Assets" in § 1.1(b): "all of Seller's right, title and interest in, to and under all assets, properties and rights of every kind and nature, whether real, personal or mixed, tangible or intangible, wherever located, used or held for use in the Business." This definition does not incorporate the "other than the Excluded Assets" limitation found in APA § 2.1. Because the Bill of Sale defines the term, the fallback rule in Bill of Sale § 1.1 ("Capitalized terms used but not defined in this Bill of Sale have the meanings given to them in the Purchase Agreement") does not apply—the Bill of Sale's own definition controls.

The practical effect is that Bill of Sale § 2.1, which conveys "all of the Purchased Assets," would transfer to Buyer:
- The HOLLIS trademark (excluded by APA § 2.2);
- The Albany manufacturing facility (excluded by APA § 2.2); and
- Seller's cash (excluded by APA § 2.2).

The broadening language "whether real, personal or mixed, tangible or intangible, wherever located" makes the over-conveyance even more explicit, as it sweeps in real property (the Albany facility) that the APA's definition would not naturally capture.

**Why it matters for Marrowind:** The Bill of Sale is the operative conveyance instrument. If a dispute arises over whether the HOLLIS trademark or the Albany facility was transferred, Buyer will point to the Bill of Sale's unambiguous (if erroneous) language. Marrowind would bear the burden of proving the parties intended the APA's carve-out to apply, which is an uphill fight against the four corners of the deed.

**Recommended Fix:**
Conform the Bill of Sale definition to the APA. Replace Bill of Sale § 1.1(b) with:

> (b) "**Purchased Assets**" has the meaning set forth in Section 2.1 of the Purchase Agreement, and includes:
>
> (i) all inventory, raw materials (including linerboard and medium), work in process, finished goods and supplies;
>
> (ii) all machinery, corrugators, converting equipment, die cutters, printers, tooling, vehicles, furniture and other tangible personal property;
>
> (iii) the Assigned Contracts;
>
> (iv) all intellectual property used or held for use in the Business (other than the HOLLIS trademark), including customer dies and print plates;
>
> (v) all accounts receivable arising from the Business;
>
> (vi) all permits, to the extent transferable; and
>
> (vii) all books, records, customer lists and supplier lists relating to the Business.

Alternatively, if the client prefers to retain the enumerated list for clarity, add the following sentence immediately after the introductory clause of § 1.1(b): "The Purchased Assets do not include the Excluded Assets."

---

## Issue 2 – Transition Services Agreement Governed by Delaware Law (Significant)

**Documents and Sections:**
- APA § 10.8 (New York governing law)
- APA § 10.9 (New York County jurisdiction)
- Bill of Sale § 5.5 (New York governing law)
- Bill of Sale § 5.6 (New York County jurisdiction)
- Escrow Agreement § 7.1 (New York governing law)
- Escrow Agreement § 7.2 (New York County jurisdiction)
- TSA § 9.3 (Delaware governing law; Delaware courts jurisdiction)

**Explanation:**
Every document in the package is governed by New York law and subject to New York County jurisdiction except the TSA, which selects Delaware law and Delaware courts. This is almost certainly a drafting error—likely a carryover from a template. There is no apparent business reason to subject the TSA to a different governing law: the services are performed in New York, the Business is a New York business, and Marrowind is a New York corporation.

The problem is compounded by APA § 10.12 (Order of Precedence), which provides that the APA controls over the Ancillary Agreements "except that each Ancillary Agreement controls as to its specific subject matter." One could argue that a document's own governing-law clause is part of its "specific subject matter," meaning the TSA's Delaware choice might survive. This creates unnecessary litigation risk over which law applies to a TSA dispute.

**Why it matters for Marrowind:** As a New York corporation, Marrowind would be litigating in Delaware under Delaware law for any TSA dispute (e.g., a dispute over service quality, fee payment, or data return). This increases cost, reduces home-field advantage, and creates the possibility of inconsistent interpretations across the deal documents.

**Recommended Fix:**
Replace TSA § 9.3 with:

> **9.3 Governing Law; Jurisdiction.** This Agreement, and all claims or causes of action arising out of or relating to this Agreement or the Services, shall be governed by and construed in accordance with the Laws of the State of New York, without giving effect to any choice or conflict of law provision or rule that would cause the application of the laws of any other jurisdiction. Each Party irrevocably submits to the exclusive jurisdiction of the State and federal courts located in New York County, New York for any action arising out of or relating to this Agreement or the Services. Each Party waives any objection to venue in those courts, including any objection based on inconvenient forum.

---

## Issue 3 – Indemnification Cap Exception Renders Escrow Inadequate as Security (Significant)

**Documents and Sections:**
- APA § 9.2(a) (Seller indemnifies for breach of representations and warranties)
- APA § 9.4(a) (cap: 10% of Purchase Price = $1,840,000)
- APA § 9.4(c) (exceptions: cap and basket do not apply to "any claim under Section 9.2(a), or to any claim arising from fraud")
- APA § 2.6(a) (Escrow Amount described as "security for Seller's indemnification obligations under Article IX")
- Escrow Agreement Recital B (escrow "serves as security for Seller's indemnification obligations under Article IX")
- Escrow Agreement § 2.1 (Escrow Amount: $1,840,000)

**Explanation:**
APA § 9.4(c) provides that the cap in § 9.4(a) and the basket in § 9.4(b) "shall not apply to any claim under Section 9.2(a)." Section 9.2(a) is the representation-and-warranty indemnity—the single most common source of post-closing claims. As drafted, Seller's exposure for a rep/warranty breach is uncapped. The Escrow Amount is set at exactly the cap amount ($1,840,000 = 10% × $18,400,000), which is internally consistent only if the cap applies to all claims. Because the cap does not apply to the most frequent category of claims, the escrow is not adequate security for Seller's actual Article IX obligations.

This appears to be a drafting error. The standard market structure is: the cap applies to all indemnification claims, with exceptions only for fraud and (sometimes) Fundamental Representations. Here, the drafter may have intended to carve out only Fundamental Representations (defined in APA § 1.1(m) as §§ 4.1, 4.2, 4.5, and 4.12) rather than all of § 9.2(a).

**Why it matters for Marrowind:** If a Buyer claim for a non-fundamental rep breach (e.g., a challenge to the condition of assets under § 4.6 or the financial statements under § 4.7) exceeds $1,840,000, Marrowind is personally liable for the excess with no cap. The escrow, which was negotiated as the exclusive first source of recovery (APA § 9.6), provides no protection above $1,840,000 for the most likely type of claim.

**Recommended Fix (APA § 9.4(c)):**
> (c) *Exceptions.* The limitations set forth in Section 9.4(a) and Section 9.4(b) shall not apply to (i) any claim arising from fraud or (ii) any claim based on a breach of a Fundamental Representation.

This preserves the uncapped treatment for the two categories that typically warrant it (fraud and fundamental reps—organization, authority, title, brokers) while restoring the cap for ordinary rep/warranty claims.

**Note:** This is a change to the APA itself, not an ancillary document. However, it is flagged here because it directly affects the adequacy of the Escrow Agreement and should be raised in the same negotiation round.

---

## Issue 4 – Bill of Sale IP Definition Broader Than APA (Moderate)

**Documents and Sections:**
- APA § 2.1(d) ("all intellectual property used or held for use in the Business, including customer dies and print plates")
- Bill of Sale § 1.1(b)(iv) ("all intellectual property, including trademarks, trade names, customer dies and print plates")

**Explanation:**
The Bill of Sale adds "trademarks, trade names" to the illustrative list of intellectual property. While the APA's "all intellectual property used or held for use in the Business" could arguably encompass trademarks, the express addition in the Bill of Sale—combined with the missing Excluded Assets carve-out (Issue 1)—creates a specific argument that the HOLLIS trademark was intended to be conveyed. Even after fixing Issue 1, the express reference to "trademarks" in the Bill of Sale is unnecessary and invites dispute.

**Recommended Fix:**
Conform Bill of Sale § 1.1(b)(iv) to the APA:

> (iv) all intellectual property used or held for use in the Business (other than the HOLLIS trademark), including customer dies and print plates;

---

## Issue 5 – Bill of Sale Lacks Jury Trial Waiver (Moderate)

**Documents and Sections:**
- APA § 10.10 (jury waiver)
- TSA § 9.4 (jury waiver)
- Escrow Agreement § 7.3 (jury waiver)
- Bill of Sale § 5 (no jury waiver)

**Explanation:**
The Bill of Sale is the only document in the package without a jury trial waiver. In a dispute over the scope of the conveyance (e.g., whether the HOLLIS trademark was transferred), Marrowind could face a jury trial in New York County while all related disputes under the other documents are bench trials.

**Recommended Fix:**
Add to Bill of Sale § 5:

> **5.X Waiver of Jury Trial.** EACH PARTY IRREVOCABLY WAIVES ANY RIGHT TO TRIAL BY JURY IN ANY ACTION ARISING OUT OF OR RELATING TO THIS BILL OF SALE.

---

## Issue 6 – APA Order of Precedence Clause Is Inadequate to Resolve the Above Conflicts (Moderate)

**Documents and Sections:**
- APA § 10.12

**Explanation:**
APA § 10.12 states: "In the event of any conflict between this Agreement and any Ancillary Agreement, this Agreement controls over the Ancillary Agreements, except that each Ancillary Agreement controls as to its specific subject matter." This is circular: it says the APA controls, except where the ancillary document controls, without providing a test for when an ancillary document is addressing its "specific subject matter." The conflicts identified in Issues 1 and 2 are precisely the kind this clause was meant to resolve, and it fails to do so.

**Recommended Fix:**
> **10.12 Order of Precedence.** In the event of any conflict between this Agreement and any Ancillary Agreement as to the scope of the Purchased Assets, the Excluded Assets, the Assumed Liabilities, the Excluded Liabilities, the Purchase Price, or the indemnification obligations of the Parties, this Agreement controls. In all other respects, each Ancillary Agreement controls as to its specific subject matter.

This makes explicit that the APA governs the core economic and risk-allocation terms, while leaving operational details (service standards, escrow mechanics, etc.) to the ancillary documents.

---

## Issue 7 – Escrow Agreement Schedule A Not Completed (Minor / Practical)

**Document and Section:** Escrow Agreement, Schedule A

**Explanation:** Schedule A is bracketed: "[To be completed by Seller and Buyer before the Closing: names, titles, specimen signatures and call-back telephone numbers of authorized representatives; wire instructions for each of Seller and Buyer.]" This must be completed before the Closing or the Escrow Agent will not have the information needed to confirm wire instructions or verify authorized signatories.

**Recommended Action:** Confirm with the client who the authorized representatives will be and obtain wire instructions well in advance of the November 20 Closing.

---

## Items Requiring a Business Decision from the Client

The following are not purely drafting issues and require Marrowind's input:

1. **APA § 9.4(c) – Cap Exception (Issue 3).** The fix proposed above (limiting the exception to fraud and Fundamental Representations) is the market-standard approach, but it changes the risk allocation the other side may have negotiated. Confirm with the client that this is a drafting error and not a deliberate business decision to accept uncapped rep/warranty exposure. If the client believes the current language was intentional, the Escrow Amount should be increased or a separate cap for non-fundamental rep claims should be negotiated.

2. **TSA Governing Law (Issue 2).** While I am confident this is a drafting error, confirm with the client that there is no strategic reason (e.g., a Delaware-based parent of Buyer insisting on Delaware law for its own internal governance) to keep Delaware. If the answer is no, propose the fix.

3. **Escrow Agent Fees (Escrow Agreement § 5.5, Schedule C).** The fees (approximately $8,500–$9,000 over the 18-month term, split 50/50) are modest but confirm the client is comfortable bearing ~$4,500 of escrow agent costs.

---

## Items Reviewed and Found Consistent

For completeness, the following cross-document references check out:

| Topic | APA | Ancillary Document | Status |
|---|---|---|---|
| Escrow Amount ($1,840,000) | § 2.6(a) | Escrow Agmt § 2.1, Recital B | Consistent |
| Escrow release at 18 months | § 9.7 | Escrow Agmt § 4.1 | Consistent |
| TSA term (6 months) | § 6.6 | TSA § 2.1 | Consistent |
| First source of recovery = escrow | § 9.6 | Escrow Agmt § 3.6 | Consistent |
| Closing Date (Nov 20, 2026) | § 3.1 | Bill of Sale (date), TSA (date), Escrow Agmt (date) | Consistent |
| Notice addresses | § 10.2 | Bill of Sale § 5.3, TSA § 9.1, Escrow Agmt § 7.4 | Consistent |
| Service Recipient Data owned by Buyer | § 2.1(g) (books, records, customer lists) | TSA § 6.2 | Consistent |
| Non-assignable contracts / consents | § 6.3, § 4.4 | Bill of Sale § 3.4 | Consistent |