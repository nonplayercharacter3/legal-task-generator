# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Dribas Brewing Company, LLC – Brikon Systems Software License: Issue Identification and Recommendations

---

## Summary

I have reviewed all seven documents in the matter folder. The most urgent issue is that Dribas's termination notice (the "August Notice") appears to have been delivered outside the contractual window in the Side Letter, which Brikon has disputed. If the termination is ineffective, Dribas is locked into a three-year agreement with an exclusivity covenant significantly broader than what the Term Sheet contemplated, a new uncapped indemnity obligation running to Brikon, and a drafting error that likely subjects Brikon's IP infringement indemnity to the liability cap. I have identified twelve issues, prioritized below.

---

## Issue 1 – Termination Notice Delivered Outside the Contractual Window

**Where:** Side Letter §2.2; Amendment No. 1, Recital C and §6.1

**The problem.** Side Letter §2.2 provides that the Termination Notice must be "delivered no later than thirty (30) days after the Acceptance Deadline." The Acceptance Deadline is June 30, 2026 (Side Letter §2.1). Thirty days after June 30 is **July 30, 2026**. Amendment No. 1, Recital C states that the August Notice was "delivered to Licensor on August 14, 2026"—fifteen days after the deadline. Brikon disputed the effectiveness of the notice by letter dated August 28, 2026 (Recital C). Amendment §6.1 confirms the dispute is unresolved.

**Why it matters.** This is the threshold question. If the Termination Right was not validly exercised, Dribas remains bound by the Agreement for the full Initial Term (through January 14, 2029) and is obligated to pay all subscription and implementation fees. Dribas has already paid the $16,000 signature milestone and the $96,000 annual subscription fee (invoiced in advance per Agreement §3.2). The Side Letter's refund provisions (§3.1) and transition assistance (§3.4) are all triggered only "if Licensee exercises the Termination Right."

**Possible arguments for Dribas (and their strengths):**

- *Waiver / course of dealing.* Brikon did not raise the timeliness issue until August 28—fourteen days after receiving the notice—and then entered into Amendment No. 1 (September 15) which contemplates continued performance and a BIM Remediation Plan. A court could find that Brikon waived strict compliance by its conduct. This is the strongest argument but fact-dependent.
- *Substantial compliance.* The notice was only fifteen days late and was unambiguous in its terms. Delaware courts generally enforce contractual deadlines strictly, so this argument is weaker.
- *Equitable estoppel.* If Dribas can show it relied on some representation by Brikon that the deadline was extended or that the notice would be accepted, estoppel may apply. I see no evidence of such a representation in the folder.

**Recommended fix.**

1. Immediately assess the strength of the waiver argument with a Delaware litigation attorney. The Amendment's recitals and the parties' conduct between August 14 and September 15 are the key facts.
2. If the waiver argument is strong, consider referring the dispute to the escalation procedure under Amendment §6.4 and Agreement §14.1 to create a record of Brikon's continued acceptance of performance.
3. If the waiver argument is weak, evaluate whether to (a) litigate the termination question, (b) negotiate a settlement (e.g., Brikon agrees to a mutual termination with a reduced refund), or (c) perform under the Agreement and seek to mitigate damages through the BIM Remediation Plan and service credits.
4. In all scenarios, preserve the argument that Dribas's entry into Amendment No. 1 was without prejudice (as stated in Amendment §5.7) and do not take any further action that could be characterized as affirming the Agreement.

**Priority: CRITICAL.** This determines whether Dribas is in or out of the contract.

---

## Issue 2 – Liability Cap Cross-Reference Error in Restated Section 10

**Where:** Amendment No. 1 §3 (restating Agreement §10); Agreement §11.3(a)

**The problem.** The original Agreement §11.3(a) carved out "a party's obligations under Section 10.1" from the liability cap in §11.2. In the original Agreement, §10.1 was Brikon's IP infringement indemnity to Dribas—so the indemnity was uncapped, which protected Dribas.

