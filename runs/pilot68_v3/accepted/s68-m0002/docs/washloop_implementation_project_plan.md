# WASHLOOP IMPLEMENTATION PROJECT PLAN

**Tailosk Linen & Uniform Services, Inc.: Initial Plants Deployment**

| Item | Detail |
|---|---|
| Document | WashLoop Implementation Project Plan |
| Version | 1.0 (Approved) |
| Date | February 6, 2026 |
| Prepared by | Voupourt Software, LLC, Implementation Services |
| Approved by | Project leads of Voupourt Software, LLC and Tailosk Linen & Uniform Services, Inc. |
| Related documents | Software License Agreement dated as of January 15, 2026; Order Form No. 001 dated January 15, 2026; WashLoop Quality Agreement dated as of January 15, 2026 |

---

## 1. INTRODUCTION

**1.1 Purpose.** This WashLoop Implementation Project Plan (this "**Plan**") is the implementation project plan agreed by the parties for purposes of Sections 1.1, 4.1 and 4.4 of the Software License Agreement dated as of January 15, 2026 (the "**Agreement**") between Voupourt Software, LLC ("**Licensor**") and Tailosk Linen & Uniform Services, Inc. ("**Licensee**"). It is also the implementation project plan referred to in Order Form No. 001 and in the WashLoop Quality Agreement (the "**Quality Agreement**").

**1.2 Scope of this Plan.** This Plan describes how the parties will carry out the Implementation Services for the Initial Plants listed in Schedule 1 to Order Form No. 001. It covers the phases, milestones, target dates, resourcing, governance, responsibilities, dependencies and reporting for the implementation. The scope of the Implementation Services itself is set out in Section 7 of, and Schedule 2 to, Order Form No. 001. This Plan does not change that scope or the Fees.

**1.3 Defined Terms.** Capitalized terms used but not defined in this Plan have the meanings given to them in the Agreement, Order Form No. 001 or the Quality Agreement, as applicable.

**1.4 Changes.** Target dates and resourcing in this Plan may be updated by the parties' project leads through the governance process in Section 9. Any change to the scope of the Implementation Services, the Fees or the Acceptance Criteria is made only in accordance with Section 4.5 of the Agreement or Section 9.1 of the Quality Agreement, as applicable.

**1.5 Supplements.** The parties may add supplements to this Plan for additional Plants or additional work. A supplement approved by both project leads forms part of this Plan.

## 2. PROJECT OBJECTIVES

**2.1 Business Objectives.** Licensee's objectives for the implementation are to:

(a) consolidate plant operations, garment tracking and route dispatch at the Initial Plants on a single platform;

(b) replace manual soil-sort and clean-out count reconciliation with RFID-based counts by Licensee Customer and location;

(c) improve route planning and load sequencing for the 120 route vehicles based at the Initial Plants;

(d) transmit confirmed delivered quantities to Licensee's billing system by the end of each route day; and

(e) give Licensee's healthcare and hospitality customers accurate inventory, loss and rewash reporting.

**2.2 Project Objectives.** The project objectives are to:

(a) deliver the Production Release in accordance with the milestones in Section 5;

(b) achieve Acceptance of the Production Release under the Quality Agreement;

(c) bring each Initial Plant live in a phased sequence that limits disruption to production shifts and route operations; and

(d) hand over to steady-state Support Services under Exhibit A to the Agreement following hypercare at the last Initial Plant.

## 3. SCOPE SUMMARY

**3.1 Software Modules.** The implementation covers the following Software modules licensed under Section 4.1 of Order Form No. 001:

(a) Plant Management;

(b) RFID Garment Tracking;

(c) Route Dispatch; and

(d) WashLoop Driver mobile application.

**3.2 Initial Plants.**

