#!/usr/bin/env python3
"""How much of a model's disagreement with another model is just noise?

    python replay/determinism_check.py --limit 30 --repeats 5 \
        --model claude-opus-5 --effort low

    python replay/determinism_check.py --limit 30 --repeats 5 \
        --base-url https://api.deepinfra.com/v1/openai \
        --model openai/gpt-oss-120b --effort high --api-key "$KEY"

compare_models.py measures agreement between two DIFFERENT configurations
on the same recorded contexts. This measures agreement between ONE
configuration and ITSELF: the same context, the identical question, asked
``--repeats`` times in a row. A model that changes its own answer to a
question nobody changed is not comparable to a different model at all --
an 82% trade-agreement number from a substitution run has to be read
against this baseline, or a candidate that is simply noisier than the
incumbent looks exactly like one that disagrees with it.

Same guarantees as the rest of replay/: it reads the journal, calls the
model, and prints. No broker keys, no journal write, no order path.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.schemas import Bias  # noqa: E402
from config import settings as cfg  # noqa: E402
from replay import runner  # noqa: E402
from replay.runner import ReplayResult  # noqa: E402

DEFAULT_LIMIT = 30
DEFAULT_REPEATS = 5


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Repeat the same contexts through one configuration and measure self-agreement."
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument(
        "--limit", type=int, default=DEFAULT_LIMIT,
        help="distinct contexts to test (default %(default)s). Total calls = limit x repeats.",
    )
    parser.add_argument(
        "--repeats", type=int, default=DEFAULT_REPEATS,
        help="times each context is asked (default %(default)s)",
    )
    parser.add_argument("--floor", type=float, default=cfg.MIN_CONVICTION,
                        help="conviction floor a 'would trade' verdict is judged against "
                             "(default: the engine's %(default)s)")
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", default=None)
    parser.add_argument("--base-url", default="",
                        help="ask an OpenAI-compatible endpoint instead of Claude, "
                             "e.g. https://api.deepinfra.com/v1/openai")
    parser.add_argument("--api-key", default="", help="bearer token for --base-url, if it wants one")
    parser.add_argument("--concurrency", type=int, default=4,
                        help="calls in flight at once, --base-url only (default %(default)s). "
                             "Ignored for Claude, which would just meet a rate limit.")
    parser.add_argument("--timeout", type=float, default=0, help="per-call timeout in seconds")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


@dataclass(frozen=True)
class ContextStability:
    """One context, asked the same question ``n_repeats`` times."""

    ticker: str
    n_repeats: int
    n_answered: int
    #: Distinct bias VALUES seen among the answers that came back.
    directions: frozenset
    #: Distinct trade/no-trade verdicts seen (bias != NEUTRAL and conviction
    #: at or above the floor). Two answers can agree on direction and still
    #: disagree here, on either side of the floor.
    would_trade: frozenset
    #: max - min conviction among the answers that came back, or None with
    #: fewer than two.
    conviction_spread: Optional[float]

    @property
    def assessable(self) -> bool:
        """Fewer than two answers cannot be said to agree or disagree."""
        return self.n_answered >= 2

    @property
    def direction_unanimous(self) -> bool:
        return len(self.directions) <= 1

    @property
    def trade_decision_unanimous(self) -> bool:
        return len(self.would_trade) <= 1


def context_stability(ticker: str, group: list[ReplayResult], floor: float) -> ContextStability:
    answered = [r.replayed for r in group if r.replayed is not None]
    convictions = [s.conviction for s in answered]
    return ContextStability(
        ticker=ticker,
        n_repeats=len(group),
        n_answered=len(answered),
        directions=frozenset(s.bias.value for s in answered),
        would_trade=frozenset(s.bias != Bias.NEUTRAL and s.conviction >= floor for s in answered),
        conviction_spread=(max(convictions) - min(convictions)) if len(convictions) >= 2 else None,
    )


def render(stabilities: list[ContextStability], floor: float, repeats: int, label: str) -> str:
    total_calls = sum(s.n_repeats for s in stabilities)
    total_answered = sum(s.n_answered for s in stabilities)
    assessable = [s for s in stabilities if s.assessable]

    lines = [
        "SELF-AGREEMENT: SAME CONTEXT, SAME MODEL, ASKED AGAIN",
        "=" * 78,
        f"Configuration : {label}",
        f"Contexts      : {len(stabilities)}, each asked {repeats} time(s) "
        f"({total_calls} calls total)",
        f"Failure rate  : {total_calls - total_answered}/{total_calls} calls "
        f"({(total_calls - total_answered) / total_calls:.0%})" if total_calls else "n/a",
        "",
    ]
    if not assessable:
        lines.append(
            f"Fewer than 2 of {repeats} repeats answered for every context -- "
            "nothing here can be judged as stable or not."
        )
        return "\n".join(lines)

    direction_stable = sum(1 for s in assessable if s.direction_unanimous)
    trade_stable = sum(1 for s in assessable if s.trade_decision_unanimous)
    spreads = [s.conviction_spread for s in assessable if s.conviction_spread is not None]

    lines += [
        f"Assessable contexts (>=2 of {repeats} repeats answered): {len(assessable)}",
        "",
        f"Direction unanimous across every repeat      : {direction_stable}/{len(assessable)} "
        f"({direction_stable / len(assessable):.0%})",
        f"Trade decision unanimous across every repeat : {trade_stable}/{len(assessable)} "
        f"({trade_stable / len(assessable):.0%})  "
        f"<- bias != NEUTRAL and conviction >= {floor:.2f}, both repeats",
    ]
    if spreads:
        lines.append(f"Mean conviction spread (max-min) per context : {statistics.fmean(spreads):.3f}")

    lines += [
        "",
        "HOW TO READ THIS",
        "-" * 78,
        "This is the floor a substitution comparison's disagreement rate has to",
        "clear before it means anything on its own. If this configuration",
        "disagrees with ITSELF on some share of contexts, part of whatever",
        "compare_models.py reports as disagreement between two DIFFERENT models",
        "is noise neither model can be blamed for -- not evidence one is wrong.",
        "",
        "LIMITS",
        "-" * 78,
        "A context that answered fewer than twice is excluded, not counted as",
        "stable -- the same reasoning MIN_TRADES/MIN_SAMPLE convention as the",
        "rest of this package: absence of disagreement is not evidence of",
        "agreement when there was barely a chance to disagree.",
        "",
        "This cannot say WHY an answer flipped -- sampling temperature,",
        "provider-side batching, and a genuinely borderline context all produce",
        "the same symptom here. It can only say how often it happens.",
    ]
    return "\n".join(lines)


def as_json(stabilities: list[ContextStability], floor: float, repeats: int, label: str) -> dict:
    assessable = [s for s in stabilities if s.assessable]
    spreads = [s.conviction_spread for s in assessable if s.conviction_spread is not None]
    return {
        "configuration": label,
        "floor": floor,
        "repeats": repeats,
        "contexts": len(stabilities),
        "assessable_contexts": len(assessable),
        "total_calls": sum(s.n_repeats for s in stabilities),
        "answered_calls": sum(s.n_answered for s in stabilities),
        "direction_unanimous_rate": (
            sum(1 for s in assessable if s.direction_unanimous) / len(assessable)
            if assessable else None
        ),
        "trade_decision_unanimous_rate": (
            sum(1 for s in assessable if s.trade_decision_unanimous) / len(assessable)
            if assessable else None
        ),
        "mean_conviction_spread": statistics.fmean(spreads) if spreads else None,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.repeats < 2:
        print("--repeats must be at least 2: one answer cannot disagree with itself.", file=sys.stderr)
        return 2
    if not args.journal.exists():
        print(f"No journal at {args.journal}.", file=sys.stderr)
        return 1

    lines = args.journal.read_text(encoding="utf-8").splitlines()
    entries = list(runner.load_entries(lines))[-args.limit:]
    if not entries:
        print("No replayable entries found.", file=sys.stderr)
        return 1

    complete, _usages = runner.measured_completer(
        # A workflow_dispatch input with no value arrives as "", not absent --
        # normalised here so it means the same thing as leaving --effort off.
        model=args.model, effort=args.effort or None, base_url=args.base_url,
        api_key=args.api_key, timeout=args.timeout or None,
    )
    # Concurrency only against an endpoint we chose to point at -- the Claude
    # path would be firing the same rate limit compare_models.py avoids.
    workers = args.concurrency if args.base_url else 1
    repeated = [entry for entry in entries for _ in range(args.repeats)]
    print(
        f"Asking {len(entries)} context(s) x {args.repeats} repeat(s) "
        f"= {len(repeated)} calls...", file=sys.stderr,
    )
    results = runner.replay_each(
        repeated, runner.system_prompt_for_entry, complete, max_workers=workers,
    )

    stabilities = [
        context_stability(
            entries[i].ticker,
            results[i * args.repeats:(i + 1) * args.repeats],
            args.floor,
        )
        for i in range(len(entries))
    ]

    label = f"{args.model} / {args.effort}" if args.effort else args.model
    if args.as_json:
        print(json.dumps(as_json(stabilities, args.floor, args.repeats, label), indent=2))
    else:
        print(render(stabilities, args.floor, args.repeats, label))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
