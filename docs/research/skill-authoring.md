# Skill Authoring: Practices, Portability, Patterns

Status: fact check, 2026-10-19 (curl of the `.md` doc pages, GitHub API, WebFetch, read-only look at installed skills). Input to the revised R5-Q4 in [`../grilling-log.md`](../grilling-log.md). "(inferred)" marks a point that was not verified directly. Claude Code versions quoted are from the docs, not tested.

## Sources

| Id | Source |
|---|---|
| S1 | Claude Code, *Extend Claude with skills*: <https://code.claude.com/docs/en/skills> |
| S2 | Claude Code, *Subagents*: <https://code.claude.com/docs/en/sub-agents> |
| S3 | Claude Code, *Hooks* ("Hooks in skills and agents"): <https://code.claude.com/docs/en/hooks> |
| S4 | Claude Code, *Test plugins with evals* (`claude plugin eval`): <https://code.claude.com/docs/en/plugin-evals> |
| S5 | Claude Code, *Headless* (`-p`, `--bare`): <https://code.claude.com/docs/en/headless> |
| S6 | Claude Code, plugins reference and marketplace hosting: <https://code.claude.com/docs/en/plugins-reference>, <https://code.claude.com/docs/en/plugins/host-marketplace> |
| S7 | Claude Code, *Memory* (CLAUDE.md, AGENTS.md): <https://code.claude.com/docs/en/memory> |
| S8 | Anthropic, *Skill authoring best practices*: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices> |
| S9 | Anthropic, *Agent Skills overview* (levels, security): <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview> |
| S10 | Anthropic Engineering, *Equipping agents for the real world with Agent Skills* (2025-10-16; open standard 2025-12-18): <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> |
| S11 | Agent Skills specification: <https://agentskills.io/specification> |
| S12 | agentskills.io, *Best practices for skill creators*: <https://agentskills.io/skill-creation/best-practices> |
| S13 | agentskills.io, *Using scripts in skills*: <https://agentskills.io/skill-creation/using-scripts> |
| S14 | agentskills.io, *Evaluating skill output quality*: <https://agentskills.io/skill-creation/evaluating-skills> |
| S15 | agentskills.io, *Optimizing skill descriptions*: <https://agentskills.io/skill-creation/optimizing-descriptions> |
| S16 | anthropics/skills, `skills/skill-creator` (main at `dbd4588`, 2026-10-09): <https://github.com/anthropics/skills/tree/main/skills/skill-creator> |
| S17 | mattpocock-skills 1.3.1, local read-only copy: `~/.claude/plugins/cache/claude-plugins-official/mattpocock-skills/1.3.1/` (upstream <https://github.com/mattpocock/skills>) |
| S18 | obra/superpowers, `skills/writing-skills/SKILL.md`: <https://github.com/obra/superpowers/tree/main/skills/writing-skills> |
| S19 | skill-scout `framework/harness-matrix.md` (as of 2026-10-18), read-only |
| S20 | Harness docs, listed per row in §3 |

## 1. Claude Code skill anatomy and limits

**Layout** (S1, S11): `<name>/SKILL.md` (YAML frontmatter + Markdown body), plus optional `scripts/` (executed, code never enters context), `references/` (read on demand), `assets/` (templates, data). In a plugin: `<plugin>/skills/<name>/SKILL.md`, invoked as `/<plugin>:<name>`.

**Progressive disclosure** (S9, S10, S11): level 1, `name` + `description`, about 100 tokens per skill, always in context. Level 2, the body, loaded when the skill triggers: under 5,000 tokens and under 500 lines recommended. Level 3, files and scripts, loaded or run only when needed; only a script's output costs tokens.

| Field | In the open spec? | Claude Code behaviour and limits (S1 unless noted) |
|---|---|---|
| `name` | **Required** | Optional in Claude Code (defaults to the directory name). Spec: 1–64 chars, `a-z0-9-`, no leading, trailing or double hyphen, **must match the directory** (S11). Anthropic API: no XML tags, no reserved words `anthropic`, `claude` (S8). |
| `description` | **Required** | Spec: 1–1,024 chars (S11). Claude Code truncates `description` + `when_to_use` at **1,536 chars** in the listing. The whole listing has a budget of 1% of the context window; on overflow, descriptions of the least-used skills are dropped first. |
| `license`, `compatibility` (≤ 500 chars), `metadata` (string→string map) | Yes | Accepted, not acted on. |
| `allowed-tools` | Yes, **experimental** | Pre-approves the tools for **the invoking turn only**. It does not restrict other tools. It applies even in a `-p` run in an untrusted folder. |
| `when_to_use`, `argument-hint`, `arguments` | No | Trigger text appended to the description; autocomplete hint; named positional args (`$name`). |
| `disable-model-invocation` | No | Only the user can invoke the skill, and its description leaves the context. Such a skill **can't be preloaded into a subagent** (S2). |
| `user-invocable: false` | No | Only Claude can invoke it; hidden from the `/` menu. |
| `disallowed-tools` | No | Removes tools while the skill is active, e.g. `AskUserQuestion` for a background or CI skill. |
| `model`, `effort` | No | Override for the current turn only. |
| `context: fork`, `agent`, `background` | No | Runs the body as the prompt of a fresh subagent (`agent` = its type), **without the conversation history**. Runs in the background by default; under `-p` it waits for the result. |
| `hooks` | No | Registered when the skill is invoked and kept **for the rest of the session** (`once: true` runs it once) (S3). |
| `paths` | No | Globs: auto-load only when working on matching files. |
| `shell` | No | `bash` (default) or `powershell` for injected commands. |

**Body mechanics** (S1):
- **Substitutions:** `$ARGUMENTS`, `$0`/`$ARGUMENTS[N]`, `$name`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`. Plugin skills also get `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}`, which survives updates.
- **Dynamic context:** `` !`cmd` `` runs *before* Claude sees the body. A non-zero exit aborts the whole invocation, so append `|| true` to checkers that exit 1 when they find problems. It never prompts: a command that isn't allowed aborts, unless `allowed-tools` covers it.
- **Lifecycle:** the rendered body enters the conversation once and **is not re-read** on later turns. After compaction, only the **first 5,000 tokens** of each invoked skill are re-attached, within a 25,000-token total. Put the critical rules at the top.
- **Headless:** with `claude -p "/skill args"`, only the first skill on the line expands. `--bare` skips skill discovery, except for skills in `--add-dir` directories (S5).

**Subagents** (S2):
- **Preloading:** a subagent's `skills:` field preloads the **full content** of up to 32 skills. The subagent can still invoke other skills through the Skill tool unless `Skill` is removed from its tools.
- **Nesting:** subagents can nest **3 layers** deep by default (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`). Omit `Agent` from a reviewer's `tools` to keep it a leaf.
- **Plugin subagents ignore `hooks`, `mcpServers` and `permissionMode`** (security). Our plugin's reviewer agents therefore can't carry their own MCP servers or hooks.

