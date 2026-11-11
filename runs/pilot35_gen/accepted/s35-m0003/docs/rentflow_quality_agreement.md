# RENTFLOW QUALITY AGREEMENT

This RentFlow Quality Agreement (this "**Quality Agreement**") is entered into as of July 1, 2023 (the "**Effective Date**") by and between:

**Breibeith Software, Inc.**, a Delaware corporation with its principal office at 2210 Calder Ridge Parkway, Suite 400, Austin, Texas 78746 ("**Licensor**"); and

**Gliruth Event Rentals, LLC**, a Delaware limited liability company with its principal office at 845 Harrowgate Industrial Drive, Building C, Columbus, Ohio 43219 ("**Licensee**").

Licensor and Licensee are each a "**Party**" and together the "**Parties**."

## RECITALS

A. Concurrently with this Quality Agreement, the Parties are entering into a Software License Agreement dated as of the Effective Date (the "**License Agreement**"), under which Licensor licenses its RentFlow inventory, booking and dispatch platform to Licensee.

B. Section 6.2 of the License Agreement requires Licensor to provide the Software and related support in accordance with the uptime, data-accuracy and support standards set out in this Quality Agreement.

The Parties therefore agree as follows:

## 1. DEFINITIONS AND SCOPE

1.1 **Incorporated Terms.** Capitalized terms used but not defined in this Quality Agreement, including "Software," "Licensee Data," "Authorized Users," "Documentation," "License Fees" and "Term," have the meanings given to them in the License Agreement.

1.2 **Additional Definitions.** In this Quality Agreement:

"**Availability**" means the percentage of minutes in a calendar month during which the production environment of the Software is accessible to Authorized Users and its core functions (inventory lookup, booking creation and modification, and dispatch scheduling) operate materially in accordance with the Documentation, excluding Scheduled Maintenance.

"**Business Hours**" means 7:00 a.m. to 9:00 p.m. Eastern Time, Monday through Saturday, excluding U.S. federal holidays.

"**Incident**" means any failure of the Software to operate materially in accordance with the Documentation or this Quality Agreement.

"**Monthly Fee Amount**" means one-twelfth (1/12) of the Annual License Fee in effect for the relevant contract year.

"**Scheduled Maintenance**" means maintenance performed in accordance with Section 3.3.

"**Service Credit**" means a credit calculated under Section 6.

1.3 **Scope.** This Quality Agreement applies to the production environment of the Software made available to Licensee under the License Agreement. It does not apply to test or sandbox environments, or to professional services performed under a statement of work under Section 4.3 of the License Agreement, except to the extent that statement of work adopts it.

## 2. QUALITY MANAGEMENT

2.1 **Quality Program.** Licensor shall maintain a documented quality management program for the development, testing, release and operation of the Software. The program shall include version control, code review, automated regression testing before each production release, and documented rollback procedures.

2.2 **Release Management.** Licensor shall test each update and new release in a pre-production environment before deploying it to production. Licensor shall notify Licensee of any update that materially changes existing functionality in accordance with Section 6.3 of the License Agreement.

2.3 **Personnel.** Licensor shall assign a named customer success manager to Licensee's account and shall ensure that personnel supporting the Software are appropriately trained in its operation.

2.4 **Disaster Recovery.** Licensor shall maintain a disaster-recovery and business-continuity plan for the Software, test it at least once per calendar year, and provide Licensee on request with a summary of the test results. The plan shall target a recovery time objective of four (4) hours and a recovery point objective of one (1) hour.

## 3. UPTIME AND AVAILABILITY

3.1 **Availability Commitment.** Licensor shall make the Software available with Availability of at least 99.9% in each calendar month.

3.2 **Measurement.** Licensor shall measure Availability using automated monitoring from at least two geographically separate locations, at intervals of no more than one (1) minute. Licensor shall make its monthly Availability figures available to Licensee through the Software's administrative dashboard.

3.3 **Scheduled Maintenance.** Licensor may perform Scheduled Maintenance for up to eight (8) hours per calendar month. Scheduled Maintenance must (a) be performed between 11:00 p.m. and 5:00 a.m. Eastern Time, and (b) be notified to Licensee at least five (5) business days in advance. Licensor shall not schedule non-emergency maintenance on Fridays or Saturdays between April 1 and October 31, recognizing Licensee's peak event season.

3.4 **Emergency Maintenance.** Licensor may perform emergency maintenance to address a security vulnerability or prevent imminent harm to the Software, with as much notice as is reasonably practicable. Emergency maintenance counts against Availability.

## 4. DATA ACCURACY AND INTEGRITY

4.1 **Accuracy Standard.** Licensor shall ensure that the Software stores, processes, calculates and displays Licensee Data accurately and without alteration, other than alteration directed by Licensee or its Authorized Users. Without limitation, the Software shall correctly reflect inventory quantities and availability, booking dates and quantities, and delivery and dispatch assignments as entered.

4.2 **Synchronization.** Changes to inventory and booking records made through any web or mobile application of the Software shall be reflected across all applications within sixty (60) seconds under normal operating conditions.

4.3 **Backups.** Licensor shall back up Licensee Data at least hourly, retain daily backups for at least thirty (30) days, and store backups in a data center separate from the primary hosting location, in each case within the United States.

4.4 **Data Errors.** If Licensee reports, or Licensor identifies, a data error caused by the Software, Licensor shall (a) treat it as an Incident at the Severity level determined under Section 5.2; (b) restore or correct the affected Licensee Data from backups or logs; and (c) provide Licensee with a written root-cause analysis within ten (10) business days after resolution.

4.5 **Licensee Responsibilities.** Licensor is not responsible under this Section 4 for errors in Licensee Data as submitted by Licensee or its Authorized Users, consistent with Section 7.3 of the License Agreement.

