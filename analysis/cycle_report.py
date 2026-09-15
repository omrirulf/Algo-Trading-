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
from orchestrator import analysts, fundamentals, insiders, technicals  # noqa: E402
from orchestrator.news import absolute_url  # noqa: E402

#: Lines this far apart belong to different cycles. A daily cycle over 35
#: tickers takes a few minutes; 20 leaves room for a slow run without
#: swallowing yesterday's.
CYCLE_WINDOW_MINUTES = 20

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
SCORE_SECTIONS = (
    ("news_score", "news", "News"),
    ("technical_score", "technicals", "Price and chart"),
    ("fundamental_score", "fundamentals", "Company numbers"),
    ("analyst_score", "analysts", "What analysts and big funds say"),
    ("insider_score", "insiders", "Buying and selling by company insiders"),
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
    ("Confidence", "How sure the model is, from 0.00 to 1.00. A trade needs 0.60 or more."),
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
        "confidence reaches **0.60**. Below that the system writes down what it "
        "thought and does nothing. The size of a trade, the stop-loss and every "
        "limit are decided by plain code, not by the model.",
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


def render(lines: list[Line]) -> str:
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

    print(render(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
