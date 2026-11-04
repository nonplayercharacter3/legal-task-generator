# Email Thread: Onboarding of Severna Park Clinic Location

---

## 1. Message 1

**From:** Daniel Reyes-Whitford <dreyes@daitenddental.com>
**To:** Priya Venkataraman <pvenkataraman@gaiport.com>
**Cc:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>
**Date:** Tuesday, August 4, 2026, 9:42 AM
**Subject:** New clinic onboarding – Severna Park

Hi Priya,

As discussed on last week's check-in call, Daitend closed on its acquisition of the Severna Park practice (formerly Bayside Family Dentistry) on July 31. We want to bring it onto the Gaiport platform as a new Clinic Location. Please treat this email as our written request under Section 2.4 of the Master Services Agreement.

Basic details:

- **Location:** 8 Ritchie Highway, Suite 4B, Severna Park, Maryland 21146
- **Operatories:** 6
- **Expected Authorized Users:** 14 (3 dentists, 5 hygienists, 6 front-desk/billing staff)
- **Modules:** Scheduling, Billing, and Imaging, the same as our other locations
- **Legacy system:** The practice currently runs a locally hosted server with a desktop practice-management package and a separate imaging bridge. Roughly 9 years of patient records and radiographs.

We are aiming to go live in late September, ideally before the hygienists' fall recall push. Could you send over a change order and a proposed implementation timeline?

Thanks,
Daniel

Daniel Reyes-Whitford
Director of IT and Clinical Systems
Daitend Dental Partners, LLC

---

## 2. Message 2

**From:** Priya Venkataraman <pvenkataraman@gaiport.com>
**To:** Daniel Reyes-Whitford <dreyes@daitenddental.com>
**Cc:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>; Owen Laskaris <olaskaris@gaiport.com>
**Date:** Wednesday, August 5, 2026, 2:15 PM
**Subject:** RE: New clinic onboarding – Severna Park

Hi Daniel,

Congratulations on the acquisition. Late September is achievable. I've copied Owen Laskaris, who will lead the data migration.

Proposed timeline:

| Milestone | Target Date |
|---|---|
| Change order signed | August 14, 2026 |
| Legacy data extract and test load | August 24 – September 4, 2026 |
| Validation by Severna Park staff | September 8 – 11, 2026 |
| Staff training (two on-site sessions) | September 15 and 17, 2026 |
| Final cutover and go-live | Monday, September 28, 2026 |

I'll have the change order to you by Monday. It will add Severna Park to the Clinic Location list at the per-location, Authorized User and module rates in the initial Statement of Work. Data migration and training will be billed as Professional Services at the rates in that same Statement of Work. Nothing else in the Agreement changes.

Best,
Priya

Priya Venkataraman
Implementation Manager
Gaiport Clinical Systems, Inc.

---

## 3. Message 3

**From:** Owen Laskaris <olaskaris@gaiport.com>
**To:** Daniel Reyes-Whitford <dreyes@daitenddental.com>
**Cc:** Priya Venkataraman <pvenkataraman@gaiport.com>
**Date:** Thursday, August 6, 2026, 10:08 AM
**Subject:** RE: New clinic onboarding – Severna Park

Daniel,

For the extract, we'll need:

1. Read-only credentials for the legacy practice-management database, or a full export file if the vendor can produce one.
2. Access to the imaging bridge storage directory so we can pull the radiographs and intraoral scans. We convert these to DICOM on ingest, consistent with the format used for your other locations.
3. A contact at the practice who can answer questions about custom appointment codes and fee schedules.

All transfers go through our encrypted SFTP endpoint. I'll send you a one-time credential under separate cover. Please don't email any patient files.

Owen

Owen Laskaris
Senior Data Migration Engineer
Gaiport Clinical Systems, Inc.

---

## 4. Message 4

**From:** Daniel Reyes-Whitford <dreyes@daitenddental.com>
**To:** Owen Laskaris <olaskaris@gaiport.com>
**Cc:** Priya Venkataraman <pvenkataraman@gaiport.com>; Lauren Whitcombe <lwhitcombe@daitenddental.com>
**Date:** Thursday, August 6, 2026, 3:51 PM
**Subject:** RE: New clinic onboarding – Severna Park

Owen,

Understood. Lauren Whitcombe, the Severna Park office manager (copied), will be your practice contact. I'll set up the read-only database account tomorrow. The legacy vendor says a full export takes about five business days, so we'll go with direct read-only access.

Lauren, please loop in Dr. Hsu on the custom appointment codes.

Daniel

---

## 5. Message 5

**From:** Priya Venkataraman <pvenkataraman@gaiport.com>
**To:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>
**Cc:** Daniel Reyes-Whitford <dreyes@daitenddental.com>; contracts@daitenddental.com
**Date:** Monday, August 10, 2026, 11:30 AM
**Subject:** Change Order – Severna Park Clinic Location
**Attachment:** Gaiport_Daitend_Change_Order_SevernaPark.pdf

Hi Renata,

