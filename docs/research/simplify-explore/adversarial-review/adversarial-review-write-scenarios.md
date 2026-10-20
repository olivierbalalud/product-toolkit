# Adversarial Review: write-scenarios.md

## 1. The Brief
- **Target Artifact**: `write-scenarios.md` specification and related Gherkin/test guidelines (`01-lifecycle-and-gates.md`, `03-design-playbook.md`, `04-dev-playbook.md`).
- **Objective**: Stress-test the multi-mode Gherkin authoring skill (`draft`, `move`, `story`), evaluating its coupling with use cases, test automation layers, and file management mechanics.
- **Context**: The artifact was authored by an LLM to govern BDD scenario generation. This evaluation acts as an adversarial critique against BDD best practices (Dan North, Gojko Adzic's *Specification by Example*), cucumber anti-patterns, maintainability, and delivery flow.

---

## 2. Approach Taken
The review followed a structured three-step adversarial methodology:
1. **Generic Adversarial Review**: Core technical evaluation against BDD principles, test design theory, maintenance overhead, and file movement semantics.
2. **Adversarial Review across 6 Personas**: Deep-dive evaluation of developer experience, product clarity, design flexibility, and regulatory auditability across six roles:
   - Software Engineer / Technical Architect
   - Product Manager (PM)
   - UX Designer
   - Business Process Owner (Non-technical, mid-cap company)
   - Compliance & Regulatory Officer / Team Lead (Mid-cap company)
   - Small Startup CTO / CEO
3. **Synthesis & Actionable Recommendations**: Consolidating findings into concrete modifications for `write-scenarios.md`.

---

## 3. Outcome of the Adversarial Review

### 3.1 Step 1: Generic Adversarial Review

1. **Premature and Fragmented File Lifecycle (`draft` -> `move` -> `story`)**:
   - The skill creates `.feature` files in three distinct phases. Maintaining draft scenarios in `use-cases/UC-.../scenarios.draft.feature` and physically moving them into `stories/US-.../features/` via a custom Python script (`move_drafts.py`) creates unnecessary file churn and state drift.
   - Unclaimed draft scenarios linger indefinitely in the use case folder, creating split sources of truth.

2. **Conflating Acceptance Criteria with Test Implementation**:
   - The framework dictates that `.feature` files are the *only* acceptance criteria.
   - BDD scenarios should specify business rules through examples. Forcing Gherkin to act as the exhaustive design specification, API schema validation, and edge-case tracker turns readable specifications into brittle, bloated end-to-end test scripts.

3. **Copy-Key Pollution in Gherkin Scenarios**:
   - Step 4 mandates referencing UI text by copy key (e.g., `"checkout.payment.submit"`) and tagging scenarios with `@ui`.
   - This violates core BDD doctrine: scenarios become tightly coupled to front-end translation keys, rendering feature files unreadable to business stakeholders and brittle to UI refactoring.

4. **Step-Definition Binding Brittleness**:
   - The spec forces reuse of existing step definitions across unrelated domains. This frequently causes accidental coupling between contexts, where changing a step definition for one story breaks historical, frozen `.feature` files elsewhere.

---

### 3.2 Step 2: Adversarial Review from 6 Personas

#### Persona 1: Software Engineer / Technical Architect
- **Test Pyramid Distortion**: Running all Gherkin scenarios against both the business layer (fakes) and UI (Playwright-BDD) duplicates execution cost and leads to slow, flaky CI runs.
- **Git Conflict Generator**: Moving text lines between parent and child `.feature` files across concurrent branches causes frequent Git merge conflicts.
- **Step Explosion**: Reusing step text across multiple features without strict domain boundaries turns `tests/bdd/steps/` into an unmaintainable monolith.

#### Persona 2: Product Manager (PM)
- **Loss of Business Readability**: Injecting technical tokens, copy keys (`"room.booking.confirm"`), and extension IDs (`@UC-012.3a`) prevents non-technical business partners from reading or validating scenarios.
- **Specification Bloat**: Exhaustively converting every minor extension into full Gherkin produces dozens of scenarios per story, obscuring the primary business intent.

#### Persona 3: UX Designer
- **Premature UI Freezing**: Tagging scenarios with `@ui` based on copy keys before design prototypes are validated forces UX designers to design around predetermined text keys rather than user needs.
- **Inability to Represent Dynamic Micro-Interactions**: Gherkin's linear `Given/When/Then` structure fails to express modern interaction design patterns (gestures, animations, skeleton loading, optimistic UI updates).

#### Persona 4: Business Process Owner (Non-Technical, Mid-Cap)
- **Total Disconnect from Natural Language**: Gherkin is marketed as living documentation for business stakeholders, but rigid syntactic rules, regex constraints, and technical ID tagging make it an engineering tool rather than a shared business vocabulary.
- **Absence of Business Process Viewpoints**: Feature files test micro-level system reactions rather than end-to-end business operations or operational handoffs.

#### Persona 5: Compliance & Regulatory Officer (Mid-Cap)
- **Illusion of Audit Coverage**: Having a green `@UC-012.3a` Gherkin test does not prove legal compliance (e.g., that data is cryptographically erased under GDPR or that AI outputs are auditable); it only proves the happy path of the mock passed.
- **Traceability Gaps**: Scenarios focus on system steps but omit the capture of non-repudiation metadata (e.g., user IP, consent timestamps, immutable audit log verification).

#### Persona 6: Small Startup CTO / CEO
- **Engineering Drag**: Writing, maintaining, and debugging step definitions in two languages/layers (FastAPI business layer + Playwright browser) for every slice is too slow for early-stage discovery.
- **Tooling Overhead**: Maintaining custom Gherkin linters (`lint_gherkin.py`) and file-migration scripts (`move_drafts.py`) creates non-revenue-generating engineering overhead.

---

### 3.3 Step 3: Synthesis & Actionable Recommendations

| Section in `write-scenarios.md` | Current Rule / Specification | Recommended Adversarial Fix | Primary Driving Personas |
|---|---|---|---|
| **2. Scope & 6. Procedure** | Three-mode lifecycle (`draft`, `move`, `story`) moving scenarios between files. | **Eliminate Draft/Move Lifecycle:** Do not write `.feature` files at the Use Case level. Write Gherkin scenarios directly within the story directory once the story is cut. | Architect, PM, Startup CEO |
| **5. Outputs & 6. Procedure** | Scenarios embed raw translation/copy keys (e.g., `"checkout.payment.submit"`). | **Enforce Domain Language:** Scenarios must use human-readable business terms. UI copy keys belong strictly inside UI step definition implementations, not feature files. | PM, UX, BPO |
| **0. Header & 2. Scope** | Feature files serve as the sole acceptance criteria. | **Decouple Acceptance Criteria:** Use structured Markdown for business acceptance criteria (rules); use Gherkin strictly for illustrative executable examples that verify those rules. | PM, BPO, Compliance |
| **7. Scripts vs Judgement** | `move_drafts.py` deterministically moves lines between markdown/feature files. | **Deprecate `move_drafts.py`:** Replace mechanical file refactoring with unified story scenario generation. | Architect, Startup CEO |
| **6. Procedure (Step 2)** | Global reuse of existing step definitions across all domains. | **Domain-Scoped Step Definitions:** Enforce domain boundaries for step reuse to prevent global step definition coupling. | Architect |