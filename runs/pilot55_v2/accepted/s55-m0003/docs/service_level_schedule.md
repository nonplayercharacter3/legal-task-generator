# SERVICE LEVEL SCHEDULE

**Sairan Threadline Product Lifecycle Management Platform**

This Service Level Schedule (this "**Schedule**") is entered into as of January 12, 2026 between **Sairan Systems, LLC** ("**Licensor**") and **Pakairt Outdoor Apparel, Inc.** ("**Licensee**").

It is made under the Software License Agreement between the parties dated January 12, 2026 (the "**Agreement**"), and forms part of the Agreement as provided in Section 1.3 of the Agreement. Capitalized terms used but not defined in this Schedule have the meanings given in the Agreement or in Statement of Work No. 001 under the Agreement (the "**SOW**"), as applicable.

---

## 1. Scope and Definitions

**1.1 Scope.** This Schedule sets out the availability, support, maintenance and service credit commitments for the Licensed Software. It applies to the production environment from Go-Live of each Phase. It also applies to the non-production environments described in Section 2.4 of the SOW to the extent stated in Section 2.6.

**1.2 Definitions.** In this Schedule:

"**Available**" means that Authorized Users can log in to the production environment and use the material functions of each licensed module, including the integrations built under the SOW to the extent they depend on Licensor-controlled components. "**Availability**" has a corresponding meaning.

"**Business Hours**" means 7:00 a.m. to 7:00 p.m. Pacific Time, Monday to Friday, excluding U.S. federal holidays.

"**Excluded Downtime**" has the meaning given in Section 2.3.

"**Incident**" means any failure of the Licensed Software to operate in accordance with the Documentation, or any interruption to its Availability.

"**Measurement Period**" means each calendar month.

"**Monthly Fee**" means one-twelfth (1/12) of the Annual License Fee in effect for the Measurement Period concerned.

"**Monthly Availability Percentage**" means the percentage calculated under Section 2.2.

"**Resolution**" means the restoration of the affected function, either by a permanent fix or by a workaround that Licensee reasonably accepts. Where a workaround is used, Licensor shall continue to work on a permanent fix in accordance with the Software Quality Agreement.

"**Scheduled Maintenance**" has the meaning given in Section 2.4.

"**Service Credit**" means a credit calculated under Section 4.

"**Severity Level**" means the classification of an Incident as Severity 1, Severity 2, Severity 3 or Severity 4, as defined in the Software Quality Agreement.

---

## 2. Availability

**2.1 Availability Commitment.** Licensor shall ensure that the production environment of the Licensed Software is Available at least **99.7%** of the time in each Measurement Period, excluding Excluded Downtime.

**2.2 Calculation.** The Monthly Availability Percentage is calculated as follows:

> ((Total minutes in the Measurement Period − Excluded Downtime minutes) − Unavailable minutes) ÷ (Total minutes in the Measurement Period − Excluded Downtime minutes) × 100

A minute is unavailable if Licensor's monitoring, or Licensee's reasonable evidence, shows that the production environment was not Available during that minute.

**2.3 Excluded Downtime.** "**Excluded Downtime**" means any time when the production environment is not Available because of:

(a) Scheduled Maintenance carried out in accordance with Section 2.4;

(b) emergency maintenance to address a critical security vulnerability, provided that Licensor gives Licensee as much notice as is reasonably practicable and that such maintenance does not exceed four (4) hours in any Measurement Period;

(c) failure of Licensee's own systems, networks or third-party platforms that are not under Licensor's control, including Licensee's ERP, point-of-sale and e-commerce platforms;

(d) acts or omissions of Licensee or its Authorized Users in breach of the Agreement; or

(e) a force majeure event under Section 17.2 of the Agreement.

**2.4 Scheduled Maintenance.** Licensor may carry out scheduled maintenance ("**Scheduled Maintenance**") on the following terms:

(a) Scheduled Maintenance shall take place between 10:00 p.m. Saturday and 6:00 a.m. Sunday, Pacific Time, unless Licensee agrees otherwise in writing;

(b) Licensor shall give Licensee at least five (5) business days' prior written notice; and

(c) Scheduled Maintenance shall not exceed eight (8) hours in any Measurement Period.

