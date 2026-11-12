# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Namaith Facade Systems, Inc. – Review of Lavas Glazing Software License Package: Identified Issues

---

## Summary

I reviewed all five documents in the matter folder. The most significant problems are (1) the Licensee indemnity in Section 9.2 of the Agreement is dramatically broader than what the Term Sheet contemplated and is uncapped; (2) Amendment No. 1 silently removed two protections from the liability-cap exceptions that both the Term Sheet and the original Agreement had provided; and (3) the Amendment acknowledges Namaith's pending change of control by Orvand Partners but expressly disclaims any consent under Section 14.2, leaving Namaith exposed to termination when that deal closes. Details and recommended fixes follow.

---

## Issue 1: Licensee Indemnity (Section 9.2) Is Vastly Broader Than the Term Sheet and Is Uncapped

**Where:** Agreement § 9.2; Term Sheet Item 7 ("Licensee indemnity"); Agreement § 10.3(a) (as originally drafted).

**What the Term Sheet said:**
> "Licensee will indemnify Licensor against third-party claims. Licensee's indemnity is limited to claims from Licensee's negligence or modifications; subject to liability cap."

**What the Agreement actually says:**
Section 9.2 requires Namaith to indemnify Lavas for "any and all third-party claims, losses, damages, liabilities, costs and expenses" arising out of or relating to **any building, curtain wall or structure** incorporating glass fabricated using the Licensed Software. It expressly includes "claims alleging that the Licensed Software, any engineering output it generated or any tempering parameter it applied was defective or erroneous." There is no negligence limitation, no modification limitation, and no requirement that Namaith be at fault.

Section 10.3(a) (original) carves Licensee's § 9.2 indemnity out of both the liability cap and the consequential-damages exclusion, making it **uncapped**.

**Why it matters:** Namaith is effectively insuring Lavas against product-liability and building-failure claims—even where the software itself is the cause. A single catastrophic facade failure on a high-rise could generate eight- or nine-figure exposure, and Namaith would owe it to Lavas with no cap. This inverts the normal allocation of risk: the software vendor should bear the risk that its software is defective, not the customer.

**Recommended fix:**
- Revert § 9.2 to track the Term Sheet: limit the indemnity to claims resulting from Namaith's negligence, willful misconduct, or unauthorized modification of the software.
- Delete the language covering "claims alleging that the Licensed Software… was defective or erroneous"—that is Licensor's risk, not Licensee's.
- If Lavas insists on retaining some broad indemnity, make it subject to the § 10.1 cap and the § 10.2 consequential-damages exclusion (i.e., remove it from § 10.3(a)).
- Add a carve-out: Namaith's indemnity does not apply to the extent the claim is covered by Licensor's § 9.1 IP indemnity or arises from a defect in the Licensed Software.

---

## Issue 2: Amendment No. 1 Removed Licensor's IP Indemnity from the Liability-Cap Exceptions

**Where:** Amendment No. 1, § 2 (restating Agreement § 10.3); Term Sheet Item 7; original Agreement § 10.3(b).

**What changed:**
The original § 10.3(b) excluded "Licensor's indemnification obligations under Section 9.1" from the cap and the consequential-damages exclusion. The Term Sheet confirmed this: "Licensor's IP infringement indemnity is excluded from the liability cap (uncapped)."

Amendment No. 1, § 2 deletes and replaces § 10.3 with only three exceptions: (a) Licensee's § 9.2 indemnity, (b) Licensee's breach of § 7, and (c) Licensee's fee-payment obligation. The exception for Licensor's § 9.1 IP indemnity is gone.

**Why it matters:** If a third party asserts that GlazeCore infringes its patent or copyright, Lavas's indemnity obligation is now capped at roughly $1,405,000 (12 months of fees: $1,240,000 + $165,000 ThermaStress fee) and subject to the consequential-damages exclusion. A significant IP infringement verdict or settlement could far exceed that amount, and Namaith would bear the excess. The Term Sheet and the original Agreement both gave Namaith uncapped protection here; the Amendment quietly took it away.

