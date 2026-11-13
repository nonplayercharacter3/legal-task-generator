# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Lalais Medical Systems / Trasirt Holdings — Transaction Document Risk Assessment

---

## SUMMARY

I have reviewed the Stock Purchase Agreement (SPA), the Bill of Sale for service tooling (current and prior draft), and the Transition Services Agreement (TSA). I identify **thirteen issues** that create material exposure for Lalais, ranked by severity. The three most urgent are: (1) the Kestrevo sole-source detector consent is missing from the closing conditions; (2) FDA and product liability representations survive only 90 days post-closing, co-terminous with the escrow release; and (3) the TSA permits Trasirt to delegate all services—and disclose all Recipient Confidential Information—to any third party without Lalais's consent.

Items requiring client input before we respond to Trasirt are flagged at the end.

---

## ISSUE 1 — Kestrevo Change-of-Control Consent Not a Closing Condition

**Documents and Sections:**
- SPA § 4.5 (No Conflicts; Consents) — carves out matters "set forth on Schedule 4.6"
- SPA Schedule 4.6(a)(iii) — identifies the Detector Supply Agreement with Kestrevo Sensors GmbH; notes that § 14.2 of that agreement requires Kestrevo's prior written consent for a change of control, "failing which Kestrevo may terminate the Detector Supply Agreement on written notice"
- SPA Schedule 7.2(d) (Required Third-Party Consents) — lists **only** the Westbridge Facility Lease consent
- SPA § 7.2(d) — makes listed consents a condition to Buyer's obligation to close

**Why It Matters:**
Kestrevo is the **sole source** of flat-panel detectors for the Company's mobile C-arm product line (SPA Schedule 4.6(a)(iii)). If Kestrevo terminates the Detector Supply Agreement post-closing, the Company cannot manufacture its flagship products. The consent is disclosed in the Schedule 4.6 carve-out to the no-conflicts representation, so Trasirt is on notice that it is required. Yet it is omitted from Schedule 7.2(d), meaning it is **not a closing condition**. Lalais could be obligated to close without it, then face termination of its sole-source supply.

**Recommended Fix:**
Add the Kestrevo consent to Schedule 7.2(d) as a second item:

> 2. Consent of Kestrevo Sensors GmbH, as supplier under the Detector Supply Agreement dated September 15, 2022, to the change of control of the Company resulting from the transactions contemplated by this Agreement.

If Trasirt resists making it a hard closing condition (e.g., if Kestrevo has indicated it may condition consent on terms), an alternative is to add it as a condition with a long-stop date fallback: if consent is not obtained by [date], Buyer may terminate without penalty and recover expenses. But the primary ask should be inclusion in Schedule 7.2(d).

---

## ISSUE 2 — FDA and Product Liability Representations Survive Only 90 Days

**Documents and Sections:**
- SPA § 9.1(a) — general survival: 18 months post-closing
- SPA § 9.1(b) — survival for § 4.12 (Product Liability; Recalls) and § 4.14 (FDA and Regulatory Compliance): "until the Escrow Release Date"
- SPA § 2.4(b) — Escrow Release Date defined as 90 days after the Closing Date

**Why It Matters:**
For a medical device company, 90 days is an dangerously short window. FDA Form 483s from routine inspections, 510(k) deficiency letters, product liability claims from pre-closing incidents, and latent design defects can all surface well after 90 days. Because the survival period expires on the same date the escrow is released, Lalais has **neither escrow security nor indemnity rights** for any FDA or product liability issue that emerges after day 90. The only remaining recourse would be a direct claim against Trasirt for fraud (SPA § 9.4(c)), which is a high bar.

Compare: Fundamental Representations survive until 60 days after the applicable statute of limitations (SPA § 9.1(c)), which for tax and organizational matters can be years.

**Recommended Fix:**
Amend SPA § 9.1(b) to provide:

> (b) The representations and warranties in Section 4.12 (Product Liability; Recalls) and Section 4.14 (FDA and Regulatory Compliance) shall survive the Closing until the earlier of (i) 18 months after the Closing Date and (ii) 60 days after the expiration of the applicable statute of limitations for the underlying claim.

