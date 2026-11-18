# MEMORANDUM

**TO:** [Partner]
**FROM:** Associate
**DATE:** [Current Date]
**RE:** Baineind Event Rentals, LLC – Software License Agreement with Beipeiv Software, Inc.: Issue Identification and Recommended Actions

---

## Summary

I have reviewed all eight documents in the matter folder. I identify **ten issues** ranging from critical to moderate. The three most urgent are: (1) a material conflict between the Agreement and the Service Level Schedule on the definition of "Severity 1 Incident" that significantly narrows Baineind's service-level protections; (2) the pending change of control to Kestrel Venue Group, which the November 2 notice letter fails to address correctly under the assignment provisions; and (3) a governing-law and forum conflict between the Side Letter (New York) and the Agreement (Delaware). Details and recommended fixes follow.

---

## Issue 1 – Severity 1 Incident Definition: Material Conflict Between Agreement and Service Level Schedule

**Where it appears:**

| Document | Section | Definition |
|---|---|---|
| Software License Agreement | §1.18 | "any failure of the Platform preventing Licensee from creating, modifying or fulfilling Rental Orders **at any Licensee location**" |
| Platform License Term Sheet | §6.2 | Same as Agreement §1.18, with added context: "Licensee's event-day operations depend on order, dispatch and pick-list functions being available at each warehouse." |
| Service Level Schedule | §2.1 | "the **complete unavailability** of the Platform to **all** Authorized Users at **all** Licensee locations, other than during Scheduled Maintenance" |

**Why it matters:**

The Service Level Schedule definition is dramatically narrower than the Agreement and Term Sheet definitions. Under the SLS, a Severity 1 Incident exists only when the Platform is *completely* down for *every* user at *every* location. A single-warehouse outage—precisely the scenario the Term Sheet flagged as operationally critical for event-day dispatch and pick-list generation—would be classified as Severity 2 at best.

The consequences are severe:

- **Response time drops from 1 hour (24×7) to 4 Business Hours** (SLS §3.1).
- **Resolution target drops from 4 hours to 2 business days** (SLS §3.1).
- **No service credit is available for missed resolution targets** (SLS §3.4, §5.3–5.4). Credits are payable only for (a) monthly availability below 99.9% and (b) missed Severity 1 response times.
- The 99.9% availability calculation (SLS §5.2) counts only "Downtime Minutes" from Severity 1 Incidents. A 4-hour single-location outage produces zero Downtime Minutes and therefore no availability credit at all.

**Order of precedence:** Agreement §20.4 provides that, "as to service levels, the Service Level Schedule shall prevail over the body of this Agreement." The SLS definition therefore controls, despite being inconsistent with the defined term in §1.18 and with the Term Sheet.

**Recommended fix:**

- Negotiate a conforming amendment to SLS §2.1 to match the Agreement §1.18 definition (failure at *any* location preventing Rental Order creation, modification or fulfillment).
- If Beipeiv resists, at minimum add a provision that a Severity 2 Incident affecting a single location during a Peak Season (as defined in the Side Letter) triggers Severity 1 response times (1 hour, 24×7) and a service credit.
- Add service credits for missed Resolution targets, not just missed Response times.

---

## Issue 2 – Change of Control to Kestrel Venue Group: Notice Letter Is Inadequate

**Where it appears:**

| Document | Section | Relevant Text |
|---|---|---|
| Software License Agreement | §16.2 | "Any direct or indirect change in Control of Licensee is deemed an assignment… Any such assignment requires Licensor's prior written consent, which Licensor may give or withhold in its sole discretion." |
| Software License Agreement | §16.3 | "Any purported assignment in violation of this Section 16… is void as against Licensor. In that event Licensor may terminate this Agreement immediately… all License Fees for the remainder of the Initial Term become immediately due and payable." |
| Baineind Notice Letter (Nov 2, 2026) | ¶3 | "This letter is provided for Beipeiv's information, and **no action is required** by Beipeiv in connection with it." |

**Why it matters:**

The sale of 100% of Baineind's membership interests from Ostrander Holdings LLC to Kestrel Venue Group, Inc. is unambiguously a "change in Control" under §1.4 (Kestrel will own more than 50% of the membership interests). Under §16.2, this is deemed an assignment requiring Beipeiv's prior written consent, which Beipeiv may withhold in its **sole discretion**.

