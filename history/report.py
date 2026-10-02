"""The history screen's report, in plain words, from ``results.json`` alone.

Every number in the report comes from the results the screen wrote, so the
report can be written again from them without running anything. Returns are
after the registered cost (0.10% a side); a "t" is a Newey-West t (lag 3 for
race trades, which overlap for 3 sessions; lag 5 for funds' daily returns,
as registered). Nothing here decides anything.

Sections of the pre-registration are always named as such ("pre-registration
section 13.2"); a bare "section 2" is this report's own.

The stress kind (``history.stress``, the owner's instruction of 2 Oct 2026)
has its own report, ``render_stress``: each period's funds, their total
return, worst fall and return against VT and SPY, and the regime split's
volatility cut-offs. Descriptive only: no t and no verdict. ``render`` picks
it from ``meta.kind``.
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
#: A t this far from 0 is the report's line between "no clear difference" and a difference.
CLEAR_T = 2.0
#: The 5th to 95th percentile of a normal spread is this many standard deviations wide.
BAND_WIDTH_SD = 3.29
YEAR = 252


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


def _band(block: Optional[dict], digits: int = 3, signed: bool = True) -> list[str]:
    """One coin-flip band as three cells: the rule's value, the 5th to 95th percentile, the percentile."""
    if not block:
        return ["n/a", "n/a", "n/a"]
    return [pct(block.get("value"), digits, signed),
            f"{pct(block.get('low'), digits, signed)} to {pct(block.get('high'), digits, signed)}",
            f"{block['percentile']:.0f}" if block.get("percentile") is not None else "n/a"]


def band_ratio(period: Optional[dict]) -> Optional[float]:
    """How many times wider the paired t's error is than the coin-flip band's own spread (per day).

    The band's spread is its 5th-to-95th width over 3.29; the t's error is
    |mean| / |t| of "minus a coin flip". Equal if the rule's calls were as
    independent as the coin flips; larger when its calls cluster on days when
    names move together.
    """
    band = _get(period, "coin_flip_band", "mean/day") or {}
    edge = _get(period, "vs_coin_flip_expected") or {}
    if band.get("low") is None or band.get("high") is None or not edge.get("t") or edge.get("mean") is None:
        return None
    spread = (band["high"] - band["low"]) / BAND_WIDTH_SD
    return abs(edge["mean"] / edge["t"]) / spread if spread > 0 else None


def verdict(edge: Optional[dict]) -> str:
    """Better than, worse than, or no clear difference from a coin flip, read from the paired t."""
    if not edge or edge.get("t") is None or edge.get("mean") is None:
        return "not known (no paired test)"
    if abs(edge["t"]) < CLEAR_T:
        return "no clear difference from a coin flip"
    return "better than a coin flip" if edge["mean"] > 0 else "worse than a coin flip"


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
        f"{meta.get('generated_at', 'n/a')}. Lines from {meta.get('first_line_day', 'n/a')} to the last session "
        f"{meta.get('last_session', meta.get('final_through', 'n/a'))}. Price table SHA-256 "
        f"`{meta.get('prices_sha256', 'n/a')}`; history journal SHA-256 `{meta.get('journal_sha256', 'n/a')}` "
        f"({count(meta.get('journal_lines'))} lines).*",
        "",
        "**Nothing here changes the locked test, its rules or its decisions.** This is a history screen: "
        "it replays, on past prices, the rules that already run live, with the real code. It did not read "
        "the live race.",
        "",
    ]


def _under_a_dollar(results: dict) -> str:
    race = _get(results, "race", "arms", "momentum", "periods", "all years") or {}
    under = race.get("entry_under_1_dollar") or {}
    funds = _get(results, "funds", "funds", "momentum", "periods", "all years", "trades") or {}
    names = ", ".join(under.get("by_name") or {}) or "none"
    return (f"{count(under.get('trades'))} of momentum's {count(race.get('trades'))} race trades, and "
            f"{count(funds.get('entries_under_1_dollar'))} of the momentum fund's {count(funds.get('entries'))} "
            f"entries, were under $1 (names: {names})")


