# QUALITY AGREEMENT: INVENTORY AND RENTAL ORDER DATA

This Quality Agreement (this "**Quality Agreement**") is entered into as of March 1, 2026 by and between **Beipeiv Software, Inc.**, a Delaware corporation ("**Licensor**"), and **Baineind Event Rentals, LLC**, a Delaware limited liability company ("**Licensee**").

## RECITALS

A. Licensor and Licensee are parties to a Software License Agreement entered into as of March 1, 2026 (the "**Agreement**"). Under the Agreement, Licensor makes its cloud-hosted rental-management Platform available to Licensee.

B. Section 17 of the Agreement contemplates that the parties will agree data validation, inventory reconciliation and error-correction procedures for inventory and Rental Order data processed through the Platform.

C. This Quality Agreement sets out those procedures. It is the "Quality Agreement" referred to in the Agreement.

The parties therefore agree as follows:

## 1. DEFINITIONS AND SCOPE

1.1 **Defined Terms.** Capitalized terms used but not defined in this Quality Agreement have the meanings given in the Agreement.

1.2 **Additional Definitions.** In this Quality Agreement:

(a) "**Data Error**" means any inaccuracy, omission, duplication or corruption in Covered Data.

(b) "**Platform Data Error**" means a Data Error caused by a defect in the Platform. This includes defects in its calculation logic, synchronization between modules, import and export functions, or mobile applications.

(c) "**Licensee Data Error**" means a Data Error caused by data entry, configuration choices or other acts or omissions of Licensee or its Authorized Users, and not by a defect in the Platform.

(d) "**Covered Data**" means the following Licensee Data: (i) inventory item records, including item descriptions, quantities, condition codes, warehouse locations and availability status; (ii) quotes and Rental Orders, including line items, event dates, delivery and pickup windows, and pricing; (iii) delivery dispatch records; and (iv) warehouse pick lists.

(e) "**Data Quality Contact**" means the individual each party designates under Section 2.1.

(f) "**Reconciliation Report**" means the report described in Section 4.2.

1.3 **Scope.** This Quality Agreement applies to Covered Data processed through the Platform during the Term. It does not change the availability commitments, incident severity levels, response and resolution times or service credits in the Service Level Schedule.

## 2. RESPONSIBILITIES AND CONTACTS

2.1 **Data Quality Contacts.** Within fifteen (15) days after the date of this Quality Agreement, each party shall designate a Data Quality Contact by written notice to the other party. Each party may replace its Data Quality Contact by giving the other party notice. Email notice is sufficient for this purpose.

2.2 **Licensor Responsibilities.** Licensor shall:

(a) maintain the validation rules described in Section 3 within the Platform;

(b) investigate reported Data Errors in accordance with Section 5;

(c) correct Platform Data Errors at no additional charge, as required by Section 17.2 of the Agreement; and

(d) provide the Reconciliation Report and other reporting described in Section 4.

2.3 **Licensee Responsibilities.** Licensee shall:

(a) enter Covered Data accurately and in accordance with the Documentation;

(b) configure item categories, warehouse locations and pricing rules with Licensor's reasonable assistance during implementation;

(c) perform the physical inventory counts described in Section 4.1; and

(d) report suspected Data Errors promptly in accordance with Section 5.1.

## 3. DATA VALIDATION

3.1 **Validation Rules.** The Platform shall apply the following automated validation rules to Covered Data at the time of entry or import:

(a) mandatory fields for each inventory item, quote and Rental Order, as agreed during implementation;

(b) a check that no Rental Order allocates more units of an inventory item than are recorded as available for the relevant event dates, unless an Authorized User with override permissions approves the allocation;

(c) a check that delivery and pickup windows on each Rental Order fall within the hours configured for the relevant delivery zone;

(d) a check that line-item pricing on each quote and Rental Order matches the applicable pricing rules, unless an Authorized User with override permissions approves a manual adjustment; and

