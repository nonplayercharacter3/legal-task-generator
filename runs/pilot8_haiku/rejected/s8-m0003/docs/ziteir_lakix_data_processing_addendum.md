# DATA PROCESSING ADDENDUM

This Data Processing Addendum (this "**Addendum**" or "**DPA**") is entered into as of March 1, 2024 by and between **Lakix Aerial Systems, LLC**, a Delaware limited liability company ("**Supplier**" or "**Lakix**"), and **Ziteir Agronomics, Inc.**, a Delaware corporation ("**Customer**" or "**Ziteir**"). It supplements the Master Supply Agreement between the Parties dated as of March 1, 2024 (the "**Supply Agreement**"). Supplier and Customer are each a "**Party**" and together the "**Parties**."

**RECITALS**

A. Under the Supply Agreement, Supplier sells Products to Customer and provides Platform Services that capture, store and process flight logs, field maps, spray records, sensor imagery and related information generated during Customer's operations at Customer Sites.

B. Much of that information concerns the fields, crops and operations of growers to whom Customer provides services. Customer has commitments to those growers about how their information is used.

C. The Parties wish to set out the terms on which Supplier will process Farm Data in connection with the Products and Platform Services.

The Parties therefore agree as follows:

## 1. DEFINITIONS

1.1 **Incorporated Terms.** Capitalized terms used but not defined in this Addendum have the meanings given in the Supply Agreement, including "Affiliate," "Customer Sites," "Platform Services," "Products," "Statement of Work" and "Term."

1.2 **Definitions.** In this Addendum:

(a) "**Aggregated Data**" means data derived from Farm Data that has been combined with data from other sources and de-identified so that it does not identify, and cannot reasonably be used to identify, Customer, any Grower, any Customer Site or any individual field, farm or operation.

(b) "**Applicable Data Laws**" means all laws and regulations that apply to the processing of Farm Data, including state privacy, data-security and breach-notification laws and any laws governing Personal Information.

(c) "**Farm Data**" means all data and information, in any form, that is collected, generated, uploaded, captured or derived through Customer's use of the Products or Platform Services, or that Customer or a Grower provides to Supplier. Farm Data includes field boundaries, geolocation and RTK positioning data, flight logs and telemetry, application rates, spray records and as-applied maps, chemical and product usage, prescriptions, yield and agronomic data, multispectral and thermal imagery, crop-health indices, Grower identities and contact details, and any Personal Information. Farm Data does not include Aggregated Data or Supplier's diagnostic data about Product performance that contains no Farm Data.

(d) "**Grower**" means any farmer, landowner, tenant or other person for whom Customer provides services or on whose land Customer operates Products.

(e) "**Personal Information**" means any information within Farm Data that identifies, relates to, or could reasonably be linked to an identified or identifiable individual.

(f) "**Process**" or "**Processing**" means any operation performed on Farm Data, including collection, recording, storage, retrieval, analysis, use, disclosure, transfer, combination, deletion and destruction.

(g) "**Security Incident**" means any actual or reasonably suspected unauthorized access to, or acquisition, use, disclosure, alteration, loss or destruction of, Farm Data in Supplier's or a Subprocessor's possession, custody or control.

(h) "**Subprocessor**" means any third party, including any Supplier Affiliate, that Supplier engages to Process Farm Data.

## 2. SCOPE AND ROLES

2.1 **Scope.** This Addendum applies to all Farm Data that Supplier or any Subprocessor Processes in connection with the Supply Agreement, any Statement of Work, the Products or the Platform Services.

2.2 **Roles.** Customer determines the purposes and means of Processing Farm Data. Supplier Processes Farm Data only as a service provider to Customer.

2.3 **Customer Responsibilities.** Customer is responsible for obtaining any Grower authorizations needed for Customer to provide Farm Data to Supplier for the purposes described in this Addendum.

## 3. OWNERSHIP AND USE OF FARM DATA

3.1 **Ownership.** As between the Parties, Customer owns all right, title and interest in Farm Data, subject to any rights of Growers. Supplier acquires no ownership interest in Farm Data under the Supply Agreement or this Addendum.

3.2 **License to Supplier.** Customer grants Supplier a non-exclusive, non-transferable, royalty-free license during the Term to Process Farm Data solely to (a) provide, maintain and support the Platform Services and Products for Customer; (b) prevent or address security, technical or service problems; and (c) comply with applicable law.

3.3 **Prohibited Uses.** Supplier shall not, and shall ensure that its Subprocessors do not:

(a) sell, rent or license Farm Data to any third party;

(b) use Farm Data to market products or services to any Grower, or to solicit any Grower to buy spraying, mapping or agronomic services from Supplier or any third party;

