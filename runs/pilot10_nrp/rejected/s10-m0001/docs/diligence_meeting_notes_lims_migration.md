# DILIGENCE MEETING NOTES: IT / LIMS DATA MIGRATION AND EMPLOYEE TRANSFER

**Project HemaQuik: Kolais Animal Health Diagnostics, Inc. / Sounour Veterinary Systems, LLC**

**Privileged & Confidential: Attorney Work Product / Prepared at the Direction of Counsel**

| | |
|---|---|
| **Date** | May 27, 2026 |
| **Time** | 10:00 a.m. – 12:15 p.m. ET |
| **Format** | Video conference |
| **Prepared by** | Buyer deal counsel (associate) |

## 1. Attendees

**Kolais Animal Health Diagnostics, Inc. ("Buyer")**
- VP, Information Technology
- Director, Quality and Regulatory Affairs
- Director, Human Resources
- Corporate Development lead

**Sounour Veterinary Systems, LLC ("Seller")**
- Chief Information Officer
- HemaQuik Program Manager
- Head of People Operations

**Counsel**
- Buyer deal counsel (two attendees)
- Seller deal counsel (one attendee)

## 2. Purpose and Background

2.1 This session was a follow-up to the IT and HR diligence request lists. It covered three topics: (a) how data and records of the Business will be separated from Seller's systems and migrated to Buyer; (b) the scope of IT and data migration support under the Transition Services Agreement; and (c) the process for Buyer's offers of employment to Seller employees dedicated to the Business.

2.2 Background. The Asset Purchase Agreement was signed May 18, 2026 (the "APA"), with Closing scheduled for June 30, 2026. Capitalized terms not defined in these notes have the meanings given in the APA. The topics discussed relate mainly to APA Sections 2.1(e) and 2.1(f) (regulatory, quality and complaint records; customer lists and books and records), Section 2.2 (Excluded Assets), Section 6.5 (Employees) and Section 6.6 (Transition Services).

## 3. Current Systems Landscape (Seller Presentation)

3.1 Seller's CIO gave an overview of the systems that support the Business:

(a) **LIMS.** Seller runs one laboratory information management system instance. Both the Retained Business (the reference laboratories) and the HemaQuik quality control laboratory use it. HemaQuik cartridge lot release testing, QC calibration data and stability study results are stored in a separate HemaQuik "project space" within that instance. Seller confirmed that reference laboratory patient and client data is in separate project spaces. HemaQuik QC users do not have access to that data.

(b) **ERP.** Seller uses one ERP system for both businesses. HemaQuik transactions are tracked under a dedicated business unit code, so HemaQuik inventory, bills of materials, open purchase orders and customer master records can be filtered and extracted.

(c) **Complaint handling and CAPA.** Seller keeps a standalone complaint-handling and CAPA database. It contains HemaQuik records only and can be transferred as a whole.

(d) **Firmware and software repositories.** HemaQuik analyzer firmware, the cartridge-reader software and the related build tooling are kept in a dedicated source-code repository. Seller confirmed that no Retained Business code is stored in it.

(e) **Document control.** HemaQuik design history files, device master records and technical documentation are kept in Seller's electronic document management system under a HemaQuik library.

3.2 Seller confirmed that the systems themselves (the LIMS instance, the ERP instance and the enterprise licenses) are used by the Retained Business and stay with Seller as Excluded Assets. Buyer receives the HemaQuik data and records held in those systems, which are Purchased Assets under Sections 2.1(e) and 2.1(f).

## 4. Data Separation and Migration Approach

4.1 The parties discussed a phased approach:

(a) **Phase 1 (pre-Closing through Closing).** Seller will produce full extracts of the complaint/CAPA database, the source-code repository and the HemaQuik document control library. These will be delivered to Buyer at Closing. Buyer IT confirmed it can host all three in its existing environment from Day 1.

(b) **Phase 2 (post-Closing, under the Transition Services Agreement).** The HemaQuik LIMS project space and the HemaQuik ERP data will be migrated to Buyer's systems. Until cutover, Seller will provide Buyer's QC staff with continued, segregated access to the HemaQuik LIMS project space so that cartridge lot release is not interrupted.

(c) **Phase 3 (cutover and decommissioning).** After Buyer validates the migrated data, Seller will remove Buyer's access to the HemaQuik project space. It will then archive or delete the HemaQuik data held on its systems, as instructed by Buyer and subject to applicable record-retention requirements.