The November 2 notice letter is deficient in three respects:

1. **It does not request consent.** It characterizes the notice as informational and states "no action is required." If Beipeiv withholds consent (or simply does not respond), the change of control on December 15, 2026 would be a void assignment under §16.3.
2. **It does not address the fee-acceleration consequence.** If Beipeiv terminates under §16.3, all License Fees for the remainder of the Initial Term (through February 28, 2029) become immediately due. That is approximately **$372,000** (two remaining annual installments of $186,000 each, for the periods March 2027–February 2028 and March 2028–February 2029), plus any accrued amounts.
3. **It creates a confidentiality obligation on Beipeiv** (¶5) without leveraging that as part of a consent negotiation.

**Additional risk:** Even if Beipeiv consents to the assignment, §16.2 gives it sole discretion. Beipeiv could condition consent on a fee increase, additional security, or other terms. Baineind has no contractual right to consent.

**Recommended fix (urgent – before December 15, 2026 closing):**

- Send a supplemental letter or email **explicitly requesting Beipeiv's written consent** under §16.2 to the change of control, acknowledging that the transaction constitutes a deemed assignment.
- Offer to provide Kestrel Venue Group's financial statements or a parent guarantee as a condition of consent, if Beipeiv raises credit concerns.
- If Beipeiv withholds consent or does not respond before closing, evaluate: (a) whether to delay closing; (b) whether to seek consent post-closing and negotiate a waiver of the §16.3 acceleration; or (c) the commercial cost of termination and re-procurement.
- Consider whether the Kestrel transaction documents should include a condition precedent that Beipeiv consent has been obtained.

**Flag:** I cannot determine from the documents whether Beipeiv has responded to the November 2 letter. If no response has been received, the risk is acute given the December 15 target closing date.

---

## Issue 3 – Governing Law and Forum Conflict: Side Letter (New York) vs. Agreement (Delaware)

**Where it appears:**

| Document | Section | Law / Forum |
|---|---|---|
| Software License Agreement | §20.1–20.2 | Delaware law; Wilmington, Delaware courts |
| Platform License Term Sheet | §13.1–13.2 | Delaware law; Wilmington, Delaware courts |
| Side Letter | §6.1–6.2 | **New York law; Manhattan, New York courts** – "This Side Letter, **and the Agreement as modified hereby**, are governed by… New York" |

**Why it matters:**

The Side Letter's governing-law clause purports to override the Agreement's Delaware law and forum for "the Agreement as modified hereby." Under the order of precedence in Agreement §20.4, the Side Letter ranks **first**. A reasonable reading is that the Side Letter's New York law and Manhattan forum apply to the entire Agreement (at least to the extent "modified" by the Side Letter), creating uncertainty about:

- Which state's law governs interpretation of the Agreement, the SLS, and the Quality Agreement.
- Where any dispute must be litigated. Baineind is a Delaware LLC headquartered in Wilmington; litigating in Manhattan is costly and inconvenient.
- Whether New York's more plaintiff-friendly commercial law (e.g., on consequential damages waivers, duty of good faith) applies.

The Term Sheet (§13.2) clearly contemplated Delaware law and forum for the Agreement. The Side Letter's New York clause appears to be an error or an unexplained deviation.

**Recommended fix:**

- Seek a corrective amendment to Side Letter §6 to conform to Delaware law and Wilmington forum, matching the Agreement and Term Sheet.
- If Beipeiv resists, at minimum negotiate a provision that the Side Letter's governing-law clause applies only to disputes arising under the Side Letter itself, not to "the Agreement as modified hereby."

---

## Issue 4 – Licensee Indemnity (§12.2) Is Broader Than the Term Sheet Contemplated

**Where it appears:**

| Document | Section | Scope of Licensee Indemnity |
|---|---|---|
| Platform License Term Sheet | §8.3 | "third-party claims arising from Licensee Data and Licensee's use of the Platform **in breach of the Agreement's use restrictions**" |
| Software License Agreement | §12.2(b) | "all third-party claims… arising out of or relating to… Licensee's or any Authorized User's **use of the Platform**, including any claims by event customers, venues or other third parties arising from **Rental Orders processed through the Platform**" |

**Why it matters:**

The Term Sheet limited the use-based indemnity to breaches of the §3 restrictions (no reverse engineering, no competing product, etc.). The final Agreement expands it to **any** use of the Platform, expressly including claims by Baineind's event customers and venues arising from Rental Orders.

