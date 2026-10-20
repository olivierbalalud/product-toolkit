# 11. Tooling and Plugins

The third-party Claude Code plugins, skills and MCP servers the framework recommends, and how they are installed in the product monorepo. **Nothing is installed in this repository**; it only documents them [R1-Q2]. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). Sources, scores and full evidence are in the [skills research](../research/skills-landscape.md) and the [tooling research](../research/tooling-landscape.md) (2026-10-19). Facts about plugin configuration come from the Claude Code [plugin marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference) and [settings reference](https://code.claude.com/docs/en/settings-reference), checked on 2026-10-20.

## 11.1 Rules

1. **Project scope only.** Every plugin, skill and MCP server is installed at project level in the monorepo, never at user level [R3-B1 amendment, R3-B4].
2. **Pinned by commit SHA**, and **re-reviewed on every update** [R3-B4].
3. **No plugin whose hooks haven't been reviewed.** Shell commands that skills run (`` !`cmd` ``) are reviewed too [R3-B4].
4. **No skill that reads `.env` or calls third-party model or image APIs** [R3-B4].
5. **Our own skills ship as a plugin** from a marketplace inside the monorepo, so they are namespaced (`<plugin>:<skill>`) and a personal skill of the same name can't shadow them [R3-B6].
6. **Use Claude Code's mechanisms rather than override them** [R16-P].

## 11.2 Recommended

Commits are the HEAD of each repository's default branch on 2026-10-19, as recorded in the research; pin these or later reviewed commits. "Sec" is the research's security score; verdicts follow the skill-scout method.

### Design and product

| Plugin or skill | Source @ commit | Licence | For | Used in | Security | Cost |
|---|---|---|---|---|---|---|
| mattpocock skills: `grill-with-docs`, `domain-modeling`, `to-spec`, `to-tickets`, `tdd`, `code-review`, `implement-spec` | mattpocock/skills @`49dd158` | MIT | Interviews, glossary, tickets, TDD, code review, parallel implementation | Design, slice, code lane | Clean (P/P/P; `code-review` W011 explained) | Free |
| `ui-ux-pro-max` (**the skill folder only**, not the plugin) | nextlevelbuilder/ui-ux-pro-max-skill @`56ea9cf` | MIT | UX rules, palettes, accessibility checks, shadcn/Tailwind guidance | *Exploring*, UX lane | Sec 90. The plugin's sibling `design` skill reads `~/.claude/.env` and calls three image APIs, so it is excluded | Free |
| `frontend-design` | anthropics/skills @`dbd4588` | Apache-2.0 | Production UI generation baseline | Prototypes | Sec 100 | Free |
| `shadcn` | shadcn-ui/ui @`ba1503c` | MIT | shadcn components and CLI | Prototypes, design-system enablers | Runs `npx shadcn@latest info --json` when it loads: unpinned vendor CLI, accepted and noted | Free |
| Next.js skills | vercel/next.js `canary/skills` | MIT (Next.js repository) | App Router, caching, bundles | Prototypes, slices | Official | Free |
| `ux-copy` | anthropics/knowledge-work-plugins @`33eeda1` | Apache-2.0 | Microcopy, errors, empty states | Copy deck, UX lane | Sec 100 | Free |
| `ux-writing` | content-designer/ux-writing-skill @`98cacde` | MIT | UX writing, voice chart, error templates | Copy deck, UX lane | Sec 100; single maintainer | Free |
| `emil-design-eng`, `review-animations` | emilkowalski/skills @`2d22863` | MIT | Motion and micro-interactions | Motion presets, UX lane | Clean. **Not** `improve-animations` (hidden characters) | Free |
| `accessibility` | addyosmani/web-quality-skills @`afa8da9` | MIT | WCAG 2.2 | UX lane | Sec 100 | Free |
| Figma MCP server (remote) | `https://mcp.figma.com/mcp`, no Figma skills (unlicensed) | Figma terms | Design context, variables, code-to-canvas | Design, snapshots | Official | In the Figma seats (chapter 6) |
| Storybook Claude plugin | storybookjs/mcp @`4589b69` | MIT | Stories and UI states through `storybook ai` | Design system, UX lane | Sec 90; needs Storybook ≥ 10.5; monorepo support unverified | Free |

### Development and review

| Plugin or skill | Source @ commit | Licence | For | Used in | Security | Cost |
|---|---|---|---|---|---|---|
| `fastapi` | fastapi/fastapi (`.agents/skills/fastapi`) | MIT | FastAPI, Pydantic | Slices | Sec 100 | Free |
| `playwright-cli` | microsoft/playwright-cli @`b85c7a7` | Apache-2.0 | Browser automation | Slices, UX lane | Warnings explained (example credentials, browsing) | Free |
| `playwright-best-practices` | currents-dev/playwright-best-practices-skill @`283d5cb` | MIT | Playwright test practice | Slices | Sec 100 | Free |
| `playwright-bdd` | vitalets/playwright-bdd @`2084276` | MIT | Gherkin-first UI tests | Slices (`@ui` scenarios) | Sec 100; by the library's author | Free |
| `pr-review-toolkit`, `commit-commands`, `feature-dev` | anthropics/claude-plugins-official @`ea10b21` | Apache-2.0 | PR review agents, commits, feature flow | Code lane | No hooks | Free |
| `security-review` | getsentry/skills @`f57ada2` | Apache-2.0 | OWASP-style security review | Security lane | Two scanners flag it; the triggers are attack *examples* in a reference file. Accepted after review, pinned [R3-B2] | Free |
| Built-in `/security-review` | Claude Code | — | Security review of a diff | Security lane | Built in | In the subscription |

**Model usage** by plugins and our own skills counts against the Claude subscription interactively, and against the API budget in CI (review lanes, evals) [R5-Q4c, R15-Q3].

## 11.3 Considered and rejected

[R3-B1]

| Rejected | Why |
|---|---|
| impeccable | Fails the security gate (hook installer) |
| ECC, as a full plugin | 27 hooks on every tool call, some writing outside the project; cherry-pick ideas only |
| mattpocock `git-guardrails` | Writes `settings.json` |
| `security-guidance` (Anthropic) | Its hook `pip install`s an unpinned package |
| Vercel `web-design-guidelines`, `writing-guidelines` as published | No licence on the wrappers, and they fetch their rules from an unpinned URL at run time. Replaced by our own pinned copy [R3-B3, R3-D1–D7] |
| Skills under non-commercial licences | Licence |
| Builder.io, Lovable, Cursor, Figma Make, Tokens Studio | See [chapter 6](06-design-system-and-figma.md#62-tools-and-seats) [R2-Q1, R3-Q2] |
| i18n skills (lingui, i18next) | They match other libraries; next-intl has none, so it is one of our own skills [R3-B1, R3-Q4] |

## 11.4 Gaps: our own skills

Where nothing suitable exists, the framework specifies its own skills: [chapter 12](12-skills-to-build.md).

## 11.5 Which definition wins

Facts from the Claude Code documentation [R3-B5]:

| Kind | Precedence | Consequence |
|---|---|---|
| Skills | managed > **user > project** | A personal skill shadows a project skill of the same name, so ours ship in a plugin, where names are namespaced |
| Subagents | managed > `--agents` > **project > user** > plugin | |
| MCP servers | local > project (`.mcp.json`) > user > plugin > claude.ai connectors | The whole entry comes from one scope |
| Plugins | managed > flag > local > project > user | A user-installed plugin still loads in the project unless project settings set it to `false` |

**Collision hygiene** [R3-B7]: the committed `.claude/settings.json` sets known-conflicting plugins to `false` (for example a full ECC install), and a "doctor" check lists personal skills and agents in `~/.claude/` whose names clash with the project's, and user-level MCP servers that shadow project ones.

## 11.6 Wiring it in the monorepo

What the Claude Code reference documents:

- A **marketplace** is a repository or folder with `.claude-plugin/marketplace.json`. Each **plugin entry** has a `source`: a relative path (`./plugins/<name>`) inside the marketplace, or a `github`, `url` or `git-subdir` source, each with an optional **`sha`** (a full 40-character commit) that Claude Code checks out.
- A fetched plugin **without its own `plugin.json` takes the marketplace entry as its manifest**, so a bare skill folder in another repository can be wrapped as a plugin with a `git-subdir` source and a `skills` field.
- `extraKnownMarketplaces` in the project's `.claude/settings.json` registers marketplaces for everyone who opens the repository, after they accept the workspace-trust dialog. `enabledPlugins`, keyed `plugin@marketplace`, turns plugins on or off.
- A `directory` marketplace source takes an **absolute** path, which doesn't suit a repository cloned on several machines; a `github` marketplace source takes `repo`, `ref` and `path`.
- `claude --plugin-dir <path>` loads a plugin from a local directory or `.zip` **for that session only**; the flag can be repeated ([CLI reference](https://code.claude.com/docs/en/cli-reference)).
- **MCP servers** for the review lanes are declared once in the project's `.mcp.json`, because plugin subagents ignore `mcpServers` [R4-Q7e].

### Decisions

- **The marketplace lives in the monorepo** at `tools/claude-marketplace/`, registered as a `github` marketplace source (`repo` + `path`), so it works on every clone [R24-Q1].
- **Our own plugin** sits in `tools/claude-marketplace/plugins/<plugin>/`, listed with a relative-path source. It is developed and tested locally with `claude --plugin-dir tools/claude-marketplace/plugins/<plugin>` before its changes merge [R24-Q1].
- **Third-party skills that aren't plugins** (`ui-ux-pro-max`, `playwright-best-practices`, `playwright-bdd`, `accessibility`, `ux-writing`, the emilkowalski skills, `fastapi`) are **wrapped** as marketplace entries with a `git-subdir` source pinned by `sha` and a `skills` field, never copied into the monorepo. Check each wrapper with `claude plugin validate` when it is added [R24-Q2].
- **Third-party plugins** (mattpocock skills, `pr-review-toolkit`, the Storybook plugin and the others) are listed in the same marketplace with their own pinned `sha`, so every pin lives in one file [R3-B4, R3-B6].

### Example only

This is documentation for the monorepo team to adapt; nothing in this repository loads it [R5-Q5]. Names in angle brackets are placeholders.

`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "<org>-tools": {
      "source": { "source": "github", "repo": "<org>/<monorepo>", "path": "tools/claude-marketplace" }
    }
  },
  "enabledPlugins": {
    "<plugin>@<org>-tools": true,
    "mattpocock-skills@<org>-tools": true,
    "ui-ux-pro-max@<org>-tools": true,
    "<conflicting-plugin>@<marketplace>": false
  }
}
```

`tools/claude-marketplace/.claude-plugin/marketplace.json`:

```json
{
  "name": "<org>-tools",
  "plugins": [
    { "name": "<plugin>", "source": "./plugins/<plugin>" },
    {
      "name": "mattpocock-skills",
      "source": { "source": "github", "repo": "mattpocock/skills",
                  "sha": "49dd158d1076134a641b33efb035946536778336" }
    },
    {
      "name": "ui-ux-pro-max",
      "source": { "source": "git-subdir", "url": "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git",
                  "path": "<path to the skill folder>",
                  "sha": "56ea9cf174ed86786187daa9de0e6247cb0747e4" },
      "skills": ["./"]
    }
  ]
}
```

`.mcp.json`:

```json
{
  "mcpServers": {
    "figma": { "type": "http", "url": "https://mcp.figma.com/mcp" },
    "playwright": { "type": "stdio", "command": "npx", "args": ["@playwright/mcp@<pinned version>"] }
  }
}
```

## 11.7 Updating a pin

1. Open a `chore/` branch that changes one SHA in `marketplace.json`.
2. Review the diff between the old and new commits: new hooks, new `` !`cmd` `` lines, new network calls, new reads of `.env` or `~/` [R3-B4].
3. If our plugin's evals cover the changed skill, they run on the PR [R5-Q4c].
4. Merge after review. Never update pins automatically.
