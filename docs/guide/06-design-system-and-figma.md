# 6. Design System and Figma

The **look** layer: tokens, components and motion, and how the design tools, Figma and Claude Design, stay in step with code. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). Figma plans, limits and pitfalls come from the [tooling research](../research/tooling-landscape.md) (2026-10-19); concepts are explained in the [UX lens](../foundations/ux-lens.md).

## 6.1 Principles

1. **Code is the source of truth for the look** [R1-Q3]. **Code is the hub; each design tool is a spoke** that reads from it [R18-Q1]. Figma is also the visual archive, used to review, annotate and go back to, for every PRD [R2-Q1, R18-Q5].
2. **One source of truth per layer**, and nothing flows against it automatically [R3-Q2, R3-Q7]:

   | Layer | Source of truth | Goes the other way as |
   |---|---|---|
   | Tokens | DTCG JSON in git | A PR that Claude prepares from a Figma variables diff, reviewed like any PR |
   | Components | `src/packages/ui` | A design-system enabler slice |
   | Flows and screens | The prototype, then the slice | Snapshots into Figma; a change from Figma is a DCR |

3. **The look is global.** A PRD uses the design system; it never changes it. Changes go through an enabler slice, one at a time [R2-Q9, R2-Q3 (g)].
4. **Web only for now**, built so native can follow: semantic tokens, Style Dictionary targets, no web-only token names [R3-Q8].

## 6.2 Tools and seats

| Tool | Role | Cost | Decision |
|---|---|---|---|
| **Figma Professional** | Design tool of record: visual review, annotation, the "go back" target | 1 Full seat (the technical founder) + 1–2 Dev seats, about $40–52 a month | R2-Q1 |
| **Obra shadcn/ui kit** | The Figma base library: free, MIT, variables-first, tracks shadcn | Free | R3-Q3 |
| **Code Connect** | Maps Figma components to `src/packages/ui`, so the Figma MCP emits our real components | Included (Dev or Full seat) | R3-Q3 |
| **Figma MCP** (remote) | Reads design context and variables; writes to the canvas (`use_figma`, code-to-canvas) | Included; write-to-canvas is free during its beta and will become paid | R3-B1, R3-Q2 |
| **Storybook + Chromatic** | Shows coded components and screens, inside Figma through Storybook Connect; visual regression tests | Chromatic free tier: 5,000 snapshots a month | R3-Q3 |
| **Claude Design** | The alternative exploration tool, chosen per PRD (`design_tool: claude-design`). Never canonical: no version history, basic multi-user editing. In Claude Code through `/design` and `/design-sync`; the standalone claude.ai/design closes on 2026-12-14 | In the Claude subscription | R2-Q1, R18-Q4 |

Not used: Builder.io, Lovable and Cursor (R2-Q1), Tokens Studio (paid and unclear, R3-Q2), and Figma Make, whose one-way push overwrites the repository (research §2).

**Plan limits to know.** On Professional, Code Connect allows **one library and one framework**. When native mobile arrives, that becomes an ADR; Organization costs about $55 per Full seat [R3-Q3]. The Figma Variables REST API is Enterprise only, which is why tokens move through the MCP or a JSON file [R3-Q2].

## 6.3 Two design tools, one design system

