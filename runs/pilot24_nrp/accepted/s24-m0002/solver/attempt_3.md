# MEMORANDUM

**TO:** [Partner]
**FROM:** [Associate]
**DATE:** [Current Date]
**RE:** Nodix Aerial Systems / Sonox AgroDrone – Transaction Document Review

---

## Summary

I have reviewed the four documents in the matter folder: the Asset Purchase Agreement ("APA"), the Raskova Key Employee Agreement ("KEA"), the Nodix Board Consent, and the Closing Press Release. I have identified several issues, the most significant of which is a provision in the KEA that quietly strips intellectual property out of the "Fundamental Representations" category in the APA, directly contradicting what the Nodix board approved. A second major issue is a definitional error in the KEA that narrows Dr. Raskova's non-compete to only the crop-imaging product line, leaving Nodix's spray and seeding platforms unprotected against competition from her personally. Details and recommended fixes follow, ranked by significance.

---

## Issue 1 (Critical): KEA Section 7.4 Removes IP from Fundamental Representations, Contradicting the Board Consent

**Where it appears:**
- KEA, Section 7.4 ("Purchase Agreement Indemnification")
- APA, Section 9.5(b) (defining "Fundamental Representations" to include Section 4.9)
- APA, Section 9.1 (survival periods)
- Board Consent, Section 2.7 (describing IP as a Fundamental Representation)

**What the issue is:**

APA Section 9.5(b) defines "Fundamental Representations" as Sections 4.1 (Organization), 4.2 (Authority), **4.9 (Intellectual Property)**, and 4.14 (Brokers). Claims based on Fundamental Representations are exempt from the $485,000 basket and the 15% cap, and survive until 60 days after expiration of the applicable statute of limitations (APA § 9.1).

KEA Section 7.4 provides:

> "Under Section 11.10 of the Purchase Agreement, Section 9.5(b) of the Purchase Agreement is hereby amended so that the term 'Fundamental Representations' shall not include Section 4.9 (Intellectual Property). As amended, the Fundamental Representations consist of the representations and warranties in Sections 4.1 (Organization), 4.2 (Authority) and 4.14 (Brokers) of the Purchase Agreement."

Because APA Section 11.9(b) provides that an Ancillary Agreement governs "to the extent it expressly amends a specified Section of this Agreement and is signed by both Buyer and Seller," and because Sonox signs the KEA "solely for purposes of Section 7.4," this amendment is likely effective. The practical consequences for Nodix are:

| Protection | As Approved by Board (APA § 9.5(b)) | As Amended by KEA § 7.4 |
|---|---|---|
| Basket | Not applicable to IP claims | $485,000 deductible applies |
| Cap | Purchase Price ($48.5M) | 15% of Purchase Price ($7.275M) |
| Survival | 60 days after statute of limitations expires | 18 months after Closing |

**Why it matters to Nodix:**

The IP (FieldMind flight-control software, drone patents and patent applications) is the core strategic asset of this acquisition. The board consent expressly states in Section 2.7: "claims relating to title to and non-infringement of the Seller Intellectual Property, including the FieldMind flight-control software and the Sonox drone patents, are not limited by the 15% cap." The board approved the deal on that understanding. KEA Section 7.4 reverses that protection without any corresponding disclosure in the board consent.

Additionally, the 18-month survival period for IP claims is very short. If a patent invalidity challenge or a third-party infringement claim surfaces 19 months post-closing, Nodix would have no indemnification recourse against Seller for a breach of the IP representations.

There is also a corporate authority concern. Board Consent Section 3.1 provides that "Any changes approved by the Authorized Officer executing it must be consistent with the material terms described in Article 2." Because Article 2, Section 2.7 describes IP as a Fundamental Representation, KEA Section 7.4 is not "consistent" with the approved material terms. An Authorized Officer who signed the KEA with Section 7.4 included may have exceeded the authority granted by the board consent.

**Recommended fix:**