def _method(results: dict) -> list[str]:
    meta = results.get("meta", {})
    missing = meta.get("missing_tickers") or []
    return [
        "## How it was made",
        "",
        f"- **Names:** the watchlist as it is today ({count(meta.get('watchlist_names'))} names), from 2000 or "
        "from each name's first price. Most ETFs on the list started trading after 2000, so the early years have "
        "fewer names (see *Data*). "
        + (f"No prices at all for: {', '.join(missing)}. " if missing else "")
        + "**Survivorship:** the list was chosen in 2026, so funds and companies that closed or failed "
        "before then are missing. This flatters \"always long\" and the long side most.",
        "- **Journal:** one line per name per session, built from prices only. Technicals come from "
        "production's own function (`build_snapshot`) on the two years of final daily closes up to the "
        "**previous session**. A live line also has the current session's partial bar; history does not. So "
        "a history line knows about one session less than a live line.",
        "- **Live price:** there is none in the past. **The previous session's final close stands in for "
        "it.** A's veto compares that price with the 200-day average, and C's limit is set from it.",
        "- **Prices:** Yahoo's daily bars, adjusted for splits (not for dividends), as production reads them. "
        "A name that later split many times trades far under $1 in the early years, where the engine's stops, "
        f"rounded to the cent, are coarse: {_under_a_dollar(results)}. They are counted, not removed.",
        f"- **Race:** the race's own scoring. Enter at the next open, hold {meta.get('horizon', 3)} sessions, "
        "the ATR stop, the conviction floor 0.30, "
        f"{pct(meta.get('cost_per_side'), 2, False)} per side. No taxes. The coin flip is the race's own "
        f"(`rules/control.py`), {count(meta.get('seeds'))} seeds, on each rule's own lines. The race is run one "
        "calendar year at a time with fresh price sources, as the live race's are: each year's ATR warms up "
        "from 40 days before its first line, so stops in the first weeks of a year can differ a little from "
        "one run over all the years.",
        "- **Funds:** the production engine and position manager, $100,000 each, the same costs. No name is "
        "held by a real account in the past, and no short refusal (they date from 2026) applies. Dividends: "
        "the held funds (VT, SPY) keep them as cash, as the registered VT fund does; B puts all its cash, "
        "dividends too, back to work at each switch.",
        "- **Not tested:** anything that uses the AI (the model, the hybrid, and the three model funds). The "
        "AI has read about the past, so only live results can test it.",
        "- **Words:** *mean per trade* is a trade's return after costs; *mean per day* is the race's main "
        "number, the mean of the trades opened each entry day (0 on a day with none); *a year* is the "
        "yearly rate, compounded over 252 sessions a year (on a slice shorter than a year it exaggerates, so "
        "read the total there); *worst fall* is the maximum drawdown.",
        "- **t:** Newey-West t, lag 3 for race trades and lag 5 for fund days, as registered. Beyond about "
        "+2 or -2 is unlikely to be luck alone; there are many screens and many slices here, so read a t "
        "near 2 with care.",
        "",
    ]


