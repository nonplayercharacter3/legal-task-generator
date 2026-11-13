# MEMORANDUM

**To:** Partner of Record
**From:** Associate
**Re:** Dilur Interactive / Glesar Studios – Asset Purchase: Document Review Issues
**Date:** [Current]

---

## Summary

I have reviewed the five documents in the matter folder. The transaction is an asset purchase by Dilur Interactive, Inc. ("Dilur" or "Buyer") of the Emberfall game franchise from Glesar Studios LLC ("Glesar" or "Seller") for $48,500,000. I identify **ten issues** requiring attention before closing, ordered by severity. The two most urgent are (1) the Composer Claim and the likely expiration of Dilur's termination right under the Schedule Update mechanism, and (2) the Wickline Toolkit license, which cannot be assigned without Okoro's consent and which the IP Assignment Agreement does not address. I also flag a direct conflict between the IP Assignment Agreement and the APA on the cap for IP representations, and an uncapped buyer indemnity in the IP Assignment Agreement that exposes Dilur to unlimited pre-closing IP liability.

The Nightjar Localization Services Agreement does not bear on the transaction. It is Dilur's own vendor agreement, not an asset of Glesar, not an Assigned Contract, and not a source of any consent or liability issue. I have excluded it from the analysis below.

---

## Issue 1 – Composer Claim: The Section 6.7 Termination Window Has Likely Expired

**Where:** Asset Purchase Agreement § 6.7; Dilur Board Consent, Recitals C–F and Resolution 2.1; APA § 4.7, § 4.9, Schedule 4.9(d).

**The problem.** On September 14, 2026, Glesar delivered a Schedule Update disclosing a pending claim by the Emberfall Soundtrack composer alleging copyright infringement and asserting royalty rights (the "Composer Claim"). Under § 6.7 of the APA, if Buyer does not terminate within **ten (10) Business Days** after receipt of the Schedule Update, the update "shall be deemed to have cured any inaccuracy in or breach of any representation or warranty disclosed in it, for purposes of Article IX and for purposes of determining whether the conditions in Article VII have been satisfied."

September 14, 2026 was a Sunday. Counting forward, the tenth Business Day fell on **September 26, 2026**. The Board Consent is dated **October 6, 2026**—ten calendar days after the deadline passed. The Board's resolution to "object" and "reserve all rights" (Resolution 2.1) does not track any mechanism in § 6.7. The contract provides only two paths: terminate within the window, or accept the deemed cure. There is no "objection" path that preserves indemnification rights for the disclosed matter.

**Why it matters.** The Composer Claim directly implicates:
- § 4.7 (Litigation) – no pending or threatened claims;
- § 4.9(c) (Non-infringement) – the Assigned IP does not infringe third-party IP;
- § 4.9(d) (Employee/contractor assignments) – no royalty rights except as set forth on Schedule 4.9(d), which states "None."

Section 4.9 is a **Fundamental Representation** under § 9.5(c), carrying a survival period of 60 days past the applicable statute of limitations and a liability cap equal to the full Purchase Price. If the deemed cure in § 6.7 applies, Dilur loses its ability to claim breach of these representations for the Composer Claim, and the § 7.2(a) bring-down condition (which requires § 4.9 to be true "in all respects") is deemed satisfied.

**Potential mitigating arguments (but do not rely on them without further facts):**
- If Glesar knew of the Composer Claim before the Signing Date (August 24) and failed to disclose it, the fraud carve-out in § 9.5(d) preserves Dilur's rights regardless of the Schedule Update mechanism. We need to investigate when the claim arose and when Glesar first learned of it.
- If the Schedule Update is materially incomplete (e.g., it does not identify the specific compositions at issue or the amount of royalties claimed), one could argue it does not constitute a valid "disclosure" that triggers the cure. This is a factual question.
- The Composer Claim liability may still be an **Excluded Liability** under § 2.4(d) (pre-Closing IP infringement) and § 2.4(e) (pre-Closing facts), indemnifiable under § 9.2(c), which is **not** subject to the General Cap. The deemed cure in § 6.7 applies to "representations and warranties," not to the definition of Excluded Liabilities in § 2.4. This is Dilur's strongest remaining contractual hook, but it is untested and the Board Consent's framing (focused on rep breach) may have missed it.

