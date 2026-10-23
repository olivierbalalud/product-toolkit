# Cases

One row per case, `dev/` and `holdout/` alike. See the [lab README](../README.md#where-to-put-your-use-cases).

**Shapes.** The held-out set must cover `wait-point`, `long`, `background`, `time-trigger` and `many-extensions`. Other shapes worth tracking: `any-step-ext` (an extension written `*a`), `range-ext` (an extension on a range of steps, such as `2–3a`), `nested-ext` (a sub-extension, such as `3a1`), `external-service` (a step that calls an outside system and can fail), `unkeyed-ext` (exceptions written as "If …" prose, not keyed to steps). Shapes describe v1, as judged from its text.

**Held out** (2026-10-23): 04 (`many-extensions`), 15 (`time-trigger`), 20 (`wait-point`), 23 (`long`, `background`). The other 20 cases are `dev`.

| Case | Product (alias) | Language | Shapes | Split | Notes |
|---|---|---|---|---|---|
| `case-01-order-meal` | Cafeteria meal ordering (B2B) | en | `many-extensions`, `any-step-ext`, `nested-ext` | dev | Wiegers, COS UC-1, 12 steps condensed to 8 |
| `case-02-create-reservation` | Hotel property management (B2B) | en | `external-service`, `nested-ext` | dev | AIUP example; UI words in the source's steps rewritten as intent. Deposit taken in extension 6a, not in the main scenario |
| `case-03-submit-expense-report` | Expense management (B2B) | en | `wait-point` | dev | v2 is a real weak use case (Oracle WebSynergy) that bundles submit and approve; v1 ends at *Pending approval*, with approving as its own use case |
| `case-04-process-sale` | Retail point of sale (B2B) | en | `many-extensions`, `any-step-ext`, `nested-ext`, `external-service` | holdout | Larman, NextGen POS. Extension 6a stores the sale and forwards it when the back-end service returns |
| `case-05-enroll-in-seminar` | University student information (B2B) | en | — | dev | Ambler, UC 17; screen IDs removed. System steps bundle a check with a presentation (steps 2 and 4) |
| `case-06-edit-article` | Wiki platform (B2C) | en | `range-ext` | dev | Wikipedia example. Extensions `2–3a` to `2–3c` use the range form; session expiry and edit conflict on step 4 |
| `case-07-buy-product` | Online store (B2C) | en | `external-service` | dev | Fowler, casual form completed. v2 is a narrative paragraph with no numbered steps |
| `case-08-buy-stocks` | Personal finance app (B2C) | en | `wait-point`, `external-service` | dev | Cockburn, Use Case 1. Extension 4b defers the brokerage's acknowledgement; 4a is an open issue in the source |
| `case-09-configure-webhook` | Payment platform webhooks: Stripe (B2B) | en | `external-service` | dev | Gemini set. Step 6 has the outside endpoint as its subject; extension 5a has a 5-second timeout |
| `case-10-convert-lead` | CRM lead conversion: HubSpot (B2B) | en | — | dev | Gemini set. Duplicate-company check (2a) |
| `case-11-run-offcycle-payroll` | Payroll: Gusto (B2B) | en | `background`, `external-service` | dev | Gemini set. Ends with the batch queued for clearing; banking cutoff and holiday rule (4a) |
| `case-12-create-alert-monitor` | Observability alerts: Datadog (B2B) | en | `external-service` | dev | Gemini set. Three actor steps in a row (3–5); metric syntax in steps |
| `case-13-publish-component-library` | Design library publishing: Figma (B2B) | en | — | dev | Gemini set. Concurrent publication (5a) |
| `case-14-create-blend-playlist` | Shared playlist: Spotify (B2C) | en | `wait-point`, `time-trigger` | dev | Gemini set. v1 keeps the recipient's acceptance (step 4) inside the scenario, although it can come up to 48 hours later; schedules a daily refresh |
| `case-15-schedule-social-post` | Social post scheduling: Canva (B2C) | en | `time-trigger`, `external-service` | holdout | Gemini set. Publishing at the chosen time is a time-triggered continuation |
| `case-16-recover-streak` | Language learning streak: Duolingo (B2C) | en | `nested-ext` | dev | Gemini set. 48-hour grace period and local midnight in the preconditions; sub-extension 2a2a |
| `case-17-add-channel-members` | Team chat: Slack (B2B) | en | `unkeyed-ext` | dev | OpenAI set. Steps 1–2 describe navigation (opens the channel, opens member management) |
| `case-18-create-work-item` | Issue tracking: Jira (B2B) | en | `unkeyed-ext` | dev | OpenAI set. Every main-scenario step but the last is an actor step |
| `case-19-schedule-meeting` | Video meetings: Zoom (B2B) | en | `unkeyed-ext`, `external-service` | dev | OpenAI set. Calendar integration as the outside service |
| `case-20-book-home` | Short-term rental: Airbnb (B2C) | en | `wait-point`, `unkeyed-ext` | holdout | OpenAI set. A reservation request waits for the host; close to case 02, but the guest books for themselves and the host decides |
| `case-21-import-contacts` | Email marketing (B2B) | en | `long`, `many-extensions` | dev | Written for the lab. Cancel rolls the import back (6a); consent basis and plan limit before the long step |
| `case-22-generate-presentation` | AI presentation generator (B2C) | en | `long`, `external-service` | dev | Written for the lab. Cancel keeps or discards finished slides (6a); partial failure (6b); the actor may leave and the deck is still saved (6c) |
| `case-23-connect-bank-feed` | Small-business accounting (B2B) | en | `long`, `external-service`, `background` | holdout | Written for the lab. Actor authenticates at the bank inside the scenario (step 3); an interrupted import continues in the background (6b) |
| `case-24-translate-document` | Document translation (B2B) | en | `long` | dev | Written for the lab. Cancel and failure charge nothing (4a, 4b); files deleted after 24 hours (6a) |

## Not imported

Dropped from the two sets added on 2026-10-23, as the same product or the same goal as a case above:

| Use case | Set | Reason |
|---|---|---|
| Convert a qualified lead in Salesforce | OpenAI §2 | Same goal as case 10 |
| Create a sales deal in HubSpot | OpenAI §4 | Same product as case 10 |
| Create and populate a playlist in Spotify | OpenAI §6 | Same product as case 14 |
| Complete a daily learning lesson in Duolingo | OpenAI §7 | Same product as case 16 |
