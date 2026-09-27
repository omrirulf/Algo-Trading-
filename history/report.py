"""The history screen's report, in plain words, from ``results.json`` alone.

Every number in the report comes from the results the screen wrote, so the
report can be written again from them without running anything. Returns are
after the registered cost (0.10% a side); a "t" is a Newey-West t (lag 3 for
race trades, which overlap for 3 sessions; lag 5 for funds' daily returns,
as registered). Nothing here decides anything.
"""

from __future__ import annotations

from typing import Any, Optional

RACE_ARMS = (("momentum", "Momentum (the locked rule)"), ("momentum_200", "A: momentum with the 200-day veto"))
FUND_LABELS = {
    "momentum": "Momentum fund",
    "momentum_200": "A fund (200-day veto)",
    "momentum_pullback": "C fund (pullback limit)",
    "vt_timing": "B fund (VT or T-bills)",
    "vt_timing_on_spy": "B's rule on SPY (check only)",
    "vt": "VT fund (held)",
    "spy": "SPY fund (held)",
}


def pct(value: Optional[float], digits: int = 2, signed: bool = True) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:{'+' if signed else ''}.{digits}f}%"


def num(value: Optional[float], digits: int = 2) -> str:
    return "n/a" if value is None else f"{value:+.{digits}f}"


def count(value: Optional[int]) -> str:
    return "n/a" if value is None else f"{value:,}"


def _get(data: Any, *path: str, default: Any = None) -> Any:
    for key in path:
        if not isinstance(data, dict) or key not in data:
            return default
        data = data[key]
    return data


def _table(header: list[str], rows: list[list[str]]) -> list[str]:
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    out += ["| " + " | ".join(row) + " |" for row in rows]
    return out


def _test(block: Optional[dict], digits: int = 3) -> str:
    """A paired result as "mean (t)"."""
    if not block or block.get("mean") is None:
        return "n/a"
    return f"{pct(block['mean'], digits)} (t {num(block.get('t'))})"


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #


def _header(results: dict) -> list[str]:
    meta = results.get("meta", {})
    run = meta.get("run") or {}
    where = []
    if run.get("run_id"):
        where.append(f"workflow run {run['run_id']}")
    if run.get("commit"):
        where.append(f"commit `{run['commit'][:12]}`")
    return [
        "# History screen: the rules that run live, on past prices",
        "",
        f"*Written by `python -m history.screen run` ({', '.join(where) or 'a local run'}) on "
        f"{meta.get('generated_at', 'n/a')}. Lines from {meta.get('first_line_day', 'n/a')}; prices through "
        f"{meta.get('final_through', 'n/a')}. Price table SHA-256 `{meta.get('prices_sha256', 'n/a')}`; history "
        f"journal SHA-256 `{meta.get('journal_sha256', 'n/a')}` ({count(meta.get('journal_lines'))} lines).*",
        "",
        "**Nothing here changes the locked test, its rules or its decisions.** This is a history screen: "
        "it replays, on past prices, the rules that already run live, with the real code. It did not read "
        "the live race.",
        "",
    ]


def _method(results: dict) -> list[str]:
    meta = results.get("meta", {})
    missing = meta.get("missing_tickers") or []
    return [
        "## How it was made",
        "",
        "- **Names:** the watchlist as it is today (80 names), from 2000 or from each name's first price. "
        "Most funds started later than 2000, so the early years have fewer names (see *Data*). "
        + (f"No prices at all for: {', '.join(missing)}. " if missing else "")
        + "**Survivorship:** the list was chosen in 2026, so funds and companies that closed or failed "
        "before then are missing. This flatters \"always long\" and the long side most.",
        "- **Journal:** one line per name per session, built from prices only. Technicals come from "
        "production's own function (`build_snapshot`) on the two years of final daily closes up to the "
        "**previous session**. A live line also has the current session's partial bar; history does not. So "
        "a history line knows about one session less than a live line.",
        "- **Live price:** there is none in the past. **The previous session's final close stands in for "
        "it.** A's veto compares that price with the 200-day average, and C's limit is set from it.",
        f"- **Race:** the race's own scoring. Enter at the next open, hold {meta.get('horizon', 3)} sessions, "
        "the ATR stop, the conviction floor 0.30, "
        f"{pct(meta.get('cost_per_side'), 2, False)} per side. No taxes. The coin flip is the race's own "
        f"(`rules/control.py`), {count(meta.get('seeds'))} seeds, on each rule's own lines.",
        "- **Funds:** the production engine and position manager, $100,000 each, the same costs, dividends "
        "paid. No name is held by a real account in the past, and no short refusal (they date from 2026) "
        "applies.",
        "- **Not tested:** anything that uses the AI (the model, the hybrid, and the three model funds). The "
        "AI has read about the past, so only live results can test it.",
        "- **t:** Newey-West t, lag 3 for race trades and lag 5 for fund days, as registered. Above about 2 "
        "(or below -2) is unlikely to be luck alone; these screens are many, so read a t near 2 with care.",
        "",
    ]