Practical scenario: A customer's wedding is disrupted because the Platform double-booked a tent (a Platform Data Error under the Quality Agreement). The customer sues Baineind for breach of contract. Baineind's §12.2(b) indemnity to Beipeiv could be triggered if Beipeiv is named in the suit or if Beipeiv argues the claim "arises from" Baineind's use. Meanwhile, Baineind's own remedy against Beipeiv is limited by the §13.1 cap ($186,000) and the §13.2 consequential-damages waiver.

The indemnity is also not expressly limited to claims where Baineind is found at fault. The phrase "arising out of or relating to" is broad.

**Recommended fix:**

- Negotiate a carve-out from §12.2(b) for claims to the extent caused by a Platform Data Error or a breach of Beipeiv's warranty under §11.2.
- Alternatively, limit §12.2(b) to claims arising from Baineind's use **in breach of Section 3**, conforming to the Term Sheet.
- At minimum, add language clarifying that §12.2(b) does not apply to the extent a claim is caused by a defect in the Platform.

---

## Issue 5 – No Service Credits for Missed Resolution Targets

**Where it appears:**

| Document | Section |
|---|---|
| Service Level Schedule | §3.4 ("Resolution targets… are targets. Licensor shall use commercially reasonable efforts to meet them. Service credits are payable **only** as set out in Section 5.") |
| Service Level Schedule | §5.3 (availability credits only) and §5.4 (response credits only) |

**Why it matters:**

The 4-hour resolution target for Severity 1 Incidents (SLS §3.1) is aspirational. If Beipeiv takes 12 hours to resolve a Severity 1 Incident, Baineind receives no credit unless the total monthly downtime also pushes availability below 99.9%. Given the narrow SLS definition of Severity 1 (see Issue 1), many operationally critical outages won't even generate Downtime Minutes for the availability calculation.

For an event rental company, a 4-hour delay in restoring dispatch and pick-list functionality on a Saturday during peak season can mean missed deliveries, failed setups, and customer penalties—losses far exceeding the maximum monthly service credit of $4,650 (30% of the $15,500 Monthly Fee, per SLS §5.5).

**Recommended fix:**

- Add a resolution-credit tier: e.g., if a Severity 1 Incident is not resolved within the 4-hour target, Baineind receives a credit of 5% of the Monthly Fee for each additional hour (capped at the §5.5 maximum).
- Alternatively, lower the availability threshold or increase the credit percentages to make the remedy meaningful.

---

## Issue 6 – Insurance: Claims-Made Policies and No Additional-Insured Status

**Where it appears:**

| Document | Section | Detail |
|---|---|---|
| Software License Agreement | §14.1 | Requires CGL, Tech E&O, and Cyber Liability; "limits customary for providers of cloud software of comparable scope" |
| Beipeiv Certificate of Insurance | §5.4 | Tech E&O: **claims-made**, retroactive date 03/01/2019, $5M per claim / $5M aggregate |
| Beipeiv Certificate of Insurance | §5.5 | Cyber: **claims-made**, retroactive date 03/01/2019, $5M per claim / $5M aggregate |
| Beipeiv Certificate of Insurance | §1.1 | "This certificate… confers no rights upon the Certificate Holder." |
| Beipeiv Certificate of Insurance | §1.3 | Additional insured status requires a policy endorsement; none is shown. |

**Why it matters:**

1. **Claims-made risk.** The Tech E&O and Cyber policies are claims-made. If Beipeiv cancels, non-renews, or switches carriers at any policy anniversary, claims first made after the policy ends for incidents that occurred during the policy period may not be covered unless Beipeiv purchases "tail" (extended reporting period) coverage. The Agreement (§14.2) requires Beipeiv to notify Baineind of cancellation or material reduction within 30 days, but it does not require Beipeiv to maintain continuous claims-made coverage or to purchase tail coverage at termination.

2. **No additional-insured status.** Baineind cannot directly claim under Beipeiv's policies. Its sole recourse is the contractual indemnity (§12.1) and the liability cap (§13.1). If Beipeiv becomes insolvent or its insurer denies coverage, Baineind's recovery is limited to Beipeiv's assets.

