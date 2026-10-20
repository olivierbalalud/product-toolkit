# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This repo holds **research and documentation only**. It is the documented framework for designing and developing product features: process guide, templates, and a list of recommended Claude Code plugins. It does not contain product code. The product lives in a **separate monorepo**. Do not create or download plugins, skills or agents here. List and describe them in the docs instead.

- `docs/brief.md`: objectives, concerns and context as originally stated.
- `docs/grilling-log.md`: the decisions taken in each Q&A round. It is authoritative where it refines the brief. A change to the framework starts as a new round here, then the guide is updated.
- `docs/guide/`: the process guide, chapters `00-overview` to `13-adoption`. Rules cite decision IDs in brackets, e.g. `[R4-Q8′]`.
- `docs/templates/`: templates for every artifact, copied into the monorepo.
- `docs/skills/`: specs of the skills the monorepo will build (`docs/templates/skill-spec.md` format).
- `docs/foundations/`: onboarding concepts per role, and the GDPR and AI Act one-pagers.
- `docs/research/`: tooling research with sources.
- `docs/context/monorepo-fit.md`: structural facts about the product monorepo. Everything else stays generic: no product concepts or internal names.

Write the docs in English. Use the neutral example domain (meeting room booking) in examples.

**The product monorepo is strictly read-only.** Never write to it, and never run git commands that change its state (commit, checkout, pull, fetch, stash, etc.). Inspect only a read-only copy of it.

## Git commits: Conventional Commits

Every commit message must follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/):

```
<type>(<optional scope>): <description>

[optional body]

[optional footer(s)]
```

- **Types:** `feat` (new feature), `fix` (bug fix), `docs`, `style` (formatting only, no change in behavior), `refactor` (neither a fix nor a feature), `perf`, `test`, `build` (build system or dependencies), `ci`, `chore` (maintenance that touches neither src nor tests), `revert`.
- **Scope** is optional: a short noun naming the affected area, e.g. `feat(auth): ...`.
- **Description:** imperative mood, lowercase first letter, no trailing period, about 72 characters at most. Write "add export command", not "Added export command."
- **Body** (optional): explain *what* changed and *why*, not how. Put a blank line after the subject and wrap lines at about 72 characters.
- **Breaking changes:** put `!` after the type or scope (`feat(api)!: ...`), add a `BREAKING CHANGE: <explanation>` footer, or both.
- **Footers** follow the git trailer format, e.g. `Refs: #123`, `Co-Authored-By: ...`.
- Each commit covers one logical change. If a change needs two types (e.g. a fix and an unrelated refactor), split it into two commits.

Examples:

```
feat(cli): add --dry-run flag to sync command
fix: handle empty config file without crashing
docs: document release process in README
refactor(parser)!: return Result instead of throwing

BREAKING CHANGE: parse() no longer throws; callers must check the result.
```