| Plant | Address | Route Vehicles | Shift Pattern | Go-Live Sequence |
|---|---|---|---|---|
| Columbus Plant | 1400 Ferris Industrial Parkway, Columbus, Ohio 43219 | 52 | Three shifts, seven days a week | 1 |
| Cincinnati Plant | 3275 Spring Grove Commerce Drive, Cincinnati, Ohio 45232 | 38 | Two shifts, Monday through Saturday | 2 |
| Indianapolis Plant | 6020 Eastgate Logistics Boulevard, Indianapolis, Indiana 46219 | 30 | Two shifts, Monday through Saturday | 3 |

**3.3 Integrations.** The standard WashLoop connectors described in Section 4.2 of Order Form No. 001 and Section S2.4 of Schedule 2 to Order Form No. 001:

(a) the bidirectional ERP and billing interface;

(b) the RFID hardware integration with the tunnel readers and handheld scanners at each Initial Plant; and

(c) the inbound telematics interface.

**3.4 Data Migration.** The records described in Section S2.5 of Schedule 2 to Order Form No. 001: garment and linen inventory, the RFID tag registry, customer master records, route and stop records, and billing history for the preceding twenty-four (24) months.

**3.5 Environments.** One production environment and two non-production environments (testing and training), as provided under Section 9.1 of Order Form No. 001.

**3.6 Out of Scope.** The following are outside the scope of this Plan unless added by change order under Section 4.5 of the Agreement:

(a) custom interfaces other than the standard WashLoop connectors;

(b) supply, installation or replacement of RFID readers, handheld scanners, vehicle devices or network equipment;

(c) customer-facing portals or log-in access for Licensee Customers; and

(d) Plants other than the Initial Plants.

## 4. PROJECT ORGANIZATION

**4.1 Licensor Team.**

| Role | Name or Designation | Allocation |
|---|---|---|
| Implementation manager | Elena V. Marchetti | Full time until go-live at the last Initial Plant |
| Solutions architect | Assigned by Licensor | 50% during Phases 1 and 2 |
| Integration engineer | Assigned by Licensor | Full time during Phase 2; as needed thereafter |
| Data migration specialist | Assigned by Licensor | Full time during migration activities |
| Trainers (two) | Assigned by Licensor | During Phase 4 training windows |
| Quality representative | Appointed under Section 3.3 of the Quality Agreement | Throughout Phases 2 and 3 |
| Customer success manager | Designated under Section A.8 of Exhibit A to the Agreement | Quarterly and at handover |
| Hypercare support engineer | Assigned by Licensor | Thirty (30) days after each go-live |

**4.2 Licensee Team.**

| Role | Name or Designation | Allocation |
|---|---|---|
| Executive sponsor | Chief Operating Officer | Steering meetings |
| Project lead | Director, Plant Systems | 75% throughout |
| Information technology lead | Vice President, Information Technology | As needed; approval of environment and data matters |
| Plant implementation leads | One per Initial Plant, designated by Licensee | 50% from discovery to hypercare at that Plant |
| Quality representative | Appointed under Section 3.3 of the Quality Agreement | Throughout Phases 2 and 3 |
| ERP and billing analyst | Designated by Licensee | During integration build and testing |
| Internal trainers | Designated by Licensee | Train-the-trainer and Phase 4 |

**4.3 Implementation Manager.** Elena V. Marchetti is the dedicated implementation manager under Section 4.1 of the Agreement and Section 7.2 of Order Form No. 001. She is Licensee's primary point of contact during implementation. Any replacement is subject to Section 4.2 of the Agreement and Section 7.2 of Order Form No. 001.

**4.4 Decision Authority.** Each plant implementation lead has authority to make day-to-day decisions on configuration and workflow for that Initial Plant, as required by Section S2.9(a) of Schedule 2 to Order Form No. 001. Decisions affecting more than one Initial Plant, or affecting the solution design document once approved, are made by Licensee's project lead.

## 5. PHASES AND MILESTONES

**5.1 Phase Overview.**

