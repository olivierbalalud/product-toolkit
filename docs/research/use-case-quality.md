# Use Case Quality: a Rubric

Status: fact check, 2026-10-22 (curl and PDF reading of the sources below, WebFetch, WebSearch). Input to [`write-use-case`](../skills/write-use-case.md): its `references/quality.md`, the LLM grader of its evals, and the questions its interview asks. The driver settled the four tensions in §5 on 2026-10-22; they are recorded as round 31 of the [grilling log](../grilling-log.md) (R31-Q1 to R31-Q4), and the guide, the spec, the templates and the other skill specs were updated on 2026-10-23. "(inferred)" marks a point paraphrased from a title or summary rather than read in full.

**Why this exists.** `check_grid.py` checks that a use case is *complete*: every cell answered, every `yes` extended, every extension exemplified [R4-Q2, R28-Q3]. It does not check that the use case is *good*. A use case can pass every mechanical item and still have a goal that is really two goals, conditions the system cannot detect, a success guarantee that guarantees nothing, or steps that describe a screen. Spec §7 leaves these to the model with no criteria. This rubric supplies them.

**How to read it.** Each criterion has a pass/fail **test** an LLM judge can apply, the **question** the interview asks when the test fails, with a recommended answer, a **bad** and a **good** line in the meeting room booking domain, its **sources**, and what `check_grid.py` already covers. Criteria are ordered by the cost of getting them wrong, which is also the order the interview asks in (§6).

## Sources

| Id | Source |
|---|---|
| C1 | Cockburn, *Writing Effective Use Cases*, pre-publication draft #3 (2000-02-21), course-hosted extract: endpapers (Reminders, The Writing Process, **Pass/Fail Tests for Use Case Fields**, questions 1–31), table of contents with guideline titles, chapters 1–5 in part, chapter 12. <https://www.ifi.uzh.ch/dam/jcr:00000000-25a0-3d08-0000-00000ce96422/weuc_extract.pdf>; endpapers also at <https://courses.cs.duke.edu/compsci308/spring23/readings/cockburn_use_cases.pdf> |
| C2 | Larman, *Applying UML and Patterns*, 3rd ed., chapter 6 "Use Cases", from the author's site. <https://www.craiglarman.com/wiki/downloads/applying_uml/larman-ch6-applying-evolutionary-use-cases.pdf> |
| C3 | Adolph, Bramble, Cockburn, Pols, *Patterns for Effective Use Cases* (2002), table of contents (pattern names and pages). <https://www.informit.com/store/patterns-for-effective-use-cases-9780201721843>; grouping cross-checked on Mayflower GmbH's slides, <https://www.slideshare.net/slideshow/patterns-for-effective-use-cases/3205531> |

- C1 is a draft; the 2001 book may word things differently. The pass/fail tests are quoted from its endpaper. Guideline contents beyond their titles (chapters 7–8) were not in the extract: where a criterion relies on a title only, it says "(inferred)".
- C3's pattern bodies were not available (O'Reilly returned 403; no free copy). Only names are cited, as pointers.
- Not used: Use-Case 2.0 (slicing, not writing quality; already in [`pm-lens.md`](../foundations/pm-lens.md)); a Wiegers use case checklist (none found at a primary source).

**What the sources agree on.** Cockburn frames quality as fitness for purpose ("Sufficient is fine", C1 ch. 1) and separates *technique*, *project standards* and *quality*. Larman's chapter says it is "based on and consistent with" Cockburn's book. Adolph & Bramble turn the same guidance into patterns, described as "signs of quality" (C3 publisher description). There is one canon; the sources differ in emphasis, not in substance.

## 1. Goal and boundary

Wrong here, everything below is wasted (C1 §1.5: "If you happen to be wrong ... with your original, low-precision statement of goals, then the energy put into the high-precision description is wasted").

### Q1. One user goal, held by the primary actor

