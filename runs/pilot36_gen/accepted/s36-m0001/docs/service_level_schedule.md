# SERVICE LEVEL SCHEDULE

**to the Distribution Agreement dated March 1, 2025**

**between LASEISK AUTO REMARKETING, LLC ("Supplier") and KONAIS DEALER NETWORKS, INC. ("Distributor")**

## 1. INTRODUCTION AND DEFINITIONS

1.1 **Purpose.** This Service Level Schedule is the Service Level Schedule referred to in the Distribution Agreement between Supplier and Distributor dated March 1, 2025 (the "**Agreement**"). It sets out the service levels that Supplier shall meet for Platform uptime and condition-report turnaround under Sections 4.1(b) and 11.2 of the Agreement.

1.2 **Defined Terms.** Capitalised terms used but not defined in this Schedule have the meanings given in the Agreement. In this Schedule:

(a) "**Availability**" means the percentage of Scheduled Minutes in a calendar month during which the Platform is Available, calculated under Section 2.3.

(b) "**Available**" means that Dealers holding active Dealer Subscriptions can log in to the Platform, view auction run lists, place bids in simulcast sales and online events, and receive confirmation of accepted bids.

(c) "**Condition Report**" means Supplier's standard written and photographic inspection report for a vehicle consigned to a Supplier physical auction or online event. The report covers exterior and interior condition, mechanical observations, tyre and brake readings, odometer reading and announcements.

(d) "**Excluded Downtime**" has the meaning given in Section 2.4.

(e) "**Scheduled Minutes**" means the total minutes in a calendar month, less Excluded Downtime.

(f) "**Service Credit**" means a credit against Wholesale Prices calculated under Section 4.

(g) "**Severity 1 Incident**" means an incident that makes the Platform unavailable to all or substantially all Dealers, or prevents bidding in a live simulcast sale or online event.

(h) "**Severity 2 Incident**" means an incident that materially degrades a core Platform function for a significant number of Dealers but does not amount to a Severity 1 Incident.

## 2. PLATFORM UPTIME

2.1 **Uptime Commitment.** Supplier shall ensure that the Platform achieves Availability of at least 99.5% per calendar month.

2.2 **Monitoring.** Supplier shall monitor Availability using automated synthetic transactions run at intervals of no more than five minutes from at least two geographically separate locations. The Platform is treated as not Available for any interval in which two consecutive monitoring checks fail.

2.3 **Calculation.** Availability is calculated as follows:

> Availability (%) = ((Scheduled Minutes − minutes during which the Platform is not Available) ÷ Scheduled Minutes) × 100

2.4 **Excluded Downtime.** The following do not count as minutes during which the Platform is not Available ("**Excluded Downtime**"):

(a) scheduled maintenance carried out between 11:00 p.m. and 5:00 a.m. Eastern Time on any day other than a scheduled auction sale day, provided Supplier gives Distributor at least 72 hours' prior notice through the distributor portal;

(b) emergency maintenance needed to address a security vulnerability, provided Supplier gives as much notice as is reasonably practicable and keeps it to the minimum duration necessary;

(c) unavailability caused by an event of force majeure under Section 15 of the Agreement;

(d) unavailability caused by the acts or omissions of Distributor, a Dealer, or their equipment, software or internet connectivity; and

(e) suspension of a Dealer's access by Supplier under Section 4.2 of the Agreement.

2.5 **Scheduled Maintenance Limit.** Scheduled maintenance under Section 2.4(a) shall not exceed eight hours in any calendar month.

## 3. CONDITION-REPORT TURNAROUND

3.1 **Turnaround Commitment.** For each vehicle checked in at a Supplier physical auction location, Supplier shall publish a completed Condition Report on the Platform within the following periods:

| Consignment Type | Turnaround Target |
|---|---|
| Vehicle checked in by 2:00 p.m. local time at least two business days before its scheduled sale | Published no later than 6:00 p.m. local time on the business day before the sale |
| Vehicle checked in later than the cut-off above | Published no later than two hours before the vehicle's scheduled run time |
| Online-only event listing with inspection by Supplier | Published within one business day after inspection |

