# SCHEDULE B: SERVICE LEVEL SCHEDULE

**BrewOps Platform: Breneth Systems, Inc. and Gaimun Brewing Company, LLC**

This Service Level Schedule is Schedule B to the Software License and Subscription Agreement dated November 2, 2026 (the "**Agreement**") between Breneth Systems, Inc. ("**Breneth**") and Gaimun Brewing Company, LLC ("**Customer**"). Capitalized terms used but not defined in this Schedule have the meanings given in the Agreement.

---

## 1. DEFINITIONS

1.1 In this Schedule:

(a) "**Availability**" means the percentage of minutes in a calendar month during which the Platform is Available, calculated in accordance with Section 2.2.

(b) "**Available**" means that Authorized Users can log in to the Platform and use the core functions of the batch and recipe tracking, TTB excise reporting, inventory management and distributor ordering modules in material conformity with the Documentation.

(c) "**Business Hours**" means 7:00 a.m. to 7:00 p.m. Eastern Time, Monday through Friday, excluding U.S. federal holidays.

(d) "**Downtime**" means any period, measured in minutes, during which the Platform is not Available, excluding Excluded Downtime.

(e) "**Excluded Downtime**" has the meaning given in Section 2.3.

(f) "**Incident**" means any failure of the Platform to perform materially in accordance with the Documentation, including any Downtime.

(g) "**Monthly Fee**" means one-twelfth (1/12) of the annual Subscription Fees payable under the Order Form for the subscription year in which the relevant month falls.

(h) "**Scheduled Maintenance**" means maintenance of the Platform carried out in accordance with Section 3.

(i) "**Service**" means the Platform and the support services Breneth provides under the Agreement and this Schedule.

(j) "**Service Credit**" means a credit against Fees calculated in accordance with Section 5.

---

## 2. AVAILABILITY

2.1 **Availability Commitment.** Breneth shall make the Platform Available at least 99.5% availability per calendar month (the "**Availability Commitment**").

2.2 **Calculation.** Availability for a calendar month is calculated as follows:

> Availability (%) = ((Total minutes in the month − Downtime minutes) ÷ Total minutes in the month) × 100

Downtime begins at the earlier of (a) the time Breneth's monitoring systems detect that the Platform is not Available and (b) the time Customer reports the Downtime to Breneth through a channel set out in Section 4.2. Downtime ends when the Platform is restored to Available status.

2.3 **Excluded Downtime.** The following do not count as Downtime ("**Excluded Downtime**"):

(a) Scheduled Maintenance performed in accordance with Section 3;

(b) unavailability caused by Customer's or its Authorized Users' equipment, networks, internet connectivity or third-party systems not provided by Breneth or its subcontractors;

(c) unavailability caused by Customer's use of the Platform in breach of the Agreement or contrary to the Documentation;

(d) suspension of access in accordance with Section 4.4 of the Agreement; and

(e) events of force majeure described in Section 15.2 of the Agreement.

2.4 **Monitoring and Reporting.** Breneth shall monitor Availability continuously. Within ten (10) Business Days after the end of each calendar month, Breneth shall make a report available to Customer through the Platform administration console showing Availability for that month, each Downtime event, and the cause and duration of each event.

---

## 3. SCHEDULED MAINTENANCE

3.1 **Maintenance Windows.** Breneth shall perform Scheduled Maintenance between 11:00 p.m. Saturday and 5:00 a.m. Sunday Eastern Time, or at another time outside Business Hours notified in accordance with Section 3.2.

3.2 **Notice.** Breneth shall give Customer at least five (5) days' notice by email of any Scheduled Maintenance expected to make the Platform unavailable for more than thirty (30) minutes.

3.3 **Limit.** Scheduled Maintenance shall not exceed eight (8) hours in any calendar month. Any maintenance in excess of that limit, or performed without the notice required by Section 3.2, counts as Downtime.

3.4 **Regulatory Deadlines.** Breneth shall use commercially reasonable efforts to avoid scheduling maintenance during the last three (3) Business Days before any recurring TTB excise return filing deadline that applies to Customer and that Customer has notified to Breneth in writing.

---

## 4. SUPPORT

4.1 **Support Hours.** Breneth shall provide technical support during Business Hours. For Severity 1 Incidents, Breneth shall provide support twenty-four (24) hours a day, seven (7) days a week.

