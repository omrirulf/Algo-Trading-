#!/usr/bin/env python3
"""Re-ask the model the questions it has already been asked.

    # See what the model was actually shown, without spending a token
    python replay/replay_journal.py --dry-run --limit 3

    # Re-ask with the current prompt (a consistency check)
    python replay/replay_journal.py --limit 20

    # Re-ask with a changed prompt -- the point of the tool
    python replay/replay_journal.py --system-prompt prompts/v2.txt --limit 20

Every run costs one model call per entry, so ``--limit`` defaults to something
small and the run prints its cost up front. ``--dry-run`` costs nothing and is
the right first move after any prompt edit.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from replay import runner  # noqa: E402
from replay.compare import ReplaySummary  # noqa: E402

DEFAULT_LIMIT = 10


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replay journalled contexts against the model.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
                        help="journal file to read (default: the configured one)")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                        help=f"how many entries to replay, newest first (default: {DEFAULT_LIMIT})")
    parser.add_argument("--ticker", help="only replay this ticker")
    parser.add_argument("--system-prompt", type=Path,
                        help="file holding the system prompt to try (default: the live one)")
    parser.add_argument("--dry-run", action="store_true",
                        help="rebuild and print the prompts; make no model calls")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="machine-readable output")
    parser.add_argument("--verbose", action="store_true", help="show every entry, not just changes")
    return parser.parse_args(argv)


def load_system_prompt(path: Path | None) -> tuple[str, str]:
    if path is None:
        return runner.SYSTEM_PROMPT, "the live prompt"
    return path.read_text(encoding="utf-8"), str(path)


def render(summary: ReplaySummary, results: list, source: str, verbose: bool) -> str:
    out = [
        "REPLAY REPORT",
        "=" * 60,
        f"System prompt : {source}",
        f"Replayed      : {summary.n} of {len(results)} entries"
        + (f" ({len(results) - summary.n} errored)" if len(results) != summary.n else ""),
        "",
    ]

    if summary.n == 0:
        out.append("Nothing to compare. Every entry failed to replay -- see the errors below.")
    else:
        out += [
            "WHAT WOULD CHANGE",
            "-" * 60,
            f"Consequential changes : {len(summary.consequential)} of {summary.n}",
            f"  bias flips          : {summary.bias_flips}",
            f"  floor crossings     : {summary.floor_crossings}"
            f"   (the {cfg.MIN_CONVICTION:.2f} threshold the engine actually uses)",
            "",
        ]
        drift = summary.conviction_drift_direction
        mean = summary.mean_conviction_delta
        if mean is not None:
            line = f"Mean conviction change: {mean:+.3f}"
            if drift:
                line += f" -- the new prompt is systematically {drift}"
            out.append(line)
            if drift:
                out.append(
                    "  A uniform shift is not better calibration; it just moves"
                )
                out.append(
                    f"  signals across the {cfg.MIN_CONVICTION:.2f} floor."
                )
            out.append("")

        shown = summary.consequential if not verbose else summary.diffs
        if shown:
            out += ["CHANGES", "-" * 60]
            out += [f"  {d.summary()}" for d in shown]
            out.append("")
        elif not verbose:
            out += ["No change that would alter what the engine does.", ""]

    errors = [r for r in results if r.error]
    if errors:
        out += ["ERRORS", "-" * 60]
        out += [f"  {r.entry.ticker}: {r.error}" for r in errors]
        out.append("")

    out += [
        "NOTE",
        "-" * 60,
        "Replayed context is real -- it is what the model was shown at the time.",
        "The comparison is against that cycle's answer, not against the market:",
        "a prompt that changes many signals is not thereby a better prompt.",
        "Use analysis/score_journal.py to ask whether signals were any good.",
    ]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    args = parse_args(argv)

    if not args.journal.exists():
        print(f"No journal at {args.journal}. Run some cycles first.", file=sys.stderr)
        return 1

    lines = args.journal.read_text(encoding="utf-8").splitlines()
    entries = list(runner.load_entries(lines, ticker=args.ticker))
    if not entries:
        print("No replayable entries found.", file=sys.stderr)
        return 1

    entries = entries[-args.limit:] if args.limit > 0 else entries
    system_prompt, source = load_system_prompt(args.system_prompt)

    if args.dry_run:
        for entry in entries:
            print("=" * 70)
            print(f"{entry.ticker}  {entry.ts_utc or 'no timestamp'}")
            was = entry.original
            print(f"answered: {was.bias.value} {was.conviction:.2f}" if was else "answered: no signal")
            print("-" * 70)
            print(entry.prompt)
            print()
        print(f"{len(entries)} {'entry' if len(entries) == 1 else 'entries'}. No model calls made.")
        return 0

    print(f"Replaying {len(entries)} entries against {source} "
          f"({len(entries)} model calls)...", file=sys.stderr)
    results = runner.replay_all(entries, system_prompt, runner.default_completer())
    summary = runner.summarise(results)

    if args.as_json:
        print(json.dumps({
            "system_prompt_source": source,
            "entries": len(results),
            "replayed": summary.n,
            "consequential": len(summary.consequential),
            "bias_flips": summary.bias_flips,
            "floor_crossings": summary.floor_crossings,
            "mean_conviction_delta": summary.mean_conviction_delta,
            "conviction_drift": summary.conviction_drift_direction,
            "min_conviction": cfg.MIN_CONVICTION,
            "changes": [d.summary() for d in summary.consequential],
            "errors": [{"ticker": r.entry.ticker, "error": r.error} for r in results if r.error],
        }, indent=2))
    else:
        print(render(summary, results, source, args.verbose))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
