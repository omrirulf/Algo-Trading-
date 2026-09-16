"""Render a scoring run as text.

This module owns one judgement the rest of the package deliberately avoids:
**how much evidence is enough to say something.** A rank correlation over nine
signals is arithmetic, not evidence, and printing `rho = 0.61` next to it
invites exactly the conclusion the number cannot support. So every figure is
printed with its sample size, and anything below ``MIN_SAMPLE`` is marked.

The report is meant to be readable when the answer is "not yet". Two weeks
into paper trading the honest output is a coverage table and a row of `too
few`, and that is a useful thing to see rather than a bug to work around.
"""

from __future__ import annotations

from analysis import metrics
from analysis.metrics import Correlation
from analysis.reader import SCORE_FIELDS
from analysis.scoring import ScoringRun

#: Below this, a statistic is shown but explicitly marked as not yet meaningful.
MIN_SAMPLE = 20

#: Per-bucket equivalent for the conviction table.
MIN_BUCKET = 5

WIDTH = 78

_DIMENSION_LABELS = {
    "news_score": "news",
    "technical_score": "technical",
    "fundamental_score": "fundamental",
    "analyst_score": "analyst",
    "insider_score": "insider",
}


def render(run: ScoringRun) -> str:
    sections = [
        _header(run),
        _coverage(run),
        _conviction(run),
        _dimensions(run),
        _blend(run),
        _agreement(run),
        _drift(run),
        _health(run),
        _caveats(run),
    ]
    return "\n\n".join(section for section in sections if section)


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #


def _header(run: ScoringRun) -> str:
    return (
        _rule("SIGNAL JOURNAL SCORING")
        + f"\nhorizon {run.horizon} session(s) | entry rule '{run.entry_rule}' | "
        f"conviction floor {run.floor:.2f}"
    )


def _coverage(run: ScoringRun) -> str:
    read = run.read
    lines = [
        _rule("Coverage"),
        f"journal lines read        {read.total_lines}"
        + (f"  ({read.skipped} unparseable, skipped)" if read.skipped else ""),
        f"entries                   {len(read.entries)}",
        f"  produced a signal       {len(run.with_signal)}",
        f"  directional             {len(run.directional)}  (NEUTRAL: {run.neutral_count})",
        f"  scored                  {len(run.signals)}",
    ]
    for status, count in sorted(run.statuses.items()):
        if status != "ok":
            lines.append(f"  unscored, {status:<15} {count}  {_status_note(status)}")
    if not run.signals:
        lines.append("")
        lines.append(
            "No signal has a realised return yet. Everything below needs price\n"
            "outcomes; the agreement check is the exception and runs anyway."
        )
    return "\n".join(lines)


def _conviction(run: ScoringRun) -> str:
    if not run.signals:
        return ""

    correlation = metrics.conviction_vs_outcome(run.signals)
    buckets = metrics.conviction_buckets(run.signals)
    floor = metrics.floor_check(run.signals, run.floor)

    lines = [
        _rule("Does conviction predict the outcome?"),
        f"rank correlation, conviction vs signed return: {_rho(correlation)}",
        "",
        f"{'conviction':<14}{'n':>5}{'hit rate':>11}{'mean':>10}{'median':>10}",
    ]
    for bucket in buckets:
        if bucket.n == 0:
            continue
        flag = "  (thin)" if bucket.n < MIN_BUCKET else ""
        lines.append(
            f"{bucket.label:<14}{bucket.n:>5}{_pct(bucket.hit_rate):>11}"
            f"{_pct(bucket.mean_return, signed=True):>10}"
            f"{_pct(bucket.median_return, signed=True):>10}{flag}"
        )

    lines += ["", f"Floor at {floor.floor:.2f} — did it filter the right signals?"]
    lines.append(
        f"  acted on (>= floor)  n={floor.above_n:<5} "
        f"hit {_pct(floor.above_hit_rate)}  mean {_pct(floor.above_mean, signed=True)}"
    )
    lines.append(
        f"  filtered (< floor)   n={floor.below_n:<5} "
        f"hit {_pct(floor.below_hit_rate)}  mean {_pct(floor.below_mean, signed=True)}"
    )
    if floor.edge is not None:
        verdict = "the floor is keeping the better signals" if floor.edge > 0 else (
            "the floor is discarding signals that did better than the ones it kept"
        )
        lines.append(f"  edge {_pct(floor.edge, signed=True)} — {verdict}")
        if min(floor.above_n, floor.below_n) < MIN_SAMPLE:
            lines.append(f"  {_thin(min(floor.above_n, floor.below_n))}")
    return "\n".join(lines)


