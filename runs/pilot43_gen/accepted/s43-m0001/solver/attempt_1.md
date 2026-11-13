# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current]
**RE:** Dilur Interactive / Glesar Studios Asset Purchase – Pre-Signing Issue List

---

## I. ISSUES THAT COULD AFFECT CLOSING OR THE VALUE OF THE PURCHASED ASSETS

### 1. The Wickline License Terminates Automatically if the Key Employee Agreement Is Assigned Without Okoro's Consent

**Where:** Key Employee Agreement § 12.4; APA Schedule 2.1(c) item 1; APA § 6.4; APA Schedule 4.4.

**Why it matters:** Section 12.4 of the Key Employee Agreement provides that Glesar "may not assign or transfer this Agreement, or any of its rights under it, including the license granted in Section 7.2, without the prior written consent of Employee." It further provides that "[a]ny purported assignment or transfer in violation of this Section 12.4 is void, and upon any such purported assignment or transfer the license granted in Section 7.2 terminates." The trigger is broad: it covers assignment "by operation of law, merger, conversion, change of control, sale of all or substantially all of the Company's assets, or otherwise."

The APA treats the Key Employee Agreement as an Assigned Contract (Schedule 2.1(c), item 1) and requires that it be assigned and assumed at Closing (§ 6.4). Schedule 4.4 states that no third-party consents are required. Both are wrong. Okoro's consent is expressly required, and without it the assignment is void and the Wickline license terminates by its own terms—no cure period, no notice, no judicial intervention.

The Wickline Toolkit (Exhibit A to the Key Employee Agreement) includes the level and encounter editor, lighting and particle shader library, animation state-machine runtime, and build and asset-cooking utilities. These are embedded in the Emberfall Game Code (APA § 1.1(h); IP Assignment Agreement § 2.1(a)). If the license terminates, Dilur loses the right to use, modify, compile, and distribute the Wickline components as embodied in the games. The Emberfall Game Code would be incomplete or infringing. This goes to the core value of the acquisition.

**Recommended fix:**

- Obtain Okoro's written consent to the assignment before signing, or as a condition to Closing. Add Okoro's consent to Schedule 4.4 and make it a closing deliverable under § 3.2(d).
- Alternatively, negotiate a consent or waiver from Okoro as a condition precedent in the APA.
- If Okoro's consent cannot be obtained, consider requiring Glesar to negotiate a standalone license or assignment of the Wickline Toolkit (or the Company Modifications under § 7.2(d)) directly to Dilur as a separate closing deliverable, with appropriate reps and warranties.
- Amend Schedule 4.4 to list Okoro's consent. Correct the representation in § 4.4 accordingly.

Proposed language for a new item in Schedule 4.4:

> 1. Written consent of Tamsin Okoro to the assignment of the Key Employee Agreement and the transfer of the Wickline Toolkit license, in form and substance reasonably satisfactory to Buyer.

And in § 3.2(d), replace "the third-party consents listed on Schedule 4.4" with the same language (it already cross-references Schedule 4.4, so correcting the schedule suffices).

---

### 2. IP Assignment Agreement § 5.2 Imposes an Uncapped, Unlimited Indemnity on Dilur for All IP-Related Losses

**Where:** IP Assignment Agreement § 5.2; APA § 2.4(d); APA § 9.2; APA § 11.12.

**Why it matters:** Section 5.2 of the IP Assignment Agreement provides:

> "Assignee shall indemnify, defend and hold harmless the Assignor Indemnitees from and against all Losses arising out of or relating to the Assigned IP or the ownership, use, licensing, distribution or other exploitation of the Assigned IP, whether arising before or after the Effective Date. Assignee's obligations under this Section 5.2 are not subject to any limitation in the Purchase Agreement."

This means Dilur indemnifies Glesar for *all* losses relating to the Assigned IP, including pre-closing losses, with *no cap*. This directly conflicts with APA § 2.4(d), which makes "all Liabilities arising from pre-Closing infringement by or use of the Assigned IP" an Excluded Liability retained by Seller, and with APA § 9.2, which requires Seller to indemnify Buyer for Excluded Liabilities.

