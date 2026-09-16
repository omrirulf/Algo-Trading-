#!/usr/bin/env python3
"""The book as a self-contained HTML page.

    python -m analysis.dashboard > book.html
    python -m analysis.dashboard --equity 100000 > book.html

Output goes to stdout and nowhere else: ``analysis/`` may read the record and
may not write anything, and a CI invariant fails the build if that stops being
true. The redirect is the caller's.

Why HTML rather than more Markdown
-----------------------------------
``logs/cycle_report.md`` is the day's reasoning and it has outgrown its
container: at 78 names it renders around half a megabyte, which is within a
rounding error of the size where GitHub stops rendering Markdown and shows the
source instead. It is also committed every trading day, so it grows the
repository by that much again each time -- for a file that is *derived*, and
which ``store/`` already gitignores the database equivalent of.

This page is the other half of the split: the state view, small, and rendered
rather than stored. The reasoning stays in the journal it is rendered from.

What it will not do
-------------------
It shows no price it was not given and no percentage it cannot compute. The
audit record carries entries and stops, not quotes and not account equity, so
unrealised P&L and cap utilisation appear only when ``--prices`` and
``--equity`` supply them. Where they are missing the page says which number is
missing and why, rather than filling the space with something that reads like
an answer.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.portfolio import (  # noqa: E402
    LADDER_RUNGS,
    Book,
    Exposure,
    Position,
    read_book,
)
from config import settings as cfg  # noqa: E402

#: Enough history for a trend to mean anything. The scorer already refuses to
#: conclude below 20 observations; a chart is more persuasive than a number,
#: so it gets the same floor rather than a looser one.
CHART_MIN_DAYS = 20

TITLE = "Position Book"


def _e(value: Any) -> str:
    """Escape anything bound for the page. Tickers and names come from files."""
    return html.escape(str(value), quote=True)


def _money(value: Optional[float], places: int = 2) -> str:
    if value is None:
        return "—"
    return f"{value:,.{places}f}"


def _signed(value: Optional[float], places: int = 2) -> str:
    if value is None:
        return "—"
    return f"{value:+,.{places}f}"


def _pct(value: Optional[float], places: int = 1) -> str:
    if value is None:
        return "—"
    return f"{value:.{places}f}%"


def _stamp(raw: Optional[str]) -> str:
    """The audit clock, rendered readably. Left alone when unparseable."""
    if not raw:
        return "no record yet"
    text = raw.split(",")[0]
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(text, fmt).strftime("%-d %b %Y, %H:%M")
        except ValueError:
            continue
    return text


# --------------------------------------------------------------------------- #
# Style
# --------------------------------------------------------------------------- #
# Tokens are declared in full on bare :root, then redefined -- tokens only --
# for each dark path. A colour whose only definition sits inside a media query
# is invisible in the un-stamped "system" state, which is what most viewers get.

STYLE = """
:root {
  --ground:      #f6f7f9;
  --surface:     #ffffff;
  --surface-sunk:#eef1f4;
  --ink:         #161b22;
  --ink-muted:   #5b6672;
  --ink-faint:   #8894a2;
  --rule:        #dde2e8;
  --rule-strong: #c6cdd6;
  --accent:      #1d5e7f;
  --long:        #10695c;
  --long-wash:   #e3f0ed;
  --short:       #8c4b3f;
  --short-wash:  #f6e8e5;
  --warn:        #9a6700;
  --crit:        #a32c24;
  --shadow:      0 1px 2px rgba(22, 27, 34, .06), 0 4px 12px rgba(22, 27, 34, .04);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ground:      #12151a;
    --surface:     #1a1f26;
    --surface-sunk:#232932;
    --ink:         #e6eaf0;
    --ink-muted:   #93a0ae;
    --ink-faint:   #6d7986;
    --rule:        #2a313a;
    --rule-strong: #3a434e;
    --accent:      #67aecd;
    --long:        #52b5a3;
    --long-wash:   #16302c;
    --short:       #d4907f;
    --short-wash:  #33211d;
    --warn:        #d9a441;
    --crit:        #e0716a;
    --shadow:      0 1px 2px rgba(0, 0, 0, .35), 0 4px 14px rgba(0, 0, 0, .25);
  }
}
:root[data-theme="dark"] {
  --ground:      #12151a;
  --surface:     #1a1f26;
  --surface-sunk:#232932;
  --ink:         #e6eaf0;
  --ink-muted:   #93a0ae;
  --ink-faint:   #6d7986;
  --rule:        #2a313a;
  --rule-strong: #3a434e;
  --accent:      #67aecd;
  --long:        #52b5a3;
  --long-wash:   #16302c;
  --short:       #d4907f;
  --short-wash:  #33211d;
  --warn:        #d9a441;
  --crit:        #e0716a;
  --shadow:      0 1px 2px rgba(0, 0, 0, .35), 0 4px 14px rgba(0, 0, 0, .25);
}

