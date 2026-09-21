"""Three arms, the same lines, the same realised returns.

    python analysis/horse_race.py
    python analysis/horse_race.py --horizon 5 --floor 0.5

Arm A is the model: whatever the journal says it said. Arm B is the coded
thesis in ``rules/momentum.py``, recomputed here from the technicals every
line already carries. Arm C is the coin flip in ``rules/control.py``,
recomputed the same way. Each is put through the identical floor, the
identical stop and sizing arithmetic, and scored against the identical
price history -- so the only thing that differs between the rows is the
judgement, and the coin flip is what "no judgement" scores.

Every arm is offered every line, except the ones no arm was offered: a
ticker already in the book, where the model was never asked and a rule
holding the same book would not have been either. The model then answers
on fewer lines than the rules, because the screen drops some and the model
fails on some, and both of those are the model's to own -- the funnel is
part of the design being raced, not an excuse for it.

Nothing here is fitted. The momentum arm's parameters are the textbook
values and this file never touches them; it judges the rule, it does not
tune it. That is the difference between a race and a story.

This is per-trade, like baseline_compare.py, and shares its machinery:
no portfolio, no compounding, no overlap policy. Read-only in every
direction -- it reads the journal, fetches prices, and prints.
"""

from __future__ import annotations

import argparse
import logging
import statistics
import sys
from dataclasses import dataclass, replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Sequence

# Allow ``python analysis/horse_race.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.baseline_compare import (  # noqa: E402
    OhlcFetcher,
    simulate_model_trades,
    watchlist_buy_and_hold,
)
from analysis.metrics import ScoredSignal  # noqa: E402
from analysis.reader import JournalEntry, read_journal  # noqa: E402
from analysis.returns import ENTRY_AUTO, ENTRY_RULES, PriceSource, YFinancePriceSource  # noqa: E402
from analysis.scoring import score_entries  # noqa: E402
from backtest.sweep import MIN_TRADES, Outcome  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from orchestrator.technicals import TechnicalSnapshot  # noqa: E402
from rules import ARMS, control, momentum  # noqa: E402

DEFAULT_HORIZON = 3

#: Arm A's name in the report. The rule arms report under their own.
MODEL_ARM = "model"

#: Report order. The model first because it is the incumbent; the coin flip
#: last because it is the floor everything above it has to clear.
ARM_ORDER = (MODEL_ARM, momentum.NAME, control.NAME)

log = logging.getLogger("horse_race")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="horse_race",
        description="Race the model against the coded rule and a coin flip on realised returns.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
                        help="path to the signal journal (default: %(default)s)")
    parser.add_argument("--horizon", type=int, default=DEFAULT_HORIZON,
                        help="trading sessions held after entry (default: %(default)s)")
    parser.add_argument("--entry", choices=ENTRY_RULES, default=ENTRY_AUTO,
                        help="which close resolves a signal (default: %(default)s)")
    parser.add_argument("--floor", type=float, default=cfg.MIN_CONVICTION,
                        help="conviction floor applied to EVERY arm alike (default: %(default)s)")
    parser.add_argument("--equity", type=float, default=100_000.0)
    parser.add_argument("--stop-multiplier", type=float, default=cfg.ATR_STOP_MULTIPLIER)
    parser.add_argument("--max-position-pct", type=float, default=cfg.MAX_POSITION_PCT)
    parser.add_argument("-v", "--verbose", action="store_true", help="log fetch failures")
    return parser


# --------------------------------------------------------------------------- #
# Which lines, and what each arm said on them
# --------------------------------------------------------------------------- #


def offered(entries: Sequence[JournalEntry]) -> list[JournalEntry]:
    """The lines every arm is asked on: not held, and placeable in time."""
    return [e for e in entries if not e.held and e.timestamp is not None]


def entries_for_arm(name: str, lines: Sequence[JournalEntry]) -> list[JournalEntry]:
    """One entry per offered line, carrying this arm's call instead of the model's.

    The model's entries are the lines as journalled, where it produced a
    signal at all. A rule's entries are the same lines with the bias and
    conviction replaced by what the rule says of the technicals on that
    line -- ticker, timestamp and technicals untouched, so the scorer joins
    them to exactly the same forward return.
    """
    if name == MODEL_ARM:
        return [e for e in lines if e.has_signal]
    arm = ARMS[name]
    out: list[JournalEntry] = []
    for entry in lines:
        technicals = TechnicalSnapshot.from_dict(entry.technicals) if entry.technicals else None
        signal = arm(entry.ticker, technicals, entry.timestamp.astimezone(timezone.utc).date())
        out.append(replace(entry, bias=signal.bias.value, conviction=signal.conviction, scores={}, blend={}))
    return out