Under APA § 11.12 (Order of Precedence), "the IP Assignment Agreement shall control on matters concerning Assigned IP." Therefore, for any IP-related claim—including the Composer Claim (see Issue 4 below)—the IP Assignment Agreement's uncapped buyer indemnity overrides the APA's Excluded Liabilities framework. In practical terms, if the composer prevails and a judgment or settlement is entered, Glesar could turn to Dilur under § 5.2 for the full amount, uncapped, even though under the APA that liability should be Glesar's.

**Recommended fix:**

Strike or substantially revise IP Assignment Agreement § 5.2. Dilur should not indemnify Glesar for pre-closing IP liabilities. The indemnity should be limited to post-closing exploitation and should be subject to the same caps and baskets as the rest of the deal.

Proposed replacement language:

> **5.2 Indemnification by Assignee.** From and after the Effective Date, Assignee shall indemnify, defend and hold harmless the Assignor Indemnitees from and against all Losses arising out of or relating to the ownership, use, licensing, distribution or other exploitation of the Assigned IP *after the Effective Date*, to the extent such Losses result from acts or omissions of Assignee or its Affiliates after the Effective Date. Assignee's obligations under this Section 5.2 shall be subject to the limitations set forth in Section 9.5 of the Purchase Agreement.

---

### 3. IP Assignment Agreement § 6.3 Overrides the APA's Fundamental Representation Cap for IP Claims

**Where:** IP Assignment Agreement § 6.3; APA § 9.5(a) (General Cap = $7,275,000); APA § 9.5(c) (Fundamental Reps excluded from General Cap, capped at Purchase Price = $48,500,000); APA § 11.12.

**Why it matters:** APA § 9.5(c) designates § 4.9 (Intellectual Property) as a Fundamental Representation, excluded from the General Cap and the basket, with a cap equal to the full Purchase Price ($48,500,000). IP Assignment Agreement § 6.3 provides:

> "Assignor's liability for any inaccuracy in or breach of Section 4.9 of the Purchase Agreement or Section 3 of this Agreement shall be subject to the General Cap."

This caps Glesar's liability for IP representation breaches at $7,275,000 (15% of the Purchase Price), not $48,500,000. Under APA § 11.12, the IP Assignment Agreement controls on matters concerning Assigned IP. The result: if the Composer Claim (or any other IP title defect) costs Dilur more than $7,275,000, Dilur has no contractual recourse against Glesar for the excess, despite § 4.9 being a Fundamental Representation.

For a $48.5 million acquisition of a game franchise whose value is substantially in its IP, capping IP indemnification at $7.3 million is a material reduction in Dilur's protection.

**Recommended fix:**

Delete IP Assignment Agreement § 6.3, or revise it to conform to the APA's Fundamental Representation treatment:

> **6.3 Liability for Intellectual Property Matters.** Assignor's liability for any inaccuracy in or breach of Section 4.9 of the Purchase Agreement or Section 3 of this Agreement shall be subject to the limitations set forth in Section 9.5 of the Purchase Agreement, including the treatment of Fundamental Representations under Section 9.5(c).

---

### 4. The September Schedule Update Triggers the Deemed Cure in APA § 6.7; the Termination Window Has Passed

**Where:** APA § 6.7; APA § 10.1(d); Dilur Board Consent, Recitals C–F and Resolution 2.1.

**Why it matters:** On September 14, 2026 (a Monday), Glesar delivered a Schedule Update disclosing the Composer Claim—a pending claim by the Emberfall Soundtrack composer alleging copyright infringement and asserting royalty rights. Under APA § 6.7:

> "If a Schedule Update discloses a matter that would cause the condition in Section 7.2(a) not to be satisfied, Buyer may terminate this Agreement under Section 10.1(d) by written notice to Seller delivered within ten (10) Business Days after Buyer's receipt of that Schedule Update. If Buyer does not terminate this Agreement within that period, the Schedule Update shall be deemed to have cured any inaccuracy in or breach of any representation or warranty disclosed in it, for purposes of Article IX and for purposes of determining whether the conditions in Article VII have been satisfied."