The PM or UX designer explores each PRD in **one** tool, Figma or Claude Design, and stays with it for that PRD ([chapter 3, §3.4](03-design-playbook.md#34-step-3-start-exploring)) [R18-Q4]. Both tools must see the **same design system**, so each holds a **mirror** of the one in code [R18-Q3]:

| Mirror | Built from code by | Refreshed |
|---|---|---|
| Figma library | Variables (JSON import or MCP), the Obra kit, Code Connect maps | By the technical founder |
| Claude Design design system | `/design-sync` in Claude Code, which uploads the repo's React components | By hand: Claude Design has no automatic refresh, and the first sync of a large repo can take hours |

Rules [R18-Q1–Q3, R18-Q5]:

- **Every design-system enabler slice re-syncs both mirrors** as part of its done criteria ([`enb.md`](../templates/enb.md)).
- **`docs/design/design-system.md` records the commit each mirror was last synced from.** The gate check warns when a PRD's tool mirror is older than the last design-system change.
- **Neither tool changes the look.** A token or component change made in a tool is a request for an enabler slice, not a change.
- **Neither tool's files are a record.** A new exploration starts from what is built, never from an earlier PRD's tool files, so a PRD designed in Figma can be followed by one explored in Claude Design, and the other way round.
- **Snapshots go to Figma for every PRD**, whichever tool explored it (§6.7).

**Switching tools between PRDs costs a little:** to change screens built from an earlier PRD in the other tool, the designer recreates today's screen in the chosen tool. In Claude Design, from screenshots of the running app, since it cannot open Figma frames as editable screens; in Figma, by duplicating the `as-built` page.

## 6.4 Tokens

```
src/packages/tokens/
  src/*.json          DTCG, canonical (colour, spacing, radius, typography…)
  src/motion.json     durations, easings, distances [R3-Q6′]
  build/              Style Dictionary output (generated)
```

1. **DTCG JSON is canonical** [R3-Q2].
2. **Style Dictionary builds `tokens.css`**: the shadcn semantic pairs under `:root` and `.dark`, and `@theme inline`. A new token must appear in all three places, which the build guarantees. A hand-kept `globals.css` imports it. CI flags any CSS variable defined outside `tokens.css`, such as one the shadcn CLI adds with a new component; the enabler that added the component moves it into DTCG. The build also writes the Figma variables import file, and native token files later [R3-Q2, R3-Q8, R20-Q1, R20-Q4].
3. **Into Figma:** the technical founder imports the generated variables file, or updates variables through the MCP (`use_figma`) [R3-Q2, R20-Q4].
4. **Back from Figma:** a token changed in Figma comes back as a **PR prepared by Claude** from a `get_variable_defs` diff, never applied automatically [R3-Q2].
5. **Lint** forbids raw colours, arbitrary Tailwind values (`bg-[#123456]`) and raw durations in feature code [R3-Q2, R3-Q6′].
6. Tokens are a **standalone package**, so the separate company website could use the brand tokens later [R2-Q10].

Known losses in the Figma round-trip: exports drop descriptions, add Figma IDs under `$extensions`, and colour-space rounding creates noisy diffs. Review token PRs for these (research, pitfall 4).

**Names** [R17-Q1]: Figma variable names **mirror the DTCG paths exactly**, with `/` in place of `.` (`color/primary/default` ↔ `color.primary.default`). The mapping from DTCG paths to shadcn CSS variable names (`--primary`) lives in the Style Dictionary configuration, and the build writes it as a table into `docs/design/design-system.md`. A rename is made in DTCG and flows out from there.

## 6.5 Components

- `src/packages/ui` is a **pnpm workspace package** (`@<org>/ui`), following shadcn's monorepo setup: `shadcn add` writes into it. Nothing is served, so nothing is public [R3-Q5′].
- A **registry** is needed only if another repository, such as the website, must pull components. That is an ADR: a private registry with a token, or a public one if the components aren't sensitive [R3-Q5′].
- **Third-party blocks** (e.g. ReUI, Motion Primitives) enter only through a design-system enabler slice, never from a feature PRD [R3-Q5′].
- A **new component** needed by a PRD is an enabler slice with `adds_ds_component: true`. It goes through *Exploring* and the UX persona review before it is built [R2-Q3 (g), R7-Q2].
- Each component has **Storybook stories**, and a **Code Connect** map to its Figma counterpart [R3-Q3]. The map lives **beside the component** in `src/packages/ui`, and a CI check fails when a component is renamed or removed without its map. Whether the Code Connect CLI can run that check is to be verified when it is built [R17-Q2].

## 6.6 Motion

[R3-Q6′]

| What | Where | Rule |
|---|---|---|
| Motion tokens: durations, easings, distances | `src/packages/tokens/src/motion.json` | Built to CSS variables and TS constants; shared across platforms |
| Motion presets: the implementation | `src/packages/ui/src/motion/` (`presets.ts`, `motion.css`, reduced-motion handling) | One Storybook story per preset; per platform |
| Motion policy and intent catalogue | `docs/design/motion.md` | Maps each intent ("confirm success", "reveal details") to a preset |

PRD flows name only the **intent**; feature code uses presets only, and lint forbids raw durations and transitions.

## 6.7 Snapshots: keeping Figma in step

| When | What | Where in Figma | Decision |
|---|---|---|---|
| During *Exploring*, when useful | Prototype screens, captured with code-to-canvas | Drafts, for annotation | R2-Q1 |
| At Design-complete | The prototype's screens | A frozen `PRD-012.1 / design-complete` page | R3-Q7 |
| At Done | The built screens | An `as-built` page | R3-Q7 |

Snapshots are captured **from code** with code-to-canvas, whichever tool explored the PRD, so Figma holds the visual history of every PRD [R18-Q5]. Code-to-canvas produces **flat layers**, not linked components, with matching variables bound. It is a snapshot, not a sync. Snapshots are **never merged back** into code automatically [R3-Q7]. A PRD explored in Claude Design also keeps its final export in `design-export/` [R18-Q6].

**Going back to design:** duplicate the PRD's `as-built` page, change or annotate the duplicate, and raise a DCR. The DCR is worked in code, in a `design/DCR-…` worktree ([chapter 3, §3.9](03-design-playbook.md#39-changing-a-design-after-the-gate)) [R3-Q7, R10-Q1]. ### How the Figma files are organised

[R17-Q3]

| File | Contents |
|---|---|
| **Design-system library** | Based on the Obra kit: the variables and the components, mirroring code |
| **One product file per use case** | A page per PRD snapshot (`PRD-012.1 / design-complete`, `PRD-012.1 / as-built`), and a `drafts` page for captures during *Exploring*, including Claude Design screens pushed to Figma for review |

## 6.8 Pitfalls to watch

From the [tooling research](../research/tooling-landscape.md), with the rule that answers each one:

| Pitfall | Answered by |
|---|---|
| Two-way sync with no rule for who wins | One source of truth per layer (§6.1) |
| The two mirrors drift apart | Every design-system enabler re-syncs both; the gate check warns on a stale mirror (§6.3) |
| Claude Design has no version history | The record is the prototype in code, plus the final export (§6.7) |
| Screens and components don't merge back | Snapshots only; changes from Figma are DCRs |
| Plan limits move (write-to-canvas will become paid) | Re-check the plan before relying on a write path; the MCP's read tools are enough to keep working |
| Lossy token round-trips | Token PRs are reviewed, never auto-applied |
| Name drift between Figma and CSS | Figma names mirror DTCG paths; the CSS mapping is generated (§6.4) |
| Bypassing tokens | Lint in CI |
| Code Connect maps going stale | Maps beside each component, checked in CI (§6.5) |
| Per-screen tweaks to theme or motion | The look changes only through an enabler slice |
| Parallel worktrees editing tokens or `globals.css` | Shared layers change in one enabler slice at a time [R2-Q9] |

## 6.9 Where everything lives: the UX view

A map of the look layer across the repository and the two design tools. Paths follow the agreed layout [R3-Q1a–h, R13-Q0] and shadcn's monorepo setup (`packages/ui` holds shared components, `apps/web` the app; each has a `components.json`). Decisions in brackets point to the log.

```
docs/design/
  design-system.md        component inventory (with origin), token name table (generated),
                          mirror sync record: Figma and Claude Design [R17-Q1, R18-Q3]
  motion.md               motion policy and intent catalogue [R3-Q6′]
  voice-and-tone.md       voice guide (chapter 7)

src/packages/tokens/      the design tokens, canonical
  src/*.json              DTCG: colour, spacing, radius, typography…
  src/motion.json         durations, easings, distances [R3-Q6′]
  style-dictionary.config DTCG → CSS variable mapping [R17-Q1]
  build/                  generated: CSS variables, TS constants, Figma variables import file [R20-Q4]

src/packages/ui/          the design system: shared components (@<org>/ui) [R3-Q5′]
  components.json         shadcn config; registries for third-party sources
  package.json            the libraries: Tailwind v4, Radix, class-variance-authority, motion library
  src/styles/
    globals.css           hand-kept: Tailwind import and base layer; imports tokens.css [R20-Q1]
    tokens.css            generated from tokens: :root, .dark, @theme inline [R20-Q1]
  src/components/
    button.tsx            a shadcn component, as `shadcn add` writes it
    button.stories.tsx    its Storybook story
    button.figma.tsx      its Code Connect map, beside it [R17-Q2]
    …                     internal and third-party components sit here too [R20-Q2]
  src/motion/             presets.ts, motion.css, reduced-motion handling [R3-Q6′]
  src/hooks/, src/lib/    shared hooks; utils (cn)
  .storybook/             Storybook config; Chromatic publishes from here
  THIRD_PARTY.md          origin, version and licence of every pulled component [R20-Q2]

src/apps/web/
  components.json         shadcn config of the app
  components/             app-only compositions of design-system components [R20-Q3]
  app/(prototypes)/       prototype routes, excluded from production builds [R3-Q1g]
  mocks/                  MSW mocks of draft contracts

docs/product/…/US-012.1-<slug>/
  flows.md, copy.md       the flow and voice layers of the PRD
  design-export/          final Claude Design export, if design_tool is claude-design [R18-Q6]
```

| What | Where it lives | Notes |
|---|---|---|
| **Frameworks and libraries** (Tailwind, Radix, shadcn tooling, motion library) | Dependencies of `src/packages/ui/package.json` | Tailwind v4 is configured in CSS, so there is no `tailwind.config.js`. Feature code never imports the motion library directly; it uses presets [R3-Q6′] |
| **shadcn components** | `src/packages/ui/src/components/`, where `shadcn add` writes them when run from `src/apps/web` | Shared parts go to `packages/ui` and imports are rewritten to the package; app-only blocks go to `apps/web/components` (shadcn docs) |
| **Tokens** | `src/packages/tokens/src/` (DTCG, canonical); built CSS in `src/packages/ui/src/styles/` | Never edited in Figma or Claude Design [R3-Q2, R18-Q3] |
| **Motion** | Tokens in `src/packages/tokens/src/motion.json`; presets in `src/packages/ui/src/motion/`; policy in `docs/design/motion.md` | [R3-Q6′] |
| **Internally developed components** | `src/packages/ui/src/components/`, through a design-system enabler slice; origin `internal` in the inventory | [R7-Q2, R20-Q2] |
| **Components pulled from a registry or website** (e.g. ReUI, Motion Primitives, Optics) | `src/packages/ui/src/components/`, through an enabler slice only; origin, version and licence in `THIRD_PARTY.md`, origin `registry:<name>` in the inventory | Never added from a feature PRD [R3-Q5′]. **One primitives library, Radix:** a component built on another, such as Optics on Base UI (research §7), needs an ADR [R20-Q2] |
| **Design systems** | One, in code: `src/packages/tokens` + `src/packages/ui` | Mirrored in Figma and in Claude Design [R18-Q3] |
| **Figma** | Outside the repo: the design-system library file and one product file per use case [R17-Q3] | In the repo: the Code Connect maps, and the variables import file generated by the tokens build [R20-Q4] |
| **Claude Design** | Outside the repo: its design system, synced from `src/packages/ui` with `/design-sync` | In the repo: the sync record in `docs/design/design-system.md`, and each PRD's final export in `design-export/` [R18-Q3, R18-Q6] |
| **Storybook and Chromatic** | Stories beside each component; config in `src/packages/ui/.storybook/` | One story per motion preset [R3-Q6′] |
| **App-only components** | `src/apps/web/components/`: compositions of design-system components only, no styling beyond tokens. Promoted to `src/packages/ui` by an enabler once a second feature reuses one | [R20-Q3] |
| **Prototypes** | `src/apps/web/app/(prototypes)/`, moved into real routes during the slice | [R4-Q11] |
