# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository has just been created and has no source code, build system, or tests yet. When the stack is chosen, add the build, lint, and test commands here (including how to run a single test), along with a short overview of the architecture. Extend `.gitignore` with the ignore rules for that stack.

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
