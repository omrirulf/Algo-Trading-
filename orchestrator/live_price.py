"""The price of a name at the moment its signal is made, for the journal only.

The race and the shadow funds buy at the next session's open. The real account
buys the same day, mid-session, the moment the engine accepts a signal -- about
one day earlier. The rule is the same for every arm, but a one-day delay can
cost a fast, news-driven call more than a slow one, and nobody can say how much
without the price that was actually on the screen when each signal was made.
So every journal line of a cycle carries one: the owner's request of 25 Sep
2026, so that an exploratory "same-day entry" table can be built later.

Nothing that decides anything reads it. The engine sizes and stops on its own
market data (``app/market_data.py``), the race and the funds keep their
next-open rule, and this module can only ask for a price: one GET to Alpaca's
market-data host, or yfinance's last price when that is not possible. It never
places, replaces or cancels anything, and the trading host is not a URL it
knows.

One read per line, at the moment, rather than one batched read of all eighty
names when the cycle starts judging. The lines of a cycle are written at
different moments -- held names before the model is asked, judged ones many
minutes later, each a dispatch apart -- so one snapshot would be stale for
most of them, and the owner asked for the price when the signal is made. With
the connection kept open a read costs about a tenth of a second, so the honest
version costs seconds a cycle, and ``asked_at`` on each line is its own.

A price read must never break the cycle or hold it up. Every read has a hard
deadline, a source that keeps failing is not asked again this cycle, and the
whole cycle's reading has a budget; past it, a line says so and costs nothing.
``LivePrices.read`` never raises: a failure is a line with an ``error``.

The one credential here is the Alpaca bundle the engine already uses, resolved
by ``app.broker_client.resolve_credentials`` -- the one reader of those
settings -- and only in direct mode, where this process holds it by design. It
goes into two request headers and nowhere else: not a URL, not a log line, not
the journal. The CI guardrail that keeps credentials out of the orchestrator
names exactly those lines.
"""

from __future__ import annotations

import logging
import math
import re
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Final, Optional, Protocol, Sequence, TypeVar

import httpx

log = logging.getLogger(__name__)

#: Alpaca's market-data snapshot endpoint: the latest trade and the latest
#: bid/ask of a name in one answer. The data host, never the trading one.
ALPACA_SNAPSHOTS_URL: Final[str] = "https://data.alpaca.markets/v2/stocks/snapshots"
#: The feed a paper account may read in real time. IEX is one exchange, a few
#: percent of the volume, so a thin name's last IEX trade can be minutes old:
#: ``quote_at`` is the trade's own time so a reader can see how old.
ALPACA_FEED: Final[str] = "iex"

ALPACA_SOURCE: Final[str] = "alpaca-iex"
YFINANCE_SOURCE: Final[str] = "yfinance"
#: What ``source`` says when no source was asked at all.
NO_SOURCE: Final[str] = "none"

#: The longest one read may take. A good one takes a tenth of a second.
READ_TIMEOUT_SECONDS: Final[float] = 5.0
#: All the time a cycle may spend reading prices. Eighty names at a tenth of a
#: second is under ten seconds; this is the ceiling for the bad day, and it is
#: what bounds how much later the last order of a cycle can go out.
CYCLE_BUDGET_SECONDS: Final[float] = 90.0
#: A source that fails this many times in a row is not asked again this cycle.
#: One failure is a flake; three in a row is an outage, and asking it eighty
#: times would spend the budget on answers that are not coming.
FAILURES_BEFORE_GIVING_UP: Final[int] = 3
#: How much of a failure's text a line keeps. One short line: it is committed.
ERROR_CHARS: Final[int] = 300

T = TypeVar("T")


class PriceUnavailable(Exception):
    """This source could not give a price this time. Counts toward giving up."""


class NotQuoted(PriceUnavailable):
    """The source answered, but not for this name. A fact about the name, not
    about the source, so it does not count toward giving up on the source."""