- **Test:** The title is an active verb phrase naming what the primary actor wants. The main success scenario delivers exactly that, in one sitting, and nothing else of comparable size. The primary actor is someone with behaviour and a goal the system can serve, not the system or a timer.
- **Ask when it fails:** "When this ends well, what does the organiser walk away with? Is that one thing?" *Recommended:* the smallest outcome the actor would report as a day's work.
- **Bad:** "Room management"; "Book and cancel rooms"; primary actor "the scheduler".
- **Good:** "Book a room for a meeting" (organiser); "Release unconfirmed bookings" (facilities manager, triggered nightly) [R29-Q3].
- **Sources:** C1 tests 1, 2, 6–9; C1 §5.1 coffee-break test ("One person, one sitting (2-20 minutes)"); C2 §6.16 Boss, EBP and Size tests; C3 CompleteSingleGoal, IntentionRevealingName.
- **`check_grid.py`:** the `Level` field only. Whether the goal *is* at that level is judgement [R28-Q1].

### Q2. The scope is a black box with a visible edge

- **Test:** Steps name what the system does, not its parts. Anything the system calls on (a calendar service, a badge system) is a supporting actor, named as such. The designers would have to build everything in Scope and nothing outside it.
- **Ask when it fails:** "Is the calendar something we build, or something we call?" *Recommended:* outside, a supporting actor, unless the team owns it.
- **Bad:** "The booking service writes the reservation to the database and publishes an event."
- **Good:** "The system holds the room for the slot." / "The system asks the calendar service to send the invitations."
- **Sources:** C1 tests 4, 5; C1 §3.2 (a scope mistake can cost "a factor of two or more in cost"); C2 §6.13 black-box style; C3 VisibleBoundary.
- **`check_grid.py`:** none.

### Q3. Stakeholder interests drive the content

- **Test:** Each listed interest is protected somewhere: a step, an extension, a guarantee, or a stated out-of-scope. No stakeholder is listed without consequence. Off-stage stakeholders have been considered (whoever pays for empty rooms, whoever answers for personal data).
- **Ask when it fails:** "Who loses if this goes wrong and isn't in the room? What would they insist on?" *Recommended:* name the interest, then the step or guarantee that protects it.
- **Bad:** Stakeholders: "Organiser: wants to book a room." (and nothing else)
- **Good:** "Facilities manager: wants rooms not left empty by no-shows" → minimal guarantee "an unconfirmed booking can be released"; "Data protection officer: wants attendee names kept only as long as the booking" → privacy-request line.
- **Sources:** C1 tests 12–14; C1 §2.2 ("The use case ... captures *all and only* the behaviors related to satisfy the stakeholders' interests"); C1 §4.1 (missed interests resurfaced as change requests); C2 §6.9 ("Stakeholders and Interests List — Important!").
- **`check_grid.py`:** none. The grid runs over steps, never over interests. The skill's report lists each interest with the step, extension or guarantee that protects it, so a reviewer sees the gaps (T4).

### Q4. Guarantees are states someone could check

- **Test:** The success guarantee says what is true in the world afterwards (what is recorded, who knows), not a feeling ("the user is satisfied") or a restatement ("the booking succeeded"). The minimal guarantee says what is protected on *every* exit. The main success scenario ends exactly where the success guarantee becomes true.
- **Ask when it fails:** "If someone looked at the system right after success, what would they find?" *Recommended:* one sentence per stakeholder whose interest is satisfied.
- **Bad:** Success guarantee: "The booking works."
- **Good:** "The room is held for the slot in the organiser's name, and the invitees have the invitation." Minimal: "No booking is half-saved; every attempt is logged with the organiser and slot."
- **Sources:** C1 tests 13–15; C1 Reminder 9 "Stakeholders need guarantees"; C2 §6.9.
- **`check_grid.py`:** that the field is filled, not what it says.

### Q5. Preconditions are assumptions, never re-checked

