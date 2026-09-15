"""Render one cycle's journal as something a person can actually read.

The journal is one JSON object per ticker per cycle. That is the right shape
for a scorer and the wrong shape for a human deciding whether to trust a
signal: the evidence the model weighed is in there, but spread across five
nested objects and a list of prompt lines with no links.

This renders it back out as Markdown, per ticker, with each dimension's score
printed next to the evidence that produced it -- so "news_score +0.8" sits
directly under the headlines it came from, and every headline is a link you
can open. That adjacency is the whole point: a score with its evidence out of
reach is an assertion.

Read-only, and offline. It reads the journal the cycle already wrote; it never
fetches anything, and it cannot place an order.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field, fields
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from orchestrator import analysts, fundamentals, insiders, technicals  # noqa: E402

#: Lines this far apart belong to different cycles. A daily cycle over 35
#: tickers takes a few minutes; 20 leaves room for a slow run without
#: swallowing yesterday's.
CYCLE_WINDOW_MINUTES = 20

#: The model's per-dimension scores, and the context section each one judges.
SCORE_SECTIONS = (
    ("news_score", "news", "NEWS"),
    ("technical_score", "technicals", "TECHNICALS"),
    ("fundamental_score", "fundamentals", "FUNDAMENTALS"),
    ("analyst_score", "analysts", "ANALYST & INSTITUTIONAL VIEW"),
    ("insider_score", "insiders", "INSIDER ACTIVITY"),
)


@dataclass(frozen=True)
class Line:
    """One journal line, kept whole rather than reduced to scorer fields."""

    raw: dict[str, Any]

    @property
    def ticker(self) -> str:
        return str(self.raw.get("ticker") or "?")

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


def _news_block(context: dict) -> list[str]:
    """Headlines as links when the cycle captured them, plain text otherwise."""
    sources = context.get("sources") or []
    headlines = context.get("headlines") or []
    if not headlines and not sources:
        return ["_No headlines found._"]

    out: list[str] = []
    if sources:
        for item in sources:
            if not isinstance(item, dict):
                continue
            title = str(item.get("title") or "").strip() or "(untitled)"
            url = str(item.get("url") or "").strip()
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
    out.append("_Links were not captured for this cycle._")
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
        return ["_Unavailable this cycle._"]
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


def render_ticker(line: Line) -> list[str]:
    """One ticker: what it concluded, then every input it concluded it from."""
    signal = line.signal or {}
    context = line.context
    bias = signal.get("bias") or "—"
    conviction = signal.get("conviction")
    conviction_text = f"{float(conviction):.2f}" if isinstance(conviction, (int, float)) else "n/a"

    out = [f"### {line.ticker} — {bias} @ {conviction_text}", ""]

    outcome = line.outcome or {}
    if outcome:
        status = outcome.get("status") or f"HTTP {outcome.get('http_status')}"
        reason = outcome.get("reason") or ""
        qty = outcome.get("quantity")
        bits = [f"**Engine:** {status}"]
        if qty:
            bits.append(f"{qty} shares")
        if reason:
            bits.append(str(reason))
        out += [" · ".join(bits), ""]
    elif line.raw.get("error"):
        out += [f"**Failed:** {line.raw['error']}", ""]
    elif line.screen and not signal.get("rationale"):
        out += ["**Screened out** by the first-stage model; the full model was not asked.", ""]

    if signal.get("rationale"):
        out += [f"> {signal['rationale']}", ""]

    factors = signal.get("key_factors") or []
    if factors:
        out += ["**What drove it:**"] + [f"- {f}" for f in factors] + [""]

    for score_field, context_key, title in SCORE_SECTIONS:
        if context_key not in context and context_key != "news":
            continue
        score = _fmt_score(signal.get(score_field)) if signal else "n/a"
        out += [f"<details><summary><b>{title}</b> — scored {score}</summary>", ""]
        if context_key == "news":
            out += _news_block(context)
        else:
            out += _snapshot_block(context.get(context_key), context_key)
        out += ["", "</details>", ""]

    gaps = context.get("gaps") or []
    if gaps:
        out += ["**Named gaps** (scored 0.0 rather than guessed):"]
        out += [f"- {g}" for g in gaps] + [""]

    return out


def render(lines: list[Line]) -> str:
    """The whole cycle, loudest signal first."""
    if not lines:
        return "# Cycle report\n\n_No journal lines found._\n"

    when = max((l.when for l in lines if l.when), default=None)
    stamp = when.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if when else "unknown time"

    traded = [l for l in lines if (l.outcome or {}).get("status") == "ACCEPTED"]
    failed = [l for l in lines if l.raw.get("error")]

    out = [
        "# Cycle report",
        "",
        f"**{stamp}** · {len(lines)} ticker{'' if len(lines) == 1 else 's'} · "
        f"{len(traded)} accepted by the engine · {len(failed)} failed",
        "",
        "Each dimension below shows the score the model gave it next to the "
        "evidence it was given. Open a section to see the inputs.",
        "",
    ]

    for line in sorted(lines, key=lambda l: (-l.conviction, l.ticker)):
        out += render_ticker(line)

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