**Validation tooling:** `claude plugin validate <dir>` checks frontmatter and manifest syntax (v2.1.233+) (S1). `skills-ref validate ./skill` checks a skill against the spec (S11). `/skill-doctor` reports each skill's context cost and usage (S1).

## 2. Authoring best practices

1. **Start from an observed gap, not an imagined one.** Run representative tasks *without* the skill, write down the failures, build about 3 eval scenarios, measure a baseline, then write the minimum that passes (S8 "Build evaluations first", S10). Ground the skill in project material (runbooks, review comments, past fixes), not generic advice (S12).
2. **Conciseness.** Claude is already smart: add only what it would get wrong without the skill. Test each line with "would the agent get this wrong without this?" (S8, S12). The body is a recurring cost on every turn after it loads (S1).
3. **Description = what + when, third person, key terms first** (S8). The description alone decides triggering (S15). Put the main use case first, because of the listing truncation (S1).
   - Make it a little "pushy", because Claude tends to *under*-trigger (S16, S15).
   - Don't summarise the workflow in it: agents were observed following the summary instead of the body (S18, community finding).
   - Style tension: S8 wants third person ("Processes X…"), S15 wants imperative ("Use this skill when…"). `"<Does X>. Use when <Y>."` satisfies both.
   - Keep it **≤ 1,024 chars** to stay valid outside Claude Code.