body {
  background: var(--ground);
  color: var(--ink);
  font-family: "Source Sans 3", ui-sans-serif, system-ui, -apple-system, sans-serif;
  font-size: 15px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}
.wrap {
  max-width: 1080px;
  margin: 0 auto;
  padding-inline: 20px;
  padding-block: 28px 56px;
}
h1, h2, h3 { font-family: Archivo, ui-sans-serif, system-ui, sans-serif; text-wrap: balance; }
h1 { font-size: 1.6rem; font-weight: 700; letter-spacing: -.01em; margin: 0; }
h2 {
  font-size: .78rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: .09em; color: var(--ink-muted);
  margin: 0 0 12px; padding-bottom: 8px; border-bottom: 1px solid var(--rule);
}
.num { font-family: "IBM Plex Mono", ui-monospace, SFMono-Regular, monospace; font-variant-numeric: tabular-nums; }

/* -- header ------------------------------------------------------------- */
header { display: flex; flex-wrap: wrap; gap: 6px 18px; align-items: baseline;
         margin-bottom: 6px; }
.asof { color: var(--ink-muted); font-size: .85rem; }
.lede { color: var(--ink-muted); margin: 0 0 30px; max-width: 62ch; }

/* -- the risk strip ----------------------------------------------------- */
.strip { display: grid; gap: 12px; margin-bottom: 34px;
         grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); }
.tile { background: var(--surface); border: 1px solid var(--rule); border-radius: 8px;
        padding: 14px 16px; box-shadow: var(--shadow); }
.tile .k { font-size: .72rem; text-transform: uppercase; letter-spacing: .07em;
           color: var(--ink-muted); }
.tile .v { font-size: 1.5rem; font-weight: 600; margin-top: 4px; display: block; }
.tile .sub { font-size: .8rem; color: var(--ink-faint); }
.tile.flag { border-color: var(--warn); }

/* -- the book ----------------------------------------------------------- */
.scroll { overflow-x: auto; margin-bottom: 34px; }
table { border-collapse: collapse; width: 100%; min-width: 660px; }
caption { text-align: left; color: var(--ink-muted); font-size: .85rem;
          padding-bottom: 10px; }
th { font-size: .7rem; text-transform: uppercase; letter-spacing: .07em;
     color: var(--ink-muted); font-weight: 600; text-align: right;
     padding: 0 10px 8px; border-bottom: 1px solid var(--rule-strong); }
th.l, td.l { text-align: left; }
td { padding: 11px 10px; border-bottom: 1px solid var(--rule); text-align: right;
     vertical-align: middle; }
tbody tr:last-child td { border-bottom: none; }
.name { font-weight: 600; }
.sub { display: block; font-size: .78rem; color: var(--ink-faint); font-weight: 400; }

/* Direction is identity, not judgement: a short is not a bad thing. The word
   carries it; the colour only reinforces. */
.dir { display: inline-block; font-size: .74rem; font-weight: 600; letter-spacing: .04em;
       padding: 2px 8px; border-radius: 999px; border: 1px solid currentColor; }
.dir.long  { color: var(--long);  background: var(--long-wash); }
.dir.short { color: var(--short); background: var(--short-wash); }

.bar { display: block; height: 4px; border-radius: 2px; background: var(--surface-sunk);
       margin-top: 5px; overflow: hidden; }
.bar > i { display: block; height: 100%; border-radius: 2px; background: var(--accent); }
.bar.safe > i { background: var(--long); }

.rung { display: inline-flex; gap: 3px; align-items: center; }
.rung b { width: 7px; height: 7px; border-radius: 50%; background: var(--rule-strong);
          display: inline-block; }
.rung b.on { background: var(--long); }
.tag { font-size: .72rem; color: var(--long); font-weight: 600; white-space: nowrap; }

/* -- exposure ----------------------------------------------------------- */
.meters { display: grid; gap: 22px; margin-bottom: 34px;
          grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); }
.meter { margin-bottom: 14px; }
.meter .row { display: flex; justify-content: space-between; align-items: baseline;
              gap: 10px; font-size: .88rem; }
