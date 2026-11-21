# QUALITY AGREEMENT

**TruRoute Linen Suite: Service Levels and Service Credits**

This Quality Agreement (this "**Quality Agreement**") is entered into as of March 1, 2025 by and between **Trutour Systems, LLC**, a Delaware limited liability company ("**Licensor**"), and **Vougeir Linen Services, Inc.**, a Delaware corporation ("**Licensee**"). Licensor and Licensee are each a "**Party**" and together the "**Parties**."

## Recitals

A. Licensor and Licensee have entered into a Software License Agreement dated as of March 1, 2025 (the "**License Agreement**"). Under it, Licensor licenses to Licensee the TruRoute Linen Suite, a hosted platform for RFID linen tracking and route management.

B. Licensee relies on the Licensed Software for RFID scanning at soil and clean dock, for inventory reconciliation at its Licensed Plants, and for dispatching daily delivery routes to its healthcare, hospitality and industrial customers.

C. The Parties are entering into this Quality Agreement to set the availability, performance and support standards for the Licensed Software and the credits payable when Licensor does not meet them.

The Parties therefore agree as follows:

## 1. Definitions

1.1 **Defined Terms.** Capitalized terms used but not defined in this Quality Agreement have the meanings given in the License Agreement. In this Quality Agreement:

(a) "**Availability**" means the percentage of minutes in a calendar month during which the Production Environment is accessible to Authorized Users and its Core Functions operate materially in accordance with the Documentation. It is calculated as: ((Total Minutes − Unscheduled Downtime) ÷ (Total Minutes − Scheduled Maintenance)) × 100.

(b) "**Core Functions**" means (i) receipt and processing of RFID scan events from Licensee's fixed readers and handheld scanners; (ii) linen inventory and par-level reconciliation; (iii) route planning, route sheet generation and driver dispatch; and (iv) proof-of-delivery capture through the mobile driver application.

(c) "**Incident**" means any failure of the Licensed Software to operate materially in accordance with the Documentation, and any interruption of access to the Production Environment.

(d) "**Monthly Fee**" means one-twelfth (1/12) of the Annual License Fee in effect for the month concerned.

(e) "**Production Environment**" means the hosted instance of the Licensed Software that Licensee uses in live operations at the Licensed Plants.

(f) "**Scheduled Maintenance**" means maintenance performed in accordance with Section 3.3.

(g) "**Service Credits**" means the credits against fees calculated under Section 5.

(h) "**Service Levels**" means the Availability, response, resolution and data-processing standards set out in Sections 3 and 4.

(i) "**Severity Level**" means the classification of an Incident under Section 4.2.

(j) "**Unscheduled Downtime**" means the total minutes in a calendar month during which the Production Environment is not accessible, or one or more Core Functions are unavailable at one or more Licensed Plants. Scheduled Maintenance and the exclusions in Section 3.4 are not Unscheduled Downtime.

## 2. Scope

2.1 **Application.** This Quality Agreement applies to the Licensed Software at every Licensed Plant from the date the Licensed Software is deemed live at that Licensed Plant under Section 3.2 of the License Agreement, and continues for the Term.

2.2 **Support Services.** Licensor shall provide maintenance and technical support for the Licensed Software as described in Section 4. This includes corrections, patches, workarounds and the updates and upgrades Licensor makes generally available to its customers.

## 3. Availability

3.1 **Availability Commitment.** Licensor shall make the Production Environment available with Availability of at least 99.5% in each calendar month.

3.2 **Data Processing Commitments.** Licensor shall ensure that:

(a) RFID scan events received from Licensee's readers are processed and reflected in inventory records within five (5) minutes of receipt for at least 99% of scan events in each calendar month;

(b) route sheets for the following delivery day are available for printing and mobile dispatch at each Licensed Plant by 3:00 a.m. local time on at least 99% of operating days in each calendar month; and

(c) Licensee Data is backed up at least every four (4) hours to a geographically separate location, with a recovery point objective of four (4) hours and a recovery time objective of eight (8) hours.

