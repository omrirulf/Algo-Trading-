"""Render one cycle's journal as something a person can actually read.

The journal is one JSON object per ticker per cycle. That is the right shape
for a scorer and the wrong shape for a human deciding whether to trust a
signal: the evidence the model weighed is in there, but spread across five
nested objects and a list of prompt lines with no links.

This renders it back out as Markdown, per ticker, with each dimension's score
printed next to the evidence that produced it -- so "news score +0.8" sits
directly under the headlines it came from, and every headline is a link you
can open. That adjacency is the whole point: a score with its evidence out of
reach is an assertion.

Two things the report is deliberate about, because its only reader is a
person and not a machine:

* **Plain English.** Section titles, verdict lines and the framing text are
  written at roughly B1-B2 level -- short sentences, common words, and a word
  list at the end for the terms that have no simpler synonym (RSI, MACD,
  P/E). The model's own rationale and key factors are reproduced verbatim:
  paraphrasing those would make the report a summary of a summary.
* **Every ticker says what it is.** A name and a sleeve tag ("Company",
  "Index fund", "Commodity") on every heading, and the tickers grouped by
  sleeve, because "why did we not look at commodities" is a question the old
  flat list by conviction invited and could not answer.

Read-only, and offline. It reads the journal the cycle already wrote; it never
fetches anything, and it cannot place an order.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, fields
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from config.instruments import InstrumentKind, kind_for, name_for, sleeve_label  # noqa: E402
from orchestrator import (  # noqa: E402
    analysts, carry, crops, earnings, energy, flows, fundamentals, funds,
    holdings, insiders, macro, positioning, technicals,
)
from orchestrator.news import absolute_url  # noqa: E402

#: Lines this far apart belong to different cycles.
#:
#: This was 20, chosen when a cycle over 35 tickers took a few minutes. The
#: first 80-ticker cycle ran for 27.7 minutes, so the window silently cut the
#: cycle in half: it kept the last 20 minutes and dropped the first 8 -- which
#: is every single name, because the watchlist is walked in sleeve order. The
#: report looked complete and was missing sixteen companies.
#:
#: The right bound is structural rather than observed. A cycle cannot outlive
#: the heartbeat job's `timeout-minutes` (45), and the next cycle cannot start
#: before HEARTBEAT_INTERVAL_MINUTES (1440). Anything strictly between those
#: is correct; 120 sits well clear of both ends, so neither a slow run nor a
#: re-run an hour later is mis-grouped.
CYCLE_WINDOW_MINUTES = 120

#: The report is read from Israel, so it leads with Israel time and keeps UTC
#: beside it -- the journal's own timestamps are UTC and have to stay
#: checkable against it.
LOCAL_TZ = "Asia/Jerusalem"
LOCAL_TZ_LABEL = "Israel time"

#: The model's per-dimension scores, the context section each one judges, and
#: the title the report gives it. The prompt's own titles ("ANALYST &
#: INSTITUTIONAL VIEW") are shouted abbreviations aimed at a model; these are
#: aimed at a person. Changing them cannot touch the prompt -- the prompt
#: builds its own headings in ``orchestrator/context.py``.
#: A ticker carries either the company section or its fund counterpart, never
#: both -- ``render_ticker`` skips a key the context does not have -- so the
#: two pairs sit side by side here rather than in separate tables.
SCORE_SECTIONS = (
    ("news_score", "news", "News"),
    ("news_score", "macro", "Interest rates, the dollar and market nerves"),
    ("technical_score", "technicals", "Price and chart"),
    ("fundamental_score", "fundamentals", "Company numbers"),
    ("fundamental_score", "funds", "What this fund holds"),
    ("fundamental_score", "earnings", "Does this company beat its own forecasts"),
    ("fundamental_score", "carry", "What holding this fund costs you"),
    ("fundamental_score", "energy", "How much oil and gas is in storage"),
    ("fundamental_score", "crops", "How the crop is growing"),
    ("analyst_score", "analysts", "What analysts and big funds say"),
    ("analyst_score", "holdings", "What analysts say about what this fund holds"),
    ("insider_score", "insiders", "Buying and selling by company insiders"),
    ("insider_score", "positioning", "Who is positioned how"),
    ("insider_score", "flows", "Money going into and out of this fund"),
)

#: Sleeves in report order, widest-held first.
SLEEVE_ORDER = (
    InstrumentKind.EQUITY,
    InstrumentKind.BROAD_FUND,
    InstrumentKind.FOCUSED_FUND,
    InstrumentKind.COMMODITY_FUND,
)

#: The heading each sleeve gets. Plural, because it heads a list.
SLEEVE_HEADINGS: dict[InstrumentKind, str] = {
    InstrumentKind.EQUITY: "Companies",
    InstrumentKind.BROAD_FUND: "Whole-market funds",
    InstrumentKind.FOCUSED_FUND: "Sector and country funds",
    InstrumentKind.COMMODITY_FUND: "Commodities",
}

#: What a side means, in words. Kept out of the headings, which stay short,
#: and stated once in the opening block instead.
BIAS_MEANINGS = (
    ("BULLISH", "the model thinks the price will go up"),
    ("BEARISH", "the model thinks the price will go down"),
    ("NEUTRAL", "the model has no clear view"),
)

#: Terms with no simpler synonym. A report that uses them without explaining
#: them is only readable by someone who did not need it.
GLOSSARY = (
    ("Confidence", "How sure the model is, from 0.00 to 1.00. A trade needs 0.30 or more."),
    ("R", "The amount one trade risked when it was opened: the distance from the entry price to the stop-loss. +1R means the trade has earned that amount back; +3R means three times it."),
    ("Score", "How good or bad one kind of evidence looks, from -1.00 (bad) to +1.00 (good)."),
    ("Moving average (SMA)", "The average price over the last N days. A price above it usually means an up trend."),
    ("RSI", "A 0-100 meter of how fast the price has moved lately. Over 70 means a lot of buying, under 30 a lot of selling."),
    ("MACD", "Compares a short and a long average to show whether a trend is getting stronger or weaker."),
    ("P/E", "Price divided by yearly profit per share. A high number means the share is expensive next to today's profit."),
    ("ATR", "The normal size of one day's price move. The system uses it to place the stop-loss."),
    ("Stop-loss", "An order that closes the position if the price moves too far the wrong way."),
    ("Insider", "A director or senior manager of the company. They have to report their own trades."),
    ("Index fund", "One fund that holds many shares at once, so it follows a whole market instead of one company."),
    ("Sector or country fund", "A fund that holds many companies, but all of them in one industry or one country. Safer than one company, riskier than a whole-market fund."),
    ("Positioning", "How much the big professional traders are betting on a commodity or bond, from the weekly US regulator report. High numbers mean the bet is crowded, which cuts both ways."),
    ("Fund flows", "Money going into or out of a fund. When more people want a fund, new shares are created; when they leave, shares are destroyed. So a rising share count means real money came in. It has already happened -- it is not a forecast."),
    ("Roll-up", "A fund does not get analyst ratings, but the companies it holds do. A roll-up adds those ratings up, weighted by how much of each company the fund owns. The \"coverage\" number says how much of the fund that actually covers."),
    ("Beta", "How hard a fund swings compared with the whole market. Beta 1.0 moves with the market, 2.0 swings twice as hard, 0.5 half as hard."),
    ("Yield curve", "The gap between what the government pays to borrow for three months and for ten years. Normally ten years costs more. When it costs less -- an \"inverted\" curve -- markets are expecting a slowdown."),
    ("VIX", "How nervous the market is about the next month. Under 15 is calm, over 25 is stressed."),
    ("Build and draw", "A build means more oil or gas went into storage than came out last week, so there is more supply around — usually bad for the price. A draw is the opposite."),
    ("Good or excellent", "The share of a US crop that government inspectors rate as healthy. A healthier crop means more grain, which usually pushes the price down."),
    ("Beat and miss", "A company beat if it earned more than analysts forecast, and missed if it earned less."),
    ("Cost of holding", "A commodity fund does not own the gold or the oil. It owns contracts that expire every month and must be replaced, and the replacement often costs more. That difference comes out of the fund's price every month, even when the commodity itself does not move. Funds that hold real metal in a vault avoid almost all of it."),
)


@dataclass(frozen=True)
class Line:
    """One journal line, kept whole rather than reduced to scorer fields."""

    raw: dict[str, Any]

    @property
    def ticker(self) -> str:
        return str(self.raw.get("ticker") or "?")

    @property
    def name(self) -> str:
        """The readable name, or the ticker when the watchlist has no entry."""
        return name_for(self.ticker)

    @property
    def sleeve(self) -> InstrumentKind:
        """What kind of thing this is -- resolved from the ticker, never from the signal."""
        return kind_for(self.ticker)

    @property
    def sleeve_name(self) -> str:
        return sleeve_label(self.ticker)

    @property
    def when(self) -> Optional[datetime]:
        text = self.raw.get("ts_utc")
        if not isinstance(text, str):
            return None
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError:
            return None

    @property
    def context(self) -> dict:
        return self.raw.get("context") or {}

    @property
    def signal(self) -> Optional[dict]:
        return self.raw.get("signal")

    @property
    def outcome(self) -> Optional[dict]:
        return self.raw.get("outcome")

    @property
    def screen(self) -> Optional[dict]:
        return self.raw.get("screen")

    @property
    def conviction(self) -> float:
        signal = self.signal or {}
        value = signal.get("conviction")
        return float(value) if isinstance(value, (int, float)) else -1.0

    @property
    def took_a_side(self) -> bool:
        """BULLISH or BEARISH. NEUTRAL, a failure and a screen-out are not sides."""
        return str((self.signal or {}).get("bias") or "").upper() in ("BULLISH", "BEARISH")


def read_lines(path: Path) -> list[Line]:
    """Every parsable line in the journal. A bad line is skipped, not fatal."""
    out: list[Line] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return out
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            out.append(Line(parsed))
    return out


def latest_cycle(lines: list[Line], window_minutes: int = CYCLE_WINDOW_MINUTES) -> list[Line]:
    """The most recent burst of lines -- one cycle's worth.

    Grouped by time rather than by a cycle id because the journal has never
    carried one, and inventing one now would make every line already written
    unreadable by this tool.
    """
    dated = [line for line in lines if line.when is not None]
    if not dated:
        return list(lines)
    newest = max(line.when for line in dated)  # type: ignore[type-var]
    cutoff = newest - timedelta(minutes=window_minutes)
    return [line for line in dated if line.when >= cutoff]  # type: ignore[operator]


def _fmt_score(value: Any) -> str:
    if not isinstance(value, (int, float)):
        return "n/a"
    return f"{float(value):+.2f}"


def _stamp(when: Optional[datetime]) -> str:
    """The cycle time in Israel time, with UTC beside it."""
    if when is None:
        return "time unknown"
    utc = when.astimezone(timezone.utc)
    try:
        from zoneinfo import ZoneInfo

        local = utc.astimezone(ZoneInfo(LOCAL_TZ))
    except Exception:  # noqa: BLE001 - no tz database: UTC alone is still true
        return utc.strftime("%d %b %Y, %H:%M UTC")
    return (
        f"{local.strftime('%d %b %Y, %H:%M')} {LOCAL_TZ_LABEL} "
        f"({utc.strftime('%H:%M')} UTC)"
    )


def _news_block(context: dict) -> list[str]:
    """Headlines as links when the cycle captured them, plain text otherwise."""
    sources = context.get("sources") or []
    headlines = context.get("headlines") or []
    if not headlines and not sources:
        return ["_No news found for this one today._"]

    out: list[str] = []
    if sources:
        for item in sources:
            if not isinstance(item, dict):
                continue
            title = str(item.get("title") or "").strip() or "(untitled)"
            # Repaired on the way out, not only on the way in: the cycles
            # already journalled before this was fixed carry bare
            # `/goto?url=...` stubs, and a report that renders them as dead
            # links is worse than one that renders none.
            url = absolute_url(str(item.get("url") or ""))
            meta = ", ".join(
                x for x in (str(item.get("source") or ""), str(item.get("when") or "")) if x
            )
            head = f"[{title}]({url})" if url else title
            snippet = str(item.get("snippet") or "").strip()
            line = f"- {head}"
            if meta:
                line += f"  \n  <sub>{meta}</sub>"
            if snippet:
                line += f"  \n  {snippet}"
            out.append(line)
        return out

    # Journals written before URLs were captured.
    out.append("_This cycle did not save the links, so here is the text only._")
    out += [f"- {h}" for h in headlines]
    return out


#: How each stored section is turned back into the object that rendered it
#: for the model: the snapshot class, and the class of any nested records.
_SNAPSHOT_CLASSES: dict[str, tuple[type, dict[str, type]]] = {
    "technicals": (technicals.TechnicalSnapshot, {}),
    "fundamentals": (fundamentals.FundamentalSnapshot, {}),
    "analysts": (analysts.AnalystSnapshot, {}),
    "insiders": (insiders.InsiderSnapshot, {"buys": insiders.InsiderTrade, "sells": insiders.InsiderTrade}),
    "funds": (funds.FundSnapshot, {}),
    "holdings": (holdings.HoldingsSnapshot, {}),
    "macro": (macro.MacroSnapshot, {}),
    "earnings": (earnings.EarningsSnapshot, {"quarters": earnings.Quarter}),
    "energy": (energy.EnergySnapshot, {"stocks": energy.Stock}),
    "crops": (crops.CropSnapshot, {}),
    "carry": (carry.CarrySnapshot, {"windows": carry.Window}),
    "positioning": (positioning.PositioningSnapshot, {}),
    "flows": (flows.FlowSnapshot, {"windows": flows.FlowWindow}),
}


def _rebuild(cls: type, data: dict, nested: dict[str, type]) -> Any:
    """A snapshot back from its ``asdict()`` form.

    Keys the class does not know are dropped rather than fatal: a journal
    line written by a newer or older schema should still render, and an
    unknown field is not evidence the model saw.
    """
    known = {f.name for f in fields(cls)}
    kwargs = {k: v for k, v in data.items() if k in known}
    for key, sub in nested.items():
        items = kwargs.get(key)
        if isinstance(items, list):
            sub_known = {f.name for f in fields(sub)}
            kwargs[key] = [
                sub(**{k: v for k, v in item.items() if k in sub_known})
                for item in items
                if isinstance(item, dict)
            ]
    return cls(**kwargs)


def prompt_lines(context_key: str, snapshot: Any) -> Optional[list[str]]:
    """The exact lines the model was shown for this section, or None.

    None means the stored dict could not be rebuilt -- the caller falls back
    to a field table rather than showing nothing, because a report that
    hides evidence it cannot format is worse than one that formats it badly.
    """
    spec = _SNAPSHOT_CLASSES.get(context_key)
    if spec is None or not isinstance(snapshot, dict):
        return None
    cls, nested = spec
    try:
        return list(_rebuild(cls, snapshot, nested).as_lines())
    except Exception:  # noqa: BLE001 - any failure means "use the table"
        return None


def _snapshot_block(snapshot: Any, context_key: str = "") -> list[str]:
    """A stored section as the prose the model read; a field table if it cannot be rebuilt.

    The prose carries the interpretation the numbers alone do not -- "50d
    above 200d", "92% of the way up the 52-week range" -- and it is
    literally what the model was judging. The table is the fallback, not
    the goal.
    """
    if not isinstance(snapshot, dict) or not snapshot:
        return ["_Not available today._"]
    lines = prompt_lines(context_key, snapshot)
    if lines is not None:
        return ["```text"] + lines + ["```"]
    rows = ["| field | value |", "| --- | --- |"]
    for key, value in snapshot.items():
        if isinstance(value, list):
            shown = f"{len(value)} item(s)" if value else "none"
        elif isinstance(value, float):
            # 6 significant figures, so a price keeps its cents (184.55, not
            # 184.6); whole numbers get thousands separators rather than
            # exponent notation, so share counts stay readable.
            shown = f"{value:,.0f}" if value.is_integer() else f"{value:,.6g}"
        elif value is None:
            shown = "n/a"
        else:
            shown = str(value)
        if len(shown) > 120:
            shown = shown[:117] + "..."
        rows.append(f"| `{key}` | {shown} |")
    return rows


def heading(line: Line) -> str:
    """Name, ticker, what kind of thing it is, the side and how sure.

    The sleeve tag is repeated on every heading even though the tickers are
    already grouped under a sleeve, so that a heading copied or linked on its
    own still says what it is about.
    """
    signal = line.signal or {}
    bias = signal.get("bias") or "no answer"
    conviction = signal.get("conviction")
    if isinstance(conviction, (int, float)):
        sure = f"confidence {float(conviction):.2f}"
    else:
        sure = "no confidence given"
    return f"### {line.name} ({line.ticker}) · {line.sleeve_name} — {bias}, {sure}"


def render_ticker(line: Line) -> list[str]:
    """One ticker: what it concluded, then every input it concluded it from."""
    signal = line.signal or {}
    context = line.context

    out = [heading(line), ""]

    outcome = line.outcome or {}
    if outcome:
        status = outcome.get("status") or f"HTTP {outcome.get('http_status')}"
        reason = outcome.get("reason") or ""
        qty = outcome.get("quantity")
        bits = [f"**Result:** {status}"]
        if qty:
            bits.append(f"{qty} shares")
        if reason:
            bits.append(str(reason))
        out += [" · ".join(bits), ""]
    elif line.raw.get("error"):
        out += [f"**This one did not finish:** {line.raw['error']}", ""]
    elif line.screen and not signal.get("rationale"):
        out += [
            "**Stopped early.** The cheap first model saw nothing worth a "
            "closer look, so the main model was never asked.",
            "",
        ]

    if signal.get("rationale"):
        out += ["**In the model's own words:**", "", f"> {signal['rationale']}", ""]

    factors = signal.get("key_factors") or []
    if factors:
        out += ["**Main reasons it gave:**"] + [f"- {f}" for f in factors] + [""]

    for score_field, context_key, title in SCORE_SECTIONS:
        if context_key not in context and context_key != "news":
            continue
        score = _fmt_score(signal.get(score_field)) if signal else "n/a"
        out += [f"<details><summary><b>{title}</b> — score {score}</summary>", ""]
        if context_key == "news":
            out += _news_block(context)
        else:
            out += _snapshot_block(context.get(context_key), context_key)
        out += ["", "</details>", ""]

    gaps = context.get("gaps") or []
    if gaps:
        out += ["**Data that was missing** (counted as 0.00, never guessed):"]
        out += [f"- {g}" for g in gaps] + [""]

    return out


#: What each management action is called in the report. The audit log's
#: names are for code; these are for a person.
_POSITION_ACTIONS = {
    "tranche_taken": "Sold part",
    "group_cap_trimmed": "Trimmed",
    "stop_raised": "Stop raised",
    "held": "Holding",
    "protected": "Stop placed",
    "unmanaged": "Left alone",
    "error": "Problem",
}


def read_position_actions(audit_path: Path, day: str) -> list[dict]:
    """Every ``position_managed`` action the audit log recorded on ``day``.

    Matched by calendar day rather than by the journal's timestamps, because
    the audit log's ``ts`` is the runner's local clock with no offset and a
    daily cycle manages the book exactly once. A missing or unreadable file
    is an empty list: the report must never fail because a second log did.
    """
    out: list[dict] = []
    try:
        text = audit_path.read_text(encoding="utf-8")
    except OSError:
        return out
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        # Production renames message->event and asctime->ts; a plain
        # JsonFormatter does not. Accept both so the section never goes
        # quietly blank over a formatter difference.
        if (record.get("event") or record.get("message")) != "position_managed":
            continue
        stamp = str(record.get("ts") or record.get("asctime") or "")
        if not stamp.startswith(day):
            continue
        action = record.get("action")
        if isinstance(action, dict) and action.get("ticker"):
            out.append(action)
    return out


def _position_line(a: dict) -> str:
    """One action as a sentence. Numbers kept, jargon translated."""
    kind = a.get("action")
    gain = a.get("gain_r")
    gain_text = f"{float(gain):+.2f}R" if isinstance(gain, (int, float)) else "n/a"
    old, new = a.get("old_stop"), a.get("new_stop")
    stop_move = (
        f"Stop-loss raised {float(old):.2f} → {float(new):.2f}."
        if isinstance(old, (int, float)) and isinstance(new, (int, float)) and new != old
        else (f"Stop-loss {float(old):.2f}." if isinstance(old, (int, float)) else "")
    )
    if kind == "tranche_taken":
        total = int(a.get("qty_closed") or 0) + int(a.get("remaining_qty") or 0)
        return (f"Sold {a.get('qty_closed')} of {total} shares at {gain_text}, "
                f"{a.get('remaining_qty')} still held. {stop_move}").strip()
    if kind == "group_cap_trimmed":
        total = int(a.get("qty_closed") or 0) + int(a.get("remaining_qty") or 0)
        return (f"Sold {a.get('qty_closed')} of {total} shares to bring its exposure "
                f"group back under its cap, {a.get('remaining_qty')} still held. {stop_move}").strip()
    if kind == "stop_raised":
        if "trailing" in str(a.get("reason") or ""):
            return f"At {gain_text}, following the price. {stop_move}".strip()
        return f"Reached {gain_text}; too small to split, so only the stop moved. {stop_move}".strip()
    if kind == "held":
        return f"{gain_text}, holding {a.get('remaining_qty')} shares. {stop_move}".strip()
    if kind == "protected":
        new = a.get("new_stop")
        how = "estimated from today's volatility" if a.get("r_estimated") else "from the trade's own record"
        at = f" at {float(new):.2f}" if isinstance(new, (int, float)) else ""
        return f"Had no stop-loss order, so a new one was placed{at} ({how})."
    if kind == "unmanaged":
        return f"No stop-loss order found, so it was not touched. Worth a look: {a.get('reason', '')}".strip()
    return f"Could not be managed: {a.get('reason', '')}".strip()


def render_positions(actions: list[dict]) -> list[str]:
    """The open book's day. Nothing when nothing was recorded."""
    if not actions:
        return []
    out = [
        "## Open positions",
        "",
        "Checked before any new trade. R is what the trade risked at entry; "
        "the ladder sells a third at +1R and another at +3R, the stop-loss "
        "follows the price up every day, and it only ever moves up.",
        "",
        "| Position | What happened |",
        "| --- | --- |",
    ]
    order = ("tranche_taken", "group_cap_trimmed", "stop_raised", "protected", "unmanaged", "error", "held")
    for a in sorted(actions, key=lambda x: (order.index(x.get("action")) if x.get("action") in order else 9, x.get("ticker", ""))):
        ticker = str(a.get("ticker"))
        label = f"{name_for(ticker)} ({ticker}) · {sleeve_label(ticker)}"
        out.append(f"| {label} | **{_POSITION_ACTIONS.get(a.get('action'), a.get('action'))}.** {_position_line(a)} |")
    out.append("")
    return out


