# WASHLOOP QUALITY AGREEMENT

**Release Testing, Delivery and Acceptance: WashLoop Plant Management, RFID Garment-Tracking and Route-Dispatch Software**

This WashLoop Quality Agreement (this "**Quality Agreement**") is entered into as of January 15, 2026 by and between:

**Voupourt Software, LLC**, a Delaware limited liability company with its principal place of business at 2100 Harrow Court, Suite 400, Wilmington, Delaware 19801 ("**Licensor**"); and

**Tailosk Linen & Uniform Services, Inc.**, a Delaware corporation with its principal place of business at 875 Millrace Avenue, Columbus, Ohio 43215 ("**Licensee**").

Licensor and Licensee are each referred to as a "**party**" and together as the "**parties**."

## RECITALS

A. Licensor and Licensee are parties to a Software License Agreement dated as of January 15, 2026 (the "**Agreement**"). Under the Agreement, Licensor licenses its WashLoop software platform to Licensee and provides related Implementation Services, Support Services and hosting.

B. Section 4.4 of the Agreement provides that delivery, testing and acceptance of the Production Release and later releases of the Software are governed by the Quality Agreement. Order Form No. 001 ties an Implementation Fee milestone to acceptance of the Production Release under the Quality Agreement.

C. The parties are entering into this Quality Agreement to set out the quality controls, testing responsibilities, delivery mechanics and acceptance procedure for releases of the Software.

The parties therefore agree as follows:

## 1. DEFINITIONS AND INTERPRETATION

**1.1 Defined Terms.** Capitalized terms used but not defined in this Quality Agreement have the meanings given to them in the Agreement. The following terms have the following meanings in this Quality Agreement:

"**Acceptance**" means acceptance of the Production Release under Section 5.5, or deemed acceptance under Section 5.3.

"**Acceptance Certificate**" means a certificate substantially in the form of Schedule 2, signed by Licensee's project lead.

"**Acceptance Criteria**" means the criteria set out in Schedule 1. Those criteria are measured against the Documentation and the functional requirements in Schedule 3 to Order Form No. 001.

"**Acceptance Testing**" means the testing of the Production Release that Licensee carries out under Section 5.2.

"**Defect**" means a failure of a release of the Software to conform to the Documentation, the functional requirements in Schedule 3 to Order Form No. 001 or the Acceptance Criteria.

"**Delivery Date**" means the date on which Licensor makes the Production Release available to Licensee in the production environment and gives Licensee a Delivery Notice for it.

"**Delivery Notice**" means a written notice from Licensor under Section 5.1 confirming that the Production Release has been delivered.

"**Release**" means the Production Release, any corrected Production Release delivered under Section 5.4, and any Update delivered after Acceptance.

"**Rejection Notice**" has the meaning given in Section 5.3.

"**Release Notes**" means the written notes that accompany each Release. They describe its contents, the Defects corrected, known open Defects and any configuration steps Licensee must take.

"**Severity Level**" means a severity level assigned in accordance with Section A.2 of Exhibit A to the Agreement.

"**Test Environment**" means the non-production testing environment of the Software provided under Section 9.1(b) of Order Form No. 001.

"**Test Scripts**" means the test scripts for the core workflows of each Software module that Licensor provides under Section S2.6 of Schedule 2 to Order Form No. 001.

**1.2 Interpretation.** Section 1.2 of the Agreement applies to this Quality Agreement as if set out in full in it, with references to "this Agreement" read as references to this Quality Agreement where the context requires. Unless otherwise stated, references in this Quality Agreement to numbered Sections and Schedules are to sections of and schedules to this Quality Agreement. References to Sections of the Agreement or of Order Form No. 001 are identified as such.

## 2. SCOPE

**2.1 Releases Covered.** This Quality Agreement applies to the following:

(a) the Production Release of the Software configured for the Initial Plants under Order Form No. 001;

(b) any corrected Production Release delivered under Section 5.4; and

(c) Updates delivered to the production environment after Acceptance, to the extent set out in Section 6.

