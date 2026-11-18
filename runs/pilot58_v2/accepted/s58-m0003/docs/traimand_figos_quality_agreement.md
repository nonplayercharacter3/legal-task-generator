# QUALITY AGREEMENT

**Data Handling, Data Integrity and Model Validation**

This Quality Agreement is entered into as of **January 15, 2024** (the "**QA Effective Date**") by and between **Figos Analytics, LLC**, a Delaware limited liability company with its principal place of business at 410 Marquette Avenue, Suite 1200, Minneapolis, Minnesota 55401 ("**Licensor**"), and **Traimand Seed Genetics, Inc.**, an Iowa corporation with its principal place of business at 2250 Prairie Ridge Road, Ankeny, Iowa 50023 ("**Customer**"). Licensor and Customer are each a "**Party**" and together the "**Parties**."

## 1. PURPOSE AND SCOPE

**1.1 Purpose.** This Quality Agreement is the Quality Agreement referred to in the Software License Agreement between the Parties dated January 15, 2024 (the "**License Agreement**"). It sets out the Parties' responsibilities for data handling, data integrity and the validation of genomic prediction models on the Platform.

**1.2 Scope.** This Quality Agreement applies to:

(a) the receipt, storage, processing, use, retention, return and deletion of Customer Data by Licensor;

(b) the controls Licensor maintains over the integrity of data processed through the Platform Modules; and

(c) the validation of GEBV calculation methodology and model changes before deployment to Customer's production environment, including validation under Special Terms Section 2 of Order Form No. OF-001.

**1.3 Relationship to License Agreement.** This Quality Agreement forms part of the License Agreement. Capitalized terms used but not defined in this Quality Agreement have the meanings given in the License Agreement. References to Sections are to Sections of this Quality Agreement unless otherwise stated.

## 2. DEFINITIONS

**2.1 Customer Data.** "**Customer Data**" means the raw data files uploaded by Customer to the Platform, including genotype call files, marker panels, phenotypic trial records, pedigree files and associated metadata, in the form in which Customer or its Authorized Users upload them.

**2.2 Other Definitions.** In this Quality Agreement:

"**Change Control Record**" means the record described in Section 7.4.

"**Model Change**" means any Update that changes GEBV calculation methodology, default model parameters, marker quality-control thresholds, imputation methods or the relationship matrices used in GEBV computation.

"**Production Environment**" means the instance of the Platform that Customer's Authorized Users use for operational breeding and selection decisions.

"**Quality Representative**" means the individual each Party designates under Section 3.1.

"**Validation Environment**" means a non-production instance of the Platform, logically segregated from the Production Environment, that Licensor provides for validation under Section 7.

"**Validation Protocol**" means the written protocol for a Model Change prepared and approved under Section 7.2.

"**Validation Report**" means the written report of the results of executing a Validation Protocol, prepared under Section 7.3.

## 3. QUALITY GOVERNANCE

**3.1 Quality Representatives.** Each Party shall designate a Quality Representative and notify the other Party of that person's name and contact details in writing. A Party may change its Quality Representative on written notice. As of the QA Effective Date:

| | **Licensor** | **Customer** |
|---|---|---|
| Quality Representative | Dr. Priya N. Halvorsen, Director, Scientific Quality | Dr. Samuel K. Ostrander, Director of Breeding Informatics |

**3.2 Quarterly Reviews.** The Quality Representatives, together with Licensor's named account scientist under Special Terms Section 3 of Order Form No. OF-001, shall meet at least once per calendar quarter. At each meeting they shall review: (a) open data integrity deviations; (b) planned Model Changes; (c) Validation Reports issued since the previous meeting; and (d) any Security Incident notified under Section 9.2 of the License Agreement. Licensor shall circulate written minutes within ten (10) business days after each meeting.

**3.3 Escalation.** If the Quality Representatives cannot resolve a quality matter within fifteen (15) business days after either of them raises it in writing, either Party may escalate it to Licensor's Chief Executive Officer and Customer's General Counsel. Those individuals shall confer in good faith for at least ten (10) business days before either Party pursues other remedies under the License Agreement.

## 4. DATA HANDLING

**4.1 Receipt and Ingestion.** Licensor shall ingest Customer Data only through the secure upload interfaces of the Trial Data Manager and other Platform Modules, or through encrypted transfer channels agreed in writing by the Quality Representatives. Licensor shall log each upload, including file name, file size, checksum, uploading user and timestamp.

**4.2 Segregation.** Licensor shall logically segregate Customer Data from the data of Licensor's other customers. Access controls shall prevent any other customer from viewing or accessing Customer Data.