def _race_arm(results: dict, name: str, label: str) -> list[str]:
    arm = _get(results, "race", "arms", name) or {}
    periods = arm.get("periods") or {}
    lines = [f"### {label}", ""]
    rows = []
    for period, p in periods.items():
        band = _get(p, "coin_flip_band", "mean/day") or {}
        rows.append([
            period, count(p.get("trades")), pct(p.get("mean_net"), 3), pct(p.get("hit_rate"), 1, False),
            pct(p.get("mean_per_day"), 3),
            f"{pct(band.get('low'), 3)} to {pct(band.get('high'), 3)}" if band else "n/a",
            f"{band['percentile']:.0f}" if band.get("percentile") is not None else "n/a",
            _test(p.get("vs_coin_flip_expected")),
            _test(_get(p, "always_long_same_lines", "paired")),
            _test(_get(p, "always_long_every_line", "paired")),
        ])
    lines += _table(["Years", "Trades", "Mean per trade", "Hit rate", "Mean per day",
                     "Coin flip, mean per day (5th to 95th)", "Percentile in the coin flip",
                     "Minus a coin flip (per day, t)", "Minus always long, same lines (per day, t)",
                     "Minus always long, every line (per day, t)"], rows)
    lines += ["", "Longs and shorts:", ""]
    rows = []
    for period, p in periods.items():
        for side in ("longs", "shorts"):
            s = p.get(side) or {}
            rows.append([period, side, count(s.get("n")), pct(s.get("mean_net"), 3),
                         pct(s.get("hit_rate"), 1, False), _test(s.get("vs_coin_flip_expected")),
                         _test(s.get("vs_always_long_every_line_same_days")) if side == "longs" else "-"])
    lines += _table(["Years", "Side", "Trades", "Mean per trade", "Hit rate", "Minus a coin flip (per day, t)",
                     "Minus always long, every line, same days (per day, t)"], rows)
    every = _get(periods, next(iter(periods), ""), "always_long_every_line") or {}
    if every:
        lines += ["", f"For scale, *always long on every line* (every name bought for 3 sessions, every day), "
                  f"all years: {count(every.get('trades'))} trades, {pct(every.get('mean_net'), 3)} per trade, "
                  f"hit rate {pct(every.get('hit_rate'), 1, False)}."]
    return lines + [""]


def _race(results: dict) -> list[str]:
    lines = ["## 1. The race (3-session trades)", "",
             "Each rule's trades, as the live race scores them. *Mean per day* is the race's main number: the "
             "mean net return of the trades opened each entry day, 0 on a day with none. *Minus a coin flip*: "
             "the rule's trade minus what a coin flip earns on the same line on average. *Always long*: the "
             "same trade, bought.", ""]
    for name, label in RACE_ARMS:
        lines += _race_arm(results, name, label)
    veto = _get(results, "race", "veto_vs_momentum") or {}
    counters = _get(results, "funds", "counters", "momentum_200") or {}
    lines += ["### A against momentum", "", "A's main race number (section 13.2): A minus momentum, per day.", ""]
    rows = []
    for period, p in veto.items():
        c = counters.get(period) or {}
        rows.append([period, count(c.get("signals")), count(c.get("vetoed")), pct(c.get("vetoed_share"), 1, False),
                     count(c.get("no_average")), _test(p)])
    lines += _table(["Years", "Momentum signals", "Vetoed by A", "Veto share", "No 200-day average yet",
                     "A minus momentum (per day, t)"], rows)
    return lines + [""]