**2.2 Relationship to Implementation.** The implementation project plan agreed by the parties sets the milestones for delivery of the Production Release. This Quality Agreement governs how each Release is tested, delivered and accepted. It does not change the scope of the Implementation Services described in Order Form No. 001.

**2.3 Additional Plants.** Where an Order Form or a written amendment adds a Plant, the configuration and releases of the Software for that Plant are tested, delivered and accepted under this Quality Agreement, with such changes to the Acceptance Criteria as the parties agree in writing.

## 3. QUALITY MANAGEMENT

**3.1 Licensor Quality System.** Licensor shall maintain a documented software quality management system covering requirements management, design review, source code control, peer code review, build and release management, regression testing and defect tracking. Licensor shall apply that system to every Release.

**3.2 Secure Development.** Licensor shall develop and test each Release in accordance with the secure software development practices described in Section 7.4 of the Agreement and Exhibit B to the Agreement. Before delivering a Release, Licensor shall scan it for known vulnerabilities. Licensor shall not deliver a Release that contains an unremediated critical vulnerability.

**3.3 Quality Representatives.** Each party shall appoint a quality representative within ten (10) Business Days after the date of this Quality Agreement. Licensor's quality representative shall be responsible for Licensor's pre-delivery testing and the Release Notes. Licensee's quality representative shall coordinate Acceptance Testing. Either party may replace its quality representative by notice to the other party's project lead.

**3.4 Personnel.** Licensor shall staff its testing activities with personnel familiar with the Software and with commercial laundry workflows, including soil sort, tunnel washing, finishing, clean-side assembly and route operations. Section 4.2 of the Agreement applies to those personnel.

## 4. PRE-DELIVERY TESTING BY LICENSOR

**4.1 System and Integration Testing.** Before delivering the Production Release, Licensor shall carry out the following testing in the Test Environment:

(a) system testing of each Software module against the Documentation and the functional requirements in Schedule 3 to Order Form No. 001;

(b) integration testing of the standard WashLoop connectors described in Section 4.2 of Order Form No. 001, using test data agreed with Licensee;

(c) RFID read-processing testing using the tunnel-reader and handheld-scanner models installed at the Initial Plants;

(d) offline-operation and synchronization testing of the WashLoop Driver mobile application on the device models identified in the implementation project plan;

(e) performance testing at the licensed quantities in Section 3.2 of Order Form No. 001; and

(f) regression testing of all previously tested functions.

**4.2 Migrated Data.** Licensor shall validate migrated data in accordance with Section S2.5 of Schedule 2 to Order Form No. 001 before delivery. Licensor shall deliver the reconciliation report to Licensee no later than the Delivery Date.

**4.3 Test Data.** Licensor shall not load Customer Data into the Test Environment except with Licensee's prior written consent under Section 9.3 of Order Form No. 001. Where consent is not given, Licensor shall test with synthetic data that reflects the volumes and structure of Licensee's operations.

**4.4 Test Reports.** Licensor shall deliver to Licensee a pre-delivery test report at least five (5) Business Days before the planned Delivery Date. The report shall summarize the tests run, the results, the Defects found and their status, and any Defects that will remain open on delivery, with their Severity Levels.

**4.5 Delivery Readiness.** Licensor shall not deliver the Production Release while any Severity 1 or Severity 2 Defect identified in its pre-delivery testing remains open, unless Licensee's project lead agrees in writing.

## 5. DELIVERY AND ACCEPTANCE OF THE PRODUCTION RELEASE

**5.1 Delivery.** Licensor shall deliver the Production Release by deploying it to the production environment in the Hosted Environment and giving Licensee a Delivery Notice. The Delivery Notice shall be sent to Licensee's project lead and quality representative, with a copy to Licensee's notice address under Section 17.1 of the Agreement. It shall state the Release identifier and be accompanied by the Release Notes and the final pre-delivery test report.

