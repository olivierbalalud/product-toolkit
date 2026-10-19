# 8. Testing

What is tested, where the tests live, which tool runs them and when they must pass. The order in which a slice writes them is in [chapter 4, §4.7](04-dev-playbook.md#47-the-test-first-order). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

**In scope:** functional tests (from the specs), technical tests, security tests and privacy tests. **Out of scope:** the other "-ilities" (performance, load, availability and so on), which are tested separately, outside this framework (brief; [R12-Q5]).

## 8.1 Where each kind of test comes from

| Source | Becomes | Decision |
|---|---|---|
| Use-case extensions | Gherkin scenarios that cover them, or a `deferred` / `out-of-scope` mark | R1-Q7 |
| Story acceptance | Gherkin scenarios: the only acceptance criteria | R3-C1 |
| PRD §10 Who may perform each action | The authorisation test matrix | R4-Q9 |
| PRD §11 Privacy data inventory | Privacy tests | R4-Q9 |
| PRD §4 Measurement plan | Assertions that events are emitted | R4-Q4c |
| Contract | The OpenAPI diff check | R4-Q8c |
| Existing untested code that will change | Characterisation tests | R4-Q8d |
| Each line of code written | Unit tests, through TDD | R4-Q8′ |

## 8.2 Test layers

| Layer | Tool | Location | Runs against | Decision |
|---|---|---|---|---|
| **Acceptance, business layer** | pytest-bdd | `src/domains/<d>/tests/bdd/steps/`, loading the `.feature` files from `docs/product/…/features/` by path and tag | The business layer, with **fakes** behind every port | R1-Q15, R3-Q1a |
| **Acceptance, UI** | playwright-bdd | `src/apps/web/e2e/` | The running web app and API in the worktree's environment; `@ui` scenarios only | R1-Q15, R3-Q1g, R14-Q2 |
| **Unit** | pytest; the web test runner | `tests/unit/`, beside web code | One module | R4-Q8′ |
| **Integration** | pytest | `tests/integration/` | Real adapters against a **real Postgres**, one database per worktree | R4-Q8′, R2-Q9 |
| **API** | pytest | `tests/` of the domain | The FastAPI app | R4-Q8′ |
| **Contract** | OpenAPI diff (e.g. `oasdiff`) | CI | The generated spec vs `main` | R4-Q8c |
| **Characterisation** | pytest | beside the code they pin | Today's behaviour of legacy code | R4-Q8d |
| **Security and privacy** | pytest | `tests/security/` | Business layer and API | R4-Q9 |
| **Architecture** | import-linter | CI | Imports: `business/` uses neither FastAPI nor SQLAlchemy | R3-Q1f |
| **Visual** | Storybook and Chromatic | `src/packages/ui/` stories | Components and screens vs the design-complete snapshot | R2-Q5, R3-Q3 |
| **i18n** | ICU message and placeholder validation | CI | Every catalog in `src/packages/i18n/messages/` | R2-Q6 |
| **Lint** | linters | CI | No raw colours, arbitrary Tailwind values or raw durations; i18n keys only | R3-Q2, R3-Q6′, R4-Q11 |

## 8.3 Gherkin rules

- **English only**, whatever the PRD's source language, so steps never turn into French identifiers [R3-Q1a].
- **Tags** on every scenario: the story and the use-case step or extension, e.g. `@US-012.1 @UC-012.3a` [R3-Q1a].
- **Domain words** are the glossary's English terms. A step-vocabulary check flags words that are not in the glossary [R3-C3].
- **UI text** is referenced by copy-deck key, only where the exact wording matters. Playwright steps resolve keys through the next-intl catalogs, so the same scenarios run in every locale, which also tests the translations [R3-C2].
- **Reuse** existing step wording where it fits, so existing step definitions bind [R4-Q8b′].
- **Frozen at Design-complete.** A wording tweak for testability is allowed; any change in meaning needs a DCR or a later PRD's amendment [R3-Q1a, R4-Q8e′].

### Which scenarios run in which layer

Every scenario runs on the **business layer**. Scenarios tagged **`@ui`** also run in **playwright-bdd**, following the test pyramid: many fast tests, few slow ones [R14-Q2].

- The scenario's author adds `@ui` during *Exploring*; the Eng persona checks the tags.
- The gate check enforces two rules: any scenario that references a copy key is `@ui`, and every screen in `flows.md` has at least one `@ui` scenario.
- `@ui` scenarios run in every enabled locale on the slice PR, while there are two locales. Revisit when a third arrives.

## 8.4 Fakes and ports

- Every port in `business/ports/` has a fake in `tests/fakes/`. Acceptance scenarios on the business layer use only fakes, so they are fast and need no services [R1-Q15].
- The **analytics port** has a fake that records events, so tests can assert that the measurement plan's events are emitted, even before the real pipeline exists [R4-Q4c, R4-Q4d].
- Adapters are tested for real in the integration layer, never through their fakes.
- **Third-party APIs, LLM providers included,** are replaced in adapter tests by **responses recorded at the port level**. A person re-records them deliberately, never CI, and scrubs secrets and personal data before committing them [R14-Q4].

## 8.5 Security and privacy tests

The minimum for every slice [R4-Q9]:

| Area | Tests |
|---|---|
| Authorisation | Generated from PRD §10: every role × action, both allowed and denied. |
| Privacy | From PRD §11: retention; erasure and pseudonymisation; no personal data in logs; API responses return only what their purpose needs. |
| Security | The OWASP ASVS level 1 items relevant to the slice. |
| AI | For slices touching the LLM gateway or AI features: review against the OWASP Top 10 for LLM Applications, in the security lane [R12-Q6b]. |
| CI-wide | Dependency scanning and secret scanning. |

The security and privacy lane checks that these tests exist ([chapter 9](09-review-lanes.md)) [R4-Q7a].

## 8.6 Environments and data

- **Design worktrees** run the frontend only, against MSW mocks of the draft contract. Prototype routes need no tests [R2-Q9, R4-Q11].
- **Slice worktrees** get their own ports, Compose project and database from the `WorktreeCreate` hook, so integration and UI tests of two slices never share data [R2-Q9].
- **Each test owns its data.** It passes in any order, in parallel, and when run twice [R14-Q4].
- **Fixtures are synthetic.** Production data never goes into tests, fixtures or CI artifacts [R14-Q4].

## 8.7 AI feature evaluation

Recorded responses make AI features deterministic in tests, but say nothing about output quality when a prompt or model changes [R14-Q5].

- Each AI feature has an **eval set**: example inputs, the properties the output must have, and graders (rules or an LLM judge). It is listed in PRD §11b with its pass threshold.
- It runs in CI on PRs that change that feature's prompts or model configuration. A score below the threshold is a **blocking** finding.
- Eval runs are billed model calls and count against the monthly budget, like the skill evals [R5-Q4c].

## 8.8 Coverage

- **The gate is requirement coverage:** `coverage.md` green, every extension covered by a scenario or marked `deferred` / `out-of-scope` [R1-Q7, R14-Q3].
- **Line and branch coverage** are reported in CI.
- **Diff coverage** (the share of changed lines that tests cover) is shown on every PR; below 80% the code lane raises an **advisory** finding. No percentage blocks a merge [R14-Q3].

## 8.9 Results and traceability

- **Test results and reports are never committed.** JUnit files, Playwright reports and coverage go to CI artifacts, linked from the PR. A local `reports/` folder is gitignored [R3-Q1b].
- **Committed:** only the generated `coverage.md` per use case, mapping each extension to its scenarios [R3-Q1b].
- **CI artifact:** a traceability report, extension → scenario → result per test layer [R3-Q1b].

## 8.10 What runs on which PR

| PR | Runs | Decision |
|---|---|---|
| Design PR (`design/…`) | Lint (prototype routes included), gate check, coverage, step-vocabulary check, UX lane guideline checks | R4-Q11, R4-Q12, R4-Q7d |
| Slice PR (`slice/…`) | Everything in §8.2, `@ui` scenarios in every enabled locale, AI eval sets when prompts or model configuration change, gate check, all applicable review lanes | R2-Q5, R4-Q7b, R14-Q2, R14-Q5 |
| Enabler PR (`enb/…`) | Everything in §8.2 that its changes touch, gate check, code and security lanes, UX when the UI is touched | R7-Q2, R15-Q1 |
| Fix PR (`fix/…`) | Everything in §8.2 that its changes touch; a regression test tagged with the scenario; code and security lanes, UX when the UI is touched | R5-Q2, R7-Q4 |
