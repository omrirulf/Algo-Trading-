"""The monthly coach, checklist only (the owner's approval of 3 Oct 2026, with conditions).

The plan (``docs/research/monthly-coach-plan.md``) was approved on these
conditions, and this module is built to them:

* **Checklist only for the first two months** (``FIRST_MONTH`` and the month
  after), and after that until the owner confirms that they want to enter
  numbers. The checklist is fixed text made here: no model is asked, so it
  costs nothing.
* **No personal number is collected.** The checklist asks the owner to
  think about the base of the pyramid; it asks nobody to send a number
  anywhere, and nothing here reads one. The only data it reads is the
  experiment's next checkpoint date from ``logs/race_gate.json``, which is
  already public.
* **Later, the owner's numbers go only into a private Supabase project, and
  the model sees percentages only.** None of that is built: the data entry
  and the private job wait for the owner's go-ahead (``DATA_ENTRY_BUILT``).
* **Nothing personal on ntfy.sh, in the repository, in logs or in
  artifacts.** The push carries this module's fixed words and the public
  checkpoint date, nothing else (``.github/workflows/coach.yml``).
* **Cost cap: $0.10 a month** (``MONTHLY_COST_CAP_USD``), for the day a model
  call is added; the checklist itself makes none (``MODEL_CALLS``).

It runs on the first working day (Monday to Friday) of each month: the
workflow wakes on the 1st, 2nd and 3rd, and ``due`` says yes on one of them.
Standard library only; it reads one public file and prints JSON.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Final, Optional, Sequence

#: The first month a checklist is sent: the first whole month after the owner's approval of 3 Oct 2026.
FIRST_MONTH: Final[date] = date(2026, 11, 1)
#: Checklist only for this many months at least (the owner's condition), and until the owner says otherwise.
CHECKLIST_ONLY_MONTHS: Final[int] = 2
#: The coach's model budget, for the day a model call is added. The checklist makes none.
MONTHLY_COST_CAP_USD: Final[float] = 0.10
#: Model calls the checklist makes in a month.
MODEL_CALLS: Final[int] = 0
#: The private data entry (a private Supabase project): not built until the owner confirms.
DATA_ENTRY_BUILT: Final[bool] = False

#: The public file the checkpoint date is read from.
RACE_GATE: Final[Path] = Path(__file__).resolve().parent.parent / "logs" / "race_gate.json"

TITLE: Final[str] = "🗓️ Monthly check-in"

#: The checklist, word for word. No question asks for a number to be sent anywhere.
QUESTIONS: Final[tuple[str, ...]] = (
    "Did you save part of your take-home pay this month? Think of the share, not the amount.",
    "Your savings by part (world stocks, Israeli bonds, cash, anything else): is any part far from where "
    "you want it?",
    "Have you chosen a target share for each part, and how far from it you let a part drift before you "
    "rebalance?",
    "Keren hishtalmut, kupat gemel lehashkaa and pension: are this year's deposits on plan?",
)

#: Sent with the questions, every month. Nothing is to be typed into any message, page or file.
KEEP_IT_PRIVATE: Final[str] = ("Keep your answers to yourself: send no number anywhere. Nothing is "
                               "collected yet.")


def first_working_day(year: int, month: int) -> date:
    """The month's first Monday-to-Friday."""
    day = date(year, month, 1)
    while day.weekday() >= 5:
        day = day.replace(day=day.day + 1)
    return day


def due(today: date) -> bool:
    """Whether the checklist is sent on ``today``: the first working day of a month from ``FIRST_MONTH``."""
    return today >= FIRST_MONTH and today == first_working_day(today.year, today.month)


def month_number(today: date) -> int:
    """1 for ``FIRST_MONTH``, 2 for the month after, and so on."""
    return (today.year - FIRST_MONTH.year) * 12 + today.month - FIRST_MONTH.month + 1


def next_checkpoint(race_gate: Optional[dict]) -> Optional[str]:
    """The race's next planned look, as an ISO date, from ``logs/race_gate.json``; None when it says none."""
    if not isinstance(race_gate, dict):
        return None
    upcoming = race_gate.get("next")
    estimated = upcoming.get("estimated") if isinstance(upcoming, dict) else None
    if not isinstance(estimated, str):
        return None
    try:
        return date.fromisoformat(estimated).isoformat()
    except ValueError:
        return None


def _checkpoint_text(checkpoint: Optional[str]) -> str:
    if checkpoint is None:
        return "The experiment: no checkpoint date yet. No decisions before the first one."
    day = date.fromisoformat(checkpoint)
    return f"The experiment: next checkpoint about {day.day} {day:%b %Y}. No decisions before it."


def message(today: date, race_gate: Optional[dict]) -> dict[str, Any]:
    """The month's push: ``{"title", "message", "month"}``. Fixed words, the public checkpoint date, nothing else."""
    number = month_number(today)
    lines = [f"Questions for {today:%B %Y}:"]
    lines += [f"{i}. {q}" for i, q in enumerate(QUESTIONS, start=1)]
    lines.append(KEEP_IT_PRIVATE)
    lines.append(_checkpoint_text(next_checkpoint(race_gate)))
    if number == CHECKLIST_ONLY_MONTHS:
        lines.append("This is the last of the two checklist-only months. Tell Claude when you want to start "
                     "entering numbers in a private place; until then the checklist goes on.")
    return {"title": TITLE, "message": "\n".join(lines), "month": number}


def _read(path: Path) -> Optional[dict]:
    try:
        found = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return found if isinstance(found, dict) else None


def main(argv: Optional[Sequence[str]] = None) -> int:
    """``python -m coach.checklist``: print ``{"due": ..., "title", "message"}`` as JSON. Sends nothing itself."""
    parser = argparse.ArgumentParser(prog="python -m coach.checklist",
                                     description="The monthly checklist (no personal number, no model).")
    parser.add_argument("--race-gate", type=Path, default=RACE_GATE)
    parser.add_argument("--today", default=None, help="ISO date, default today in UTC")
    parser.add_argument("--force", action="store_true", help="make the message even if today is not due")
    args = parser.parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else datetime.now(timezone.utc).date()
    out: dict[str, Any] = {"date": today.isoformat(), "due": due(today)}
    if out["due"] or args.force:
        out |= message(today, _read(args.race_gate))
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
