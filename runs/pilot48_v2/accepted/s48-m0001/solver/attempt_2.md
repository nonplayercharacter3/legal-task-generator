# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Stutind Solar Installations, LLC – Zikeiv Software, Inc. License Arrangement: Issue Identification

---

## Summary

I have reviewed all ten documents in the matter folder. The signed Software License Agreement (January 15, 2026) departs materially from the negotiated Term Sheet (December 12, 2025) and the prior Licensor draft (January 6, 2026) in several respects unfavorable to Stutind. A Side Letter (June 10, 2026) further narrows Stutind's liability protections. Additionally, Stutind's August 24, 2026 notice of nonconformity regarding the Permitting Automation Module appears to be untimely under the SOW's own acceptance provisions, creating a deemed-acceptance risk that undermines Stutind's current position.

Below are the issues I have identified, in order of materiality.

---

## Issue 1: Exclusivity Covenant Dramatically Expanded Beyond Negotiated Scope

**Where:**
- Term Sheet §9 (negotiated scope)
- Prior Draft License Agreement §3.4 (reflects Term Sheet)
- Signed Agreement §3.4 (as executed)
- Order Form §4 (defines Territory)

**The Problem:**

The Term Sheet limited exclusivity to: *"Residential rooftop design software only, in Arizona and Nevada. Stutind's commercial, utility-scale and other business lines, and all jurisdictions outside Arizona and Nevada, are not covered."*

The prior draft tracked this language. The **signed** Agreement §3.4 instead provides:

> "Licensee shall not, and shall cause its Affiliates not to, **license, use, develop or procure any solar system design, permitting or proposal software** other than the Licensed Software **for any installation in the Territory**."

The Order Form defines the Territory as "the United States and Canada" (§4).

This changes the covenant in four dimensions:

| Dimension | Term Sheet / Prior Draft | Signed Agreement |
|---|---|---|
| Software type | Residential rooftop **design** software only | **Any** solar system design, permitting **or proposal** software |
| Business lines | Carve-out for commercial, utility-scale, other | **No carve-out** |
| Geography | Arizona and Nevada only | United States and Canada |
| Prohibited acts | License or procure | License, use, **develop** or procure |

**Why It Matters for Stutind:**

Stutind is a "residential and commercial solar installation contractor" (Agreement Recital B). The signed covenant prohibits Stutind from using *any* third-party design, permitting, or proposal software for *any* installation in the US or Canada—residential or commercial. It also prohibits Stutind from *developing* its own internal tools in those categories. If Stutind currently uses or wants to use other tools (e.g., a commercial design platform, an in-house proposal generator, or a permitting tool for a state outside AZ/NV), it is in breach. The 36-month Initial Term (through January 31, 2029) plus potential 36-month renewals makes this a multi-year lock-in.

**Recommended Fix:**

Amend §3.4 to restore the Term Sheet scope: limit to residential rooftop design software; carve out commercial, utility-scale, and other business lines; limit geography to Arizona and Nevada (or at minimum, the jurisdictions in SOW Schedule A plus where Stutind actually installs); and remove "develop" and "use" from the prohibited acts (retain "license" and "procure"). If Zikeiv resists, negotiate a per-jurisdiction or per-business-line exception mechanism.

**Flag:** I cannot determine from the documents alone whether Stutind currently uses or has used any other software that would constitute a present breach. The client should be asked to confirm.

---

## Issue 2: Renewal Term Changed from 12 Months to 36 Months

**Where:**
- Term Sheet §5(c)
- Signed Agreement §10.2
- Order Form §2.3
- Agreement §1.3 (order of precedence)

**The Problem:**

The Term Sheet and the Agreement both specify 12-month renewal terms. The Order Form §2.3 overrides:

> "the Subscription Term renews automatically for successive **thirty-six (36) month** renewal terms."

Under the order of precedence (Agreement §1.3), the Order Form controls. Stutind is therefore locked into 36-month renewal periods, not 12-month.

**Why It Matters:**

A 36-month renewal triples the commitment Stutind makes at each renewal. Combined with Issue 3 (narrow non-renewal window) and Issue 9 (list-price renewal fees), this significantly reduces Stutind's negotiating leverage and exit flexibility.

**Recommended Fix:**

Amend Order Form §2.3 to restore 12-month renewal terms, or at minimum negotiate a step-down (e.g., first renewal at 12 months, subsequent renewals at 24 months). Alternatively, negotiate a right to convert a 36-month renewal to three consecutive 12-month periods with annual re-pricing.

---

## Issue 3: Non-Renewal Notice Window Is Narrow and Easy to Miss

