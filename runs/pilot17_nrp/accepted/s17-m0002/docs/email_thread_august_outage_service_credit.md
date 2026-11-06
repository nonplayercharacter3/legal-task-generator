# Email Thread: Reelpath Outage of August 19, 2026 and August Service Credit

## 1. Message 1

**From:** Simev Support <support@simevsystems.com>
**To:** Jonah Wexler <jwexler@trilundpictures.com>
**Cc:** Priya Natarajan <pnatarajan@simevsystems.com>
**Date:** Wednesday, August 19, 2026, 2:26 p.m. ET
**Subject:** [Severity 1] Ticket #RP-260819-0147: Reelpath unavailable (all modules)

Jonah,

We confirm receipt of your call to the support line at 2:19 p.m. ET. We have logged the issue as Severity 1 under Section 5.3(a) of the Service Level Schedule.

Our monitoring flagged the Platform as not Available from 2:14 p.m. ET. Authorized Users cannot log in, and the secure media hosting module is not serving uploads, streams or downloads. Our engineering team is engaged. Initial indications point to a fault in a storage controller in the primary hosting environment.

We have no indication of any Security Incident. Licensee Content is encrypted at rest. We have seen no access to Licensee Content other than by our authorized personnel.

We will send status updates at least every two hours until the issue is resolved.

Simev Systems Support

## 2. Message 2

**From:** Simev Support <support@simevsystems.com>
**To:** Jonah Wexler <jwexler@trilundpictures.com>
**Cc:** Priya Natarajan <pnatarajan@simevsystems.com>
**Date:** Wednesday, August 19, 2026, 4:10 p.m. ET
**Subject:** RE: [Severity 1] Ticket #RP-260819-0147: Reelpath unavailable (all modules)

Jonah,

Status update: the failed storage controller did not hand over automatically to its standby unit. Our engineers are carrying out a manual failover and then verifying data integrity on the affected volumes. We do not yet have a confirmed restoration time. The next update will follow by 6:10 p.m. ET or sooner.

Simev Systems Support

## 3. Message 3

**From:** Simev Support <support@simevsystems.com>
**To:** Jonah Wexler <jwexler@trilundpictures.com>
**Cc:** Priya Natarajan <pnatarajan@simevsystems.com>
**Date:** Wednesday, August 19, 2026, 6:31 p.m. ET
**Subject:** RE: [Severity 1] Ticket #RP-260819-0147: Reelpath unavailable (all modules) – RESOLVED

Jonah,

The Platform was restored and confirmed Available across all three modules at 6:26 p.m. ET. Integrity checks on the affected volumes are complete. No Licensee Content was lost or altered. Pending uploads queued before 2:14 p.m. have resumed.

Total unavailability was 4 hours 12 minutes (252 minutes). We will provide a root cause summary within five Business Days. The outage will also be included in the August monthly report under Section 2.5 of the Service Level Schedule.

We apologize for the disruption.

Simev Systems Support

## 4. Message 4

**From:** Jonah Wexler <jwexler@trilundpictures.com>
**To:** Priya Natarajan <pnatarajan@simevsystems.com>
**Cc:** Rachel Okafor <rokafor@trilundpictures.com>
**Date:** Thursday, August 20, 2026, 9:47 a.m. ET
**Subject:** Yesterday's Reelpath outage

Priya,

Thanks to your team for the updates yesterday. The outage hit while two of our festival screener deliveries were in progress. We re-sent those links once access returned, and no deadlines were missed. Still, four hours in the middle of a weekday is significant for us.

Please send the root cause summary when it is ready, along with details of any steps you are taking so the standby controller fails over automatically next time. I'm copying Rachel in Business and Legal Affairs so she can track the service credit position for August.

Jonah Wexler
Director of Distribution Operations
Trilund Pictures Releasing, LLC

## 5. Message 5

**From:** Priya Natarajan <pnatarajan@simevsystems.com>
**To:** Jonah Wexler <jwexler@trilundpictures.com>
**Cc:** Rachel Okafor <rokafor@trilundpictures.com>
**Date:** Wednesday, August 26, 2026, 3:05 p.m. ET
**Subject:** RE: Yesterday's Reelpath outage – root cause summary

Jonah, Rachel,

A summary of the root cause is below.

5.1 **Cause.** A firmware fault caused a storage controller in our primary data center to stop responding. The standby controller's failover trigger depended on a health-check signal that the same fault suppressed. As a result, automatic failover did not start, and our engineers completed the failover manually.

5.2 **Remediation.** We have applied the vendor's corrected firmware to all controllers in the primary and backup environments. We have also added an independent health check that starts failover without relying on the controller's own signal. We tested the new trigger during the Scheduled Maintenance window on Sunday, August 23.

5.3 **Classification.** This was not Scheduled Maintenance and not a force majeure event. The full 252 minutes count as Downtime for August.

The August monthly report will show the Availability figure and the resulting Service Credit.

Best,
Priya Natarajan
Senior Account Manager, Simev Systems, Inc.

## 6. Message 6

**From:** Priya Natarajan <pnatarajan@simevsystems.com>
**To:** Jonah Wexler <jwexler@trilundpictures.com>; Rachel Okafor <rokafor@trilundpictures.com>
**Date:** Friday, September 11, 2026, 11:20 a.m. ET
**Subject:** Reelpath Monthly Service Report – August 2026

Jonah, Rachel,

The August 2026 monthly report under Section 2.5 of the Service Level Schedule is attached. In summary:

| Item | August 2026 |
|---|---|
| Minutes in month | 44,640 |
| Scheduled Maintenance (Aug. 9, 12:00–1:30 a.m.; Aug. 23, 12:00–1:30 a.m. ET) | 180 minutes |
| Total Minutes (after Excluded Downtime) | 44,460 |
| Downtime (Aug. 19, 2:14–6:26 p.m. ET, storage controller fault) | 252 minutes |
| Availability | 99.43% |
| Availability Commitment | 99.5% |
| Service Credit tier | Less than 99.5% but at least 99.0%: 5% |
| Monthly Fee ($186,000 ÷ 12) | $15,500.00 |
| Service Credit accrued | $775.00 |

Both Scheduled Maintenance windows fell within the Sunday window. Notice of each went out by email more than five Business Days in advance. No other Downtime was recorded in August.

Under Section 4.4 of the Schedule, we will apply the $775.00 credit against the next invoice issued to Trilund. That will be the additional usage invoice for the quarter ending August 31, 2026.

Best,
Priya

## 7. Message 7

**From:** Rachel Okafor <rokafor@trilundpictures.com>
**To:** Priya Natarajan <pnatarajan@simevsystems.com>
**Cc:** Jonah Wexler <jwexler@trilundpictures.com>
**Date:** Monday, September 14, 2026, 10:12 a.m. ET
**Subject:** RE: Reelpath Monthly Service Report – August 2026

Priya,

Thanks for the report. I have checked the numbers against the Schedule. 252 minutes over 44,460 minutes gives 99.433% Availability, which falls in the 5% tier. 5% of the $15,500 Monthly Fee is $775. Jonah's team's internal logs also show first failure at 2:14 p.m. and restoration at 6:26 p.m., so we agree with the Downtime figure.

Please confirm once the credit appears on the invoice.

Rachel Okafor
Head of Business and Legal Affairs
Trilund Pictures Releasing, LLC

## 8. Message 8

**From:** Simev Billing <billing@simevsystems.com>
**To:** Rachel Okafor <rokafor@trilundpictures.com>
**Cc:** Priya Natarajan <pnatarajan@simevsystems.com>; accountspayable@trilundpictures.com
**Date:** Friday, September 18, 2026, 9:02 a.m. ET
**Subject:** Invoice SIM-INV-2026-0911 – Reelpath Additional Usage, June 1 – August 31, 2026

Dear Rachel,

Invoice SIM-INV-2026-0911 is attached, issued under Section 5.1 of the Agreement:

| Line | Description | Amount |
|---|---|---|
| 1 | Additional hosted storage above 60 TB: 4 TB × $300 per TB per month × 3 months (June–August 2026) | $3,600.00 |
| 2 | Service Credit – August 2026 (Service Level Schedule, Section 4) | ($775.00) |
| | **Total due** | **$2,825.00** |

Payment is due within thirty (30) days of receipt.

Simev Systems Billing

## 9. Message 9

**From:** Rachel Okafor <rokafor@trilundpictures.com>
**To:** Priya Natarajan <pnatarajan@simevsystems.com>
**Cc:** Jonah Wexler <jwexler@trilundpictures.com>; accountspayable@trilundpictures.com
**Date:** Friday, September 18, 2026, 2:40 p.m. ET
**Subject:** RE: Invoice SIM-INV-2026-0911 – Reelpath Additional Usage, June 1 – August 31, 2026

Priya,

Confirmed. The storage line reflects the Amendment No. 1 rate of $300 per terabyte, and the August credit has been applied correctly. Accounts payable will process $2,825.00 in the ordinary course. We consider the August outage closed on our side.

Jonah will raise the new failover trigger at the Q3 service review so we can confirm it is performing as expected.

Thanks,
Rachel