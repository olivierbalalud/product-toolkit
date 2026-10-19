# SWE lens: from prototype to maintained codebase

What a software engineer needs to think and do to turn a Design-complete PRD and its prototype into a slice that is tested, reviewed and easy to change later. The reading path and the other lenses are in [`README.md`](README.md); see also [`pm-lens.md`](pm-lens.md), [`ux-lens.md`](ux-lens.md) and, for security, privacy and AI, [`security-privacy-ai.md`](security-privacy-ai.md). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

All links were checked on 2026-10-19 ([sources](../research/foundations-sources-eng-legal.md)). **Time** counts the text plus any video under 30 minutes; longer videos are marked optional.

## Key behaviours

- **The spec is the source.** The PRD, its `.feature` files, the draft contract and the fit analysis say what to build. Code that does something else is a defect or a DCR, never a quiet improvement [R2-Q4, R4-Q7c].
- **Tests first.** Scenarios are bound and red before business code exists, in the order of [chapter 4, §4.7](../guide/04-dev-playbook.md#47-the-test-first-order) [R4-Q8′].
- **Small, reversible steps.** Tracer-bullet tickets, expand before contract, characterisation tests before touching untested code [R4-Q7′, R4-Q8d].
- **Respect the hexagon.** The business layer imports neither FastAPI nor SQLAlchemy; everything outside it is an adapter behind a port [R3-Q1f].
- **Existing code counts.** Reuse and extend before you change, and never break a consumer the PRD doesn't list [R4-Q8c].

---

### Contract-first APIs
**Roles:** SWE core · UX optional · PM optional   **Time:** ~19 min (text + video)
**Definition.** In a contract-first (or design-first) approach, the API's description is agreed before the code: endpoints, schemas and errors, written in OpenAPI. Clients and servers are then built against that contract in parallel. The current OpenAPI version is 3.2.1 (September 2026).
**Why it matters.** SWE: front end, back end and tests can work in parallel against one agreed shape, and breaking changes become visible. UX: the prototype can run on realistic mocks early.
**In this framework.** The **agreement** is contract-first, the **file** is generated: a draft contract, `contract.draft.yaml` (PRD §12, [`prd.md`](../templates/prd.md)), is written during design against the fit analysis, and the prototype's MSW mocks follow it [R2-Q3 (l), R4-Q8a]. In the slice, FastAPI generates the OpenAPI from the Pydantic schemas; it is reconciled with the draft, then diffed against `main` (e.g. with `oasdiff`) so CI blocks any breaking change the PRD doesn't list [R4-Q8′, R4-Q8c]. The web app uses a client generated from it, `src/packages/api-client/` [R3-Q1g].
**Key literature.** OpenAPI Initiative, [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) (v3.2.1, 2026).
**Learn it.** Text: [Best Practices: "Use a Design-First Approach"](https://learn.openapis.org/best-practices.html) (OpenAPI Initiative, ~7 min). Video: [The Language of API Design: Creating your OpenAPI Description](https://www.youtube.com/watch?v=V5fMaz0sybw) (Erik Wilde, 12:10).

### BDD, specification by example and Gherkin
**Roles:** SWE core · PM core · UX optional   **Time:** ~16 min (text; video +30 min optional)
**Definition.** Behaviour-driven development (Dan North, 2006) describes a feature through concrete examples of its behaviour, written so business and engineering read them the same way. Specification by example (Gojko Adzic) makes those examples the specification and the tests at once. Gherkin is the `Given / When / Then` format that tools such as Cucumber run.
**Why it matters.** SWE: the scenarios become executable acceptance tests. PM: acceptance is written once, in a form that can't drift from the code. UX: failure paths are spelled out, not left to guesswork.
**In this framework.** The `.feature` files **are** the acceptance criteria [R3-C1]. They are **English only**, whatever the PRD's language, so steps never turn into French identifiers [R3-Q1a]; domain words come from the glossary [R3-C3]; UI text is referenced by copy key [R3-C2]; scenarios are tagged with story and extension IDs and frozen at Design-complete [R3-Q1a]. pytest-bdd runs them on the business layer with fakes, playwright-bdd on the UI [R1-Q15]. Unlike classic BDD, the scenarios are drafted by the PRD's driver with agents during *Exploring* rather than in a workshop; **example mapping** is a good way to run that conversation. Template: [`feature.feature`](../templates/feature.feature); see chapter [8](../guide/08-testing.md).
**Key literature.** Dan North, "Introducing BDD" (2006); Gojko Adzic, *Specification by Example* (2011).
**Learn it.** Text: [Introducing BDD](https://dannorth.net/blog/introducing-bdd/) (Dan North, ~13 min) and [Given When Then](https://martinfowler.com/bliki/GivenWhenThen.html) (Martin Fowler, ~3 min); for example mapping, [Introducing Example Mapping](https://cucumber.io/blog/bdd/example-mapping-introduction/) (Matt Wynne, ~9 min, optional); reference: [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) (Cucumber). Video (optional): [20 Years of BDD](https://www.youtube.com/watch?v=og8Gr05dz6Y) (Dan North, 29:45). No example-mapping talk by Wynne himself was found.

### Spec-driven development
**Roles:** SWE core · PM optional   **Time:** ~17 min (text; video +40 min optional)
**Definition.** Spec-driven development (SDD) is an AI-assisted way of working where a written specification, not the chat history, drives what a coding agent builds. Tools such as GitHub spec-kit and Kiro structure it as requirements, a design and a task list. Thoughtworks rates it *Assess* and warns the term is used inconsistently.
**Why it matters.** SWE: agents build what is written, so the quality of the spec bounds the quality of the code. PM: the spec is the point of control over agent work.
**In this framework.** We practise SDD without spec-kit or Kiro [R12-Q3]: the spec is the PRD, its `.feature` files, the contract and the fit analysis, all in `docs/product/…` per use case. `to-tickets` cuts it into tickets and `implement-spec` builds them with `tdd` [R4-Q7′]. See [chapter 4](../guide/04-dev-playbook.md).
**Key literature.** Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" (2025).
**Learn it.** Text: [Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) (Birgitta Böckeler, martinfowler.com, ~17 min); context: [Tech Radar: Spec-driven development](https://www.thoughtworks.com/radar/techniques/spec-driven-development) (Thoughtworks, ~2 min). Video (optional): [The ONLY guide you'll need for GitHub Spec Kit](https://www.youtube.com/watch?v=a9eR1xsfvHg) (channel "Den", 40:00).

### TDD
**Roles:** SWE core   **Time:** ~7 min (text; video +49 min optional)
**Definition.** Test-driven development (Kent Beck) writes a failing test first, then the least code that makes it pass, then refactors, in short cycles. Beck's "Canon TDD" adds a first step: list the test scenarios before writing any.
**Why it matters.** SWE: code exists only because a test asked for it, so it stays covered and easy to change.
**In this framework.** Each ticket is built with the `tdd` skill, inside `implement-spec` [R4-Q7′]. The slice-level order puts BDD scenarios first (red), then business logic, adapters, API and UI [R4-Q8′]; unit tests accompany each step. Fakes behind ports keep the business-layer loop fast [R1-Q15].
**Key literature.** Kent Beck, *Test-Driven Development: By Example* (2002).
**Learn it.** Text: [Canon TDD](https://tidyfirst.substack.com/p/canon-tdd) (Kent Beck, ~7 min). Video (optional): [Canon Test-Driven Development](https://www.youtube.com/watch?v=90VBvjYedWI) (Kent Beck, Craft 2025, 48:46).

### Domain modelling and DDD
**Roles:** SWE core · PM optional   **Time:** ~8 min (text; video +57 min optional)
**Definition.** Domain-driven design (Eric Evans) puts a model of the business domain at the centre of the code. Its **ubiquitous language** is one vocabulary shared by experts, specs and code; a **bounded context** is the boundary within which one model and its language apply.
**Why it matters.** SWE: names in the code match what the business means, and models don't leak across contexts. PM: the glossary keeps specs precise.
**In this framework.** Each `src/domains/<d>` is one bounded context *and* one deployable [R3-Q1h]. The ubiquitous language is the bilingual glossary, `docs/product/glossary.md`; code and Gherkin use its **English** terms [R3-A5, R3-C3]. The `domain-modeling` skill helps keep the glossary sharp [R3-B1]. Evans's free DDD Reference summarises the patterns.
**Key literature.** Eric Evans, *Domain-Driven Design* (2003); [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) (2015, free PDF).
**Learn it.** Text: [Domain Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html) (~3 min), [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) (~4 min) and [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html) (~1 min), all Martin Fowler. Video (optional): [What is DDD](https://www.youtube.com/watch?v=pMuiVlnGqjk) (Eric Evans, DDD Europe 2019, 57:05).

### Hexagonal architecture
**Roles:** SWE core   **Time:** ~23 min (text; video +56 min optional)
**Definition.** Hexagonal architecture, or ports and adapters (Alistair Cockburn, 2005), isolates the application core from the outside world. The core declares **ports** (interfaces); **adapters** connect them to a UI, an API, a database or another system, and can be swapped, for example for fakes in tests.
**Why it matters.** SWE: business rules are testable without a database or a web server, and technologies can change without touching them.
**In this framework.** The hexagon applies to the **business layer only**: `app/business/{model,usecases,ports}` imports neither FastAPI nor SQLAlchemy, and an import-linter contract enforces it [R3-Q1f]. Technical services behind the ports take whatever shape they need (brief). Every port has a fake in `tests/fakes/`, which is how BDD scenarios run without services [R1-Q15]. Legacy code can be reached through a port rather than rewritten [R4-Q8d].
**Key literature.** Alistair Cockburn, "Hexagonal Architecture" (2005).
**Learn it.** Text: [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) (Alistair Cockburn, ~23 min). Video (optional): [Hexagonal Architecture](https://www.youtube.com/watch?v=k0ykTxw7s0Y) (Alistair Cockburn, Tech Excellence, 56:16).

### Modalities
**Roles:** SWE optional   **Time:** ~34 min (text + video)
**Definition.** At the engineering level, modalities are the channels a system is driven through: a web UI, a public API, a CLI, background jobs, events, later a mobile app. In a hexagonal design each one is an inbound (driving) adapter calling the same business core.
**Why it matters.** SWE: a rule written once in the core serves every channel, and a new channel is a new adapter, not a rewrite.
**In this framework.** The SWE meaning is decided in [R12-Q4]; the UX meaning (input modes, touch points) is in [`ux-lens.md`](ux-lens.md#modalities-and-touch-points). The web app (`src/apps/web`), the CLI (`src/apps/cli`) and each domain's API (`app/api`) are inbound adapters onto `business/usecases` [R3-Q1f, R3-Q1g]. Native mobile, later, will be one more [R3-Q8].
**Key literature.** Alistair Cockburn, "Hexagonal Architecture" (2005): "allow an application to equally be driven by users, programs, automated test or batch scripts".
**Learn it.** Text: [Hexagonal architecture pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html) (AWS Prescriptive Guidance, ~9 min). Video: [Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters](https://www.youtube.com/watch?v=FXwBWS4qDAA) (ArjanCodes, 25:23; uses our stack).

### Repo conventions
**Roles:** SWE optional · PM optional   **Time:** ~16 min (text; video +35 min optional)
**Definition.** Repo conventions are the shared rules for how work is named and stored: commit messages, branch names, folder layout. Conventional Commits is a commit message format (`type(scope): description`). A monorepo keeps several apps and packages in one repository with shared tooling.
**Why it matters.** SWE: anyone, human or agent, can find things and read history without asking. PM: commit scopes and branch names trace work back to artifacts.
**In this framework.** Commits follow Conventional Commits, with the **artifact ID as scope**, e.g. `docs(PRD-012.1): add state matrix` [R4-Q5′]. Branches are `design/`, `slice/`, `enb/`, `adr/` plus `fix/` and the other types; a DCR gets `design/DCR-…` [R4-Q5′, R10-Q1]. Worktree names are the branch name with `/` replaced by `-` [R4-Q5′]. Specs live under **`docs/`** [R13-Q0]. Python uses a uv workspace, the web side a pnpm workspace [R3-Q1g]. Test reports are never committed [R3-Q1b]. See [chapter 2](../guide/02-artifacts-and-ids.md) and [chapter 5](../guide/05-worktrees-and-parallelism.md).
**Key literature.** [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).
**Learn it.** Text: [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) (~8 min) and [Monorepo Explained](https://monorepo.tools/) (monorepo.tools, maintained by Nx, ~8 min). Video (optional): [The Gentle Monorepo](https://www.youtube.com/watch?v=k49496sH9aw) (PyData Amsterdam 2025, 35:00).

### Characterisation tests, strangler fig and parallel change
**Roles:** SWE core   **Time:** ~47 min (text + video)
**Definition.** A **characterisation test** (Michael Feathers) records what existing code actually does, so you can change it safely. The **strangler fig** (Martin Fowler) replaces an old system gradually by routing work to new code around it. **Parallel change**, or expand–migrate–contract, changes an interface by adding the new form beside the old, moving callers, then removing the old.
**Why it matters.** SWE: the code base already exists in part, and these are the safe ways to change it without breaking what works.
**In this framework.** Before changing existing behaviour that no test covers, a slice adds characterisation tests; it touches only what it needs, reaches old code through a port (strangler) rather than rewriting it, and leaves whole-module restructuring to an enabler slice [R4-Q8d]. `to-tickets` sequences a wide mechanical refactor as expand, migrate in batches, contract ([chapter 4](../guide/04-dev-playbook.md#45-step-4-cut-the-tickets)).
**Key literature.** Michael Feathers, *Working Effectively with Legacy Code* (2004).
**Learn it.** Text: [Characterization Testing](https://michaelfeathers.silvrback.com/characterization-testing) (Michael Feathers, ~6 min), [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html) (Martin Fowler, ~5 min) and [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) (Danilo Sato, ~6 min). Video: [Looking Back at Working Effectively with Legacy Code](https://www.youtube.com/watch?v=5OA5v-ALkbM) (Michael Feathers, InfoQ, 29:58). No video on parallel change by a recognised author was found.

### ADRs
**Roles:** SWE core · PM optional   **Time:** ~16 min (text; video +39 min optional)
**Definition.** An architecture decision record (Michael Nygard, 2011) is a short document capturing one significant decision: its context, the decision and its consequences. MADR is a Markdown template for ADRs that also records the options considered.
**Why it matters.** SWE: the next person, or agent, knows why the code is the way it is. PM: feasibility gaps get a visible, reviewable answer.
**In this framework.** ADRs follow MADR, in English, in `docs/adr/NNNN-slug.md` [R3-A2]; template [`adr.md`](../templates/adr.md). A gap found in design opens a `Proposed` ADR, which blocks Dev-ready but not Design-complete [R1-Q13]; a gap found during a slice pauses only the tickets it affects [R13-Q3]. An ADR may cite entries of an older decision register it supersedes [R3-A2].
**Key literature.** Michael Nygard, "Documenting Architecture Decisions" (2011).
**Learn it.** Text: [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (Michael Nygard, ~7 min) and [MADR](https://adr.github.io/madr/) (~9 min). Video (optional): [Creating effective and objective ADRs](https://www.youtube.com/watch?v=DSRQ-90eDBw) (Piet van Dongen, Devoxx, 39:18). No video by Nygard was found.

### The "-ilities"
**Roles:** SWE optional · PM optional   **Time:** ~9 min (text; video +47 min optional)
**Definition.** The "-ilities" are a system's quality attributes, as opposed to its functions: security, reliability, maintainability, performance and so on. ISO/IEC 25010:2023 groups them into nine characteristics; arc42 shows how to state them as testable quality scenarios.
**Why it matters.** SWE: they drive most architecture choices. PM: they are requirements too, even when nobody writes them down.
**In this framework.** The framework covers **security, privacy, accessibility and maintainability** (through the hexagon, tests and review lanes). **Performance, scalability, availability and observability** are left to ADRs and tested outside the framework [R12-Q5]. Only the first four of the nine ISO names were confirmed from the overview page; the standard itself is paid.
**Key literature.** ISO/IEC 25010:2023, product quality model (paid).
**Learn it.** Text: [ISO 25010 overview](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010) (iso25000.com, ~4 min) and [arc42 Section 10: Quality requirements](https://docs.arc42.org/section-10/) (~5 min). Video (optional): [Getting Quality Right](https://www.youtube.com/watch?v=4Zb4q27u2EU) (Gernot Starke, NewCrafts 2024, 46:54).

### Feature toggles and expand–contract migrations
**Roles:** SWE optional   **Time:** ~36 min (text + video)
**Definition.** A feature toggle (or flag) switches a piece of behaviour on or off at run time, so code can ship before it is released. An expand–contract migration changes a database schema in steps that keep old and new code working together.
**Why it matters.** SWE: they decouple deploying from releasing and make schema changes safe on a live system.
**In this framework.** **Context only.** How a `Done` slice reaches users is out of scope: deployment and release come from ADRs (brief) [R11-Q12b]. Expand–contract is the same idea as parallel change, above.
**Key literature.** Pete Hodgson, "Feature Toggles (aka Feature Flags)" (2017).
**Learn it.** Text: [Feature Flag](https://martinfowler.com/bliki/FeatureFlag.html) (Martin Fowler, ~6 min); longer: [Feature Toggles](https://martinfowler.com/articles/feature-toggles.html) (Pete Hodgson, ~39 min, optional). Video: [Feature Flags Suck!](https://www.youtube.com/watch?v=MDERgrcaT6w) (Pete Hodgson, 29:56).

---

**Core time for this lens:** about 3 h 25 min (the ten core entries above, optional videos excluded). The two optional entries add about 45 min.
