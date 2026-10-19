---
id: UC-012
title: <Goal of the primary actor, as a short active verb phrase>
status: Draft            # Draft | Ready for review | Under review | Complete [R7-Q1]
driver: <name>
priority: <number or label>   # informs the pick, never makes it [R6-Q1]
source_locale: en        # en | fr [R1-Q11]
inputs: []               # IDs of personas, journeys, pain points this use case draws on [R3-A5]
stories: []              # filled when stories are cut: [US-012.1, US-012.2]
---
<!-- Copied to doc/product/use-cases/UC-012-<slug>/use-case.md. Cockburn "fully dressed" format [R1-Q6]. -->

# UC-012: <title>

| Field | Value |
|---|---|
| **Primary actor** | <role> |
| **Scope** | <the system under design> |
| **Level** | User goal <!-- or Summary / Subfunction --> |
| **Trigger** | <what starts it> |
| **Preconditions** | <what must be true before it starts> |
| **Minimal guarantees** | <what is true however it ends, e.g. nothing is half-saved, the attempt is logged> |
| **Success guarantees** | <what is true when the main scenario succeeds> |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| <role> | <what they need protected or achieved> |

## Main success scenario

1. <Actor> <does something>.
2. The system <responds>.
3. …

## Failure-category check

<!-- Run every step through every category [R4-Q2]. Each "yes" becomes an extension below. "n/a" needs no reason; "out-of-scope" does. -->

| Step | Invalid input | Not found | Duplicate | No permission | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon | Privacy request |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | | |
| 2 | | | | | | | | | | | |

## Extensions

<!-- ID = UC-012.<step><letter>. Each one has a handling outcome, or is marked deferred / out-of-scope with a reason [R1-Q7]. -->

- **UC-012.2a** <condition>:
  1. The system <handles it>.
  2. Returns to step <n> / The use case ends.
- **UC-012.3a** <condition>: `deferred`, <reason>.

## Technology and data variations

- <step>: <variation, e.g. file uploaded by drag and drop or by picker>

## Related information

- **Frequency:** <how often>
- **Open issues:** <questions still open>
