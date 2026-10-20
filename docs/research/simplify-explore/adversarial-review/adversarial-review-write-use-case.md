# Adversarial Review: write-use-case.md

## 1. The Brief
- **Target Artifact**: `write-use-case.md` specification and related lifecycle/playbook documentation (`01-lifecycle-and-gates.md`, `02-artifacts-and-ids.md`, `03-design-playbook.md`).
- **Objective**: Stress-test the design, mechanics, and assumptions of `write-use-case.md` to identify structural flaws, bottlenecks, and anti-patterns.
- **Context**: The artifact was authored by an LLM within a gate-checked product delivery framework. This evaluation acts as an adversarial critique against industry standards (Cockburn, Jacobson, Agile user stories, compliance, and startup velocity).

---

## 2. Approach Taken
The review followed a structured three-step adversarial methodology:
1. **Generic Adversarial Review**: Core technical and architectural stress-testing against software engineering fundamentals, requirements theory (Alistair Cockburn's *Writing Effective Use Cases*, Ivar Jacobson's *Use Case 2.0*), and iterative delivery principles.
2. **Adversarial Review across 6 Personas**: Deep-dive critique evaluating organizational impact, interaction design, compliance, governance, and business feasibility across six distinct roles:
   - Software Engineer / Technical Architect
   - Product Manager (PM)
   - UX Designer
   - Business Process Owner (Non-technical, mid-cap company)
   - Compliance & Regulatory Officer / Team Lead (Mid-cap company)
   - Small Startup CTO / CEO
3. **Synthesis & Actionable Recommendations**: Consolidating findings into a clear matrix of actionable modifications to harden and refine `write-use-case.md`.

---

## 3. Outcome of the Adversarial Review

### 3.1 Step 1: Generic Adversarial Review

1. **Goal-Level Ambiguity (Missing Cockburn Goal Hierarchy)**:
   - The spec mandates Cockburn's "fully dressed" format but omits Cockburn’s primary classification: Goal Levels (Summary/Kite, User Goal/Sea Level, Subfunction/Fish).
   - Without constraining use cases strictly to **User Goal (Sea Level / Blue)**, requirements oscillate between multi-month business workflows and micro-interactions ("User enters text"), breaking downstream story sizing.