3.2 **Performance Standard.** Supplier shall meet the applicable turnaround target for at least 95% of Condition Reports published in each calendar month.

3.3 **Exclusions.** Section 3.1 does not apply to vehicles (a) that the consignor delivers without keys, title documents or an operable battery; (b) that the consignor requests to sell "as-is" without inspection; or (c) whose inspection is delayed by an event of force majeure under Section 15 of the Agreement.

## 4. SERVICE CREDITS

4.1 **Uptime Service Credits.** If Availability in a calendar month falls below the commitment in Section 2.1, Distributor is entitled to a Service Credit equal to the following percentage of the Wholesale Prices invoiced for Dealer Subscriptions activated in that month:

| Monthly Availability | Service Credit |
|---|---|
| Less than 99.5% but at least 99.0% | 3% |
| Less than 99.0% but at least 98.0% | 7% |
| Less than 98.0% | 12% |

4.2 **Condition-Report Service Credits.** If Supplier fails to meet the performance standard in Section 3.2 in a calendar month, Distributor is entitled to a Service Credit equal to 2% of the Wholesale Prices invoiced for Dealer Subscriptions activated in that month.

4.3 **Cap.** Total Service Credits for any calendar month shall not exceed 15% of the Wholesale Prices invoiced for Dealer Subscriptions activated in that month.

4.4 **Claims.** To receive a Service Credit, Distributor shall submit a written claim within 30 days after the end of the calendar month to which it relates. Supplier shall review and respond to each claim within 15 days after receipt. Supplier shall apply approved Service Credits against the next invoice issued under Section 6.3 of the Agreement. Any credits outstanding at expiry or termination of the Agreement shall be paid to Distributor within 30 days.

4.5 **Remedy.** In line with Section 11.2 of the Agreement, Service Credits are Distributor's remedy for Supplier's failure to meet the service levels in this Schedule. This Section 4.5 does not limit either Party's rights under Section 14.2 of the Agreement.

## 5. INCIDENT MANAGEMENT AND SUPPORT

5.1 **Support Desk.** Supplier shall maintain a distributor support desk, reachable by telephone and email, from 7:00 a.m. to 9:00 p.m. Eastern Time on business days and during all scheduled auction sale hours. Supplier shall also provide an on-call escalation contact at all times for Severity 1 Incidents.

5.2 **Response and Restoration Targets.**

| Severity | Initial Response | Status Updates | Target Restoration |
|---|---|---|---|
| Severity 1 | 30 minutes | Every 60 minutes | 4 hours |
| Severity 2 | 2 hours | Every 4 hours | 1 business day |
| Other | 1 business day | As reasonably requested | Next scheduled release |

5.3 **Root Cause Analysis.** For each Severity 1 Incident, Supplier shall deliver a written root cause analysis and remediation plan to Distributor within 10 business days after restoration.

## 6. REPORTING AND REVIEW

6.1 **Monthly Report.** Within 10 business days after the end of each calendar month, Supplier shall make a service level report available to Distributor through the distributor portal. The report shall show Availability, Excluded Downtime, Condition Report turnaround performance, Severity 1 and Severity 2 Incidents, and any Service Credits accrued.

6.2 **Quarterly Review.** Senior operational representatives of the Parties shall meet, in person or by video conference, at least once each calendar quarter. At each meeting they shall review service level performance, open incidents and planned Platform changes notified under Section 4.1(d) of the Agreement.

6.3 **Records.** Supplier shall retain monitoring data and Condition Report time stamps for at least 24 months. On reasonable request, Supplier shall make relevant extracts available to Distributor to verify a Service Credit claim.

## 7. GENERAL

7.1 **Changes.** This Schedule may be amended only in accordance with Section 17.4 of the Agreement.

7.2 **Incorporation.** This Schedule forms part of the arrangement between the Parties under the Agreement. Sections 15 (Force Majeure), 17.1 (Governing Law) and 17.6 (Notices) of the Agreement apply to it.

**AGREED** by the Parties as of March 1, 2025.

**LASEISK AUTO REMARKETING, LLC**

By: ______________________________
Name:
Title:

**KONAIS DEALER NETWORKS, INC.**

By: ______________________________
Name:
Title: