- **ID / Name:** UC-17 — Enroll in Seminar
- **Scope:** University enrollment system (black box) · **Level:** User goal (!)
- **Primary actor:** Student
- **Supporting actor:** Student billing service
- **Stakeholders & interests:**
  - Student — gets a seat in a seminar that fits their schedule, with clear fees.
  - Registrar — only eligible students are enrolled; prerequisites are respected.
  - Bursar — fees and taxes billed correctly.
  - Instructor — class capacity respected.
- **Trigger:** Student wants to enroll in a seminar.
- **Preconditions:** Student is registered at the university and authenticated.
- **Minimal guarantees** *(added)*: A student is never enrolled without being billed, nor billed without being enrolled; seminar capacity is never exceeded.
- **Success guarantees:** Student enrolled in the seminar; fees billed; enrollment confirmation available to the Student.

**Main success scenario**
1. Student asks to enroll in a seminar.
2. System verifies the Student may enroll this term (BR129) and presents the available seminars.
3. Student chooses a seminar.
4. System verifies the prerequisites (BR130) and that the seminar fits the Student's schedule (BR143).
5. System presents the fees, including applicable student fees and taxes (BR180, BR45).
6. Student confirms the enrollment.
7. System enrolls the Student, bills the fees (BR100) and confirms the enrollment.

**Extensions**
- 2a. Student is not eligible to enroll: System explains why; use case ends.
- 3a. Student finds no suitable seminar: use case ends.
- 4a. Prerequisites missing: System lists the missing prerequisites; continue at step 3.
- 4b. Schedule conflict *(added)*: System shows the conflicting seminar; continue at step 3.
- 4c. Seminar is full *(added)*: System offers the waiting list or another section; continue at step 3.
- 6a. Student declines the fees: use case ends.

**Technology & data variations:** confirmation shown on screen, emailed or printed.