3.3 **Scheduled Maintenance.** Licensor may perform Scheduled Maintenance only between 11:00 p.m. Saturday and 4:00 a.m. Sunday, Eastern Time, and only after at least five (5) business days' written notice to Licensee. Scheduled Maintenance may not exceed eight (8) hours in a calendar month. Maintenance beyond that limit or outside that window is Unscheduled Downtime, unless Licensee approves it in writing in advance.

3.4 **Exclusions.** Unscheduled Downtime does not include unavailability caused by:

(a) Licensee's network, internet connectivity, RFID hardware or end-user devices, unless supplied or managed by Licensor;

(b) use of the Licensed Software by Licensee in breach of the License Agreement or contrary to the Documentation;

(c) a force majeure event under Section 17.1 of the License Agreement, except to the extent the unavailability exceeds the recovery time objective in Section 3.2(c); or

(d) suspension of access at Licensee's written request.

## 4. Support and Incident Management

4.1 **Support Channels.** Licensor shall maintain a telephone support line and a web-based ticketing portal staffed 24 hours a day, 7 days a week, for Severity 1 and Severity 2 Incidents. Severity 3 and Severity 4 Incidents may be logged at any time and will be handled between 7:00 a.m. and 7:00 p.m. Eastern Time on business days.

4.2 **Severity Levels.** Licensee shall assign the Severity Level when it reports an Incident. Licensor may propose a reclassification acting reasonably, and Licensee's classification applies until Licensee agrees to the change.

| Severity | Description |
|---|---|
| Severity 1 | The Production Environment is unavailable, or a Core Function is unavailable at any Licensed Plant, with no workaround. |
| Severity 2 | A Core Function is materially degraded at any Licensed Plant, or a Severity 1 Incident has a temporary workaround. |
| Severity 3 | A non-core function is impaired, or a Core Function is impaired in a way that does not materially disrupt operations. |
| Severity 4 | Cosmetic issues, documentation errors and requests for information. |

4.3 **Response and Resolution Times.** Licensor shall meet the following times, measured from the time Licensee reports the Incident or, if earlier, from the time Licensor's monitoring detects it:

| Severity | Initial Response | Status Updates | Resolution or Workaround |
|---|---|---|---|
| Severity 1 | 30 minutes | Every hour | 4 hours |
| Severity 2 | 1 hour | Every 4 hours | 12 hours |
| Severity 3 | 4 business hours | Daily | 5 business days |
| Severity 4 | 2 business days | Weekly | Next scheduled release |

4.4 **Root Cause Analysis.** Within five (5) business days after resolving a Severity 1 Incident, Licensor shall give Licensee a written root cause analysis. It must describe the cause, the duration and the affected Licensed Plants, and the corrective actions taken or planned to prevent recurrence.

4.5 **Account Management.** Licensor shall designate an account manager to serve as Licensee's primary contact for support escalations and service reviews.

## 5. Service Credits

5.1 **Availability Credits.** If Availability in a calendar month falls below the commitment in Section 3.1, Licensor shall issue Service Credits as follows:

| Monthly Availability | Service Credit (% of Monthly Fee) |
|---|---|
| Less than 99.5% but at least 99.0% | 5% |
| Less than 99.0% but at least 98.0% | 10% |
| Less than 98.0% but at least 96.0% | 15% |
| Less than 96.0% | 25% |

5.2 **Resolution Credits.** For each Severity 1 Incident not resolved or worked around within the time in Section 4.3, Licensor shall issue a Service Credit of 2% of the Monthly Fee for each additional four-hour period, or part of one, until resolution or workaround.

5.3 **Data Processing Credits.** For each calendar month in which Licensor fails to meet any commitment in Section 3.2(a) or 3.2(b), Licensor shall issue a Service Credit of 5% of the Monthly Fee for each commitment missed.

5.4 **Monthly Cap.** Service Credits for any calendar month shall not exceed 35% of the Monthly Fee for that month.

5.5 **Application of Credits.** Licensor shall apply Service Credits against the next invoice issued to Licensee under the License Agreement. Any Service Credits not applied when the License Agreement expires or terminates shall be paid to Licensee within thirty (30) days.