def _dimensions(run: ScoringRun) -> str:
    if not run.signals:
        return ""
    correlations = metrics.dimension_correlations(run.signals)
    lines = [
        _rule("Which dimension actually carried information?"),
        "Each score against the ticker's raw forward return.",
        "",
        f"{'dimension':<14}{'n':>5}{'rank corr':>14}",
    ]
    for name in SCORE_FIELDS:
        correlation = correlations[name]
        lines.append(
            f"{_DIMENSION_LABELS[name]:<14}{correlation.n:>5}"
            f"{_rho(correlation, show_n=False):>14}"
        )
    if max((c.n for c in correlations.values()), default=0) < MIN_SAMPLE:
        lines.append("")
        lines.append(_thin(max((c.n for c in correlations.values()), default=0)))
    return "\n".join(lines)


def _blend(run: ScoringRun) -> str:
    if not run.blend_signals:
        return ""
    comparison = metrics.blend_comparison(run.blend_signals)
    lines = [
        _rule("Does the learned blend carry information?"),
        "The five scores blended into one, against the ticker's raw forward return.",
        "Every line with a signal and a score counts here, NEUTRAL included: the",
        "blend takes a side on those too. 'learned blend' is the composite as it",
        "was journalled, with whatever weights that cycle had -- the walk-forward",
        "record, never a refit that has seen the return it is judged on.",
        "",
        f"{'policy':<18}{'n':>5}{'called':>8}{'rank corr':>14}{'hit rate':>10}",
    ]
    for check in (comparison.model, comparison.equal, comparison.learned):
        lines.append(
            f"{check.label:<18}{check.n:>5}{check.called:>8}"
            f"{_rho(check.rank_corr, show_n=False):>14}{_pct(check.hit_rate):>10}"
        )
    learned = comparison.learned
    if learned.n:
        fallback = learned.n - comparison.learned_fitted
        lines.append(
            f"  learned composites from fitted weights: {comparison.learned_fitted}; "
            f"from the equal-weight fallback: {fallback}"
        )
    if comparison.disagreements:
        lines += [
            "",
            f"  model and blend called opposite directions  n={comparison.disagreements:<5} "
            f"model hit {_pct(comparison.model_hit_rate_when_disagreeing)}  "
            f"blend hit {_pct(comparison.blend_hit_rate_when_disagreeing)}",
        ]
    lines.append("")
    verdict = metrics.promotion_verdict(comparison, MIN_SAMPLE)
    lines.append(("  READY TO LEAVE SHADOW: " if verdict.ready else "  ") + verdict.reason)
    return "\n".join(lines)


def _agreement(run: ScoringRun) -> str:
    check = metrics.agreement_check(run.entries)
    if check.aligned_n == 0 and check.conflicted_n == 0:
        return ""

    lines = [
        _rule("Does conviction fall when the dimensions disagree?"),
        "The prompt requires it. This needs no price data, so it is answerable",
        "from the first cycle onward.",
        "",
        f"  all dimensions agree   n={check.aligned_n:<5} "
        f"mean conviction {_num(check.aligned_mean_conviction)}",
        f"  at least one dissents  n={check.conflicted_n:<5} "
        f"mean conviction {_num(check.conflicted_mean_conviction)}",
    ]
    if check.gap is not None:
        if check.gap > 0:
            verdict = "conviction is lower when dimensions conflict, as instructed"
        elif check.gap == 0:
            verdict = "no difference — the instruction is not changing behaviour"
        else:
            verdict = "conviction is HIGHER when dimensions conflict — the opposite of the instruction"
        lines.append(f"  gap {_num(check.gap, signed=True)} — {verdict}")
    lines.append(
        f"  rank corr, score spread vs conviction: "
        f"{_rho(check.dispersion_vs_conviction)} (negative is correct)"
    )
    lines.append(
        "  Across several dimensions unanimity is rare and 'at least one dissents' is\n"
        "  the common case — read the spread correlation as the finer measure."
    )
    if min(check.aligned_n, check.conflicted_n) < MIN_BUCKET:
        lines.append(f"  {_thin(min(check.aligned_n, check.conflicted_n))}")
    return "\n".join(lines)