**5.2 Acceptance Testing.** From the Delivery Date, Licensee may carry out Acceptance Testing of the Production Release against the Acceptance Criteria. Licensee may use the Test Scripts and any additional tests it reasonably designs. Licensor shall provide reasonable support during Acceptance Testing, including the attendance of its implementation manager at test sessions on request and the response times in Exhibit A to the Agreement for any Defect reported. Licensee may carry out Acceptance Testing at one or more Initial Plants, including through parallel processing against its existing systems.

**5.3 Rejection.** Licensee may reject the Production Release by written notice to Licensor that identifies in reasonable detail each Acceptance Criterion that the Production Release fails to meet (a "**Rejection Notice**"), given within fifteen (15) Business Days after the Delivery Date. If Licensee gives a Rejection Notice in accordance with this Section 5.3, Licensee may, at its election stated in the Rejection Notice or by later notice, either (a) require Licensor to correct and redeliver the Production Release under Section 5.4, or (b) recover from Licensor all Implementation Fees paid under Order Form No. 001, which Licensor shall refund within thirty (30) days after Licensee's election. If Licensee does not give a Rejection Notice within that period, the Production Release is deemed accepted on the last day of that period. Following deemed acceptance, Licensee's remedy for any failure of the Production Release to meet the Acceptance Criteria is re-performance and correction under Sections 11.2 and 11.3 of the Agreement.

**5.4 Correction and Redelivery.** Where Licensee requires correction under Section 5.3(a), Licensor shall correct the Defects identified in the Rejection Notice and redeliver the Production Release within twenty (20) Business Days after the Rejection Notice, at no additional charge. Redelivery is made in accordance with Section 5.1, and Sections 5.2 and 5.3 apply to the redelivered Production Release, with the Delivery Date being the date of the new Delivery Notice. Licensee may make its election under Section 5.3(b) in respect of a redelivered Production Release.

**5.5 Acceptance Certificate.** If Licensee determines during Acceptance Testing that the Production Release meets the Acceptance Criteria, Licensee's project lead shall sign and deliver an Acceptance Certificate to Licensor. Acceptance occurs on the date of the Acceptance Certificate.

**5.6 Open Defects on Acceptance.** Acceptance does not relieve Licensor of its obligation to correct any Defect, whether listed in the Release Notes, recorded in the Acceptance Certificate or found later. Licensor shall correct those Defects within the resolution targets in Exhibit A to the Agreement.

**5.7 Milestone Invoice.** Licensor may issue the invoice for the Implementation Fee milestone described in Section 3.4 of Order Form No. 001 as "Acceptance of the Production Release under the Quality Agreement" on or after Acceptance. The invoice shall be accompanied by a copy of the Acceptance Certificate or, in the case of deemed acceptance, a statement of the Delivery Date.

## 6. UPDATES AFTER ACCEPTANCE

**6.1 Release Schedule.** Licensor shall publish to Licensee, at least quarterly, a schedule of planned maintenance releases and minor and major version releases for the following six (6) months.

**6.2 Advance Availability.** Licensor shall make each minor or major version release available in the Test Environment at least fifteen (15) Business Days before deploying it to the production environment. Licensor shall make each maintenance release available in the Test Environment at least five (5) Business Days before production deployment. Emergency fixes for Severity 1 Defects or critical vulnerabilities may be deployed on shorter notice where Licensor reasonably considers it necessary, and Licensor shall give Licensee as much notice as is practicable.

**6.3 Update Testing.** Licensor shall carry out the testing described in Section 4.1, scaled to the content of the Update, before making it available in the Test Environment. Licensee may test each Update in the Test Environment before production deployment.

**6.4 Deferral.** Where Licensee's testing of a minor or major version release in the Test Environment identifies a Severity 1 or Severity 2 Defect, Licensee may by notice ask Licensor to defer production deployment until the Defect is corrected. Licensor shall not unreasonably refuse a deferral request. Deployments shall be scheduled within the maintenance windows in Section A.5 of Exhibit A to the Agreement and in accordance with Section 5.5 of the Agreement.

