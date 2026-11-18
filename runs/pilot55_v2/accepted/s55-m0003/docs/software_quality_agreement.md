# SOFTWARE QUALITY AGREEMENT

**Sairan Threadline Product Lifecycle Management Platform**

This Software Quality Agreement (this "**Quality Agreement**") is entered into as of January 12, 2026 between **Sairan Systems, LLC** ("**Licensor**") and **Pakairt Outdoor Apparel, Inc.** ("**Licensee**").

It is made under the Software License Agreement between the parties dated January 12, 2026 (the "**Agreement**"). It forms part of the Agreement as provided in Section 1.3 of the Agreement and is the Software Quality Agreement referred to in Section 3.4 of the Agreement. Capitalized terms used but not defined in this Quality Agreement have the meanings given in the Agreement, in Statement of Work No. 001 under the Agreement (the "**SOW**") or in the Service Level Schedule, as applicable.

---

## 1. Purpose and Scope

**1.1 Purpose.** This Quality Agreement sets out the requirements that Licensor shall meet in developing, testing, releasing and correcting the Licensed Software. It also defines the Severity Levels used in the SOW and the Service Level Schedule.

**1.2 Scope.** This Quality Agreement applies to:

(a) the Licensed Software, including all Updates;

(b) the configurations and integrations that Licensor builds under the SOW; and

(c) the production environment and the non-production environments described in Section 2.4 of the SOW.

**1.3 Relationship with the Service Level Schedule.** The Service Level Schedule governs Availability, Incident response and Resolution Targets, and Service Credits. This Quality Agreement governs defect classification, permanent correction of defects, and the testing and release of Updates.

---

## 2. Definitions

**2.1** In this Quality Agreement:

"**Defect**" means any failure of the Licensed Software, or of a configuration or integration built by Licensor under the SOW, to conform to the Documentation, the approved solution design document or the Acceptance Criteria.

"**Emergency Fix**" means an Update released outside the normal release cycle to correct a Severity 1 Defect or a critical security vulnerability.

"**Escaped Defect**" means a Severity 1 or Severity 2 Defect that first appears in the production environment and is caused by an Update.

"**Major Release**" means an Update that introduces new functionality or material changes to existing functionality, user interfaces, data models or application programming interfaces.

"**Maintenance Release**" means an Update that consists mainly of Defect corrections, security patches and minor enhancements, with no material change to existing functionality.

"**Permanent Fix**" means a correction of a Defect in the code or configuration of the Licensed Software that removes the need for any workaround.

"**Quality Records**" has the meaning given in Section 8.1.

"**Release Notes**" means the written description of an Update described in Section 5.3.

---

## 3. Severity Levels

**3.1 Definitions.** Each Incident and each Defect shall be classified at one of the following Severity Levels:

| Severity Level | Definition |
|---|---|
| **Severity 1 (Critical)** | The production environment is not Available, or a material function of a licensed module is unusable for all or a substantial number of Authorized Users, and no workaround is available. This level also covers any confirmed corruption or loss of Customer Data, and any Security Incident affecting the Licensed Software. |
| **Severity 2 (High)** | A material function of a licensed module, or an integration built under the SOW, is materially impaired, and no reasonable workaround is available. Severity 2 also covers a Severity 1 condition for which a temporary workaround has been provided. |
| **Severity 3 (Medium)** | A non-material function is impaired, or a material function is impaired but a reasonable workaround is available. Licensee's business operations continue with limited inconvenience. |
| **Severity 4 (Low)** | A cosmetic issue, documentation error, or request for information, with no material effect on use of the Licensed Software. |

**3.2 Classification.** Severity Levels shall be assigned and reclassified in accordance with Section 3.3 of the Service Level Schedule. A Defect found during user acceptance testing under Section 5 of the SOW shall be classified using the same definitions.

**3.3 Reclassification after Workaround.** Where a workaround is accepted for a Severity 1 or Severity 2 Defect, the Incident is treated as resolved for the purposes of the Service Level Schedule. The underlying Defect shall then be tracked to Permanent Fix under Section 4.

