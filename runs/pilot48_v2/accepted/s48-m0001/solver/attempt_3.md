# MEMORANDUM

**TO:** Partner of Record
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Stutind Solar Installations, LLC – Review of Zikeiv Software Agreement Package: Identified Issues

---

## Summary

I have reviewed all ten documents in the matter folder. I identify **fourteen issues** ranging from critical to moderate. The two most urgent are (1) a probable missed deadline for rejecting Deliverable D-2 under the SOW, which may have triggered deemed acceptance of the non-conforming Permitting Automation Module, and (2) the Side Letter's amendment to Section 12.2, which stripped most of Stutind's uncapped-liability protections. Several other provisions in the executed agreement depart materially from what the Term Sheet and prior draft negotiated, most notably the exclusivity covenant and the renewal structure.

---

## Issue 1 – Probable Deemed Acceptance of Deliverable D-2 (CRITICAL)

**Where:** SOW §5.2; Notice Letter §§1.1, 2, 3; Delivery Confirmation dated August 3, 2026 (referenced in Notice Letter §1.1).

**Analysis.** SOW §5.2 provides that Licensee must give written notice of any Nonconformity "within ten (10) Business Days after the Delivery Date," and that "[i]f Licensee does not give a notice of Nonconformity within that period, Deliverable D-2 is deemed accepted as of the last day of that period."

The Delivery Confirmation is dated **August 3, 2026 (a Tuesday)**. Counting ten Business Days after that date (excluding weekends and U.S. federal holidays per Agreement §1.1):

| Business Day | Date |
|---|---|
| 1 | Wed, Aug 4 |
| 2 | Thu, Aug 5 |
| 3 | Fri, Aug 6 |
| 4 | Mon, Aug 10 |
| 5 | Tue, Aug 11 |
| 6 | Wed, Aug 12 |
| 7 | Thu, Aug 13 |
| 8 | Fri, Aug 14 |
| 9 | Mon, Aug 17 |
| 10 | **Tue, Aug 18** |

The deadline was **August 18, 2026**. Stutind's Notice Letter is dated **August 24, 2026** – four Business Days late. On its face, D-2 was deemed accepted on August 18.

**Why it matters.** If deemed acceptance is effective:
- The Milestone 2 payment event (acceptance of D-2) has occurred, making the **$148,000** SOW fee due (SOW §6.1).
- Stutind's rejection in Notice Letter §3.1 may be a nullity.
- Stutind loses the leverage of SOW §5.4 (termination and full refund after two failed redeliveries) because the acceptance clock has already run.
- Zikeiv could argue Stutind is in breach of the payment obligation and invoke the suspension right in Agreement §6.5.

**Mitigating considerations.** Stutind's Notice Letter §3.2 expressly disclaims deemed acceptance. There may be arguments that (a) the ten-day window was unreasonable given the scope of testing across thirteen jurisdictions and multiple project types, (b) Zikeiv's substantial nonconformities constitute a repudiatory breach that overrides the deemed-acceptance mechanism, or (c) Zikeiv may be estopped from relying on the clause if it knew or should have known of the defects. However, the plain language is against Stutind, and no court has addressed whether a deemed-acceptance clause can be overridden by subsequent notice of material defects.

**Recommended fix.**
1. **Immediately** send a supplemental letter to Zikeiv acknowledging the timing issue, reiterating the Nonconformities, and asserting that the defects are so material that deemed acceptance cannot apply as a matter of law (fundamental breach / failure of condition precedent to acceptance).
2. Preserve all testing logs, screenshots, and project files referenced in the Notice Letter.
3. Do **not** pay the $148,000 invoice if one is received; the Notice Letter §4.2 already constitutes a dispute under Agreement §6.4.
4. Assess whether to request a waiver or amendment of the acceptance deadline as a condition of continuing the commercial relationship.
5. If Zikeiv insists on payment or threatens suspension, escalate to a formal demand for cure under SOW §5.3 and reserve all rights under SOW §5.4 and Agreement §10.3.

**Flag:** I cannot determine from the documents whether the Notice Letter was actually *sent* on August 24 or merely *dated* August 24. If it was sent by email earlier (e.g., August 18 or 19) but the letter is dated August 24, the analysis changes. Confirm the actual transmission date with the client.

---

## Issue 2 – Side Letter Gutted the Liability Cap Exclusions (CRITICAL)

