# Time and duration in use cases, stories and UX

Research for [Round 29](../../grilling-log.md#round-29-time-and-duration-in-use-cases-2026-10-20). The question came up during Round 28: should *cancel or abandon*, an actor-step category, also apply to a system step that runs long enough to interrupt, such as an upload? Answering it means looking at how long each step takes, and Cockburn calls that the anchor of his latest book.

Researched on 2026-10-20. Every source below was fetched and read, and the key quotes were checked against the live pages. PDFs were text-extracted. Statements marked **[inference]** are ours, not the source's. Page numbers for *Writing Effective Use Cases* (WEUC) come from the free pre-publication drafts, not from the 2001 printed book.

## 1. The framing: "verbs have time durations"

Humanizing Work Show #113, *Alistair Cockburn on Use Cases & User Stories* (January 2024), chapter "The role of verbs and time", [from 4:20](https://www.youtube.com/watch?v=CRvwbRqi_ss&t=260s) to 7:01. This summary is taken from YouTube's auto-generated captions; the episode page also has a transcript.

- **Two concepts come first.** Cockburn opens with the first two concepts of *Unifying User Stories, Use Cases, Story Maps*: "verbs have time durations, and if you can't master that, you got nothing", and "verbs break down into smaller time duration" verbs.
- **Everything is goal-oriented.** A spec has no descriptive passages, only action verbs. "Every action you state is presumed to succeed." Every goal has sub-goals and steps, and "if you have a goal that takes that long, the steps are going to take that long."
- **The literature misses this.** It is the "magic that's missing in all of the literature": use cases, story maps, epics and features all have this duration aspect, but "when we write verbs, people don't play with that explicitly."
- **Decomposing never invades the design.** "You could keep breaking it down forever and you never invade the system." His example is "insert card into ATM": a step that small is still "all externally visible activities".
- **Use cases carry only the verbs.** When you decompose, you decompose "everything: the data, performance, scalability, UI", and "use cases only handle the verb part, and user stories handle all of them."

Later in the interview (13:00–13:45) he ties duration to goal level: "verb durations, I call them levels, altitude levels". Readers "get uncomfortable if you don't match the verb levels in a scenario": "you don't have a one month process followed by a five minute process step."

The same idea is in his 2024 talk slides: "1. Verbs imply durations. 2. Decompose verbs into 'smaller' (shorter duration) verbs." It is also in the table of contents of the book's 2nd edition (2025): §1.2 "Verbs imply durations" and §1.3 "Decompose verbs into shorter-duration verbs". The book's body text was not available. The framing goes back at least to 2002 ("a more immediate goal (targeting a smaller time span)", *Use Cases, Ten Years Later*).

## 2. Use cases and time

### 2.1 Duration is goal level

- **Cockburn's coffee-break test** (WEUC draft #3, §5.1, p. 57): "In most circumstances, it passes the test: one person, one sitting (2-20 minutes)." It is a heuristic, not a hard rule. "On-line auctions take several days, so fail the single-sitting test."
- **Summary use cases are defined by time span:**
  - they "typically execute over hours, days, weeks, months, or years" (draft #3, §5.2, p. 59);
  - a summary use case "takes multiple user-goal sessions to complete" (draft #3, glossary);
  - a user goal is "typically performed by one primary actor in one sitting of 2-20 minutes (less if the primary actor is a computer), after which they can leave" (draft #3, glossary).
- **Larman agrees.** His elementary business process "doesn't take days and multiple sessions… it is a task done during a single session. It is probably between a few minutes and an hour in length" (*Applying UML and Patterns*, 2nd ed., ch. 6, p. 60). He allows "reasonable violations"; the guideline finds "the dominant level".
- **Jacobson sets no limit on elapsed time.** Use-Case 2.0 (2011) and the *Use-Case Foundation* (Jacobson and Cockburn, 2024) give none. A use case runs "from the initial event to the realization of the value it provides or the eventual failure".

### 2.2 What Cockburn does with a goal that doesn't fit one sitting

His examples show four moves. None of them is stated as a general rule.

1. **Raise the goal to summary level**, with each sitting as a user-goal use case. Examples: *Operate an Insurance Policy*; *Handle a Claim*, "work that may take days, weeks or months… it contains many single-sitting activities" (1999 draft, p. 163).
2. **End the user-goal use case at the wait point** and hand off to a later one. In *Buy Stocks over the Web*, extension 4b is "PAF logs the delay, sets a timer to ask the user about the outcome", then "(see use case Update questioned purchase)" (draft #3, p. 17).
3. **Save and resume inside a user-goal use case.** *Register Loss* (1999 draft, pp. 165–169) has three extensions:
   - "Clerk can save the loss any time before completion";
   - "Clerk wants to restart a loss which has been interrupted, saved or needs completion";
   - a timeout on the saved state: "System decides it is time to commit and log the loss".
4. **In a summary use case, write long waits as other actors' steps** and timeouts as extensions: "Vendor does not deliver on time: System does alert of non-delivery" (*Buy Something*, draft #3, pp. 22–23).

**[inference]** Read with the 2024 rule ("match the verb levels"), these examples give a rule: a step that waits hours or days inside a user-goal scenario mixes levels, so the use case ends at the wait and the continuation becomes its own use case.

### 2.3 Time as a trigger, timeouts and "at any time"

- **Time as a trigger.** Cockburn's template says "Trigger: <what starts the use case, may be time event>" (TR.96.03a, 1998).
- **Time as an actor.** The 1999 draft (p. 29) says: "A less obvious example of a non-operator primary actor is time. Some use cases are triggered by time, say, midnight, or the end of the month." For the primary actor, "we find out who cares that the use case actually runs at that time", and getting it wrong costs "not much".
- **Larman** only asks "Is 'time' an actor because the system does something in response to a time event?" (p. 61) and does not answer.
- **Robertson and Robertson** (*Mastering the Requirements Process*, 2nd ed., 2006): "Time-triggered business events are initiated by the arrival of a predetermined time (or date)." The idea traces back to McMenamin and Palmer's "temporal" events (*Essential Systems Analysis*, 1984).
- **Wiegers and Beatty** (*Software Requirements*, 3rd ed.): a temporal event fires "when the computer's clock reaches a specified time" or "when a preset duration has passed since a previous event".
- **Timeouts.** Brainstorm "Inaction by the primary actor (timeouts)", and ask "What happens if the primary actor walks away, or the secondary actor never replies?" (1999 draft, pp. 72, 74).
- **"At any time" extensions.** "If the condition can occur at any time, use an asterisk ('*') instead of the step number", e.g. "*b. User walked away without notice (timeout)" (1999 draft, p. 75). Larman uses the same `*a` labels. A cancel is written "At any time prior to receiving goods, Requestor can change or cancel the request" (draft #3, p. 23).
- **Performance targets mix two durations.** The project information of *Buy Goods* gives "5 minutes for order, 45 days until paid" (1999 draft, p. 171). **[inference]** That is two different durations: an interaction time and a business deadline. A deadline is a domain rule that becomes a timer; an interaction time is a quality attribute.

## 3. UX and time

### 3.1 Response-time limits

- **Miller (1968)** set no single limit; his question was "Response time to what?" He lists 17 classes of action, each with its own limit:
  - 0.1 s for key feedback;
  - 1 s for the next page;
  - 2 s for conversation;
  - 4 s to acknowledge a command;
  - 15 s before "the system had better be designed to free the user from physical and mental captivity".

  Two of his rules matter most here. First, delays over 2 s "should follow only a condition of task closure". Second, a command should be acknowledged "within four seconds", while "execution and final confirmation… may have long and variable delays of minutes."
- **Card, Robertson and Mackinlay (1991)** give three human time constants: perceptual 0.1 s, immediate response 1 s, and unit task 10 s ("say, 5-30 sec"). They cite Card, Moran and Newell, not Miller.
- **Nielsen (1993)** turned these into the three limits that are now standard:
  - 0.1 s feels instantaneous;
  - 1 s keeps the "flow of thought" uninterrupted;
  - 10 s is "the limit for keeping the user's attention focused on the dialogue".

  Above 10 s, use percent-done progress and "a clearly signposted way for the user to interrupt the operation". Longer delays "are only acceptable during natural breaks in the user's work". *Powers of 10* (2009) extends the scale: simple tasks take about 1 minute, most web tasks less than an hour, and multi-person workflows a month or more.
- **Doherty and Thadhani** (IBM, 1982). Their brief argues for "subsecond" response: going from 3 s to 0.3 s took users from 180 to 371 transactions an hour. The popular "400 ms Doherty threshold" does not appear in the archived brief; treat it as folklore.
- **Google's RAIL model and INP:**
  - RAIL: respond to input within 100 ms; beyond 1 s "users lose focus"; beyond 10 s they "are likely to abandon tasks".
  - INP: thresholds are measured at the 75th percentile of real use.

### 3.2 Progress, cancel and waiting

- **Myers (1985):** "people prefer to have progress indicators". They lower anxiety and let people plan the wait.
- **Harrison et al. (2007, 2010):** pauses near the end make a bar feel slower; acceleration at the end feels faster. Run variable stages first.
- **NN/g:**
  - a progress indicator "for any action that takes longer than about 1.0 second";
  - a looped spinner for 2 to 10 s, percent-done for 10 s or more (Sherwin, 2014);
  - skeleton screens for full-page loads under 10 s; above that, "an explicit estimation of duration" (Tankala, 2023).
- **Apple HIG:** prefer determinate progress, so people can "decide whether to do something else while waiting". "When it's feasible, let people halt processing"; offer Pause as well as Cancel when cancelling has side effects. Don't show "90 percent completion in five seconds and the last 10 percent in 5 minutes".
- **User control and freedom** (NN/g, Rosala, 2020): users "should be able to cancel that task at any point". The example given is a large download.
- **Maister (1985):** uncertain waits feel longer than known, finite waits; unexplained waits feel longer than explained ones; occupied time feels shorter. He wrote about service queues; the transfer to UX is **[inference]**.
- **Optimistic UI** (React `useOptimistic`) shows the result at once and rolls back on failure. **[inference]** This moves a likely-to-succeed network wait into the instant class.

### 3.3 Goals that span sessions

- **GOV.UK task list:** use it only when users "do not want to, or cannot, complete all the tasks in one sitting"; then "consider allowing users to save their progress".
- **GOV.UK "Complete multiple tasks":** show the list "at the start of each returning session", with statuses.
- **GOV.UK confirmation pages:** they include a reference and "details of what happens next and when".
- **GOV.UK One Login:** a "Save and complete later" link on every page.
- **Cost of save-and-return:** the MoJ (2023) and DWP (2021) posts weigh it: "Save and Return isn't free". DWP says to measure how many sessions users need before building it.
- **Status trackers** (NN/g, Rosala, 2019): pull (trackers) and push (updates), and "set expectations for the wait time".
- **Resuming after an interruption.** Altmann and Trafton (2002): a suspended goal decays, and resuming needs cues in the environment, linked before the goal was suspended. Mark, Gudith and Klocke (2008): interrupted work is finished faster, but with "more stress, higher frustration". **[inference]** A resume screen should show where the user stopped and what comes next.
- **WCAG 2.2:** 2.2.1 Timing Adjustable (A) exempts limits longer than 20 hours; 2.2.5 Re-authenticating (AAA) requires no data loss; 2.2.6 Timeouts (AAA) requires a warning unless data is kept more than 20 hours.

### 3.4 Duration classes

No source gives this exact table. It condenses the limits above into four classes for one step, plus the multi-session case, which is not a step. The boundaries come from the sources; merging Nielsen's 0.1 s and 1 s classes, and the "can leave" cut, are **[inference]**.

| Class | Duration | The actor | What the design needs | Sources |
|---|---|---|---|---|
| **instant** | under 1 s | doesn't wait | the result in place; no indicator, which would only flash | Nielsen 1993; Card 1991; NN/g 2023 |
| **wait** | 1 to 10 s | waits, attention on the task | a labelled spinner or skeleton; the rest of the screen stays usable | Miller 1968; Nielsen 1993; NN/g 2014, 2023; Apple HIG |
| **long** | over 10 s | stays, but attention drifts | determinate progress and an estimate; cancel (and pause if cancelling loses work); may leave the screen | Nielsen 1993; Card 1991; Myers 1985; Harrison 2007; Apple HIG; NN/g 2020 |
| **background** | minutes or more | may leave | an immediate acknowledgement, a visible status, a notification on success or failure, a findable result, cancel from the status | Miller 1968 (acknowledge vs complete); Apple HIG; NN/g 2019, 2024; AIP-151 |
| *multi-session* | hours to weeks | leaves and comes back, often after someone else acts | not a step: separate sittings, each its own goal; saved progress, a status, "what happens next and when" | Cockburn WEUC; Nielsen 2009; GOV.UK; WCAG 2.2 |

## 4. Stories, system design and tests

### 4.1 Splitting stories

- **Humanizing Work splitting guide** (Lawrence and Green), Workflow Steps pattern: "build the simple end-to-end case first and then add the middle steps and special cases"; "the most obvious split—one step at a time from beginning to end—is the wrong way to go."
- **Same guide, Defer Performance pattern:** split into "make it work" and "make it fast". It warns: "It's easy to get in a habit of calling stories done that aren't really done."
- **Patton:** "I'm always imagining time moving left to right" on a story map. The top slice is the walking skeleton, a term he credits to Cockburn.
- **SPIDR (Cohn) and INVEST (Wake)** have no technique based on time.
- **[inference]** A story whose outcome appears days later ("the hold is released after 24 h") is testable only if the test controls the clock (§4.3).

### 4.2 Long-running work in the system and its API

- **Sagas** (Garcia-Molina and Salem, 1987): long-lived transactions "hold on to database resources for relatively long periods of time". A saga splits one into steps, each with a compensating transaction.
- **Azure's Saga pattern** adds two kinds of step: *pivot*, the point of no return, and *retryable*.
- **[inference]** A step past the pivot can't be cancelled. That decides whether *cancel* applies to a long step.
- **Passage of time as a domain event.** Verraes (2019): "Replace cron jobs and scheduled commands, with an agnostic event to indicate the passage of time", such as `DayHasPassed`. He shows the scenarios as Given/When/Then. Pacana (2018) names deadline events after their meaning, e.g. `TimeToPayForInvoiceExpired`.
- **Waiting in workflow engines:**
  - Hohpe: conversations "span hours, days, or even months"; correlate them by ID.
  - Temporal: a durable wait "works identically whether the wait is five seconds or five months".
  - AWS Step Functions: Standard workflows last up to a year; human approval waits on a task token, with a heartbeat timeout.
- **The API must decide sync or async up front.**
  - Google AIP-151: methods that may take long return an operation; "a good rule of thumb is 10 seconds". The same number as Nielsen's attention limit.
  - RFC 9110: 202 Accepted is "intentionally noncommittal", and should point to a status monitor.
  - Azure's Asynchronous Request-Reply pattern adds the details:
    - validate synchronously, then return 202 with `Location` and `Retry-After`;
    - a status resource with a closed set of states;
    - 303 to the result;
    - cancel with DELETE;
    - an idempotency key;
    - a retention period.

### 4.3 Time in acceptance tests

- **Fowler (2011):** "Never use bare sleeps to wait for asynchronous responses: use a callback or polling." "Always wrap the system clock, so it can be easily substituted for testing."
- **Wynne,** *Death to sleeps!*: listen for an event, or poll with a timeout.
- **Temporal's test server** skips time, so a day-long timer runs in milliseconds.
- **Gherkin clock steps** exist in libraries (godogx/clocksteps: `Given the clock is at …`). Cucumber's own docs say nothing about time.
- **[inference]**, consistent with Fowler and Verraes:
  - set "now" in a Given;
  - write time passing as a When in business words;
  - write a deadline rule as a pair of examples, with boundary cases.

## 5. What this means for the framework

These conclusions are ours, drawn from the findings above. The decisions are in Round 29.

1. **A step's duration is part of its verb, not a performance requirement.** Cockburn puts data, UI and performance in the stories, but duration in the verb. Whether a system step takes under a second, a few seconds, minutes, or until tomorrow changes what the actor can do: wait, cancel, leave, come back. That is behaviour the actor sees, so it belongs in the use case. Performance targets stay out of the framework [R12-Q5].
2. **The steps of one scenario should share a level.** A wait of hours or days inside a user-goal scenario means the goal is a summary goal. End the use case at the wait, and start the next one from the other actor's action or from time (Cockburn's four moves, §2.2).
3. **Time can trigger a use case.** The primary actor is the stakeholder who cares that it runs, not "the clock" (Cockburn).
4. **Cancel follows duration, not step kind.** An actor can interrupt any step long enough to watch: a *long* or *background* system step, unless it is past the point of no return (Nielsen; Apple; NN/g; sagas).
5. **A background step must say how the actor learns the outcome** (Miller's split between acknowledgement and completion; NN/g; Apple).
6. **The duration class sets the API shape from the first story.** Use an asynchronous operation from about 10 s (AIP-151; Nielsen). Changing a synchronous endpoint to an asynchronous one later breaks clients. Stories may defer cancel and notification, but not the shape.
7. **The duration class sets the loading state.** A spinner, a skeleton, progress with cancel, or a status and a notification (§3.4).
8. **Time in Gherkin.** Set "now" in a Given, write time passing as a When, put the clock behind a port with a fake, and never use sleeps (Fowler; Verraes).

## 6. Sources

### Public (free to read)

| Author | Title | Year | URL | Contribution |
|---|---|---|---|---|
| Humanizing Work Show with Alistair Cockburn | #113 Alistair Cockburn on Use Cases & User Stories | 2024 | [video](https://www.youtube.com/watch?v=CRvwbRqi_ss&t=260s); [transcript](https://www.humanizingwork.com/alistair-cockburn-on-use-cases-user-stories/) | "Verbs have time durations"; match verb levels in a scenario |
| Alistair Cockburn | Unifying User stories, Use cases, Story maps: the talk (slides) | 2024 | https://alistaircockburn.com/Unifying%20us%20uc%20sm.pdf | "Verbs imply durations" as concept 1; use cases not below fish level |
| Alistair Cockburn | *Unifying…*, 2nd ed., chapter 0 and contents (author's draft) | 2025 | https://alistaircockburn.com/UnifyingV2_chapter0.pdf | Chapter titles §1.2 and §1.3 on durations |
| Alistair Cockburn | Basic Use Case Template, TR.96.03a | 1998 | https://www.cs.helsinki.fi/u/mluukkai/ohmas09/usecase.pdf (copy whose licence allows redistribution with credit) | Trigger "may be time event"; timeouts |
| Ivar Jacobson, Alistair Cockburn | Use-Case Foundation v1.1 | 2024 | https://alistaircockburn.com/Use%20Case%20Foundation.pdf | Use case from initial event to value or failure; no duration rule |
| Karl Wiegers, Joy Beatty | Modeling System Events (adapted from *Software Requirements*, 3rd ed.) | 2013 | https://modernanalyst.com/Resources/Articles/tabid/115/ID/2932/Modeling-System-Events.aspx | Temporal events defined |
| Robert B. Miller | Response time in man-computer conversational transactions | 1968 | https://yusufarslan.net/sites/yusufarslan.net/files/upload/content/Miller1968.pdf (third-party copy; free on the ACM DL as part of its 1951–2000 backfile) | Per-class limits; closure rule; acknowledge vs complete |
| S. K. Card, G. G. Robertson, J. D. Mackinlay | The information visualizer | 1991 | https://courses.ischool.berkeley.edu/i213/s99/Readings/p181-card.pdf (course copy) | 0.1 / 1 / 10 s time constants |
| Jakob Nielsen | Response Times: The 3 Important Limits | 1993 | https://www.nngroup.com/articles/response-times-3-important-limits/ | The three limits; progress and interrupt above 10 s |
| Jakob Nielsen | Powers of 10: Time Scales in User Experience | 2009 | https://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/ | Minutes to months |
| W. J. Doherty, A. J. Thadhani | The Economic Value of Rapid Response Time (IBM) | 1982 | https://archive.computerhistory.org/resources/access/text/2024/03/102751398-05-01-acc.pdf | Subsecond response and productivity |
| Ben Shneiderman | Response Time and Display Rate in Human Performance with Computers | 1984 | https://www.cs.umd.edu/users/ben/papers/Shneiderman1984Response.pdf | Response-time category per class of command |
| Google | RAIL model; Interaction to Next Paint | 2020; 2025 | https://web.dev/articles/rail; https://web.dev/articles/inp | 100 ms response; 1 s and 10 s perception; p75 |
| Brad A. Myers | The importance of percent-done progress indicators | 1985 | https://www.cs.cmu.edu/~bam/papers/percentdoneCHI85.pdf | Users prefer progress indicators |
| C. Harrison et al. | Rethinking the progress bar; Faster progress bars | 2007; 2010 | https://chrisharrison.net/projects/progressbars/ProgBarHarrison.pdf; https://chrisharrison.net/projects/progressbars2/ProgressBarsHarrison.pdf | Perceived duration |
| NN/g (Sherwin; Tankala; Flaherty; Rosala) | Progress indicators; Skeleton screens 101; Indicators, validations and notifications; User control and freedom; Status trackers and progress updates | 2014–2024 | https://www.nngroup.com/articles/progress-indicators/; https://www.nngroup.com/articles/skeleton-screens/; https://www.nngroup.com/articles/indicators-validations-notifications/; https://www.nngroup.com/articles/user-control-and-freedom/; https://www.nngroup.com/articles/status-tracker-progress-update/ | Indicator by duration; cancel; status and notifications |
| Apple | Human Interface Guidelines: Progress indicators; Loading; Managing notifications | current | https://developer.apple.com/design/human-interface-guidelines/progress-indicators | Determinate progress, cancel and pause, honest pacing |
| David Maister | The Psychology of Waiting Lines | 1985 | https://davidmaister.com/articles/1/52/ | Perceived waiting |
| G. Mark, D. Gudith, U. Klocke | The cost of interrupted work | 2008 | https://www.interruptions.net/literature/Mark-CHI08.pdf | Interruptions cost stress |
| E. M. Altmann, J. G. Trafton | Memory for goals | 2002 | https://www.interruptions.net/literature/Altmann-CogSci02.pdf | Resumption needs cues |
| GOV.UK Design System | Task list; Complete multiple tasks; Check answers; Confirmation pages | current | https://design-system.service.gov.uk/components/task-list/; https://design-system.service.gov.uk/patterns/complete-multiple-tasks/; https://design-system.service.gov.uk/patterns/confirmation-pages/ | Multi-session goals |
| GOV.UK One Login; MoJ; DWP | Save progress; Save for later in MoJ Forms; Measuring complex digital services | 2021–current | https://sign-in.service.gov.uk/documentation/design-recommendations/save-progress; https://mojdigital.blog.gov.uk/2023/10/26/balancing-security-and-usability-to-add-save-for-later-to-moj-forms/; https://dataingovernment.blog.gov.uk/2021/11/09/measuring-complex-digital-services | Save and return, and its cost |
| W3C | Understanding WCAG 2.2: 2.2.1, 2.2.5, 2.2.6 | current | https://www.w3.org/WAI/WCAG22/Understanding/timeouts.html | 20-hour retention; no loss on re-authentication |
| React | useOptimistic | current | https://react.dev/reference/react/useOptimistic | Optimistic UI with rollback |
| Richard Lawrence, Peter Green | The Humanizing Work Guide to Splitting User Stories | current | https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/ | End-to-end first; defer performance |
| Jeff Patton | The New Backlog Is Better Represented as a Map | 2008, upd. 2023 | https://jpattonassociates.com/the-new-backlog/ | Time left to right; walking skeleton |
| Mike Cohn; Bill Wake | SPIDR; INVEST | 2003–2026 | https://www.mountaingoatsoftware.com/blog/five-simple-but-powerful-ways-to-split-user-stories; https://xp123.com/invest-in-good-stories-and-smart-tasks/ | No time technique |
| Mathias Verraes | Passage of Time Event | 2019 | https://verraes.net/2019/05/patterns-for-decoupling-distsys-passage-of-time-event/ | Time as a domain event, with Given/When/Then |
| Paweł Pacana | Modeling passing time with events | 2018 | https://blog.arkency.com/modeling-passing-time-with-events/ | Naming deadline events |
| Hector Garcia-Molina, Kenneth Salem | Sagas (abstract) | 1987 | https://www.cs.princeton.edu/research/techreps/598 | Long-lived transactions; compensation |
| Microsoft | Saga pattern; Asynchronous Request-Reply pattern | 2025; 2026 | https://learn.microsoft.com/en-us/azure/architecture/patterns/saga; https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply | Pivot step; 202 + status + cancel |
| Gregor Hohpe | Conversations between loosely coupled systems; Starbucks does not use two-phase commit | 2017; 2004 | https://www.enterpriseintegrationpatterns.com/patterns/conversation/; https://www.enterpriseintegrationpatterns.com/ramblings/18_starbucks.html | Long conversations; correlation; retry or compensate |
| Google | AIP-151 Long-running operations | current | https://google.aip.dev/151 | Operation from about 10 s |
| IETF | RFC 9110, §15.3.3 202 Accepted | 2022 | https://www.rfc-editor.org/rfc/rfc9110 | 202 points to a status monitor |
| Temporal; AWS | Human-in-the-loop approvals; Python testing suite; Step Functions workflow types and integration patterns | current | https://docs.temporal.io/guides/reliable-document-approvals; https://docs.temporal.io/develop/python/testing-suite; https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html | Durable waits; time-skipping tests |
| Martin Fowler | Eradicating Non-Determinism in Tests | 2011 | https://martinfowler.com/articles/nonDeterminism.html | No sleeps; wrap the clock |
| Matt Wynne | Death to sleeps! | 2013 | https://blog.mattwynne.net/2013/06/03/death-to-sleeps/ | Events or polling in acceptance tests |
| godogx | clocksteps | current | https://github.com/godogx/clocksteps | Gherkin clock steps in practice |

**Course-hosted copies whose hosting may not be authorised.** These are linked for reading only; cite the book.

- Cockburn, *Writing Effective Use Cases*, pre-publication draft #3 (2000): [TU Košice copy](https://kurzy.kpi.fei.tuke.sk/zsi/resources/CockburnBookDraft.pdf); the extract on goal levels is at [UZH](https://www.ifi.uzh.ch/dam/jcr:00000000-25a0-3d08-0000-00000ce96422/weuc_extract.pdf).
- Cockburn, *Writing Effective Use Cases*, 1999 draft: [ELTE copy](https://people.inf.elte.hu/molnarba/Informaciorendszerek_ELTE/Writing_effective_Use_cases_Cockburn.pdf). It has the `*a` convention, time as an actor, *Register Loss* and *Handle a Claim*.
- Cockburn, "Use Cases, Ten Years Later" (2002): [UFCG copy](https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm).
- Larman, *Applying UML and Patterns*, 2nd ed., ch. 6: [Duke copy](https://courses.cs.duke.edu/cps108/spring04/readings/usecaseslarman.pdf).
- Jacobson, Spence, Bittner, *Use-Case 2.0* (2011): read on a third-party site. The publisher's English link did not load.
- Robertson and Robertson, 2nd ed., "Time-Triggered Business Events": read on an unauthorised mirror, which is not linked here.

### Private / paywalled

| Author | Title | Year | Contribution |
|---|---|---|---|
| Alistair Cockburn | *Writing Effective Use Cases* (Addison-Wesley) | 2001 | Ch. 5 goal levels; the print source for the drafts above |
| Alistair Cockburn | *Unifying User Stories, Use Cases, Story Maps: The Power of Verbs*, 2nd ed. | 2025 | §1.2 "Verbs imply durations", §1.3 "Decompose verbs into shorter-duration verbs" (not read) |
| Craig Larman | *Applying UML and Patterns*, 3rd ed. | 2004 | The EBP guideline (2nd ed. read) |
| James and Suzanne Robertson (and Andrew Reed, 4th ed.) | *Mastering the Requirements Process*, 2nd ed. 2006; 4th ed. 2024 | 2006; 2024 | Time-triggered business events |
| Stephen McMenamin, John Palmer | *Essential Systems Analysis* | 1984 | Origin of "temporal" events |
| Steven C. Seow | *Designing and Engineering Time* | 2008 | Instantaneous, immediate, continuous and captive classes (known only through Mozilla's Photon guide) |
| Jakob Nielsen | *Usability Engineering*, ch. 5 | 1993 | Full text of the three limits |
| Jeff Patton | *User Story Mapping* (O'Reilly) | 2014 | Book form of the backbone and slices (not read) |
| Alberto Brandolini | *Introducing EventStorming* (Leanpub) | 2021 | The timeline and policies (table of contents only) |
| Matt Wynne, Aslak Hellesøy, Steve Tooke | *The Cucumber Book*, 2nd ed. | 2017 | Chapter on asynchronous components (table of contents only) |
| Steve Freeman, Nat Pryce | *Growing Object-Oriented Software, Guided by Tests*, ch. 27 | 2009 | Testing asynchronous code (table of contents only) |
| Ivar Jacobson, Alistair Cockburn | "Use Cases are Essential", *ACM Queue* 21(5) | 2023 | Normally free; returned 403, not read |

## 7. Not found or uncertain

- **No source states "split a long goal at each wait point" as a rule.** Cockburn's examples show it (§2.2); the rule is ours.
- **The body text of *Unifying*, §1.2 and §1.3, was not read.** Only the chapter titles, the 2024 slides and the interview were.
- **"A use case is not a transaction"** was not found in this exact wording. Cockburn's drafts say Jacobson called a *step* a transaction.
- **The "400 ms Doherty threshold"** is not in the archived IBM brief.
- **"Miller's 10 seconds" is a misattribution.** Miller's figures are 0.1, 1, 2, 4 and 15 s; the 10 s comes from Card et al.
- **No source** prescribes duration classes for use-case steps, or how to write acceptance criteria per class. The table in §3.4 and the conclusions in §5 are ours.
- **Material Design 3** pages did not render for the fetcher. Gojko Adzic's *Specification by Example* has no fetchable passage on time. Brandolini has no confirmed notation for time-triggered events.
