# STATEMENT OF WORK NO. 1

**Implementation Services – Protoux CellTrace Platform**

This Statement of Work No. 1 (this "**SOW**") is entered into as of March 2, 2026 (the "**SOW Effective Date**") by and between **Protoux Analytics, Inc.**, a Delaware corporation ("**Licensor**" or "**Protoux**"), and **Glenox Circular Materials, Inc.**, a Delaware corporation ("**Licensee**" or "**Glenox**").

This SOW is issued under the Software License Agreement between Licensor and Licensee dated as of March 2, 2026 (the "**Agreement**"). It is a "Statement of Work" for the purposes of the Agreement and is governed by the Agreement. Capitalized terms used but not defined in this SOW have the meanings given in the Agreement.

## 1. Purpose and Scope

1.1 **Purpose.** Licensor shall perform the implementation, configuration, integration and training services described in this SOW (the "**Implementation Services**"). These services will make the Platform operational for Licensee's lithium-ion battery chain-of-custody, feedstock intake and materials-recovery activities at the Licensed Site.

1.2 **Licensed Site.** The Implementation Services relate only to the Licensed Site identified in the Order Form. Work at any other Licensee facility requires an amended Order Form under Section 4.3 of the Agreement and a separate statement of work.

1.3 **Platform Modules in Scope.** The Implementation Services cover the Platform modules licensed under the Order Form, configured for the following functional areas:

(a) **Chain-of-Custody:** receipt, weighing, labelling and tracking of incoming battery lots from drop-off, collection and haulage sources through to discharge, dismantling and black-mass production;

(b) **Feedstock Intake:** supplier and lot registration, chemistry classification, state-of-charge and hazard flags, and intake documentation;

(c) **Process Analytics:** ingestion of process telemetry from the hydrometallurgical leaching, solvent extraction and precipitation circuits; and

(d) **Recovery Reporting:** recovery-yield dashboards for lithium, nickel, cobalt and manganese, and the standard reports described in Section 3.

1.4 **Out of Scope.** Unless the parties agree otherwise in a change order under Section 8, the following are excluded: (a) custom software development beyond configuration of standard Platform functionality; (b) procurement or installation of Licensee hardware, scales, sensors or network equipment; (c) migration of historical records created before January 1, 2025; and (d) integrations other than those listed in Section 2.4.

## 2. Implementation Services

2.1 **Phase 1 – Discovery and Design.** Licensor shall:

(a) hold a project kickoff meeting with Licensee's project team, in person at the Licensed Site or by video conference;

(b) conduct workshops with Licensee's operations, quality, environmental, health and safety, and IT personnel to document current intake, custody and process-data workflows; and

(c) prepare a solution design document setting out the Platform configuration, data model, user roles, integration specifications and the edge connector deployment plan (the "**Design Document**").

2.2 **Phase 2 – Configuration.** Licensor shall configure the Platform in accordance with the approved Design Document. This includes site and process-area hierarchy, lot and container identifiers, custody event types, user roles and permissions for Authorized Users, alert thresholds and report templates.

2.3 **Phase 3 – Edge Connector Deployment.** Licensor shall provide, and remotely support Licensee in installing, the Platform's edge connectors on Licensee equipment at the Licensed Site under Section 4.2 of the Agreement. Licensor shall validate data flows from the intake scales, labelling stations and process historian identified in the Design Document.

2.4 **Phase 4 – Integrations.** Licensor shall configure the following integrations using the Platform's standard application programming interfaces:

(a) a one-way feed of process data from Licensee's process historian at the Licensed Site;

(b) a two-way interface with Licensee's enterprise resource planning system for supplier master data and shipment records; and

(c) single sign-on through Licensee's identity provider.

2.5 **Phase 5 – Testing.** Licensor shall carry out system and integration testing. It shall then support Licensee's user acceptance testing under Section 5.

2.6 **Phase 6 – Training and Go-Live.** Licensor shall deliver:

(a) up to four administrator training sessions and up to eight end-user training sessions, each of up to three hours, for Licensee's Authorized Users;

(b) training materials, which Licensee may copy for internal use at the Licensed Site; and

(c) go-live support, including on-site or remote attendance during the first two weeks of production use.

2.7 **Hypercare.** For 30 days after go-live, Licensor shall provide a named support engineer and a daily stand-up call with Licensee's project manager. After the hypercare period, the Platform is supported under Section 6 of the Agreement.

## 3. Deliverables

3.1 Licensor shall provide the following deliverables (each, a "**Deliverable**"):

| No. | Deliverable | Phase |
|---|---|---|
| D-1 | Project plan and RACI matrix | 1 |
| D-2 | Design Document | 1 |
| D-3 | Configured Platform environment for the Licensed Site | 2 |
| D-4 | Edge connector deployment and data-flow validation report | 3 |
| D-5 | Integration specifications and test results | 4 |
| D-6 | Test plan, test scripts and acceptance test report | 5 |
| D-7 | Training materials and attendance records | 6 |
| D-8 | Go-live readiness checklist and hypercare close-out report | 6 |

3.2 **Licensee-Owned Deliverables.** For the purposes of Section 9.2 of the Agreement, the following are Licensee-owned deliverables once Licensee has paid for them in full: the site-specific report templates and dashboard layouts, the process-area and custody-event configuration created only for Licensee, and the written content of Deliverables D-2, D-4 and D-8 that describes Licensee's operations. Section 9.2 of the Agreement applies to any Licensor pre-existing materials or general Platform functionality included in them.

## 4. Timeline

4.1 **Target Schedule.** The parties shall use reasonable efforts to meet the following target schedule, measured from the SOW Effective Date:

| Milestone | Target Completion |
|---|---|
| M1 – Kickoff held and Design Document approved | Week 6 |
| M2 – Platform configuration and edge connector deployment complete | Week 14 |
| M3 – Integrations complete and system testing passed | Week 20 |
| M4 – User acceptance testing completed | Week 24 |
| M5 – Go-live | Week 26 |
| M6 – Hypercare completed | Week 30 |

4.2 **Dependencies.** The target schedule depends on Licensee performing its responsibilities under Section 6 on time. If a Licensee delay affects the schedule, the parties shall agree a revised schedule through the change control procedure in Section 8.

## 5. Acceptance

5.1 **Acceptance Testing.** Licensee shall conduct user acceptance testing against the acceptance criteria in the approved Design Document and test plan within 15 business days after Licensor notifies Licensee that the Platform is ready for testing.

5.2 **Acceptance or Rejection.** Within that period, Licensee shall either confirm acceptance in writing or give Licensor written notice of each material non-conformity with the acceptance criteria, with reasonable detail. Licensor shall correct each notified non-conformity and resubmit the affected item for retesting, which shall follow the same procedure.

5.3 **Deemed Acceptance.** An item is accepted on the earlier of (a) Licensee's written acceptance; and (b) Licensee's use of the item in production for chain-of-custody recording at the Licensed Site, other than during a parallel run agreed in the test plan.

5.4 **Document Deliverables.** Licensee shall review each document Deliverable within 10 business days after receipt and either approve it or provide written comments. Licensor shall address reasonable comments and resubmit the Deliverable.

## 6. Licensee Responsibilities

Licensee shall:

(a) appoint a project manager with authority to make day-to-day project decisions and approve Deliverables;

(b) make appropriate operations, quality, IT and environmental, health and safety personnel available for workshops, testing and training;

(c) provide safe access to the Licensed Site for Licensor personnel during working hours, subject to Licensee's site safety induction, personal protective equipment and visitor rules;

(d) supply, install and maintain the servers, network connectivity, scales, scanners and other equipment on which edge connectors will run, as specified in the Design Document;

(e) provide timely access to its process historian, enterprise resource planning system and identity provider, and to the relevant vendor contacts; and

(f) review and validate sample data and confirm that the data submitted to the Platform during implementation complies with Section 3 of the Data Processing Addendum.

## 7. Fees and Expenses

7.1 **Implementation Fee.** Licensee shall pay Licensor a fixed fee of $165,000 for the Implementation Services (the "**Implementation Fee**"). The Implementation Fee is separate from the Subscription Fees.

7.2 **Payment Milestones.** Licensor shall invoice the Implementation Fee as follows:

| Milestone | Percentage | Amount |
|---|---|---|
| M1 – Design Document approved | 25% | $41,250 |
| M3 – Integrations complete and system testing passed | 25% | $41,250 |
| M4 – User acceptance testing completed | 30% | $49,500 |
| M6 – Hypercare completed | 20% | $33,000 |

7.3 **Expenses.** Licensee shall reimburse Licensor's reasonable, pre-approved travel and accommodation expenses for on-site attendance at the Licensed Site, at cost and supported by receipts, up to a total of $18,000 for this SOW. Licensor shall invoice expenses monthly in arrears.

7.4 **Additional Services.** Services outside the scope of this SOW will be charged at the following time-and-materials rates, only if approved in a change order:

| Role | Hourly Rate |
|---|---|
| Solution Architect | $265 |
| Implementation Consultant | $210 |
| Integration Engineer | $225 |
| Trainer | $175 |

7.5 **Payment Terms.** Invoices under this SOW are payable in accordance with Section 7 of the Agreement.

## 8. Change Control

8.1 Either party may request a change to the scope, Deliverables, schedule or fees under this SOW by written change request to the other party's project manager.

8.2 Within 10 business days after receiving or making a change request, Licensor shall provide a written impact assessment describing the effect of the change on scope, schedule and fees.

8.3 A change is effective only when set out in a written change order signed by authorized representatives of both parties. Until then, Licensor shall continue to perform this SOW without the change.

## 9. Project Governance

9.1 **Project Managers.** Each party shall appoint a project manager, identified at the kickoff meeting. Each party may replace its project manager on reasonable notice to the other.

9.2 **Status Reporting.** Licensor's project manager shall provide a written status report every two weeks, covering progress against the schedule, open risks and issues, and actions required from each party.

9.3 **Steering Committee.** A steering committee made up of one senior representative of each party shall meet monthly during the implementation to review progress and resolve escalated issues. Any dispute not resolved by the steering committee shall be handled under Section 16.3 of the Agreement.

9.4 **Personnel.** Licensor shall assign qualified personnel to perform the Implementation Services in accordance with Section 6.4 of the Agreement. Licensor personnel at the Licensed Site shall comply with Licensee's site safety rules notified to them in advance.

## 10. Data and Security

10.1 Licensor shall process any Personal Data received during the Implementation Services in accordance with the Data Processing Addendum.

10.2 Sample, test and migration data shall be loaded only into Licensor's United States-hosted environments, in accordance with Section 6.3 of the Data Processing Addendum. Licensor shall not copy Customer Data to personal devices or removable media.

10.3 The edge connectors deployed under Phase 3 shall be configured and updated in accordance with Annex 3 of the Data Processing Addendum.

## 11. Term

11.1 This SOW takes effect on the SOW Effective Date. It continues until the Implementation Services are completed and all Deliverables are accepted, unless terminated earlier under the Agreement. Section 3.2 of the Agreement applies if the Agreement expires before this SOW is completed.

---

**IN WITNESS WHEREOF**, the parties have executed this SOW as of the SOW Effective Date.

| **PROTOUX ANALYTICS, INC.** | **GLENOX CIRCULAR MATERIALS, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: | Name: |
| Title: | Title: |
| Date: | Date: |