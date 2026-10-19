# Vercel Guideline Sources

Status: fact check, 2026-10-19 (curl, GitHub API, WebFetch). Input to decisions R3-D1..D7 in [`../grilling-log.md`](../grilling-log.md). "(inferred)" marks a point that was not verified directly.

## Upstreams

| Skill (vercel-labs/agent-skills) | Fetches at runtime | Canonical repo | Licence | Human page |
|---|---|---|---|---|
| `web-design-guidelines` | `raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` | vercel-labs/web-interface-guidelines | **MIT**, © 2025 Vercel Labs | <https://vercel.com/design/guidelines>, probably rendered from README.md (inferred) |
| `writing-guidelines` | `raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md` | vercel-labs/writing-guidelines | **MIT**, © 2026 Vercel Labs | None found. `/design/writing` redirects to `/geist` |

- `vercel-labs/agent-skills` itself has **no LICENSE file**; its README says only "MIT". The upstream guideline repos have proper MIT LICENSE files.
- A local, edited copy is allowed as long as it **keeps the copyright and permission notice**.

## Version signals

- **Neither file has a version number or date.** `metadata.version: "1.0.0"` in SKILL.md versions the skill, not the rules.
- The **human page has no date metadata**: no JSON-LD, `dateModified` or `og:updated_time`. It carries only a Vercel deployment id and an asset prefix. Both change with every vercel.com deploy, so they make poor content signals (inferred).
- HTTP: an ETag on both raw files and on the page, no `Last-Modified`.
- **Best anchor:** the latest commit touching `command.md`, from `api.github.com/repos/<o>/<r>/commits?path=command.md&per_page=1`. Fetch the file pinned at that commit: `raw.githubusercontent.com/<o>/<r>/<sha>/command.md`.

| Upstream | Latest commit SHA | Date | Note |
|---|---|---|---|
| web-interface-guidelines | `4ecfb9fb8d1d3b7009674869b3aaee2f904042e1` | 2026-10-05 | Commit message: "Add desktop overscroll guideline" |
| writing-guidelines | `11483f8b60f3a90aa396b07a3cfbc32d42741162` | 2026-05-30 | README is newer (`83e2316…`, 2026-06-01) |

## Content breakdown

| | Web interface guidelines | Writing guidelines |
|---|---|---|
| **Size** | 104 items: 90 rules in 16 sections, plus 14 anti-patterns | 146 items: 110 rules in 21 sections, plus 36 anti-patterns |
| **Vercel-specific** | "Content & Copy" (7 items). These are Vercel brand choices: Title Case, "&", numerals, second person. | About 30–35 items: vercel.com links, model strings, internal `meta.*` fields, `<Steps/>`, ACME demo, the internal PR review process, "we" meaning Vercel |
| **Library-specific, not Vercel-specific** | About 8 items: `<Link>`, `focus-visible:ring-*`, nuqs, virtua, hydration safety, `priority` | — |
| **Process, not checkable in prose** | — | "AI workflow" (10 items) |
| **Generic** | About 95 items | About 110 items |

**The two sets contradict each other:**
- Heading case: Title Case (web) vs sentence case (writing).
- Placeholders: ALL_CAPS placeholders appear in the web README but are banned by the writing rules.
- Em dashes: used in the web text but banned by the writing rules.

## Directives aimed at the agent (none malicious)

- Both SKILL.md files hand control to the remote file: "The fetched content contains all the rules and output format instructions."
- Both `command.md` files define their own output format: "Group by file… `file:line`… No preamble", "sacrifice grammar for brevity".
- The writing "AI workflow" lines can read as orders to the model (e.g. "Use only enterprise models…").
- → In our copy, these are **stripped and replaced** by our own output format.