If Trasirt insists on a shorter period, the absolute floor should be 12 months, and the escrow release date should be decoupled from the survival period (i.e., extend the escrow holdback for claims under § 4.12 and § 4.14 beyond 90 days).

**Client Input Needed:** Confirm whether any FDA inspections are scheduled in the near term and whether there are any open 510(k) communications or MDR trends that would make the 90-day window particularly risky.

---

## ISSUE 3 — TSA Permits Unilateral Delegation and Broad Disclosure to Delegates

**Documents and Sections:**
- TSA § 13.2 (Assignment) — "Provider may assign this Agreement, or delegate the performance of any Services, in whole or in part, to **any Person** without the consent of Recipient."
- TSA § 9.3 (Permitted Disclosures) — "Provider may also disclose Recipient Confidential Information to its permitted assignees and delegates under Section 13.2, to the extent needed for them to perform the Services."
- TSA § 1.1 (Definition of "Recipient Confidential Information") — includes "installed-base service records, Customer site data, equipment configuration and service history, service firmware and diagnostic software, complaint and service event records"

**Why It Matters:**
Trasirt can hand the entire transition services operation to any third party—potentially a competitor of Lalais or an underqualified provider—without notice or consent. That third party would then have lawful access to all of the Company's service firmware, diagnostic software, customer data, and complaint records. There is no requirement that the delegate be bound by confidentiality obligations equivalent to TSA § 9 (though § 9.3 implies it, the delegation right in § 13.2 does not condition delegation on the delegate's agreement to be bound). There is no termination right for Recipient if it objects to a particular delegate.

This is particularly acute because the non-compete in SPA § 6.8 carves out TSA performance, meaning Trasirt (and by extension its delegates) is actively servicing the Company's products during the transition. A delegate with access to service firmware and diagnostic software could gain deep technical knowledge of the product line.

**Recommended Fix:**
Amend TSA § 13.2 to add:

> Provider may assign this Agreement, or delegate the performance of any Services, in whole or in part, to any Person **only if** (a) the assignee or delegate is an Affiliate of Provider or a professional services firm with demonstrated experience in medical device field service, (b) the assignee or delegate agrees in writing to be bound by confidentiality and data protection obligations no less protective than Sections 8 and 9 of this Agreement, and (c) Provider gives Recipient at least fifteen (15) Business Days' prior written notice identifying the proposed assignee or delegate. Recipient may object to any proposed assignee or delegate on reasonable grounds, in which case Provider shall not make the assignment or delegation.

Also add to TSA § 9.3: "Provider shall ensure that any assignee or delegate to whom it discloses Recipient Confidential Information is bound by written confidentiality obligations no less protective than this Section 9."

---

## ISSUE 4 — TSA Indemnification Excludes Ordinary Negligence

**Documents and Sections:**
- TSA § 11.1 (Indemnification by Provider) — covers third-party claims "to the extent caused by Provider's **gross negligence**, willful misconduct, breach of Section 8.3 or Section 9, or violation of Applicable Law"
- TSA § 11.3 (Exclusion of Consequential Damages) — bars indirect, consequential, special or punitive damages and lost profits
- TSA § 11.4 (Cap) — aggregate liability capped at total Monthly Service Fees (~$4,920,000)

**Why It Matters:**
The Company services CT and MRI equipment in hospital settings. A field service error arising from **ordinary negligence**—a miscalibrated phantom, a misdiagnosed fault code, a missed preventive maintenance step—could result in patient injury or equipment damage. Under the current TSA, Provider's indemnification is triggered only by gross negligence or willful misconduct. For ordinary negligence, Recipient's sole remedy is a direct damages claim, which is subject to the consequential damages exclusion (§ 11.3) and the ~$4.92M cap (§ 11.4). A serious patient injury claim could exceed the cap, and the consequential damages exclusion could bar lost revenue from equipment downtime.

**Recommended Fix:**
Amend TSA § 11.1 to lower the threshold:

> Provider shall indemnify Recipient, the Company and their respective directors, officers and employees against all Losses arising from third-party claims to the extent caused by Provider's **negligence**, willful misconduct, breach of Section 8.3 or Section 9, or violation of Applicable Law in performing the Services.

