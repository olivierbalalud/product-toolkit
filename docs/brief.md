# Product Toolkit: Brief

Status: initial brief, captured 2026-10-19. Decisions refining it are logged in [`grilling-log.md`](grilling-log.md).

## Objectives

1. Find a way of working where we design screens in Claude Design or Figma and keep the designs in sync with a code repo.
2. Design and document a process for designing and then developing several features in parallel using git worktrees.

## Key concerns

- **Tools vs harnesses.** We want a good mix of tools for rapid development and a harness for a proper SDLC. Seeds to research:
  - builder.io (free version for now), Figma, Lovable, Cursor, shadcn studio
  - <https://optics.agusmayol.com.ar/>
  - <https://shadcnstudio.com/blog/shadcn-react-component-libraries/>
  - <https://github.com/affaan-m/ECC>
  - <https://www.aihero.dev/skills>
  - <https://github.com/wshobson/agents>
- **Design completeness**, not just coverage of business rules.
- **Clear gating rules** from prototype/mockup screens to design-complete. Flows and screens must be open to iteration before a PRD becomes design-complete.
- **Edge cases**: use case extensions must be covered.
- **Separation of concerns**: tone of voice and product look (themes, micro-interactions) are kept separate from screen flows and from the key information and key actions of a user story.
- **Languages**: each PRD is designed and coded in either English or French, and translations into the other languages are generated from it. That means English and French now, other Latin languages later.
- **Three perspectives**: always check against each perspective in the team: product manager, UX designer, software engineer.
- **Two-way design ↔ code**: once we move from design to code, we must be able to go back into the design tool. A proper design system is very likely the enabler, but there may be other pitfalls.

## Context

- Small, early-stage startup team: founders plus 1 or 2 developers.
- Given: development uses Claude Code and VS Code, and specs, PRDs and use cases are written in Markdown.
- A monorepo holds the frontend apps, the services and deployment (Docker for dev, Kubernetes for staging and prod).
- The company website (pricing, legal, sales, hero pages, etc.) is separate and **outside** the monorepo.
- Infrastructure components (workflow engine, observability stack, database style for each use case or workflow, etc.) are either already known or decided independently of this framework:
  - Technical choices come from **ADRs**.
  - A **TRD** is provided for a PRD when clarification beyond the standard stack and the existing ADRs is needed.
  - If a feasibility or performance gap is found while a PRD is being crystallised or iterated, the framework must provide a way to surface it and structure it so it can feed a **new ADR**.

## Process (as envisioned)

### Designing

1. Pick a use case from the list of partially written use cases.
2. Flesh out the use case until it is complete.
3. Detail one or more user stories from the use case.
4. Pick up user stories.
5. For each picked-up user story, write a PRD until it is **design-complete**.

### Developing

1. Pick up a design-complete PRD and read its TRDs and the relevant ADRs.
2. Launch one or more agents to develop the screens and backend services (greenfield or brownfield).
3. From the user story's point of view, the whole feature is picked up as a **slice**. Work is done when the slice is done.
4. From the architecture's point of view, there are several layers:
   - **Frontend**: web only for now, React + shadcn + Tailwind on Next.js. Leave it open to Android and iOS later, which is why shadcn + Tailwind were chosen.
   - **Service layer**: a hexagonal-style architecture for the business layer. The technical services underneath it vary in shape (enterprise systems of record, databases, document DBs, ingestion pipelines, etc.), so a hexagonal style is unlikely to fit anything other than the business layer.
   - Services are exposed as **FastAPI** routes with **Pydantic**, running on Gunicorn/Uvicorn workers.

## Testing approach

### During design

- A user story provides BDD outcomes. Its BDD scenarios (GIVEN / WHEN / THEN …) become a functional test suite of auto-generated textual test cases.
- Thinking in user stories tends not to uncover every edge case. So go through the **use cases first** and find failure paths through their **extensions**. Then assess whether the user stories of a use case together cover all of that use case's extensions.

### During development

- **TDD, functional:** write the test suite first, with mocks, for every BDD textual test case. Mocks are built with ports and adapters, which is where the hexagonal style of the business layer fits in. The suite must include edge cases, failure paths and every extension of the use cases covered.
- **TDD, technical:** write all the technical tests.
- **Other required tests:** security and privacy (privacy by design).
- Testing for the other "-ilities" is **outside** this framework.
