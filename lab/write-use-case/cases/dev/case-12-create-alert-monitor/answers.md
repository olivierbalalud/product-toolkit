# Answers: create an alert monitor

## Actor, goal and scope

- The person doing this is a site reliability engineer, or a DevOps engineer; same job for us.
- The system is our observability and alerting platform.
- They start because a new service has just gone to production and needs automated latency and anomaly monitoring.
- Before they start they're signed in with permission to create monitors, and the paging and chat integrations are already set up and authorized; setting those up is a separate job.
- The paging service and the chat service are outside systems; the platform calls on them to test the routing.
- The aggregation can be an average, a maximum or a percentile such as the 99th.
- An alert can be routed to a paging service, a chat channel, or both.
- It happens a few times a month per team, mostly when a new service goes to production.

## Stakeholders and guarantees

- The engineer wants to set up monitoring for the new service in one go, see from past data that the thresholds make sense, and know the alerts will actually reach someone.
- The on-call team wants alerts they can act on, with little noise and an explicit runbook, during critical incidents.
- Product owners want the service level agreements monitored proactively.
- A monitor never evaluates or notifies unless it was activated with consistent thresholds and reachable targets; nothing half-configured is ever left running.
- When it works, the monitor is live and evaluating incoming metrics over its window, the warning and alert thresholds are registered with their recovery thresholds, and the message, runbook link and priority tags are saved with targets the test found active and reachable.
- No personal data is involved: a monitor holds metric queries, thresholds, a message template and team routing targets.

## Main scenario

- Along with the metric, the aggregation and the scope tags, they choose the timeframe of past data to preview.
- The thresholds come with how long the metric has to stay past them before anything fires.
- The warning threshold must always be less severe than the alert threshold.
- Each recovery threshold must be less severe than the threshold it clears; that's what stops alerts flapping.
- The message can use variables such as the host name and the current value; it also carries the runbook link and the priority tags, such as the severity.
- The test of the routing targets is a dry run that confirms each one is active and reachable.
- Activating the monitor happens right after the test, and the engineer is told the monitor is live.

## What can go wrong

- The query is malformed or asks for an aggregation we don't support.
- No data at all came in for that metric and those tags over the previewed timeframe.
- The thresholds conflict: the warning is as severe as the alert or more, or a recovery threshold isn't less severe than the threshold it clears.
- The message uses a variable we don't know, or a routing target is written wrong.
- A routing target is no longer active: an archived chat channel or a deactivated paging service.
- The paging or chat service doesn't answer the test.
- They give up before the monitor is activated.

## How each is handled

- Bad query: the system says what's wrong and they fix it.
- No data: the system says nothing came in for that combination of tags; they either change the tags or confirm anyway, so the monitor watches whatever data arrives from now on, and they go on to the thresholds.
- Conflicting thresholds: the system points out the conflict and won't accept them until they're corrected.
- Unknown variable or malformed target: the system names it and activates nothing; they fix the message or the target.
- Inactive target: nothing is activated, their settings are kept, and the system names the target; they pick an active one and the test runs again.
- Service not answering: nothing is activated, their settings are kept, and the system names the target that didn't answer; they try again or give up, and if they give up no monitor is created.
- Giving up: the settings are thrown away and no monitor exists.

## Durations

- Validating the query and showing the preview of past data takes a few seconds.
- Validating the notification, running the dry run and activating the monitor takes a few seconds too, mainly the round trip to the paging and chat services.

## Out of scope

- A second monitor on the same metric and scope: allowed, for instance with other thresholds; we don't check for one.
- Activating a monitor whose target couldn't be reached: not offered; they fix the target or try again.