If Trasirt resists, at minimum add an exception to the consequential damages exclusion (§ 11.3) for bodily injury or death claims:

> The exclusion in this Section 11.3 shall not apply to Losses arising from personal injury or death.

---

## ISSUE 5 — TSA Performance Standard Is Backward-Looking and Lacks SLAs

**Documents and Sections:**
- TSA § 3.2(b) — services must be provided with "substantially the same scope, priority, quality, timeliness and level of care as the corresponding services were provided to the Business during the **12 months before the Closing Date**"
- TSA Schedule A — describes services in general terms but specifies no response times, uptime percentages, dispatch windows, or first-time-fix rates

**Why It Matters:**
The benchmark is whatever the pre-closing service level was. If the Business's technical support hotline had a 4-hour response time before closing, that becomes the contractual standard—even if it's inadequate for hospital customers. There are no objective SLA metrics, no service credits for missed targets, and no reporting requirements. For a company whose customers are hospitals relying on imaging equipment for patient care, ambiguous service levels create operational risk and customer dissatisfaction that could erode the installed-base revenue stream Lalais is acquiring.

**Recommended Fix:**
Add a new TSA § 3.6 (Service Levels):

> **3.6 Service Levels.** Provider shall meet the following minimum service levels during the Term:
> (a) Technical support hotline: response within 30 minutes during business hours;
> (b) Remote service platform: 99.5% monthly uptime;
> (c) Field service dispatch: engineer on-site within 4 business hours for critical failures (equipment down), 2 business days for non-critical;
> (d) Preventive maintenance: completed within 5 business days of scheduling;
> (e) Complaint forwarding: within 1 Business Day (or 24 hours for reportable events) as required by Section 3.3.
>
> If Provider fails to meet a service level in any calendar month, Recipient shall be entitled to a service credit equal to [5]% of the Monthly Service Fee for each missed level, capped at [20]% of the Monthly Service Fee per month.

**Client Input Needed:** What were the actual pre-closing service levels? If they were strong, the backward-looking benchmark may be acceptable as a floor, but specific SLAs should still be added for enforceability.

---

## ISSUE 6 — Bill of Sale Allows Seller to Retain Electronic Service Manuals Indefinitely

**Documents and Sections:**
- Bill of Sale § 3.2 (Electronic Materials) — after delivering complete copies, Seller may "retain only such copies as Seller needs to perform the Transition Services Agreement **or to comply with applicable Law**"
- Prior Draft Bill of Sale § 3.2 — required only delivery of complete copies; contained **no** retention right
- TSA § 9.5 (Confidentiality Survival) — 5 years general; indefinite for trade secrets, service firmware, and Customer data

**Why It Matters:**
The current Bill of Sale is a material change from the prior draft. It gives Trasirt a continuing right to retain service manuals, field modification instructions, and service bulletins—documents that constitute the technical knowledge base for servicing the Company's products. The "to comply with applicable Law" language is undefined and potentially perpetual. Even after the TSA expires (12 months), Trasirt could argue it needs to retain the manuals for legal compliance. Combined with the non-compete carve-out for TSA performance (SPA § 6.8(a)), this gives Trasirt a prolonged foothold in the Company's technical documentation.

**Recommended Fix:**
Amend Bill of Sale § 3.2 to add:

> After delivery, Seller may retain copies solely to the extent necessary to perform the Transition Services Agreement during its Term. Within thirty (30) days after expiration or termination of the Transition Services Agreement, Seller shall certify in writing that it has deleted or destroyed all retained copies, except those required by Applicable Law, and shall identify any such legally required copies and the specific Law requiring retention. Seller's retention right under this Section 3.2 shall in no event extend beyond the expiration of the Transition Services Agreement plus thirty (30) days, other than for copies required by Applicable Law.

---

## ISSUE 7 — No Representations in the Bill of Sale Regarding Asset Condition

**Documents and Sections:**
- Bill of Sale § 6 — "The representations, warranties, covenants and indemnities of Seller in the Stock Purchase Agreement are not enlarged or diminished by this Bill of Sale."
- Bill of Sale (entire document) — contains no representations or warranties from Seller regarding the Transferred Assets
- SPA § 4.8 (Title to Assets; Sufficiency) — covers title and overall sufficiency but not condition
- SPA § 4.10 (Intellectual Property) — covers ownership/right to use, not completeness or currency of service manuals

