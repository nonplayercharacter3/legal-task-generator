# EXHIBIT A: SERVICE LEVEL SCHEDULE

**LiftSense Remote-Monitoring and Predictive-Maintenance Platform**

This Service Level Schedule (this "**Schedule**") is attached to and forms part of the Software License Agreement effective as of March 3, 2025 (the "**Agreement**") between **Velert Systems, LLC** ("**Licensor**") and **Rekaind Vertical Services, Inc.** ("**Licensee**"). It applies to every Order Form executed under the Agreement unless an Order Form expressly provides otherwise. Capitalized terms used but not defined in this Schedule have the meanings given in the Agreement.

## 1. DEFINITIONS

1.1 "**Business Day**" means any day other than a Saturday, a Sunday or a day on which national banks in Philadelphia, Pennsylvania or Columbus, Ohio are authorized or required to close.

1.2 "**Chronic Availability Failure**" has the meaning given in Section 4.1.

1.3 "**Core Functions**" means the following functions of the Platform:
(a) receipt and processing of Equipment Data from Connected Devices;
(b) generation and delivery of entrapment, passenger-alarm, out-of-service and safety-related fault alerts to Licensee's designated dispatch contacts;
(c) the web and mobile dispatch and work-order applications used by Licensee's dispatchers and technicians; and
(d) the application programming interfaces that Licensee uses to exchange data with its own systems, as described in the Documentation.

1.4 "**Downtime**" means any period during which one or more Core Functions are unavailable or materially impaired for Licensee, measured in minutes, other than Excluded Downtime. A Core Function is "materially impaired" where either of the following applies:
(a) alerts are delayed by more than five (5) minutes beyond the delivery time stated in the Documentation; or
(b) Authorized Users are unable to create, assign, update or close work orders.

1.5 "**Excluded Downtime**" has the meaning given in Section 2.4.

1.6 "**Incident**" means any failure, defect, error or interruption of the Platform or a Connected Device, or any failure of the Platform to perform materially in accordance with the Documentation.

1.7 "**Measurement Period**" means each calendar month during a Subscription Term. If a Subscription Term begins or ends during a calendar month, that partial month is a Measurement Period of its own.

1.8 "**Monthly Fee**" means, for an Order Form and a Measurement Period, one-twelfth (1/12) of the annual subscription fee payable under that Order Form for the annual billing period in which the Measurement Period falls.

1.9 "**Platform Availability**" means, for any Measurement Period, the percentage calculated under Section 2.2.

1.10 "**Resolution**" means that the Incident has been corrected, or that Licensor has implemented a workaround that restores the affected functionality with no material loss of performance. Licensee must have confirmed the workaround as acceptable, and that confirmation shall not be unreasonably withheld. "**Resolve**" has a corresponding meaning.

1.11 "**Response**" means that a qualified Licensor support engineer has acknowledged the Incident to Licensee's reporting contact by telephone or through the support portal and has begun active work on diagnosis.

1.12 "**Scheduled Maintenance**" has the meaning given in Section 5.1.

1.13 "**Service Credit**" means the credit calculated under Section 3.

1.14 "**Severity Level**" means the classification of an Incident under Section 6.1.

1.15 "**Support Hours**" means 7:00 a.m. to 8:00 p.m. Eastern Time on each Business Day.

## 2. PLATFORM AVAILABILITY

2.1 **Availability Commitment.** Licensor shall make the Core Functions available to Licensee and its Authorized Users with a Platform Availability of at least 99.5% in each Measurement Period.

2.2 **Calculation.** Platform Availability for a Measurement Period is calculated as follows:

> Platform Availability (%) = ((Total Minutes − Downtime) ÷ Total Minutes) × 100

In this formula:
- "Total Minutes" means the total number of minutes in the Measurement Period, less the minutes of Excluded Downtime in that Measurement Period; and
- "Downtime" is measured from the earlier of (i) the time Licensor's monitoring systems detect the Downtime and (ii) the time Licensee reports it to Licensor's help desk, until the time the affected Core Function is restored.

