# NIMBUS SERVICE LEVEL SCHEDULE

This Nimbus Service Level Schedule (this "**SLA Schedule**") is attached to the Platform License Agreement between **Drupuv Systems, Inc.** ("**Drupuv**") and **Fatesk Interactive Entertainment, LLC** ("**Fatesk**") dated as of February 1, 2027 (the "**Agreement**"). This document is the "SLA Schedule" referred to in the Agreement. Capitalized terms used but not defined in this SLA Schedule have the meanings given in the Agreement.

## 1. Scope and Definitions

1.1 **Scope.** This SLA Schedule sets out the following for the Platform as used with the Licensed Titles:

(a) the availability and performance service levels;

(b) the incident severity levels;

(c) the support channels, response times and resolution times; and

(d) the service credits that apply.

1.2 **Definitions.** In this SLA Schedule:

(a) "**Core Services**" means each of the following Platform services: (i) matchmaking; (ii) player login and authentication; (iii) cross-platform accounts; and (iv) in-game commerce and storefront services, including entitlement grants and virtual currency balances.

(b) "**Downtime**" means any period of one (1) minute or longer during which a Core Service fails to respond, or returns errors for more than five percent (5%) of requests, as measured under Section 5.3.

(c) "**Emergency Maintenance**" means maintenance that Drupuv reasonably needs to perform at short notice to address a security vulnerability or to prevent an imminent incident.

(d) "**Monthly Fee**" means one-twelfth (1/12) of the annual license fee in effect under Section 5 of the Agreement for the relevant contract year.

(e) "**Region**" means each geographic hosting region through which the Platform serves End Users. At the date of the Agreement these are North America East, North America West, Europe, Asia-Pacific and South America.

(f) "**Scheduled Maintenance**" means maintenance performed in accordance with Section 9.1.

(g) "**Service Month**" means each calendar month during the Term.

## 2. Incident Severity Levels

2.1 **Incident Severity Levels.** Each incident affecting the Platform shall be classified under one of the following severity levels:

(a) "**Severity 1 Incident**" means an incident resulting in the complete unavailability of the Platform to all End Users in all regions.

(b) "**Severity 2 Incident**" means an incident that makes one or more Core Services unavailable, or materially degraded, for some or all End Users, where the incident is not a Severity 1 Incident. This includes an outage confined to one or more Regions, or to one or more first-party platforms.

(c) "**Severity 3 Incident**" means an incident that causes a partial or non-critical loss of Platform functionality, or degraded performance, where a reasonable workaround is available and the Core Services remain usable.

(d) "**Severity 4 Incident**" means a minor defect, documentation error, cosmetic issue or request for information that has no material effect on End Users.

The severity classifications in this Section 2.1 apply for all purposes of the Agreement.

2.2 **Initial Classification.** Fatesk may assign an initial severity level when reporting an incident. When Drupuv detects an incident before Fatesk reports it, Drupuv shall assign the initial severity level and notify Fatesk of it. In each case the severity level shall be assigned in accordance with Section 2.1.

2.3 **Reclassification.** Either Party may propose that an incident be reclassified if new information shows that the incident meets the criteria for a different severity level under Section 2.1. Until the Parties' support contacts agree on any reclassification, Drupuv shall continue to work the incident at the higher of the proposed severity levels. Any disagreement shall be escalated under Section 3.3.

## 3. Support Channels and Escalation

3.1 **Support Channels.** Drupuv shall provide the support required by Section 7.1 of the Agreement through the following channels:

(a) a dedicated 24x7 telephone hotline for Severity 1 Incidents and Severity 2 Incidents;

(b) a web-based support portal, where tickets may be opened and tracked at all severity levels; and

(c) a shared real-time messaging channel between Drupuv's live operations team and Fatesk's live operations team.

3.2 **Support Contacts.** Each Party shall designate up to ten (10) named support contacts and shall keep its list of contacts current. Drupuv shall assign a named technical account manager to Fatesk.

3.3 **Escalation Path.** The escalation path is as follows:

| Level | Drupuv | Fatesk |
|---|---|---|
| 1 | On-call incident commander | Live operations lead |
| 2 | Director of Site Reliability Engineering | Head of Online Services |
| 3 | Vice President of Customer Engineering | Chief Technology Officer |

