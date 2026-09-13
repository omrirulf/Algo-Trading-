"""Score the signal journal against what the market actually did.

    python analysis/score_journal.py
    python analysis/score_journal.py --horizon 5 --entry next
    python analysis/score_journal.py --json > scores.json

Read-only in every direction: it opens the journal, fetches price history, and
prints. It holds no broker keys, touches no order path, and cannot write to the
journal it is reading.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict
from pathlib import Path

# Allow ``python analysis/score_journal.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import metrics, report  # noqa: E402
from analysis.reader import SCORE_FIELDS, read_journal  # noqa: E402
from analysis.returns import ENTRY_AUTO, ENTRY_RULES, YFinancePriceSource  # noqa: E402
from analysis.scoring import build_run  # noqa: E402
from config import settings as cfg  # noqa: E402

DEFAULT_HORIZON = 3

log = logging.getLogger("score_journal")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="score_journal",
        description="Join journalled signals to realised returns and report.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--journal",
        type=Path,
        default=cfg.SIGNAL_JOURNAL_PATH,
        help="path to the signal journal (default: %(default)s)",
    )
    parser.add_argument(
        "--horizon",
        type=int,
        default=DEFAULT_HORIZON,
        help="trading sessions held after entry (default: %(default)s)",
    )
    parser.add_argument(
        "--entry",
        choices=ENTRY_RULES,
        default=ENTRY_AUTO,
        help=(
            "which close to enter at: 'auto' uses the same session when the signal "
            "fired before the close, 'next' always waits a session, 'same' always "
            "uses the signal date (default: %(default)s)"
        ),
    )
    parser.add_argument(
        "--floor",
        type=float,
        default=cfg.MIN_CONVICTION,
        help="conviction floor to evaluate (default: the engine's %(default)s)",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of a report")
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

    try:
        read = read_journal(args.journal)
    except FileNotFoundError:
        print(
            f"No journal at {args.journal}.\n"
            "The orchestrator writes one entry per ticker per cycle; run it first.",
            file=sys.stderr,
        )
        return 1

    if not read.entries:
        print(f"{args.journal} has no usable entries.", file=sys.stderr)
        return 1

    run = build_run(
        read=read,
        source=YFinancePriceSource(),
        horizon=args.horizon,
        floor=args.floor,
        entry_rule=args.entry,
    )

    print(json.dumps(as_json(run), indent=2) if args.json else report.render(run))
    return 0


def as_json(run) -> dict:
    """Machine-readable form, for feeding a notebook rather than a terminal."""
    correlations = metrics.dimension_correlations(run.signals)
    agreement = metrics.agreement_check(run.entries)
    drift = metrics.conviction_drift(run.entries, run.floor)
    with_gaps, gap_kinds = metrics.gap_summary(run.entries)

    return {
        "horizon": run.horizon,
        "entry_rule": run.entry_rule,
        "floor": run.floor,
        "coverage": {
            "lines": run.read.total_lines,
            "skipped": run.read.skipped,
            "entries": len(run.entries),
            "with_signal": len(run.with_signal),
            "directional": len(run.directional),
            "scored": len(run.signals),
            "statuses": dict(run.statuses),
        },
        "conviction_vs_outcome": asdict(metrics.conviction_vs_outcome(run.signals)),
        "buckets": [asdict(b) for b in metrics.conviction_buckets(run.signals)],
        "floor_check": asdict(metrics.floor_check(run.signals, run.floor)),
        "dimensions": {
            name: asdict(correlations[name]) for name in SCORE_FIELDS
        },
        "agreement": {
            "aligned_n": agreement.aligned_n,
            "aligned_mean_conviction": agreement.aligned_mean_conviction,
            "conflicted_n": agreement.conflicted_n,
            "conflicted_mean_conviction": agreement.conflicted_mean_conviction,
            "gap": agreement.gap,
            "dispersion_vs_conviction": asdict(agreement.dispersion_vs_conviction),
        },
        "drift": {
            "first_n": drift.first_n,
            "first_mean": drift.first_mean,
            "second_n": drift.second_n,
            "second_mean": drift.second_mean,
            "change": drift.change,
            "daily": [
                {"date": day.isoformat(), "n": n, "mean_conviction": mean}
                for day, n, mean in drift.daily
            ],
        },
        "health": {
            "cycles_with_gaps": with_gaps,
            "gap_kinds": dict(gap_kinds),
            "bias": dict(metrics.bias_distribution(run.entries)),
        },
        "min_sample_for_confidence": report.MIN_SAMPLE,
    }


if __name__ == "__main__":
    raise SystemExit(main())
