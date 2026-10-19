---
id: PRD-012.1
story: US-012.1
use_case: UC-012
title: <short title>
status: Draft            # becomes the PRD; see prd.md for the full template
driver: <name>
priority: <number or label>
source_locale: en
extensions: [UC-012.2a, UC-012.3a]   # the extensions this story handles [R2-Q4, R4-Q3]
---
<!-- A story and its PRD are 1:1 and share one file; there is no separate story.md in the monorepo [R1-Q9, R9-Q1]. This is the Draft-stage start of
     …/stories/US-012.1-<slug>/prd.md. When the PRD enters Exploring, extend it with prd.md. -->

# US-012.1: <title>

**As a** <role>, **I want** <capability>, **so that** <benefit>.

<!-- The "so that" must trace to a user benefit in §3a of the PRD [R4-Q4a]. -->

## Path through the use case

<!-- A vertical path that delivers value on its own: the main scenario, or a coherent part of it,
     plus the extensions it must handle [R4-Q3]. INVEST (see guide chapter 3, step 2); about one week of slice work at most. -->

- Main scenario steps: <1–5>
- Extensions handled: UC-012.2a, UC-012.3a
- Extensions left to other stories: <listed in coverage.md>

## Draft acceptance criteria

<!-- May be in the source locale during Exploring; converted to English Gherkin before Design-complete [R3-C1]. -->

- <criterion>
