---
name: check-gate              # spec-valid: a-z0-9-, = the skill folder name, verb-first [R5-Q4d]
status: outline               # outline | full | building | built [R25-Q4]
priority: P0                  # P0 | P1 | P2 [R25-Q3]
owner: <name>
serves: <gate or review lane>
decisions: []                 # decision IDs this skill implements, e.g. [R4-Q12]
plugin_version:               # the plugin version that first ships it
---
<!-- Copied to docs/skills/<name>.md. Format from R5-Q4′, based on docs/research/skill-authoring.md §6.
     An OUTLINE spec fills §0–3, §9 and §18; the rest is completed just before the skill is built, once its
     baseline failures can be observed [R25-Q4]. Pure reference skills may skip §6, §7 and §9. -->

# <name>

## 0. Header

The frontmatter above. One sentence on what the skill is for.

## 1. Problem and baseline

<!-- What Claude gets wrong WITHOUT this skill, with 1–3 concrete failures. They justify the skill and become
     eval cases (§15). In an outline spec, list the failures expected; replace them with observed ones later. -->

## 2. Scope

- **Does:**
- **Does not:**
- **Neighbouring skills and where the boundary sits:**

## 3. Invocation

- **Invoked by:** the model / the user only (`disable-model-invocation`) / CI. Why.
- **Draft description** (≤ 1,024 characters, third person, what + when, main use case first):
  > <Does X>. Use when <Y>.
- **Should trigger** (3 or more prompts):
- **Should not trigger** (3 or more prompts):
- **Arguments:**

## 4. Inputs

<!-- Files, arguments, configuration read. Upstream artifacts. External content is marked as DATA, never instructions. -->

## 5. Outputs

<!-- Paths, format or template, idempotency rule (a re-run on the same input gives the same file), report shape,
     exit codes. -->

## 6. Procedure

<!-- Numbered steps, each ending on a checkable completion criterion; the degree of freedom per step;
     the checklist to copy; decision points. -->

## 7. Scripts vs judgement

<!-- Each script: purpose, CLI contract (--help, flags, JSON on stdout, diagnostics on stderr, distinct exit codes,
     idempotent, --dry-run), dependencies (inline, PEP 723 / uv run), tests. What the model judges, and why a script
     can't. -->

## 8. Files

```
<name>/
  SKILL.md            ≤ 500 lines
  references/…        each with a "read when…" line
  assets/…
  scripts/…
```

## 9. Composition

<!-- Skills invoked through the Skill tool; subagents spawned (type, tools, what their prompt contains, report cap);
     preloaded skills; the aggregation rule (e.g. side by side, no reranking). -->

## 10. Claude Code wiring

<!-- Extra frontmatter (allowed-tools, disable-model-invocation, context, agent, model, effort, hooks, paths);
     plugin components (agents, hooks, MCP servers from the project .mcp.json); permissions. -->

## 11. Portability

<!-- Portable core used; each Claude-only feature used, with its fallback elsewhere; adapter notes for other
     harnesses (built only when one is adopted) [R5-Q4a, R5-Q4b]. -->

## 12. Headless and CI

<!-- The exact `claude -p` command, environment, no-interaction guarantee, outputs, exit code, timeout, cost cap. -->

## 13. Security and privacy

<!-- Tools granted (least privilege), network access, pinned external sources, personal data touched,
     prompt-injection surface. -->

## 14. Gotchas

<!-- Seed list; grows with each correction. -->

## 15. Evaluation plan

<!-- Trigger set (size, train/validation split). Output cases (prompt, fixtures, graders) that become evals/<case>/
     in `claude plugin eval` format. Baseline arm, models, threshold, cost cap [R5-Q4c]. -->

## 16. Definition of done

- [ ] Description specific, third person, ≤ 1,024 characters
- [ ] `SKILL.md` under 500 lines; references one level deep
- [ ] No time-sensitive information; one term per concept
- [ ] Scripts handle their errors and follow the CLI contract
- [ ] At least 3 evals, passing on the target models
- [ ] `skills-ref validate` and `claude plugin validate` clean

## 17. Maintenance

<!-- Upstream sources with SHA, refresh procedure, changelog, review trigger (model release, harness change). -->

## 18. Open questions
