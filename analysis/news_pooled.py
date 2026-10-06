"""The card's replacement rule (2), pooled over five weekday checks (the owner's decision of 6 Oct 2026).

The owner's words: "Run the same news check on four more weekdays, so five
days in total, before the 2026-12-22 freeze. Spread them over at least two
different weeks if you can. Pool all five days for each name. Replace a
name only if its pooled share of relevant headlines is under 30% with at
least 10 pooled headlines, or if it had zero headlines on all five days
(this includes ZTO if it never answers). A name with fewer than 10 pooled
headlines is kept, unless it had zero on all five days." And: "Keep STT and
IRM."

One check is one weekday's run of ``.github/workflows/universe-news-check.yml``
over every name of the list (the universe's own query, company name plus
ticker, and the code-only rule of ``analysis/news_relevance.py``), with the
names whose search failed asked again the same day. Each day is kept as one
file, ``docs/research/news-checks/YYYY-MM-DD.json``, made from the run's
``RESULT`` and ``FAILED`` lines (``--from-log``). A name with no answer on a
day has no headline that day: it adds nothing to the pooled counts, and it
counts as zero for "zero headlines on all five days".

The rule decides only once there are exactly five checks on five different
weekdays; before that the report says how many there are. It applies to
every name of the list (rule (2) is the list's rule); the 19 names under 30%
on 2026-10-05, and ZTO, are the ones it was written for. A replacement is
chosen as the card says, never by price, return or score.

Pure: no network, no file written. ``main`` reads the day files and prints.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Final, Iterable, Mapping, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.news_relevance import FAIL_BELOW  # noqa: E402
from config import shadow_universe as su  # noqa: E402
from config.market_calendar import is_trading_day  # noqa: E402

#: The number of weekday checks the rule pools (the owner: "five days in total").
DAYS_NEEDED: Final[int] = 5
#: Under this many pooled headlines a name is kept, unless it had none on every day.
MIN_POOLED_HEADLINES: Final[int] = 10
#: The last day a check can count: the list freezes on the registration date.
LAST_DAY: Final[date] = su.REGISTRATION
#: The owner's decision of 6 Oct 2026: the two replacements of 3 Oct stay, whatever the pooled result.
KEPT: Final[dict[str, str]] = {
    "STT": "kept by the owner's decision of 6 Oct 2026 (replaced BK on 3 Oct by rule (3))",
    "IRM": "kept by the owner's decision of 6 Oct 2026 (replaced AVB on 3 Oct by rule (3))",
}
#: Where the day files live.
CHECKS_DIR: Final[Path] = Path(__file__).resolve().parent.parent / "docs" / "research" / "news-checks"

REPLACE: Final[str] = "replace"
KEEP: Final[str] = "keep"


@dataclass(frozen=True)
class DayCheck:
    """One weekday's check: each name's (headlines, relevant, named by name), or None for no answer."""

    day: date
    runs: tuple[int, ...]
    names: Mapping[str, Optional[tuple[int, int, int]]]


@dataclass(frozen=True)
class Pooled:
    """One name over the checks, and what the rule says."""

    ticker: str
    days: int
    answered: int
    headlines: int
    relevant: int
    named: int
    zero_every_day: bool
    decision: Optional[str] = None
    reason: str = ""

    @property
    def share(self) -> Optional[float]:
        return self.relevant / self.headlines if self.headlines else None


def load_day(path: Path | str) -> DayCheck:
    """A day file, checked: every name of the list as it stood that day once, nothing else, counts that make sense.

    A name replaced after that day (``su.REPLACED``) is in the file in place
    of the name that replaced it, so a replacement never makes an earlier
    day file unreadable.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    day = date.fromisoformat(data["day"])
    names: dict[str, Optional[tuple[int, int, int]]] = {}
    for ticker, counts in data["names"].items():
        if counts is None:
            names[ticker] = None
            continue
        headlines, relevant, named = (int(c) for c in counts)
        if not 0 <= named <= relevant <= headlines:
            raise ValueError(f"{path}: {ticker}: counts out of order: {counts}")
        names[ticker] = (headlines, relevant, named)
    missing = sorted(set(su.TICKERS) - set(names))
    extra = sorted(set(names) - set(su.TICKERS))
    # The list as it stood that day: a name replaced since may be there, and its replacement not.
    out_since = {old for old in extra if old in su.REPLACED}
    in_since = {new for new in missing if new in {n for n, _ in su.REPLACED.values()}}
    swapped = any(old in names and new in names for old, (new, _) in su.REPLACED.items())
    if set(missing) - in_since or set(extra) - out_since or len(names) != len(su.TICKERS) or swapped:
        raise ValueError(f"{path}: not the list: missing {missing}, not in the list {extra}")
    return DayCheck(day=day, runs=tuple(int(r) for r in data.get("runs") or ()), names=names)


