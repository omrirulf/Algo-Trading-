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
from typing import Any, Optional

from orchestrator import analysts, fundamentals, technicals
from orchestrator.technicals import TechnicalSnapshot

log = logging.getLogger(__name__)

#: Daily history pulled per ticker. Needs to cover a 200-day moving average
#: plus its warm-up and a 52-week high/low, so a calendar year is not enough.
HISTORY_PERIOD = "2y"

#: Fundamentals, analyst ratings and ownership change daily at most, but the
#: heartbeat runs hourly. Caching them keeps an unauthenticated, rate-limited
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
    gaps: list[str] = field(default_factory=list)


@dataclass
class _SlowData:
    info: dict[str, Any]
    calendar: Any
    recommendations: Any
    upgrades_downgrades: Any
    institutional_holders: Any
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


@dataclass(frozen=True)
class TickerContext:
    """Everything the model sees, and an honest list of what is missing."""

    ticker: str
    headlines: list[str] = field(default_factory=list)
    technicals: Optional[technicals.TechnicalSnapshot] = None
    fundamentals: Optional[fundamentals.FundamentalSnapshot] = None
    analysts: Optional[analysts.AnalystSnapshot] = None
    gaps: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        """Plain JSON-serialisable form, for the signal journal."""
        return {
            "ticker": self.ticker,
            "headlines": list(self.headlines),
            "technicals": self.technicals.as_dict() if self.technicals else None,
            "fundamentals": self.fundamentals.as_dict() if self.fundamentals else None,
            "analysts": self.analysts.as_dict() if self.analysts else None,
            "gaps": list(self.gaps),
        }

    def as_prompt(self) -> str:
        sections = [f"TICKER: {self.ticker}", self._news_section()]
        sections.extend(
            self._section(title, snapshot)
            for title, snapshot in (
                ("TECHNICALS (daily bars)", self.technicals),
                ("FUNDAMENTALS", self.fundamentals),
                ("ANALYST & INSTITUTIONAL VIEW", self.analysts),
            )
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


def gather(
    ticker: str,
    headlines: list[str],
    provider: Optional[YFinanceContextProvider] = None,
) -> TickerContext:
    """Build the full context for ``ticker``. Never raises."""
    raw = (provider or get_provider()).fetch(ticker)
    gaps = list(raw.gaps)

    technical_snapshot = _build_technicals(raw, gaps)
    last_close = technical_snapshot.last_close if technical_snapshot else None

    fundamental_snapshot = None
    analyst_snapshot = None
    if raw.info:
        fundamental_snapshot = _attempt(
            lambda: fundamentals.build_snapshot(raw.info, raw.calendar),
            "fundamentals",
            gaps,
        )
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

    return TickerContext(
        ticker=ticker,
        headlines=list(headlines),
        technicals=technical_snapshot,
        fundamentals=fundamental_snapshot,
        analysts=analyst_snapshot,
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