def direction_agreement(
    a: Sequence[JournalEntry], b: Sequence[JournalEntry]
) -> tuple[Optional[float], int]:
    """Of the lines where both took a side, the share on which they took the same one."""
    calls_a = {(e.ticker, e.timestamp): e.bias for e in a if e.is_directional}
    calls_b = {(e.ticker, e.timestamp): e.bias for e in b if e.is_directional}
    both = [key for key in calls_a if key in calls_b]
    if not both:
        return None, 0
    return sum(1 for key in both if calls_a[key] == calls_b[key]) / len(both), len(both)


# --------------------------------------------------------------------------- #
# Fetching once, for every arm
# --------------------------------------------------------------------------- #


def prewarm(
    lines: Sequence[JournalEntry], source: PriceSource, fetcher: OhlcFetcher,
    horizon: int, today: date,
) -> None:
    """Fetch each ticker once, over the widest window any arm will ask for.

    Both price sources cache by ticker and answer a later, narrower request
    from the first fetch -- so whichever arm ran first would decide how much
    history the others got. Asking for the union up front, before any arm
    runs, is what makes the order of the arms not matter. The windows here
    are exactly the ones score_entries and simulate_model_trades would ask
    for themselves, computed over every offered line rather than one arm's.
    """
    span: dict[str, tuple[date, date]] = {}
    for entry in lines:
        day = entry.timestamp.astimezone(timezone.utc).date()
        lo, hi = span.get(entry.ticker, (day, day))
        span[entry.ticker] = (min(lo, day), max(hi, day))
    for ticker, (lo, hi) in sorted(span.items()):
        source.closes(ticker, lo, today)
        fetcher.ohlc(ticker, lo, hi + timedelta(days=horizon * 2 + 10))


# --------------------------------------------------------------------------- #
# Racing one arm
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ArmResult:
    name: str
    #: Lines the arm was asked on.
    offered: int
    #: Of those, lines where it took a side.
    directional: int
    #: Of those, with a realised outcome and conviction at or above the floor.
    acted_on: int
    #: The acted-on trades, re-simulated through the real stop and sizing.
    outcome: Outcome
    could_not_simulate: int
    #: Every acted-on signal, so the window can be read off the union.
    scored: tuple[ScoredSignal, ...] = ()