- **Test:** Each precondition is something the system can rely on because another use case put it in place, and the scenario never checks it. Anything the scenario checks is an extension, not a precondition. "None" is better than filler.
- **Ask when it fails:** "Does the system verify this during the use case? Then it's an extension." *Recommended:* move it to an extension on the step that checks it.
- **Bad:** Precondition "The room is free" (then step 3 checks availability); "The system is running".
- **Good:** "The organiser is signed in." Availability is extension 3a.
- **Sources:** C1 tests 10, 11; C2 §6.9 ("don't bother with a precondition or success guarantee unless you are stating something non-obvious").
- **`check_grid.py`:** none on content; an explicit `None` in Preconditions passes the "no field is empty" rule (T2).

## 2. Main success scenario

### Q6. Each step has one subject and shows who has the ball

- **Test:** Every step is one simple sentence, subject–verb–object, whose subject is a named actor (the organiser, the system, the calendar service). No passive voice, no step where two actors act.
- **Ask when it fails:** rarely a question; the writer fixes it. If the actor is genuinely unclear: "Who does this, the organiser or the system?"
- **Bad:** "The room is selected and confirmed."
- **Good:** "2. (actor) The organiser chooses a room." "3. (system) The system confirms the room is free for the slot."
- **Sources:** C1 test 20; C1 guideline titles 1 "It uses simple grammar", 2 "It shows clearly, 'Who has the ball'", 3 "It is written from a bird's eye point of view" (inferred from titles); C1 Reminders 3, 5; C1 ch. 19 (leaving out the subject of a sentence is one of the three most common mistakes); C3 ActorIntentAccomplished.
- **`check_grid.py`:** the `(actor)`/`(system)` marker exists [R28-Q6], not that the sentence's subject matches it.

### Q7. Steps state intent, not interface or technology

- **Test:** No screens, controls, gestures, navigation or layout, including words the UI warning list misses ("drags", "dropdown", "taps the card", "on page 2"). No technology choices.
- **Ask when it fails:** "What is the organiser trying to achieve with that click?" *Recommended:* the intent, in the actor's words.
- **Bad:** "The organiser opens the calendar view, drags across 10:00–11:00 and clicks Book."
- **Good:** "The organiser asks for a room for Tuesday 10:00–11:00."
- **Sources:** C1 test 23; C1 guideline 5 "It shows the actor's intent, not movements" (title); C1 Reminder 7 "Keep the GUI out"; C1 ch. 19 (UI detail is one of the three most common mistakes); C2 §6.11 essential style; C3 VisibleActorIntent, TechnologyNeutral.
- **`check_grid.py`:** warns on a fixed word list [R28-Q7]; the rest is judgement.

### Q8. Every step moves the goal forward, one level down

- **Test:** Removing any step would lose something a stakeholder needs. No step is pure display, waiting or bookkeeping that nobody depends on. Each step's goal is just below the use case's goal: not a sub-sub-step ("types the date"), not a goal of the same size ("organises the meeting"). Asking "why?" of a step leads to the use case goal. The main success scenario has 3 to 9 steps, counted after bundling: one system step may validate, record and respond together when those actions share a duration class, and is split only where the duration class changes (T1).
- **Ask when it fails:** "If we dropped this step, who would notice?" *Recommended:* merge it into its neighbour or drop it.
- **Bad:** "4. The system shows a loading indicator." "5. The organiser reviews the details."
- **Good:** "4. (system) The system holds the room and sends the invitations."
- **Sources:** C1 tests 17–19, 22; C1 Reminders "Show a goal succeeding", "Ask 'why' to find a next-higher level goal"; C1 guideline titles 4 "process moving distinctly forward", 6 "a 'reasonable' set of actions"; C1 §5.5 "Use 3-10 steps per use case" and The Writing Process step 8 "Use 3 to 9 steps"; C3 ForwardProgress, LeveledSteps.
- **`check_grid.py`:** none; whether a system step should be bundled or split is judgement (T1).

### Q9. Information passed is named, at the right precision