Attached is the change order adding Severna Park as a Clinic Location under Section 2.4 of the Master Services Agreement. In summary, it:

- adds Severna Park to the Clinic Location list effective on the go-live date;
- adds 14 Authorized Users and the Scheduling, Billing and Imaging modules for that location, at the rates in the initial Statement of Work;
- covers data migration and two on-site training sessions as Professional Services at the Statement of Work rates; and
- confirms that all other terms of the Agreement, the DPA and the existing Statement of Work remain unchanged.

Per-location charges start with the first monthly invoice after go-live and appear as a separate line item from the Platform Fee.

Please sign via the DocuSign link, and Marcus will countersign.

Best,
Priya

---

## 6. Message 6

**From:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>
**To:** Priya Venkataraman <pvenkataraman@gaiport.com>
**Cc:** Daniel Reyes-Whitford <dreyes@daitenddental.com>; contracts@daitenddental.com
**Date:** Thursday, August 13, 2026, 4:47 PM
**Subject:** RE: Change Order – Severna Park Clinic Location

Priya,

Our legal team has reviewed the change order. I've signed it in DocuSign this afternoon.

One request: please make sure the Severna Park charges appear as a separate line item on the invoice, as described in your email. Our finance team allocates platform costs by location.

Thanks,
Renata

Renata Okonkwo-Hale
Chief Operating Officer
Daitend Dental Partners, LLC

---

## 7. Message 7

**From:** Priya Venkataraman <pvenkataraman@gaiport.com>
**To:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>
**Cc:** Daniel Reyes-Whitford <dreyes@daitenddental.com>; contracts@daitenddental.com
**Date:** Friday, August 14, 2026, 9:12 AM
**Subject:** RE: Change Order – Severna Park Clinic Location

Renata,

Marcus countersigned this morning. You should have the fully executed copy from DocuSign. I've also confirmed with our billing team that Severna Park will be invoiced as its own line item.

Best,
Priya

---

## 8. Message 8

**From:** Owen Laskaris <olaskaris@gaiport.com>
**To:** Daniel Reyes-Whitford <dreyes@daitenddental.com>; Lauren Whitcombe <lwhitcombe@daitenddental.com>
**Cc:** Priya Venkataraman <pvenkataraman@gaiport.com>
**Date:** Friday, September 4, 2026, 5:20 PM
**Subject:** RE: New clinic onboarding – Severna Park – test load complete

Daniel, Lauren,

The test load is complete. Results:

- 6,812 patient records migrated, with 0 hard failures. 23 records have missing insurance subscriber dates, flagged in the validation report.
- 41,906 radiographs and intraoral scans converted to DICOM and linked to patient charts.
- 412 future appointments loaded. Custom codes are mapped per Dr. Hsu's spreadsheet.

The validation environment is open. Please have staff spot-check charts and images between September 8 and 11.

Owen

---

## 9. Message 9

**From:** Lauren Whitcombe <lwhitcombe@daitenddental.com>
**To:** Owen Laskaris <olaskaris@gaiport.com>
**Cc:** Daniel Reyes-Whitford <dreyes@daitenddental.com>; Priya Venkataraman <pvenkataraman@gaiport.com>
**Date:** Friday, September 11, 2026, 3:02 PM
**Subject:** RE: New clinic onboarding – Severna Park – test load complete

Owen,

Validation is done. We checked 150 charts across all three dentists, and the images and ledgers look right. We've corrected the 23 insurance records directly in the legacy system, so they should come across cleanly on the final load. We're good to proceed with training and the September 28 cutover.

Lauren

---

## 10. Message 10

**From:** Priya Venkataraman <pvenkataraman@gaiport.com>
**To:** Daniel Reyes-Whitford <dreyes@daitenddental.com>; Lauren Whitcombe <lwhitcombe@daitenddental.com>
**Cc:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>; Owen Laskaris <olaskaris@gaiport.com>
**Date:** Monday, September 28, 2026, 1:36 PM
**Subject:** Severna Park – live on Gaiport

All,

Severna Park went live this morning. The final delta load ran overnight without errors, and the first patients were checked in at 8:00 a.m. Owen will stay on hypercare through Friday, October 2. After that, Severna Park support requests should go through the standard support line.

The legacy server can be decommissioned once Daitend's records-retention review is complete. Owen can send a written confirmation of the migrated record counts for your files.

Thanks to everyone for a smooth onboarding.

Best,
Priya

---

## 11. Message 11

**From:** Daniel Reyes-Whitford <dreyes@daitenddental.com>
**To:** Priya Venkataraman <pvenkataraman@gaiport.com>
**Cc:** Renata Okonkwo-Hale <rokonkwohale@daitenddental.com>; Owen Laskaris <olaskaris@gaiport.com>; Lauren Whitcombe <lwhitcombe@daitenddental.com>
**Date:** Monday, September 28, 2026, 4:18 PM
**Subject:** RE: Severna Park – live on Gaiport

Priya, Owen,

Thanks. Day one went well. Please send the record-count confirmation, and we'll file it with the change order. We'll start the legacy server retention review next week.

Daniel