class SourceUnavailable(PriceUnavailable):
    """The source cannot answer at all this cycle -- no credentials, or they
    were refused. Asking again would only spend the budget."""


@dataclass(frozen=True)
class Quote:
    """One price, and the data's own time for it (UTC ISO-8601, or None)."""

    price: float
    bid: Optional[float] = None
    ask: Optional[float] = None
    quote_at: Optional[str] = None


class PriceSource(Protocol):
    name: str

    def quote(self, ticker: str, timeout: float) -> Quote: ...


# --------------------------------------------------------------------------- #
# Small pure helpers
# --------------------------------------------------------------------------- #


def _positive(value: Any) -> Optional[float]:
    """A finite positive number, or None. IEX sends 0 for an empty side."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) and number > 0 else None


def iso_utc(value: Any) -> Optional[str]:
    """Any timestamp the sources send, as ``datetime.isoformat()`` in UTC.

    Alpaca's carry nine fractional digits and a ``Z``; ``fromisoformat`` takes
    six, so the rest is dropped -- nanoseconds do not move a trade to another
    day. The same format as the journal's own ``ts_utc``, so the two compare.
    """
    if isinstance(value, datetime):
        moment = value
    elif hasattr(value, "to_pydatetime"):  # a pandas Timestamp
        moment = value.to_pydatetime()
    elif isinstance(value, str) and value.strip():
        text = re.sub(r"(\.\d{6})\d+", r"\1", value.strip())
        if text.endswith(("Z", "z")):
            text = text[:-1] + "+00:00"
        try:
            moment = datetime.fromisoformat(text)
        except ValueError:
            return None
    else:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc).isoformat()


def _scrub(text: str, secrets: Sequence[str]) -> str:
    """One bounded line, with any credential value blanked out.

    Nothing here builds a message from a credential, and no answer from the
    data host should echo one. This is the belt to those braces: the text is
    committed to a public history, where a key cannot be recalled.
    """
    for secret in secrets:
        if secret:
            text = text.replace(secret, "[redacted]")
    return " ".join(text.split())[:ERROR_CHARS]


def _within(seconds: float, call: Callable[[], T]) -> T:
    """Run ``call`` and wait at most ``seconds`` for it; raise if it is late.

    The HTTP clients have timeouts of their own, but a timeout on each read of
    a socket is not a deadline on the whole call, and yfinance's cookie dance
    has been known to hang. A daemon thread is the one wait that is certain to
    end: a call still running when it is given up on is left to finish on its
    own, and cannot stop the process from exiting.
    """
    if seconds <= 0:
        raise PriceUnavailable("no time left to ask")
    box: dict[str, Any] = {}
    done = threading.Event()

    def run() -> None:
        try:
            box["value"] = call()
        except BaseException as exc:  # noqa: BLE001 - handed back to the caller
            box["error"] = exc
        finally:
            done.set()

    threading.Thread(target=run, name="live-price", daemon=True).start()
    if not done.wait(seconds):
        raise PriceUnavailable(f"no answer within {seconds:.1f}s")
    if "error" in box:
        raise box["error"]
    return box["value"]


def failed(asked_at: str, source: str, error: str) -> dict[str, Any]:
    """The ``live`` record of a line whose price could not be read."""
    return {"price": None, "bid": None, "ask": None, "quote_at": None,
            "asked_at": asked_at, "source": source, "error": error}


def answered(quote: Quote, asked_at: str, source: str) -> dict[str, Any]:
    """The ``live`` record of a line whose price was read. No ``error`` key."""
    return {"price": quote.price, "bid": quote.bid, "ask": quote.ask,
            "quote_at": quote.quote_at, "asked_at": asked_at, "source": source}


# --------------------------------------------------------------------------- #
# The sources
# --------------------------------------------------------------------------- #


def _broker_credentials() -> Any:
    """The engine's own Alpaca bundle, from the one module that reads it."""
    from app.broker_client import resolve_credentials

    return resolve_credentials()


