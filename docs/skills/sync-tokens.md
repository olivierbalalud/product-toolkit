---
name: sync-tokens
status: outline
priority: P1
owner: <name>
serves: Design-system enablers
decisions: [R3-Q2, R17-Q1, R18-Q3, R20-Q1, R20-Q4]
plugin_version:
---

# sync-tokens

## 0. Header

Turns a Figma variables change into a token PR, and keeps both design-system mirrors' sync record current.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- applies Figma's exported values directly, including `$extensions` IDs and colour-rounding noise.
- Edits `tokens.css` by hand.
- Forgets to record the mirrors' sync commit.

## 2. Scope

- **Does:** reads Figma variables (`get_variable_defs`), maps names by the DTCG mirror rule, writes the DTCG change and rebuilds `tokens.css` and the Figma import file, opens a PR for review; updates the sync record in `docs/design/design-system.md` after a re-sync [R3-Q2, R17-Q1, R18-Q3, R20-Q4].
- **Does not:** apply anything without review, or change components.
- **Neighbouring skills:** Used in design-system enabler slices; the gate check warns on stale mirrors [R18-Q3].

## 3. Invocation

- **Invoked by:** the user, in a design-system enabler slice.
- **Draft description:**
  > Prepares a reviewed pull request from a Figma variables change to the project's DTCG tokens, and records design-system mirror syncs. Use when tokens changed in Figma or after re-syncing Figma or Claude Design.
- **Should trigger:**
  - "bring the Figma colour change into tokens"
  - "sync tokens from Figma"
  - "record that Claude Design was re-synced"
- **Should not trigger:**
  - "add a new button variant"
  - "change the copy"
  - "review accessibility"
- **Arguments:** Figma file; optional token group.

## 4. Inputs

_To be completed before building (R25-Q4)._

## 5. Outputs

_To be completed before building (R25-Q4)._

## 6. Procedure

_To be completed before building (R25-Q4)._

## 7. Scripts vs judgement

_To be completed before building (R25-Q4)._

## 8. Files

_To be completed before building (R25-Q4)._

## 9. Composition

- Uses the `figma` MCP server from `.mcp.json`; plan-validate-execute: write `changes.json`, validate, apply [skill-authoring research §4].

## 10. Claude Code wiring

_To be completed before building (R25-Q4)._

## 11. Portability

_To be completed before building (R25-Q4)._

## 12. Headless and CI

_To be completed before building (R25-Q4)._

## 13. Security and privacy

_To be completed before building (R25-Q4)._

## 14. Gotchas

_To be completed before building (R25-Q4)._

## 15. Evaluation plan

_To be completed before building (R25-Q4)._

## 16. Definition of done

_To be completed before building (R25-Q4)._

## 17. Maintenance

_To be completed before building (R25-Q4)._

## 18. Open questions

- Whether it also drives `/design-sync` for the Claude Design mirror or only records it.
