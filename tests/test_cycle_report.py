"""The cycle report: every score shown next to the evidence behind it."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import pytest

from analysis import cycle_report as cr


def _line(ticker="AAPL", when="2026-09-15T15:06:00+00:00", **kw):
    entry = {
        "ticker": ticker,
        "ts_utc": when,
        "context": {
            "ticker": ticker,
            "headlines": ["Apple beats on earnings — Revenue up 8% (Reuters, 2 hours ago)"],
            "sources": [{
                "title": "Apple beats on earnings", "snippet": "Revenue up 8%",
                "source": "Reuters", "when": "2 hours ago", "url": "https://example.com/a",
            }],
            "technicals": {"rsi14": 61.2, "last_close": 195.3},
            "fundamentals": {"trailing_pe": 34.2},
            "analysts": {"recommendation": "buy"},
            "insiders": {"buys": [], "sells": []},
            "gaps": [],
        },
        "signal": {
            "ticker": ticker, "bias": "BULLISH", "conviction": 0.72,
            "rationale": "Guidance raise corroborated by an uptrend.",
            "news_score": 0.8, "technical_score": 0.5,
            "fundamental_score": 0.1, "analyst_score": 0.6, "insider_score": 0.0,
            "key_factors": ["Guidance raised 8%"],
        },
        "outcome": {"status": "ACCEPTED", "reason": "ok", "quantity": 50},
        "error": None,
    }
    entry.update(kw)
    return cr.Line(entry)


def test_a_headline_is_rendered_as_a_link():
    text = "\n".join(cr.render_ticker(_line()))
    assert "[Apple beats on earnings](https://example.com/a)" in text
    assert "Reuters, 2 hours ago" in text


def test_each_score_sits_next_to_its_own_evidence():
    """The reason this report exists: a score out of reach of its inputs is an assertion."""
    text = "\n".join(cr.render_ticker(_line()))
    news_at = text.index("News</b> — score +0.80")
    tech_at = text.index("Price and chart</b> — score +0.50")
    assert news_at < text.index("Apple beats on earnings") < tech_at
    assert "rsi14" in text[tech_at:]


def test_a_journal_without_urls_still_renders_and_says_so():
    """Lines written before URLs were captured must not render as empty."""
    line = _line()
    line.raw["context"]["sources"] = []
    text = "\n".join(cr.render_ticker(line))
    assert "did not save the links" in text
    assert "Apple beats on earnings" in text


def test_a_failed_ticker_names_its_failure():
    line = _line(signal=None, outcome=None, error="Bright Data HTTP 401")
    text = "\n".join(cr.render_ticker(line))
    assert "Bright Data HTTP 401" in text


def test_a_screened_ticker_says_the_full_model_was_not_asked():
    line = _line(
        signal={"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.2},
        outcome=None,
        screen={"model": "claude-haiku-4-5", "bias": "NEUTRAL"},
    )
    text = "\n".join(cr.render_ticker(line))
    assert "Stopped early" in text
    assert "never asked" in text


def test_the_latest_cycle_excludes_yesterday():
    now = datetime(2026, 9, 15, 15, 6, tzinfo=timezone.utc)
    lines = [
        _line("OLD", when=(now - timedelta(days=1)).isoformat()),
        _line("NEW", when=now.isoformat()),
        _line("ALSO", when=(now - timedelta(minutes=3)).isoformat()),
    ]
    picked = {l.ticker for l in cr.latest_cycle(lines)}
    assert picked == {"NEW", "ALSO"}


def test_the_report_leads_with_the_strongest_conviction():
    quiet = _line("QUIET")
    quiet.raw["signal"]["conviction"] = 0.10
    loud = _line("LOUD")
    loud.raw["signal"]["conviction"] = 0.90
    text = cr.render([quiet, loud])
    assert text.index("### LOUD") < text.index("### QUIET")


def test_a_truncated_line_is_skipped_not_fatal(tmp_path):
    path = tmp_path / "journal.log"
    path.write_text(
        json.dumps(_line().raw) + "\n{ truncated\n" + json.dumps(_line("MSFT").raw) + "\n"
    )
    assert [l.ticker for l in cr.read_lines(path)] == ["AAPL", "MSFT"]


def test_a_missing_journal_is_empty_not_an_exception(tmp_path):
    assert cr.read_lines(tmp_path / "nope.log") == []


def test_the_header_counts_what_happened():
    text = cr.render([_line("AAPL"), _line("MSFT", outcome=None, error="down")])
    assert "2 names checked" in text and "1 traded" in text and "1 with a problem" in text


def test_the_report_never_places_an_order():
    """Read-only by construction: it must not import the broker or the engine."""
    src = (cr.__file__ and open(cr.__file__).read()) or ""
    assert "broker_client" not in src
    assert "execution_engine" not in src
    assert "submit" not in src


def test_a_price_keeps_its_cents():
    """A report that rounds 184.55 to 184.6 is not the number the model saw."""
    line = _line()
    line.raw["context"]["technicals"] = {"last_close": 184.55, "shares": 37000000.0}
    text = "\n".join(cr.render_ticker(line))
    assert "184.55" in text
    assert "37,000,000" in text


# --------------------------------------------------------------------------- #
# The prose the model read, rebuilt from what the journal stored
# --------------------------------------------------------------------------- #


def test_a_stored_section_renders_as_the_lines_the_model_read():
    """The report shows "50d above 200d", not a table of sma50 and sma200."""
    from orchestrator import technicals

    snap = technicals.TechnicalSnapshot(
        last_close=184.55, as_of="2026-09-14", bars=250, sma20=179.1, sma50=171.4, sma200=163.7,
        macd=2.14, macd_signal=1.82, macd_histogram=0.32,
        distance_sma20=0.03, distance_sma50=0.077, distance_sma200=0.128,
        rsi14=61.2, return_1d=0.008, return_5d=0.021, return_21d=0.064, return_63d=0.11,
        low_52w=121.3, high_52w=190.2, position_in_52w_range=0.92,
        atr14=4.26, atr_pct_of_price=0.023, annualised_volatility=0.31, relative_volume=1.4,
    )
    line = _line()
    line.raw["context"]["technicals"] = snap.as_dict()
    text = "\n".join(cr.render_ticker(line))
    for expected in snap.as_lines():
        assert expected in text
    assert "| `rsi14` |" not in text


def test_insider_trades_are_rebuilt_from_their_stored_dicts():
    from orchestrator import insiders

    snap = insiders.build_snapshot()
    trade = insiders.InsiderTrade(when="2026-08-20", who="J. Smith", role="CFO", shares=50_000.0, value=8.6e6)
    stored = snap.as_dict()
    stored.update({"buys": [trade.__dict__], "distinct_buyers": 1, "shares_purchased": 50_000.0})
    line = _line()
    line.raw["context"]["insiders"] = stored
    text = "\n".join(cr.render_ticker(line))
    assert "J. Smith (CFO): 50,000 shares" in text
    assert "insiders spending their own money" in text


def test_an_unknown_journal_key_is_dropped_not_fatal():
    """A line from a newer schema must still render."""
    from orchestrator import fundamentals

    stored = fundamentals.build_snapshot({"sector": "Technology", "marketCap": 4.5e12}).as_dict()
    stored["field_added_next_year"] = 1
    lines = cr.prompt_lines("fundamentals", stored)
    assert lines is not None
    assert any("Technology" in l for l in lines)


def test_a_dict_that_cannot_be_rebuilt_falls_back_to_the_table():
    """Hiding evidence the report cannot format would be worse than a table."""
    line = _line()
    line.raw["context"]["technicals"] = {"bars": "not-a-number", "rsi14": 61.2}
    text = "\n".join(cr.render_ticker(line))
    assert "| `rsi14` | 61.2 |" in text


def test_an_unknown_section_uses_the_table():
    assert cr.prompt_lines("weather", {"temp": 1}) is None


def test_a_link_journalled_before_the_fix_still_opens():
    """Cycles stored before absolute_url existed carry bare `/goto?url=...`."""
    line = _line()
    line.raw["context"]["sources"] = [{
        "title": "Old story", "snippet": "", "source": "Reuters",
        "when": "2h ago", "url": "/goto?url=CAESkQEB",
    }]
    text = "\n".join(cr.render_ticker(line))
    assert "[Old story](https://www.google.com/goto?url=CAESkQEB)" in text


# --------------------------------------------------------------------------- #
# Every name says what it is: a real name, and a sleeve tag
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "ticker,name,sleeve",
    [
        ("LLY", "Eli Lilly", "Company"),
        ("TLT", "US government bonds, 20+ years", "Index fund"),
        ("XLE", "US energy companies", "Sector or country"),
        ("EWZ", "Brazil", "Sector or country"),
        ("GLD", "Gold", "Commodity"),
    ],
)
def test_a_heading_carries_the_real_name_and_the_sleeve(ticker, name, sleeve):
    """"NVO" asks the reader to hold 35 symbols in their head. "Novo Nordisk" does not."""
    head = cr.heading(_line(ticker))
    assert name in head
    assert f"({ticker})" in head
    assert sleeve in head


def test_a_ticker_with_no_name_falls_back_to_its_symbol():
    """A ticker added to the watchlist before anyone wrote its name down still renders."""
    head = cr.heading(_line("ZZZZ"))
    assert "ZZZZ" in head
    # Unrecognised resolves to EQUITY, the smallest cap -- so "Company" here
    # is the same fail-closed default the sizing code uses.
    assert "Company" in head


def test_the_sleeve_tag_is_on_the_heading_even_though_the_list_is_grouped():
    """A heading linked or copied on its own has to stand up by itself."""
    text = cr.render([_line("GLD")])
    assert "## Commodities" in text
    assert "· Commodity —" in text


def test_the_report_groups_by_what_the_thing_is():
    text = cr.render([_line("GLD"), _line("LLY"), _line("TLT"), _line("XLE")])
    order = [
        text.index("## Companies"),
        text.index("## Whole-market funds"),
        text.index("## Sector and country funds"),
        text.index("## Commodities"),
    ]
    assert order == sorted(order)
    # ...and each name sits under its own group.
    assert text.index("Eli Lilly") < text.index("## Whole-market funds")
    assert text.index("US energy companies (XLE)") > text.index("## Sector and country funds")
    assert text.index("Gold (GLD)") > text.index("## Commodities")


def test_conviction_still_orders_within_a_group():
    loud, quiet = _line("LLY"), _line("TEVA")
    loud.raw["signal"]["conviction"] = 0.90
    quiet.raw["signal"]["conviction"] = 0.10
    text = cr.render([quiet, loud])
    assert text.index("Eli Lilly") < text.index("Teva")


def test_an_empty_sleeve_gets_no_heading():
    text = cr.render([_line("LLY")])
    assert "## Companies" in text
    assert "## Commodities" not in text


def test_the_summary_says_what_each_group_did():
    """"Did we even look at the commodities today" has to be answerable at a glance."""
    quiet = _line("SLV")
    quiet.raw["signal"]["bias"] = "NEUTRAL"
    broken = _line("USO", signal=None, outcome=None, error="down")
    text = cr.render([_line("GLD"), quiet, broken])
    assert "| Commodities | 3 | 1 | 1 | 1 |" in text


def test_a_neutral_call_is_not_counted_as_taking_a_side():
    line = _line("LLY")
    line.raw["signal"]["bias"] = "NEUTRAL"
    assert not line.took_a_side
    assert _line("LLY").took_a_side


# --------------------------------------------------------------------------- #
# Plain English
# --------------------------------------------------------------------------- #


def test_the_report_explains_the_floor_and_the_three_sides():
    """The reader is not a developer. The rules have to be in the report itself."""
    text = cr.render([_line("LLY")])
    assert "0.60" in text
    for side in ("BULLISH", "BEARISH", "NEUTRAL"):
        assert side in text


def test_the_word_list_covers_the_terms_with_no_simpler_synonym():
    text = cr.render([_line("LLY")])
    for term in ("RSI", "MACD", "P/E", "Stop-loss"):
        assert f"**{term}**" in text


def test_the_models_own_words_are_quoted_not_rewritten():
    """The rationale is evidence. A paraphrase of it is not."""
    line = _line()
    line.raw["signal"]["rationale"] = "A rich multiple tempers an otherwise clean catalyst."
    text = "\n".join(cr.render_ticker(line))
    assert "> A rich multiple tempers an otherwise clean catalyst." in text


def test_the_stamp_leads_with_israel_time():
    """The person reading this is in Israel; UTC stays beside it, not instead of it."""
    text = cr.render([_line("LLY", when="2026-09-15T14:07:00+00:00")])
    assert "17:07 Israel time" in text
    assert "(14:07 UTC)" in text


# --------------------------------------------------------------------------- #
# The cycle window has to outlast a cycle
# --------------------------------------------------------------------------- #


def test_the_window_outlasts_the_longest_possible_cycle():
    """A window shorter than a run truncates the report and says nothing.

    Regression: at 20 minutes, the first 80-ticker cycle (27.7 minutes) was
    rendered from its last 20 minutes only. Every single name was missing and
    the report looked complete, because the watchlist is walked in sleeve
    order and the companies go first.

    The job's own timeout is the upper bound on how long a cycle can run, so
    that is what the window is checked against -- not against a duration
    someone observed once.
    """
    import re
    from pathlib import Path

    workflow = Path(__file__).resolve().parent.parent / ".github/workflows/heartbeat.yml"
    timeout = int(re.search(r"^\s*timeout-minutes:\s*(\d+)", workflow.read_text(), re.M).group(1))
    assert cr.CYCLE_WINDOW_MINUTES > timeout


def test_the_window_is_shorter_than_the_gap_between_cycles():
    """Too wide and two days of signals render as one cycle."""
    from config import settings as cfg

    assert cr.CYCLE_WINDOW_MINUTES < cfg.HEARTBEAT_INTERVAL_MINUTES


def test_a_cycle_longer_than_the_old_window_stays_whole():
    now = datetime(2026, 9, 15, 19, 10, tzinfo=timezone.utc)
    lines = [
        _line("LLY", when=(now - timedelta(minutes=28)).isoformat()),   # first out
        _line("XLE", when=(now - timedelta(minutes=14)).isoformat()),
        _line("CANE", when=now.isoformat()),                            # last out
        _line("OLD", when=(now - timedelta(days=1)).isoformat()),       # yesterday
    ]
    picked = {l.ticker for l in cr.latest_cycle(lines)}
    assert picked == {"LLY", "XLE", "CANE"}


# --------------------------------------------------------------------------- #
# The open book, from the audit log
# --------------------------------------------------------------------------- #


def _audit_line(day, **action):
    return json.dumps({"ts": f"{day} 18:42:00,000", "level": "INFO",
                       "event": "position_managed", "action": action})


def test_the_positions_section_reads_the_audit_log_for_the_cycles_day(tmp_path):
    audit = tmp_path / "audit.log"
    audit.write_text("\n".join([
        _audit_line("2026-09-15", ticker="LLY", action="tranche_taken", gain_r=1.02, qty_closed=1,
                    remaining_qty=3, old_stop=1079.13, new_stop=1142.29),
        _audit_line("2026-09-15", ticker="GLD", action="held", gain_r=0.31, remaining_qty=12, old_stop=310.5, new_stop=310.5),
        _audit_line("2026-09-14", ticker="XOM", action="tranche_taken", gain_r=1.0, qty_closed=5, remaining_qty=10),
        json.dumps({"event": "signal_processed", "ts": "2026-09-15 18:50:00,000", "result": {}}),
        "{ not json",
    ]))
    actions = cr.read_position_actions(audit, "2026-09-15")
    assert [a["ticker"] for a in actions] == ["LLY", "GLD"]   # yesterday's XOM is not today's


def test_the_positions_section_is_plain_english_with_names_and_kinds(tmp_path):
    actions = [
        {"ticker": "LLY", "action": "tranche_taken", "gain_r": 1.02, "qty_closed": 1,
         "remaining_qty": 3, "old_stop": 1079.13, "new_stop": 1142.29},
        {"ticker": "GLD", "action": "held", "gain_r": 0.31, "remaining_qty": 12, "old_stop": 310.5, "new_stop": 310.5},
        {"ticker": "TLT", "action": "unmanaged", "reason": "no live stop order; left untouched"},
    ]
    text = cr.render([_line("LLY")], actions)
    assert "## Open positions" in text
    assert "| Eli Lilly (LLY) · Company | **Sold part.** Sold 1 of 4 shares at +1.02R, 3 still held. Stop-loss raised 1079.13 → 1142.29. |" in text
    assert "| Gold (GLD) · Commodity | **Holding.** +0.31R, holding 12 shares. Stop-loss 310.50. |" in text
    assert "**Left alone.** No stop-loss order found" in text
    # Sold and flagged rows come before the merely-held ones.
    assert text.index("Eli Lilly (LLY)") < text.index("Gold (GLD)")
    assert text.index("(TLT)") < text.index("Gold (GLD)")


def test_no_management_records_means_no_section_not_an_empty_one():
    text = cr.render([_line("LLY")], [])
    assert "## Open positions" not in text
    text = cr.render([_line("LLY")])
    assert "## Open positions" not in text


def test_the_word_list_explains_r():
    text = cr.render([_line("LLY")])
    assert "**R**" in text and "+1R" in text


def test_the_opening_states_the_new_floor_and_the_ladder():
    text = cr.render([_line("LLY")])
    assert "reaches **0.30**" in text
    assert "a third of it is sold" in text
    assert "The stop only ever moves up" in text
