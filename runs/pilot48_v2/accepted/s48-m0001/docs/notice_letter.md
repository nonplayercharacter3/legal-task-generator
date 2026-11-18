**STUTIND SOLAR INSTALLATIONS, LLC**

**August 24, 2026**

**BY EMAIL AND OVERNIGHT COURIER**

Zikeiv Software, Inc.
Attention: General Counsel

With a copy to:
Zikeiv Software, Inc.
Attention: Project Manager, Statement of Work No. 1 (Permitting Automation Module)

**Re: Statement of Work No. 1 (Permitting Automation Module) dated January 15, 2026 under the Software License Agreement dated January 15, 2026 between Zikeiv Software, Inc. and Stutind Solar Installations, LLC; Notice of Nonconformity and Rejection of Deliverable D-2**

Dear Counsel:

We write on behalf of Stutind Solar Installations, LLC ("**Licensee**") about Statement of Work No. 1 (the "**SOW**"). The SOW was issued under the Software License Agreement between Zikeiv Software, Inc. ("**Licensor**") and Licensee dated January 15, 2026 (the "**Agreement**"). Capitalized terms used but not defined in this letter have the meanings given in the SOW or the Agreement.

## 1. Background

**1.1 Delivery.** Licensor delivered Deliverable D-2, the Permitting Automation Module (the "**Module**"), to the Licensee test environment. Licensor's Delivery Confirmation dated August 3, 2026 confirmed that the Module was available for acceptance testing.

**1.2 Testing.** Licensee's permitting coordinators and design staff then tested the Module against the Acceptance Criteria in the Functional Specification approved under Milestone 1. They used test cases built from those Acceptance Criteria, as Section 4.3 of the SOW requires. Testing covered each authority having jurisdiction listed in Schedule A to the SOW. It used project files drawn from Licensee's current residential and commercial pipeline.

## 2. Notice of Nonconformity

Under Section 5.2 of the SOW, Licensee gives Licensor written notice that the Module does not meet its Acceptance Criteria in the material respects described below. Licensee's test logs, screenshots and sample output files for each item have been uploaded to the shared project folder. They are labeled with the reference numbers below.

**2.1 NC-01: Plan set assembly fails for multi-array systems (all Schedule A jurisdictions).**

*Steps to reproduce:*
1. Open any HelioPlan Design project with two or more roof arrays on different azimuths.
2. Select "Generate Permit Package" in the Module.

*Result:* The Module generates a single-line diagram showing only the first array, and the module and string counts on the plan set do not match the design. 31 of 44 multi-array test projects failed. Accurate plan sets for multi-array systems are an Acceptance Criterion in Section 4.1 of the Functional Specification.

**2.2 NC-02: Structural attachment details omitted (City of Phoenix, City of Scottsdale, City of Tucson).**

*Steps to reproduce:* Generate a permit package for any project in these jurisdictions where the roof type is concrete tile.

*Result:* The Module omits the structural attachment detail sheet, which each of these jurisdictions requires. The jurisdiction-specific validation rule does not flag the missing sheet before submission. This fails Acceptance Criteria 4.3 and 5.2.

**2.3 NC-03: Incorrect application form population (Clark County, City of Henderson, City of North Las Vegas).**

*Steps to reproduce:* Generate a permit package for any project in these jurisdictions where the contractor license field is populated from Licensee's CRM record.

*Result:* The Module fills the Nevada contractor license number into the electrical permit number field. It leaves the license number field blank. Packages in this condition would be rejected at intake. This fails Acceptance Criterion 5.1 (automated population of permit application forms).

**2.4 NC-04: Export format errors (Maricopa County, Pima County, City of Las Vegas).**

*Steps to reproduce:* Export a completed permit package for any project in these jurisdictions.

*Result:* The Module exports a single combined PDF. Each of these jurisdictions requires separately bookmarked PDF files with set file-naming conventions. For Maricopa County, the exported files also exceed the portal's file-size limit. This fails Acceptance Criterion 6.1.

**2.5 NC-05: CRM integration does not return permit status.**

*Steps to reproduce:* Generate a package for any project linked to a CRM opportunity, then check the opportunity record.

*Result:* The permit package status is not written back to the CRM opportunity record through the HelioPlan Integrations connector. This fails Acceptance Criterion 7.2 and the integration requirement in Section 3.1(d) of the SOW.

**2.6 NC-06: Validation rules produce false "ready to submit" status.**

*Steps to reproduce:* Generate a package for any commercial project over 100 kW in the City of Mesa, City of Chandler or Town of Gilbert.

*Result:* The Module marks the package "ready to submit" even though the required fire department access plan and rapid shutdown labeling sheet are missing. This fails Acceptance Criterion 5.2.

## 3. Rejection

**3.1 Rejection.** For the reasons stated in Section 2, Licensee hereby rejects Deliverable D-2. The Module does not meet its Acceptance Criteria, and Licensee does not accept Deliverable D-2.

**3.2 No Acceptance.** Licensee does not agree that Deliverable D-2 has been accepted, whether deemed or otherwise. Licensee has not used the Module in production, and nothing in its testing or other conduct should be treated as acceptance.

**3.3 Correction and Redelivery.** Under Section 5.3 of the SOW, Licensee requests that Licensor correct each Nonconformity described in Section 2. Licensor should then redeliver Deliverable D-2 with a new Delivery Confirmation. Licensee asks that Licensor's Project Manager provide a written correction plan and target redelivery date before the next status meeting under Section 7.2 of the SOW.

## 4. Milestone 2 Fee

**4.1 Withholding.** Acceptance of Deliverable D-2 under Section 5 of the SOW has not occurred, so the payment event for Milestone 2 has not occurred. Licensee will withhold payment of the Milestone 2 fee of $148,000.

**4.2 Disputed Invoice.** If Licensor issues an invoice for the Milestone 2 fee, this letter is Licensee's written notice of dispute under Section 6.4 of the Agreement, as applied to the SOW Fees by Section 6.4 of the SOW. The basis of the dispute is set out in Sections 2 and 3 of this letter. Licensee will work with Licensor in good faith to resolve the dispute.

## 5. Reservation of Rights

Licensee reserves all of its rights and remedies under the SOW and the Agreement, including its rights under Section 5.4 of the SOW and Section 13.3 of the Agreement. No delay or omission by Licensee in exercising any right waives that right.

## 6. Contacts

Please direct technical questions about the Nonconformities to Licensee's Project Manager under the SOW. Please send all formal correspondence about this letter to the undersigned at the notice address stated on the Agreement signature page, as Section 15.1 of the Agreement requires.

We look forward to Licensor's prompt response.

Sincerely,

**STUTIND SOLAR INSTALLATIONS, LLC**

By: ______________________________
Name: ____________________________
Title: Chief Executive Officer

cc: Stutind Solar Installations, LLC, Director of Operations
Stutind Solar Installations, LLC, Project Manager, Statement of Work No. 1
Zikeiv Software, Inc., Enterprise Account Executive, Southwest Region