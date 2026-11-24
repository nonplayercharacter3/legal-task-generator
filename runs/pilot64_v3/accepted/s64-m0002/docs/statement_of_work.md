# STATEMENT OF WORK NO. 1

**DairyLedger Implementation Services**

This Statement of Work No. 1 (this "**SOW**") is entered into as of March 1, 2026 (the "**SOW Effective Date**") by and between **TILIL SYSTEMS, INC.**, a Delaware corporation ("**Licensor**"), and **KUNOUX CREAMERY, INC.**, a Wisconsin corporation ("**Licensee**"). It is made under the Software-as-a-Service License Agreement between Licensor and Licensee dated as of March 1, 2026 (the "**License Agreement**").

## 1. GENERAL

**1.1 Incorporation.** This SOW is the "SOW" referred to in the License Agreement. It describes the Implementation Services and is governed by the License Agreement in accordance with Section 4.1 of the License Agreement.

**1.2 Definitions.** Capitalized terms used but not defined in this SOW have the meanings given in the License Agreement. In this SOW:

"**Acceptance Certificate**" means a written certificate in the form of Attachment 2, signed by Licensee's Project Manager, confirming acceptance of a Deliverable or Milestone.

"**Eau Claire Plant**" means Licensee's processing plant at 4400 Creamery Road, Eau Claire, Wisconsin.

"**Go-Live**" means, for an Implementation Site, the first day on which the Subscription Services are used in production at that site to record raw milk receiving and lot creation for all inbound loads.

"**Hypercare Period**" means, for an Implementation Site, the 30-day period beginning on the Go-Live date for that site.

"**Implementation Sites**" means the Eau Claire Plant and the Sheboygan Plant.

"**Milestone**" means each milestone identified in Section 5.

"**Project Manager**" means the project manager appointed by a party under Section 7.

"**Sheboygan Plant**" means Licensee's processing plant in Sheboygan, Wisconsin.

"**Steering Committee**" means the committee described in Section 7.4.

"**Test Plan**" means the test plan prepared by Licensor and approved by Licensee under Section 6.1.

## 2. SCOPE OF IMPLEMENTATION SERVICES

**2.1 Overview.** Licensor shall configure, integrate and deploy the subscribed modules of the Subscription Services at the Implementation Sites. It shall also migrate in-scope historical records, train Licensee personnel and Authorized Users, and support each Implementation Site through Go-Live and the Hypercare Period. All of this shall follow the Documentation and this SOW.

**2.2 Workstreams.** The Implementation Services consist of the following workstreams.

(a) **Discovery and Design.** Licensor shall conduct on-site and remote discovery workshops at each Implementation Site covering raw milk receiving, farm pickup and hauling routes, silo and tank management, lot coding, cold-chain monitoring points, laboratory testing, finished product release and recall procedures. Licensor shall prepare a Solution Design Document describing the configuration of each subscribed module, the lot genealogy model, user roles and permissions, alert thresholds, and report formats.

(b) **Configuration.** Licensor shall configure the Subscription Services in accordance with the approved Solution Design Document. This includes facility, silo, tank and line hierarchies; farm supplier and hauler master data structures; lot code formats; temperature alert thresholds and escalation rules; and standard trace-back, trace-forward and recall report templates.

(c) **Integration.** Licensor shall build and test the interfaces listed in Section 2.3.

(d) **Data Migration.** Licensor shall migrate the historical records described in Section 2.4.

(e) **Field Device Deployment.** Licensor shall deliver, configure and commission the Licensor-supplied in-tanker and in-silo temperature sensors and gateways in the quantities set out in the Order Form. Licensor shall also verify the offline capture and synchronization functions described in Section A.2 of Exhibit A to the License Agreement.

(f) **Supplier and Hauler Onboarding.** Licensor shall provide the onboarding materials and support described in Section 2.5.

(g) **Training.** Licensor shall deliver the training described in Section 2.6.

(h) **Go-Live and Hypercare.** Licensor shall provide cutover planning, on-site Go-Live support and Hypercare support as described in Section 2.7.

**2.3 Integrations.** Licensor shall develop, configure and test the following interfaces between the Subscription Services and Licensee systems:

| No. | Licensee System | Direction | Data |
|---|---|---|---|
| INT-1 | Enterprise resource planning system | Bi-directional | Supplier master, purchase receipts, finished goods lots, production orders |
| INT-2 | Laboratory information management system | Inbound to DairyLedger | Raw milk test results (somatic cell count, bacteria, antibiotic residue, components) |
| INT-3 | Milk receiving bay scales | Inbound to DairyLedger | Load weights and receiving timestamps |
| INT-4 | Plant historian / SCADA (silo temperature and level) | Inbound to DairyLedger | Silo temperature and level readings |
| INT-5 | Supplier payroll and premium system | Outbound from DairyLedger | Pickup volumes and quality results by farm supplier |