.meter .row .r { color: var(--ink-muted); }
.track { height: 8px; border-radius: 4px; background: var(--surface-sunk);
         margin-top: 6px; position: relative; overflow: hidden; }
.track > i { display: block; height: 100%; border-radius: 4px; background: var(--accent); }
.track > u { position: absolute; top: -2px; bottom: -2px; width: 2px;
             background: var(--crit); text-decoration: none; }
.cap-note { font-size: .78rem; color: var(--ink-faint); margin-top: 4px; }
.over { color: var(--crit); font-weight: 600; }

/* -- notes -------------------------------------------------------------- */
.note { background: var(--surface); border: 1px solid var(--rule);
        border-left: 3px solid var(--accent); border-radius: 6px;
        padding: 14px 16px; margin-bottom: 14px; }
.note h3 { font-size: .92rem; margin: 0 0 4px; }
.note p { margin: 0; color: var(--ink-muted); font-size: .89rem; }
.empty { color: var(--ink-muted); padding: 28px 0; }
footer { margin-top: 40px; padding-top: 16px; border-top: 1px solid var(--rule);
         color: var(--ink-faint); font-size: .8rem; }

@media (max-width: 520px) {
  .wrap { padding-inline: 16px; }
  h1 { font-size: 1.35rem; }
  .tile .v { font-size: 1.28rem; }
}
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
"""


# --------------------------------------------------------------------------- #
# Fragments
# --------------------------------------------------------------------------- #


def _tiles(book: Book) -> str:
    risk = book.risk_dollars
    at_risk_label = "Locked in" if risk < 0 else "At risk if every stop fills"
    pnl = book.unrealised

    tiles = [
        (
            "Open positions",
            str(len(book.positions)),
            f"{len(book.longs)} long · {len(book.shorts)} short",
            False,
        ),
        (
            "Exposure at entry",
            "$" + _money(book.notional, 0),
            "sum of position sizes",
            False,
        ),
        (
            at_risk_label,
            "$" + _money(abs(risk), 0),
            "every stop, at once",
            False,
        ),
        (
            "Stops past entry",
            f"{book.protected_count} of {len(book.positions)}",
            "cannot lose from here",
            False,
        ),
    ]
    if pnl is not None:
        tiles.append((
            "Unrealised",
            "$" + _signed(pnl, 0),
            "at live prices" if book.marks_are_live else "at the last recorded prices",
            False,
        ))

    out = ['<section class="strip">']
    for key, value, sub, flag in tiles:
        out.append(
            f'<div class="tile{" flag" if flag else ""}">'
            f'<span class="k">{_e(key)}</span>'
            f'<span class="v num">{_e(value)}</span>'
            f'<span class="sub">{_e(sub)}</span></div>'
        )
    out.append("</section>")
    return "".join(out)


def _position_row(book: Book, p: Position) -> str:
    mark = book.mark_for(p)
    distance = p.stop_distance_pct or 0.0
    # The bar reads as "how much room before the stop", scaled so a typical
    # ATR-width stop fills a readable part of the track rather than a sliver.
    width = max(3.0, min(100.0, distance * 5.0))
    rungs = "".join(
        f'<b class="{"on" if i < p.rungs_taken else ""}"></b>'
        for i in range(len(LADDER_RUNGS))
    )
    protected = ' <span class="tag">protected</span>' if p.protected else ""

    cells = [
        f'<td class="l"><span class="name">{_e(p.name)}</span>'
        f'<span class="sub">{_e(p.ticker)} · {_e(p.sleeve)}</span></td>',
        f'<td class="l"><span class="dir {"long" if p.is_long else "short"}">'
        f'{_e(p.direction)}</span></td>',
        f'<td class="num">{_e(f"{p.quantity:,}")}</td>',
        f'<td class="num">{_e(_money(p.entry_price))}</td>',
        f'<td class="num">{_e(_money(p.stop))}'
        f'<span class="sub">{_e(_pct(p.stop_distance_pct))} away</span>'
        f'<span class="bar{" safe" if p.protected else ""}">'
        f'<i style="width:{width:.0f}%"></i></span></td>',
        f'<td class="num">{_e(_money(p.notional, 0))}</td>',
        f'<td class="num">{_e(_money(abs(p.risk_dollars), 0))}{protected}</td>',
    ]
    if book.marks_known:
        if mark.known:
            detail = (
                f'<span class="sub">{_e(f"{mark.r_multiple:+.2f}R")}</span>'
                if mark.r_multiple is not None
                else ""
            )
            cells.append(
                f'<td class="num">{_e(_signed(mark.unrealised, 0))}{detail}</td>'
            )
        else:
            # Opened this cycle, so the manager has not looked at it yet. Said
            # plainly rather than shown as a zero, which would read as flat.
            cells.append(
                '<td class="num">—<span class="sub">not checked yet</span></td>'
            )
    cells.append(f'<td class="l"><span class="rung">{rungs}</span></td>')
    return "<tr>" + "".join(cells) + "</tr>"


def _book_table(book: Book) -> str:
    if not book.positions:
        return (
            '<h2>The book</h2><p class="empty">No open positions in the record. '
            "Once a cycle accepts a signal it appears here.</p>"
        )
    headers = [
        ("Position", "l"), ("Side", "l"), ("Qty", ""), ("Entry", ""),
        ("Stop in force", ""), ("Size", ""), ("Risk", ""),
    ]
    if book.marks_known:
        headers.append(
            ("Unrealised" if book.marks_are_live else "Unrealised (recorded)", "")
        )
    headers.append(("Ladder", "l"))

    rows = "".join(
        _position_row(book, p)
        for p in sorted(book.positions, key=lambda x: -x.notional)
    )
    head = "".join(
        f'<th class="{cls}">{_e(label)}</th>' for label, cls in headers
    )
    return (
        "<h2>The book</h2>"
        '<div class="scroll"><table>'
        "<caption>Largest first, all figures in US dollars. Risk is what this "
        "position loses if its stop fills. The ladder sells a third at +1R and "
        "another at +3R; a filled dot is a rung already taken.</caption>"
        f"<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>"
    )


def _meter(exposure: Exposure) -> str:
    """One bucket. Share of the book is the bar; the cap is a marker on it."""
    share = exposure.share_of_book or 0.0
    used, cap = exposure.used_pct, exposure.cap_pct
    right = _pct(share) + " of book"
    note = f"${_money(exposure.notional, 0)}"

    marker = ""
    if used is not None and cap is not None:
        # With equity known the bar becomes cap-relative, which is the
        # question the caps are actually written in.
        share = min(100.0, used / (cap * 100.0) * 100.0)
        right = f"{_pct(used)} of equity"
        note = (
            f"${_money(exposure.notional, 0)} · cap {_pct(cap * 100, 0)} · "
            + (
                f'<span class="over">over by {_pct(abs(exposure.headroom_pct))}</span>'
                if exposure.over_cap
                else f"{_pct(exposure.headroom_pct)} of headroom left"
            )
        )
        marker = "<u></u>" if exposure.over_cap else ""

    return (
        '<div class="meter">'
        f'<div class="row"><span>{_e(exposure.label)}</span>'
        f'<span class="r num">{right}</span></div>'
        f'<div class="track"><i style="width:{min(100.0, max(1.0, share)):.0f}%"></i>{marker}</div>'
        f'<div class="cap-note num">{note}</div>'
        "</div>"
    )


def _exposure(book: Book) -> str:
    if not book.positions:
        return ""
    groups = "".join(_meter(e) for e in book.by_group())
    sleeves = "".join(_meter(e) for e in book.by_sleeve())
    # Gross as a share of the book is 100% by definition and says nothing. It
    # becomes a real number only once there is an equity to divide by.
    gross = _meter(book.gross()) if book.equity else ""

    denominator = (
        ""
        if book.equity
        else (
            '<div class="note"><h3>Cap use needs your account equity</h3>'
            "<p>Every cap is written as a percentage of equity, and the audit "
            "record keeps what was decided but not the equity it was decided "
            "against. Bars below show each bucket's share of the book, which is "
            "exact. Pass <span class=\"num\">--equity</span> to measure them "
            "against the caps instead.</p></div>"
        )
    )
    return (
        "<h2>Where the risk is concentrated</h2>"
        f"{denominator}"
        '<div class="meters">'
        f"<div><h3>By group</h3>{groups}</div>"
        f"<div><h3>By sleeve</h3>{sleeves}{gross}</div>"
        "</div>"
    )


def _not_yet(book: Book, days: int) -> str:
    """What the page deliberately does not show, and what would change that."""
    notes = []
    if not book.marks_known:
        notes.append((
            "No prices yet, so no profit or loss",
            "The record carries each entry and its stop, and the position "
            "manager has not yet written down a price for anything held. "
            "Rather than compute something that looks like P&L from a stale "
            "entry, this page leaves it out until there is a real mark.",
        ))
    elif not book.marks_are_live:
        stamps = [m.as_of for m in (book.mark_for(p) for p in book.positions) if m.as_of]
        when = _stamp(max(stamps)) if stamps else "the last cycle"
        notes.append((
            f"Profit and loss is as of {when}, not now",
            "These are the prices the position manager wrote down when it last "
            "checked the book, which is the most recent mark the record holds. "
            "They are a cycle old, not live, and a position opened since then "
            "has no mark at all. Supply current prices to replace them.",
        ))
    if days < CHART_MIN_DAYS:
        notes.append((
            f"Charts need about {CHART_MIN_DAYS} days; there are {days}",
            "A trend line through a handful of points is decoration, and a "
            "chart persuades harder than a number does. The scorer already "
            "refuses to conclude under 20 observations, and this holds to the "
            "same floor rather than a looser one.",
        ))
    if not notes:
        return ""
    body = "".join(
        f'<div class="note"><h3>{_e(title)}</h3><p>{_e(text)}</p></div>'
        for title, text in notes
    )
    return f"<h2>Not shown yet</h2>{body}"


# --------------------------------------------------------------------------- #
# The page
# --------------------------------------------------------------------------- #


def render(book: Book, *, days_of_history: int = 0) -> str:
    """One self-contained HTML page. No script, no fetch, no external data."""
    longs, shorts = len(book.longs), len(book.shorts)
    if book.positions:
        lede = (
            f"{len(book.positions)} positions are open — {longs} long and "
            f"{shorts} short — carrying ${_money(book.notional, 0)} of exposure. "
            f"If every stop filled at once the book would "
            + ("give back " if book.risk_dollars >= 0 else "keep ")
            + f"${_money(abs(book.risk_dollars), 0)}."
        )
    else:
        lede = "Nothing is open. This page fills in as soon as a cycle accepts a signal."

    return f"""<title>{TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Sans+3:wght@400;600&display=swap">
<style>{STYLE}</style>
<div class="wrap">
  <header>
    <h1>{TITLE}</h1>
    <span class="asof">as recorded {_e(_stamp(book.as_of))}</span>
  </header>
  <p class="lede">{lede}</p>
  {_tiles(book)}
  {_book_table(book)}
  {_exposure(book)}
  {_not_yet(book, days_of_history)}
  <footer>
    Reconstructed from <span class="num">logs/execution_audit.log</span> by
    <span class="num">analysis/dashboard.py</span> — the book as this system
    recorded its own decisions, which is not the same as the broker's copy of
    it. A stop that filled overnight shows here until the next cycle notices.
  </footer>
</div>
"""


def _days_of_history(journal_path: Path) -> int:
    """Distinct calendar days the journal covers. Zero if it cannot be read."""
    days: set[str] = set()
    try:
        text = journal_path.read_text(encoding="utf-8")
    except OSError:
        return 0
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            entry = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(entry, dict):
            stamp = str(entry.get("ts_utc") or entry.get("timestamp") or "")
            if len(stamp) >= 10:
                days.add(stamp[:10])
    return len(days)


def _prices_from(raw: Optional[str]) -> dict[str, float]:
    """``TICKER=PRICE,TICKER=PRICE`` into a mapping. Bad pairs are refused."""
    out: dict[str, float] = {}
    for chunk in (raw or "").split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        ticker, _, value = chunk.partition("=")
        try:
            out[ticker.strip().upper()] = float(value)
        except ValueError as exc:
            raise SystemExit(f"could not read a price from {chunk!r}: {exc}")
    return out


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="dashboard", description="Render the open book as an HTML page."
    )
    parser.add_argument("--audit", type=Path, default=cfg.AUDIT_LOG_PATH)
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument(
        "--equity", type=float, default=None,
        help="account equity, to measure exposure against the caps",
    )
    parser.add_argument(
        "--prices", default=None, metavar="TICKER=PRICE,...",
        help="current prices, to show unrealised profit and loss",
    )
    args = parser.parse_args(argv)

    # Written to stdout and never to a path, because ``analysis/`` is
    # read-only by construction and CI enforces it: the scorer and everything
    # beside it may read the record and may not touch it. The caller redirects
    # -- the same way the workflow already renders the Markdown report.
    book = read_book(args.audit, equity=args.equity, prices=_prices_from(args.prices))
    sys.stdout.write(render(book, days_of_history=_days_of_history(args.journal)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