Ten business days after Monday, September 14, 2026, expired on Monday, September 29, 2026. The Board Consent is dated October 6, 2026—five business days after the deadline. The Board authorized an "Objection Notice" (Resolution 2.1) but not a termination notice. An objection is not a termination. The deemed cure has therefore operated: for purposes of Article IX (indemnification) and Article VII (closing conditions), the Composer Claim is deemed cured.

This means:
- Dilur may have lost its indemnification rights under § 9.2(a) for the inaccuracy in §§ 4.7 and 4.9 caused by the Composer Claim.
- The Composer Claim no longer prevents satisfaction of the closing condition in § 7.2(a).
- The Board's reservation of rights (Resolution 2.2) has no clear contractual basis to override the deemed cure.

The Composer Claim implicates § 4.9 (a Fundamental Representation), § 4.7 (Litigation), and Schedule 4.9(d) (which states "None" for royalty obligations). If the composer is a contractor who contributed to the Soundtrack without executing a valid assignment to Glesar, the title to the Emberfall Soundtrack (APA § 1.1(j); Schedule 2.1(a) item 3) may be defective.

**Recommended fix:**

This is the most time-sensitive issue. Options, in order of preference:

1. **Negotiate a specific indemnity or escrow with Glesar** covering the Composer Claim, structured as an amendment to the APA that carves the Composer Claim out of the deemed cure. The Board has already authorized this negotiation (Resolution 2.3). Propose language such as:

   > Notwithstanding Section 6.7, the Parties agree that the September Schedule Update shall not be deemed to have cured any inaccuracy in or breach of any representation or warranty of Seller, and Seller shall indemnify Buyer under Section 9.2 for all Losses arising out of or relating to the Composer Claim, without limitation under Section 9.5.

2. **Assert that the deemed cure does not apply to fraud.** If Glesar knew of the Composer Claim before the Signing Date (August 24, 2026) and failed to disclose it, the initial failure to disclose may constitute fraud, which is carved out of all limitations under § 9.5(d) and arguably outside the scope of § 6.7's deemed cure (which operates on "inaccuracy in or breach of any representation or warranty," not on fraudulent concealment). Investigate whether Glesar had actual knowledge before signing.

3. **Termination.** If the Composer Claim is material and Glesar will not agree to a specific indemnity, consider whether termination under § 10.1(c) (breach of representation not cured within 20 days) is still available. The § 6.7 deemed cure applies "for purposes of Article IX and for purposes of determining whether the conditions in Article VII have been satisfied." It does not expressly preserve or extinguish the termination right under § 10.1(c), which is a separate mechanism. However, this is an argument, not a clear right, and should be pursued cautiously.

4. **In any event, do not waive the objection.** The Board's Objection Notice (Resolution 2.1) should be sent immediately if not already sent, to preserve equitable arguments and to put Glesar on notice.

---

### 5. Schedule 4.4 Is Incorrect: Okoro's Consent Is Required

**Where:** APA Schedule 4.4; APA § 4.4; Key Employee Agreement § 12.4.

**Why it matters:** Schedule 4.4 states: "None. No third-party consents are required." This is flatly incorrect. Section 12.4 of the Key Employee Agreement requires Okoro's prior written consent for any assignment or transfer, including a "sale of all or substantially all of the Company's assets." The APA's own § 4.4 represents that no consents are required "except as set forth on Schedule 4.4." The schedule is therefore a false disclosure, and the representation in § 4.4 is inaccurate as of the Signing Date.

This is not merely a technical error. It means:
- The closing deliverable in § 3.2(d) (third-party consents) cannot be satisfied as currently drafted.
- The condition in § 7.2(c) (consents obtained) cannot be met.
- Glesar's representation in § 4.4 is breached, giving Dilur a potential termination right under § 10.1(c) (if not cured within 20 days).