Licensor is responsible for the DairyLedger side of each interface. Licensee is responsible for making its systems, application programming interfaces, test environments and system administrators available as described in Section 8.

**2.4 Data Migration.** Licensor shall migrate the following records from Licensee's legacy spreadsheets and receiving logs into the Subscription Services, using data extracts provided by Licensee in the format agreed in the Solution Design Document:

(a) farm supplier master records, including organic certification status and certification expiry dates, for active suppliers;

(b) hauler, route and driver master records;

(c) raw milk receiving and test records for the 24 months before the SOW Effective Date; and

(d) open consumer-complaint records and complaint records closed within the 12 months before the SOW Effective Date.

Licensor shall perform up to two trial migrations and one production migration for each Implementation Site. Licensor shall provide a reconciliation report for each migration showing record counts and exceptions. Licensee is responsible for cleansing source data and resolving exceptions identified in the reconciliation reports.

**2.5 Supplier and Hauler Onboarding.** As contemplated by Section 6.4 of the License Agreement, Licensor shall provide:

(a) a supplier and hauler onboarding kit, including quick-start guides for the mobile applications in English and Spanish;

(b) up to six live webinar sessions for farm suppliers and haulers, scheduled in consultation with Licensee;

(c) a dedicated onboarding support queue for farm suppliers and haulers during the period from 30 days before through 30 days after Go-Live at each Implementation Site; and

(d) weekly onboarding status reports showing invited, registered and active suppliers, haulers and drivers.

Licensee remains responsible for inviting its farm suppliers, haulers and drivers and for any agreements between Licensee and those persons.

**2.6 Training.** Licensor shall deliver:

(a) administrator training for up to 10 Licensee administrators, consisting of not less than 16 hours of instruction;

(b) train-the-trainer sessions for up to 20 Licensee super-users at each Implementation Site;

(c) role-based end-user training materials for receiving, laboratory, production, quality assurance and recall team roles; and

(d) one recall simulation exercise at each Implementation Site before Go-Live. In each exercise Licensee's recall team generates trace-back and trace-forward reports for a sample finished product lot using the Subscription Services.

**2.7 Go-Live and Hypercare.** Licensor shall prepare a cutover plan for each Implementation Site, including rollback criteria. Licensor shall provide at least two qualified consultants on site for the first five Business Days after Go-Live. During the Hypercare Period, Licensor shall hold daily stand-up calls with Licensee and prioritize defect resolution. At the end of the Hypercare Period, Licensor shall hand over the site to its standard support organization under Exhibit A to the License Agreement.

**2.8 Out of Scope.** The following are outside the scope of this SOW unless added by a change order under Section 10:

(a) implementation at any Licensee or Affiliate facility other than the Implementation Sites;

(b) interfaces other than those listed in Section 2.3;

(c) migration of records other than those listed in Section 2.4;

(d) installation of plant network cabling, wireless access points or other plant infrastructure, which is Licensee's responsibility under Section 6.3 of the License Agreement; and

(e) changes to Licensee's enterprise resource planning, laboratory information management or SCADA systems, other than enabling the interfaces in Section 2.3.

## 3. FUNCTIONAL SPECIFICATIONS

**3.1 Specifications.** The functional specifications for purposes of Section 11.2 of the License Agreement are set out in Attachment 1 and, once approved by Licensee, the Solution Design Document.

**3.2 Conflicts within this SOW.** If the approved Solution Design Document is inconsistent with Attachment 1, Attachment 1 shall control unless the Solution Design Document expressly identifies the variation and Licensee's Project Manager has approved it in writing.

## 4. DELIVERABLES

**4.1 Deliverables.** Licensor shall provide the following Deliverables:

| No. | Deliverable | Ownership |
|---|---|---|
| DEL-1 | Project plan and RACI matrix | Licensor |
| DEL-2 | Solution Design Document | Licensor |
| DEL-3 | Configured Subscription Services for each Implementation Site | Licensor |
| DEL-4 | Interfaces INT-1 through INT-5 (DairyLedger connectors and configurations) | Licensor |
| DEL-5 | Data mapping documents describing Licensee's systems and legacy data | Licensee |
| DEL-6 | Migration reconciliation reports | Licensee |
| DEL-7 | Test Plan and test results | Licensor |
| DEL-8 | Licensee-specific standard operating procedures for receiving, lot coding, cold-chain alert response and recall | Licensee |
| DEL-9 | Role-based training content incorporating Licensee information | Licensee |
| DEL-10 | Cutover plans and Go-Live readiness checklists | Licensor |
| DEL-11 | Hypercare close-out report for each Implementation Site | Licensor |

**4.2 Ownership.** The Deliverables marked "Licensee" in Section 4.1 are Licensee-owned deliverables for purposes of Section 9.3 of the License Agreement. All other Deliverables are owned as provided in Section 9.3 of the License Agreement.

## 5. PROJECT PLAN AND MILESTONES

**5.1 Phasing.** The Implementation Services shall be performed in two phases. Phase 1 covers the Eau Claire Plant and Phase 2 covers the Sheboygan Plant. Licensor shall deliver a detailed project plan (DEL-1) within 10 Business Days after the SOW Effective Date, consistent with the target dates below.

**5.2 Milestones.**

| Milestone | Description | Target Date |
|---|---|---|
| M1 | Project kickoff and approval of project plan (DEL-1) | March 20, 2026 |
| M2 | Approval of Solution Design Document (DEL-2) | May 1, 2026 |
| M3 | Phase 1 configuration, interfaces and trial migration complete; system integration testing passed for the Eau Claire Plant | July 10, 2026 |
| M4 | Phase 1 user acceptance testing passed and Go-Live at the Eau Claire Plant | August 17, 2026 |
| M5 | Phase 1 Hypercare close-out (DEL-11) | September 16, 2026 |
| M6 | Phase 2 user acceptance testing passed and Go-Live at the Sheboygan Plant | November 9, 2026 |
| M7 | Phase 2 Hypercare close-out and final acceptance | December 9, 2026 |

**5.3 Adjustment of Dates.** Target dates may be adjusted only through the change control procedure in Section 10. Section 4.3 of the License Agreement applies to delays caused by Licensee's failure to perform its responsibilities under Section 8.

**5.4 Status Reporting.** Licensor's Project Manager shall provide a written status report each week. The report shall cover progress against the project plan, upcoming activities, open risks and issues, decisions required, and the status of change requests.

## 6. TESTING AND ACCEPTANCE

**6.1 Test Plan.** Licensor shall prepare the Test Plan (DEL-7) and deliver it to Licensee at least 15 Business Days before the start of system integration testing for Phase 1. The Test Plan shall include test scripts covering each functional specification in Attachment 1, each interface in Section 2.3, migration validation, offline capture and synchronization, and the recall simulation in Section 2.6(d). Licensee shall review and approve the Test Plan, or provide reasonable comments, within 10 Business Days after receipt.

**6.2 System Integration Testing.** Licensor shall perform system integration testing in a non-production environment in accordance with the Test Plan and shall deliver the test results to Licensee.

**6.3 User Acceptance Testing.** Licensee shall perform user acceptance testing for each Implementation Site in accordance with the Test Plan, with Licensor's support, during a testing window of 15 Business Days. Licensee shall record any defects in the project defect log and classify them using the severity levels in Section A.5 of Exhibit A to the License Agreement.

**6.4 Acceptance Criteria.** A Deliverable or Milestone that is subject to testing shall be accepted when:

(a) all test scripts in the Test Plan applicable to it have been executed;

(b) no Severity 1 or Severity 2 defects remain open; and

(c) any open Severity 3 defects are documented in a remediation plan agreed by both Project Managers.

Documentary Deliverables shall be accepted when they materially conform to this SOW and contain no material errors or omissions.

**6.5 Acceptance Procedure.** On completion of testing, or on delivery of a documentary Deliverable, Licensor shall submit an Acceptance Certificate to Licensee. Within 10 Business Days after receipt, Licensee shall either sign the Acceptance Certificate or give Licensor written notice describing each material nonconformity with the acceptance criteria. Licensor shall correct each notified nonconformity and resubmit the Deliverable or Milestone for re-testing or review, and the procedure in this Section 6.5 shall apply again. If Licensee neither signs the Acceptance Certificate nor gives notice of nonconformity within the 10 Business Day period, the Deliverable or Milestone shall be deemed accepted. Licensee's production use of the Subscription Services at an Implementation Site does not constitute acceptance of Milestone M4 or M6, except that Go-Live under an approved cutover plan with no open Severity 1 or Severity 2 defects shall be treated as satisfaction of the Go-Live element of those Milestones.

**6.6 Repeated Failure.** If a Milestone fails acceptance testing three times for reasons attributable to Licensor, Licensee may, by written notice, either require Licensor to continue correction at no additional charge or treat the failure as a material breach for purposes of Section 14.3(a) of the License Agreement.

