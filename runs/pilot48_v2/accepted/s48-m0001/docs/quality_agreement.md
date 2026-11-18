# QUALITY AND SERVICE LEVEL AGREEMENT

This Quality and Service Level Agreement (this "**Quality Agreement**") is entered into as of January 15, 2026 between **Zikeiv Software, Inc.**, a Delaware corporation ("**Licensor**"), and **Stutind Solar Installations, LLC**, an Arizona limited liability company ("**Licensee**"). It is entered into under, and forms part of, the Software License Agreement between Licensor and Licensee dated January 15, 2026 (the "**Agreement**"). Capitalized terms used but not defined in this Quality Agreement have the meanings given in the Agreement.

## 1. Purpose and Scope

**1.1 Purpose.** This Quality Agreement sets out the availability, support, maintenance, disaster recovery and service credit commitments that Licensor makes for the Licensed Software under Section 4.2 of the Agreement.

**1.2 Scope.** This Quality Agreement applies to the production environment of the Licensed Software. That environment includes the HelioPlan Design, HelioPlan Proposal, HelioPlan Permit and HelioPlan Integrations modules listed in the Order Form. It also covers any module or deliverable provided under an SOW once that module or deliverable is in production use. It does not apply to sandbox, test or staging environments.

## 2. Definitions

In this Quality Agreement:

"**Available**" means that Authorized Users can log in to the Licensed Software and use its material functions, including creating and saving designs, generating proposals and generating permit packages.

"**Business Hours**" means 6:00 a.m. to 6:00 p.m. Arizona time on Business Days.

"**Downtime**" means any period during which the Licensed Software is not Available, other than Excluded Downtime.

"**Excluded Downtime**" means unavailability caused by: (a) Scheduled Maintenance; (b) Licensee's or its Authorized Users' equipment, networks or internet connectivity; (c) Licensee's use of the Licensed Software in breach of the Agreement; (d) outages of third-party utility interconnection portals or authority-having-jurisdiction permitting systems, as described in Section 4.4 of the Agreement; or (e) a force majeure event under Section 15.5 of the Agreement, subject to Licensor's obligations under Section 7 of this Quality Agreement.

"**Incident**" means any failure, error or degradation of the Licensed Software reported by Licensee or detected by Licensor.

"**Monthly Uptime Percentage**" means the total minutes in a calendar month, minus the minutes of Downtime in that month, divided by the total minutes in that month, expressed as a percentage.

"**Scheduled Maintenance**" means maintenance performed during a Maintenance Window, or at another time on at least five (5) Business Days' prior written notice to Licensee.

"**Maintenance Window**" means Sundays between 12:00 a.m. and 4:00 a.m. Arizona time.

"**Service Credit**" means a credit calculated under Section 5.

## 3. Availability Commitment

**3.1 Uptime.** Licensor shall make the Licensed Software Available with a Monthly Uptime Percentage of at least 99.5% in each calendar month of the Subscription Term.

**3.2 Scheduled Maintenance.** Licensor shall use commercially reasonable efforts to keep Scheduled Maintenance to no more than eight (8) hours per calendar month. Licensor shall not schedule maintenance outside a Maintenance Window between March 1 and October 31 of any year, except for emergency security patches.

**3.3 Monitoring.** Licensor shall monitor the availability of the Licensed Software continuously. It shall maintain a status page that shows current availability and any open Severity 1 or Severity 2 Incidents.

**3.4 Reporting.** Within ten (10) Business Days after the end of each calendar month, Licensor shall provide Licensee with a written report showing the Monthly Uptime Percentage for that month, each Downtime event and its cause, and the Incidents opened and resolved during the month by severity level.

## 4. Support

**4.1 Support Channels.** Licensor shall provide support by telephone, email and an online ticketing portal. Severity 1 Incidents may be reported by telephone at any time, 24 hours a day, 7 days a week. All other Incidents may be reported at any time and will be handled during Business Hours.