A Severity 1 Incident is escalated to Level 2 immediately. It is escalated to Level 3 if it is not resolved within four (4) hours. A Severity 2 Incident is escalated to Level 2 if no workaround is in place within four (4) hours.

## 4. Response and Resolution Times

4.1 **Response and Resolution Targets.** Drupuv shall respond to and resolve incidents within the following times:

| Severity | Response Time | Status Updates | Workaround Target | Resolution Target |
|---|---|---|---|---|
| Severity 1 | 1 hour | Every hour | 4 hours | 12 hours |
| Severity 2 | 2 hours | Every 2 hours | 8 hours | 2 days |
| Severity 3 | 8 business hours | Daily | 3 business days | 10 business days |
| Severity 4 | 2 business days | Weekly | Not applicable | Next scheduled release |

4.2 **Measurement.** Response time runs from the earlier of Drupuv's detection of the incident and Fatesk's report of it through a channel listed in Section 3.1. A response means acknowledgement by a qualified Drupuv engineer who has begun active work on the incident. For Severity 1 and Severity 2 Incidents, response, workaround and resolution times run continuously, 24 hours a day, 7 days a week. "Business hours" means 8:00 a.m. to 6:00 p.m. U.S. Eastern Time on business days.

4.3 **Severity 1 Obligations.** For each Severity 1 Incident, Drupuv shall also perform its obligations under Sections 7.2 and 7.4 of the Agreement.

4.4 **Root Cause Analysis for Severity 2 Incidents.** Within ten (10) business days after resolving a Severity 2 Incident, Drupuv shall deliver a written root cause analysis to Fatesk if Fatesk requests one.

## 5. Availability Service Level

5.1 **Availability Commitment.** Each Core Service shall be available at least 99.95% of the time in each Service Month. Availability is measured separately for each Core Service and for each Region.

5.2 **Calculation.** Availability for a Core Service in a Region is calculated as follows:

Availability % = ((Total Minutes in the Service Month − Excluded Minutes − Downtime Minutes) ÷ (Total Minutes in the Service Month − Excluded Minutes)) × 100

"Excluded Minutes" are the minutes of unavailability caused by an event listed in Section 7.5.

5.3 **Monitoring.** Drupuv shall monitor each Core Service in each Region using synthetic transactions run at intervals of no more than one (1) minute from at least three (3) independent monitoring locations. Drupuv shall give Fatesk read-only access to the monitoring dashboards in real time. Fatesk may submit its own monitoring data to support a claim of Downtime. The Parties shall reconcile any differences in good faith.

## 6. Performance Service Levels

6.1 **Performance Commitments.** In each Service Month, measured at the 95th percentile for each Region:

(a) login and authentication requests shall complete within 500 milliseconds;

(b) matchmaking shall place End Users in a match within the queue time configured for the relevant playlist, plus 30 seconds, for at least 95% of matchmaking requests;

(c) in-game purchase transactions, including entitlement grant and receipt validation, shall complete within 2 seconds; and

(d) cross-platform account linking and profile retrieval requests shall complete within 750 milliseconds.

6.2 **Capacity.** Drupuv shall maintain capacity to meet the commitments in Section 6.1 at peak concurrent use up to the Licensed Concurrency. Drupuv shall also continue to serve all End Users during any overage, in accordance with Section 2.2 of the Agreement.

## 7. Service Credits

7.1 **Availability Credits.** If any Core Service falls below the availability commitment in Section 5.1 in any Region in a Service Month, Fatesk is entitled to the following service credit for that Core Service:

| Monthly Availability | Service Credit (% of Monthly Fee) |
|---|---|
| Less than 99.95% but at least 99.9% | 5% |
| Less than 99.9% but at least 99.5% | 10% |
| Less than 99.5% but at least 99.0% | 20% |
| Less than 99.0% | 30% |

Where a Core Service falls below the commitment in more than one Region in the same Service Month, the credit is calculated on the lowest Region's availability.