## 7. PROJECT GOVERNANCE AND PERSONNEL

**7.1 Licensor Personnel.** Licensor shall staff the project in accordance with Section 4.2 of the License Agreement. Licensor's named implementation project manager is Dana Okonkwo-Reyes. Licensor shall also assign a solution architect, an integration engineer, a data migration specialist, a field device technician and a training lead.

**7.2 Licensee Personnel.** Licensee's Project Manager is Marcus Lindqvist, Director of Plant Systems. Licensee shall also designate a quality assurance lead, a receiving lead and an IT integration lead for each Implementation Site.

**7.3 Key Personnel Continuity.** Licensor shall not reassign its Project Manager or solution architect away from the project before Milestone M7 except for reasons outside Licensor's reasonable control or with Licensee's consent, not to be unreasonably withheld. Any replacement is subject to Section 4.2 of the License Agreement.

**7.4 Steering Committee.** The Steering Committee consists of the two Project Managers, Licensor's Vice President of Customer Delivery, and Licensee's Vice President of Operations and Vice President of Quality Assurance. It shall meet monthly and at any key decision point. It shall review progress, resolve issues escalated by the Project Managers and approve change orders above the threshold in Section 10.3. Matters the Steering Committee cannot resolve shall be referred to executive negotiation under Section 16.2 of the License Agreement.

**7.5 Escalation Contacts.** The escalation contacts for purposes of Section A.6 of Exhibit A to the License Agreement are:

| Level | Licensor | Licensee |
|---|---|---|
| 1 | Implementation Project Manager | Project Manager |
| 2 | Director of Support Operations | Director of Plant Systems |
| 3 | Vice President of Customer Delivery | Vice President of Operations |

Either party may update its escalation contacts by written notice to the other party's Project Manager.

## 8. LICENSEE RESPONSIBILITIES

As part of its cooperation under Section 4.3 of the License Agreement, Licensee shall:

(a) make its subject matter experts available for discovery workshops, design reviews and testing as scheduled in the project plan;

(b) provide Licensor with timely access to the Implementation Sites, plant networks, test environments and systems listed in Section 2.3, and with system administrator support;

(c) provide legacy data extracts in the agreed format by the dates in the project plan, and cleanse source data;

(d) ensure that plant network connectivity and wireless coverage at receiving bays, silo areas and laboratories meet the minimum technical requirements in the Documentation at least 20 Business Days before scheduled field device deployment;

(e) review Deliverables and make decisions within the time periods stated in this SOW or, where no period is stated, within five Business Days;

(f) perform user acceptance testing under Section 6.3;

(g) release staff for training sessions and ensure that super-users complete train-the-trainer sessions before Go-Live;

(h) invite farm suppliers, haulers and drivers to the Subscription Services in accordance with the onboarding schedule; and

(i) brief Licensor personnel on site safety, sanitation, food defense and good manufacturing practice rules under Section 4.4 of the License Agreement.

## 9. FEES AND EXPENSES

**9.1 Implementation Fees.** The Implementation Fees for the Implementation Services are a fixed fee of $312,000, invoiced on the following Milestones:

| Milestone | Percentage | Amount |
|---|---|---|
| M1 | 15% | $46,800 |
| M2 | 15% | $46,800 |
| M4 | 30% | $93,600 |
| M6 | 25% | $78,000 |
| M7 | 15% | $46,800 |

Licensor may invoice each Milestone payment upon acceptance of the relevant Milestone under Section 6. Invoices are payable in accordance with Section 7.3 of the License Agreement.

**9.2 Change Orders.** Additional services under an approved change order shall be charged at the rates in Section 9.3, unless the change order states a fixed fee.

**9.3 Rates.** Licensor's professional services rates for the term of this SOW are:

| Role | Hourly Rate |
|---|---|
| Project Manager | $210 |
| Solution Architect | $245 |
| Integration Engineer | $225 |
| Data Migration Specialist | $195 |
| Field Device Technician | $165 |
| Training Lead | $175 |

**9.4 Expenses.** Licensee shall reimburse Licensor's reasonable, documented travel and out-of-pocket expenses for on-site work at the Implementation Sites, in accordance with Section 7.8 of the License Agreement and Licensee's travel policy. Reimbursable expenses under this SOW shall not exceed $38,000 in total without the prior written approval of Licensee's Project Manager. Licensor shall invoice expenses monthly in arrears with supporting receipts.

**9.5 Taxes.** Section 7.7 of the License Agreement applies to the Implementation Fees and expenses.

## 10. CHANGE CONTROL