Platform Availability is calculated to two decimal places.

2.3 **Partial Unavailability.** Some Downtime affects only part of Licensee's portfolio, such as where alerts fail for Licensed Units connected through a particular gateway firmware version, cellular carrier or regional data ingestion node. In that case, the Downtime counts in proportion to the number of Licensed Units affected compared with the total number of Licensed Units under the applicable Order Form. Downtime affecting twenty-five percent (25%) or more of the Licensed Units counts in full.

2.4 **Excluded Downtime.** The following are Excluded Downtime and do not count as Downtime:
(a) Scheduled Maintenance carried out in accordance with Section 5;
(b) unavailability caused by Licensee's breach of the Agreement, or by Licensee's misuse of the Platform contrary to the Documentation;
(c) unavailability caused by hardware, software, networks or connectivity supplied by Licensee or by a building owner. This exclusion does not cover Connected Devices, or connectivity that Licensor supplies under an Order Form;
(d) unavailability of an individual Licensed Unit caused by loss of building power, or by physical damage to a Connected Device not caused by Licensor;
(e) suspension of the Platform by Licensor in accordance with Section 7.5 of the Agreement; and
(f) unavailability caused by a Force Majeure Event, but only to the extent the unavailability could not have been prevented by the business continuity and disaster recovery measures described in Section 8 of this Schedule and in the Documentation.

Downtime of the alert-delivery Core Function described in Section 1.3(b) is not Excluded Downtime under Section 2.4(a). The only exception is Scheduled Maintenance during which Licensor maintains alert delivery through the failover path described in Section 5.3.

2.5 **Monitoring.** Licensor shall monitor the availability and performance of the Core Functions continuously, using automated monitoring tools that check each Core Function at intervals of not more than one (1) minute. Licensor shall retain monitoring logs for not less than twenty-four (24) months. Licensor shall make those logs available to Licensee on reasonable request to verify Platform Availability calculations and Service Credits, as contemplated by Section 7.7 of the Agreement.

2.6 **Status Page.** Licensor shall maintain a status page, accessible to Authorized Users, that shows the current operating status of each Core Function. Licensor shall update the status page within fifteen (15) minutes after detecting any Downtime.

## 3. SERVICE CREDITS

3.1 **Service Credit Schedule.** If Platform Availability under an Order Form falls below 99.5% in any Measurement Period, Licensee is entitled to a Service Credit equal to the following percentage of the Monthly Fee for that Order Form:

| Platform Availability in the Measurement Period | Service Credit (% of Monthly Fee) |
|---|---|
| Less than 99.5% but at least 99.0% | 5% |
| Less than 99.0% but at least 98.0% | 10% |
| Less than 98.0% but at least 97.0% | 20% |
| Less than 97.0% | 30% |

3.2 **Alert Delivery Credit.** In addition to any Service Credit under Section 3.1, Licensee is entitled to a Service Credit of two percent (2%) of the Monthly Fee for each separate occasion in a Measurement Period on which the alert-delivery Core Function described in Section 1.3(b) suffers Downtime of more than thirty (30) consecutive minutes affecting five percent (5%) or more of the Licensed Units.

3.3 **Maximum Credits.** The total Service Credits for any single Measurement Period under an Order Form shall not exceed forty percent (40%) of the Monthly Fee for that Order Form.

3.4 **Application.** Licensor shall calculate Service Credits and show them in the Service Report for the applicable Measurement Period. Service Credits are applied in accordance with Section 5.3 of the Agreement. Licensee need not make a separate claim for a Service Credit shown in a Service Report. If Licensee believes that a Service Report understates the Service Credits due, Licensee may notify Licensor within sixty (60) days after delivery of that Service Report. The Parties shall then resolve the matter under Section 9.

3.5 **Nature of Service Credits.** The Parties agree that Service Credits are a price adjustment that reflects the reduced value of the Platform. Service Credits are not a penalty.