**Recommended fix:**

- Amend Schedule 4.4 to list Okoro's consent (see proposed language in Issue 1 above).
- Amend § 4.4 to reflect the correction.
- Make Okoro's consent a condition to Closing under § 7.2(c) (it already is, by cross-reference to Schedule 4.4, once the schedule is corrected).
- Consider whether the inaccuracy in § 4.4 as of the Signing Date gives Dilur an independent termination right under § 10.1(c), separate from the § 6.7 analysis.

---

## II. OTHER SIGNIFICANT ISSUES

### 6. The Composer Claim Raises a Title Defect in the Emberfall Soundtrack

**Where:** Dilur Board Consent, Recital C; APA § 4.9(a), (c), (d); APA Schedule 2.1(a) item 3; APA Schedule 4.9(d).

**Why it matters:** The Emberfall Soundtrack (all musical compositions, sound recordings, stems and audio assets for the Emberfall franchise) is a core component of the Assigned IP (APA § 1.1(j); Schedule 2.1(a) item 3). The Composer Claim alleges that Glesar's exploitation of "certain compositions and master recordings" infringes the composer's copyrights and that the composer is owed royalties. Schedule 4.9(d) states "None" for royalty obligations, and § 4.9(d) represents that every contributor "has executed a valid written assignment to Seller of all of that Person's rights in that contribution."

If the composer is correct, Glesar does not own the compositions or master recordings in question, and the "Assigned IP" as defined includes assets Glesar has no right to sell. This is a title defect in a Fundamental Representation (§ 4.9). Even if the deemed cure in § 6.7 has operated (see Issue 4), the underlying title problem remains: Dilur would be paying $48.5 million for a Soundtrack in which it may not have clear ownership.

**Recommended fix:**

- Require Glesar to produce the composer's agreement (employment, work-for-hire, or license) and any assignment of rights. If no valid assignment exists, negotiate a direct assignment or license from the composer to Dilur as a condition to Closing.
- If the Composer Claim cannot be resolved before Closing, negotiate an escrow or holdback of a portion of the Purchase Price (the Board has authorized this under Resolution 2.3) sufficient to cover the exposure.
- In the interim, treat the Soundtrack as a potentially defective asset and consider whether the Purchase Price should be adjusted.

---

### 7. APA § 2.7 (Non-Assignable Assets) Fallback Is Inadequate for the Wickline License

**Where:** APA § 2.7; Key Employee Agreement § 7.2, § 12.4.

**Why it matters:** Section 2.7 provides that if an Assigned Contract cannot be assigned without an unobtained consent, the APA "shall not constitute an assignment" and Seller shall "provide Buyer the benefits of that Assigned Contract under any reasonable arrangement Buyer requests." This fallback is designed for ordinary commercial contracts (e.g., a distribution agreement where the counterparty withholds consent). It is wholly inadequate for the Wickline license because:

- The Wickline license does not merely fail to assign; it *terminates* automatically upon a non-consented assignment (§ 12.4). There are no "benefits" to provide under a "reasonable arrangement" if the license no longer exists.
- The "reasonable arrangement" language gives Glesar discretion over the terms, and Glesar has no obligation to grant a new license to Dilur.
- The Emberfall Game Code cannot be built, distributed, or updated without the Wickline components. A "reasonable arrangement" that provides access to the code but not the right to use the Wickline toolkit is not commercially viable.

**Recommended fix:**

- Add a specific provision addressing the Wickline Toolkit. For example:

  > If the consent of Tamsin Okoro required under Section 12.4 of the Key Employee Agreement has not been obtained at or before the Closing, Seller shall, as a condition to the Closing, negotiate in good faith and execute a standalone license or assignment of the Wickline Toolkit (or the Company Modifications under Section 7.2(d) of the Key Employee Agreement) to Buyer on terms no less favorable than those in Section 7.2 of the Key Employee Agreement, in form and substance reasonably satisfactory to Buyer.