(e) duplicate-record detection for inventory items and customer and venue records.

3.2 **Override Log.** The Platform shall record each override of a validation rule in an audit log. The log shall show the Authorized User, the date and time, the rule overridden and any comment entered. Licensee may export the log at any time.

3.3 **Changes to Validation Rules.** Either party may propose changes to the validation rules by notice to the other party's Data Quality Contact. Licensor shall implement changes that the parties agree in writing within thirty (30) days after agreement, or within another period the parties agree. Changes requested by Licensee that require custom development are Additional Services under Section 5.3 of the Agreement.

3.4 **Bulk Imports.** Before completing any bulk import of Covered Data, Licensor shall run the validation rules against the import file. Licensor shall give Licensee an exception report listing every record that fails validation. Licensor shall not complete the import until Licensee has approved the exception report or corrected the failing records.

## 4. INVENTORY RECONCILIATION AND REPORTING

4.1 **Physical Counts.** Licensee shall perform a physical count of inventory at each warehouse location at least once in each calendar quarter. Licensee shall record the results in the Platform using the cycle-count function described in the Documentation.

4.2 **Reconciliation Report.** Within five (5) business days after Licensee records the results of a quarterly physical count for a warehouse location, Licensor shall make available a Reconciliation Report for that location. The report shall identify each inventory item for which the quantity recorded in the Platform differs from the physical count, together with the transaction history for that item since the previous count.

4.3 **Review Meeting.** Within ten (10) business days after each Reconciliation Report is made available, the Data Quality Contacts shall meet, by video conference unless they agree otherwise. They shall review any variances and agree which variances may be Platform Data Errors requiring investigation under Section 5.

4.4 **Monthly Dashboard.** Licensor shall make available to Licensee, within the Platform, a monthly data-quality dashboard showing (a) the number of validation rule overrides by rule and by location, (b) the number of Data Errors reported, investigated and corrected during the month, and (c) the status of any open Data Error investigations.

## 5. ERROR REPORTING, INVESTIGATION AND CORRECTION

5.1 **Reporting.** Licensee shall report suspected Data Errors through Licensor's online support portal. Each report should identify the affected records, the location concerned and, where known, the circumstances in which the Data Error arose. If a suspected Data Error also affects the availability or operation of the Platform, Licensee may report it as an incident under the Service Level Schedule. In that case the Service Level Schedule governs the classification and response to the incident, and this Section 5 governs the correction of the affected Covered Data.

5.2 **Investigation.** Licensor shall begin investigating each reported Data Error within two (2) business days after receiving the report. Within five (5) business days after receiving the report, Licensor shall tell Licensee in writing whether Licensor considers the Data Error to be a Platform Data Error or a Licensee Data Error, and its reasons.

5.3 **Correction of Platform Data Errors.** For each Platform Data Error, Licensor shall at no additional charge:

(a) correct the affected Covered Data, or give Licensee a corrected data file and instructions for loading it;

(b) identify any other Covered Data affected by the same defect and correct it; and

(c) correct the underlying defect in the Platform in accordance with Section 11.2 of the Agreement.

Licensor shall complete the correction under clause (a) within five (5) business days after confirming the Platform Data Error. However, if the Data Error affects a Rental Order with an event date within the following seven (7) days, Licensor shall complete that correction within one (1) business day.

5.4 **Licensee Data Errors.** Licensee is responsible for correcting Licensee Data Errors. At Licensee's request, Licensor shall provide reasonable assistance by telephone and through the support portal at no additional charge. Licensor may charge for bulk corrections of Licensee Data Errors as Additional Services under Section 5.3 of the Agreement, at the rates that apply under the Agreement and the Side Letter.

5.5 **Disagreement on Classification.** If Licensee disagrees with Licensor's classification of a Data Error, the Data Quality Contacts shall meet within five (5) business days to try to resolve the disagreement. If they cannot resolve it, either party may escalate the matter under Section 7. While the disagreement is unresolved, Licensor shall correct the affected Covered Data if Licensee asks it to. If the Data Error is later agreed or determined to be a Licensee Data Error, Licensor may charge for that correction under Section 5.4.