Licensor shall not schedule maintenance during any blackout period that Licensee notifies to Licensor at least thirty (30) days in advance for seasonal line reviews, sales meetings or product launches. Licensee may notify no more than four (4) blackout periods in any twelve (12) month period, each of no more than five (5) consecutive days.

**2.5 Performance.** Licensor shall use commercially reasonable efforts to ensure that standard page loads and searches in the production environment complete within three (3) seconds for ninety-five percent (95%) of transactions in each Measurement Period, measured at Licensor's hosting boundary.

**2.6 Non-Production Environments.** Licensor shall use commercially reasonable efforts to keep the development and test and training environments Available during Business Hours. Sections 2.1, 4 and 5 do not apply to non-production environments.

---

## 3. Support and Maintenance

**3.1 Support Channels.** Licensor shall provide support through:

(a) its online support portal, available twenty-four (24) hours a day, seven (7) days a week;

(b) a telephone support line, available twenty-four (24) hours a day, seven (7) days a week for Severity 1 and Severity 2 Incidents, and during Business Hours for all other Incidents; and

(c) email to the support address Licensor notifies to Licensee from time to time.

**3.2 Authorized Contacts.** Licensee may designate up to ten (10) authorized support contacts, who will normally be Licensee's super users or IT staff. Licensor shall accept Incident reports from any authorized support contact.

**3.3 Classification.** Licensee shall assign an initial Severity Level when it reports an Incident. Licensor may propose a different Severity Level, acting reasonably. If the parties disagree, Licensee's classification applies until the Incident is escalated and resolved under Section 3.6.

**3.4 Response and Resolution Targets.** Licensor shall respond to and resolve Incidents within the following targets, measured from the time the Incident is reported through a channel in Section 3.1:

| Severity Level | Initial Response | Status Updates | Resolution Target | Support Coverage |
|---|---|---|---|---|
| Severity 1 | 30 minutes | Every 2 hours | 4 hours | 24 x 7 |
| Severity 2 | 2 hours | Every 4 hours | 1 business day | 24 x 7 |
| Severity 3 | 1 business day | Every 2 business days | 10 business days | Business Hours |
| Severity 4 | 2 business days | Weekly | Next scheduled maintenance release | Business Hours |

**3.5 Continuous Effort.** For Severity 1 and Severity 2 Incidents, Licensor shall work continuously until Resolution. Licensee shall make appropriate personnel available to assist.

**3.6 Escalation.** If an Incident is not resolved within its Resolution Target, either party may escalate it as follows:

| Level | Licensor | Licensee |
|---|---|---|
| 1 | Support Manager | IT Applications Manager |
| 2 | Vice President, Customer Success | Vice President, Product Operations |
| 3 | Chief Executive Officer | Chief Operating Officer |

Escalation under this Section 3.6 does not affect the escalation of disputes under Section 16.2 of the Agreement.

**3.7 Root Cause Analysis.** For each Severity 1 Incident, Licensor shall deliver a written root cause analysis within five (5) business days after Resolution. The analysis shall describe the cause, the remediation taken and the steps Licensor will take to prevent recurrence.

**3.8 Maintenance and Updates.** Licensor shall provide all Updates to Licensee as part of the Annual License Fee. Licensor shall test and release Updates in accordance with the Software Quality Agreement. Licensor shall support the current release of the Licensed Software and the immediately preceding major release.

**3.9 Backup and Recovery.** Licensor shall back up Customer Data in accordance with Annex 2 to the DPA. For the production environment, Licensor shall maintain:

(a) a recovery point objective of no more than four (4) hours; and

(b) a recovery time objective of no more than eight (8) hours.

---

## 4. Service Credits

**4.1 Availability Credits.** If the Monthly Availability Percentage in a Measurement Period falls below the commitment in Section 2.1, Licensor shall credit Licensee the following percentage of the Monthly Fee:

| Monthly Availability Percentage | Service Credit |
|---|---|
| Less than 99.7% but at least 99.5% | 5% |
| Less than 99.5% but at least 99.0% | 10% |
| Less than 99.0% but at least 98.0% | 20% |
| Less than 98.0% | 30% |

