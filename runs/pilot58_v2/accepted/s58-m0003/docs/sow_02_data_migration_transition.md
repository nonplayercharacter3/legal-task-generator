# STATEMENT OF WORK NO. 02

**Data Migration and Transition Services**

**Licensor:** Figos Analytics, LLC
**Customer:** Traimand Seed Genetics, Inc.
**SOW Date:** October 28, 2026 (the "**SOW Effective Date**")
**Governing Agreement:** Software License Agreement between Licensor and Customer dated January 15, 2024 (the "**License Agreement**")

This Statement of Work is entered into under Section 4.2 of the License Agreement and forms part of it. Capitalized terms used but not defined in this Statement of Work have the meanings given in the License Agreement. References to Sections are to Sections of this Statement of Work unless otherwise stated.

## RECITALS

A. Customer subscribes to the Platform Modules under Order Form No. OF-001. Customer uses the Platform to compute GEBVs and support selection decisions in its corn and soybean breeding programs.

B. Customer holds historical multi-environment trial data in legacy systems that has not been loaded to the Platform. Customer wishes Licensor to migrate that data to the Platform, harmonize it with Customer Data already on the Platform, and prepare Customer's complete breeding dataset for transfer to other systems.

C. On September 22, 2026, Customer entered into an Agreement and Plan of Merger with Kestrel Row Crop Holdings, Inc. ("**Kestrel**"). Under that agreement, Customer will become a wholly owned subsidiary of Kestrel. Customer expects to integrate its breeding informatics operations with those of Kestrel's other row crop businesses after closing, and requires the transition deliverables described in this Statement of Work to support that integration.

D. The Parties wish to set out the scope, schedule and Fees for the Services described below.

## 1. DEFINITIONS

In this Statement of Work:

"**Legacy Systems**" means Customer's BreedTrak laboratory information management system (version 6.2), its archived Oracle trial database, and the spreadsheet archives maintained by Customer's regional research stations, each as identified in Exhibit A.

"**Legacy Trial Data**" means the phenotypic trial records, plot-level yield and agronomic observations, environmental and management covariates, seed lot records and associated metadata for trial seasons 2009 through 2023 that Customer extracts from the Legacy Systems and supplies to Licensor under this Statement of Work. Legacy Trial Data includes data generated at cooperator sites operated by growers under agreements with Customer, and data relating to germplasm that Customer has in-licensed from third parties.

"**Migration Specification**" means the written specification described in Section 3.1.

"**Transition Package**" means the export of Customer's breeding dataset described in Section 3.4.

## 2. OBJECTIVES

The objectives of this Statement of Work are to:

(a) load the Legacy Trial Data to the Platform through the Trial Data Manager so that it is available for GEBV computation alongside Customer Data already on the Platform;

(b) harmonize trait definitions, units, location identifiers and germplasm identifiers across the Legacy Trial Data and existing Customer Data; and

(c) produce a complete, documented Transition Package that Customer can load to other breeding informatics systems.

## 3. SCOPE OF SERVICES

**3.1 Migration Specification.** Within fifteen (15) business days after the SOW Effective Date, Licensor shall prepare and deliver a Migration Specification for Customer's review. The Migration Specification shall:

(a) map each source field in the Legacy Systems to the corresponding Trial Data Manager field;

(b) define transformation rules for trait units, date formats, location codes and germplasm identifiers;

(c) set out data quality rules and the treatment of records that fail them; and

(d) describe reconciliation reporting, including record counts by season, location and crop.

Customer shall approve the Migration Specification, or provide written comments, within ten (10) business days after receipt. Licensor shall address Customer's reasonable comments and redeliver the Migration Specification within five (5) business days.

**3.2 Extraction Support.** Customer shall extract the Legacy Trial Data from the Legacy Systems and deliver it to Licensor through the encrypted transfer channel agreed by the Quality Representatives under Section 4.1 of the Quality Agreement. Licensor shall provide up to forty (40) hours of technical assistance to Customer's personnel in preparing extraction scripts and file layouts that conform to the Migration Specification.

**3.3 Migration and Harmonization.** Licensor shall:

(a) transform and load the Legacy Trial Data to the Platform in accordance with the approved Migration Specification;