**Recommended fix.**
1. **Immediately** send a written notice to Glesar (under the authority in Board Consent Resolution 2.3) that (a) asserts the Composer Claim liability is an Excluded Liability under §§ 2.4(d) and 2.4(e) and is indemnifiable under § 9.2(c) without regard to the General Cap; (b) demands that Glesar confirm in writing that it bears all liability for the Composer Claim; and (c) reserves all rights, including the fraud carve-out.
2. **Negotiate a special indemnity or escrow.** Given the Board's authorization (Resolution 2.3), propose a holdback of a negotiated amount from the Purchase Price (or an escrow funded by Glesar) to cover the Composer Claim, to be released upon resolution of the claim. Proposed language for an amendment:

> **Section 9.8 (new).** Notwithstanding anything to the contrary in this Agreement or Section 6.7, Seller shall indemnify, defend and hold harmless the Buyer Indemnitees from and against all Losses arising out of or relating to the Composer Claim disclosed in the Schedule Update dated September 14, 2026, including all royalties, damages, settlements and costs associated with it. Seller's obligations under this Section 9.8 shall survive the Closing until the Composer Claim is finally resolved and shall not be subject to the General Cap, the basket in Section 9.5(b), or the survival period in Section 9.1.

3. **Investigate the timing** of Glesar's knowledge of the Composer Claim relative to the Signing Date. If Glesar knew before August 24 and did not disclose, prepare a fraud-based claim as a fallback.

---

## Issue 2 – Wickline Toolkit: License Cannot Be Assigned Without Okoro's Consent; Termination Triggered by Asset Sale

**Where:** Key Employee Agreement § 12.4, § 7.2(b); APA § 6.4, Schedule 2.1(c) item 1, Schedule 4.4.

**The problem.** The Emberfall Game Code incorporates the Wickline Toolkit, a proprietary engine developed by Tamsin Okoro before her employment. Glesar holds only a **non-exclusive, royalty-free license** to Wickline under § 7.2(b) of the Key Employee Agreement. Critically, § 12.4 provides:

> "The Company may not assign or transfer this Agreement, or any of its rights under it, **including the license granted in Section 7.2**, without the prior written consent of Employee. This restriction applies whether the assignment or transfer occurs by operation of law, merger, conversion, change of control, **sale of all or substantially all of the Company's assets**, or otherwise. **Any purported assignment or transfer in violation of this Section 12.4 is void, and upon any such purported assignment or transfer the license granted in Section 7.2 terminates.**"

The APA contemplates assigning the Key Employee Agreement to Dilur at Closing (§ 6.4; Schedule 2.1(c) item 1). But the Key Employee Agreement makes that assignment **void** without Okoro's consent and **terminates the Wickline license** upon any such purported assignment.

**Why it matters.** Without the Wickline license, Dilur does not have the right to use, modify, or distribute the Wickline components embedded in the Emberfall Game Code. The Wickline components include the level editor, shader library, animation state-machine runtime, and build utilities (Exhibit A to the Key Employee Agreement). These are not peripheral—they are core engine infrastructure. Losing the license could render the acquired Game Code partially unusable or expose Dilur to infringement claims by Okoro.

**Recommended fix.**
1. **Obtain Okoro's written consent to the assignment before Closing.** Add her consent to Schedule 4.4 and make it a condition to Closing under § 7.2(c).
2. **Negotiate a standalone license or assignment of Wickline** from Okoro to Dilur, separate from the employment agreement, so that the license survives even if Okoro's employment ends. Proposed terms: exclusive (or at minimum, the same non-exclusive scope), perpetual, irrevocable, royalty-free, covering use in the Emberfall franchise **and in Dilur's other titles** (see Issue 6 below).
3. **Amend Schedule 4.4** to list Okoro's consent. The current entry—"None. No third-party consents are required"—is factually incorrect and makes the § 4.4 representation inaccurate as of the Signing Date.

---

## Issue 3 – IP Assignment Agreement § 6.3 Caps IP Representations at the General Cap, Contradicting the APA

**Where:** IP Assignment Agreement § 6.3; APA § 9.5(c), § 11.12.

**The problem.** APA § 9.5(c) designates § 4.9 (Intellectual Property) as a **Fundamental Representation**, excluded from the General Cap ($7,275,000) and the basket, with Seller's liability capped at the full Purchase Price ($48,500,000).

IP Assignment Agreement § 6.3 states:

> "Assignor's liability for any inaccuracy in or breach of Section 4.9 of the Purchase Agreement or Section 3 of this Agreement shall be subject to the **General Cap**."

APA § 11.12 (Order of Precedence) provides: "In the event of any conflict or inconsistency between this Agreement and any other Transaction Document, **the IP Assignment Agreement shall control on matters concerning Assigned IP**."

Read together, § 6.3 of the IP Assignment Agreement overrides the APA's Fundamental Rep treatment for IP claims, reducing Dilur's maximum recovery for an IP breach from $48.5 million to $7.275 million.