**6.5 Rollback.** Licensor shall maintain the ability to roll back each Update in the production environment to the immediately preceding version. If an Update causes a Severity 1 Defect, Licensor shall roll it back on Licensee's request unless Licensor can correct the Defect within the Severity 1 resolution target in Exhibit A to the Agreement.

**6.6 Functionality.** Section 5.2 of the Agreement applies to each Update.

## 7. DEFECT MANAGEMENT

**7.1 Reporting.** Licensee may report Defects through the web-based ticketing portal or the support telephone line described in Exhibit A to the Agreement. Licensee shall assign a Severity Level to each Defect in good faith in accordance with Section A.2 of Exhibit A to the Agreement.

**7.2 Defect Log.** Licensor shall maintain a log of all Defects reported during pre-delivery testing, Acceptance Testing and production use. For each Defect, the log shall record the date reported, the Severity Level, the affected module and Plant, a description, the root cause once known, the corrective action and the date of correction. Licensor shall give Licensee read access to the log through the ticketing portal.

**7.3 Root Cause Analysis.** For each Severity 1 Defect, and for each Severity 2 Defect that recurs within ninety (90) days after correction, Licensor shall deliver a written root cause analysis within ten (10) Business Days after correction. The analysis shall describe the cause, the corrective action taken and the preventive measures adopted.

**7.4 Data Integrity Defects.** Where a Defect affects the integrity of RFID reads, inventory counts, delivered quantities or billing extracts, Licensor shall, in addition to correcting the Defect, identify the affected records and provide a corrected data set or a reconciliation that allows Licensee to correct its records and invoices to Licensee Customers.

## 8. QUALITY RECORDS AND REVIEWS

**8.1 Records.** Licensor shall retain the test plans, test results, pre-delivery test reports, Release Notes, Defect log and root cause analyses for each Release for at least three (3) years after the Release.

**8.2 Quality Reviews.** The parties' quality representatives shall meet quarterly to review Release quality, Defect trends, open Defects by Severity Level and planned Releases. These reviews may be held as part of the quarterly business reviews described in Section A.8 of Exhibit A to the Agreement.

**8.3 Quality Audit.** No more than once in any twelve-month period and on at least thirty (30) days' notice, Licensee may review Licensor's software quality management system and the records described in Section 8.1 as they relate to the Software. Licensee may conduct the review itself or through an independent reviewer bound by confidentiality obligations at least as protective as Section 8 of the Agreement. Licensor may require the review to be conducted remotely or at its offices during normal business hours. A review under this Section 8.3 may be combined with a security assessment under Section 7.5 of the Agreement.

**8.4 Findings.** If a review under Section 8.3 identifies a material non-conformity with Section 3, Licensor shall deliver a corrective action plan within twenty (20) Business Days and implement it in accordance with its timetable.

## 9. CHANGES

**9.1 Changes to Acceptance Criteria.** The Acceptance Criteria may be changed only by written agreement of the parties' project leads, or by a change order signed under Section 4.5 of the Agreement where the change affects the scope of the Implementation Services.

**9.2 Changes to Procedures.** The parties' quality representatives may agree in writing changes to the testing procedures, report formats and meeting arrangements in this Quality Agreement that do not affect Sections 5.3 through 5.5, the Acceptance Criteria or the Fees.

## 10. GOVERNANCE AND ESCALATION

**10.1 Status Reporting.** During the period from the planned Delivery Date until Acceptance, Licensor shall report on testing and Defect status at the weekly implementation status meetings described in Section 7.3 of Order Form No. 001.

**10.2 Escalation.** Any disagreement between the parties on whether a Release meets the Acceptance Criteria, or on the Severity Level of a Defect, shall first be referred to the parties' project leads and then, if unresolved, dealt with under Section 16.2 of the Agreement.

## 11. TERM

**11.1 Term.** This Quality Agreement takes effect on the date first written above and continues for so long as the Agreement remains in effect.

