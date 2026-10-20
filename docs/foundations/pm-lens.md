# PM Lens: From Use Case to User Story to PRD

What a product manager needs to think and do in this framework, with the concepts behind it. Times count the text marked *core*; long videos are optional. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

## Contents

- [1. Key behaviours](#1-key-behaviours)
- [2. Core concepts](#2-core-concepts)
  - [2.1 Use cases](#21-use-cases)
  - [2.2 Goal levels](#22-goal-levels)
  - [2.3 Use-Case 2.0 and slices](#23-use-case-20-and-slices)
  - [2.4 The extension matrix](#24-the-extension-matrix)
  - [2.5 User stories](#25-user-stories)
  - [2.6 INVEST](#26-invest)
  - [2.7 Story mapping](#27-story-mapping)
  - [2.8 Story splitting and vertical slices](#28-story-splitting-and-vertical-slices)
  - [2.9 Shape Up](#29-shape-up)
  - [2.10 Measurable outcomes and product metrics](#210-measurable-outcomes-and-product-metrics)
- [3. Optional concepts](#3-optional-concepts)
  - [3.1 Jobs to be done and personas](#31-jobs-to-be-done-and-personas)
- [4. Context](#4-context)

## 1. Key behaviours

| Behaviour | What it looks like here | Where |
|---|---|---|
| **Decomposition** | Break a goal into a main scenario, the scenario into steps, each step into the ways it can fail, then cut the whole into small stories. | [Chapter 3, §3.2–3.3](../guide/03-design-playbook.md#32-step-1-complete-the-use-case) |
| **Precision** | One term per concept, taken from the glossary; one testable sentence per rule; every extension has a handling outcome or an explicit `deferred`. | [Glossary](../guide/02-artifacts-and-ids.md#22-where-artifacts-live), [R4-Q2] |
| **Thinking in outcomes** | Start from what the user gains and how you would see it, not from the features you will ship. | PRD §3, [R4-Q4a] |
| **Saying no to scope** | Out-of-scope lists, deferred extensions, a one-week cap per story, and stories that wait their turn. | PRD §5, [R4-Q3] |

**A name clash to avoid:** this framework's *persona reviewers* (PM, UX, Eng) are review agents that play a team role [R1-Q12]. They are not *user personas*, which describe customers (see the last entry).

## 2. Core concepts

### 2.1 Use cases

- **Roles:** PM [core] · UX [core] · SWE [optional]
- **Time:** ~22 min (+42 min video, optional)

**Definition**

A use case describes how an actor reaches a goal with a system: a numbered main success scenario, plus **extensions** for every condition that makes a step go differently. Ivar Jacobson introduced them; Alistair Cockburn gave them their written "fully dressed" form, with stakeholders, preconditions and guarantees.

**Why it matters**

- **PM:** it is where edge cases are found before anyone designs a screen.
- **UX:** it lists every situation a flow must handle.
- **SWE:** it is the behaviour the business layer must implement.

**In this framework**

Every use case is written at the user-goal level ([§2.2](#22-goal-levels)) in the fully dressed format [R1-Q6, R28-Q1] and moves from `Draft` to `Complete` [R28-Q11]. Stories are cut only from a complete use case ([chapter 1, §1.3](../guide/01-lifecycle-and-gates.md#13-before-a-prd-exists-the-use-case-gate)). Departure from the literature: Cockburn also allows casual, brief formats; we don't. Template: [`use-case.md`](../templates/use-case.md).

**Learn it**

- Text: [Use-Case Foundation v1.1](https://alistaircockburn.com/Use%20Case%20Foundation.pdf) (Jacobson & Cockburn, ~4 min)
- Text: [Basic use case template](https://web.archive.org/web/20140330001816/http://alistair.cockburn.us/Basic+use+case+template) (Cockburn, archived copy, ~17 min)
- Text: [Use Case](https://martinfowler.com/bliki/UseCase.html) (Martin Fowler, ~1 min)
- Video: [Alistair Cockburn on Use Cases & User Stories](https://www.youtube.com/watch?v=CRvwbRqi_ss) (Humanizing Work, 41:43)

**Key literature**

- Ivar Jacobson et al., *Object-Oriented Software Engineering: A Use Case Driven Approach* (1992)
- Alistair Cockburn, *Writing Effective Use Cases* (2000)

### 2.2 Goal levels

- **Roles:** PM [core] · UX [core] · SWE [optional]
- **Time:** ~17 min (text + video; +8 min text, optional)

**Definition**

Cockburn sorts goals by altitude. A **user goal** ("sea level", blue, a waves icon) is one the primary actor can finish and then walk away happy: his **coffee-break test** is "After I get done with this, I can take a coffee break", typically one person, one sitting, 2 to 20 minutes. Above it, a **summary** goal (white, a kite or, very high, a cloud) groups several user goals and runs over hours to years. Below it, a **subfunction** (indigo, a fish) is a step that serves a user goal, such as "find a customer"; a goal too low to write at all is a **clam**. Asking "why?" of a goal moves up a level. Larman's **elementary business process** is the same idea.

Cockburn now frames the levels as time: **verbs have durations**. Every goal is a verb, its steps are verbs of shorter duration, and you can keep breaking them down without ever describing the system's inside. A reader is uneasy when one scenario mixes levels: "you don't have a one month process followed by a five minute process step". He calls this the anchor of his latest book.

**Why it matters**

- **PM:** the level decides the size of everything downstream. A summary goal ("manage the office") yields stories too big to slice; a subfunction ("enter a date") yields stories with no value of their own.
- **UX:** one user goal is usually one task flow, from entry to the moment the user is done.
- **SWE:** a user goal is usually one business use case in the domain layer (`business/usecases`).

**In this framework**

Every use case is written at the **user-goal** level, and the template fixes its `Level` field to `User goal` [R28-Q1]. "Book a meeting room" passes the coffee-break test; "Manage the office's rooms" is a summary goal, and "Choose a time slot" is a subfunction. A summary goal is kept, if at all, as a short map listing the user-goal use cases it groups: no fields, no failure grid, no stories. A subfunction is written as a step of the user-goal use case that needs it. The steps of a use case share one level of duration: a step that waits hours or days for someone else or for a deadline ends the use case at a **wait point**, and each system step that isn't instant says how long it takes (`wait`, `long` or `background`), because that decides whether the actor can cancel it or leave [R29-Q1, R29-Q2]. The use-case writer checks the level first ([chapter 3, §3.2](../guide/03-design-playbook.md#32-step-1-complete-the-use-case)). Departure: Cockburn writes use cases at every level and recommends writing the 2 to 5 outermost summary use cases; we write only user goals, so every use case can be cut into stories the same way.

**Learn it**

- Text: [Use Case Levels](https://ttm4115.iik.ntnu.no/unit-4-req/preparation-1.html) (NTNU course notes, ~4 min; Cockburn's own figures are 3 to 9 steps, not 3 to 8)
- Text: [*Writing Effective Use Cases*, draft, chapter 5 "Three Named Goal Levels"](https://www.ifi.uzh.ch/dam/jcr:00000000-25a0-3d08-0000-00000ce96422/weuc_extract.pdf) (Cockburn, pre-publication draft hosted by the University of Zurich, pages 57 to 62, ~10 min)
- Text: [*Applying UML and Patterns*, chapter 6](https://courses.cs.duke.edu/cps108/spring04/readings/usecaseslarman.pdf) (Larman, course copy; section 6.8, "Use Cases for Elementary Business Processes", ~8 min, optional)
- Video: ["The role of verbs and time"](https://www.youtube.com/watch?v=CRvwbRqi_ss&t=260s), a chapter of the Humanizing Work interview with Cockburn (4:20 to 7:01, ~3 min; the whole interview is 41:43, and 13:00 to 13:45 covers matching levels)
- Further: [Time and duration in use cases](../research/simplify-explore/time-and-duration.md), the research behind duration classes and wait points
- *Note:* No free French resource was found.

**Key literature**

- Alistair Cockburn, "Structuring Use Cases with Goals", *Journal of Object-Oriented Programming* (1997)
- Alistair Cockburn, *Writing Effective Use Cases* (2000), chapter 5; in French, *Rédiger des cas d'utilisation efficaces* (2001)
- Craig Larman, *Applying UML and Patterns*, chapter 6 (2nd ed., 2002)

### 2.3 Use-Case 2.0 and slices

- **Roles:** PM [optional] · UX [optional] · SWE [optional]
- **Time:** ~33 min (+59 min video, optional)

**Definition**

Use-Case 2.0 is Jacobson's lightweight update of use cases for agile teams. Its central idea is the **use-case slice**: one or more paths through a use case, small enough to build and test on their own.

**Why it matters**

- **PM:** it is the bridge between analysing a whole goal and delivering it in pieces.
- **SWE:** a slice is an end-to-end unit of work, not a layer.

**In this framework**

Our user story is exactly a slice: a vertical path through the use case plus the extensions it handles [R4-Q3]. Departure: we don't use Use-Case 2.0's slice states or its own backlog; one story = one PRD = one slice = one PR [R1-Q9].

**Learn it**

- Text: ["Use-Case 2.0: The Hub of Software Development"](https://web.archive.org/web/20250908161806/https://queue.acm.org/detail.cfm?id=2912151) (Jacobson, Spence, Kerr, ACM Queue 2016, archived copy, ~33 min; the slice definition is in the first third)
- Video: ["Use-Case 2.0: The Hub of Modern Software Development"](https://www.youtube.com/watch?v=p5gDbf0je8k) (Ivar Jacobson, ACM, 58:50)
- *Note:* The free ebook is announced on an [archived Ivar Jacobson International page](https://web.archive.org/web/20250210154328/https://www.ivarjacobson.com/publications/white-papers/use-case-20-e-book); how it downloads today is unverified.

**Key literature**

- Ivar Jacobson, Ian Spence, Kurt Bittner, *Use-Case 2.0: The Guide to Succeeding with Use Cases* (2011)

### 2.4 The extension matrix

- **Roles:** PM [core] · UX [core] · SWE [optional]
- **Time:** ~10 min

**Definition**

A grid that runs each main-scenario step through the failure categories of its kind. **Actor steps** (the actor provides or chooses something) are checked for invalid input, duplicate, no permission, and cancel or abandon. **System steps** (the system looks up, stores or calls something) are checked for not found, conflict or concurrent edit, timeout or external system down, partial failure, quota or limit, and stale data. *Privacy request* is asked once for the whole use case. Every cell is either "n/a", an extension, or `out-of-scope` with a reason.

**Why it matters**

- **PM:** it turns "think of edge cases" into a checklist, so they are found systematically rather than by luck.
- **UX:** each extension becomes a state or a message the screens must show.
- **SWE:** each one becomes a scenario and a test.

**In this framework**

This grid is our own addition to Cockburn's format [R4-Q2]. Splitting it by step kind keeps it short: an 8-step use case needs about 40 answers rather than 88 [R28-Q6]. A use case can't be `Complete` until every step has been through it; each handled extension gets a one-line concrete example, which later becomes its first Gherkin scenario [R28-Q3]; and every extension must later be claimed by a story or marked `deferred` [R1-Q7]. Grid: [`use-case.md`](../templates/use-case.md#failure-category-check); how to run it: [chapter 3, §3.2](../guide/03-design-playbook.md#32-step-1-complete-the-use-case).

**Learn it**

- Text: the extensions part of Cockburn's [Basic use case template](https://web.archive.org/web/20140330001816/http://alistair.cockburn.us/Basic+use+case+template) (archived)
- Text: the worked example in [Use cases vs user stories](use-cases-vs-user-stories.md#a-the-use-case)
- *Note:* No video covers this grid.

**Key literature**

- Alistair Cockburn, *Writing Effective Use Cases* (2000), on finding extension conditions

### 2.5 User stories

- **Roles:** PM [core] · UX [core] · SWE [optional]
- **Time:** ~22 min (+52 min video, optional)

**Definition**

A user story is a short statement of a need from the user's side, usually written with the **Connextra template**: "As a \<role\>, I want \<capability\>, so that \<benefit\>." Ron Jeffries' **three Cs** describe it: a **Card** (the sentence), a **Conversation** (the details) and a **Confirmation** (the tests that show it is done).

**Why it matters**

- **PM:** the "so that" forces a reason for every piece of work.
- **UX:** the conversation is where flows are explored.
- **SWE:** the confirmation is what the code must pass.

**In this framework**

A story is always a path through a use case, never a free-standing wish [R4-Q3]. It lives at the top of its PRD, which starts as the story's Draft [R9-Q1]. The conversation is *Exploring*; the confirmation is English Gherkin [R3-C1]. Its "so that" must trace to a user benefit in PRD §3a [R4-Q4a]. Departure: XP stories are throw-away cards; ours are recorded in the PRD. See [chapter 3, §3.3](../guide/03-design-playbook.md#what-a-user-story-is) and [`story.md`](../templates/story.md).

**Learn it**

- Text: [User Stories](https://www.mountaingoatsoftware.com/agile/user-stories) (Mike Cohn, ~17 min)
- Text: [Essential XP: Card, Conversation, Confirmation](https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/) (Ron Jeffries, 2001, ~3 min)
- Text: [User Story](https://martinfowler.com/bliki/UserStory.html) (Martin Fowler, ~2 min)
- Video: [User Stories Explained](https://www.youtube.com/watch?v=6q5-cVeNjCE) (Mike Cohn, 52:04)
- *Note:* The Connextra template is from Connextra (2001); it is usually credited to Rachel Davies, though no primary source was found.

**Key literature**

- Kent Beck, *Extreme Programming Explained* (1999)
- Mike Cohn, *User Stories Applied* (2004)

### 2.6 INVEST

- **Roles:** PM [core] · UX [optional] · SWE [optional]
- **Time:** ~8 min (+40 min video, optional)

**Definition**

Six qualities of a good story, from Bill Wake: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable.

**Why it matters**

- **PM:** a quick test of whether a story is ready to design.
- **SWE:** a story that fails *E* or *S* is a risk to the slice.

**In this framework**

*Small* means about one week of slice work [R4-Q3]; *Independent* is reached by moving shared work into enabler slices, and means independent of every story except the first of its use case, which the later ones build on [R28-Q8]; *Testable* means its acceptance can be written as Gherkin. Each letter is read for this framework in [chapter 3, §3.3](../guide/03-design-playbook.md#33-step-2-cut-stories).

**Learn it**

- Text: [INVEST in Good Stories, and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/) (Bill Wake, ~8 min)
- Video: [Agile Book Club: User Stories (with Bill Wake)](https://www.youtube.com/watch?v=6i6c-ZiHWs8) (James Shore, 39:49)
- French: [INVESTissez dans de bonnes stories et dans des tâches SMART](http://www.les-traducteurs-agiles.org/2015/02/23/investissez-dans-de-bonnes-stories-et-dans-des-taches-smart.html) (~8 min)
- French: [INVEST : Qu'est-ce qu'une bonne User Story ?](https://www.youtube.com/watch?v=PO4vDYkezgY) (Scrum Life, 10:06)

**Key literature**

- Bill Wake, "INVEST in Good Stories, and SMART Tasks" (2003)

### 2.7 Story mapping

- **Roles:** PM [core] · UX [optional] · SWE [optional]
- **Time:** ~16 min (+56 min video, optional)

**Definition**

A story map lays the steps of a user's journey left to right (the backbone) and the stories for each step underneath, top to bottom by priority. Horizontal cuts across the map are releases that each work end to end.

**Why it matters**

- **PM:** it shows the whole journey at once, so the first releases stay thin but complete.

**In this framework**

An optional technique, with no template. For one use case, the backbone is the main scenario's steps, the cards beneath are the extensions, and each horizontal cut is a story. Departure: Patton maps a whole product journey; we usually map one use case at a time.

**Learn it**

- Text: [The New User Story Backlog is a Map](https://jpattonassociates.com/the-new-backlog/) (Jeff Patton, ~16 min)
- Video: [User Stories & Story Mapping Demystified](https://www.youtube.com/watch?v=5R1z8POfvgQ) (Jeff Patton, 55:53)
- French: [Le User Story Mapping](https://www.youtube.com/watch?v=dvnU_R0mu98) (Scrum Life, 12:44)

**Key literature**

- Jeff Patton, *User Story Mapping* (2014)

### 2.8 Story splitting and vertical slices

- **Roles:** PM [core] · UX [optional] · SWE [optional]
- **Time:** ~45 min

**Definition**

Splitting turns a story that is too big into smaller ones that each still deliver value. A **vertical slice** cuts through every layer (screen, API, business logic, data) for a narrow piece of behaviour; a **tracer bullet** (Hunt & Thomas) is the first such slice, built to prove the path works end to end.

**Why it matters**

- **PM:** small vertical stories ship and teach something every week.
- **SWE:** layer-by-layer work hides integration problems until the end.

**In this framework**

Stories are vertical paths through a use case [R4-Q3]. The first story of a use case is its tracer bullet: the thinnest path through the whole main scenario. Each later story adds extensions or one variation, which is the splitting-by-variation pattern of the Humanizing Work guide below [R28-Q8]. `to-tickets` then cuts a slice into tracer-bullet tickets ([chapter 4, §4.5](../guide/04-dev-playbook.md#45-step-4-cut-the-tickets)) [R4-Q7′].

**Learn it**

- Text: [The Humanizing Work Guide to Splitting User Stories](https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/) (Richard Lawrence & Peter Green, ~30 min)
- Text: [Elephant Carpaccio exercise](https://web.archive.org/web/20150220065851/http://alistair.cockburn.us/Elephant+Carpaccio+exercise) (Cockburn, archived copy, ~5 min)
- Video: [How to Split a User Story](https://www.youtube.com/watch?v=irorOjThcD8) (Humanizing Work, 10:20)
- *Note:* Tracer bullets: no free text found; see the book.

**Key literature**

- Andrew Hunt & David Thomas, *The Pragmatic Programmer* (1999; 20th-anniversary edition 2019)

### 2.9 Shape Up

- **Roles:** PM [core] · UX [optional] · SWE [optional]
- **Time:** ~49 min

**Definition**

Basecamp's method for product work. Work is **shaped** first (rough, solved and bounded) within an **appetite**, a fixed amount of time the team is willing to spend; scope varies, time doesn't. Shaped pitches are **bet** on for six-week cycles, and **breadboards** and **fat-marker sketches** keep early designs rough on purpose.

**Why it matters**

- **PM:** appetite is a disciplined way of saying no to scope.
- **UX:** breadboards and fat-marker sketches are fast ways to explore flows.

**In this framework**

We borrow ideas, not the method. The one-week cap per story is our appetite [R4-Q3]; shaping is close to *Exploring*; a founder's explicit pick plays the part of the bet [R6-Q1]. Departures: there are no six-week cycles or betting table, and sketches are only exploration, because the real-stack prototype is what counts [R1-Q5].

**Learn it**

- Text: [Introduction](https://basecamp.com/shapeup/0.3-chapter-01) (~9 min)
- Text: [Set Boundaries](https://basecamp.com/shapeup/1.2-chapter-03) (appetite, ~10 min)
- Text: [Find the Elements](https://basecamp.com/shapeup/1.3-chapter-04) (breadboarding and fat-marker sketches, ~12 min)
- Video: [Shaping in a Nutshell](https://www.youtube.com/watch?v=h_8M23wVjXk) (Ryan Singer, 17:54)

**Key literature**

- Ryan Singer, [*Shape Up: Stop Running in Circles and Ship Work that Matters*](https://basecamp.com/shapeup) (2019, free online)

### 2.10 Measurable outcomes and product metrics

- **Roles:** PM [core] · UX [optional] · SWE [optional]
- **Time:** ~38 min (+58 min video, optional)

**Definition**

An **outcome** is a change in what users do, not the feature that was shipped (Josh Seiden's "outcomes over output"). Metrics make outcomes visible: Google's **HEART** framework (Happiness, Engagement, Adoption, Retention, Task success; set through Goals → Signals → Metrics); a **North Star metric** that captures the value users get; **customer retention rate**, (customers at end − new customers) ÷ customers at start; and **NPS**, the share of promoters minus the share of detractors.

**Why it matters**

- **PM:** without a signal, nobody can tell whether a PRD worked.
- **SWE:** every metric needs events or logs that the code must emit.

**In this framework**

PRD §3a lists **user benefits**, each with an observable signal, from the first PRD. §3b adds numeric targets once `metrics_stage: growth` [R4-Q4a, R4-Q4b]. Metrics are defined once in the tracking plan's catalogue with `MET-` IDs; customer retention rate is the template's `MET-001` [R8-Q3]. Events (`EVT-`) feed them, and an outcome review closes the loop after `Done` [R4-Q4c, R4-Q4e]. See [chapter 3, §3.5](../guide/03-design-playbook.md#outcome-and-measurement), [chapter 10](../guide/10-outcomes-and-measurement.md), [`tracking-plan.md`](../templates/tracking-plan.md) and [`settings.yaml`](../templates/settings.yaml).

**Learn it**

- Text: the HEART paper above (~18 min)
- Text: [Every Product Needs a North Star Metric](https://amplitude.com/blog/product-north-star-metric) (Amplitude, vendor, ~10 min)
- Text: [Measuring Your Net Promoter Score](https://www.netpromotersystem.com/about/measuring-your-net-promoter-score/) (Bain, ~3 min)
- Text: [Customer retention rate](https://blog.hubspot.com/service/customer-retention-rate) (HubSpot, vendor, ~7 min)
- Video: [Webinar: Outcomes over output with Josh Seiden](https://www.youtube.com/watch?v=o5z4Dj1EhbQ) (Sense & Respond Learning, 58:09)
- *Note:* No free text by Seiden was found; see the book.
- *Note:* Retention sources are vendor pages only.

**Key literature**

- Josh Seiden, *Outcomes Over Output* (2019)
- Kerry Rodden, Hilary Hutchinson, Xin Fu, ["Measuring the User Experience on a Large Scale"](https://research.google.com/pubs/archive/36299.pdf) (CHI 2010, the HEART paper, free)
- Fred Reichheld, "The One Number You Need to Grow" (HBR, 2003)

## 3. Optional concepts

### 3.1 Jobs to be done and personas

- **Roles:** PM [optional] · UX [optional] · SWE [optional]
- **Time:** ~27 min

**Definition**

**Jobs to be done** (Clayton Christensen; Tony Ulwick) says customers "hire" a product to make progress in a situation, so research starts from the job, not the customer's profile. A **persona** (Alan Cooper) is an archetype of a user, built from research, that keeps a team designing for someone specific.

**Why it matters**

- **PM:** they explain *why* a use case matters to someone.
- **UX:** personas anchor design choices.

**In this framework**

Personas, journeys, pain points and blockers are produced **outside** the framework and arrive as inputs in `docs/product/inputs/`; use cases cite them by typed ID, such as `PER-001` [R3-A5, R11-Q11, R30-Q1]. They are not the PM, UX and Eng persona reviewers.

**Learn it**

- Text: [Jobs to Be Done theory](https://www.christenseninstitute.org/theory/jobs-to-be-done/) (Christensen Institute, ~10 min)
- Text: [Personas Make Users Memorable](https://www.nngroup.com/articles/persona/) (NN/g, ~6 min)
- Video: [Clay Christensen: The Jobs to be Done Theory](https://www.youtube.com/watch?v=Stc0beAxavY) (HubSpot, 7:10)
- Video: [Personas 101](https://www.youtube.com/watch?v=rv9yfrV-EAs) (NN/g, 3:42)
- Further: [The Origin of Personas](https://web.archive.org/web/20101229080750/http://www.cooper.com/journal/2003/08/the_origin_of_personas.html) (Alan Cooper, archived copy, ~12 min)
- *Note:* Ulwick's free book sits behind a contact form, and the HBR article is paywalled.

**Key literature**

- Clayton Christensen et al., *Competing Against Luck* (2016)
- Tony Ulwick, *What Customers Want* (2005)
- Alan Cooper, *The Inmates Are Running the Asylum* (1998)

## 4. Context

Ideas that shape how product teams think, but that this framework does not run as a process. Discovery happens before and outside it [R11-Q11].

| Concept | In one line | Learn it |
|---|---|---|
| **Design thinking** | A human-centred loop of empathising, defining, ideating, prototyping and testing (IDEO, Stanford d.school). | [Design Thinking by IDEO](https://designthinking.ideo.com/) (~2 min); [Design Thinking Bootleg](https://dschool.stanford.edu/tools/design-thinking-bootleg) (d.school method cards); video [What is Design Thinking?](https://www.youtube.com/watch?v=ldYzbV0NDp8) (IDEO U, 1:55) |
| **Double Diamond** | Two diamonds: discover and define the right problem, then develop and deliver the right solution, each widening then narrowing (UK Design Council). This framework works in the second diamond. | [The Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) (Design Council, ~4 min); video [Celebrating 20 years of the Double Diamond](https://www.youtube.com/watch?v=5FpKuJSCbx0) (1:13) |
| **IBM Enterprise Design Thinking** | IBM's version for large teams: the Loop (observe, reflect, make), **Hills** (outcome statements for users), **Playbacks** (regular reviews) and **Sponsor users** (real users on the team). Hills resemble our PRD §3a benefits; Playbacks resemble our gate reviews. | [Hills](https://web.archive.org/web/20221221182334/http://www.ibm.com/design/thinking/page/framework/keys/hills/) (IBM, archived copy, ~4 min); video [Enterprise Design Thinking at IBM](https://www.youtube.com/watch?v=8mcClemz_pM) (Eleanor Bartosh, 22:50) |
| **Continuous discovery** | Weekly contact with customers by the team that builds the product, mapped as an opportunity solution tree (Teresa Torres). | [Product Discovery Basics](https://www.producttalk.org/product-discovery/) (Teresa Torres, ~10 min); video [Introduction to Modern Product Discovery](https://www.youtube.com/watch?v=l7-5x0ra2tc) (36:45) |
