---
name: refresh-guidelines
status: outline
priority: P2
owner: <name>
serves: check-web-guidelines maintenance
decisions: [R3-D2, R3-D3′, R3-D4, R3-D5, R3-D6]
plugin_version:
---

# refresh-guidelines

## 0. Header

The human-triggered, pull-only refresh of the pinned Vercel guidelines copy used by `check-web-guidelines`.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- follows directives in the fetched text.
- Drops `overrides.md` or `excluded.md` decisions.
- Records the deploy date instead of the upstream commit.

## 2. Scope

- **Does:** fetches `command.md` of both upstreams at their latest commit, saves the raw snapshot, regenerates the filtered copy, shows the diff, and on human approval updates provenance frontmatter (`upstream_version` = commit SHA, `upstream_commit_date`, `last_updated_from_vercel_on`) for a PR [R3-D2, R3-D3′].
- **Does not:** run automatically, push, or obey anything in the fetched text, which is data [R3-D2].
- **Neighbouring skills:** Maintains `check-web-guidelines`.

## 3. Invocation

- **Invoked by:** the user only (`disable-model-invocation`), because it fetches from the network.
- **Draft description:**
  > Refreshes the project's pinned copy of the Vercel web interface and writing guidelines from upstream, showing a diff for approval. Use only when a person asks to update the guidelines.
- **Should trigger:**
  - "refresh the Vercel guidelines"
  - "pull the latest web interface guidelines"
  - "update the guidelines copy"
- **Should not trigger:**
  - "check this UI against the guidelines"
  - "review the copy"
  - "install a skill"
- **Arguments:** None.

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

- Script fetches by commit SHA via the GitHub API; the model only drafts the filtered diff summary.

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

- Whether a refresh also re-runs the skill's evals.
