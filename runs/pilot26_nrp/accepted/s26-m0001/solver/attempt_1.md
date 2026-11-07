# MEMORANDUM

**To:** [Partner]
**From:** [Associate]
**Date:** [Current Date]
**Re:** Poseirt Commerce Logistics, LLC – Master Services Agreement, Order Form No. 1, and Service Level Schedule: Issue Identification and Recommended Revisions

---

## Executive Summary

I have reviewed the Poseirt MSA, Order Form No. 1, the Service Level Schedule, and (for context) the Kelvane fabric testing agreement. The Poseirt package contains several provisions that, as drafted, leave Seinon materially exposed. The three most serious issues are: (1) the Order Form's exclusivity clause is dramatically broader than the MSA's and locks Seinon into Poseirt for *all* fulfillment *worldwide* across *all channels*; (2) the Service Level Schedule makes service credits Seinon's *sole and exclusive remedy* for any service failure, including Security Incidents, and directly overrides the MSA's carve-out that would have left Security Incidents uncapped; and (3) the governing law and venue provisions conflict between the MSA (Delaware) and the Order Form (New York). Several other issues compound these risks. I flag items 1–4 below as requiring client input before we respond to Poseirt.

---

## Issue 1: Exclusivity Scope – Order Form §4 vs. MSA §2.4

**Where:** Order Form No. 1, Section 4; MSA, Section 2.4.

**What it says:**

- MSA §2.4: "Customer will use Provider as its exclusive provider of **direct-to-consumer e-commerce fulfillment** of Seinon products **shipped to the United States and Canada**."
- Order Form §4: "Customer will use Provider as its exclusive provider of **all fulfillment, warehousing and logistics services** for **all Seinon products in all sales channels worldwide**, including direct-to-consumer e-commerce, **wholesale distribution and retail-store replenishment**. Customer will not engage, and will cause its **Affiliates** not to engage, any third party to provide those services during the term of this Order Form."

**Why it matters:** Per MSA §1.3 (Order of Precedence), the Order Form controls over the MSA. The operative exclusivity is therefore the Order Form's version, which is orders of magnitude broader. It would prohibit Seinon from using any other 3PL for wholesale distribution, retail replenishment, or international shipping for the entire 60-month term (plus any renewal). It also extends the restriction to Affiliates. For a company that designs, manufactures, and sells technical outdoor apparel, this likely means Seinon cannot use a second or regional warehouse, cannot have a different partner handle its wholesale channel, and cannot fulfill international orders through a local 3PL. This is an operational straitjacket that no e-commerce-only provider should be getting in a first-order form.

**Recommended fix:** Strike Order Form §4 in its entirety and replace with language that tracks MSA §2.4, or delete MSA §2.4 and insert a single, negotiated exclusivity provision in the Order Form that is no broader than:

> "During the term of this Order Form, Customer will use Provider as its exclusive provider of direct-to-consumer e-commerce order fulfillment (pick, pack, and ship) for Seinon products shipped to the United States and Canada through the Storefront. Nothing in this Section restricts Customer from using Provider or any other party for wholesale distribution, retail-store replenishment, international fulfillment, or any other logistics service."

**Client flag:** Before we respond, we need to confirm with the client whether it currently uses, or plans to use, any other fulfillment provider for wholesale, retail replenishment, or international channels. If so, the current Order Form language is a deal-breaker as written.

---

## Issue 2: Service Credits as Sole and Exclusive Remedy – SLS §6.3

**Where:** Service Level Schedule, Section 6.3.

**What it says:** "Service Credits and Customer's termination right under Section 6.2 are Customer's **sole and exclusive remedies** for any Service Failure, **including any Security Incident**."

**Why it matters:** This provision eliminates Seinon's right to recover actual damages for any service failure. Consider the practical effect:

- If the Storefront is down for 24 hours during a holiday peak and Seinon loses $500,000 in revenue, its remedy is a 15% service credit on the Monthly Platform Fee = **$7,275** (SLS §5.1).
- If Provider's warehouse mis-ships 5% of orders for a month, the credit is 5% × $48,500 = **$2,425**, regardless of the cost of returns, customer churn, or brand damage.
- The maximum monthly credit is capped at 25% of the Monthly Platform Fee = **$12,125** (SLS §5.2).

