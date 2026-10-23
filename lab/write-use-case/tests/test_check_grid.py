"""Tests for skill/scripts/check_grid.py: every dev gold passes, every v2 fails,
and each rule fires on a gold version broken in exactly that way."""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

LAB = Path(__file__).resolve().parents[1]
SCRIPT = LAB / "skill" / "scripts" / "check_grid.py"
DEV = LAB / "cases" / "dev"
GOLDS = sorted(DEV.glob("case-*/gold.md"))
V2S = sorted(DEV.glob("case-*/v2-bad.md"))
# A gold with a long step, a range and several extensions per step.
BASE = DEV / "case-21-import-contacts" / "gold.md"

spec = importlib.util.spec_from_file_location("check_grid", SCRIPT)
check_grid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_grid)


def rules_for(text: str, tmp_path: Path) -> set[str]:
    f = tmp_path / "use-case.md"
    f.write_text(text, encoding="utf-8")
    return {e["rule"] for e in check_grid.check(f, None).errors}


def mutate(old: str, new: str, count: int = -1) -> str:
    text = BASE.read_text(encoding="utf-8")
    assert old in text, f"fixture text not found: {old!r}"
    return text.replace(old, new, count)


@pytest.mark.parametrize("gold", GOLDS, ids=lambda p: p.parent.name)
def test_gold_passes(gold, tmp_path):
    assert rules_for(gold.read_text(encoding="utf-8"), tmp_path) == set()


@pytest.mark.parametrize("v2", V2S, ids=lambda p: p.parent.name)
def test_v2_fails(v2, tmp_path):
    assert rules_for(v2.read_text(encoding="utf-8"), tmp_path)


@pytest.mark.parametrize("old,new,rule", [
    ("| **Level** | User goal |", "| **Level** | Summary |", "level"),
    ("| **Supporting actors** | None |", "| **Supporting actors** |  |", "field-empty"),
    ("| **Supporting actors** | None |\n", "", "field-missing"),
    ("1. (actor) The Marketing Manager provides", "1. The Marketing Manager provides", "step-mark"),
    ("(system, long)", "(system, slow)", "duration-unknown"),
    ("1. (actor) The Marketing Manager provides", "1. (actor, wait) The Marketing Manager provides", "duration-on-actor"),
    ("| 6 | n/a |", "| 6 |  |", "grid-empty"),
    ("| 6 | n/a |", "| 6 | maybe |", "grid-value"),
    ("| 6 | n/a |", "| 6 | yes |", "grid-yes-unnamed"),
    ("| 6 | n/a |", "| 6 | yes: UC-021.6z |", "grid-yes-unknown"),
    ("| 6 | n/a |", "| 6 | out-of-scope |", "grid-oos-reason"),
    ("| 7 | n/a |", "| 9 | n/a |", "grid-row-step"),
    ("*Example:*", "*Instance:*", "ext-example"),
    ("**Privacy request:**", "**Privacy:**", "privacy-line"),
    ("- **UC-021.6a**", "- **UC-021.9a**", "ext-id-step"),
    ("UC-021.1-5a", "UC-021.5-1a", "ext-id-range"),
    ("id: UC-021", "id: UC-21", "frontmatter-id"),
])
def test_rule_fires(old, new, rule, tmp_path):
    assert rule in rules_for(mutate(old, new), tmp_path)


def test_long_step_cancel_cannot_be_na(tmp_path):
    text = BASE.read_text(encoding="utf-8")
    row = next(l for l in text.splitlines() if l.startswith("| 6 |"))
    cells = row.split("|")
    cells[-2] = " n/a "
    assert "cancel-long" in rules_for(text.replace(row, "|".join(cells)), tmp_path)


def test_wait_step_cancel_must_be_na(tmp_path):
    text = BASE.read_text(encoding="utf-8")
    row = next(l for l in text.splitlines() if l.startswith("| 2 |"))
    cells = row.split("|")
    cells[-2] = " yes: UC-021.6a "
    assert "cancel-short" in rules_for(text.replace(row, "|".join(cells)), tmp_path)


def test_background_step_last(tmp_path):
    text = mutate("7. (system) The system presents the import report",
                  "7. (system, background) The system presents the import report")
    assert "background-last" in rules_for(text, tmp_path)


def test_missing_grid_row(tmp_path):
    text = BASE.read_text(encoding="utf-8")
    row = next(l for l in text.splitlines() if l.startswith("| 7 |"))
    assert "grid-row-missing" in rules_for(text.replace(row + "\n", ""), tmp_path)


def test_deferred_needs_reason(tmp_path):
    text = BASE.read_text(encoding="utf-8")
    text = text.replace("## Technology and data variations",
                        "- **UC-021.7a** The report cannot be shown: `deferred`.\n\n## Technology and data variations")
    assert "ext-reason" in rules_for(text, tmp_path)


def test_unknown_input_id(tmp_path):
    text = mutate("inputs: []", "inputs: [PER-001]")
    assert "inputs-unknown" in rules_for(text, tmp_path)


def test_ui_word_warns_without_failing(tmp_path):
    f = tmp_path / "use-case.md"
    f.write_text(mutate("5. (actor) The Marketing Manager starts the import.",
                        "5. (actor) The Marketing Manager clicks the button to start the import."), encoding="utf-8")
    rep = check_grid.check(f, None)
    assert not rep.errors and {"ui-word"} <= {w["rule"] for w in rep.warnings}


def test_cli_contract(tmp_path):
    ok = subprocess.run([sys.executable, str(SCRIPT), str(BASE)], capture_output=True, text=True)
    assert ok.returncode == 0 and json.loads(ok.stdout)["ok"] is True
    bad = subprocess.run([sys.executable, str(SCRIPT), str(V2S[0])], capture_output=True, text=True)
    assert bad.returncode == 1 and json.loads(bad.stdout)["errors"]
    missing = subprocess.run([sys.executable, str(SCRIPT), str(tmp_path / "nope.md")], capture_output=True, text=True)
    assert missing.returncode == 2
