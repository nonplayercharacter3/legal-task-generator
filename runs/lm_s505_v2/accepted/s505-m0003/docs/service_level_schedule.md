# SERVICE LEVEL SCHEDULE

This Service Level Schedule (this "**Service Level Schedule**") is entered into as of January 15, 2025 (the "**SLS Effective Date**") by and between **Lebun Interactive, Inc.**, a Delaware corporation ("**Customer**"), and **Draibouth Studios LLC**, a Delaware limited liability company ("**Provider**"). Customer and Provider are each a "**Party**" and together the "**Parties**."

## RECITALS

A. Customer and Provider are parties to a Master Services Agreement dated as of January 15, 2025 (the "**Agreement**"). Under the Agreement, Provider performs game quality assurance testing, localization and live-operations support services for Customer under Order Forms.

B. Section 7 of the Agreement requires Provider to meet the service levels, issue the service credits and provide the performance reports set out in this Service Level Schedule. Section 3.5 of the Agreement requires Provider to give Customer scheduling and staffing priority consistent with the capacity commitments in this Service Level Schedule.

The Parties therefore agree as follows:

## 1. SCOPE AND INTERPRETATION

1.1 **Application.** This Service Level Schedule applies to all Services performed under every Order Form, unless an Order Form expressly states different service levels for particular Services.

1.2 **Relationship to the Agreement.** This Service Level Schedule forms part of the Agreement. Capitalized terms used but not defined in this Service Level Schedule have the meanings given to them in the Agreement or the Quality Agreement.

1.3 **Days and Times.** Unless this Service Level Schedule states "business days," references to days are to calendar days. "Business Hours" means 9:00 a.m. to 6:00 p.m. Pacific Time on business days. All times are measured in Pacific Time.

## 2. DEFINITIONS

2.1 **Defined Terms.** In this Service Level Schedule:

"**Measurement Period**" means each calendar month during the term of an Order Form.

"**Monthly Fees**" means, for a Measurement Period and an Order Form, the total Fees invoiced or invoiceable under that Order Form for Services performed in that Measurement Period. For milestone Fees, it means the milestone Fee divided by the number of Measurement Periods between the start of work on that milestone and its Milestone date.

"**Player Ticket**" means a player inquiry or complaint received through a ticketing, email or chat channel for which Provider provides player support under an Order Form.

"**Service Credit**" means the amount calculated under Section 7.

"**Service Level**" means each performance standard in Sections 3, 4 and 5.

"**Service Level Failure**" means Provider's failure to meet a Service Level in a Measurement Period.

## 3. QUALITY ASSURANCE TESTING SERVICE LEVELS

3.1 **Defect Reporting Response Times.** Provider shall enter each Defect report in the bug database designated under Section 3.2 of the Quality Agreement, in the form required by Section 3.3 of the Quality Agreement, within the following times after the tester first reproduces the Defect:

| **Severity Level** | **Reporting Time** | **Customer Notification** |
|---|---|---|
| Severity 1 – Critical | 2 hours | Immediate email and phone notice to Customer's quality contact |
| Severity 2 – Major | 8 hours | Email notice to Customer's quality contact |
| Severity 3 – Moderate | 1 business day | Bug database entry only |
| Severity 4 – Minor | 2 business days | Bug database entry only |

**Target:** At least 95% of Defect reports in each Severity Level are entered within the applicable Reporting Time in each Measurement Period, and 100% of Severity 1 Defects are reported within 4 hours.

3.2 **Test Execution.** Provider shall execute all test cases scheduled for a Build in the approved test plan within the test cycle stated in the applicable Order Form or, if none is stated, within five (5) business days after Delivery to Provider of the Build to be tested.

**Target:** At least 98% of scheduled test cases executed within the test cycle in each Measurement Period.

3.3 **Regression Verification.** Provider shall verify each Defect that Customer marks as fixed within two (2) business days after Customer makes the Build containing the fix available, or within one (1) business day for a Severity 1 Defect.

**Target:** At least 95% of fix verifications completed within the applicable time in each Measurement Period.

3.4 **Report Accuracy.** Defect reports must be reproducible from the reproduction steps provided and must not duplicate an existing open report.

**Target:** No more than 5% of Defect reports in a Measurement Period are closed by Customer as "cannot reproduce" or "duplicate."

## 4. LOCALIZATION SERVICE LEVELS

4.1 **Translation Turnaround.** Provider shall return translated and reviewed text for each Target Language identified in an Order Form within the following times after Customer delivers the source text:

| **Batch Size (source words)** | **Turnaround** |
|---|---|
| Up to 2,000 | 2 business days |
| 2,001 to 10,000 | 5 business days |
| 10,001 to 50,000 | 10 business days |
| Over 50,000 | As agreed in the Order Form or in writing |

