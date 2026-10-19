---
id: PRD-012.1
story: US-012.1
use_case: UC-012
title: <short title>
status: Exploring        # Draft | Exploring | Design-complete | Dev-ready | In development | Done [R1-Q8]
driver: <name>
priority: <number or label>
source_locale: en        # en | fr [R1-Q11]
design_tool: figma       # figma | claude-design; fixed once Exploring starts [R18-Q4]
extensions: [UC-012.2a, UC-012.3a]
adrs: []                 # e.g. [ADR-0007]; a Proposed ADR blocks Dev-ready [R1-Q13]
trds: []                 # e.g. [TRD-012.1]
enablers: []             # e.g. [ENB-004] [R4-Q4d, R5-Q1]
amends: []               # scenarios of earlier PRDs this PRD changes [R4-Q8e′]
amended_by: []           # later PRDs or fix/ branches that changed this PRD's scenarios
open_dcrs: []            # [R7-Q3]
outcome_review_due:      # set at Done: Done date + measurement window [R4-Q4e]
---
<!-- Copied to …/stories/US-012.1-<slug>/prd.md. Section order is fixed [R4-Q4, R4-Q4a]; §1 is the frontmatter above. -->

# PRD-012.1: <title>

## 2. Problem

**Story:** As a <role>, I want <capability>, so that <benefit>.

<!-- The problem in the user's terms: what goes wrong today, for whom, how often. Evidence: cite inputs by ID. -->

## 3. Expected outcome

### 3a. User benefits

<!-- Mandatory from the first PRD [R4-Q4b]. Written from the user's side ("can do X without Y").
     Not "the PRD ships features X/Y/Z" [R4-Q4 amendment]. -->

| Benefit | Observable signal |
|---|---|
| <can do X without Y> | <task completed / time to complete / error rate / support requests / interview feedback> |

### 3b. Success metrics

<!-- Optional while settings.yaml has metrics_stage: discovery; mandatory at growth [R4-Q4b].
     Metrics are defined once in the tracking plan's catalogue; reference them by MET- ID [R8-Q3]. -->

| Metric | Baseline | Target | Window | Leading / lagging |
|---|---|---|---|---|
| MET-003 | | | | |

## 4. Measurement plan

<!-- Each event or log field, entered in docs/product/tracking-plan.md. Every property also goes in §11 [R4-Q4c].
     A missing pipeline, dashboard or BI model is an ENB, linked in frontmatter [R4-Q4d]. -->

| Event | Feeds | Status |
|---|---|---|
| EVT-014 `room_booked` | Benefit 1, MET-003 | planned |

## 5. Scope

- **In scope:** …
- **Out of scope:** …

## 6. Personas and context

<!-- Cite personas and journeys by ID [R3-A5]. Context of use: device, frequency, environment. -->

## 7. Flows

See [`flows.md`](flows.md): flow map, screens, key information and actions, state matrix.

## 8. Copy deck

See [`copy.md`](copy.md).

## 9. Acceptance

<!-- The English .feature files ARE the acceptance criteria. Don't restate them here [R3-C1]. -->

- [`features/<name>.feature`](features/)

## 10. Who may perform each action

<!-- Becomes the authorisation test matrix: every role × action, allowed and denied [R4-Q9]. -->

| Action | <role 1> | <role 2> | <role 3> |
|---|---|---|---|
| <action> | ✅ | ❌ | ✅ own items only |

## 11. Privacy data inventory

<!-- Every personal data item shown, collected, logged or sent to analytics. Becomes the privacy tests [R4-Q9]. -->

| Data | Where | Purpose | Legal basis | Retention | Shown to |
|---|---|---|---|---|---|
| | screen / API / log / analytics event | | | | |

### 11b. AI use

<!-- Only if the PRD uses an AI model [R12-Q6a]. Not legal advice: see docs/foundations/ai-act-one-pager.md. -->

| Item | Answer |
|---|---|
| Model and provider | |
| Data sent to the model (link the rows above) | |
| Human oversight | <who checks or can override the output> |
| Transparency notice to users (AI Act Art. 50) | <copy key of the notice> |
| AI Act risk category | prohibited / high-risk / limited (transparency) / minimal. Prohibited stops the PRD; high-risk needs an ADR with legal advice before Design-complete [R14-Q1]. |
| Eval set | <path to the eval set>, pass threshold <score> [R14-Q5] |
| User or third-party content sent to the model? | yes → prompt-injection threat check in the Eng review [R12-Q6c] |

## 12. Draft API contract

See [`contract.draft.yaml`](contract.draft.yaml). It is written against the fit analysis, [`fit.md`](fit.md) [R4-Q8a]; the prototype mocks against it.

## 13. Accessibility and responsive behaviour

- **Focus order and keyboard use:** …
- **Labels and announcements:** …
- **Breakpoints:** …

## 14. Technical questions

| Question | Raised by | Answer or link |
|---|---|---|
| | SWE persona / fit analysis | ADR-0007 / TRD-012.1 / answered here |

## 15. Open questions

<!-- Must be empty for Dev-ready [R5-Q1]. -->

## 16. Reviews and sign-off

See [`reviews.md`](reviews.md).

## 17. Outcome review

<!-- Filled in on outcome_review_due, after Done [R4-Q4e]. -->

- **Result:** met | missed | inconclusive
- **Numbers:**
- **Follow-up:** new story / DCR on a later PRD / none