def _fund_rows(results: dict, names: tuple[str, ...]) -> list[str]:
    rows = []
    for name in names:
        fund = _get(results, "funds", "funds", name) or {}
        for period, p in (fund.get("periods") or {}).items():
            f = p.get("fund") or {}
            vt = p.get("vs_vt") or {}
            rows.append([
                FUND_LABELS.get(name, name), period, pct(f.get("total_return"), 1), pct(f.get("annualised"), 1),
                pct(f.get("max_drawdown"), 1, False), pct(f.get("mean_invested"), 0, False),
                _test(vt, 4),
                pct(_get(vt, "fund", "annualised"), 1) + " vs " + pct(_get(vt, "compared", "annualised"), 1),
                pct(_get(vt, "fund", "max_drawdown"), 1, False) + " vs "
                + pct(_get(vt, "compared", "max_drawdown"), 1, False),
                _test(p.get("vs_spy"), 4),
            ])
    return _table(["Fund", "Years", "Total return", "A year", "Worst fall", "Invested (mean)",
                   "Minus VT fund (per day, t)", "A year: fund vs VT (same days)", "Worst fall: fund vs VT",
                   "Minus SPY fund (per day, t)"], rows)


def _funds(results: dict) -> list[str]:
    funds = _get(results, "funds", "funds") or {}
    vt_first = _get(results, "funds", "vt_first_session")
    lines = ["## 2. The funds (the production engine)", "",
             f"Each fund against the VT fund (VT bought and held). VT has prices only from {vt_first or 'n/a'}, so "
             f"every comparison with VT starts there; the SPY fund (SPY bought and held from the first session) is "
             f"a longer yardstick. *Invested* is the book's gross exposure as a share of equity; *worst fall* is "
             f"the maximum drawdown.", ""]
    lines += _fund_rows(results, ("momentum", "momentum_200", "momentum_pullback"))
    lines += ["", "Held funds, for scale:", ""]
    rows = []
    for name in ("vt", "spy"):
        for period, p in ((funds.get(name) or {}).get("periods") or {}).items():
            f = p.get("fund") or {}
            rows.append([FUND_LABELS[name], period, f.get("from", "n/a"), pct(f.get("total_return"), 1),
                         pct(f.get("annualised"), 1), pct(f.get("max_drawdown"), 1, False)])
    lines += _table(["Fund", "Years", "From", "Total return", "A year", "Worst fall"], rows)
    lines += ["", "Longs and shorts in the funds (closed trades; the return is the trade's profit over what it "
              "cost to open, costs and dividends in):", ""]
    rows = []
    for name in ("momentum", "momentum_200", "momentum_pullback"):
        for period, p in ((funds.get(name) or {}).get("periods") or {}).items():
            t = p.get("trades") or {}
            for side in ("long", "short"):
                s = _get(t, "sides", side) or {}
                rows.append([FUND_LABELS[name], period, side, count(s.get("n")), pct(s.get("mean_return"), 2),
                             pct(s.get("hit_rate"), 1, False)])
    lines += _table(["Fund", "Years", "Side", "Closed trades", "Mean return", "Hit rate"], rows)
    lines += ["", "A and C against the momentum fund (their registered comparator, section 13):", ""]
    rows = []
    for name in ("momentum_200", "momentum_pullback"):
        for period, p in ((funds.get(name) or {}).get("periods") or {}).items():
            m = p.get("vs_momentum") or {}
            rows.append([FUND_LABELS[name], period, _test(m, 4),
                         pct(_get(m, "fund", "total_return"), 1) + " vs "
                         + pct(_get(m, "compared", "total_return"), 1)])
    lines += _table(["Fund", "Years", "Minus momentum fund (per day, t)", "Total return: fund vs momentum fund"], rows)
    room = (funds.get("momentum") or {}).get("order_matters") or {}
    if room.get("cycle_days"):
        share = room.get("days", 0) / room["cycle_days"]
        lines += ["", f"The momentum fund ran out of room (cash, the gross cap, a group or sleeve cap, the "
                  f"stock-market limit or the 40-position limit) before the end of the list on "
                  f"{count(room.get('days'))} of {count(room.get('cycle_days'))} cycle days "
                  f"({pct(share, 0, False)}), skipping {count(room.get('skipped'))} signals. On those days "
                  f"watchlist order, not the signal, decided what it bought."]
    return lines + [""]