**Target:** At least 95% of batches returned within the applicable Turnaround in each Measurement Period.

4.2 **Linguistic Quality.** Localized Deliverables must meet the standards in Section 7 of the Quality Agreement.

**Target:** No more than one (1) Severity 2 localization Defect per 10,000 source words, and no Severity 1 localization Defect, identified by Customer in Delivered localized text in each Measurement Period.

4.3 **Urgent Requests.** For text that Customer designates as urgent, including legal, age-rating and platform-mandated text, Provider shall return translated and reviewed text of up to 500 source words per Target Language within one (1) business day.

## 5. LIVE-OPERATIONS SUPPORT SERVICE LEVELS

5.1 **Player Support Response Times.** Provider shall send a first substantive response to each Player Ticket within the following times after it is received:

| **Channel** | **First Response Time** |
|---|---|
| Chat (during Coverage Hours) | 2 minutes |
| Ticketing | 12 hours |
| Email | 24 hours |

**Target:** At least 90% of Player Tickets in each channel receive a first substantive response within the applicable First Response Time in each Measurement Period.

5.2 **Escalation.** Provider shall escalate to Customer's designated live-operations contact, in accordance with the escalation procedures approved under Section 10.2 of the Agreement, any Player Ticket or live-environment issue that involves a suspected security incident, account compromise, payment issue, server outage, threat of harm or legal claim.

**Target:** 100% of escalations made within 30 minutes after Provider identifies the issue.

5.3 **Player Ticket Resolution.** Provider shall resolve each Player Ticket that it is authorized to resolve under Customer's approved procedures within three (3) days after receipt.

**Target:** At least 85% of such Player Tickets resolved within three (3) days in each Measurement Period.

5.4 **Moderation Coverage Hours.** Unless an Order Form states otherwise, Provider shall provide community moderation on the channels identified in the applicable Order Form during the following hours ("**Coverage Hours**"):

(a) for the first thirty (30) days after commercial release of a Customer Title, twenty-four (24) hours a day, seven (7) days a week; and

(b) after that period, sixteen (16) hours a day, seven (7) days a week, from 6:00 a.m. to 10:00 p.m. Pacific Time.

Chat-channel player support is available during the same Coverage Hours.

**Target:** Moderation coverage staffed for at least 99% of scheduled Coverage Hours in each Measurement Period.

5.5 **Content Removal.** During Coverage Hours, Provider shall remove or hide content that violates Customer's community policies within fifteen (15) minutes after it is flagged or identified. For content involving threats of harm, personal information or illegal material, the removal time is five (5) minutes.

**Target:** At least 95% of flagged content addressed within the applicable time in each Measurement Period.

5.6 **Player Satisfaction.** Provider shall maintain an average player satisfaction score of at least 80% on Customer's post-interaction survey, measured across all Player Tickets with a completed survey in each Measurement Period.

## 6. CAPACITY AND STAFFING COMMITMENTS

6.1 **Scheduling Priority.** Consistent with Section 3.5 of the Agreement, Provider shall give Customer's Order Forms priority over its other customers' work in scheduling test cycles, localization batches and live-operations staffing.

6.2 **Ramp-Up Capacity.** On thirty (30) days' written notice from Customer, Provider shall increase the QA testing headcount assigned to Customer by up to fifty percent (50%) above the minimum staffing stated in the applicable Order Form. On ten (10) business days' notice, Provider shall increase it by up to twenty-five percent (25%).

6.3 **Surge Capacity.** For the period from fourteen (14) days before through thirty (30) days after commercial release of a Customer Title, Provider shall reserve sufficient player support and moderation personnel to meet the Service Levels in Section 5 at a Player Ticket volume of up to three (3) times the volume forecast that Customer provides at least thirty (30) days before release.

6.4 **Minimum Staffing.** Provider shall maintain any minimum staffing stated in an Order Form. Provider's failure to do so for more than five (5) business days in a Measurement Period is a Service Level Failure.

6.5 **Staff Continuity.** Provider shall use reasonable efforts to keep personnel assigned to a Customer Title on that title for the duration of the applicable Order Form. Turnover of assigned QA personnel should not exceed fifteen percent (15%) in any rolling three-month period, excluding removals that Customer requests under Section 4.3 of the Agreement.

## 7. SERVICE CREDITS

7.1 **Calculation.** For each Service Level Failure, Provider shall issue a Service Credit equal to the following percentage of the Monthly Fees under the affected Order Form for the Measurement Period in which the failure occurred:

| **Service Level** | **Service Credit** |
|---|---|
| Section 3.1 (Severity 1 or Severity 2 reporting) | 5% |
| Section 3.1 (Severity 3 or Severity 4 reporting) | 2% |
| Sections 3.2, 3.3 and 3.4 | 2% each |
| Sections 4.1 and 4.3 | 3% each |
| Section 4.2 | 4% |
| Sections 5.1 and 5.3 | 3% each |
| Sections 5.2 and 5.5 | 5% each |
| Section 5.4 | 4% |
| Section 5.6 | 1% |
| Section 6.4 | 5% |