**Why It Matters:**
Lalais is acquiring physical tooling (torque drivers, calibration fixtures, HV diagnostic sets, kVp/mAs meters), calibration phantoms, and service manuals. There is no representation that:
- The tooling is in working order and not damaged or worn beyond usefulness;
- The calibration phantoms are currently within their calibration intervals (expired phantoms are worthless for quality assurance);
- The service manuals are complete, current, and include all revisions and field modification instructions;
- The diagnostic software on the service laptops is the latest version.

If the phantoms are out of calibration or the tooling is worn, the Company's ability to perform quality-assured service is compromised, and the cost to replace specialized medical imaging calibration equipment is non-trivial.

**Recommended Fix:**
Add a new Bill of Sale § 1.4:

> **1.4 Seller's Representations.** Seller represents and warrants that, as of the Effective Date: (a) the Transferred Assets are in good working order and condition, normal wear and tear excepted; (b) all calibration phantoms are within their current calibration intervals and accompanied by valid calibration certificates; (c) the service manuals, field modification instructions and service bulletins transferred hereunder are complete and include all revisions issued as of the Effective Date; and (d) the diagnostic and service software loaded on the service laptops is the latest version released by the Company as of the Effective Date.

This representation should be covered by the SPA's indemnification (Article 9) and survival provisions.

---

## ISSUE 8 — TSA Third-Party System Consents Are Only "Commercially Reasonable Efforts"

**Documents and Sections:**
- TSA § 3.5 — "Provider shall use **commercially reasonable efforts** to obtain, at its own cost, any consents from third-party licensors or vendors of the Provider Systems that are required for Provider to provide the Services"
- TSA § 3.1 — Provider shall provide the Services (unconditional obligation)

**Why It Matters:**
The Provider Systems (ERP platform, remote service platform, dispatch and ticketing systems) are owned or licensed by Trasirt or its Affiliates. If a key licensor (e.g., the ERP vendor or the remote connectivity platform provider) refuses to consent to post-closing use by the Company, Provider's obligation under § 3.5 is only to use "commercially reasonable efforts"—not to actually obtain the consent. Yet § 3.1 imposes an unconditional duty to provide the Services. The result is a potential conflict: Provider may be unable to perform § 3.1 through no fault of its own, but § 3.5 does not give Recipient a termination right or fee abatement if consents are not obtained.

**Recommended Fix:**
Amend TSA § 3.5 to add:

> If Provider is unable to obtain any such consent that is necessary to provide a Service, Provider shall notify Recipient in writing within five (5) Business Days. If the consent remains unobtained for more than thirty (30) days after the Closing Date, Recipient may, at its option: (a) terminate the affected Service without penalty, with a pro-rata refund of fees paid for that Service; or (b) require Provider to use its own systems or arrange alternative hosting at no additional cost to Recipient.

---

## ISSUE 9 — Deductible Operates as a True Deductible, Not a Tipping Basket

**Documents and Sections:**
- SPA § 9.4(a) — Seller not liable "until the aggregate amount of all Losses under that Section exceeds $932,500 (the 'Deductible'), **after which Seller shall be liable only for Losses in excess of the Deductible**"

**Why It Matters:**
The first $932,500 of post-closing losses is borne entirely by Lalais. In a medical device business, a single product liability settlement or an FDA consent decree could generate $1M+ in losses, but Lalais absorbs the first $932,500. A "tipping basket" (or "threshold") structure—where once losses exceed the threshold, all losses from dollar one are recoverable—would be significantly more favorable.

**Recommended Fix:**
Amend SPA § 9.4(a):

> (a) Seller shall not be liable under Section 9.2(a), other than for breaches of Fundamental Representations, unless the aggregate amount of all Losses under that Section exceeds $932,500 (the "Threshold"), after which Seller shall be liable for **all** Losses under that Section from the first dollar.

If Trasirt resists a full tipping basket, a compromise is a "shared threshold" where Lalais bears the first 50% of losses up to the Threshold and 100% above it, or the Threshold is reduced.