def _b(results: dict) -> list[str]:
    funds = _get(results, "funds", "funds") or {}
    counters = _get(results, "funds", "counters") or {}
    vt_first = _get(results, "funds", "vt_first_session") or "n/a"
    b_days = _get(funds, "vt_timing", "periods", "all years", "vs_vt", "from") or "n/a"
    crash = " So B's history starts after the 2008 crash." if b_days > "2009-03" else ""
    lines = ["## 3. B: VT or T-bills by the 10-month average", "",
             f"The registered rule on VT. VT has prices from {vt_first}, so B's first decision is the first "
             f"month-end with ten month-end closes, and B holds from {b_days}.{crash} Beside it, B's own code with SPY in place of VT, from the first "
             f"month-end BIL (the T-bills) had prices ({_get(counters, 'vt_timing_on_spy', 'first_month_end') or 'n/a'}): "
             f"not the registered rule, a check against the owner's quick test on SPY. *Worst fall* is the "
             f"maximum drawdown.", ""]
    rows = []
    for name, compared in (("vt_timing", "vs_vt"), ("vt_timing_on_spy", "vs_spy")):
        fund = funds.get(name) or {}
        for period, p in (fund.get("periods") or {}).items():
            m = p.get(compared) or {}
            if not m.get("days"):
                continue
            rows.append([FUND_LABELS[name], period, f"{m.get('from')} to {m.get('to')}",
                         pct(_get(m, "fund", "annualised"), 1) + " vs " + pct(_get(m, "compared", "annualised"), 1),
                         pct(_get(m, "fund", "max_drawdown"), 1, False) + " vs "
                         + pct(_get(m, "compared", "max_drawdown"), 1, False), _test(m, 4)])
    lines += _table(["Fund", "Years", "Days", "A year: B vs held", "Worst fall: B vs held",
                     "B minus held (per day, t)"], rows)
    for name in ("vt_timing", "vt_timing_on_spy"):
        c = counters.get(name) or {}
        lines += ["", f"{FUND_LABELS[name]}: {count(c.get('switches'))} switches, "
                  f"{count(c.get('days_out_of_vt'))} trading days out of the market, now in "
                  f"{c.get('state') or 'n/a'} (last month-end {c.get('last_signal') or 'n/a'})."]
    return lines + [""]


def _c(results: dict) -> list[str]:
    counters = _get(results, "funds", "counters", "momentum_pullback") or {}
    race = _get(results, "race", "pullback_filled_vs_missed") or {}
    orders = _get(results, "funds", "funds", "momentum_pullback", "orders") or {}
    lines = ["## 4. C: the pullback limit", "",
             "Would each momentum signal's limit (signal price minus half the ATR; a short, plus) have filled "
             "in its 3 sessions? Counted from prices, as the live counter is.", ""]
    rows = [[period, count(c.get("filled")), count(c.get("missed")), pct(c.get("fill_rate"), 1, False)]
            for period, c in counters.items()]
    lines += _table(["Years", "Filled", "Missed", "Fill rate"], rows)
    lines += ["", "The race trade (next open, 3 sessions) of signals whose limit filled against those whose "
              "limit did not. **Read with care:** a long's limit fills only if the price falls first, inside "
              "the same 3 sessions the race trade is scored on, so filled signals must look worse here. This "
              "says what C avoids, not what C earns; C's result is its fund (section 2).", ""]
    rows = []
    for period, p in race.items():
        for label in ("all", "longs", "shorts"):
            b = p.get(label) or {}
            rows.append([period, label, count(_get(b, "filled", "n")), pct(_get(b, "filled", "mean_net"), 2),
                         count(_get(b, "missed", "n")), pct(_get(b, "missed", "mean_net"), 2),
                         pct(b.get("missed_minus_filled"), 2), num(b.get("welch_t"))])
    lines += _table(["Years", "Side", "Filled", "Filled: mean", "Missed", "Missed: mean", "Missed minus filled",
                     "Welch t (reading only)"], rows)
    if orders:
        lines += ["", f"In the C fund: {count(orders.get('placed'))} orders placed, "
                  f"{count(orders.get('filled_open'))} filled at the open and {count(orders.get('filled_range'))} "
                  f"during the day ({pct(orders.get('fill_rate_of_orders'), 1, False)}), "
                  f"{count(orders.get('missed'))} cancelled after 3 sessions, {count(orders.get('no_room'))} "
                  f"filled but refused for lack of room; {count(orders.get('acted_differently'))} signals on "
                  f"which C and the momentum fund did differently (section 13.7)."]
    return lines + [""]