**Where:** Side Letter §2 (amending Agreement §12.2); Agreement §§12.1, 12.2, 12.3; DPA §9.

**Analysis.** Original Agreement §12.2 excluded from both the liability cap (§12.1) and the consequential-damages waiver (§12.3):
- (a) a Party's indemnification obligations under Section 11;
- (b) a Party's breach of Section 9 (Data Security) or Section 8 (Confidentiality);
- (c) a Party's gross negligence or willful misconduct.

Side Letter §2 replaces all of the above with a single provision:

> "The limitation in Section 12.1 and the exclusion in Section 12.3 do not apply to **Licensor's obligations under Section 11.1 (Infringement Indemnity)**."

The practical effect:

| Scenario | Original §12.2 | Amended §12.2 (Side Letter) |
|---|---|---|
| Zikeiv data breach | Uncapped; consequential damages recoverable | **Capped at 12 months' fees ($312,000); no consequential damages** |
| Zikeiv confidentiality breach | Uncapped; consequential damages recoverable | **Capped; no consequential damages** |
| Zikeiv gross negligence / willful misconduct | Uncapped; consequential damages recoverable | **Capped; no consequential damages** |
| Zikeiv IP infringement indemnity | Uncapped | Uncapped (preserved) |
| Stutind's indemnity to Zikeiv (§11.3) | Uncapped | **Now capped** (favors Stutind, but asymmetry is notable) |

DPA §9 expressly subjects DPA liability to "the limitations and exclusions of liability in Section 12 of the Agreement." Therefore, a Zikeiv-caused data breach that exposes Stutind to state AG enforcement, class-action litigation, or customer attrition is recoverable only up to $312,000 in direct damages, with no lost-profits recovery.

**Why it matters.** Stutind holds Personal Data of homeowners and commercial customers (names, addresses, property/parcel data, utility account numbers, e-signature records – DPA Annex 1). A breach could trigger notification obligations under Arizona, Nevada, and potentially other state laws, regulatory penalties, and third-party claims. The $312,000 cap is likely a fraction of Stutind's actual exposure. The Side Letter also eliminates the gross-negligence carve-out, meaning even a willful security failure by Zikeiv is capped.

**Recommended fix.**
1. Negotiate a restoration of at least the data-security and confidentiality exclusions from the cap. A reasonable compromise: uncapped for breach of Section 9 and Section 8, capped (but at a higher multiple, e.g., 3× or 5× annual fees) for gross negligence.
2. If Zikeiv resists, require a corresponding increase in Zikeiv's cyber liability insurance (currently $5M per claim under Agreement §14.1(c)) and a direct right of Stutind's insurers to subrogate against Zikeiv.
3. Document the business justification for the original §12.2 language (Term Sheet §11(b) expressly contemplated these exclusions) to support a future renegotiation or, if necessary, a claim of mutual mistake or unconscionability.

**Flag:** The Side Letter is dated June 10, 2026 and appears to have been signed by Stutind's CEO (the acknowledgment block is present). I cannot determine from the documents what Stutind received in exchange beyond the $31,200 credit and the seat-charge waiver. If the client believes the §12.2 amendment was not a knowing, voluntary trade-off, there may be arguments under Arizona or Delaware law (the agreement is governed by Delaware law per §16.1) for rescission or reformation, but these are fact-intensive and I flag them for further investigation.

---

## Issue 3 – Exclusivity Covenant Massively Expanded Beyond Term Sheet (HIGH)

**Where:** Agreement §3.4; Order Form §4 (Territory); Term Sheet §9; Prior Draft §3.4.

**Analysis.** The evolution of the exclusivity obligation:

| Document | Scope of Software Restricted | Geographic Scope | Carve-outs |
|---|---|---|---|
| **Term Sheet §9** | "Residential rooftop design software only" | "Arizona and Nevada" | Commercial, utility-scale, permitting, proposal software all excluded |
| **Prior Draft §3.4** | "Residential rooftop solar design software" | "Arizona or Nevada" | Commercial, utility-scale, permitting, proposal software, and out-of-state installations all excluded |
| **Final Agreement §3.4** | "Any solar system design, permitting or proposal software" | "The Territory" (= US and Canada, per Order Form §4) | **None** |
| **Final Agreement §3.4 (added)** | — | — | Stutind must "cause its Affiliates not to" comply |

The final provision also adds the verb **"develop"**, which could be read to prohibit Stutind from building its own internal design or permitting tools.

