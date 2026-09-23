"""The book as the record describes it, in one snapshot.

Reconstructed from the audit log and the journal, never fetched: every
number here comes from lines a test can write, and the honest blanks -- no
mark, no equity, a position the manager stopped seeing -- stay blank.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from analysis import book
from config import settings as cfg

DAY = date(2026, 9, 17)


def entry(ticker, entry_price, stop, qty, side="buy", when="2026-09-15 15:50:05,196"):
    return json.dumps({
        "event": "signal_processed", "ts": when, "level": "INFO",
        "signal": {"ticker": ticker},
        "result": {"status": "ACCEPTED", "ticker": ticker, "entry_price": entry_price,
                   "stop_price": stop, "quantity": qty, "side": side, "order_id": f"o-{ticker}"},
    })


def managed(ticker, action, when, price=0.0, gain_r=0.0, remaining=None, new_stop=None):
    return json.dumps({
        "event": "position_managed", "ts": when, "level": "INFO",
        "action": {"ticker": ticker, "action": action, "price": price, "gain_r": gain_r,
                   "remaining_qty": remaining, "new_stop": new_stop, "reason": ""},
    })


def journal_line(ticker, when, bias="NEUTRAL", conviction=0.2, outcome="REJECTED", equity=None,
                 error=None, cost=0.04, screen_cost=0.002, held=False):
    return json.dumps({
        "ticker": ticker, "ts_utc": when, "error": error, "held": held,
        "signal": None if (error or held) else {"ticker": ticker, "bias": bias, "conviction": conviction},
        "outcome": None if (error or held or outcome is None) else {"status": outcome, "reason": "r", "equity": equity},
        "usage": {"cost_usd": cost} if not error and not held and outcome is not None else None,
        "screen": {"usage": {"cost_usd": screen_cost}} if not error and not held else None,
        "context": {"gaps": []},
    })


@pytest.fixture
def logs(tmp_path):
    audit = tmp_path / "execution_audit.log"
    journal = tmp_path / "signal_journal.log"
    audit.write_text("")
    journal.write_text("")
    return audit, journal


def write(path: Path, *lines):
    path.write_text("\n".join(lines) + "\n")


# --- positions -------------------------------------------------------------------


def test_a_position_is_rebuilt_from_its_entry_and_the_passes_after_it(logs):
    audit, journal = logs
    write(audit,
          entry("LLY", 100.0, 96.0, 9),
          managed("LLY", "tranche_taken", "2026-09-16 15:47:00,000", price=104.0, gain_r=1.0, remaining=6, new_stop=100.0),
          managed("LLY", "held", "2026-09-17 15:47:00,000", price=105.0, gain_r=1.25, remaining=6, new_stop=100.0))
    write(journal, journal_line("LLY", "2026-09-17T15:48:00+00:00"))
    [p] = book.build(audit, journal, DAY)["positions"]
    assert p["ticker"] == "LLY" and p["name"] and p["side"] == "buy"
    assert p["quantity"] == 6 and p["stop"] == 100.0 and p["entry_stop"] == 96.0
    assert p["rungs_taken"] == 1 and p["r"] == 4.0
    assert p["mark"] == 105.0 and p["marked_at"] == "2026-09-17T15:47:00" and p["gain_r"] == 1.25
    assert p["unrealised"] == 30.0                     # (105 - 100) * 6
    assert p["risk_to_stop"] == 30.0                   # (105 - 100) * 6
    assert p["market_value"] == 630.0
    assert p["has_stop"] is True and p["last_action"] == "held"


def test_a_short_is_valued_the_other_way_round(logs):
    audit, journal = logs
    write(audit, entry("TLT", 81.11, 82.41, 147, side="sell"),
          managed("TLT", "held", "2026-09-17 15:47:00,000", price=81.34, gain_r=-0.18, remaining=147, new_stop=82.41))
    [p] = book.build(audit, journal, DAY)["positions"]
    assert p["unrealised"] == pytest.approx(-33.81)   # (81.34 - 81.11) * -1 * 147
    assert p["risk_to_stop"] == pytest.approx(157.29)  # (82.41 - 81.34) * 147


def test_a_placeholder_price_is_never_read_as_a_mark(logs):
    """An unmanaged or error pass records price 0.0. That is not a quote."""
    audit, journal = logs
    write(audit, entry("XLY", 110.15, 113.36, 63, side="sell"),
          managed("XLY", "unmanaged", "2026-09-17 15:47:00,000", price=0.0, remaining=63))
    [p] = book.build(audit, journal, DAY)["positions"]
    assert p["mark"] is None and p["unrealised"] is None
    assert p["risk_to_stop"] == pytest.approx((113.36 - 110.15) * 63)  # from the entry, honestly
    assert p["has_stop"] is False


def test_a_position_the_manager_stopped_seeing_is_closed_not_dropped(logs):
    audit, journal = logs
    write(audit,
          entry("XOM", 100.0, 96.0, 7), entry("LLY", 100.0, 96.0, 9),
          managed("XOM", "held", "2026-09-16 15:47:00,000", price=101.0, remaining=7, new_stop=96.0),
          managed("LLY", "held", "2026-09-16 15:47:00,000", price=101.0, remaining=9, new_stop=96.0),
          managed("LLY", "held", "2026-09-17 15:47:00,000", price=102.0, remaining=9, new_stop=96.0))
    snap = book.build(audit, journal, DAY)
    assert [p["ticker"] for p in snap["positions"]] == ["LLY"]
    [closed] = snap["closed"]
    assert closed["ticker"] == "XOM" and closed["last_seen"] == "2026-09-16"
    assert "not seen by the manager since 2026-09-16" in closed["closed_reason"]


def test_a_new_entry_after_a_close_starts_a_fresh_position(logs):
    audit, journal = logs
    write(audit,
          entry("XOM", 100.0, 96.0, 7, when="2026-09-10 15:50:00,000"),
          managed("XOM", "tranche_taken", "2026-09-11 15:47:00,000", price=104.0, remaining=5, new_stop=100.0),
          entry("XOM", 110.0, 105.0, 8, when="2026-09-16 15:50:00,000"),
          managed("XOM", "held", "2026-09-17 15:47:00,000", price=111.0, remaining=8, new_stop=105.0))
    [p] = book.build(audit, journal, DAY)["positions"]
    assert p["entry_price"] == 110.0 and p["rungs_taken"] == 0 and p["quantity"] == 8


# --- equity and the caps -------------------------------------------------------------


def test_equity_is_the_newest_the_journal_recorded_and_fills_the_caps(logs):
    audit, journal = logs
    write(audit, entry("LLY", 100.0, 96.0, 100),
          managed("LLY", "held", "2026-09-17 15:47:00,000", price=100.0, remaining=100, new_stop=96.0))
    write(journal,
          journal_line("AAPL", "2026-09-16T15:48:00+00:00", equity=90_000.0),
          journal_line("LLY", "2026-09-17T15:48:00+00:00", equity=100_000.0),
          journal_line("XOM", "2026-09-17T15:49:00+00:00"))  # NEUTRAL: no equity read
    snap = book.build(audit, journal, DAY)
    assert snap["equity"] == 100_000.0 and snap["equity_at"] == "2026-09-17T15:48:00+00:00"
    whole, funds, names, stocks = snap["exposure"]["caps"]
    assert whole["label"] == "Whole account" and whole["cap"] == 95_000.0 and whole["used"] == 10_000.0
    assert whole["headroom"] == 85_000.0 and whole["share"] == pytest.approx(10.5)
    assert names["used"] == 10_000.0 and names["cap"] == 100_000.0 * cfg.MAX_SINGLE_NAME_SLEEVE_PCT
    assert funds["used"] == 0.0
    # LLY counts at its beta against the stock-market limit, and the label
    # says which way the book leans -- the bar cannot, since the cap is on
    # the size of the net either way.
    assert stocks["label"] == "Stock market (net long, by beta)"
    assert stocks["used"] == pytest.approx(10_000.0 * 0.66)
    assert stocks["cap"] == 100_000.0 * cfg.MAX_EQUITY_RISK_PCT
    [group] = snap["exposure"]["groups"]
    assert group["cap_pct"] == cfg.MAX_EXPOSURE_GROUP_PCT and group["used"] == 10_000.0


def test_a_book_short_the_market_says_short_rather_than_showing_a_bare_size(logs):
    """The cap is on the size of the net, so the bar reads the same either way.

    A short book at 30% of the stock limit and a long book at 30% draw an
    identical bar, and they are opposite bets. The label is the only place
    the side can be shown, so it carries it.
    """
    audit, journal = logs
    write(audit, entry("XBI", 100.0, 104.0, 100, side="sell"),
          managed("XBI", "held", "2026-09-17 15:47:00,000", price=100.0, remaining=100, new_stop=104.0))
    write(journal, journal_line("XBI", "2026-09-17T15:48:00+00:00", equity=100_000.0))
    snap = book.build(audit, journal, DAY)
    stocks = snap["exposure"]["caps"][3]
    assert stocks["label"] == "Stock market (net short, by beta)"
    # Size, not sign: the row shows how big the bet is, as the cap does.
    assert stocks["used"] == pytest.approx(10_000.0 * 1.03)


def test_without_equity_the_caps_say_so_rather_than_guess(logs):
    audit, journal = logs
    write(audit, entry("LLY", 100.0, 96.0, 100))
    snap = book.build(audit, journal, DAY)
    assert snap["equity"] is None
    assert all(c["cap"] is None and c["share"] is None for c in snap["exposure"]["caps"])
    assert snap["exposure"]["gross"] == 10_000.0 and snap["exposure"]["at_risk"] == 400.0


# --- today's cycle -------------------------------------------------------------------


def test_the_funnel_counts_tickers_once_and_reads_the_whole_cost(logs):
    audit, journal = logs
    write(journal,
          journal_line("A", "2026-09-17T15:48:00+00:00", outcome=None, cost=0.0),        # screened out
          journal_line("B", "2026-09-17T15:49:00+00:00"),                                # judged NEUTRAL
          journal_line("C", "2026-09-17T15:50:00+00:00", bias="BULLISH", conviction=0.7, outcome="ACCEPTED"),
          journal_line("D", "2026-09-17T15:51:00+00:00", bias="BEARISH", conviction=0.5, outcome="REJECTED"),
          journal_line("E", "2026-09-17T15:52:00+00:00", error="context: TimeoutError"),
          journal_line("F", "2026-09-17T15:53:00+00:00", held=True),                     # already held
          journal_line("B", "2026-09-17T19:10:00+00:00"),                                # a duplicate cycle
          journal_line("Z", "2026-09-16T15:48:00+00:00"))                                # yesterday
    c = book.build(audit, journal, DAY)["cycle"]
    assert c["tickers"] == 6 and c["lines"] == 7
    assert c["held"] == 1 and c["screened_out"] == 1 and c["judged"] == 3 and c["failed"] == ["E"]
    assert [d["ticker"] for d in c["directional"]] == ["C", "D"]
    assert c["accepted"] == ["C"]
    assert c["cost_usd"] == pytest.approx(0.04 * 4 + 0.002 * 5, abs=0.005)
    assert c["started"] == "2026-09-17T15:48:00+00:00" and c["finished"] == "2026-09-17T19:10:00+00:00"


def test_a_held_position_is_not_counted_as_screened_out(logs):
    """A held ticker and a screened-out one are the same two fields (no
    outcome, no error), so the split lives entirely in `held`. Conflating
    them read as a live screen right up until the screen was turned off on
    23 Sep 2026: with it off, every no-outcome/no-error line is a held
    position, and a dashboard that still called the whole bucket "screened
    out" was reporting a stage that no longer runs."""
    audit, journal = logs
    write(journal,
          journal_line("A", "2026-09-23T15:48:00+00:00", held=True),
          journal_line("B", "2026-09-23T15:49:00+00:00", held=True),
          journal_line("C", "2026-09-23T15:50:00+00:00", bias="BULLISH", conviction=0.6, outcome="ACCEPTED"))
    c = book.build(audit, journal, date(2026, 9, 23))["cycle"]
    assert c["held"] == 2
    assert c["screened_out"] == 0
    assert c["judged"] == 1


