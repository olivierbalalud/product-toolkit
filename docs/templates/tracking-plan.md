<!-- Copied to docs/product/tracking-plan.md, one per product [R4-Q4c]. The analytics or BI tool is chosen
     by an ADR, outside the framework [R4-Q4d]. Every event property is also in the PRD's privacy
     inventory; no personal data in analytics by default [R4-Q4c]. -->

# Tracking plan

## Metric catalogue

<!-- Each metric defined once; PRDs reference it by ID [R8-Q3]. -->

| ID | Name | Formula | Period | Data source | Leading / lagging | Owner |
|---|---|---|---|---|---|---|
| MET-001 | Customer retention rate | (customers at end − new customers) ÷ customers at start | month | billing | lagging | founders |
| MET-003 | Booking completion rate | `room_booked` ÷ `booking_started` | week | analytics | leading | <driver> |

## Events

<!-- ID plus a snake_case name, since analytics tools key events by name [R8-Q4].
     Privacy class per property: none | pseudonymous | personal. `personal` needs a reason recorded in the
     PRD's privacy inventory, and the privacy reviewer flags it [R9-Q2].
     Consent per event: `exempt` only if it meets every CNIL audience-measurement condition (publisher-only audience
     measurement, anonymous statistics, no cross-referencing or passing on, no cross-site tracking); otherwise
     `required`, and the event is sent only after the user consents. The privacy reviewer checks it [R21-Q1]. -->

| ID | Name | Trigger | Properties (name: type, privacy class) | Consent | Feeds | PRDs | Status |
|---|---|---|---|---|---|---|---|
| EVT-013 | `booking_started` | Booking form opened | `room_size: int, none` | exempt | MET-003 | PRD-012.1 | planned |
| EVT-014 | `room_booked` | Booking confirmed | `duration_min: int, none` | exempt | MET-003 | PRD-012.1 | planned / emitted |
