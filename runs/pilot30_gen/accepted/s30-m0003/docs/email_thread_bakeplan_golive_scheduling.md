# Email Thread: BakePlan Go-Live Scheduling, Order Form No. 1 Licensed Facilities

## 1. Message 1

**From:** Tomas Reyes <t.reyes@rivixsystems.com>
**To:** Grace Lindqvist <g.lindqvist@veilound.com>
**Cc:** Dana Okafor <d.okafor@rivixsystems.com>
**Date:** March 18, 2026, 9:42 AM ET
**Subject:** BakePlan implementation: proposed go-live sequence

Hi Grace,

Thanks for the kickoff call on Monday, and for confirming your designation as Veilound's project manager. As noted in our March 10 email, I am Rivix's project manager for the Order Form No. 1 implementation.

Following our discussion, here is a proposed go-live sequence for the five Licensed Facilities. It is designed to meet the six-month target in Section 5.2 of the Order Form:

| **No.** | **Facility** | **Proposed Go-Live** |
|---|---|---|
| 1 | Allentown Bread Plant | Monday, May 11, 2026 |
| 2 | Reading Bun and Roll Plant | Monday, June 8, 2026 |
| 3 | Hagerstown Sweet Goods Plant | Monday, July 13, 2026 |
| 4 | Lehigh Valley Distribution Center | Monday, August 3, 2026 |
| 5 | Corporate Offices | Monday, August 17, 2026 |

We suggest starting with Allentown because it has the largest recipe library and the most complex oven and proofer configuration. Getting it live first gives us a template for the other plants.

For each plant we would plan a weekend cutover. Production Scheduler configuration would be locked the Thursday before, and the final recipe and allergen migration validation report would go to your team on the Friday.

Let me know if these dates work with your production calendar.

Best,
Tomas

Tomas Reyes | Implementation Lead | Rivix Systems, Inc.

## 2. Message 2

**From:** Grace Lindqvist <g.lindqvist@veilound.com>
**To:** Tomas Reyes <t.reyes@rivixsystems.com>
**Cc:** Martin Hallberg <m.hallberg@veilound.com>; Ben Achterberg <b.achterberg@veilound.com>
**Date:** March 19, 2026, 4:15 PM ET
**Subject:** RE: BakePlan implementation: proposed go-live sequence

Tomas,

Thanks. The sequence works for us in principle. Two adjustments:

1. **Reading.** June 8 falls in the middle of our summer bun ramp-up for the grilling season. Could we move Reading to Monday, June 22? Ben Achterberg (Reading plant manager, copied) says the line schedule is lighter that week.

2. **Hagerstown.** Hagerstown has a planned oven rebuild on Line 2 in the week of July 6. July 13 should be fine, but the Line 2 capacity profile will need to reflect the new oven. I will send the updated specifications once maintenance confirms them.

On migration: our current count is approximately 2,140 active recipe formulations across all plants, which is within the 2,500 in Section 5.1(b). We will finish cleaning up obsolete versions before Allentown data is extracted.

Can you also confirm that Severity 1 emergency support will be in place from the Allentown cutover weekend?

Grace

Grace Lindqvist | Director, Production Systems | Veilound Bakeries, Inc.

## 3. Message 3

**From:** Tomas Reyes <t.reyes@rivixsystems.com>
**To:** Grace Lindqvist <g.lindqvist@veilound.com>
**Cc:** Martin Hallberg <m.hallberg@veilound.com>; Ben Achterberg <b.achterberg@veilound.com>; Dana Okafor <d.okafor@rivixsystems.com>
**Date:** March 20, 2026, 11:03 AM ET
**Subject:** RE: BakePlan implementation: proposed go-live sequence

Grace,

Both adjustments are fine on our side.

- **Reading** moves to Monday, June 22, 2026. That still leaves three weeks before Hagerstown.
- **Hagerstown** stays at Monday, July 13, 2026. We will build the Line 2 profile as soon as we receive your updated oven specifications. We need them by June 26 to stay on schedule.

Confirmed on support. Twenty-four-hour Severity 1 coverage under Section 11.1 of the Agreement applies to any Licensed Facility with production scheduling running on BakePlan. For each cutover weekend we will also have a named on-call engineer, who I will identify in the cutover runbook.

We will also avoid scheduling any maintenance in the week before or after each go-live. Any maintenance that does occur will be announced at least 48 hours in advance and performed outside 4:00 a.m. to 8:00 p.m. Eastern Time, as usual.

Updated sequence:

| **No.** | **Facility** | **Go-Live** |
|---|---|---|
| 1 | Allentown Bread Plant | Monday, May 11, 2026 |
| 2 | Reading Bun and Roll Plant | Monday, June 22, 2026 |
| 3 | Hagerstown Sweet Goods Plant | Monday, July 13, 2026 |
| 4 | Lehigh Valley Distribution Center | Monday, August 3, 2026 |
| 5 | Corporate Offices | Monday, August 17, 2026 |

If you are happy with this, please reply confirming, and we will treat this thread as the written agreement on go-live dates under Section 11.3 of the Agreement and Section 5.2 of the Order Form.

Tomas

## 4. Message 4

**From:** Grace Lindqvist <g.lindqvist@veilound.com>
**To:** Tomas Reyes <t.reyes@rivixsystems.com>
**Cc:** Martin Hallberg <m.hallberg@veilound.com>; Ben Achterberg <b.achterberg@veilound.com>; Dana Okafor <d.okafor@rivixsystems.com>
**Date:** March 20, 2026, 2:37 PM ET
**Subject:** RE: BakePlan implementation: proposed go-live sequence

Tomas,

Confirmed. Veilound agrees to the go-live dates in the updated table in your 11:03 AM email.

Next steps on our side:

1. Recipe cleanup and Allentown extract to Rivix by April 17.
2. Hagerstown Line 2 oven specifications by June 26.
3. Plant training rosters to you two weeks before each go-live, so that on-site administrator and train-the-trainer sessions can be scheduled under Section 5.1(d).
4. ERP integration test credentials for the production order and inventory level interfaces by April 3.

Please send the draft cutover runbook for Allentown when it is ready.

Thanks,
Grace

## 5. Message 5

**From:** Tomas Reyes <t.reyes@rivixsystems.com>
**To:** Grace Lindqvist <g.lindqvist@veilound.com>
**Cc:** Martin Hallberg <m.hallberg@veilound.com>
**Date:** August 18, 2026, 8:51 AM ET
**Subject:** RE: BakePlan implementation: proposed go-live sequence

Grace,

Quick close-out note. The Corporate Offices went live yesterday as scheduled, so all five Licensed Facilities under Order Form No. 1 are now live on BakePlan, ahead of the six-month target.

As set out in Section 3.4 of the Order Form, our finance team will now issue the second fifty percent (50%) installment of the implementation fee. It will go to accountspayable@veilound.com, with a copy to you.

Thank you and the plant teams for a smooth rollout. I will set up a post-implementation review call for early September.

Best,
Tomas