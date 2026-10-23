# Use case quality: 15 criteria and the interview rules

Read during step 3 (to pick and phrase questions) and step 8 (to check the result). Condensed from Cockburn, *Writing Effective Use Cases*, Larman, *Applying UML and Patterns* ch. 6, and Adolph & Bramble, *Patterns for Effective Use Cases*. Examples are from a meeting room booking product.

Each criterion has a **test** (pass or fail), the **question** to ask when it fails with a recommended answer, and a **bad** and a **good** line. **Form** criteria (Q6, Q7, Q9, Q10) are fixed without asking. **Content** criteria are asked about, one question per failing criterion.

Contents: [Interview rules](#interview-rules) · [Goal and boundary Q1–Q5](#goal-and-boundary) · [Main scenario Q6–Q10](#main-scenario) · [Extensions Q11–Q14](#extensions) · [The whole Q15](#the-whole-use-case)

## Interview rules

- **Ask in order of precision:** actor and goal (Q1–Q2), stakeholders and guarantees (Q3–Q5), the main scenario (Q6–Q10), the full list of conditions (Q11–Q12), and only then the handling (Q13–Q14). Draft the whole list of conditions before working out how each is handled: people who start on the handling run out of energy before the list is complete.
- **One failing criterion, one question**, phrased as below, with its recommended answer.
- **Spend questions on content, not form.** The questions worth asking are Q1, Q3, Q11 and Q13. Q6, Q10 and most of Q7 are fixed silently.
- **Don't ask what the inputs already answer.** A question whose answer is in an input, the notes or the glossary is a defect of the interview.

## Goal and boundary

### Q1. One user goal, held by the primary actor (content)

- **Test:** The title is an active verb phrase naming what the primary actor wants. The main scenario delivers exactly that, in one sitting, and nothing else of comparable size. The primary actor has behaviour and a goal; it is not the system or a timer.
- **Ask:** "When this ends well, what does the organiser walk away with? Is that one thing?" *Recommended:* the smallest outcome the actor would report as a day's work.
- **Bad:** "Room management"; "Book and cancel rooms"; primary actor "the scheduler".
- **Good:** "Book a room for a meeting" (organiser); "Release unconfirmed bookings" (facilities manager, triggered by time).

### Q2. The scope is a black box with a visible edge (content)

- **Test:** Steps name what the system does, not its parts. Anything the system calls on is a supporting actor. The team would build everything in Scope and nothing outside it.
- **Ask:** "Is the calendar something we build, or something we call?" *Recommended:* outside, a supporting actor, unless the team owns it.
- **Bad:** "The booking service writes the reservation to the database and publishes an event."
- **Good:** "The system holds the room for the slot." / "The system asks the calendar service to send the invitations."

### Q3. Stakeholder interests drive the content (content)

- **Test:** Each listed interest is protected somewhere: a step, an extension, a guarantee, or a stated out-of-scope. No stakeholder is listed without consequence. Off-stage stakeholders have been considered (whoever pays for empty rooms, whoever answers for personal data).
- **Ask:** "Who loses if this goes wrong and isn't in the room? What would they insist on?" *Recommended:* name the interest, then the step or guarantee that protects it.
- **Bad:** Stakeholders: "Organiser: wants to book a room." (and nothing else)
- **Good:** "Facilities manager: rooms aren't left empty by no-shows" → success guarantee "the booking is unconfirmed until check-in". "Data protection officer: attendee names kept only as long as the booking" → privacy-request line.
- The report lists each interest with what protects it, or flags it as unprotected.

### Q4. Guarantees are states someone could check (content)

- **Test:** The success guarantee says what is true in the world afterwards (what is recorded, who knows), not a feeling or a restatement of the steps. The minimal guarantee says what is protected on *every* exit. The main scenario ends exactly where the success guarantee becomes true.
- **Ask:** "If someone looked at the system right after success, what would they find?" *Recommended:* one sentence per stakeholder whose interest is satisfied.
- **Bad:** Success guarantee "The booking works."
- **Good:** "The room is held for the slot in the organiser's name, and the invitees have the invitation." Minimal: "No booking is half-saved; every attempt is logged with the organiser and slot."

### Q5. Preconditions are assumptions, never re-checked (content)

- **Test:** Each precondition is put in place by another use case, and the scenario never checks it. Anything the scenario checks is an extension. `None` is better than filler.
- **Ask:** "Does the system verify this during the use case? Then it's an extension." *Recommended:* move it to an extension on the step that checks it.
- **Bad:** Precondition "The room is free" (then step 3 checks availability); "The system is running".
- **Good:** "The organiser is signed in." Availability is extension 3a.

## Main scenario

### Q6. Each step has one subject and shows who has the ball (form)

- **Test:** Every step is one simple sentence, subject–verb–object, whose subject is a named actor. No passive voice, no step where two actors act.
- **Fix:** rewrite it. Ask only if the actor is genuinely unclear: "Who does this, the organiser or the system?"
- **Bad:** "The room is selected and confirmed."
- **Good:** "2. (actor) The organiser chooses a room." "3. (system) The system confirms the room is free for the slot."

### Q7. Steps state intent, not interface or technology (form)

- **Test:** No screens, controls, gestures, navigation or layout, including words the script's warning list misses ("drags", "dropdown", "opens the settings page"). No technology choices.
- **Fix:** rewrite as intent. Ask only if the intent can't be inferred: "What is the organiser trying to achieve with that click?"
- **Bad:** "The organiser opens the calendar view, drags across 10:00–11:00 and clicks Book."
- **Good:** "The organiser asks for a room for Tuesday 10:00–11:00."

### Q8. Every step moves the goal forward, one level down (content)

- **Test:** Removing any step would lose something a stakeholder needs. No step is pure display, waiting or bookkeeping. Each step is just below the use case's goal: not a sub-sub-step ("types the date"), not a goal of the same size ("organises the meeting"). 3 to 9 steps, counted after bundling system actions that share a duration class.
- **Ask:** "If we dropped this step, who would notice?" *Recommended:* merge it into its neighbour or drop it.
- **Bad:** "4. The system shows a loading indicator." "5. The organiser reviews the details." "2. The system checks that the organiser may book and asks for the slot."
- **Good:** "4. (system) The system holds the room and sends the invitations."

### Q9. Information passed is named, at the right precision (form)

- **Test:** Each actor step names the information given, by nickname ("the slot", "the attendees"). Not "the details", and no fields, formats or lengths, which belong to the glossary or the data rules. A rule the system enforces is named where it bites, by reference.
- **Fix:** name two to four nicknames; move field rules to the glossary or a business rule.
- **Bad:** "The organiser enters the details." / "The organiser enters a title (max 80 characters), a start time (HH:MM)…"
- **Good:** "The organiser gives the slot, the expected attendees and any equipment needed." "The system applies the booking policy (BR-1)."

### Q10. The scenario validates; it does not branch (form)

- **Test:** No "if", "otherwise", "check whether" in the main scenario. A check is the system validating; its failure is an extension on that step.
- **Fix:** move the branch to an extension.
- **Bad:** "3. The system checks whether the room is free. If so it books it, otherwise it shows an error."
- **Good:** "3. (system) The system confirms the room is free for the slot." / "3a. The room is booked for an overlapping slot: …"

## Extensions

### Q11. Conditions are what the system detects and must handle (content)

- **Test:** Each condition is something the system (or an actor) can observe at that step, and the system has to respond. Not an inference, a cause it can't see, or an inner state. A `yes` cell whose condition the system can't detect is `n/a`. No cell needs an invented condition.
- **Ask:** "At that step, what exactly does the system see?" *Recommended:* the observable symptom, not its cause.
- **Bad:** "3a. The organiser changes their mind." "4a. The network is slow." "4b. The calendar service has a bug."
- **Good:** "2a. The organiser abandons the request." "4a. The calendar service does not answer within 10 seconds."

### Q12. The extension list is rationalised (content)

- **Test:** No two extensions on the same step have the same handling under different wording; they are merged. Low-level failures are rolled up into what the actor experiences. A condition at many steps is written once (`*a` for every step, `3-6a` for a range), and other cells name it. Conditions with different handling or a different return point stay separate.
- **Ask:** "Does the system do anything different in these cases? If not, they are one condition." *Recommended:* merge, in the wording the actor would recognise.
- **Bad:** "3a. The room was deleted." "3b. The room was archived." "3c. The room ID is unknown." (same handling)
- **Good:** "3a. The room no longer exists: …"

### Q13. Handling is decided behaviour with a clear ending (content)

- **Test:** Each handled extension says what the system does, not only that it reports a problem, and where it goes next: back to a named step, to another extension, or to the end with the minimal guarantee honoured. "The system shows an error" alone fails.
- **Ask:** "After that, what can the organiser do, and what does the system keep?" *Recommended:* the most helpful recovery the business accepts, and where it rejoins.
- **Bad:** "3a. The room is taken: the system shows an error."
- **Good:** "3a. The room was booked for an overlapping slot meanwhile: 1. The system offers the nearest free room in the same building for the slot. 2. Returns to step 2."

### Q14. Examples are concrete and add information (content)

- **Test:** Each example names a specific actor, value and moment, and would read as a test scenario. It doesn't restate the condition.
- **Ask:** "Give me one real instance: who, which room, what time?" An extension nobody can give an example for is not understood yet.
- **Bad:** "*Example:* the room is unavailable."
- **Good:** "*Example:* Ana asks for room 3 on Tuesday at 10:00; Ben booked it at 09:59."

## The whole use case

### Q15. Variations are "how", not "what" (content)

- **Test:** Each technology and data variation changes how a step is done, not what happens. A different outcome is an extension.
- **Ask:** "Does the outcome change, or only the means?" *Recommended:* outcome changes → extension.
- **Bad:** Variation "2: booking fails if the room is full."
- **Good:** "2: the organiser finds the room by name, on the floor plan, or by the code on the door."

**Not scored here.** Cockburn's last tests are for people: "Is this what you want?", "Will you be able to tell, upon delivery, whether you got this?", "Can you implement this?". They belong to the driver's sign-off on the use case PR.
