# Answers: enroll in a seminar

## Actor, goal and scope

- The system is the university's enrollment system, treated as a black box.
- The student starts because they want a seat in a seminar.
- Before they start, they're already registered at the university and authenticated.
- Billing isn't done by the enrollment system itself: it calls on the student billing service to bill the fees.
- It's busiest during each term's enrollment period, when every student enrolls in several seminars; the rest of the term it happens now and then.
- The confirmation can be shown to the student, sent by email or printed.
- Getting a seat from the waiting list later is a separate thing, not part of this.

## Stakeholders and guarantees

- The student wants a seat in a seminar that fits their schedule, and to know clearly what it will cost.
- The registrar wants only eligible students enrolled, and prerequisites respected.
- The bursar wants fees and taxes billed correctly.
- The instructor wants the class capacity respected.
- However it ends, a student is never enrolled without being billed, nor billed without being enrolled.
- A seminar never ends up with more students enrolled than it has seats.
- When it works: the student is enrolled in the seminar, the fees are billed through the billing service, and the student can get the enrollment confirmation.

## Main scenario

- The first thing the system checks is whether the student may enroll at all this term; there are rules for that.
- Seminars the student is already enrolled in aren't offered again, so they can't pick one twice.
- Prerequisites are set per seminar, by rule.
- Fitting the schedule means the seminar doesn't overlap a seminar already in the student's schedule.
- The fees shown include the student fees that apply and the taxes, each worked out by its own rule.
- Enrolling a student in a seminar bills its fees, by rule.

## What can go wrong

- The student isn't allowed to enroll this term.
- The student is missing a prerequisite for the seminar they chose.
- The seminar they chose overlaps one already in their schedule.
- The seminar they chose is full.
- The student doesn't find a seminar that suits them.
- The student doesn't accept the fees.
- Someone else takes the last seat between the fees being shown and the student confirming.
- The billing service doesn't answer, or the enrollment goes through but the billing doesn't, or the other way round.

## How each is handled

- Not allowed to enroll: the system explains why, and it stops there.
- Missing prerequisite: the system lists what's missing, and the student picks a seminar again.
- Schedule overlap: the system shows the seminar it clashes with, and the student picks again.
- Seminar full: the system offers its waiting list, plus the other sections of that seminar that still have a seat. The student can pick another section or seminar. Or they join the waiting list: they're put on it and told they'll be notified when a seat frees up, and that's the end of it for now; they're neither enrolled nor billed.
- No suitable seminar, or fees declined: nothing is enrolled or billed, and it stops.
- Last seat taken meanwhile: nothing is enrolled or billed, the system says the seminar is now full, and it goes on exactly as for a full seminar.
- Billing service down, or only half of it went through: the system undoes whichever part succeeded so the student is neither enrolled nor billed, tells them it didn't work, and keeps their choice so they can try again or give up.

## Durations

- Checking eligibility and listing the seminars is immediate.
- Checking prerequisites, schedule and seats, and working out the fees, is immediate.
- Enrolling and billing takes a few seconds, because it goes through the billing service; the student waits for the confirmation.

## Out of scope

- Exporting or erasing a student's enrollment and billing records: that's a separate job, and the university has to keep some of those records anyway.