def _how_to_read() -> list[str]:
    """The framing text. Short sentences, common words, nothing assumed."""
    sides = "; ".join(f"**{name}** = {meaning}" for name, meaning in BIAS_MEANINGS)
    return [
        "## How to read this",
        "",
        "Once a day the system looks at every name on the list. For each one it "
        "reads five kinds of evidence and gives each kind a score from -1.00 "
        "(bad) to +1.00 (good). Then it picks a side and says how sure it is, "
        "from 0.00 to 1.00.",
        "",
        f"The three sides: {sides}.",
        "",
        "Being sure is not enough on its own. A trade only happens when "
        "confidence reaches **0.30**. Below that the system writes down what it "
        "thought and does nothing. The size of a trade, the stop-loss and every "
        "limit are decided by plain code, not by the model.",
        "",
        "Open positions are checked first, before any new trade. When a trade "
        "has earned back what it risked (+1R), a third of it is sold and the "
        "stop-loss moves up to the entry price, so it can no longer lose. At "
        "three times that (+3R) another third is sold and the stop moves up "
        "again. The last third stays open. Every day the stop-loss also follows "
        "the price up, so a position only ever closes when its stop is hit. "
        "The stop only ever moves up.",
        "",
        "Under each name you will find the five scores. Click a grey line to "
        "open it and see the exact evidence behind that score. The words inside "
        "quotation marks are the model's own; nothing there has been rewritten.",
        "",
    ]