(b) apply the integrity controls described in Section 6.1 of the Quality Agreement to each loaded file;

(c) harmonize germplasm identifiers in the Legacy Trial Data against the pedigree records held in the Pedigree and Relationship Module, and report unresolved identifiers to Customer;

(d) deliver a reconciliation report for each trial season showing records received, records loaded, records rejected and the reason for each rejection; and

(e) perform one trial GEBV run for each crop using the harmonized dataset, and deliver a comparison of predictive ability against the most recent production run.

**3.4 Transition Package.** Following acceptance of the migration under Section 5, Licensor shall prepare and deliver a Transition Package containing:

(a) all Customer Data held on the Platform, including the migrated Legacy Trial Data, in CSV and Apache Parquet formats;

(b) the GEBVs, marker-effect estimates and genomic relationship matrices from the most recent production run for each crop and maturity group;

(c) the model specifications and parameter sets used in those runs, sufficient to permit an independent quantitative geneticist to reproduce the computation outside the Platform;

(d) a data dictionary describing each file, field, unit and code list; and

(e) a manifest listing each file with its record count and checksum.

**3.5 Knowledge Transfer.** Licensor shall conduct up to three (3) remote working sessions, each of up to four (4) hours, with Customer's breeding informatics team and any third-party systems personnel Customer designates, to walk through the Transition Package and answer questions about its structure and contents.

**3.6 Out of Scope.** The following are outside the scope of this Statement of Work: (a) extraction of data from the Legacy Systems, except the assistance described in Section 3.2; (b) correction of source data errors in the Legacy Systems; (c) configuration of any system other than the Platform; and (d) any Model Change. Any of those services may be added only by a change order under Section 4.4 of the License Agreement.

## 4. DELIVERABLES AND SCHEDULE

| **No.** | **Deliverable** | **Target Date** |
|---|---|---|
| 1 | Migration Specification | 15 business days after SOW Effective Date |
| 2 | Migrated and harmonized Legacy Trial Data, with reconciliation reports | 30 business days after receipt of complete Legacy Trial Data |
| 3 | Trial GEBV run comparison | 10 business days after Deliverable 2 |
| 4 | Transition Package | 15 business days after acceptance of Deliverables 2 and 3 |
| 5 | Knowledge transfer sessions | Within 20 business days after delivery of Deliverable 4 |

Target dates for Deliverables 2 through 5 are extended day for day for any delay caused by Customer's failure to supply the Legacy Trial Data or to perform its responsibilities under Section 6.

## 5. ACCEPTANCE

**5.1 Review.** Customer shall review each Deliverable within ten (10) business days after receipt and notify Licensor in writing of its acceptance or of any material nonconformity with this Statement of Work or the approved Migration Specification.

**5.2 Correction.** Licensor shall correct any notified nonconformity and redeliver the Deliverable within ten (10) business days. The review process in Section 5.1 then applies to the redelivered Deliverable.

**5.3 Deemed Acceptance.** A Deliverable is deemed accepted if Customer does not notify Licensor of a material nonconformity within the review period, or if Customer uses the Deliverable in its Production Environment for operational selection decisions.

## 6. CUSTOMER RESPONSIBILITIES

**6.1** Customer shall designate Dr. Samuel K. Ostrander, Director of Breeding Informatics, as its project lead for this Statement of Work.

**6.2** Customer shall deliver the complete Legacy Trial Data to Licensor within twenty (20) business days after approval of the Migration Specification.

**6.3** Customer shall provide timely access to personnel familiar with the Legacy Systems and shall resolve data quality queries within five (5) business days after Licensor raises them.

**6.4** Customer is responsible for obtaining all rights and consents needed to provide the Legacy Trial Data to Licensor for the purposes of this Statement of Work, consistent with Sections 3.2 and 6.1 of the License Agreement.

## 7. CUSTOMER INDEMNITY

**7.1 Indemnity.** Customer shall defend Licensor and its Affiliates, and their officers, directors and employees, against any third-party claim arising from the Legacy Trial Data or from Licensor's receipt, processing, loading or transfer of the Legacy Trial Data in accordance with this Statement of Work. This includes any claim that the Legacy Trial Data was collected, used or transferred in breach of grower agreements, cooperator trial agreements, third-party germplasm licenses, material transfer agreements or other obligations owed by Customer to any third party. Customer shall indemnify those persons against all Losses arising from any such claim.