- Alternatively, make Okoro's consent a condition to Closing (see Issue 1) so that § 2.7 is not triggered.

---

### 8. No Escrow, Holdback, or Security for Indemnification Obligations

**Where:** APA § 2.5; APA Article IX.

**Why it matters:** The Purchase Price is paid in full by wire transfer at Closing (§ 2.5). There is no escrow, holdback, letter of credit, or other security for Glesar's indemnification obligations under Article IX. Given the Composer Claim (Issue 4), the potential Wickline license termination (Issue 1), and the reduced IP cap (Issue 3), Dilur's post-closing remedy is an unsecured claim against Glesar—a small LLC that will have distributed the $48.5 million proceeds. If Glesar dissolves or its members extract the funds, Dilur's indemnification rights may be worthless.

**Recommended fix:**

- Negotiate an escrow or holdback of a portion of the Purchase Price (e.g., $5–10 million) for a period sufficient to cover the survival of the Fundamental Representations (60 days after the applicable statute of limitations expires, per § 9.1). The Board has authorized this (Resolution 2.3).
- Alternatively, require a parent guarantee or personal guarantee from Glesar's managing member.
- At minimum, given the Composer Claim, negotiate a specific escrow for that claim.

---

### 9. "Knowledge of Seller" Includes Tamsin Okoro, Whose Cooperation May Be Compromised

**Where:** APA § 1.1(p); Key Employee Agreement § 12.4.

**Why it matters:** "Knowledge of Seller" is defined as the actual knowledge of Glesar's managing member, its CFO, and Tamsin Okoro. Multiple representations are qualified by "to the Knowledge of Seller" (§§ 4.3(c), 4.6, 4.7, 4.9(c)). If Okoro withholds consent to the assignment (Issue 1) or departs, her continued availability as a knowledge source is uncertain. More practically, if Okoro is the person with the most detailed knowledge of the Wickline Toolkit's integration into the Emberfall Game Code, her potential adversarial position (if she objects to the deal) could affect the reliability of knowledge-qualified reps.

**Recommended fix:**

- This is a lower-priority issue, but consider adding a sentence to the APA requiring Seller to use reasonable efforts to maintain Okoro's cooperation as a knowledge source through Closing, or expanding the knowledge group to include the lead audio engineer or technical director.

---

## III. DRAFTING AND HOUSEKEEPING ISSUES

### 10. APA § 1.1(n) References Exhibit A, but the IP Assignment Agreement Is a Separate Document

**Where:** APA § 1.1(n); APA Exhibit A.

**Why it matters:** Section 1.1(n) defines "IP Assignment Agreement" as the agreement "to be delivered at the Closing in the form attached as Exhibit A." Exhibit A states "[Attached separately.]" The IP Assignment Agreement in the folder appears to be the operative document, not merely a form. The cross-reference should be cleaned up to avoid ambiguity about whether the attached form or a separately negotiated document controls.

**Recommended fix:** Revise § 1.1(n) to read: "the Intellectual Property Assignment Agreement between Seller, as assignor, and Buyer, as assignee, in the form attached as Exhibit A, as may be amended by mutual written agreement of the Parties before the Closing."

---

### 11. IP Assignment Agreement § 6.2 Survival Period Is Correct but Should Be Harmonized with § 6.3

**Where:** IP Assignment Agreement § 6.2; § 6.3.

**Why it matters:** Section 6.2 provides that the Section 3 representations survive for the Fundamental Representation period (60 days after statute of limitations). Section 6.3 subjects the same representations to the General Cap. These two provisions are in tension: the longer survival period implies greater protection, but the lower cap undermines it. Fixing § 6.3 (see Issue 3) will resolve the tension.

---

### 12. APA § 9.5(b) Basket Is a Tipping Basket (First-Dollar Recovery)

**Where:** APA § 9.5(b).

**Why it matters:** The basket is $242,500 (0.5% of the Purchase Price). Once exceeded, Seller is liable "from the first dollar." This is a tipping basket, not a deductible, which is favorable to Dilur. No change needed, but be aware that the basket does not apply to Fundamental Representations (§ 9.5(c)), so the Composer Claim (if it qualifies as a Fundamental Rep breach) would not be subject to the basket in any event.