4. **Naming.** Lowercase and hyphens, gerund preferred (`writing-use-cases`), with noun or verb phrases acceptable. Avoid vague names (`helper`, `utils`) and the reserved words, and keep one pattern across the collection (S8).
5. **Size.** Keep the body under 500 lines and 5k tokens. Split into referenced files when it grows. Keep must-hold rules near the top so they survive compaction (S1, S8, S11).
6. **References one level deep from SKILL.md.** Claude may only `head` files that are reached through other files. Give a reference over 100 lines a table of contents (S8). Say *when* to read each file, e.g. "Read `references/errors.md` if the API returns non-200" (S12).
7. **Degrees of freedom: match specificity to fragility.** Use prose heuristics where many approaches are valid, pseudo-code or parameters where a preferred pattern exists, and an exact script where steps are fragile (S8). Give **defaults, not menus**, and **procedures over one-off answers** (S12).
8. **Scripts for deterministic work.** Pre-written scripts are more reliable than generated code, save tokens and behave the same on every run (S8).
   - Scripts *solve* errors instead of deferring them to Claude, and no constant goes unexplained (S8).
   - For agent use, a script (S13):
     - never prompts interactively
     - has a `--help`
     - writes structured output (JSON) to stdout and diagnostics to stderr
     - uses distinct, documented exit codes
     - is idempotent
     - offers `--dry-run` and safe defaults
     - declares its dependencies inline (PEP 723, `uv run`)
   - State whether Claude should **run** a script or **read** it as reference (S8).
