# SERVICE LEVEL SCHEDULE

**LaneCast Platform**

This Service Level Schedule is attached to and forms part of the Software License Agreement dated as of June 16, 2025 (the "**Agreement**") between **Draibav Systems, Inc.** ("**Licensor**") and **Logith Auto Auctions, LLC** ("**Licensee**"). Capitalized terms used but not defined in this Schedule have the meanings given in the Agreement.

## 1. DEFINITIONS

1.1 "**Auction Day**" means any day on which Licensee conducts a scheduled sale at any Licensed Site or through the Platform's online auction module, as shown in the sale calendar Licensee provides to Licensor through the Platform.

1.2 "**Auction Hours**" means, on each Auction Day, the period from 6:00 a.m. to 8:00 p.m. local time at the Licensed Site concerned.

1.3 "**Business Hours**" means 7:00 a.m. to 7:00 p.m. Eastern Time, Monday through Friday, excluding U.S. federal holidays.

1.4 "**Downtime**" means any period during which the Platform, or any of its simulcast bidding, online auction, mobile bidding or vehicle condition reporting modules, is unavailable to, or materially fails to function for, Licensee, its Authorized Users, Bidders or Consignors, as measured by Licensor's monitoring tools and confirmed by Licensee's reasonable records. Downtime does not include Excluded Downtime.

1.5 "**Excluded Downtime**" means unavailability caused by (a) Scheduled Maintenance; (b) failures of Licensee's own networks, hardware or internet connectivity at a Licensed Site that are not provided or managed by Licensor; (c) Licensee's breach of the Agreement or use of the Platform contrary to the Documentation; or (d) a force majeure event under Section 16.6 of the Agreement, other than an event that Licensor's disaster recovery and business continuity obligations under Section 6 of this Schedule are designed to address.

1.6 "**Monthly Availability**" means, for each calendar month, the percentage calculated as: ((Total Minutes − Downtime Minutes) ÷ Total Minutes) × 100, where "Total Minutes" is the total number of minutes in the month and "Downtime Minutes" is the total number of minutes of Downtime in that month.

1.7 "**Scheduled Maintenance**" means maintenance of the Platform that is carried out in accordance with Section 2.3.

1.8 "**Service Credit**" means a credit against Subscription Fees calculated under Section 4.

## 2. AVAILABILITY

2.1 **Availability Commitment.** Licensor shall make the Platform available with a Monthly Availability of at least 99.9% in each calendar month (the "**Availability Commitment**").

2.2 **Auction Hours.** Licensor shall use its best efforts to ensure that no Downtime occurs during Auction Hours. Licensor shall staff its network operations center during all Auction Hours with personnel able to respond immediately to a Severity 1 Incident.

2.3 **Scheduled Maintenance.** Licensor may perform Scheduled Maintenance only (a) outside Auction Hours; (b) for no more than eight (8) hours in any calendar month; and (c) on at least five (5) Business Days' prior notice to Licensee through the Platform and by email. Emergency maintenance required to address a security vulnerability may be performed on shorter notice, but counts as Downtime if performed during Auction Hours.

2.4 **Reporting.** Within ten (10) days after the end of each calendar month, Licensor shall provide Licensee with a written report stating the Monthly Availability for that month, each Downtime event and its duration, root cause and remediation, and any Service Credits due.

## 3. SUPPORT

3.1 **Support Channels.** Licensor shall provide telephone, email and in-Platform ticket support. Telephone support for Severity 1 and Severity 2 Incidents is available twenty-four (24) hours a day, seven (7) days a week. Support for other Incidents is available during Business Hours.

3.2 **Severity Levels and Response Times.** Licensor shall classify each reported incident (an "**Incident**") reasonably and in good faith, taking into account Licensee's reasonable assessment, and shall respond and resolve as follows:

| Severity | Description | Initial Response | Target Resolution or Workaround |
|---|---|---|---|
| 1 – Critical | The Platform or any simulcast bidding or online auction module is unavailable or unusable during Auction Hours, or a Security Incident is suspected | 15 minutes | 2 hours |
| 2 – High | A material function is degraded with no reasonable workaround, including condition report publishing or mobile bidding | 1 hour | 8 hours |
| 3 – Medium | A non-critical function is impaired, or a workaround is available | 4 Business Hours | 5 Business Days |
| 4 – Low | Cosmetic issues, documentation errors or general questions | 1 Business Day | Next scheduled release |