For a 60-month contract with a $48,500 monthly platform fee (≈$2.9M in platform fees alone, plus fulfillment fees), the total maximum recovery for *any* service failure over the life of the contract is trivially small relative to the business risk.

**Recommended fix:** Delete the "sole and exclusive remedy" language. Replace with:

> "Service Credits are a minimum remedy for Service Failures and are not exclusive. Customer may pursue any other remedy available at law or in equity, including termination for material breach under Section 9.3 of the MSA and recovery of damages, subject to the limitations in Section 11 of the MSA."

If Poseirt insists on an exclusive-remedy structure for routine SL misses (which is common), we should at minimum: (a) raise the credit percentages substantially, (b) remove the 25% monthly cap, and (c) carve out Security Incidents, data loss, and Provider's gross negligence or willful misconduct from the exclusive-remedy provision.

**Client flag:** This is the single most commercially significant issue in the package. The client needs to understand that as drafted, it is effectively buying a 5-year service with no meaningful financial recourse for underperformance. We should present this to the client with a quantified example (e.g., "If the Storefront is down for 4 hours on Black Friday, your maximum recovery is $2,425").

---

## Issue 3: Security Incident Liability – SLS §6.3 Overrides MSA §11.3(b)

**Where:** Service Level Schedule, Section 6.3 (second sentence); MSA, Section 11.3(b).

**What it says:**

- MSA §11.3(b): The liability cap in §11.2 "shall not apply to … (b) Security Incidents, including Provider's obligations under Section 8.3."
- SLS §6.3: "Notwithstanding Section 11.3 of the MSA, Provider's aggregate liability arising out of or relating to Security Incidents **shall not exceed the cap set out in Section 11.2 of the MSA**."

**Why it matters:** The SLS provision directly contradicts and overrides the MSA. Per the order of precedence (MSA §1.3), the SLS ranks above the MSA, so the SLS language governs. The net effect is that Provider's liability for a Security Incident—including a breach of Shopper Data containing names, addresses, payment-related data, and order histories of Seinon's end customers—is capped at 12 months of fees (MSA §11.2). For a company processing consumer payment data, a breach could generate seven-figure or eight-figure costs (forensic investigation, notification, credit monitoring, regulatory fines, class-action defense). Capping that at roughly $600K–$1M (12 months of platform + fulfillment fees) is unacceptable.

Additionally, the MSA already requires Provider to carry $10M in cyber and privacy liability insurance (MSA §12). The insurance is there to backstop uncapped liability. The SLS provision effectively renders that insurance requirement meaningless from a contractual recovery standpoint.

**Recommended fix:** Delete the second sentence of SLS §6.3 in its entirety. Confirm that MSA §11.3(b) remains the governing provision, so Security Incidents are excluded from both the consequential-damages waiver (§11.1) and the liability cap (§11.2). If Poseirt resists, the fallback position should be a super-cap for Security Incidents (e.g., 3× the general cap, or a fixed dollar amount no less than the cyber insurance limit of $10M).

**Client flag:** This needs to go to the client. The client should understand that as drafted, if Poseirt suffers a data breach exposing its end-customer payment data, Poseirt's maximum contractual liability would be roughly one year of fees. The client's own regulatory exposure (state AG actions, potential CCPA/CPRA liability for failing to ensure vendor security) is not capped.

---

## Issue 4: Governing Law and Venue Conflict – Order Form §8 vs. MSA §14

**Where:** Order Form No. 1, Section 8; MSA, Section 14.1 and 14.2.

**What it says:**

- MSA §14.1–14.2: Delaware law; exclusive jurisdiction in Wilmington, Delaware.
- Order Form §8: New York law; exclusive jurisdiction in New York County, New York.

**Why it matters:** Per MSA §1.3, the Order Form controls. So the operative governing law is New York and the venue is New York County. This creates several problems:

1. **Inconsistency and confusion.** A reader of the MSA alone would assume Delaware law governs. The conflict invites threshold litigation over which law applies to which issues.
2. **Substantive differences.** New York and Delaware differ on issues relevant here (e.g., enforcement of exclusive-remedy clauses, interpretation of "material breach," and the availability of certain equitable remedies).
3. **Convenience.** Seinon is a Delaware corporation. Litigating in New York County is more costly and less convenient than Wilmington.