2. **Upfront Slicing Trap (Waterfall Anti-Pattern)**:
   - The requirement that all fields and every failure category across all steps must be 100% complete before any user story can be cut (`R4-Q2`) creates a Big Design Up Front (BDUF) bottleneck.
   - In modern elicitation (Jacobson's *Use Case 2.0*), use cases are discovered and delivered incrementally in thin vertical slices rather than fully exhausted upfront.

3. **Mechanical Matrix Explosion (N x 11 Grid)**:
   - Forcing an 8-step use case to run every step against 11 failure categories produces an 88-cell Cartesian matrix.
   - Actor actions are subjected to infrastructure concerns (e.g., "stale data" or "concurrent edit" on a step where a user reads a prompt), causing hallucinated edge cases or mindless boilerplate.

4. **Premature Formalization (Gherkin in Use Cases)**:
   - Step 5 requires generating `scenarios.draft.feature` using `write-scenarios` before a use case is considered complete.
   - Conflating behavioral requirements elicitation with executable test syntax at this early stage causes premature commitment to implementation details before UX flows and APIs are explored.

5. **UI Contamination**:
   - Alternating step definitions ("Actor does X, System does Y") frequently introduce screen widgets, modals, and click paths, violating the core principle that look and UI mechanics belong to *Exploring*.

---

### 3.2 Step 2: Adversarial Review from 6 Personas

#### Persona 1: Software Engineer / Technical Architect
- **Premature Infrastructure Invariants**: Demanding error-handling outcomes for edge cases like "conflict/concurrent edit" and "partial failure" during use case writing forces functional writers to make distributed-systems decisions (e.g., optimistic locking, idempotency keys, two-phase commits) before ADRs or architecture spikes exist.
- **Leaky Abstractions**: Concurrency, transport drops, and stale cache states are technical implementation details, not domain requirements of the primary actor.

#### Persona 2: Product Manager (PM)
- **Velocity Bottleneck**: The hard gate requirement prevents cutting MVP vertical paths when the core business flow is clear, delaying time-to-market.
- **Unweighted Complexity**: A rare, low-risk edge case requires the same structural ceremony (grid cells, extension IDs, draft Gherkin) as the primary revenue-generating flow.
- **Inflexible Traceability**: Updating a use case to reflect user feedback post-launch requires re-running verification scripts (`check_grid.py`) across legacy steps.

#### Persona 3: UX Designer
- **State Freezing Before Interaction Design**: Textually specifying recovery outcomes before wireframing or prototyping locks the team into predetermined assumptions (e.g., text banner vs. conversational recovery vs. inline correction).
- **Stripped Human Context**: Cockburn tables strip out cognitive load, emotional state, context of use, and multi-channel nuances.
- **Rigid Linearity**: Real users navigate non-linearly (tabs, deep links, multi-device handoffs), which rigid sequential step structures fail to capture.

#### Persona 4: Business Process Owner (Non-Technical, Mid-Cap)
- **Technical Jargon Alienation**: Gherkin syntax, concurrent edit handling, and API diff references make the artifact unreadable to business and operational stakeholders.
- **Absence of Real-World Handoffs**: Fails to model offline human-in-the-loop workflows, asynchronous managerial approvals, and manual exception escalation paths.
- **Missing Operational Context**: Does not address SLAs, cost impacts, RACI ownership, or business continuity plans.

#### Persona 5: Compliance & Regulatory Officer (Mid-Cap)
- **Trivialization of Regulatory Obligations**: Treats `privacy request` as a single generic step failure checkbox alongside "not found" or "invalid input."
- **Missing AI Governance Gate**: Despite AI features being governed downstream, the use case lacks mandatory early elicitation of automated decision-making, bias risk, profiling, and EU AI Act classification.
- **Audit Trail Deficits**: Frontmatter driver assignments lack non-repudiation, role segregation, or formal sign-off history required by regulated audit frameworks (SOC 2, ISO 27001).

#### Persona 6: Small Startup CTO / CEO
- **Process Bureaucracy**: Managing an elaborate chain of multi-tiered artifacts, custom Python linters, and strict gates burns runway and reduces agility.
- **Brittle Automation**: Custom gate scripts break frequently when product discovery is volatile, forcing engineers to debug process tooling rather than shipping customer value.
- **Context Fragmentation**: Juggling four interconnected skills (`write-use-case`, `write-scenarios`, `write-stories`, `check-gate`) causes high cognitive load.

---

### 3.3 Step 3: Synthesis & Actionable Recommendations

| Section in `write-use-case.md` | Current Rule / Specification | Recommended Adversarial Fix | Primary Driving Personas |
|---|---|---|---|
| **0. Header & 2. Scope** | "Fully dressed" format with undefined scope level. | Enforce **Sea-Level / User Goal** (Elementary Business Process) only. Strictly reject Kite (Summary) and Fish/Clam (Subfunction) scopes. | Architect, PM, Startup CEO |
| **2. Scope & 6. Procedure (Step 5)** | Draft Gherkin scenarios (`scenarios.draft.feature`) required before use case completion. | **Remove Gherkin from the Use Case stage.** Express extensions strictly in Cockburn format (condition + business handling + target step). Defer Gherkin to `write-scenarios` during *Exploring*. | UX, PM, Architect, BPO |
| **6. Procedure (Step 4)** | Exhaustive Cartesian grid (N steps x 11 categories) evaluated identically across all steps. | **Semantic Partitioning:** Apply failure categories conditionally: User steps evaluate behavioral exceptions; System/I/O steps evaluate infrastructural exceptions. | Architect, Startup CEO, PM |
| **6. Procedure (Step 4)** | `privacy request` included as an incidental failure category. | **Elevate Compliance:** Remove privacy from step cells. Add a dedicated upfront "Regulatory & Data Classification" section (GDPR, personal data touched, automated decision-making). | Compliance Officer |
| **1. Lifecycle & Gates** | Hard gate: 100% of extensions and categories must be completed before cutting any story. | **Enable Sliced Maturity:** Allow a `Core-Complete` status (Main Success Scenario + critical business extensions) so MVP vertical stories can be cut immediately. | PM, Startup CEO |
| **14. Gotchas** | Focuses on step numbering and deferred flags. | Add **UI-Free Mandate**: explicitly reject any reference to screens, modals, clicks, or visual widgets in use case steps. | UX Designer, Architect |