7.2 **Performance Credits.** For each commitment in Section 6.1 that Drupuv fails to meet in any Region in a Service Month, Fatesk is entitled to a service credit of 3% of the Monthly Fee.

7.3 **Launch Window Credits.** If an availability shortfall under Section 7.1 occurs in a Service Month that includes a launch window designated under Section 6.3 of the Agreement, the service credit for that Core Service is doubled.

7.4 **Maximum Credits.** Total service credits in any Service Month shall not exceed 50% of the Monthly Fee.

7.5 **Exclusions.** Downtime and performance failures are excluded from the service level calculations to the extent they are caused by:

(a) Scheduled Maintenance performed in accordance with Section 9.1;

(b) the acts or omissions of Fatesk, its contractors or its Affiliates, including defects in Licensed Title code that is not Drupuv integration code delivered under the Statement of Work;

(c) the unavailability of a first-party platform holder's network, identity service or storefront, where the Platform is otherwise operating normally; or

(d) a force majeure event, to the extent it excuses performance under Section 17.5 of the Agreement.

Emergency Maintenance is not excluded.

7.6 **Application of Credits.** Drupuv shall calculate the service credits due and include them in the monthly report under Section 10.1. Service credits shall be applied or paid in accordance with Section 5.6 of the Agreement. Fatesk does not need to submit a claim to receive a service credit. Fatesk may, however, dispute any calculation within sixty (60) days after receiving the monthly report. In accordance with Section 8.3 of the Agreement, service credits do not limit Fatesk's other rights and remedies.

## 8. Launch Windows

8.1 **Elevated On-Call Staffing.** During each launch window designated under Section 6.3 of the Agreement, Drupuv shall:

(a) assign at least two (2) dedicated site reliability engineers and one (1) incident commander to the Licensed Title being launched, on call at all times;

(b) open a standing incident bridge, which Drupuv engineers shall join within fifteen (15) minutes after Fatesk's request;

(c) pre-provision capacity of at least 125% of the expected peak concurrent users that Fatesk notifies to Drupuv for the launch; and

(d) freeze all non-emergency configuration changes and deployments affecting the Licensed Titles.

8.2 **Pre-Launch Review.** At least ten (10) business days before each launch window, Drupuv shall hold a readiness review with Fatesk. The review shall cover capacity, monitoring and escalation contacts for the launch.

## 9. Maintenance

9.1 **Scheduled Maintenance.** Drupuv may perform Scheduled Maintenance for up to eight (8) hours in each Service Month, on the following conditions:

(a) Drupuv gives Fatesk at least seven (7) days' written notice;

(b) the maintenance is performed between 2:00 a.m. and 6:00 a.m. local time in the affected Region; and

(c) the maintenance does not fall within a designated launch window.

Maintenance that does not meet these conditions counts as Downtime.

9.2 **Emergency Maintenance.** Drupuv shall give Fatesk as much notice of Emergency Maintenance as is reasonably practicable. Drupuv shall keep the duration and impact of Emergency Maintenance to a minimum.

9.3 **Rolling Maintenance.** Where reasonably practicable, Drupuv shall perform maintenance Region by Region, and shall use rolling deployment techniques that avoid Downtime.

## 10. Reporting and Review

10.1 **Monthly Report.** In accordance with Section 8.2 of the Agreement, Drupuv shall deliver a report to Fatesk within ten (10) business days after the end of each Service Month. The report shall set out:

(a) availability for each Core Service in each Region;

(b) performance against each commitment in Section 6.1;

(c) all incidents by severity level, with response, workaround and resolution times;

(d) Scheduled Maintenance and Emergency Maintenance performed; and

(e) the service credits due.

10.2 **Quarterly Service Review.** The Parties shall meet each calendar quarter to review service performance, open incidents, upcoming launch windows and capacity planning.

10.3 **Records.** Drupuv shall retain the monitoring data and incident records supporting each monthly report for at least twenty-four (24) months. Drupuv shall make them available to Fatesk on reasonable request.

## Signature Page

**DRUPUV SYSTEMS, INC.**

By: ______________________________
Name:
Title:
Date:

**FATESK INTERACTIVE ENTERTAINMENT, LLC**

By: ______________________________
Name:
Title:
Date: