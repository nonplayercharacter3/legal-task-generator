# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Date]
**RE:** Voutuv Infrastructure Partners, LLC – Acquisition of Kelthorn Thermal Systems, Inc.: Issue Identification and Recommended Revisions

---

## I. CRITICAL ISSUES

### Issue 1: Survival Period for General Representations Is ~90 Days vs. 18 Months in the LOI

**Where it appears:**
- SPA § 1.1 (definition of "Survival Date"): "the date that is sixty (60) days after delivery of the Closing Statement."
- SPA § 2.4(a): Closing Statement is due within 30 days after the Closing Date.
- SPA § 9.1: General representations and warranties survive until the Survival Date.
- LOI § 4.1: "The general representations and warranties of Seller will survive Closing for 18 months after Closing."

**Why it matters to Voutuv:**
The SPA as drafted gives the buyer approximately 90 days after closing (30 days for the Closing Statement + 60 days to the Survival Date) to discover and assert claims for breaches of any non-fundamental representation. The LOI contemplated 18 months. For a $214.5 million acquisition of a manufacturing business, 90 days is operationally insufficient to surface problems in areas such as:

- Product warranty claims (§ 4.8) – warranty issues often manifest when the first seasonal failure cycle occurs, which can be 6–12 months post-installation;
- Environmental compliance (§ 4.9) – refrigerant handling violations or permit issues may not become apparent until a regulatory audit or a new project;
- Material contract breaches (§ 4.6) – counterparty breaches or non-renewal intentions may only emerge after the buyer assumes control;
- Intellectual property (§ 4.10) – third-party infringement claims or gaps in the Transferred IP often surface during integration or when a new product line is launched.

The Fundamental Representations (organization, capitalization, brokers) survive until 60 days after the applicable statute of limitations, so those are adequately protected. But every other representation – financial statements, material contracts, customers/suppliers, product warranty, environmental, IP, litigation – falls into the 90-day window. This is a material and adverse deviation from the LOI and from market practice for a deal of this size.

**Recommended fix:**
Restore the 18-month survival period for general representations and warranties, as contemplated in the LOI. Amend the definition of "Survival Date" in § 1.1 and conform § 9.1.

**Proposed language (SPA § 1.1):**

> "**Survival Date**" means the date that is eighteen (18) months after the Closing Date.

**Proposed language (SPA § 9.1, first sentence):**

> The representations and warranties in this Agreement survive the Closing until the Survival Date; provided that the Fundamental Representations survive until sixty (60) days after the expiration of the applicable statute of limitations.

---

### Issue 2: Northvale Compute LLC Consent Is Not a Condition to Closing

**Where it appears:**
- SPA Schedule 4.6, item 1: Identifies the Northvale Compute LLC Master Supply Agreement as a Material Contract. States that the agreement "requires Northvale Compute LLC's prior written consent to any change of control of the Company. If that consent is not obtained, Northvale Compute LLC may terminate the agreement on 30 days' notice." Notes that this agreement "represented approximately 41% of the Company's revenue for fiscal year 2025."
- SPA Schedule 7.2(c) – Required Consents: Lists only the landlord consent for the Austin, Texas facility. The Northvale consent is **absent**.
- SPA § 7.2(c): Buyer's closing condition requires delivery of "each of the consents listed in Schedule 7.2(c)."
- SPA § 6.5, final sentence: "Obtaining any such consent, other than the consents listed in Schedule 7.2(c), shall not be a condition to Closing."

**Why it matters to Voutuv:**
Northvale Compute LLC is the Company's largest customer at ~41% of revenue. The SPA as drafted does not make the Northvale consent a condition to closing. Section 6.5 expressly provides that any consent not listed in Schedule 7.2(c) is not a closing condition. This means Voutuv could be compelled to close – and wire $214.5 million – without the consent of the customer that generates nearly half the Company's revenue. Post-closing, Northvale could terminate on 30 days' notice, destroying a substantial portion of the deal's value. The buyer would then have only an indemnification claim against Seller (subject to the deductible, cap, and – under Issue 1 – a 90-day survival period that may have already run).

This is the single most dangerous structural gap in the SPA.

