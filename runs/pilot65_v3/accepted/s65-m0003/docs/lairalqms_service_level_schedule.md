# LAIRALQMS SERVICE LEVEL SCHEDULE

This LairalQMS Service Level Schedule (this "**Service Level Schedule**") is entered into as of March 16, 2026 by and between **Lairal Systems, LLC**, a Delaware limited liability company with its principal place of business at 4400 Commerce Parkway, Suite 300, Cary, North Carolina 27518 ("**Licensor**"), and **Trouvar Therapeutics, Inc.**, a Delaware corporation with its principal place of business at 1201 Market Street, Suite 1800, Wilmington, Delaware 19801 ("**Licensee**").

It is entered into under the Software License Agreement between Licensor and Licensee dated March 16, 2026 (the "**License Agreement**"). Licensor and Licensee are each referred to as a "**Party**" and together as the "**Parties**."

## 1. GENERAL

1.1 **Service Level Schedule under the License Agreement.** This Service Level Schedule is the Service Level Schedule referred to in the License Agreement and is governed by the License Agreement. On execution by both Parties, it forms part of the Agreement.

1.2 **Purpose.** This Service Level Schedule sets out:

(a) the availability commitment for the Hosted Services;

(b) the maintenance windows for the Hosted Services;

(c) the support tiers, hours and response targets for the Licensed Software and the Hosted Services;

(d) the recovery point and recovery time objectives for the Hosted Services;

(e) the service credits that apply if the availability commitment is not met; and

(f) the reporting that Licensor will provide on its performance.

These matters are referred to in Sections 2.3, 7.1, 7.4, 7.5 and 7.6 of the License Agreement.

1.3 **Capitalized Terms.** Capitalized terms used but not defined in this Service Level Schedule have the meanings given to them in the License Agreement.

1.4 **Application.** This Service Level Schedule applies to each Order Form from the Subscription Start Date stated in that Order Form. It applies until the end of the Term and during any transition period under Section 14.7 of the License Agreement.

## 2. DEFINITIONS

2.1 **Definitions.** In this Service Level Schedule:

"**Availability Commitment**" has the meaning given in Section 3.1.

"**Available**" means that Authorized Users can log in to the Hosted Services and use the material functions of the Licensed Software. These functions include creating, executing, reviewing and approving electronic batch records, applying electronic signatures, and viewing and generating audit trails. Each function must perform in all material respects in accordance with the Documentation. "**Availability**" has a corresponding meaning.

"**Business Hours**" means 8:00 a.m. to 6:00 p.m. U.S. Eastern Time on Business Days.

"**Emergency Maintenance**" has the meaning given in Section 4.4.

"**Incident**" means any failure of the Licensed Software or the Hosted Services to perform in accordance with the Documentation or this Service Level Schedule, or any interruption or degradation of the Hosted Services.

"**Measurement Period**" means each calendar month. If the Subscription Start Date or the end of the Term falls during a calendar month, the Measurement Period for that month is the part of that month falling within the Term.

"**Monthly Availability Percentage**" has the meaning given in Section 3.2.

"**Monthly Subscription Amount**" means one-twelfth (1/12) of the Annual Subscription Fee under the applicable Order Form for the Subscription Year in which the relevant Measurement Period falls.

"**Priority Level**" means the priority assigned to an Incident under Section 6.1.

"**Recovery Point Objective**" or "**RPO**" means the maximum period of Licensee Data, measured back in time from the start of a Disaster, that may be lost as a result of that Disaster.

"**Recovery Time Objective**" or "**RTO**" means the maximum period between the declaration of a Disaster and the restoration of the Hosted Services to Available status.

"**Disaster**" means any event that makes the primary data center used for the Hosted Services, or a material part of its infrastructure, unable to support the Hosted Services, and that Licensor cannot reasonably expect to remedy within the Recovery Time Objective at that data center.

"**Resolution**" means that the Incident has been corrected, or that Licensor has implemented a permanent fix. "**Resolve**" has a corresponding meaning.

"**Response**" means that a qualified Licensor support engineer has acknowledged the Incident to Licensee's named support contact, has begun work on the Incident and has communicated an initial assessment. "**Respond**" has a corresponding meaning.

"**Scheduled Maintenance**" has the meaning given in Section 4.1.

"**Service Credit**" means a credit calculated under Section 8.

"**Support Portal**" means Licensor's web-based customer support portal for the Licensed Software.