**Why it matters.** This is precisely the scenario Dilur faces with the Composer Claim. If the Composer Claim constitutes a breach of § 4.9 (which it likely does), Dilur's recovery is capped at 15% of the Purchase Price rather than the full amount. For a $48.5 million acquisition of an IP-centric business, this is a material reduction in protection.

**Recommended fix.** Amend IP Assignment Agreement § 6.3 to conform to the APA. Proposed replacement:

> **6.3 Liability for Intellectual Property Matters.** Assignor's liability for any inaccuracy in or breach of Section 4.9 of the Purchase Agreement or Section 3 of this Agreement shall be subject to the limitations set forth in Section 9.5 of the Purchase Agreement, including the treatment of Section 4.9 as a Fundamental Representation under Section 9.5(c) thereof.

Alternatively, if Glesar resists, negotiate a **super-cap** for IP claims (e.g., 50% of the Purchase Price) as a compromise, but do not accept the current 15% General Cap for Fundamental Reps.

---

## Issue 4 – IP Assignment Agreement § 5.2: Uncapped Buyer Indemnity for All IP-Related Losses

**Where:** IP Assignment Agreement § 5.2; APA § 2.4(d), § 9.2(c).

**The problem.** IP Assignment Agreement § 5.2 requires Dilur to indemnify Glesar for:

> "all Losses arising out of or relating to the Assigned IP or the ownership, use, licensing, distribution or other exploitation of the Assigned IP, **whether arising before or after the Effective Date**. Assignee's obligations under this Section 5.2 are **not subject to any limitation in the Purchase Agreement**."

This means Dilur must indemnify Glesar for pre-closing IP claims—including, potentially, the Composer Claim—with **no cap, no basket, and no survival limit**.

**Why it matters.** This directly contradicts the APA's allocation of risk:
- APA § 2.4(d) makes pre-Closing IP infringement an **Excluded Liability** retained by Seller.
- APA § 9.2(c) requires Seller to indemnify Buyer for Excluded Liabilities.

Under § 5.2 of the IP Assignment Agreement, Dilur would be indemnifying Glesar for the very claims that Glesar is supposed to indemnify Dilur for. If the Composer Claim proceeds, Glesar could turn to Dilur under § 5.2, creating a circular indemnity that effectively shifts the pre-closing IP risk to Dilur.

**Recommended fix.** Delete § 5.2 in its entirety, or replace with:

> **5.2 Indemnification by Assignee.** From and after the Effective Date, Assignee shall indemnify, defend and hold harmless the Assignor Indemnitees from and against all Losses arising out of or relating to the ownership, use, licensing, distribution or other exploitation of the Assigned IP **arising after the Effective Date**, subject to the limitations in Section 9.5 of the Purchase Agreement.

The key changes: (a) limit to post-Effective Date matters; (b) subject to the APA's caps and basket.

---

## Issue 5 – Schedule 4.4 Is Incorrect: Third-Party Consents Are Required

**Where:** APA Schedule 4.4, § 4.4, § 7.2(c); Key Employee Agreement § 12.4.

**The problem.** Schedule 4.4 states: "None. No third-party consents are required." This is inaccurate. At minimum, Okoro's consent is required to assign the Key Employee Agreement and the Wickline license (Key Employee Agreement § 12.4). Additionally, the platform distribution agreements and middleware license agreements listed in Schedule 2.1(c) (items 2 and 3) very likely contain anti-assignment clauses requiring counterparty consent. We cannot verify this because the data room index and the underlying agreements are not in the folder (see Issue 9).

**Why it matters.** The § 4.4 representation ("No consent... is required... except as set forth on Schedule 4.4") is false as of the Signing Date. This is a breach of a representation that is subject to the bring-down condition in § 7.2(a). If discovered post-closing, it could give rise to an indemnification claim—but more practically, it means the § 7.2(c) condition (all consents on Schedule 4.4 obtained) is vacuously satisfied because the schedule is empty, masking the fact that required consents have not been obtained.

**Recommended fix.**
1. Populate Schedule 4.4 with all required consents (Okoro; platform holders; middleware licensors).
2. Make each consent a condition to Closing under § 7.2(c).
3. For any consent that cannot be obtained before Closing, use the § 2.7 fallback (non-assignable assets) but negotiate a more specific arrangement.

---

## Issue 6 – Wickline License Scope Is Limited to the Emberfall Franchise

**Where:** Key Employee Agreement § 7.2(b).

