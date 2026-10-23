#!/usr/bin/env python3
"""Simulated driver for interview runs: answers one question from a case's answers.md.

Usage: ask_driver.py --case CASE_DIR --log TRANSCRIPT.md "question"

Prints the driver's answer on stdout and appends the question and answer to the
transcript, so a run's questions can be counted afterwards. Uses `claude -p` with a
small model and no tools; each call is a billed model call.

Exit codes: 0 answered, 2 usage error or missing answers.md, 3 the model call failed.
"""
import argparse
import subprocess
import sys
from pathlib import Path

PROMPT = """You play the product owner of a software product in an interview about one use case.
Everything you know is in the facts below. Rules:
- Answer briefly, in plain words, from the facts only. A fact counts if it settles the point,
  even when it is worded differently from the question.
- A question may have several parts: answer every part the facts settle, and for each part they
  don't, say "Not decided: <that part>. Use your recommendation."
- If the question proposes an answer that agrees with the facts, say yes (and correct any detail that differs).
- Only if no fact bears on the question at all, reply exactly: "Not decided. Use your recommendation."
- Don't volunteer facts the question didn't ask about. Never mention that you have a list of facts.

FACTS
{facts}

QUESTION
{question}
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--case", type=Path, required=True, help="case folder holding answers.md")
    ap.add_argument("--log", type=Path, required=True, help="transcript file to append to")
    ap.add_argument("--model", default="haiku")
    ap.add_argument("question")
    args = ap.parse_args()
    answers = args.case / "answers.md"
    if not answers.is_file():
        print(f"ask_driver: no answers.md in {args.case}", file=sys.stderr)
        return 2
    prompt = PROMPT.format(facts=answers.read_text(encoding="utf-8"), question=args.question)
    try:
        out = subprocess.run(
            ["claude", "-p", "--model", args.model, "--disallowedTools", "*"],
            input=prompt, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"ask_driver: model call failed: {e}", file=sys.stderr)
        return 3
    if out.returncode != 0:
        print(f"ask_driver: model call failed: {out.stderr.strip()}", file=sys.stderr)
        return 3
    answer = out.stdout.strip()
    args.log.parent.mkdir(parents=True, exist_ok=True)
    n = sum(1 for l in args.log.read_text(encoding="utf-8").splitlines() if l.startswith("**Q")) if args.log.exists() else 0
    with args.log.open("a", encoding="utf-8") as f:
        f.write(f"**Q{n + 1}.** {args.question}\n\n**A{n + 1}.** {answer}\n\n")
    print(answer)
    return 0


if __name__ == "__main__":
    sys.exit(main())
