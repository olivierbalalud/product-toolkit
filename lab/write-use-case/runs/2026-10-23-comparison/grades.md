# Grades: drafts A and B against gold

Criteria are the 15 of `docs/research/use-case-quality.md` (Q1 to Q15). "Invented" counts content the gold doesn't have and that a product owner hadn't decided, including items the draft marks as "recommendation" or lists under open issues.

## case-01-order-meal

| Draft | Coverage | Invented | Quality | Criteria failed | Form issues |
|---|---|---|---|---|---|
| A | 9 | 2 | 9 | none clearly. Q13 is borderline: 7b's "lowers the quantity" is an odd way to recover from a full window | No system step presents the delivery windows, so 4d ("no window left") is keyed to actor step 4 and no grid cell cites it |
| B | 7 | 14 | 6 | Q4/Q8 (the summary at step 4 shows a delivery charge before delivery is chosen at step 7, which B flags itself), Q10 ("checks that the date is still open" in step 8), Q2/Q3 (payroll becomes a supporting system that can refuse, not in gold), Q7 (step 9 by email, "closes the app") | Step 8 is marked `(system, wait)` but nothing waits. Privacy line reads `no:` but gives a deferral reason. Grid IDs are in backticks (`UC-001.*a`) |

**A invented:** the payroll authorization stored with the order (step 6, success guarantee); 7e marked out of scope as "the driver put this case out of scope".
**B invented:** Payroll system as an authorizing supporting actor and 8e (refusal); a 7-day horizon; a 10:30 cutoff; windows from 11:30 to 13:30; 20 places per window; a flat delivery charge; no caps; ordering only for oneself; a fixed list of locations; no card payment; 7c duplicate submit; 8d price change; email confirmation and 9a; a Delivery staff stakeholder.
**B missing:** the whole non-deliverable-item rule and extension (gold BR-3, 5b), the pickup time (raised as an open issue), and a coherent step order.

A follows the gold almost line for line: the same rules (cutoff/closed day, payroll registration, non-deliverable items, full windows → pickup), the same step-8 race conditions (window or item taken, inventory down or partly reserved, cutoff passed) and the same abandon range. Its only loss is the 15-minute window length. B reorders the scenario so the total is confirmed before delivery or pickup is chosen. It drops the non-deliverable-item rule and fills the gaps with about fourteen numeric or behavioural "recommendations" the owner never gave.

## case-08-buy-stocks

| Draft | Coverage | Invented | Quality | Criteria failed | Form issues |
|---|---|---|---|---|---|
| A | 8 | 13 | 6 | Q7 (connection technology inside step 2, which the gold keeps as a variation), Q9 (field lists in steps 2 and 4: currency, fees, execution time, order reference), Q8 (step 2 bookkeeping "opens a purchase attempt that records…"; steps 4 and 5 are both system steps of the same duration class and should be bundled, T1), Q2 (internal records exposed), Q12 (4a and `*a` overlap) | Template comments left in the front matter (`# Draft \| Complete [R28-Q11]`, `priority: TBD`). Privacy line reads `no:` but gives a deferral reason. 4b continues as prose after its numbered list. 3c and 4e are not cited in the grid |
| B | 9 | 2 | 9 | Q4 borderline: the success guarantee leaves out that the user has seen the updated portfolio | Variations say `None`, though gold has the embedded-session-or-API variation at step 2 |

**A invented:** a purchase-attempt record with fields; required and optional confirmation fields (BR-2); 3a brokerage rejection (gold puts the brokerage's validation out of scope); 3c several purchases per session; 4a connection drop; 4c duplicate confirmation (BR-4); 4d partial fill; 5a save failure with retry; `*a` app session expiry; price validation and a decline path in 4b; BR-5 no amount limits; BR-6 12-month retention; a support stakeholder.
**A missing:** the device-crash extension (gold 3a, deferred) and the named follow-up use case (Resolve a Pending Purchase).
**B invented:** 4c "session ends before any confirmation"; 4d "portfolio can't be updated".

B matches the gold's shape exactly: four steps, the same `out-of-scope` cells on step 3, the deferred device-crash extension with the reconcile-at-next-launch direction, 4a deferred to pending and 4b asking for missing details. It loses only the variation and adds two plausible extensions. A has most of the gold's substance but buries it under a brokerage-integration design: field lists, deduplication, partial fills, rejections and retention, all owner decisions it lists as recommendations. It also moves the technology variation into the main scenario.

## case-21-import-contacts

| Draft | Coverage | Invented | Quality | Criteria failed | Form issues |
|---|---|---|---|---|---|
| A | 8 | 4 | 8 | Q13 (1b "returns to step 2", but it is detected at step 4 and should rejoin at step 5) | 3a is not cited in the grid (step 3 is `n/a` throughout). Variations say `None`. Quota and stale-data cells on step 6 give the same out-of-scope reason twice |
| B | 9 | 15 | 6 | Q15 (variations 3 "unmapped column becomes a custom field" and 6 "existing contacts also tagged" change the outcome), Q10 ("if the Manager has left, emails them" in step 7), Q7 (formats named in step 1, XLSX, email), Q12 (2a and 3a are both "no email column", handled the same) | No "Related use cases" line. Grid IDs are in backticks |

**A invented:** "offers no upgrade / never pushes an upgrade" (gold lists Upgrade Plan as related); 6c one import at a time per audience (BR-7); 6d concurrent edit or unsubscribe, never resubscribe; 6b retry back to step 1 and failed runs recorded in the history.
**A missing:** the clipboard/CSV/spreadsheet variation, an explicit "manager leaves, import completes" extension (only partly implied), the duration note, the explicit email-as-identity rule, and the related use cases Upgrade Plan and Send Campaign.
**B invented:** a 50 MB limit; an email when the import finishes or fails; a Compliance stakeholder and a proof-of-consent record; 4b "nothing would change"; 4c change choices after the counts; 6c one import at a time; 6d deleted contacts re-added as new; `*a` session expiry or permission removed; mapping heuristics; custom fields; tagging existing contacts; downloading skipped rows; default import name; the import never changes subscription status; the limit counts all contacts.

Both drafts cover the gold's core well: the mapping, consent with non-subscribed storage, the limit check, invalid and duplicate rows, rollback on cancel and on failure. B covers slightly more of the gold's substance (variation, walking away from a long import, duration). It pays for that with about fifteen invented rules and variations, two of which change the outcome. A invents a few concurrency rules and drops the variation and the walk-away path, but stays close to what was decided.

## Overall verdict

- **case-01:** A is clearly better: higher coverage (9 vs 7), almost nothing invented (2 vs 14) and better quality (9 vs 6). B's step order is broken.
- **case-08:** B is clearly better: higher coverage (9 vs 8), far less invented (2 vs 13) and better quality (9 vs 6).
- **case-21:** A is moderately better. B has a slight edge on coverage (9 vs 8), but A invents much less (4 vs 15) and scores higher on quality (8 vs 6).

There is no consistent winner by letter. The decisive factor in every case is the same: one draft keeps to what the owner decided, and the other fills gaps with "recommended" rules, extensions and variations. A does that in case 08; B does it in cases 01 and 21.
