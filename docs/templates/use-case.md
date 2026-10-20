---
id: UC-012
title: <Goal of the primary actor, as a short active verb phrase>
status: Draft            # Draft | Complete [R28-Q11]
driver: <name>
priority: <number or label>   # informs the pick, never makes it [R6-Q1]
source_locale: en        # en | fr [R1-Q11]
inputs: []               # input IDs it draws on: PER-, JRN-, PP-, BLK-, OBJ-, HYP-, e.g. [PER-001, BLK-003] [R3-A5, R30-Q1]
stories: []              # filled when stories are cut: [US-012.1, US-012.2]
---
<!-- Copied to docs/product/use-cases/UC-012-<slug>/use-case.md. Cockburn "fully dressed" format [R1-Q6],
     at the user-goal level only [R28-Q1]. Step and extension IDs are renumbered only with `write-use-case renumber`,
     and only until a PRD that references them reaches Design-complete; after that, add `3.1`-style IDs
     and mark removed ones `retired`, never reused [R28-Q19′]. -->

# UC-012: <title>

| Field | Value |
|---|---|
| **Primary actor** | <role> <!-- for a time-triggered use case, the stakeholder who cares that it runs, never "the clock" [R29-Q3] --> |
| **Scope** | <the system under design> |
| **Level** | User goal <!-- always: one actor, one sitting, goal reached (coffee-break test) [R28-Q1]. A step that waits hours or days for someone else or for a deadline ends the use case there [R29-Q2] --> |
| **Trigger** | <what starts it: the actor's request, or a time event such as "24 hours after a request with no approval" [R29-Q3]> |
| **Preconditions** | <what must be true before it starts> |
| **Minimal guarantees** | <what is true however it ends, e.g. nothing is half-saved, the attempt is logged> |
| **Success guarantees** | <what is true when the main scenario succeeds; if it ends at a wait point, what is pending and how the actor will hear [R29-Q2]> |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| <role> | <what they need protected or achieved> |

## Main success scenario

<!-- Intent, not interface: no screens, buttons or clicks [R28-Q7]. Mark each step (actor) or (system) [R28-Q6].
     Add a system step's duration class when it isn't instant (under 1 s) [R29-Q1]:
     wait = 1 to 10 s; long = over 10 s, the actor stays; background = minutes or more, the actor may leave.
     A background step is followed by a system step that tells the actor the outcome [R29-Q5]. -->

1. (actor) <Actor> <provides or chooses something>.
2. (system) The system <looks up, stores or calls something>.
3. (system, long) The system <does something that takes over 10 seconds, reporting progress>.
4. …

## Failure-category check

<!-- Run each step through the categories of its kind [R4-Q2, R28-Q6]. Each "yes" becomes an extension below.
     "n/a" needs no reason; "out-of-scope" does. Cancel / abandon on a system step is answered only for long and
     background steps, and is never "n/a" there: "out-of-scope" needs a reason such as "past the point of no return";
     it is "n/a" for instant and wait steps [R29-Q4]. -->

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | | | | |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | | | | | | | n/a |
| 3 | | | | | | | |

**Privacy request:** <yes / no>: <can the actor ask to export or erase the personal data this use case handles? If yes, the extension that handles it, or `deferred` with a reason>

## Extensions

<!-- ID = UC-012.<step><letter>. Each one has a handling outcome, or is marked deferred / out-of-scope with a reason [R1-Q7].
     Each handled extension has a one-line concrete example; it becomes the first Gherkin scenario in Exploring [R28-A, R28-Q3]. -->

- **UC-012.2a** <condition>:
  1. The system <handles it>.
  2. Returns to step <n> / The use case ends.

  *Example:* <a concrete instance, e.g. "Ana books room 3 for 10:00, but Ben booked it a second earlier.">
- **UC-012.3a** <condition>: `deferred`, <reason>.

## Technology and data variations

<!-- Each variation is a candidate for its own story [R28-Q8]. -->

- <step>: <variation, e.g. a room booked for a single slot or as a weekly series>

## Related information

- **Frequency:** <how often>
- **Open issues:** <questions still open>
