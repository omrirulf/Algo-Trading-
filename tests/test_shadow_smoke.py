"""The smoke check: the fund machinery on a real-shaped journal, reporting health and never a result."""

from __future__ import annotations

from datetime import date, datetime, timezone

import pandas as pd

from analysis.reader import JournalEntry
from shadow import smoke

#: What a health row may say. Anything else -- an equity, a return, a win
#: rate -- would be a fund result shown before the fund test starts.
ALLOWED = {"name", "sessions", "accepted", "refused", "fills", "open", "problems", "held"}


class Flat:
    def ohlc(self, ticker, start, end):
        days = pd.bdate_range("2026-05-01", "2026-10-09")
        return pd.DataFrame({"Open": 100.0, "High": 101.0, "Low": 99.0, "Close": 100.0, "Volume": 1e6,
                             "Dividends": 0.0}, index=days)


def entry(day: int, ticker: str, bias: str = "BULLISH") -> JournalEntry:
    return JournalEntry(ticker=ticker, timestamp=datetime(2026, 10, day, 16, 10, tzinfo=timezone.utc),
                        timestamp_is_exact=True, bias=bias, conviction=0.8)


def test_the_smoke_run_reports_health_and_nothing_else(capsys):
    entries = [entry(1, "NVDA"), entry(1, "XOM", "BEARISH"), entry(2, "MSFT"), entry(5, "LQD", "BEARISH")]

    report = smoke.smoke(entries, 5, 3, Flat(), date(2026, 10, 7), frozenset({"LQD"}))

    assert [r["name"] for r in report] == ["model", "momentum", "hybrid", "vt", "coin-0", "coin-1", "coin-2"]
    for row in report:
        assert set(row) <= ALLOWED, row
    model = report[0]
    assert model["sessions"] == 5 and model["problems"] == []
    assert model["accepted"] == 3 and model["refused"] == 1        # LQD: the paper account cannot short it
    assert model["fills"] == {"entry": 3} and model["open"] == 3
    assert "cycles acted on: 3" in capsys.readouterr().out


def test_a_problem_turns_the_run_red(monkeypatch, tmp_path, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text("", encoding="utf-8")
    rows = [{"name": "model", "sessions": 5, "accepted": 1, "refused": 0, "fills": {}, "open": 1,
             "problems": ["model: NVDA stops cover 0 of 10"]}]
    monkeypatch.setattr(smoke, "smoke", lambda *a, **k: [dict(r) for r in rows])
    assert smoke.main(["--journal", str(journal), "--audit", str(tmp_path / "none.log")]) == 1
    assert "PROBLEM model: NVDA stops cover 0 of 10" in capsys.readouterr().out

    rows[0]["problems"] = []
    assert smoke.main(["--journal", str(journal), "--audit", str(tmp_path / "none.log")]) == 0
    assert "OK: the machinery held" in capsys.readouterr().out