**11.2 Survival.** Sections 5.6, 7.4, 8.1 and 12 survive expiry or termination of this Quality Agreement, together with any rights and obligations accrued before expiry or termination.

## 12. GENERAL

**12.1 Relationship to the Agreement.** This Quality Agreement is the Quality Agreement referred to in Section 1.1 and Section 4.4 of the Agreement.

**12.2 Governing Law and Disputes.** This Quality Agreement and any dispute arising out of or relating to it are governed by the laws of the State of Delaware, without regard to its conflict of laws principles. Sections 16.2 through 16.5 of the Agreement apply to any dispute arising out of or relating to this Quality Agreement.

**12.3 Notices.** Delivery Notices, Rejection Notices and Acceptance Certificates shall be given in writing in accordance with Section 17.1 of the Agreement, with copies to the parties' project leads and quality representatives. Other communications under this Quality Agreement may be given by email between the parties' project leads or quality representatives.

**12.4 Confidentiality.** The terms of this Quality Agreement and all test reports, Defect logs and root cause analyses delivered under it are Confidential Information under Section 8 of the Agreement.

**12.5 Amendment and Waiver.** This Quality Agreement may be amended or waived only in accordance with Section 17.9 of the Agreement, except as provided in Section 9.2.

**12.6 Severability.** If any provision of this Quality Agreement is held invalid or unenforceable, it shall be enforced to the maximum extent permissible and the remaining provisions continue in full force and effect.

**12.7 Assignment.** This Quality Agreement may be assigned only together with the Agreement and in accordance with Section 15.2 of the Agreement.

**12.8 Counterparts and Electronic Signature.** This Quality Agreement may be executed in counterparts, each of which is an original and all of which together constitute one instrument. Signatures delivered by electronic means or in portable document format are as effective as originals.

**IN WITNESS WHEREOF**, the parties have caused this Quality Agreement to be executed by their duly authorized representatives as of the date first written above.

| **VOUPOURT SOFTWARE, LLC** | **TAILOSK LINEN & UNIFORM SERVICES, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: Marcus D. Ellerby | Name: Renata J. Holloway |
| Title: Chief Executive Officer | Title: Chief Operating Officer |
| Date: January 15, 2026 | Date: January 15, 2026 |

---

## SCHEDULE 1 – ACCEPTANCE CRITERIA

**S1.1 General.** The Production Release meets the Acceptance Criteria if each criterion in Sections S1.2 through S1.7 is met, as shown by the Test Scripts and Licensee's Acceptance Testing, and no Severity 1 or Severity 2 Defect remains open.

**S1.2 Plant Management.**

| Ref. | Criterion |
|---|---|
| PM-1 | Soil weights are recorded by Licensee Customer at receiving and sorting at each Initial Plant. |
| PM-2 | Each wash batch is tracked through the tunnel washers and conventional washers, with formula, weight and cycle time recorded. |
| PM-3 | Items are tracked through drying and finishing lines. |
| PM-4 | Cart build is supported by Licensee Customer and delivery location. |
| PM-5 | Production throughput, pounds per operator hour and rewash rates are reported by Plant, shift and line. |

**S1.3 RFID Garment Tracking.**

| Ref. | Criterion |
|---|---|
| RF-1 | Tunnel-reader reads are processed at the throughput rates specified in the Documentation for each Initial Plant's installed reader models. |
| RF-2 | Soil-in and clean-out counts reconcile by Licensee Customer and location, with a read-accuracy rate of at least 99.5% across a sample of not less than 10,000 tagged items. |
| RF-3 | Garment life-cycle and wash-count history is maintained for each tagged item, including migrated items. |
| RF-4 | Items exceeding a configured wash-count threshold are flagged for inspection or retirement. |
| RF-5 | Customer inventory and loss reports are generated by customer, department and item type. |

**S1.4 Route Dispatch.**