## 5. SUPPORT

5.1 **Support Channels.** Licensor shall provide support by telephone and through an online ticketing portal during Business Hours, and by telephone 24 hours a day, 7 days a week, for Severity 1 Incidents.

5.2 **Severity Levels and Response Times.** Licensor shall classify each Incident reasonably and in good faith, taking into account Licensee's description of its business impact, and shall respond and resolve as follows:

| Severity | Description | Initial Response | Target Resolution or Workaround |
|---|---|---|---|
| Severity 1 | Software unavailable, or booking or dispatch functions inoperable, for all or a substantial number of Authorized Users | 30 minutes, 24/7 | 4 hours |
| Severity 2 | Material function degraded, or a data error affecting active bookings or dispatches, with no reasonable workaround | 2 Business Hours | 1 business day |
| Severity 3 | Non-critical function impaired, or a reasonable workaround exists | 1 business day | 5 business days |
| Severity 4 | Cosmetic issue, documentation question or enhancement request | 2 business days | Next scheduled release, at Licensor's discretion |

5.3 **Escalation.** If a Severity 1 or Severity 2 Incident is not resolved within its target resolution time, Licensor shall escalate it to its Vice President of Engineering and provide Licensee with status updates at least every two (2) hours (Severity 1) or every business day (Severity 2) until resolved.

5.4 **Reporting.** Within ten (10) business days after the end of each calendar quarter, Licensor shall deliver to Licensee a report summarizing Availability, Incidents by severity, response and resolution times, and Service Credits accrued in that quarter.

5.5 **Governance Meetings.** The Parties' account representatives shall meet, in person or by video conference, at least once each calendar quarter to review the report under Section 5.4 and any open quality issues.

## 6. SERVICE CREDITS

6.1 **Availability Credits.** If Availability in any calendar month falls below the commitment in Section 3.1, Licensee is entitled to a Service Credit equal to the following percentage of the Monthly Fee Amount:

| Monthly Availability | Service Credit |
|---|---|
| Less than 99.9% but at least 99.5% | 5% |
| Less than 99.5% but at least 99.0% | 10% |
| Less than 99.0% | 20% |

6.2 **Response Credits.** For each Severity 1 Incident for which Licensor misses the initial response time in Section 5.2, Licensee is entitled to an additional Service Credit of 2% of the Monthly Fee Amount.

6.3 **Maximum Credits.** Total Service Credits for any calendar month will not exceed 25% of the Monthly Fee Amount.

6.4 **Application.** Licensor shall apply accrued Service Credits against the next invoice for License Fees. Any Service Credits accrued but not applied at the end of the Term shall be paid to Licensee within thirty (30) days.

6.5 **Chronic Failure.** If Availability falls below 99.0% in any two (2) calendar months within a rolling six (6) month period, or if more than three (3) Severity 1 Incidents occur in any calendar quarter, the failure is a material breach of the License Agreement for purposes of Section 13.2 of the License Agreement.

6.6 **Remedies.** Service Credits and the remedies described in Section 6.5 are Licensee's remedies for Licensor's failure to meet the standards in this Quality Agreement, consistent with Section 8.2 of the License Agreement.

## 7. AUDITS AND CORRECTIVE ACTION

7.1 **Third-Party Assurance.** Licensor shall obtain, at least once every twelve (12) months, a SOC 2 Type II report covering the systems used to host and operate the Software, and shall provide a copy to Licensee on request, subject to Section 15 of the License Agreement.

7.2 **Quality Audit.** Once per contract year, on at least thirty (30) days' written notice, Licensee or an independent auditor bound by confidentiality obligations may review Licensor's records reasonably necessary to verify compliance with this Quality Agreement. Audits shall be conducted during normal business hours and in a manner that does not unreasonably disrupt Licensor's operations. Each Party bears its own audit costs.

7.3 **Corrective Action Plans.** If an audit, a quarterly report or a root-cause analysis shows a failure to meet this Quality Agreement, Licensor shall deliver a written corrective action plan within fifteen (15) business days and shall implement it in accordance with its terms.

## 8. TERM AND AMENDMENT

8.1 **Term.** This Quality Agreement takes effect on the Effective Date and continues for the Term of the License Agreement. It ends automatically on the expiration or termination of the License Agreement, except that Sections 6.4 and 9 survive.

8.2 **Amendment.** No amendment to this Quality Agreement is effective unless in writing and signed by both Parties.

## 9. GOVERNING LAW AND JURISDICTION

9.1 **Governing Law.** This Quality Agreement, and any dispute arising out of or relating to the performance, availability or accuracy of the Software, are governed by the laws of the State of New York, without regard to its conflict-of-laws rules.

9.2 **Jurisdiction.** Each Party submits to the exclusive jurisdiction of the state and federal courts located in New York County, New York for any action arising out of or relating to this Quality Agreement or to the performance, availability or accuracy of the Software, and waives any objection to venue in those courts.

## 10. GENERAL

10.1 **Notices.** Notices under this Quality Agreement shall be given in the manner and to the addresses set out in Section 17.1 of the License Agreement.

10.2 **Counterparts.** This Quality Agreement may be executed in counterparts, including by electronic signature, each of which is an original and all of which together are one instrument.

---

**IN WITNESS WHEREOF**, the Parties have executed this Quality Agreement as of the Effective Date.

**BREIBEITH SOFTWARE, INC.**

By: ______________________________
Name: Marcus D. Halloway
Title: Chief Revenue Officer
Date: July 1, 2023

**GLIRUTH EVENT RENTALS, LLC**

By: ______________________________
Name: Teresa V. Okonkwo-Lind
Title: Chief Executive Officer
Date: July 1, 2023