9. **Feedback loops.** Validator → fix → repeat. Its error messages should be verbose and actionable ("Field X not found. Available: …") (S8).
10. **Plan-validate-execute** for batch, destructive or high-stakes changes: write a plan file, validate it with a script, then apply (S8).
11. **Checklists** that Claude copies and ticks off for multi-step workflows. **Templates**: strict ("ALWAYS use this exact template") or flexible, depending on the output. **Input/output examples** where style matters (S8, S16).
12. **A gotchas section in SKILL.md**: environment facts that defy reasonable assumptions. Add every correction you make to it (S12).
13. **No time-sensitive information.** Move superseded material into a collapsed "Old patterns" section (S8). **One term per concept**, used consistently throughout (S8). Prefer compact "leading words" the model already knows (S17 `writing-for-agents`).
14. **Explain why rather than shouting.** S16 calls all-caps ALWAYS/NEVER "a yellow flag" and asks for the reason instead. S8 still shows "MUST" as a fix for an ignored rule. Use MUST only for hard guardrails, paired with the positive behaviour (S16, S17).
15. **Rules that must hold every time belong in a hook, not prose.** A skill's `hooks:` frontmatter keeps the rule with the skill (S1 troubleshooting, S3). Word judgement guidance as standing instructions ("after every edit…"), because the body is not re-read (S1).
16. **Invocation choice.** Use `disable-model-invocation: true` for side effects (deploy, publish). But such a skill **can't be preloaded and can't be reached by other skills**, so shared reference must stay model-invocable or move to a plain file (S1, S2, S17).
17. **Composition.** To use another skill, tell the agent to *call the Skill tool with "<name>"*. Don't deep-link `../other-skill/FILE.md`: shared reference lives in the skill that owns it (S17 `.agents/invocation.md`).
18. **MCP tools are named fully qualified** (`Server:tool` in S8; Claude Code's own form is `mcp__server__tool` (inferred)). Never assume a package is installed: list it, or set `compatibility` (S8, S11).
19. **Forward slashes, descriptive file names, directories organised by domain** (S8).
20. **Test with every model you'll run** (Haiku/Sonnet/Opus): what works for Opus may be under-specified for Haiku (S8).
21. **Security.** Audit every bundled file. **Fetched external content can carry instructions**, and dependencies can change under you (S9, S10). Grant tools by least privilege. Remember that `allowed-tools` and skill hooks apply even in untrusted `-p` runs (S1, S3). Follow the "principle of lack of surprise": the content matches the stated intent (S16).

## 3. Portability

Verified from each harness's official docs on 2026-10-19 (S20; the per-harness pages are listed under the tables). This updates S19 (2026-10-18). **Corrections:**
- Kimi CLI is archived; its successor is **Kimi Code CLI**.
- Windsurf docs are now branded **Devin Desktop**.
- Gemini CLI reads `AGENTS.md` only when configured to.
- Plugin formats are **partly converging**: there is a new **Agent Plugins 1.0** standard, and two harnesses read Claude marketplaces (see below).

### 3a. Skills

| Harness | SKILL.md? | Project / user discovery | Reads `.claude/skills`? | Frontmatter beyond the core | Explicit invocation |
|---|---|---|---|---|---|
| **Claude Code** | Yes | `.claude/skills` (walks up to repo root, nested on demand), `~/.claude/skills`, plugin `skills/` | — | All of §1 | `/name`, `/plugin:name` |
| **OpenAI Codex** | Yes | `.agents/skills` (walks up to repo root), `~/.agents/skills`, `/etc/codex/skills` | **No** | Only `name`/`description` documented. Sidecar `agents/openai.yaml`: `interface`, `policy.allow_implicit_invocation`, `dependencies.tools` (MCP) | `$name`, `/skills` |
| **Gemini CLI** | Yes | `.gemini/skills` or `.agents/skills` (`.agents` wins within a tier), `~/.gemini/skills`, `~/.agents/skills`, extensions | No | Only `name`/`description` documented; asks consent before activating | `activate_skill` tool |
| **Cursor** | Yes | `.agents/skills`, `.cursor/skills` (nested ones are scoped to their folder), `~/` variants | **Yes** (also `.codex/skills`) | `paths` (legacy `globs`), `disable-model-invocation`, `icon`, `color`, `metadata` | `/name` |
| **GitHub Copilot** (CLI, cloud agent, VS Code) | Yes | `.github/skills`, `.agents/skills`, `~/.copilot/skills`, `~/.agents/skills` | **Yes** (VS Code also `~/.claude/skills`) | `license`, `allowed-tools`; VS Code adds `argument-hint`, `user-invocable`, `disable-model-invocation` | `/name` (VS Code) |
| **Kimi Code CLI** (Moonshot) | Yes | `.kimi-code/skills`, `.agents/skills`, `~/.kimi-code/skills`, `~/.agents/skills` | No; `/import-from-cc-codex` copies them in | Own camelCase keys: `whenToUse`, `disableModelInvocation`, `arguments`, `type` | `/skill:name` |
| **OpenCode** | Yes | `.opencode/skills`, `.agents/skills`, `~/.config/opencode/skills`, `~/.agents/skills` | **Yes** (also `~/.claude/skills`) | Spec fields only; extras go under `metadata` (`opencode/slash`, `opencode/autoinvoke`); per-agent `permission.skill` | Slash, if enabled |
| **Amp** | Yes | `.agents/skills`, `~/.config/agents/skills`, `~/.agents/skills`, `~/.config/amp/skills` | **Yes** (also `~/.claude/plugins/cache`) | `mcpServers` frontmatter or a sibling `mcp.json` | — |
| **Windsurf / Devin Desktop** | Yes | `.devin/skills` (legacy `.windsurf/skills`), `.agents/skills`, `~/.config/devin/skills` | Only when Claude-config reading is on | `name`/`description` | `@name` |

agentskills.io/clients lists 46 clients, including all of the above except Kimi, Windsurf/Devin and Antigravity. Gemini CLI moved to **Antigravity CLI** for consumer tiers on 2026-06-18; enterprise and paid API keys keep Gemini CLI. Antigravity is said to keep skills, hooks, subagents and extensions (Google blog), but that is not verified in its own docs.

### 3b. Everything else: subagents, hooks, MCP, plugins, instructions

| Harness | Subagents (can they preload skills?) | Hooks | MCP config | Plugins / marketplace | Instruction file | Headless |
|---|---|---|---|---|---|---|
| **Claude Code** | `.claude/agents/*.md`; **`skills:` preload** | settings, plugin `hooks/hooks.json`, skill/agent frontmatter | `.mcp.json`, plugin | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | `CLAUDE.md`; reads `AGENTS.md` (v2.1.277+) only when there is no `CLAUDE.md`, otherwise `@AGENTS.md` import (S7) | `claude -p` |
| **Codex** | `.codex/agents/*.toml`; skills inherited, **can only be disabled** | `.codex/hooks.json` or `config.toml`; Claude-like event names (`PreToolUse`, `PostToolUse`, `Stop`, `SubagentStart`…) | `.codex/config.toml` `[mcp_servers]` | Agent Plugins `plugin.json` (+ `.codex-plugin/`); marketplace `.agents/plugins/marketplace.json`, **also reads `.claude-plugin/marketplace.json`** ("legacy-compatible") and sets `CLAUDE_PLUGIN_ROOT` | `AGENTS.md`; `CLAUDE.md` only via `project_doc_fallback_filenames` | `codex exec` |
| **Gemini CLI** | `.gemini/agents/*.md`; no skills field | `settings.json`; different names (`BeforeTool`, `AfterTool`…); accepts `CLAUDE_PROJECT_DIR` | `settings.json` `mcpServers` | Extensions `gemini-extension.json` | `GEMINI.md`; `AGENTS.md` via `context.fileName` | `gemini -p` |
| **Cursor** | `.cursor/agents`, **also `.claude/agents`**, `.codex/agents`; no skills field | `.cursor/hooks.json` (`preToolUse`…); "supports loading hooks from … Claude Code" | `.cursor/mcp.json` | Agent Plugins or `.cursor-plugin/`; no Claude plugin support documented | `AGENTS.md`, `.cursor/rules` | `agent -p` |
| **Copilot** | `.github/agents/*.agent.md`; no skills field | `.github/hooks/*.json`; **also reads `.claude/settings.json`** | `.mcp.json`, `.github/mcp.json` | Agent Plugins or Copilot `plugin.json`; **reads `.claude-plugin/marketplace.json`** | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | `copilot -p` |
| **Kimi Code** | `.kimi-code/agents/*.md`; loads Claude-style agent files and ignores unknown keys | `config.toml` `[[hooks]]`, Claude event names | `.kimi-code/mcp.json` | `kimi.plugin.json` | `AGENTS.md` | `kimi -p` |
| **OpenCode** | `.opencode/agents/*.md` (`mode: subagent`) | JS/TS plugins (`tool.execute.before`…) | `opencode.json` `mcp` | npm/JS plugins | `AGENTS.md`, falls back to `CLAUDE.md` | `opencode run` |
| **Amp** | Through plugins (`amp.createAgent`) | TS plugins in `.amp/plugins/` | `amp.mcpServers` | TS plugins | `AGENTS.md`, falls back to `CLAUDE.md` | `amp -x` |

Harness doc pages:
- Codex: <https://developers.openai.com/codex/skills>, `/codex/hooks`, plugins <https://developers.openai.com/plugins/build/plugins>
- Gemini CLI: <https://geminicli.com/docs/cli/skills/>; Antigravity move: <https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/>
- Cursor: <https://cursor.com/docs/context/skills>
- Copilot: <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
- Kimi Code: <https://moonshotai.github.io/kimi-code/en/customization/skills>, repo <https://github.com/MoonshotAI/kimi-code>
- OpenCode: <https://opencode.ai/docs/skills/>
- Amp: <https://ampcode.com/docs/customize/skills>
- Windsurf / Devin Desktop: <https://docs.windsurf.com/windsurf/cascade/skills>
- Agent Plugins: <https://agent-plugins.org/compatible-clients>. Its portable components are **skills and MCP only**. Clients: VS Code, Cursor, Copilot, ChatGPT/Codex, Kiro and others; **Claude Code is not listed**.

### 3c. Verdict

**SKILL.md is the portable unit; everything around it is not.**
- The core format (folder + SKILL.md + `name`/`description` + `scripts/`/`references/`/`assets/`) loads in every harness above.
- `.agents/skills` reaches every harness except Claude Code, which only reads `.claude/skills`.
- Subagents, hooks and plugin manifests differ per harness, and so does how MCP is wired to a skill. **Subagent skill preloading (`skills:`) is Claude Code-only.**
- Hook event names are converging on Claude's (Codex, Kimi, Copilot, Cursor) but are not identical.

**Portable core (write every skill to this):**
1. Frontmatter limited to `name` (= folder, spec regex), `description` (≤ 1,024 chars) and, optionally, `license`, `compatibility`, `metadata`.
2. Body in plain Markdown with relative paths. No `` !`cmd` ``, no `$ARGUMENTS`, no `${CLAUDE_*}`. Inputs are described in prose ("the user supplies a PRD path").
3. Deterministic logic lives in `scripts/` (self-contained, inline dependencies, JSON out, exit codes), so it also runs in CI with no agent at all.
4. Composition is written as "use the `<name>` skill" (any harness's skill tool), not as Claude-specific `/plugin:name` syntax.
5. Any spawning of reviewers is written as an *optional* step: "if you can run subagents, run these in parallel; otherwise run them in sequence and keep the reports separate" (inferred).

**Claude Code-only extras:**
- frontmatter: `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `disallowed-tools`, `model`, `effort`, `context`/`agent`/`background`, `hooks`, `paths`, `shell`
- `allowed-tools` semantics (the field is experimental in the spec, and its syntax differs)
- body syntax: `` !`cmd` ``, `$ARGUMENTS` and `$N`, `${CLAUDE_SKILL_DIR}` and the other `${CLAUDE_*}` variables
- subagent `skills:` preload
- plugin namespacing, `${CLAUDE_PLUGIN_DATA}`
- `claude plugin eval`

Some of these keys are honoured elsewhere under the same name: `disable-model-invocation` (Cursor, VS Code) and `paths` (Cursor).

**Recommended isolation (inferred, derived from the above):**
- **Layer 1, skill (portable):** `skills/<name>/` holds only the portable core. It is the single source of truth.
- **Layer 2, Claude wiring (plugin):** `agents/*.md` (review lanes with `skills:`), `hooks/hooks.json`, `.mcp.json`, `plugin.json`, `evals/`. Claude-only frontmatter keys may be added to SKILL.md *only* if they are harmless when ignored. Unknown-key handling is: ignored by Claude Code and Kimi agents; a **hard error** on claude.ai/API upload (S1); undocumented for Codex and Gemini. Otherwise keep the keys in a per-harness overlay that a build step merges in.
- **Layer 3, other-harness adapters, only when needed:** Codex `agents/openai.yaml` sidecar per skill (mattpocock-skills already ships one for every skill, S17). `.codex/agents/*.toml` or `.github/agents/*.agent.md` lane definitions that inline the "preloaded" skill text or tell the agent to load it. An Agent Plugins `plugin.json` (skills + MCP) for Codex, Cursor and Copilot.
- **Instructions:** keep `AGENTS.md` as the shared file and have `CLAUDE.md` import it with `@AGENTS.md` (S7). Gemini needs `context.fileName`.
- **CI:** run `skills-ref validate` (spec conformance) and `claude plugin validate` on every change, so a Claude-only key can't silently enter Layer 1.

## 4. Patterns catalogue

| Pattern | Use when | Structure | Real example |
|---|---|---|---|
| **Fan-out reviewers, aggregate without reranking** | Several independent review axes | Check preconditions *before* fan-out ("a bad ref or empty diff should fail here, not inside two parallel sub-agents"). Spawn N subagents in one turn, each prompt carrying everything it needs (reference pasted in, since subagents don't see the parent's context) and a word cap. Present the reports under per-axis headings, **no merge, no cross-axis winner**. | S17 `skills/engineering/code-review/SKILL.md` steps 4–5 |
| **Subagent with preloaded skills** | A lane reviewer needs its rules from upstream skills | `agents/<lane>.md` with `skills: [a, b]` and `tools:` without `Agent` (leaf). Preloaded skills must be model-invocable. | S2 "Preload skills into subagents" |
| **Forked task skill** | Self-contained research or analysis that must not see chat history | `context: fork` + `agent: Explore`; the body is the whole task | S1 "Run skills in a subagent" |
| **Task-graph orchestrator** | Many tickets with dependencies | Work a *frontier* of unblocked tasks. Implementer subagents in worktrees, a merger subagent, a final review skill. Communicate through **context pointers** (paths), not copied text. | S17 `implement-spec/SKILL.md` |
| **Script checks, LLM judges** | Gate-check, fit-check | A script does the mechanical part (frontmatter schema, required files, ID cross-references, coverage counts) and emits JSON. The LLM judges only what the script can't (semantic gaps). The same script runs in CI without an agent. | S8 "Prefer scripts for deterministic operations"; anthropics/skills `skills/pdf/scripts/check_fillable_fields.py` |
| **Validator feedback loop** | Output has a checkable format (Gherkin, ICU messages, OpenAPI) | Generate → run validator → fix from its errors → repeat until clean | S8 "Implement feedback loops"; anthropics/skills `skills/docx/scripts/office/validate.py` |
| **Plan-validate-execute** | Batch or destructive edits (catalog updates, many files) | Analyse → write `changes.json` → validate it with a script → apply → verify | S8; anthropics/skills `skills/pdf/forms.md` + `check_bounding_boxes.py` |
| **Checklist-driven workflow** | Multi-step procedures where skipping is the risk | A copyable checklist in the body, ticked off as Claude goes; each step ends on a checkable **completion criterion** | S8 "Use workflows for complex tasks"; S17 `writing-for-agents` |
| **Template filling** | Fixed artifact shape (use case, story, report) | `assets/<template>.md` or an inline template, strict or flexible | S8 "Template pattern"; S16 "Defining output formats" |
| **Domain router references** | One skill, several variants (locales, frameworks) | SKILL.md picks the variant, then reads only `references/<variant>.md` | S16 `cloud-deploy/references/{aws,gcp,azure}.md`; S8 "Domain-specific organization" |
| **Config- or manifest-driven** | Behaviour depends on repo layout (tracker, glossary path, catalog dirs) | Read a config file written by a setup skill. If it is missing, tell the user to run the setup skill; don't guess. | S17 "The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`" |
| **Rounds interview** | Eliciting use cases or decisions from a human | Work the *frontier* of a design tree: numbered questions, each with a recommended answer; look up facts with subagents, never ask the user for them | S17 `productivity/grilling/SKILL.md` |
| **External content as data** | Pinned upstream guidelines (Vercel), fetched docs | Pin by commit SHA. A pull-only refresh script writes a local copy with provenance. Upstream "directives aimed at the agent" are stripped, and the skill's own output format overrides the upstream one. | S9 security; our [`vercel-guidelines.md`](vercel-guidelines.md) |
| **Idempotent file outputs** | Skills that write spec artifacts | Fixed paths derived from IDs, create-if-missing, stable ordering, regenerate only marked sections, `--dry-run`. A re-run on unchanged input gives a byte-identical file (inferred good practice; S13 for scripts). | S13 "Idempotency" |
| **Dynamic context injection** | Live state is always needed (diff, PR) | `` !`git diff HEAD` `` in the body. **Claude Code only**; the portable fallback is "run `scripts/x.sh` first". | S1 |
| **Hook-enforced invariant** | A rule must hold on every tool call | `hooks: PreToolUse` in the skill frontmatter, or a plugin `hooks/hooks.json` | S1, S3 |
| **Dual-mode: interactive and headless** | Gate-check and review lanes also run in CI | All inputs come from arguments or files, never a question. `disallowed-tools: AskUserQuestion` on the CI variant. Results go to a file in a fixed format, plus a script exit code for the gate. In `-p`, forked skills block until done. | S1, S5 |
| **Gotchas list** | Every skill | A `## Gotchas` section in SKILL.md that grows with each correction | S12 |

## 5. Testing and evaluation

| Layer | What | Tool | Source |
|---|---|---|---|
| Static | Frontmatter schema, name = directory, description ≤ 1,024, body ≤ 500 lines, links one level deep | `skills-ref validate`; `claude plugin validate`; our own lint in CI (inferred) | S1, S11 |
| Scripts | Unit tests like any code | Repo test runner | (inferred) |
| Triggering | About 20 labelled queries (8–10 should trigger, 8–10 near-miss shouldn't), split ~60/40 into train and validation, several runs each. Pick the best description by validation pass rate. | `tool_used: Skill` grader in `claude plugin eval`; skill-creator's description optimiser | S15, S4, S16 |
| Output quality | Realistic prompts plus fixtures, run **with and without** the skill. Write assertions *after* the first outputs; a PASS needs quoted evidence. Drop assertions that pass in both arms. | `claude plugin eval` (CI); skill-creator `evals/evals.json` (authoring loop) | S4, S14, S16 |
| Comparison | Blind A/B between two versions; human feedback file per case | skill-creator `agents/comparator.md`, review viewer | S16, S14 |
| Discipline skills | "Pressure scenarios": watch the agent break the rule without the skill, then close each rationalisation | Manual with subagents | S18 |
| Models | Every model you'll run | `--model` per run | S8 |

**`claude plugin eval`** (S4, v2.1.269+):
- **Layout:** `evals/<case>/prompt.md` (frontmatter: `runs`, `model`, `max_turns`, `allowed_tools`, `env` with `EVAL_*` keys) plus `graders/*.md`.
- **Grader types:** `regex`, `tool_used`, `tool_order`, `file_exists`, `llm` (best of 3 judge votes) and `baseline`. A grader can target the last message, the trace, the files created, or one file's contents.
- **Fixtures:** `case.yaml` with `context.scaffold_script` (needs `--scaffold`). MCP tools are mocked under `evals/mocks/`.
- **Runs:** each case runs 3× with the plugin and 3× without it. The report shows `WITH`, `W/OUT` and `Δ`.
- **CI:** `--json --threshold 0.8 --trust-plugin --model <pinned> --max-cost-usd <cap>`. The exit code follows the threshold, and `Δ` never changes it. Every run is a billed model call.
- **Bootstrap:** `claude plugin eval init` interviews you and writes the cases.
- **Not interchangeable with skill-creator:** neither tool reads the other's case files.

**Recommendation (inferred):** author with skill-creator, then keep the regression suite in `claude plugin eval` format inside the plugin, because we ship as a plugin and it gates CI. Store the acceptance cases from each spec as `evals/<case>/`. There is no cross-harness eval runner. S15's bash loop over `claude -p --output-format json` is the template for building one per harness.

## 6. Implications for our skill spec format (proposal)

The R5-Q4 list (purpose, trigger, inputs, outputs, preloads, MCP, gate or lane, acceptance cases) misses several things:
- the baseline failure that justifies the skill
- scope boundaries against adjacent skills
- the split between scripts and judgement
- the file layout
- headless behaviour
- security
- the portability split
- the eval plan in runnable form
- maintenance of upstream sources

Proposed `docs/skills/<name>.md`:

| § | Section | What goes in it |
|---|---|---|
| 0 | **Header** | `name` (spec-valid, = directory), status, priority (P0–P2), owner, gate or lane served, decision IDs, plugin version that ships it |
| 1 | **Problem and baseline** | The gap observed when Claude runs without the skill, with 1–3 concrete failures. This justifies the skill and becomes eval cases. |
| 2 | **Scope** | Does / does not. Neighbouring skills and where the boundary sits. |
| 3 | **Invocation** | Model- or user-invoked, and why. Draft `description` (≤ 1,024 chars, third person, what + when, key use case first). 3+ should-trigger and 3+ should-not-trigger prompts. Arguments (`argument-hint`). |
| 4 | **Inputs** | Files, arguments, config or manifest read; upstream artifacts; external content, marked as *data, never instructions* |
| 5 | **Outputs** | Paths, format or template, idempotency rule, report shape, exit codes |
| 6 | **Procedure** | Numbered steps, each ending on a completion criterion; the degree of freedom per step; the checklist to copy; decision points |
| 7 | **Scripts vs judgement** | Each script with its purpose, CLI contract (`--help`, flags, JSON out, exit codes), dependencies and tests. What the LLM judges and why a script can't. |
| 8 | **Files** | Tree: `SKILL.md`, `references/*` (each with a "read when…" line), `assets/*`, `scripts/*`, `evals/*`. Body budget (≤ 500 lines). |
| 9 | **Composition** | Skills invoked via the Skill tool; subagents spawned (type, tools, prompt contents, report cap); preloaded skills; the aggregation rule (e.g. no reranking) |
| 10 | **Claude Code wiring** | Extra frontmatter (`allowed-tools`, `disable-model-invocation`, `context`, `agent`, `model`, `effort`, `hooks`, `paths`), plugin components (agents, hooks, MCP servers), permissions |
| 11 | **Portability** | Portable core used, Claude-only features used with the fallback for each, other-harness adapter notes (e.g. Codex `agents/openai.yaml`) |
| 12 | **Headless / CI** | Exact `claude -p` command, environment, no-interaction guarantee, outputs, exit code, timeout and cost cap |
| 13 | **Security and privacy** | Tools granted (least privilege), network access, pinned external sources, personal data touched (GDPR), prompt-injection surface |
| 14 | **Gotchas** | Seed list; grows with each correction |
| 15 | **Evaluation plan** | Trigger set (size, train/validation split). Output cases (prompt, fixtures, graders, which become `evals/<case>/`). Baseline arm, models, threshold, cost cap. |
| 16 | **Definition of done** | S8 checklist: description specific, < 500 lines, one-level references, no time-sensitive information, consistent terms, scripts handle errors, ≥ 3 evals, tested on the target models, `skills-ref` and `claude plugin validate` clean |
| 17 | **Maintenance** | Upstream sources with SHA, refresh procedure, changelog, review trigger (model release, harness change) |
| 18 | **Open questions** | Anything still undecided |

Lighter variant (inferred): pure reference skills (glossary, guidelines copy) can skip §6, §7 and §9.

## Open questions / unverified points

- How a plugin subagent's `skills:` field names a *plugin* skill (bare `name` or `plugin:name`) is not stated in S2 or S6. Test it before the review lanes rely on it.
- Whether `--bare` loads plugins passed with `--plugin-dir` is not stated in S5. CI may need `--add-dir` or a non-bare run.
- Codex and Gemini CLI don't document what they do with unknown frontmatter keys. Test one skill with Claude-only keys in each target harness before choosing between "keys in SKILL.md" and "overlay build step".
- Whether Claude Code will adopt Agent Plugins 1.0 is unknown. Codex and Copilot reading `.claude-plugin/marketplace.json` is documented, but untested with our plugin (agents, hooks).
- Antigravity CLI's skill paths and formats were not checked in its own docs.
- `allowed-tools` syntax differs between harnesses (`Bash(git:*)` in S11, `Bash(git *)` in S1). Treat the field as Claude-only in practice (inferred).
- Relative script paths (`scripts/x.py`) in the body: the spec says they resolve from the skill root (S11). Claude Code's shell runs in the project directory, so `${CLAUDE_SKILL_DIR}` is safer there. The portable phrasing that works in both is unverified.
- Both eval tools spend real model usage. We have no budget figure yet.