3.3 **Escalation.** If a Severity 1 Incident is not resolved within its target resolution time, Licensor shall escalate it to its Vice President of Operations and provide Licensee with status updates at least every thirty (30) minutes until resolution.

3.4 **Root Cause Analysis.** Within five (5) Business Days after resolving any Severity 1 Incident, Licensor shall deliver to Licensee a written root cause analysis and corrective action plan.

3.5 **Updates.** Licensor shall provide all Updates to Licensee at no additional charge and shall deploy Updates in a manner that does not cause Downtime during Auction Hours.

## 4. SERVICE CREDITS

4.1 **Credit Schedule.** If Monthly Availability in any calendar month falls below the Availability Commitment, Licensee will be entitled to a Service Credit equal to the following percentage of the Subscription Fees for that month:

| Monthly Availability | Service Credit |
|---|---|
| Less than 99.9% but at least 99.5% | 5% |
| Less than 99.5% but at least 99.0% | 10% |
| Less than 99.0% but at least 98.0% | 20% |
| Less than 98.0% | 30% |

4.2 **Auction Hours Downtime.** In addition to any Service Credit under Section 4.1, for each Severity 1 Incident that causes Downtime of more than thirty (30) consecutive minutes during Auction Hours, Licensee will be entitled to a further Service Credit of 5% of the Subscription Fees for that month.

4.3 **Application.** Licensor shall apply Service Credits automatically against the next invoice following the report under Section 2.4. Any Service Credits outstanding at expiration or termination of the Agreement shall be paid to Licensee within thirty (30) days. Service Credits for any month may not exceed in total 50% of the Subscription Fees for that month.

4.4 **Relationship to Other Remedies.** Service Credits are a price adjustment reflecting reduced service value and are not a penalty. Service Credits are without prejudice to Licensee's rights under Section 5 of this Schedule and Section 12 of the Agreement.

## 5. TERMINATION RIGHTS

5.1 **Chronic Failure.** A "**Chronic Failure**" occurs if Monthly Availability is below 99.0% in any three (3) calendar months within any rolling six (6) month period.

5.2 **Termination for Chronic Failure.** If a Chronic Failure occurs, Licensee may terminate the Agreement, in whole or with respect to any one or more Licensed Sites, by giving Licensor written notice within thirty (30) days after the end of the third affected month. Termination takes effect on the date stated in Licensee's notice, which may be no later than one hundred eighty (180) days after the date of the notice. On termination under this Section 5.2, no early termination fee, accelerated Fees or other termination charge will be payable, and Section 12.6(c) and Section 12.7 of the Agreement apply.

5.3 **Severity 1 Failures.** If three (3) or more Severity 1 Incidents each cause Downtime of more than two (2) hours during Auction Hours in any period of ninety (90) consecutive days, Licensee may terminate the Agreement by written notice to Licensor within thirty (30) days after the third such Incident, on the same terms as apply under Section 5.2.

5.4 **Partial Termination.** If Licensee terminates with respect to fewer than all Licensed Sites, the Subscription Fees will be reduced pro rata to reflect the Licensed Sites remaining under the Agreement, as set out in the Order Form.

## 6. DISASTER RECOVERY AND BUSINESS CONTINUITY

6.1 **Plan.** Licensor shall maintain, test at least annually, and provide a summary to Licensee on request of, a written disaster recovery and business continuity plan for the Platform.

6.2 **Redundancy.** Licensor shall host the Platform in at least two (2) geographically separate data centers located in the United States, with production data replicated between them continuously.

6.3 **Recovery Objectives.** Following a disaster affecting the primary hosting environment, Licensor shall restore the Platform to full operation with a recovery time objective of four (4) hours and a recovery point objective of fifteen (15) minutes.

6.4 **Backups.** Licensor shall perform daily backups of all Licensee Data, retain backups for at least thirty (30) days, and test restoration from backup at least quarterly.

## 7. GENERAL

7.1 **Review.** The Parties shall meet at least quarterly to review Licensor's performance under this Schedule, open Incidents and planned Updates.

7.2 **Changes.** Licensor may not change this Schedule in any manner that reduces the service levels, Service Credits or termination rights available to Licensee, except by a written amendment signed by both Parties in accordance with Section 16.3 of the Agreement.