---

## ISSUE 10 — Bill of Sale Scope Depends on Undelivered Asset Register

**Documents and Sections:**
- Bill of Sale Schedule A, Part 1, item 5 — "Service laptops loaded with Company diagnostic and service software, assigned to the field service personnel listed in **the asset register delivered by Seller to Buyer before the Closing**"
- Bill of Sale Schedule A, Part 1, item 6 — "Specialized CT and MRI service tooling held at Seller's regional depots … **as identified in that asset register**"
- Prior Draft Schedule A, Part 1 — same items with note: "[*Note to Draft: Quantities to be confirmed against Seller asset register.*]"

**Why It Matters:**
The scope of at least two categories of Transferred Assets is defined by a document that has not yet been delivered. If the asset register is incomplete, inaccurate, or delivered late, Lalais could close without knowing the full extent of what it is receiving. The CT and MRI service tooling (gantry alignment fixtures, RF coil test fixtures, helium-level service tooling) is specialized and expensive to replace. An incomplete register could mean the Company is left without critical service capability for its installed base.

**Recommended Fix:**
Add to Bill of Sale § 3.1:

> Seller shall deliver the asset register to Buyer no later than ten (10) Business Days before the Closing Date. If the asset register is not delivered by that date, or if it is materially incomplete, Buyer may postpone the Closing until the register is delivered and verified, without penalty.

Also add to SPA § 3.2(b) or as a new closing condition in § 7.2: delivery of the asset register in form and substance satisfactory to Buyer.

**Client Input Needed:** Has the asset register been delivered? If so, has it been reviewed for completeness?

---

## ISSUE 11 — TSA Data Security Standard Is Vague; No Explicit HIPAA or FDA Data Integrity Requirement

**Documents and Sections:**
- TSA § 8.3 — safeguards "no less protective than those Provider applied to the corresponding data of the Business before the Closing, and no less than **reasonable industry standards**"
- TSA § 1.1 (Definition of "Applicable Law") — includes FDA regulations at 21 C.F.R. Parts 803, 806 and 820, but does not expressly reference HIPAA, HITECH, or state privacy laws
- TSA § 1.1 (Definition of "Recipient Confidential Information") — includes "Customer site data, equipment configuration and service history, complaint and service event records"