**Recommended fix:**
Add the Northvale Compute LLC consent to Schedule 7.2(c) so that it becomes a condition to Buyer's closing obligation under § 7.2(c).

**Proposed language (SPA Schedule 7.2(c), add item 2):**

> 2. Consent of Northvale Compute LLC to the change of control of the Company resulting from the sale of the Shares, pursuant to the Thermal Systems Master Supply Agreement identified in Schedule 4.6, item 1.

Additionally, consider adding a specific closing condition in § 7.2 that the Northvale agreement remains in full force and effect and has not been terminated or given notice of non-renewal. This provides a belt-and-suspenders protection in case the consent is granted but accompanied by a termination right that is exercised before closing.

**Proposed language (SPA § 7.2, add new subsection (g)):**

> (g) the Thermal Systems Master Supply Agreement between the Company and Northvale Compute LLC identified in Schedule 4.6, item 1, shall remain in full force and effect, and neither the Company nor Northvale Compute LLC shall have delivered any notice of termination or non-renewal under that agreement.

**Facts needed from client:** Has the Northvale consent been requested? Is there any indication of Northvale's willingness to consent? Are there any side discussions or conditions Northvale has signaled? This affects whether we should also negotiate a specific form of consent or a side letter.

---

## II. SIGNIFICANT ISSUES

### Issue 3: TSA Governed by Texas Law and Harris County Jurisdiction – Split from SPA

**Where it appears:**
- TSA § 12.2: "This Agreement…shall be governed by and construed in accordance with the laws of the State of Texas…Each Party irrevocably submits to the exclusive jurisdiction of the state and federal courts located in Harris County, Texas…Sections 11.9 and 11.10 of the Purchase Agreement do not apply to this Agreement, and this Section 12.2 expressly provides otherwise for purposes of Section 11.4 of the Purchase Agreement."
- SPA § 11.9: Delaware governing law.
- SPA § 11.10: Exclusive Delaware jurisdiction.
- SPA § 11.4: Order of precedence – SPA prevails over Ancillary Agreements "unless an Ancillary Agreement expressly provides otherwise."

**Why it matters to Voutuv:**
The TSA is an Ancillary Agreement under the SPA (§ 1.1). The TSA's express carve-out in § 12.2 means that disputes over the transition services – which will be ongoing for 9 months post-closing and will involve the Company's ERP, payroll, and field-service dispatch – are litigated in Texas under Texas law, while all other deal disputes (indemnification, working capital, covenants) are litigated in Delaware under Delaware law. This creates:

- **Litigation fragmentation:** A single factual dispute (e.g., Provider's failure to perform payroll services causing employee wage-and-hour exposure) could implicate both the TSA (service failure) and the SPA (Seller's covenant to deliver the TSA at closing, or the Company's post-closing operational risk). The parties could end up in parallel proceedings in different jurisdictions.
- **Inconsistent legal standards:** Texas and Delaware law differ on issues such as the scope of implied covenants, the enforceability of liability caps, and the interpretation of "good faith."
- **Practical burden:** Voutuv, as a Delaware LLC, would need to maintain a Texas litigation presence for the 9-month TSA period.

The TSA's § 12.2 is drafted to "expressly provide otherwise" for purposes of the SPA's order-of-precedence clause (§ 11.4), so it is technically effective. But it is a poor outcome for the buyer.

**Recommended fix:**
Conform the TSA to the SPA's governing law and jurisdiction (Delaware). If there is a business reason for Texas law (e.g., the services are performed in Texas, or Provider's systems are hosted in Texas), at minimum conform the jurisdiction to Delaware to avoid split proceedings.

**Proposed language (TSA § 12.2):**

> **Governing Law; Jurisdiction.** This Agreement, and all claims, disputes and causes of action arising out of or relating to this Agreement or the Services, shall be governed by and construed in accordance with the Laws of the State of Delaware, without giving effect to any choice or conflict of law provision that would cause the application of the Laws of any other jurisdiction. Each Party irrevocably submits to the exclusive jurisdiction of the courts specified in Section 11.10 of the Purchase Agreement for any action arising out of or relating to this Agreement or the Services, and agrees not to commence any such action in any other court.