def test_the_alarms_ride_along(logs):
    audit, journal = logs
    write(audit, entry("XLY", 110.0, 113.0, 63, side="sell"),
          managed("XLY", "unmanaged", "2026-09-17 15:47:00,000", remaining=63))
    write(journal, journal_line("XLY", "2026-09-17T15:48:00+00:00"))
    snap = book.build(audit, journal, DAY)
    assert snap["alarms"][0]["severity"] == "critical"
    assert "without a working stop" in snap["alarms"][0]["title"]
    assert snap["ladder"][0]["take_at_r"] == cfg.PROFIT_LADDER[0].take_at_r


# --- the CLI and the rules -----------------------------------------------------------


def test_the_cli_writes_json_the_page_can_read(logs, capsys):
    audit, journal = logs
    write(audit, entry("LLY", 100.0, 96.0, 9))
    assert book.main(["--audit", str(audit), "--journal", str(journal), "--day", "2026-09-17", "--json"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["day"] == "2026-09-17" and out["positions"][0]["ticker"] == "LLY"
    assert out["generated_at"].endswith("+00:00")


def test_the_table_reads_for_a_person(logs, capsys):
    audit, journal = logs
    write(audit, entry("LLY", 100.0, 96.0, 9))
    book.main(["--audit", str(audit), "--journal", str(journal), "--day", "2026-09-17"])
    text = capsys.readouterr().out
    assert "Equity not yet recorded" in text and "LLY" in text


def test_missing_logs_are_an_empty_book_not_a_crash(tmp_path):
    snap = book.build(tmp_path / "no.log", tmp_path / "no2.log", DAY)
    assert snap["positions"] == [] and snap["exposure"]["gross"] == 0.0


def test_the_book_never_reaches_a_broker_or_a_model():
    source = Path(book.__file__).read_text()
    for banned in ("broker_client", "alpaca", "anthropic", "httpx", "yfinance", "submit_", "ExecutionEngine"):
        assert banned not in source, banned


def test_the_workflow_writes_and_commits_the_snapshot():
    import yaml

    wf = yaml.safe_load((Path(__file__).resolve().parents[1] / ".github/workflows/heartbeat.yml").read_text())
    steps = {s.get("name"): s for s in wf["jobs"]["cycle"]["steps"]}
    step = steps["Write the book snapshot"]
    assert step["if"] == "always() && steps.guard.outputs.ran != 'yes' && inputs.mode != 'protect'"
    assert "python -m analysis.book --json" in step["run"]
    assert "python -m analysis.brief" in step["run"]
    assert "logs/book.json" in steps["Commit the journal"]["run"]
    assert "logs/brief.txt" in steps["Commit the journal"]["run"]
    # The desk is published by the heartbeat itself, right after the commit:
    # a push with the job's token starts no other workflow.
    names = list(steps)
    publish = steps["Publish the desk"]
    assert names.index("Publish the desk") == names.index("Commit the journal") + 1
    assert publish["if"] == step["if"]
    assert "bash dashboard/publish.sh" in publish["run"] and "::warning::" in publish["run"]
    assert publish["env"]["GH_TOKEN"] == "${{ github.token }}"


def test_the_duration_group_row_carries_hyg_and_embs_rate_charge_too(logs):
    """The dashboard must show the same Duration total the risk engine enforces.

    HYG and EMB are grouped with Credit, but each also owes Duration a
    fraction of its market value for the interest-rate risk neither Credit
    nor the stock-market limit measures.
    """
    audit, journal = logs
    write(audit, entry("EMB", 100.0, 104.0, 100, side="sell"),
          managed("EMB", "held", "2026-09-17 15:47:00,000", price=100.0, remaining=100, new_stop=104.0))
    write(journal, journal_line("EMB", "2026-09-17T15:48:00+00:00", equity=100_000.0))
    snap = book.build(audit, journal, DAY)
    by_label = {g["label"]: g for g in snap["exposure"]["groups"]}
    # EMB is charged in full to its own group (Credit) and, on top of that,
    # a duration-equivalent slice (weight 0.65) against Duration -- a second
    # charge, not a move.
    assert by_label["Credit"]["used"] == pytest.approx(10_000.0)
    assert by_label["Duration"]["used"] == pytest.approx(6_500.0)