**The problem.** The Wickline license permits use "solely in connection with the development, publication, distribution, operation and exploitation of the **Emberfall franchise and any sequels, expansions, ports or remasters** of it." The Wickline Toolkit includes general-purpose engine components (level editor, shader library, animation runtime, build utilities) that Dilur would likely want to use across its broader portfolio.

**Why it matters.** If Dilur's business plan includes reusing Wickline technology in other titles, the current license does not permit that. Dilur would be paying $48.5 million for an asset (the Game Code) that contains technology it can only use in one franchise.

**Recommended fix.** As part of negotiating Okoro's consent (Issue 2), seek to expand the license scope. Proposed language for a new or amended § 7.2(b):

> "Employee hereby grants to the Company [and its successors and assigns, including Dilur Interactive, Inc. and its Affiliates] a non-exclusive, worldwide, perpetual, irrevocable, royalty-free, fully paid-up license to use, reproduce, modify, create derivative works of, compile and incorporate the Wickline Toolkit in connection with the development, publication, distribution, operation and exploitation of the Emberfall franchise and any sequels, expansions, ports or remasters of it, **and in connection with any other video game or interactive entertainment product developed or published by the Company or its Affiliates**."

If Okoro resists full portfolio access, a fallback is to limit the expansion to "the Company's action role-playing titles" or to a defined number of additional titles.

---

## Issue 7 – IP Assignment Agreement Does Not Address Wickline

**Where:** IP Assignment Agreement §§ 2.1, Schedule A; Key Employee Agreement § 7.2.

**The problem.** The IP Assignment Agreement assigns the "Emberfall Game Code" (Schedule A, item 2), which incorporates Wickline. But the IP Assignment Agreement contains no reference to the Wickline license, no assignment of the license (which cannot be assigned without Okoro's consent), and no carve-out acknowledging that Glesar's rights in the Wickline components are limited to a license rather than ownership.

**Why it matters.** The assignment in § 2.1 purports to transfer "all of Assignor's right, title and interest in, to and under the Assigned IP." But Glesar's "right, title and interest" in the Wickline components is only a non-exclusive license that terminates upon the asset sale (per § 12.4 of the Key Employee Agreement). The IP Assignment Agreement creates a false impression that Dilur is receiving full ownership of everything in the Game Code repositories.

**Recommended fix.** Add a new section to the IP Assignment Agreement:

> **2.5 Third-Party IP Components.** The Parties acknowledge that the Emberfall Game Code incorporates certain components of the Wickline Toolkit, in which Assignor holds a non-exclusive license under the Key Employee Agreement. The assignment in Section 2.1 includes all of Assignor's right, title and interest in and to the Wickline license, to the extent assignable. Assignee's rights in the Wickline Toolkit are subject to the terms of the Key Employee Agreement, including Section 12.4 thereof, and to any consent or additional license obtained from Tamsin Okoro as a condition to Closing.

This at minimum puts Dilur on notice and creates a hook to require Okoro's consent as a closing condition.

---

## Issue 8 – APA § 4.9(a) Ownership Representation Is Potentially Inaccurate as to Wickline

**Where:** APA § 4.9(a); Key Employee Agreement § 7.2(a).

**The problem.** § 4.9(a) represents that "Seller is the **sole and exclusive owner** of all right, title and interest in and to the Assigned IP." But the Assigned IP includes the Emberfall Game Code, which contains Wickline components in which Glesar is not the owner—Okoro is. Glesar holds only a license.

**Why it matters.** If this representation is inaccurate, it is a breach of a Fundamental Representation. However, because § 4.9 is a Fundamental Rep (true in "all respects" for the bring-down condition), even a technical inaccuracy could block closing under § 7.2(a) unless cured or waived. In practice, this gives Glesar leverage: it could argue the rep is inaccurate and negotiate a price reduction, or Dilur could argue it is a known and disclosed limitation (via the Key Employee Agreement) and not a material inaccuracy.

**Recommended fix.** Add a carve-out to § 4.9(a) or to Schedule 2.1(a):

> "Seller is the sole and exclusive owner of all right, title and interest in and to the Assigned IP, **except that the Emberfall Game Code incorporates certain components of the Wickline Toolkit, in which Tamsin Okoro retains ownership and Seller holds a non-exclusive license as set forth in the Key Employee Agreement, which license is included in the Assigned IP and assigned to Buyer at the Closing subject to Section 12.4 of the Key Employee Agreement**."

This cleans up the representation and makes the Wickline issue express rather than latent.

---

## Issue 9 – Missing Documents

The following documents are referenced in the APA or are necessary for Dilur to make an informed decision but are **not in the folder**:

| Document | Referenced In | Why Needed |
|---|---|---|
| **Disclosure Schedule** (delivered at Signing) | APA § 1.1(g) | To verify what Glesar actually disclosed at signing; critical to assessing whether the Composer Claim was known pre-signing (fraud analysis for Issue 1) |
| **September 14, 2026 Schedule Update** | Board Consent, Recital C | To assess adequacy of disclosure; to determine whether the § 6.7 cure is valid |
| **Data room index** (platform and middleware agreements) | APA Schedule 2.1(c), items 2–3 | To identify anti-assignment clauses and required consents (Issue 5) |
| **Platform distribution agreements** | APA Schedule 2.1(c), item 2 | Same |
| **Middleware license agreements** | APA Schedule 2.1(c), item 3 | Same |
| **Asset register** (tangible personal property) | APA Schedule 2.1(b) | To verify what hardware is being acquired |
| **Full employee list with compensation** | APA Schedule 4.10 | To assess assumed employment liabilities and Good Reason exposure |
| **Okoro's consent to assignment** | Key Employee Agreement § 12.4 | Required closing deliverable (Issue 2) |
| **Composer's claim / complaint** | Board Consent, Recital C | To assess the scope and magnitude of the Composer Claim |

**Recommended action.** Request all of the above from Glesar (or from our data room access) before proceeding to Closing. The Disclosure Schedule and the September Schedule Update in particular are essential to the Issue 1 analysis.

---

## Issue 10 – Key Employee Agreement: Good Reason Trigger and Reporting Structure

**Where:** Key Employee Agreement § 1.1(c) (Good Reason), § 2.1 (reporting structure), § 5.5 (severance).

**The problem.** "Good Reason" includes "a material diminution in Employee's title, authority or creative responsibilities for the Emberfall franchise." Post-acquisition, Dilur will be reorganizing the business. If Okoro's reporting line changes (she currently reports to Glesar's Managing Member, who will no longer be in the picture), or if Dilur assigns creative oversight to another executive, Okoro could claim Good Reason and trigger 12 months' severance ($285,000) plus COBRA.

