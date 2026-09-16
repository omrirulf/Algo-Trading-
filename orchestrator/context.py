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

from config import settings as cfg
from config.instruments import is_fund
from orchestrator import (
    analysts, flows, formatting as fmt, fundamentals, funds, holdings, insiders,
    macro, positioning, technicals,
)
from orchestrator.technicals import TechnicalSnapshot

log = logging.getLogger(__name__)

#: Daily history pulled per ticker. Needs to cover a 200-day moving average
#: plus its warm-up and a 52-week high/low, so a calendar year is not enough.
HISTORY_PERIOD = "2y"

#: Fundamentals, analyst ratings and ownership change daily at most, but the
#: heartbeat runs daily. Caching them keeps an unauthenticated, rate-limited
#: data source from being asked the same question 24 times a day.
SLOW_DATA_TTL_SECONDS = 6 * 60 * 60

#: History pulled for each macro symbol. A month of sessions, so a one-week
#: change has a full week of trading days behind it even across a holiday.
MACRO_PERIOD = "1mo"


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
    #: yfinance ``funds_data`` payloads, fetched only for funds.
    fund_payloads: dict[str, Any] = field(default_factory=dict)
    #: Weekly CFTC rows, newest first, for tickers with a futures contract.
    positioning_rows: list[dict] = field(default_factory=list)
    #: ``(symbol, weight, analyst snapshot)`` for a fund's largest holdings.
    holding_analysts: list = field(default_factory=list)
    #: The accumulated share-count series for this fund, read back from the
    #: project's own log -- nowhere free publishes one.
    shares_series: Any = None
    #: Today's reading and how it was measured, for the caller to append.
    share_reading: tuple = ()
    #: Histories for the macro symbols, keyed by Yahoo symbol.
    macro_histories: dict[str, Any] = field(default_factory=dict)
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
    fund_payloads: dict[str, Any]
    positioning_rows: list[dict]
    holding_analysts: list
    shares_series: Any
    share_reading: tuple
    macro_histories: dict[str, Any]
    gaps: list[str]