**4.2 Resolution Credits.** If Licensor fails to meet the Resolution Target for a Severity 1 Incident, Licensor shall credit Licensee two percent (2%) of the Monthly Fee for each full four (4) hour period beyond the Resolution Target, up to ten percent (10%) of the Monthly Fee for each Incident.

**4.3 Monthly Maximum.** The total Service Credits under Sections 4.1 and 4.2 for any Measurement Period shall not exceed thirty-five percent (35%) of the Monthly Fee.

**4.4 Reporting and Application.** Within ten (10) business days after the end of each Measurement Period, Licensor shall provide Licensee with a service level report under Section 6.1, including the calculation of any Service Credits due. Licensor shall apply Service Credits against the next invoice for the Annual License Fee. If no further invoice is due, Licensor shall pay the Service Credits to Licensee within thirty (30) days.

**4.5 Nature of Credits.** The parties agree that Service Credits are a price adjustment reflecting the reduced value of the services, and are not a penalty. Service Credits are without prejudice to Licensee's other rights and remedies under the Agreement, including the termination right in Section 5.

---

## 5. Termination for Chronic Service Level Failure

**5.1 Termination Right.** For the purposes of Section 12.4 of the Agreement, Licensee may terminate the Agreement by written notice to Licensor if any of the following occurs:

(a) the Monthly Availability Percentage falls below 99.0% in any three (3) consecutive Measurement Periods;

(b) the Monthly Availability Percentage falls below 99.7% in any four (4) Measurement Periods within any rolling twelve (12) month period; or

(c) Licensor fails to meet the Resolution Target for three (3) or more Severity 1 Incidents within any rolling six (6) month period.

**5.2 Timing of Notice.** Licensee must give notice under Section 5.1 within ninety (90) days after the end of the Measurement Period in which the relevant right first arises. The termination takes effect on the date stated in the notice, which shall be no earlier than thirty (30) days after the notice is given.

**5.3 Effect.** If Licensee terminates under this Section 5:

(a) Licensor shall refund any prepaid Annual License Fee for the period after the effective date of termination;

(b) Licensor shall provide the data export assistance described in Section 5.3 of the Agreement; and

(c) on Licensee's request, Licensor shall provide reasonable transition assistance for up to ninety (90) days at the daily rates in Section 4.5 of the SOW.

---

## 6. Reporting and Governance

**6.1 Monthly Reports.** Licensor shall provide Licensee with a monthly service level report covering:

(a) the Monthly Availability Percentage and any Excluded Downtime;

(b) the number of Incidents reported, by Severity Level, and performance against the targets in Section 3.4;

(c) performance against the target in Section 2.5;

(d) any Service Credits due; and

(e) open root cause analyses and remediation actions.

**6.2 Quarterly Reviews.** The parties shall meet each calendar quarter to review service performance, upcoming Updates and Scheduled Maintenance, and any improvement actions.

**6.3 Records.** Licensor shall retain monitoring data and Incident records for at least twenty-four (24) months. On reasonable request, Licensor shall make them available to Licensee to verify any report under Section 6.1.

---

## 7. Licensee Responsibilities

Licensee shall:

(a) report Incidents promptly through the channels in Section 3.1, with the information reasonably available to it;

(b) provide reasonable access to personnel and information that Licensor needs to diagnose and resolve Incidents; and

(c) maintain the third-party systems and network connections under its control that are needed to access the Licensed Software.

---

## 8. General

**8.1 Notices.** Notices under Section 5 must be given in accordance with Section 17.1 of the Agreement. Operational communications under Sections 2, 3, 4 and 6 may be given through the support portal or by email.

**8.2 Amendment.** Any amendment to this Schedule must be in writing and signed by both parties.

**8.3 Counterparts.** This Schedule may be signed in counterparts, including by electronic signature.

---

**IN WITNESS WHEREOF**, the parties have executed this Schedule as of the date first written above.

| **SAIRAN SYSTEMS, LLC** | **PAKAIRT OUTDOOR APPAREL, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: Daniel R. Okafor | Name: Margaret L. Tessaro |
| Title: Chief Executive Officer | Title: Chief Operating Officer |
| Date: January 12, 2026 | Date: January 12, 2026 |