1. **Immediately:** Confirm with the client whether the board (or the Authorized Officers who signed) was aware of KEA Section 7.4 before execution. If not, this is a potential breach of the board's approval conditions and should be elevated to the board.
2. **Negotiate a corrective amendment:** Seek to amend KEA Section 7.4 (or the APA) to restore Section 4.9 to the Fundamental Representations. Because KEA Section 8.5 provides that "Section 7.4 may be amended only by a written instrument that the Company and Seller also sign," we have a clear mechanism.
3. **If Seller resists:** At minimum, negotiate (a) an extension of the survival period for IP representations to match the original Fundamental Rep survival (statute of limitations + 60 days), and (b) a reduction or elimination of the basket for IP claims.
4. **Corporate hygiene:** If the board was not informed, consider whether a ratifying board consent is warranted to cure the authority gap.

**Flag to client:** This is the most urgent item. The deal has already closed (per the press release), so we are now in the post-closing indemnification period. Every day that passes reduces the window in which Nodix can assert IP claims. If the 18-month survival applies, Nodix has until approximately April 30, 2028 to bring any IP-related indemnification claim. We should confirm the client understands this deadline and consider whether any IP issues have already surfaced.

---

## Issue 2 (High): KEA Defines "Business" Narrowly, Limiting Dr. Raskova's Non-Compete to Crop-Imaging Only

**Where it appears:**
- KEA, Section 1.1 (definition of "Business")
- KEA, Section 1.1 (definition of "Competing Business")
- KEA, Section 6.1 (Non-Competition covenant)
- APA, Section 1.1 (definition of "Business" – broader)
- Board Consent, Section 2.4 (describes "Business" as the full agricultural drone operation)

**What the issue is:**

The APA defines "Business" as:

> "the design, manufacture, sale and servicing of agricultural drones, payloads and flight-control and agronomic software, including spray, seeding and imaging platforms"

The KEA defines "Business" as:

> "the crop-imaging drone product line marketed as the Sonox Scout series, as conducted by Seller immediately before the Closing and by the Company after the Closing"

The KEA's "Competing Business" definition incorporates this narrow "Business" term. As a result, Dr. Raskova's non-compete (KEA § 6.1) prohibits her from engaging in or supporting only businesses competitive with the **crop-imaging drone product line (Sonox Scout series)**. She is not restricted from competing in spray drones, seeding drones, or the broader agricultural drone space.

**Why it matters to Nodix:**

Nodix paid $48.5M for the full agricultural drone business, including spray, seeding, and imaging platforms. The press release and board consent both describe the acquisition in those broader terms. Yet the person who founded and ran the entire business is only contractually restricted from competing in one product line. If Dr. Raskova leaves Nodix (employment is at-will, KEA § 2.5) and starts or joins a spray-drone company, the KEA non-compete would not prevent it.

The APA's Seller non-compete (Section 6.4) does cover the full "Business" for 5 years, but it binds Sonox AgroDrone LLC as an entity. Post-closing, Sonox is a shell with no operations (KEA § 2.3 permits Dr. Raskova to "wind up the affairs of Seller" but prohibits her from causing Seller to "conduct any business operations"). An entity non-compete against a dormant LLC provides limited practical deterrence compared to a personal covenant.

**Recommended fix:**

1. **Determine intent:** Confirm with the client whether the narrow "Business" definition in the KEA was a deliberate negotiation point or a drafting error. Given that the board consent (Section 2.10) describes the covenants as intended "to protect the goodwill of the Business acquired by the Company" (using the APA's broader definition), this appears to be a drafting error.
2. **Amend KEA Section 1.1:** Replace the narrow "Business" definition with the APA's definition, or at minimum expand it to cover "the design, manufacture, sale and servicing of agricultural drones, payloads and flight-control and agronomic software, including spray, seeding and imaging platforms."
3. **If amendment is not possible:** Consider whether the APA's Seller non-compete (Section 6.4) can be enforced against Dr. Raskova personally in her capacity as managing member of Sonox, or whether a new personal covenant can be negotiated as a condition of continued employment or vesting of equity.

**Flag to client:** This issue is particularly acute because Dr. Raskova's employment is at-will. If she departs voluntarily (resigning without Good Reason requires only 60 days' notice, KEA § 4.1), the non-compete runs for 24 months from the Termination Date. But during those 24 months, she could lawfully launch or join a spray-drone or seeding-drone venture. The client should assess whether this risk is acceptable given her role as CTO and her access to all product lines.