class YFinanceContextProvider:
    """Fetches the raw context for a ticker, caching the slow-moving parts.

    The cache lives on the instance and the heartbeat runs one cycle at a time
    (``max_instances=1``), so no locking is needed.
    """

    def __init__(
        self,
        ttl_seconds: float = SLOW_DATA_TTL_SECONDS,
        fund_size_path: Any = None,
    ) -> None:
        self._ttl = ttl_seconds
        #: Read here, appended to by the caller after the cycle. Injectable so
        #: a test never touches the repository's real history.
        self._fund_size_path = fund_size_path or cfg.FUND_SIZE_LOG_PATH
        self._cache: dict[str, tuple[float, _SlowData]] = {}
        #: Analyst coverage keyed by *holding*, not by watchlist ticker. Forty
        #: funds overlap heavily -- the same handful of megacaps sits at the
        #: top of a dozen of them -- so without this the same company would be
        #: looked up a dozen times in one cycle.
        self._holding_cache: dict[str, tuple[float, Any]] = {}
        #: The macro block is the same for every ticker in a cycle, so it is
        #: cached once rather than once per ticker.
        self._macro_cache: Optional[tuple[float, dict[str, Any]]] = None

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
            fund_payloads=slow.fund_payloads,
            positioning_rows=slow.positioning_rows,
            holding_analysts=slow.holding_analysts,
            shares_series=slow.shares_series,
            share_reading=slow.share_reading,
            macro_histories=slow.macro_histories,
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
        fund_payloads = self._fund_payloads(handle, ticker, gaps)
        slow = _SlowData(
            fund_payloads=fund_payloads,
            positioning_rows=self._positioning_rows(ticker, gaps),
            holding_analysts=self._holding_analysts(ticker, fund_payloads, gaps),
            shares_series=flows.series_from_log(ticker, self._fund_size_path)
            if is_fund(ticker) else None,
            share_reading=flows.reading_from_info(info) if is_fund(ticker) else (),
            macro_histories=self._macro_histories(ticker, gaps),
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

    @staticmethod
    def _fund_payloads(handle: Any, ticker: str, gaps: list[str]) -> dict[str, Any]:
        """yfinance's fund section, for funds that have one.

        Skipped entirely for a single name and for a single-commodity fund:
        neither has holdings, and asking would record a gap for something
        that was never on offer.
        """
        if funds.fund_shape(ticker) == funds.NO_FUND_SECTION:
            return {}
        data = _attempt(lambda: handle.funds_data, "fund holdings", gaps)
        if data is None:
            return {}
        payloads: dict[str, Any] = {}
        for name in (
            "equity_holdings", "bond_holdings", "bond_ratings", "fund_operations",
            "fund_overview", "top_holdings", "sector_weightings", "asset_classes",
        ):
            # Each property fetches separately inside yfinance, so one that
            # 404s must not cost the others.
            payloads[name] = _attempt(lambda n=name: getattr(data, n, None), f"fund {name}", gaps)
        return payloads

    @staticmethod
    def _positioning_rows(ticker: str, gaps: list[str]) -> list[dict]:
        """Weekly CFTC rows, for the tickers that track one futures contract."""
        if positioning.contract_for(ticker) is None:
            return []
        return _attempt(lambda: positioning.fetch_rows(ticker), "CFTC positioning", gaps) or []

    def _macro_histories(self, ticker: str, gaps: list[str]) -> dict[str, Any]:
        """Rates, the dollar and volatility -- six symbols, once per cycle.

        Funds only. The company prompt is the input every replay and sanity
        baseline was measured against, so a new section in it would invalidate
        all of them, for a block that matters far less to a single name.
        """
        if not is_fund(ticker):
            return {}
        if self._macro_cache and self._macro_cache[0] > time.monotonic():
            return self._macro_cache[1]

        try:
            import yfinance as yf
        except ImportError:  # pragma: no cover - dependency is pinned
            return {}

        histories: dict[str, Any] = {}
        missed: list[str] = []
        for symbol in macro.SYMBOLS:
            try:
                frame = yf.Ticker(symbol).history(period=MACRO_PERIOD, interval="1d")
            except Exception:  # noqa: BLE001 - one missing rate is not a cycle
                frame = None
            if frame is None or getattr(frame, "empty", True):
                missed.append(symbol)
                continue
            histories[symbol] = frame
        if missed:
            gaps.append(f"macro series for {', '.join(missed)}")
        self._macro_cache = (time.monotonic() + self._ttl, histories)
        return histories

    def _holding_analysts(
        self, ticker: str, fund_payloads: dict[str, Any], gaps: list[str]
    ) -> list[tuple[str, Optional[float], Any]]:
        """Analyst coverage of each of the fund's largest holdings.

        Equity funds only. A bond fund's holdings are bonds, which nobody
        rates on a 1-to-5 buy scale, and a commodity fund holds bullion.
        """
        if funds.fund_shape(ticker) != funds.EQUITY_FUND:
            return []
        pairs = holdings.holdings_from_payload(fund_payloads.get("top_holdings"))
        if not pairs:
            return []
        out: list[tuple[str, Optional[float], Any]] = []
        missed: list[str] = []
        for symbol, weight in pairs:
            snapshot = self._analyst_for(symbol)
            if snapshot is None:
                missed.append(symbol)
            out.append((symbol, weight, snapshot))
        if missed:
            # One line, not one per holding: five failures quoted in full cost
            # more prompt than the section they failed to fill.
            gaps.append(f"analyst coverage of {len(missed)} holdings ({', '.join(missed)})")
        return out

    def _analyst_for(self, symbol: str) -> Any:
        """One holding's analyst snapshot, cached across every fund that holds it."""
        cached = self._holding_cache.get(symbol)
        if cached and cached[0] > time.monotonic():
            return cached[1]

        snapshot = None
        try:
            import yfinance as yf

            handle = yf.Ticker(symbol)
            info = dict(handle.info or {})
            if info:
                price = fmt.clean(info.get("currentPrice"))
                if price is None:
                    price = fmt.clean(info.get("regularMarketPrice"))
                actions = None
                try:
                    actions = handle.upgrades_downgrades
                except Exception:  # noqa: BLE001 - the ratings alone are enough
                    actions = None
                snapshot = analysts.build_snapshot(
                    info=info, upgrades_downgrades=actions, last_close=price
                )
        except Exception as exc:  # noqa: BLE001 - a missed holding is a gap
            log.debug("analyst lookup failed for holding %s: %s", symbol, exc)
            snapshot = None

        self._holding_cache[symbol] = (time.monotonic() + self._ttl, snapshot)
        return snapshot


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
    ("MACRO (the weather every fund trades in)", "macro"),
    ("FUNDAMENTALS", "fundamentals"),
    ("FUND BASICS", "funds"),
    ("ANALYST & INSTITUTIONAL VIEW", "analysts"),
    ("ANALYST VIEW OF THE HOLDINGS", "holdings"),
    ("INSIDER ACTIVITY", "insiders"),
    ("POSITIONING (CFTC, weekly)", "positioning"),
    ("FUND FLOWS (creations and redemptions)", "flows"),
)