| Phase | Description | Target Start | Target Finish |
|---|---|---|---|
| 0 | Mobilization and environment provisioning | January 19, 2026 | January 30, 2026 |
| 1 | Discovery and design | February 2, 2026 | March 6, 2026 |
| 2 | Configuration, integration build and data migration | February 23, 2026 | March 27, 2026 |
| 3 | Pre-delivery testing, delivery and acceptance | March 9, 2026 | Acceptance under the Quality Agreement |
| 4 | Training, site readiness and phased go-live | April 13, 2026 | July 17, 2026 |
| 5 | Hypercare, handover and project closure | May 18, 2026 | August 21, 2026 |

**5.2 Key Milestones.**

| Ref. | Milestone | Target Date | Owner |
|---|---|---|---|
| M1 | Non-production environments provisioned (Section 2.3 of Order Form No. 001) | January 30, 2026 | Licensor |
| M2 | Plan approved by both project leads | February 6, 2026 | Both |
| M3 | Discovery workshops completed at all Initial Plants | February 20, 2026 | Licensor |
| M4 | Solution design document delivered | February 27, 2026 | Licensor |
| M5 | Solution design document approved | March 6, 2026 | Licensee |
| M6 | Configuration and integration build complete | March 20, 2026 | Licensor |
| M7 | Final trial data migration and reconciliation complete | March 27, 2026 | Licensor |
| M8 | Pre-delivery test report delivered (Section 4.4 of the Quality Agreement) | March 30, 2026 | Licensor |
| M9 | Production Release delivered with Delivery Notice (Section 5.1 of the Quality Agreement) | April 6, 2026 | Licensor |
| M10 | Acceptance of the Production Release | Under Section 5 of the Quality Agreement | Licensee |
| M11 | Go-live, Columbus Plant | May 18, 2026 | Both |
| M12 | Go-live, Cincinnati Plant | June 15, 2026 | Both |
| M13 | Go-live, Indianapolis Plant | July 13, 2026 | Both |
| M14 | Handover to steady-state Support Services and project closure | August 21, 2026 | Both |

**5.3 Dependencies.** Each milestone depends on completion of the milestones before it, except where Section 6 states otherwise. Go-live at an Initial Plant depends on Acceptance of the Production Release, completion of the site readiness assessment for that Initial Plant, completion of training for that Initial Plant, and Licensee's go/no-go decision under Section 7.4.

## 6. PHASE DETAIL

### 6.1 Phase 0: Mobilization and Environment Provisioning

(a) Licensor provisions the testing and training environments in the Hosted Environment, in accordance with Section 2.3 of Order Form No. 001.

(b) Licensor issues user credentials for the non-production environments to the Licensee project team.

(c) The parties appoint their quality representatives under Section 3.3 of the Quality Agreement.

(d) Licensee issues its purchase order under Section 8.5 of Order Form No. 001.

(e) The parties hold the project kick-off meeting and confirm the governance calendar in Section 9.

(f) Licensee provides its site safety, sanitation, infection-control and security policies for each Initial Plant under Section 4.3 of the Agreement before Licensor's first on-site visit.

### 6.2 Phase 1: Discovery and Design

**6.2.1 Discovery Workshops.** Licensor conducts on-site discovery workshops at each Initial Plant under Section S2.1 of Schedule 2 to Order Form No. 001. The workshops cover soil receiving, sorting, washing, drying, finishing, clean-side assembly, shipping and route operations.

| Plant | Workshop Dates |
|---|---|
| Columbus Plant | February 3 to 5, 2026 |
| Cincinnati Plant | February 10 to 12, 2026 |
| Indianapolis Plant | February 17 to 19, 2026 |

**6.2.2 Workshop Attendance.** Licensee shall make available for each workshop the plant implementation lead, a production supervisor from each shift, the route supervisor, a customer service representative familiar with the Plant's healthcare accounts, and an information technology representative.

**6.2.3 Solution Design Document.** Licensor delivers the solution design document by February 27, 2026. It describes the configuration of each Software module, the integrations in Section 4.2 of Order Form No. 001 and the data migration approach. Licensee reviews the document and either approves it or returns consolidated comments by March 6, 2026. Licensor addresses comments within three (3) Business Days after receipt.