def _race_arm(results: dict, name: str, label: str) -> list[str]:
    arm = _get(results, "race", "arms", name) or {}
    periods = arm.get("periods") or {}
    lines = [f"### {label}", ""]
    rows = []
    for period, p in periods.items():
        rows.append([
            period, count(p.get("trades")), pct(p.get("mean_net"), 3), pct(p.get("hit_rate"), 1, False),
            pct(p.get("mean_per_day"), 3), _test(p.get("vs_coin_flip_expected")),
            _test(_get(p, "always_long_same_lines", "paired")), _test(_get(p, "always_long_every_line", "paired")),
        ])
    lines += _table(["Years", "Trades", "Mean per trade", "Hit rate", "Mean per day", "Minus a coin flip (per day, t)",
                     "Minus always long, same lines (per day, t)", "Minus always long, every line (per day, t)"],
                    rows)
    lines += ["", "The race's coin-flip band on the rule's own lines (read the t above first):", ""]
    rows = []
    for period, p in periods.items():
        bands = p.get("coin_flip_band") or {}
        long_same = _get(bands, "mean/day", "others", "always long, same lines") or {}
        rows.append([period, *_band(bands.get("mean net")), *_band(bands.get("hit rate"), 1, False),
                     *_band(bands.get("mean/day")),
                     f"{long_same['percentile']:.0f}" if long_same.get("percentile") is not None else "n/a"])
    lines += _table(["Years", "Mean per trade", "Coin flip", "Percentile", "Hit rate", "Coin flip", "Percentile",
                     "Mean per day", "Coin flip", "Percentile", "Always long, same lines: percentile"], rows)
    lines += ["", "Longs and shorts. *Same side, every line* takes the same side on every line on the same days: "
              "it asks whether the rule picked the right names for that side.", ""]
    rows = []
    for period, p in periods.items():
        for side in ("longs", "shorts"):
            s = p.get(side) or {}
            rows.append([period, side, count(s.get("n")), pct(s.get("mean_net"), 3), pct(s.get("hit_rate"), 1, False),
                         pct(s.get("same_side_every_line_mean_net"), 3),
                         _test(s.get("vs_same_side_every_line_same_days"))])
    lines += _table(["Years", "Side", "Trades", "Mean per trade", "Hit rate", "Same side, every line (per day)",
                     "Minus same side, every line (per day, t)"], rows)
    every = _get(periods, next(iter(periods), ""), "always_long_every_line") or {}
    if every:
        lines += ["", f"For scale, *always long on every line* (every name bought for 3 sessions, every day), "
                  f"all years: {count(every.get('trades'))} trades, {pct(every.get('mean_net'), 3)} per trade, "
                  f"hit rate {pct(every.get('hit_rate'), 1, False)}."]
    return lines + [""]