def _summary_table(lines: list[Line]) -> list[str]:
    """One row per sleeve: how many were looked at, and what came of them.

    Here because a flat list ordered by conviction cannot answer "did we even
    look at the commodities today", and that turned out to be the first
    question a reader asks.
    """
    rows = [
        "| Group | Looked at | Took a side | No clear view | Problems |",
        "| --- | --- | --- | --- | --- |",
    ]
    for sleeve in SLEEVE_ORDER:
        group = [l for l in lines if l.sleeve is sleeve]
        if not group:
            continue
        problems = [l for l in group if l.raw.get("error")]
        sided = [l for l in group if l.took_a_side]
        quiet = len(group) - len(sided) - len(problems)
        rows.append(
            f"| {SLEEVE_HEADINGS[sleeve]} | {len(group)} | {len(sided)} | "
            f"{quiet} | {len(problems)} |"
        )
    return rows


def _glossary() -> list[str]:
    out = [
        "## Word list",
        "",
        "Terms that appear above and have no simpler word:",
        "",
    ]
    out += [f"- **{term}** — {meaning}" for term, meaning in GLOSSARY]
    out.append("")
    return out


def render(lines: list[Line], position_actions: Optional[list[dict]] = None) -> str:
    """The whole cycle: grouped by what the thing is, loudest signal first."""
    if not lines:
        return "# Daily report\n\n_Nothing in the journal to show._\n"

    when = max((l.when for l in lines if l.when), default=None)
    traded = [l for l in lines if (l.outcome or {}).get("status") == "ACCEPTED"]
    failed = [l for l in lines if l.raw.get("error")]
    checked = f"{len(lines)} name{'' if len(lines) == 1 else 's'} checked"

    out = [
        "# Daily report",
        "",
        f"**{_stamp(when)}** · {checked} · {len(traded)} traded · "
        f"{len(failed)} with a problem",
        "",
    ]
    out += _summary_table(lines)
    out.append("")
    out += render_positions(position_actions or [])
    out += _how_to_read()

    for sleeve in SLEEVE_ORDER:
        group = sorted(
            (l for l in lines if l.sleeve is sleeve),
            key=lambda l: (-l.conviction, l.ticker),
        )
        if not group:
            continue
        out += [f"## {SLEEVE_HEADINGS[sleeve]}", ""]
        for line in group:
            out += render_ticker(line)

    out += _glossary()
    return "\n".join(out)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
        help="path to the signal journal (default: the configured one)",
    )
    parser.add_argument(
        "--audit", type=Path, default=cfg.AUDIT_LOG_PATH,
        help="path to the execution audit log, for the open-positions section",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="render every line in the journal rather than the most recent cycle",
    )
    parser.add_argument(
        "--ticker", action="append", default=None,
        help="restrict to these tickers (repeatable)",
    )
    args = parser.parse_args(argv)

    lines = read_lines(args.journal)
    if not lines:
        print(f"No readable lines in {args.journal}", file=sys.stderr)
        return 1
    if not args.all:
        lines = latest_cycle(lines)
    if args.ticker:
        wanted = {t.upper() for t in args.ticker}
        lines = [l for l in lines if l.ticker.upper() in wanted]

    when = max((l.when for l in lines if l.when), default=None)
    day = when.astimezone(timezone.utc).strftime("%Y-%m-%d") if when else ""
    actions = read_position_actions(args.audit, day) if day and not args.all else []
    print(render(lines, actions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