"**Total Minutes**" means the total number of minutes in the applicable Measurement Period.

"**Unavailable Minutes**" means the number of minutes during the applicable Measurement Period in which the Hosted Services are not Available, excluding only the minutes excluded under Section 3.3.

"**Workaround**" means a temporary procedure or configuration that restores the affected functionality, so that the Incident no longer meets the criteria for its original Priority Level, and that Licensee's quality unit has confirmed in writing does not compromise data integrity or the validated state of the Licensed Software. Licensee will not unreasonably withhold or delay that confirmation.

## 3. AVAILABILITY

3.1 **Availability Commitment.** Licensor will make the Hosted Services Available at least 99.9% of the time in each Measurement Period, measured in accordance with Section 3.2 (the "**Availability Commitment**").

3.2 **Calculation.** The Monthly Availability Percentage for each Measurement Period is calculated as follows:

Monthly Availability Percentage = ((Total Minutes − Excluded Minutes − Unavailable Minutes) ÷ (Total Minutes − Excluded Minutes)) × 100

In this Section 3.2, "**Excluded Minutes**" means the minutes excluded under Section 3.3. The result is rounded to two decimal places.

3.3 **Exclusions.** The following minutes are excluded from the calculation of the Monthly Availability Percentage, but only to the extent the Hosted Services are not Available as a direct result:

(a) Scheduled Maintenance performed within the maintenance windows and on the notice required by Section 4;

(b) a failure of Licensee's own network connections, end-user devices, browsers, identity provider or other systems that are Licensee's responsibility under Section 5.4 of the License Agreement;

(c) any act or omission of Licensee or its Authorized Users in breach of the Agreement, or any configuration change made by Licensee administrators against Licensor's written advice;

(d) a suspension that Licensor is permitted to carry out under Section 7.7 of the License Agreement; and

(e) a Force Majeure Event under Section 17.7 of the License Agreement, other than any failure by Licensor to maintain and execute its backup and disaster-recovery arrangements.

Emergency Maintenance is not excluded from the calculation of the Monthly Availability Percentage.

3.4 **Monitoring.** Licensor will monitor the Availability of the Hosted Services continuously. It will use automated synthetic transactions run at intervals of not more than five (5) minutes from at least two (2) locations outside the hosting data centers. Each period of unavailability detected by monitoring, or reported by Licensee and confirmed by Licensor, will be recorded as Unavailable Minutes from the earlier of detection and Licensee's report, until the Hosted Services are again Available.

3.5 **Disputed Measurements.** If Licensee reasonably believes that Licensor's monitoring has not captured a period during which the Hosted Services were not Available, Licensee may notify Licensor within thirty (30) days after receiving the monthly service report for the applicable Measurement Period, with supporting evidence. The Parties will review the evidence in good faith. Any disagreement that they cannot resolve at the monthly service review will be dealt with under Section 17.3 of the License Agreement.

3.6 **Performance.** Licensor will use commercially reasonable efforts to ensure that, during each Measurement Period, at least ninety-five percent (95%) of page loads and record transactions in the Hosted Services complete within three (3) seconds, measured at the edge of Licensor's hosting network. A sustained failure to meet this target that prevents Authorized Users from executing or reviewing batch records in the ordinary course is treated as an Incident and assigned a Priority Level under Section 6.1.

## 4. MAINTENANCE

4.1 **Scheduled Maintenance.** "**Scheduled Maintenance**" means planned maintenance of the Hosted Services, including the deployment of Updates and infrastructure patches, that Licensor performs within the maintenance windows in Section 4.2 and on the notice required by Section 4.3.

4.2 **Maintenance Windows.** Scheduled Maintenance may be performed only:

(a) between 10:00 p.m. on Saturday and 4:00 a.m. on the following Sunday, U.S. Eastern Time; or

(b) at any other time that Licensee's QMS System Owner agrees in writing in advance.

Scheduled Maintenance that makes the Hosted Services unavailable may not exceed eight (8) hours in total in any Measurement Period. Any unavailability caused by maintenance beyond that limit counts as Unavailable Minutes.

4.3 **Notice.** Licensor will give Licensee at least five (5) Business Days' prior notice of each Scheduled Maintenance event affecting the production environment, in accordance with Section 7.5 of the License Agreement. Each notice will state:

(a) the planned start and end times;

(b) the nature of the maintenance;

(c) the expected impact on Availability and on Authorized Users; and