**Why it matters.** Stutind is a residential *and* commercial solar installer (Agreement Recital B). The final covenant prevents Stutind from using any competing design, permitting, or proposal software anywhere in the US or Canada for *any* installation type – commercial, utility-scale, residential – for the entire 36-month Initial Term (and any Renewal Term). If HelioPlan's permitting module is non-functional (as the Notice Letter alleges) or if Stutind needs a different tool for a specific commercial project, Stutind is in breach.

The Territory definition in the Order Form (US and Canada) was not in the Prior Draft's Order Form definition (which listed only "subscription, seats, Fees and Subscription Term"). The final Agreement §1.1 added "Territory" to the Order Form definition, creating the link between the Order Form's broad territory and the exclusivity covenant.

**Recommended fix.**
1. Negotiate a conforming amendment to §3.4 that restores the Term Sheet scope: residential rooftop design software only, limited to Arizona and Nevada, with express carve-outs for commercial, utility-scale, permitting, and proposal software.
2. If Zikeiv will not agree, at minimum add a carve-out permitting Stutind to use alternative software where HelioPlan is materially unavailable or non-conforming for a period exceeding 30 days.
3. Remove or narrow the "develop" language to avoid restricting internal tooling.
4. Remove the affiliate extension or limit it to affiliates that actually perform solar installations in the restricted geography.

**Flag:** Because Agreement §16.4 (Entire Agreement) supersedes the Term Sheet, Stutind cannot rely on the Term Sheet to interpret §3.4. The Prior Draft is similarly superseded. The only evidence of the parties' original intent is the document trail itself. If this goes to litigation, the Prior Draft and Term Sheet would be admissible as background (not to vary the terms, but potentially to show course of dealing or to support a reformation claim if the deviation was clerical rather than substantive). Given the magnitude of the change, a court is more likely to find it was a substantive negotiation outcome.

---

## Issue 4 – Renewal Terms Changed from 12 to 36 Months at List Price (HIGH)

**Where:** Order Form §§2.3, 2.4; Agreement §10.2; Term Sheet §5(c); Prior Draft §10.2.

**Analysis.**

| Provision | Term Sheet / Prior Draft / Agreement §10.2 | Order Form §§2.3–2.4 (controls per §1.3 precedence) |
|---|---|---|
| Renewal term length | 12 months | **36 months** |
| Renewal pricing | Not specified (implied: same or negotiated) | **"Licensor's then-current list price"** |
| Non-renewal notice deadline | 60 days before term end | **Received no earlier than 120 days and no later than 90 days before term end** (a 30-day window) |

Because the Order Form has first priority under Agreement §1.3, the 36-month renewal at list price controls.

**Why it matters.**
- If Stutind misses the narrow 30-day non-renewal window, it is locked into another **36 months** (not 12) at whatever Zikeiv's list price is at that time – with no cap, no most-favored-nation protection, and no price escalation limit.
- For the Initial Term ending January 31, 2029, the non-renewal notice must be **received** between approximately **October 3, 2028** (120 days prior) and **November 2, 2028** (90 days prior). Missing this window by even one day triggers a 36-month auto-renewal.
- The list-price reset means Stutind's $312,000/year rate (negotiated for the Initial Term) provides no protection for Renewal Terms.

**Recommended fix.**
1. **Calendar the non-renewal notice window immediately** (October 3 – November 2, 2028, for the Initial Term; equivalent windows for any Renewal Term). Set internal reminders at 150 days, 130 days, and 100 days before term end.
2. Negotiate an amendment to Order Form §2.3 to restore 12-month renewal terms or, at minimum, cap renewal price increases (e.g., no more than CPI or 5% per year).
3. If Zikeiv resists, consider whether the 36-month renewal at list price, combined with the exclusivity covenant, creates an unreasonable restraint of trade under Delaware law (the governing law per §16.1). This is a long shot but worth preserving as an argument.

---

## Issue 5 – Assignment Clause Made One-Sided; Change-of-Control Protection Removed (HIGH)

**Where:** Agreement §15.3; Term Sheet §13; Prior Draft §15.3.

**Analysis.**