**Why It Matters:**
Service records for CT and MRI equipment in hospital settings may contain patient-identifiable information (e.g., patient name or ID in service tickets, imaging parameters tied to a specific patient's exam). If so, HIPAA applies. The TSA's data security standard ("reasonable industry standards") does not explicitly require HIPAA compliance or FDA data integrity standards (21 C.F.R. Part 11 for electronic records). A data breach of patient information would trigger regulatory exposure for the Company (now owned by Lalais) that the TSA's indemnification may not fully cover (see Issue 4).

**Recommended Fix:**
Amend TSA § 8.3 to add:

> Where Recipient Data includes protected health information as defined by the Health Insurance Portability and Accountability Act of 1996 (HIPAA), Provider shall comply with all applicable requirements of HIPAA and the HITECH Act, and the parties shall execute a Business Associate Agreement in the form attached hereto as Exhibit B. Where Recipient Data includes electronic records subject to 21 C.F.R. Part 11, Provider shall maintain those records in compliance with that Part.

---

## ISSUE 12 — No Termination Right or Remedy if Provider's Delegation Degrades Service

**Documents and Sections:**
- TSA § 13.2 — Provider may delegate to any Person without consent (see Issue 3)
- TSA § 12.1 — termination only for material breach with 30-day cure period
- TSA § 3.2(b) — performance standard is "substantially the same" as pre-closing

**Why It Matters:**
Even if we fix the delegation right (Issue 3), there is no specific remedy if a delegate's performance is inferior. Recipient would need to establish a "material breach" under § 12.1, which requires the performance to fall below the § 3.2(b) standard. Given the vagueness of that standard (Issue 5), this is a high bar. The 30-day cure period further delays any remedy.

**Recommended Fix:**
In addition to the fixes in Issues 3 and 5, add to TSA § 12.1:

> For purposes of this Section 12.1, a material breach includes: (a) Provider's failure to meet the service levels in Section 3.6 for two consecutive months; (b) Provider's delegation of Services to a Person not approved under Section 13.2; or (c) Provider's failure to cure a data security incident under Section 8.3 within 48 hours of discovery.

---

## ISSUE 13 — SPA § 4.8 Sufficiency Representation Is Undermined by TSA Termination

**Documents and Sections:**
- SPA § 4.8 — assets "together with the assets transferred under the Bill of Sale and the services provided under the Transition Services Agreement, are sufficient for the continued conduct of the Business"
- TSA § 12.1–12.2 — either party may terminate for breach or insolvency
- SPA § 9.2(a) — indemnity for breach of representations

**Why It Matters:**
The sufficiency representation is expressly predicated on the TSA services continuing. If the TSA is terminated early (e.g., Provider insolvency under TSA § 12.2, or Provider material breach under § 12.1), the basis for the § 4.8 representation collapses. Technically, the representation was true at closing (the TSA was in effect), so it may not be "breached." But Lalais is left without the services it was told were necessary for the Business to function, and without a clear indemnity trigger.

**Recommended Fix:**
Add to SPA § 9.2 a new clause:

> (d) any failure of the Transition Services Agreement to be performed in accordance with its terms for a period exceeding thirty (30) days after the Closing Date, whether by reason of termination, Provider insolvency, or otherwise, to the extent such failure results in the Business being unable to continue in substantially the same manner as before the Closing.

Alternatively, add a TSA covenant requiring Provider to use commercially reasonable efforts to ensure the Services continue for the full Term regardless of any assignment or delegation, and a specific indemnity in the TSA for early termination caused by Provider.

---

## ITEMS REQUIRING CLIENT INPUT BEFORE WE RESPOND TO TRASIRT

1. **Kestrevo relationship status.** Has Trasirt requested Kestrevo's consent? Has Kestrevo responded? If Kestrevo has signaled it may impose conditions (e.g., a supply price increase or exclusivity expansion), we need to understand that before agreeing to make it a closing condition.

2. **FDA inspection calendar.** Are any FDA inspections (routine or for-cause) scheduled for the Company in the next 12 months? Any open 483s or warning letters not reflected in Schedule 4.14(c)? This directly affects the urgency of Issue 2.

3. **Pre-closing service levels.** What were the actual response times, uptime, and dispatch windows for the remote service platform, hotline, and field service in the 12 months before signing? This determines whether the TSA § 3.2(b) benchmark is a floor we can live with or whether we need to negotiate higher SLAs.

4. **Asset register.** Has the asset register referenced in Bill of Sale Schedule A been delivered? If so, please provide it for review. If not, we should make its delivery a condition precedent to closing.

5. **Patient data in service records.** Do the Company's service tickets, complaint files, or remote diagnostic logs contain patient-identifiable information? If yes, we need to confirm HIPAA applicability and negotiate the BAA (Issue 11).

6. **Trasirt's ERP and remote platform vendors.** Who are the third-party licensors of the Provider Systems? Are there known change-of-control or data-use restrictions in those licenses? This affects Issue 8.

---

## ITEMS I COULD NOT RESOLVE FROM THE DOCUMENTS ALONE

- The content of the **Disclosure Schedule** beyond the excerpts provided (Schedules 4.6, 4.14(b), and 7.2(d) are shown; Schedules 4.15, 4.14(c), and any other schedules are not). There may be additional disclosed exceptions that affect the analysis.
- The **Facility Lease** itself (only the change-of-control provision is described in Schedule 4.6(a)(ii)). I cannot confirm whether the landlord's consent is subject to conditions or whether the lease has other provisions (e.g., rent escalation, expansion rights) that interact with the transaction.
- The **Detector Supply Agreement** with Kestrevo (only the change-of-control provision is described). I cannot confirm the term, pricing, volume commitments, or whether Kestrevo has termination rights other than the change-of-control trigger.
- The **escrow agreement** (referenced in SPA § 2.4 but not provided). The mechanics of claim resolution and release may contain additional protections or gaps.
- The **asset register** (referenced in Bill of Sale Schedule A but not provided).