---

## Issue 3 (High): Board Consent Describes IP as a Fundamental Representation; KEA Section 7.4 Is Inconsistent with Approved Material Terms

**Where it appears:**
- Board Consent, Section 2.7
- Board Consent, Section 3.1 (second RESOLVED clause)
- KEA, Section 7.4

**What the issue is:**

This is the governance dimension of Issue 1. Board Consent Section 2.7 states:

> "The Fundamental Representations are Sections 4.1 (Organization), 4.2 (Authority), 4.9 (Intellectual Property) and 4.14 (Brokers). Claims for breach of the Fundamental Representations, and claims for fraud, are not subject to the basket or to the 15% cap."

Board Consent Section 3.1 provides that the Authorized Officers may execute the agreements "in substantially the form presented to the Board" and that "[a]ny changes approved by the Authorized Officer executing it must be consistent with the material terms described in Article 2."

KEA Section 7.4 is a change that is **not** consistent with Article 2, Section 2.7. It removes IP from the Fundamental Representations, which is the opposite of what Article 2 describes.

**Why it matters to Nodix:**

If an Authorized Officer signed the KEA with Section 7.4 included without specific board authorization for that change, the execution may be ultra vires the board's grant of authority. This does not necessarily void the amendment (the counterparty may still be bound), but it creates internal governance exposure for the signing officer and potentially for the board. It also weakens Nodix's position if it later seeks to argue that the amendment should not be given effect.

**Recommended fix:**

1. **Identify who signed** the KEA on Nodix's behalf and confirm whether that person understood Section 7.4's effect before signing.
2. **Board ratification or corrective action:** Present the issue to the board. Options include (a) ratifying the amendment if the board determines it is acceptable, or (b) directing management to negotiate its removal.
3. **Document the board's awareness:** If the board did not specifically approve Section 7.4, this should be noted in the minutes to create a record that supports any later challenge to the amendment's validity.

**Flag to client:** This is an internal governance issue that the client's General Counsel and Corporate Secretary should address promptly. It does not require Seller's cooperation, but it does require board-level attention.

---

## Issue 4 (Moderate): Mismatch Between Seller Non-Compete Duration (5 Years) and Employee Non-Compete Duration (Employment + 24 Months)

**Where it appears:**
- APA, Section 6.4 (5-year Restricted Period for Seller)
- KEA, Section 1.1 ("Restricted Period" = employment + 24 months post-termination)
- Board Consent, Section 2.8 (describes 5-year Seller non-compete) and Section 2.10 (describes 24-month post-employment period for Dr. Raskova)

**What the issue is:**

The APA binds Sonox (the entity) for 5 years post-closing. The KEA binds Dr. Raskova (the individual) for only the duration of her employment plus 24 months. Because her employment is at-will, the total restriction could be as short as 24 months (if she is terminated or resigns immediately post-closing) or as long as many years (if she remains employed).

The board consent appears to have approved both durations as stated (Sections 2.8 and 2.10), so this may be a negotiated outcome rather than an error. However, the practical effect is that there is a significant gap: after Dr. Raskova's 24-month post-employment restriction expires (potentially as early as October 30, 2028), Sonox is still bound by its 5-year restriction (until October 30, 2031). But as noted in Issue 2, Sonox is a dormant entity, and Dr. Raskova's personal restriction is narrower in scope anyway.

**Why it matters to Nodix:**

The 5-year entity non-compete is of limited practical value if the entity has no operations and the principal (Dr. Raskova) is only personally restricted for a shorter period and in a narrower scope. Nodix's real protection against Dr. Raskova competing is the KEA non-compete, which may expire well before the APA non-compete.

**Recommended fix:**

