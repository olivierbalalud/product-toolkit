# Durations, wait points and time triggers

Read during steps 2 to 4. Examples are from a meeting room booking product.

## Duration classes

Every system step has a duration class: what the actor experiences in normal use. It is an order of magnitude that changes what the actor can do (wait, cancel, leave), not a performance target.

| Class | Mark | Takes | The actor | The grid adds |
|---|---|---|---|---|
| instant | `(system)` (default, not written) | under 1 s | doesn't notice | nothing |
| wait | `(system, wait)` | 1 to 10 s | waits on the spot | nothing; cancel is `n/a` |
| long | `(system, long)` | over 10 s | stays and watches progress, may give up | cancel: `yes` or `out-of-scope` with a reason, never `n/a` |
| background | `(system, background)` | minutes or more | may leave | cancel as for long; the next step tells the actor the outcome |

Examples:

- "The system presents the free rooms" — instant.
- "The system checks the attendees' calendars through the calendar service and proposes three slots" — `wait`, if the calendar service takes a few seconds.
- "The system imports the 2,000 bookings from the old tool, showing progress" — `long`.
- "The system recalculates the occupancy report for the past year" — `background`, followed by "(system) The system notifies the facilities manager that the report is ready."

**Rules.**

- Ask the driver when unsure. A slow lookup that *should* be instant is instant.
- One system step may bundle several actions while they share a class. An instant or `wait` step includes its own response. After a `long` or `background` step, the outcome is its own step.
- A `background` step is never the last step and is never followed directly by an actor step: a system step that tells the actor the outcome comes next.
- A size-dependent step (a few rows in seconds, thousands in minutes) takes the class of the normal large case the actor must be able to cancel: usually `long`.
- Extensions that happen *during* a `long` or `background` step (the actor cancels, the service fails half-way) are keyed to that step.
- An extension on a `background` step says how the actor, who may have left, learns of it ("the system emails the facilities manager that the report failed").
- A step whose time goes into sending the actor's data (an upload) is `long`; cancelling aborts the transfer.

## Wait points

All steps of one scenario share one level of duration: "you don't have a one-month process followed by a five-minute step". A step that waits hours or days for another person, an outside party or a deadline is a **wait point**, and the use case ends there.

| Signal in the inputs | Example | What to do |
|---|---|---|
| Another person acts after the actor | "Facilities approves the large-room request" | End at "the request is sent". Approving is facilities' use case. |
| Someone accepts later | "The invitee accepts the shared booking" | End when the invitation is sent. Accepting is the invitee's use case. |
| An outside party answers later | "The catering supplier confirms the order within a day" | End when the order is sent. The supplier's answer starts its own use case. |
| A deadline must pass | "Unconfirmed bookings are released 15 minutes after the start" | A separate, time-triggered use case. |

At a wait point:

- the success guarantee says what is pending and how the actor will hear: "The request is pending facilities' approval; the organiser is notified of the decision."
- the continuation is named under Related use cases ("Approve a large-room request").
- the scenario has no step after the hand-over: no "waits for", no "approves".

**Waits inside extensions.** An extension whose handling waits for someone else or a deadline (joining a waiting list for a room, asking an administrator for access, a supplier that defers its answer) ends the use case there in the same way: it says what is pending and how the actor will hear, and the continuation is its own use case.

**Not a wait point.** An actor pausing *their own* work (leaving a half-finished booking to find the attendee list) is *cancel or abandon*, handled as discard or save-and-resume.

## Time triggers

A use case may be started by time: "every night at 02:00", "15 minutes after a booking's start without check-in".

- `Trigger` names the time event.
- The primary actor is the stakeholder who cares that it runs (the facilities manager who wants empty rooms released), never "the clock" or "the system".
- Such a use case often has only system steps; the grid applies as usual.

Example: **Release unconfirmed bookings.** Primary actor: facilities manager. Trigger: 15 minutes after a booking's start, with no check-in. Steps: (system) The system releases the room and records the no-show. (system) The system tells the organiser the booking was released.
