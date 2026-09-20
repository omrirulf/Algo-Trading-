"""Does it pay to lean in when everyone is afraid -- and what does the sizing do anyway?

Two questions, deliberately answered in one place because the answer to the
second changes what the first one means.

**Does buying fear work?** "The dare is the winner" is a real effect -- the
volatility risk premium is among the more durable things in markets -- but
the level of the VIX cannot by itself say which side of a crash you are
standing on. The VIX passed 40 in September 2008 and the market fell another
40%; it passed 40 in April 2020 and buying was excellent. So this module
never reports an average without the tail beside it, and it splits every
regime by whether volatility was *rising or falling* at the time, which is
the distinction the level alone hides.

**What does the risk engine already do in that regime?** Position size comes
from a cap in dollars (``risk_engine.calculate_position_size`` -- volatility
is nowhere in it) and the stop comes from ``ATR_STOP_MULTIPLIER x ATR``. So
when volatility rises the position stays the same size and the stop moves
further away, and the dollars at risk per trade rise with it. Nobody chose
that; it falls out of the two rules meeting. Before deciding to be *more*
aggressive in a high-VIX regime it is worth knowing how much more aggressive
the book already is, and that is what ``risk_per_trade_by_regime`` measures.

Like every other module in ``analysis/``, this one cannot change a cap or
place an order: it prints, and a person decides. CI enforces both.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Optional, Sequence

import numpy as np
import pandas as pd

from config import settings as cfg

#: Yahoo's ticker for the CBOE volatility index.
VIX_TICKER: str = "^VIX"

#: What the market is, for the forward-return question. RSP rather than SPY
#: for the same reason the watchlist holds it: a cap-weighted index is a
#: concentrated technology bet wearing a diversified label.
MARKET_TICKER: str = "RSP"

#: VIX bands. Not evenly spaced, because the interesting question is not
#: "what does a slightly elevated VIX do" but "what happens out in the tail",
#: and the tail is thin: above 40 is a few dozen days in twenty years.
VIX_BANDS: tuple[tuple[str, float, float], ...] = (
    ("calm (<15)", 0.0, 15.0),
    ("normal (15-20)", 15.0, 20.0),
    ("uneasy (20-30)", 20.0, 30.0),
    ("afraid (30-40)", 30.0, 40.0),
    ("panic (40+)", 40.0, float("inf")),
)

#: Forward horizons, in trading days: about a week, a month, a quarter.
HORIZONS: tuple[tuple[str, int], ...] = (("1w", 5), ("1m", 21), ("3m", 63))

#: Trailing window for "is volatility rising or falling". Five days: long
#: enough not to be one day's noise, short enough to still be inside the
#: move rather than describing the one before it.
TREND_WINDOW: int = 5

#: A regime needs at least this many observations before its numbers are
#: worth printing. The panic band is thin by construction and a mean over
#: eleven days is an anecdote.
MIN_DAYS: int = 30


@dataclass(frozen=True)
class RegimeResult:
    """One VIX band, one horizon: the average, and the tail beside it."""

    band: str
    horizon: str
    days: int
    mean_pct: Optional[float]
    median_pct: Optional[float]
    worst_pct: Optional[float]
    best_pct: Optional[float]
    share_positive: Optional[float]

    def as_dict(self) -> dict:
        return asdict(self)


def forward_return(closes: pd.Series, horizon: int) -> pd.Series:
    """Return from each day to ``horizon`` trading days later, as a fraction.

    Shifted backwards, so the value on day *t* is what a position opened at
    *t* would have made. The last ``horizon`` days are NaN because their
    future has not happened -- dropped rather than filled, since filling
    them would be inventing the one thing this measures.
    """
    if horizon < 1:
        raise ValueError(f"horizon must be >= 1, got {horizon}")
    return closes.shift(-horizon) / closes - 1.0


def vix_trend(vix: pd.Series, window: int = TREND_WINDOW) -> pd.Series:
    """+1 where the VIX is above where it was ``window`` days ago, else -1.

    The distinction the level cannot make. A VIX of 40 on the way up and a
    VIX of 40 on the way down are the same reading and, historically, very
    different trades.
    """
    return np.sign(vix - vix.shift(window)).fillna(0.0)


def by_regime(
    vix: pd.Series,
    market: pd.Series,
    bands: Sequence[tuple[str, float, float]] = VIX_BANDS,
    horizons: Sequence[tuple[str, int]] = HORIZONS,
    min_days: int = MIN_DAYS,
) -> list[RegimeResult]:
    """Forward market returns, grouped by the VIX band on the day of entry."""
    aligned = pd.concat([vix.rename("vix"), market.rename("mkt")], axis=1).dropna()
    results: list[RegimeResult] = []
    for label, low, high in bands:
        in_band = (aligned["vix"] >= low) & (aligned["vix"] < high)
        for horizon_label, horizon in horizons:
            fwd = forward_return(aligned["mkt"], horizon)[in_band].dropna()
            if len(fwd) < min_days:
                results.append(RegimeResult(label, horizon_label, len(fwd),
                                            None, None, None, None, None))
                continue
            results.append(RegimeResult(
                label, horizon_label, len(fwd),
                round(float(fwd.mean()) * 100, 2),
                round(float(fwd.median()) * 100, 2),
                round(float(fwd.min()) * 100, 2),
                round(float(fwd.max()) * 100, 2),
                round(float((fwd > 0).mean()) * 100, 1),
            ))
    return results


def by_regime_and_trend(
    vix: pd.Series,
    market: pd.Series,
    bands: Sequence[tuple[str, float, float]] = VIX_BANDS,
    horizons: Sequence[tuple[str, int]] = HORIZONS,
    window: int = TREND_WINDOW,
    min_days: int = MIN_DAYS,
) -> dict:
    """The same, split by whether volatility was rising or falling that day.

    This is the split that decides whether "buy fear" is a rule or a
    coin-flip. If the two halves of a band disagree, the level alone is not
    a signal and a rule built on it is a rule built on an average of two
    different things.
    """
    trend = vix_trend(vix, window)
    out: dict = {}
    for direction, mask in (("rising", trend > 0), ("falling", trend < 0)):
        out[direction] = [
            r.as_dict() for r in by_regime(
                vix[mask], market[mask], bands, horizons, min_days,
            )
        ]
    return out


def true_range(ohlc: pd.DataFrame) -> pd.Series:
    """Wilder's true range per bar, as a fraction of that bar's close.

    The same quantity ``market_data.calculate_atr`` smooths, left unsmoothed
    and expressed relative to price so it can be compared across tickers and
    across twenty years of price levels.

    The first bar is dropped, exactly as ``calculate_atr`` drops it: two of
    the three terms in a true range are measured against the *previous*
    close, so the first bar can only ever report its own high-low span. That
    is not a small true range, it is an incomplete one, and averaging it in
    would quietly bias every window that starts on a gap.
    """
    high, low, close = ohlc["High"], ohlc["Low"], ohlc["Close"]
    prev = close.shift(1)
    tr = pd.concat([high - low, (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    return (tr / close).iloc[1:].dropna()


def risk_per_trade_by_regime(
    vix: pd.Series,
    ohlc: pd.DataFrame,
    cap_pct: float = cfg.MAX_BROAD_FUND_PCT,
    multiplier: float = cfg.ATR_STOP_MULTIPLIER,
    bands: Sequence[tuple[str, float, float]] = VIX_BANDS,
    min_days: int = MIN_DAYS,
) -> list[dict]:
    """What one trade stands to lose, by VIX band, as a share of the account.

    The arithmetic the engine performs without anyone writing it down:

        size in dollars   = equity x cap_pct              (volatility absent)
        stop distance     = multiplier x ATR
        dollars at risk   = size x (stop distance / price)
                          = equity x cap_pct x multiplier x (ATR / price)

    So risk per trade is proportional to ``ATR / price``, which is exactly
    what rises in a panic. The cap holds the *position* constant and lets the
    *risk* float, which is the opposite of what a cap is usually assumed to
    do.
    """
    tr = true_range(ohlc)
    aligned = pd.concat([vix.rename("vix"), tr.rename("tr")], axis=1).dropna()
    rows = []
    for label, low, high in bands:
        window = aligned[(aligned["vix"] >= low) & (aligned["vix"] < high)]["tr"]
        if len(window) < min_days:
            rows.append({"band": label, "days": len(window),
                         "median_tr_pct": None, "risk_per_trade_pct": None})
            continue
        median_tr = float(window.median())
        rows.append({
            "band": label,
            "days": len(window),
            "median_tr_pct": round(median_tr * 100, 2),
            "risk_per_trade_pct": round(cap_pct * multiplier * median_tr * 100, 3),
        })
    return rows


def report(vix: pd.Series, market: pd.Series, ohlc: Optional[pd.DataFrame] = None) -> dict:
    """Everything this module measures, as one structure."""
    aligned = pd.concat([vix.rename("vix"), market.rename("mkt")], axis=1).dropna()
    return {
        "observations": int(len(aligned)),
        "first_day": str(aligned.index.min().date()) if len(aligned) else None,
        "last_day": str(aligned.index.max().date()) if len(aligned) else None,
        "market": MARKET_TICKER,
        "trend_window": TREND_WINDOW,
        "min_days": MIN_DAYS,
        "by_regime": [r.as_dict() for r in by_regime(vix, market)],
        "by_regime_and_trend": by_regime_and_trend(vix, market),
        "risk_per_trade": (
            risk_per_trade_by_regime(vix, ohlc) if ohlc is not None else None
        ),
        "cap_pct": cfg.MAX_BROAD_FUND_PCT,
        "atr_multiplier": cfg.ATR_STOP_MULTIPLIER,
    }


def fetch(start: str = "2007-01-01") -> tuple[pd.Series, pd.Series, pd.DataFrame]:
    """VIX closes, market closes, and the market's OHLC bars.

    The only function here that touches the network, imported lazily so every
    test in this package runs without it -- the same arrangement
    ``analysis/correlations.py`` and ``app/market_data.py`` use.
    """
    import yfinance as yf  # imported lazily so tests never need it

    frame = yf.download([VIX_TICKER, MARKET_TICKER], start=start, interval="1d",
                        auto_adjust=True, progress=False, group_by="ticker")
    if frame is None or frame.empty:
        raise RuntimeError("yfinance returned no data")
    vix = frame[VIX_TICKER]["Close"].dropna()
    ohlc = frame[MARKET_TICKER][["High", "Low", "Close"]].dropna()
    return vix, ohlc["Close"], ohlc


def render(data: dict) -> str:
    """The report as something a person can read in one screen."""

    def cell(value: Optional[float], width: int = 8, suffix: str = "") -> str:
        return f"{value:+.2f}{suffix}".rjust(width) if isinstance(value, float) else "--".rjust(width)

    lines = [
        f"VIX regimes against {data['market']}, {data['observations']} days "
        f"({data['first_day']} to {data['last_day']}).",
        "",
        "## Does buying fear pay? Forward returns by VIX band",
        "",
        "Mean is the case for leaning in; worst is the case against. A band "
        f"with fewer than {data['min_days']} days is left blank rather than "
        "averaged into a number that reads like evidence.",
        "",
        f"{'band':<16} {'horiz':>5} {'days':>5} {'mean':>8} {'median':>8} "
        f"{'worst':>8} {'best':>8} {'win%':>6}",
        f"{'-' * 16} {'-' * 5} {'-' * 5} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 6}",
    ]
    for row in data["by_regime"]:
        win = f"{row['share_positive']:.0f}%".rjust(6) if isinstance(row["share_positive"], float) else "--".rjust(6)
        lines.append(
            f"{row['band']:<16} {row['horizon']:>5} {row['days']:>5} "
            f"{cell(row['mean_pct'])} {cell(row['median_pct'])} "
            f"{cell(row['worst_pct'])} {cell(row['best_pct'])} {win}"
        )

    trend = data.get("by_regime_and_trend") or {}
    if trend:
        lines += [
            "",
            f"## The same bands, split by whether the VIX was rising or falling "
            f"({data['trend_window']}d)",
            "",
            "The split the level cannot make. A VIX of 40 on the way up and a "
            "VIX of 40 on the way down read identically and are not the same "
            "trade. Where the two halves disagree, the level alone is not a "
            "signal.",
            "",
            f"{'band':<16} {'horiz':>5} {'rising mean':>12} {'rising worst':>13} "
            f"{'falling mean':>13} {'falling worst':>14}",
            f"{'-' * 16} {'-' * 5} {'-' * 12} {'-' * 13} {'-' * 13} {'-' * 14}",
        ]
        rising = {(r["band"], r["horizon"]): r for r in trend.get("rising", [])}
        falling = {(r["band"], r["horizon"]): r for r in trend.get("falling", [])}
        for key in rising:
            up, down = rising[key], falling.get(key, {})
            lines.append(
                f"{key[0]:<16} {key[1]:>5} {cell(up.get('mean_pct'), 12)} "
                f"{cell(up.get('worst_pct'), 13)} {cell(down.get('mean_pct'), 13)} "
                f"{cell(down.get('worst_pct'), 14)}"
            )

    risk = data.get("risk_per_trade")
    if risk:
        lines += [
            "",
            "## What one trade already risks, by VIX band",
            "",
            f"Size is {data['cap_pct']:.0%} of equity and does not move with "
            f"volatility -- the stop does, at {data['atr_multiplier']}x ATR. So the "
            "dollars at risk per trade are whatever the band below says, and "
            "nobody chose them.",
            "",
            f"{'band':<16} {'days':>6} {'daily range':>12} {'risk per trade':>15}",
            f"{'-' * 16} {'-' * 6} {'-' * 12} {'-' * 15}",
        ]
        for row in risk:
            tr = f"{row['median_tr_pct']:.2f}%".rjust(12) if isinstance(row["median_tr_pct"], float) else "--".rjust(12)
            rp = f"{row['risk_per_trade_pct']:.2f}%".rjust(15) if isinstance(row["risk_per_trade_pct"], float) else "--".rjust(15)
            lines.append(f"{row['band']:<16} {row['days']:>6} {tr} {rp}")
        measured = [r["risk_per_trade_pct"] for r in risk
                    if isinstance(r.get("risk_per_trade_pct"), float)]
        if len(measured) >= 2:
            lines += [
                "",
                f"  Calmest band to most fearful: {measured[0]:.2f}% -> "
                f"{measured[-1]:.2f}% of the account per trade, "
                f"about {measured[-1] / measured[0]:.1f}x, at the same position size.",
            ]

    lines += [
        "",
        "Nothing here changes a cap or a prompt. A finding is promoted by a",
        "person editing config/settings.py or the system prompt by hand, with",
        "the number above written into the comment beside it.",
    ]
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Measure whether leaning into fear pays, and what the book already risks."
    )
    parser.add_argument("--start", default="2007-01-01",
                        help="first day to fetch (default: 2007-01-01)")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)

    vix, market, ohlc = fetch(start=args.start)
    data = report(vix, market, ohlc)
    print(json.dumps(data, indent=2) if args.as_json else render(data))
    return 0


__all__ = [
    "VIX_TICKER", "MARKET_TICKER", "VIX_BANDS", "HORIZONS", "TREND_WINDOW",
    "MIN_DAYS", "RegimeResult",
    "forward_return", "vix_trend", "by_regime", "by_regime_and_trend",
    "true_range", "risk_per_trade_by_regime", "report", "fetch", "render", "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
