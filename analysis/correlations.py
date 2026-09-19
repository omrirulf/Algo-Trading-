"""Realised correlation between the things this book can hold.

    python -m analysis.correlations                  # the report, for a person
    python -m analysis.correlations --json           # the numbers, for a machine
    python -m analysis.correlations --start 2007-01-01

``config/instruments.py`` groups tickers by what they are assumed to correlate
with. Every one of those groups is a *hypothesis* -- a plausible story about
what moves together -- and until this module existed none of them had been
measured. This measures them, and nothing else: it cannot size a position,
place an order, or change a cap. ``analysis/`` is forbidden from writing files
at all (CI greps for it), so the report goes to stdout and a workflow captures
it.

Why it must not set a cap by itself
-----------------------------------
The same reason ``BLEND_MODE`` is pinned to ``shadow``: a fitted number inside
the risk engine is a number nobody can audit. Correlation is unstable, it is
estimated here from a few hundred observations per pair across thousands of
pairs, and a cap that quietly rewires itself is exactly what the rest of this
codebase refuses to allow. So this prints evidence; a person promotes a
finding into ``EXPOSURE_GROUPS`` or ``EXPOSURE_GROUP_CAP_OVERRIDES`` by hand,
with the measured number written into the comment beside it.

Why stress correlation, and not the average
-------------------------------------------
A cap exists for the day the book is losing money. Diversification fails
exactly then: correlations converge toward one in a sell-off, which is the
opposite of what a full-sample average reports. So every pair is measured over
three windows -- recent (60d), long (250d) and **stress** (the worst days for
``RSP``, the book's broad-equity proxy) -- and the verdict names which of them
it held in:

``stable``
    Strong in all three. A real, persistent link; the honest candidate for a
    group merge or a tighter cap.
``stress-only``
    Weak day to day, strong when the market is falling. The most dangerous
    kind and the one a full-sample number misses entirely -- two positions
    that look like diversification right up to the morning it matters.
``fades-in-stress``
    Strong normally, weak in the tail. This is diversification working; it
    argues *against* capping the pair together.
``emerging``
    Strong in the last quarter only. The weakest evidence here and the most
    likely to be noise, but a regime that has genuinely changed looks like
    this first.
``weak``
    Not there. Which is a finding too: several of the stories in this file's
    git history were exactly that.

The stress window is defined by equity, because a book that is 70% funds and
25% single names is mostly an equity book. That is a choice, not a law, and a
pair whose own tail sits elsewhere (a rates shock with equities flat) is one
this window will understate. Said here rather than discovered later.

Named crises, on top of that
----------------------------
The quantile window blends every bad day since the start date into one
number, which buries the most useful comparison available: 2008 was a credit
and solvency crisis, 2020 a liquidity scramble, 2022 a rates repricing, and
they did not produce the same correlations. ``CRISES`` measures each one
separately.

That only works if the data reaches them, and for much of this watchlist it
does not: the copper and grain funds, MCHI, INDA, KSA and XLC were all
launched in the 2010s and have no 2008 at all. ``coverage()`` reports how
many tickers each window actually had, and the crisis table prints a dash
rather than a number for a pair that did not yet exist -- because the
alternative is a reader comparing one pair's 2008 against another's 2020
and believing they are the same measurement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Optional, Sequence

import numpy as np
import pandas as pd

from config.instruments import EXPOSURE_GROUPS, name_for
from config.watchlist import DEFAULT_WATCHLIST

#: Recent and long windows, in trading days. 60 is about a quarter, 250 about
#: a year -- short enough to catch a regime that has changed, long enough that
#: one bad fortnight does not define the answer.
SHORT_WINDOW: int = 60
LONG_WINDOW: int = 250

#: The stress window: the worst this fraction of days for STRESS_BENCHMARK.
#: 5% of a year is about 13 days, which is few enough that the estimate is
#: noisy and enough that it is not one afternoon. Read the count printed
#: beside the number before trusting it.
STRESS_QUANTILE: float = 0.05
STRESS_BENCHMARK: str = "RSP"

#: |r| at or above this is called a link. Deliberately high: at 0.3 half the
#: watchlist is "correlated" with the other half and the word stops meaning
#: anything. A cap should answer to a number that would survive being read
#: aloud.
STRONG: float = 0.60

#: Fewer overlapping observations than this and the pair is reported as
#: unmeasured rather than as a number. A correlation from eight days is not a
#: small correlation, it is noise with a decimal point.
MIN_OBSERVATIONS: int = 20

STABLE = "stable"
STRESS_ONLY = "stress-only"
FADES = "fades-in-stress"
EMERGING = "emerging"
WEAK = "weak"
UNMEASURED = "unmeasured"


@dataclass(frozen=True)
class Crisis:
    """One named drawdown, measured on its own rather than blended in."""

    label: str
    short: str
    start: str
    end: str


#: The regimes worth measuring separately, peak to trough.
#:
#: A single quantile-based stress window blends these together, which hides
#: the thing most worth knowing: correlations that hold in one crisis often
#: do not hold in the next, because each one has a different cause. 2008 was
#: credit and bank solvency, 2020 was a liquidity scramble in which even
#: Treasuries sold off for a week, 2022 was rates repricing and is the only
#: one of the three where bonds and equities fell *together* for a year. A
#: pair that co-moves in all of them is a different animal from one that
#: co-moved in 2022 alone.
#:
#: Dates are index peaks and troughs rather than round months, so each
#: window is the drawdown itself and not the recovery either side of it.
CRISES: tuple[Crisis, ...] = (
    Crisis("Global financial crisis", "GFC'08", "2007-10-09", "2009-03-09"),
    Crisis("Euro sovereign debt", "Euro'11", "2011-07-01", "2011-10-04"),
    Crisis("China and oil", "Oil'15", "2015-08-01", "2016-02-11"),
    Crisis("Q4 2018 selloff", "Q4'18", "2018-10-01", "2018-12-24"),
    Crisis("Covid crash", "Covid'20", "2020-02-19", "2020-03-23"),
    Crisis("Rates repricing", "Rates'22", "2022-01-03", "2022-10-12"),
)


@dataclass(frozen=True)
class CrisisResult:
    """One pair through one crisis. ``days`` is why to believe it or not."""

    label: str
    short: str
    raw: Optional[float]
    excess: Optional[float]
    days: int


# --------------------------------------------------------------------------- #
# The hypotheses
# --------------------------------------------------------------------------- #
#: Pairs worth adjudicating by name, because each one is a story someone told
#: about this watchlist -- including several told confidently by an LLM in the
#: conversation that produced this file. A named pair gets measured whether or
#: not it clears the threshold, so a story that is wrong is recorded as wrong
#: rather than quietly dropped from the output.
#:
#: Left and right are sets of tickers, equal-weighted. Where a side is exactly
#: an existing exposure group it is named as one, so the report reads as a
#: check on ``EXPOSURE_GROUPS`` rather than on an ad-hoc basket.

HYPOTHESES: tuple[tuple[str, tuple[str, ...], tuple[str, ...]], ...] = (
    ("Dollar vs duration", ("UUP",), ("IEF", "TLT")),
    ("Dollar vs precious metals", ("UUP",), ("GLD", "SLV", "GDX")),
    ("Dollar vs emerging markets", ("UUP",), ("VWO", "MCHI", "INDA", "EWZ")),
    ("Gold vs inflation-linked (real rates)", ("GLD",), ("TIP",)),
    ("Chips vs Taiwan and Korea", ("NVDA", "ASML", "SMH"), ("EWT", "EWY")),
    ("Duration vs utilities", ("IEF", "TLT"), ("XLU",)),
    ("Duration vs real estate", ("IEF", "TLT"), ("VNQ", "XHB")),
    ("Duration vs regional banks", ("IEF", "TLT"), ("KRE",)),
    ("High yield vs US equity", ("HYG",), ("RSP", "IWM")),
    ("Energy vs Canada", ("XOM", "USO", "XLE"), ("EWC",)),
    ("Silver vs copper", ("SLV",), ("CPER",)),
)


# --------------------------------------------------------------------------- #
# Pure math -- no network, no I/O, so the tests need neither
# --------------------------------------------------------------------------- #


def daily_returns(closes: pd.DataFrame) -> pd.DataFrame:
    """Simple daily returns from a frame of closes, one column per ticker.

    Simple rather than log returns: these are correlated and compared, never
    compounded, and simple returns are what the exposure numbers elsewhere in
    this package are denominated in.
    """
    return closes.sort_index().pct_change().dropna(how="all")


def stress_index(
    returns: pd.DataFrame,
    benchmark: str = STRESS_BENCHMARK,
    quantile: float = STRESS_QUANTILE,
) -> pd.Index:
    """The worst ``quantile`` of days for ``benchmark``.

    Empty when the benchmark is missing, which the caller reports as
    unmeasured rather than silently falling back to the full sample -- a
    stress number quietly computed over every day is worse than no stress
    number, because it looks like one.
    """
    if benchmark not in returns.columns:
        return pd.Index([])
    series = returns[benchmark].dropna()
    if series.empty:
        return pd.Index([])
    cutoff = series.quantile(quantile)
    return series[series <= cutoff].index


def basket(returns: pd.DataFrame, tickers: Sequence[str]) -> Optional[pd.Series]:
    """One equal-weighted return series for a set of tickers.

    Equal weight rather than cap or exposure weight: the caps this informs are
    expressed per group, and a group's members are each capped individually,
    so no member is privileged in advance. Missing tickers are skipped -- a
    delisted ETN should not take a whole basket out of the report.
    """
    present = [t for t in tickers if t in returns.columns]
    if not present:
        return None
    return returns[present].mean(axis=1, skipna=True)


def book_factor(returns: pd.DataFrame) -> Optional[pd.Series]:
    """The one thing every holding has in common: the watchlist's average day.

    What ``market_residual`` regresses against, and deliberately **not**
    ``STRESS_BENCHMARK``. Regressing eighty series against one ETF injects
    that ETF's own idiosyncratic noise into every residual with the same
    sign, so the residuals all end up sharing a ``-beta x noise(RSP)`` term
    and correlate with each other for a reason that has nothing to do with
    the holdings. Measured on synthetic data where the true excess
    correlation was zero, that artefact alone produced ~0.9. Averaging
    across the whole watchlist drives the noise down instead of stamping it
    on everything.

    A group's own members are inside the average, which pulls its residual
    slightly toward zero -- a twelve-name group is 15% of an eighty-name
    mean. That biases toward reporting *fewer* links than exist, which is
    the right direction for a number that might tighten a cap.
    """
    if returns.empty:
        return None
    factor = returns.mean(axis=1, skipna=True).dropna()
    return factor if len(factor) >= MIN_OBSERVATIONS else None


def market_residual(series: pd.Series, market: pd.Series) -> Optional[pd.Series]:
    """``series`` with its common-factor beta removed: what is left after
    "everything moved".

    The number that makes the cross-group section worth reading. Raw
    correlation between two equity groups is ~0.8 for the boring reason that
    both are equities, and reporting 171 pairs of 0.8 answers a question
    nobody asked -- that risk is what ``MAX_GROSS_EXPOSURE_PCT`` exists for.
    What a *group* cap wants to know is whether two groups move together
    **beyond** the factor they already share, because that is the part
    holding both of them does not diversify away.

    One factor, fitted by least squares, and nothing else. Crude is
    deliberate: a richer factor model fitted here would be a fitted model
    nobody can audit, which is precisely what this module is careful not to
    become.
    """
    joined = pd.concat([series, market], axis=1).dropna()
    if len(joined) < MIN_OBSERVATIONS:
        return None
    s, m = joined.iloc[:, 0], joined.iloc[:, 1]
    variance = float(m.var())
    if variance == 0 or not np.isfinite(variance):
        return None
    beta = float(s.cov(m)) / variance
    return s - beta * m


def correlation(left: pd.Series, right: pd.Series) -> tuple[Optional[float], int]:
    """Pearson r over the days both series have, and how many days that was.

    The count travels with the number on purpose. Every caller has to decide
    whether to believe it, and that decision is about the sample size far more
    often than about the coefficient.
    """
    joined = pd.concat([left, right], axis=1).dropna()
    if len(joined) < MIN_OBSERVATIONS:
        return None, len(joined)
    a, b = joined.iloc[:, 0], joined.iloc[:, 1]
    if a.std() == 0 or b.std() == 0:
        return None, len(joined)
    return float(a.corr(b)), len(joined)


def verdict(recent: Optional[float], long: Optional[float], stress: Optional[float]) -> str:
    """Which windows the link held in -- the whole point of measuring three.

    The verdict turns on the **long** and **stress** windows, because those
    are the two a cap would be answering to: does this link persist, and does
    it survive the days that hurt. ``recent`` is context rather than a vote --
    a quiet quarter should not downgrade a link that a year of data and the
    last sell-off both agree on -- with one exception: a pair that is strong
    only in the recent window is ``emerging``, which is worth seeing early
    even though it is the weakest evidence here.

    Sign is ignored throughout. For a cap's purposes an inverse pair is as
    correlated as a direct one; what differs is whether the two positions
    hedge or compound, and this module cannot know that because exposure is
    tracked as an absolute dollar amount. Anything acting on a negative
    number has to deal with that first.
    """
    if long is None and stress is None:
        return UNMEASURED
    strong_recent = recent is not None and abs(recent) >= STRONG
    strong_long = long is not None and abs(long) >= STRONG
    strong_stress = stress is not None and abs(stress) >= STRONG
    if strong_stress and not strong_long:
        return STRESS_ONLY
    # Missing stress data is not evidence of diversification, so a link the
    # long window is sure about still counts -- the report prints the empty
    # stress column beside it.
    if strong_long and (strong_stress or stress is None):
        return STABLE
    if strong_long:
        return FADES
    if strong_recent:
        return EMERGING
    return WEAK


@dataclass(frozen=True)
class PairResult:
    """One pair, measured over every window, with the verdict that follows.

    ``excess_*`` are the same correlations with each side's market beta
    removed: co-movement the two positions have over and above both being
    exposed to the same stock market. For two equity groups that is the only
    number that says anything a gross-exposure cap does not already handle.
    """

    label: str
    left: tuple[str, ...]
    right: tuple[str, ...]
    recent: Optional[float]
    long: Optional[float]
    stress: Optional[float]
    excess_long: Optional[float]
    excess_stress: Optional[float]
    stress_days: int
    observations: int
    verdict: str
    #: The same classification applied to the excess numbers. For two equity
    #: groups this is the one worth reading: ``verdict`` can say "stable"
    #: about a pair whose entire co-movement is the market factor.
    excess_verdict: str = UNMEASURED
    #: The pair through each named drawdown, in ``CRISES`` order.
    crises: tuple[CrisisResult, ...] = ()

    def as_dict(self) -> dict:
        out = asdict(self)
        out["left"] = list(self.left)
        out["right"] = list(self.right)
        out["crises"] = [asdict(c) for c in self.crises]
        return out

    def crisis(self, short: str) -> Optional[CrisisResult]:
        return next((c for c in self.crises if c.short == short), None)

    @property
    def rank_by(self) -> float:
        """What sorts a list of these: the strongest thing the pair shows.

        Excess in the tail first, because that is the co-movement a group cap
        is the only limit standing against; raw numbers only when there is no
        excess to report.
        """
        for value in (self.excess_stress, self.excess_long, self.stress, self.long):
            if value is not None:
                return abs(value)
        return 0.0


def _measure_crisis(
    crisis: Crisis,
    a: pd.Series,
    b: pd.Series,
    ra: Optional[pd.Series],
    rb: Optional[pd.Series],
) -> CrisisResult:
    """One pair inside one named drawdown.

    The excess figure slices residuals fitted over the **whole** sample
    rather than re-fitting a beta inside the window. Covid'20 is 23 trading
    days; a beta estimated from 23 points and then subtracted would remove
    mostly noise, and the question being asked is anyway "given how these
    two normally track the market, did they move together here" rather than
    "what was their beta that month".
    """
    window_a, window_b = a.loc[crisis.start:crisis.end], b.loc[crisis.start:crisis.end]
    raw, days = correlation(window_a, window_b)
    excess = None
    if ra is not None and rb is not None:
        excess, _ = correlation(
            ra.loc[crisis.start:crisis.end], rb.loc[crisis.start:crisis.end]
        )
    return CrisisResult(crisis.label, crisis.short, raw, excess, days)


def measure_pair(
    returns: pd.DataFrame,
    label: str,
    left: Sequence[str],
    right: Sequence[str],
    stress: pd.Index,
    market: Optional[pd.Series] = None,
    crises: Sequence[Crisis] = CRISES,
) -> PairResult:
    """One named pair, raw and market-adjusted, over every window and crisis."""
    a, b = basket(returns, left), basket(returns, right)
    if a is None or b is None:
        return PairResult(label, tuple(left), tuple(right),
                          None, None, None, None, None, 0, 0,
                          UNMEASURED, UNMEASURED)
    long_r, n = correlation(a.tail(LONG_WINDOW), b.tail(LONG_WINDOW))
    recent_r, _ = correlation(a.tail(SHORT_WINDOW), b.tail(SHORT_WINDOW))
    stress_r, stress_n = (
        correlation(a.reindex(stress).dropna(), b.reindex(stress).dropna())
        if len(stress) else (None, 0)
    )

    excess_long = excess_stress = None
    ra = rb = None
    if market is not None:
        ra, rb = market_residual(a, market), market_residual(b, market)
        if ra is not None and rb is not None:
            excess_long, _ = correlation(ra.tail(LONG_WINDOW), rb.tail(LONG_WINDOW))
            if len(stress):
                excess_stress, _ = correlation(
                    ra.reindex(stress).dropna(), rb.reindex(stress).dropna()
                )
        else:
            ra = rb = None

    crisis_results = tuple(
        _measure_crisis(crisis, a, b, ra, rb) for crisis in crises
    )

    return PairResult(
        label=label, left=tuple(left), right=tuple(right),
        recent=recent_r, long=long_r, stress=stress_r,
        excess_long=excess_long, excess_stress=excess_stress,
        stress_days=stress_n, observations=n,
        verdict=verdict(recent_r, long_r, stress_r),
        excess_verdict=verdict(None, excess_long, excess_stress),
        crises=crisis_results,
    )


def cohesion(returns: pd.DataFrame, groups: Optional[dict] = None) -> list[dict]:
    """How tightly each existing exposure group actually moves together.

    The check nobody has run on ``EXPOSURE_GROUPS``. A group whose members
    average a low pairwise correlation is not one bet being made several ways
    -- it is several bets sharing a label, and capping it as one is leaving
    room on the table. A group near 1.0 is the opposite: Duration, measured,
    is the case that justified its own tighter cap.

    Reported as the mean of every pairwise correlation inside the group, over
    the long window, plus the loosest member -- the one whose correlation to
    the rest is weakest, which is where a group tends to be wrong.
    """
    groups = EXPOSURE_GROUPS if groups is None else groups
    window = returns.tail(LONG_WINDOW)
    out: list[dict] = []
    for group, tickers in groups.items():
        present = [t for t in tickers if t in window.columns]
        if len(present) < 2:
            continue
        matrix = window[present].corr()
        pairs = [
            float(matrix.iloc[i, j])
            for i in range(len(present))
            for j in range(i + 1, len(present))
            if np.isfinite(matrix.iloc[i, j])
        ]
        if not pairs:
            continue
        # The loosest member: lowest mean correlation to everyone else.
        to_rest = {
            t: float(matrix[t].drop(labels=[t]).mean())
            for t in present
            if np.isfinite(matrix[t].drop(labels=[t]).mean())
        }
        odd_one = min(to_rest, key=to_rest.get) if to_rest else None
        out.append({
            "group": group,
            "members": len(present),
            "mean_pairwise": round(float(np.mean(pairs)), 3),
            "min_pairwise": round(float(np.min(pairs)), 3),
            "loosest_member": odd_one,
            "loosest_member_r": round(to_rest[odd_one], 3) if odd_one else None,
        })
    return sorted(out, key=lambda row: row["mean_pairwise"])


def cross_group(returns: pd.DataFrame, stress: pd.Index,
                groups: Optional[dict] = None,
                market: Optional[pd.Series] = None) -> list[PairResult]:
    """Every pair of exposure groups, measured against each other.

    The gap the named hypotheses were guessing at. Each group's members are
    equal-weighted into one series and every pair of those series is
    measured, so a link nobody thought to write down still surfaces.

    Ranked by excess correlation in the tail rather than by the raw number.
    Ranking by raw would put "Technology vs Health care" at the top of every
    run and say only that both are equities, which is true, already capped by
    gross exposure, and not what anyone opened this report to find out.
    """
    groups = EXPOSURE_GROUPS if groups is None else groups
    names = [g for g in groups if basket(returns, groups[g]) is not None]
    results: list[PairResult] = []
    for i, left in enumerate(names):
        for right in names[i + 1:]:
            results.append(measure_pair(
                returns, f"{left} vs {right}", groups[left], groups[right],
                stress, market,
            ))
    return sorted(results, key=lambda r: r.rank_by, reverse=True)


def coverage(returns: pd.DataFrame, crises: Sequence[Crisis] = CRISES) -> dict:
    """Which tickers existed when -- without this the crisis table lies.

    Fetching from 2007 does not give 2007 data for eighty tickers. CPER,
    CORN, WEAT, SOYB, CANE, MCHI, INDA, KSA and XLC all launched in the
    2010s; the copper and grain funds did not exist in 2008 at all. A table
    that simply prints a blank for them invites the reader to compare a
    2008 number for one pair against a 2020 number for the next and treat
    the two as the same measurement.

    So the report says, per crisis, how many of the requested tickers had
    prices then -- and names the ones that never see 2008, because they are
    the reason a whole-history verdict is not available for every row.
    """
    first_day = {
        str(ticker): str(returns[ticker].first_valid_index().date())
        for ticker in returns.columns
        if returns[ticker].first_valid_index() is not None
    }
    per_crisis = []
    for crisis in crises:
        window = returns.loc[crisis.start:crisis.end]
        present = [c for c in window.columns if window[c].notna().any()]
        per_crisis.append({
            "label": crisis.label,
            "short": crisis.short,
            "start": crisis.start,
            "end": crisis.end,
            "days": int(len(window)),
            "tickers": len(present),
        })
    return {"first_day": first_day, "crises": per_crisis}


def report(returns: pd.DataFrame) -> dict:
    """Everything this module measures, as one structure."""
    stress = stress_index(returns)
    # Two different reference series, on purpose. The stress *window* is the
    # equity market's worst days, because "the day the book was hurting" is a
    # statement about equities and RSP is a stable, externally meaningful
    # definition of it. The *residual* is taken against the watchlist average,
    # because a single ETF is too noisy to subtract eighty times -- see
    # book_factor.
    market = book_factor(returns)
    named = [measure_pair(returns, label, left, right, stress, market)
             for label, left, right in HYPOTHESES]
    crossed = cross_group(returns, stress, market=market)
    return {
        "observations": int(len(returns)),
        "first_day": str(returns.index.min().date()) if len(returns) else None,
        "last_day": str(returns.index.max().date()) if len(returns) else None,
        "tickers": int(returns.shape[1]),
        "stress_days": int(len(stress)),
        "stress_benchmark": STRESS_BENCHMARK,
        "market_adjusted": market is not None,
        "windows": {"recent": SHORT_WINDOW, "long": LONG_WINDOW,
                    "strong_threshold": STRONG},
        "coverage": coverage(returns),
        "hypotheses": [p.as_dict() for p in named],
        "group_cohesion": cohesion(returns),
        "cross_group": [p.as_dict() for p in crossed],
    }


# --------------------------------------------------------------------------- #
# The edge: prices in, and the report out
# --------------------------------------------------------------------------- #


def fetch_closes(tickers: Sequence[str], start: str = "2007-01-01") -> pd.DataFrame:
    """Daily adjusted closes, one column per ticker.

    The only function here that touches the network, and it is imported
    lazily so every test in this package runs without it -- the same
    arrangement ``app/market_data.py`` uses. Tickers that return nothing are
    dropped and named in the report rather than failing the run: a watchlist
    of eighty will eventually contain one delisted ETN, and that should cost
    one row, not the whole measurement.
    """
    import yfinance as yf  # imported lazily so tests never need it

    frame = yf.download(
        list(tickers), start=start, interval="1d",
        auto_adjust=True, progress=False, group_by="column",
    )
    if frame is None or frame.empty:
        raise RuntimeError("yfinance returned no data for any ticker")
    closes = frame["Close"] if isinstance(frame.columns, pd.MultiIndex) else frame
    return closes.dropna(axis=1, how="all")


def render(data: dict) -> str:
    """The report as something a person can read in one screen."""
    lines = [
        f"{data['tickers']} tickers, {data['observations']} days "
        f"({data['first_day']} to {data['last_day']}).",
        f"Stress window: the worst {STRESS_QUANTILE:.0%} of days for "
        f"{data['stress_benchmark']} -- {data['stress_days']} days.",
        f"A link is |r| >= {STRONG}. 'excess' is correlation after each side's "
        f"beta to the watchlist average is removed.",
        "",
        "## The stories, adjudicated",
        "",
        f"{'pair':<40} {'recent':>7} {'long':>7} {'stress':>7} {'excess':>7}  verdict",
        f"{'-' * 40} {'-' * 7} {'-' * 7} {'-' * 7} {'-' * 7}  {'-' * 16}",
    ]

    def cell(value: Optional[float]) -> str:
        return f"{value:+.2f}" if isinstance(value, float) else "   --"

    for row in data["hypotheses"]:
        lines.append(
            f"{row['label']:<40} {cell(row['recent']):>7} {cell(row['long']):>7} "
            f"{cell(row['stress']):>7} {cell(row['excess_stress']):>7}  {row['verdict']}"
        )

    crisis_cols = [c["short"] for c in data["coverage"]["crises"]]
    if crisis_cols:
        lines += [
            "",
            "## The same pairs, crisis by crisis (excess r)",
            "",
            "Each drawdown measured on its own, because they had different "
            "causes and a link that holds in one need not hold in the next. "
            "A dash means one side did not exist yet.",
            "",
            f"{'pair':<40} " + " ".join(f"{c:>9}" for c in crisis_cols),
            f"{'-' * 40} " + " ".join("-" * 9 for _ in crisis_cols),
        ]
        for row in data["hypotheses"]:
            by_short = {c["short"]: c for c in row["crises"]}
            cells = " ".join(
                f"{cell(by_short.get(c, {}).get('excess')):>9}" for c in crisis_cols
            )
            lines.append(f"{row['label']:<40} {cells}")
        lines += [
            "",
            f"{'tickers with data':<40} "
            + " ".join(f"{c['tickers']:>9}" for c in data["coverage"]["crises"]),
        ]

    lines += [
        "",
        "## Do the existing groups hold together?",
        "",
        f"{'group':<26} {'members':>7} {'mean r':>7} {'min r':>7}  loosest member",
        f"{'-' * 26} {'-' * 7} {'-' * 7} {'-' * 7}  {'-' * 30}",
    ]
    for row in data["group_cohesion"]:
        loose = (f"{name_for(row['loosest_member'])} ({row['loosest_member']}) "
                 f"{row['loosest_member_r']:+.2f}" if row["loosest_member"] else "")
        lines.append(
            f"{row['group']:<26} {row['members']:>7} {row['mean_pairwise']:>7.2f} "
            f"{row['min_pairwise']:>7.2f}  {loose}"
        )

    def excess_of(row: dict) -> float:
        for key in ("excess_stress", "excess_long"):
            if isinstance(row.get(key), float):
                return abs(row[key])
        return 0.0

    linked = [r for r in data["cross_group"] if excess_of(r) >= STRONG]
    lines += [
        "",
        "## Groups that move together beyond the market, but are capped apart",
        "",
        f"({len(linked)} of {len(data['cross_group'])} group pairs clear "
        f"|excess r| >= {STRONG}; ranked by the tail)",
        "",
        f"{'pair':<48} {'long':>7} {'stress':>7} {'ex.long':>8} {'ex.strs':>8}  "
        f"verdict (on excess)",
        f"{'-' * 48} {'-' * 7} {'-' * 7} {'-' * 8} {'-' * 8}  {'-' * 18}",
    ]
    for row in linked[:25]:
        lines.append(
            f"{row['label']:<48} {cell(row['long']):>7} {cell(row['stress']):>7} "
            f"{cell(row['excess_long']):>8} {cell(row['excess_stress']):>8}  "
            f"{row['excess_verdict']}"
        )
    if not linked:
        lines.append(
            "(none -- every group pair's co-movement is explained by the market "
            "factor the gross cap already bounds)"
        )

    lines += [
        "",
        "Nothing here changes a cap. A finding is promoted by editing",
        "EXPOSURE_GROUPS or EXPOSURE_GROUP_CAP_OVERRIDES by hand, with the",
        "number above written into the comment beside it.",
    ]
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Measure what actually moves together on this watchlist."
    )
    parser.add_argument(
        "--start", default="2007-01-01",
        help="first day to fetch (default: 2007-01-01, to reach the 2008 crisis)",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--tickers", default="",
                        help="comma-separated override of the watchlist")
    args = parser.parse_args(argv)

    tickers = (
        tuple(t.strip().upper() for t in args.tickers.split(",") if t.strip())
        or DEFAULT_WATCHLIST
    )
    closes = fetch_closes(tickers, start=args.start)
    data = report(daily_returns(closes))
    missing = sorted(set(tickers) - set(closes.columns))
    data["missing"] = missing
    print(json.dumps(data, indent=2) if args.as_json else render(data))
    if missing:
        print(f"\nNo data for: {', '.join(missing)}")
    return 0


__all__ = [
    "SHORT_WINDOW", "LONG_WINDOW", "STRESS_QUANTILE", "STRESS_BENCHMARK",
    "STRONG", "MIN_OBSERVATIONS",
    "STABLE", "STRESS_ONLY", "FADES", "WEAK", "UNMEASURED",
    "HYPOTHESES", "CRISES", "Crisis", "CrisisResult", "PairResult",
    "daily_returns", "stress_index", "basket", "book_factor", "market_residual",
    "correlation", "verdict", "measure_pair", "cohesion", "cross_group",
    "coverage", "report",
    "fetch_closes", "render", "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