4.2 Seller's CIO estimated that Phase 2 can be completed in four to six months after Closing. That is within the support period of up to nine months after the Closing Date in APA Section 6.6. Buyer's VP of IT agreed the estimate was reasonable and noted the remaining period as contingency.

4.3 Buyer's Director of Quality explained that the migrated LIMS data must be validated before Buyer relies on it for lot release. This includes audit trails and electronic signature records. Seller agreed to provide its existing LIMS validation documentation and data dictionary for the HemaQuik project space. Seller also agreed to make a LIMS administrator available to support Buyer's validation testing.

4.4 Seller confirmed there are no third-party license restrictions preventing the export of HemaQuik data from the LIMS or ERP in standard formats (CSV/XML and database dumps).

## 5. Transition Services Agreement: IT Scope

5.1 The parties walked through the draft IT and data migration service schedule to the Transition Services Agreement. Points agreed in principle:

(a) **Services.** Continued hosting of, and segregated user access to, the HemaQuik LIMS project space and ERP business unit. Data extraction and migration support. Help-desk support for transferred users during the transition.

(b) **Service levels.** Service levels to be consistent with those Seller currently provides internally to the HemaQuik team.

(c) **Data security.** Seller will apply the same security controls to HemaQuik data that it applies to its own data. Access will be limited to named Seller IT personnel who need it to perform the services.

(d) **Pricing.** Cost-plus pricing, consistent with the draft service schedule circulated by Seller's counsel.

5.2 Seller's counsel will circulate a revised IT service schedule reflecting these points. No changes to the APA were proposed or needed.

## 6. Employee Transfer

6.1 **Population.** Seller's Head of People Operations confirmed that 41 employees are dedicated to the Business. They work in engineering (14), manufacturing and QC (17), field service (6) and product management/marketing (4). Buyer's Director of HR confirmed that these employees correspond to the population Buyer has identified for offers under APA Section 6.5.

6.2 **Shared IT personnel.** Two Seller IT staff support both the LIMS and the HemaQuik QC laboratory. They will stay with Seller and will provide transition support under the Transition Services Agreement. Buyer does not intend to extend offers to them.

6.3 **Offer timing.** Buyer intends to extend offers by June 12, 2026, with acceptance due by June 22, 2026 and employment effective as of the Closing Date. Seller agreed to make employees available for information sessions during the week of June 8, 2026.

6.4 **Pre-Closing employee liabilities.** Seller confirmed that it will pay all accrued wages, bonuses, accrued paid time off and other compensation for the period through the Closing Date. This is consistent with APA Section 2.4(d). Buyer HR will provide its benefits enrollment timeline so that transferring employees have no gap in health coverage.

6.5 **Employee data.** Seller will transfer personnel files of employees who accept Buyer's offers, subject to applicable privacy law and each employee's consent where required. Personnel files of employees who do not accept will not be transferred.

6.6 **System access for transferring employees.** Transferring employees will receive Buyer credentials on the Closing Date. During Phase 2, those who need continued access to the HemaQuik LIMS project space or ERP business unit will receive Seller guest credentials limited to the HemaQuik data, as set out in Section 4.1(b) of these notes.

## 7. Action Items

| # | Action | Owner | Target Date |
|---|---|---|---|
| 1 | Circulate revised IT/data migration service schedule to the Transition Services Agreement | Seller counsel | June 3, 2026 |
| 2 | Deliver HemaQuik LIMS validation documentation and data dictionary | Seller CIO | June 5, 2026 |
| 3 | Confirm Day 1 hosting environment for complaint/CAPA database, source-code repository and document control library | Buyer VP IT | June 10, 2026 |
| 4 | Deliver final list and organizational chart of the 41 dedicated employees | Seller People Operations | June 3, 2026 |
| 5 | Extend employment offers | Buyer HR | June 12, 2026 |
| 6 | Circulate benefits enrollment timeline for transferring employees | Buyer HR | June 10, 2026 |
| 7 | Prepare draft migration validation plan | Buyer Quality | June 19, 2026 |
| 8 | Schedule pre-Closing dry run of Phase 1 data extracts | Seller CIO / Buyer VP IT | June 24, 2026 |

## 8. Next Meeting

A follow-up session will be held the week of June 15, 2026, to review the revised IT service schedule and the status of employee offers.

*End of notes.*