5.6 **Root-Cause Report.** For any Platform Data Error that affects more than fifty (50) Rental Orders, or Rental Orders at more than one Licensee location, Licensor shall give Licensee a written root-cause report within ten (10) business days after correcting the Data Error. The report shall describe the cause, the records affected, the corrective action taken and the steps Licensor has taken to prevent recurrence.

## 6. DATA MIGRATION

6.1 **Initial Migration.** As part of the implementation services under Section 4.1 of the Agreement, Licensor shall migrate Licensee's existing inventory and customer records into the Platform. Before go-live, Licensor shall give Licensee a migration reconciliation report comparing record counts and item quantities in Licensee's legacy system with those loaded into the Platform.

6.2 **Acceptance of Migrated Data.** Licensee shall review the migration reconciliation report within ten (10) business days after receiving it and notify Licensor of any discrepancies. Licensor shall correct discrepancies caused by the migration process at no additional charge before go-live.

6.3 **Exit Data.** On expiration or termination of the Agreement, the Covered Data shall be made available for export in accordance with Section 7.3 of the Agreement. Licensor shall include the override log described in Section 3.2 and the most recent Reconciliation Report for each location in the export.

## 7. GOVERNANCE AND ESCALATION

7.1 **Quarterly Review.** The Data Quality Contacts shall meet at least once each calendar quarter. At the meeting they shall review the monthly dashboards, open investigations, Reconciliation Reports and any proposed changes to the validation rules.

7.2 **Escalation.** Either party may escalate any matter under this Quality Agreement that the Data Quality Contacts cannot resolve within ten (10) business days. Escalation is made by notice to the other party's account executive (for Licensee, its Chief Operating Officer or a person of equivalent seniority). The escalation contacts shall meet within ten (10) business days after the notice. Escalation under this Section 7.2 does not limit either party's rights or remedies under the Agreement.

## 8. RECORDS AND AUDIT

8.1 **Records.** Licensor shall retain records of each Data Error report, investigation, classification and correction for the Term and for one (1) year afterward.

8.2 **Audit.** Once in each contract year, on at least thirty (30) days' notice, Licensee may review Licensor's records under Section 8.1 relating to Licensee. Licensee may also review the operation of the validation rules for Licensee's instance of the Platform. Each review shall take place remotely or at Licensor's offices during normal business hours and is subject to Section 10 of the Agreement.

## 9. TERM

9.1 This Quality Agreement takes effect on March 1, 2026 and remains in effect for the Term of the Agreement. It ends automatically on expiration or termination of the Agreement. Sections 6.3 and 8.1 survive for the periods stated in them.

## 10. GENERAL

10.1 **Relationship to the Agreement.** This Quality Agreement is entered into under Section 17 of the Agreement. The provisions of the Agreement apply to this Quality Agreement, including Sections 10 (Confidentiality), 13 (Limitation of Liability), 16 (Assignment) and 20 (General).

10.2 **Notices.** Except as provided in Sections 2.1 and 3.3, notices under this Quality Agreement shall be given in accordance with Section 20.3 of the Agreement.

10.3 **Amendment.** This Quality Agreement may be amended only by a written instrument signed by authorized representatives of both parties.

10.4 **Counterparts.** This Quality Agreement may be executed in counterparts, including by electronic signature.

**IN WITNESS WHEREOF**, the parties have executed this Quality Agreement as of March 1, 2026.

| **BEIPEIV SOFTWARE, INC.** | **BAINEIND EVENT RENTALS, LLC** |
|---|---|
| By: ______________________ | By: ______________________ |
| Name: ____________________ | Name: ____________________ |
| Title: _____________________ | Title: _____________________ |
| Date: _____________________ | Date: _____________________ |