def day_from_log(text: str, day: date, runs: Sequence[int]) -> dict:
    """A day file's contents from the runs' logs that day, oldest first.

    Each run prints ``RESULT {ticker: [headlines, relevant, named]}`` and
    ``FAILED [tickers]``. A later run (a recheck of the names that failed)
    replaces what an earlier one said about the names it asked; a name no
    run answered is None. Every name of the list must have been asked.
    """
    asked: dict[str, Optional[list[int]]] = {}
    results = re.findall(r"^(?:.*?\s)?RESULT (\{.*\})\s*$", text, re.M)
    failed = re.findall(r"^(?:.*?\s)?FAILED (\[.*\])\s*$", text, re.M)
    if len(results) != len(failed):
        raise ValueError(f"{len(results)} RESULT line(s) but {len(failed)} FAILED line(s)")
    for result, broken in zip(results, failed):
        for ticker, counts in json.loads(result).items():
            asked[ticker] = [int(c) for c in counts]
        for ticker in json.loads(broken):
            asked[ticker] = None
    missing = [t for t in su.TICKERS if t not in asked]
    if missing:
        raise ValueError(f"not asked that day: {', '.join(missing)}")
    return {"day": day.isoformat(), "runs": [int(r) for r in runs],
            "query": "company name plus ticker (config.shadow_universe.news_query)",
            "rule": "code-only (analysis/news_relevance.py)",
            "names": {t: asked[t] for t in su.TICKERS}}


def day_json(made: dict) -> str:
    """A day file's text: the header fields, then one name a line, in the list's order."""
    head = {k: v for k, v in made.items() if k != "names"}
    body = ",\n".join(f"  {json.dumps(t)}: {json.dumps(c)}" for t, c in made["names"].items())
    return json.dumps(head)[:-1] + ',\n "names": {\n' + body + "\n }\n}\n"


def problems(days: Sequence[DayCheck]) -> list[str]:
    """Why these checks cannot be pooled yet; empty when the rule can decide."""
    out = []
    dates = [d.day for d in days]
    if len(set(dates)) != len(dates):
        out.append("two checks on the same day")
    for d in dates:
        if not is_trading_day(d):
            out.append(f"{d} is not a weekday the market traded")
        if d >= LAST_DAY:
            out.append(f"{d} is on or after the day the list freezes ({LAST_DAY})")
    if len(set(dates)) < DAYS_NEEDED:
        out.append(f"{len(set(dates))} of {DAYS_NEEDED} checks so far")
    elif len(set(dates)) > DAYS_NEEDED:
        out.append(f"{len(set(dates))} checks: the rule pools exactly {DAYS_NEEDED}")
    return out


def weeks(days: Sequence[DayCheck]) -> list[tuple[int, int]]:
    """The ISO weeks the checks fall in (the owner: "at least two different weeks if you can")."""
    return sorted({d.day.isocalendar()[:2] for d in days})


def decide(found: Pooled) -> tuple[str, str]:
    """The owner's rule for one name pooled over five checks."""
    if found.ticker in KEPT:
        return KEEP, KEPT[found.ticker]
    if found.zero_every_day:
        if found.answered == 0:
            return REPLACE, "no answer on any of the five days: zero headlines on all five days"
        return REPLACE, "zero headlines on all five days"
    if found.headlines < MIN_POOLED_HEADLINES:
        return KEEP, f"fewer than {MIN_POOLED_HEADLINES} pooled headlines ({found.headlines}), not zero on all five days"
    if found.relevant < FAIL_BELOW * found.headlines:
        return REPLACE, f"{found.relevant} of {found.headlines} pooled headlines relevant, under 30%"
    return KEEP, f"{found.relevant} of {found.headlines} pooled headlines relevant, 30% or more"