| Ref. | Criterion |
|---|---|
| RD-1 | All routes and stops for the Initial Plants are configured, with routes of up to sixty (60) stops each. |
| RD-2 | Daily load sequences are generated by route from clean-side cart build data. |
| RD-3 | Real-time route progress is displayed on the dispatch board using telematics data. |
| RD-4 | Confirmed delivered quantities are transmitted to Licensee's billing system no later than the end of each route day. |

**S1.5 WashLoop Driver Mobile Application.**

| Ref. | Criterion |
|---|---|
| DR-1 | The application operates offline for a full route day and synchronizes on reconnection without data loss. |
| DR-2 | Customer signatures and delivery exceptions, including photographs, are captured and synchronized. |
| DR-3 | Handheld RFID scanning at customer locations operates for the supported scanner models. |
| DR-4 | The device security requirements in Section B.9 of Exhibit B to the Agreement are met. |

**S1.6 Integrations and Data Migration.**

| Ref. | Criterion |
|---|---|
| IN-1 | The ERP and billing interface exchanges customer master records, item pricing, delivered quantities and invoice-ready billing extracts without manual intervention. |
| IN-2 | The telematics interface receives vehicle location and route-completion data. |
| IN-3 | Migrated records reconcile to Licensee's extracts, with any exceptions identified in the reconciliation report and corrected or accepted in writing by Licensee. |

**S1.7 Performance and Reporting.**

| Ref. | Criterion |
|---|---|
| PF-1 | The Software performs at the licensed quantities in Section 3.2 of Order Form No. 001 without degradation below the response times stated in the Documentation. |
| PF-2 | Standard reports and raw transaction data can be scheduled and exported in a commonly used, machine-readable format. |

## SCHEDULE 2 – FORM OF ACCEPTANCE CERTIFICATE

*[Letterhead of Tailosk Linen & Uniform Services, Inc.]*

To: Voupourt Software, LLC, 2100 Harrow Court, Suite 400, Wilmington, Delaware 19801, Attention: General Counsel

Copy: Licensor implementation manager; Licensor quality representative

Date: [●]

**Re: WashLoop Quality Agreement dated as of January 15, 2026: Acceptance Certificate**

1. We refer to the WashLoop Quality Agreement (the "**Quality Agreement**"). Terms defined in the Quality Agreement have the same meanings in this certificate.

2. Release identifier: [●]. Delivery Date: [●].

3. Licensee confirms that the Production Release identified above meets the Acceptance Criteria and accepts it under Section 5.5 of the Quality Agreement.

4. Open Defects at the date of this certificate, which Licensor shall correct in accordance with Section 5.6 of the Quality Agreement: [list, with Severity Levels, or "None"].

| **TAILOSK LINEN & UNIFORM SERVICES, INC.** |
|---|
| By: ______________________ |
| Name: |
| Title: Project Lead |

## SCHEDULE 3 – FORM OF REJECTION NOTICE

*[Letterhead of Tailosk Linen & Uniform Services, Inc.]*

To: Voupourt Software, LLC, 2100 Harrow Court, Suite 400, Wilmington, Delaware 19801, Attention: General Counsel

Copy: Licensor implementation manager; Licensor quality representative

Date: [●]

**Re: WashLoop Quality Agreement dated as of January 15, 2026: Rejection Notice**

1. We refer to the WashLoop Quality Agreement (the "**Quality Agreement**"). Terms defined in the Quality Agreement have the same meanings in this notice.

2. Release identifier: [●]. Delivery Date: [●].

3. This is a Rejection Notice under Section 5.3 of the Quality Agreement. The Production Release fails to meet the following Acceptance Criteria:

| Ref. | Description of failure | Test Script or test reference | Severity Level |
|---|---|---|---|
| [●] | [●] | [●] | [●] |

4. Licensee elects to [require correction and redelivery under Section 5.4] / [recover the Implementation Fees paid under Order Form No. 001 under Section 5.3(b)] of the Quality Agreement.

| **TAILOSK LINEN & UNIFORM SERVICES, INC.** |
|---|
| By: ______________________ |
| Name: |
| Title: |