# SERVICE LEVEL SCHEDULE

This Service Level Schedule (this "**Schedule**") is entered into under the Master Services Agreement dated as of March 2, 2026 (the "**MSA**" or the "**Agreement**") between **Seinon Outdoor Gear, Inc.** ("**Customer**") and **Poseirt Commerce Logistics, LLC** ("**Provider**"). This Schedule is the Service Level Schedule referred to in the MSA. It applies to the Services provided under Order Form No. 1 and under each later Order Form that references it. Capitalized terms used but not defined in this Schedule have the meanings given in the MSA or the applicable Order Form.

## 1. Purpose and Scope

**1.1 Purpose.** This Schedule sets out the following for the Services:

(a) the service levels;

(b) the methods for measuring and reporting them; and

(c) the service credits that apply when a service level is not met.

**1.2 Scope.** This Schedule covers:

(a) the Storefront and Platform services described in Section 2.1 of the MSA and Section 5.1 of the Order Form; and

(b) the fulfillment services at the Facility described in Section 2.2 of the MSA and Section 5.2 of the Order Form.

## 2. Definitions

In this Schedule:

(a) "**Business Day**" means any day other than a Saturday, Sunday or United States federal holiday.

(b) "**Measurement Period**" means each calendar month during the term of an Order Form.

(c) "**Scheduled Maintenance**" means planned maintenance of the Platform that meets all of the following conditions:

- Provider notifies Customer at least five (5) Business Days in advance;
- the maintenance occurs between 11:00 p.m. and 4:00 a.m. Pacific Time; and
- the maintenance does not exceed eight (8) hours in any Measurement Period.

(d) "**Service Credit**" means a credit against Fees, calculated as set out in Section 5.

(e) "**Service Failure**" means either:

- Provider's failure to meet a Service Level in any Measurement Period; or
- the occurrence of a Security Incident.

(f) "**Service Level**" means each performance standard set out in Section 3.

(g) "**Storefront Availability**" means the percentage of minutes in a Measurement Period, excluding Scheduled Maintenance, during which the Storefront home page, product pages, cart and checkout are all accessible to end customers and capable of accepting orders. Availability is measured by Provider's external synthetic monitoring at one-minute intervals from at least three (3) geographically separate locations in North America.

## 3. Service Levels

**3.1 Storefront and Platform Service Levels.**

| No. | Service Level | Target |
|---|---|---|
| SL-1 | Storefront Availability | 99.9% per Measurement Period |
| SL-2 | Checkout page response time (median, server-side) | 2.0 seconds or less |
| SL-3 | Order transmission from Platform to Facility | 99.9% of orders within 15 minutes of placement |

**3.2 Fulfillment Service Levels.**

| No. | Service Level | Target |
|---|---|---|
| SL-4 | Inbound receiving: Products received, inspected and available for sale | 99% of cartons within two (2) Business Days of delivery to the Facility |
| SL-5 | Ship timeliness: orders shipped in accordance with the order cut-off in Section 5.3 of the Order Form (2:00 p.m. Pacific Time) | 99.5% of orders |
| SL-6 | Order accuracy: orders shipped with correct SKUs, quantities and end-customer address | 99.8% of orders |
| SL-7 | Inventory record accuracy by unit | 99.5% |
| SL-8 | Returns processing: returned units inspected, graded and dispositioned | 98% of units within three (3) Business Days of receipt |

**3.3 Support Service Levels.** Provider will provide 24x7 support for Priority 1 incidents and Business Day support (6:00 a.m. to 6:00 p.m. Pacific Time) for all other incidents. The response and resolution targets are as follows:

| Priority | Description | Response | Target Resolution or Workaround |
|---|---|---|---|
| P1 | Storefront or checkout unavailable, or Facility unable to ship | 30 minutes | 4 hours |
| P2 | Material degradation of a core function | 2 hours | 1 Business Day |
| P3 | Non-critical defect or request | 1 Business Day | 10 Business Days |

The applicable Service Level (SL-9) is met if Provider meets the response target for at least 95% of incidents in each priority level in the Measurement Period.

**3.4 Security Notification.** Provider will notify Customer of each Security Incident within forty-eight (48) hours after becoming aware of it, in accordance with Section 8.3 of the MSA (SL-10).

## 4. Measurement and Reporting

**4.1 Measurement of Fulfillment Service Levels.** Provider will measure each fulfillment Service Level from the warehouse management system records for the Facility, as follows:

(a) **Ship timeliness (SL-5)** is measured by the carrier scan time of each order.

(b) **Order accuracy (SL-6)** is measured by the number of orders reported as mis-shipped by end customers or Customer and confirmed by Provider's investigation, divided by total orders shipped.

**4.2 Inventory Record Accuracy.** Inventory record accuracy (SL-7) is calculated for each Measurement Period by the following steps:

(a) Take the total units counted in all cycle counts and physical inventories performed in the Measurement Period under Section 7.1 of the Order Form.

(b) Subtract the absolute value of all unit variances between counted and system quantities.

(c) Divide the result by the total units counted.

**4.3 Monthly Report.** Within ten (10) Business Days after the end of each Measurement Period, Provider will deliver to Customer a written performance report. The report will include:

(a) Provider's measured performance against each Service Level;

(b) details of each Service Failure;

(c) the root cause and remediation steps for each Service Failure; and

(d) the Service Credits due.

**4.4 Data Access.** Customer may review the underlying measurement data on reasonable request. Customer may also have Provider's measurements verified by an independent third party no more than once per contract year. If verification shows that Provider understated a Service Failure, Provider will bear the reasonable cost of verification.

## 5. Service Credits

**5.1 Credit Amounts.** For each Service Level that Provider fails to meet in a Measurement Period, Provider will issue a Service Credit equal to the percentage of the Monthly Platform Fee shown below:

| Service Level | Performance in Measurement Period | Service Credit |
|---|---|---|
| SL-1 Storefront Availability | Below 99.9% but at or above 99.5% | 5% |
| SL-1 Storefront Availability | Below 99.5% but at or above 99.0% | 10% |
| SL-1 Storefront Availability | Below 99.0% | 15% |
| SL-2, SL-3 | Below target | 2% each |
| SL-4, SL-8 | Below target | 3% each |
| SL-5, SL-6 | Below target | 5% each |
| SL-7 | Below target | 4% |
| SL-9 | Below target | 2% |
| SL-10 | Notification not made within 48 hours | 5% per Security Incident |

**5.2 Maximum Credits.** The total Service Credits for any Measurement Period will not exceed twenty-five percent (25%) of the Monthly Platform Fee for that Measurement Period.

**5.3 Application.** Provider will apply Service Credits against the next invoice issued after the monthly report for the Measurement Period in which the credits accrue. If no further invoice will be issued, Provider will pay the amount of any accrued Service Credits to Customer within thirty (30) days.

**5.4 Exceptions.** A failure to meet a Service Level does not give rise to a Service Credit to the extent the failure is caused by any of the following:

(a) Scheduled Maintenance;

(b) a force majeure event under Section 15.3 of the MSA;

(c) Customer's breach of Section 4 of the MSA, including late or inaccurate advance shipping notices; or

(d) failures of Customer's enterprise resource planning system or other Customer-controlled systems.

## 6. Remedies

**6.1 Remediation.** For each Service Failure, Provider will do the following:

(a) promptly investigate and correct the Service Failure;

(b) perform a root-cause analysis; and

(c) deliver to Customer a written corrective action plan within ten (10) Business Days.

**6.2 Chronic Failure.** A "**Chronic Failure**" occurs if either of the following happens:

(a) Provider fails to meet the same Service Level in any three (3) Measurement Periods within a rolling six (6) month period; or

(b) Storefront Availability falls below 99.0% in any two (2) consecutive Measurement Periods.

On a Chronic Failure, Customer may terminate the affected Order Form on written notice to Provider, without payment of any termination fee. Customer must give that notice within sixty (60) days after the Chronic Failure occurs. Section 9.5 of the MSA (Transition Assistance) applies to any such termination.

**6.3 Exclusive Remedy.** Service Credits and Customer's termination right under Section 6.2 are Customer's sole and exclusive remedies for any Service Failure, including any Security Incident. Notwithstanding Section 11.3 of the MSA, Provider's aggregate liability arising out of or relating to Security Incidents shall not exceed the cap set out in Section 11.2 of the MSA.

**6.4 Credits Not a Penalty.** The parties agree that Service Credits are a reasonable price adjustment reflecting the reduced value of the Services, and are not a penalty.

## 7. Review

**7.1 Quarterly Review.** The parties' account representatives will meet at least once each calendar quarter to review Provider's performance under this Schedule and any corrective action plans.

**7.2 Adjustment of Service Levels.** The parties may agree to add, remove or adjust Service Levels to reflect changes in the Services. No adjustment is effective unless it is made in writing and signed by both parties in accordance with Section 15.5 of the MSA.

## 8. General

**8.1 Incorporation.** This Schedule forms part of the contract for each Order Form as described in Section 1.2 of the MSA.

**8.2 Counterparts.** This Schedule may be signed in counterparts, including by electronic signature. Each counterpart is an original, and all counterparts together constitute one instrument.

---

**IN WITNESS WHEREOF**, the parties have executed this Service Level Schedule as of the date last signed below.

| **SEINON OUTDOOR GEAR, INC.** | **POSEIRT COMMERCE LOGISTICS, LLC** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: | Name: |
| Title: | Title: |
| Date: | Date: |