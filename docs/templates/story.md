---
id: PRD-012.1
story: US-012.1
use_case: UC-012
title: <short title>
status: Draft            # becomes the PRD; see prd.md for the full template
driver: <name>
priority: <number or label>
source_locale: en
extensions: [UC-012.2a, UC-012.3a]   # the only list of the extensions this story handles [R4-Q3, R28-Q4]
touches: [ui, api]       # ui, api, or both; decides which companion files the gate requires.
                         # Free to change until Design-complete, then through a DCR [R28-Q5, R28-Q18]
---
<!-- A story and its PRD are 1:1 and share one file; there is no separate story.md in the monorepo [R1-Q9, R9-Q1]. This is the Draft-stage start of
     …/stories/US-012.1-<slug>/prd.md. When the PRD enters Exploring, extend it with prd.md. -->

# US-012.1: <title>

**As a** <role>, **I want** <capability>, **so that** <benefit>.

<!-- The "so that" must trace to a user benefit in §3a of the PRD [R4-Q4a]. -->

## Path through the use case

<!-- The first story of a use case is the thinnest path through the whole main scenario; each later story adds
     extensions or one variation [R28-Q8]. INVEST (see guide chapter 3); about one week of slice work at most.
     No acceptance criteria here: the Gherkin scenarios are written during Exploring, starting from the
     extensions' examples in the use case [R28-Q4]. -->

- Main scenario steps: <1–5>
- Variation: <the "Technology and data variations" item this story adds, if any>