(c) use Farm Data to make commodity trading, land-valuation or input-pricing decisions, or disclose it to any third party for those purposes;

(d) combine Farm Data with data from other sources except to create Aggregated Data under Section 3.4; or

(e) attempt to re-identify any Aggregated Data.

3.4 **Aggregated Data.** Supplier may create Aggregated Data and use it to improve the Products and Platform Services. Supplier shall not publish or disclose Aggregated Data in a form that relates to fewer than ten (10) distinct Growers or that identifies any county-level region in which fewer than ten (10) Growers are represented.

## 4. PROCESSING INSTRUCTIONS

4.1 **Instructions.** Supplier shall Process Farm Data only in accordance with this Addendum, the Supply Agreement and Customer's other documented written instructions. The configuration and use of the Platform Services by Customer constitute instructions.

4.2 **Unlawful Instructions.** Supplier shall promptly notify Customer if it believes an instruction violates Applicable Data Laws. Supplier is not required to carry out that instruction until the Parties resolve the matter.

4.3 **Legal Demands.** If Supplier receives a subpoena, court order or other legal demand for Farm Data, Supplier shall, unless legally prohibited, promptly notify Customer and give Customer a reasonable opportunity to seek a protective order. Supplier shall disclose only the Farm Data it is legally required to disclose.

## 5. PERSONNEL

5.1 **Access Limited.** Supplier shall limit access to Farm Data to those employees and contractors who need it to perform Supplier's obligations.

5.2 **Confidentiality.** Supplier shall ensure that all persons authorized to Process Farm Data are bound by written confidentiality obligations at least as protective as those in this Addendum and Section 12 of the Supply Agreement.

5.3 **Training.** Supplier shall provide data-security and privacy training to personnel with access to Farm Data at least annually.

## 6. SECURITY

6.1 **Security Program.** Supplier shall maintain a written information-security program with administrative, technical and physical safeguards appropriate to the nature of Farm Data and consistent with industry standards for cloud-hosted services. The program must include at least:

(a) encryption of Farm Data in transit using TLS 1.2 or higher and at rest using AES-256 or equivalent;

(b) role-based access controls, multi-factor authentication for administrative access, and prompt removal of access for departing personnel;

(c) logical separation of Customer's Farm Data from the data of Supplier's other customers;

(d) logging and monitoring of access to systems that store Farm Data, with logs kept for at least twelve (12) months;

(e) vulnerability management, including patching of critical vulnerabilities within thirty (30) days and annual third-party penetration testing;

(f) secure configuration of Products, including authenticated and encrypted transfer of flight and spray data from Products to the Platform Services; and

(g) business-continuity and backup procedures, with daily backups of Farm Data kept in a separate location.

6.2 **Certification.** Supplier shall maintain a SOC 2 Type II report, or an equivalent independent assessment, covering the Platform Services, and shall provide the most recent report to Customer on request, subject to Section 12 of the Supply Agreement.

6.3 **Data Location.** Supplier shall store and Process Farm Data only in data centers located in the United States, unless Customer agrees otherwise in writing.

## 7. SUBPROCESSORS

7.1 **Authorization.** Customer authorizes Supplier to engage the Subprocessors listed in Annex A. Supplier shall give Customer at least thirty (30) days' written notice before engaging any new Subprocessor.

7.2 **Objection.** Customer may object to a new Subprocessor on reasonable grounds relating to data protection within fifteen (15) days after notice. The Parties shall then work in good faith to resolve the objection. If they cannot resolve it within thirty (30) days, Supplier shall not use that Subprocessor to Process Customer's Farm Data.

7.3 **Flow-Down.** Supplier shall bind each Subprocessor by written agreement to data-protection obligations at least as protective as those in this Addendum. Supplier remains responsible for each Subprocessor's performance.

## 8. SECURITY INCIDENTS

8.1 **Notice.** Supplier shall notify Customer in writing without undue delay, and in any event within forty-eight (48) hours, after becoming aware of a Security Incident.

8.2 **Content.** The notice shall describe, to the extent then known, the nature of the Security Incident, the categories and approximate volume of Farm Data and the Growers affected, the likely consequences, and the steps Supplier has taken or proposes to take. Supplier shall supplement the notice as more information becomes available.

8.3 **Response.** Supplier shall promptly investigate, contain and remediate each Security Incident and cooperate with Customer's reasonable requests in connection with it.

8.4 **Notifications and Costs.** Customer controls whether, when and how any Grower, individual or regulator is notified of a Security Incident, except where Supplier is independently required by law to give notice. Supplier shall reimburse Customer's reasonable costs of notifications, credit-monitoring services, forensic investigation and call-center support arising from a Security Incident caused by Supplier's or a Subprocessor's breach of this Addendum.