(d) any Updates to be deployed, with references to the release notes.

Major version releases remain subject to the notice and validation process in Section 3.4 of the License Agreement.

4.4 **Emergency Maintenance.** "**Emergency Maintenance**" means maintenance that cannot reasonably wait for the next maintenance window because it is needed to address a critical security vulnerability or to prevent an imminent failure of the Hosted Services. Licensor will:

(a) give Licensee as much prior notice of Emergency Maintenance as is reasonably practicable, by telephone and email to Licensee's named support contacts;

(b) limit Emergency Maintenance to the minimum scope and duration necessary; and

(c) within five (5) Business Days afterwards, provide a written summary of the reason for the Emergency Maintenance, the actions taken and any effect on Licensee Data or the validated state of the Licensed Software.

4.5 **Manufacturing Operations.** Licensor acknowledges that the Raleigh Facility operates multiple production shifts and that unavailability during batch execution may affect product quality and release. Licensor will consult Licensee's QMS System Owner before scheduling any maintenance that may affect a planned manufacturing campaign that Licensee has notified to Licensor. Licensor will reschedule that maintenance where it can reasonably do so.

## 5. SUPPORT SERVICES

5.1 **Support Tier.** Licensee's subscription under Order Form No. 1 includes Licensor's Enterprise support tier. The Enterprise support tier includes:

(a) support for Priority 1 and Priority 2 Incidents twenty-four (24) hours a day, seven (7) days a week, including U.S. federal holidays;

(b) support for Priority 3 and Priority 4 Incidents and for service requests during Business Hours;

(c) a named customer success manager, as described in Section 9.3 of Order Form No. 1;

(d) access to the Support Portal, the knowledge base and release documentation; and

(e) monthly service review meetings under Section 10.2.

5.2 **Logging Incidents.** Licensee's named support contacts may log Incidents and service requests:

(a) through the Support Portal at any time;

(b) by telephone to Licensor's support line, which Licensor will staff at all times for Priority 1 and Priority 2 Incidents; or

(c) by email to Licensor's support address for Priority 3 and Priority 4 Incidents and service requests.

Priority 1 Incidents must be reported by telephone, followed by a Support Portal entry. Licensor will make its support line telephone number and support email address available on the Support Portal and will notify Licensee in writing of any change.

5.3 **Named Support Contacts.** Licensee may designate named support contacts in accordance with Section 9.2 of Order Form No. 1. Licensor may also accept an Incident report from any Authorized User where the circumstances reasonably require it.

5.4 **Support Personnel.** Licensor will provide support through personnel who:

(a) are trained on the Licensed Software and on GxP data-integrity principles;

(b) are located in the United States; and

(c) have completed Licensor's background checks under Section 10.6 of the License Agreement.

Support personnel will access Licensee Data only as necessary to Respond to and Resolve an Incident, and only in accordance with Section 10.5 of the License Agreement.

5.5 **Language.** Support will be provided in English.

## 6. INCIDENT PRIORITY LEVELS AND RESPONSE TARGETS

6.1 **Priority Levels.** Each Incident will be assigned a Priority Level as follows:

| Priority Level | Description |
|---|---|
| Priority 1 (Critical) | The Hosted Services are not Available. A core GxP function, including batch-record execution, review by exception, electronic signature or audit-trail generation, is unusable. Or there is a confirmed or suspected loss, corruption or unauthorized alteration of Licensee Data. |
| Priority 2 (High) | A core GxP function is materially degraded, or is usable only with a significant manual procedure, so that manufacturing, quality review or batch release is materially delayed. |
| Priority 3 (Medium) | A non-core function is impaired, or a core function is impaired in a way that has a moderate effect on operations and for which a reasonable Workaround exists. |
| Priority 4 (Low) | A minor defect, cosmetic issue, documentation error or request for information, with little or no effect on operations. |

6.2 **Assignment of Priority.** Licensee will propose the Priority Level when it logs an Incident, acting reasonably and in accordance with Section 6.1. Licensor may propose a different Priority Level if it reasonably believes that the Incident has been misclassified. Licensor will not downgrade a Priority Level without the agreement of Licensee's named support contact or QMS System Owner. If the Parties cannot agree, the Incident will be handled at the Priority Level proposed by Licensee while the matter is escalated under Section 6.6.

6.3 **Response and Resolution Targets.** Licensor will Respond to and Resolve Incidents within the following targets, measured from the time the Incident is logged in accordance with Section 5.2 or is detected by Licensor's monitoring, whichever is earlier:

| Priority Level | Response Target | Workaround Target | Resolution Target | Status Updates |
|---|---|---|---|---|
| Priority 1 | 30 minutes, 24x7 | 4 hours | 24 hours | Every 60 minutes |
| Priority 2 | 1 hour, 24x7 | 8 hours | 5 days | Every 4 hours |
| Priority 3 | 4 Business Hours | 5 Business Days | Next scheduled maintenance release | Every 2 Business Days |
| Priority 4 | 1 Business Day | Not applicable | Next minor version release, at Licensor's discretion | On request |

6.4 **Effect of Workaround.** If Licensor provides a Workaround for a Priority 1 or Priority 2 Incident, the Incident will be reclassified to the Priority Level that reflects its remaining effect. The Resolution Target for the reclassified Incident is measured from the time the Workaround is provided. The reclassification does not affect the measurement of Unavailable Minutes before the Workaround was provided.

6.5 **Priority 1 Procedures.** For each Priority 1 Incident, Licensor will:

(a) assign a named incident manager and keep that person engaged continuously until the Incident is resolved or reclassified;

(b) open a conference bridge for Licensee's representatives;

(c) where the Incident involves possible loss, corruption or alteration of Licensee Data, notify Licensee's Vice President, Quality in addition to the named support contacts, and treat the Incident as a Security Incident under Section 10.8 of the License Agreement where it meets that definition; and

(d) within five (5) Business Days after Resolution, deliver a written root cause analysis. The analysis will cover the timeline, root cause, effect on Licensee Data and audit trails, corrective and preventive actions, and the Unavailable Minutes recorded.

6.6 **Escalation.** If Licensor does not meet a Response, Workaround or Resolution target, or if Licensee reasonably considers that an Incident is not receiving appropriate attention, Licensee may escalate the Incident through the escalation contacts in Section 9.4 of Order Form No. 1. For Priority 1 Incidents, escalation to Level 2 is automatic if no Workaround has been provided within two (2) hours. Escalation to Level 3 is automatic if no Workaround has been provided within four (4) hours.

6.7 **Licensee Cooperation.** Licensee will provide reasonable information and assistance to help Licensor diagnose and Resolve Incidents. This includes making appropriate personnel available and providing descriptions, screenshots and logs within its control. Time spent waiting for information that Licensor has reasonably requested from Licensee is not counted against the Workaround and Resolution targets. Time spent waiting for that information is still counted as Unavailable Minutes where the Hosted Services are not Available.

6.8 **Changes to Validated Configuration.** Any correction, patch or Workaround that changes the configuration of the Licensed Software will be implemented through Licensee's change-control procedures and the quality agreement under Section 8.3 of the License Agreement. For a Priority 1 Incident, emergency change-control may be applied. Licensor will provide the documentation reasonably required for Licensee's change-control records.

## 7. BACKUP, RECOVERY AND DISASTER RECOVERY OBJECTIVES

7.1 **Backups.** Licensor will perform backups of the Hosted Services in accordance with Section 7.1 of the License Agreement. Licensor will monitor each backup job and will investigate and re-run any failed backup job within four (4) hours after the failure.

7.2 **Recovery Point Objective.** The Recovery Point Objective for the Hosted Services is four (4) hours.

7.3 **Recovery Time Objective.** The Recovery Time Objective for the Hosted Services is eight (8) hours.

7.4 **Declaration of Disaster.** Licensor will declare a Disaster, and invoke its disaster-recovery plan, as soon as it reasonably determines that a Disaster has occurred. In any event, it will do so no later than two (2) hours after the start of any unplanned unavailability of the Hosted Services that it cannot reasonably expect to remedy within the Recovery Time Objective at the primary data center. Licensor will notify Licensee by telephone and email immediately on declaring a Disaster.

7.5 **Restoration of Individual Records.** At Licensee's request, Licensor will restore Licensee Data from backup to correct an accidental deletion or corruption that is not caused by a Disaster. Licensor will do so within one (1) Business Day after the request for a Priority 1 matter, and within three (3) Business Days for any other matter. Restoration under this Section 7.5 is provided at no additional charge for up to four (4) requests in each Subscription Year, and after that at Licensor's then-current professional services rates. Restoration following any loss or corruption caused by Licensor's breach is subject to Section 12.4 of the License Agreement and is provided at no charge.

