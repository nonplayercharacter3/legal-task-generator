# NIMBUS IMPLEMENTATION STATEMENT OF WORK

This Nimbus Implementation Statement of Work (this "**SOW**") is entered into as of February 1, 2027 (the "**SOW Effective Date**") by and between **Drupuv Systems, Inc.**, a Delaware corporation ("**Drupuv**"), and **Fatesk Interactive Entertainment, LLC**, a Delaware limited liability company ("**Fatesk**").

This SOW is entered into under the Platform License Agreement between Drupuv and Fatesk dated as of February 1, 2027 (the "**Agreement**"). It is the "Statement of Work" referred to in the Agreement. Capitalized terms used but not defined in this SOW have the meanings given in the Agreement.

## 1. Purpose and Scope

1.1 **Purpose.** Drupuv shall implement the Platform for the Licensed Titles and integrate it with them. The goal is to have matchmaking, player login and authentication, cross-platform accounts and in-game commerce operating in production for each Licensed Title.

1.2 **Licensed Titles in Scope.** This SOW covers the Licensed Titles listed in Exhibit A to the Agreement as of the SOW Effective Date:

(a) *Ironveil: Frontier* (PC, PlayStation, Xbox);

(b) the *Ironveil: Frontier* mobile companion application (iOS, Android); and

(c) *Project Halcyon* (working title; PC, PlayStation, Xbox, Nintendo).

1.3 **Additional Titles.** Implementation work for any title added to Exhibit A after the SOW Effective Date will be performed under a change order or a separate statement of work agreed under Section 10.2.

## 2. Implementation Services

Drupuv shall perform the following Implementation Services.

2.1 **Discovery and Integration Design.** Drupuv shall:

(a) review Fatesk's existing online services architecture, build pipelines and platform-holder certification requirements;

(b) prepare a written integration design document for each Licensed Title, covering SDK placement, authentication flows, account-linking rules across platforms, matchmaking queue configuration, and storefront and entitlement mapping; and

(c) deliver a project plan with milestone dates consistent with Section 3.

2.2 **SDK Integration.** Drupuv shall:

(a) integrate the Platform SDKs and APIs into the client and server builds of each Licensed Title, in Fatesk-designated source branches;

(b) configure matchmaking rulesets, skill-rating parameters and regional queue settings as specified in the approved integration design document;

(c) implement player login and authentication through each applicable first-party platform identity service, with cross-platform account linking;

(d) integrate in-game commerce with each applicable first-party storefront and with Fatesk's web store, including entitlement grants, virtual currency balances and receipt validation; and

(e) support Fatesk's engineering team in resolving integration defects identified during platform-holder certification.

2.3 **Data Migration.** Drupuv shall:

(a) migrate existing *Ironveil: Frontier* End User account records, profile data, entitlements, virtual currency balances and purchase history from Fatesk's current backend systems to the Platform;

(b) perform at least two (2) full rehearsal migrations in a staging environment before the production migration;

(c) reconcile the migrated records against source data and deliver a written reconciliation report showing record counts, balance totals and any exceptions; and

(d) perform the production migration during a maintenance window Fatesk approves in advance.

2.4 **Launch Readiness.** Drupuv shall:

(a) conduct load and soak testing of the Platform configuration for each Licensed Title at not less than the Licensed Concurrency;

(b) conduct failover and regional disaster recovery testing;

(c) prepare launch runbooks, escalation contacts and monitoring dashboards for each Licensed Title;

(d) provide on-site or remote "war room" support from Drupuv engineers for the first seventy-two (72) hours after each Licensed Title goes live on the Platform; and

(e) deliver a written launch readiness report confirming the completion of the activities in this Section 2.4.

2.5 **Knowledge Transfer.** Drupuv shall provide up to forty (40) hours of training to Fatesk's live operations and engineering staff on Platform administration, configuration tools and monitoring.

## 3. Milestones and Schedule

3.1 **Milestones.** Drupuv shall use commercially reasonable efforts to achieve the following milestones by the target dates set out in the approved project plan:

| Milestone | Description |
|---|---|
| M1 – Design Approval | Fatesk accepts the integration design documents and project plan under Section 2.1 |
| M2 – Integration Complete | SDK integration under Section 2.2 completed for all Licensed Titles in staging |
| M3 – Migration Complete | Production data migration under Section 2.3 completed and reconciliation report accepted |
| M4 – Launch Readiness | Launch readiness activities under Section 2.4 completed and launch readiness report accepted |

3.2 **Delays.** Drupuv shall notify Fatesk promptly if it expects any milestone to be delayed. The notice shall state the cause and Drupuv's proposed recovery plan. A delay caused by Fatesk's failure to perform its responsibilities under Section 7 extends the affected target date by a reasonable period.

## 4. Acceptance

4.1 **Acceptance Criteria.** Each milestone is accepted when the related deliverables conform in all material respects to this SOW and the approved integration design document. In addition:

(a) for M2, all integration test cases in the approved test plan must pass with no open Severity 1 or Severity 2 defects;

(b) for M3, the reconciliation report must show no unresolved discrepancies in entitlements or virtual currency balances; and

(c) for M4, load testing must demonstrate stable operation at not less than the Licensed Concurrency.

4.2 **Acceptance Process.** Fatesk shall have ten (10) business days after Drupuv's notice of completion of a milestone to accept it or to give written notice describing any non-conformity. Drupuv shall correct any notified non-conformity and resubmit the milestone, and the acceptance process shall then repeat. If Fatesk does not respond within the ten (10) business day period, Drupuv may give a reminder notice. The milestone is deemed accepted if Fatesk does not respond within five (5) business days after that reminder.

## 5. Fees

5.1 **Implementation Fee.** The fee for the Implementation Services is a $420,000 fixed fee (the "**Implementation Fee**"). The Implementation Fee covers all Implementation Services described in Section 2. Drupuv shall not charge any additional time-and-materials fees for this scope.

5.2 **Payment Schedule.** Drupuv shall invoice the Implementation Fee as follows:

| Event | Amount |
|---|---|
| SOW Effective Date | $84,000 |
| Acceptance of M2 | $126,000 |
| Acceptance of M3 | $126,000 |
| Acceptance of M4 | $84,000 |
| **Total** | **$420,000** |

5.3 **Payment Terms.** Invoices are payable in accordance with Section 5.2 of the Agreement. Fees exclude taxes, which are governed by Section 5.5 of the Agreement.

5.4 **Expenses.** Travel expenses for on-site launch support under Section 2.4(d) are reimbursable at cost if Fatesk approves them in writing in advance. No other expenses are reimbursable.

## 6. Personnel and Project Governance

6.1 **Project Managers.** Each Party shall appoint a project manager as its primary point of contact for this SOW. Each Party shall give the other written notice of its project manager's name within five (5) business days after the SOW Effective Date.

6.2 **Drupuv Personnel.** Section 4.2 of the Agreement applies to the personnel Drupuv assigns to the Implementation Services. Drupuv shall assign a named lead solutions architect for the full duration of this SOW.

6.3 **Status Reporting.** The project managers shall meet at least weekly. Drupuv shall deliver a written status report each week covering progress against milestones, open risks and open defects.

6.4 **Escalation.** Any issue the project managers cannot resolve within five (5) business days shall be escalated to Drupuv's Vice President of Customer Engineering and Fatesk's Head of Online Services.

## 7. Fatesk Responsibilities

Fatesk shall, in accordance with Section 4.3 of the Agreement:

(a) give Drupuv timely access to the relevant build environments, source branches and staging environments;

(b) provide export files and schema documentation for the source data to be migrated under Section 2.3;

(c) make available engineering, live operations and quality assurance personnel with appropriate knowledge of the Licensed Titles;

(d) obtain any first-party platform developer credentials needed for the integration work; and

(e) review and respond to deliverables within the times stated in Section 4.

## 8. Deliverables and Intellectual Property

8.1 **Deliverables.** "**Deliverables**" means the integration design documents, project plan, reconciliation reports, launch runbooks, monitoring dashboard configurations, launch readiness report, and any integration code written by Drupuv specifically for the Licensed Titles under this SOW.

8.2 **Ownership.** Subject to Fatesk's payment in full of the Implementation Fee, Fatesk owns all right, title and interest in the Deliverables. Until that payment, Drupuv grants Fatesk a non-exclusive license to use the Deliverables for the Licensed Titles.

8.3 **Drupuv Materials.** The Deliverables do not include the Platform, the Documentation, or any of Drupuv's pre-existing materials or generally applicable tools, which remain Drupuv's property under Section 10.1 of the Agreement. To the extent any Drupuv materials are incorporated into a Deliverable, they are licensed to Fatesk as part of the Platform under Section 2 of the Agreement.

8.4 **Fatesk Data.** All Fatesk Data handled during the Implementation Services, including migrated data, is subject to Section 9 of the Agreement.

## 9. Governing Law and Venue

9.1 **Governing Law.** This SOW and any dispute arising out of or relating to this SOW or the Implementation Services are governed by the laws of the State of California, without regard to its conflict of laws principles.

9.2 **Venue.** Each Party submits to the exclusive jurisdiction of the state and federal courts located in San Francisco County, California for any action arising out of or relating to this SOW or the Implementation Services. Each Party waives any objection to venue in those courts.

## 10. General

10.1 **Term of SOW.** This SOW begins on the SOW Effective Date and continues until Fatesk accepts M4 and the launch support period under Section 2.4(d) ends for each Licensed Title, unless terminated earlier together with the Agreement.

10.2 **Change Orders.** Either Party may request a change to the scope, schedule or fees of this SOW. No change is binding unless it is set out in a written change order signed by both Parties.

10.3 **Warranty.** The Implementation Services are subject to the warranty in Section 13.2(b) of the Agreement.

10.4 **Counterparts.** This SOW may be executed in counterparts, including by electronic signature. Each counterpart is an original, and all of them together form one instrument.

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