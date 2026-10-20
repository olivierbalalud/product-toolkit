---
name: check-setup
status: outline
priority: P1
owner: <name>
serves: Every developer machine
decisions: [R3-B5, R3-B7, R3-B4]
plugin_version:
---

# check-setup

## 0. Header

The collision 'doctor': finds personal skills, agents, plugins and MCP servers that shadow or conflict with the project's.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- a personal skill silently shadows a project one of the same name.
- A user-level MCP server overrides the project's.
- A known-conflicting plugin loads from user scope.

## 2. Scope

- **Does:** lists `~/.claude/skills` and `~/.claude/agents` names that clash with the project's, user-level MCP servers that shadow project ones, and enabled user plugins that project settings should disable [R3-B5, R3-B7].
- **Does not:** change user settings; it reports and suggests.
- **Neighbouring skills:** Complements `.claude/settings.json`'s `false` entries [R3-B7].

## 3. Invocation

- **Invoked by:** the user, on setup and after installing anything personal.
- **Draft description:**
  > Reports personal Claude Code skills, agents, plugins and MCP servers that clash with or shadow the project's configuration. Use when setting up the repo or when a skill behaves unexpectedly.
- **Should trigger:**
  - "check my Claude setup for conflicts"
  - "why is a different skill running"
  - "doctor"
- **Should not trigger:**
  - "install a plugin"
  - "review this PR"
  - "set up the worktree"
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

- A script does the listing and comparing; no subagents.

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

- Whether it also checks plugin pins against `marketplace.json`.
