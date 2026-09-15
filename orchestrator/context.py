"""Assemble everything the analyst model is allowed to see about one ticker.

This is the only module that talks to yfinance. It fetches the raw pieces once
per ticker per cycle, hands them to the pure parsers in ``technicals``,
``fundamentals`` and ``analysts``, and renders the result into the text block
that goes into the user prompt.

Two rules shape the error handling, and they are deliberately different:

* **Enrichment failures degrade.** Every source is fetched independently and a
  failure records a gap instead of raising. The model is told which sections
  are missing and instructed to score those dimensions neutral. Losing the
  fundamentals of one ticker must not cost the whole cycle.
* **News failures do not degrade** -- but that decision belongs to the caller
  (``heartbeat.process_ticker``), not here. News is the input the strategy was
  designed around; silently trading on technicals alone when Bright Data is
  down would be running a different strategy than the one under test.

No credentials of any kind are read here: yfinance is unauthenticated, which
is why the enriched context needs no new API key.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Any, Optional, Sequence

from config.instruments import is_fund
from orchestrator import analysts, fundamentals, insiders, technicals
from orchestrator.technicals import TechnicalSnapshot

log = logging.getLogger(__name__)

#: Daily history pulled per ticker. Needs to cover a 200-day moving average
#: plus its warm-up and a 52-week high/low, so a calendar year is not enough.
HISTORY_PERIOD = "2y"

#: Fundamentals, analyst ratings and ownership change daily at most, but the
#: heartbeat runs daily. Caching them keeps an unauthenticated, rate-limited
#: data source from being asked the same question 24 times a day.
SLOW_DATA_TTL_SECONDS = 6 * 60 * 60


# --------------------------------------------------------------------------- #
# Raw data access
# --------------------------------------------------------------------------- #


@dataclass
class RawMarketData:
    """Unparsed yfinance payloads plus whatever failed to arrive."""

    history: Any = None
    info: dict[str, Any] = field(default_factory=dict)
    calendar: Any = None
    recommendations: Any = None
    upgrades_downgrades: Any = None
    institutional_holders: Any = None
    insider_purchases: Any = None
    insider_transactions: Any = None
    gaps: list[str] = field(default_factory=list)


@dataclass
class _SlowData:
    info: dict[str, Any]
    calendar: Any
    recommendations: Any
    upgrades_downgrades: Any
    institutional_holders: Any
    insider_purchases: Any
    insider_transactions: Any
    gaps: list[str]


class YFinanceContextProvider:
    """Fetches the raw context for a ticker, caching the slow-moving parts.

    The cache lives on the instance and the heartbeat runs one cycle at a time
    (``max_instances=1``), so no locking is needed.
    """

    def __init__(self, ttl_seconds: float = SLOW_DATA_TTL_SECONDS) -> None:
        self._ttl = ttl_seconds
        self._cache: dict[str, tuple[float, _SlowData]] = {}

    def fetch(self, ticker: str) -> RawMarketData:
        try:
            import yfinance as yf  # imported lazily so tests never need it
        except ImportError as exc:  # pragma: no cover - dependency is pinned
            return RawMarketData(gaps=[f"yfinance unavailable: {exc}"])

        try:
            handle = yf.Ticker(ticker)
        except Exception as exc:  # noqa: BLE001 - any failure is just a gap
            return RawMarketData(gaps=[f"could not open {ticker} on yfinance: {exc}"])

        history, history_gaps = self._history(handle, ticker)
        slow = self._slow_data(handle, ticker)

        return RawMarketData(
            history=history,
            info=slow.info,
            calendar=slow.calendar,
            recommendations=slow.recommendations,
            upgrades_downgrades=slow.upgrades_downgrades,
            institutional_holders=slow.institutional_holders,
            insider_purchases=slow.insider_purchases,
            insider_transactions=slow.insider_transactions,
            gaps=history_gaps + slow.gaps,
        )

    def _history(self, handle: Any, ticker: str) -> tuple[Any, list[str]]:
        try:
            frame = handle.history(period=HISTORY_PERIOD, interval="1d", auto_adjust=False)
        except Exception as exc:  # noqa: BLE001
            return None, [f"price history unavailable: {_brief(exc)}"]
        if frame is None or getattr(frame, "empty", True):
            return None, [f"no price history returned for {ticker}"]
        return frame, []

    def _slow_data(self, handle: Any, ticker: str) -> _SlowData:
        cached = self._cache.get(ticker)
        if cached and cached[0] > time.monotonic():
            return cached[1]

        gaps: list[str] = []
        info = _attempt(lambda: dict(handle.info or {}), "company fundamentals", gaps) or {}
        slow = _SlowData(
            info=info,
            calendar=_attempt(lambda: handle.calendar, "earnings calendar", gaps),
            recommendations=_attempt(
                lambda: handle.recommendations, "analyst recommendations", gaps
            ),
            upgrades_downgrades=_attempt(
                lambda: handle.upgrades_downgrades, "upgrade/downgrade history", gaps
            ),
            institutional_holders=_attempt(
                lambda: handle.institutional_holders, "institutional holders", gaps
            ),
            insider_purchases=_attempt(
                lambda: handle.insider_purchases, "insider buy/sell summary", gaps
            ),
            insider_transactions=_attempt(
                lambda: handle.insider_transactions, "insider transactions", gaps
            ),
            gaps=gaps,
        )
        self._cache[ticker] = (time.monotonic() + self._ttl, slow)
        return slow


#: Gaps go into the prompt. A stack of connection errors quoted in full costs
#: hundreds of tokens per ticker and tells the model nothing the first clause
#: did not; the full text still goes to the log.
MAX_GAP_DETAIL = 120


def _brief(exc: Exception) -> str:
    text = " ".join(str(exc).split())
    return text if len(text) <= MAX_GAP_DETAIL else text[: MAX_GAP_DETAIL - 1] + "…"


def _attempt(fetch: Any, label: str, gaps: list[str]) -> Any:
    """Run ``fetch``, recording a gap instead of propagating a failure."""
    try:
        return fetch()
    except Exception as exc:  # noqa: BLE001 - yfinance raises anything at all
        log.warning("%s unavailable: %s", label, exc)
        gaps.append(f"{label} unavailable: {_brief(exc)}")
        return None


_provider: Optional[YFinanceContextProvider] = None


def get_provider() -> YFinanceContextProvider:
    """Lazily construct the shared provider so its cache survives across cycles."""
    global _provider
    if _provider is None:
        _provider = YFinanceContextProvider()
    return _provider


# --------------------------------------------------------------------------- #
# Assembled context
# --------------------------------------------------------------------------- #


#: Prompt heading -> ``TickerContext`` attribute, in the order they are shown.
#: News is handled separately: it is never "unavailable", only empty.
ENRICHMENT_SECTIONS = (
    ("TECHNICALS (daily bars)", "technicals"),
    ("FUNDAMENTALS", "fundamentals"),
    ("ANALYST & INSTITUTIONAL VIEW", "analysts"),
    ("INSIDER ACTIVITY", "insiders"),
)

#: Sections that only exist for a company. A fund has no analysts publishing
#: targets on it and no insiders filing Form 4 -- so for an index these are
#: omitted outright rather than rendered as "unavailable this cycle". The
#: difference is not cosmetic: "we tried and failed" invites the model to
#: wonder what it missed, while a section that was never there is simply not
#: part of the question.
SINGLE_NAME_ONLY_SECTIONS = frozenset({"analysts", "insiders"})


@dataclass(frozen=True)
class TickerContext:
    """Everything the model sees, and an honest list of what is missing."""

    ticker: str
    headlines: list[str] = field(default_factory=list)
    #: The same news, structured, with the link each prompt line drops. Kept
    #: beside ``headlines`` rather than inside them so the prompt stays
    #: byte-identical to what every replay and sanity baseline was measured
    #: against, while a person reviewing a signal can still open the source.
    sources: list[dict] = field(default_factory=list)
    technicals: Optional[technicals.TechnicalSnapshot] = None
    fundamentals: Optional[fundamentals.FundamentalSnapshot] = None
    analysts: Optional[analysts.AnalystSnapshot] = None
    insiders: Optional[insiders.InsiderSnapshot] = None
    gaps: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        """Plain JSON-serialisable form, for the signal journal."""
        return {
            "ticker": self.ticker,
            "headlines": list(self.headlines),
            "sources": list(self.sources),
            "technicals": self.technicals.as_dict() if self.technicals else None,
            "fundamentals": self.fundamentals.as_dict() if self.fundamentals else None,
            "analysts": self.analysts.as_dict() if self.analysts else None,
            "insiders": self.insiders.as_dict() if self.insiders else None,
            "gaps": list(self.gaps),
        }

    def as_prompt(self) -> str:
        fund = is_fund(self.ticker)
        sections = [f"TICKER: {self.ticker}", self._news_section()]
        sections.extend(
            self._section(title, getattr(self, attribute))
            for title, attribute in ENRICHMENT_SECTIONS
            if not (fund and attribute in SINGLE_NAME_ONLY_SECTIONS)
        )
        if self.gaps:
            sections.append(
                "DATA GAPS (score these dimensions 0.0 rather than guessing)\n"
                + "\n".join(f"- {gap}" for gap in self.gaps)
            )
        return "\n\n".join(sections)

    def _news_section(self) -> str:
        body = "\n".join(f"- {headline}" for headline in self.headlines) or "- none found"
        return f"NEWS (past 24 hours)\n{body}"

    @staticmethod
    def _section(title: str, snapshot: Any) -> str:
        if snapshot is None:
            return f"{title}\n- unavailable this cycle"
        return f"{title}\n" + "\n".join(snapshot.as_lines())


def _split_headlines(headlines: Sequence[Any]) -> tuple[list[str], list[dict]]:
    """Prompt lines, and the structured records when the caller supplied them."""
    lines: list[str] = []
    sources: list[dict] = []
    for item in headlines:
        as_line = getattr(item, "as_line", None)
        if callable(as_line):
            lines.append(as_line())
            sources.append(item.as_dict())
        else:
            lines.append(str(item))
    return lines, sources


def gather(
    ticker: str,
    headlines: Sequence[Any],
    provider: Optional[YFinanceContextProvider] = None,
) -> TickerContext:
    """Build the full context for ``ticker``. Never raises.

    ``headlines`` takes either plain prompt lines or ``news.Headline``
    records. Records additionally carry their URL into ``sources``; strings
    are accepted unchanged so the replay harnesses, which rebuild lines from
    a stored journal, need no change.
    """
    lines, sources = _split_headlines(headlines)
    raw = (provider or get_provider()).fetch(ticker)
    gaps = list(raw.gaps)

    technical_snapshot = _build_technicals(raw, gaps)
    last_close = technical_snapshot.last_close if technical_snapshot else None

    # A fund has no analyst coverage and no Form 4 filings. Skipping the two
    # builds keeps their failures from being recorded as "gaps", which would
    # tell the model to score as 0.0 something that was never on offer.
    company = not is_fund(ticker)

    fundamental_snapshot = None
    analyst_snapshot = None
    if raw.info:
        fundamental_snapshot = _attempt(
            lambda: fundamentals.build_snapshot(raw.info, raw.calendar),
            "fundamentals",
            gaps,
        )
    if raw.info and company:
        analyst_snapshot = _attempt(
            lambda: analysts.build_snapshot(
                info=raw.info,
                recommendations=raw.recommendations,
                upgrades_downgrades=raw.upgrades_downgrades,
                institutional_holders=raw.institutional_holders,
                last_close=last_close,
            ),
            "analyst view",
            gaps,
        )

    # Insider data does not come from ``info``, so it is built independently.
    # A source that failed is None and renders as unavailable; a source that
    # returned an empty frame is real information -- nobody traded -- and the
    # snapshot says so.
    insider_snapshot = None
    if company and (
        raw.insider_purchases is not None or raw.insider_transactions is not None
    ):
        insider_snapshot = _attempt(
            lambda: insiders.build_snapshot(
                purchases=raw.insider_purchases,
                transactions=raw.insider_transactions,
            ),
            "insider activity",
            gaps,
        )

    return TickerContext(
        ticker=ticker,
        headlines=lines,
        sources=sources,
        technicals=technical_snapshot,
        fundamentals=fundamental_snapshot,
        analysts=analyst_snapshot,
        insiders=insider_snapshot,
        gaps=gaps,
    )


def _build_technicals(raw: RawMarketData, gaps: list[str]) -> Optional[TechnicalSnapshot]:
    if raw.history is None:
        return None
    try:
        return technicals.build_snapshot(raw.history)
    except (ValueError, KeyError) as exc:
        gaps.append(f"technicals could not be computed: {exc}")
        return None


__all__ = ["TickerContext", "YFinanceContextProvider", "gather", "get_provider"]