3. **CGL limits may be low.** The CGL is $1M per occurrence / $2M aggregate. While the Agreement only requires "customary" limits, for a cloud provider whose failure could trigger large third-party claims (e.g., a data breach affecting Baineind's customers), $1M CGL is modest. The $5M Tech E&O and Cyber limits are more meaningful.

**Recommended fix:**

- Add a requirement in §14 that Beipeiv maintain continuous claims-made coverage (same or earlier retroactive date) for the Term plus at least six years (the typical statute of limitations for contract and tort claims in Delaware), or purchase tail coverage of equivalent duration at termination.
- Request that Baineind be added as an additional insured on the Tech E&O and Cyber policies (or at minimum on the Cyber policy for data-breach claims).
- Consider requiring a minimum CGL limit of $2M per occurrence / $4M aggregate.

---

## Issue 7 – Data Exit Window (60 Days) Shorter Than Transition Assistance Period (90 Days)

**Where it appears:**

| Document | Section | Period |
|---|---|---|
| Software License Agreement | §7.3 | Licensee Data available for export for **60 days** after expiration/termination, then deleted |
| Software License Agreement | §15.5 | Transition assistance available for up to **90 days** after expiration/termination |

**Why it matters:**

If Baineind needs the full 90 days of transition assistance (e.g., migrating to a new platform), Beipeiv will have deleted the Licensee Data at day 60. Baineind would be unable to export data it still needs for the transition. The Quality Agreement (§6.3) confirms that exit data is governed by §7.3.

**Recommended fix:**

- Amend §7.3 to extend the export window to at least 90 days (matching the transition assistance period), or provide that the export window is extended for as long as Baineind is receiving transition assistance under §15.5.
- As a practical matter, Baineind should perform a full data export **before** any termination or expiration, not after.

---

## Issue 8 – Liability Cap and Consequential Damages Waiver May Be Inadequate

**Where it appears:**

| Document | Section |
|---|---|
| Software License Agreement | §13.1 (cap: fees paid/payable in 12 months before claim = **$186,000**) |
| Software License Agreement | §13.2 (waiver of indirect, consequential, lost profits, revenues, goodwill) |
| Software License Agreement | §13.3 (Excluded Claims: indemnity, confidentiality, gross negligence/fraud/willful misconduct, fee payment) |
| Platform License Term Sheet | §8.4 ("Customary exclusions from the cap and from the waiver of consequential damages will be addressed in the Agreement") |

**Why it matters:**

Baineind's entire event-day operations—quoting, order processing, dispatch, pick lists—run through the Platform. A multi-hour outage during peak season, a data corruption event, or a security breach could cause lost rental revenue, customer breach claims, and reputational harm far exceeding $186,000. The §13.2 waiver bars recovery of lost profits and revenues. The §13.3 exclusions do not include data loss, Platform warranty breach, or service-level failures.

The Term Sheet promised that "customary exclusions" would be "addressed in the Agreement." The final Agreement's exclusions are narrower than what a licensee in Baineind's position would typically negotiate (e.g., no carve-out for data loss or for Beipeiv's breach of the Platform warranty).

**Recommended fix:**

- Add to §13.3 (Excluded Claims): (a) Beipeiv's breach of §7 (Licensee Data) or §8 (Security); (b) Beipeiv's breach of the Platform warranty in §11.2(a); (c) Beipeiv's failure to meet Service Level Schedule commitments (so that service credits are not the sole remedy).
- Alternatively, increase the cap to 2× or 3× annual fees for data-related and security-related claims.
- Carve out Baineind's lost rental revenue directly caused by a Platform outage during a Peak Season from the §13.2 consequential-damages waiver.

---

## Issue 9 – Side Letter Peak-Season Rates Fixed Only for Initial Term

**Where it appears:**

| Document | Section |
|---|---|
| Side Letter | §3.2 ("These rates are fixed for the **Initial Term**.") |
| Side Letter | §3.3 (Outside Peak Seasons, rates "may not exceed the rates in Section 3.1 by more than ten percent (10%)") |
| Software License Agreement | §5.4 (Renewal fee increases capped at 5% per year) |

**Why it matters:**

During any Renewal Term (after February 28, 2029), Beipeiv can increase the Peak-Season Additional Service rates without limitation. The 10% ceiling in §3.3 applies only to non-Peak-Season rates relative to Peak-Season rates; it does not cap the Peak-Season rates themselves. Combined with the 5% annual increase on base License Fees (§5.4), Baineind's total cost could rise significantly at renewal.

**Recommended fix:**

- Amend Side Letter §3.2 to fix the rates for the full Term (Initial + all Renewal Terms), or cap increases at 5% per renewal year (matching §5.4).

---

## Issue 10 – Implementation Timeline Overlaps First Peak Season

**Where it appears:**

| Document | Section | Detail |
|---|---|---|
| Side Letter | §1.1(a) | First Peak Season: **April 1** through June 30 |
| Implementation Kickoff Notes | §3.1 | Go-live target: **April 6**, 2026 |
| Implementation Kickoff Notes | §3.2 | Legacy system in read-only mode until go-live |
| Service Level Schedule | §8.1 | SLS in effect from March 1, 2026 |

**Why it matters:**

The Platform was not expected to be live until April 6, but the first Peak Season began April 1. During April 1–5:

- The Peak Season support engineer (Side Letter §2.1) would have been assigned but had no live Platform to support.
- If Baineind attempted to use the Platform before full go-live (e.g., for quoting or order entry), any failure might not be covered by the SLS if the Platform was not yet "available" in the contractual sense.
- The Side Letter §2.3 maintenance restriction (no non-emergency maintenance on weekends or pre-holidays during Peak Season) would technically apply, but there was no live system to maintain.

This is a minor issue given that go-live occurred (presumably) on or near April 6, but it highlights a gap in the implementation plan: the Peak Season protections were not fully operational when the season began.

**Recommended fix (for future reference):**

- In any re-papering or renewal, align the first Peak Season start date with the go-live date, or provide that Peak Season protections (including the SLS) apply from go-live rather than from the calendar date.

---

## Items I Cannot Resolve from the Documents Alone

| # | Item | Why it's unresolved |
|---|---|---|
| A | **Has Beipeiv responded to the November 2, 2026 notice letter?** | No response from Beipeiv is in the folder. If Beipeiv has withheld consent or demanded conditions, the analysis in Issue 2 changes significantly. |
| B | **Has go-live actually occurred, and was it on April 6, 2026?** | The kickoff notes set a target date, but there is no go-live confirmation in the folder. If go-live was delayed, the Peak Season overlap (Issue 10) is more acute. |
| C | **Has Baineind paid the first annual License Fee ($186,000, due by ~March 31, 2026)?** | No payment records in the folder. If payment was late, interest under §6.3 may have accrued, and Beipeiv could argue a material breach under §15.3(a). |
| D | **Has Beipeiv delivered the SOC 2 Type II report (due ~April 17, 2026 per kickoff notes)?** | No report in the folder. If not delivered, Baineind has a potential (minor) breach claim under §8.3. |
| E | **What is Beipeiv's current insurance status for the 2027–2028 policy year?** | The certificate in the folder covers 03/01/2026–03/01/2027 only. If Beipeiv has let the claims-made policies lapse or changed carriers, the retroactive-date issue in Issue 6 becomes immediate. |
| F | **Are there any open incidents, Data Errors, or service-level failures since go-live?** | No operational records in the folder. If there are, they may support a pattern-of-breach argument or a service-credit claim. |

---

## Priority Action Items

| Priority | Action | Deadline |
|---|---|---|
| **CRITICAL** | Send supplemental letter to Beipeiv explicitly requesting written consent under §16.2 to the Kestrel change of control; do not close without consent or a negotiated waiver of §16.3 acceleration. | **Before December 15, 2026** |
| **HIGH** | Open negotiation on SLS §2.1 (Severity 1 definition) and §3.4/§5 (resolution credits). Propose conforming amendment. | Within 30 days |
| **HIGH** | Seek corrective amendment to Side Letter §6 (governing law/forum) to restore Delaware law and Wilmington forum. | Within 30 days |
| **MEDIUM** | Negotiate §12.2(b) carve-out for Platform-caused claims; §13.3 expansion for data/security claims; §7.3 extension to 90 days. | Next amendment cycle or renewal negotiation |
| **MEDIUM** | Request confirmation of Beipeiv's 2027–2028 insurance policies (same carriers, same or earlier retroactive date, continuous coverage). | Within 60 days |
| **LOW** | Calendar the §15.2 non-renewal notice deadline (~November 30, 2028) and the §5.4 fee-increase notice window (90 days before each Renewal Term). | Ongoing |