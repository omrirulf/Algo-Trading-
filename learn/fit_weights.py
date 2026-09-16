#!/usr/bin/env python3
"""Fit the blend weights from the journal and write them for the next cycle.

    python learn/fit_weights.py                 # journal file -> logs/blend_weights.json
    python learn/fit_weights.py --db            # from the index built by store/build_db.py
    python learn/fit_weights.py --dry-run       # fit and report, write nothing

What goes in
------------
Every journal line the full model answered, with at least one dimension
scored, joined to the close-to-close return over ``--horizon`` sessions after
it by the same no-lookahead entry rule the scorer uses. NEUTRAL lines are
included: the scores on them are real observations, and they are most of the
journal. Screened lines are not: the screening model's scores are a different
model's reads, and weights fitted to one are not weights for the other. A
signal whose horizon has not elapsed is pending and left out, so a nightly
refit never learns from a return that is not in yet.

The target
----------
The return is divided by the ticker's ATR as a share of price, as the journal
recorded it at signal time, so a 2% move in a staple and a 2% move in a chip
maker are not the same label. It is then winsorised at +-4 ATRs so one
earnings gap cannot own a small regression. A line with no ATR is skipped
rather than mixed in at a different scale.

Lines journalled before the prompt asked for null scores carry 0.0 for a
dimension whose source failed. Where the gap list names that source and the
score is exactly 0.0, it is read as null.

What comes out
--------------
One JSON file, written atomically, in the shape ``analysis.blend`` reads:
the weights per level with their counts, the model, the horizon, the decay
and the prior, and the date the decay was measured from. It is the only file
this package writes, and the package has no order path; CI checks both.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Optional

# Allow ``python learn/fit_weights.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import blend  # noqa: E402
from analysis.reader import SCORE_FIELDS, JournalEntry, read_database, read_journal  # noqa: E402
from analysis.returns import (  # noqa: E402
    ENTRY_AUTO,
    ENTRY_RULES,
    PriceSource,
    YFinancePriceSource,
    forward_return,
)
from analysis.score_journal import DEFAULT_HORIZON  # noqa: E402
from config import settings as cfg  # noqa: E402
from orchestrator.llm import MODEL  # noqa: E402

log = logging.getLogger("fit_weights")

#: Bound on the target, in ATRs.
WINSOR = 4.0

SKIP_NO_SIGNAL = "no signal"
SKIP_OTHER_MODEL = "other model"
SKIP_NO_SCORES = "no scores"
SKIP_NO_TIMESTAMP = "no timestamp"
SKIP_NO_ATR = "no atr"
SKIP_DUPLICATE = "duplicate"

#: A gap naming one of these sources, beside a score of exactly 0.0, is a null.
#: Only for lines written before the prompt asked for null itself.
GAP_KEYWORDS: tuple[tuple[str, str], ...] = (
    ("fundamental", "fundamental_score"),
    ("earnings", "fundamental_score"),
    ("analyst", "analyst_score"),
    ("recommendation", "analyst_score"),
    ("upgrade", "analyst_score"),
    ("institutional", "analyst_score"),
    ("insider", "insider_score"),
    ("positioning", "insider_score"),
    ("fund flows", "insider_score"),
)


def is_full_model(entry: JournalEntry, model: str = MODEL) -> bool:
    """Whether the line's answer came from the model the weights are for.

    The API reports a dated id (``claude-haiku-4-5-20251001``) where the code
    names a family (``claude-haiku-4-5``), so this is a prefix match.
    """
    return bool(entry.model) and entry.model.startswith(model)


def nulled_by_gaps(scores: Mapping[str, Optional[float]], gaps: Iterable[str]) -> dict[str, Optional[float]]:
    """Read a legacy 0.0 as null where a gap names the dimension's source."""
    out = dict(scores)
    for gap in gaps:
        text = gap.lower()
        names = set()
        if "yfinance" in text:
            names.update(name for name in SCORE_FIELDS if name != "news_score")
        names.update(name for keyword, name in GAP_KEYWORDS if keyword in text)
        for name in names:
            if out.get(name) == 0.0:
                out[name] = None
    return out


@dataclass
class Prepared:
    observations: list[blend.Observation] = field(default_factory=list)
    #: Why lines were left out, by reason; ``used`` is the count that went in.
    statuses: Counter = field(default_factory=Counter)


def prepare(
    entries: Iterable[JournalEntry],
    source: PriceSource,
    *,
    horizon: int,
    entry_rule: str = ENTRY_AUTO,
    model: str = MODEL,
    today: Optional[date] = None,
) -> Prepared:
    """Turn journal lines into observations the blend can fit."""
    today = today or datetime.now(timezone.utc).date()
    prepared = Prepared()
    statuses = prepared.statuses
    candidates: dict[str, dict[date, tuple[JournalEntry, dict[str, Optional[float]]]]] = {}

    for entry in entries:
        if not entry.has_signal:
            statuses[SKIP_NO_SIGNAL] += 1
            continue
        if not is_full_model(entry, model):
            statuses[SKIP_OTHER_MODEL] += 1
            continue
        scores = nulled_by_gaps(entry.scores, entry.gaps)
        if not any(value is not None for value in scores.values()):
            statuses[SKIP_NO_SCORES] += 1
            continue
        if entry.timestamp is None:
            statuses[SKIP_NO_TIMESTAMP] += 1
            continue
        if not entry.atr_pct or entry.atr_pct <= 0:
            statuses[SKIP_NO_ATR] += 1
            continue
        day = entry.timestamp.astimezone(timezone.utc).date()
        per_day = candidates.setdefault(entry.ticker, {})
        if day in per_day:
            statuses[SKIP_DUPLICATE] += 1  # one observation per ticker per day: the last line wins
        per_day[day] = (entry, scores)

    for ticker, per_day in sorted(candidates.items()):
        series = source.closes(ticker, min(per_day), today)
        for day, (entry, scores) in sorted(per_day.items()):
            lookup = forward_return(
                series,
                entry.timestamp,
                horizon=horizon,
                timestamp_is_exact=entry.timestamp_is_exact,
                entry=entry_rule,
            )
            if not lookup.ok:
                statuses[lookup.status] += 1
                continue
            target = lookup.value.pct / entry.atr_pct  # type: ignore[union-attr]
            target = max(-WINSOR, min(WINSOR, target))
            prepared.observations.append(blend.Observation(ticker, day, scores, target))

    statuses["used"] = len(prepared.observations)
    return prepared


