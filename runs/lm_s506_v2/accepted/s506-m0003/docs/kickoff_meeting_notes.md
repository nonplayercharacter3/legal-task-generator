# KICKOFF MEETING NOTES

**Project:** Protoux CellTrace Platform – Implementation at the Licensed Site (Statement of Work No. 1)
**Date:** March 12, 2026
**Time:** 9:30 a.m. – 12:15 p.m. (Eastern Time)
**Location:** Glenox Circular Materials, Inc., 400 Lee Road, Rochester, New York 14606 (Training Room B), with remote participants by video conference
**Prepared by:** Protoux project management office
**Status:** Final, circulated to attendees on March 13, 2026

## 1. Attendees

**Glenox Circular Materials, Inc. ("Glenox")**
- Dana Whitcombe, Director of Operations, Rochester (Glenox project manager)
- Marcus Feld, IT Infrastructure Manager
- Priya Ramaswamy, Quality and Process Engineering Lead
- Tom Okafor, Environmental, Health and Safety Manager
- Leah Brandt, Corporate Counsel (first 45 minutes only)

**Protoux Analytics, Inc. ("Protoux")**
- Jordan Ellery, Implementation Project Manager (Protoux project manager)
- Sofia Marchetti, Solution Architect
- Ben Hartigan, Integration Engineer (remote)
- Carla Nguyen, Customer Success Manager (remote)

## 2. Purpose of Meeting

2.1 The meeting was the project kickoff meeting under Phase 1 (Section 2.1(a)) of Statement of Work No. 1 dated as of March 2, 2026 (the "SOW"), issued under the Software License Agreement dated as of March 2, 2026 (the "Agreement").

2.2 The objectives were to confirm the project team and governance, walk through scope and the target schedule, agree the discovery workshop plan, and record open actions.

## 3. Project Team and Governance

3.1 **Project managers.** The parties confirmed Dana Whitcombe as Glenox's project manager and Jordan Ellery as Protoux's project manager, as required by Section 9.1 of the SOW.

3.2 **Status reporting.** Protoux will issue written status reports every two weeks under Section 9.2 of the SOW, starting March 27, 2026. Reports will go to both project managers and the steering committee members.

3.3 **Steering committee.** The steering committee under Section 9.3 of the SOW will be Glenox's Vice President, Operations and Protoux's Vice President, Customer Delivery. The first meeting is proposed for the week of April 13, 2026, and monthly after that.

3.4 **Weekly working session.** The project managers agreed to a standing weekly working session on Tuesdays at 2:00 p.m. (Eastern Time) during the implementation.

## 4. Scope Review

4.1 Sofia Marchetti walked through the four licensed modules in Order Form No. 1: Chain-of-Custody, Feedstock Intake, Process Analytics and Recovery Reporting. The team confirmed that the implementation covers the Rochester hydrometallurgical recovery facility only, consistent with Section 1.2 of the SOW.

4.2 The team confirmed the integrations listed in Section 2.4 of the SOW: (a) one-way process historian feed; (b) two-way ERP interface for supplier master data and shipment records; and (c) single sign-on through Glenox's identity provider.

4.3 Priya Ramaswamy asked whether historical intake records could be loaded. Protoux noted that migration of records created before January 1, 2025 is out of scope under Section 1.4(c) of the SOW. Glenox will confirm by March 27, 2026 whether it wants a change order impact assessment for any earlier records. Records from January 1, 2025 onward will be addressed in the Design Document.

4.4 The team noted the Order Form limits of 75 named Authorized Users and 12 edge connector instances. Marcus Feld's preliminary count is 58 users at go-live and 9 edge connector instances, leaving room for growth.

## 5. Target Schedule

5.1 Jordan Ellery presented the target schedule from Section 4.1 of the SOW, measured from the SOW Effective Date:

| Milestone | Target Completion | Indicative Date |
|---|---|---|
| M1 – Kickoff held and Design Document approved | Week 6 | April 13, 2026 |
| M2 – Platform configuration and edge connector deployment complete | Week 14 | June 8, 2026 |
| M3 – Integrations complete and system testing passed | Week 20 | July 20, 2026 |
| M4 – User acceptance testing completed | Week 24 | August 17, 2026 |
| M5 – Go-live | Week 26 | August 31, 2026 |
| M6 – Hypercare completed | Week 30 | September 28, 2026 |

5.2 Glenox flagged a planned maintenance shutdown of the solvent extraction circuit in late June 2026. Protoux will plan process historian validation around it. No change to the target schedule is needed at this stage.

## 6. Discovery Workshops

6.1 The parties agreed the following workshops for the weeks of March 16 and March 23, 2026:

| Workshop | Glenox Participants | Format |
|---|---|---|
| Battery intake, weighing and labelling | Operations, EHS | On site |
| Chain-of-custody through discharge, dismantling and black-mass production | Operations, Quality | On site |
| Process telemetry and historian tags | Process Engineering, IT | Hybrid |
| ERP and supplier master data | IT, Procurement | Remote |
| User roles, access and single sign-on | IT | Remote |
| Reporting and recovery-yield dashboards | Quality, Operations | Hybrid |

6.2 Protoux will issue a draft Design Document by April 3, 2026 for Glenox review under Section 5.4 of the SOW (10 business days).

## 7. Site Access and Safety

7.1 Tom Okafor confirmed that Protoux personnel attending on site must complete Glenox's site safety induction before entering process areas. Personal protective equipment will be issued at reception. Protoux will send names of on-site attendees at least two business days before each visit.

7.2 Protoux confirmed its personnel will follow Glenox's site safety and visitor rules, consistent with Section 6(c) and Section 9.4 of the SOW.

## 8. Data Handling

8.1 Leah Brandt reminded the team that drop-off customer, driver and employee details captured in intake and custody records should be limited to what is reasonably necessary, in line with Section 3.3 of the Data Processing Addendum. The Design Document will identify which personal data fields are captured at each intake step.

8.2 Protoux confirmed that sample and test data will be loaded only into its United States-hosted environments, as required by Section 10.2 of the SOW. No Customer Data will be copied to personal devices or removable media.

8.3 Glenox will nominate a privacy contact for Security Incident notices under Section 12.4 of the Data Processing Addendum.

## 9. Fees and Invoicing

9.1 Carla Nguyen confirmed that the first Implementation Fee invoice ($41,250) will be issued on approval of the Design Document at milestone M1, in accordance with Section 7.2 of the SOW. Travel expenses will be invoiced monthly in arrears against the $18,000 cap in Section 7.3 of the SOW.

## 10. Action Items

| No. | Action | Owner | Due |
|---|---|---|---|
| 1 | Circulate workshop invitations and agendas | J. Ellery (Protoux) | March 13, 2026 |
| 2 | Provide process historian tag list and network diagram for edge connector locations | M. Feld (Glenox) | March 20, 2026 |
| 3 | Provide sample intake tickets and custody forms (redacted) | P. Ramaswamy (Glenox) | March 20, 2026 |
| 4 | Send site safety induction materials to Protoux | T. Okafor (Glenox) | March 16, 2026 |
| 5 | Confirm ERP vendor contact and test environment access | M. Feld (Glenox) | March 27, 2026 |
| 6 | Confirm approach to pre-2025 historical records | D. Whitcombe (Glenox) | March 27, 2026 |
| 7 | Nominate Glenox privacy contact | L. Brandt (Glenox) | March 20, 2026 |
| 8 | Issue draft Design Document | S. Marchetti (Protoux) | April 3, 2026 |
| 9 | Issue first bi-weekly status report | J. Ellery (Protoux) | March 27, 2026 |

## 11. Next Meeting

11.1 First weekly working session: Tuesday, March 17, 2026, 2:00 p.m. (Eastern Time), by video conference.

*These notes record the discussion for project management purposes. They do not amend the Agreement, the Order Form, the Data Processing Addendum or the SOW. Any change to scope, schedule or fees will be handled through the change control procedure in Section 8 of the SOW.*