Amendment No. 1 §3 deletes and replaces Section 10 in its entirety. In the restated Section 10:
- **§10.1** is now the *Licensee Indemnity* (Dribas indemnifying Brikon for regulatory data claims).
- **§10.2** is now the *Infringement Indemnity* (Brikon indemnifying Dribas for IP claims).

The Amendment does not update the cross-reference in §11.3(a). As a result:
- §11.3(a) now reads "a party's obligations under Section 10.1"—which refers to **Dribas's** indemnity to Brikon. This means Dribas's regulatory indemnity is uncapped (Brikon can recover unlimited amounts from Dribas).
- Brikon's IP infringement indemnity (now §10.2) is **no longer expressly carved out** from the cap. It appears to be subject to the 12-month fees cap in §11.2 (approximately $96,000–$114,000 depending on timing).

**Why it matters.** If a third party brings an IP infringement claim against Dribas based on the BrewLedger software, Brikon's indemnity obligation may be capped at roughly one year of fees. For a serious infringement claim (e.g., a patent covering brewery scheduling algorithms), that cap could be far below Dribas's actual exposure. Meanwhile, Dribas's new indemnity to Brikon for regulatory matters is uncapped.

**Recommended fix.**

1. Raise this with Brikon's counsel as a drafting error and seek a conforming amendment to §11.3(a) to reference "Section 10.2" (or both §10.1 and §10.2, depending on the commercial intent).
2. If Brikon resists, argue that the plain intent of the original §11.3(a) was to carve out the IP indemnity from the cap, and that the renumbering in the restated Section 10 was mechanical. Delaware courts look to the parties' intent, and the Term Sheet §11.3(a) expressly carved out "Brikon's IP infringement indemnity."
3. Do not sign any further amendments or order forms without first correcting this cross-reference.

**Priority: HIGH.** This is a latent exposure that will only become acute if an IP claim arises, but it is a clear drafting error that should be fixed now while the parties are in a cooperative (if disputed) posture.

---

## Issue 3 – Exclusivity Covenant Dramatically Broader Than Term Sheet

**Where:** Agreement §2.5 and Schedule A.7; Term Sheet §§5.1–5.2

**The problem.** The Term Sheet agreed to a narrow exclusivity:

> "Dribas will agree that, during the Term, it will not license or use **production-scheduling software** other than BrewLedger **at Licensee's Wilmington and Dover breweries only**." (Term Sheet §5.1)

> "Dribas will remain free to select, license, use and develop software of its choice for all other functions and at all other locations. These include its **taproom point-of-sale, distributor and sales management, accounting, and raw material and finished goods inventory systems**. The covenant will **bind Dribas only, and not its Affiliates**." (Term Sheet §5.2)

The executed Agreement §2.5 provides:

> "Licensee shall not, and **shall cause its Affiliates not to**, license, use or develop **any brewery management, inventory, point-of-sale or distribution software** other than the Licensed Software, **anywhere in the world**. Licensee shall use the Licensed Software as its **system of record** for the functions it supports."

This is broader in four dimensions:

| Dimension | Term Sheet | Executed Agreement |
|---|---|---|
| Software categories | Production-scheduling only | Brewery management, inventory, POS, distribution |
| Geographic scope | Wilmington and Dover only | Anywhere in the world |
| Affiliates | Not bound | Bound |
| System of record | Not mentioned | Expressly required |

Schedule A.7 confirms the 20% discount was given "in consideration of the covenant in Section 2.5"—so Brikon will argue the broader covenant is the bargained-for consideration.