**Recommended fix:**
- Negotiate a further amendment restoring § 10.3(b) (Licensor's § 9.1 indemnity) as an exception to both the cap and the consequential-damages exclusion, consistent with the Term Sheet and the original Agreement.
- If Lavas resists full uncapped treatment, seek a super-cap (e.g., 3× or 5× annual fees) for IP indemnity obligations.
- Confirm that the Parent Guaranty (which guarantees § 9.1 obligations) is not itself rendered ineffective by the cap—see Issue 7 below.

---

## Issue 3: Amendment No. 1 Made the Confidentiality-Breach Exception One-Way

**Where:** Amendment No. 1, § 2 (restating Agreement § 10.3); Term Sheet Item 7; original Agreement § 10.3(c).

**What changed:**
Original § 10.3(c): "either Party's breach of Section 7" was excluded from the cap and consequential-damages exclusion—mutual protection.

Amended § 10.3(b): only "Licensee's breach of Section 7" is excluded. Licensor's breach of confidentiality is now subject to the ~$1.405M cap and the consequential-damages exclusion.

The Term Sheet stated that "breaches of confidentiality" (without limiting to one party) would be excluded from both the cap and the consequential-damages exclusion.

**Why it matters:** Namaith's Licensee Data (project files, customer designs, tempering records) is Lavas's most sensitive exposure. If Lavas leaks Namaith's proprietary engineering data to a competitor, Namaith's recovery is now capped and cannot include lost profits or lost business opportunity—precisely the damages a data leak would cause.

**Recommended fix:**
- Restore mutual treatment: "either Party's breach of Section 7" as an exception to both § 10.1 and § 10.2.
- Alternatively, if Lavas will not agree to full mutuality, at minimum exclude Licensor's breach of § 7 from the consequential-damages exclusion (so Namaith can recover lost profits from a data leak), even if a cap applies.

---

## Issue 4: Change of Control – No Consent Granted Despite Pending Orvand Partners Acquisition

**Where:** Amendment No. 1, Recital D and § 5; Agreement § 14.2; Agreement § 1.4 (definition of "Control").

**Facts:**
- Recital D of the Amendment states that Namaith Holdings Corp. (parent of Namaith) has signed a definitive agreement to be acquired by Orvand Partners Fund III, L.P.
- Under § 1.4, a change in ownership of an entity that Controls Namaith is a change of Control of Namaith.
- § 14.2 provides that any change of Control of Licensee "shall be deemed an assignment of this Agreement by Licensee requiring Licensor's prior written consent." If it occurs without consent, Licensor may terminate within 120 days of becoming aware.
- § 5 of the Amendment states: "Nothing in this Amendment is a waiver of, or a consent under, any provision of the Agreement."

**Why it matters:** The Amendment acknowledges the Orvand Partners deal in a recital but does not grant the § 14.2 consent. A recital is not an operative provision, and § 5 expressly disclaims any consent. When the Orvand Partners acquisition closes, Namaith will technically be in breach of § 14.2, giving Lavas the right to terminate the entire license (and the ThermaStress module) within 120 days. Namaith cannot afford to lose its fabrication software mid-transaction.

**Recommended fix:**
- Before the Orvand Partners deal closes, obtain a separate written consent from Lavas under § 14.2 (or a further amendment expressly granting consent). This should be a condition to closing in the Orvand Partners definitive agreement.
- If Lavas wants leverage, be prepared to offer a concession (e.g., agreeing to the insurance-rating verification in Issue 5, or a fee adjustment) in exchange for the consent.
- Do not rely on the recital or on Lavas's silence as implied consent—§ 16.2 requires amendments to be in writing and signed.

---

## Issue 5: Insurance – A.M. Best Rating Compliance Is Unclear

**Where:** Agreement § 11.1 (requiring insurers rated "A- VII or better by A.M. Best"); Insurance Certificate Cover Letter, § 2 and § 3.

**The problem:**
The cover letter states the following ratings:
- Bastrop Mutual Casualty Company (CGL): **A XII**
- Meridian Specialty Insurance Company (Tech E&O): **A+ XV**

The cover letter asserts in § 3(c) that "each insurer is rated A- VII or better by A.M. Best." On the standard A.M. Best scale, "A-" corresponds to category IV (Excellent), and category VII corresponds to "B" (Good). The notation "A- VII" in the Agreement is ambiguous—it could mean "A- or better" (categories I–IV) or it could be a drafting error. The ratings as stated in the cover letter ("A XII" and "A+ XV") do not clearly map to the A.M. Best scale in a way that confirms compliance.

**Why it matters:** If the insurers are not actually rated at the required level, Namaith's insurance protection is weaker than the contract contemplates. In a large loss, the insurer's financial strength directly affects Namaith's ability to collect.

**Recommended fix:**
- Request that Harrowgate (the broker) or Lavas confirm in writing the exact A.M. Best rating and category number for each insurer as of the certificate date.
- Clarify with Lavas what "A- VII or better" was intended to mean. If the intent was "A- or better" (i.e., A-, A, A+, A++), verify that both insurers meet that threshold.
- If an insurer does not meet the threshold, demand a replacement policy or an additional insured endorsement from a compliant carrier before the next renewal.

---

## Issue 6: Insurance – Claims-Made E&O Policy vs. Long-Term Coverage Requirement

**Where:** Agreement § 11.1 (coverage required "during the Term and for two (2) years afterward"); Cover Letter § 2 (Tech E&O is claims-made, policy period March 1, 2026 – March 1, 2027, retroactive date March 1, 2019).

**The problem:**
The initial Term runs five years from March 3, 2026 (through ~March 3, 2031). Adding the two-year tail, Licensor must maintain insurance through ~March 3, 2033. The current claims-made policy expires March 1, 2027. The cover letter promises renewal certificates but provides no mechanism to ensure continuous coverage. With a claims-made policy, if there is any gap between policies (even a day), claims first made during the gap are not covered. The 30-day cancellation notice (§ 11.2) helps but does not eliminate the risk.

**Why it matters:** If Lavas lets the E&O policy lapse or fails to renew on time, Namaith could lose coverage for software-related claims (data breaches, system failures causing production losses) that arise during the gap—precisely the type of claim the $5M policy is meant to back.

**Recommended fix:**
- Request that Lavas confirm in writing how it will maintain continuous claims-made coverage through the full required period (Term + 2 years). Specifically, ask whether it will (a) renew the claims-made policy annually without gap, or (b) purchase an extended reporting period (tail) at the end of the Term.
- Add a covenant (via amendment or side letter) requiring Lavas to deliver evidence of continuous coverage or a bound tail policy at least 60 days before any policy expiration.
- Consider requiring that the claims-made policy include a 60-day "prior acts" or "extended reporting" provision as standard.

---

## Issue 7: Parent Guaranty Is Subject to the Same Liability Cap as the Agreement

**Where:** Guaranty § 3.2; Agreement § 10.1.

**The problem:**
Guaranty § 3.2 provides: "Guarantor's liability for any Guaranteed Obligation is no greater than Licensor's liability for that obligation under the License Agreement, **including Section 10 of the License Agreement**."

This means the Guarantor (Lavas Technologies Holdings) is exposed only up to the same cap that limits Licensor. After Amendment No. 1, that cap is ~$1,405,000 for most obligations. For the few uncapped obligations (Namaith's own indemnity, Namaith's confidentiality breach, fee payment), the Guaranty is irrelevant because those are Namaith's obligations, not Lavas's.

**Why it matters:** The practical value of the Guaranty is significantly reduced. If Lavas (the LLC subsidiary) is undercapitalized or becomes insolvent, Namaith can look to the parent—but only for up to ~$1.4M. For a five-year contract with annual fees of $1.4M+, that is less than one year's fees. The Guaranty was presumably obtained to protect Namaith against Licensor's credit risk; as drafted, it provides limited protection.

**Recommended fix:**
- Negotiate a carve-out in Guaranty § 3.2 so that the Guarantor's liability is not subject to the § 10.1 cap for at least: (a) Licensor's § 9.1 IP indemnity (if restored to uncapped per Issue 2), (b) Licensor's § 8.2 warranty refund obligations, and (c) any amounts in excess of the cap resulting from Licensor's gross negligence or willful misconduct.
- Alternatively, seek a standalone cap for the Guaranty that is higher than the Agreement cap (e.g., 2× or 3× annual fees).
- At minimum, confirm that the Guaranty covers the ThermaStress Module Fee and related obligations added by Amendment No. 1 (the Guaranty was executed before the Amendment; § 4.1(b) preserves the Guaranty through amendments made "in accordance with [the Agreement's] terms," but this should be confirmed).

---

## Issue 8: Governing Law Mismatch – Agreement (Delaware) vs. Guaranty (New York)

**Where:** Agreement § 15.1–15.2 (Delaware law; Wilmington, DE forum); Guaranty § 12.1–12.2 (New York law; Manhattan / S.D.N.Y. forum).

**Why it matters:** If Namaith needs to enforce both the Agreement and the Guaranty (e.g., Licensor breaches and Namaith also demands on the Guaranty), it may face parallel proceedings in two jurisdictions under two different bodies of law. This increases cost, creates potential for inconsistent rulings, and complicates strategy. New York guaranty law and Delaware contract law can differ on issues such as the enforceability of "absolute" guaranties, the effect of modifications on the guarantor, and available defenses.

**Recommended fix:**
- Request that Lavas agree to conform the Guaranty's governing law and forum to Delaware / Wilmington, matching the Agreement. This is a reasonable ask and should not be a significant concession for Lavas (which is a Delaware entity with its principal place of business in Texas, not New York).
- If Lavas resists, at minimum negotiate a provision allowing Namaith to join a Guaranty claim as a counterclaim or third-party claim in any Delaware action on the Agreement, or to enforce the Guaranty in Delaware if the Agreement action is pending there.

---

## Issue 9: Guaranty – No Remedy if Parent Sells Licensor

**Where:** Guaranty § 8.2 (notice only); Guaranty § 4.1(c) (Guaranty survives change in ownership of Licensor).

**The problem:**
If Lavas Technologies Holdings sells Licensor to a third party, § 8.2 requires only that the Guarantor notify Namaith within 10 business days. There is no termination right, no requirement to obtain a replacement guaranty, and no fee adjustment. § 4.1(c) provides that the Guaranty is not affected by "any change in the corporate existence, structure or ownership of Licensor."

**Why it matters:** The entire rationale for the Guaranty is that the parent has the financial wherewithal to back the subsidiary. If the parent sells the subsidiary to a private equity firm or a competitor, the economic relationship changes fundamentally. Namaith would be locked into a five-year contract (plus renewals) with a new owner, backed by a guaranty from a parent that no longer owns the business.

**Recommended fix:**
- Add a provision giving Namaith the right to terminate the Agreement (without penalty and with a pro rata refund) if Licensor is sold to a third party that is not an Affiliate of the Guarantor, or if the Guarantor ceases to own a majority of Licensor.
- Alternatively, require that any buyer of Licensor assume the Guaranty or provide a replacement guaranty of equivalent credit quality as a condition to closing.

---

## Issue 10: Section 9.2 Indemnity and Section 9.1 Indemnity – Overlap and Allocation Unclear

**Where:** Agreement §§ 9.1 and 9.2.

**The problem:**
A single event (e.g., a building failure caused by a software defect that also happens to infringe a third party's patent) could trigger both § 9.1 (Licensor indemnifies Namaith for IP claims) and § 9.2 (Namaith indemnifies Lavas for building claims). The Agreement does not allocate responsibility when both sections are implicated.

**Why it matters:** Without a clear allocation, Namaith could be caught in the middle: paying Lavas under § 9.2 for a building claim while simultaneously trying to collect from Lavas under § 9.1 for the IP component of the same event. The net economic result depends on the cap (which, post-Amendment, now applies to § 9.1), creating an asymmetry that favors Lavas.

**Recommended fix:**
- Add a "order of contribution" or "allocation" provision: where a single claim gives rise to obligations under both § 9.1 and § 9.2, the obligations shall be allocated in proportion to each party's responsibility, and neither party shall be required to indemnify the other for amounts that the indemnifying party would be obligated to pay under its own indemnity section.
- At minimum, clarify that § 9.2 does not apply to the extent the underlying claim is covered by § 9.1.

---

## Issue 11: 180-Day Non-Renewal Notice Period – Practical Risk

**Where:** Agreement § 12.2.

**Why it matters:** The Initial Term ends ~March 3, 2031. To avoid the first automatic one-year renewal, Namaith must give notice by ~September 5, 2030. This is a long lead time. If Namaith's business needs change (e.g., it develops in-house software, or the Orvand Partners integration leads to a different vendor strategy), it must make the decision 18 months before the term ends. Missing the deadline locks in another year at $1,405,000.

**Recommended fix:**
- This is less of a "fix" and more of a calendar item. Flag to the client that the non-renewal notice deadline for the first renewal is approximately **September 5, 2030**, and for each subsequent annual renewal, 180 days before the end of that renewal year.
- Consider negotiating a reduction to 90 or 120 days in a future amendment, though this is low-priority given the long initial term.

---

## Issue 12: Licensee Cannot Assign to Its Own Affiliate Without Consent

**Where:** Agreement § 14.1.

**The problem:**
§ 14.1 permits **Licensor** to assign to an Affiliate without consent, but provides no analogous right for **Licensee**. Any assignment by Namaith—including to a wholly owned subsidiary in connection with a reorganization—requires Lavas's prior written consent.

**Why it matters:** If the Orvand Partners integration involves moving Namaith's operations to a different entity (e.g., a new operating company under the Orvand Partners structure), Namaith would need Lavas's consent to assign the license. Combined with Issue 4 (change-of-control consent), this could give Lavas significant leverage over Namaith's post-acquisition corporate structure.

**Recommended fix:**
- In the consent negotiation for the Orvand Partners deal (Issue 4), also seek a provision allowing Namaith to assign to an Affiliate (or to a successor entity in connection with the Orvand Partners transaction) without further consent, provided the assignee assumes all obligations in writing.

---

## Issue 13: Guaranty – 10-Business-Day Performance Window May Be Inadequate

**Where:** Guaranty § 2.2.

**The problem:**
If Licensor fails to perform a Guaranteed Obligation, the Guarantor must "within ten (10) business days after written demand… perform the obligation, or cause it to be performed." For payment obligations, 10 business days is workable. For performance obligations (e.g., implementing the ThermaStress module, providing 24×7 support, correcting a software nonconformity), 10 business days may be unrealistic, particularly if the Guarantor must engage a "qualified third party reasonably acceptable to Beneficiary."

**Why it matters:** If the Guarantor cannot perform within 10 business days, it is in breach of the Guaranty. Namaith's remedy would be a damages claim against the Guarantor—but the amount of damages for delayed software support or implementation is difficult to quantify and may be subject to the consequential-damages exclusion (depending on how the Guaranty interacts with the Agreement's limitation of liability).

**Recommended fix:**
- Seek to extend the performance window to 30 days for non-payment obligations, while keeping 10 business days for payment.
- Clarify that the Guarantor's failure to perform within the stated window gives Namaith the right to engage a third party at the Guarantor's expense (a "step-in" right), rather than limiting Namaith to a damages claim.

---

## Issue 14: Section 13.4(a) – 90-Day Post-Termination Transition May Be Insufficient

**Where:** Agreement § 13.4(a)–(b).

**The problem:**
On termination, Namaith has 90 days to complete in-progress fabrication orders and export its data. For large curtain-wall or insulating-glass projects with long lead times, 90 days may not be enough to wind down.

**Why it matters:** If Namaith is terminated for cause (e.g., for the change-of-control issue in Issue 4), it could lose access to the software mid-project, with only 90 days to finish. The data export right (§ 13.4(b)) is limited to "a standard, non-proprietary format," which may not preserve all tempering recipes, project histories, or integration configurations.

**Recommended fix:**
- Extend the post-termination use period to 180 days, or tie it to the completion date of the last in-progress order (whichever is earlier).
- Specify the data export format in more detail (e.g., CSV, JSON, or a named industry standard) and require that it include all tempering recipes, project parameters, and traceability records.
- Require Licensor to cooperate with Namaith's transition to a replacement vendor during the post-termination period.

---

## Issue 15: Term Sheet Supersession – Limited Evidentiary Value

**Where:** Agreement § 16.3; Term Sheet, opening paragraph.

**The problem:**
§ 16.3 states: "This Agreement supersedes the Term Sheet." The Term Sheet itself states it is non-binding (except Item 12). This means the Term Sheet cannot be used as a contract to enforce the original commercial deal. However, it may still be admissible as evidence of the parties' intent to interpret ambiguities in the Agreement (under Delaware law, prior negotiations are generally admissible to explain ambiguous terms, though the parol evidence rule limits their use to contradict the written agreement).

**Why it matters:**
If a dispute arises over whether Amendment No. 1's restatement of § 10.3 was a negotiated change or a drafting error, the Term Sheet provides strong evidence that the parties originally agreed to uncapped IP indemnity and mutual confidentiality exceptions. But it is not a guarantee of success—the Amendment is a later, signed writing that expressly modifies the Agreement.

**Recommended fix:**
- No contractual fix available post-signing. But preserve the Term Sheet and all negotiation correspondence as evidence.
- In any future amendment, include a recital acknowledging the Term Sheet and confirming which terms are being changed and which are being preserved.

---

## Issue 16: Section 5.3 – Feedback Clause Could Capture Proprietary Process Know-How

**Where:** Agreement § 5.3.

**The problem:**
"Licensor may use any suggestions Licensee provides about the Licensed Software without obligation, provided Licensor does not disclose Licensee Data or Licensee's Confidential Information."

If Namaith's engineers suggest a feature that is based on Namaith's proprietary tempering process or design methodology, Lavas could implement and license that feature to Namaith's competitors. The protection is limited to "Licensee Data" and "Confidential Information"—a suggestion that is not marked confidential and does not contain project-specific data could be used freely.

**Why it matters:** In a competitive facade-engineering market, process innovations suggested to a software vendor can have significant value. Namaith's engineers may not consistently mark their suggestions as confidential.

**Recommended fix:**
- Add a provision that Licensor shall not implement or disclose any suggestion that embodies or is derived from Licensee's trade secrets or proprietary processes, regardless of whether it is marked confidential.
- Train Namaith's Authorized Users to mark all software-related feedback as confidential before submission.

---

## Issue 17: Insurance Certificate – No Evidence of Additional Insured Status

**Where:** Cover Letter § 1 and § 6; Agreement § 11.

**The problem:**
The cover letter states that Namaith is named as "certificate holder." It does not confirm that Namaith is named as an **additional insured** on either policy. A certificate holder is merely a recipient of information; an additional insured is a party to the insurance contract with direct coverage rights.

Section 11 of the Agreement does not explicitly require additional insured status, but the practical purpose of the insurance requirement is to give Namaith a direct source of recovery. If Namaith is only a certificate holder, it must look to Lavas (and then the Guaranty) for recovery, and the insurer owes no duty to Namaith directly.

**Recommended fix:**
- Confirm with Harrowgate whether Namaith is an additional insured on both policies. If not, request that Lavas add Namaith as an additional insured (at least on the CGL policy, and ideally on the Tech E&O policy as well).
- If Lavas resists, at minimum ensure the policies include a "loss payable" clause directing proceeds to Namaith for claims in which Namaith is the injured party.

---

## Issue 18: Ambiguity – "A- VII or Better" Rating Threshold

**Where:** Agreement § 11.1; Cover Letter § 3(c).

**The problem:**
The phrase "rated A- VII or better by A.M. Best" is not standard A.M. Best notation. On the A.M. Best scale, "A-" is a financial strength rating (category IV), and "VII" is a category number corresponding to "B" (Good). It is unclear whether the threshold is (a) A- or better (categories I–IV), (b) B or better (categories I–VII), or (c) some other intended meaning. The cover letter repeats the same ambiguous language and asserts compliance without clarifying the threshold.

**Why it matters:**
If the threshold is actually "B or better" (category VII), then the stated ratings may or may not comply. If it is "A- or better" (category IV), the compliance question is even more acute. The ambiguity cuts both ways but creates uncertainty about whether Namaith has a breach claim if an insurer's rating drops.

**Recommended fix:**
- Request that Lavas confirm in writing the intended rating threshold (e.g., "A- (IV) or better" or "B (VII) or better").
- Amend § 11.1 to use unambiguous A.M. Best notation (e.g., "a financial strength rating of 'A-' or better as assigned by A.M. Best").
- Verify the current ratings of both insurers directly with A.M. Best.

---

## Items Flagged as Ambiguous or Incomplete

| # | Item | Detail |
|---|------|--------|
| A | Schedule A – "as amended from time to time" (§ 1.8) | The definition of "Licensed Software" incorporates Schedule A "as amended from time to time." Amendment No. 1 added the ThermaStress module. But the language could be read to allow Licensor to unilaterally modify the module list. In practice, § 16.2 requires written amendment, but the definitional language is loose. Confirm that no modules can be added or removed without a signed amendment. |
| B | Guaranty § 1.2 – "as in effect on the date hereof" | The Guaranty's definition of "Licensed Software" is frozen as of March 3, 2026. The ThermaStress module was added by Amendment No. 1 on September 14, 2026. Does the Guaranty cover the ThermaStress module? § 4.1(b) says the Guaranty is not affected by amendments "made in accordance with [the Agreement's] terms," which suggests it does. But the frozen definition in § 1.2 creates ambiguity. Confirm in writing that the Guaranty extends to the ThermaStress module. |
| C | Cover Letter – actual certificate not in file | The cover letter references an "Enclosure: Certificate of Liability Insurance dated March 26, 2026," but the actual certificate is not in the matter folder. The cover letter's summary should be verified against the actual certificate, particularly for additional insured status, exclusions, and the claims-made policy's extended reporting provisions. |
| D | Amendment No. 1 – no reference to Guaranty | The Amendment does not mention the Parent Guaranty or confirm that the Guaranty extends to the new ThermaStress obligations. Given the frozen definition in Guaranty § 1.2 (see Item B above), this is a gap. |

---

## Recommended Next Steps (Priority Order)

1. **Before Orvand Partners closing:** Obtain written consent from Lavas under § 14.2 (Issue 4). Make this a condition to closing in the Orvand Partners definitive agreement.
2. **Immediately:** Raise Issues 2 and 3 (Amendment No. 1's § 10.3 restatement) with Lavas. These are material adverse changes from both the Term Sheet and the original Agreement. Seek a further amendment restoring the Licensor IP indemnity exception and the mutual confidentiality exception.
3. **In parallel:** Raise Issue 1 (Section 9.2 scope). This is the largest single exposure and should be the centerpiece of any renegotiation.
4. **Verify insurance:** Request confirmation of A.M. Best ratings (Issue 5/18), additional insured status (Issue 17), and the actual certificate (Item C).
5. **Address Guaranty gaps:** Seek conforming changes to governing law (Issue 8), cap carve-outs (Issue 7), and confirmation of ThermaStress coverage (Items B, D).
6. **Calendar:** Mark the 180-day non-renewal deadline (~September 5, 2030) and the insurance renewal date (March 1, 2027) in the client's compliance calendar (Issue 11, Issue 6).

---

Let me know if you want me to draft any of the proposed amendments or the consent request letter for the Orvand Partners change of control.