This is less clearly an "error" than Issues 1–3, as the board consent describes both durations. However, if the client is not comfortable with the gap, options include:
1. Negotiate an extension of the KEA Restricted Period (e.g., to 36 or 48 months post-termination).
2. Add a provision that if Dr. Raskova's employment ends before a specified date (e.g., the second anniversary), the Restricted Period is extended to ensure a minimum total restriction period.
3. Rely on the combination of the narrow-scope issue (Issue 2) fix and the duration to create adequate protection.

**Flag to client:** Confirm whether the 24-month post-employment period was a deliberate business decision or whether the client expected longer protection given the 5-year entity covenant.

---

## Issue 5 (Moderate): FAA Certificates Included Only "To the Extent Transferable"

**Where it appears:**
- APA, Section 2.1(e)
- Board Consent, Section 2.3 and Section 3.5
- Press Release, Section 2

**What the issue is:**

APA Section 2.1(e) includes in the Purchased Assets "all FAA certificates, waivers and exemptions held by Seller, **to the extent transferable**." This qualifier means Nodix may not receive all FAA authorizations. Some FAA certificates (particularly operational waivers) are personal to the holder and require a new application by the transferee.

Board Consent Section 3.5 authorizes officers to "prepare, execute and file all notices, applications and filings with any Governmental Authority, including the Federal Aviation Administration, needed to transfer or reissue the FAA certificates." This contemplates that some will need to be reissued.

The press release states that Nodix acquired "its transferable Federal Aviation Administration certificates, waivers and exemptions" – accurately reflecting the "to the extent transferable" limitation.

**Why it matters to Nodix:**

If key FAA waivers (e.g., for beyond-visual-line-of-sight operations, night operations, or operations over people) cannot be transferred and must be reissued, there may be a gap in Nodix's operational authority post-closing. During the reapplication period, Nodix may be unable to operate certain Sonox products in the same manner. This could affect customer contracts and revenue.

**Recommended fix:**

1. **Confirm status:** Determine which FAA certificates, waivers, and exemptions were actually transferred at closing versus which require reapplication. This information should be in the Disclosure Schedule (APA § 4.10) or in the closing deliverables.
2. **Track reapplications:** Ensure that all necessary FAA reapplications have been filed and monitor their status. The board consent authorizes the General Counsel to handle this.
3. **Customer communication:** If any operational gaps exist, confirm that the customer communication described in the press release (Section 4) addresses any temporary service limitations.

**Flag to client:** This is an operational/regulatory matter rather than a legal defect in the documents. The client should confirm that the FAA transition plan is on track and that no critical waivers have lapsed or are in limbo.

---

## Issue 6 (Lower): Press Release Lists Sonox as a Post-Closing Media Contact

**Where it appears:**
- Press Release, Section 8 (Media Contacts)

**What the issue is:**

The press release lists two media contacts: Nodix Corporate Communications and "Sonox AgroDrone LLC, Attention: Dr. Raskova." Post-closing, Sonox is a dormant entity that has sold substantially all its assets. Dr. Raskova is now a Nodix employee (CTO, Agricultural Systems). Listing her as a Sonox contact is confusing and could create the impression that Sonox continues to operate independently.

**Why it matters to Nodix:**

This is a minor issue. The primary risk is confusion among customers, dealers, or the media about the corporate structure post-closing. It could also create an awkward situation if Dr. Raskova's employment with Nodix ends and she is still listed as a Sonox contact.

**Recommended fix:**

If the press release has not yet been widely distributed, consider issuing a corrected version with only the Nodix media contact. If it has already been distributed, no action is likely necessary, but the client's communications team should be aware of the inconsistency.

---

## Issue 7 (Lower): Press Release Describes Acquisition of "Substantially All of the Assets of Sonox" While APA Is More Precise

**Where it appears:**
- Press Release, Section 1
- APA, Section 2.1 and Recital C

**What the issue is:**

The press release states Nodix acquired "substantially all of the assets of Sonox AgroDrone LLC." The APA is more precise: it transfers "all of Seller's right, title and interest in all assets, properties and rights used or held for use in the Business" (APA § 2.1), with specific exclusions in Section 2.2 (cash, organizational documents, non-assigned contracts, employee benefit plans).

