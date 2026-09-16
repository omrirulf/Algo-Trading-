"""The scorer end to end: journal file in, report out, no network."""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone

import pytest

from analysis import report
from analysis.reader import read_journal
from analysis.returns import PriceSeries
from analysis.score_journal import as_json, build_parser, main
from analysis.scoring import build_run, score_entries

START = date(2026, 3, 2)


class FakePrices:
    """A 1%-a-day series for every ticker, so outcomes are known in advance."""

    def __init__(self, sessions: int = 30, step: float = 0.01, tickers=None):
        self.sessions, self.step, self.tickers = sessions, step, tickers
        self.asked: list[str] = []

    def closes(self, ticker: str, start: date, end: date) -> PriceSeries:
        self.asked.append(ticker)
        if self.tickers is not None and ticker not in self.tickers:
            return PriceSeries(ticker, [])
        bars = [
            (START + timedelta(days=i), 100.0 * (1 + self.step) ** i)
            for i in range(self.sessions)
        ]
        return PriceSeries(ticker, bars)


def journal_line(offset=0, hour=14, ticker="NVDA", bias="BULLISH", conviction=0.72, **scores):
    """One journal line, ``offset`` sessions into the fake price series."""
    stamp = datetime(2026, 3, 2, hour, tzinfo=timezone.utc) + timedelta(days=offset)
    blend = scores.pop("blend", None)
    payload = {
        "ts_utc": stamp.isoformat(),
        "ticker": ticker,
        "context": {"headlines": ["h"], "gaps": scores.pop("gaps", [])},
        "signal": {
            "ticker": ticker, "bias": bias, "conviction": conviction, "rationale": "r",
            "news_score": scores.get("news", 0.5),
            "technical_score": scores.get("technical", 0.5),
            "fundamental_score": scores.get("fundamental", 0.1),
            "analyst_score": scores.get("analyst", 0.3),
            "key_factors": ["f"],
        },
        "outcome": {"http_status": 200, "status": "ACCEPTED"},
        "error": None,
        "blend": blend,
    }
    return json.dumps(payload) + "\n"


@pytest.fixture
def journal(tmp_path):
    def write(lines):
        path = tmp_path / "signal_journal.log"
        path.write_text("".join(lines), encoding="utf-8")
        return path
    return write


# --------------------------------------------------------------------------- #
# Joining
# --------------------------------------------------------------------------- #


def test_a_rising_series_makes_bullish_calls_hits(journal):
    read = read_journal(journal([journal_line(offset=d) for d in (0, 1, 2)]))
    signals, statuses = score_entries(read.entries, FakePrices(), horizon=3, today=date(2026, 4, 1))

    assert len(signals) == 3
    assert statuses["ok"] == 3
    assert all(s.hit for s in signals)
    assert signals[0].signed_return == pytest.approx(1.01**3 - 1)


def test_bearish_calls_on_the_same_series_are_misses(journal):
    read = read_journal(journal([journal_line(bias="BEARISH")]))
    signals, _ = score_entries(read.entries, FakePrices(), horizon=3, today=date(2026, 4, 1))
    assert not signals[0].hit


def test_neutral_signals_are_not_scored_at_all(journal):
    """Folding a non-call in as a zero would drag every average to the middle."""
    read = read_journal(journal([journal_line(bias="NEUTRAL"), journal_line(bias="BULLISH")]))
    signals, _ = score_entries(read.entries, FakePrices(), horizon=3, today=date(2026, 4, 1))
    assert len(signals) == 1 and signals[0].entry.bias == "BULLISH"


def test_recent_signals_are_pending_rather_than_scored_as_flat(journal):
    read = read_journal(journal([journal_line(offset=27)]))
    signals, statuses = score_entries(read.entries, FakePrices(sessions=30), horizon=3)
    assert signals == [] and statuses["pending"] == 1


def test_a_ticker_without_history_is_reported_not_dropped_silently(journal):
    read = read_journal(journal([journal_line(ticker="NVDA"), journal_line(ticker="DELISTED")]))
    signals, statuses = score_entries(
        read.entries, FakePrices(tickers={"NVDA"}), horizon=3, today=date(2026, 4, 1)
    )
    assert len(signals) == 1 and statuses["no_history"] == 1