7.6 **Integrity Verification.** After any restoration of Licensee Data, Licensor will provide Licensee with a written confirmation identifying:

(a) the backup used and its timestamp;

(b) the scope of data restored; and

(c) the results of the integrity checks performed, including checks of audit-trail continuity and electronic signature linkage.

7.7 **Disaster-Recovery Testing.** Licensor will test its disaster-recovery plan for the Hosted Services at least annually, in accordance with Section 7.1(e) of the License Agreement. Each test summary will state whether the Recovery Point Objective and Recovery Time Objective were achieved. Licensor will give Licensee at least thirty (30) days' notice of each test, and Licensee's quality representatives may observe the test. Any failure to achieve either objective in a test will be handled through Licensor's corrective and preventive action process and reported to Licensee in writing.

## 8. SERVICE CREDITS

8.1 **Entitlement.** If the Monthly Availability Percentage for any Measurement Period is below the Availability Commitment, Licensee will be entitled to a Service Credit, calculated as a percentage of the Monthly Subscription Amount, in accordance with Section 7.6 of the License Agreement:

| Monthly Availability Percentage | Service Credit |
|---|---|
| Less than 99.9% but at least 99.5% | 5% of the Monthly Subscription Amount |
| Less than 99.5% but at least 99.0% | 10% of the Monthly Subscription Amount |
| Less than 99.0% but at least 98.0% | 20% of the Monthly Subscription Amount |
| Less than 98.0% | 30% of the Monthly Subscription Amount |

8.2 **Recovery Time Credit.** If, following a declared Disaster, Licensor fails to restore the Hosted Services to Available status within the Recovery Time Objective, Licensee will be entitled to an additional Service Credit of ten percent (10%) of the Monthly Subscription Amount for the Measurement Period in which the Disaster was declared. This additional Service Credit is payable in addition to any Service Credit under Section 8.1.

8.3 **Response Credit.** If Licensor fails to meet the Response Target or the Workaround Target for a Priority 1 Incident, Licensee will be entitled to an additional Service Credit of two percent (2%) of the Monthly Subscription Amount for each such failure. The Service Credits under this Section 8.3 may not exceed ten percent (10%) of the Monthly Subscription Amount in any Measurement Period.

8.4 **Maximum Monthly Credit.** The total Service Credits for any Measurement Period under Sections 8.1 to 8.3 will not exceed fifty percent (50%) of the Monthly Subscription Amount.

8.5 **Application of Credits.** Licensor will calculate the Service Credits due for each Measurement Period and show them in the monthly service report under Section 10.1. Licensee is not required to make a claim for Service Credits that are shown in a monthly service report. Licensee may claim Service Credits that are not shown in a report by notice under Section 3.5. Licensor will apply all Service Credits against the next invoice for the Annual Subscription Fee. If no further invoice will be issued under the applicable Order Form, Licensor will pay the amount of the Service Credits to Licensee within thirty (30) days after the end of the Term or the transition period, whichever is later.

8.6 **Other Remedies.** Service Credits are a price adjustment reflecting the reduced value of the Hosted Services. They are without prejudice to Licensee's other rights and remedies under the Agreement, as provided in Section 7.6 of the License Agreement. These include Licensee's termination rights under Section 14.3 of the License Agreement.

## 9. CHRONIC FAILURE

9.1 **Chronic Availability Failure.** For the purposes of Section 14.3 of the License Agreement, Licensor fails to meet the availability commitment in the Service Level Schedule in a month if the Monthly Availability Percentage for that Measurement Period is below the Availability Commitment.

9.2 **Remediation Plan.** If the Monthly Availability Percentage is below the Availability Commitment in any two (2) Measurement Periods during any rolling period of six (6) months, Licensor will deliver a written remediation plan to Licensee within ten (10) Business Days after the end of the second Measurement Period. The plan will identify the root causes and the actions Licensor will take, with dates. Licensor will report on its implementation at each monthly service review until the actions are complete. The delivery of a remediation plan does not limit Licensee's rights under Section 14.3 of the License Agreement.

9.3 **Repeated Priority 1 Incidents.** If three (3) or more Priority 1 Incidents with the same or a related root cause occur in any rolling period of three (3) months, the Parties' executive sponsors under Section 6.5 of Order Form No. 1 will meet within ten (10) Business Days to review the root cause and Licensor's corrective and preventive actions.

## 10. REPORTING AND SERVICE REVIEWS