---

### Issue 4: Bill of Sale Schedule A Is Unpopulated – Buyer Cannot Verify the Transferred Assets

**Where it appears:**
- Bill of Sale, Schedule A, Part 1 (Test Equipment): All five line items have [●] for Manufacturer/Model, Serial No., and Current Location.
- Bill of Sale, Schedule A, Part 2 (Transferred IP): Patents/applications row has [●] for both title/description and registration number. Copyrights row has [●] for registration number.
- SPA § 3.2(a)(iii): Seller must deliver "evidence reasonably satisfactory to Buyer that the Bill of Sale has been executed and delivered and that the Transferred Test Assets have been transferred to the Company."
- SPA § 6.4: Seller must cause the Subsidiary to "transfer the Transferred Test Assets to the Company free and clear of all Encumbrances."
- SPA § 4.10: IP representation includes "upon delivery of the Bill of Sale, the Intellectual Property included in the Transferred Test Assets."

**Why it matters to Voutuv:**
The Transferred Test Assets are a condition to the deal's economics – the Recitals (§ C) and the IP representation (§ 4.10) both incorporate them. But with Schedule A entirely placeholder, the buyer cannot:

- Confirm the specific equipment and IP that will be transferred;
- Verify that the assets are located where represented and are in working condition;
- Confirm that the IP registrations (patents, copyrights) are valid and properly identified;
- Satisfy itself that the "evidence reasonably satisfactory" required by § 3.2(a)(iii) has been delivered.

If the Bill of Sale is executed with an empty or incomplete schedule, the transfer may be ineffective for specific assets, and the buyer's IP representation (§ 4.10) would be hollow.

**Recommended fix:**
Require that Schedule A be completed and attached as a condition to the Bill of Sale's effectiveness. Add a specific closing deliverable requiring a completed and verified Schedule A.

**Proposed language (SPA § 3.2(a), amend item (iii)):**

> (iii) the Bill of Sale, duly executed by the Subsidiary of Seller and accepted by the Company, with Schedule A thereto completed in all respects (including identification of all Test Equipment by manufacturer, model and serial number, and all Transferred IP by title and registration or application number), together with evidence reasonably satisfactory to Buyer that the Transferred Test Assets have been transferred to the Company free and clear of all Encumbrances;

**Facts needed from client:** Does the buyer's technical due diligence team have a list of the specific test equipment and IP they expect to see in the Bill of Sale? If so, we should use that list to populate Schedule A before the Bill of Sale is finalized.

---

### Issue 5: Working Capital Adjustment – Buyer Pays on Seller's Estimate at Closing with Only $2M Escrow

**Where it appears:**
- SPA § 2.2(c): At closing, Buyer pays "the Purchase Price less the amounts paid under Sections 2.2(a) and 2.2(b), plus or minus the amount by which Seller's good-faith estimate of Closing Working Capital…exceeds or falls short of Target Working Capital."
- SPA § 2.2(a): Adjustment Escrow Amount is $2,000,000.
- SPA § 2.4(d): If final Closing Working Capital is less than the estimate, "the shortfall shall be paid to Buyer from the Adjustment Escrow Amount and, to the extent the Adjustment Escrow Amount is insufficient, by Seller."
- SPA § 1.1: "Target Working Capital" means $18,750,000.
- LOI § 2.2: "a target to be agreed on the basis of Buyer's financial due diligence."
- LOI § 2.3: "A portion of the Purchase Price, in an amount to be agreed, will be deposited in escrow at Closing to secure the working capital adjustment."

**Why it matters to Voutuv:**
The structure requires the buyer to pay, at closing, an amount that reflects Seller's estimate of working capital. If Seller's estimate is $20 million (above the $18.75 million target), the buyer pays an additional $1.25 million at closing. If the true Closing Working Capital turns out to be $16 million, the buyer is owed a $4 million true-up – but only $2 million is in escrow. The remaining $2 million is an unsecured claim against Seller, subject to the indemnification limitations and (under Issue 1) the short survival period.

