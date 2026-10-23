#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check a use case file against the mechanical rules of the use case gate.

Usage: check_grid.py USE_CASE.md [--inputs-dir DIR]

Prints a JSON report on stdout: {"file", "ok", "errors": [...], "warnings": [...]}.
Each finding is {"rule", "message"}. Diagnostics go to stderr.

Exit codes: 0 no errors (warnings allowed), 1 errors found, 2 usage or read error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

FIELDS = ["Primary actor", "Supporting actors", "Scope", "Level", "Trigger",
          "Preconditions", "Minimal guarantees", "Success guarantees"]
DURATIONS = {"wait", "long", "background"}
ACTOR_COLS = ["Invalid input", "Duplicate", "No permission", "Cancel / abandon"]
SYSTEM_COLS = ["Not found", "Conflict / concurrent edit", "Timeout / external down",
               "Partial failure", "Quota / limit", "Stale data", "Cancel / abandon"]
UI_WORDS = ["click", "button", "screen", "modal", "tap", "field"]
WAIT_WORDS = ["hours", "days", "tomorrow", "overnight", "waits for", "approves"]
INPUT_PREFIXES = ("PER", "JRN", "PP", "BLK", "OBJ", "HYP")

STEP_NUM = r"\d+(?:\.\d+)*"
EXT_KEY = rf"(?:{STEP_NUM}-{STEP_NUM}|\*|{STEP_NUM})"
EXT_ID_RE = re.compile(rf"UC-(\d{{3}})\.({EXT_KEY})([a-z])")
STEP_RE = re.compile(rf"^({STEP_NUM})\.\s+\((actor|system)(?:,\s*([a-z]+))?\)\s+(.*)$")
STEP_LIKE_RE = re.compile(rf"^({STEP_NUM})\.\s+(.*)$")
EXT_HEAD_RE = re.compile(rf"^- \*\*`?(UC-\d{{3}}\.{EXT_KEY}[a-z])`?\*\*\s*(.*)$")


class Report:
    def __init__(self, path: str):
        self.path, self.errors, self.warnings = path, [], []

    def error(self, rule: str, message: str) -> None:
        self.errors.append({"rule": rule, "message": message})

    def warn(self, rule: str, message: str) -> None:
        self.warnings.append({"rule": rule, "message": message})

    def as_dict(self) -> dict:
        return {"file": self.path, "ok": not self.errors,
                "errors": self.errors, "warnings": self.warnings}


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            meta[key.strip()] = value.split("#", 1)[0].strip()
    return meta, text[end + 4:]