- **Test:** Each actor step says what information is given, by nickname ("the slot", "the attendees"). It does not say "the details", and it does not list fields, formats or lengths, which belong to the glossary or the data rules. A rule the system enforces is named where it bites, by reference.
- **Ask when it fails:** "What does the system need from the organiser here, by name?" *Recommended:* two to four nicknames; field rules go to the glossary.
- **Bad:** "The organiser enters the details." / "The organiser enters a title (max 80 characters), a start time (HH:MM)…"
- **Good:** "The organiser gives the slot, the expected attendees and any equipment needed." "The system applies the booking policy (maximum four hours)."
- **Sources:** C1 test 24; C1 Reminders "For data descriptions: Only put precision level 1 into the use case text"; C1 ch. 16 (field-level data "belongs in the requirements somewhere — and not in the use case"); C1 §1.3 (use cases are not the business rules or data formats).
- **`check_grid.py`:** none; `check_terms.py` flags nicknames missing from the glossary.

### Q10. The scenario validates; it does not branch

- **Test:** No "if", "otherwise", "check whether" in the main success scenario. A check is written as the system validating, and its failure is an extension on that step.
- **Ask when it fails:** rarely a question; the writer moves the branch to an extension.
- **Bad:** "3. The system checks whether the room is free. If so it books it, otherwise it shows an error."
- **Good:** "3. (system) The system confirms the room is free for the slot." / "3a. The room is booked for an overlapping slot: …"
- **Sources:** C1 test 25; C1 guideline 7 "It doesn't 'check whether', it 'validates'" (title); C1 ch. 11 preferred style ("no *if* statements"); C2 §6.9 "Defer all conditional and branching statements to the Extensions section".
- **`check_grid.py`:** none.

## 3. Extensions

### Q11. Conditions are what the system detects and must handle

- **Test:** Each condition is phrased as something the system (or an actor) can observe at that step, and the system has to respond to it. Not an inference, a cause it cannot see, or an inner state. A grid cell answered `yes` with a condition the system cannot detect is wrong: the cell is `n/a`. A cell never needs an invented condition: it may cite an extension that already covers it (T3).
- **Ask when it fails:** "At that step, what exactly does the system see?" *Recommended:* the observable symptom, not its cause.
- **Bad:** "3a. The organiser changes their mind." "4a. The network is slow." "4b. The calendar service has a bug."
- **Good:** "2a. The organiser abandons the request." "4a. The calendar service does not answer within 10 seconds."
- **Sources:** C1 tests 26, 27; C1 guideline 11 "The condition says what was detected" (title); The Writing Process step 9 "Include all that the system can detect and must handle"; C2 §6.9 ("the latter is an inference"); C3 DetectableConditions.
- **`check_grid.py`:** that a `yes` has an extension, not that its condition is detectable.

### Q12. The extension list is rationalised

- **Test:** No two extensions on the same step have the same handling under different wording; they are merged. Low-level failures are rolled up into what the step's actor experiences. A condition that can happen during many steps is written once: `UC-NNN.*a` for any step, `UC-NNN.3-6a` for a range of steps, and a `yes` cell on another step cites that extension instead of repeating it (T3).
- **Ask when it fails:** "Does the system do anything different in these cases? If not, they are one condition." *Recommended:* merge, keep the wording the actor would recognise.
- **Bad:** "3a. The room was deleted." "3b. The room was archived." "3c. The room ID is unknown." (same handling)
- **Good:** "3a. The room no longer exists: …"
- **Sources:** C1 ch. 8 section titles "Brainstorm all conceivable failures and alternative courses", "Rationalize the extensions list", "Roll up failures" (inferred from titles); C2 §6.9 `*a` "at any time" extensions; C3 ExhaustiveAlternatives, MergeDroplets.
- **`check_grid.py`:** none on merging; after T3 it accepts `*a` and range IDs and a `yes` cell that cites an extension keyed to another step or range.

### Q13. Handling is decided behaviour with a clear ending