**Recommended fix:** Conform Order Form §8 to MSA §14. Proposed replacement:

> "This Order Form is governed by, and any dispute arising out of or relating to it will be governed by, the laws of the State of Delaware, without regard to its conflict-of-laws principles. Each party submits to the exclusive jurisdiction of the state or federal courts located in Wilmington, Delaware, in accordance with Section 14.2 of the Agreement."

Alternatively, if the client prefers New York law for commercial reasons, conform MSA §14 to match. The key point is that the documents must be consistent.

**Client flag:** Confirm with the client which forum it prefers. If the client has no strong preference, Delaware (its state of incorporation) is the natural choice and is consistent with the Kelvane agreement.

---

## Issue 5: No Termination for Convenience

**Where:** MSA, Section 9 (Term and Termination). The MSA provides for termination for cause (§9.3), insolvency (§9.4), and Chronic Failure under the SLS (§6.2). There is no termination for convenience.

**Why it matters:** Combined with the 60-month Initial Term (Order Form §2) and auto-renewal for successive 60-month terms (MSA §9.2), Seinon is locked in for a minimum of 5 years with no exit right short of proving material breach or Chronic Failure. If Poseirt's service quality degrades gradually (staying just above the Chronic Failure threshold), or if Seinon's business strategy changes (e.g., it acquires a competitor with its own 3PL, or it decides to bring fulfillment in-house), it has no clean exit.

For contrast, the Kelvane fabric testing agreement (a far less critical vendor) includes a termination for convenience on 30 days' notice (Kelvane §13.2).

**Recommended fix:** Add a termination for convenience provision. A market-standard approach for a contract of this size:

> "**9.7 Termination for Convenience.** Customer may terminate an Order Form for convenience on one hundred eighty (180) days' prior written notice to Provider. Upon such termination, Customer will pay (a) all Fees accrued through the effective date of termination, and (b) a transition fee equal to [X]% of the Monthly Platform Fee for the remaining term, declining by [Y]% for each month that has elapsed. Provider's obligations under Sections 8.4 and 9.5 will apply."

If Poseirt will not accept a pure convenience termination, negotiate a "strategic change" trigger (e.g., if Customer acquires or is acquired by an entity that provides competing fulfillment services).

**Client flag:** The client should decide how much termination flexibility it needs. At minimum, we should not agree to a 60-month lock with no exit.

---

## Issue 6: Auto-Renewal with Narrow Notice Window – MSA §9.2

**Where:** MSA, Section 9.2.

**What it says:** Each Order Form renews automatically for a successive term equal to the Initial Term (i.e., another 60 months). Non-renewal notice must be given "no earlier than 100 days and no later than 90 days before the expiration of the then-current term."

**Why it matters:** The notice window is only 10 days wide (from 100 to 90 days before expiration). For a 60-month term, that means Seinon must send non-renewal notice between approximately month 54.7 and month 55.0. If the client's operations team misses that 10-day window, it is locked in for another 5 years. This is a classic "auto-renewal trap."

**Recommended fix:** Widen the window and/or add a reminder obligation:

> "An Order Form will not renew if either party delivers written notice of non-renewal no earlier than 180 days and no later than 60 days before the expiration of the then-current term. Provider will send a written reminder to Customer 200 days before the expiration of each term, noting the non-renewal deadline."

Alternatively, eliminate auto-renewal entirely and require affirmative renewal by both parties.

---

## Issue 7: Low Service Credit Values and Monthly Cap – SLS §§5.1–5.2

**Where:** Service Level Schedule, Sections 5.1 and 5.2.

**What it says:** Service credits are calculated as a percentage of the Monthly Platform Fee ($48,500). The maximum total credit per month is 25% of that fee ($12,125).

**Why it matters:** Even setting aside the exclusive-remedy issue (Issue 2), the credit values are too low to provide meaningful incentive. A 5% credit for missing the ship-timeliness SL (SL-5) is $2,425. If 1% of orders are late (missing the 99.5% target), the cost to Provider of the delay (expedited re-shipment, customer service) is likely less than $2,425, so there is no real financial penalty. The 25% monthly cap means that even if *every* service level is missed in a month, Provider's total exposure is $12,125.

