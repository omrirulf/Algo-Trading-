"""The prices a night's scoring used: handed over, hashed, archived -- and no number moved.

``--with-prices`` on the race and the funds adds one field, ``prices_sha256``,
and prints the price table as one last line. The owner's condition
(26 Sep 2026): NO number in any race or fund output may change. So each
output is produced twice from the same inputs, with and without the flag,
and compared byte for byte apart from the new field. Then the table itself:
it hashes to its field, it survives the archive's dedup and can be rebuilt
from it, and a table that does not check is refused whole.
"""

from __future__ import annotations

import json
import random
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import httpx
import numpy as np
import pandas as pd
import pytest
import yaml

from analysis import decision_gate, horse_race, price_tape
from analysis.baseline_compare import OhlcFetcher
from analysis.returns import YFinancePriceSource
from store import push_remote, scoring_prices
from store.remote import RemoteArchive

ROOT = Path(__file__).resolve().parent.parent
TICKERS = ("NVDA", "XOM", "TLT", "GLD", "JPM", "SPY", "VT")


def _frames(seed: int = 7) -> dict[str, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    days = pd.bdate_range("2026-03-02", "2026-09-18")
    frames = {}
    for ticker in TICKERS:
        close = 100 * np.exp(np.cumsum(rng.normal(0.0008, 0.02, len(days))))
        opened = close * np.exp(rng.normal(0, 0.006, len(days)))
        high = np.maximum(opened, close) * (1 + np.abs(rng.normal(0, 0.01, len(days))))
        low = np.minimum(opened, close) * (1 - np.abs(rng.normal(0, 0.01, len(days))))
        dividends = np.where(np.arange(len(days)) % 63 == 5, 0.25, 0.0)
        frames[ticker] = pd.DataFrame({"Open": opened, "High": high, "Low": low, "Close": close,
                                       "Adj Close": close * 0.99, "Volume": 1e6, "Dividends": dividends},
                                      index=days)
    return frames


@pytest.fixture
def vendor(monkeypatch):
    """yfinance, replaced at the one call each real price source makes -- so the
    real caching, finality cut and ``recorded`` all run."""
    frames = _frames()

    def closes(self, ticker, start, end):
        df = frames.get(ticker)
        return [] if df is None else [(ts.date(), float(c)) for ts, c in df["Close"].items()]

    def ohlc(self, ticker, start, end):
        return frames.get(ticker, pd.DataFrame())

    monkeypatch.setattr(YFinancePriceSource, "_fetch", closes)
    monkeypatch.setattr(OhlcFetcher, "_fetch", ohlc)
    return frames


def _journal(path: Path) -> Path:
    pick = random.Random(3)
    lines = []
    for day in pd.bdate_range("2026-07-20", "2026-09-10"):
        for i, ticker in enumerate(TICKERS[:5]):
            stamp = datetime(day.year, day.month, day.day, 15, 10, tzinfo=timezone.utc) + timedelta(seconds=i)
            q = pick.uniform(-0.3, 0.3)
            lines.append({
                "ts_utc": stamp.isoformat(), "ticker": ticker,
                "context": {"technicals": {"last_close": 100.0, "return_63d": q,
                                           "distance_sma50": q / 3 + pick.uniform(-0.03, 0.03),
                                           "annualised_volatility": 0.3, "atr_pct_of_price": 0.02}},
                "signal": {"ticker": ticker, "bias": pick.choice(["BULLISH", "BEARISH", "NEUTRAL"]),
                           "conviction": round(pick.uniform(0.2, 0.9), 2), "rationale": "r"},
            })
    path.write_text("".join(json.dumps(line) + "\n" for line in lines), encoding="utf-8")
    return path


NOW = datetime(2026, 9, 19, 23, 0, tzinfo=timezone.utc)


def _race(tmp_path, monkeypatch, capsys, *extra) -> list[str]:
    journal = _journal(tmp_path / "journal.log")
    monkeypatch.setattr(decision_gate, "DECISION_CUTOFF", date(2000, 1, 1))
    monkeypatch.setattr(decision_gate, "FAILURE_WATCH_START", date(2000, 1, 1))
    monkeypatch.setattr(horse_race, "_now", lambda: NOW)
    code = horse_race.main(["--journal", str(journal), "--seeds", "30", "--account",
                            str(tmp_path / "no-account.jsonl"), *extra])
    assert code == 0
    return capsys.readouterr().out.splitlines()


# --------------------------------------------------------------------------- #
# No number moves
# --------------------------------------------------------------------------- #


def test_the_race_gate_is_byte_for_byte_the_same_apart_from_the_new_field(vendor, tmp_path, monkeypatch, capsys):
    (plain,) = _race(tmp_path, monkeypatch, capsys, "--gate-json")
    gate, table = _race(tmp_path, monkeypatch, capsys, "--gate-json", "--with-prices")
    tape = json.loads(table)
    digest = tape["prices_sha256"]
    # The same bytes, with one key appended at the end.
    assert gate == plain[:-1] + f', "prices_sha256": "{digest}"}}'
    assert list(json.loads(gate)) == [*json.loads(plain), "prices_sha256"]
    scored = json.loads(plain)
    assert scored["independent"] > 0                                    # the race did score something
    assert sum(g["n"] for g in scored["conviction_groups"]["model"]) > 0
    # The table is what the race read, and hashes to the field.
    assert price_tape.digest(tape["rows"]) == digest and tape["consumer"] == "race-gate"
    assert set(tape["coverage"]) == {"closes", "ohlc", "basket"}
    assert {"SPY", "VT"} <= {r["ticker"] for r in tape["rows"] if r["instance"] == "basket"}
    nvda = [r for r in tape["rows"] if r["instance"] == "ohlc" and r["ticker"] == "NVDA"]
    first = vendor["NVDA"].loc[pd.Timestamp(nvda[0]["date"])]
    assert (nvda[0]["open"], nvda[0]["close"], nvda[0]["dividends"]) == (
        float(first["Open"]), float(first["Close"]), float(first["Dividends"]))


def test_the_race_report_is_line_for_line_the_same_apart_from_the_new_lines(vendor, tmp_path, monkeypatch, capsys):
    plain = _race(tmp_path, monkeypatch, capsys, "--per-trade")
    with_prices = _race(tmp_path, monkeypatch, capsys, "--per-trade", "--with-prices")
    tape = json.loads(with_prices[-1])
    assert with_prices[:-2] == plain
    assert with_prices[-2] == f"prices_sha256: {tape['prices_sha256']}"
    assert set(tape["coverage"]) == {"closes", "ohlc", "basket", "closes_long", "ohlc_long"}
    assert tape["consumer"] == "race-report"


def _funds_inputs(tmp_path, monkeypatch):
    from shadow import calibration as calib
    from shadow import run as shadow_run
    from shadow import schedule
    from shadow.market import Bars

    monkeypatch.setattr(schedule, "CALIBRATION_START", date(2026, 8, 3))
    monkeypatch.setattr(schedule, "FUND_START", date(2026, 8, 17))

    def passed(**kw):
        # The calibration's own fetch, through the run's fetcher, as the real one makes it.
        Bars.fetch({"VT", "SPY", "NVDA"}, kw["start"], kw["final_through"], kw["fetcher"])
        return {"status": "passed"}

    monkeypatch.setattr(calib, "calibration_report", passed)
    monkeypatch.setattr(shadow_run, "_now", lambda: NOW)
    journal = _journal(tmp_path / "journal.log")
    return shadow_run, ["--journal", str(journal), "--audit", str(tmp_path / "audit.log"),
                        "--account", str(tmp_path / "account.jsonl"), "--random", "2"]


def test_the_funds_are_byte_for_byte_the_same_apart_from_the_new_field(vendor, tmp_path, monkeypatch, capsys):
    shadow_run, args = _funds_inputs(tmp_path, monkeypatch)
    assert shadow_run.main(args) == 0
    (plain,) = capsys.readouterr().out.splitlines()
    assert shadow_run.main([*args, "--with-prices"]) == 0
    funds, table = capsys.readouterr().out.splitlines()
    tape = json.loads(table)
    assert funds == plain[:-1] + f',"prices_sha256":"{tape["prices_sha256"]}"}}'
    record = json.loads(plain)
    assert record["funds"] and sum(f["trades"] for f in record["funds"]["list"]) > 0   # the funds traded
    assert price_tape.digest(tape["rows"]) == tape["prices_sha256"] and tape["consumer"] == "funds"
    assert set(tape["coverage"]) == {"ohlc"} and "VT" in tape["coverage"]["ohlc"]["tickers"]


def test_a_source_the_tape_cannot_read_adds_nothing_and_breaks_nothing():
    rows, coverage = price_tape.rows_and_coverage([("fake", object())])
    assert rows == [] and coverage == {}
    assert price_tape.digest([]) == price_tape.digest([])


# --------------------------------------------------------------------------- #
# The archive's side: checked, deduplicated, rebuildable
# --------------------------------------------------------------------------- #


def _tape(vendor, consumer="race-gate") -> dict:
    closes, fetcher = YFinancePriceSource(date(2026, 9, 18)), OhlcFetcher(date(2026, 9, 18))
    for ticker in ("NVDA", "SPY"):
        closes.closes(ticker, date(2026, 6, 1), date(2026, 9, 18))
        fetcher.ohlc(ticker, date(2026, 6, 1), date(2026, 9, 18))
    basket = YFinancePriceSource(date(2026, 9, 18))
    basket.closes("SPY", date(2026, 3, 1), date(2026, 9, 18))
    return price_tape.tape((("closes", closes), ("ohlc", fetcher), ("basket", basket)),
                           consumer=consumer, final_through=date(2026, 9, 18), generated_at=NOW)


def test_a_night_is_rebuilt_from_the_archive_and_matches_its_hash(vendor):
    tape = scoring_prices.load(price_tape.dumps(_tape(vendor)))
    stored = scoring_prices.price_rows(tape, "1")
    run = scoring_prices.run_row(tape, "1")
    # Each bar once: the closes source and the basket read SPY's same closes.
    assert len(stored) < len(tape["rows"])
    rebuilt = []
    for instance, part in run["coverage"].items():
        for ticker, span in part["tickers"].items():
            bars = sorted((r for r in stored if r["kind"] == part["kind"] and r["ticker"] == ticker
                           and span["first"] <= r["bar_date"] <= span["last"]), key=lambda r: r["bar_date"])
            assert len(bars) == span["bars"]
            rebuilt += [{"instance": instance, "kind": r["kind"], "ticker": ticker, "date": r["bar_date"],
                         "open": r["open"], "high": r["high"], "low": r["low"], "close": r["close"],
                         "dividends": r["dividends"]} for r in bars]
    rebuilt.sort(key=lambda r: (r["instance"], r["ticker"], r["date"]))
    assert price_tape.digest(rebuilt) == run["prices_sha256"] == tape["prices_sha256"]


@pytest.mark.parametrize("tamper", [
    lambda t: t["rows"][3].update(close=t["rows"][3]["close"] + 0.01),     # a number changed
    lambda t: t["rows"].pop(),                                              # a bar dropped
    lambda t: t.update(consumer="someone"),                                 # not one of ours
    lambda t: t["rows"][0].update(ticker="nvda; drop table"),               # not a ticker
    lambda t: t.update(note="Bearer " + "z" * 30),                          # credential-shaped
])
def test_a_table_that_does_not_check_is_refused_whole(vendor, tamper):
    tape = _tape(vendor)
    tamper(tape)
    with pytest.raises(scoring_prices.TapeError):
        scoring_prices.load(json.dumps(tape))


def _supabase(monkeypatch):
    from config.settings import get_settings
    from tests.test_archive_capture import SECRET_KEY, URL, Supabase

    settings = get_settings()
    monkeypatch.setattr(settings, "supabase_url", URL, raising=False)
    monkeypatch.setattr(settings, "supabase_service_key", SECRET_KEY, raising=False)
    fake = Supabase()
    real = RemoteArchive.from_settings
    monkeypatch.setattr(RemoteArchive, "from_settings", staticmethod(
        lambda cls=None, client=None: real(client=httpx.Client(transport=httpx.MockTransport(fake)))))
    return fake


def test_the_price_push_is_idempotent_and_refuses_a_bad_table(vendor, tmp_path, monkeypatch, capsys):
    fake = _supabase(monkeypatch)
    good = tmp_path / "race-gate.json"
    good.write_text(price_tape.dumps(_tape(vendor)))
    args = ["--only", "prices", "--prices", str(good), "--run-id", "18000000001"]
    assert push_remote.main(args) == 0
    stored = dict(fake.rows["scoring_prices"])
    assert push_remote.main(args) == 0
    assert fake.rows["scoring_prices"] == stored and len(fake.rows["scoring_runs"]) == 1
    assert "scoring_prices: 0 pushed" in capsys.readouterr().out
    (run,) = fake.rows["scoring_runs"].values()
    assert run["run_id"] == "18000000001" and run["consumer"] == "race-gate"
    # Only prices were sent: no journal, no account, no model calls.
    assert set(fake.rows) == {"scoring_prices", "scoring_runs"}

    bad = tmp_path / "bad.json"
    tape = _tape(vendor)
    tape["rows"][0]["close"] += 1
    bad.write_text(json.dumps(tape))
    before = sum(len(t) for t in fake.rows.values())
    assert push_remote.main(["--only", "prices", "--prices", str(bad)]) == 1
    assert sum(len(t) for t in fake.rows.values()) == before


# --------------------------------------------------------------------------- #
# The workflows: credential-free runs hand over, one keyed workflow pushes
# --------------------------------------------------------------------------- #


def _workflow(name: str) -> dict:
    return yaml.safe_load((ROOT / ".github" / "workflows" / name).read_text())


def test_the_race_and_the_funds_hand_their_prices_over_and_hold_no_secret():
    for name in ("horse-race.yml", "funds.yml"):
        text = (ROOT / ".github" / "workflows" / name).read_text()
        assert "secrets." not in text and "--with-prices" in text
        assert "name: scoring-prices" in text and "retention-days: 90" in text
    funds = {s.get("name"): s for s in _workflow("funds.yml")["jobs"]["funds"]["steps"]}
    # The committed files are the first line, the table the last: split, and counted.
    for step, out in (("The race's gate", "race_gate"), ("Calibration and the funds", "funds")):
        run = funds[step]["run"]
        assert f'head -n 1 "$RUNNER_TEMP/{out}.out" > "$RUNNER_TEMP/{out}.json"' in run
        assert f'test "$(wc -l < "$RUNNER_TEMP/{out}.out")" = "2"' in run


def test_the_push_workflow_takes_only_main_s_scheduled_runs_and_holds_only_the_archive_key():
    wf = _workflow("scoring-prices.yml")
    triggers = wf.get("on") or wf[True]
    assert triggers["workflow_run"]["workflows"] == ["horse race", "shadow funds"]
    assert {_workflow("horse-race.yml")["name"], _workflow("funds.yml")["name"]} == {"horse race", "shadow funds"}
    condition = wf["jobs"]["push"]["if"]
    for guard in ("head_branch == 'main'", "head_repository.full_name == github.repository",
                  "conclusion == 'success'", "event == 'schedule'"):
        assert guard in condition
    assert "pull_request" not in condition
    text = (ROOT / ".github" / "workflows" / "scoring-prices.yml").read_text()
    import re
    assert set(re.findall(r"secrets\.([A-Z_]+)", text)) == {"SUPABASE_URL", "SUPABASE_SERVICE_KEY", "NTFY_TOPIC"}
    assert wf["permissions"] == {"contents": "read", "actions": "read"}
    push = next(s for s in wf["jobs"]["push"]["steps"] if s.get("name") == "Push them to Supabase")
    assert "--only prices" in push["run"]


def test_the_heartbeat_keeps_its_model_calls_as_a_90_day_artifact_before_the_push():
    steps = _workflow("heartbeat.yml")["jobs"]["cycle"]["steps"]
    names = [s.get("name") for s in steps]
    keep = steps[names.index("Keep the day's model calls as an artifact")]
    assert names.index("Keep the day's model calls as an artifact") < names.index("Push the archive to Supabase")
    assert keep["with"]["path"] == "logs/model_io/" and keep["with"]["retention-days"] == 90
    assert keep.get("continue-on-error") is True and keep["if"].startswith("always()")
    # And archive-push.yml can send such an artifact again.
    retry = _workflow("archive-push.yml")
    inputs = (retry.get("on") or retry[True])["workflow_dispatch"]["inputs"]
    assert "model_io_run" in inputs and retry["permissions"]["actions"] == "read"


def test_the_capture_directory_is_never_committed():
    assert "logs/model_io/" in (ROOT / ".gitignore").read_text().splitlines()
    heartbeat = (ROOT / ".github" / "workflows" / "heartbeat.yml").read_text()
    assert all("model_io" not in line for line in heartbeat.splitlines() if "git add" in line)
