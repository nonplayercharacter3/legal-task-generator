# STATEMENT OF WORK NO. 2: PHASE 2 IMPLEMENTATION

This Statement of Work No. 2 (this "**SOW**") is entered into as of September 15, 2026 (the "**SOW Effective Date**") by and between **Laipeisk Systems, Inc.**, a Delaware corporation ("**Licensor**"), and **Bredeix Organic Creamery, LLC**, a New York limited liability company ("**Licensee**").

This SOW is issued under the Software License and Services Agreement between Licensor and Licensee effective as of April 1, 2025 (the "**Agreement**"). It is governed by the Agreement. Capitalized terms used but not defined in this SOW have the meanings given in the Agreement.

## 1. Purpose and Background

1.1 **Purpose.** This SOW describes the Phase 2 Services and Deliverables for Licensee's implementation of the Software. Phase 2 extends the Software, implemented in Phase 1 for core milk-procurement and farmer-supplier records, to farmer-supplier payment processing, milk-quality tracking and logistics. It also records the status of Phase 1 as of the SOW Effective Date.

1.2 **Background.** The Parties acknowledge the following:

(a) Phase 1 of the implementation was performed under Statement of Work No. 1 dated April 1, 2025 ("**SOW No. 1**"). It covered configuration of the HerdLedger procurement module, migration of Licensee's farmer-supplier master records, and the producer-intake interface for Licensee's receiving stations (the "**Phase 1 Deliverable**").

(b) Licensee has informed Licensor that on August 28, 2026, the sole owner of Licensee's parent company, Bredeix Dairy Holdings, LLC, signed a Unit Purchase Agreement with Northfold Provisions Group. Closing of that transaction is expected in the first quarter of 2027.

(c) Licensee has asked that the Phase 2 schedule in Section 5 take account of the integration planning expected to follow that transaction. Licensor has agreed to the schedule in Section 5 on that basis. Nothing in this SOW constitutes Licensor's consent under Section 16.2 of the Agreement.

## 2. Phase 1 Status

2.1 **Phase 1 Delivery.** Licensor gave Delivery of the Phase 1 Deliverable to Licensee's designated test environment on July 20, 2026.

2.2 **Rejection Notice.** Licensee delivered to Licensor a Rejection Notice dated August 7, 2026. The notice identifies the following nonconformities with the Specifications in the Phase 1 Deliverable:

(a) duplicate producer records created during migration of the farmer-supplier master file;

(b) failure of the producer-intake interface to post component test results (butterfat, protein and somatic cell count) to the correct producer account; and

(c) incorrect application of organic premium rates to producers whose organic certification renewal dates fall within the current pay period.

Licensor contends that the Rejection Notice was not delivered within the period required by Section 6.2 of the Agreement and that the Phase 1 Deliverable has been accepted. Licensee disputes that the Phase 1 Deliverable has been deemed accepted and reserves all rights under the Agreement and SOW No. 1 in respect of the Phase 1 Deliverable and the Phase 1 milestone fee.

2.3 **Phase 1 Remediation.** Licensor will investigate the items listed in Section 2.2 as part of the Phase 2 data-readiness activities described in Section 3.2(a). Each Party's position under Section 2.2 remains unchanged by this.

## 3. Scope of Phase 2 Services

3.1 **Overview.** Licensor shall configure, integrate and deploy the following Software modules for Licensee's operations at its processing facility and its producer receiving stations in New York and Vermont:

(a) the farmer-supplier payment module;

(b) the milk-quality tracking module; and

(c) the logistics module.

3.2 **Services.** The Phase 2 Services consist of:

(a) **Data Readiness.** Licensor will review and cleanse the farmer-supplier master data in the Software, including producer identifiers, bank account details, organic certification records and premium schedules, so that the data can be used by the payment module.

(b) **Payment Module Configuration.** Licensor will configure producer pay calculations, including base price, component pricing, quality premiums and deductions, organic premiums, hauling charges, and cooperative and checkoff deductions. Licensor will also configure semi-monthly pay-period processing and producer settlement statements.

(c) **Banking Interface.** Licensor will build an ACH payment file interface to Licensee's designated bank, in NACHA format, together with the positive-pay file needed to issue producer payments.

(d) **Milk-Quality Tracking.** Licensor will configure the quality module to receive laboratory results from Licensee's contracted milk-testing laboratory, flag samples that exceed antibiotic-residue and somatic-cell thresholds, and generate producer quality reports.

(e) **Logistics.** Licensor will configure route, hauler and tanker-load records and the bill-of-lading reports for farm pickups.

(f) **ERP Interface.** Licensor will build a general-ledger export from the payment module to Licensee's enterprise resource planning system.

(g) **Training.** Licensor will provide up to six (6) half-day training sessions for Licensee's procurement, field-service and accounts-payable staff. Sessions may be remote or on site.

(h) **Go-Live Support.** Licensor will provide hypercare support for the first two (2) producer pay cycles processed in production.

3.3 **Out of Scope.** The following are outside this SOW unless added by change order under Section 3.4 of the Agreement: (a) interfaces to systems not listed in Section 3.2; (b) migration of historical producer pay data from before January 1, 2025; (c) customization of the Software's source code; and (d) hardware, network or third-party software procurement.