def _context(results: dict) -> list[str]:
    all_years = _get(results, "race", "arms", "momentum", "periods", "all years") or {}
    band = _get(all_years, "coin_flip_band", "mean/day") or {}
    edge = all_years.get("vs_coin_flip_expected") or {}
    percentile = band.get("percentile")
    t = edge.get("t")
    inside = percentile is not None and 5.0 <= percentile <= 95.0
    close = inside and t is not None and abs(t) < 2.0
    verdict = (
        "On history, momentum's 3-session trades are **close to a coin flip**: inside the coin flip's band "
        if close else
        "On history, momentum's 3-session trades are **not the same as a coin flip**: "
    ) + (f"(percentile {percentile:.0f}; minus a coin flip {pct(edge.get('mean'), 3)} per day, t {num(t)})."
         if percentile is not None else "(no band).")
    return [
        "## 5. What this means for the live race (context only)",
        "",
        verdict,
        "",
        "The owner's observation, written here as context: *at a 3-day horizon, momentum looks close to random "
        "on history. So in the live race, \"the AI beats momentum\" may mean little more than \"the AI beats "
        "random\".* The race already has the coin flip as its floor (the model must also be above the 95th "
        "percentile of its own coin flip, section 5), and the index test (the winner must beat VT). This "
        "screen **changes nothing in the locked test**: the arms, the metric, the looks and the decision rule "
        "stay as registered.",
        "",
    ]


def _data(results: dict) -> list[str]:
    data = results.get("data") or {}
    rows = []
    for c in data.get("coverage") or []:
        rows.append([c["ticker"], c.get("first") or "no prices", count(c.get("bars"))])
    by_year = _get(results, "race", "lines_by_year") or {}
    gaps = data.get("price_gaps") or {}
    cal = data.get("calendar_vs_production") or {}
    integrity = _get(results, "funds", "integrity") or {}
    lines = ["## 6. Data", "",
             "Lines per year: " + ", ".join(f"{y}: {count(n)}" for y, n in sorted(by_year.items())) + ".", "",
             f"Missing price days (a name trading, no bar): {count(gaps.get('missing'))} of "
             f"{count(gaps.get('ticker_days'))} ticker-days ({pct(gaps.get('share'), 2, False)}).", "",
             "The calendar is the days SPY traded (production's list covers 2025-2027 only). Where it differs "
             f"from production's list since 2025: {cal or 'nowhere'}.", "",
             f"Fund integrity: {'no problems' if integrity.get('ok') else integrity.get('problems')}; "
             f"{count(integrity.get('data_holes'))} ticker-days with no bar met by the funds.", "",
             "First price of each name:", ""]
    lines += _table(["Name", "First bar", "Bars"], rows)
    return lines + [""]


def render(results: dict) -> str:
    lines: list[str] = []
    for section in (_header, _method, _race, _funds, _b, _c, _context, _data):
        lines += section(results)
    return "\n".join(lines).rstrip() + "\n"


__all__ = ["render"]