**4.3 Personnel Access.** Licensor shall limit access to Customer Data to personnel and permitted subcontractors who need that access to provide the Platform or Services to Customer. Each such person must have completed Licensor's data handling training within the preceding twelve (12) months. Licensor shall review access rights at least quarterly and revoke them promptly when no longer required.

**4.4 Hosting Location.** Licensor shall store and process Customer Data only in the United States, consistent with Section 3.4 of Order Form No. OF-001.

**4.5 Subcontractors.** Licensor shall maintain a list of subcontractors that host or process Customer Data and provide it to Customer on request. Licensor shall give Customer at least thirty (30) days' written notice before adding a subcontractor that will host or process Customer Data. Each such subcontractor must be bound by written obligations at least as protective of Customer Data as this Quality Agreement and Section 9 of the License Agreement.

**4.6 Security.** Licensor shall protect Customer Data in accordance with Section 9.1 of the License Agreement. Licensor shall notify and handle Security Incidents in accordance with Section 9.2 of the License Agreement.

## 5. DATA USE, RETENTION AND DELETION

**5.1 Permitted Use.** Licensor shall use Customer Data solely to provide the Platform and Services to Customer under the License Agreement, including to compute GEBVs and other analytics that Customer requests through the Platform Modules, to provide support, and to perform validation under Section 7.

**5.2 No Training for Other Customers.** Licensor shall not use Customer Data to develop, train, calibrate, tune or benchmark any statistical or machine-learning model, reference panel or imputation library that Licensor offers or makes available to any other customer or third party. Licensor shall not combine Customer Data with the data of any other customer for any purpose.

**5.3 No Disclosure or Sale.** Licensor shall not sell, license, disclose or otherwise make Customer Data available to any third party, except to permitted subcontractors under Section 4.5 or as required by law in accordance with Section 9.5 of the License Agreement.

**5.4 Retention During the Subscription Term.** During the Subscription Term, Licensor shall retain Customer Data for as long as Customer maintains it on the Platform. Customer may delete individual files through the Platform interface. On Customer's written request, Licensor shall delete specified Customer Data from the Production Environment and the Validation Environment within thirty (30) days and confirm the deletion in writing.

**5.5 Return.** On expiration or termination of an Order Form, Licensor shall make Customer Data available for export in accordance with Section 12.4 of the License Agreement.

**5.6 Deletion After Termination.** Within thirty (30) days after the end of the export period under Section 12.4 of the License Agreement following expiration or termination of the last Order Form, Licensor shall permanently delete all Customer Data from its systems and the systems of its subcontractors, including the Production Environment, the Validation Environment and all backups. Backup media that cannot practicably be purged sooner shall be overwritten in the ordinary rotation cycle, which shall not exceed ninety (90) days, and shall remain subject to Section 9 of the License Agreement until overwritten.

**5.7 Certification.** Within ten (10) business days after completing deletion under Section 5.6, an officer of Licensor shall certify the deletion to Customer in writing.

## 6. DATA INTEGRITY

**6.1 Integrity Controls.** Licensor shall maintain controls designed to ensure that Customer Data is processed completely and accurately. At a minimum, those controls shall include:

(a) checksum verification of each uploaded file against the checksum recorded at upload;

(b) automated validation of file format, marker identifiers, sample identifiers and pedigree consistency, with exceptions reported to Customer through the Trial Data Manager;

(c) version control of each dataset used in a GEBV computation, so that any GEBV run can be traced to the input dataset version, model version and parameter set used; and

(d) audit trails recording the creation, modification and deletion of records, which Authorized Users cannot alter.

**6.2 Deviations.** Licensor shall notify Customer's Quality Representative within two (2) business days after identifying any deviation that has caused, or is reasonably likely to cause, incorrect GEBVs or other outputs to be delivered to the Production Environment. The notice shall describe the deviation, the affected runs and the proposed corrective action. Licensor shall complete a root-cause investigation and provide a written corrective and preventive action plan within twenty (20) business days after the notice.

**6.3 Re-computation.** If a deviation attributable to Licensor causes incorrect GEBVs to be delivered, Licensor shall re-run the affected computations and deliver corrected results at no additional charge.

**6.4 Customer Responsibilities.** Customer is responsible for the accuracy and completeness of the data it uploads, consistent with Section 6.1 of the License Agreement. Customer shall review data validation exception reports promptly and correct or confirm flagged records.

## 7. MODEL VALIDATION

