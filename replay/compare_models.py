#!/usr/bin/env python3
"""Compare model and effort configurations on recorded context.

    # What the incumbent actually costs, measured (1 cell, N calls)
    python replay/compare_models.py --limit 20 --only claude-opus-5:medium

    # The staircase walk: enter top-left, step down on pass, right on fail
    python replay/compare_models.py --limit 20

Every cell replays the *same* journal contexts, so the only thing that varies
is the configuration. Cost comes from the API's own token counts.

    # A non-Claude candidate for the FULL model (see the warning below)
    python replay/compare_models.py --limit 40 \
        --base-url https://api.deepinfra.com/v1/openai \
        --only openai/gpt-oss-120b:high --api-key "$KEY"

This cannot tell you which model is *right* -- there is no ground truth for a
trading signal until the market moves. It tells you what each costs and how
differently each behaves against the incumbent.

**The 90% floor was written for a choice between Claude tiers, and it does
not transfer to ``--base-url``.** Moving the screen is a decision about who
gets *asked*; its worst case is a trade not taken, which is why that tool
gates on escalation recall. Moving the full model is a decision about what is
*traded*, and its worst case is a position opened on the wrong side -- an
actual loss rather than a missed gain. A 90% agreement there means one call in
ten differs on the question that moves money, and the ten percent is not
visible in this table as anything but a number. Treat a passing cell as
permission to look harder, never as permission to switch.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from replay import runner  # noqa: E402
from replay.compare_configs import (  # noqa: E402
    EFFORT_NOTCHES,
    MODEL_TIERS,
    Cell,
    clears_floor,
    error_kinds,
    staircase_order,
)

#: Pre-registered before any cell runs, per the cost guide: a floor read off
#: the results afterwards is not evidence, it is a story fitted to them.
DEFAULT_FLOOR = 0.90


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare model/effort configurations.")
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--limit", type=int, default=20,
                        help="contexts per cell (default 20). Every cell costs this many calls.")
    parser.add_argument("--floor", type=float, default=DEFAULT_FLOOR,
                        help=f"agreement a cell must clear to be acceptable (default {DEFAULT_FLOOR})")
    parser.add_argument("--only", action="append", default=None,
                        metavar="MODEL:EFFORT",
                        help="probe just these cells, e.g. claude-sonnet-5:low")
    parser.add_argument("--tickers", type=int, default=0,
                        help="watchlist size to project a monthly bill for "
                             "(default: however many are configured)")
    parser.add_argument("--dry-run", action="store_true",
                        help="print the plan and its call budget; make no calls")
    parser.add_argument("--base-url", type=str, default="",
                        help="ask an OpenAI-compatible endpoint instead of Claude, "
                             "e.g. https://api.deepinfra.com/v1/openai. Use with "
                             "--only MODEL:EFFORT naming that endpoint's model. This "
                             "moves the call that DECIDES WHAT IS TRADED, not the "
                             "screen that decides who gets asked -- read the floor "
                             "note below before trusting an agreement number here.")
    parser.add_argument("--api-key", type=str, default="",
                        help="bearer token for --base-url, if it wants one")
    parser.add_argument("--concurrency", type=int, default=8,
                        help="calls in flight at once, --base-url only (default 8). "
                             "A reasoning model answers this question in ~97s, so a "
                             "sample large enough to separate 97%% from 90%% is hours "
                             "sequentially and minutes in parallel. Ignored for Claude, "
                             "which would just meet a rate limit.")
    parser.add_argument("--timeout", type=float, default=0,
                        help="per-call timeout in seconds, --base-url only. The "
                             "default one decides WHICH contexts get graded: a call "
                             "that runs long is one the model found hard, so cutting "
                             "it drops the hard contexts and grades the candidate on "
                             "the easy remainder. Raise it when the failure breakdown "
                             "is mostly timeouts.")
    parser.add_argument("--emit-pairs", action="store_true",
                        help="print the candidate's answers and the incumbent's to "
                             "stdout as {_side, line} records, over exactly the "
                             "contexts where both answered. Split by _side and feed "
                             "each to analysis/score_journal.py to ask which was "
                             "RIGHT -- agreement only says whether they are "
                             "interchangeable, and says nothing about the lines "
                             "where they were not. Printed rather than written "
                             "because replay/ must not open a file for writing: a "
                             "path argument aimed at the real journal would destroy "
                             "the record this whole harness reads.")
    parser.add_argument("--answered-by", type=str, default="",
                        help="replay only lines whose recorded answer came from this "
                             "model, as the API reported it (e.g. claude-opus-5). "
                             "Without it, a window straddling a model change grades "
                             "the candidate against two incumbents at once.")
    parser.add_argument("--days", type=str, default="",
                        metavar="FROM..TO",
                        help="replay only lines journalled on these UTC days, "
                             "inclusive, e.g. 2026-09-15..2026-09-22")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


def parse_days(spec: str) -> tuple[Optional[date], Optional[date]]:
    """``FROM..TO`` as two dates, either end optional; blank is no bound."""
    if not spec.strip():
        return None, None
    lo, sep, hi = spec.partition("..")
    if not sep:
        raise SystemExit(f"--days wants FROM..TO, got {spec!r}")
    try:
        first = date.fromisoformat(lo.strip()) if lo.strip() else None
        last = date.fromisoformat(hi.strip()) if hi.strip() else None
    except ValueError as exc:
        raise SystemExit(f"--days: {exc}") from exc
    if first and last and first > last:
        raise SystemExit(f"--days: {first} is after {last}")
    return first, last


def select_entries(
    entries: list, *, answered_by: str = "", first: Optional[date] = None,
    last: Optional[date] = None, limit: int = 0,
) -> list:
    """The recorded lines a run grades against, in journal order.

    Filters first, then keeps the most recent ``limit`` of what is left --
    so ``--answered-by claude-opus-5 --days 2026-09-15..2026-09-22`` is
    exactly the lines that model answered in that window, and a ``limit``
    at or above their number takes all of them. A line with no usable
    timestamp cannot be placed in a window and is dropped by one.
    """
    kept = []
    for entry in entries:
        if answered_by and entry.model != answered_by:
            continue
        if first or last:
            day = _day_of(entry.ts_utc)
            if day is None or (first and day < first) or (last and day > last):
                continue
        kept.append(entry)
    return kept[-limit:] if limit > 0 else kept


def _day_of(stamp: Optional[str]) -> Optional[date]:
    if not stamp:
        return None
    try:
        return date.fromisoformat(str(stamp)[:10])
    except ValueError:
        return None


#: The three calls, in the order a reader expects them.
MIX_ORDER = (("BULLISH", "LONG"), ("BEARISH", "SHORT"), ("NEUTRAL", "NEUTRAL"))


def bias_mix(cell: Cell) -> dict:
    """LONG / SHORT / NEUTRAL on both sides, over the lines both answered.

    Only lines where both produced a signal count, on either side: a mix
    over different lines would compare two samples, not two models. Also
    how many of the incumbent's SHORT lines the candidate called SHORT too,
    which is the number the owner's trigger (a) read. That trigger was a
    one-time check: it tripped and was closed on 2026-09-25 with the model
    kept, so a low number here is reported for reading and asks nobody to
    stop or revert.
    """
    both = [d for d in cell.diffs if d.before is not None and d.after is not None]
    incumbent = {label: 0 for _, label in MIX_ORDER}
    candidate = {label: 0 for _, label in MIX_ORDER}
    names = dict(MIX_ORDER)
    for d in both:
        incumbent[names[d.before.bias.value]] += 1
        candidate[names[d.after.bias.value]] += 1
    shorted = [d for d in both if d.before.bias.value == "BEARISH"]
    kept_short = sum(1 for d in shorted if d.after.bias.value == "BEARISH")
    agreed = sum(1 for d in both if not d.bias_flipped)
    return {
        "lines": len(both),
        "incumbent": incumbent,
        "candidate": candidate,
        "agreement": agreed / len(both) if both else None,
        "incumbent_shorts": len(shorted),
        "candidate_also_short": kept_short,
        "short_retention": kept_short / len(shorted) if shorted else None,
    }


def render_mix(cell: Cell, incumbent_name: str) -> list[str]:
    mix = bias_mix(cell)
    out = [
        "",
        f"CALL MIX ON THE SAME {mix['lines']} LINES (both answered)",
        "-" * 82,
        f"{'call':<10} {incumbent_name:>22} {cell.model:>26}",
    ]
    for _, label in MIX_ORDER:
        a, b = mix["incumbent"][label], mix["candidate"][label]
        pa = f"{a / mix['lines']:.0%}" if mix["lines"] else "n/a"
        pb = f"{b / mix['lines']:.0%}" if mix["lines"] else "n/a"
        out.append(f"{label:<10} {a:>15} ({pa:>4}) {b:>19} ({pb:>4})")
    agree = mix["agreement"]
    out.append(f"agreement on the call: {('%.1f%%' % (agree * 100)) if agree is not None else 'n/a'}")
    retention = mix["short_retention"]
    out.append(
        f"where {incumbent_name} said SHORT: {mix['candidate_also_short']} of "
        f"{mix['incumbent_shorts']} also SHORT from {cell.model}"
        + (f" ({retention:.0%})" if retention is not None else "")
    )
    if retention is not None:
        out.append(
            "  below a quarter (the owner's trigger (a), a one-time check, closed on "
            "2026-09-25 with the model kept)"
            if retention < 0.25 else
            "  at or above a quarter: trigger (a) not met"
        )
    costs = [u.cost_usd for u in cell.usages if u.cost_usd is not None]
    out.append(f"measured cost of this run: ${sum(costs):.2f} over {len(cell.usages)} priced call(s)")
    return out


def cells_to_probe(args: argparse.Namespace) -> list[tuple[str, str]]:
    if not args.only:
        return staircase_order()
    chosen = []
    for spec in args.only:
        model, _, effort = spec.partition(":")
        if not effort:
            raise SystemExit(f"--only wants MODEL:EFFORT, got {spec!r}")
        chosen.append((model, effort))
    return chosen


def run_cell(
    entries, model: str, effort: str, baseline_by_key: dict,
    base_url: str = "", api_key: str = "", workers: int = 1,
    timeout: float | None = None, emit_pairs: bool = False,
) -> Cell:
    complete, usages = runner.measured_completer(
        model=model, effort=effort, base_url=base_url, api_key=api_key,
        timeout=timeout,
    )
    # Per-ticker system prompts, not the one shared string: a fund is sent the
    # macro prompt trimmed to the sections it carried, and the recorded answer
    # this is graded against was produced that way. Asking a candidate a
    # different question than the baseline was asked is not a comparison.
    results = runner.replay_each(
        entries, runner.system_prompt_for_entry, complete, max_workers=workers
    )
    if emit_pairs:
        _print_pairs(results, usages)
    return Cell(
        model=model,
        effort=effort,
        usages=usages,
        diffs=[r.diff for r in results if r.error is None],
        errors=[r.error for r in results if r.error],
    )


def _print_pairs(results, usages) -> int:
    """Print the candidate's answers and the incumbent's, to stdout.

    Printed rather than written, because replay/ is forbidden from opening a
    file for writing and that rule is right: this tool runs often and
    casually while iterating, and an --emit-journal pointed at
    logs/signal_journal would destroy the only record of what the model
    actually said. Handing the lines to the caller removes the failure mode
    instead of guarding against it.

    Only contexts where BOTH produced a signal are printed, on either side. A
    candidate scored on more days than the incumbent is being compared on a
    different market rather than a different model, and the difference in
    realised return would then be partly that.
    """
    printed = 0
    for result, usage in zip(results, list(usages) + [None] * len(results)):
        if result.replayed is None or result.entry.original is None:
            continue
        for side, signal, used in (
            ("candidate", result.replayed, usage),
            ("incumbent", result.entry.original, None),
        ):
            print(json.dumps({
                "_side": side,
                "line": json.loads(runner.as_journal_line(result.entry, signal, used)),
            }))
        printed += 1
    print(f"printed {printed} paired context(s); split by _side and score each with "
          f"analysis/score_journal.py. Agreement says whether the two are "
          f"interchangeable; only realised returns say which was right where they "
          f"were not.", file=sys.stderr)
    return printed


def render(cells: list[Cell], floor: float, tickers: int, incumbent: Cell | None) -> str:
    out = [
        "MODEL / EFFORT COMPARISON",
        "=" * 82,
        f"Contexts per cell : {cells[0].n + len(cells[0].errors) if cells else 0}",
        f"Agreement floor   : {floor:.0%} (pre-registered)",
        f"Projected for     : {tickers} tickers, {cfg.CYCLES_PER_TRADING_DAY} cycle(s)/day",
        "",
        f"{'configuration':<26} {'$/call':>8} {'$/month':>9} {'agree':>7} "
        f"{'trade-agree':>12} {'out tok':>8} {'fail':>6}",
        "-" * 82,
    ]
    for cell in cells:
        verdict = clears_floor(cell, floor)
        mark = "  <- cheapest acceptable" if incumbent and cell is incumbent else (
            "" if verdict is not False else "  (below floor)"
        )
        per_call = cell.cost_per_call
        monthly = cell.monthly_usd(tickers)
        out.append(
            f"{cell.label:<26} "
            f"{('$%.4f' % per_call) if per_call is not None else 'n/a':>8} "
            f"{('$%.0f' % monthly) if monthly is not None else 'n/a':>9} "
            f"{(('%.0f%%' % (cell.bias_agreement * 100)) if cell.bias_agreement is not None else 'n/a'):>7} "
            f"{(('%.0f%%' % (cell.tradeable_agreement * 100)) if cell.tradeable_agreement is not None else 'n/a'):>12} "
            f"{('%.0f' % cell.mean_output_tokens) if cell.mean_output_tokens is not None else 'n/a':>8} "
            f"{cell.failure_rate:>5.0%}"
            f"{mark}"
        )

    for cell in cells:
        if cell.errors:
            out += ["", f"why {len(cell.errors)} call(s) failed in {cell.label}:"]
            out += [f"  {n:>4}  {kind}" for kind, n in error_kinds(cell.errors)]
    out += ["", "HOW TO READ THIS", "-" * 82]
    out += [
        "trade-agree is the number that matters: the share of contexts where this",
        "cell and the incumbent agreed on whether to trade at all. A signal that",
        f"matches on direction but lands the other side of MIN_CONVICTION",
        f"({cfg.MIN_CONVICTION:.2f}) produces a different portfolio.",
        "",
        "out tok is mean output tokens. Output bills at ~5x input here, so it is",
        "where the money goes and effort is the lever that moves it.",
        "",
        "LIMITS",
        "-" * 82,
        "Agreement is not correctness. A cell that matches the incumbent 100% of",
        "the time is interchangeable *with the incumbent*, which only helps if the",
        "incumbent was right -- and nothing here knows that. Only",
        "analysis/score_journal.py, against realised returns, can say whether any",
        "configuration produces signals worth trading.",
        "",
        "Each cell starts with a cold cache (the cache is per model, and effort is",
        "part of its key), so these costs are an upper bound on steady state.",
    ]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.tickers <= 0:
        from config.settings import get_settings
        args.tickers = len(get_settings().watchlist_tickers)
    plan = cells_to_probe(args)

    if args.dry_run:
        print(f"Would probe {len(plan)} cells x {args.limit} contexts "
              f"= {len(plan) * args.limit} model calls.")
        for model, effort in plan:
            print(f"  {model} / {effort}")
        print("\nStaircase: enter top-left, step down on a pass, right on a fail.")
        print("Use --only MODEL:EFFORT to probe one cell.")
        return 0

    if not args.journal.exists():
        print(f"No journal at {args.journal}. Run some cycles first -- this "
              f"compares configurations on real recorded context.", file=sys.stderr)
        return 1

    lines = args.journal.read_text(encoding="utf-8").splitlines()
    first, last = parse_days(args.days)
    entries = select_entries(
        list(runner.load_entries(lines)), answered_by=args.answered_by,
        first=first, last=last, limit=args.limit,
    )
    if not entries:
        print("No replayable entries found.", file=sys.stderr)
        return 1

    print(f"Probing {len(plan)} cells x {len(entries)} contexts "
          f"= {len(plan) * len(entries)} model calls...", file=sys.stderr)

    cells: list[Cell] = []
    incumbent: Cell | None = None
    for model, effort in plan:
        # Concurrency only against an endpoint we chose to point at. The
        # Claude path would be firing a whole journal at a rate limit, and a
        # rate-limited context is a lost one where a slow one is only slow.
        workers = args.concurrency if args.base_url else 1
        cell = run_cell(entries, model, effort, {}, args.base_url, args.api_key,
                        workers, args.timeout or None, args.emit_pairs)
        cells.append(cell)
        if clears_floor(cell, args.floor) and (
            incumbent is None
            or (cell.cost_per_call or float("inf")) < (incumbent.cost_per_call or float("inf"))
        ):
            incumbent = cell

    if args.as_json:
        print(json.dumps({
            "floor": args.floor,
            "tickers": args.tickers,
            "cells": [
                {
                    "model": c.model, "effort": c.effort, "n": c.n,
                    "cost_per_call_usd": c.cost_per_call,
                    "monthly_usd": c.monthly_usd(args.tickers),
                    "bias_agreement": c.bias_agreement,
                    "tradeable_agreement": c.tradeable_agreement,
                    "mean_output_tokens": c.mean_output_tokens,
                    "clears_floor": clears_floor(c, args.floor),
                    "failures": len(c.errors),
                    "mix": bias_mix(c),
                }
                for c in cells
            ],
            "cheapest_acceptable": incumbent.label if incumbent else None,
        }, indent=2))
    else:
        # With --emit-pairs, stdout carries the records and nothing else:
        # mixing a human report into the stream the caller is about to split
        # would corrupt it. Diagnostics go to stderr, which is where the rest
        # of this tool's progress already goes.
        report = render(cells, args.floor, args.tickers, incumbent)
        incumbent_name = args.answered_by or "recorded"
        for cell in cells:
            report += "\n" + "\n".join(render_mix(cell, incumbent_name))
        print(report, file=sys.stderr if args.emit_pairs else sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
