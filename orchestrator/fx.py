"""The currency risk that does not show up anywhere in the P&L.

The account is denominated in dollars. Your life is denominated in shekels.
Those are different currencies, and the gap between them is a real position
you hold whether or not anything in this system acknowledges it: a 10% year in
USD alongside a 10% fall in USD/ILS is a flat year in the only unit that buys
groceries.

Nothing else in this codebase would ever have told you that. The journal, the
scorer and the backtest all measure dollars, so an FX move is invisible to
every one of them -- it does not reduce a return, it silently redenominates
it.

Why this module measures rather than hedges
--------------------------------------------
It cannot hedge. There is no route from an Alpaca equities account to a
shekel:

- Alpaca trades ``us_equity``, ``us_option`` and ``crypto``. No spot FX, no
  forwards, no futures. This is read off the SDK's own AssetClass enum.
- **No US-listed ILS currency fund exists.** There are dollar-index funds
  (UUP, UDN) and single-currency funds for the majors (FXE euro, FXY yen,
  FXB sterling). The shekel is not among them.
- The "currency-hedged" ETFs -- HEFA, DBEF and their relatives -- hedge a
  *foreign* currency back into dollars. That is the opposite direction: they
  remove EUR or JPY exposure for a dollar-based holder. They do nothing for a
  dollar portfolio held by a shekel-based person.
- UDN is the closest proxy and is not close. It tracks a basket that is 58%
  euro and contains no shekel at all, so hedging USD/ILS with it is a bet on
  the euro wearing a hedge's clothing. A partial hedge against the wrong
  index is a second position, not less risk.

So the useful thing is to make the exposure visible and let it inform
decisions taken outside this account -- at a bank, with a forward, or by
simply holding fewer dollars. An honest number beats a hedge that does not
hedge.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

#: Yahoo's symbol for dollars per shekel. ``ILS=X`` quotes USD/ILS -- how many
#: shekels one dollar buys -- so it *rises* when the dollar strengthens.
USD_ILS_SYMBOL = "ILS=X"

#: How much history to pull. Enough to state a change over a period rather
#: than just a level, since the level alone says nothing about risk.
LOOKBACK = "3mo"


@dataclass(frozen=True)
class FxRate:
    """One observation of USD/ILS, or a named reason there isn't one."""

    symbol: str = USD_ILS_SYMBOL
    rate: Optional[float] = None
    change_3mo_pct: Optional[float] = None
    gap: str = ""

    @property
    def ok(self) -> bool:
        return self.rate is not None

    def as_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "rate": self.rate,
            "change_3mo_pct": self.change_3mo_pct,
            "gap": self.gap,
        }

    def as_lines(self) -> list[str]:
        if not self.ok:
            return [f"- USD/ILS unavailable: {self.gap}"]
        lines = [f"- USD/ILS: {self.rate:.4f} shekels per dollar"]
        if self.change_3mo_pct is not None:
            direction = "stronger" if self.change_3mo_pct > 0 else "weaker"
            lines.append(
                f"- dollar {direction} by {abs(self.change_3mo_pct):.1f}% over 3 months"
            )
        return lines


def fetch_rate(symbol: str = USD_ILS_SYMBOL, lookback: str = LOOKBACK) -> FxRate:
    """Current USD/ILS and its recent move. Never raises.

    A failure here must not take down a cycle that produced perfectly good
    signals -- the exposure is worth reporting, but it is not worth trading
    on, so a missing rate degrades to a named gap like every other source.
    """
    try:
        import yfinance as yf

        bars = yf.Ticker(symbol).history(period=lookback, interval="1d")
    except Exception as exc:  # noqa: BLE001 - any failure is just a gap
        return FxRate(symbol=symbol, gap=f"fetch failed: {type(exc).__name__}")

    if bars is None or bars.empty or "Close" not in bars.columns:
        return FxRate(symbol=symbol, gap="no bars returned")

    closes = [float(c) for c in bars["Close"].dropna()]
    if not closes:
        return FxRate(symbol=symbol, gap="no closes in the window")

    change = None
    if len(closes) > 1 and closes[0]:
        change = (closes[-1] / closes[0] - 1) * 100

    return FxRate(
        symbol=symbol,
        rate=round(closes[-1], 4),
        change_3mo_pct=round(change, 2) if change is not None else None,
    )


def in_shekels(usd_amount: float, rate: float) -> float:
    """Convert a dollar figure at a given USD/ILS rate."""
    return usd_amount * rate


def shekel_return_pct(usd_return_pct: float, fx_change_pct: float) -> float:
    """What a dollar return was worth to a shekel-based holder.

    Returns compound rather than add: a 10% dollar gain alongside a 10% fall
    in the dollar is -1%, not 0%. The difference is small at these sizes and
    grows with both.
    """
    return ((1 + usd_return_pct / 100) * (1 + fx_change_pct / 100) - 1) * 100


__all__ = [
    "USD_ILS_SYMBOL",
    "FxRate",
    "fetch_rate",
    "in_shekels",
    "shekel_return_pct",
]