def _auth_headers(credentials: Any) -> dict[str, str]:
    """The two headers Alpaca's data host reads, exactly as the SDK sends them.

    The only lines in the orchestrator that touch a broker credential; the CI
    guardrail names them. What they build goes into the client's headers and
    nowhere else.
    """
    if credentials.is_oauth:
        return {"Authorization": "Bearer " + credentials.access_token}
    return {"APCA-API-KEY-ID": credentials.api_key, "APCA-API-SECRET-KEY": credentials.secret_key}


def _secret_values(headers: dict[str, str]) -> tuple[str, ...]:
    """Every credential value in the headers, for ``_scrub``."""
    values = []
    for name, value in headers.items():
        if name == "Authorization":
            value = value.removeprefix("Bearer ")
        values.append(value)
    return tuple(v for v in values if v)


def _message(response: httpx.Response) -> str:
    """The error message Alpaca put in the body, if it put one there."""
    try:
        body = response.json()
    except ValueError:
        return ""
    message = body.get("message") if isinstance(body, dict) else None
    return f" ({message})" if isinstance(message, str) and message.strip() else ""


class AlpacaIex:
    """The latest IEX trade and bid/ask for one name, from Alpaca's data host.

    Read-only by construction: the client is pointed at one URL and only ever
    asked to GET it. The credential is resolved at the first read, not when
    the reader is built, so building a reader never touches a key.
    """

    name = ALPACA_SOURCE

    def __init__(self, credentials: Callable[[], Any] = _broker_credentials,
                 client_factory: Callable[..., httpx.Client] = httpx.Client) -> None:
        self._credentials = credentials
        self._client_factory = client_factory
        self._client: Optional[httpx.Client] = None
        self._secrets: tuple[str, ...] = ()
        self._lock = threading.Lock()

    def _get_client(self, timeout: float) -> httpx.Client:
        with self._lock:
            if self._client is None:
                try:
                    headers = _auth_headers(self._credentials())
                except Exception as exc:  # noqa: BLE001 - no key: the next source answers
                    raise SourceUnavailable(
                        f"no Alpaca credentials ({type(exc).__name__}: {exc})"
                    ) from None
                self._secrets = _secret_values(headers)
                # One client, kept open for the cycle: the connection is reused,
                # which is what makes eighty reads cost seconds, not minutes.
                self._client = self._client_factory(headers=headers, timeout=timeout)
            return self._client

    def quote(self, ticker: str, timeout: float) -> Quote:
        client = self._get_client(timeout)
        symbol = ticker.strip().upper()
        try:
            response = client.get(
                ALPACA_SNAPSHOTS_URL, params={"symbols": symbol, "feed": ALPACA_FEED},
                timeout=timeout,
            )
        except httpx.HTTPError as exc:
            raise PriceUnavailable(self._clean(f"{type(exc).__name__}: {exc}")) from None
        if response.status_code in (401, 403):
            # A refused key is refused for the rest of the cycle too.
            raise SourceUnavailable(self._clean(f"HTTP {response.status_code}{_message(response)}"))
        if response.status_code != 200:
            raise PriceUnavailable(self._clean(f"HTTP {response.status_code}{_message(response)}"))
        try:
            body = response.json()
        except ValueError:
            raise PriceUnavailable("the answer was not JSON") from None
        snapshot = body.get(symbol) if isinstance(body, dict) else None
        trade = snapshot.get("latestTrade") if isinstance(snapshot, dict) else None
        price = _positive(trade.get("p")) if isinstance(trade, dict) else None
        if price is None:
            raise NotQuoted(f"no IEX trade for {symbol}")
        book = snapshot.get("latestQuote")
        book = book if isinstance(book, dict) else {}
        return Quote(
            price=price,
            bid=_positive(book.get("bp")),
            ask=_positive(book.get("ap")),
            # The trade's own time: ``price`` is that trade's price.
            quote_at=iso_utc(trade.get("t")),
        )

    def redactions(self) -> tuple[str, ...]:
        """The credential values this source holds, for blanking out of any text."""
        return self._secrets

    def _clean(self, text: str) -> str:
        return _scrub(text, self._secrets)

    def close(self) -> None:
        if self._client is not None:
            self._client.close()