- **Test:** Each handled extension says what the system does, not only that it reports a problem, and where it goes next: back to a named step, to an alternative success, or to failure with the minimal guarantee honoured. "The system shows an error" alone fails.
- **Ask when it fails:** "After that, what can the organiser do, and what does the system keep?" *Recommended:* the most helpful recovery the business accepts, plus where it rejoins.
- **Bad:** "3a. The room is taken: the system shows an error."
- **Good:** "3a. The room was booked for an overlapping slot meanwhile: 1. The system offers the nearest free room in the same building for the slot. 2. Returns to step 2."
- **Sources:** C1 The Writing Process step 10 ("Each will ends back in the MSS, at a separate success exit, or in failure" [sic]); C1 Reminders 8 "Two endings", 21 "Handle failures"; C1 §1.4 (writing the handling is where new stakeholders, goals and business rules surface); C1 §2.1 "Goals can fail".
- **`check_grid.py`:** that handling or a `deferred`/`out-of-scope` reason exists [R1-Q7].

### Q14. Examples are concrete and add information

- **Test:** Each example names a specific actor, value and moment, and would read as a test scenario. It does not restate the condition in other words.
- **Ask when it fails:** "Give me one real instance: who, which room, what time?" An extension nobody can give an example for is not understood yet (spec §6 step 6).
- **Bad:** "*Example:* the room is unavailable."
- **Good:** "*Example:* Ana asks for room 3 on Tuesday at 10:00; Ben booked it at 09:59."
- **Sources:** framework rule [R28-Q3]; C1 glossary "concrete scenario" and §1.6 usage narrative (a "situated example", "highly specific").
- **`check_grid.py`:** that `*Example:*` exists, not its content.

## 4. The whole use case

### Q15. Variations are "how", not "what"

- **Test:** Each technology and data variation changes how a step is done, not what happens. A different outcome is an extension.
- **Ask when it fails:** "Does the outcome change, or only the means?" *Recommended:* outcome changes → extension.
- **Bad:** Variation "2: booking fails if the room is full."
- **Good:** "2: the organiser finds the room by name, on the floor plan, or by the code on the door." [R28-Q8]
- **Sources:** C1 test 28; C1 ch. 9 ("What is happening is the same, but how it is done might vary").
- **`check_grid.py`:** none.

**Human check, not scored.** Cockburn's last three tests are put to people, not to a judge: to sponsors and users, "Is this what you want?" and "Will you be able to tell, upon delivery, whether you got this?"; to developers, "Can you implement this?" (C1 tests 29–31; ch. 12 "When are we done?"). They belong to the driver's sign-off on the `uc/UC-…` PR [R28-Q11], not to the skill.

## 5. Tensions with the current framework, and decisions

Four places where the sources and the framework's rules pulled apart. The driver accepted the recommendation in each case on 2026-10-22.

- **T1. Step count vs the actor/system split.** Cockburn: 3–9 steps (C1 Writing Process step 8; 3–10 in §5.5); a step may carry a "reasonable set of actions" (guideline 6). The framework marks every step `(actor)` or `(system)` [R28-Q6], and the spec's gotcha splits a step that takes input and stores it. A routine booking then tends to run past nine steps (our estimate, not measured) and fails Q8's size test by construction.
  *Decided:* one system step may bundle validate, record and respond when those actions share a duration class; it is split only where the duration class changes [R29-Q1]. The grid's categories and the duration classes stay attached to the step that matters. The 3–9 range applies after bundling. Actor and system steps stay separate: the gotcha still holds for input followed by storage.
- **T2. Mandatory fields vs no filler.** Spec §6 step 3 is "done when no field is empty". Larman: don't write a precondition or guarantee "unless you are stating something non-obvious"; Cockburn: "Sufficient is fine". Required fields invite filler ("The system is running").
  *Decided:* Preconditions accepts an explicit `None`, which counts as filled. Q4 and Q5 score what the fields say, not whether they contain text.
- **T3. One extension per grid cell vs a rationalised list.** The grid asks each category of each step and wants an extension per `yes` [R4-Q2]; extension IDs are keyed to one step (`UC-NNN.3a`). Cockburn rolls failures up and merges equivalent conditions; Larman uses `*a` (any step) and `3-6a` (a range of steps). The grid as written nudged towards duplicates (Q12) and towards inventing conditions to fill `yes` cells (Q11).
  *Decided:* both forms are accepted. Extension IDs may be `UC-NNN.*a` (any step) or `UC-NNN.3-6a` (steps 3 to 6), next to the existing `UC-NNN.3a`. A `yes` cell may cite an extension keyed to another step or to a range, instead of requiring a new extension on its own step.