4.2 **Reporting Channels.** Customer may report Incidents through the BrewOps support portal, by email to Breneth's designated support address, or, for Severity 1 Incidents, by telephone to Breneth's designated support line.

4.3 **Severity Levels and Response Times.** Breneth shall classify each Incident reasonably and in good faith, taking account of Customer's description of the business impact, and shall respond within the following times:

| **Severity** | **Description** | **Initial Response** | **Target Resolution or Workaround** |
|---|---|---|---|
| Severity 1 (Critical) | Platform not Available, or a core module (including TTB excise reporting) unusable, with no workaround | 1 hour, 24/7 | 8 hours |
| Severity 2 (High) | Material degradation of a core module, with a workaround available or a limited number of Authorized Users affected | 4 Business Hours | 2 Business Days |
| Severity 3 (Medium) | Non-critical function impaired; core operations unaffected | 1 Business Day | 10 Business Days |
| Severity 4 (Low) | General question, documentation issue or enhancement request | 2 Business Days | Next scheduled release, as Breneth determines |

4.4 **Escalation.** If a Severity 1 or Severity 2 Incident is not resolved within its target resolution time, Breneth shall escalate it to its support manager and provide Customer with status updates at least every four (4) hours for Severity 1 Incidents and every Business Day for Severity 2 Incidents until resolution.

4.5 **Root Cause Analysis.** Within five (5) Business Days after resolving any Severity 1 Incident, Breneth shall provide Customer with a written summary of the root cause and the corrective actions taken or planned.

---

## 5. SERVICE CREDITS

5.1 **Entitlement.** If Availability in any calendar month falls below the Availability Commitment, Customer is entitled to a Service Credit calculated as a percentage of the Monthly Fee for that month:

| **Monthly Availability** | **Service Credit (% of Monthly Fee)** |
|---|---|
| Less than 99.5% but at least 99.0% | 2% |
| Less than 99.0% but at least 98.0% | 5% |
| Less than 98.0% | 10% |

5.2 **Claiming Service Credits.** To receive a Service Credit, Customer must submit a written request to Breneth within thirty (30) days after the end of the month in which the shortfall occurred, identifying the dates and approximate times of the Downtime. Breneth shall confirm the Service Credit within fifteen (15) Business Days. Breneth shall apply confirmed Service Credits against the next invoice for Subscription Fees. If no further invoice is due because the Subscription Term has expired or terminated, Breneth shall pay the amount of any confirmed and unapplied Service Credit to Customer within thirty (30) days.

5.3 **Maximum Service Credit.** The total Service Credits for any calendar month shall not exceed 10% of the Monthly Fee for that month.

5.4 **Remedy.** Service Credits are Customer's sole and exclusive remedy, and Breneth's sole liability, for any Service failure, including any failure to meet the Availability Commitment or the response times in Section 4.3, and including loss or corruption of Customer Data arising from or in connection with any Service failure.

5.5 **No Cash Value.** Except as provided in Section 5.2, Service Credits have no cash value and may not be transferred or exchanged.

---

## 6. CHRONIC FAILURE

6.1 **Chronic Failure Review.** If Availability falls below 98.0% in any two (2) consecutive calendar months, or in any three (3) calendar months within a rolling twelve (12) month period, the Parties' designated representatives shall meet within ten (10) Business Days at Customer's request. At the meeting Breneth shall present a written remediation plan. Breneth shall implement the agreed remediation plan.

---

## 7. CUSTOMER RESPONSIBILITIES

7.1 Customer shall:

(a) report Incidents promptly through the channels in Section 4.2 and give reasonable detail of the symptoms and business impact;

(b) designate up to three (3) Authorized Users as primary support contacts and keep their contact details current; and

(c) provide reasonable cooperation, information and remote access needed for Breneth to diagnose and resolve Incidents.

---

## 8. REVIEW

8.1 **Service Reviews.** At either Party's request, and not more than once per calendar quarter, the Parties shall hold a service review covering Availability, Incident trends, open Severity 1 and Severity 2 Incidents and planned Platform updates.

8.2 **Changes.** This Schedule may be amended only in accordance with Section 15.4 of the Agreement.

---

| **BRENETH SYSTEMS, INC.** | **GAIMUN BREWING COMPANY, LLC** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: | Name: |
| Title: | Title: |
| Date: | Date: |