---

## 4. Defect Management

**4.1 Defect Tracking.** Licensor shall record every Defect reported by Licensee, or identified by Licensor, in a defect-tracking system. Each record shall include the Severity Level, the date reported, the affected module, the status and the target date for Permanent Fix. Licensee's authorized support contacts shall have read access to the records for Defects affecting Licensee.

**4.2 Permanent Fix Targets.** Licensor shall deliver a Permanent Fix within the following periods, measured from the date of Resolution under the Service Level Schedule:

| Severity Level | Permanent Fix Target |
|---|---|
| Severity 1 | 10 business days |
| Severity 2 | 20 business days |
| Severity 3 | The next Maintenance Release that is at least 15 business days after the Defect is reported |
| Severity 4 | At Licensor's discretion, and no later than the next Major Release |

**4.3 Root Cause.** For each Severity 1 Defect, the root cause analysis required by Section 3.7 of the Service Level Schedule shall identify whether the Defect is an Escaped Defect. Where it is, the analysis shall identify the testing gap that allowed the Escaped Defect to reach production and the corrective action taken.

**4.4 Regression.** Each Permanent Fix shall include automated regression tests designed to detect the recurrence of the Defect in later Updates.

**4.5 Defects in Licensee Systems.** Licensor is not responsible under this Section 4 for defects in Licensee's ERP, product information management, point-of-sale or e-commerce platforms, or in other third-party systems not under Licensor's control. Licensor shall reasonably cooperate with Licensee and its providers to diagnose any issue at the interface with an integration built under the SOW.

---

## 5. Release Management

**5.1 Release Cadence.** Licensor intends to release Updates on the following cadence:

(a) up to two (2) Major Releases in each calendar year;

(b) Maintenance Releases approximately monthly; and

(c) Emergency Fixes as required.

**5.2 Notice.** Licensor shall give Licensee prior written notice of each Update, which may be given through the support portal or by email:

(a) for a Major Release, at least thirty (30) days before deployment to the production environment;

(b) for a Maintenance Release, at least five (5) business days before deployment; and

(c) for an Emergency Fix, as much notice as is reasonably practicable.

**5.3 Release Notes.** Each notice of a Major Release or Maintenance Release shall be accompanied by Release Notes. The Release Notes shall describe the new or changed functionality, the Defects corrected, any known Defects remaining, any effect on integrations or application programming interfaces, and any action required of Licensee.

**5.4 Pre-Production Availability.** Licensor shall deploy each Major Release to the test and training environment at least fifteen (15) business days before deploying it to production, and each Maintenance Release at least three (3) business days before. Licensee may test the Update during that period. If Licensee reports a Severity 1 or Severity 2 Defect in the Update during that period, Licensor shall not deploy the Update to production until the Defect is corrected, unless Licensee agrees otherwise in writing.

**5.5 Deployment Windows.** Licensor shall deploy Major Releases and Maintenance Releases to the production environment only during Scheduled Maintenance under Section 2.4 of the Service Level Schedule. Licensor shall not deploy them during any blackout period that Licensee notifies under that Section. Emergency Fixes may be deployed as emergency maintenance under Section 2.3(b) of the Service Level Schedule.

**5.6 Backward Compatibility.** Licensor shall use commercially reasonable efforts to ensure that no Update requires changes to the integrations built under the SOW. Where an Update requires such changes, Licensor shall identify them in the Release Notes and shall make the corresponding changes to the Licensor-built components of those integrations at no additional charge.

**5.7 Supported Releases.** Licensor shall support releases as set out in Section 3.8 of the Service Level Schedule.

**5.8 Rollback.** Licensor shall maintain the ability to roll back each Update in the production environment. If an Update causes an Escaped Defect that cannot be corrected promptly, Licensor shall roll back the Update on Licensee's request.

---

## 6. Development and Testing Standards