def _yfinance_minutes(ticker: str, timeout: float) -> Any:
    """Today's one-minute bars for ``ticker``, unadjusted. The network call."""
    import yfinance as yf  # imported lazily so tests never need it

    return yf.Ticker(ticker).history(
        period="1d", interval="1m", auto_adjust=False, actions=False, timeout=timeout,
    )


class YFinanceLast:
    """yfinance's last price: the close of the latest one-minute bar.

    The fallback, used only when Alpaca cannot answer: in webhook mode, where
    this process holds no broker key by design, or when Alpaca fails. It has
    no bid or ask, and its time is the start of that minute's bar -- the trade
    itself happened within the minute after it.
    """

    name = YFINANCE_SOURCE

    def __init__(self, minutes: Callable[[str, float], Any] = _yfinance_minutes) -> None:
        self._minutes = minutes

    def quote(self, ticker: str, timeout: float) -> Quote:
        frame = self._minutes(ticker, timeout)
        closes = getattr(frame, "get", lambda _: None)("Close")
        if closes is None or getattr(frame, "empty", True):
            # Counted as a failure, not a name yfinance lacks: every name on
            # the watchlist trades every session, so an empty answer is Yahoo
            # refusing or failing, and asking it eighty more times would be
            # the wrong response to that.
            raise PriceUnavailable("yfinance returned no one-minute bars")
        for stamp, value in reversed(list(closes.items())):
            price = _positive(value)
            if price is not None:
                return Quote(price=price, quote_at=iso_utc(stamp))
        raise PriceUnavailable("yfinance returned no usable close")


# --------------------------------------------------------------------------- #
# The reader a cycle holds
# --------------------------------------------------------------------------- #


@dataclass
class _SourceState:
    failures: int = 0
    gave_up: Optional[str] = None