The press release's language is broader than the APA's. If Sonox holds assets not "used or held for use in the Business," those were not acquired, but the press release's language could imply they were.

**Why it matters to Nodix:**

This is unlikely to create a legal issue, but if there is ever a dispute about what was included in the acquisition, the press release's broader language could be cited by a counterparty (e.g., a creditor of Sonox) to argue that more assets were transferred than actually were.

**Recommended fix:**

No action required unless a dispute arises. If the client wants to be precise, future communications should use the APA's formulation ("substantially all of the assets used or held for use in the Business").

---

## Issues I Could Not Resolve from the Documents Alone

1. **Disclosure Schedule contents.** The APA references multiple sections of the Disclosure Schedule (Sections 4.3, 4.7, 4.9, 4.10, 4.12). I do not have the Disclosure Schedule and therefore cannot confirm: (a) which specific FAA certificates and waivers are listed, (b) which patents and patent applications are claimed, (c) whether any consents are required for Assigned Contracts, or (d) whether any employees other than Dr. Raskova are listed. If the client can provide the Disclosure Schedule, I can cross-check the representations against it.

2. **Whether the KEA was actually executed with Section 7.4 included.** The documents in the folder appear to be execution copies (signature blocks are blank in the APA and board consent, but the press release confirms closing occurred). I am assuming the KEA was signed as drafted, including Section 7.4. If there was a side letter or different version signed, the analysis would change.

3. **Identity of the Authorized Officer who signed.** The board consent authorizes both the CEO and CFO to sign. I do not know which one actually executed the KEA, or whether the signer was aware of Section 7.4's effect.

4. **Status of FAA reapplications.** I cannot determine from these documents whether the necessary FAA filings have been made or are pending.

---

## Items to Raise with the Client Before We Act

1. **Was the board aware of KEA Section 7.4?** This is the threshold question. If the board approved the deal understanding that IP was a Fundamental Representation (as Section 2.7 of the consent states), and Section 7.4 was inserted without board knowledge, we need to decide whether to (a) seek to undo the amendment, (b) seek a ratifying board action, or (c) accept the reduced protection and adjust our post-closing monitoring accordingly.

2. **Was the narrow "Business" definition in the KEA intentional?** If it was a drafting error, we should move quickly to amend it while Dr. Raskova is still employed and the relationship is cooperative. If it was a negotiated point, we need to understand the client's risk tolerance for the gap in non-compete protection.

3. **What is the client's posture now that the deal has closed?** The press release confirms closing on October 30, 2026. The client is now in the post-closing period. Any amendments to the APA or KEA will require Seller's/Dr. Raskova's cooperation. We should assess the client's leverage (e.g., Dr. Raskova's retention bonus installments are still outstanding – $375,000 due on each of the first and second anniversaries) and her motivation to cooperate.

4. **Has any IP issue already surfaced?** Given that the 18-month survival clock (if Issue 1 is not fixed) runs from October 30, 2026, Nodix has until approximately April 30, 2028 to assert IP-related indemnification claims. The client should confirm whether any IP diligence issues were identified pre-closing that might give rise to a claim within that window.

---

## Recommended Next Steps (Priority Order)

| Priority | Action | Deadline Consideration |
|---|---|---|
| 1 | Confirm with client whether board was aware of KEA § 7.4 | Immediate |
| 2 | If board was not aware, present to board for ratification or directive to negotiate | Before next board meeting |
| 3 | Send letter to Seller/Dr. Raskova seeking amendment of KEA § 7.4 (restore IP as Fundamental Rep) and KEA § 1.1 (broaden "Business" definition) | Within 30 days |
| 4 | Confirm FAA certificate transfer status with General Counsel's regulatory team | Within 30 days |
| 5 | Calendar the 18-month IP claim deadline (April 30, 2028) and the 18-month general rep survival deadline (April 30, 2028) | Immediate |
| 6 | Calendar Dr. Raskova's first retention bonus payment date (October 30, 2027) as a leverage point for negotiations | Advance notice |