**6.2.4 Data Extract Specification.** As part of the solution design document, Licensor specifies the formats for the data extracts that Licensee provides under Section S2.9(b) of Schedule 2 to Order Form No. 001.

### 6.3 Phase 2: Configuration, Integration Build and Data Migration

**6.3.1 Configuration.** Licensor configures the Software in the testing environment in accordance with the approved solution design document and Section S2.3 of Schedule 2 to Order Form No. 001. Configuration begins on February 23, 2026 for elements already confirmed in workshops. The remaining elements are configured following approval of the solution design document.

**6.3.2 Integration Build.**

| Interface | Build Window | Licensee Dependency |
|---|---|---|
| ERP and billing (bidirectional) | February 23 to March 20, 2026 | Test instance of ERP system and ERP and billing analyst available from February 23, 2026 |
| RFID hardware | March 2 to March 20, 2026 | Access to tunnel readers and handheld scanners at each Initial Plant for calibration |
| Telematics (inbound) | March 2 to March 13, 2026 | Telematics provider test credentials provided by February 27, 2026 |

**6.3.3 Data Migration.** Data migration follows the approach in the approved solution design document and Section S2.5 of Schedule 2 to Order Form No. 001.

| Step | Target Date | Owner |
|---|---|---|
| Licensee provides initial data extracts | March 6, 2026 | Licensee |
| Trial load 1 and reconciliation report | March 13, 2026 | Licensor |
| Licensee review and correction of source data | March 18, 2026 | Licensee |
| Trial load 2 and reconciliation report | March 25, 2026 | Licensor |
| Final validation before delivery | March 27, 2026 | Licensor |
| Reconciliation report delivered (Section 4.2 of the Quality Agreement) | No later than the Delivery Date | Licensor |

**6.3.4 Test Data.** Customer Data is loaded into the testing environment only with the prior written consent of Licensee's Vice President, Information Technology, under Section 9.3 of Order Form No. 001. Otherwise Licensor tests with synthetic data under Section 4.3 of the Quality Agreement.

### 6.4 Phase 3: Pre-Delivery Testing, Delivery and Acceptance

**6.4.1 Pre-Delivery Testing.** Licensor carries out the system, integration, RFID read-processing, offline-operation, performance and regression testing described in Section 4.1 of the Quality Agreement between March 9 and March 27, 2026.

**6.4.2 Test Scripts.** Licensor provides the Test Scripts for the core workflows of each Software module under Section S2.6 of Schedule 2 to Order Form No. 001 by March 20, 2026. This allows Licensee's quality representative to prepare for Acceptance Testing.

**6.4.3 Pre-Delivery Test Report.** Licensor delivers the pre-delivery test report by March 30, 2026, at least five (5) Business Days before the planned Delivery Date, in accordance with Section 4.4 of the Quality Agreement.

**6.4.4 Delivery.** The planned Delivery Date for the Production Release is April 6, 2026. Delivery is made in accordance with Section 5.1 of the Quality Agreement. Section 4.5 of the Quality Agreement applies to any open Severity 1 or Severity 2 Defect.

**6.4.5 Acceptance Testing.** Licensee carries out Acceptance Testing in accordance with Section 5.2 of the Quality Agreement. The parties plan the following activities:

(a) execution of the Test Scripts in the production environment by Licensee's quality representative and plant implementation leads;

(b) parallel processing at the Columbus Plant against Licensee's existing systems for a representative sample of production shifts and routes;

(c) RFID read-accuracy sampling against Criterion RF-2 in Schedule 1 to the Quality Agreement; and

(d) end-to-end testing of the ERP and billing interface, including a trial billing cycle.

Licensor's implementation manager attends Acceptance Testing sessions on request. Licensor's quality representative supports Defect triage in accordance with Section 7 of the Quality Agreement.

**6.4.6 Acceptance.** Acceptance, rejection, correction and redelivery are governed by Sections 5.3 through 5.5 of the Quality Agreement. Nothing in this Plan changes those Sections.

### 6.5 Phase 4: Training, Site Readiness and Phased Go-Live

**6.5.1 Site Readiness Assessments.** Licensor conducts a site readiness assessment at each Initial Plant at least twenty (20) Business Days before its target go-live date, under Section S2.2 of Schedule 2 to Order Form No. 001. Each assessment confirms whether the existing equipment meets the requirements of the Documentation, as described in Section S1.4 of Schedule 1 to Order Form No. 001.

| Plant | Assessment Date | Target Go-Live |
|---|---|---|
| Columbus Plant | April 13, 2026 | May 18, 2026 |
| Cincinnati Plant | May 11, 2026 | June 15, 2026 |
| Indianapolis Plant | June 8, 2026 | July 13, 2026 |

Licensor delivers a written readiness report within three (3) Business Days after each assessment. The report identifies any remediation required by either party.

**6.5.2 Training.** Licensor delivers the training described in Section S2.7 of Schedule 2 to Order Form No. 001 as follows:

| Training | Audience | Target Timing |
|---|---|---|
| Administrator training (three days) | Licensee plant administrators and system administrators | April 14 to 16, 2026 |
| Train-the-trainer (one session) | Licensee internal trainers | April 21, 2026 |
| Supervisor training (one day per shift) | Supervisors at each Initial Plant | Two weeks before go-live at that Plant |
| Route driver training | Route drivers at each Initial Plant | During the ten (10) days before go-live at that Plant, scheduled for each route start time |

Training is delivered in the training environment. Licensor provides role-based training materials in electronic form before each session, which Licensee may reproduce under Section 7.6 of Order Form No. 001.

**6.5.3 Cutover.** For each Initial Plant, Licensor prepares a cutover checklist at least ten (10) Business Days before go-live. The checklist covers final data load, opening inventory and tag registry reconciliation, route and stop activation, device enrollment for the WashLoop Driver mobile application, ERP interface activation and fallback procedures. Cutover is scheduled to begin after the last route of the day preceding go-live.

**6.5.4 Phasing Rationale.** The Columbus Plant goes first because it has the largest route fleet and three-shift operation, and because parallel processing during Acceptance Testing takes place there. The Cincinnati and Indianapolis Plants follow at four-week intervals so that lessons learned can be applied and so that hypercare periods do not overlap materially.

### 6.6 Phase 5: Hypercare, Handover and Project Closure

**6.6.1 Go-Live Support.** Licensor provides on-site go-live support at each Initial Plant for the first five (5) production days after go-live, under Section S2.8 of Schedule 2 to Order Form No. 001.

**6.6.2 Hypercare.** Licensor provides a dedicated support engineer for thirty (30) days after the go-live date of each Initial Plant, available on site or remotely during that Plant's production shifts, under Section 7.5 of Order Form No. 001.

**6.6.3 Handover.** Following hypercare at the Indianapolis Plant, Licensor's implementation manager hands the account over to the customer success manager designated under Section A.8 of Exhibit A to the Agreement. The handover includes:

(a) a list of open Defects, with Severity Levels, carried into steady-state support;

(b) the final configuration workbook for each Software module;

(c) the final data migration reconciliation reports;

(d) the as-built interface specifications; and

(e) a list of recommended follow-up items.

**6.6.4 Project Closure Report.** Licensor delivers a project closure report by August 21, 2026. The report summarizes milestones achieved, open items, lessons learned and the status of any change orders.

## 7. GO-LIVE CRITERIA AND DECISION

**7.1 Readiness Criteria.** Before each go-live, the parties confirm that:

(a) Acceptance of the Production Release has occurred under the Quality Agreement;

(b) the site readiness report for the Initial Plant shows no unresolved remediation item that would prevent production use;

