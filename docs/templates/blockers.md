<!-- Copied to docs/product/inputs/blockers.md. A blocker is a condition, seen from a customer's or user's side,
     that stops them buying or adopting whatever the product's value. Blockers are unscored [R30-Q4′, R30-Q19].
     Each sits under the earliest stage where it bites [R30-Q5′]. Its text says who is blocked (PER-…), the journey
     stage (JRN-…), the pain point it grew from if any (PP-…), and each cause with one of three words and its evidence:
     product-gap (we can build our way out), external-limit (a third party's system can't do it today),
     legal-or-business (paperwork, contracts, price) [R30-Q6, R30-Q7′, R30-Q15′].
     Three fields only [R30-Q21′]:
       status     open | resolved | accepted; the founders change it in a PR [R30-Q16]
       review_by  only when accepted: the date to look at it again; check-gate warns once it has passed [R30-Q20]
       evidence   only when resolved: a link, or one statement of what was done, who confirmed it, when,
                  and where the proof is kept, without its content [R30-Q18′, R30-Q20]
     Responses cite the blocker, never the reverse: a use case in inputs:, an ADR or an enabler in raised_by:.
     index.md lists them [R30-Q17]. Imported text stays as written; only its IDs are rewritten [R30-Q2]. -->

# Blockers

## Buying

### BLK-001: The DPO can't approve the purchase without a data processing agreement

- **status:** resolved
- **evidence:** Data processing agreement signed with the first customer; confirmed by the CEO on 2026-11-04; kept in the company's contract store.

The customer's DPO (PER-004) will not sign off without a data processing agreement and a record of processing (JRN-003 Qualify). Cause: legal-or-business, no agreement existed (evidence: OBJ-002).

## Adoption

### BLK-002: Staff on the company's calendar suite can't see their bookings in their calendar

- **status:** accepted
- **review_by:** 2027-03-01

Employees (PER-002) book a room but the booking never shows in their calendar, so they forget it and the room is released (JRN-002 Use; grew from PP-007). Cause: external-limit, the calendar suite lets no outside app write events for a company without an admin-approved app (evidence: research note on calendar integration). Accepted for now: those customers are told before signing.

### BLK-003: Rooms can't be booked from a phone

- **status:** open

Employees (PER-002) decide where to meet while walking between meetings; without a phone booking they don't use the product (JRN-002 Use; grew from PP-003). Cause: product-gap, no responsive booking flow (evidence: usability notes, 2026-10).