#: Sections that only exist for a company. A fund has no analysts publishing
#: targets on it and no insiders filing Form 4 -- so for an index these are
#: omitted outright rather than rendered as "unavailable this cycle". The
#: difference is not cosmetic: "we tried and failed" invites the model to
#: wonder what it missed, while a section that was never there is simply not
#: part of the question.
#:
#: ``fundamentals`` joined them when the fund sections below arrived. A fund
#: was being handed the company form -- sector, market cap, profit margin,
#: next earnings date -- which rendered as seven blanks and, for bond funds,
#: occasionally as nonsense: the first 80-ticker cycle showed the model a
#: forward P/E of -4,036 for a Treasury fund. Funds get ``funds`` instead.
SINGLE_NAME_ONLY_SECTIONS = frozenset({"fundamentals", "analysts", "insiders"})

#: The mirror image: sections that only exist for a fund. Both are omitted
#: when absent rather than rendered as unavailable, because absent here means
#: "this kind of thing does not have one" -- gold has no holdings to report,
#: and a single-country fund has no futures contract. A fetch that was
#: attempted and failed still records a gap, so the two cases stay distinct.
FUND_ONLY_SECTIONS = frozenset({"funds", "holdings", "macro", "positioning", "flows"})


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
    #: A fund's own numbers, in place of the company form.
    funds: Optional[funds.FundSnapshot] = None
    #: The analyst view of a fund, rolled up from the analyst view of what it
    #: holds -- nobody publishes a target on XLE, but XLE *is* its holdings.
    holdings: Optional[holdings.HoldingsSnapshot] = None
    #: What the large speculators hold, for the tickers that track a future.
    positioning: Optional[positioning.PositioningSnapshot] = None
    #: Creations and redemptions: a fund's share count is its money in and out.
    flows: Optional[flows.FlowSnapshot] = None
    #: Rates, the curve, the dollar and volatility. The same for every ticker
    #: in a cycle, which is why the provider fetches it once.
    macro: Optional[macro.MacroSnapshot] = None
    #: ``(shares, source)`` measured this cycle, for the caller to append to
    #: the fund-size log. Not part of the prompt: it is the *series* the model
    #: reads, and one reading is not a series.
    share_reading: tuple = ()
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
            "funds": self.funds.as_dict() if self.funds else None,
            "holdings": self.holdings.as_dict() if self.holdings else None,
            "positioning": self.positioning.as_dict() if self.positioning else None,
            "flows": self.flows.as_dict() if self.flows else None,
            "macro": self.macro.as_dict() if self.macro else None,
            "gaps": list(self.gaps),
        }

    def as_prompt(self) -> str:
        fund = is_fund(self.ticker)
        sections = [f"TICKER: {self.ticker}", self._news_section()]
        for title, attribute in ENRICHMENT_SECTIONS:
            if fund and attribute in SINGLE_NAME_ONLY_SECTIONS:
                continue
            if not fund and attribute in FUND_ONLY_SECTIONS:
                continue
            value = getattr(self, attribute)
            if value is None and attribute in FUND_ONLY_SECTIONS:
                # Never on offer for this ticker, or fetched and failed -- in
                # which case a gap already says so. Either way, printing a
                # form of blanks would be the thing this replaced.
                continue
            sections.append(self._section(title, value))
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

    fund_snapshot = None
    if not company:
        fund_snapshot = _attempt(
            lambda: funds.build_snapshot(ticker, info=raw.info, **(raw.fund_payloads or {})),
            "fund basics",
            gaps,
        )

    holdings_snapshot = None
    if raw.holding_analysts:
        holdings_snapshot = _attempt(
            lambda: holdings.build_snapshot(ticker, raw.holding_analysts),
            "analyst view of the holdings",
            gaps,
        )

    flow_snapshot = None
    if raw.shares_series is not None:
        flow_snapshot = _attempt(
            lambda: flows.build_snapshot(ticker, raw.shares_series, price=last_close),
            "fund flows",
            gaps,
        )

    macro_snapshot = None
    if raw.macro_histories:
        macro_snapshot = _attempt(
            lambda: macro.build_snapshot(raw.macro_histories), "macro", gaps
        )

    positioning_snapshot = None
    if raw.positioning_rows:
        positioning_snapshot = _attempt(
            lambda: positioning.build_snapshot(ticker, raw.positioning_rows),
            "CFTC positioning",
            gaps,
        )

    fundamental_snapshot = None
    analyst_snapshot = None
    if raw.info and company:
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
        funds=fund_snapshot,
        holdings=holdings_snapshot,
        positioning=positioning_snapshot,
        flows=flow_snapshot,
        macro=macro_snapshot,
        share_reading=raw.share_reading,
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