Additionally, § 2.1 states she reports to "the Company's Managing Member." After the asset purchase, Glesar may be a shell or dissolved entity. The Key Employee Agreement, as assigned to Dilur, contains a reference to a role that may not exist.

**Why it matters.** This is a manageable but real post-closing risk. If Dilur restructures the Emberfall team in a way that diminishes Okoro's role, it faces a severance payment and potential loss of the key creative talent (and with her, the Wickline relationship).

**Recommended fix.**
1. In negotiating Okoro's consent to the assignment (Issue 2), confirm in writing that her title, reporting structure, and creative responsibilities will be preserved for a defined period (e.g., 18–24 months post-closing).
2. Amend § 2.1 of the Key Employee Agreement to replace "the Company's Managing Member" with "the Company's [CEO / Head of Development / such other senior executive as the Company designates]" to accommodate the post-acquisition structure.
3. Model the severance exposure ($285,000 + COBRA) as a contingent liability in Dilur's post-closing integration plan.

---

## Note on the Nightjar Localization Services Agreement

I reviewed the Nightjar agreement in full. It is a services agreement between Dilur and Nightjar Localization Ltd. for translation, localization, and QA work on Dilur's own titles. It is:
- Not an asset of Glesar;
- Not listed as an Assigned Contract;
- Not a source of any consent, liability, or IP issue relevant to the acquisition;
- Governed by its own terms (New York law, Manhattan jurisdiction) that do not conflict with the APA.

It does not bear on the deal. No action required.

---

## Recommended Next Steps (Priority Order)

1. **Send the Objection/Reservation Notice to Glesar immediately** (authorized by Board Consent Resolution 2.1), specifically asserting the Excluded Liability position under §§ 2.4(d)–(e) and § 9.2(c) with respect to the Composer Claim, and demanding confirmation of Glesar's responsibility.
2. **Request Okoro's written consent** to the assignment of the Key Employee Agreement and the Wickline license, and open a negotiation for a standalone or expanded Wickline license.
3. **Circulate a markup of the IP Assignment Agreement** to Glesar's counsel addressing Issues 3, 4, and 7 (cap conflict, uncapped buyer indemnity, Wickline gap).
4. **Request the missing documents** listed in Issue 9, particularly the Disclosure Schedule, the September Schedule Update, and the Composer's complaint.
5. **Amend Schedule 4.4** to reflect all required consents.
6. **Address the Wickline ownership carve-out** in APA § 4.9(a) (Issue 8).
7. **Plan for post-closing integration** of the Okoro relationship (Issue 10).