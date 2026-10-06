"""The voting arm in the funds program: nothing before 2026-12-22, then a race arm and a fund, shadow only.

Pre-registration section 13.11 (the owner's instruction of 4 Oct 2026,
item 1). This file pins the evaluation side: that no key of the vote is in
the funds document before ``config.model_vote.START``; that the race arm
trades the vote's side and its comparator the single call's, on exactly the
lines the vote answered, with a Newey-West t at lag 3; that the fund and its
comparator run only on a look night from the start, are paired from the
sessions after it, with lag 5, and never enter the funds' list; that the
two family rows read their counts of "acting differently"; and that the IC
comparison is descriptive and in no family.

Offline throughout: made-up lines, votes and prices.
"""

from __future__ import annotations

import json
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from analysis import vote as model_vote
from analysis.horse_race import newey_west_t
from analysis.reader import JournalEntry
from analysis.vote import Answer, key_of
from app.schemas import Bias
from config import model_vote as mv
from config import settings as cfg
from shadow import exploratory as xp
from shadow import run as shadow_run
from shadow import vote as sv
from shadow.fund import Day, Line
from tests.test_exploratory import build_args, passed_calibration
from tests.test_shadow_fund import S, said, universe
from tests.test_shadow_variants import Walks

ROOT = Path(__file__).resolve().parents[1]

#: The night before the vote's start, and its first night (a look's night at 23:00 UTC).
THE_NIGHT_BEFORE = datetime(2026, 12, 21, 23, 0, tzinfo=timezone.utc)
THE_FIRST_NIGHT = datetime(2026, 12, 22, 23, 0, tzinfo=timezone.utc)

LOOK_ONE = {"looks": [{"reached": True}, {"reached": False}, {"reached": False}]}


def vote_json(entry: JournalEntry, votes: list[tuple], *, error: str | None = None) -> str:
    """One vote line in the runner's format (scratchpad spec, "Vote line format"): one per production line.

    ``votes`` are votes 1 to 5 as ``(bias, conviction)``, or ``None`` for a
    vote that failed.
    """
    rows = []
    for n, vote in enumerate(votes, start=1):
        bias, conviction = vote if vote is not None else (None, None)
        rows.append({"vote": n, "bias": bias, "conviction": conviction, "scores": {},
                     "error": None if vote is not None else "timeout", "asks": 1, "cost_usd": 0.003})
    return json.dumps({"ts_utc": (entry.timestamp + timedelta(hours=7)).isoformat(), "event": mv.EVENT,
                       "ticker": entry.ticker, "line_ts_utc": entry.timestamp.isoformat(), "run_id": "1",
                       "prompt_sha256": "0" * 64, "model_setup": {}, "reasoning_effort": "high",
                       "votes": rows, "answer": None, "asks": 4, "cost_usd": 0.012, "error": error})


def write_votes(directory: Path, lines: list[str]) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "2026-12.log").write_text("\n".join(lines) + "\n")
    return directory


# --------------------------------------------------------------------------- #
# Nothing before 2026-12-22
# --------------------------------------------------------------------------- #


def args_with_votes(tmp_path, race=None):
    entry = said("XLE", date(2026, 12, 22), bias="BEARISH", conviction=0.6)
    votes = write_votes(tmp_path / "model_vote", [vote_json(entry, [("BEARISH", 0.6)] + [("BULLISH", 0.7)] * 4)])
    args = build_args(tmp_path, race)
    args.votes = votes
    return args