5.6 **Claiming Credits.** Licensor shall calculate Service Credits in each monthly report under Section 6.1. Licensee may dispute a calculation, or claim a credit the report omits, by written notice within sixty (60) days after receiving the report.

5.7 **Other Remedies.** Service Credits are a price adjustment reflecting the reduced value of the Licensed Software. They do not limit Licensee's rights under Section 7 of this Quality Agreement or under Section 13 of the License Agreement.

## 6. Reporting and Service Reviews

6.1 **Monthly Reports.** Within ten (10) business days after the end of each calendar month, Licensor shall give Licensee a written report. The report must show:

(a) Availability for the month;

(b) each Incident by Severity Level, with response and resolution times;

(c) performance against each commitment in Section 3.2;

(d) Scheduled Maintenance performed; and

(e) the Service Credits due.

6.2 **Monitoring Data.** On request, Licensor shall give Licensee reasonable access to the underlying monitoring logs and ticket records supporting each report.

6.3 **Quarterly Reviews.** The Parties' account representatives shall meet at least quarterly to review performance, open Incidents, planned releases and any improvement plans.

## 7. Chronic Service Failure

7.1 **Termination Right.** Licensee may terminate the License Agreement by written notice to Licensor if:

(a) Availability falls below 99.0% in any three (3) calendar months within a rolling period of six (6) calendar months;

(b) Availability falls below 95.0% in any single calendar month; or

(c) three (3) or more Severity 1 Incidents in any rolling period of ninety (90) days are not resolved or worked around within the time in Section 4.3.

7.2 **Exercise.** Licensee must exercise the right in Section 7.1 within ninety (90) days after the end of the month in which the triggering event occurs.

7.3 **Effect.** Termination under Section 7.1 has the consequences stated in Section 13.4 of the License Agreement. Licensor shall provide the transition assistance described in Section 13.5 of the License Agreement without charge.

## 8. Improvement Plans

8.1 If Licensor fails to meet any Service Level in two (2) consecutive calendar months, Licensor shall deliver a written improvement plan within fifteen (15) business days. The plan must identify the causes and set out the corrective steps and a timetable. Licensor shall implement the plan and report on its progress in each monthly report until the Service Level has been met for three (3) consecutive months.

## 9. Governing Law and Disputes

9.1 **Governing Law and Forum.** This Quality Agreement and all disputes arising out of or relating to it, including claims for Service Credits, are governed by the laws of the State of New York, without regard to its conflict-of-laws rules. Each Party submits to the exclusive jurisdiction of the state or federal courts located in New York County, New York for any action arising out of or relating to this Quality Agreement.

9.2 **Escalation.** Before commencing an action relating to Service Levels or Service Credits, a Party shall give the other written notice of the dispute. The Parties' account representatives shall meet within ten (10) business days after the notice. If they do not resolve the dispute within twenty (20) business days after the notice, either Party may refer it to a senior executive of each Party, who shall meet within a further ten (10) business days. This Section 9.2 does not prevent a Party from seeking urgent interim relief.

9.3 **Continued Performance.** During any dispute, Licensor shall continue to provide the Licensed Software and support in accordance with this Quality Agreement.

## 10. General

10.1 **Term.** This Quality Agreement takes effect on March 1, 2025 and continues for as long as the License Agreement remains in effect.

10.2 **Notices.** Notices under this Quality Agreement shall be given in the manner, and to the addresses, provided in Section 16.1 of the License Agreement.

10.3 **Amendment.** This Quality Agreement may be amended only by a written instrument signed by both Parties. Licensor may not reduce any Service Level during the Term.

10.4 **Severability.** If any provision of this Quality Agreement is held unenforceable, the remaining provisions remain in full force and effect.

10.5 **Counterparts.** This Quality Agreement may be executed in counterparts, including by electronic signature. Each counterpart is an original, and all of them together are one instrument.

---

**IN WITNESS WHEREOF**, the Parties have executed this Quality Agreement as of March 1, 2025.

| **TRUTOUR SYSTEMS, LLC** | **VOUGEIR LINEN SERVICES, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: Dana R. Whitcombe | Name: Marcel A. Vougeir |
| Title: Chief Executive Officer | Title: President |