**4.2 Severity Levels.** Licensor shall assign each Incident a severity level in good faith, taking into account Licensee's reasonable assessment:

| Severity | Description |
|---|---|
| Severity 1 (Critical) | The Licensed Software is not Available, or a core module (Design, Proposal or Permit) cannot be used by all or most Authorized Users, or Licensee Data is corrupted or exposed. |
| Severity 2 (High) | A core function is materially impaired for a significant number of Authorized Users and no reasonable workaround exists. |
| Severity 3 (Medium) | A function is impaired but a reasonable workaround exists, or a non-core function is unavailable. |
| Severity 4 (Low) | Cosmetic issues, documentation errors or requests for information. |

**4.3 Response and Resolution Targets.**

| Severity | Initial Response | Status Updates | Target Resolution or Workaround |
|---|---|---|---|
| Severity 1 | 30 minutes, 24x7 | Every 2 hours | 8 hours |
| Severity 2 | 2 Business Hours | Every Business Day | 2 Business Days |
| Severity 3 | 1 Business Day | Weekly | 10 Business Days |
| Severity 4 | 2 Business Days | As needed | Next scheduled release |

**4.4 Escalation.** If a Severity 1 Incident is not resolved within its target resolution time, Licensor shall escalate it to its Vice President of Engineering. Licensor shall continue work until the Incident is resolved or a workaround is in place. If a Severity 1 Incident is not resolved within twenty-four (24) hours, the Parties' account executives shall confer by telephone at least once a day until resolution.

**4.5 Root Cause Analysis.** Within five (5) Business Days after resolving any Severity 1 Incident, Licensor shall provide Licensee with a written root cause analysis. The analysis shall describe the cause, the corrective actions taken and the measures adopted to prevent the Incident from recurring.

**4.6 Named Contacts.** Licensee may designate up to five (5) named support contacts who may open and escalate tickets on Licensee's behalf. Authorized Users may also submit tickets through the online portal.

## 5. Service Credits

**5.1 Credit Schedule.** If the Monthly Uptime Percentage in any calendar month falls below the commitment in Section 3.1, Licensee is entitled to a Service Credit equal to the following percentage of the monthly portion of the Annual Subscription Fee (being one-twelfth of the Annual Subscription Fee then in effect):

| Monthly Uptime Percentage | Service Credit |
|---|---|
| Less than 99.5% but at least 99.0% | 5% |
| Less than 99.0% but at least 98.0% | 10% |
| Less than 98.0% but at least 95.0% | 20% |
| Less than 95.0% | 30% |

**5.2 Resolution Failures.** If Licensor fails to meet the target resolution time for a Severity 1 Incident, Licensee is entitled to an additional Service Credit of 5% of the monthly portion of the Annual Subscription Fee for each full twenty-four (24) hour period after the target resolution time passes until the Incident is resolved.

**5.3 Maximum Credit.** The total Service Credits for any calendar month shall not exceed 50% of the monthly portion of the Annual Subscription Fee.

**5.4 Claiming Credits.** Licensor shall show any Service Credit due on the monthly report under Section 3.4. If Licensee believes a Service Credit is due that is not shown, Licensee may request it in writing within sixty (60) days after receiving the monthly report. Licensor shall respond in good faith within ten (10) Business Days.

**5.5 Application.** Licensor shall apply Service Credits against the next invoice for subscription Fees. If no further invoice will be issued, Licensor shall pay accrued Service Credits to Licensee within thirty (30) days after the end of the Subscription Term.

**5.6 Remedy.** As provided in Section 4.2 of the Agreement, Service Credits are Licensee's sole monetary remedy for availability failures. This is without prejudice to Licensee's termination rights under Section 10 of the Agreement and Section 6 of this Quality Agreement.

## 6. Chronic Failure

