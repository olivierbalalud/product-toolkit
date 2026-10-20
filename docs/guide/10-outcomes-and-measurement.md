# 10. Outcomes and Measurement

How a PRD states what it should achieve, how that is measured, and how the result is checked after the slice ships. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). Concepts are in the [PM lens](../foundations/pm-lens.md#29-measurable-outcomes-and-product-metrics).

## 10.1 Principles

1. **Outcome, not output.** A PRD's outcome is what the user gains and what the business can measure, never "the PRD ships features X, Y and Z" [R4-Q4].
2. **Every story has a reason that can be seen.** The story's "so that" traces to a user benefit in PRD §3a, and each benefit has an observable signal [R4-Q4a].
3. **Numbers when the product is ready for them.** Numeric targets are optional while the product is in discovery, and mandatory once it is in growth [R4-Q4b].
4. **No measurement without the code to produce it.** Every metric needs events or log fields that the slice emits and tests [R4-Q4c].
5. **No personal data in analytics by default**, and consent where French law requires it [R4-Q4c, R9-Q2, R21-Q1].

## 10.2 In the PRD

| Section | Contents | Decision |
|---|---|---|
| **§3a User benefits** | What the user can expect, in their terms ("can do X without Y"), each with an observable signal: task completed, time to complete, error rate, support requests, interview feedback. Mandatory from the first PRD. | R4-Q4a, R4-Q4b |
| **§3b Success metrics** | Per metric: its `MET-` ID, baseline, target, measurement window, leading or lagging. Optional at `metrics_stage: discovery`, mandatory at `growth`. | R4-Q4a, R4-Q4b, R8-Q3 |
| **§4 Measurement plan** | Each event or log field the PRD needs, with its `EVT-` ID, what it feeds, and its status (`planned`, `emitted`). | R4-Q4c, R8-Q4 |
| **§17 Outcome review** | Filled in after Done: result, numbers, follow-up. | R4-Q4e |

**Business metrics** come in once the product is more mature: for example the **customer retention rate** (CRR), churn, or NPS [R4-Q4 amendment]. Retention rate and churn are close to two views of one number, which is why every metric is defined once, in the catalogue.

## 10.3 The product stage

`docs/product/settings.yaml` holds `metrics_stage: discovery | growth` [R4-Q4b, R8-Q2]. The founders switch it, for example after the first paying customers. The gate check reads it: at `growth`, a PRD can't pass Design-complete without §3b.

## 10.4 The tracking plan

One per product: `docs/product/tracking-plan.md`, from [`tracking-plan.md`](../templates/tracking-plan.md) [R4-Q4c].

**Metric catalogue** [R8-Q3]: each metric is defined once, with its `MET-NNN` ID, name, formula, period, data source, leading or lagging, and owner. PRDs refer to metrics by ID, so two PRDs can't define "retention" two ways.

**Dimension catalogue** [R23-Q2]: the attributes metrics are split by, such as a customer's plan or a company's size. Each dimension gets a `DIM-NNN` ID, its name, the entity and attribute it comes from, how often it is expected to change, its privacy class, whether its history is needed, and, when it is, the expected number of changes per month [R23-Q4]. Each metric lists its dimensions, each marked **`as-at-event`** (the value when the event happened) or **`as-now`** (today's value). "Retention by plan" gives different numbers under each, so the PRD decides which it means.

**Events** [R8-Q4, R9-Q2, R21-Q1]:

| Field | Rule |
|---|---|
| ID and name | `EVT-NNN` plus a name in the form `object_action`, past tense, English, snake_case (`room_booked`, `booking_cancelled`), because analytics tools key events by name. The gate check checks names against the tracking plan [R22-Q2] |
| Trigger | What makes the code emit it |
| Properties | Name, type and **privacy class** (`none`, `pseudonymous`, `personal`). `personal` needs a reason in the PRD's privacy inventory, and the privacy reviewer flags it. Every property is also listed in the PRD's §11 inventory |
| Consent | `exempt` only if the event meets every CNIL audience-measurement condition (audience measurement for the publisher alone, anonymous statistics only, no cross-referencing or passing on, no cross-site tracking); otherwise `required`, and it is sent only after the user consents ([GDPR one-pager](../foundations/gdpr-one-pager.md)) |
| Feeds | The benefit or `MET-` metric it serves |
| Expected volume | Events per day, as input to the BI and observability ADRs [R23-Q4] |
| Status | `planned` until a slice emits it, then `emitted`; `deprecated` once replaced |

**Changing an event** [R22-Q3]: an event's meaning never changes under the same name. Adding an optional property is allowed. Removing or retyping a property, or changing the trigger, creates a **new** event, and the old one is marked `deprecated`, so data before and after stays comparable.

## 10.5 In the slice

- Events go through an **analytics port** in the business layer. Tests assert them with the port's **fake**, which records what was emitted [R4-Q4c].
- **Done** requires the PRD's events to be emitted, asserted in tests, and visible on staging ([chapter 1, §1.8](01-lifecycle-and-gates.md#18-in-development--done)) [R4-Q4c].
- **History is captured from the first slice** that introduces a dimension needed `as-at-event`, because history that isn't captured can't be rebuilt later [R23-Q3]. Either as a **snapshot** property on the event, allowed only if the dimension's privacy class is `none`, or as a **change event** (`<object>_changed`) or a history row with a valid-from time in the operational database. The fit analysis says which applies; the privacy reviewer checks it.
- If the real pipeline, event store, dashboard or BI model doesn't exist yet, the PRD links an **enabler slice** for it. That enabler doesn't block Dev-ready, because the slice is built against the fake, but it must be done before the outcome review [R4-Q4d].
- **Choosing the analytics or BI tool** is an infrastructure decision, made by ADR, outside this framework [R4-Q4d]. So is **how the warehouse keeps history**: slowly changing dimension types, warehouse tables, change-capture tooling and ingest patterns. The framework only records what each metric means in time and what history is needed, as input to that ADR. Observability (logs, metrics, traces) is a separate stack, also outside the framework [R23-Q1].

## 10.6 The outcome review

[R4-Q4e]

1. At Done, the PRD's `outcome_review_due:` is set to the Done date plus the measurement window: the longest window in §3b, or the default in `settings.yaml` (**4 weeks**), which a PRD may override [R22-Q1].
2. On that date, the driver fills in §17: result `met`, `missed` or `inconclusive`; the numbers; and the follow-up: a new story, a DCR on a later PRD, or nothing.
3. The generated `docs/product/index.md` lists overdue reviews.

The lifecycle has no status after `Done`; the review is a section of the PRD, not a gate. A `Done` PRD is otherwise a point-in-time record and is not rewritten [R4-Q8e′].
