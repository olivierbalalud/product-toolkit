---
id: UC-005
title: Enroll in a seminar
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-005: Enroll in a seminar

| Field | Value |
|---|---|
| **Primary actor** | Student |
| **Supporting actors** | Student billing service (bills the fees) |
| **Scope** | University enrollment system |
| **Level** | User goal |
| **Trigger** | The Student wants to enroll in a seminar. |
| **Preconditions** | The Student is registered at the university and authenticated. |
| **Minimal guarantees** | A Student is never enrolled without being billed, nor billed without being enrolled; a seminar never has more students enrolled than it has seats. |
| **Success guarantees** | The Student is enrolled in the seminar; the fees are billed through the Student billing service; the enrollment confirmation is available to the Student. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Student | Gets a seat in a seminar that fits their schedule, with clear fees. |
| Registrar | Only eligible students are enrolled; prerequisites are respected. |
| Bursar | Fees and taxes are billed correctly. |
| Instructor | Class capacity is respected. |

## Main success scenario

1. (actor) The Student asks to enroll in a seminar.
2. (system) The system verifies that the Student may enroll this term (BR-1) and presents the seminars available to the Student.
3. (actor) The Student chooses a seminar.
4. (system) The system verifies the prerequisites (BR-2), that the seminar fits the Student's schedule (BR-3) and that it has a free seat, and presents the fees, including the applicable student fees and taxes (BR-4, BR-5).
5. (actor) The Student confirms the enrollment.
6. (system, wait) The system enrolls the Student, bills the fees through the Student billing service (BR-6) and confirms the enrollment.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | yes: UC-005.2a | n/a |
| 3 | yes: UC-005.3a, UC-005.3b | n/a | n/a | yes: UC-005.3-5a |
| 5 | n/a | n/a | n/a | yes: UC-005.3-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-005.4a | n/a | n/a |
| 6 | n/a | yes: UC-005.6a | yes: UC-005.6b | yes: UC-005.6b | yes: UC-005.6a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a Student's enrollment and billing records is its own use case, and the records the university must keep limit what can be erased.

## Extensions

- **UC-005.2a** The Student may not enroll this term (BR-1):
  1. The system explains why the Student may not enroll.
  2. The use case ends.

  *Example:* Omar asks to enroll for the spring term while his registration is suspended for an unpaid fee; the system tells him so and enrolls him in nothing.
- **UC-005.3a** The Student lacks prerequisites for the chosen seminar (BR-2):
  1. The system lists the missing prerequisites.
  2. Returns to step 3.

  *Example:* Lina chooses Advanced Statistics, which requires Statistics 1; she has not passed it, so she chooses Statistics 1 instead.
- **UC-005.3b** The chosen seminar overlaps a seminar already in the Student's schedule (BR-3):
  1. The system shows the conflicting seminar.
  2. Returns to step 3.

  *Example:* Lina chooses Modern Poetry on Tuesdays 14:00–16:00, which overlaps her Linguistics seminar at 15:00, so she chooses the Thursday section instead.
- **UC-005.4a** The chosen seminar is full:
  1. The system says the seminar is full and offers its waiting list and the other sections of the seminar that have a free seat.
  2. The Student chooses another section or another seminar: returns to step 3.
  3. Or the Student joins the waiting list: the system records the Student on it and says the Student will be notified when a seat becomes free; the use case ends with the Student neither enrolled nor billed.

  *Example:* Sara chooses section B of Organic Chemistry, whose 30 seats are all taken; she joins its waiting list and is told she will be notified if a seat becomes free.
- **UC-005.3-5a** The Student stops without enrolling: no seminar suits them, or they decline the fees:
  1. The system enrolls and bills nothing.
  2. The use case ends.

  *Example:* Jonas sees that the fees for Film Studies include a 120 € materials fee, declines them and leaves without enrolling.
- **UC-005.6a** The last seat was taken after the fees were presented:
  1. The system enrolls and bills nothing and says the seminar is now full.
  2. Continues as in UC-005.4a.

  *Example:* Sara and Tom both see the last seat in section A of Organic Chemistry; Tom confirms first, so Sara is told the section is full and offered its waiting list.
- **UC-005.6b** The Student billing service does not answer, or only one of enrolling and billing succeeds:
  1. The system reverses whichever of the enrollment and the billing succeeded, so the Student is neither enrolled nor billed.
  2. The system tells the Student the enrollment was not made and keeps the Student's choice.
  3. The Student tries again: returns to step 6. Or the Student stops: the use case ends.

  *Example:* Lina confirms Statistics 1 at 9:02 while the billing service is down; she is neither enrolled nor billed, and her retry at 9:10 succeeds.

## Technology and data variations

- 6: the confirmation is shown to the Student, sent by email, or printed.

## Related information

- **Frequency:** peaks during each term's enrollment period, when each Student enrolls in several seminars; occasional during the rest of the term.
- **Business rules:** BR-1 who may enroll in a given term (step 2, UC-005.2a) · BR-2 a seminar's prerequisites must be met (step 4, UC-005.3a) · BR-3 a seminar may not overlap a seminar already in the Student's schedule (step 4, UC-005.3b) · BR-4 the student fees that apply to a seminar (step 4) · BR-5 the taxes on seminar fees (step 4) · BR-6 enrolling in a seminar bills its fees (step 6, UC-005.6b).
- **Related use cases:** Enroll from the Waiting List.
- **Open issues:** None