def _drift(run: ScoringRun) -> str:
    drift = metrics.conviction_drift(run.entries, run.floor)
    if drift.first_n == 0 and drift.second_n == 0:
        return ""
    lines = [
        _rule("Is conviction drifting?"),
        "A model that creeps toward always-confident makes the floor a no-op.",
        "",
        f"  first half   n={drift.first_n:<5} mean {_num(drift.first_mean)}  "
        f"above floor {_pct(drift.first_above_floor)}",
        f"  second half  n={drift.second_n:<5} mean {_num(drift.second_mean)}  "
        f"above floor {_pct(drift.second_above_floor)}",
    ]
    if drift.change is not None:
        lines.append(f"  change {_num(drift.change, signed=True)}")
    return "\n".join(lines)


def _health(run: ScoringRun) -> str:
    entries = run.entries
    if not entries:
        return ""
    with_gaps, kinds = metrics.gap_summary(entries)
    biases = metrics.bias_distribution(entries)

    lines = [_rule("Input health")]
    share = with_gaps / len(entries)
    lines.append(f"  cycles with a context gap  {with_gaps}/{len(entries)} ({_pct(share)})")
    for kind, count in kinds.most_common(6):
        lines.append(f"    {kind:<40} {count}")
    if share > 0.5:
        lines.append(
            "  More than half of all cycles ran on incomplete context. Treat every\n"
            "  number above as describing a different system than the intended one."
        )

    lines.append("")
    total_bias = sum(biases.values())
    lines.append(f"  bias distribution ({total_bias} signals)")
    for bias in ("BULLISH", "BEARISH", "NEUTRAL"):
        count = biases.get(bias, 0)
        lines.append(f"    {bias:<10} {count:>5}  {_pct(count / total_bias if total_bias else None)}")
    errors = sum(1 for e in entries if e.error)
    if errors:
        lines.append(f"  cycles that produced no signal: {errors}")
    return "\n".join(lines)


def _caveats(run: ScoringRun) -> str:
    lines = [
        _rule("How to read this"),
        f"* Returns are close-to-close over {run.horizon} session(s) and ignore the "
        "stop-loss,",
        "  slippage and commission. They measure the signal, not the strategy's P&L.",
        f"* Entry rule '{run.entry_rule}': "
        + _entry_note(run.entry_rule),
        f"* Anything marked 'too few' has fewer than {MIN_SAMPLE} observations. It is",
        "  arithmetic, not evidence — the sign can flip on one more data point.",
        "* A single earnings day can dominate a small sample; rank correlations are",
        "  used throughout to blunt that, not to eliminate it.",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Formatting
# --------------------------------------------------------------------------- #


def _entry_note(rule: str) -> str:
    return {
        "auto": "same-session close when the signal fired before the close\n"
        "  and carried an exact UTC timestamp, next session's close otherwise.",
        "next": "always the next session's close. Never uses a price the\n"
        "  model could have seen, at the cost of the same-day move.",
        "same": "always the signal date's close. Only honest if the heartbeat\n"
        "  runs during the session — an after-hours signal scores against a past price.",
    }.get(rule, rule)


def _status_note(status: str) -> str:
    return {
        "pending": "(too recent — no outcome yet)",
        "no_entry_bar": "(no session on or after the signal)",
        "no_history": "(price history unavailable)",
        "no_timestamp": "(unparseable timestamp)",
    }.get(status, "")


def _rule(title: str) -> str:
    return f"{title}\n{'-' * min(len(title), WIDTH)}"


def _thin(n: int) -> str:
    return f"too few to conclude anything (n={n}, want {MIN_SAMPLE}+)"


def _rho(correlation: Correlation, show_n: bool = True) -> str:
    """``show_n`` is off where the surrounding table already has an n column."""
    suffix = f" (n={correlation.n})" if show_n else ""
    if correlation.rho is None:
        return f"n/a{suffix}"
    body = f"{correlation.rho:+.2f}{suffix}"
    if correlation.n < MIN_SAMPLE:
        body += " — too few"
    return body


def _pct(value: float | None, signed: bool = False) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:{'+' if signed else ''}.1f}%"


def _num(value: float | None, signed: bool = False) -> str:
    if value is None:
        return "n/a"
    return f"{value:{'+' if signed else ''}.3f}"