- **T4. Interests are never checked against the body.** Nothing mechanical links Stakeholders and interests to steps or guarantees, so the list decays into decoration.
  *Decided:* Q3 stays judgement. The skill's report lists each interest with the step, extension or guarantee that protects it, or flags it as unprotected.

**Changes these decisions imply** (made with round 31, 2026-10-23; T1 → R31-Q1, T2 → R31-Q2, T3 → R31-Q3, T4 → R31-Q4):

| Decision | Files |
|---|---|
| T1 | [`write-use-case`](../skills/write-use-case.md) §6 step 4 and the §14 gotcha on input and storage; [`use-case.md`](../templates/use-case.md) main-scenario comment; [chapter 3](../guide/03-design-playbook.md) where it describes steps |
| T2 | [`write-use-case`](../skills/write-use-case.md) §6 step 3 and §7 (`check_grid.py`); [`use-case.md`](../templates/use-case.md) Preconditions row |
| T3 | [`write-use-case`](../skills/write-use-case.md) §6 step 6, §7 (`check_grid.py`, `renumber.py`) and `renumber` mode; [`check-gate`](../skills/check-gate.md) (IDs that point nowhere); [`use-case.md`](../templates/use-case.md) extensions comment; every place that quotes the ID format: [chapter 2](../guide/02-artifacts-and-ids.md), chapters [1](../guide/01-lifecycle-and-gates.md), [3](../guide/03-design-playbook.md) and [8](../guide/08-testing.md), [`write-stories`](../skills/write-stories.md), [`write-scenarios`](../skills/write-scenarios.md), templates [`story.md`](../templates/story.md), [`prd.md`](../templates/prd.md) and [`feature.feature`](../templates/feature.feature) (`@UC-…` tags and `extensions:` lists must accept `*a` and ranges) |
| T4 | [`write-use-case`](../skills/write-use-case.md) §5 (report contents) |

## 6. What the interview takes from this

- **Ask in order of precision.** Actor and goal (Q1–Q2), then stakeholders and guarantees (Q3–Q5), then the main scenario (Q6–Q10), then the full list of conditions (Q11–Q12), and only then the handling (Q13–Q14). Cockburn's "Work breadth-first, from lower precision to higher precision" (C1 Reminders; §1.5), and: "Draft this list completely before working out how the system must handle them all. ... People who start writing the failure handling immediately often run out of energy before listing all the failure conditions."
- **One failing criterion, one question**, phrased as in the criterion, with its recommended answer. Q6, Q10 and most of Q7 are fixed by the writer without asking.
- **Spend questions on content, not form.** Cockburn's "second particularly valuable moment" is the failure brainstorm, where the business experts end up "huddled together or making phone calls to resolve 'What should the system do here?'" (C1 §1.4). Form criteria are corrected silently; questions go to Q1, Q3, Q11 and Q13.
- **Don't ask what the inputs already answer.** A question whose answer is in a cited input, the facts note or the glossary is a defect of the interview, not of the use case.

## 7. Checking the rubric against the sample pairs

The rubric earns its place only if it explains the difference between a good and a bad use case on real material. For each sample pair (good v1, bad v2):

1. List every difference between v1 and v2 that matters to a reader.
2. Tag each with the criterion it breaks (Q1–Q15), or `none`.
3. After all pairs, tally.

| Result | Meaning | Action |
|---|---|---|
| A difference tagged `none` | The rubric misses a quality dimension | Add a criterion, or widen one |
| A criterion that never fires across all pairs | Not a failure seen in practice | Keep it in the reference, drop it from the grader |
| A criterion that fires on most pairs | The main failure mode | Put it first in `SKILL.md` and in the interview |
| v1 fails a criterion | Either v1 is not gold, or the criterion is wrong | Decide which; fix one |

The tally then sets the grader's weights and the order of the interview questions, instead of the order of this document.
