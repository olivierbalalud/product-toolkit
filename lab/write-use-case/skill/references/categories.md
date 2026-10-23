# Failure categories and the grid

Read during step 5, and during the interview when you propose conditions (topic 4). Examples are from a meeting room booking product, using this scenario:

1. (actor) The organiser asks for a room for a slot and a number of attendees.
2. (system) The system presents the free rooms that fit.
3. (actor) The organiser chooses a room.
4. (system, wait) The system holds the room, sends the invitations through the calendar service and confirms the booking.

## Cell values

| Value | Means | Example |
|---|---|---|
| `yes: UC-012.3a` | The condition can arise at this step and is handled; name every extension that answers it, comma-separated | `yes: UC-012.4a, UC-012.4b` |
| `n/a` | The condition can't arise here, or there is nothing to enforce (no limit, no content rules). Bare: no reason | `n/a` |
| `out-of-scope: <reason>` | It can arise, and the driver decided it isn't handled here | `out-of-scope: deleting a room is the facilities manager's use case, which decides what happens to its bookings` |

IDs with `*` go in backticks: `` yes: `UC-012.*a` ``.

## Actor-step categories

| Category | Ask | Example condition | Typically `n/a` when |
|---|---|---|---|
| **Invalid input** | Can what the actor gives be unusable or break a rule? | 1a: the slot is longer than four hours (BR-1); the slot is in the past | The step only confirms or asks; there are no rules on the input |
| **Duplicate** | Can the same thing be given or submitted twice, or already exist? | 1b: the organiser already has a booking for an overlapping slot | Repeating is harmless and creates nothing twice |
| **No permission** | Can this actor be refused here? | 3a: the room is reserved for the board, and the organiser isn't on it | Anyone who meets the preconditions may do it |
| **Cancel / abandon** | Can the actor give up or walk away here? | `UC-012.1-3a`: the organiser gives up before choosing; nothing is held | Rarely; after the point of no return it is `out-of-scope` |

## System-step categories

| Category | Ask | Example condition | Typically `n/a` when |
|---|---|---|---|
| **Not found** | Can what the step looks up be missing? | 2a: no free room fits the slot and attendees | The step creates rather than looks up |
| **Conflict / concurrent edit** | Can someone else change the same thing at the same time? | 4a: another organiser booked the room a second earlier | Nobody else can touch it, or the outcome is the same either way |
| **Timeout / external down** | Does the step call an outside system that can fail or be slow? | 4b: the calendar service does not answer within 10 seconds | No outside system is called |
| **Partial failure** | Can the step do part of its work and fail on the rest? | 4c: the room is held but the invitations can't be sent | The step does one indivisible thing |
| **Quota / limit** | Can a limit be reached (a plan, a capacity, a count)? | 4d: the organiser already holds the maximum of ten future bookings (BR-2) | No limit exists |
| **Stale data** | Can what the actor saw have changed since it was shown? | 4a again: the room shown as free at step 2 was taken | Nothing shown earlier is relied on |
| **Cancel / abandon** | Only for `long` and `background` steps: can the actor stop it while it runs? | 5a: the organiser cancels the import of 2,000 bookings at 30% | Always `n/a` on instant and `wait` steps |

## Keying: which step a condition belongs to

- **Invalid input is keyed to the actor step that provides the input**, even when a later system step detects it. That system step answers `n/a` for it, and never cites it from another column (a file over the size limit is the actor's invalid input, not the reading step's quota).
- A condition detected *during* a `long` or `background` step belongs to that step.
- A condition that recurs at another step with the **same** handling: that step's cell names the first extension. With **different** handling (a deadline passing between choosing and confirming, when nothing is stored at confirmation): its own extension there.
- A condition that can occur at **every** step: `UC-012.*a`. Over **part** of the scenario: a range, `UC-012.1-3a` ("any time before the booking is held"). Abandoning stops being possible once the work is stored, so it is usually a range.
- A permission checked "up front, when the actor asks" is keyed to the actor's request step, not to a later step.
- A wrong choice the actor corrects before confirming is an alternative: an extension no cell names, not invalid input.
- A failure that fits no category (the actor's device crashes) is still an extension; no cell names it, and it is keyed to the step where it happens.

## Never invent

- A cell is `yes` only for a condition the inputs or the driver confirmed. Plausible but unconfirmed is `n/a` and a line in the report.
- Don't cite an extension just to fill a cell: only one whose handling answers that condition, unchanged.
- An alternative that isn't a failure (several identical items, a preview) is not a "duplicate" or "invalid input".

## Privacy request

Answered once per use case, as a line after the grid:

- `**Privacy request:** yes: UC-012.5a` when this use case handles the request itself.
- `` **Privacy request:** yes: `deferred`, exporting or erasing an organiser's booking history is a separate account privacy use case. `` when the use case handles personal data and the request belongs elsewhere. This is the usual answer.
- `**Privacy request:** no: the use case handles no personal data.` only when that is true. Names on a booking, attendee lists and history are personal data.