This creates two risks:
1. **Credit risk:** The buyer's recovery for a working capital shortfall above $2 million depends on Seller's solvency and willingness to pay.
2. **Cash flow risk:** The buyer overpays at closing based on Seller's estimate and must wait 30+ days (Closing Statement) + up to 60+ days (dispute resolution) to recover the overpayment.

The $2 million escrow is approximately 0.93% of the Purchase Price. Given that the Target Working Capital is $18.75 million, a reasonable range of working capital variation could easily exceed $2 million.

**Recommended fix:**
Two options, in order of preference:

*Option A (preferred):* Remove the at-closing working capital adjustment from § 2.2(c). Pay the fixed Purchase Price at closing (less escrow and debt payoff), and make the entire working capital adjustment a post-closing true-up. This eliminates the overpayment-at-closing risk.

*Option B (fallback):* Increase the Adjustment Escrow Amount to a level that covers a reasonable range of working capital variation (e.g., $5 million or a collar of ±$2.5 million around Target Working Capital).

**Proposed language for Option A (SPA § 2.2(c), delete the "plus or minus" clause):**

> (c) to Seller, the Purchase Price less the amounts paid under Sections 2.2(a) and 2.2(b).

Then conform § 2.4(d) to provide for a bilateral post-closing adjustment without reference to an "estimate used under Section 2.2(c)."

**Facts needed from client:** What is the basis for the $18,750,000 Target Working Capital? Was it derived from the buyer's financial due diligence as the LOI contemplated? What is the range of working capital variation the buyer's financial advisors expect? This will inform the appropriate escrow size if Option B is pursued.

---

## III. MODERATE ISSUES

### Issue 6: TSA Service Fees Are Unpopulated

**Where it appears:**
- TSA Schedule A: Monthly Service Fee for ERP, Payroll, and Field-Service Dispatch are all $[●].
- TSA § 5.1: Fees are defined as "Provider's actual cost…without mark-up."

**Why it matters to Voutuv:**
While the fee formula is defined (cost without markup), the absence of stated amounts means the Company's post-closing cost structure is uncertain. More importantly, without a stated fee, there is no benchmark against which to evaluate whether Provider's invoicing is consistent with the "cost without markup" standard. The Company (and by extension, Voutuv) would have to audit Provider's cost allocations from scratch.

**Recommended fix:**
Populate Schedule A with the monthly fees based on Provider's cost allocation for the trailing 12 months. If the parties cannot agree on specific amounts, add a mechanism for the Company to review and challenge Provider's cost calculations.

**Proposed language (TSA § 5.1, add sentence):**

> Provider shall make available to the Company, upon request and no more than once per quarter, a reasonable level of detail supporting the cost calculations underlying the Service Fees, including the allocation methodology for personnel costs, system costs and license costs.

---

### Issue 7: LOI Investment Committee Condition Not Carried into SPA

**Where it appears:**
- LOI § 7(e): "approval of the Transaction by Buyer's investment committee" is listed as a condition to closing.
- SPA Article VII: No investment committee approval condition appears.

**Why it matters to Voutuv:**
The LOI was non-binding (except § 9), so the IC condition had no legal effect. However, its omission from the SPA means Voutuv has no contractual walk-right if its investment committee has not approved the transaction. If the IC has not yet approved (or has approved subject to conditions not yet satisfied), the buyer has no formal mechanism to delay or terminate.

**Recommended fix:**
If the IC has not yet approved, add the condition back.

**Proposed language (SPA § 7.2, add new subsection):**

> (h) the Transaction shall have been approved by Buyer's investment committee.

**Facts needed from client:** Has Voutuv's investment committee approved this transaction? If yes, this point is moot. If no, or if approval is conditional, this should be added as a closing condition.

---

### Issue 8: Ostrander Freight Agreement – Auto-Renewal Notice Deadline Falls Between Signing and Closing

**Where it appears:**
- Ostrander Freight Services Agreement § 4.1: Initial Term is 3 years from March 1, 2024, i.e., through February 28, 2027.
- Ostrander Freight Services Agreement § 4.2: Auto-renews for successive 1-year periods. Either party may prevent renewal by written notice at least 90 days before the end of the then-current term.
- SPA § 6.1: Conduct of business covenant – Company must operate in the ordinary course.
- SPA Schedule 4.6, item 3: The Ostrander agreement is listed as a Material Contract.