**6.1 Development Lifecycle.** Licensor shall maintain a documented software development lifecycle for the Licensed Software. It shall include requirements management, peer code review, version control and segregation of development, test and production environments.

**6.2 Testing.** Before releasing any Major Release or Maintenance Release, Licensor shall carry out, and record the results of:

(a) unit and integration testing of all changed components;

(b) automated regression testing of the material functions of each licensed module;

(c) performance testing sufficient to confirm continued compliance with Section 2.5 of the Service Level Schedule; and

(d) security testing, including static code analysis and vulnerability scanning against recognized industry standards such as the OWASP Top 10.

**6.3 Release Criteria.** Licensor shall not release an Update to the production environment if it has any known open Severity 1 or Severity 2 Defect affecting a licensed module.

**6.4 Security Measures.** Licensor's security testing under Section 6.2(d) is in addition to the technical and organizational measures described in Annex 2 to the DPA.

**6.5 Test Data.** Licensor shall not use production Customer Data in development or testing environments other than those provided to Licensee under Section 2.4 of the SOW, unless Licensee gives prior written consent. Any use of personal data is subject to the DPA.

---

## 7. Configuration Change Control

**7.1 Licensee Configurations.** Licensor shall not change the configuration of Licensee's production environment, including workflows, approval routings, attribute libraries and user roles, except:

(a) at Licensee's request through the support portal;

(b) through change control under Section 7 of the SOW; or

(c) where needed to implement an Emergency Fix, with notice to Licensee as soon as reasonably practicable.

**7.2 Configuration Records.** Licensor shall keep a record of every configuration change made to Licensee's environments, including the date, the person making the change and the authorizing request.

---

## 8. Quality Records, Metrics and Review

**8.1 Quality Records.** Licensor shall keep records of its testing, release, Defect and configuration-change activities under this Quality Agreement (the "**Quality Records**") for at least twenty-four (24) months.

**8.2 Quality Metrics.** Licensor shall report the following metrics to Licensee each calendar quarter:

(a) the number of open Defects, by Severity Level and module;

(b) performance against the Permanent Fix targets in Section 4.2;

(c) the number of Escaped Defects; and

(d) the Updates released during the quarter.

**8.3 Quarterly Review.** The metrics under Section 8.2 shall be reviewed at the quarterly review meetings held under Section 6.2 of the Service Level Schedule.

**8.4 Verification.** On reasonable request, and not more than once in any twelve (12) month period, Licensor shall make relevant Quality Records available to Licensee to verify compliance with this Quality Agreement. Any review shall be carried out during normal business hours, without unreasonable disruption to Licensor's operations. Information disclosed is Licensor's Confidential Information under Section 7 of the Agreement.

---

## 9. Governance

**9.1 Quality Contacts.** Each party shall appoint a quality contact responsible for matters under this Quality Agreement:

- **Licensor:** Director, Quality Engineering.
- **Licensee:** IT Applications Manager.

**9.2 Escalation.** Matters under this Quality Agreement that the quality contacts cannot resolve shall be escalated under Section 3.6 of the Service Level Schedule. Disputes shall then be resolved under Section 16 of the Agreement.

---

## 10. General

**10.1 Term.** This Quality Agreement continues for the Term of the Agreement.

**10.2 Notices.** Formal notices under this Quality Agreement must be given in accordance with Section 17.1 of the Agreement. Operational communications, including notices under Section 5.2, may be given through the support portal or by email.

**10.3 Amendment.** Any amendment to this Quality Agreement must be in writing and signed by both parties.

**10.4 Counterparts.** This Quality Agreement may be signed in counterparts, including by electronic signature.

---

**IN WITNESS WHEREOF**, the parties have executed this Quality Agreement as of the date first written above.

| **SAIRAN SYSTEMS, LLC** | **PAKAIRT OUTDOOR APPAREL, INC.** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: Daniel R. Okafor | Name: Margaret L. Tessaro |
| Title: Chief Executive Officer | Title: Chief Operating Officer |
| Date: January 12, 2026 | Date: January 12, 2026 |