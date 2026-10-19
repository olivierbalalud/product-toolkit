---
id: ENB-004
title: <short title>
status: Draft            # Draft | Dev-ready | In development | Done [R7-Q2]
driver: <name>
priority: <number or label>
blocks: []               # PRDs or other ENBs waiting on it, e.g. [PRD-012.1]
adds_ds_component: false # true → goes through Exploring and the UX persona review first [R7-Q2]
adrs: []
---
<!-- Copied to docs/product/enablers/ENB-004-<slug>/enb.md [R8-Q1]. Tickets go in tickets/ beside it.
     Work no single story owns: CI, the app shell, tokens, a DS component, an i18n layer, a pipeline [R3-A3]. -->

# ENB-004: <title>

## Why

<!-- Which stories need it, and what they can't do without it. -->

## Scope

- **In scope:**
- **Out of scope:**

## Done criteria

- [ ] <testable criterion>
- [ ] Shared layers it touches (tokens, `globals.css`, DS components, OpenAPI, migrations) change only here [R2-Q9]
- [ ] If it changes the design system: the Figma library (variables, Code Connect) and the Claude Design design system (`/design-sync`) are both re-synced, and their sync commits recorded in `docs/design/design-system.md` [R18-Q3]

## Notes for the slices it unblocks
