"""Exploratory arm: cluster buying by insiders, with nothing fitted.

The thesis: when several of a company's own officers and directors buy its
shares on the open market with their own money inside the same window, the
stock tends to do well over the following months. Lakonishok and Lee
("Are Insider Trades Informative?", *Review of Financial Studies* 2001)
found the effect in six-month aggregates of net insider purchases; Cohen,
Malloy and Pomorski ("Decoding Inside Information", *Journal of Finance*
2012) found it concentrated in *opportunistic* buys rather than routine
ones. Sales carry almost no information -- an insider sells for a house,
a tax bill or diversification -- so only the buying side is a signal.

The rule
--------
BULLISH when, in the ``WINDOW_DAYS`` before the line, at least
``MIN_DISTINCT_BUYERS`` distinct insiders made open-market purchases and
the open-market shares bought exceed the open-market shares sold. Otherwise
NEUTRAL. Never BEARISH: selling is not evidence. Conviction is fixed at
``CONVICTION``, above the engine's floor, so every call is a scoreable
trade.

What counts as a purchase
-------------------------
Only what ``orchestrator/insiders.py`` already classifies as one: a Form 4
transaction whose text says "purchase". Stock awards, option exercises,
gifts and tax withholding are excluded there, with tests, before this rule
ever sees the list. Two further exclusions are this rule's own, because the
data can name them and the thesis is about *people*: the issuer buying back
its own shares (``role`` "Issuer"), and a ten-per-cent holder (``role``
containing "Owner"), which is a fund rebalancing, not a leader's view.

Why every number here is fixed
------------------------------
180 days is the six-month aggregation of Lakonishok and Lee and is also the
window the prompt's own snapshot carries, so the arm reads exactly what the
model read. Two buyers is the smallest number that is a cluster. Nothing
was chosen by looking at what this journal would then say, and nothing
will be moved by it.

Why exploratory
---------------
Four in five names on the watchlist are funds, which have no insiders, and
a cluster of buys is rare on the rest. The arm is NEUTRAL on nearly every
line. It is scored only on the lines where it took a side, paired against
the model and the momentum rule on those same lines, at the race's horizon
and at twenty sessions, because the effect it is named after plays out over
months. It reports "too few" until the pre-registered minimum and can never
change the main decision.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Optional

from app.schemas import Bias, LLMSignal
from orchestrator.insiders import InsiderSnapshot, InsiderTrade

NAME = "insiders"

#: Calendar days before the line inside which a purchase counts.
WINDOW_DAYS = 180
#: The smallest number of distinct open-market buyers that is a cluster.
MIN_DISTINCT_BUYERS = 2
#: Fixed, and above MIN_CONVICTION, so every call is a trade the scorer sees.
CONVICTION = 0.50

#: Roles that are not a person acting on a view.
_NOT_A_LEADER = ("issuer", "owner")


def signal_for(ticker: str, snapshot: Optional[InsiderSnapshot], day: Optional[date]) -> LLMSignal:
    """The insider arm's call for one ticker, from the snapshot the model saw."""
    if snapshot is None:
        return _neutral(ticker, "no insider section in the context")
    if day is None:
        return _neutral(ticker, "no day to anchor the window on")

    cutoff = day - timedelta(days=WINDOW_DAYS)
    buys = [t for t in snapshot.buys if _inside(t, cutoff) and _is_leader(t)]
    sells = [t for t in snapshot.sells if _inside(t, cutoff) and _is_leader(t)]
    buyers = {t.who for t in buys if t.who}
    bought = sum(t.shares or 0.0 for t in buys)
    sold = sum(t.shares or 0.0 for t in sells)

    if len(buyers) < MIN_DISTINCT_BUYERS:
        return _neutral(
            ticker, f"{len(buyers)} distinct open-market buyer(s) in {WINDOW_DAYS}d, "
                    f"need {MIN_DISTINCT_BUYERS}",
        )
    if bought <= sold:
        return _neutral(
            ticker, f"{len(buyers)} buyers but {bought:,.0f} shares bought vs {sold:,.0f} sold",
        )
    return LLMSignal(
        ticker=ticker,
        bias=Bias.BULLISH,
        conviction=CONVICTION,
        rationale=(
            f"{len(buyers)} distinct insiders bought {bought:,.0f} shares on the open market "
            f"vs {sold:,.0f} sold in {WINDOW_DAYS}d"
        ),
    )


def _inside(trade: InsiderTrade, cutoff: date) -> bool:
    if not trade.when:
        return False
    try:
        return datetime.fromisoformat(trade.when[:10]).date() >= cutoff
    except ValueError:
        return False


def _is_leader(trade: InsiderTrade) -> bool:
    role = (trade.role or "").lower()
    return not any(word in role for word in _NOT_A_LEADER)


def _neutral(ticker: str, reason: str) -> LLMSignal:
    return LLMSignal(ticker=ticker, bias=Bias.NEUTRAL, conviction=0.0, rationale=f"{NAME}: {reason}")


__all__ = ["NAME", "WINDOW_DAYS", "MIN_DISTINCT_BUYERS", "CONVICTION", "signal_for"]