**6.1 Chronic Failure.** A "**Chronic Failure**" occurs if: (a) the Monthly Uptime Percentage falls below 99.5% in any three (3) calendar months within a rolling six (6) month period; (b) the Monthly Uptime Percentage falls below 95.0% in any single calendar month; or (c) four (4) or more Severity 1 Incidents occur within any rolling ninety (90) day period.

**6.2 Effect.** A Chronic Failure constitutes a material breach of the Agreement for purposes of Section 10.3 of the Agreement. Licensee may give notice of termination under Section 10.3 of the Agreement within ninety (90) days after the Chronic Failure occurs. The provisions of Section 10.5 of the Agreement apply to any such termination, including the refund of prepaid Fees under Section 10.5(c).

## 7. Business Continuity and Disaster Recovery

**7.1 Plan.** Licensor shall maintain a written business continuity and disaster recovery plan for the Licensed Software. It shall test the plan at least once each calendar year and give Licensee a summary of the test results on request.

**7.2 Backups.** Licensor shall back up Licensee Data at least once every twenty-four (24) hours. It shall keep the backups, encrypted, in a data center located in the United States that is geographically separate from the primary hosting facility. Backups shall be retained for at least thirty (30) days.

**7.3 Recovery Objectives.** If a disaster affects the primary hosting facility, Licensor shall restore the Licensed Software with a recovery time objective of eight (8) hours and a recovery point objective of twenty-four (24) hours.

**7.4 Force Majeure.** As provided in Section 15.5 of the Agreement, a force majeure event does not excuse Licensor's obligations under this Section 7.

## 8. Quality Management

**8.1 Release Management.** Licensor shall test each Update in a non-production environment before deploying it to production. Licensor shall give Licensee at least ten (10) Business Days' notice of any Update that materially changes the user interface or workflow of a core module, together with release notes.

**8.2 Permitting Content.** Licensor shall maintain the jurisdiction-specific permitting templates, code references and plan-set formats in HelioPlan Permit for the jurisdictions in which Licensee installs systems. Licensor shall use commercially reasonable efforts to update that content within thirty (30) days after an authority having jurisdiction publishes a change to its requirements and Licensor becomes aware of it. This Section 8.2 does not limit Section 13.4 of the Agreement.

**8.3 Defect Correction.** Licensor shall correct defects in the Licensed Software in accordance with the severity levels and targets in Section 4. Corrections shall be deployed as Updates at no additional charge.

**8.4 Security.** Licensor's information security, incident notification and audit obligations are set out in Section 9 of the Agreement and in the DPA. Any Incident involving unauthorized access to Licensee Data shall be classified as Severity 1 for purposes of this Quality Agreement.

## 9. Governance

**9.1 Quarterly Reviews.** The Parties shall hold a service review at least once each calendar quarter. The review shall cover service performance, open Incidents, upcoming Updates, the product roadmap and any requested improvements.

**9.2 Service Managers.** Each Party shall appoint a service manager to act as its primary contact for this Quality Agreement. A Party may replace its service manager by notice to the other.

**9.3 Continuous Improvement.** Licensor shall consider in good faith any reasonable request by Licensee to improve service levels or support processes. Any agreed change shall be documented under Section 10.2.

## 10. General

**10.1 Term.** This Quality Agreement remains in effect for the Subscription Term and ends automatically when the Agreement expires or is terminated.

**10.2 Amendment.** This Quality Agreement may be amended only by a written instrument signed by authorized representatives of both Parties.

**10.3 Incorporation.** This Quality Agreement is governed by the Agreement. Sections 15 and 16 of the Agreement apply to this Quality Agreement as if set out in full.

**10.4 Counterparts.** This Quality Agreement may be executed in counterparts, including by electronic signature.

---

| **ZIKEIV SOFTWARE, INC.** | **STUTIND SOLAR INSTALLATIONS, LLC** |
|---|---|
| By: ______________________________ | By: ______________________________ |
| Name: ____________________________ | Name: ____________________________ |
| Title: _____________________________ | Title: _____________________________ |
| Date: _____________________________ | Date: _____________________________ |