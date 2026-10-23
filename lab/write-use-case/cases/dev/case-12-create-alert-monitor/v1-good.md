* **Use Case ID:** UC-B2B-04
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Site Reliability Engineer (SRE) / DevOps Engineer
* **Scope:** Datadog SaaS (Observability & Alerting Platform)
* **Stakeholders & Interests:**
  * *On-Call Engineering Team:* Needs actionable, low-noise alerts with explicit runbooks during critical incidents.
  * *Product Owners:* Need assurance that service level agreements (SLAs) are monitored proactively.
* **Preconditions:**
  1. The target infrastructure or service emits metrics (e.g., `trace.http.request.duration`) ingested within the last 24 hours.
  2. Integration webhooks (e.g., PagerDuty service key, Slack ops channel) are configured and authorized.
* **Success Guarantees (Postconditions):**
  1. The monitor rule is actively evaluating incoming telemetry against defined temporal windows.
  2. Multi-tier thresholds (Warning vs. Critical) are registered with explicit hysteresis conditions.
  3. Escalation notification templates and priority tags (e.g., `severity:p1`) are saved and associated with notification endpoints.
* **Trigger:** A new microservice is deployed to production requiring automated anomaly and latency monitoring.

**Main Success Scenario (MSS):**
1. Actor specifies the metric query, aggregation function (e.g., `p99`), and filtering tags (e.g., `env:production`, `service:payments`).
2. System evaluates the query syntax and renders historical metric previews across the requested timeframe.
3. Actor defines the evaluation conditions, specifying threshold values for `Alert` (> 800ms) and `Warning` (> 500ms) sustained over a 5-minute sliding window.
4. Actor configures alert recovery thresholds to establish hysteresis and prevent alert flapping.
5. Actor authors the contextual notification payload, embedding dynamic variables (`{{host.name}}`, `{{value}}`), troubleshooting runbook URLs, and routing targets (`@pagerduty-payments-sev1`).
6. System validates notification channel syntax and runs a dry-run test against active downstream channels.
7. System activates the monitor and queues it in the distributed evaluation engine.

**Extensions (Alternate & Failure Paths):**
* **2a. Specified metric has had zero ingestion points over the selected retrospective window:**
  * 2a1. System notifies Actor of missing telemetry for the combination of scope tags.
  * 2a2. Actor modifies the tag filters or confirms monitor creation to evaluate future ingested streams.
* **4a. The Warning threshold is configured higher than or equal to the Alert threshold:**
  * 4a1. System highlights the logic conflict and blocks submission.
  * 4a2. Actor corrects the threshold relationship to proceed.
* **6a. Downstream notification routing references an archived channel or deactivated PagerDuty service:**
  * 6a1. System flags the unreachable destination target.
  * 6a2. Actor selects an active notification channel.