def _race(results: dict) -> list[str]:
    ratio = band_ratio(_get(results, "race", "arms", "momentum", "periods", "all years"))
    lines = ["## 1. The race (3-session trades)", "",
             "Each rule's trades, as the live race scores them. *Minus a coin flip*: the rule's trade minus what "
             "a coin flip earns on the same line on average, day by day. *Always long*: the same trade, bought.",
             "",
             "**How to read the coin-flip band.** Each coin flip picks long or short for every line on its own. "
             "A real rule does not: momentum goes long on most names on the same days, and those names move "
             "together. So the band is much narrower than the real uncertainty"
             + (f" (here the t's own error is about {ratio:.1f} times the band's spread)" if ratio else "")
             + ", and a rule with no skill can land outside it. The t (*minus a coin flip*) allows for this; "
             "the band is the race's registered yardstick (the live race's condition 3, pre-registration "
             "section 5, reads the same band), shown for completeness.", ""]
    for name, label in RACE_ARMS:
        lines += _race_arm(results, name, label)
    veto = _get(results, "race", "veto_vs_momentum") or {}
    counters = _get(results, "funds", "counters", "momentum_200") or {}
    lines += ["### A against momentum", "",
              "A's main race number (pre-registration section 13.2): A minus momentum, per day. The signal counts "
              "are cut by the signal's day and the race by the trade's entry day, one session later.", ""]
    rows = []
    for period, p in veto.items():
        c = counters.get(period) or {}
        rows.append([period, count(c.get("signals")), count(c.get("vetoed")), pct(c.get("vetoed_share"), 1, False),
                     count(c.get("no_average")), _test(p)])
    lines += _table(["Years", "Momentum signals (at or above 0.30)", "Vetoed by A", "Veto share",
                     "No 200-day average yet (kept)", "A minus momentum (per day, t)"], rows)
    share = _get(counters, "all years", "vetoed_share")
    if share is not None and share < 0.10:
        lines += ["", f"The veto removed {pct(share, 1, False)} of momentum's signals, under the 10% named in "
                  "the pre-registration (section 13.2): **A is then almost the momentum rule, and its result "
                  "says little.**"]
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
             f"a longer yardstick. *Invested* is the book's gross exposure as a share of equity.", ""]
    lines += _fund_rows(results, ("momentum", "momentum_200", "momentum_pullback"))
    lines += ["", "How the funds trade: positions are closed by the ATR stop and the profit ladder, so they are held "
              "for days, not months, and every entry and exit pays 0.10%.", ""]
    rows = []
    for name in ("momentum", "momentum_200", "momentum_pullback"):
        for period, p in ((funds.get(name) or {}).get("periods") or {}).items():
            t = p.get("trades") or {}
            f = p.get("fund") or {}
            rows.append([FUND_LABELS[name], period, count(t.get("entries")),
                         f"{f.get('mean_positions'):.0f}" if f.get("mean_positions") is not None else "n/a",
                         f"{t['mean_days_held']:.1f}" if t.get("mean_days_held") is not None else "n/a",
                         pct(t.get("costs_per_year"), 1, False), pct(t.get("win_rate"), 1, False)])
    lines += _table(["Fund", "Years", "Entries", "Positions (mean)", "Days held (mean)", "Costs a year",
                     "Closed trades won"], rows)
    lines += ["", "Held funds, for scale (dividends kept as cash, so a little under the index's own return):", ""]
    rows = []
    for name in ("vt", "spy"):
        for period, p in ((funds.get(name) or {}).get("periods") or {}).items():
            f = p.get("fund") or {}
            rows.append([FUND_LABELS[name], period, f.get("from", "n/a"), pct(f.get("total_return"), 1),
                         pct(f.get("annualised"), 1), pct(f.get("max_drawdown"), 1, False),
                         pct(f.get("mean_invested"), 0, False)])
    lines += _table(["Fund", "Years", "From", "Total return", "A year", "Worst fall", "Invested (mean)"], rows)
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
    lines += ["", "A and C against the momentum fund (their registered comparator, pre-registration section 13):", ""]
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
    b_from = _get(funds, "vt_timing", "periods", "all years", "vs_vt", "from")
    if b_from:
        start = f"B holds from {b_from}." + (" So B's history starts after the 2008 crash." if b_from > "2009-03"
                                             else "")
    else:
        start = "B has no sessions in this run."
    lines = ["## 3. B: VT or T-bills by the 10-month average", "",
             f"The registered rule on VT. VT has prices from {vt_first}, so B's first decision is the first "
             f"month-end with ten month-end closes. {start} Beside it, B's own code with SPY in place of VT, from "
             f"the first month-end BIL (the T-bills) had prices "
             f"({_get(counters, 'vt_timing_on_spy', 'first_month_end') or 'n/a'}): not the registered rule, a "
             f"check against the owner's quick test on SPY. B puts dividends back to work at each switch; the held "
             f"funds keep them as cash, so over B's days the held VT fund was "
             f"{pct(_get(funds, 'vt_timing', 'periods', 'all years', 'vs_vt', 'compared', 'mean_invested'), 0, False)} "
             f"invested on average, against B's "
             f"{pct(_get(funds, 'vt_timing', 'periods', 'all years', 'vs_vt', 'fund', 'mean_invested'), 0, False)} "
             f"(when B holds VT or BIL). This helps B a little.", ""]
    rows = []
    for name, compared in (("vt_timing", "vs_vt"), ("vt_timing_on_spy", "vs_spy")):
        fund = funds.get(name) or {}
        for period, p in (fund.get("periods") or {}).items():
            m = p.get(compared) or {}
            if not m.get("days"):
                continue
            short = " (under a year)" if m["days"] < YEAR else ""
            rows.append([FUND_LABELS[name], period + short, f"{m.get('from')} to {m.get('to')}",
                         pct(_get(m, "fund", "total_return"), 1) + " vs " + pct(_get(m, "compared", "total_return"), 1),
                         pct(_get(m, "fund", "annualised"), 1) + " vs " + pct(_get(m, "compared", "annualised"), 1),
                         pct(_get(m, "fund", "max_drawdown"), 1, False) + " vs "
                         + pct(_get(m, "compared", "max_drawdown"), 1, False), _test(m, 4)])
    lines += _table(["Fund", "Years", "From - to", "Total: B vs held", "A year: B vs held", "Worst fall: B vs held",
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
              "the same 3 sessions the race trade is scored on, so filled signals must look worse here, and the "
              "t is huge for that reason. This says what C avoids, not what C earns; C's result is its fund "
              "(section 2).", ""]
    rows = []
    for period, p in race.items():
        for label in ("all", "longs", "shorts"):
            b = p.get(label) or {}
            rows.append([period, label, count(_get(b, "filled", "n")), pct(_get(b, "filled", "mean_net"), 2),
                         count(_get(b, "missed", "n")), pct(_get(b, "missed", "mean_net"), 2),
                         pct(b.get("missed_minus_filled"), 2), num(b.get("welch_t"))])
    lines += _table(["Years", "Side", "Filled", "Filled: mean", "Missed", "Missed: mean", "Missed minus filled",
                     "Welch t (reading only)"], rows)
    placed = orders.get("placed") or 0
    if placed:
        bought = (orders.get("filled_open") or 0) + (orders.get("filled_range") or 0)
        refused = orders.get("no_room") or 0
        reached = bought + refused
        lines += ["", f"In the C fund: {count(placed)} orders placed. The price reached the limit on "
                  f"{count(reached)} of them ({pct(reached / placed, 1, False)}): {count(bought)} were bought "
                  f"({count(orders.get('filled_open'))} at the open, {count(orders.get('filled_range'))} during "
                  f"the day) and {count(refused)} were refused because the book was full. "
                  f"{count(orders.get('missed'))} were cancelled after 3 sessions. On "
                  f"{count(orders.get('acted_differently'))} signals C and the momentum fund acted differently "
                  f"(pre-registration section 13.7)."]
    return lines + [""]


def _context(results: dict) -> list[str]:
    arm = _get(results, "race", "arms", "momentum", "periods") or {}
    all_years = arm.get("all years") or {}
    edge = all_years.get("vs_coin_flip_expected") or {}
    band = _get(all_years, "coin_flip_band", "mean/day") or {}
    said = verdict(edge)
    close = said == "no clear difference from a coin flip"
    slices = "; ".join(f"{name}: {verdict(p.get('vs_coin_flip_expected'))} "
                       f"({pct(_get(p, 'vs_coin_flip_expected', 'mean'), 3)} a day, "
                       f"t {num(_get(p, 'vs_coin_flip_expected', 't'))})"
                       for name, p in arm.items() if name != "all years")
    lines = ["## 5. What this means for the live race (context only)", "",
             f"On history, momentum's 3-session trades show **{said}**: minus a coin flip "
             f"{pct(edge.get('mean'), 3)} a day, t {num(edge.get('t'))}, over all years"
             + (f" (percentile {band['percentile']:.0f} in the race's band)" if band.get("percentile") is not None
                else "") + f". By slice: {slices}.", "",
             "The owner's observation, written here as context: *at a 3-day horizon, momentum looks close to random "
             "on history. So in the live race, \"the AI beats momentum\" may mean little more than \"the AI beats "
             "random\".* " + ("This screen agrees." if close else "This screen does not fully agree: see above."),
             ""]
    long_same = _get(band, "others", "always long, same lines") or {}
    since = _get(results, "funds", "funds", "momentum", "periods", "2010 on", "vs_vt") or {}
    if long_same.get("percentile") is not None:
        lines += [
            "The race also has the coin flip as a floor (pre-registration section 5, condition 3), but on history "
            "this floor is weak. Buying every line momentum picked would score "
            f"{pct(long_same.get('value'), 3)} a day, at percentile {long_same['percentile']:.0f} of the coin "
            "flip's band, with no skill at all: prices mostly rise, and a coin flip is short half the time. A "
            "model that is mostly long clears the floor the same way (pre-registration section 11.5 says this of "
            "the fund band). The real protection is the index test: the winner must beat VT. On history, the "
            f"momentum fund trailed the VT fund from 2010 by {pct(since.get('mean'), 4)} a day "
            f"(t {num(since.get('t'))}).", ""]
    lines += ["This screen **changes nothing in the locked test**: the arms, the metric, the looks and the decision "
              "rule stay as registered.", ""]
    return lines


def _data(results: dict) -> list[str]:
    data = results.get("data") or {}
    rows = []
    for c in data.get("coverage") or []:
        rows.append([c["ticker"], c.get("first") or "no prices", count(c.get("bars"))])
    by_year = _get(results, "race", "lines_by_year") or {}
    gaps = data.get("price_gaps") or {}
    cal = data.get("calendar_vs_production") or {}
    closed = cal.get("traded_but_production_says_closed") or []
    open_ = cal.get("no_bar_but_production_says_open") or []
    differs = []
    if open_:
        differs.append("no bar, but production's list says open: " + ", ".join(open_))
    if closed:
        differs.append("a bar, but production's list says closed: " + ", ".join(closed))
    integrity = _get(results, "funds", "integrity") or {}
    lines = ["## 6. Data", "",
             "Lines per year: " + ", ".join(f"{y}: {count(n)}" for y, n in sorted(by_year.items())) + ".", "",
             f"Missing price days (a name trading, no bar): {count(gaps.get('missing'))} of "
             f"{count(gaps.get('ticker_days'))} ticker-days ({pct(gaps.get('share'), 2, False)}).", "",
             "The calendar is the days SPY traded (production's list of holidays covers 2025-2027 only). Since "
             "2025 the two differ " + ("on these days: " + "; ".join(differs) if differs else "on no day") + ".", "",
             f"Fund integrity: {'no problems' if integrity.get('ok') else integrity.get('problems')}; "
             f"{count(integrity.get('data_holes'))} ticker-days with no bar met by the funds.", "",
             "First price of each name:", ""]
    lines += _table(["Name", "First bar", "Bars"], rows)
    return lines + [""]


# --------------------------------------------------------------------------- #
# The stress kind
# --------------------------------------------------------------------------- #

#: The stress kind's funds, in its report's order: momentum, A, B, C, VT, SPY (``history.stress.FUNDS``).
STRESS_FUNDS = ("momentum", "momentum_200", "vt_timing", "momentum_pullback", "vt", "spy")
STRESS_KIND = "stress"
#: The label of a period VT did not exist in (``history.stress.VT_MISSING``).
VT_MISSING = "VT did not exist; against SPY instead"


def _stress_header(results: dict) -> list[str]:
    meta = results.get("meta", {})
    run = meta.get("run") or {}
    where = []
    if run.get("run_id"):
        where.append(f"workflow run {run['run_id']}")
    if run.get("commit"):
        where.append(f"commit `{run['commit'][:12]}`")
    names = list((results.get("periods") or {}).keys())
    listed = (", ".join(names[:-1]) + " and " + names[-1]) if len(names) > 1 else "".join(names)
    return [
        f"# History screen: stress periods ({listed or 'none'})",
        "",
        f"*Written by `python -m history.screen run --kind stress` ({', '.join(where) or 'a local run'}) on "
        f"{meta.get('generated_at', 'n/a')}. Prices through {meta.get('final_through', 'n/a')}. Price table SHA-256 "
        f"`{meta.get('prices_sha256', 'n/a')}`; history journal SHA-256 `{meta.get('journal_sha256', 'n/a')}` "
        f"({count(meta.get('journal_lines'))} lines).*",
        "",
        "**Nothing here changes the locked test, its rules or its decisions.** This is a history screen: it "
        "replays, on past prices, the rules that need no model, with the real code. It did not read the live "
        "race.",
        "",
        "**Descriptive only.** This report shows how deep each fund fell, and how it did against holding VT (or "
        "SPY), in four bad stretches of the market. It has no t and no verdict: four periods, each chosen "
        "because it was bad, cannot show whether a rule is good or bad. The "
        f"{count(meta.get('watchlist_names'))} names are today's watchlist: many did not exist in 2000 (each "
        "period below says how many had prices), and funds and companies that closed before 2026 are missing "
        "(survivorship).",
        "",
    ]


def _stress_method(results: dict) -> list[str]:
    meta = results.get("meta", {})
    periods = results.get("periods") or {}
    spans = "; ".join(f"{name}: {p.get('first', 'n/a')} to {p.get('last', 'n/a')}" for name, p in periods.items())
    missing = meta.get("missing_tickers") or []
    return [
        "## How it was made",
        "",
        f"- **Periods** (fixed in the code, `history/stress.py`): {spans or 'none'}. Each end is a trading day.",
        f"- **A fresh start in each period:** every fund starts with ${meta.get('starting_cash', 100_000):,.0f} on "
        "the period's first session. The indicators warm up on the prices before it: each line's technicals "
        "(momentum's 63-day return and 50-day average) read the two years of final closes before its day, A's "
        "200-day average reads the 200 closes before it, and B decides at the last month-end before the period "
        "from VT's 10 month-end closes up to it. The first trades are at the open of the first session, on the "
        "lines of the session before it (the live funds act on the previous session's lines the same way).",
        "- **Funds:** momentum, A (the 200-day veto) and C (the pullback limit) through the production engine; "
        "B (VT or T-bills by the 10-month average); VT and SPY bought and held. The same code as the full "
        "screen. **No AI arms:** the model has read about these years, so they cannot test it.",
        "- **As in the full screen:** the previous session's final close stands in for the live price; prices "
        "are Yahoo's daily bars adjusted for splits (not for dividends); "
        f"{pct(meta.get('cost_per_side'), 2, False)} per side on every trade; dividends on the ex-date (the held "
        "funds keep them as cash); no taxes."
        + (f" No prices at all for: {', '.join(missing)}." if missing else ""),
        "- **Not possible:** where a fund's prices do not exist, the report says \"not possible\" and why. "
        "Nothing stands in for a missing fund.",
        "- **Words:** *total return* is over the fund's own sessions in the period; *worst fall* is the maximum "
        "drawdown, the deepest fall from the running high within the period (the start counts as a high); "
        "*minus VT* is the fund's total return minus VT's over the same sessions (when VT starts later in the "
        "period, over VT's sessions only), and *minus SPY* the same against SPY; *invested* is the book's gross "
        "exposure as a share of equity.",
        "",
    ]


def _stress_vs(block: Optional[dict], first: Optional[str]) -> str:
    """One comparison as "difference (fund vs compared)", with its first session when it starts later."""
    if not block:
        return "-"
    if not block.get("possible"):
        return f"not possible: {block.get('why') or 'n/a'}"
    text = f"{pct(block.get('difference'), 1)} ({pct(block.get('fund_return'), 1)} vs " \
           f"{pct(block.get('compared_return'), 1)})"
    if block.get("from") and block.get("from") != first:
        text += f", from {block['from']}"
    return text


def _stress_period(name: str, period: dict) -> list[str]:
    names = period.get("names") or {}
    vt = period.get("vt") or {}
    first = period.get("first_session") or period.get("first")
    lines = [f"## {name} ({period.get('first', 'n/a')} to {period.get('last', 'n/a')}, "
             f"{count(period.get('sessions'))} sessions)", "",
             f"Names with prices: {count(names.get('with_prices'))} of the {count(names.get('watchlist'))} "
             f"watchlist names ({count(names.get('from_the_first_session'))} from the first session"
             + ("; the others started during the period)."
                if (names.get("with_prices") or 0) > (names.get("from_the_first_session") or 0) else ").")
             + (f" First trades at the open of {first}, on the lines of {period['first_cycle']}."
                if period.get("first_cycle") else ""), ""]
    spy_header = "Minus SPY (same sessions)"
    if vt.get("in_period") == "none":
        lines += [f"**{VT_MISSING}.** VT's first price is {vt.get('first_price') or 'not in the table'}, so there "
                  "is no VT fund here, and each fund's return is shown against SPY (bought and held from the same "
                  "$100,000).", ""]
        spy_header += f": {VT_MISSING}"
    elif vt.get("in_period") == "part":
        lines += [f"VT only from {vt.get('first_price')} (its first price): *minus VT* is over VT's sessions only, "
                  "from that day; *minus SPY* is over the whole period.", ""]
    rows = []
    funds = period.get("funds") or {}
    for fund in STRESS_FUNDS:
        row = funds.get(fund) or {}
        label = FUND_LABELS.get(fund, fund)
        if not row.get("possible"):
            rows.append([label, f"not possible: {row.get('why') or 'n/a'}", "-", "-", "-", "-", "-", "-", "-"])
            continue
        rows.append([label, row.get("first", "n/a"), row.get("last", "n/a"), count(row.get("sessions")),
                     pct(row.get("total_return"), 1), pct(row.get("max_drawdown"), 1, False),
                     pct(row.get("mean_invested"), 0, False),
                     _stress_vs(row.get("vs_vt"), first) if fund != "vt" else "-",
                     _stress_vs(row.get("vs_spy"), first) if fund != "spy" else "-"])
    lines += _table(["Fund", "From", "To", "Sessions", "Total return", "Worst fall", "Invested (mean)",
                     "Minus VT (same sessions)", spy_header], rows)
    notes = []
    traded = [f"{FUND_LABELS[f]} {count(funds[f]['entries'])}" for f in ("momentum", "momentum_200",
                                                                         "momentum_pullback")
              if (funds.get(f) or {}).get("possible") and funds[f].get("entries") is not None]
    if traded:
        notes.append("Entries: " + ", ".join(traded) + ".")
    b = funds.get("vt_timing") or {}
    if b.get("possible"):
        switches = b.get("switches")
        notes.append(f"{FUND_LABELS['vt_timing']}: first decision {b.get('first_decision', 'n/a')}, "
                     f"{count(switches)} switch{'' if switches == 1 else 'es'} in the period.")
    if notes:
        lines += ["", " ".join(notes)]
    return lines + [""]


def _stress_cutoffs(results: dict) -> list[str]:
    block = results.get("regime_cutoffs") or {}
    lines = ["## VT 21-day realized volatility terciles, from its first 21 returns to 2026-09-30 (the regime "
             "split's cut-offs, pre-registration section 13.10)", ""]
    if not block.get("possible"):
        return lines + [f"Not possible: {block.get('why') or 'no result'}.", ""]
    c1, c2 = block["cutoffs"]
    by = block.get("by_tercile") or {}
    lines += [f"Each session's volatility is the annualised standard deviation (x sqrt(252)) of VT's 21 daily log "
              f"returns ending at that session's own final close (adjusted for splits, not for dividends, as the "
              f"race and the funds read it), from the first session with 21 returns "
              f"({block.get('first_session')}) to {block.get('last_session')}: {count(block.get('sessions'))} "
              "sessions. The cut-offs are the 1/3 and 2/3 quantiles of that series (numpy's default method, "
              "'linear'; `analysis.regimes.tercile_cutoffs`). In the regime split itself, a session's state uses "
              "the volatility up to the previous close.", ""]
    if not block.get("complete"):
        lines += [f"**The prices end before {block.get('window_end')}: these are not the registration's "
                  "cut-offs.**", ""]
    lines += _table(["Tercile", "21-day volatility (a year)", "Sessions"], [
        ["low", f"up to {pct(c1, 2, False)}", count(by.get("low"))],
        ["mid", f"over {pct(c1, 2, False)}, up to {pct(c2, 2, False)}", count(by.get("mid"))],
        ["high", f"over {pct(c2, 2, False)}", count(by.get("high"))],
    ])
    lines += ["", f"At full precision (`results.json`, `regime_cutoffs`): c1 = {c1!r}, c2 = {c2!r}.", ""]
    return lines


def _stress_data(results: dict) -> list[str]:
    data = results.get("data") or {}
    first = data.get("first_prices") or {}
    warm = data.get("warm_up") or {}
    lines = ["## Data", "",
             "First prices: " + ", ".join(f"{t} {d or 'none'}" for t, d in first.items()) + ".", "",
             f"Warm-up: the first period needs prices from {warm.get('needed_from', 'n/a')}; the calendar (SPY) "
             f"starts {warm.get('calendar_first_bar') or 'n/a'}"
             + (" (enough)." if warm.get("enough") else " (**not enough**: the first period's indicators start "
                                                        "late)."), ""]
    for name, period in (results.get("periods") or {}).items():
        integrity = period.get("integrity") or {}
        if not integrity:
            continue
        lines.append(f"- {name}: fund integrity "
                     f"{'no problems' if integrity.get('ok') else integrity.get('problems')}; "
                     f"{count(integrity.get('data_holes'))} ticker-days with no bar met by the funds.")
    return lines + [""]


def render_stress(results: dict) -> str:
    """The stress kind's report, from its ``results.json`` alone."""
    lines: list[str] = []
    lines += _stress_header(results)
    lines += _stress_method(results)
    for name, period in (results.get("periods") or {}).items():
        lines += _stress_period(name, period)
    lines += _stress_cutoffs(results)
    lines += _stress_data(results)
    return "\n".join(lines).rstrip() + "\n"


def render(results: dict) -> str:
    if (results.get("meta") or {}).get("kind") == STRESS_KIND:
        return render_stress(results)
    lines: list[str] = []
    for section in (_header, _method, _race, _funds, _b, _c, _context, _data):
        lines += section(results)
    return "\n".join(lines).rstrip() + "\n"


__all__ = ["STRESS_FUNDS", "VT_MISSING", "band_ratio", "render", "render_stress", "verdict"]