## 9. GROWER AND INDIVIDUAL REQUESTS

9.1 **Assistance.** Supplier shall provide reasonable assistance, including through Platform Services functionality, to enable Customer to respond to requests from Growers or individuals to access, correct, export or delete Farm Data.

9.2 **Direct Requests.** If Supplier receives a request directly from a Grower or individual concerning Farm Data, Supplier shall promptly forward it to Customer and shall not respond except as Customer instructs or as required by law.

## 10. AUDIT

10.1 **Information.** Supplier shall make available to Customer on request the information reasonably necessary to show compliance with this Addendum.

10.2 **Audit Rights.** Once per Contract Year, and also after any Security Incident, Customer or an independent auditor bound by confidentiality obligations may audit Supplier's compliance with this Addendum. Customer shall give at least thirty (30) days' prior written notice. Audits shall take place during normal business hours and shall not unreasonably interfere with Supplier's operations. Customer bears its own audit costs. If an audit reveals material non-compliance, Supplier shall bear the reasonable cost of the audit and shall promptly remedy the non-compliance.

## 11. EXPORT, RETURN AND DELETION

11.1 **Export During the Term.** Customer may export Farm Data at any time during the Term through the Platform Services in commonly used, machine-readable formats, including CSV, GeoJSON, shapefile and GeoTIFF.

11.2 **Export on Termination.** Upon termination or expiration of the Supply Agreement, and on Customer's written request made within sixty (60) days afterward, Supplier shall provide Customer with a complete export of Farm Data in the formats described in Section 11.1 at no additional charge. Supplier shall continue to provide read-only access to the Platform Services for that sixty (60) day period.

11.3 **Deletion.** Within thirty (30) days after the export is delivered or the sixty (60) day period ends, whichever is earlier, Supplier shall delete all Farm Data from its systems and those of its Subprocessors. Supplier shall certify the deletion in writing on request. Supplier may retain Farm Data in backup systems until overwritten in the ordinary course, not to exceed ninety (90) days, or as required by law. Any retained Farm Data remains subject to this Addendum.

## 12. GOVERNING LAW AND FORUM

12.1 **Governing Law.** This Addendum and all claims arising out of or relating to Farm Data are governed by the laws of the State of New York, without regard to its conflict-of-laws rules.

12.2 **Forum.** Any action arising out of or relating to this Addendum or to Farm Data shall be brought exclusively in the state and federal courts located in the Borough of Manhattan, New York, New York. Each Party irrevocably submits to the jurisdiction of those courts and waives any objection to venue in them.

## 13. TERM AND GENERAL

13.1 **Term.** This Addendum takes effect on the date stated above and continues for as long as Supplier or any Subprocessor Processes Farm Data.

13.2 **Survival.** Sections 3, 5, 8, 11 and 12 survive termination or expiration of the Supply Agreement for as long as Supplier or any Subprocessor holds Farm Data.

13.3 **Relationship to Supply Agreement.** This Addendum forms part of the Supply Agreement as provided in Section 13.1 of the Supply Agreement. Section 17 of the Supply Agreement applies to this Addendum, including its notice provisions.

13.4 **Amendment.** This Addendum may be amended only by a written instrument signed by authorized representatives of both Parties.

13.5 **Counterparts.** This Addendum may be executed in counterparts, including by electronic signature, each of which is an original and all of which together are one instrument.

IN WITNESS WHEREOF, the Parties have executed this Addendum as of the date first written above.

| **LAKIX AERIAL SYSTEMS, LLC** | **ZITEIR AGRONOMICS, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: | Name: |
| Title: | Title: |
| Date: | Date: |

## ANNEX A: AUTHORIZED SUBPROCESSORS

| Subprocessor | Function | Data Location |
|---|---|---|
| Lakix cloud hosting provider (U.S. regions) | Infrastructure hosting for Platform Services and backups | United States |
| Lakix Aerial Systems support Affiliate | Tier 2 technical support and troubleshooting | United States |
| Transactional email provider | System notifications and account emails | United States |

## ANNEX B: CATEGORIES OF FARM DATA

| Category | Examples |
|---|---|
| Field and location data | Field boundaries, Customer Site coordinates, RTK positioning, flight paths |
| Application data | Spray records, as-applied maps, application rates, chemical and product usage, tank-mix records |
| Sensor and imagery data | Multispectral and thermal imagery from LX-MS4-PS and LX-TH2-PS payload sensors, crop-health indices |
| Operational data | Flight logs and telemetry from LX-AX9-SD spray drones, battery and maintenance records tied to Customer Sites |
| Grower data | Grower names, farm names, contact details, service histories |
| Personal Information | Names, emails and phone numbers of Grower contacts and Customer personnel, pilot identifiers |