**Why it matters to Voutuv:**
The 90-day non-renewal notice deadline is approximately November 30, 2026 (90 days before February 28, 2027). The SPA is dated September 15, 2026, and the outside date is January 15, 2027. This means the notice deadline falls during the pre-closing period when Seller still controls the Company. Seller could (i) allow the agreement to auto-renew for another year (binding the Company to Ostrander through February 2028), or (ii) give non-renewal notice (letting the agreement lapse at the end of the Initial Term). Either decision could be inconsistent with the buyer's post-closing operational plans.

The conduct of business covenant (§ 6.1) requires ordinary-course operation, but a renewal/non-renewal decision on a freight agreement is arguably within the ordinary course. The buyer should be explicit.

**Recommended fix:**
Add the Ostrander agreement renewal decision to the list of matters requiring buyer consent under § 6.1, or add it to Schedule 4.4 (No Conflicts exceptions) with a specific covenant.

**Proposed language (SPA § 6.1, add sentence):**

> Without limiting the foregoing, the Company shall not give or fail to give any notice under Section 4.2 of the Freight Services Agreement between the Company and Ostrander Freight Logistics, Inc. (identified in Schedule 4.6, item 3) without Buyer's prior written consent.

**Note:** The Ostrander agreement's § 12.3 provides that a change in ownership or control is not an assignment and does not require consent. This is favorable to Voutuv – no Ostrander consent is needed for the stock purchase itself.

---

### Issue 9: Bill of Sale IP Recordation – "Promptly" Is Indefinite

**Where it appears:**
- Bill of Sale § 4.1: "Transferor shall, on or promptly after the Effective Date, execute and deliver short-form assignments in recordable form in favor of the Company."

**Why it matters to Voutuv:**
"Promptly" has no fixed deadline. If the Transferred IP includes registered patents or copyrights (Schedule A, Part 2, items 3 and 4), failure to record the assignment could impair the Company's ability to enforce those rights against third parties or to use them as collateral. The buyer needs a definite timeline.

**Recommended fix:**

**Proposed language (Bill of Sale § 4.1):**

> To the extent any Transferred IP is registered or the subject of a pending application with any Governmental Authority, Transferor shall, on or before the fifteenth (15th) day after the Effective Date, execute and deliver short-form assignments in recordable form in favor of the Company.

---

### Issue 10: Transfer Taxes Split 50/50

**Where it appears:**
- SPA § 8.3: "All transfer, documentary, sales, use, stamp and registration Taxes incurred in connection with this Agreement shall be borne one-half by Buyer and one-half by Seller."

**Why it matters to Voutuv:**
In a stock purchase, transfer taxes (if any apply) are typically borne by the seller or by the company. A 50/50 split is not standard and imposes an unnecessary cost on the buyer. The economic impact is likely small (stock transfers generally do not trigger transfer taxes in most states, though some states impose a documentary stamp tax on stock transfers), but it is an unnecessary concession.

**Recommended fix:**

**Proposed language (SPA § 8.3):**

> All transfer, documentary, sales, use, stamp and registration Taxes incurred in connection with this Agreement shall be borne by Seller.

---

## IV. DOCUMENTS WITH NO DIRECT BEARING ON TRANSACTION DOCUMENTS

### Ostrander Freight Services Agreement

This document is an existing vendor contract of the Company, not a deal document to be negotiated as part of the transaction. It has bearing on the transaction only in the following limited respects:

1. It is identified as a Material Contract in SPA Schedule 4.6, item 3 (annual spend ~$1.4M exceeds the $1M threshold in § 4.6(b));
2. Its assignment/change-of-control provision (§ 12.3) confirms that no Ostrander consent is required for the stock purchase;
3. Its renewal timing creates the interim-period issue described in Issue 8 above.

No changes to the Ostrander agreement itself are needed or appropriate as part of the deal documents. It will be inherited by the Company (and thus by Voutuv) at closing. The buyer should be aware of its terms for post-closing operational planning, particularly the cargo liability cap (§ 7.2: $250,000 per Shipment) and the hazardous materials restriction (§ 9.2), which is relevant given the Company's use of refrigerants and coolants.

