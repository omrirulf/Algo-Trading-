#!/usr/bin/env python3
"""Ask the same recorded context twice: once with the headlines, once without.

    python replay/news_ablation.py --limit 100 --model claude-opus-5 --effort low
    python replay/news_ablation.py --limit 100 --model claude-opus-5 --emit-pairs

The scorer reports that the model's ``news_score`` correlates *negatively*
with the return that followed (-0.25 over n=48 at the time of writing). That
is a statement about a number the model emits, not about whether reading the
headlines helped or hurt: the score is one of five dimensions, and the model
may be discounting it, inverting it, or using the headlines for something the
score does not capture. The only way to find out what the news section is
doing is to take it away and ask again.

What this measures
------------------
For each recorded context, the model is asked the identical question twice in
the same run: once with the ``NEWS`` block exactly as production sent it, and
once with the headlines removed. Everything else -- the system prompt, the
technicals, the fundamentals, the model, the effort -- is held fixed, so the
only difference between the two answers is the news.

Both answers are *fresh*. The journalled answer is free and sits in the
report as a third column, but it is not the baseline, because a model that
disagrees with itself about one context in ten would otherwise contribute its
whole flip rate to the ablation's. That self-flip rate is measured here too,
on these same contexts, from the with-news answer against the journalled one
-- so the report carries its own noise floor rather than borrowing one from a
different run on different lines. **An ablation flip rate that does not clear
its own self-flip rate is not evidence the news changed anything.**

Removing, not blanking loudly
-----------------------------
"Without news" is the context with ``headlines`` emptied, which renders as
``NEWS (past 24 hours)\\n- none found`` -- a shape production already sends
whenever a quiet ticker returns nothing, and one this model has answered many
times. Cutting the heading out entirely would be a truer "no news source at
all", and was rejected for exactly that reason: it would hand the model a
prompt shape it has never seen, and the ablation would then be measuring
novelty as well as news. ``- unavailable this cycle`` was rejected too --
that asserts a failed lookup, which is a different claim (see
``TickerContext._news_section``).

Only contexts that actually carry headlines are eligible. Blanking a line
that already says "none found" is a no-op that costs two calls to learn
nothing.

Which one was right
-------------------
Agreement and conviction say whether the news *moved* the answer. They cannot
say which answer the market rewarded. ``--emit-pairs`` prints both sides as
journal-shaped lines, to be split by ``_side`` and handed to
``analysis/score_journal.py`` -- the same route ``compare_models.py`` takes,
for the same reason: prices are the ground truth and that tool already knows
how to join signals to them.

Same guarantees as the rest of replay/: it reads the journal, calls the
model, and prints. No broker keys, no journal write, no order path.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.schemas import LLMSignal  # noqa: E402
from config import settings as cfg  # noqa: E402
from replay import runner  # noqa: E402
from replay.runner import ReplayEntry, ReplayResult  # noqa: E402

DEFAULT_LIMIT = 100

#: The two arms, in report order. The recorded prompt first, because it is
#: what production sends today.
WITH_NEWS = "with-news"
WITHOUT_NEWS = "without-news"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask each recorded context with and without its headlines.",
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument(
        "--limit", type=int, default=DEFAULT_LIMIT,
        help="contexts to ask (default %(default)s). Total calls = limit x 2, "
             "because each is asked both ways in this run.",
    )
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", default=None)
    parser.add_argument(
        "--floor", type=float, default=cfg.MIN_CONVICTION,
        help="conviction floor a 'would trade' verdict is judged against "
             "(default: the engine's %(default)s)",
    )
    parser.add_argument("--base-url", default="",
                        help="ask an OpenAI-compatible endpoint instead of Claude")
    parser.add_argument("--api-key", default="", help="bearer token for --base-url, if it wants one")
    parser.add_argument("--concurrency", type=int, default=4,
                        help="calls in flight at once, --base-url only (default %(default)s). "
                             "Ignored for Claude, which would just meet a rate limit.")
    parser.add_argument("--timeout", type=float, default=0, help="per-call timeout in seconds")
    parser.add_argument("--dry-run", action="store_true",
                        help="report the sample and the call count, ask nothing")
    parser.add_argument(
        "--emit-pairs", action="store_true",
        help="print both sides as journal-shaped lines for analysis/score_journal.py; "
             "the human report then goes to stderr",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


# --------------------------------------------------------------------------- #
# The sample, and the two prompts for each line
# --------------------------------------------------------------------------- #


def eligible(entries: list[ReplayEntry]) -> list[ReplayEntry]:
    """The lines the ablation can say anything about: the ones with headlines.

    A context whose news block already reads "none found" is its own control;
    asking it both ways costs two calls to prove that an empty list stayed
    empty.
    """
    return [e for e in entries if e.context is not None and e.context.headlines]


def without_news(entry: ReplayEntry) -> ReplayEntry:
    """The same line, with the headlines taken out of the prompt.

    Built by re-rendering a real ``TickerContext`` rather than by editing the
    prompt string, so what the model is asked stays something
    ``as_prompt()`` can produce -- the section order, spacing and wording are
    the ones production would send for a ticker with no headlines that day.
    """
    blanked = replace(entry.context, headlines=[], sources=[])
    return replace(entry, context=blanked, prompt=blanked.as_prompt())


# --------------------------------------------------------------------------- #
# One context, asked both ways
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Ablation:
    """One recorded context, asked with the news and without it."""

    ticker: str
    ts_utc: Optional[str]
    #: Fresh answers from this run. ``None`` when that call failed.
    with_news: Optional[LLMSignal]
    without_news: Optional[LLMSignal]
    #: What the journal recorded when this line was live. Free, and not the
    #: baseline: it is here to measure the model's disagreement with itself.
    journalled: Optional[LLMSignal]

    @property
    def assessable(self) -> bool:
        """Both fresh calls answered, so the pair can be compared at all."""
        return self.with_news is not None and self.without_news is not None

    @property
    def direction_changed(self) -> Optional[bool]:
        if not self.assessable:
            return None
        return self.with_news.bias != self.without_news.bias

    def trade_decision_changed(self, floor: float) -> Optional[bool]:
        """Did removing the news change whether this line would be traded?"""
        if not self.assessable:
            return None
        return _would_trade(self.with_news, floor) != _would_trade(self.without_news, floor)

    @property
    def conviction_delta(self) -> Optional[float]:
        """Without-news conviction minus with-news conviction."""
        if not self.assessable:
            return None
        return self.without_news.conviction - self.with_news.conviction

    @property
    def self_flipped(self) -> Optional[bool]:
        """The noise floor: the with-news answer against the journalled one.

        Same context, same question, same configuration, asked on different
        days. Any disagreement here is the model disagreeing with itself,
        and the ablation has to clear it to mean anything.
        """
        if self.with_news is None or self.journalled is None:
            return None
        return self.with_news.bias != self.journalled.bias


def _would_trade(signal: LLMSignal, floor: float) -> bool:
    return signal.bias.value in ("BULLISH", "BEARISH") and signal.conviction >= floor


def ablate(
    entries: list[ReplayEntry], complete: runner.Completer, max_workers: int = 1,
) -> tuple[list[Ablation], list[ReplayResult]]:
    """Ask every entry both ways and pair the answers up.

    The system prompt is resolved once per line, from the *recorded* context,
    and handed to both arms. The fund prompt is narrowed by which sections a
    context carries, and although emptying ``headlines`` does not change that
    set today, deriving it twice would leave the ablation one refactor away
    from varying two things at once.
    """
    prompts = {id(entry): runner.system_prompt_for_entry(entry) for entry in entries}
    blanked = [without_news(entry) for entry in entries]
    for original, stripped in zip(entries, blanked):
        prompts[id(stripped)] = prompts[id(original)]

    asked = entries + blanked
    results = runner.replay_each(asked, lambda e: prompts[id(e)], complete, max_workers)
    half = len(entries)
    return [
        Ablation(
            ticker=entry.ticker,
            ts_utc=entry.ts_utc,
            with_news=kept.replayed,
            without_news=stripped.replayed,
            journalled=entry.original,
        )
        for entry, kept, stripped in zip(entries, results[:half], results[half:])
    ], results


# --------------------------------------------------------------------------- #
# What the pairs add up to
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Summary:
    n_asked: int
    n_assessable: int
    failures: int
    direction_changed: int
    trade_decision_changed: int
    self_comparable: int
    self_flipped: int
    mean_conviction_with: Optional[float]
    mean_conviction_without: Optional[float]
    mean_abs_conviction_delta: Optional[float]
    mean_abs_news_score_with: Optional[float]
    mean_abs_news_score_without: Optional[float]

    @property
    def flip_rate(self) -> Optional[float]:
        if not self.n_assessable:
            return None
        return self.direction_changed / self.n_assessable

    @property
    def trade_flip_rate(self) -> Optional[float]:
        if not self.n_assessable:
            return None
        return self.trade_decision_changed / self.n_assessable

    @property
    def self_flip_rate(self) -> Optional[float]:
        if not self.self_comparable:
            return None
        return self.self_flipped / self.self_comparable

    @property
    def clears_the_noise_floor(self) -> Optional[bool]:
        """Did removing the news move the answer more than the model's own wobble?

        A one-sided comparison of two rates, deliberately crude: this is a
        gate on whether the number is worth reading at all, not a p-value.
        """
        if self.flip_rate is None or self.self_flip_rate is None:
            return None
        return self.flip_rate > self.self_flip_rate


def summarise(pairs: list[Ablation], floor: float, failures: int) -> Summary:
    good = [p for p in pairs if p.assessable]
    comparable = [p for p in pairs if p.self_flipped is not None]
    return Summary(
        n_asked=len(pairs),
        n_assessable=len(good),
        failures=failures,
        direction_changed=sum(1 for p in good if p.direction_changed),
        trade_decision_changed=sum(1 for p in good if p.trade_decision_changed(floor)),
        self_comparable=len(comparable),
        self_flipped=sum(1 for p in comparable if p.self_flipped),
        mean_conviction_with=_mean([p.with_news.conviction for p in good]),
        mean_conviction_without=_mean([p.without_news.conviction for p in good]),
        mean_abs_conviction_delta=_mean([abs(p.conviction_delta) for p in good]),
        mean_abs_news_score_with=_mean(
            [abs(p.with_news.news_score) for p in good if p.with_news.news_score is not None]
        ),
        mean_abs_news_score_without=_mean(
            [abs(p.without_news.news_score) for p in good if p.without_news.news_score is not None]
        ),
    )


def _mean(values: list[float]) -> Optional[float]:
    return statistics.fmean(values) if values else None


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render(summary: Summary, pairs: list[Ablation], floor: float, label: str) -> str:
    out = [
        "THE NEWS SECTION, TAKEN AWAY",
        "=" * 78,
        f"Configuration : {label}",
        f"Contexts      : {summary.n_asked} asked both ways "
        f"({summary.n_asked * 2} calls), {summary.n_assessable} answered twice",
        f"Failure rate  : {summary.failures}/{summary.n_asked * 2} calls",
        "",
        "DID THE NEWS MOVE THE ANSWER?",
        "-" * 78,
        f"{'direction changed when the news was removed':<52}{_pct(summary.flip_rate):>8}"
        f"  ({summary.direction_changed}/{summary.n_assessable})",
        f"{'  ... the model disagreeing with ITSELF (noise floor)':<52}"
        f"{_pct(summary.self_flip_rate):>8}  ({summary.self_flipped}/{summary.self_comparable})",
        f"{'trade decision changed (side and floor together)':<52}"
        f"{_pct(summary.trade_flip_rate):>8}  ({summary.trade_decision_changed}/{summary.n_assessable})",
        "",
        _floor_verdict(summary),
        "",
        "WHAT ELSE CHANGED",
        "-" * 78,
        f"{'mean conviction, with the news':<52}{_num(summary.mean_conviction_with):>8}",
        f"{'mean conviction, without it':<52}{_num(summary.mean_conviction_without):>8}",
        f"{'mean absolute change in conviction':<52}{_num(summary.mean_abs_conviction_delta):>8}",
        f"{'mean |news_score|, with the news':<52}{_num(summary.mean_abs_news_score_with):>8}",
        f"{'mean |news_score|, without it':<52}{_num(summary.mean_abs_news_score_without):>8}",
        "",
        "  The last pair is the sanity check, not a finding: with the headlines",
        "  gone the news dimension should collapse toward zero. If it does not,",
        "  the model is scoring news from something other than the news block",
        "  and every number above is about the wrong thing.",
    ]

    changed = [p for p in pairs if p.direction_changed]
    if changed:
        out += [
            "",
            "EVERY LINE THE NEWS TURNED",
            "-" * 78,
            f"{'ticker':<8}{'day':<12}{'with news':<22}{'without news':<22}{'journalled':<12}",
        ]
        for pair in sorted(changed, key=lambda p: (p.ts_utc or "", p.ticker)):
            out.append(
                f"{pair.ticker:<8}{(pair.ts_utc or '')[:10]:<12}"
                f"{_call(pair.with_news):<22}{_call(pair.without_news):<22}"
                f"{(pair.journalled.bias.value if pair.journalled else 'n/a'):<12}"
            )

    out += [
        "",
        "HOW TO READ THIS",
        "-" * 78,
        "The flip rate is not the finding on its own. This model answers the",
        "same context differently about one time in ten for no reason at all,",
        "and that rate is measured here, on these contexts, in the row under",
        "it. Only the gap between the two is about the news.",
        "",
        "And a moved answer is not a better answer. Nothing above says which",
        "side the market rewarded -- for that, run with --emit-pairs and score",
        "both sides against realised returns.",
        "",
        "LIMITS",
        "-" * 78,
        "Only contexts that carried headlines are asked; a line whose news",
        "block already said 'none found' is its own control and is skipped.",
        "'Without news' means the headlines are gone and the heading remains,",
        "which is a shape production already sends. A system that fetched no",
        "news at all would also drop the news dimension from the system prompt",
        "and the schema, and this does not measure that.",
    ]
    return "\n".join(out)


def _floor_verdict(summary: Summary) -> str:
    if summary.clears_the_noise_floor is None:
        return "  verdict: not enough answered twice to compare anything."
    if not summary.clears_the_noise_floor:
        return (
            "  verdict: removing the news moved the answer NO MORE than the model's\n"
            "  own inconsistency does. On this sample the news section is not\n"
            "  measurably changing what the model says."
        )
    gap = summary.flip_rate - summary.self_flip_rate
    return (
        f"  verdict: removing the news moved the answer on {_pct(gap)} more of the\n"
        "  contexts than the model's own wobble accounts for. The news is\n"
        "  changing the call; whether for the better is a returns question."
    )


def _call(signal: Optional[LLMSignal]) -> str:
    if signal is None:
        return "n/a"
    news = "" if signal.news_score is None else f", news {signal.news_score:+.2f}"
    return f"{signal.bias.value} {signal.conviction:.2f}{news}"


def _pct(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value * 100:.0f}%"


def _num(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value:.3f}"


def as_json(summary: Summary, pairs: list[Ablation], floor: float, label: str) -> dict:
    return {
        "configuration": label,
        "floor": floor,
        "contexts_asked": summary.n_asked,
        "calls": summary.n_asked * 2,
        "assessable": summary.n_assessable,
        "failures": summary.failures,
        "direction_flip_rate": summary.flip_rate,
        "self_flip_rate": summary.self_flip_rate,
        "trade_decision_flip_rate": summary.trade_flip_rate,
        "clears_the_noise_floor": summary.clears_the_noise_floor,
        "mean_conviction_with": summary.mean_conviction_with,
        "mean_conviction_without": summary.mean_conviction_without,
        "mean_abs_conviction_delta": summary.mean_abs_conviction_delta,
        "mean_abs_news_score_with": summary.mean_abs_news_score_with,
        "mean_abs_news_score_without": summary.mean_abs_news_score_without,
        "changed": [
            {
                "ticker": p.ticker, "ts_utc": p.ts_utc,
                "with_news": p.with_news.model_dump(mode="json") if p.with_news else None,
                "without_news": p.without_news.model_dump(mode="json") if p.without_news else None,
            }
            for p in pairs if p.direction_changed
        ],
    }


def print_pairs(entries: list[ReplayEntry], pairs: list[Ablation]) -> int:
    """Both sides, journal-shaped, for ``analysis/score_journal.py``.

    Printed rather than written: replay/ may not open a file for writing, and
    that rule is what stops a path argument aimed at the real journal from
    destroying the record. Only contexts where both sides answered are
    printed, so the two are scored over the identical days -- otherwise part
    of any difference in realised return would just be a difference in which
    market each side was in.
    """
    printed = 0
    for entry, pair in zip(entries, pairs):
        if not pair.assessable:
            continue
        for side, signal in ((WITH_NEWS, pair.with_news), (WITHOUT_NEWS, pair.without_news)):
            print(json.dumps({
                "_side": side,
                "line": json.loads(runner.as_journal_line(entry, signal)),
            }))
        printed += 1
    print(f"printed {printed} paired context(s); split by _side and score each with "
          f"analysis/score_journal.py.", file=sys.stderr)
    return printed


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.journal.exists():
        print(f"No journal at {args.journal}. Run some cycles first -- this asks "
              f"the model about real recorded context.", file=sys.stderr)
        return 1

    lines = args.journal.read_text(encoding="utf-8").splitlines()
    entries = eligible(list(runner.load_entries(lines)))[-args.limit:]
    if not entries:
        print("No entry in this journal carries headlines, so there is nothing to "
              "take away.", file=sys.stderr)
        return 1

    label = f"{args.model} / {args.effort}" if args.effort else args.model
    print(f"Asking {len(entries)} context(s) x 2 = {len(entries) * 2} calls "
          f"({label})...", file=sys.stderr)
    if args.dry_run:
        print("--dry-run: nothing asked.", file=sys.stderr)
        return 0

    complete, _usages = runner.measured_completer(
        model=args.model, effort=args.effort or None, base_url=args.base_url,
        api_key=args.api_key, timeout=args.timeout or None,
    )
    # Concurrency only against an endpoint we chose to point at; the Claude
    # path would be firing a whole journal at a rate limit, and a
    # rate-limited context is a lost one where a slow one is only slow.
    workers = args.concurrency if args.base_url else 1
    pairs, results = ablate(entries, complete, workers)
    failures = sum(1 for r in results if r.error)
    summary = summarise(pairs, args.floor, failures)

    if args.emit_pairs:
        print_pairs(entries, pairs)
        print(render(summary, pairs, args.floor, label), file=sys.stderr)
    elif args.as_json:
        print(json.dumps(as_json(summary, pairs, args.floor, label), indent=2))
    else:
        print(render(summary, pairs, args.floor, label))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
