# STATEMENT OF WORK NO. 1: LOOMSIGHT IMPLEMENTATION SERVICES

This Statement of Work No. 1 (this "**SOW**") is dated March 16, 2026 (the "**SOW Date**"). It is entered into by **Vopein Systems LLC**, a Pennsylvania limited liability company ("**Vopein**" or "**Licensor**"), and **Proudert Technical Fabrics, Inc.**, a Delaware corporation ("**Proudert**" or "**Licensee**"), under the Software License Agreement between them entered into as of March 2, 2026 (the "**Agreement**").

This SOW references the Agreement and, once signed by both Parties, is a Statement of Work within the meaning of Section 1.11 of the Agreement.

## 1. Definitions

1.1 Capitalized terms used but not defined in this SOW have the meanings given in the Agreement. These include "Authorized User," "Licensed Site," "Licensee Data," "Licensee Systems," "Services," "Software" and "Support Services."

1.2 In this SOW:

(a) "**Go-Live**" means the date on which Licensee first uses the Software in production for live production orders at the Licensed Site, as confirmed in writing by both Parties' Project Managers.

(b) "**Hypercare Period**" means the thirty (30) days following Go-Live.

(c) "**Project Manager**" means the individual each Party designates under Section 6.1.

(d) "**Project Plan**" means the detailed implementation plan delivered under Section 3.1(a), as updated by agreement of the Project Managers.

## 2. Scope of Services

2.1 **Overview.** Licensor shall implement the LoomSight modules listed in Schedule A of the Agreement at the Licensed Site. These are LoomSight MES Core, LoomSight Quality, LoomSight Connect and LoomSight Reports. Licensor shall carry out the work described in this Section 2.

2.2 **Discovery and Design.** Licensor shall:

(a) conduct on-site discovery workshops at the Licensed Site covering production order flow, loom scheduling, work-in-process tracking, roll grading and quality recordkeeping for Licensee's conveyor belting fabric, geotextile and filtration media lines;

(b) document Licensee's current-state processes and the target-state configuration of the Software; and

(c) prepare a solution design document describing configuration settings, master data structures, user roles and integration points.

2.3 **Installation and Configuration.** Licensor shall install the Software on Licensee-provided servers at the Licensed Site, in a test environment and a production environment. Licensor shall configure the Software in line with the approved solution design document, including:

(a) production order templates, routings and loom groupings;

(b) defect codes, roll grading rules, statistical process control charts and certificate-of-analysis templates; and

(c) user roles and permissions for Authorized Users.

2.4 **Integration.** Using LoomSight Connect, Licensor shall build and test:

(a) interfaces to the loom controllers on the weaving floor at the Licensed Site, as listed in the solution design document; and

(b) a bidirectional interface to Licensee's enterprise resource planning system for production orders, material consumption and finished-roll inventory.

2.5 **Data Migration.** Licensor shall migrate open production orders, active product specifications and twelve (12) months of historical roll quality records from Licensee's existing systems into the Software. Licensee shall provide source data extracts in a format agreed by the Project Managers.

2.6 **Reports.** Licensor shall configure the standard LoomSight Reports dashboards and up to eight (8) custom reports specified by Licensee during discovery.

2.7 **Training.** Licensor shall provide:

(a) administrator training for up to six (6) Licensee system administrators;

(b) train-the-trainer sessions for up to twelve (12) Licensee super-users; and

(c) end-user training sessions at the Licensed Site, scheduled across all production shifts, for up to seventy-five (75) Authorized Users.

2.8 **Go-Live and Hypercare.** Licensor shall provide on-site go-live support for the first five (5) production days after Go-Live. During the Hypercare Period it shall provide dedicated remote support with daily status calls. After the Hypercare Period, support transitions to the Support Services under Section 4 of the Agreement.

2.9 **Out of Scope.** The following are outside the scope of this SOW: implementation at any location other than the Licensed Site; hardware procurement; network cabling; modules not listed in Schedule A of the Agreement; and custom development of new Software functionality. Any of these may be added only by a change order under Section 9.

## 3. Deliverables

3.1 Licensor shall provide the following deliverables (each a "**Deliverable**"):

(a) Project Plan;

(b) current-state process documentation;

(c) solution design document;

(d) configured test environment;

(e) integration specifications and test results for each interface under Section 2.4;

(f) data migration mapping and reconciliation report;

(g) user acceptance testing ("**UAT**") scripts;

(h) training materials and attendance records;

(i) configured production environment; and

(j) go-live readiness checklist and hypercare close-out report.

3.2 Ownership of Deliverables is governed by Section 7 of the Agreement.

## 4. Schedule and Milestones

4.1 The Parties shall use reasonable efforts to meet the following target schedule. The Project Plan will refine it.

| Milestone | Description | Target Completion |
|---|---|---|
| M1 | Project Plan and solution design document approved | May 1, 2026 |
| M2 | Test environment configured and integrations built | July 17, 2026 |
| M3 | Data migration and UAT completed and accepted | September 11, 2026 |
| M4 | Training completed and Go-Live | October 5, 2026 |
| M5 | Hypercare Period completed and close-out report accepted | November 4, 2026 |

4.2 If either Party expects a milestone to be delayed, its Project Manager shall promptly notify the other Party's Project Manager. The notice shall give the cause of the delay and a proposed revised date. A delay caused by Licensee's failure to perform its responsibilities under Section 7 extends the affected dates by a corresponding period.

## 5. Acceptance