(c) supervisor and route driver training for the Initial Plant is complete;

(d) the final data load for the Initial Plant has been reconciled, with any exceptions corrected or accepted in writing by Licensee;

(e) devices for the WashLoop Driver mobile application are enrolled for all route vehicles based at the Initial Plant; and

(f) the fallback procedures in the cutover checklist have been reviewed with the plant implementation lead.

**7.2 Go/No-Go Meeting.** The parties hold a go/no-go meeting two (2) Business Days before each target go-live date. Licensor's implementation manager presents the readiness position against Section 7.1.

**7.3 Licensor Recommendation.** Licensor's implementation manager states whether Licensor recommends proceeding.

**7.4 Licensee Decision.** Licensee's project lead decides whether to proceed with go-live. If go-live is deferred, the parties' project leads agree a revised target date through the governance process in Section 9.

## 8. RESPONSIBILITIES

**8.1 Responsibility Matrix.** In the table below, "R" means responsible for performing the activity, "A" means accountable for approving it, "C" means consulted, and "I" means informed.

| Activity | Licensor | Licensee |
|---|---|---|
| Environment provisioning | R, A | I |
| Discovery workshops | R | C |
| Solution design document | R | A |
| Data extracts from existing systems | C | R, A |
| Configuration of Software modules | R | C |
| Integration build | R | C |
| ERP test instance and analyst | I | R, A |
| RFID reader and scanner access and maintenance | C | R, A |
| Data migration and reconciliation | R | A |
| Pre-delivery testing and test report | R, A | I |
| Acceptance Testing | C | R, A |
| Site readiness assessment | R | C |
| Equipment remediation | C | R, A |
| Training delivery | R | C |
| Training attendance | I | R, A |
| Cutover | R | A |
| Go/no-go decision | C | R, A |
| Go-live and hypercare support | R | C |
| Handover and closure report | R | A |

**8.2 Licensee Cooperation.** Licensee provides the cooperation described in Section 3.3 of the Agreement and Section S2.9 of Schedule 2 to Order Form No. 001. Where Licensor considers that a Licensee dependency in this Plan has not been met, Licensor raises it in the weekly status meeting and records it in the RAID log under Section 10.

## 9. GOVERNANCE

**9.1 Weekly Status Meetings.** The parties hold weekly implementation status meetings under Section 7.3 of Order Form No. 001, on Tuesdays at 10:00 a.m. Eastern Time, by video conference unless the project leads agree otherwise. Attendees are the implementation manager, Licensee's project lead, the plant implementation leads for any Initial Plant in an active phase, and the quality representatives during Phase 3.

**9.2 Minutes.** Licensor circulates written minutes within two (2) Business Days after each weekly meeting. The minutes record open risks, issues, decisions and actions, together with progress against milestones.

**9.3 Monthly Steering Meetings.** The parties' project leads hold a monthly steering meeting attended by at least one senior representative of each party, including Licensee's executive sponsor. Steering meetings are held in the first week of each month from March 2026 until project closure. The steering meeting reviews milestone status, the RAID log, change requests and resourcing.

**9.4 Status Reporting During Testing.** From the planned Delivery Date until Acceptance, Licensor reports on testing and Defect status at each weekly status meeting, under Section 10.1 of the Quality Agreement.

**9.5 Change Requests.** Either party may raise a change request at a weekly status meeting or by written request to the other party's project lead. Licensor provides an impact assessment covering scope, schedule and Fees within five (5) Business Days. No change to scope, schedule or Fees is binding unless documented in a change order signed under Section 4.5 of the Agreement. Changes to target dates that do not affect scope or Fees may be agreed by the project leads and recorded in the minutes.

**9.6 Escalation.** Issues that cannot be resolved at the weekly status meeting are escalated to the monthly steering meeting, or to an ad hoc steering call if urgent. Disputes are dealt with under Section 16.2 of the Agreement. Disagreements on Acceptance Criteria or Severity Levels are dealt with under Section 10.2 of the Quality Agreement.