**Recommended fix:**

- Increase the credit percentages (e.g., SL-5 and SL-6 to 10% each; SL-1 to 10/20/30% tiers).
- Remove or raise the 25% monthly cap (e.g., to 50% or uncapped).
- Add a mechanism for credits to escalate if the same SL is missed for consecutive months (e.g., double the credit in the second consecutive miss).
- Base some credits on fulfillment fees rather than just the platform fee, since fulfillment failures (SL-4 through SL-8) are driven by warehouse operations, not platform hosting.

---

## Issue 8: Restricted Independent Verification – SLS §4.4

**Where:** Service Level Schedule, Section 4.4.

**What it says:** Customer may have Provider's measurements verified by an independent third party "no more than once per contract year."

**Why it matters:** Over a 60-month term, Seinon gets only five verification rights. If Provider's WMS data is inaccurate or if there is a dispute about whether a service level was met, Seinon may have to wait up to a year to independently verify. This undermines the entire service-level regime.

**Recommended fix:**

> "Customer may have Provider's measurements verified by an independent third party no more than once per Measurement Period in which a Service Failure is reported, and in any event no more than four (4) times per contract year. If verification shows that Provider understated a Service Failure by more than [5]%, Provider will bear the reasonable cost of verification and will issue the corrected Service Credit within ten (10) Business Days."

---

## Issue 9: Broad Exception for Customer Breach – SLS §5.4(c)

**Where:** Service Level Schedule, Section 5.4(c).

**What it says:** No service credit is owed to the extent the failure is caused by "Customer's breach of Section 4 of the MSA, including late or inaccurate advance shipping notices."

**Why it matters:** MSA Section 4 covers Customer's obligations regarding products, materials, compliance with law, and cooperation. This is a broad section. As drafted, if Seinon is even slightly late on an advance shipping notice (which is an operational detail, not a fundamental breach), Provider could argue that *all* service-level failures during the affected period are excused. The "including" language makes it clear that Provider intends to use this broadly.

**Recommended fix:** Narrow the exception to direct causation:

> "(c) Customer's breach of Section 4.1 of the MSA (Products and Materials), but only to the extent that the specific Service Level failure was directly caused by that breach and could not have been avoided by Provider's exercise of reasonable diligence."

Remove the reference to Section 4 as a whole.

---

## Issue 10: Go-Live Is a "Target," Not a Commitment – Order Form §6.2

**Where:** Order Form No. 1, Section 6.2.

**What it says:** "The parties **target** Storefront go-live and commencement of fulfillment at the Facility within ninety (90) days after the Order Form Effective Date."

**Why it matters:** The word "target" makes this aspirational, not obligatory. If Provider misses the 90-day go-live, there is no service credit, no termination right, and no damages remedy (especially given the exclusive-remedy provision in SLS §6.3). Seinon would be paying the Monthly Platform Fee from April 1, 2026 (the Order Form Effective Date) with no live Storefront and no contractual lever to force a date.

**Recommended fix:**

> "Provider will achieve Storefront go-live and commencement of fulfillment at the Facility no later than ninety (90) days after the Order Form Effective Date (the 'Go-Live Date'). If Provider fails to achieve go-live by the Go-Live Date, Customer may (a) terminate this Order Form without penalty, or (b) continue the relationship with the Monthly Platform Fee abated at 100% for each week of delay beyond the Go-Live Date, up to a maximum of [X] weeks, after which Customer may terminate without penalty."

---

## Issue 11: Assignment Without Consent to Any Successor – MSA §15.2

**Where:** MSA, Section 15.2.

**What it says:** "Either party may assign this Agreement without consent to a successor to all or substantially all of its business or assets, if it gives written notice of the assignment."