10.1 **Monthly Service Report.** Within ten (10) Business Days after the end of each Measurement Period, Licensor will deliver to Licensee's business contact and quality contact a written service report. The report will state:

(a) the Monthly Availability Percentage, with a list of each period of unavailability, its duration, its cause and any minutes excluded under Section 3.3 together with the basis for the exclusion;

(b) all Scheduled Maintenance and Emergency Maintenance performed;

(c) the number of Incidents opened, resolved and outstanding, by Priority Level, with performance against each Response, Workaround and Resolution target;

(d) the results of backup monitoring, including any failed backup jobs and their re-run status;

(e) any Security Incidents, by reference to the notices given under Section 10.8 of the License Agreement;

(f) the Service Credits due for the Measurement Period; and

(g) upcoming Updates and planned maintenance for the following three (3) months.

10.2 **Monthly Service Review.** The customer success manager will hold a service review meeting with Licensee's business contact each month, in accordance with Section 9.3 of Order Form No. 1, to discuss the monthly service report, open Incidents, remediation actions and planned changes. Licensee's QMS System Owner and quality representatives may attend.

10.3 **Annual Review.** At least once in each Subscription Year, the Parties will review this Service Level Schedule. The review will consider Licensor's performance, changes in Licensee's operations and any changes in Licensor's standard service levels. Any change to this Service Level Schedule is effective only if made in accordance with Section 17.9 of the License Agreement. Licensor will not reduce any commitment in this Service Level Schedule during the Term.

10.4 **Records.** Licensor will retain its monitoring data, Incident records and backup logs for the Hosted Services for at least the Term and two (2) years afterwards. It will make them available to Licensee on reasonable request, including in connection with a supplier audit under Section 8.4 of the License Agreement or a Regulatory Authority inspection under Section 8.5 of the License Agreement.

## 11. SERVICE REQUESTS

11.1 **Standard Service Requests.** The Enterprise support tier includes the following service requests at no additional charge, subject to the targets below:

| Service Request | Target Completion |
|---|---|
| Creation, modification or deactivation of Administrator User accounts | 1 Business Day |
| Password reset for Administrator Users where self-service is unavailable | 4 Business Hours |
| Provision of audit-trail extracts or system logs for a defined period | 3 Business Days |
| Provision of current infrastructure qualification records under Section 7.3 of the License Agreement | 5 Business Days |
| Provision of the current SOC 2 Type II report and bridge letter under Section 10.7 of the License Agreement | 5 Business Days |
| Configuration of single sign-on settings under Section 7.3 of Order Form No. 1 | 5 Business Days |

11.2 **Inspection Support Requests.** If Licensee notifies Licensor that a Regulatory Authority inspection is in progress or has been announced, Licensor will treat related requests for records, audit-trail extracts and system documentation as Priority 2 matters for the duration of the inspection. Licensor will make a knowledgeable representative available on the same day for questions relating to the Hosted Services.

11.3 **Other Requests.** Requests outside the scope of Section 11.1 or Section 11.2 that are not Incidents may be dealt with as Professional Services under a Statement of Work or a change order.

## 12. GENERAL

12.1 **Relationship to the License Agreement.** This Service Level Schedule supplements Sections 7 and 13.2 of the License Agreement. Licensor's obligations under this Service Level Schedule are in addition to its obligations under those Sections.

12.2 **Contacts.** Operational communications under this Service Level Schedule may be given to the contacts listed in Section 10 of Order Form No. 1 and to Licensee's named support contacts. Formal notices must be given in accordance with Section 17.6 of the License Agreement.

12.3 **Amendment.** This Service Level Schedule may be amended only in accordance with Section 17.9 of the License Agreement.

12.4 **Counterparts and Electronic Signatures.** This Service Level Schedule may be executed in counterparts and by electronic signature in accordance with Section 17.19 of the License Agreement.

*[Signature page follows.]*

---

IN WITNESS WHEREOF, the Parties have caused this LairalQMS Service Level Schedule to be executed by their duly authorized representatives as of March 16, 2026.

**LAIRAL SYSTEMS, LLC**

By: ______________________________
Name: Dana R. Whitcombe
Title: Chief Executive Officer
Date: March 16, 2026

**TROUVAR THERAPEUTICS, INC.**

By: ______________________________
Name: Marisol Okafor-Lindqvist
Title: Chief Operating Officer
Date: March 16, 2026