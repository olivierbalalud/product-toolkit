---
id: UC-012
title: Create an alert monitor
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-012: Create an alert monitor

| Field | Value |
|---|---|
| **Primary actor** | Site reliability engineer (or DevOps engineer) |
| **Supporting actors** | Paging service and chat service (the routing targets tested at step 6) |
| **Scope** | Observability and alerting platform |
| **Level** | User goal |
| **Trigger** | A new service is deployed to production and needs automated latency and anomaly monitoring. |
| **Preconditions** | The engineer is signed in with permission to create monitors; the integrations with the paging service and the chat service are configured and authorized. |
| **Minimal guarantees** | No monitor evaluates metrics or sends notifications unless it is activated at step 6 with consistent thresholds and reachable routing targets; nothing half-configured is left active. |
| **Success guarantees** | The monitor is active and evaluates incoming metrics over its evaluation window; its Warning and Alert thresholds are registered with their recovery thresholds; its notification message, runbook link and priority tags are saved with routing targets that the dry run found active and reachable. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Site reliability engineer | Sets up monitoring for the new service in one sitting, sees from past data that the thresholds make sense, and knows the alerts will reach someone. |
| On-call engineering team | Gets actionable, low-noise alerts with an explicit runbook during critical incidents. |
| Product owners | The service level agreements are monitored proactively. |

## Main success scenario

1. (actor) The engineer specifies the metric to watch: the metric, its aggregation, the scope tags such as environment and service, and the timeframe to preview.
2. (system, wait) The system validates the query and presents a preview of the metric's history over that timeframe.
3. (actor) The engineer sets the Warning and Alert thresholds and how long the metric must stay past them (BR-1).
4. (actor) The engineer sets the recovery thresholds, so that an alert does not flap (BR-2).
5. (actor) The engineer writes the notification message, with variables such as the host name and the current value, adds the runbook link and the priority tags, and chooses the routing targets.
6. (system, wait) The system validates the notification, confirms with a dry run that each routing target is active and reachable, activates the monitor so that it starts evaluating incoming metrics, and confirms to the engineer that the monitor is active.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-012.1a | out-of-scope: a second monitor on the same metric and scope is allowed, for instance with other thresholds; the system does not look for one | n/a | yes: UC-012.1-5a |
| 3 | yes: UC-012.3-4a | n/a | n/a | yes: UC-012.1-5a |
| 4 | yes: UC-012.3-4a | n/a | n/a | yes: UC-012.1-5a |
| 5 | yes: UC-012.5a | n/a | n/a | yes: UC-012.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-012.2a | n/a | n/a | n/a | n/a | n/a | n/a |
| 6 | yes: UC-012.6a | n/a | yes: UC-012.6b | yes: UC-012.6a, UC-012.6b | n/a | n/a | n/a |

**Privacy request:** no: the monitor holds metric queries, thresholds, a message template and team routing targets, not personal data.

## Extensions

- **UC-012.1-5a** The engineer abandons before the monitor is activated:
  1. The system discards the monitor's settings; no monitor is created.
  2. The use case ends.

  *Example:* Kenji has set the thresholds for the checkout service when he is pulled into an incident and closes the session; no monitor is created.
- **UC-012.1a** The query is malformed or uses an aggregation the system does not support:
  1. The system says what is wrong with the query.
  2. Returns to step 1.

  *Example:* Kenji asks for the "p999" aggregation of the request duration; the system says it does not exist, and he chooses the 99th percentile.
- **UC-012.2a** The metric has no data points for the scope tags over the previewed timeframe:
  1. The system says that no data was received for that combination of scope tags.
  2. The engineer changes the scope tags: returns to step 1. Or the engineer confirms the monitor so that it evaluates data received from now on: continues at step 3.

  *Example:* Kenji scopes the request duration to the new checkout service, deployed this morning and not yet receiving traffic; the preview of the past day is empty, and he confirms the monitor so it evaluates data as traffic arrives.
- **UC-012.3-4a** The thresholds conflict: the Warning threshold is as severe as the Alert threshold or more (BR-1), or a recovery threshold is not less severe than the threshold it clears (BR-2):
  1. The system highlights the conflict and does not accept the thresholds.
  2. Returns to step 3, where the engineer corrects them.

  *Example:* Marta sets the Warning at 900 ms and the Alert at 800 ms for the payments service; the system flags the conflict, and she lowers the Warning to 500 ms.
- **UC-012.5a** The notification message uses a variable the system does not know, or a routing target is malformed:
  1. The system names the unknown variable or the malformed target and activates nothing.
  2. Returns to step 5.

  *Example:* Marta's message refers to a variable "hostname", which does not exist; the system names it, and she uses the host name variable instead.
- **UC-012.6a** A routing target is no longer active: an archived chat channel or a deactivated paging service:
  1. The system activates nothing, keeps the monitor's settings and names the unreachable target.
  2. The engineer chooses an active target in its place: returns to step 6.

  *Example:* Marta routes the alert to the payments team's paging service and to the "payments-ops" chat channel, archived last month; the dry run flags the channel, and she routes to "payments-incidents" instead.
- **UC-012.6b** The paging service or the chat service does not answer the dry run:
  1. The system activates nothing, keeps the monitor's settings and names the target that did not answer.
  2. The engineer tries again: returns to step 6. Or the engineer abandons: no monitor is created and the use case ends.

  *Example:* During Marta's dry run the paging service does not answer; nothing is activated, her settings are kept, and her second try two minutes later succeeds.

## Technology and data variations

- 1: the aggregation is an average, a maximum or a percentile such as the 99th.
- 5: the routing targets are a paging service, a chat channel, or both.

## Related information

- **Frequency:** a few times a month per team, typically when a new service goes to production.
- **Business rules:** BR-1 the Warning threshold is less severe than the Alert threshold (step 3, UC-012.3-4a) · BR-2 each recovery threshold is less severe than the threshold it clears, so that an alert does not flap (step 4, UC-012.3-4a).
- **Related use cases:** Configure Notification Integration.
- **Open issues:** None