## 4. CHRONIC AVAILABILITY FAILURE

4.1 **Definition.** A "**Chronic Availability Failure**" occurs under an Order Form where there is Platform Availability below 99.5% in three consecutive calendar months, each as calculated under Section 2.2 and reported, or required to be reported, in the Service Report for the applicable Measurement Period.

4.2 **Termination Right.** Upon a Chronic Availability Failure, Licensee may terminate the affected Order Form under Section 12.6 of the Agreement. To do so, Licensee must deliver written notice of termination to Licensor, in accordance with Section 15.5 of the Agreement, within thirty (30) days after delivery of the Service Report for the third consecutive calendar month in which Platform Availability was below 99.5%. The notice must identify the Order Form being terminated and the Measurement Periods on which Licensee relies.

4.3 **Effective Date of Termination.** A termination under Section 4.2 takes effect on the date stated in Licensee's notice. That date may not be earlier than the date the notice is delivered or later than ninety (90) days after that date. If the notice does not state a date, the termination takes effect thirty (30) days after the notice is delivered.

4.4 **Consequences.** On a termination under Section 4.2:
(a) Licensor shall refund prepaid Fees and waive early termination charges as provided in Section 12.6 of the Agreement;
(b) Licensor shall pay or credit all Service Credits accrued through the effective date of termination; and
(c) Licensee may request transition assistance under Section 12.8 of the Agreement.

4.5 **Remediation Plan.** If Platform Availability falls below 99.5% in two consecutive Measurement Periods under an Order Form, Licensor shall deliver a written remediation plan to Licensee within ten (10) Business Days after delivery of the second Service Report. The plan must identify the root causes of the Downtime, the corrective actions Licensor will take and the target dates for completing them. Senior technical representatives of each Party shall meet within five (5) Business Days after delivery of the remediation plan to review it. The delivery of a remediation plan, and Licensee's participation in its review, do not affect Licensee's rights under Section 3 or this Section 4.

## 5. SCHEDULED MAINTENANCE

5.1 **Scheduled Maintenance.** "**Scheduled Maintenance**" means planned maintenance of the Platform that meets all of the following conditions:
(a) it is carried out between 12:00 a.m. and 4:00 a.m. Eastern Time on a Sunday, or at another time agreed in writing by Licensee's operational contact;
(b) Licensor has given Licensee at least five (5) Business Days' advance notice by email to Licensee's operational contacts and on the status page; and
(c) it does not exceed eight (8) hours in total in any Measurement Period.

Maintenance that does not meet each of these conditions is not Scheduled Maintenance. Any unavailability caused by it counts as Downtime.

5.2 **Emergency Maintenance.** Licensor may carry out emergency maintenance without advance notice where necessary to address a critical security vulnerability or to prevent imminent Downtime. Licensor shall give Licensee notice as soon as reasonably practicable. Unavailability caused by emergency maintenance counts as Downtime.

5.3 **Alert Failover.** During any Scheduled Maintenance or emergency maintenance, Licensor shall maintain delivery of entrapment, passenger-alarm and safety-related fault alerts to Licensee's designated dispatch contacts through Licensor's secondary alert-routing path, as described in the Documentation. This path uses SMS and automated voice call to the dispatch contacts. Licensor shall test the secondary alert-routing path at least once in each calendar quarter and report the results in the next Service Report.

5.4 **Updates.** Licensor shall give Licensee at least thirty (30) days' advance notice of any major release that changes the user interface of the dispatch or work-order applications. Licensor shall also make release notes and training materials available before that release is deployed to production.

## 6. INCIDENT MANAGEMENT AND SUPPORT

6.1 **Severity Levels.** Licensor shall assign a Severity Level to each Incident as follows, acting reasonably and taking account of Licensee's assessment:

| Severity Level | Description |
|---|---|
| **Severity 1 (Critical)** | Any Core Function is unavailable for all or a substantial part of the Licensed Units, or any defect prevents or delays the generation or delivery of entrapment, passenger-alarm or safety-related fault alerts for any Licensed Unit. |
| **Severity 2 (High)** | A Core Function is materially impaired, or a non-core function is unavailable, with a significant effect on Licensee's dispatch or maintenance operations, and no acceptable workaround exists. |
| **Severity 3 (Medium)** | A function of the Platform is impaired, but a workaround is available or the effect on Licensee's operations is limited. |
| **Severity 4 (Low)** | A cosmetic defect, a documentation error, a general question, or a request for an enhancement. |

Any Incident within Section 5.7 of the Agreement is a Severity 1 Incident.

6.2 **Response and Resolution Times.** Licensor shall meet the following targets for each Incident, measured from the earlier of Licensee's report and Licensor's detection of the Incident:

| Severity Level | Support Coverage | Response Time | Resolution Target |
|---|---|---|---|
| Severity 1 | 24 hours a day, 7 days a week | 15 minutes | 4 hours |
| Severity 2 | 24 hours a day, 7 days a week | 1 hour | 12 hours |
| Severity 3 | Support Hours | 4 Support Hours | 5 Business Days |
| Severity 4 | Support Hours | 1 Business Day | Next scheduled release, or as agreed |

6.3 **Severity 1 Procedures.** For each Severity 1 Incident, Licensor shall:
(a) assign an incident manager who remains the single point of contact for Licensee until Resolution;
(b) provide status updates to Licensee's operational contacts at least every thirty (30) minutes until Resolution;
(c) where the Incident affects alert delivery, notify Licensee's dispatch center by telephone within fifteen (15) minutes after detection, so that Licensee can arrange manual monitoring of the affected units; and
(d) deliver a written root-cause analysis within five (5) Business Days after Resolution, identifying the cause of the Incident and the steps taken to prevent recurrence.

6.4 **Escalation.** If Licensor does not Resolve a Severity 1 Incident within its Resolution target, or a Severity 2 Incident within twice its Resolution target, Licensee may escalate the Incident to the following Licensor contacts, in order:
(a) Licensor's Director of Customer Support;
(b) Licensor's Vice President of Engineering; and
(c) Licensor's Chief Technology Officer.

Licensor shall keep current contact details for each escalation contact in the support portal.

6.5 **Reporting Channels.** Licensee may report Incidents:
- by telephone to Licensor's help desk, at any time for Severity 1 and Severity 2 Incidents;
- through the support portal; or
- by email to Licensor's designated support address.

Severity 1 and Severity 2 Incidents should be reported by telephone. Licensor shall maintain a dedicated telephone line for Licensee's dispatch center.

6.6 **Licensee Cooperation.** Licensee shall provide Licensor with reasonably available information about each Incident it reports. This includes the affected Licensed Units, the symptoms observed and any relevant error messages. Licensee shall also give reasonable access to its personnel for diagnosis. Where Licensor's ability to Resolve an Incident is delayed because Licensee has not provided reasonably requested information or access, the period of that delay does not count toward the Resolution target.

6.7 **Connected Device Replacement.** Where an Incident is caused by a defective Connected Device, Licensor shall ship a replacement device by overnight courier within one (1) Business Day after diagnosis. Licensor's warranty obligations under Section 4.3 of the Agreement apply to that replacement.

## 7. SERVICE REPORTS

7.1 **Delivery.** Licensor shall deliver a Service Report to Licensee for each Measurement Period within the first five (5) Business Days of the following calendar month. Licensor shall deliver each Service Report by email to Licensee's operational contacts designated in the applicable Order Form and shall post it in the support portal.

7.2 **Contents.** Each Service Report shall include, for each Order Form:
(a) Platform Availability for the Measurement Period, both overall and for each Core Function;
(b) the date, time, duration, affected Core Functions and affected Licensed Units for each period of Downtime;
(c) each period of Excluded Downtime claimed, with the basis for the exclusion;
(d) the number of Incidents opened and Resolved at each Severity Level, and Licensor's performance against the Response and Resolution targets in Section 6.2;
(e) the number of alerts generated and delivered, and the median and ninety-fifth (95th) percentile alert-delivery times;
(f) any Service Credits due under Section 3;
(g) the results of any test of the secondary alert-routing path under Section 5.3; and
(h) the status of any open root-cause analyses and remediation plans.