| Document | Assignment Restriction | Change-of-Control Right |
|---|---|---|
| Term Sheet §13 | Mutual: "Neither party may assign without the other party's prior written consent." | None |
| Prior Draft §15.3 | Mutual, with "not unreasonably withheld" qualifier. | If a solar installation provider acquires control of Licensor, Licensee may terminate within 90 days. |
| **Final Agreement §15.3** | **One-sided:** "Licensee shall not assign... without Licensor's prior written consent." No restriction on Licensor. No "not unreasonably withheld." | **Deleted.** |

**Why it matters.**
- Zikeiv can assign the agreement (e.g., in an M&A transaction) without Stutind's consent. Stutind could wake up to a new licensor – potentially a competitor or a less capable entity – with no exit right.
- The Prior Draft's change-of-control termination right specifically protected against the scenario where a solar installer acquires Zikeiv and gains access to Stutind's business data, pricing, and customer information through the combined entity. That protection is gone.
- Stutind, by contrast, cannot assign even in connection with its own M&A without Zikeiv's consent (which can be withheld for any reason or no reason).

**Recommended fix.**
1. Negotiate a restoration of mutual assignment restrictions with a "not unreasonably withheld" standard.
2. Re-insert a change-of-control termination right for Stutind, triggered if Zikeiv is acquired by (a) a solar installation company, or (b) any entity that would place Stutind's Confidential Information (including Licensee Data, pricing, and customer records) in the hands of a competitor.
3. At minimum, require Zikeiv to give Stutind 90 days' prior written notice of any assignment or change of control, with Stutind's right to terminate and receive a pro-rata refund of prepaid fees.

---

## Issue 6 – DPA Governing Law and Jurisdiction Conflict (MEDIUM)

**Where:** DPA §§11.1–11.2; Agreement §§16.1–16.2; Agreement §1.3 (Order of Precedence).

**Analysis.** The main Agreement specifies Delaware law and exclusive jurisdiction in New Castle County, Delaware. The DPA specifies **California law** and exclusive jurisdiction in **San Francisco County, California**. Agreement §1.3 gives the DPA precedence "as to Personal Data."

**Why it matters.**
- A data protection dispute (e.g., a breach of DPA obligations) is governed by California law and must be litigated in San Francisco, while a general contract dispute (e.g., payment, exclusivity, termination) is governed by Delaware law in New Castle County.
- This split creates strategic complexity: Zikeiv could forum-shop by characterizing a dispute as "relating to the processing of Personal Data" to pull it to California, or Stutind might need to file in two jurisdictions for related claims.
- California privacy law (CCPA/CPRA) imposes different and in some respects more stringent obligations than Delaware or Arizona law. The DPA's reference to "Applicable Data Protection Laws" (DPA §1) includes California law by incorporation, but the governing-law clause means California substantive law controls the DPA relationship.

**Recommended fix.**
1. Negotiate conforming governing law and jurisdiction clauses across all documents (Delaware for everything, or at minimum a unified forum for related disputes).
2. If Zikeiv insists on California for the DPA (perhaps because its privacy compliance team is based there), add a provision that permits either party to file in the other forum if the claims are "related to" or "arise out of the same transaction or occurrence as" a claim pending in the first-filed forum.

---

## Issue 7 – Subprocessors Not Identified by Name in DPA (MEDIUM)

**Where:** DPA Annex 3.

**Analysis.** Annex 3 lists five subprocessor categories by function only:
- "Primary cloud hosting provider"
- "Secondary cloud hosting provider"
- "Transactional email service"
- "E-signature service"
- "Customer support ticketing service"

None are identified by legal name. All are listed as located in the United States.

**Why it matters.**
- Stutind cannot assess the security posture, compliance history, or financial stability of the actual entities processing its customers' Personal Data.
- The subprocessor objection mechanism (DPA §6.3) is less meaningful if Stutind does not know who the subprocessors are and cannot research them.
- If a subprocessor is later identified as having a poor security record or being involved in a breach, Stutind may argue it should have been informed earlier – but the contract only requires notice of *new* subprocessors (§6.2), not periodic re-identification of existing ones.
- In a regulatory inquiry or class action, Stutind (as controller) may be asked to identify who processed the data. The DPA does not obligate Zikeiv to provide names on request.

**Recommended fix.**
1. Require Zikeiv to populate Annex 3 with the legal names of all current subprocessors as a condition of the DPA being considered fully executed.
2. Add a provision requiring Zikeiv to update Annex 3 (with names) within 30 days of any subprocessor change, not just for *new* subprocessors.
3. Add Stutind's right to request the names of all subprocessors at any time, with Zikeiv obligated to respond within 10 Business Days.

