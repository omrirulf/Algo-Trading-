#!/usr/bin/env python3
"""Compare a candidate screening model against the production Haiku screen.

    # Dry run: how many recorded lines actually have a screen to compare against
    python replay/compare_screening.py --limit 50 --dry-run

    # A local Ollama model
    python replay/compare_screening.py --base-url http://localhost:11434/v1 \\
        --model qwen2.5:14b --limit 50

    # A hosted free/cheap tier
    python replay/compare_screening.py --base-url https://api.groq.com/openai/v1 \\
        --model llama-3.1-8b-instant --api-key "$GROQ_API_KEY" --limit 50

This asks a *narrower* question than ``compare_models.py``: not "which Claude
tier is cheapest" but "does this specific endpoint, asked exactly as the
screening stage asks Haiku, agree with what Haiku actually said" -- on the
same recorded contexts, with the same system prompt each ticker really got,
and the same ``reasoning=False`` the funnel always sends the screen.

The baseline is the recorded *screen*, not the recorded final signal. On a
line the screen escalated, those are different answers -- the screen's own
NEUTRAL-or-not call versus the full model's directional one -- and grading a
screening candidate against the full model would be grading it on a question
production never put to it. A line with no recorded screen (screening was
off, or the screen itself errored that day) has nothing honest to compare
against and is skipped, not silently treated as a pass.

Agreement is reported, and so is a second, stricter number: escalation
*recall* -- of the lines where Haiku's screen was directional, the share the
candidate also called directional. The two errors an agreement floor treats
alike are not alike in cost. A candidate that quietly turns a tradeable name
NEUTRAL costs a trade production's funnel can never recover, because the full
model is never asked about a NEUTRAL screen. A candidate that escalates a
name Haiku would have screened out costs one avoidable full-model call. A
symmetric floor can pass a candidate that is quietly turning winners into
NEUTRAL as long as it makes up the percentage elsewhere; recall cannot be
fooled that way, which is why it -- not trade agreement -- is what gates the
verdict below.

Like ``compare_models.py``, this has no path to the execution engine and
tells you agreement and cost, never correctness -- see that module's
docstring for why, and ``analysis/score_journal.py`` for the only tool that
can speak to realised returns.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.schemas import Bias  # noqa: E402
from config import settings as cfg  # noqa: E402
from orchestrator.llm import AnthropicSignalProvider, OpenAICompatibleProvider  # noqa: E402
from replay import runner  # noqa: E402
from replay.compare import SignalDiff  # noqa: E402
from replay.compare_configs import Cell, clears_floor  # noqa: E402

#: Same pre-registered bar ``compare_models.py`` uses, for the same reason:
#: a floor read off the results afterwards is a story fitted to them, not
#: evidence. There is nothing screening-specific that would justify a
#: different number.
DEFAULT_FLOOR = 0.90

#: What share of Haiku's directional calls the candidate must also escalate.
#: Set apart from, and higher than, DEFAULT_FLOOR: a missed escalation is a
#: silently lost trade, not a merely different one, so this is the number
#: that gates the verdict -- see the module docstring for why the two are not
#: interchangeable.
DEFAULT_RECALL_FLOOR = 0.95

#: Below this many compared lines, a passing number is not yet evidence. At
#: 45/50 (90%) the 95% confidence interval is roughly 78-96% -- wide enough
#: to certify nothing. This is a printed warning, not a refusal: a small
#: sample is still the right first look, just not the last one.
MIN_TRUSTWORTHY_SAMPLE = 100


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare a candidate screening endpoint against the recorded Haiku screen."
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--limit", type=int, default=200,
                        help="most recent journal lines to consider (default 200 -- "
                             "raised from an earlier 50, which cannot actually certify "
                             "a 90%% floor: at 45/50 the 95%% confidence interval is "
                             "roughly 78-96%%). Lines with no recorded screen are "
                             "skipped, not padded back in.")
    parser.add_argument("--base-url", type=str, default="",
                        help="OpenAI-compatible base URL, e.g. http://localhost:11434/v1. "
                             "Required unless --dry-run.")
    parser.add_argument("--model", type=str, default="",
                        help="Model name to ask that endpoint for. Required unless --dry-run.")
    parser.add_argument("--effort", choices=("low", "medium", "high"), default=None,
                        help="ask the candidate WITH reasoning on, at this effort. "
                             "Off by default, because the production screen is asked "
                             "with reasoning off and that is what a candidate has to "
                             "be graded against. Use it to separate 'this model is "
                             "weak' from 'the cheap setting crippled it' -- a "
                             "reasoning model has no true off switch, so the screen's "
                             "reasoning_effort=low is a real handicap. A result from "
                             "this is a PROPOSAL for what the screen would have to "
                             "become, not a measurement of what it does now, and the "
                             "header says so.")
    parser.add_argument("--api-key", type=str, default="",
                        help="Bearer token for --base-url, if it wants one.")
    parser.add_argument("--floor", type=float, default=DEFAULT_FLOOR,
                        help=f"trade agreement the candidate must clear (default {DEFAULT_FLOOR}). "
                             "Reported, but recall -- below -- is what gates the verdict.")
    parser.add_argument("--recall-floor", type=float, default=DEFAULT_RECALL_FLOOR,
                        help=f"share of Haiku's directional calls the candidate must also "
                             f"escalate (default {DEFAULT_RECALL_FLOOR}). A miss here is a "
                             f"silently lost trade, not just a different one -- see the "
                             f"module docstring.")
    parser.add_argument("--tickers", type=int, default=0,
                        help="watchlist size to project a monthly bill for "
                             "(default: however many are configured)")
    parser.add_argument("--show-diffs", action="store_true",
                        help="print every consequential disagreement (bias flip or floor crossing)")
    parser.add_argument("--dry-run", action="store_true",
                        help="report how many recorded lines have a comparable screen; make no calls")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


def _comparable_entries(journal: Path, limit: int) -> tuple[list, int]:
    """Loaded entries that have a recorded screen to compare against, and a skip count."""
    if not journal.exists():
        print(f"No journal at {journal}. Run some cycles first -- this compares "
              f"against real recorded screens.", file=sys.stderr)
        raise SystemExit(1)
    lines = journal.read_text(encoding="utf-8").splitlines()
    loaded = list(runner.load_entries(lines))[-limit:]
    comparable = [e for e in loaded if runner.recorded_screen_signal(e) is not None]
    return comparable, len(loaded) - len(comparable)


def escalation_recall(diffs: list[SignalDiff]) -> tuple[float | None, int, int]:
    """Of Haiku's directional calls, the share the candidate also escalated.

    Returns ``(recall, recalled, haiku_escalated)``. ``None`` when Haiku never
    escalated on any compared line -- there is nothing to have missed, and
    reporting 100% would flatter a candidate that was never actually tested
    against this failure mode.

    A candidate that answered ``NEUTRAL`` counts as a miss here exactly like
    one that never answered at all would -- but a candidate that *errored* on
    this line never reaches this function, because ``run()`` never builds a
    diff for an errored call. That asymmetry is deliberate: an error falls
    through to the full model in production (``apply_screen`` catches it and
    asks anyway), so it costs one call, not a trade -- the same as an
    incumbent Haiku screen that errors today. It belongs in ``failure_rate``,
    not here.
    """
    haiku_escalated = [
        d for d in diffs if d.before is not None and d.before.bias is not Bias.NEUTRAL
    ]
    if not haiku_escalated:
        return None, 0, 0
    recalled = sum(
        1 for d in haiku_escalated if d.after is not None and d.after.bias is not Bias.NEUTRAL
    )
    return recalled / len(haiku_escalated), recalled, len(haiku_escalated)


def _incumbent_reference_cost(entries: list) -> tuple[float | None, int]:
    """What the recorded Haiku screen itself cost over these same lines.

    Not a call this tool makes -- read straight from what the journal already
    recorded -- so it costs nothing to show and grounds the candidate's
    number against the incumbent it is being compared to, not just against
    zero.
    """
    costs = []
    for entry in entries:
        usage = (entry.recorded_screen or {}).get("usage") or {}
        cost = usage.get("cost_usd")
        if isinstance(cost, (int, float)):
            costs.append(cost)
    return (sum(costs) / len(costs) if costs else None), len(costs)


def run(args: argparse.Namespace) -> int:
    entries, skipped = _comparable_entries(args.journal, args.limit)
    if not entries:
        print("No journal lines with a recorded screen to compare against. "
              "SCREENING_ENABLED may be off, or the journal is too young.", file=sys.stderr)
        return 1

    if args.tickers <= 0:
        from config.settings import get_settings
        args.tickers = len(get_settings().watchlist_tickers)

    incumbent_cost, incumbent_n = _incumbent_reference_cost(entries)

    if args.dry_run:
        print(f"{len(entries)} of {len(entries) + skipped} recent journal lines have a "
              f"recorded screen to compare against ({skipped} skipped: no screen recorded).")
        print(f"Would call the candidate {len(entries)} times, reasoning off, "
              f"the exact system prompt each ticker was actually sent.")
        if incumbent_cost is not None:
            print(f"For reference, the recorded Haiku screen cost ${incumbent_cost:.5f}/call "
                  f"over these {incumbent_n} lines (${incumbent_cost * args.tickers * cfg.CYCLES_PER_TRADING_DAY * 21:.2f}/month at {args.tickers} tickers).")
        return 0

    if not args.base_url or not args.model:
        print("--base-url and --model are required (or pass --dry-run).", file=sys.stderr)
        return 2

    provider = OpenAICompatibleProvider(base_url=args.base_url, model=args.model, api_key=args.api_key)
    complete, usages = runner.screening_candidate_completer(provider, args.model, args.effort)

    diffs: list[SignalDiff] = []
    errors: list[str] = []
    print(f"Asking the candidate for {len(entries)} lines ({skipped} skipped: "
          f"no recorded screen to compare against)...", file=sys.stderr)
    for entry in entries:
        result = runner.replay_one(entry, runner.system_prompt_for_entry(entry), complete)
        if result.error is not None:
            errors.append(result.error)
            continue
        diffs.append(SignalDiff(
            ticker=entry.ticker,
            before=runner.recorded_screen_signal(entry),
            after=result.replayed,
        ))

    cell = Cell(model=args.model, effort=args.effort or "screen", usages=usages, diffs=diffs, errors=errors)
    agreement_verdict = clears_floor(cell, args.floor)
    recall, recalled, haiku_escalated = escalation_recall(diffs)
    recall_verdict = None if recall is None else recall >= args.recall_floor
    # Recall gates the overall verdict; trade agreement is reported beside it
    # but a candidate cannot pass on agreement alone -- see the module
    # docstring for why the two errors it lumps together are not alike in cost.
    verdict = recall_verdict if recall_verdict is not None else agreement_verdict
    small_sample = cell.n < MIN_TRUSTWORTHY_SAMPLE

    if args.show_diffs:
        for diff in diffs:
            if diff.consequential:
                print(diff.summary())

    if args.as_json:
        print(json.dumps({
            "model": args.model,
            "base_url": args.base_url,
            "floor": args.floor,
            "recall_floor": args.recall_floor,
            "n": cell.n,
            "small_sample": small_sample,
            "skipped_no_baseline": skipped,
            "bias_agreement": cell.bias_agreement,
            "tradeable_agreement": cell.tradeable_agreement,
            "clears_floor": agreement_verdict,
            "escalation_recall": recall,
            "escalation_recall_n": haiku_escalated,
            "clears_recall_floor": recall_verdict,
            "failure_rate": cell.failure_rate,
            "verdict_pass": verdict,
            "candidate_cost_per_call_usd": cell.cost_per_call,
            "candidate_monthly_usd": cell.monthly_usd(args.tickers),
            "incumbent_haiku_cost_per_call_usd": incumbent_cost,
        }, indent=2))
        return 0

    print()
    print("SCREENING CANDIDATE VS THE RECORDED HAIKU SCREEN")
    print("=" * 72)
    print(f"Candidate         : {args.model}  ({args.base_url})")
    if args.effort:
        print(f"Asked with        : reasoning ON at effort={args.effort}  <- NOT how the "
              f"screen asks today")
        print( "                    A pass here is a proposal to change the screen, not")
        print( "                    a green light for the current configuration.")
    else:
        print( "Asked with        : reasoning off (exactly as the cycle asks the screen)")
    print(f"Lines compared    : {cell.n}  ({skipped} skipped: no recorded screen)")
    if small_sample:
        print(f"                    ** fewer than {MIN_TRUSTWORTHY_SAMPLE} lines -- "
              f"a passing number here is a first look, not evidence yet **")
    print(f"Bias agreement    : {_pct(cell.bias_agreement)}")
    print(f"Trade agreement   : {_pct(cell.tradeable_agreement)}  (reported for reference; "
          f"see escalation recall below for the number that gates the verdict)")
    print(f"Escalation recall : {_pct(recall)}  of {haiku_escalated} line(s) Haiku escalated, "
          f"the candidate also escalated {recalled}  <- THE NUMBER THAT MATTERS")
    print(f"Failure rate      : {cell.failure_rate:.0%}  (bad JSON, unreachable, etc. -- "
          f"in production this falls through to the full model, never a bad trade)")
    print(f"Candidate cost    : {_usd(cell.cost_per_call)}/call, "
          f"{_usd(cell.monthly_usd(args.tickers))}/month at {args.tickers} tickers")
    if incumbent_cost is not None:
        print(f"Haiku screen cost : {_usd(incumbent_cost)}/call, for reference")
    print()
    if verdict is None:
        print("VERDICT: unknown -- nothing comparable came back.")
    elif verdict:
        print(f"VERDICT: clears the {args.recall_floor:.0%} escalation-recall floor. Safe to "
              f"point SCREENING_BASE_URL/SCREENING_MODEL at this in production"
              f"{' once the sample is larger' if small_sample else ''}.")
    else:
        print(f"VERDICT: below the {args.recall_floor:.0%} escalation-recall floor -- this "
              f"candidate is quietly turning some of Haiku's tradeable calls into NEUTRAL. "
              f"Do not flip this on.")
    print()
    print("LIMITS")
    print("-" * 72)
    print("Agreement with Haiku is not correctness -- it says this candidate would")
    print("make the same funnel decisions Haiku did, not that either was right.")
    print("A high failure rate silently reverts every one of those lines to the full")
    print("model, which erases the saving without ever risking a bad trade. Recall only")
    print("sees a candidate that answered; it cannot see a false-NEUTRAL production would")
    print("have made on a line no recorded screen exists for.")
    return 0


def _pct(value: float | None) -> str:
    return f"{value:.0%}" if value is not None else "n/a"


def _usd(value: float | None) -> str:
    return f"${value:.5f}" if value is not None else "n/a (unpriced model)"


def main(argv: list[str] | None = None) -> int:
    return run(parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