def test_price_history_is_fetched_once_per_ticker(journal):
    prices = FakePrices()
    read = read_journal(journal([journal_line(offset=d) for d in range(8)]))
    score_entries(read.entries, prices, horizon=3, today=date(2026, 4, 1))
    assert prices.asked == ["NVDA"]


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def render(journal_path, horizon=3, floor=0.6, **kw):
    run = build_run(
        read=read_journal(journal_path), source=FakePrices(**kw), horizon=horizon,
        floor=floor, today=date(2026, 4, 1),
    )
    return run, report.render(run)


def test_report_flags_a_sample_too_small_to_conclude_from(journal):
    _, text = render(journal([journal_line(offset=d) for d in (0, 1, 2)]))
    assert "too few" in text


def test_report_does_not_flag_a_sample_over_the_threshold(journal):
    # Conviction spread evenly across the range so BOTH sides of the floor
    # clear MIN_SAMPLE — the floor comparison is only as strong as its
    # smaller half, which is the whole point of flagging it.
    lines = [
        journal_line(offset=i, conviction=0.1 + (i % 10) * 0.09, news=(i % 7 - 3) / 3)
        for i in range(60)
    ]
    _, text = render(journal(lines), sessions=80)
    assert "too few to conclude" not in text
    assert "— too few" not in text


def test_dimension_table_does_not_repeat_the_sample_size(journal):
    _, text = render(journal([journal_line(offset=d) for d in (0, 1, 2)]))
    dimension_rows = [ln for ln in text.splitlines() if ln.startswith("news ")]
    assert dimension_rows and "(n=" not in dimension_rows[0]


def test_every_reported_correlation_carries_its_sample_size(journal):
    """A bare rho invites a conclusion the sample may not support."""
    import re

    _, text = render(journal([journal_line(offset=d) for d in (0, 1, 2)]))
    reported = [ln for ln in text.splitlines() if re.search(r"rank corr(elation)?,", ln)]
    assert reported, "expected at least one reported correlation"
    for line in reported:
        assert "n=" in line, line


def test_report_survives_an_all_pending_journal(journal):
    """Two days in, the honest output is a coverage table, not a crash."""
    run, text = render(journal([journal_line(offset=27)]), **{"sessions": 30})
    assert run.signals == []
    assert "No signal has a realised return yet" in text
    assert "pending" in text


def test_report_names_the_entry_rule_it_used(journal):
    _, text = render(journal([journal_line()]))
    assert "entry rule 'auto'" in text
    assert "same-session close" in text


def test_report_warns_when_most_cycles_ran_degraded(journal):
    lines = [journal_line(offset=d, gaps=["fundamentals unavailable: HTTP 429"]) for d in (0, 1, 2)]
    _, text = render(journal(lines))
    assert "More than half of all cycles ran on incomplete context" in text


def test_report_calls_out_a_floor_that_filters_the_wrong_way(journal):
    # Low-conviction bullish calls on a rising series, high-conviction bearish ones:
    # the floor is keeping the losers.
    lines = [journal_line(offset=d, bias="BEARISH", conviction=0.9) for d in (0, 1, 2)]
    lines += [journal_line(offset=d, bias="BULLISH", conviction=0.2) for d in (3, 4, 5)]
    _, text = render(journal(lines))
    assert "discarding signals that did better" in text


def test_agreement_section_appears_without_any_price_data(journal):
    run = build_run(
        read=read_journal(journal([journal_line(news=0.8, technical=-0.8)])),
        source=FakePrices(tickers=set()), horizon=3, floor=0.6, today=date(2026, 4, 1),
    )
    text = report.render(run)
    assert run.signals == []
    assert "Does conviction fall when the dimensions disagree?" in text


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def test_json_output_is_serialisable_and_carries_the_sample_threshold(journal):
    run, _ = render(journal([journal_line(offset=d) for d in (0, 1, 2)]))
    payload = json.loads(json.dumps(as_json(run)))
    assert payload["coverage"]["scored"] == 3
    assert payload["min_sample_for_confidence"] == report.MIN_SAMPLE
    assert "news_score" in payload["dimensions"]


def test_missing_journal_exits_with_a_usable_message(tmp_path, capsys):
    code = main(["--journal", str(tmp_path / "nope.log")])
    assert code == 1
    assert "run it first" in capsys.readouterr().err


def test_a_journal_with_no_usable_entries_exits_nonzero(tmp_path, capsys):
    path = tmp_path / "j.log"
    path.write_text("not json\n", encoding="utf-8")
    assert main(["--journal", str(path)]) == 1
    assert "no usable entries" in capsys.readouterr().err