---

## Issue 8 – Data Return Format Not Adequately Specified (MEDIUM)

**Where:** Agreement §7.5; DPA §10.2.

**Analysis.** Agreement §7.5 requires Zikeiv to make Licensee Data "available for export in a commonly used machine-readable format" within 30 days after termination. The term "commonly used machine-readable format" is not defined.

**Why it matters.** Stutind's Licensee Data includes complex system designs, single-line diagrams, structural attachment details, equipment specification sheets, permit packages in jurisdiction-specific formats, CRM pipeline data, and proposal pricing (Agreement §1.1 definition of "Licensee Data"; SOW §3.1(c)). If Zikeiv exports this data as flat PDFs or generic CSVs, Stutind may be unable to re-import it into a replacement platform without significant manual rework. The 30-day export window may also be insufficient for the volume of data Stutind has accumulated over a 36-month term with 180 seats.

**Recommended fix.**
1. Negotiate a data export specification as an exhibit to the Agreement or Order Form, identifying the specific formats required for each data category (e.g., system designs in a structured format preserving array geometry, electrical parameters, and component selections; permit packages in the native AHJ file formats; CRM data in a schema-mapped CSV or API export).
2. Extend the export window from 30 to 60 days for the initial export, with Zikeiv providing incremental exports during the wind-down period.
3. Add a requirement that Zikeiv provide a data dictionary or schema documentation with the export.

---

## Issue 9 – SOW Module Ownership Creates Lock-In (MEDIUM)

**Where:** SOW §9; Agreement §7.3; Agreement §3.1.

**Analysis.** SOW §9 incorporates Agreement §7.3, which provides that "Licensor owns all modifications and enhancements to the Licensed Software, including any developed under an SOW." The Module "forms part of the Licensed Software and is licensed to Licensee under Section 3.1... for the Subscription Term at no additional subscription fee."

**Why it matters.** Stutind is paying **$250,000** (SOW §6.1) for the development of jurisdiction-specific automation logic for 13 AHJs. That logic – the rule sets, validation checks, form-population mappings, and export format handlers – is owned by Zikeiv. If the agreement terminates or expires:
- Stutind loses access to the Module (the license under §3.1 ends).
- Stutind can export its *data* (§7.5) but not the *automation logic* that transforms that data into permit-ready packages.
- Stutind would need to re-develop or re-purchase equivalent functionality from another vendor.
- The exclusivity covenant (§3.4) means Stutind cannot use a competing product during the term, so it is locked in even while the Module is non-functional.

**Recommended fix.**
1. Negotiate a perpetual, irrevocable license to the Module (or at minimum to the jurisdiction-specific configurations and rule sets) that survives termination, so Stutind can use the logic with a replacement platform.
2. Alternatively, require Zikeiv to deliver the Module's source code or a detailed technical specification of the rule sets to an escrow agent, releasable to Stutind upon termination.
3. At minimum, add a transition-services obligation requiring Zikeiv to make the Module available in read-only mode for 12 months post-termination at no charge.

---

## Issue 10 – Service Credits Are Inadequate Sole Remedy for Downtime (MEDIUM)

**Where:** Agreement §4.2; Quality Agreement §§5.1–5.6, 6.

**Analysis.** Service credits are Stutind's "sole monetary remedy for availability failures" (Agreement §4.2; Quality Agreement §5.6). The maximum credit is 50% of the monthly fee portion (Quality Agreement §5.3), which equals 50% × ($312,000 ÷ 12) = **$13,000 per month**.

Even in a worst-case scenario of total platform unavailability for an entire month (0% uptime), the credit tier is 30% (Quality Agreement §5.1), plus potential resolution-failure credits under §5.2, capped at 50% total. Stutind's actual costs of a month's downtime – idle installers, missed permit deadlines, lost customer trust, breach of Stutind's own contracts with homeowners – would far exceed $13,000.

The consequential damages exclusion (Agreement §12.3) bars recovery of lost profits or lost revenue for downtime, and the Side Letter has removed the gross-negligence carve-out that might have applied in an extreme scenario.

**Why it matters.** Stutind's entire design, proposal, and permitting workflow runs through HelioPlan. A multi-day outage during peak season (March–October) could cost Stutind tens or hundreds of thousands of dollars in delayed installations, with no contractual recovery beyond $13,000.