**7.2 Exclusions.** Customer has no obligation under Section 7.1 to the extent a claim arises from Licensor's use or disclosure of the Legacy Trial Data other than as permitted by the License Agreement, the Quality Agreement or this Statement of Work.

**7.3 Procedure.** The procedure in Section 10.4 of the License Agreement applies to claims under this Section 7.

## 8. SUBSCRIPTION STATUS

**8.1 Non-Renewal Notice.** On October 14, 2026, Customer delivered to Licensor written notice of non-renewal of Order Form No. OF-001 under Section 12.2 of the License Agreement. Licensor has notified Customer in writing that it disputes the effectiveness of that notice.

**8.2 Reservation of Positions.** Neither Party waives, and each Party expressly reserves, its rights and positions regarding the notice described in Section 8.1. Nothing in this Statement of Work, and no performance or payment under it, constitutes an admission by either Party regarding the effectiveness of that notice or the duration of the Subscription Term.

**8.3 Performance.** Licensor shall perform the Services in accordance with this Statement of Work regardless of the resolution of the matter described in Section 8.1.

## 9. FEES AND INVOICING

**9.1 Fees.** The Fees for the Services are as follows:

| **Item** | **Fees (USD)** |
|---|---|
| Migration Specification (Deliverable 1) | $24,000 |
| Migration, harmonization and trial GEBV run (Deliverables 2 and 3) | $96,500 |
| Transition Package (Deliverable 4) | $48,000 |
| Knowledge transfer sessions (Deliverable 5) | $18,000 |
| **Total** | **$186,500** |

**9.2 Additional Services.** Technical assistance under Section 3.2 above forty (40) hours, and any other Services agreed by change order, are charged at $285 per hour.

**9.3 Invoicing.** Licensor shall invoice the Fee for each Deliverable monthly in arrears following its acceptance, in accordance with Section 5.1 of the License Agreement. Invoices are payable in accordance with Section 5.2 of the License Agreement.

**9.4 Expenses.** All Services will be performed remotely. No travel or other expenses are chargeable under this Statement of Work.

## 10. PROJECT GOVERNANCE

**10.1 Project Leads.** Licensor's project lead for this Statement of Work is Rachel T. Lindqvist, VP, Customer Accounts. Each Party may change its project lead on written notice.

**10.2 Status Reporting.** The project leads shall meet by video conference at least every two weeks during the term of this Statement of Work. Licensor shall circulate a written status report before each meeting covering progress against the schedule in Section 4, open issues and risks.

**10.3 Data Handling.** Licensor shall handle the Legacy Trial Data and all other Customer Data processed under this Statement of Work in accordance with Section 9 of the License Agreement and the Quality Agreement.

## 11. TERM

This Statement of Work begins on the SOW Effective Date. It continues until all Deliverables have been accepted and the knowledge transfer sessions have been completed, unless terminated earlier under Section 12.3 of the License Agreement.

---

The Parties have executed this Statement of Work as of the SOW Effective Date.

| **FIGOS ANALYTICS, LLC** | **TRAIMAND SEED GENETICS, INC.** |
|---|---|
| By: _______________________ | By: _______________________ |
| Name: Daniel R. Okafor | Name: Margaret L. Vries |
| Title: Chief Executive Officer | Title: President and Chief Executive Officer |
| Date: October 28, 2026 | Date: October 28, 2026 |

---

### EXHIBIT A — LEGACY SYSTEMS

| **System** | **Content** | **Seasons** | **Approx. Volume** |
|---|---|---|---|
| BreedTrak LIMS v6.2 | Corn and soybean yield trials, agronomic notes, seed lot records | 2015–2023 | 4.1 million plot records |
| Archived Oracle trial database | Corn yield trials and environmental covariates | 2009–2014 | 2.3 million plot records |
| Regional research station spreadsheet archives | Soybean maturity, disease ratings and cooperator site observations | 2009–2023 | Approx. 3,800 workbook files |