**7.1 Validation Required.** Licensor shall not deploy a Model Change to the Production Environment until it has been validated in accordance with this Section 7. Security patches and bug fixes that do not alter GEBV calculation results are not Model Changes. Licensor shall document its basis for that determination in the Change Control Record.

**7.2 Validation Protocol.** At least thirty (30) days before the planned deployment of a Model Change, Licensor shall deliver to Customer's Quality Representative a draft Validation Protocol. The Validation Protocol shall describe:

(a) the nature of the Model Change and the reasons for it;

(b) the reference datasets to be used, drawn from Customer's historical genotypic and phenotypic data held on the Platform;

(c) the validation method, including the cross-validation scheme or forward-validation design to be used;

(d) the metrics to be reported, including predictive ability, rank correlation of GEBVs between the current and proposed methods, regression bias, and the proportion of top-ranked lines retained within the top 10% under each method, reported by crop and maturity group; and

(e) acceptance criteria.

Customer shall approve the Validation Protocol, or provide written comments, within ten (10) business days after receipt. Licensor shall address Customer's reasonable comments before executing the Validation Protocol.

**7.3 Execution and Validation Report.** Licensor shall execute the approved Validation Protocol in the Validation Environment and deliver a Validation Report to Customer's Quality Representative. The Validation Report shall present results against each acceptance criterion and identify any deviation from the Validation Protocol. Customer shall accept or reject the Validation Report in writing within ten (10) business days after receipt. Customer may reject the Validation Report only if an acceptance criterion is not met or the Validation Protocol was not followed in a material respect.

**7.4 Change Control Record.** Licensor shall maintain a Change Control Record for each Model Change. The record shall include the Validation Protocol, the Validation Report, Customer's acceptance, the deployment date, and the model and software versions deployed. Licensor shall make the Change Control Record available to Customer on request.

**7.5 Deployment Timing.** Licensor shall schedule deployments of Model Changes in accordance with Special Terms Section 1 of Order Form No. OF-001. Licensor shall retain the immediately preceding model version for at least twelve (12) months after deployment of a Model Change. On Customer's request during that period, Licensor shall re-run any computation under the preceding version for comparison.

**7.6 Customer-Requested Models.** If Customer requests the configuration of a custom model or parameter set, Licensor shall validate it under this Section 7 before it is used in the Production Environment. The Parties shall agree any associated Fees in a Statement of Work.

## 8. RECORDS AND AUDIT

**8.1 Record Retention.** Licensor shall retain Validation Protocols, Validation Reports, Change Control Records, deviation investigations and quarterly review minutes for the Subscription Term and for three (3) years after it ends. Those records shall not contain Customer Data except to the extent required to document validation results in summary form.

**8.2 Quality Audits.** Once per contract year, on thirty (30) days' written notice, Customer or an independent auditor bound by confidentiality obligations may audit Licensor's compliance with this Quality Agreement during normal business hours. Customer may also conduct an audit following a Security Incident or a deviation notified under Section 6.2. Audits under this Section 8.2 are in addition to Customer's rights under Section 9.6 of the License Agreement. Each Party shall bear its own costs of an audit, unless the audit reveals a material non-compliance by Licensor, in which case Licensor shall reimburse Customer's reasonable audit costs.

**8.3 Findings.** Licensor shall respond in writing to audit findings within twenty (20) business days, with a corrective action plan and timeline for each finding.

## 9. TERM AND AMENDMENT

**9.1 Term.** This Quality Agreement begins on the QA Effective Date and continues for as long as the License Agreement remains in effect. Sections 5.5, 5.6, 5.7 and 8.1 survive expiration or termination until Licensor's obligations under them are fully performed.

**9.2 Review.** The Quality Representatives shall review this Quality Agreement at least once every two (2) years and recommend any amendments.

**9.3 Amendment.** This Quality Agreement may be amended only by a written instrument signed by authorized representatives of both Parties, in accordance with Section 15.6 of the License Agreement.

**9.4 Counterparts.** This Quality Agreement may be executed in counterparts, including by electronic signature. Each counterpart is an original, and together they constitute one instrument.

IN WITNESS WHEREOF, the Parties have executed this Quality Agreement as of the QA Effective Date.

| **FIGOS ANALYTICS, LLC** | **TRAIMAND SEED GENETICS, INC.** |
|---|---|
| By: _______________________ | By: _______________________ |
| Name: Daniel R. Okafor | Name: Margaret L. Vries |
| Title: Chief Executive Officer | Title: President and Chief Executive Officer |
| Date: January 15, 2024 | Date: January 15, 2024 |