**Recommended fix.**
1. Negotiate an increase in the service-credit maximum (e.g., 100% of monthly fee for 0% uptime months) and add a tier for "total unavailability" (0% uptime) that triggers a pro-rata fee abatement rather than a fixed-percentage credit.
2. Carve out from the consequential damages exclusion any downtime exceeding 24 consecutive hours, allowing Stutind to recover documented direct costs (e.g., overtime pay for idle crews, expedited shipping for time-sensitive materials).
3. Strengthen the Chronic Failure threshold (Quality Agreement §6.1) to include a single month below 90% uptime, giving Stutind a termination right more readily.

---

## Issue 11 – Entire Agreement Clause Eliminates Term Sheet as Interpretive Aid (MEDIUM)

**Where:** Agreement §16.4; Term Sheet (all sections); Prior Draft (all sections).

**Analysis.** Agreement §16.4 provides that the Agreement "supersedes all prior and contemporaneous proposals, term sheets, negotiations, understandings and agreements, whether written or oral." The Term Sheet and Prior Draft are therefore not part of the contractual record.

**Why it matters.** As Issues 3, 4, and 5 demonstrate, the final agreement deviates significantly from the Term Sheet on exclusivity, renewal terms, and assignment. Because of the entire-agreement clause, Stutind cannot point to the Term Sheet to argue that the final language was a drafting error or that the parties' "true agreement" was the narrower Term Sheet version. The Prior Draft is similarly excluded.

This is not itself a "defect" in the documents – entire-agreement clauses are standard. But it means that the deviations identified in Issues 3–5 are now the operative terms, and Stutind's only recourse is to negotiate amendments or, in extremis, litigate for reformation (which requires clear and convincing evidence of a mutual mistake or fraudulent inducement – a high bar).

**Recommended fix.** No contractual fix is available post-signing without Zikeiv's agreement. The practical fix is to use the Term Sheet and Prior Draft as leverage in renegotiation: "These provisions deviate from what we agreed in the Term Sheet; please conform the agreement." If Zikeiv refuses, assess whether the deviations are material enough to support a reformation or rescission claim (fact-intensive; requires evidence of what was actually discussed and when the changes were introduced).

---

## Issue 12 – Suspension Right Could Be Triggered by the SOW Fee Dispute (MEDIUM)

**Where:** Agreement §6.5; Notice Letter §§4.1–4.2; SOW §6.2.

**Analysis.** Agreement §6.5 permits Zikeiv to "suspend access to the Licensed Software if undisputed amounts remain unpaid more than thirty (30) days after Licensee receives written notice of non-payment."

Stutind is withholding the $148,000 Milestone 2 fee (Notice Letter §4.1) and has given notice of dispute under Agreement §6.4 (Notice Letter §4.2). If Zikeiv characterizes the fee as "undisputed" (arguing that deemed acceptance occurred on August 18, per Issue 1), sends a non-payment notice, and Stutind does not pay within 30 days, Zikeiv could suspend the entire platform.

**Why it matters.** Suspension of HelioPlan would halt Stutind's design, proposal, and permitting operations for all 164 active users. Given the exclusivity covenant (§3.4), Stutind cannot switch to a competing platform while suspended – it would be in breach of the Agreement for using any alternative software, yet unable to use the licensed software.

**Recommended fix.**
1. Ensure the Notice Letter's dispute assertion (§4.2) is airtight and that Stutind continues to engage in good-faith resolution as §6.4 requires.
2. If Zikeiv sends a non-payment notice, respond immediately confirming the dispute and citing the Nonconformities. Do not allow the 30-day window to expire without a resolution or a formal extension agreement.
3. Negotiate a provision (or side letter) stating that fees subject to a good-faith dispute under §6.4 are not "undisputed amounts" for purposes of §6.5, and that Zikeiv may not suspend the platform while a dispute is pending.
4. As a contingency, prepare a short-term manual workaround for permit package assembly in case of suspension, and document it to show good faith.

---

## Issue 13 – DPA Does Not Require Zikeiv to Identify Itself as Processor in Customer-Facing Notices (LOW)

**Where:** DPA §2.3(b); DPA Annex 1.

**Analysis.** DPA §2.3(b) makes Stutind responsible for "giving any notices to Data Subjects that Applicable Data Protection Laws require." Some state privacy laws (e.g., the Nevada Privacy Law, the Arizona Privacy Act if enacted) may require that a business's privacy policy identify its service providers or the categories of third parties with whom it shares personal data.