def test_a_look_before_the_start_has_no_key_of_the_vote_anywhere(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    monkeypatch.setattr(shadow_run, "vote_lines_in", lambda path: pytest.fail("the vote's lines read early"))
    out = shadow_run.build(args_with_votes(tmp_path, LOOK_ONE), THE_NIGHT_BEFORE)
    assert calls[-1]["votes"] is None
    assert mv.ARM not in out["exploratory"]["counters"]
    (record,) = out["exploratory"]["checkpoints"]
    assert mv.ARM not in record["race"] and mv.ARM not in record["tests"] and mv.ARM not in record["counters"]
    assert "vote_ic" not in record
    # The table does not even list the vote's rows before its date.
    names = {r["name"] for r in record["table"]["rows"]}
    assert "model_vote, race arm" not in names and "model_vote, fund" not in names


def test_between_checkpoints_before_the_start_the_vote_is_not_even_read(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    monkeypatch.setattr(shadow_run, "vote_lines_in", lambda path: pytest.fail("the vote's lines read early"))
    out = shadow_run.build(args_with_votes(tmp_path), THE_NIGHT_BEFORE)
    assert mv.ARM not in out["exploratory"]["counters"] and calls[-1]["votes"] is None
    assert '"model_vote' not in json.dumps(out)


def test_from_the_start_the_counters_are_there_and_hold_counts_only(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    out = shadow_run.build(args_with_votes(tmp_path), THE_FIRST_NIGHT)
    counters = out["exploratory"]["counters"][mv.ARM]
    assert set(counters) == set(model_vote.COUNTER_KEYS)
    assert counters["lines"] == counters["answered"] == 1 and counters["extra_calls"] == 4
    assert all(type(v) is int for v in counters.values())
    # Between checkpoints: counters, and no answer is handed to the funds.
    assert calls[-1]["votes"] is None and out["exploratory"]["checkpoints"] == []


def test_the_first_look_from_the_start_carries_the_race_arm_the_fund_and_the_ic_comparison(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    out = shadow_run.build(args_with_votes(tmp_path, LOOK_ONE), THE_FIRST_NIGHT)
    (key,) = calls[-1]["votes"]
    assert key[0] == "XLE" and calls[-1]["votes"][key].side == "LONG"
    (record,) = out["exploratory"]["checkpoints"]
    assert mv.ARM in record["counters"]
    # No production line in this journal: the race arm and the IC comparison have nothing yet.
    assert record["race"][mv.ARM]["lines"] == 0 and record["race"][mv.ARM]["t"] is None
    assert record["vote_ic"]["descriptive"] is True and record["vote_ic"]["no_data"] is True
    rows = {r["name"]: r for r in record["table"]["rows"]}
    assert rows["model_vote, race arm"]["no_data"] and rows["model_vote, fund"]["no_data"]
    json.dumps(out, allow_nan=False)


def test_without_a_path_there_are_no_vote_lines():
    assert shadow_run.vote_lines_in(None) == {}
    parsed = shadow_run.build_parser().parse_args([])
    assert parsed.votes is None
    assert shadow_run.build_parser().parse_args(["--votes", "logs/model_vote"]).votes == Path("logs/model_vote")


def test_the_funds_workflow_passes_the_vote_lines_and_holds_no_secret():
    text = (ROOT / ".github" / "workflows" / "funds.yml").read_text()
    assert "secrets." not in text
    run = next(s for s in yaml.safe_load(text)["jobs"]["funds"]["steps"]
               if s.get("name") == "Calibration and the funds")["run"]
    assert "--votes logs/model_vote" in run and "--thesis logs/thesis_check" in run


# --------------------------------------------------------------------------- #
# The signals: the vote, and the single call on the same lines
# --------------------------------------------------------------------------- #


def test_the_vote_fund_trades_the_answer_and_the_comparator_the_single_call_on_the_same_lines():
    day = date(2026, 12, 22)
    answered, unanswered = said("XLE", day, bias="BEARISH", conviction=0.6), said("GLD", day, bias="BULLISH")
    found = {key_of(answered): Answer("LONG", 0.48, 4, 5)}
    vote, comparator = sv.vote_signal(found), sv.comparator_signal(found)
    signal = vote(Line("XLE", day, 1, answered))
    assert signal.bias is Bias.BULLISH and signal.conviction == pytest.approx(0.48)
    single = comparator(Line("XLE", day, 1, answered))
    assert single.bias is Bias.BEARISH and single.conviction == pytest.approx(0.6)
    # A line the vote has no answer for is not dispatched by either.
    assert vote(Line("GLD", day, 1, unanswered)) is None and comparator(Line("GLD", day, 1, unanswered)) is None
    neutral = sv.vote_signal({key_of(answered): Answer("NEUTRAL", 0.0, 0, 5)})(Line("XLE", day, 1, answered))
    assert neutral.bias is Bias.NEUTRAL and neutral.conviction == 0.0


# --------------------------------------------------------------------------- #
# The race arm
# --------------------------------------------------------------------------- #

DEC22, DEC23, DEC21 = date(2026, 12, 22), date(2026, 12, 23), date(2026, 12, 21)


def race_case():
    """Production lines and their vote lines, each line with a reason to be in or out."""
    lines = {
        "long_vs_short": said("XLE", DEC22, bias="BEARISH", conviction=0.6),     # vote LONG, model SHORT
        "too_few_votes": said("GLD", DEC22, bias="BULLISH", conviction=0.6),     # 2 of 5 succeeded: dropped
        "same_side": said("TLT", DEC23, bias="BEARISH", conviction=0.7),         # both SHORT
        "tie": said("XLK", DEC23, bias="BULLISH", conviction=0.5),               # vote NEUTRAL, model LONG
        "before_start": said("IWM", DEC21, bias="BULLISH", conviction=0.6),      # voted, but before START
        "no_vote_line": said("HYG", DEC22, bias="BULLISH", conviction=0.6),
    }
    held = JournalEntry(ticker="JPM", timestamp=lines["long_vs_short"].timestamp, held=True)
    votes = [
        vote_json(lines["long_vs_short"], [("BEARISH", 0.6)] + [("BULLISH", 0.6)] * 4),
        vote_json(lines["too_few_votes"], [("BULLISH", 0.6), ("BULLISH", 0.6), None, None, None]),
        vote_json(lines["same_side"], [("BEARISH", 0.7)] * 5),
        vote_json(lines["tie"], [("BULLISH", 0.5), ("BULLISH", 0.5), ("BEARISH", 0.5), ("BEARISH", 0.5),
                                 ("NEUTRAL", 0.5)]),
        vote_json(lines["before_start"], [("BEARISH", 0.9)] * 5),
        vote_json(held, [("BULLISH", 0.9)] * 5),
    ]
    found = model_vote.answers(model_vote.read_lines(votes))
    return lines, [*lines.values(), held], found


def fake_arm_trades(seen: dict):
    """``xp.arm_trades`` without prices: a long earns 2%, a short loses 1%, entered at the next session."""

    def trades(name, entries, how):
        above = [e for e in entries if e.is_directional and (e.conviction or 0.0) >= how.floor]
        seen[name] = [(e.ticker, e.bias, e.conviction, e.scores, e.blend) for e in above]
        return [SimpleNamespace(ticker=e.ticker, signal_at=e.timestamp, net=0.02 if e.bias == "BULLISH" else -0.01,
                                entry_day=xp.sessions_after(e.timestamp.date(), 1)[0]) for e in above]

    return trades


HOW = xp.RaceSettings(cfg.MIN_CONVICTION, 3, "auto", date(2027, 1, 10), None, None, 100_000.0, 2.0, 0.05, 0.001)


def test_the_race_arm_trades_the_votes_side_on_the_lines_it_answered_against_the_single_call(monkeypatch):
    lines, journal, found = race_case()
    assert key_of(lines["too_few_votes"]) not in found            # fewer than 3 votes: no answer
    seen: dict = {}
    monkeypatch.setattr(xp, "arm_trades", fake_arm_trades(seen))
    answered = [e for e in journal if e.model_answered]
    out = sv.race(answered, found, HOW)
    # The vote: its own side and conviction, the scores and blend left out; NEUTRAL does not trade.
    assert seen[mv.ARM] == [("XLE", "BULLISH", pytest.approx(0.48), {}, {}),
                            ("TLT", "BEARISH", pytest.approx(0.7), {}, {})]
    # The single call on exactly the same lines: the dropped line, the line before START, the held line and
    # the line without a vote are in neither arm.
    assert [(t, b) for t, b, *_ in seen["model"]] == [("XLE", "BEARISH"), ("TLT", "BEARISH"), ("XLK", "BULLISH")]
    assert out["lines"] == 3 and out["trades"] == 2 and out["model_trades"] == 3
    # Vote minus model per entry day: +2% - (-1%) the day after the 22nd; -1% - mean(-1%, +2%) after the 23rd.
    diffs = [0.03, -0.01 - 0.005]
    assert out["days"] == 2 and out["mean_daily_diff"] == pytest.approx(sum(diffs) / 2)
    assert out["t"] == pytest.approx(newey_west_t(diffs, 3)) and HOW.horizon == 3
    # Acting differently: XLE (LONG against SHORT) and XLK (no trade against LONG); TLT is the same.
    assert out["acted"] == 2


def test_acting_differently_is_counted_after_productions_floor():
    day = DEC22
    weak = said("XLE", day, bias="BULLISH", conviction=0.6)
    found = {key_of(weak): Answer("LONG", 0.24, 2, 5)}                  # under 0.30: the vote does not trade
    assert sv.acted([weak], found) == 1
    found = {key_of(weak): Answer("LONG", 0.36, 3, 5)}
    assert sv.acted([weak], found) == 0
    assert cfg.MIN_CONVICTION == 0.30


def test_the_checkpoint_race_adds_the_vote_only_when_it_is_given(monkeypatch):
    monkeypatch.setattr(xp, "race_settings", lambda today, final_through, lines: HOW)
    monkeypatch.setattr(xp, "race_tests", lambda *a, **k: {"insiders": {}})
    monkeypatch.setattr(sv, "race", lambda lines, found, how: {"t": 1.5, "how": how})
    bars = None
    assert shadow_run.checkpoint_race([], bars, DEC22, DEC22) == {"insiders": {}}
    out = shadow_run.checkpoint_race([], bars, DEC22, DEC22, votes={})
    assert out[mv.ARM] == {"t": 1.5, "how": HOW}


# --------------------------------------------------------------------------- #
# The fund and its comparator
# --------------------------------------------------------------------------- #


def fund_case(monkeypatch):
    """Four names every session, the model always short; from START, the vote long on two of them,
    NEUTRAL on a third and silent on the fourth."""
    start = S[10]
    monkeypatch.setattr(mv, "START", start)
    sessions = S[:30]
    entries = [said(t, d, bias="BEARISH", conviction=0.6)
               for d in sessions[:-1] for t in ("MSFT", "JPM", "XOM", "NVDA")]
    found = {}
    for e in entries:
        if e.timestamp.date() < start:
            continue
        if e.ticker in ("MSFT", "JPM"):
            found[key_of(e)] = Answer("LONG", 0.6, 5, 5)
        elif e.ticker == "XOM":
            found[key_of(e)] = Answer("NEUTRAL", 0.0, 0, 5)
    return start, sessions, entries, found


def test_the_vote_fund_and_its_comparator_trade_only_the_answered_lines_from_the_start(monkeypatch):
    start, sessions, entries, found = fund_case(monkeypatch)
    made = []
    real = shadow_run.vote_funds
    monkeypatch.setattr(shadow_run, "vote_funds", lambda *a, **k: made.extend(real(*a, **k)) or made)
    bars = universe()
    out, checks = shadow_run.run_funds(entries, sessions[0], sessions[-1], Walks(bars), random_funds=1,
                                       processes=1, shortable_no=frozenset(), votes=found)
    vote_fund, comparator = made
    assert (vote_fund.name, comparator.name) == (mv.ARM, mv.COMPARATOR_FUND)
    bought = [(f.day, f.ticker, f.side) for f in vote_fund.broker.fills if f.kind == "entry"]
    sold = [(f.day, f.ticker, f.side) for f in comparator.broker.fills if f.kind == "entry"]
    assert bought and sold
    # The vote: long, and only where it answered LONG; the comparator: the model's short on every line the
    # vote answered, NEUTRAL included; neither on the line it did not answer, and nothing before START.
    assert {t for _, t, _ in bought} <= {"MSFT", "JPM"} and {s for *_, s in bought} == {"buy"}
    assert {t for _, t, _ in sold} <= {"MSFT", "JPM", "XOM"} and "XOM" in {t for _, t, _ in sold}
    assert {s for *_, s in sold} == {"sell"}
    assert min(d for d, *_ in bought + sold) > start
    # Never in the funds' list, and checked like every fund.
    assert mv.ARM not in {r["name"] for r in out["list"]} and mv.COMPARATOR_FUND not in {r["name"] for r in out["list"]}
    assert checks["four"]["ok"] is True
    test = out["tests"][mv.ARM]
    assert test["compare_to"] == mv.COMPARATOR_FUND
    assert test["days"] == sum(1 for d in sessions if d > start) and date.fromisoformat(test["from"]) > start
    assert test == shadow_run.paired(vote_fund, comparator, after=start) | {"acted": test["acted"]}
    # Every answered line acts differently here: LONG or NEUTRAL against the model's short.
    assert test["acted"] == len(found) == sv.acted(sv.lines_with_an_answer(entries, found), found)
    json.dumps(out, allow_nan=False)


def test_without_votes_no_vote_fund_is_run(monkeypatch):
    _, sessions, entries, _ = fund_case(monkeypatch)
    monkeypatch.setattr(shadow_run, "vote_funds", lambda *a, **k: pytest.fail("a vote fund without votes"))
    out, _ = shadow_run.run_funds(entries, sessions[0], sessions[5], Walks(universe()), random_funds=1,
                                  processes=1, shortable_no=frozenset())
    assert mv.ARM not in out["tests"]


def equity_fund(name: str, days: list[date], equity: list[float]):
    return SimpleNamespace(name=name, days=[Day(d, e, e, 0.0, 0) for d, e in zip(days, equity)])


def test_the_fund_test_is_paired_from_the_sessions_after_the_start_with_lag_5():
    days = S[:8]
    mine = equity_fund("a", days, [100_000.0, 100_500.0, 100_200.0, 101_000.0, 100_800.0, 101_500.0, 101_200.0,
                                   102_000.0])
    theirs = equity_fund("b", days, [100_000.0, 99_800.0, 100_100.0, 100_300.0, 100_000.0, 100_400.0, 100_600.0,
                                     100_500.0])
    every = shadow_run.paired(mine, theirs)
    later = shadow_run.paired(mine, theirs, after=days[2])
    assert every["days"] == 8 and later["days"] == 5 and later["from"] == days[3].isoformat()

    def returns(f):
        equity = [100_000.0] + [d.equity for d in f.days]
        return {d.day: b / a - 1.0 for d, a, b in zip(f.days, equity, equity[1:])}

    diffs = [returns(mine)[d] - returns(theirs)[d] for d in days[3:]]
    assert later["mean_daily_diff"] == pytest.approx(sum(diffs) / 5)
    assert later["t"] == pytest.approx(newey_west_t(diffs, 5)) and shadow_run.VS_MODEL_LAG == 5
    # Every other caller is unchanged.
    assert shadow_run.paired(mine, theirs, after=None) == every


# --------------------------------------------------------------------------- #
# The family: two rows, read by the table; "not tested" under 20 at the final look
# --------------------------------------------------------------------------- #


def test_the_family_has_the_vote_as_a_race_arm_and_as_a_fund():
    rows = [row for row in shadow_run.FAMILY if row[2] == mv.ARM]
    assert rows == [("model_vote, race arm", "race", mv.ARM, ("race", mv.ARM, "acted")),
                    ("model_vote, fund", "tests", mv.ARM, ("tests", mv.ARM, "acted"))]
    assert len(shadow_run.FAMILY) == 12
    assert not any(row[1] == "vote_ic" for row in shadow_run.FAMILY)          # the IC comparison is descriptive


def test_the_table_reads_the_vote_and_says_not_tested_under_20_at_the_final_look():
    stats = {"sr": 0.2, "t_days": 60, "skew": 0.0, "kurt": 3.0}
    record = {"look": 2,
              "race": {mv.ARM: {"t": 1.2, "stats": stats, "mean_daily_diff": 0.001, "acted": 25}},
              "tests": {mv.ARM: {"t": -0.3, "stats": stats, "mean_daily_diff": -0.0001, "acted": 25}}}
    rows = {r["name"]: r for r in shadow_run.checkpoint_table_for(record)["rows"]}
    race, fund = rows["model_vote, race arm"], rows["model_vote, fund"]
    assert race["t"] == 1.2 and race["acted_differently"] == 25 and race["dsr"] is not None
    assert fund["t"] == -0.3 and fund["acted_differently"] == 25 and race["outcome"] == "not proven"
    final = {"look": shadow_run.FINAL_LOOK,
             "race": {mv.ARM: dict(record["race"][mv.ARM], acted=19)},
             "tests": {mv.ARM: dict(record["tests"][mv.ARM], acted=19)}}
    rows = {r["name"]: r for r in shadow_run.checkpoint_table_for(final)["rows"]}
    assert rows["model_vote, race arm"]["outcome"] == rows["model_vote, fund"]["outcome"] == "not tested"
    assert shadow_run.MIN_ACTED == 20


def test_a_table_made_before_the_start_does_not_list_the_vote_at_all():
    """The owner, 4 Oct 2026: nothing of a new idea is shown before its registration date, not even a "no data" row."""
    early = {"look": 1, "made_on": (mv.START - timedelta(days=1)).isoformat()}
    names = {r["name"] for r in shadow_run.checkpoint_table_for(early)["rows"]}
    assert not any(name.startswith("model_vote") for name in names)
    assert len(names) == len(shadow_run.FAMILY) - 2
    on_the_day = {"look": 1, "made_on": mv.START.isoformat()}
    rows = {r["name"]: r for r in shadow_run.checkpoint_table_for(on_the_day)["rows"]}
    assert rows["model_vote, race arm"]["no_data"] is True and rows["model_vote, fund"]["no_data"] is True
    assert set(shadow_run.FAMILY_FROM) == {"model_vote, race arm", "model_vote, fund"}
    assert set(shadow_run.FAMILY_FROM.values()) == {mv.START}


# --------------------------------------------------------------------------- #
# The IC comparison: descriptive only
# --------------------------------------------------------------------------- #


def test_the_ic_comparison_is_descriptive_and_reads_the_vote_score_against_the_single_call():
    day = DEC22
    names = ["XLE", "GLD", "TLT", "XLK", "IWM", "HYG", "JPM", "MSFT", "NVDA", "XOM"]
    entries, votes, bars = [], [], {}
    after = xp.sessions_after(day, 3)
    for i, ticker in enumerate(names):
        e = said(ticker, day, bias="BULLISH", conviction=0.6,
                 blend={"composite": i / 10, "applied": {"news_score": 1.0}})
        entries.append(e)
        row = json.loads(vote_json(e, [("BULLISH", 0.6)] * 5))
        for vote in row["votes"][1:]:
            vote["scores"] = {"news_score": -i / 10}
        votes.append(json.dumps(row))
        bars[ticker] = [(d, 100.0, 100.0 + i + k) for k, d in enumerate(after)]
    lines = model_vote.read_lines(votes)
    out = model_vote.ic_comparison(entries, lines, bars, after[-1])
    assert out["descriptive"] is True and out["in_family"] is False and "main" not in out
    assert out["lines"] == 10
    one = out["horizons"]["1"]
    # The single call ranks the names as they then moved (IC 1); the vote's mean score ranks them backwards.
    assert one["single_call"]["mean_ic"] == pytest.approx(1.0) and one["vote"]["mean_ic"] == pytest.approx(-1.0)
    assert one["vote_minus_single_call"]["mean"] == pytest.approx(-2.0)
    assert "t" not in out and "stats" not in out


def test_the_ic_comparisons_prices_come_through_a_fetcher_of_its_own(monkeypatch):
    asked = []

    class Fetcher:
        def __init__(self, **kw):
            pass

        def ohlc(self, ticker, start, end):
            asked.append((ticker, start, end))
            import pandas as pd

            return pd.DataFrame()

    monkeypatch.setattr(shadow_run, "OhlcFetcher", Fetcher)
    entry = said("XLE", DEC22)
    lines = model_vote.read_lines([vote_json(entry, [("BULLISH", 0.6)] * 5)])
    used: list = []
    out = shadow_run.vote_ic_record([entry], lines, DEC23, used)
    assert [name for name, _ in used] == ["ohlc_vote_ic"]
    assert asked == [("XLE", DEC22 - timedelta(days=45), DEC23)]
    assert out["descriptive"] is True and out["in_family"] is False
    # No vote answer: nothing is fetched.
    used.clear()
    shadow_run.vote_ic_record([entry], {}, DEC23, used)
    assert used == []


def test_the_vote_lines_are_read_as_the_runner_writes_them(tmp_path):
    entry = said("XLE", DEC22, bias="BEARISH", conviction=0.6)
    directory = write_votes(tmp_path / "model_vote", [
        vote_json(entry, [("BEARISH", 0.6)] + [("BULLISH", 0.6)] * 4),
        vote_json(replace(entry, ticker="GLD"), [("BULLISH", 0.6)], error="no archived input for this line"),
    ])
    lines = shadow_run.vote_lines_in(directory)
    assert set(lines) == {("XLE", entry.timestamp), ("GLD", entry.timestamp)}
    found = model_vote.answers(lines)
    assert list(found) == [("XLE", entry.timestamp)] and found[("XLE", entry.timestamp)].side == "LONG"
    counts = model_vote.counters(lines, DEC22)
    assert counts["not_voted"] == 1 and counts["answered"] == 1


# --------------------------------------------------------------------------- #
# The rule itself: the side needs 3 of the 5 votes; the vote score counts vote 1
# --------------------------------------------------------------------------- #


def _votes(*said) -> list[model_vote.Vote]:
    """Votes 1 to 5 from ``(bias, conviction)``; None is a failed vote."""
    return [model_vote.Vote(n, *pair) if pair is not None else model_vote.Vote(n, error="timeout")
            for n, pair in enumerate(said, start=1)]


def test_a_side_with_only_two_votes_is_neutral_even_when_it_leads():
    """The owner, 4 Oct 2026: the plurality needs at least 3 of the 5 votes, otherwise NEUTRAL."""
    votes = _votes(("BULLISH", 1.0), ("BULLISH", 1.0), ("BEARISH", 0.5), ("NEUTRAL", 0.5), None)
    assert model_vote.aggregate(votes) == Answer("NEUTRAL", 0.0, 0, 4)
    assert model_vote.tradeable("NEUTRAL", 0.0, cfg.MIN_CONVICTION) == model_vote.NO_TRADE


def test_three_of_four_successful_votes_is_an_answer_whose_share_is_out_of_five():
    votes = _votes(("BULLISH", 0.6), ("BULLISH", 0.5), ("BULLISH", 0.7), ("BEARISH", 0.4), None)
    answer = model_vote.aggregate(votes)
    assert (answer.side, answer.agree, answer.successful) == ("LONG", 3, 4)
    assert answer.conviction == pytest.approx(3 / 5 * (0.6 + 0.5 + 0.7) / 3)
    assert model_vote.aggregate(_votes(("BULLISH", 0.6), ("BULLISH", 0.5), None, None, None)) is None


def _entry_with_blend(composite: float | None, applied: dict | None) -> JournalEntry:
    blend = {"composite": composite} | ({"applied": applied} if applied is not None else {})
    return JournalEntry(ticker="XLE", timestamp=datetime(2026, 12, 22, 15, tzinfo=timezone.utc), bias="BULLISH",
                        conviction=0.6, blend=blend)


def _line_of(votes: list[model_vote.Vote]) -> model_vote.VoteLine:
    stamp = datetime(2026, 12, 22, 15, tzinfo=timezone.utc)
    return model_vote.VoteLine(key=("XLE", stamp), ticker="XLE", day=stamp.date(), votes=tuple(votes))


def test_the_vote_score_is_the_mean_of_the_successful_votes_with_vote_one_included():
    """The owner, 4 Oct 2026: the vote score is the mean of the five blended scores. Vote 1 is the line's own."""
    weights = {"technical_score": 1.0}
    flat = {"news_score": None, "technical_score": 0.0, "fundamental_score": None, "analyst_score": None,
            "insider_score": None}
    four = [model_vote.Vote(n, "NEUTRAL", 0.0, dict(flat)) for n in range(2, 6)]
    entry = _entry_with_blend(0.5, weights)
    first = model_vote.Vote(1, "BULLISH", 0.6, dict(flat))
    assert model_vote.vote_score(entry, _line_of([first, *four])) == pytest.approx(0.5 / 5)
    failed = [*four[:3], model_vote.Vote(5, error="timeout")]
    assert model_vote.vote_score(entry, _line_of([first, *failed])) == pytest.approx(0.5 / 4)
    # A line that recorded no weights has no vote score: its other votes could not be blended alike.
    assert model_vote.vote_score(_entry_with_blend(0.5, None), _line_of([first, *four])) is None


def test_an_answered_line_with_no_vote_record_is_counted_as_missing():
    """Section 13.11: "a line not voted that day ... is counted", whatever kept it from being voted."""
    stamp = datetime(2026, 12, 22, 15, tzinfo=timezone.utc)
    voted = JournalEntry(ticker="XLE", timestamp=stamp, timestamp_is_exact=True, bias="BULLISH", conviction=0.6)
    lost = JournalEntry(ticker="GLD", timestamp=stamp, timestamp_is_exact=True, bias="NEUTRAL", conviction=0.0)
    held = JournalEntry(ticker="TLT", timestamp=stamp, timestamp_is_exact=True, held=True)
    early = JournalEntry(ticker="SLV", timestamp=stamp - timedelta(days=1), timestamp_is_exact=True,
                         bias="BULLISH", conviction=0.6)
    lines = {("XLE", stamp): _line_of(_votes(("BULLISH", 0.6), ("BULLISH", 0.6), ("BULLISH", 0.6), None, None))}
    counts = model_vote.counters(lines, stamp.date(), [voted, lost, held, early])
    assert counts["missing"] == 1 and counts["lines"] == 1 and counts["answered"] == 1
    assert model_vote.counters(lines, stamp.date())["missing"] == 0          # no journal given: none counted