def race_arm(
    name: str, lines: Sequence[JournalEntry], *, floor: float, horizon: int,
    entry_rule: str, today: date, source: PriceSource, fetcher: OhlcFetcher,
    equity: float, stop_multiplier: float, max_position_pct: float,
) -> ArmResult:
    arm_lines = entries_for_arm(name, lines)
    scored, _ = score_entries(arm_lines, source, horizon, entry_rule, today)
    acted = [s for s in scored if s.conviction >= floor]
    trades, _matched, dropped = simulate_model_trades(
        acted, equity=equity, horizon_days=horizon, stop_multiplier=stop_multiplier,
        max_position_pct=max_position_pct, fetcher=fetcher,
    )
    return ArmResult(
        name=name,
        offered=len(arm_lines),
        directional=sum(1 for e in arm_lines if e.is_directional),
        acted_on=len(acted),
        outcome=Outcome(label=name, trades=trades),
        could_not_simulate=dropped,
        scored=tuple(acted),
    )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.ERROR,
        format="%(levelname)s %(name)s: %(message)s",
    )
    if args.horizon < 1:
        print("--horizon must be at least 1 session", file=sys.stderr)
        return 2

    try:
        read = read_journal(args.journal)
    except FileNotFoundError as exc:
        print(f"{exc}\nThe orchestrator writes one entry per ticker per cycle; run it first.", file=sys.stderr)
        return 1
    lines = offered(read.entries)
    if not lines:
        print(f"{args.journal} has no lines any arm could be asked on.", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).date()
    source = YFinancePriceSource()
    fetcher = OhlcFetcher()
    prewarm(lines, source, fetcher, args.horizon, today)

    results = [
        race_arm(
            name, lines, floor=args.floor, horizon=args.horizon, entry_rule=args.entry,
            today=today, source=source, fetcher=fetcher, equity=args.equity,
            stop_multiplier=args.stop_multiplier, max_position_pct=args.max_position_pct,
        )
        for name in ARM_ORDER
    ]
    if not any(r.acted_on for r in results):
        print("No arm has a resolved, above-floor trade yet -- nothing to race.", file=sys.stderr)
        return 1

    agreement, agreed_on = direction_agreement(
        entries_for_arm(MODEL_ARM, lines), entries_for_arm(momentum.NAME, lines)
    )

    everything = [s for r in results for s in r.scored]
    window_start = min(s.forward.entry_date for s in everything)
    window_end = max(s.forward.exit_date for s in everything)
    # A fresh source: the shared one above holds each ticker from its own
    # earliest line, which for most tickers is later than the race's
    # window_start, and a cache hit would then answer from too short a span.
    basket = YFinancePriceSource()
    watchlist_return, watchlist_n, watchlist_missing = watchlist_buy_and_hold(
        DEFAULT_WATCHLIST, window_start, window_end, basket,
    )
    spy_return, spy_n, _ = watchlist_buy_and_hold(("SPY",), window_start, window_end, basket)

    print(render(
        results, floor=args.floor, horizon=args.horizon,
        window_start=window_start, window_end=window_end,
        agreement=agreement, agreed_on=agreed_on,
        watchlist_return=watchlist_return, watchlist_n=watchlist_n,
        watchlist_total=len(DEFAULT_WATCHLIST), watchlist_missing=watchlist_missing,
        spy_return=spy_return if spy_n else None,
    ))
    return 0


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render(
    results: Sequence[ArmResult], *, floor: float, horizon: int,
    window_start: date, window_end: date,
    agreement: Optional[float], agreed_on: int,
    watchlist_return: Optional[float], watchlist_n: int, watchlist_total: int,
    watchlist_missing: int, spy_return: Optional[float],
) -> str:
    lines = [
        "THREE ARMS, THE SAME LINES, THE SAME REALISED RETURNS",
        "=" * 78,
        f"horizon {horizon} session(s) | conviction floor {floor} applied to every arm | "
        f"window {window_start} to {window_end}",
        "",
        "Coverage: what each arm was asked, and what it did with it",
        "-" * 78,
        f"{'arm':<12}{'offered':>9}{'took a side':>13}{'acted on':>10}{'simulated':>11}{'dropped':>9}",
    ]
    for r in results:
        lines.append(
            f"{r.name:<12}{r.offered:>9}{r.directional:>13}{r.acted_on:>10}"
            f"{r.outcome.n:>11}{r.could_not_simulate:>9}"
        )
    lines += [
        "",
        "  'offered' differs between the model and the rules by design: the",
        "  screen drops lines and the model fails on lines, and both are the",
        "  model's to own. 'dropped' is warm-up, cap or missing bars in the",
        "  stop simulation -- excluded, not counted as a hit or a miss.",
        "",
        "The race: per-trade, through the real stop and sizing",
        "-" * 78,
        f"{'arm':<12}{'n':>5}{'hit rate':>11}{'median':>10}{'mean':>10}{'stopped out':>13}",
    ]
    for r in results:
        o = r.outcome
        flag = "" if o.n == 0 or o.enough else "  <- too few"
        lines.append(
            f"{r.name:<12}{o.n:>5}{_pct(_hit_rate(o)):>11}{_pct(o.median_return):>10}"
            f"{_pct(_mean_return(o)):>10}{_pct(o.stop_hit_rate):>13}{flag}"
        )
    lines += [
        "",
        f"Direction agreement, model vs {momentum.NAME}, where both took a side: "
        f"{_pct(agreement)} (n={agreed_on})",
        "",
        "Buy-and-hold, same window, no arm at all:",
        f"  watchlist ({watchlist_n}/{watchlist_total} tickers priced"
        + (f", {watchlist_missing} missing" if watchlist_missing else "")
        + f")  {_pct(watchlist_return)}",
        f"  SPY{'':<45}{_pct(spy_return)}",
        "",
        "HOW TO READ THIS",
        "-" * 78,
        f"The {control.NAME} row is the number the other two are really measured",
        "against: it is what taking a side with no information scores on these",
        "names over these windows. An arm that cannot beat it is not reading",
        "anything. The buy-and-hold rows say what the direction of the market",
        "alone was worth, which in a rising week is most of what 'always long'",
        "would have got.",
        "",
        f"The {momentum.NAME} arm's parameters are the textbook ones and were not",
        "chosen by looking at this journal. This report judges the rule; it",
        "does not tune it, and a good number here is not a reason to start.",
        "",
        "LIMITS",
        "-" * 78,
        "Per-trade, not a portfolio: no overlapping positions, no cash, no",
        "compounding -- the same scope as baseline_compare.py, for the same",
        "reason. Anything marked 'too few' is arithmetic, not evidence, and",
        "a week's worth of trades all inside one market regime is fewer",
        "independent observations than the n column suggests.",
    ]
    return "\n".join(lines)


def _hit_rate(outcome: Outcome) -> Optional[float]:
    if not outcome.trades:
        return None
    return sum(1 for t in outcome.trades if t.return_pct > 0) / outcome.n


def _mean_return(outcome: Outcome) -> Optional[float]:
    if not outcome.trades:
        return None
    return statistics.fmean(t.return_pct for t in outcome.trades)


def _pct(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value * 100:+.1f}%"


if __name__ == "__main__":
    raise SystemExit(main())