**10.1 Change Requests.** Either party may request a change to the scope, Deliverables, Milestones or target dates by submitting a written change request to the other party's Project Manager. The request shall describe the change and the reason for it.

**10.2 Impact Assessment.** Within five Business Days after submitting or receiving a change request, Licensor shall provide a written impact assessment. The assessment shall state the effect of the change on scope, Deliverables, project plan, target dates and Fees, and any effect on the functional specifications. Licensor shall not charge for preparing impact assessments unless the assessment requires more than eight hours of effort and Licensee has approved the charge in advance.

**10.3 Approval.** A change becomes binding only when both parties sign a written change order in accordance with Section 4.6 of the License Agreement. Change orders with a value of up to $25,000 may be signed by the Project Managers. Change orders above that amount, or that move Milestone M4 or M6 by more than 20 Business Days, require Steering Committee approval and signature by an authorized officer of each party.

**10.4 Continuation of Work.** Pending agreement on a change order, Licensor shall continue to perform the Implementation Services in accordance with this SOW as it stands.

## 11. GENERAL

**11.1 Term of SOW.** This SOW begins on the SOW Effective Date. It continues until Licensee accepts Milestone M7 and all Implementation Fees are paid, unless the License Agreement terminates earlier.

**11.2 Notices.** Notices under this SOW, other than routine project communications between the Project Managers, shall be given in accordance with Section 16.5 of the License Agreement.

**11.3 Counterparts.** This SOW may be executed in counterparts and by electronic signature in accordance with Section 16.18 of the License Agreement.

## ATTACHMENT 1 — FUNCTIONAL SPECIFICATIONS

**1. Farm Pickup.** The mobile application shall record, for each farm pickup: farm supplier, bulk tank identifier, pickup time, tank temperature, volume, driver, tanker and sample identifier. The application shall capture location by GPS at the time of recording and shall operate offline as described in Section A.2 of Exhibit A to the License Agreement.

**2. Tanker Tracking.** The Subscription Services shall link each tanker load to all farm pickups comprising it. They shall record in-transit temperatures from Licensor-supplied sensors at intervals of not more than five minutes.

**3. Plant Receiving.** The Subscription Services shall record receiving time, scale weight (via INT-3), receiving temperature and laboratory results (via INT-2). They shall prevent a load from being released to a silo until required tests have been entered and passed, unless a user with an authorized override role records an override with a reason.

**4. Silo and Lot Genealogy.** The Subscription Services shall track silo fills and draws, assign lot codes in the format set out in the Solution Design Document, and maintain the genealogy linking each finished product lot to the silos, tanker loads and farm pickups from which it was produced.

**5. Cold-Chain Alerts.** The Subscription Services shall generate alerts by on-screen notification, email and SMS when a configured temperature threshold is exceeded. They shall escalate unacknowledged alerts in accordance with the configured escalation rules, and shall log all alerts, acknowledgements and corrective actions.

**6. Trace and Recall Reports.** For any finished product lot or farm supplier, the Subscription Services shall generate trace-back and trace-forward reports within five minutes of request, and shall export them in PDF and CSV formats.

**7. Organic Certification Tracking.** The Subscription Services shall record each farm supplier's organic certification status and expiry date. They shall alert designated users 60 days and 30 days before expiry, and shall flag pickups from suppliers whose certification has lapsed.

**8. Consumer Complaints.** The Subscription Services shall record consumer complaints, link them to finished product lots where identified, and track investigation status and closure.

**9. Roles and Audit Trail.** The Subscription Services shall support role-based access control and shall maintain a time-stamped audit trail of record creation, modification and deletion that cannot be edited by users.

## ATTACHMENT 2 — FORM OF ACCEPTANCE CERTIFICATE

**Acceptance Certificate — SOW No. 1**

Deliverable / Milestone: ______________________________

Implementation Site (if applicable): ______________________________

Date submitted by Licensor: ______________________________

Licensee confirms that the Deliverable or Milestone identified above has met the acceptance criteria in Section 6.4 of SOW No. 1, subject to the remediation plan (if any) attached.

Open Severity 3 defects and remediation plan reference: ______________________________

Signed for Kunoux Creamery, Inc. by its Project Manager:

Name: ______________________________
Signature: ______________________________
Date: ______________________________

## SIGNATURES

IN WITNESS WHEREOF, the parties have executed this Statement of Work No. 1 by their duly authorized representatives as of the SOW Effective Date.

**TILIL SYSTEMS, INC.**

By: ______________________________
Name: ______________________________
Title: ______________________________
Date: ______________________________

**KUNOUX CREAMERY, INC.**

By: ______________________________
Name: ______________________________
Title: ______________________________
Date: ______________________________