7.3 **Review Meetings.** The Parties' operational contacts shall meet, by video conference or in person, within ten (10) Business Days after delivery of each Service Report to review it. They shall also meet quarterly at a senior level to review overall service performance, the Platform roadmap and any proposed changes to this Schedule.

7.4 **Accuracy.** Licensor shall prepare each Service Report accurately and in good faith from its monitoring logs and support records. Licensee's acceptance of a Service Report, or its failure to object to one, does not waive any of Licensee's rights under the Agreement, except as provided in Section 3.4.

## 8. BUSINESS CONTINUITY AND DISASTER RECOVERY

8.1 **Redundancy.** Licensor shall host the Platform in at least two (2) geographically separate data center regions in the United States. Licensor shall configure the Platform so that the alert-delivery Core Function fails over automatically to the secondary region if the primary region becomes unavailable.

8.2 **Recovery Objectives.** In the event of a disaster affecting the primary hosting region, Licensor shall meet the following objectives:
(a) for the alert-delivery Core Function, a recovery time objective of thirty (30) minutes and a recovery point objective of five (5) minutes; and
(b) for all other Core Functions, a recovery time objective of four (4) hours and a recovery point objective of one (1) hour.

8.3 **Backups.** Licensor shall back up Customer Data at least daily. Licensor shall retain backups for at least thirty (30) days and store them encrypted in a region separate from the primary hosting region.

8.4 **Testing.** Licensor shall test its business continuity and disaster recovery plan at least once in each calendar year. Licensor shall provide Licensee with a written summary of the test results, including any deficiencies identified and the steps taken to correct them, within thirty (30) days after each test.

## 9. DISPUTES CONCERNING SERVICE LEVELS

9.1 **Good-Faith Review.** If Licensee disputes any Platform Availability calculation, Excluded Downtime claim, Severity Level classification or Service Credit, the Parties' operational contacts shall first meet within ten (10) Business Days to review the relevant monitoring logs and support records.

9.2 **Escalation.** If the operational contacts do not resolve the dispute within ten (10) Business Days after their first meeting, either Party may refer it to Licensee's Chief Operating Officer and Licensor's Vice President of Engineering. Those individuals shall meet within ten (10) Business Days after the referral.

9.3 **Other Remedies.** This Section 9 does not prevent either Party from exercising any right or remedy under the Agreement while a dispute is under review. It also does not prevent either Party from seeking relief in accordance with Section 15.2 of the Agreement.

## 10. CHANGES TO THIS SCHEDULE

10.1 **Amendment.** This Schedule may be amended only in accordance with Section 15.9 of the Agreement.

10.2 **No Reduction.** Licensor shall not reduce the service levels, Response or Resolution targets, Service Credits or recovery objectives in this Schedule for any Order Form during its Subscription Term, except by an amendment signed by both Parties.

10.3 **Annual Review.** At the quarterly senior review meeting held nearest to each anniversary of the Order Effective Date of an Order Form, the Parties shall consider in good faith whether any service level should be adjusted to reflect changes in the Platform, Licensee's portfolio of Licensed Units or industry practice. No adjustment takes effect unless it is made by an amendment under Section 10.1.

---

**Acknowledged and agreed** as part of the Software License Agreement effective as of March 3, 2025.

| **VELERT SYSTEMS, LLC** | **REKAIND VERTICAL SERVICES, INC.** |
|---|---|
| By: /s/ Daniel P. Arrowood | By: /s/ Marisol T. Quenneville |
| Name: Daniel P. Arrowood | Name: Marisol T. Quenneville |
| Title: Chief Executive Officer | Title: President and Chief Executive Officer |
| Date: March 3, 2025 | Date: March 3, 2025 |