## 4. Deliverables and Specifications

4.1 **Deliverables.** The Phase 2 Deliverables are:

| No. | Deliverable | Description |
|---|---|---|
| D2-1 | Data Readiness Report | Cleansed farmer-supplier master data and a reconciliation report |
| D2-2 | Payment Module Configuration | Configured pay calculations and settlement statements, tested against two parallel pay cycles |
| D2-3 | Banking Interface | ACH and positive-pay file interfaces, validated with Licensee's bank |
| D2-4 | Quality and Logistics Configuration | Configured quality and logistics modules with laboratory import |
| D2-5 | ERP Interface | General-ledger export, validated against Licensee's chart of accounts |
| D2-6 | Production Go-Live | Deployment of D2-2 through D2-5 to production |

4.2 **Specifications.** The Specifications for each Deliverable are the functional and technical requirements set out in Exhibit 1 to this SOW (Phase 2 Functional Requirements, version 1.3, dated September 8, 2026) and the Documentation.

4.3 **Parallel Testing.** For Deliverable D2-2, Licensor's testing will include two (2) parallel pay cycles. In each cycle, producer pay calculated in the Software will be reconciled to pay calculated in Licensee's existing system. Variances must be explained and resolved before Delivery.

4.4 **Acceptance.** Delivery and acceptance of each Phase 2 Deliverable are governed by Section 6 of the Agreement.

## 5. Schedule

5.1 **Target Dates.** Licensor shall use commercially reasonable efforts to give Delivery of each Phase 2 Deliverable by the following target dates:

| Deliverable | Target Delivery Date |
|---|---|
| D2-1 Data Readiness Report | November 16, 2026 |
| D2-2 Payment Module Configuration | January 18, 2027 |
| D2-3 Banking Interface | January 18, 2027 |
| D2-4 Quality and Logistics Configuration | February 15, 2027 |
| D2-5 ERP Interface | March 15, 2027 |
| D2-6 Production Go-Live | April 19, 2027 |

5.2 **Dependencies.** The target dates depend on Licensee meeting its responsibilities under Section 7 on time. If Licensee is delayed in performing a responsibility, the affected target dates will be extended by a corresponding period.

## 6. Fees and Payment

6.1 **Phase 2 Fees.** The Phase 2 Services are provided on a fixed-fee basis. The total fixed fee is $412,000, payable as milestone fees under Section 5.2 of the Agreement:

| Milestone | Milestone Fee |
|---|---|
| Acceptance of D2-1 | $41,200 |
| Acceptance of D2-2 | $103,000 |
| Acceptance of D2-3 | $61,800 |
| Acceptance of D2-4 | $72,100 |
| Acceptance of D2-5 | $51,500 |
| Acceptance of D2-6 | $82,400 |
| **Total** | **$412,000** |

6.2 **Training and Hypercare.** The training in Section 3.2(g) and the hypercare support in Section 3.2(h) are included in the fixed fee.

6.3 **Additional Services.** Services requested beyond the scope of this SOW will be charged at the following rates under a change order: Solution Architect, $245 per hour; Implementation Consultant, $195 per hour; Integration Developer, $210 per hour.

6.4 **Expenses.** Licensee shall reimburse reasonable, pre-approved travel expenses for on-site work, in line with Licensee's travel policy. Licensor will invoice these expenses at cost, monthly in arrears.

6.5 **Invoicing.** Licensor shall invoice each milestone fee on acceptance of the related Deliverable. Payment is due in accordance with Section 5.3 of the Agreement.

## 7. Licensee Responsibilities

Licensee shall:

(a) designate a project manager with authority to make day-to-day project decisions;

(b) provide current producer contracts, premium schedules and organic certification records by October 15, 2026;

(c) arrange for its bank and its milk-testing laboratory to provide file specifications and test environments by November 2, 2026;

(d) make procurement and accounts-payable staff available for parallel-cycle reconciliation; and

(e) provide test environment access and credentials for its ERP system.

## 8. Project Governance

8.1 **Project Managers.** Licensor's project manager is Dana Ostrovik. Licensee's project manager is Marcus Telley. Either Party may replace its project manager on written notice.

8.2 **Status Meetings.** The project managers shall meet weekly, and Licensor shall circulate a written status report after each meeting covering progress, risks, open issues and schedule.

8.3 **Steering Committee.** A steering committee of one senior executive from each Party shall meet monthly. It serves as the first escalation level under Section 15.2 of the Agreement.

## 9. Personal Data

The Phase 2 Services involve processing of Personal Data of Licensee's farmer-suppliers, including bank account and payment information, and of Licensee's employees. That processing is governed by the DPA.

## 10. Term of SOW

This SOW begins on the SOW Effective Date. It continues until acceptance of Deliverable D2-6 and completion of the hypercare support in Section 3.2(h), unless terminated earlier under the Agreement.

---

**IN WITNESS WHEREOF**, the Parties have executed this SOW as of the SOW Effective Date.

**LAIPEISK SYSTEMS, INC.**

By: ______________________________
Name:
Title:

**BREDEIX ORGANIC CREAMERY, LLC**

By: ______________________________
Name:
Title:

---

*Exhibit 1: Phase 2 Functional Requirements, version 1.3, dated September 8, 2026 (attached separately)*