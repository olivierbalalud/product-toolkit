# Adversarial Review: write-stories.md

## 1. The Brief
- **Target Artifact**: `write-stories.md` specification and story-cutting workflow (`01-lifecycle-and-gates.md`, `02-artifacts-and-ids.md`, `03-design-playbook.md`).
- **Objective**: Stress-test the user story slicing methodology, INVEST validation criteria, and coupling with use case extensions and PRD lifecycles.
- **Context**: The artifact was authored by an LLM to govern the transition from Use Cases to User Stories and Draft PRDs. This evaluation acts as an adversarial critique against Agile principles, Extreme Programming (XP), lean product management, and team autonomy.

---

## 2. Approach Taken
The review followed a structured three-step adversarial methodology:
1. **Generic Adversarial Review**: Core evaluation against XP fundamentals (Beck, Jeffries), Agile slicing heuristics (Richard Lawrence, Bill Wake's INVEST), and delivery throughput.
2. **Adversarial Review across 6 Personas**: Deep-dive evaluation across six roles:
   - Software Engineer / Technical Architect
   - Product Manager (PM)
   - UX Designer
   - Business Process Owner (Non-technical, mid-cap company)
   - Compliance & Regulatory Officer / Team Lead (Mid-cap company)
   - Small Startup CTO / CEO
3. **Synthesis & Actionable Recommendations**: Consolidating findings into concrete improvements for `write-stories.md`.

---

## 3. Outcome of the Adversarial Review

### 3.1 Step 1: Generic Adversarial Review

1. **Mechanical Decomposition vs. True Slicing**:
   - The skill defines story cutting as grouping use case steps and claiming extensions.
   - This is mechanical decomposition, not value-based slicing. It encourages slicing by execution path (e.g., "Story 1 = Steps 1-3", "Story 2 = Steps 4-6") rather than thin end-to-end value increments (e.g., Simple Booking with Cash -> Booking with Credit Card -> Booking with Promo Codes).

2. **False Conformance to INVEST "Independent"**:
   - The spec claims stories must be independent (`Independent: It can be designed, built and shipped without waiting for another story`).
   - Slicing an 8-step use case into sequential path stories inherently violates Independence: Step 4 cannot function in production without Steps 1-3 having run. This forces artificial dependencies and staging workarounds.

3. **Artifact Duplication (1:1 Story to PRD Tight Coupling)**:
   - Section 0 and 2 enforce a strict 1:1:1:1 mapping: One Story = One PRD = One Slice = One PR (`R1-Q9`).
   - A User Story (XP) is a lightweight planning placeholder; a PRD is a comprehensive requirements dossier. Forcing every single user story—even minor single-day enhancements—to generate a full PRD folder with 7 companion files (`flows.md`, `copy.md`, `fit.md`, `contract.draft.yaml`, `reviews.md`, etc.) introduces excessive administrative ceremony.

4. **Negotiability Violation (The Three Cs)**:
   - Under Ron Jeffries' Three Cs, a story is a *Card* representing a promise for a *Conversation*.
   - Pre-allocating all use case extensions into fixed story buckets with automated gate scripts (`check_cut.py`) locks down the scope before the team conversation and discovery even begin.

---

### 3.2 Step 2: Adversarial Review from 6 Personas

#### Persona 1: Software Engineer / Technical Architect
- **Artificial Slicing Inefficiencies**: Forcing vertical slices through all layers (UI, API, DB, security) for minor edge cases wastes time. If a database model or shared adapter needs to evolve, doing it through small, disjointed feature slices causes continuous schema migrations and integration churn.
- **Premature Contract Definition**: Forcing each cut story to immediately define API contract drafts (`contract.draft.yaml`) before developer refinement leads to speculative contracts that are rewritten during development.

#### Persona 2: Product Manager (PM)
- **Loss of Strategic Outcome Focus**: The story statement is reduced to an accounting mechanism for claiming use case extensions (`coverage.md`). The focus shifts from "Did we move the product metric?" to "Did we check off all extension IDs?"
- **Inflexible Release Packaging**: Because every story is tied 1:1 to an isolated PRD and slice PR, releasing a cohesive feature set requires orchestrating multiple independent PR merges and cherry-picks.

#### Persona 3: UX Designer
- **Fragmented User Experiences**: Slicing by use-case paths fractures UI design. A designer cannot design a cohesive screen flow in `flows.md` if Story 1 only covers inputs and Story 2 covers error states on the same screen. UX must design holistic journeys, not piecemeal steps.
- **Coordination Overhead**: Updating a common screen layout requires raising Design Change Requests (DCRs) across multiple in-flight PRD directories.

#### Persona 4: Business Process Owner (Non-Technical, Mid-Cap)
- **Unrecognizable Increments**: Slicing along internal technical path boundaries often results in intermediate deployments that deliver no stand-alone operational business utility, confusing end-users and operational staff.
- **Missing Change Management**: The slicing criteria ignore organizational readiness (training, SOP updates, operational documentation), focusing entirely on code deployment.

#### Persona 5: Compliance & Regulatory Officer (Mid-Cap)
- **Fragmented Regulatory Posture**: When a workflow handling regulated data is cut across 3 different stories, privacy and security controls become fragmented. One story might implement data ingestion without the corresponding retention/erasure slice being scheduled for weeks, creating compliance exposure.
- **Loss of Holistic Risk Assessment**: Assessing an AI feature or financial transaction slice-by-slice blinds compliance officers to the aggregate risk of the full workflow.

#### Persona 6: Small Startup CTO / CEO
- **Excessive Folder Overhead**: Creating separate directories, worktrees, and PRD packages for 3-day tasks kills shipping momentum.
- **Paralysis by Analysis**: Founders spend more time debating whether a slice is purely "INVEST-compliant" and passing `check_cut.py` than validating ideas with paying customers.

---

### 3.3 Step 3: Synthesis & Actionable Recommendations

| Section in `write-stories.md` | Current Rule / Specification | Recommended Adversarial Fix | Primary Driving Personas |
|---|---|---|---|
| **0. Header & 2. Scope** | Strict 1:1:1:1 invariant: One Story = One PRD = One Slice = One PR (`R1-Q9`). | **Flexible Story Packaging:** Allow multiple related stories to live under a single coherent Feature PRD. Reserve full PRD directories for major capabilities, not micro-slices. | Startup CEO, UX, PM |
| **6. Procedure (Step 1)** | Cutting stories strictly by chopping use case steps into sequential paths. | **Adopt Value-Based Slicing Patterns:** Slice by business variation, data simplicity, or operational rule complexity (e.g., SPIDR / Lawrence heuristics), ensuring every slice is a complete end-to-end thread. | PM, Architect, BPO |
| **2. Scope & 6. Procedure (Step 5)** | Calls `write-scenarios` in `move` mode to physically relocate draft scenarios. | **Direct Story Scenario Authoring:** Remove the `move` dependency. Author Gherkin scenarios directly for the story based on its specific business slice. | Architect, Startup CEO |
| **7. Scripts vs Judgement** | `check_cut.py` enforces mechanical validation that every extension is accounted for. | **Advisory Slicing Validation:** Downgrade `check_cut.py` from a blocking gate check to an advisory report highlighting unaddressed business risks. | Startup CEO, PM |
| **14. Gotchas** | Only warns about layer-only stories and tag mistagging. | Add **UX & Compliance Integrity Gotchas**: Warn against slicing that breaks user flow continuity or leaves sensitive data flows without end-to-end security controls. | UX Designer, Compliance |