def write_artifact(artifact: blend.WeightsArtifact, path: Path) -> None:
    """The one write in this package. Atomic, so a cycle never reads half a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(artifact.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


_SHORT = {
    "news_score": "news",
    "technical_score": "tech",
    "fundamental_score": "fund",
    "analyst_score": "anlst",
    "insider_score": "insdr",
}


def render(artifact: blend.WeightsArtifact, prepared: Prepared) -> str:
    """What was fitted, from what, in a form a workflow log can show."""
    statuses = prepared.statuses
    skipped = ", ".join(f"{k} {v}" for k, v in sorted(statuses.items()) if k != "used" and v)
    lines = [
        f"blend weights {artifact.digest()}: model {artifact.model}, horizon {artifact.horizon} "
        f"session(s), half-life {artifact.half_life:g}, prior {artifact.prior_strength:g}, "
        f"fitted {artifact.fitted_on}",
        f"observations used: {statuses['used']}" + (f" (left out: {skipped})" if skipped else ""),
    ]
    if not artifact.levels:
        lines.append("no level fitted; every ticker blends with equal weights")
        return "\n".join(lines)
    header = f"{'level':<24} {'n':>5} {'n_eff':>7} {'own':>5}  " + "  ".join(f"{_SHORT[n]:>6}" for n in SCORE_FIELDS)
    lines += ["", header]
    for key, level in sorted(artifact.levels.items(), key=_level_order):
        weights = "  ".join(f"{level.weights[name]:>+6.2f}" for name in SCORE_FIELDS)
        lines.append(f"{key:<24} {level.n_raw:>5} {level.n_effective:>7.1f} {level.own_share:>5.2f}  {weights}")
    return "\n".join(lines)


def _level_order(item: tuple[str, blend.LevelWeights]) -> tuple[int, str]:
    key = item[0]
    depth = 0 if key == blend.GLOBAL_KEY else 1 if key.startswith("kind:") else 2
    return depth, key


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fit_weights",
        description="Fit the blend weights from the journal and write them for the next cycle.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
                        help="signal journal to read (default: %(default)s)")
    parser.add_argument("--db", nargs="?", const=cfg.DATABASE_PATH, type=Path, default=None,
                        help="read from the index instead (default when given with no value: %(const)s)")
    parser.add_argument("--since", metavar="YYYY-MM-DD", help="only lines from this date on. Requires --db")
    parser.add_argument("--out", type=Path, default=cfg.BLEND_WEIGHTS_PATH,
                        help="weights file to write (default: %(default)s)")
    parser.add_argument("--horizon", type=int, default=DEFAULT_HORIZON,
                        help="sessions of forward return to fit against (default: %(default)s)")
    parser.add_argument("--entry", choices=ENTRY_RULES, default=ENTRY_AUTO,
                        help="which close to enter at, as the scorer defines it (default: %(default)s)")
    parser.add_argument("--half-life", type=float, default=blend.DEFAULT_HALF_LIFE,
                        help="sessions over which an observation's weight halves (default: %(default)s)")
    parser.add_argument("--prior", type=float, default=blend.DEFAULT_PRIOR_STRENGTH,
                        help="pseudo-observations a level's parent is worth (default: %(default)s)")
    parser.add_argument("--dry-run", action="store_true", help="fit and report, write nothing")
    parser.add_argument("-v", "--verbose", action="store_true", help="log fetch failures")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.ERROR,
        format="%(levelname)s %(name)s: %(message)s",
    )
    if args.horizon < 1:
        print("--horizon must be at least 1 session", file=sys.stderr)
        return 2
    if args.since and not args.db:
        print("--since needs --db: the journal file has no index to seek in.", file=sys.stderr)
        return 2

    try:
        read = read_database(args.db, since=args.since) if args.db else read_journal(args.journal)
    except FileNotFoundError as exc:
        print(f"{exc}\nThe orchestrator writes one entry per ticker per cycle; run it first.", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).date()
    prepared = prepare(
        read.entries, YFinancePriceSource(), horizon=args.horizon, entry_rule=args.entry, today=today
    )
    artifact = blend.fit_hierarchy(
        prepared.observations,
        model=MODEL,
        horizon=args.horizon,
        as_of=today,
        half_life=args.half_life,
        prior_strength=args.prior,
    )
    print(render(artifact, prepared))
    if args.dry_run:
        return 0
    write_artifact(artifact, args.out)
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