def test_a_nonsense_horizon_is_refused(journal, capsys):
    code = main(["--journal", str(journal([journal_line()])), "--horizon", "0"])
    assert code == 2
    assert "at least 1 session" in capsys.readouterr().err


def test_defaults_come_from_the_engines_own_settings():
    from config import settings as cfg

    args = build_parser().parse_args([])
    assert args.floor == cfg.MIN_CONVICTION
    assert args.journal == cfg.SIGNAL_JOURNAL_PATH



# --------------------------------------------------------------------------- #
# The learned blend
# --------------------------------------------------------------------------- #


def test_the_blend_is_judged_on_neutral_lines_too_and_the_report_compares_policies(journal):
    lines = [
        journal_line(offset=d, blend={"mode": "shadow", "composite": 0.3, "level": "equal"})
        for d in (0, 1, 2)
    ]
    lines.append(journal_line(
        offset=3, bias="NEUTRAL", conviction=0.2, news=-0.5,
        blend={"mode": "shadow", "composite": -0.2, "level": "ticker:NVDA"},
    ))
    read = read_journal(journal(lines))
    run = build_run(read, FakePrices(), horizon=3, floor=0.6, today=date(2026, 4, 1))

    assert len(run.signals) == 3          # directional only, as before
    assert len(run.blend_signals) == 4    # the NEUTRAL line joins the blend's population

    text = report.render(run)
    section = text.split("Does the learned blend carry information?")[1]
    for label in ("model conviction", "equal weights", "learned blend"):
        assert label in section
    assert "from fitted weights: 1; from the equal-weight fallback: 3" in section
    assert "too few" in section

    payload = as_json(run)
    assert payload["blend"]["learned"]["n"] == 4
    assert payload["blend"]["learned_fitted"] == 1
    assert payload["blend"]["model"]["called"] == 3
    assert payload["blend"]["equal"]["n"] == 4


def test_lines_from_before_the_blend_existed_still_get_the_equal_weight_row(journal):
    read = read_journal(journal([journal_line(offset=d) for d in (0, 1, 2)]))
    run = build_run(read, FakePrices(), horizon=3, floor=0.6, today=date(2026, 4, 1))
    payload = as_json(run)
    assert payload["blend"]["learned"]["n"] == 0
    assert payload["blend"]["equal"]["n"] == 3
    assert payload["blend"]["equal"]["hit_rate"] == 1.0   # rising prices, bullish scores
    assert "Does the learned blend carry information?" in report.render(run)



class WavyPrices:
    """Closes that rise and fall, so three-session returns actually vary."""

    def closes(self, ticker, start, end):
        import math
        bars = [(START + timedelta(days=i), 100.0 + 5.0 * math.sin(i / 2.0) + 0.3 * i) for i in range(60)]
        return PriceSeries(ticker, bars)


def test_the_json_carries_the_verdict_and_the_report_shouts_when_it_is_ready(journal):
    import math
    closes = [100.0 + 5.0 * math.sin(i / 2.0) + 0.3 * i for i in range(60)]
    lines = []
    for d in range(30):
        up = closes[d + 3] > closes[d]
        lines.append(journal_line(
            offset=d, conviction=0.3 + 0.02 * (d % 10),   # the model's conviction varies but is noise
            blend={"mode": "shadow", "composite": 0.6 if up else -0.6, "level": "ticker:NVDA"},
        ))
    run = build_run(read_journal(journal(lines)), WavyPrices(), horizon=3, floor=0.6, today=date(2026, 6, 1))
    payload = as_json(run)
    assert payload["blend"]["promotion"]["ready"] is True
    assert "more often than not" in payload["blend"]["promotion"]["reason"]
    assert "READY TO LEAVE SHADOW" in report.render(run)


def test_a_thin_blend_is_reported_as_not_ready(journal):
    lines = [journal_line(offset=d, blend={"mode": "shadow", "composite": 0.3, "level": "equal"}) for d in (0, 1, 2)]
    run = build_run(read_journal(journal(lines)), FakePrices(), horizon=3, floor=0.6, today=date(2026, 4, 1))
    payload = as_json(run)
    assert payload["blend"]["promotion"] == {"ready": False, "reason": "too few learned composites to judge (n=3, want 20+)"}
    assert "READY TO LEAVE SHADOW" not in report.render(run)