**Where:**
- Term Sheet §5(c) (60 days' notice)
- Signed Agreement §10.2 (60 days' notice)
- Order Form §2.4 (120-to-90-day window)

**The Problem:**

The Agreement provides that either party may prevent renewal by notice "at least sixty (60) days before the end of the then-current Subscription Term." The Order Form §2.4 narrows this to a specific window:

> "A notice of non-renewal is effective only if it is received **no earlier than 120 days and no later than ninety (90) days** before the last day of the Initial Term or the then-current Renewal Term."

For the Initial Term ending January 31, 2029, the window is approximately **October 3 through November 2, 2028**—a 31-day window. If Stutind's notice arrives on October 2 or November 3, it is ineffective and the term auto-renews for 36 months.

**Why It Matters:**

This is a "use it or lose it" provision with no cure. A single administrative error (wrong date, sent to wrong address, delivered late by courier) locks Stutind in for another 36 months at list price. The Agreement's notice provision (§15.1) requires delivery by hand, overnight courier, or email with confirmation—adding logistical complexity.

**Recommended Fix:**

Amend Order Form §2.4 to (a) widen the window (e.g., 180 to 60 days before term end), (b) provide that notice is effective if *sent* (not received) within the window, or (c) add a provision that if a non-renewal notice is sent within the window but not received due to carrier delay, it is nonetheless effective. Stutind should also calendar the window immediately with multiple internal reminders.

---

## Issue 4: Side Letter Eliminates Most Liability Cap Exceptions

**Where:**
- Original Agreement §12.2 (three exceptions)
- Side Letter §2 (replaces §12.2 with single exception)
- DPA §9 (DPA liability subject to Agreement §12)

**The Problem:**

Original §12.2 excluded from the liability cap and consequential damages waiver:
- (a) a Party's indemnification obligations under Section 11;
- (b) a Party's breach of Section 9 (Data Security) or Section 8 (Confidentiality); and
- (c) a Party's gross negligence or willful misconduct.

The Side Letter §2 replaces this with:

> "The limitation in Section 12.1 and the exclusion in Section 12.3 do not apply to **Licensor's obligations under Section 11.1 (Infringement Indemnity)**."

The practical effect:

| Claim Type | Before Side Letter | After Side Letter |
|---|---|---|
| Zikeiv IP infringement indemnity (§11.1) | Uncapped | Uncapped |
| Zikeiv data security breach (§9) | Uncapped | **Capped at 12 months' fees (~$312K)** |
| Zikeiv confidentiality breach (§8) | Uncapped | **Capped at 12 months' fees (~$312K)** |
| Zikeiv gross negligence / willful misconduct | Uncapped | **Capped at 12 months' fees (~$312K)** |
| Stutind's indemnity to Zikeiv (§11.3) | Uncapped | **Capped at 12 months' fees (~$312K)** |
| Consequential damages (any claim) | Excluded except as noted | **Excluded for virtually all claims** |

**Why It Matters:**

This is the single most financially dangerous change in the document set. Stutind processes homeowner personal data (addresses, property info, utility account numbers, e-signature records—see DPA Annex 1). A data breach at Zikeiv could trigger:
- Regulatory fines (state AGs, CFPB)
- Customer notification costs (mailing, call center, credit monitoring for potentially thousands of homeowners)
- Class action exposure
- Reputational harm and lost business

Under the Side Letter, Stutind's recovery for any of these is capped at approximately $312,000, and consequential damages (lost profits, reputational harm) are excluded entirely. DPA §7.4 (reimbursement of notification costs) is subject to this cap via DPA §9.

Additionally, Stutind's *own* indemnity obligation to Zikeiv (§11.3) is now capped—this is favorable to Stutind but was likely not the intended trade.

**Recommended Fix:**

Negotiate a restoration of at minimum the data security and confidentiality exceptions from original §12.2. A reasonable compromise: cap exceptions for (a) §11.1 indemnity, (b) breach of §9 (Data Security), and (c) gross negligence or willful misconduct. If Zikeiv will not budge, Stutind should require increased cyber insurance (the Agreement already requires $5M cyber—confirm the policy is in place and consider requiring additional coverage or a higher limit specifically for data breach). Stutind should also assess whether its own cyber insurance adequately covers the gap.

**Flag:** I cannot determine from the documents what consideration Stutind received for agreeing to the Side Letter's §12.2 amendment. The Side Letter couples it with a $31,200 credit and seat-charge waiver (§1), which is modest relative to the risk transferred. The client should confirm the business context of this trade.

---

## Issue 5: Assignment Made One-Way; Change-of-Control Protection Removed

**Where:**
- Term Sheet §13 (mutual consent)
- Prior Draft §15.3 (mutual consent + change-of-control termination right)
- Signed Agreement §15.3 (Licensee-only restriction)

**The Problem:**

The Term Sheet provided: "Neither party may assign without the other party's prior written consent."

The prior draft added: consent "shall not be unreasonably withheld," and a termination right for Stutind if "a provider of solar installation services acquires control of Licensor."

The **signed** Agreement §15.3 provides only:

> "**Licensee** shall not assign or otherwise transfer this Agreement... without **Licensor's** prior written consent."

There is no restriction on Licensor's ability to assign. There is no "not unreasonably withheld" standard. There is no change-of-control termination right.

**Why It Matters:**

Zikeiv can sell the contract (or be acquired) and the agreement transfers automatically to the acquirer without Stutind's consent. If a competitor of Stutind (a solar installer) acquires Zikeiv, Stutind's confidential data (pricing, customer records, pipeline, site data) would be accessible to that competitor's affiliate—subject only to the confidentiality covenant, which is now capped (see Issue 4). The prior draft specifically addressed this scenario; the signed agreement does not.

**Recommended Fix:**

Amend §15.3 to (a) make the restriction mutual, (b) add "consent not to be unreasonably withheld" for Stutind's benefit, and (c) restore the change-of-control termination right from the prior draft (at minimum for acquisition by a solar installation competitor). Alternatively, add a provision that in connection with any assignment or change of control, Zikeiv shall provide Stutind the opportunity to terminate with a pro-rata refund.

---

## Issue 6: SOW Notice of Nonconformity Appears Untimely—Deemed Acceptance Risk

**Where:**
- SOW §5.2 (10-business-day acceptance window)
- Notice Letter (dated August 24, 2026)
- Notice Letter §1.1 (Delivery Confirmation dated August 3, 2026)

**The Problem:**

SOW §5.2 provides:

> "Licensee shall give Licensor written notice of any Nonconformity within **ten (10) Business Days** after the Delivery Date. If Licensee does not give a notice of Nonconformity within that period, Deliverable D-2 is **deemed accepted** as of the last day of that period."

The Delivery Date is August 3, 2026 (a Monday). Counting 10 Business Days (excluding weekends and federal holidays; no federal holidays fall in this period):

| Business Day | Date |
|---|---|
| 1 | Tuesday, August 4 |
| 2 | Wednesday, August 5 |
| 3 | Thursday, August 6 |
| 4 | Friday, August 7 |
| 5 | Monday, August 10 |
| 6 | Tuesday, August 11 |
| 7 | Wednesday, August 12 |
| 8 | Thursday, August 13 |
| 9 | Friday, August 14 |
| 10 | **Monday, August 17** |

The notice letter is dated **August 24, 2026**—five business days after the deadline. Under the plain language of SOW §5.2, Deliverable D-2 is deemed accepted as of August 17, 2026.

The Notice Letter §3.2 attempts to override this: "Licensee does not agree that Deliverable D-2 has been accepted, whether deemed or otherwise." However, a unilateral statement cannot negate a contractual deemed-acceptance clause.

**Why It Matters:**

If D-2 is deemed accepted:
- The Milestone 2 payment event has occurred (SOW §6.1), and the $148,000 fee is due.
- Stutind's withholding position in Notice Letter §4.1 is contractually unsupportable.
- Stutind may lose the right to reject under SOW §5.4 (which requires a Nonconformity to persist "after the second redelivery"—a process that may not be available if the deliverable is already accepted).
- The warranty in SOW §10 / Agreement §13.2(a) still applies (the Module must perform in accordance with the Functional Specification), but the remedy under §13.3 is correction or termination of the SOW with refund—Stutind would need to argue that the nonconformities constitute a failure to perform in accordance with the spec, not a rejection of the deliverable.

**Recommended Fix (Immediate):**

1. **Determine whether the notice was actually received by Zikeiv on or before August 17.** The letter is dated August 24, but if it was sent by email with confirmation on or before August 17 and the date on the letter is a clerical error, Stutind may have a timing defense. Review email headers and courier receipts.
2. **If the notice was genuinely late**, immediately send a supplemental letter arguing: (a) the 10-day period is unreasonable as a matter of Delaware law given the complexity of the Module and the number of jurisdictions tested; (b) Zikeiv's own conduct (e.g., failure to provide adequate test data or environment) tolled or extended the period; or (c) Zikeiv is estopped from relying on deemed acceptance given its knowledge of the testing results.
3. **Preserve the warranty claim** under Agreement §13.2(a) and SOW §10 independently of the acceptance issue. Even if D-2 is deemed accepted, the Module's failure to conform to the Functional Specification is a warranty breach for which Stutind has a remedy under §13.3.
4. **Do not pay the $148,000** until the status of acceptance is resolved. The Notice Letter's §4.2 (disputed invoice) provides a basis for withholding under Agreement §6.4 if Zikeiv invoices.

**Flag:** This is time-sensitive. If Zikeiv has already invoiced or is about to invoice for Milestone 2, Stutind should be prepared to assert the §6.4 dispute. The client should confirm the exact date and method of delivery of the August 24 letter and whether any earlier informal communication (email, call) put Zikeiv on notice of the nonconformities before August 17.

---

## Issue 7: DPA Governed by California Law and Forum—Conflicts with Main Agreement

**Where:**
- Agreement §16.1–16.2 (Delaware law; New Castle County, Delaware forum)
- DPA §11.1–11.2 (California law; San Francisco County, California forum)
- Agreement §1.3 (DPA controls "as to Personal Data")

**The Problem:**

The DPA specifies California governing law and exclusive jurisdiction in San Francisco County. The main Agreement specifies Delaware law and New Castle County. The order of precedence gives the DPA priority "as to Personal Data."

This creates a split-regime: a single incident (e.g., a data breach) could give rise to claims governed by Delaware law (contract breach of the Agreement) and California law (DPA obligations), potentially litigated in different forums.

**Why It Matters:**

- California privacy law (CCPA/CPRA) imposes obligations and penalties that differ from Delaware contract law. Stutind may benefit from California's consumer protection framework in a data breach scenario, but also faces the complexity of litigating in two jurisdictions.
- The DPA's California forum may be more favorable to Stutind for data protection claims (California courts are experienced with privacy issues), but it adds cost and complexity.
- In practice, the issues may be intertwined (e.g., a security breach is both a §9 violation under Delaware law and a DPA violation under California law), making it unclear which forum has primary jurisdiction.

**Recommended Fix:**

This is lower priority than Issues 1–6, but Stutind should be aware of the split. If the relationship is renewed or amended, consider conforming the DPA to Delaware law/forum for administrative simplicity, or adding a provision that the main Agreement's forum clause controls for all disputes "arising out of or relating to" the relationship, with the DPA's California clause applying only to standalone data protection regulatory matters.

---

## Issue 8: Stutind Does Not Own the Permitting Automation Module It Paid $250,000 to Develop

**Where:**
- SOW §9 (incorporates Agreement §7.3)
- Agreement §7.3 (Licensor owns all modifications and enhancements)
- SOW §3.1 (detailed development scope)
- SOW §6.1 ($250,000 total SOW Fees)

**The Problem:**

SOW §9 states: "Section 7.3 of the Agreement applies to the Module and all other Deliverables." Agreement §7.3 provides: "Licensor owns all modifications and enhancements to the Licensed Software, **including any developed under an SOW**."

Stutind is paying $250,000 for the development of a module that encodes jurisdiction-specific permitting rules for 13 AZ/NV authorities—rules that Stutind's permitting staff helped define in discovery workshops (SOW §3.1(a), §4.1). Despite this, Zikeiv owns the Module. Stutind receives only a non-exclusive, non-transferable license for the Subscription Term (Agreement §3.1).

If the agreement terminates or expires, Stutind loses the Module. The jurisdiction-specific configurations, validation rules, and workflow logic that Stutind co-developed become Zikeiv's proprietary asset, potentially reusable for Stutind's competitors.

**Why It Matters:**

- Stutind's $250,000 investment produces no lasting intellectual property asset.
- On termination, Stutind must transition to a different permitting process with no ownership of the automation it funded.
- Zikeiv can offer the same (or similar) jurisdiction-specific automation to Stutind's competitors.
- The exclusivity covenant (Issue 1) means Stutind cannot simply switch to another platform during the term.

**Recommended Fix:**

Negotiate one of the following:
- **Co-ownership** of the jurisdiction-specific rule sets and configurations (with Stutind retaining an perpetual, irrevocable license to use them);
- **Perpetual license** to the Module surviving termination (at minimum for the jurisdictions in Schedule A);
- **Source code escrow** with release on termination or Chronic Failure; or
- **Data and configuration portability** right: on termination, Zikeiv delivers the jurisdiction-specific rule sets, templates, and validation logic in a usable format to Stutind.

At minimum, Stutind should negotiate a transition assistance period (e.g., 6 months of continued access post-termination) to allow re-platforming.

---

## Issue 9: Renewal Fees at Licensor's Then-Current List Price

**Where:**
- Order Form §2.3
- Order Form §3.2 (Initial Term fees fixed at $312,000/year)

**The Problem:**

The Initial Term fee is fixed at $312,000/year for 180 seats. But Order Form §2.3 provides that renewal terms are "charged at **Licensor's then-current list price** for the Licensed Software and the number of installer seats in effect at the end of the preceding term."

There is no price cap, escalation limit, or most-favored-customer provision for renewals.

**Why It Matters:**

After 36 months (or 72 months with one renewal), Stutind is subject to whatever price Zikeiv sets. In a rising-cost environment or if Zikeiv repositions HelioPlan as a premium product, Stutind could face significant fee increases with no contractual protection. Combined with the 36-month renewal term (Issue 2) and narrow non-renewal window (Issue 3), Stutind has limited ability to walk away.

**Recommended Fix:**

Negotiate a renewal price protection clause: e.g., renewal fees shall not increase by more than CPI or 5% per year, whichever is greater. Alternatively, negotiate a right to match any lower price offered to similarly situated customers. At minimum, add a provision that if the list price increase exceeds a threshold (e.g., 20%), Stutind may terminate without penalty.

---

## Issue 10: Subprocessors Not Named in DPA

**Where:**
- DPA Annex 3
- DPA §6.1–6.3

**The Problem:**

Annex 3 lists subprocessors by function only:

| Subprocessor | Function |
|---|---|
| Primary cloud hosting provider | Infrastructure hosting |
| Secondary cloud hosting provider | Backup and DR |
| Transactional email service | Notifications |
| E-signature service | Customer proposals |
| Customer support ticketing service | Ticket management |

No company names are provided. DPA §6.3 allows Stutind to object to *new* subprocessors, but Stutind cannot assess the security posture, jurisdiction, or identity of the *current* subprocessors.

**Why It Matters:**

- Stutind cannot verify that its homeowner data is being handled by reputable, secure providers.
- If a subprocessor is involved in a breach, Stutind may not know which entity to investigate or hold accountable.
- The DPA requires all subprocessors to be in the United States (§5.2), but without names, Stutind cannot confirm compliance.
- In a regulatory inquiry, Stutind may be asked to identify its data processors' subprocessors.

**Recommended Fix:**

Require Zikeiv to populate Annex 3 with actual entity names within 30 days. Add a provision that failure to identify subprocessors is a breach of the DPA. Request the most recent SOC 2 reports for each subprocessor (or at minimum the primary cloud hosting provider).

---

## Issue 11: Data Location Requirement vs. Canadian Territory

**Where:**
- DPA §5.2 (US-only storage)
- Order Form §4 (Territory includes Canada)
- DPA §1 (Applicable Data Protection Laws includes Canadian law)
- DPA Annex 1 (Data Subjects include customers)

**The Problem:**

The Territory includes Canada, meaning Stutind may onboard Canadian customers and their data into HelioPlan. However, DPA §5.2 requires all Personal Data to be stored "only in data centers located in the United States." Canadian privacy law (PIPEDA and provincial equivalents) does not prohibit cross-border data transfers per se, but requires that equivalent protection be maintained. Storing Canadian residents' data in the US is permissible under PIPEDA if the recipient provides comparable protection, but it creates a compliance burden for Stutind as the "controller."

**Why It Matters:**

If Stutind serves Canadian customers, it must ensure its privacy notices and consent processes account for US data storage. A Canadian data breach involving US-stored data could implicate both US and Canadian notification regimes. The DPA's 72-hour notification (consistent with Agreement §9.3) may not align with specific Canadian provincial requirements.

**Recommended Fix:**

Confirm with the client whether Stutind currently serves or plans to serve Canadian customers. If yes, negotiate either (a) a Canadian data residency option, or (b) a specific annex addressing Canadian privacy compliance (consent language, cross-border transfer impact assessment, etc.).

---

## Issue 12: "Develop" Added to Exclusivity Prohibited Acts

**Where:**
- Term Sheet §9 (no "develop" restriction)
- Prior Draft §3.4 (no "develop" restriction)
- Signed Agreement §3.4 (includes "develop")

**The Problem:**

The signed exclusivity prohibits Stutind from "developing" solar design, permitting, or proposal software. The Term Sheet and prior draft only restricted licensing or procuring from third parties.

**Why It Matters:**

A solar installation company may wish to build internal tools—for example, a simple spreadsheet-based proposal calculator, an internal CRM plugin, or a custom permitting checklist tool. The signed covenant could be read to prohibit even internal development of tools that fall within "solar system design, permitting or proposal software." This is overbroad and could stifle operational innovation.

**Recommended Fix:**

Carve out internal tools that are not offered to third parties and do not replicate the core functionality of HelioPlan. For example: "This Section 3.4 does not apply to software tools developed solely for Licensee's internal administrative use that do not perform solar system design, permitting package generation, or customer proposal generation as a primary function."

---

## Issue 13: Service Credits Are the Sole Monetary Remedy for Availability Failures

**Where:**
- Agreement §4.2
- Quality Agreement §5.1–5.6
- Quality Agreement §6 (Chronic Failure threshold)

**The Problem:**

Service credits are capped at 50% of the monthly fee (Quality Agreement §5.3), which is approximately $13,000/month. The maximum annual credit exposure is ~$156,000 (50% × $312,000). The Chronic Failure termination right requires either:
- 3 months below 99.5% uptime in a rolling 6-month period, OR
- 1 month below 95.0% uptime, OR
- 4+ Severity 1 incidents in 90 days.

**Why It Matters:**

If the platform experiences moderate but persistent degradation (e.g., 99.0% uptime every month), Stutind receives only a 10% credit ($2,600/month) and cannot terminate. Stutind's installers lose productivity, proposals are delayed, and permit submissions slip—but the monetary remedy is nominal. The Chronic Failure threshold is high; a single month at 94.9% triggers it, but three months at 99.4% does not (they must be within a rolling 6-month period, and 99.4% is below 99.5%, so actually three months at 99.4% *would* trigger it). Let me correct: three months below 99.5% in a rolling six-month period *does* trigger Chronic Failure. So the realistic risk is persistent uptime between 95.0% and 99.5% in fewer than three months per six-month window.

**Recommended Fix:**

Lower the Chronic Failure threshold (e.g., 2 months below 99.5% in a rolling 6-month period) or add a "cumulative downtime" trigger (e.g., total Downtime exceeding X hours in any quarter). Increase the service credit percentages. Add a right to terminate with pro-rata refund if uptime falls below 99.0% in any single month.

---

## Issue 14: SOW Repeated Failure Remedy Does Not Refund Milestone 1

**Where:**
- SOW §5.4
- SOW §6.1

**The Problem:**

If D-2 fails acceptance twice and Stutind terminates under SOW §5.4(b), the refund covers "all Fees paid under this SOW for Deliverables D-2 and D-3." The Milestone 1 fee ($62,000 for the Functional Specification) is not refunded.

**Why It Matters:**

If the Module ultimately cannot be made to conform, Stutind loses $62,000 for a specification that, while useful, has standalone value only in connection with the Module. Given that the current nonconformities (Issue 6) suggest fundamental design flaws (multi-array handling, jurisdiction-specific rules, form population logic), there is a realistic risk that two rounds of correction may not suffice.

**Recommended Fix:**

Amend SOW §5.4 to include D-1 fees in the refund, or at minimum provide that if termination occurs under §5.4, Stutind retains a perpetual license to use the Functional Specification and any jurisdiction-specific rule sets documented therein.

---

## Issue 15: Entire Agreement Clause Supersedes Term Sheet

**Where:**
- Agreement §16.4
- Term Sheet (all sections)

**The Problem:**

Agreement §16.4 states the Agreement "supersedes all prior and contemporaneous proposals, term sheets, negotiations, understandings and agreements, whether written or oral." The Term Sheet is therefore not part of the contractual framework.

**Why It Matters:**

Stutind cannot rely on the Term Sheet to argue that the exclusivity should be read narrowly, that renewals should be 12 months, or that assignment should be mutual. Under Delaware law (which governs), the parol evidence rule generally bars introduction of prior negotiations to contradict or vary the written agreement. The Term Sheet is admissible only to show ambiguity, and the signed agreement is largely unambiguous (if unfavorable).

The prior draft is similarly superseded. However, the prior draft is useful as evidence of what Stutind's counsel negotiated and what changed in the final version—potentially relevant if there is a claim of mutual mistake or if the changes were made without Stutind's awareness.

**Recommended Fix:**

No contractual fix available post-signing for this issue. However, the prior draft and Term Sheet are critical evidence for any renegotiation or dispute. Preserve them. If Stutind was not made aware of the changes between the prior draft and the signed version (exclusivity scope, renewal term, assignment, §12.2), this may support a claim of non-disclosure or, in an extreme case, rescission for fraud in the inducement—though this is a high bar under Delaware law.

**Flag:** The client should be asked: (a) who reviewed and approved the final signed Agreement versus the prior draft; (b) whether the changes in exclusivity, renewal term, and assignment were flagged internally before signing; and (c) whether there is any email or communication showing Zikeiv presented the final terms as consistent with the Term Sheet.

---

## Issue 16: No Penalty for SOW Schedule Delays

**Where:**
- SOW §6.5 (target schedule)
- SOW §4.4 (Licensee delay extends Licensor dates)

**The Problem:**

SOW §6.5 states: "Target dates are estimates. The Project Managers shall update them as the project progresses." There is no liquidated damages, service credit, or termination right tied to missing target dates. The only asymmetry is in SOW §4.4, which extends Licensor's dates if *Licensee* is delayed.

**Why It Matters:**

If Zikeiv's corrections to the Module (following the current nonconformity notice) take quarters, Stutind has no contractual lever to accelerate. The target schedule (Q3 2026 for Milestone 2) is already at risk given the August 3 delivery with six material nonconformities. Stutind's permitting operations remain manual for the 13 Schedule A jurisdictions during the correction period.

**Recommended Fix:**

Negotiate a "longstop date" for Milestone 2 acceptance (e.g., December 31, 2026), with a right to terminate the SOW and receive a full refund (including D-1) if the Module is not accepted by that date. Alternatively, add liquidated damages for each month of delay beyond the target.

---

## Issue 17: Agreement §13.4 Disclaimer May Undermine Warranty for Permitting Output

**Where:**
- Agreement §13.4
- SOW §10
- Quality Agreement §8.2

**The Problem:**

Agreement §13.4 disclaims any warranty that "permit submissions prepared using the Licensed Software will be approved by any authority having jurisdiction" and states "Licensee remains responsible for engineering review and code compliance."

SOW §10 incorporates §13.2(a) for the Module "measured against the Functional Specification as well as the Documentation." Quality Agreement §8.2 requires Zikeiv to maintain jurisdiction-specific content but adds: "This Section 8.2 does not limit Section 13.4 of the Agreement."

**Why It Matters:**

The six nonconformities in the Notice Letter (wrong field population, missing structural details, incorrect export formats, false "ready to submit" status) are precisely the type of errors that lead to permit rejection. Zikeiv could argue that §13.4 disclaims any warranty about the *accuracy* of permit output, and that Stutind is "responsible for engineering review and code compliance." However, this argument is weak where the Functional Specification explicitly requires correct form population (Acceptance Criterion 5.1), correct structural details (Criteria 4.3, 5.2), and correct export formats (Criterion 6.1). The Module's failure to meet its own Acceptance Criteria is a breach of §13.2(a) regardless of §13.4.

Still, the disclaimer creates litigation risk and may be used to argue that downstream consequences (permit rejection, resubmission costs, project delays) are not covered.

**Recommended Fix:**

Clarify that §13.4 does not limit the warranty in §13.2(a) as applied through SOW §10. Add language: "Section 13.4 does not apply to the extent the Licensed Software or any Module fails to perform in accordance with the Documentation or an approved Functional Specification."

---

## Issue 18: Side Letter Reference Customer Obligations

**Where:**
- Side Letter §3.1 (case study)
- Side Letter §3.2 (reference calls)

**The Problem:**

Stutind agreed to (a) one written case study and (b) up to four reference calls with prospective Zikeiv customers through January 31, 2027. The case study requires Stutind's written approval of final text (good). The reference calls require only "mutually convenient times" and protect against disclosure of "pricing, Licensee Data or other Confidential Information."

**Why It Matters:**

- Reference calls with *prospective* Zikeiv customers could include Stutind's competitors. Even with the confidentiality protection, a competitor could learn from the call that Stutind uses HelioPlan, the general scope of its operations, and its satisfaction level.
- The case study, even with approval rights, publicly associates Stutind with HelioPlan and may reveal operational details (number of permits processed, jurisdictions served, team size).
- These obligations are ongoing and could create friction if Stutind's experience with the software is negative (as the current SOW issues suggest).

**Recommended Fix:**

Add a right to decline any reference call if the prospective customer is a direct competitor of Stutind (i.e., a solar installer in AZ or NV). Add a right to terminate the reference obligation if the agreement is in dispute or if Stutind has given notice of non-renewal. For the case study, limit the scope to permitting workflow efficiency (not pricing, volume, or competitive positioning).

---

## Issue 19: Quality Agreement §8.2 Permits Content Obligation Is Soft

**Where:**
- Quality Agreement §8.2
- Agreement §13.4 (cross-referenced)

**The Problem:**

Quality Agreement §8.2 requires Zikeiv to "use **commercially reasonable efforts** to update" jurisdiction-specific permitting content "within thirty (30) days after an authority having jurisdiction publishes a change." The standard is "commercially reasonable efforts," not a hard obligation. And the section expressly preserves the §13.4 disclaimer.

**Why It Matters:**

If a jurisdiction changes its permit requirements and Zikeiv does not update HelioPlan Permit within 30 days (or at all), Stutind may generate non-compliant permit packages. The "commercially reasonable efforts" standard is difficult to enforce—Zikeiv can argue it allocated resources to other customers' jurisdictions first. Stutind bears the risk of permit rejection and rework.

**Recommended Fix:**

For the 13 Schedule A jurisdictions specifically, elevate the standard from "commercially reasonable efforts" to a firm obligation: "Licensor shall update jurisdiction-specific content within thirty (30) days of a published change." Add a service credit or fee abatement for each day the update is late. Cross-reference the SOW's jurisdiction list so the obligation is not limited to "jurisdictions in which Licensee installs systems" (which is broader and less precise).

---

## Issue 20: No Most-Favored-Customer or Price Protection for Additional Seats

**Where:**
- Order Form §3.3 ($1,733.33/seat/year for additional seats)
- Agreement §2.2

**The Problem:**

Additional seats above 180 are charged at $1,733.33 per seat per subscription year. This rate is fixed for the Initial Term but is not addressed for Renewal Terms. The Order Form's renewal provision (§2.3) refers to "Licensor's then-current list price for the Licensed Software and the number of installer seats in effect"—which could be read to include a different per-seat rate for additional seats at renewal.

**Why It Matters:**

If Stutind grows beyond 180 installers (plausible for a company serving 13+ jurisdictions across two states), the cost of additional seats at renewal could increase without limitation.

**Recommended Fix:**

Add to the Order Form: "The per-seat rate for additional seats shall not increase by more than [X]% per renewal term." Or: "Additional seats during any Renewal Term shall be charged at the same per-seat rate as the Initial Term."

---

## Items Flagged as Unresolvable from the Documents Alone

1. **Whether Stutind is in current breach of the exclusivity covenant (Issue 1).** The documents do not reveal what other software Stutind currently uses or has used. The client must confirm.

2. **Whether the August 24 notice was actually delivered before August 17 (Issue 6).** The letter is *dated* August 24, but the actual transmission date (email timestamp, courier receipt) is not in the folder. If it was transmitted earlier and the date is a drafting error, the analysis changes.

3. **What consideration Stutind received for the Side Letter's §12.2 amendment (Issue 4).** The $31,200 credit and seat waiver appear modest. There may be commercial context (e.g., a service failure in Year 1) not documented in the folder.

4. **Whether Zikeiv has assigned or changed control since signing (Issue 5).** No document in the folder addresses this.

5. **The current status of Zikeiv's correction efforts on the Module.** The folder ends with Stutind's notice letter. There is no response from Zikeiv, no correction plan, and no redelivery.

6. **Whether Stutind has Canadian customers in the platform (Issue 11).** The Territory includes Canada, but no document confirms actual Canadian data processing.

7. **The identity of the subprocessors listed in DPA Annex 3 (Issue 10).** Names are not provided in any document.

8. **Whether the Functional Specification (Deliverable D-1) is in the folder.** It is referenced throughout but not included. The specific Acceptance Criteria cited in the Notice Letter (4.1, 4.3, 5.1, 5.2, 6.1, 7.2) cannot be independently verified without it.

---

## Recommended Next Steps (Priority Order)

1. **Immediately:** Confirm the actual transmission date of the August 24 notice letter. If late, prepare a supplemental position paper (see Issue 6).
2. **This week:** Ask the client to confirm current software usage across all business lines and geographies to assess exclusivity breach risk (Issue 1).
3. **This week:** Request the Functional Specification (D-1) from the shared project folder to verify the Acceptance Criteria cited in the Notice Letter.
4. **Before Year 2 invoice (January 31, 2027):** Open a renegotiation dialogue with Zikeiv addressing Issues 1–5, 8, and 9. The SOW nonconformities provide natural leverage.
5. **Calendar:** Non-renewal notice window for the Initial Term: **October 3 – November 2, 2028** (Issue 3). Set multiple internal reminders.
6. **Ongoing:** Request named subprocessor identities and SOC 2 reports (Issue 10). Confirm cyber insurance certificates are current (Agreement §14.2).