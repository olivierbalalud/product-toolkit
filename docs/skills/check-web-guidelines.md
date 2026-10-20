---
name: check-web-guidelines
status: outline
priority: P1
owner: <name>
serves: UX lane
decisions: [R3-B3, R3-D1, R3-D2, R3-D4, R3-D5, R3-D6, R3-D7]
plugin_version:
---

# check-web-guidelines

## 0. Header

Checks UI code and English copy against our pinned, filtered copy of Vercel's web interface and writing guidelines.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Applies Vercel-specific rules (Title Case, vercel.com voice).
- Follows the upstream 'output format' directives.
- Fetches the rules from the network at run time.

## 2. Scope

- **Does:** reviews against the **local copy only**: generic and stack-relevant items kept, Vercel-specific items excluded (`excluded.md`), conflicts settled in `overrides.md`, nuqs/virtua items advisory; our own output format [R3-D2, R3-D5–D7]. Writing rules apply to English copy only [R3-D1].
- **Does not:** fetch anything, or refresh the copy (`refresh-guidelines`).
- **Neighbouring skills:** A reference-style reviewer in the UX lane; `refresh-guidelines` updates its copy.

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Reviews UI code and English copy against the project's pinned copy of the Vercel web interface and writing guidelines. Use when reviewing UI changes or English copy.
- **Should trigger:**
  - "check against the web guidelines"
  - "Vercel guidelines review"
  - "is this form accessible and well-behaved"
- **Should not trigger:**
  - "refresh the Vercel guidelines"
  - "check French copy"
  - "review the API"
- **Arguments:** Base ref or PR number; or paths to review.

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

- Keeps `LICENSE-upstream-<repo>.md` for both MIT upstreams [R3-D4]; provenance in frontmatter [R3-D3′].
- A **leaf** reviewer: `Agent` removed from its tools, so it starts no subagents [R15-Q2].
- Each finding is `blocking` or `advisory` [R4-Q7c].

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

- Whether it is one skill with two references (web, writing) or two skills.