def held(days: Sequence[DayCheck]) -> list[str]:
    """The names the day files hold, in the first day's order, then any that came in later."""
    return list(dict.fromkeys(t for d in days for t in d.names))


def pool(days: Sequence[DayCheck], tickers: Optional[Iterable[str]] = None) -> list[Pooled]:
    """Every name the day files hold, pooled over the checks; decided only when ``problems`` is empty.

    A name pooled over fewer days than the checks (on the list for only some
    of them: it came in, or went out, by another rule in between) is not
    decided: the rule is written for five days.
    """
    ready = not problems(days)
    out = []
    for ticker in (held(days) if tickers is None else tickers):
        counts = [d.names[ticker] for d in days if ticker in d.names]
        answered = [c for c in counts if c is not None]
        found = Pooled(
            ticker=ticker, days=len(counts), answered=len(answered),
            headlines=sum(c[0] for c in answered), relevant=sum(c[1] for c in answered),
            named=sum(c[2] for c in answered),
            zero_every_day=all(c is None or c[0] == 0 for c in counts),
        )
        if ready and len(counts) < len(days):
            found = Pooled(**{**found.__dict__, "reason": f"on the list on {len(counts)} of the {len(days)} days"})
        elif ready:
            decision, reason = decide(found)
            found = Pooled(**{**found.__dict__, "decision": decision, "reason": reason})
        out.append(found)
    return out


def _pct(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value:.0%}"


def report(days: Sequence[DayCheck], pooled: Sequence[Pooled]) -> str:
    """The pooled table, the names the rule replaces with their reasons, or why it cannot decide yet."""
    lines = ["# The universe news check, pooled (card rule (2), the owner's decision of 6 Oct 2026)", ""]
    lines.append("Checks: " + (", ".join(f"{d.day} (runs {', '.join(map(str, d.runs)) or 'n/a'})" for d in days)
                               or "none"))
    spread = weeks(days)
    lines.append(f"Weeks: {len(spread)} different ({', '.join(f'{y}-W{w:02d}' for y, w in spread) or 'none'}).")
    waiting = problems(days)
    if waiting:
        lines += ["", "**No decision yet**: " + "; ".join(waiting) + "."]
    else:
        replaced = [p for p in pooled if p.decision == REPLACE]
        lines += ["", f"**Replace: {len(replaced)} name(s)**" + (": " if replaced else ".")
                  + ", ".join(f"{p.ticker} ({p.reason})" for p in replaced)]
        kept = [p for p in pooled if p.ticker in KEPT]
        lines += ["Kept by the owner's decision: " + ", ".join(
            f"{p.ticker} ({p.relevant} of {p.headlines}, {_pct(p.share)})" for p in kept)]
    lines += ["", "| Name | Days answered | Headlines | Relevant | Share | Named | Decision |",
              "| --- | ---: | ---: | ---: | ---: | ---: | --- |"]
    for p in pooled:
        lines.append(f"| {p.ticker} | {p.answered} of {p.days} | {p.headlines} | {p.relevant} | {_pct(p.share)} "
                     f"| {p.named} | {p.decision or 'waiting'} |")
    return "\n".join(lines) + "\n"


def load_days(directory: Path | str = CHECKS_DIR) -> list[DayCheck]:
    """Every day file, oldest first."""
    return sorted((load_day(p) for p in sorted(Path(directory).glob("*.json"))), key=lambda d: d.day)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--from-log", type=Path, default=None,
                        help="print a day file made from the check's log(s) that day, oldest run first")
    parser.add_argument("--day", type=date.fromisoformat, default=None, help="the check's day (with --from-log)")
    parser.add_argument("--run", type=int, action="append", default=[], help="a run id (with --from-log; repeat)")
    parser.add_argument("--dir", type=Path, default=CHECKS_DIR, help="the day files (default: %(default)s)")
    args = parser.parse_args(argv)
    if args.from_log is not None:
        if args.day is None:
            parser.error("--from-log needs --day")
        made = day_from_log(args.from_log.read_text(encoding="utf-8"), args.day, args.run)
        print(day_json(made), end="")
        return 0
    days = load_days(args.dir)
    print(report(days, pool(days)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