def sections(body: str) -> dict[str, list[str]]:
    out, current = {}, "_top"
    out[current] = []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            current = m.group(1).strip()
            out[current] = []
        else:
            out[current].append(line)
    return out


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def table_rows(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        s = line.strip()
        if s.startswith("|") and s.endswith("|") and not re.match(r"^\|[\s\-|:]+\|$", s):
            rows.append([c.strip() for c in s[1:-1].split("|")])
    return rows


def find_table(lines: list[str], first_header: str) -> tuple[list[str], list[list[str]]] | None:
    """Return (header, data rows) of the table whose header row starts with first_header."""
    rows, block = [], []
    for line in lines + [""]:
        if line.strip().startswith("|"):
            block.append(line)
        elif block:
            rows.append(table_rows(block))
            block = []
    for tbl in rows:
        if tbl and tbl[0] and tbl[0][0] == first_header:
            return tbl[0], tbl[1:]
    return None


def step_key(num: str) -> tuple[int, ...]:
    return tuple(int(p) for p in num.split("."))


def key_covers(key: str, step: str, steps: list[str]) -> bool:
    if key == "*":
        return True
    if "-" in key:
        lo, hi = key.split("-")
        return step_key(lo) <= step_key(step) <= step_key(hi)
    return key == step


def check(path: Path, inputs_dir: Path | None) -> Report:
    rep = Report(str(path))
    text = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    body = strip_comments(body)
    secs = sections(body)

    uc_id = meta.get("id", "")
    m = re.fullmatch(r"UC-(\d{3})", uc_id)
    if not m:
        rep.error("frontmatter-id", f"frontmatter id {uc_id!r} is not UC-NNN")
    uc_num = m.group(1) if m else None

    # Field table
    field_tbl = find_table(secs.get("_top", []), "Field")
    fields = {}
    if not field_tbl:
        rep.error("field-table", "no field table (| Field | Value |)")
    else:
        for row in field_tbl[1]:
            if len(row) >= 2:
                fields[row[0].replace("*", "").strip()] = row[1].strip()
        for f in FIELDS:
            if f not in fields:
                rep.error("field-missing", f"field '{f}' is missing from the field table")
            elif not fields[f] or re.fullmatch(r"<[^>]*>", fields[f]):
                rep.error("field-empty", f"field '{f}' is empty")
        level = fields.get("Level", "")
        if level and not level.lower().startswith("user goal"):
            rep.error("level", f"Level is {level!r}, not 'User goal'")

    # Inputs
    inputs = re.findall(r"[A-Z]+-\d{3}", meta.get("inputs", ""))
    if inputs:
        headings = set()
        if inputs_dir and inputs_dir.is_dir():
            for f in inputs_dir.glob("*.md"):
                headings |= set(re.findall(r"^#+\s+([A-Z]+-\d{3})", f.read_text(encoding="utf-8"), re.M))
        for i in inputs:
            if not i.startswith(INPUT_PREFIXES):
                rep.error("inputs-prefix", f"inputs: {i} has no input prefix")
            elif i not in headings:
                rep.error("inputs-unknown", f"inputs: {i} matches no heading in the inputs folder")

    # Main scenario
    scen = secs.get("Main success scenario")
    steps: dict[str, dict] = {}
    order: list[str] = []
    if scen is None:
        rep.error("scenario-missing", "no 'Main success scenario' section")
        scen = []
    for line in scen:
        s = line.strip()
        sm = STEP_RE.match(s)
        if sm:
            num, kind, dur, txt = sm.groups()
            if dur is not None and kind == "actor":
                rep.error("duration-on-actor", f"step {num}: an actor step has no duration class")
            if dur is not None and dur not in DURATIONS:
                rep.error("duration-unknown", f"step {num}: duration class {dur!r} is not wait, long or background")
            steps[num] = {"kind": kind, "dur": dur or "instant", "text": txt}
            order.append(num)
            low = f" {txt.lower()} "
            for w in UI_WORDS:
                if re.search(rf"\b{w}s?\b", low):
                    rep.warn("ui-word", f"step {num}: UI word '{w}'")
            for w in WAIT_WORDS:
                if re.search(rf"\b{re.escape(w)}\b", low):
                    rep.warn("wait-word", f"step {num}: '{w}' suggests a wait point inside the scenario")
        elif STEP_LIKE_RE.match(s):
            rep.error("step-mark", f"step {STEP_LIKE_RE.match(s).group(1)}: not marked (actor) or (system)")
    if scen and not steps:
        rep.error("scenario-empty", "the main scenario has no marked steps")
    for i, num in enumerate(order):
        if steps[num]["dur"] == "background":
            nxt = order[i + 1] if i + 1 < len(order) else None
            if nxt is None:
                rep.error("background-last", f"step {num}: a background step is the last step")
            elif steps[nxt]["kind"] == "actor":
                rep.error("background-then-actor", f"step {num}: a background step is followed by an actor step")

    # Extensions
    ext_lines = secs.get("Extensions", [])
    extensions: dict[str, dict] = {}
    current = None
    for line in ext_lines:
        hm = EXT_HEAD_RE.match(line.strip()) if not line.startswith("  ") else None
        if hm:
            eid, rest = hm.groups()
            if eid in extensions:
                rep.error("ext-duplicate-id", f"{eid}: defined twice")
            current = {"head": rest, "body": [], "id": eid}
            extensions[eid] = current
        elif current is not None:
            current["body"].append(line)
    for eid, ext in extensions.items():
        em = EXT_ID_RE.fullmatch(eid)
        num, key = em.group(1), em.group(2)
        if uc_num and num != uc_num:
            rep.error("ext-id-uc", f"{eid}: does not belong to UC-{uc_num}")
        if key != "*":
            if "-" in key:
                lo, hi = key.split("-")
                if lo not in steps or hi not in steps:
                    rep.error("ext-id-step", f"{eid}: range {key} names a step that doesn't exist")
                elif step_key(lo) >= step_key(hi):
                    rep.error("ext-id-range", f"{eid}: range {key} is not first lower than last")
            elif key not in steps:
                rep.error("ext-id-step", f"{eid}: step {key} doesn't exist")
        head, body_text = ext["head"], "\n".join(ext["body"])
        marked = re.search(r"`(deferred|out-of-scope)`", head)
        if marked:
            reason = head[marked.end():].strip(" ,.:;")
            if not reason:
                rep.error("ext-reason", f"{eid}: `{marked.group(1)}` without a reason")
            ext["handled"] = False
        else:
            if not re.search(r"^\s+\d+\.\s+\S", body_text, re.M):
                rep.error("ext-handling", f"{eid}: no handling steps")
            if not re.search(r"\*Example:\*\s*\S", body_text):
                rep.error("ext-example", f"{eid}: handled extension without *Example:*")
            ext["handled"] = True

    # Grids
    grid_lines = secs.get("Failure-category check", [])
    if not grid_lines:
        rep.error("grid-missing", "no 'Failure-category check' section")
    seen_rows: dict[str, str] = {}
    for kind, cols in (("actor", ACTOR_COLS), ("system", SYSTEM_COLS)):
        found = None
        block_tables = []
        block = []
        for line in grid_lines + [""]:
            if line.strip().startswith("|"):
                block.append(line)
            elif block:
                block_tables.append(table_rows(block))
                block = []
        for t in block_tables:
            if t and t[0][:1] == ["Step"] and t[0][1:] == cols:
                found = t
        if found is None:
            rep.error("grid-table", f"no {kind}-step table with columns {', '.join(cols)}")
            continue
        for row in found[1:]:
            if not row or not row[0]:
                continue
            num = row[0]
            if num in seen_rows:
                rep.error("grid-row-duplicate", f"step {num}: appears twice in the grid")
            seen_rows[num] = kind
            if num not in steps:
                rep.error("grid-row-step", f"grid row {num}: no such step")
            elif steps[num]["kind"] != kind:
                rep.error("grid-row-kind", f"step {num}: is an {steps[num]['kind']} step but sits in the {kind}-step table")
            cells = row[1:]
            if len(cells) != len(cols):
                rep.error("grid-row-width", f"step {num}: {len(cells)} cells, expected {len(cols)}")
                continue
            for col, cell in zip(cols, cells):
                where = f"step {num}, {col}"
                low = cell.lower()
                if not cell:
                    rep.error("grid-empty", f"{where}: empty cell")
                    continue
                if low.startswith("yes"):
                    ids = ["".join(t) for t in re.findall(r"(UC-\d{3}\.)(" + EXT_KEY + r")([a-z])", cell)]
                    if not ids:
                        rep.error("grid-yes-unnamed", f"{where}: 'yes' names no extension")
                    for i in ids:
                        if i not in extensions:
                            rep.error("grid-yes-unknown", f"{where}: names {i}, which doesn't exist")
                elif low == "n/a":
                    pass
                elif low.startswith("out-of-scope"):
                    if not cell[len("out-of-scope"):].strip(" :,-"):
                        rep.error("grid-oos-reason", f"{where}: out-of-scope without a reason")
                else:
                    rep.error("grid-value", f"{where}: {cell!r} is not yes, n/a or out-of-scope")
                if kind == "system" and col == "Cancel / abandon" and num in steps:
                    dur = steps[num]["dur"]
                    if dur in ("long", "background") and (low == "n/a" or not cell):
                        rep.error("cancel-long", f"step {num}: a {dur} step needs a cancel answer, not n/a")
                    if dur in ("instant", "wait") and low != "n/a":
                        rep.error("cancel-short", f"step {num}: cancel on an {dur} step must be n/a")
    for num in order:
        if num not in seen_rows:
            rep.error("grid-row-missing", f"step {num}: no row in the grid")

    if not re.search(r"^\*\*Privacy request:\*\*\s*\S", "\n".join(grid_lines), re.M):
        rep.error("privacy-line", "no 'Privacy request:' line")

    return rep


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("use_case", type=Path, help="path to use-case.md")
    ap.add_argument("--inputs-dir", type=Path, default=None,
                    help="folder of input files (default: docs/product/inputs next to the repo root, if any)")
    args = ap.parse_args(argv)
    try:
        rep = check(args.use_case, args.inputs_dir)
    except OSError as e:
        print(f"check_grid: cannot read {args.use_case}: {e}", file=sys.stderr)
        return 2
    json.dump(rep.as_dict(), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0 if not rep.errors else 1


if __name__ == "__main__":
    sys.exit(main())
