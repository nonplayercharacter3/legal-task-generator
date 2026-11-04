# Daitend Dental Partners: Internal Email Thread, Imaging Module Rollout

---

## 1. Email: Rollout Kickoff

**From:** Renata Okafor, Director of Clinical Operations
**To:** Imaging Rollout Working Group
**Cc:** Marcus Lindqvist, IT Manager; Dr. Priya Venkataraman, Clinical Director
**Date:** Monday, September 9, 2024, 8:42 a.m.
**Subject:** Imaging Module rollout: phased plan for all 22 clinics

Team,

Thanks for joining Friday's call. Here is a summary of what we agreed.

We will move all 22 clinics from the legacy local imaging servers onto the Gaiport Imaging Module in three waves:

| Wave | Clinics | Target go-live |
|---|---|---|
| 1 (pilot) | Dover, Newark Main, Middletown | October 7, 2024 |
| 2 | 9 clinics (northern region) | November 4, 2024 |
| 3 | 10 clinics (southern region) | December 2, 2024 |

Each clinic will have one "imaging champion," usually the lead hygienist, who attends Gaiport's training session and serves as the first point of contact for staff questions.

Marcus is confirming sensor and workstation compatibility. Dr. Venkataraman is reviewing the clinical image-viewing workflow with the pilot dentists.

Please send me your clinic champion nominations by Friday, September 13.

Renata

---

## 2. Email: Sensor Compatibility Check

**From:** Marcus Lindqvist, IT Manager
**To:** Renata Okafor
**Cc:** Imaging Rollout Working Group
**Date:** Wednesday, September 11, 2024, 3:15 p.m.
**Subject:** RE: Imaging Module rollout: phased plan for all 22 clinics

Renata,

I compared our sensor inventory against Gaiport's current Documentation (the hardware compatibility list in the Imaging Module setup guide).

- **Intraoral sensors:** All sensors at 19 clinics are on the supported list. Three clinics (Smyrna, Milford and Seaford) still use an older sensor model. It is supported, but it needs a driver update that we install ourselves.
- **Panoramic units:** All supported. Two units need a firmware update from the device manufacturer, not from Gaiport. I have requested service visits.
- **Workstations:** Fourteen operatory workstations are below the minimum RAM spec in the Documentation. I have already budgeted the replacements under this year's IT refresh, and they will be in place before Wave 3.
- **Bandwidth:** Our internet links at all clinics meet the recommended upload speed for full-resolution radiographs.

None of this changes the wave dates. I will track the three driver updates for Wave 3.

Marcus

---

## 3. Email: Pilot Clinical Workflow

**From:** Dr. Priya Venkataraman, Clinical Director
**To:** Renata Okafor; Marcus Lindqvist
**Date:** Thursday, September 19, 2024, 7:58 p.m.
**Subject:** RE: Imaging Module rollout: phased plan for all 22 clinics

Renata, Marcus,

I sat with the Dover and Middletown dentists for the workflow review. Their feedback:

1. Image capture into the patient chart is faster than with the legacy server. The image attaches to the appointment automatically, which removes a manual step.
2. Side-by-side comparison of prior bitewings works well. The dentists want the "compare" view set as the default layout. Gaiport's trainer showed us how to set that per user.
3. Annotation tools are adequate. One dentist asked whether measurements carry over when images are exported. I confirmed with Gaiport support that exports are in DICOM format and keep the calibration data.

As a reminder to everyone: the Imaging Module is a viewing and records tool. Diagnosis stays with our dentists, and our clinical protocols do not change.

I'm comfortable proceeding with the pilot on October 7.

Priya

---

## 4. Email: Legacy Image Migration

**From:** Marcus Lindqvist, IT Manager
**To:** Renata Okafor
**Cc:** Imaging Rollout Working Group
**Date:** Tuesday, October 1, 2024, 11:20 a.m.
**Subject:** Legacy image migration for Wave 1

Renata,

Gaiport's implementation team confirmed the migration plan for the pilot clinics:

- Historic radiographs from the three pilot clinics' local servers will be bulk-uploaded over the weekend of October 5–6.
- Gaiport will run a record-count reconciliation afterward. I will spot-check fifty patient charts per clinic on Monday morning before patients arrive.
- The legacy servers will stay read-only for ninety days as a fallback. After that, we will decommission them under our standard media-disposal procedure.

Gaiport has posted a scheduled maintenance notice for Saturday night, October 5, from 11:00 p.m. to 2:00 a.m. ET. The notice went out on October 1, comfortably more than 48 hours ahead. No clinic is open during that window.

Marcus

---

## 5. Email: Pilot Go-Live Report

**From:** Renata Okafor, Director of Clinical Operations
**To:** Imaging Rollout Working Group
**Cc:** Dr. Priya Venkataraman
**Date:** Friday, October 11, 2024, 4:47 p.m.
**Subject:** Wave 1 go-live: week one summary

All,

The first week of the pilot went well. Highlights:

- **Volume:** About 1,140 images captured across Dover, Newark Main and Middletown.
- **Support tickets:** Seven opened with Gaiport, all resolved. Five were user questions on annotation settings. Two concerned a sensor not being recognized after a workstation restart, which Gaiport's support line fixed by phone within the hour. Their support desk is staffed 7:00 a.m. to 8:00 p.m. ET on business days, which covers our clinic hours.
- **Migration:** Marcus's spot-check found all sampled historic images present and correctly matched to patients.
- **Staff feedback:** Positive overall. Front-office staff like that imaging appointments now show on the same schedule screen.

Lessons for Waves 2 and 3:

1. Schedule champion training at least one week before go-live, not the Thursday before.
2. Pre-load the default "compare" layout for all dentist profiles before go-live.
3. Print the one-page sensor troubleshooting sheet for every operatory.

Unless anyone objects by Wednesday, we will proceed with Wave 2 on November 4.

Renata

---

## 6. Email: Wave 2 Confirmation

**From:** Marcus Lindqvist, IT Manager
**To:** Renata Okafor
**Cc:** Imaging Rollout Working Group
**Date:** Monday, October 28, 2024, 9:05 a.m.
**Subject:** RE: Wave 1 go-live: week one summary

Renata,

Wave 2 readiness checklist is complete:

- Champion training held October 22–23 (all nine champions attended).
- Default dentist layouts pre-configured.
- Legacy migration for the nine northern clinics scheduled for November 2–3, with Gaiport's maintenance notice already posted.
- Troubleshooting sheets printed and shipped to each clinic.

The Wave 3 workstation replacements arrive November 18, and the three sensor driver updates are queued for the same week. We remain on track for December 2.

Marcus

---

## 7. Email: Rollout Closeout

**From:** Renata Okafor, Director of Clinical Operations
**To:** Imaging Rollout Working Group
**Cc:** Dr. Priya Venkataraman; Chief Operating Officer
**Date:** Friday, December 13, 2024, 2:30 p.m.
**Subject:** Imaging Module rollout complete: all 22 clinics live

All,

As of December 2, all 22 clinics are live on the Imaging Module. Wave 3 went smoothly. The new workstations and driver updates were installed on schedule, and we logged no Severity 1 incidents during any wave.

Legacy servers at the Wave 1 clinics will be decommissioned in early January, once the ninety-day fallback period ends, followed by Waves 2 and 3 on the same ninety-day cadence. Marcus will circulate the disposal certificates when complete.

Thank you to every clinic champion for the extra hours. I'll schedule a short retrospective in January to capture lessons for future module rollouts.

Renata