**Why it matters.** If Dribas (or any Affiliate) uses a different POS system at its taprooms, a different inventory management tool for raw materials, or any distribution software at any location, it is in breach of §2.5. A material breach gives Brikon the right to terminate under §12.2 (which would forfeit Dribas's termination rights and refund claims) or to claim damages. The "system of record" language further requires Dribas to route all supported functions through BrewLedger, even if a third-party tool would be more suitable.

**Recommended fix.**

1. Inventory all software currently used by Dribas and its Affiliates for brewery management, inventory, POS, or distribution functions. Identify any that fall within the §2.5 restriction.
2. If any current systems are caught, negotiate a carve-out with Brikon (e.g., a side letter or amendment listing permitted legacy systems with a phase-out date).
3. If the termination dispute (Issue 1) is resolved in Dribas's favor, this issue becomes moot. If Dribas remains in the Agreement, this is the most significant ongoing compliance risk.
4. Brief management and the Board on the scope of the covenant so that no new software is procured without legal review.

**Priority: HIGH.** This is a continuing obligation that could trigger a material breach at any time.

---

## Issue 4 – New Licensee Indemnity to Brikon (Regulatory Claims)

**Where:** Amendment No. 1 §3, restated §10.1

**The problem.** The original Agreement contained only one indemnity: Brikon's IP infringement indemnity to Dribas (§10.1). The Term Sheet §10 contemplated only that indemnity. Amendment No. 1 adds a new **Licensee Indemnity** requiring Dribas to defend and indemnify Brikon against any claim by a third party or governmental/regulatory authority arising from:

(a) any label, formula, statement of composition or other Regulatory Submission Data that Dribas submits;
(b) any filing Dribas makes to a regulatory authority using output of the Licensed Software; or
(c) Dribas's failure to comply with laws governing the production, labeling, advertising, distribution or sale of alcoholic beverages.

The exclusions in restated §10.3 protect Dribas to the extent the claim arises from an Error in the software, Brikon's breach, or Brikon's alteration of data. But the base obligation is broad: if the TTB or Delaware ABC brings an enforcement action related to a label or formula that Dribas submitted through BrewLedger, Dribas must defend and indemnify Brikon.

**Why it matters.** Alcohol regulatory enforcement can carry significant penalties (fines, seizure, license suspension). Brikon is a software company with limited assets in a regulatory dispute; Dribas is the regulated entity. The indemnity effectively makes Dribas Brikon's insurer for regulatory risk. Combined with Issue 2 (the cap cross-reference error), Dribas's indemnity is uncapped while Brikon's IP indemnity may be capped.

**Recommended fix.**

1. Assess whether the indemnity is commercially reasonable. The exclusions for software Errors and Brikon's breach provide some protection, but they place the burden on Dribas to prove the claim arose from a software defect rather than from Dribas's own data or filing decisions.
2. Negotiate a mutual cap on the Licensee Indemnity (e.g., limited to the fees paid in the 12 months preceding the claim, or a fixed dollar amount), or at minimum clarify that the indemnity does not extend to punitive or exemplary fines imposed on Brikon.
3. Ensure Dribas's compliance team understands that any regulatory submission made through the LFC Module triggers this indemnity. Implement internal review procedures so that submissions are accurate before they are made.
4. Confirm that Dribas's existing insurance (including any regulatory liability or professional liability coverage) responds to this indemnity obligation. The Board Consent §8.5 directed a review of the insurance program—confirm whether that review addressed this new exposure.

**Priority: HIGH.** This is a new, uncapped financial obligation that was not in the original deal.

---

## Issue 5 – DPA Governed by New York Law in New York Courts

**Where:** DPA §§12.1–12.2; Agreement §15.1; Term Sheet §13.1

**The problem.** The main Agreement is governed by Delaware law with exclusive jurisdiction in New Castle County, Delaware (Agreement §15.1). The Term Sheet §13.1 contemplated only Delaware law and New Castle County courts. But DPA §§12.1–12.2 provide that the DPA is governed by **New York law** with exclusive jurisdiction in **New York County, New York**.

Under the order of precedence (Agreement §15.6), the DPA ranks above the main Agreement. So for any dispute arising under the DPA (data protection obligations, subprocessor issues, breach notification), the parties must litigate in New York under New York law. For all other disputes, they litigate in Delaware under Delaware law.

**Why it matters.**

- **Cost and complexity.** Dribas will need New York counsel for any data protection dispute, in addition to Delaware counsel for commercial disputes.
- **Inconsistent outcomes.** A single factual scenario (e.g., a data breach caused by a software defect) could implicate both the DPA (breach notification, security obligations) and the main Agreement (warranty, service levels, termination). The parties could end up with parallel proceedings in different jurisdictions applying different laws.
- **Strategic disadvantage.** Brikon is a Delaware corporation headquartered in Wilmington. Requiring Dribas to litigate data disputes in New York imposes a home-court disadvantage on Dribas that was not contemplated in the Term Sheet.

**Recommended fix.**

1. Seek an amendment to DPA §12 to conform the governing law and forum to Delaware, consistent with the main Agreement and the Term Sheet. Frame it as a conforming correction.
2. If Brikon resists (its standard DPA form likely uses NY law for all customers), at minimum negotiate a provision that permits Dribas to bring a data protection claim in Delaware when it is ancillary to a claim under the main Agreement.
3. If the termination dispute (Issue 1) is resolved in Dribas's favor and the relationship ends, this issue becomes less urgent but still relevant for the data return/deletion period (DPA §11, Agreement §7.8).

**Priority: MEDIUM-HIGH.** Not immediately actionable but should be raised in any renegotiation.

---

## Issue 6 – Amendment No. 1 May Lack Required Board Authorization

**Where:** Board Consent §§2.1, 9.3(c); Amendment No. 1 (executed September 15, 2026)

**The problem.** The Board Consent of January 12, 2026 approved the License Agreement, Side Letter, and DPA "substantially in the form presented." Section 9.3(c) reserves to the Board prior approval for "any amendment of the License Agreement, the Side Letter or the DPA that **increases the Company's financial commitment**, extends the Term or limits the Company's rights."

Amendment No. 1:
- Adds the LFC Module with $18,000/year subscription fees and $12,000 implementation fees (increases financial commitment).
- Adds a new Licensee Indemnity obligation (limits Dribas's rights / increases its exposure).
- Does not extend the Term, but the continued performance obligation during the termination dispute (Amendment §6.3) has the practical effect of extending Dribas's commitment.

There is **no evidence in the folder** of a subsequent Board consent or resolution approving Amendment No. 1. The Amendment was signed by Elena V. Dribas as CEO and Managing Member on September 15, 2026.

**Why it matters.**

- If the LLC Agreement requires Board approval for amendments that increase financial commitments (as the Board Consent contemplates), the Amendment may not be validly authorized. This could give Dribas an argument that the Amendment is void or voidable—potentially undoing the new indemnity, the LFC Module fees, and the continued-performance obligation.
- Conversely, Brikon could argue that Elena Dribas, as Managing Member and an Authorized Officer under Board Consent §9.1, had authority to sign the Amendment under the general authority in §9.2, and that Brikon was entitled to rely on that authority (Board Consent §9.4 permits third-party reliance on certificates of authority).
- The internal governance issue could also create friction among the Members (Elena Dribas, Jonas Dribas, and Harbor Lane Brewing Investors, LLC).

**Recommended fix.**

1. Review the LLC Agreement to confirm the exact approval requirements for amendments to material contracts.
2. If Board approval was required and not obtained, convene the Board to ratify the Amendment (if the commercial terms are acceptable) or to reject it (if Dribas wishes to argue the Amendment is unauthorized).
3. Be cautious about asserting the Amendment is unauthorized as a litigation strategy: it would also undo the BIM Remediation Plan (Amendment §5), the LFC Module (which Dribas wants), and the reservation of rights language (Amendment §6) that preserves Dribas's termination position.
4. Document the analysis for the file in case the authorization question becomes relevant in the termination dispute.

**Priority: MEDIUM.** An internal governance issue that could become externally relevant if the termination dispute is litigated.

---

## Issue 7 – Continued Payment Obligation During Termination Dispute

**Where:** Amendment No. 1 §§6.2–6.3; Agreement §§3.2, 14.3

**The problem.** Amendment §6.3 requires each Party to "continue to perform its obligations under the Agreement" pending resolution of the termination dispute. Agreement §3.2 requires annual subscription fees to be invoiced "annually in advance, beginning on the Effective Date and on each anniversary of the Effective Date." The second anniversary invoice (due January 15, 2028) will fall while the dispute is likely still unresolved if it goes to litigation.

Additionally, the LFC Module implementation fee milestone of $6,000 was due on signature of Amendment No. 1 (Amendment §4.3), and the $18,000 LFC subscription fee will be invoiced on Acceptance of the LFC Module (Amendment §4.2).

**Why it matters.** Dribas is contractually obligated to keep paying while arguing it should have been able to terminate. If the dispute resolves in Brikon's favor, these payments are owed. If it resolves in Dribas's favor, Dribas will need to claw them back—adding complexity to any refund claim.

**Recommended fix.**

1. Pay all undisputed invoices when due to avoid giving Brikon an independent termination right for non-payment (Agreement §12.2) or a suspension right (§3.5).
2. For any invoice that Dribas believes should not be paid because the Agreement has terminated, use the disputed-amounts procedure in §3.4: notify Brikon in writing of the dispute and the basis before the due date, and pay the undisputed portion.
3. Track all payments made after August 14, 2026 in a separate ledger to facilitate a refund claim if the termination is upheld.

**Priority: MEDIUM.** A practical cash-flow and preservation issue.

---

## Issue 8 – "System of Record" Obligation Not in Term Sheet

**Where:** Agreement §2.5 (last sentence)

**The problem.** The executed Agreement requires Dribas to "use the Licensed Software as its system of record for the functions it supports." This language does not appear in the Term Sheet. Combined with the broad exclusivity in §2.5 (see Issue 3), it means Dribas cannot maintain parallel or backup systems for any supported function without potentially breaching the Agreement.

This creates tension with:
- Board Consent §7.1, which directs management to keep legacy systems operational until BIM Acceptance (parallel operation is protected by Side Letter §4.6, but only "until the BIM is Accepted at a Site").
- The practical reality that Dribas may want to maintain its own spreadsheets as a backup.

**Why it matters.** If the BIM is never Accepted (and the termination dispute fails), Dribas is required to use BrewLedger as its system of record for all supported functions—but the BIM is not working. Dribas could be in breach of §2.5 for maintaining legacy systems as its true system of record, even though Side Letter §4.6 protects parallel operation only until Acceptance.

**Recommended fix.**

1. Seek clarification from Brikon that "system of record" does not prohibit maintaining backup or archival copies of data in other formats (which Board Consent §7.3 already contemplates).
2. If the BIM is not Accepted and the termination dispute fails, negotiate a provision that allows Dribas to maintain its legacy systems as a fallback until the BIM is remediated, without constituting a breach of §2.5.

**Priority: MEDIUM.** Becomes acute only if the termination fails and the BIM remains unaccepted.

---

## Issue 9 – Employee/Data Subject Notices May Not Have Been Delivered

**Where:** Board Consent §4.3; DPA §3.3

**The problem.** Board Consent §4.3 directed the Director of Operations to prepare and deliver notices to employees and contractors "before the Company's Authorized Users begin live use of the BrewLedger Platform." DPA §3.3 makes Licensee responsible for providing any notices and obtaining any consents required under Applicable Data Protection Law.

There is no evidence in the folder that these notices were prepared or delivered. The DPA's Recital B identifies the categories of personal data processed (employee names, credentials, shift records, distributor contacts, taproom customer details).

**Why it matters.** Under the Delaware Personal Data Privacy Act (referenced in DPA §1.2), a Controller must provide notice to individuals whose personal data is being shared with a service provider. If Dribas failed to provide this notice before employees' data was entered into BrewLedger, Dribas may be in violation of state privacy law. This is Dribas's own compliance obligation (DPA §3.3), but a violation could give employees a private right of action or draw regulatory attention.

**Recommended fix.**

1. Confirm with Rachel Steen (Director of Operations) whether employee notices were delivered before live use began.
2. If not, deliver them immediately. The Delaware PDPA does not have a private right of action for notice failures, but the Delaware Attorney General can enforce, and the gap could be raised in any data breach investigation.
3. Document the delivery in the compliance file.

**Priority: MEDIUM.** A compliance housekeeping item that could become significant if a data breach occurs.

---

## Issue 10 – Lender Notice Under Revolving Credit Facility

**Where:** Board Consent §5.4

**The problem.** The Board directed the Controller to "confirm, before the License Agreement is executed, whether the Company's revolving credit facility requires notice to or consent from the lender for the Company's entry into the Transaction Documents. If notice or consent is required, the Controller shall give or obtain it."

There is no evidence in the folder that this confirmation was made or that any notice was given. The Agreement was executed January 15, 2026; the Board Consent is dated January 12, 2026—only three days' window.

**Why it matters.** If the credit facility contains a restricted payments or material contracts clause requiring notice or consent for contracts above a certain threshold, and no notice was given, Dribas may be in technical default under the credit facility. This could give the lender the right to accelerate the loan or impose other remedies. The total annual commitment ($96,000 subscription + potential LFC Module fees + implementation costs) may or may not exceed the facility's threshold.

**Recommended fix.**

1. Confirm immediately with Jonas Dribas (CFO/Controller) whether the lender notice was given.
2. If not, review the credit facility agreement for the applicable threshold and give notice promptly. Most facilities cure technical defaults if notice is given before the lender demands action.
3. If the Amendment No. 1 increased the commitment above the threshold, confirm whether a supplemental notice is required.

**Priority: MEDIUM.** A technical default risk that is inexpensive to cure if caught early.

---

## Issue 11 – LFC Module Timeline Is Non-Binding

**Where:** Amendment No. 1 §2.6

**The problem.** Amendment §2.6 requires Brikon to use "commercially reasonable efforts" to deliver the LFC Module readiness notice by December 15, 2026. This is not a hard deadline with termination or refund consequences. Compare with the BIM, which had a firm Acceptance Deadline (June 30, 2026) backed by the Termination Right in the Side Letter.

**Why it matters.** Dribas is paying $6,000 (50% of the LFC implementation fee) on signature of the Amendment and will pay another $6,000 on Acceptance, plus $18,000/year in subscription fees. If Brikon misses the December 15 target, Dribas has no termination right and no specific remedy short of arguing material breach under §12.2 (which requires a 30-day cure period and a showing that the failure is "material"). A missed "commercially reasonable efforts" target is unlikely to constitute a material breach.

**Recommended fix.**

1. Add the LFC Module to the key-dates calendar maintained under Board Consent §6.5.
2. If the December 15, 2026 target is missed, document the delay and raise it at the next quarterly service review (Amendment §7.3 requires BIM Remediation Plan review at these meetings; extend the same discipline to the LFC Module).
3. In any future amendment or order form, seek a firm acceptance deadline with termination rights for the LFC Module, mirroring the Side Letter's approach for the BIM.

**Priority: LOW-MEDIUM.** The LFC Module is newer and less critical than the BIM, but the lack of enforcement leverage is worth noting.

---

## Issue 12 – Side Letter Target Dates for BIM Readiness Notices Were Missed (Non-Binding)

**Where:** Side Letter §4.2; Amendment No. 1, Recital B

**The problem.** Side Letter §4.2 set target dates for BIM Readiness Notices: Wilmington by April 30, 2026; Dover by May 15, 2026. The actual dates were May 22, 2026 (Wilmington) and June 19, 2026 (Dover)—22 and 34 days late, respectively. Side Letter §4.2 expressly states these are "planning targets" and that "Licensor's failure to meet them is not, of itself, a breach."

**Why it matters.** While not independently actionable, the missed targets are relevant evidence in the termination dispute (Issue 1). They show a pattern of delay by Brikon that contributed to the BIM not being Accepted by the June 30 deadline. If Dribas argues waiver or estoppel based on Brikon's conduct, the missed targets support the narrative that Brikon knew or should have known the Acceptance Deadline would be missed and did not take adequate steps to protect Dribas's termination right (e.g., by notifying Dribas of the risk under Side Letter §6.3, which requires notice within five business days of becoming aware of a circumstance that will prevent Acceptance by the deadline).

**Recommended fix.**

1. Determine whether Brikon gave a delay notice under Side Letter §6.3 before June 30, 2026. If it did not, this strengthens Dribas's waiver/estoppel argument: Brikon had a contractual duty to warn Dribas of the risk to the Acceptance Deadline and failed to do so.
2. Preserve all project communications (weekly status reports under Side Letter §6.1, steering meeting minutes under §6.2) as evidence of Brikon's knowledge of the delay.
3. Use the missed targets as leverage in any settlement negotiation: Brikon's own conduct contributed to the missed deadline, and its failure to give a §6.3 delay notice arguably waived strict compliance with the §2.2 notice window.

**Priority: MEDIUM.** Supporting evidence for Issue 1 rather than an independent claim.

---

## Additional Observations

**A. Board Consent §9.3(a) – Termination Notice Requires Board Approval.**
The Board Consent reserves to the Board the approval of "a notice of termination of the License Agreement given by the Company, other than a termination limited to a single Module." The August Notice terminated the Agreement in its entirety. There is no evidence in the folder of a Board resolution authorizing the August Notice. If the termination is challenged, Brikon could argue the notice was not validly authorized. However, Board Consent §9.3 provides that "where the Chief Executive Officer determines that a notice must be given before the Board can reasonably act, the Chief Executive Officer may give the notice after consulting the Company's counsel and at least one other member of the Board." Given the 30-day window (which closed July 30), the CEO likely acted under this emergency provision. Confirm that the consultation requirement was met and document it.

**B. DPA Annex 2 – Fieldline Integration Partners.**
Fieldline Integration Partners, LLC is listed as a Subprocessor with on-site access at the Breweries for BIM integration work, with "access to Authorized User and operator records limited to the period of on-site work." Confirm that Fieldline's personnel signed confidentiality agreements and complied with Dribas's site safety and sanitation rules (Side Letter §5.3). If Fieldline's engagement has ended, confirm that Brikon obtained deletion certification from Fieldline under DPA §11.3.

**C. Agreement §15.12 – Publicity.**
Brikon may identify Dribas as a customer "in a non-public list provided to prospective investors or acquirers under confidentiality obligations." Given the current dispute, confirm that Brikon is not using Dribas as a reference or case study. If Brikon is in a fundraising or M&A process, Dribas's name on a customer list could be commercially sensitive while the parties are in dispute.

---

## Recommended Next Steps (Prioritized)

| # | Action | Owner | Timing |
|---|---|---|---|
| 1 | Assess waiver/estoppel arguments re: late Termination Notice; obtain Delaware litigation counsel opinion | Outside litigation counsel | Immediate |
| 2 | Confirm whether Brikon gave a Side Letter §6.3 delay notice before June 30, 2026 | Rachel Steen / file review | Immediate |
| 3 | Confirm CEO consulted counsel and a Board member before giving the August Notice (Board Consent §9.3) | Elena Dribas | Immediate |
| 4 | Inventory all software used by Dribas and Affiliates for brewery management, inventory, POS, or distribution; identify §2.5 compliance gaps | IT / Operations | 2 weeks |
| 5 | Review LLC Agreement re: Amendment authorization; determine if Board ratification is needed | Corporate counsel | 2 weeks |
| 6 | Confirm lender notice under credit facility was given | Jonas Dribas (CFO) | 1 week |
| 7 | Confirm employee/data subject notices were delivered before live use | Rachel Steen | 1 week |
| 8 | Raise §11.3(a) cross-reference error with Brikon's counsel; seek conforming amendment | Outside counsel | Next negotiation touchpoint |
| 9 | Raise DPA governing law/forum with Brikon's counsel | Outside counsel | Next negotiation touchpoint |
| 10 | Add LFC Module December 15, 2026 target and all other key dates to the Board Consent §6.5 calendar | Rachel Steen | 1 week |
| 11 | Preserve all project communications, weekly reports, and steering meeting materials | Rachel Steen / legal hold | Immediate |
| 12 | Review Dribas's insurance program for coverage of the new Licensee Indemnity (Amendment §10.1) | Jonas Dribas / broker | 30 days |

---

*This memorandum is based solely on the seven documents in the matter folder. It does not address facts outside those documents (e.g., the content of weekly status reports, the LLC Agreement, the credit facility, or the BrewLedger Functional Specification). Recommendations should be validated against the full factual record before action is taken.*