**Why it matters:** If Poseirt is acquired by a competitor of Seinon, or by a company with inferior infrastructure, the agreement (including all of Poseirt's obligations) transfers automatically. Seinon has no right to object. Given the exclusivity provision (Issue 1) and the 60-month term, this is a significant risk.

**Recommended fix:**

> "Provider may not assign this Agreement without Customer's prior written consent, except that Provider may assign to a successor in interest to all or substantially all of Provider's business or assets, provided that (a) the successor is not a direct competitor of Customer, (b) the successor assumes all of Provider's obligations under this Agreement in writing, and (c) Customer has the right to terminate the affected Order Form without penalty within thirty (30) days after receiving notice of the assignment if Customer reasonably determines that the successor does not have the capability to perform the Services."

---

## Issue 12: Liability Cap Structure – MSA §11.2

**Where:** MSA, Section 11.2.

**What it says:** "Each party's aggregate liability … will not exceed the fees paid or payable in the 12 months preceding the claim."

**Why it matters:** In the first 12 months of the relationship, the cap equals roughly one year of fees. If the Monthly Platform Fee is $48,500/month and fulfillment fees average, say, $80,000/month, the cap in year one is approximately $1.57M. That may be adequate for some claims but is low for others (e.g., a major inventory loss event). More importantly, the cap is *trailing*—it grows over time, which means the cap in month 13 is the same as in month 12, but the cap in month 60 reflects a full year of fees. The structure is not inherently wrong, but combined with the exclusive-remedy provision (Issue 2) and the Security Incident override (Issue 3), it creates a very low-risk profile for Provider.

For contrast, the Kelvane agreement uses "the greater of (a) the fees paid or payable … in the twelve (12) months preceding the event giving rise to the claim and (b) one hundred thousand dollars ($100,000)" (Kelvane §11.2). The floor of $100,000 ensures a minimum cap even in the early months.

**Recommended fix:** Add a floor: "…will not exceed the greater of (a) the fees paid or payable in the 12 months preceding the claim, and (b) two million dollars ($2,000,000)." This ensures a meaningful minimum cap from day one.

---

## Issue 13: Chronic Failure Threshold Is High – SLS §6.2

**Where:** Service Level Schedule, Section 6.2.

**What it says:** A Chronic Failure occurs if (a) the same SL is missed in 3 of any 6 rolling months, or (b) Storefront Availability falls below 99.0% in 2 consecutive months.

**Why it matters:** This is the only termination right tied to performance (absent a general material breach under MSA §9.3, which is a high bar). Under prong (a), Provider can miss an SL in 3 out of 6 months and still not trigger a Chronic Failure if the misses are spread out (e.g., months 1, 3, and 5 of a 6-month window—wait, that *is* 3 in 6, so it would trigger). Actually, re-reading: "fails to meet the same Service Level in any three (3) Measurement Periods within a rolling six (6) month period." So 3 misses of the same SL in any 6-month window triggers it. That's actually not unreasonable. The more concerning issue is that this is the *only* performance-based exit, and it requires 3 misses. If Provider misses 2 of 6 months on every SL, it never triggers a Chronic Failure, and (given the exclusive-remedy clause) Seinon has no other performance-based termination right.

**Recommended fix:** In addition to fixing the exclusive-remedy issue (Issue 2), lower the threshold:

> "(a) Provider fails to meet the same Service Level in any two (2) Measurement Periods within a rolling four (4) month period; or (b) Provider fails to meet two or more different Service Levels in the same Measurement Period; or (c) Storefront Availability falls below 99.5% in any two (2) consecutive Measurement Periods."

---

## Issue 14: No Service Level for Data Migration or Implementation

**Where:** Order Form No. 1, Section 6; Service Level Schedule, Section 3.

**What it says:** The SLS covers Storefront availability, response times, order transmission, inbound receiving, ship timeliness, order accuracy, inventory accuracy, returns processing, support, and security notification. There is no service level for the implementation phase (data migration, ERP integration, initial inventory transfer).

**Why it matters:** The implementation period (first 90 days) is when the most disruptive errors occur—data loss during migration, integration failures, inventory discrepancies at transfer. If the Storefront goes live with corrupted product data or the ERP integration fails, there is no SL to measure against and no credit to claim.

**Recommended fix:** Add an implementation SL or, at minimum, a milestone-based acceptance criterion:

> "Provider will complete data migration and ERP integration in accordance with the implementation plan. Customer will have thirty (30) days after go-live to identify and report material data errors. Provider will correct material data errors at no charge. If more than [X]% of SKUs have material data errors at go-live, Customer may delay acceptance and the Go-Live Date will be extended accordingly."

---

## Issue 15: Reconciliation of SLS §6.3 with MSA §11.3 – Structural Inconsistency

**Where:** SLS §6.3; MSA §§11.1, 11.2, 11.3.

**What it says:** This is a sub-point of Issues 2 and 3, but worth calling out structurally. The MSA carves Security Incidents out of both the consequential-damages exclusion (§11.1) and the cap (§11.2) via §11.3(b). The SLS then (a) makes service credits the exclusive remedy for Security Incidents (§6.3, first sentence) and (b) re-imposes the §11.2 cap on Security Incidents (§6.3, second sentence). The result is that a Security Incident—arguably the highest-severity failure a provider can commit—carries less contractual risk for Provider than a routine SL miss, because at least for an SL miss the (theoretical) right to sue for damages under MSA §9.3 (material breach) might survive, whereas for a Security Incident the SLS expressly forecloses all remedies beyond the credit and the capped amount.

**Recommended fix:** As noted in Issues 2 and 3, delete SLS §6.3 in its entirety and replace with a provision that preserves MSA §11.3's carve-outs.

---

## Re: Kelvane Fabric Testing Agreement

The Kelvane agreement is a separate vendor arrangement for textile testing and does not directly affect the Poseirt deal. However, two features are relevant as negotiating context:

1. **Termination for convenience (Kelvane §13.2):** Either party may terminate on 30 days' notice. The absence of any comparable right in the Poseirt package (Issue 5) is stark by contrast. We can cite this internally to the client to illustrate the asymmetry.

2. **Liability cap floor (Kelvane §11.2):** The "greater of fees or $100,000" structure (Issue 12) is a useful benchmark. Even a low-value testing vendor gets a $100K floor; a $3M+/year logistics provider should get a much higher one.

I do not recommend raising the Kelvane agreement with Poseirt, but the client should be aware of the contrast when evaluating the Poseirt terms.

---

## Summary of Items Requiring Client Input Before We Respond to Poseirt

| # | Issue | Client Decision Needed |
|---|---|---|
| 1 | Exclusivity scope (Order Form §4) | Does Seinon use or plan to use other 3PLs for wholesale, retail replenishment, or international? What is the maximum exclusivity it can accept? |
| 2 | Exclusive remedy / service credits (SLS §6.3) | What is the client's risk tolerance for uncapped vs. capped recovery on service failures? Will it accept credits as the sole remedy for routine SL misses if we can raise the credit values? |
| 3 | Security Incident cap override (SLS §6.3) | Confirm that the client requires Security Incidents to be excluded from the liability cap (consistent with MSA §11.3(b) and the $10M cyber insurance requirement). |
| 4 | Governing law / venue (Order Form §8) | Delaware or New York? (Recommendation: Delaware, consistent with MSA and the Kelvane agreement.) |
| 5 | Termination for convenience | How much exit flexibility does the client need? Is a 180-day-notice convenience termination with a declining buyout acceptable? |

---

## Recommended Negotiating Priorities (in order of importance)

1. **Strike or narrow Order Form §4** (exclusivity) – non-negotiable.
2. **Delete SLS §6.3** (exclusive remedy + Security Incident cap override) – non-negotiable.
3. **Conform governing law/venue** (Order Form §8 to MSA §14, or vice versa) – must fix.
4. **Add termination for convenience** or a strategic-change exit – high priority.
5. **Widen the auto-renewal notice window** (MSA §9.2) – high priority.
6. **Make go-live a firm commitment** with consequences (Order Form §6.2) – high priority.
7. **Raise service credit values and remove the 25% monthly cap** (SLS §§5.1–5.2) – medium priority.
8. **Add a liability cap floor** (MSA §11.2) – medium priority.
9. **Narrow the Customer-breach exception** (SLS §5.4(c)) – medium priority.
10. **Increase independent verification rights** (SLS §4.4) – medium priority.
11. **Add assignment protections** (MSA §15.2) – medium priority.
12. **Lower the Chronic Failure threshold** (SLS §6.2) – lower priority (moot if exclusive remedy is fixed).
13. **Add implementation/data-migration protections** (Order Form §6) – lower priority.