# Use Cases vs User Stories

Two tools that are often treated as rivals. In this framework they work together: the **use case** finds every way a goal can succeed or fail, and **user stories** cut that goal into pieces that can be designed, built and shipped one at a time. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

- **Time:** ~17 min of reading (+64 min video, optional)

**Learn it**

- Text: [Use Cases And Stories](https://martinfowler.com/bliki/UseCasesAndStories.html) (Martin Fowler, ~2 min)
- Text: [Advantages of User Stories over Requirements and Use Cases](https://www.mountaingoatsoftware.com/agile/advantages-of-user-stories-for-requirements) (Mike Cohn, ~9 min)
- Text: [Unifying user stories, use cases, story maps](https://alistaircockburn.com/Unifying%20us%20uc%20sm.pdf) (Alistair Cockburn, slides, ~6 min)
- Video: [Use Cases and User Stories: Perfect Partners with Mike Cohn](https://www.youtube.com/watch?v=yT3FLPR8OFU) (Ivar Jacobson International, 1:04:14)
- Further: the free chapter 0 of Cockburn's [*Unifying User Stories, Use Cases, Story Maps*](https://alistaircockburn.com/UnifyingV2_chapter0.pdf) (2nd ed.)

## 1. Side by side

| Dimension | Use case | User story | In this framework |
|---|---|---|---|
| **Origin** | Ivar Jacobson, late 1980s (*OOSE*, 1992); written style by Alistair Cockburn (*Writing Effective Use Cases*, 2000) | Kent Beck and Extreme Programming, late 1990s; the "As a… I want… so that…" template from Connextra (2001); Mike Cohn, *User Stories Applied* (2004) | Both are used, in that order |
| **Purpose** | Describe how an actor reaches a goal with the system, and everything that can go wrong on the way | Plan and deliver a small piece of value, and start a conversation about it | The use case is the **analysis** tool; the story is the **delivery** unit [R1-Q9] |
| **Format** | Structured text: actor, preconditions, guarantees, a numbered main scenario, numbered extensions | One sentence on a card, plus a conversation and acceptance tests (the three Cs) | Cockburn "fully dressed" use case [R1-Q6]; Connextra sentence at the top of the PRD; acceptance as English Gherkin [R3-C1] |
| **Granularity** | One user goal ("sea level" in Cockburn's [goal levels](pm-lens.md#22-goal-levels)): one actor, one sitting, goal reached | Small enough to finish in an iteration; can be split much finer | Use cases are **always** at the user-goal level, never summary or subfunction [R28-Q1]; a story is about one week of slice work at most [R4-Q3] |
| **Emphasis** | Completeness of behaviour, including failure | Value to the user, and negotiation of the solution | Completeness first (the use case gate), value second (the story's "so that" traces to PRD §3a) [R4-Q2, R4-Q4a] |
| **Failure paths** | Explicit: each extension names a condition and how it is handled | Not part of the format; usually found in conversation or tests, so easily missed | Every main-scenario step is checked against the failure categories of its kind (actor or system), each extension gets a concrete example, and every extension must be claimed by a story or marked `deferred` / `out-of-scope` [R4-Q2, R1-Q7, R28-Q3, R28-Q6] |
| **Lifespan** | Long-lived: a description of behaviour that is kept up to date | Short-lived: often discarded once delivered | The use case and the `.feature` files on `main` stay current; the PRD that carries a story becomes a point-in-time record at `Done` [R4-Q8e′] |

## 2. One feature, both forms

A generic feature: a **member** adds a **document** to a **folder** in a shared workspace. The IDs (`UC-021`, `US-021.1` …) follow [chapter 2](../guide/02-artifacts-and-ids.md).

### (a) The use case

| Field | Value |
|---|---|
| **Use case** | UC-021: Upload a document |
| **Primary actor** | Member |
| **Scope / level** | The application / user goal |
| **Trigger** | The member wants to add a document to a folder |
| **Preconditions** | The member is signed in and can see the folder |
| **Minimal guarantees** | No partial document is ever stored; the attempt is logged, without the file's content |
| **Success guarantees** | The document is stored in the folder, visible to the folder's members, and the member is told |

**Why this is a user goal.** It passes Cockburn's coffee-break test ([goal levels](pm-lens.md#22-goal-levels)): one member, in one sitting, leaves with the document in the folder. "Manage the team's documents" would be a summary goal, a map of several use cases like this one; "choose a file" would be a subfunction, which is step 3 here, not a use case of its own [R28-Q1].

**Main success scenario**, each step marked by kind and written as intent, not screens [R28-Q6, R28-Q7]:

1. (actor) The member asks to add a document to a folder.
2. (system) The system states the accepted formats and the maximum size.
3. (actor) The member provides a file.
4. (system) The system checks the file and transfers it, reporting progress.
5. (system) The system stores the document in the folder and confirms.

**Extensions**, found by running each step through the categories of its kind ([chapter 3, §3.2](../guide/03-design-playbook.md#32-step-1-complete-the-use-case)), each with a concrete example [R28-Q3]:

- **UC-021.1a** *No permission*: the member can see the folder but may not add to it. The system does not offer the upload and says who can grant access. The use case ends.
  *Example:* Léa, a guest in "Projects", asks to add a file; she is told that Sam, the folder's owner, can grant access.
- **UC-021.3a** *Invalid input*: the file's format is not accepted, or it is too large. The system says which limit was broken. Back to step 3.
  *Example:* Sam provides a 2 GB video where the limit is 100 MB; he is told the size limit.
- **UC-021.4a** *Conflict*: a document with the same name already exists in the folder. The system offers to keep both, under a new name, or to cancel. Continue at step 5, or end.
  *Example:* Sam uploads "budget.xlsx" to a folder that already holds one; he keeps both, and his becomes "budget (2).xlsx".
- **UC-021.4b** *External system down*: storage is unavailable or the connection drops. Nothing is stored; the system asks the member to try again. Back to step 3.
  *Example:* the connection drops at 60 %; nothing appears in the folder and Sam is asked to try again.
- **UC-021.4c** *Cancel*: the member cancels while the file transfers (step 4). Nothing is stored. The use case ends.
  *Example:* Sam stops the transfer at 30 %; the folder is unchanged.
- **UC-021.4d** *Quota reached*: the workspace has no storage left. The system explains and says who can raise the limit. The use case ends.
  *Example:* the workspace has used its 10 GB; Sam is told that an administrator can raise the limit.

The other categories were checked too. **Privacy request:** yes, but erasing a member's documents is its own use case, so this one points to it.

### (b) Stories cut from it

Each story is a vertical path through the use case that delivers value on its own [R4-Q3]. The first is the thinnest path through the whole main scenario; each later one adds extensions [R28-Q8]:

| Story | Statement | Path through UC-021 |
|---|---|---|
| **US-021.1** | As a member, I want to upload a document to a folder, so that the people I work with find it in one place. | Steps 1–5, plus 1a and 3a |
| **US-021.2** | As a member, I want to be warned when a document with the same name already exists, so that I never overwrite someone else's version. | 4a |
| **US-021.3** | As a member, I want a cancelled or failed upload to leave nothing behind, so that I can simply try again. | 4b, 4c |

Extension 4d (*quota reached*) is claimed by no story yet.

### (c) One scenario

The acceptance of US-021.1, for extension 3a, in English Gherkin, written during *Exploring* from the extension's example. The scenario sits under the plain-English rule it illustrates, and describes UI text in domain words, not copy keys [R28-Q10, R28-Q16]:

```gherkin
@US-021.1
Feature: Upload a document

  Rule: A file over the size limit or in an unaccepted format is never stored

    @UC-021.3a @ui
    Scenario: Reject a file that is too large
      Given I am a member of the "Projects" folder
      When I upload a 2 GB file where the limit is 100 MB
      Then no document is added to the folder
      And I am told the file is over the size limit
```

### (d) What `coverage.md` shows

`coverage.md` is generated from the stories' `extensions:` and the scenario tags, never written by hand [R3-Q1b]:

| Extension | Stories | Scenarios | Status |
|---|---|---|---|
| Main scenario | US-021.1 | 1 | covered |
| UC-021.1a | US-021.1 | 1 | covered |
| UC-021.3a | US-021.1 | 2 | covered |
| UC-021.4a | US-021.2 | 2 | covered |
| UC-021.4b | US-021.3 | 1 | covered |
| UC-021.4c | US-021.3 | 1 | covered |
| UC-021.4d | — | — | **unclaimed: no story claims it** |

The gap on 4d stays visible until a story claims the extension or someone marks it `deferred` with a reason.

## 3. How they complement each other

- **The use case finds the edge cases; stories deliver them.** Thinking in stories alone tends to produce the happy path. The failure-category grid makes failure paths appear systematically, and each extension's example makes it concrete, before any story is written ([chapter 1, §1.3](../guide/01-lifecycle-and-gates.md#13-before-a-prd-exists-the-use-case-gate)).
- **Stories make the use case deliverable.** A whole use case is usually too big for one slice. Cutting it into vertical paths ([chapter 3, §3.3](../guide/03-design-playbook.md#33-step-2-cut-stories)) gives pieces that pass INVEST and ship in about a week. Jacobson's *Use-Case 2.0* calls the same idea **use-case slices**; Cockburn's *Unifying* book says the same.
- **`coverage.md` ties the two together.** Every extension is either covered by a story's scenarios or explicitly deferred, so nothing is silently dropped [R1-Q7].
- **Gherkin is the confirmation of both.** A scenario is tagged with its story and the use-case step or extension it covers, so the same file proves the story is done and the use case is handled.
- **Each lives as long as it is useful.** The use case and the scenarios on `main` describe current behaviour; the story's PRD records why and how one piece was built [R4-Q8e′].