**Why it matters.** If Stutind's privacy policy must list Zikeiv (or its subprocessors) as a service provider, but the DPA does not obligate Zikeiv to provide that information or to cooperate in drafting the notice, Stutind may be in compliance difficulty. This is a minor operational issue but could become material if a state AG inquires.

**Recommended fix.** Add a DPA provision requiring Zikeiv to (a) identify itself and its subprocessors in a format suitable for inclusion in Stutind's privacy policy, and (b) provide reasonable cooperation in responding to any regulator inquiry about the processing relationship.

---

## Issue 14 – No Price Protection or Most-Favored-Customer Clause for Renewals (LOW)

**Where:** Order Form §2.3.

**Analysis.** Order Form §2.3 states that Renewal Term fees are "at Licensor's then-current list price." There is no cap on price increases, no most-favored-customer provision, and no right to match a lower price offered to a comparable customer.

**Why it matters.** Over a potential 36-month Renewal Term, Zikeiv could increase list prices by any amount. If Stutind's 180 seats are repriced at, say, $250,000 per 100 seats (a 39% increase), the annual fee jumps to $450,000. Combined with the exclusivity covenant and the narrow non-renewal window, Stutind has limited leverage to resist.

**Recommended fix.**
1. Negotiate a price escalation cap for Renewal Terms (e.g., not to exceed the greater of CPI or 3% per year).
2. Add a most-favored-customer clause: if Zikeiv offers a lower per-seat rate to a solar installer of comparable size (100+ seats) in the same geography during a Renewal Term, Stutind is entitled to the same rate.
3. Alternatively, lock the per-seat rate for the Initial Term plus one Renewal Term.

---

## Items I Cannot Resolve from the Documents Alone

| # | Item | What I Need |
|---|---|---|
| A | **Actual transmission date of the Notice Letter.** The letter is dated August 24, 2026, but was it sent by email on that date or earlier? If sent on or before August 18, the deemed-acceptance issue (Issue 1) may not arise. | Email headers or courier receipt showing the date the notice was actually transmitted. |
| B | **Circumstances of the Side Letter negotiation.** Was the §12.2 amendment a knowing trade for the $31,200 credit, or was it presented as a "housekeeping" amendment? Were there emails or calls discussing the liability change? | Communication records from May–June 2026 between Stutind and Zikeiv regarding the Side Letter. |
| C | **Whether the Order Form's 36-month renewal and narrow non-renewal window were discussed.** The Term Sheet and Prior Draft both specify 12-month renewals with 60-day notice. If the 36-month/120-90-day structure was inserted without Stutind's awareness, there may be a reformation argument. | Drafting history of the Order Form; email correspondence between January 6 and January 15, 2026. |
| D | **Stutind's actual data volumes and formats.** To assess the adequacy of the 30-day export window and the "commonly used machine-readable format" standard, I need to know what data Stutind has loaded and in what formats. | A data inventory from Stutind's IT Manager (Tom Hadley). |
| E | **Whether Stutind has any Affiliates** that perform solar installations. The final §3.4 extends exclusivity to Affiliates. If Stutind has no Affiliates, this is moot; if it does, the scope of the covenant is broader than apparent. | Corporate structure information. |
| F | **Zikeiv's identity as subprocessors.** To assess Issue 7, I need to know who the actual subprocessors are. If any are well-known entities with public security track records, the risk is lower. | Request from Zikeiv under DPA §8.3 (security questionnaire) or a direct ask. |

---

## Priority Action Items

1. **Today:** Confirm the actual send date of the August 24 Notice Letter. If it was sent after August 18, prepare a supplemental assertion of rights (Issue 1).
2. **This week:** Send a letter to Zikeiv's General Counsel raising the Side Letter §12.2 amendment as a material change that Stutind did not fully appreciate, and requesting restoration of the data-security and confidentiality exclusions from the cap (Issue 2).
3. **This week:** Calendar the non-renewal notice window (October 3 – November 2, 2028) and set internal alerts (Issue 4).
4. **Next 30 days:** Open a renegotiation dialogue covering Issues 3, 4, 5, 8, 9, and 10. Package these as a "conforming amendments" request tied to the Term Sheet.
5. **Ongoing:** Do not pay the $148,000 Milestone 2 fee until the acceptance dispute is resolved. Maintain good-faith communication per Agreement §6.4 (Issue 12).