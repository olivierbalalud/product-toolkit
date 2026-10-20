<!-- Copied to docs/product/tracking-plan.md, one per product [R4-Q4c]. The analytics or BI tool is chosen
     by an ADR, outside the framework [R4-Q4d]. Every event property is also in the PRD's privacy
     inventory; no personal data in analytics by default [R4-Q4c]. -->

# Tracking plan

## Metric catalogue

<!-- Each metric defined once; PRDs reference it by ID [R8-Q3]. -->

| ID | Name | Formula | Period | Data source | Dimensions | Leading / lagging | Owner |
|---|---|---|---|---|---|---|---|
| MET-001 | Customer retention rate | (customers at end − new customers) ÷ customers at start | month | billing | DIM-001 as-at-event | lagging | founders |
| MET-003 | Booking completion rate | `room_booked` ÷ `booking_started` | week | analytics | DIM-002 as-now | leading | <driver> |

## Dimension catalogue

<!-- Attributes metrics are split by. as-at-event = the value when the event happened; as-now = today's value [R23-Q2].
     A dimension needed as-at-event is captured from the first slice that introduces it: a snapshot property on the
     event (privacy class none only) or a change event / history row with valid-from time [R23-Q3]. -->

| ID | Name | Source (entity.attribute) | Expected change frequency | Privacy class | History needed | Captured as | Changes per month |
|---|---|---|---|---|---|---|---|
| DIM-001 | Customer plan | `organisation.plan` | a few times a year | none | yes | snapshot on events / `organisation_plan_changed` | ~10 |
| DIM-002 | Room size | `room.capacity` | rarely | none | no | — | — |

## Events

<!-- ID plus a snake_case name, since analytics tools key events by name [R8-Q4].
     Privacy class per property: none | pseudonymous | personal. `personal` needs a reason recorded in the
     PRD's privacy inventory, and the privacy reviewer flags it [R9-Q2].
     Consent per event: `exempt` only if it meets every CNIL audience-measurement condition (publisher-only audience
     measurement, anonymous statistics, no cross-referencing or passing on, no cross-site tracking); otherwise
     `required`, and the event is sent only after the user consents. The privacy reviewer checks it [R21-Q1]. -->

| ID | Name | Trigger | Properties (name: type, privacy class) | Consent | Feeds | PRDs | Per day | Status |
|---|---|---|---|---|---|---|---|---|
| EVT-013 | `booking_started` | Booking form opened | `room_size: int, none` | exempt | MET-003 | PRD-012.1 | ~200 | planned |
| EVT-014 | `room_booked` | Booking confirmed | `duration_min: int, none` | exempt | MET-003 | PRD-012.1 | ~150 | planned / emitted |