class LivePrices:
    """One cycle's price reader: sources in order of preference, with limits.

    Built once per cycle and read once per journal line. ``read`` asks the
    first source that has not been given up on, falls back to the next, and
    returns the line's ``live`` record whatever happens.
    """

    def __init__(
        self,
        sources: Sequence[PriceSource],
        *,
        read_timeout: float = READ_TIMEOUT_SECONDS,
        budget: float = CYCLE_BUDGET_SECONDS,
        give_up_after: int = FAILURES_BEFORE_GIVING_UP,
        clock: Callable[[], float] = time.monotonic,
        now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
    ) -> None:
        self.sources = tuple(sources)
        self._timeout = read_timeout
        self._budget = budget
        self._give_up_after = give_up_after
        self._clock = clock
        self._now = now
        self._spent = 0.0
        self._states = {source.name: _SourceState() for source in self.sources}

    @property
    def spent(self) -> float:
        """Seconds this cycle has spent waiting on price sources so far."""
        return self._spent

    def read(self, ticker: str) -> dict[str, Any]:
        """The ``live`` record for ``ticker``, read now. Never raises."""
        first_asked: Optional[str] = None
        source_name = NO_SOURCE
        reasons: list[str] = []
        try:
            for source in self.sources:
                state = self._states[source.name]
                if state.gave_up:
                    reasons.append(f"{source.name}: {state.gave_up}")
                    continue
                left = self._budget - self._spent
                if left <= 0:
                    reasons.append(
                        f"this cycle's {self._budget:.0f}s for reading prices is used up"
                    )
                    break
                wait = min(self._timeout, left)
                asked_at = self._now().isoformat()
                first_asked = first_asked or asked_at
                source_name = source.name
                started = self._clock()
                try:
                    # Bound now, not when the thread gets round to it: a call
                    # given up on must not pick up the next source's name.
                    quote = _within(wait, lambda s=source, w=wait: s.quote(ticker, w))
                    if not isinstance(quote, Quote) or _positive(quote.price) is None:
                        raise PriceUnavailable("the answer was not a positive price")
                except NotQuoted as exc:
                    reasons.append(f"{source.name}: {self._clean(str(exc))}")
                    continue
                except SourceUnavailable as exc:
                    reason = self._clean(str(exc))
                    state.gave_up = f"not asked this cycle ({reason})"
                    log.warning("live prices: %s cannot answer this cycle (%s)", source.name, reason)
                    reasons.append(f"{source.name}: {reason}")
                    continue
                except Exception as exc:  # noqa: BLE001 - any failure is a line, never a crash
                    state.failures += 1
                    reason = self._clean(
                        str(exc) if isinstance(exc, PriceUnavailable) else f"{type(exc).__name__}: {exc}"
                    )
                    reasons.append(f"{source.name}: {reason}")
                    log.info("live prices: %s gave no price for %s (%s)", source.name, ticker, reason)
                    if state.failures >= self._give_up_after:
                        state.gave_up = (
                            f"failed {state.failures} times in a row; not asked again this cycle"
                        )
                        log.warning("live prices: %s %s", source.name, state.gave_up)
                    continue
                finally:
                    self._spent += max(0.0, self._clock() - started)
                state.failures = 0
                return answered(quote, asked_at, source.name)
            error = "; ".join(reasons) or "no price source"
            return failed(first_asked or self._now().isoformat(), source_name, self._clean(error))
        except Exception as exc:  # noqa: BLE001 - the promise is "never raises"
            log.exception("live prices: the reader itself failed for %s", ticker)
            return failed(first_asked or datetime.now(timezone.utc).isoformat(), source_name,
                          f"the price reader failed: {type(exc).__name__}")

    def _clean(self, text: str) -> str:
        """``text`` on one bounded line, with every source's credential blanked."""
        held = [value for source in self.sources
                for value in getattr(source, "redactions", lambda: ())()]
        return _scrub(text, held)

    def close(self) -> None:
        """Let go of any open connection. Never raises."""
        for source in self.sources:
            close = getattr(source, "close", None)
            if close is None:
                continue
            try:
                close()
            except Exception:  # noqa: BLE001 - closing a connection is not worth a crash
                log.debug("live prices: could not close %s", source.name, exc_info=True)


def for_dispatcher(dispatcher: object) -> Optional[LivePrices]:
    """The reader for a cycle that trades through ``dispatcher``. Never raises.

    Direct mode holds the engine's Alpaca key by design, so it asks Alpaca
    first and yfinance only when Alpaca cannot answer. Webhook mode holds no
    broker key -- that is the point of it -- so it asks yfinance alone, and
    never goes looking for a key. Any other dispatcher is a test double or an
    experiment: it gets no reader, and its lines carry no price rather than a
    network call nobody asked for.
    """
    from orchestrator.dispatch import DirectDispatcher, WebhookDispatcher

    try:
        if isinstance(dispatcher, DirectDispatcher):
            return LivePrices([AlpacaIex(), YFinanceLast()])
        if isinstance(dispatcher, WebhookDispatcher):
            return LivePrices([YFinanceLast()])
    except Exception:  # noqa: BLE001 - no reader is a line without a price, not a crash
        log.exception("live prices: could not build the reader; lines will carry no price")
    return None


__all__ = [
    "ALPACA_FEED", "ALPACA_SNAPSHOTS_URL", "ALPACA_SOURCE", "AlpacaIex", "CYCLE_BUDGET_SECONDS",
    "FAILURES_BEFORE_GIVING_UP", "LivePrices", "NO_SOURCE", "NotQuoted", "PriceSource",
    "PriceUnavailable", "Quote", "READ_TIMEOUT_SECONDS", "SourceUnavailable", "YFINANCE_SOURCE",
    "YFinanceLast", "answered", "failed", "for_dispatcher", "iso_utc",
]