5.1 **Document Deliverables.** Licensee shall review each written Deliverable within ten (10) business days after receipt and either approve it or provide written comments identifying material deficiencies. Licensor shall address the comments and resubmit the Deliverable within ten (10) business days.

5.2 **UAT.** Licensee shall perform UAT using the agreed UAT scripts. Licensee shall accept Milestone M3 when the Software passes all UAT scripts with no open Severity 1 or Severity 2 issues, as those severities are defined in Section 4.2 of the Agreement. Licensor shall correct any failed scripts, and Licensee shall retest, within the periods set in the Project Plan.

5.3 **Deemed Acceptance.** If Licensee neither approves nor provides written comments on a Deliverable or milestone within the applicable review period, Licensor may notify Licensee in writing. If Licensee does not respond within five (5) business days after that notice, the Deliverable or milestone is deemed accepted. Using the Software in production for live production orders is deemed acceptance of Milestone M4.

## 6. Personnel and Governance

6.1 **Project Managers.** Each Party shall designate a Project Manager within five (5) business days after the SOW Date. The Project Manager is responsible for day-to-day coordination and may approve Deliverables and Project Plan updates. Project Managers may not sign change orders unless separately authorized in writing.

6.2 **Licensor Team.** Licensor shall staff the project with a Project Manager, a lead solution architect, at least one integration engineer and at least one quality-module consultant. Personnel replacement is governed by Section 3.3 of the Agreement.

6.3 **Status Reporting.** The Project Managers shall hold weekly status meetings. Licensor shall circulate a written status report covering progress, risks, open issues and upcoming activities.

6.4 **Steering Committee.** A steering committee of one senior executive from each Party shall meet monthly, and on request of either Project Manager, to resolve escalated issues.

6.5 **Site Rules and Data Security.** Licensor personnel shall comply with Section 3.3 of the Agreement while at the Licensed Site. They shall comply with Section 8.2 of the Agreement and Schedule B whenever they access Licensee Systems or Licensee Data.

## 7. Licensee Responsibilities

7.1 Licensee shall, in a timely manner:

(a) designate a Project Manager and make subject-matter experts from production, quality, maintenance and information technology reasonably available;

(b) provide and maintain servers, operating systems, databases and network connectivity at the Licensed Site meeting the specifications in the Documentation;

(c) provide reasonable remote access to the test and production environments, subject to Licensee's security procedures;

(d) arrange access to loom controllers and coordinate any required controller vendor support;

(e) provide source data extracts and validate migrated data;

(f) schedule Authorized Users for training; and

(g) perform UAT.

## 8. Fees and Payment

8.1 **Fixed Fee.** The Services under this SOW are provided for a fixed fee of $214,500 (the "**Implementation Fee**"). The Implementation Fee is payable on acceptance of the milestones as follows:

| Milestone | Percentage | Amount |
|---|---|---|
| M1 | 15% | $32,175 |
| M2 | 25% | $53,625 |
| M3 | 25% | $53,625 |
| M4 | 25% | $53,625 |
| M5 | 10% | $21,450 |
| **Total** | **100%** | **$214,500** |

8.2 **Invoicing and Payment.** Licensor shall invoice each milestone payment upon acceptance of the milestone. Payment terms and invoice disputes are governed by Section 5.3 of the Agreement.

8.3 **Expenses.** Reasonable travel and out-of-pocket expenses are reimbursable under Section 5.6 of the Agreement. Total reimbursable expenses under this SOW shall not exceed $28,000 without Licensee's prior written approval.

8.4 **Additional Services.** Services added by change order are charged at the rates in the change order. If the change order states no rates, the following hourly rates apply: Project Manager, $210; solution architect, $245; integration engineer, $225; consultant or trainer, $190.

8.5 **Taxes.** Taxes are governed by Section 5.5 of the Agreement.

## 9. Change Orders

9.1 Changes to this SOW are governed by Section 3.5 of the Agreement. A Party requesting a change shall submit a written change request to the other Party's Project Manager. Within ten (10) business days, Licensor shall provide a written impact assessment covering scope, schedule and fees.

9.2 No change takes effect, and Licensor is not required to perform any changed or additional work, until a written change order is signed by authorized representatives of both Parties.

## 10. Governing Law and Forum

10.1 This SOW and all disputes arising out of or relating to the Services are governed by the laws of the Commonwealth of Pennsylvania, without regard to its conflict-of-laws principles.

10.2 Each Party irrevocably submits to the exclusive jurisdiction of the state and federal courts located in Allegheny County, Pennsylvania, for any action arising out of or relating to this SOW or the Services. Each Party waives any objection to venue in those courts.

## 11. General

11.1 **Incorporation.** Under Section 3.2 of the Agreement, this SOW forms part of the Agreement upon signature by both Parties. Except as stated in this SOW, the terms of the Agreement apply to the Services.

11.2 **Warranty.** The Services are subject to the services warranty in Section 10.2 of the Agreement. The twelve (12) month Software warranty period under Section 10.1 of the Agreement begins on Go-Live.

11.3 **Term of SOW.** This SOW begins on the SOW Date and continues until acceptance of Milestone M5, unless terminated earlier under Section 13 of the Agreement.

11.4 **Counterparts.** This SOW may be executed in counterparts, including by electronic signature. All counterparts together constitute one instrument.

---

**IN WITNESS WHEREOF**, the Parties have executed this SOW as of the SOW Date.

**VOPEIN SYSTEMS LLC**

By: ______________________________
Name:
Title:
Date:

**PROUDERT TECHNICAL FABRICS, INC.**

By: ______________________________
Name:
Title:
Date: