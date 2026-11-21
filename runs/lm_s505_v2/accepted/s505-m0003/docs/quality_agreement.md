# QUALITY AGREEMENT

This Quality Agreement (this "**Quality Agreement**") is entered into as of January 15, 2025 (the "**QA Effective Date**") by and between **Lebun Interactive, Inc.**, a Delaware corporation ("**Customer**"), and **Draibouth Studios LLC**, a Delaware limited liability company ("**Provider**"). Customer and Provider are each a "**Party**" and together the "**Parties**."

## RECITALS

A. Customer and Provider are parties to a Master Services Agreement dated as of January 15, 2025 (the "**Agreement**"). Under the Agreement, Provider performs game quality assurance testing, localization and live-operations support services for Customer under Order Forms.

B. Sections 2.1, 6.1 and 6.2 of the Agreement require Provider to perform the Services and deliver Deliverables in accordance with this Quality Agreement. They also make acceptance and rejection of Deliverables subject to the procedures in this Quality Agreement.

The Parties therefore agree as follows:

## 1. SCOPE

1.1 **Application.** This Quality Agreement sets out the quality standards, Delivery requirements, acceptance and rejection procedures and defect classification that apply to all Deliverables, including Builds, under every Order Form.

1.2 **Relationship to the Agreement.** This Quality Agreement forms part of the Agreement. Capitalized terms used but not defined in this Quality Agreement have the meanings given to them in the Agreement.

## 2. DEFINITIONS

2.1 **Defined Terms.** In this Quality Agreement:

"**Acceptance Criteria**" means the criteria stated in the applicable Order Form for a Deliverable, together with the quality standards in Section 3 and the defect thresholds in Section 6.

"**Defect**" means any failure of a Deliverable to conform to its Acceptance Criteria, its specifications in the applicable Order Form, or the requirements of a platform holder identified in that Order Form.

"**Delivery**" means, for a Build, the upload of the complete Build to the Delivery Portal together with the Delivery Package described in Section 4.2. For any other Deliverable, it means transmission of the complete Deliverable to Customer's designated quality contact by the Delivery Portal or by email. Delivery occurs on the date Provider's Delivery notice under Section 4.3 is sent. "**Delivered**" has a corresponding meaning.

"**Delivery Package**" has the meaning given in Section 4.2.

"**Delivery Portal**" means the access-controlled file transfer system that Customer designates for receipt of Builds and other Deliverables, or any replacement system that Customer designates by written notice.

"**Milestone**" means a milestone stated in an Order Form, including any alpha, beta, release candidate or gold master milestone.

"**Rejection Notice**" has the meaning given in Section 5.2.

"**Severity Level**" means the classification of a Defect under Section 6.1.

2.2 **Days.** Unless this Quality Agreement states "business days," references to days are to calendar days.

## 3. QUALITY STANDARDS

3.1 **General Standard.** Provider shall perform all Services and prepare all Deliverables in accordance with Section 3.1 of the Agreement, the Acceptance Criteria and this Quality Agreement.

3.2 **Test Coverage.** For each Customer Title, Provider shall prepare a test plan that identifies the features, platforms, hardware configurations, languages and game modes to be tested. Provider shall submit the test plan to Customer for approval before testing begins. Provider shall execute all test cases in the approved test plan for each Build it Delivers, and record the results in the bug database that Customer designates.

3.3 **Bug Reporting.** Each Defect report must include a unique identifier, a summary, reproduction steps, a reproduction rate, the affected platform and Build version, the proposed Severity Level, and supporting screenshots, video or logs where available. Provider shall enter Defect reports in the designated bug database within the response times in the Service Level Schedule.

3.4 **Regression Testing.** Before Delivering any Build that incorporates fixes, Provider shall regression test every Defect marked as fixed in that Build and verify that the fix has not introduced new Defects in related features.

3.5 **Certification Pre-Checks.** For any Build to be submitted to a platform holder, Provider shall complete a pre-check against that platform holder's current technical requirements checklist. Provider shall report all failures in the Delivery Package.