## 10. RISKS, ASSUMPTIONS, ISSUES AND DEPENDENCIES

**10.1 RAID Log.** Licensor maintains a log of risks, assumptions, issues and dependencies (the "**RAID log**") in the project workspace, to which Licensee's project team has read and comment access. The RAID log is reviewed at each weekly status meeting.

**10.2 Initial Risks.**

| Ref. | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | Quality of source data in existing systems delays migration | Medium | High | Two trial loads; early review of reconciliation reports; Licensee data cleansing between loads | Both |
| R2 | Tunnel-reader read rates below Documentation throughput at older readers | Medium | High | Calibration during integration build; identification of any upgrades in site readiness assessments | Licensor (calibration); Licensee (equipment) |
| R3 | ERP test instance unavailable during build window | Low | High | Confirm availability by February 20, 2026 | Licensee |
| R4 | Seasonal volume increase at Cincinnati Plant hospitality accounts during summer go-live | Medium | Medium | Go-live scheduled for mid-June; additional hypercare cover during weekend peaks | Both |
| R5 | Driver availability for training across route start times | Medium | Medium | Sessions scheduled for each route start time; train-the-trainer for refresher sessions | Licensee |
| R6 | Cellular coverage gaps on rural routes affecting synchronization | Low | Medium | Offline-operation testing under Section 4.1(d) of the Quality Agreement; route-specific testing during parallel processing | Licensor |

**10.3 Assumptions.**

(a) Licensee's existing systems can produce extracts in the formats specified in the solution design document.

(b) The RFID tags currently in circulation at the Initial Plants are compatible with the reader models specified in the Documentation.

(c) Licensee's plant implementation leads are available at the allocation stated in Section 4.2.

(d) No Plant other than the Initial Plants is added during the period covered by this Plan without a supplement under Section 1.5.

(e) Licensor personnel attending the Initial Plants comply with the site policies provided under Section 4.3 of the Agreement, including requirements for handling soiled healthcare linen.

## 11. COMMUNICATIONS

**11.1 Project Workspace.** Licensor provides a shared project workspace for this Plan, the RAID log, meeting minutes, the solution design document, test reports and training materials. Access is limited to named members of each party's project team.

**11.2 Defect Reporting.** During Phases 3 to 5, Defects are reported through the web-based ticketing portal or support telephone line described in Exhibit A to the Agreement, in accordance with Section 7.1 of the Quality Agreement.

**11.3 Formal Notices.** Delivery Notices, Rejection Notices and Acceptance Certificates are given in accordance with Section 12.3 of the Quality Agreement and Section 17.1 of the Agreement. Communications through the project workspace or at meetings are not formal notices.

**11.4 Plant Communications.** Each plant implementation lead is responsible for communicating go-live dates, training schedules and cutover arrangements to plant and route personnel. Licensor provides template communications on request.

## 12. INVOICING MILESTONES

**12.1 Implementation Fee Milestones.** For reference, the Implementation Fee milestones in Section 3.4 of Order Form No. 001 correspond to the milestones in this Plan as follows:

| Order Form Milestone | Amount | Plan Milestone |
|---|---|---|
| Execution of this Order Form | $55,950 | Order Form Date (before M1) |
| Acceptance of the Production Release under the Quality Agreement | $74,600 | M10 |
| Go-live at the last of the Initial Plants | $55,950 | M13 |

**12.2 Invoice Support.** Each milestone invoice is accompanied by the evidence required under Section 8.2 of Order Form No. 001 and, for the acceptance milestone, Section 5.7 of the Quality Agreement.

## 13. SECURITY AND DATA HANDLING DURING IMPLEMENTATION

**13.1 Data Extracts.** Licensee transfers data extracts to Licensor only through the secure file transfer facility in the Hosted Environment. Extracts are not sent by email.

**13.2 Access.** Licensor project personnel have access to Customer Data only as needed for the activities in this Plan, in accordance with Section 7 of the Agreement and Exhibit B to the Agreement.

