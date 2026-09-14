#!/usr/bin/env python3
"""Does every ticker on the watchlist actually exist and trade?

    python backtest/verify_tickers.py
    python backtest/verify_tickers.py --json

The watchlist was written from knowledge, not from market data -- the sandbox
that wrote it cannot reach Yahoo. Several holdings are also the kind of thing
that quietly stops existing: ETNs get called by their issuer, and small funds
close and delist. A symbol that no longer resolves would fail every cycle for
that ticker, silently, as a "no bars" gap.

So this checks. It fetches recent bars for every ticker and reports three
things per symbol: whether it resolves at all, how thinly it trades, and how
volatile it is -- the last because the position caps are justified by relative
volatility, and a holding far outside the expected range is an argument for
re-tuning its cap.

Read-only. No orders, no LLM, no credentials.
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

from config.instruments import (  # noqa: E402
    BROAD_FUNDS,
    COMMODITY_FUNDS,
    SINGLE_NAMES,
    InstrumentKind,
    kind_for,
)

#: Below this median dollar volume a stop is likely to fill badly, and the
#: spread becomes a real cost rather than a rounding error.
THIN_DOLLAR_VOLUME = 5_000_000.0


@dataclass(frozen=True)
class Check:
    ticker: str
    kind: str
    resolved: bool
    bars: int = 0
    last_close: Optional[float] = None
    median_dollar_volume: Optional[float] = None
    daily_vol_pct: Optional[float] = None
    note: str = ""

    @property
    def thin(self) -> bool:
        return (
            self.median_dollar_volume is not None
            and self.median_dollar_volume < THIN_DOLLAR_VOLUME
        )

    def as_dict(self) -> dict:
        return {
            "ticker": self.ticker, "kind": self.kind, "resolved": self.resolved,
            "bars": self.bars, "last_close": self.last_close,
            "median_dollar_volume": self.median_dollar_volume,
            "daily_vol_pct": self.daily_vol_pct, "thin": self.thin,
            "note": self.note,
        }


def check(ticker: str, period: str = "3mo") -> Check:
    """Never raises: one bad symbol must not void the whole report."""
    kind = kind_for(ticker).value
    try:
        import yfinance as yf

        bars = yf.Ticker(ticker).history(period=period, interval="1d", auto_adjust=False)
    except Exception as exc:  # noqa: BLE001 - any failure is just "could not check"
        return Check(ticker, kind, False, note=f"fetch failed: {type(exc).__name__}")

    if bars is None or bars.empty or "Close" not in bars.columns:
        return Check(ticker, kind, False, note="no bars returned -- delisted or wrong symbol")

    closes = [float(c) for c in bars["Close"].dropna()]
    if len(closes) < 2:
        return Check(ticker, kind, False, bars=len(closes), note="too few bars to judge")

    returns = [closes[i] / closes[i - 1] - 1 for i in range(1, len(closes))]
    dollar_volume = None
    if "Volume" in bars.columns:
        volumes = [
            float(v) * float(c)
            for v, c in zip(bars["Volume"], bars["Close"])
            if v == v and c == c
        ]
        dollar_volume = statistics.median(volumes) if volumes else None

    return Check(
        ticker=ticker, kind=kind, resolved=True, bars=len(closes),
        last_close=round(closes[-1], 2),
        median_dollar_volume=round(dollar_volume) if dollar_volume else None,
        daily_vol_pct=round(statistics.pstdev(returns) * 100, 2),
    )


def render(results: list[Check]) -> str:
    lines = [
        "TICKER VERIFICATION",
        "",
        f"{'ticker':<8}{'kind':<16}{'ok':<5}{'last':>9}{'$vol/day':>14}{'daily vol':>11}",
    ]
    for r in results:
        vol = "--" if r.median_dollar_volume is None else f"${r.median_dollar_volume/1e6:,.1f}M"
        lines.append(
            f"{r.ticker:<8}{r.kind:<16}{'yes' if r.resolved else 'NO':<5}"
            f"{('--' if r.last_close is None else f'{r.last_close:,.2f}'):>9}"
            f"{vol:>14}"
            f"{('--' if r.daily_vol_pct is None else f'{r.daily_vol_pct:.2f}%'):>11}"
        )

    broken = [r for r in results if not r.resolved]
    if broken:
        lines += ["", "DOES NOT RESOLVE -- these would fail every cycle, silently:"]
        lines += [f"  {r.ticker}: {r.note}" for r in broken]

    thin = [r for r in results if r.thin]
    if thin:
        lines += [
            "",
            f"THIN (under ${THIN_DOLLAR_VOLUME/1e6:.0f}M/day) -- wide spreads, and a stop",
            "can fill well below where it was placed:",
        ]
        lines += [
            f"  {r.ticker}: ${r.median_dollar_volume/1e6:,.1f}M/day" for r in thin
        ]

    # The caps are justified by relative volatility, so a holding well outside
    # the expected range is an argument for re-tuning its cap rather than a
    # curiosity.
    equities = [r.daily_vol_pct for r in results
                if r.kind == InstrumentKind.EQUITY.value and r.daily_vol_pct]
    funds = [r.daily_vol_pct for r in results
             if r.kind == InstrumentKind.BROAD_FUND.value and r.daily_vol_pct]
    commodities = [r.daily_vol_pct for r in results
                   if r.kind == InstrumentKind.COMMODITY_FUND.value and r.daily_vol_pct]
    if equities and funds:
        lines += [
            "",
            "MEDIAN DAILY VOLATILITY BY KIND",
            f"  single name      {statistics.median(equities):.2f}%",
            f"  broad fund       {statistics.median(funds):.2f}%",
        ]
        if commodities:
            lines.append(f"  commodity fund   {statistics.median(commodities):.2f}%")
        ratio = statistics.median(equities) / statistics.median(funds)
        lines += [
            "",
            f"A single name is {ratio:.1f}x as volatile as a broad fund here.",
            "Risk per trade scales as cap/volatility, so the broad-fund cap is",
            f"defensible up to about {ratio:.1f}x the single-name cap on these numbers.",
        ]
        if commodities:
            c_ratio = statistics.median(commodities) / statistics.median(equities)
            lines.append(
                f"A commodity fund is {c_ratio:.1f}x as volatile as a single name, "
                f"which is the case for capping it {'below' if c_ratio > 1 else 'near'} one."
            )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify every watchlist ticker resolves.")
    parser.add_argument("--period", default="3mo")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)

    results = [
        check(t, args.period) for t in SINGLE_NAMES + BROAD_FUNDS + COMMODITY_FUNDS
    ]
    print(json.dumps([r.as_dict() for r in results], indent=2) if args.as_json
          else render(results))

    # Non-zero when something does not resolve, so a scheduled run cannot
    # report success while a holding is quietly broken.
    return 1 if any(not r.resolved for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