---

## V. ADDITIONAL OBSERVATIONS (LOWER PRIORITY)

### Observation A: MAE Definition Carve-Out for Industry Conditions

**Where:** SPA § 1.1, "Material Adverse Effect" definition.

The MAE definition carves out "conditions generally affecting the data center cooling industry." While the "disproportionate effect" qualifier limits this, in a sector-specific downturn (e.g., a slowdown in hyperscale data center capex), the Company could be hit by a general industry condition that is nonetheless severe. The buyer should be comfortable with this carve-out given the Company's concentration in a single end-market. No change recommended, but flag for client awareness.

### Observation B: Section 6.5 Consent Fee Proviso

**Where:** SPA § 6.5: "neither Seller nor the Company shall be required to pay any consent fee or make any concession to obtain any such consent."

If Northvale (or the landlord) demands a consent fee or economic concession as a condition of consent, Seller is not obligated to pay it. This could create a situation where a consent is effectively unobtainable on terms the counterparty requires. If the Northvale consent is added to Schedule 7.2(c) (per Issue 2), consider whether this proviso should be carved out for that specific consent.

### Observation C: TSA Liability Cap May Be Inadequate

**Where:** TSA § 9.3: Cap is "total Service Fees paid and payable under this Agreement."

If the monthly Service Fees are modest (e.g., $30,000–$50,000 per month for ERP, payroll, and dispatch), the 9-month cap could be as low as $270,000–$450,000. A data breach (carved out from the cap under § 9.3) or a gross negligence event would be uncapped, but an ordinary negligence failure (e.g., payroll error causing employee tax penalties) would be subject to the cap. The buyer should confirm the expected fee levels and assess whether the cap is adequate.

---

## VI. FACTS NEEDED FROM CLIENT

| # | Question | Relevance |
|---|----------|-----------|
| 1 | Has Voutuv's investment committee approved the transaction? | Determines whether Issue 7 requires action. |
| 2 | What is the basis for the $18,750,000 Target Working Capital? Was it derived from buyer's financial due diligence? | Informs Issue 5 (escrow sizing) and confirms LOI § 2.2 was satisfied. |
| 3 | What is the status of the Northvale Compute LLC consent? Has it been requested? Any indication of consent or conditions? | Critical to Issue 2. Affects whether a side letter or specific consent form is needed. |
| 4 | Does the buyer's technical due diligence team have a confirmed list of the test equipment and IP to be included in Bill of Sale Schedule A? | Critical to Issue 4. |
| 5 | What are the expected monthly TSA service fees? | Informs Issues 6 and 10 (TSA cap adequacy). |
| 6 | What is the expected closing date? | Affects Issue 8 (Ostrander renewal timing) and overall survival period analysis. |
| 7 | Have buyer's diligence teams (legal, financial, environmental, IP) identified any specific areas of concern that would make the 90-day survival period (Issue 1) particularly acute? | Helps prioritize and frame the survival period negotiation. |

---

## VII. SUMMARY OF RECOMMENDED ACTIONS (IN ORDER OF PRIORITY)

| Priority | Issue | Action |
|----------|-------|--------|
| 1 | Northvale consent not a closing condition | Add to Schedule 7.2(c); add § 7.2(g) |
| 2 | Survival period ~90 days vs. 18 months in LOI | Amend "Survival Date" definition; conform § 9.1 |
| 3 | TSA governed by Texas law / Harris County | Conform to Delaware law and jurisdiction |
| 4 | Bill of Sale Schedule A unpopulated | Require completed Schedule A as closing deliverable |
| 5 | Working capital paid on Seller's estimate; $2M escrow | Remove at-closing adjustment or increase escrow |
| 6 | TSA Service Fees unpopulated | Populate Schedule A; add cost transparency mechanism |
| 7 | IC approval condition dropped | Add back if IC has not approved |
| 8 | Ostrander renewal notice deadline in interim period | Add to § 6.1 consent requirements |
| 9 | Bill of Sale IP recordation "promptly" | Set 15-day deadline |
| 10 | Transfer taxes 50/50 | Shift to Seller |