7.2 **Cap.** The total Service Credits for an Order Form in a Measurement Period shall not exceed twenty percent (20%) of the Monthly Fees under that Order Form for that Measurement Period.

7.3 **Application.** Provider shall show each Service Credit on the invoice for the Measurement Period after the one in which the Service Level Failure occurred. If no further invoice is due under the applicable Order Form, Provider shall pay the Service Credit to Customer within thirty (30) days after the end of the Measurement Period.

7.4 **Nature of Service Credits.** As stated in Section 7.2 of the Agreement, Service Credits are a price adjustment that reflects the reduced value of the Services. They are not Customer's sole remedy for a Service Level Failure that also constitutes a material breach of the Agreement. Any damages Customer recovers for the same failure are reduced by the Service Credits issued for it.

## 8. EXCLUSIONS

8.1 **Excused Failures.** A Service Level Failure is excused to the extent it is caused by:

(a) a force majeure event under Section 17.7 of the Agreement;

(b) Customer's failure to deliver Builds, source text, development kits, access credentials or approved scripts and procedures when required by the applicable Order Form, or Customer's other breach of the Agreement;

(c) unavailability of Customer's bug database, Delivery Portal, ticketing system or other Customer-controlled systems; or

(d) Player Ticket volumes that exceed the forecast in Section 6.3, but only for the excess volume and only during the period described in that Section.

8.2 **Notice of Excused Failure.** To rely on Section 8.1, Provider shall notify Customer in writing of the cause and its expected effect within two (2) business days after Provider becomes aware of it, and shall use reasonable efforts to meet the affected Service Levels despite it.

## 9. REPORTING AND REVIEW

9.1 **Monthly Reports.** Within ten (10) business days after the end of each Measurement Period, Provider shall deliver to Customer the monthly report required by Section 7.3 of the Agreement. Each report must state, for each Order Form:

(a) Provider's actual performance against each Service Level;

(b) each Service Level Failure, its cause and the corrective action taken;

(c) the Service Credits due;

(d) headcount assigned, by role, against any minimum staffing; and

(e) Player Ticket volumes by channel and Defect counts by Severity Level.

9.2 **Measurement Data.** Provider shall measure performance using data from the designated bug database, ticketing system and moderation tools. Provider shall give Customer read access to the underlying data on request and shall keep it for the period stated in Section 8.4 of the Quality Agreement.

9.3 **Service Reviews.** Service Level performance shall be reviewed at the monthly quality reviews under Section 8.2 of the Quality Agreement.

9.4 **Corrective Action.** If Provider fails the same Service Level in two (2) consecutive Measurement Periods, Provider shall deliver a written corrective action plan under Section 8.3 of the Quality Agreement.

## 10. CHRONIC FAILURE

10.1 **Chronic Failure.** A "**Chronic Failure**" occurs if Provider fails (a) the same Service Level in three (3) Measurement Periods within any six (6) consecutive Measurement Periods, or (b) any Service Level in Section 3.1 (Severity 1 reporting), 5.2 or 6.4 in two (2) consecutive Measurement Periods.

10.2 **Effect.** A Chronic Failure is a material breach of the affected Order Form for the purposes of Section 15.2 of the Agreement.

## 11. REVIEW AND CHANGES

11.1 **Annual Review.** The Parties shall review the Service Levels at least once a year in good faith to reflect changes in the Services, platforms and industry practice.

11.2 **Changes.** This Service Level Schedule may be amended only by a written instrument signed by both Parties. Service Levels for a particular Order Form may also be stated or changed in that Order Form or a signed change order under Section 2.3 of the Agreement.

## 12. GENERAL

12.1 **Governing Law.** This Service Level Schedule is governed by the laws of the State of Delaware, without regard to its conflict of laws principles. Section 17.2 of the Agreement applies to any action arising out of or relating to this Service Level Schedule.

12.2 **Notices.** Notices under Sections 8.2 and 10 must be given in accordance with Section 17.3 of the Agreement. Operational communications and reports under Sections 3, 5 and 9 may be given by email or through the designated bug database or ticketing system.

12.3 **Counterparts.** This Service Level Schedule may be signed in counterparts, including by electronic signature. Each counterpart is an original, and together they form one instrument.

---

**IN WITNESS WHEREOF**, the Parties have signed this Service Level Schedule as of the SLS Effective Date.

| **LEBUN INTERACTIVE, INC.** | **DRAIBOUTH STUDIOS LLC** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: | Name: |
| Title: | Title: |
| Service Level Contact: | Service Level Contact: |