---

## IV. MISSING DOCUMENTS AND INFORMATION

The following items are referenced in the deal documents but are not in the folder. I recommend requesting them before signing:

| # | Item | Referenced In | Why Needed |
|---|------|---------------|------------|
| 1 | The Disclosure Schedule (as delivered on the Signing Date) | APA § 1.1(g) | To verify what Glesar actually disclosed, particularly regarding the Composer, the Wickline Toolkit, and any IP defects. The September Schedule Update is not in the folder either. |
| 2 | The September Schedule Update (original) | Dilur Board Consent, Recital C | To confirm the exact scope of the Composer Claim and the representations it implicates. |
| 3 | The Composer's agreement with Glesar (employment, work-for-hire, or license) | APA § 4.9(d) | To assess whether Glesar actually owns the Soundtrack compositions and master recordings. |
| 4 | The data room index and the platform distribution agreements and middleware license agreements | APA Schedule 2.1(c) items 2–3 | To verify that these contracts are assignable, to identify any change-of-control or anti-assignment provisions, and to confirm that Schedule 4.4's "no consents required" statement is accurate for them as well. |
| 5 | The asset register for tangible personal property | APA Schedule 2.1(b) | To confirm the scope of hardware being acquired. |
| 6 | The full employee list with titles and compensation | APA Schedule 4.10 | To assess whether any other employees have IP assignments or restrictive covenants that could affect the deal. |
| 7 | Okoro's consent to the assignment (if available) | Key Employee Agreement § 12.4 | Critical closing deliverable (see Issue 1). |
| 8 | Any UCC filings, security agreements, or evidence of encumbrances on the Purchased Assets | APA § 4.5 | To verify the "free and clear of all Encumbrances" representation. |
| 9 | The Emberfall Game Code repositories (or at minimum a build manifest showing Wickline integration) | APA § 3.2(g); Key Employee Agreement Exhibit A | To confirm the extent of Wickline's integration and assess the impact of license termination. |

---

## V. THE NIGHTJAR LOCALIZATION SERVICES AGREEMENT

**Where:** nightjar_localization_services_agreement.md (entire document).

**Assessment:** I reviewed this agreement. It is a pre-existing services contract between Dilur and Nightjar Localization Ltd. (effective February 2, 2026) for translation, localization, and QA services for "certain Dilur titles." It does not involve Glesar, the Emberfall franchise, or any of the Purchased Assets. It is not listed as an Assigned Contract in APA Schedule 2.1(c). It creates no encumbrance on any asset being acquired. Its assignment clause (§ 11.4) permits Dilur to assign to a successor without consent, so it would survive the transaction unaffected.

**Conclusion:** This agreement does not bear on the deal. No action required.

---

## VI. SUMMARY OF RECOMMENDED ACTIONS BEFORE SIGNING

| Priority | Action |
|----------|--------|
| 1 | Obtain Okoro's written consent to the assignment of the Key Employee Agreement and the Wickline license, or restructure the deal to secure the Wickline rights independently. |
| 2 | Revise IP Assignment Agreement § 5.2 to eliminate the uncapped buyer indemnity for pre-closing IP losses. |
| 3 | Revise IP Assignment Agreement § 6.3 to conform to the APA's Fundamental Representation cap. |
| 4 | Address the Composer Claim: negotiate a specific indemnity, escrow, or holdback; assess whether the § 6.7 deemed cure can be overcome (fraud argument, § 10.1(c) termination right); send the Objection Notice immediately if not already sent. |
| 5 | Correct Schedule 4.4 to list Okoro's consent and any other required consents. |
| 6 | Negotiate an escrow or holdback mechanism for general indemnification security. |
| 7 | Request the missing documents listed in Section IV. |
| 8 | Clean up drafting issues (APA § 1.1(n), IP Assignment Agreement § 6.2/6.3 harmony). |