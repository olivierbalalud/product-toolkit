# Cockburn's fully dressed use case: fields and goal levels

Read during step 2, or whenever a field's meaning is unclear. Examples are from a meeting room booking product.

## Goal levels

Cockburn sorts goals by level. This framework writes use cases at **one** level only: the user goal.

| Level | Test | Example | What to do with it |
|---|---|---|---|
| Summary ("kite") | Spans many sittings, often several actors or days | "Manage the office's meeting rooms" | Write a short map: the user-goal use cases it groups, in time order, with the waits between them. No fields, no grid, no stories. |
| **User goal ("sea level")** | One primary actor, one sitting (2 to 20 minutes), leaves with the goal reached | "Book a room for a meeting" | A use case. |
| Subfunction ("fish") | Nobody would stop after doing only this | "Enter the date", "Sign in", "Look up a room" | A step (or part of one) in the use case that needs it. Never a use case of its own. |

**Coffee-break test.** After doing it, would the actor take a coffee break and say "I booked the room"? If they would only say "I entered a date", it is a subfunction. If they'd need to come back tomorrow, it is a summary, or the use case hides a wait point.

**Asking "why?" moves up a level; asking "how?" moves down.** "Why does the organiser enter a date?" → to book a room (user goal). "How does the organiser book a room?" → the steps.

**Informal use cases often hide several use cases:**

- Two actors with a wait between them ("the organiser requests a large room; facilities approves it"): split at the wait. The request ends at "sent"; approving is facilities' own use case.
- One version per technical option ("book via the web", "book via the calendar plug-in"): write it once; the options are variations of a step, and the choice between technologies is an ADR.
- A login, onboarding or setup flow written as a use case: a subfunction or a precondition.

## The fields

| Field | What goes in it | Good | Bad |
|---|---|---|---|
| **Title** | The primary actor's goal, as a short active verb phrase | "Book a room for a meeting" | "Room booking module"; "Book and cancel rooms" (two goals) |
| **Primary actor** | The role whose goal this is: someone with behaviour the system serves. For a use case started by time, the stakeholder who cares that it runs. | "Organiser (an employee)"; "Facilities manager" for a nightly release of unconfirmed bookings | "The scheduler"; "The system"; "The clock" |
| **Supporting actors** | Outside systems or people a step calls on, or `None` | "Calendar service (sends the invitations)" | The actor's own browser or messaging app; a part of the system under design |
| **Scope** | The system under design, as a black box: everything the team builds and nothing it calls | "Room booking service" | "The booking microservice and its database" |
| **Level** | Always `User goal` | | |
| **Trigger** | What starts it: the actor's intent or request, or a time event | "The organiser needs a room for a meeting"; "Every night at 02:00" | "The organiser clicks New booking" |
| **Preconditions** | What another use case guarantees before this one starts, never checked again in the scenario; or `None` | "The organiser is signed in." | "The room is free" (the scenario checks that: it's an extension); "The system is running" (filler) |
| **Minimal guarantees** | What is true however it ends: what is protected on every exit | "No booking is half-saved; the room is never held without a booking." | "Errors are handled." |
| **Success guarantees** | The state of the world when the main scenario succeeds: what is recorded, who knows. At a wait point, what is pending and how the actor will hear | "The room is held for the slot in the organiser's name, and the invitees have the invitation." | "The booking works."; a replay of every step |

## Stakeholders and interests

A stakeholder is anyone with an interest in how the use case behaves, including people who are not there: whoever pays for empty rooms, whoever answers for personal data. Each interest must be protected somewhere: a step, an extension, a guarantee, or a stated out-of-scope. A stakeholder whose interest nothing protects is either missing behaviour or doesn't belong in the table.

| Stakeholder | Interest | Protected by |
|---|---|---|
| Organiser | Gets a suitable room without double-checking the calendar | Steps 2 to 4 |
| Facilities manager | Rooms aren't left empty by no-shows | Success guarantee: the booking is unconfirmed until check-in |
| Invitees | Hear about the meeting in time | Step 4 (invitations) |

## Main success scenario

The one path where everything goes right, in 3 to 9 steps, each marked `(actor)` or `(system)` and each stating intent:

1. (actor) The organiser asks for a room for a slot and a number of attendees.
2. (system) The system presents the free rooms that fit, nearest first.
3. (actor) The organiser chooses a room.
4. (system) The system holds the room for the slot, sends the invitations through the calendar service and confirms the booking.

The scenario ends exactly where the success guarantee becomes true.

## Extensions

Everything else: failures and alternatives, keyed to the step where they are detected (`UC-012.3a`), to a range (`UC-012.2-3a`) or to every step (`UC-012.*a`). Each has a condition, handling, an ending (returns to a step, continues as another extension, or ends), and a one-line example.

## Technology and data variations

How a step may be done differently with the same outcome: "2: the organiser finds the room by name, on the floor plan, or by the code on the door." A different outcome is an extension. Each variation is a candidate for its own story.

## Related information

- **Frequency:** how often it happens ("about 200 bookings a day, peaking at 09:00").
- **Business rules:** policies the steps cite by ID: "BR-1 a booking lasts at most four hours (step 1, UC-012.1a)".
- **Related use cases:** by goal: continuations after a wait point, time-triggered follow-ups, separate tasks ("Cancel a booking", "Release unconfirmed bookings").
- **Open issues:** only what the driver left open; otherwise `None`.