## 4. DELIVERY

4.1 **Delivery Method.** Provider shall Deliver each Build through the Delivery Portal. Provider shall not deliver Builds by removable media, public file-sharing services or any other method unless Customer approves it in writing in advance.

4.2 **Delivery Package.** Each Build must be accompanied by a delivery package (the "**Delivery Package**") that includes:

(a) the Build version number and target platforms;

(b) release notes identifying new content, changes and fixes since the previous Build;

(c) a list of all known open Defects, by Severity Level;

(d) a summary of test results against the approved test plan, including test case pass rates;

(e) the results of any certification pre-check under Section 3.5; and

(f) for localized Builds, the linguistic quality assurance report described in Section 7.3.

4.3 **Delivery Notice.** When Provider has uploaded a Build and its Delivery Package, Provider shall notify Customer's designated quality contact by email that the Build is available on the Delivery Portal. The notice must identify the Order Form, the Milestone (if any) and the Build version number.

4.4 **Incomplete Delivery.** If Provider uploads a Build without a Delivery Package that meets Section 4.2, Customer may notify Provider of the missing items within three (3) business days after the Delivery notice. In that case, Delivery occurs when Provider supplies the missing items.

## 5. ACCEPTANCE AND REJECTION

5.1 **Acceptance Testing.** After Delivery, Customer may test and review each Deliverable to determine whether it meets its Acceptance Criteria. Customer may perform the testing itself, through its Affiliates or through a platform holder's submission process. Provider shall give Customer reasonable assistance with acceptance testing at no additional charge.

5.2 **Rejection; Deemed Acceptance.** Customer may reject a Build or other Deliverable that does not meet its Acceptance Criteria by giving Provider written notice of rejection within fifteen (15) days after Delivery (the "**Rejection Period**"). The Rejection Period therefore ends 15 calendar days after Delivery. The notice must identify the Defects that are the grounds for rejection in reasonable detail, by reference to the bug database where applicable (a "**Rejection Notice**"). Customer may accept a Deliverable at any time during the Rejection Period by written notice. If Customer does not give a Rejection Notice within the Rejection Period, the Deliverable is deemed accepted on the last day of the Rejection Period. Once a Deliverable is accepted or deemed accepted:

(a) any milestone Fee related to that Deliverable becomes payable and may be invoiced under Section 5.1 of the Agreement; and

(b) Customer's remedies for any Defect in that Deliverable are limited to the warranty remedies in Sections 11.2(b) and 11.3 of the Agreement.

5.3 **Remediation.** If Customer gives a timely Rejection Notice, Provider shall correct the Defects identified in it and re-Deliver the corrected Deliverable within ten (10) days after receiving the Rejection Notice, or within any longer period that Customer agrees in writing. For a Severity 1 Defect, Provider shall begin remediation within twenty-four (24) hours after receiving the Rejection Notice.

5.4 **Re-Delivered Deliverables.** Sections 5.1 and 5.2 apply to each re-Delivered Deliverable. For a re-Delivered Deliverable, Customer's review may be limited to the Defects identified in the earlier Rejection Notice and any Defects introduced by the correction.

5.5 **Repeated Rejection.** If Customer rejects the same Deliverable a second time on the basis of a timely Rejection Notice, Customer may, at its option and by written notice, (a) require Provider to remediate again under Section 5.3; (b) accept the Deliverable subject to an equitable reduction of the related Fees agreed by the Parties in writing; or (c) treat the failure as a material breach of the applicable Order Form for the purposes of Section 15.2 of the Agreement.

5.6 **Milestone Dates.** Acceptance or deemed acceptance of a Deliverable does not relieve Provider of any liability for late Delivery against a Milestone date stated in the applicable Order Form.

## 6. DEFECT CLASSIFICATION

6.1 **Severity Levels.** Defects are classified as follows:

| **Severity Level** | **Description** |
|---|---|
| Severity 1 – Critical | Crash, freeze, data loss, save corruption, security vulnerability, or failure of a platform holder mandatory requirement that would block certification or release. |
| Severity 2 – Major | Loss of a core feature or game mode, progression blocker with no reasonable workaround, or material localization error affecting gameplay, legal text or age-rating content. |
| Severity 3 – Moderate | Feature malfunction with a reasonable workaround, significant visual or audio error, or localization error affecting comprehension. |
| Severity 4 – Minor | Cosmetic, typographical or minor visual or audio issue that does not affect gameplay or comprehension. |

6.2 **Classification Disputes.** Provider shall propose a Severity Level for each Defect it reports. Customer's quality contact may reclassify any Defect by notice in the bug database, and Customer's classification controls for purposes of acceptance.

6.3 **Release Thresholds.** Unless the applicable Order Form states otherwise, a release candidate or gold master Build does not meet its Acceptance Criteria if it contains any known open Severity 1 or Severity 2 Defect, or more than ten (10) known open Severity 3 Defects.

## 7. LOCALIZATION QUALITY

7.1 **Linguistic Standards.** Localized Deliverables must be accurate, complete and consistent with Customer's approved glossaries, style guides and translation memories. They must also comply with the legal and age-rating requirements of each target market that Customer identifies in the applicable Order Form.

7.2 **Review.** Provider shall have each localized Deliverable reviewed by a second qualified linguist who is a native speaker of the target language and who did not perform the original translation.

7.3 **LQA Report.** For each localized Build, Provider shall prepare a linguistic quality assurance report that lists in-context issues found, by language and Severity Level, and their status.

## 8. QUALITY MANAGEMENT AND RECORDS

8.1 **Quality Contacts.** Each Party shall designate a quality contact and notify the other Party of any change in writing. Customer's quality contact receives Delivery notices under Section 4.3.

8.2 **Quality Reviews.** The quality contacts shall meet at least monthly, by video conference or in person, to review Defect trends, test coverage, open corrective actions and any matters raised in the monthly reports under Section 7.3 of the Agreement.

8.3 **Corrective Action.** If Customer identifies a recurring quality failure, Provider shall deliver a written corrective action plan within ten (10) business days after Customer's request and shall implement the plan as approved by Customer.

8.4 **Records.** Provider shall keep complete records of test plans, test execution results, Delivery Packages, Delivery notices and Defect reports for each Customer Title for at least three (3) years after the final Delivery under the applicable Order Form. Provider shall make them available to Customer on request.

8.5 **Quality Audits.** On ten (10) business days' prior written notice and no more than twice in any twelve (12) month period, Customer or its designee may audit Provider's facilities, processes and records for compliance with this Quality Agreement. Provider shall correct any non-compliance identified in an audit within a reasonable period agreed with Customer.

## 9. TERM

9.1 **Term.** This Quality Agreement takes effect on the QA Effective Date and remains in effect for as long as the Agreement or any Order Form remains in effect.

9.2 **Survival.** Sections 5.2, 5.6 and 8.4 survive termination or expiration of this Quality Agreement for any Deliverable Delivered before termination or expiration.

## 10. GENERAL

10.1 **Amendment.** This Quality Agreement may be amended only by a written instrument signed by both Parties.

10.2 **Notices.** Rejection Notices and other notices under Section 5 must be in writing and given to Provider's quality contact by email, with a copy sent in accordance with Section 17.3 of the Agreement. Delivery notices and other operational communications under Sections 3, 4, 6 and 8 may be given by email or through the designated bug database.

10.3 **Governing Law.** This Quality Agreement is governed by the laws of the State of Delaware, without regard to its conflict of laws principles. Section 17.2 of the Agreement applies to any action arising out of or relating to this Quality Agreement.

10.4 **Counterparts.** This Quality Agreement may be signed in counterparts, including by electronic signature. Each counterpart is an original, and together they form one instrument.

---

**IN WITNESS WHEREOF**, the Parties have signed this Quality Agreement as of the QA Effective Date.

| **LEBUN INTERACTIVE, INC.** | **DRAIBOUTH STUDIOS LLC** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: | Name: |
| Title: | Title: |
| Quality Contact: | Quality Contact: |