**13.3 Devices.** Devices used for the WashLoop Driver mobile application are enrolled and configured in accordance with Section B.9 of Exhibit B to the Agreement before use on any route.

## 14. APPROVAL

The parties' project leads approve this Plan as the implementation project plan agreed by the parties.

| **VOUPOURT SOFTWARE, LLC** | **TAILOSK LINEN & UNIFORM SERVICES, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: Elena V. Marchetti | Name: ______________________ |
| Title: Implementation Manager | Title: Director, Plant Systems (Project Lead) |
| Date: February 6, 2026 | Date: February 6, 2026 |

---

## APPENDIX A: GOVERNANCE CALENDAR

| Meeting | Frequency | Day and Time | Chair | Minutes |
|---|---|---|---|---|
| Implementation status meeting | Weekly | Tuesdays, 10:00 a.m. ET | Licensor implementation manager | Licensor, within two (2) Business Days |
| Steering meeting | Monthly | First Thursday of the month, 2:00 p.m. ET | Licensee project lead | Licensor, within two (2) Business Days |
| Quality review (Phase 3) | Weekly, alongside status meeting | Tuesdays, 11:00 a.m. ET | Quality representatives | Recorded in status minutes |
| Go/no-go meeting | Once per Initial Plant | Two (2) Business Days before go-live | Licensee project lead | Licensor, same day |
| Hypercare stand-up | Daily during hypercare | Start of first production shift | Licensor support engineer | Issue log in ticketing portal |

## APPENDIX B: CUTOVER CHECKLIST TEMPLATE

| Step | Description | Owner | Completed |
|---|---|---|---|
| 1 | Confirm go/no-go decision recorded | Licensee project lead | |
| 2 | Freeze changes to existing systems for the Plant | Licensee | |
| 3 | Final extract of inventory, tag registry, customer, route and billing records | Licensee | |
| 4 | Final data load and reconciliation report | Licensor | |
| 5 | Licensee sign-off of reconciliation exceptions | Licensee plant implementation lead | |
| 6 | Activate routes and stops in Route Dispatch module | Licensor | |
| 7 | Confirm device enrollment for all route vehicles | Licensee | |
| 8 | Activate ERP and billing interface for the Plant | Licensor, with Licensee ERP analyst | |
| 9 | Confirm tunnel-reader and handheld-scanner connectivity | Licensor, with Licensee information technology | |
| 10 | Confirm fallback procedures and contacts | Both | |
| 11 | Start of first production shift on the Software | Licensee | |

## APPENDIX C: DELIVERABLES REGISTER

| Deliverable | Source Requirement | Target Date | Approver |
|---|---|---|---|
| Implementation project plan (this Plan) | Section 4.1 of the Agreement | February 6, 2026 | Both project leads |
| Solution design document | Section S2.1 of Schedule 2 to Order Form No. 001 | February 27, 2026 | Licensee project lead |
| Data migration reconciliation reports | Section S2.5 of Schedule 2 to Order Form No. 001 | Each trial load and final load | Licensee project lead |
| Test Scripts | Section S2.6 of Schedule 2 to Order Form No. 001 | March 20, 2026 | Licensee quality representative |
| Pre-delivery test report | Section 4.4 of the Quality Agreement | March 30, 2026 | Licensee quality representative (review) |
| Release Notes and Delivery Notice | Section 5.1 of the Quality Agreement | Delivery Date | Not applicable |
| Site readiness reports | Section S2.2 of Schedule 2 to Order Form No. 001 | Three (3) Business Days after each assessment | Licensee plant implementation lead |
| Training materials | Section 7.6 of Order Form No. 001 | Before each session | Licensee project lead |
| Cutover checklists | Section 6.5.3 of this Plan | Ten (10) Business Days before each go-live | Licensee plant implementation lead |
| Project closure report | Section 6.6.4 of this Plan | August 21, 2026 | Both project leads |