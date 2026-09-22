"""Taking the news away must change exactly one thing.

An ablation is only an ablation if the two prompts differ in the news block
and nowhere else, if the two answers are paired to the right side, and if
the flip rate it reports is read against the model's own inconsistency
rather than against zero. Each of those is a silent-wrongness bug -- a
swapped pair or a drifting system prompt produces a clean-looking number
about the wrong question -- so each gets a test.
"""

from __future__ import annotations

import json

import pytest

from app.schemas import Bias, LLMSignal
from orchestrator.context import TickerContext
from replay import news_ablation as na
from replay import runner
from replay.runner import ReplayEntry

HEADLINES = ["Chipmaker raises guidance — revenue seen up 20% (Reuters, 2h ago)"]


def journal_line(ticker="AAPL", bias="BULLISH", conviction=0.72, headlines=HEADLINES,
                 ts="2026-09-12T14:00:00+00:00") -> str:
    context = TickerContext(ticker=ticker, headlines=list(headlines))
    return json.dumps({
        "ts_utc": ts, "ticker": ticker, "context": context.as_dict(),
        "signal": {"ticker": ticker, "bias": bias, "conviction": conviction, "rationale": "r"},
        "outcome": None, "error": None,
    })


def entry(ticker="AAPL", headlines=HEADLINES) -> ReplayEntry:
    lines = [journal_line(ticker, headlines=headlines)]
    return next(iter(runner.load_entries(lines)))


def signal(bias=Bias.BULLISH, conviction=0.7, news=0.5) -> LLMSignal:
    return LLMSignal(ticker="AAPL", bias=bias, conviction=conviction, rationale="r",
                     news_score=news)


def pair(with_bias=Bias.BULLISH, without_bias=Bias.BULLISH, with_conv=0.7,
         without_conv=0.7, journalled=Bias.BULLISH, repeated=None,
         asked_model="claude-opus-5", journalled_model="claude-opus-5") -> na.Ablation:
    return na.Ablation(
        ticker="AAPL", ts_utc="2026-09-12T14:00:00+00:00",
        with_news=signal(with_bias, with_conv),
        without_news=signal(without_bias, without_conv),
        journalled=None if journalled is None else signal(journalled),
        journalled_model=journalled_model,
        asked_model=asked_model,
        repeated=None if repeated is None else signal(repeated),
    )


# --------------------------------------------------------------------------- #
# The sample: only lines the ablation can say anything about
# --------------------------------------------------------------------------- #


def test_only_lines_that_carry_headlines_are_eligible():
    """Blanking a line that already says 'none found' costs two calls to
    prove an empty list stayed empty."""
    lines = [journal_line("AAPL"), journal_line("MSFT", headlines=[])]
    assert [e.ticker for e in na.eligible(list(runner.load_entries(lines)))] == ["AAPL"]


def test_a_line_with_no_rebuilt_context_is_not_eligible():
    assert na.eligible([ReplayEntry(ticker="X", ts_utc=None, prompt="p", original=None)]) == []


# --------------------------------------------------------------------------- #
# The two prompts differ in the news block and nowhere else
# --------------------------------------------------------------------------- #


def test_removing_the_news_leaves_the_rest_of_the_prompt_byte_identical():
    original = entry()
    stripped = na.without_news(original)
    assert "Chipmaker raises guidance" in original.prompt
    assert "Chipmaker raises guidance" not in stripped.prompt

    def without_news_block(prompt: str) -> list[str]:
        return [s for s in prompt.split("\n\n") if not s.startswith("NEWS (past 24 hours)")]

    assert without_news_block(original.prompt) == without_news_block(stripped.prompt)


def test_the_blanked_prompt_says_none_found_rather_than_unavailable():
    """'none found' is a quiet day; 'unavailable' asserts a failed lookup.
    The ablation must not make a claim the cycle never made."""
    stripped = na.without_news(entry())
    news_block = stripped.prompt.split("\n\n", 2)[1]
    assert news_block == "NEWS (past 24 hours)\n- none found"


def test_the_blanked_prompt_is_something_as_prompt_can_produce():
    """Built by re-rendering a real context, not by editing a string: the
    ablated prompt must be identical to what a genuinely newsless cycle
    would have sent for the same ticker."""
    stripped = na.without_news(entry())
    newsless = TickerContext(ticker="AAPL", headlines=[])
    assert stripped.prompt == newsless.as_prompt()
    assert stripped.context.headlines == [] and stripped.context.sources == []


def test_both_arms_are_asked_with_the_same_system_prompt():
    """The fund prompt is narrowed by the sections a context carries. If the
    blanked context were re-resolved, the ablation would be one refactor
    away from varying the system prompt as well as the news."""
    seen: list[str] = []

    def complete(system, user, schema):
        seen.append(system)
        return json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    na.ablate([entry(), entry("MSFT")], complete)
    assert len(seen) == 4
    assert len(set(seen)) == 1


# --------------------------------------------------------------------------- #
# Pairing: the two answers must not be swapped
# --------------------------------------------------------------------------- #


def test_the_with_and_without_answers_land_on_the_right_side():
    """Both arms are asked in one flat list, with-news first. A slicing
    error here would silently invert every conclusion."""
    def complete(system, user, schema):
        # The prompt itself says which arm this is.
        bias = "BEARISH" if "- none found" in user else "BULLISH"
        ticker = user.split("TICKER: ", 1)[1].split("\n", 1)[0]
        return json.dumps({"ticker": ticker, "bias": bias, "conviction": 0.5, "rationale": "r"})

    pairs, results = na.ablate([entry(), entry("MSFT")], complete)
    assert len(pairs) == 2 and len(results) == 4
    for p in pairs:
        assert p.with_news.bias is Bias.BULLISH
        assert p.without_news.bias is Bias.BEARISH


def test_each_pair_keeps_its_own_ticker_and_timestamp():
    def complete(system, user, schema):
        ticker = user.split("TICKER: ", 1)[1].split("\n", 1)[0]
        return json.dumps({"ticker": ticker, "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    pairs, _ = na.ablate([entry("AAPL"), entry("MSFT")], complete)
    assert [p.ticker for p in pairs] == ["AAPL", "MSFT"]
    assert all(p.ts_utc == "2026-09-12T14:00:00+00:00" for p in pairs)


def test_a_failed_call_on_either_side_makes_the_pair_unassessable():
    assert not na.Ablation("AAPL", None, signal(), None, None).assessable
    assert not na.Ablation("AAPL", None, None, signal(), None).assessable
    assert na.Ablation("AAPL", None, signal(), signal(), None).assessable


# --------------------------------------------------------------------------- #
# What the pair means
# --------------------------------------------------------------------------- #


def test_a_direction_change_is_the_two_fresh_answers_not_the_journalled_one():
    p = pair(with_bias=Bias.BULLISH, without_bias=Bias.BEARISH, journalled=Bias.BEARISH)
    assert p.direction_changed is True
    assert p.self_flipped is True      # the journalled answer disagrees too, separately


# --- the noise floor, and what is allowed to stand in for one -------------------


def test_the_repeat_is_the_floor_whenever_there_is_one():
    """Same prompt, same model, same run: nothing between the two answers
    but the model's own sampling."""
    assert pair(with_bias=Bias.BULLISH, repeated=Bias.BULLISH).repeat_flipped is False
    assert pair(with_bias=Bias.BULLISH, repeated=Bias.BEARISH).repeat_flipped is True
    assert pair().repeat_flipped is None, "no repeat was asked for"


def test_the_repeat_beats_the_journal_as_the_floor():
    """Both available: the repeat wins, because the journalled answer was
    produced on another day and, on a funnel, often by another model."""
    p = pair(with_bias=Bias.BULLISH, repeated=Bias.BULLISH, journalled=Bias.BEARISH)
    assert p.journal_flipped is True and p.repeat_flipped is False
    assert p.self_flipped is False


def test_the_journal_fallback_only_counts_the_same_models_answers():
    """The funnel writes Haiku on a screened line and the full model on an
    escalated one. Diffing a fresh Opus answer against Haiku's is a
    cross-model disagreement, not a noise floor."""
    same = pair(with_bias=Bias.BEARISH, journalled=Bias.BULLISH,
                asked_model="claude-opus-5", journalled_model="claude-opus-5")
    assert same.journal_comparable is True and same.self_flipped is True

    crossed = pair(with_bias=Bias.BEARISH, journalled=Bias.BULLISH,
                   asked_model="claude-opus-5", journalled_model="claude-haiku-4-5-20251001")
    assert crossed.journal_comparable is False
    assert crossed.journal_flipped is None and crossed.self_flipped is None


def test_a_dated_snapshot_is_the_same_model_as_its_alias():
    """The config names an alias; the API answers with the snapshot."""
    p = pair(asked_model="claude-haiku-4-5", journalled_model="claude-haiku-4-5-20251001")
    assert p.journal_comparable is True


def test_a_candidate_the_journal_never_ran_has_no_fallback_floor_at_all():
    p = pair(asked_model="openai/gpt-oss-120b", journalled_model="claude-opus-5")
    assert p.self_flipped is None


def test_a_trade_decision_changes_when_a_call_crosses_the_floor_either_way():
    same_side = pair(with_conv=0.50, without_conv=0.20)
    assert same_side.direction_changed is False
    assert same_side.trade_decision_changed(floor=0.30) is True
    assert same_side.trade_decision_changed(floor=0.10) is False


def test_a_neutral_call_is_never_a_trade_whatever_its_conviction():
    p = pair(with_bias=Bias.BULLISH, without_bias=Bias.NEUTRAL, with_conv=0.9, without_conv=0.9)
    assert p.trade_decision_changed(floor=0.30) is True


def test_conviction_delta_is_without_minus_with():
    assert pair(with_conv=0.4, without_conv=0.7).conviction_delta == pytest.approx(0.3)


# --------------------------------------------------------------------------- #
# The summary, and the noise floor it is read against
# --------------------------------------------------------------------------- #


def test_the_flip_rate_is_counted_over_assessable_pairs_only():
    pairs = [
        pair(without_bias=Bias.BEARISH),                      # flipped
        pair(),                                               # did not
        na.Ablation("AAPL", None, signal(), None, None),      # failed; excluded
    ]
    summary = na.summarise(pairs, floor=0.30, failures=1)
    assert summary.n_assessable == 2
    assert summary.flip_rate == pytest.approx(0.5)


def test_an_ablation_no_bigger_than_the_models_own_wobble_does_not_clear_the_floor():
    """Two flips out of four either way: the news moved nothing the model
    was not already moving on its own."""
    pairs = [
        pair(without_bias=Bias.BEARISH, repeated=Bias.BEARISH),
        pair(without_bias=Bias.BEARISH, repeated=Bias.BEARISH),
        pair(repeated=Bias.BULLISH), pair(repeated=Bias.BULLISH),
    ]
    summary = na.summarise(pairs, floor=0.30, failures=0)
    assert summary.flip_rate == pytest.approx(0.5)
    assert summary.self_flip_rate == pytest.approx(0.5)
    assert summary.clears_the_noise_floor is False
    assert "NO MORE than" in na.render(summary, pairs, 0.30, "m")


def test_an_ablation_bigger_than_the_wobble_clears_it():
    pairs = [pair(without_bias=Bias.BEARISH, repeated=Bias.BULLISH) for _ in range(3)]
    pairs.append(pair(repeated=Bias.BULLISH))
    summary = na.summarise(pairs, floor=0.30, failures=0)
    assert summary.flip_rate == pytest.approx(0.75)
    assert summary.self_flip_rate == pytest.approx(0.0)
    assert summary.clears_the_noise_floor is True
    assert "changing the call" in na.render(summary, pairs, 0.30, "m")


def test_the_summary_names_where_its_floor_came_from():
    repeats = na.summarise([pair(repeated=Bias.BULLISH)], 0.30, 0)
    assert repeats.floor_source == "repeat"
    assert "asked twice" in repeats.floor_label

    journal = na.summarise([pair()], 0.30, 0)
    assert journal.floor_source == "journal"
    assert "journalled" in journal.floor_label


def test_a_run_with_no_floor_withholds_its_verdict_rather_than_implying_zero():
    """The failure this guards against: a cross-model comparison inflating
    the floor until a real effect reads as nothing. With no floor at all the
    honest output is a refusal, not a number."""
    pairs = [pair(without_bias=Bias.BEARISH, asked_model="openai/gpt-oss-120b",
                  journalled_model="claude-opus-5") for _ in range(4)]
    summary = na.summarise(pairs, floor=0.30, failures=0)
    assert summary.flip_rate == pytest.approx(1.0)
    assert summary.floor_source is None and summary.self_flip_rate is None
    assert summary.clears_the_noise_floor is None

    text = na.render(summary, pairs, 0.30, "openai/gpt-oss-120b")
    assert "WITHHELD" in text
    assert "--repeat-with-news" in text
    assert "NOT MEASURED" in text


def test_the_report_says_how_many_journalled_answers_were_the_wrong_model():
    pairs = [pair(repeated=Bias.BULLISH, journalled_model="claude-haiku-4-5-20251001")
             for _ in range(3)]
    summary = na.summarise(pairs, 0.30, 0)
    assert summary.journal_cross_model == 3
    assert "came from another model" in na.render(summary, pairs, 0.30, "m")


def test_nothing_assessable_is_a_verdict_of_its_own_not_a_zero():
    summary = na.summarise([], floor=0.30, failures=4)
    assert summary.flip_rate is None and summary.clears_the_noise_floor is None
    assert "not enough answered twice" in na.render(summary, [], 0.30, "m")


def test_the_report_names_every_line_the_news_turned():
    pairs = [pair(without_bias=Bias.BEARISH), pair()]
    text = na.render(na.summarise(pairs, 0.30, 0), pairs, 0.30, "claude-opus-5 / low")
    assert "EVERY LINE THE NEWS TURNED" in text
    assert "claude-opus-5 / low" in text
    assert text.count("AAPL") == 1, "only the changed line is listed"


# --------------------------------------------------------------------------- #
# The returns half
# --------------------------------------------------------------------------- #


def test_emitted_pairs_carry_both_sides_of_the_same_context(capsys):
    entries = [entry("AAPL"), entry("MSFT")]
    pairs = [pair(), na.Ablation("MSFT", None, signal(), None, None)]
    printed = na.print_pairs(entries, pairs)
    assert printed == 1, "a pair only one side answered is not scoreable"

    records = [json.loads(line) for line in capsys.readouterr().out.splitlines() if line.strip()]
    assert [r["_side"] for r in records] == [na.WITH_NEWS, na.WITHOUT_NEWS]
    # Same context and same instant on both sides: only the signal differs.
    assert records[0]["line"]["ticker"] == records[1]["line"]["ticker"] == "AAPL"
    assert records[0]["line"]["ts_utc"] == records[1]["line"]["ts_utc"]
    assert records[0]["line"]["context"] == records[1]["line"]["context"]


def test_emitting_pairs_keeps_the_human_report_off_stdout(tmp_path, monkeypatch, capsys):
    """stdout is about to be split into journal lines; a report mixed into
    it would corrupt the stream."""
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL") + "\n", encoding="utf-8")

    def complete(system, user, schema):
        return json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    monkeypatch.setattr(runner, "measured_completer", lambda **kwargs: (complete, []))
    assert na.main(["--journal", str(journal), "--model", "m", "--emit-pairs"]) == 0

    captured = capsys.readouterr()
    for line in captured.out.splitlines():
        if line.strip():
            json.loads(line)          # every stdout line is a record
    assert "THE NEWS SECTION" in captured.err


# --------------------------------------------------------------------------- #
# main() end to end
# --------------------------------------------------------------------------- #


def test_main_asks_each_context_exactly_twice(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text("\n".join([journal_line("AAPL"), journal_line("MSFT")]) + "\n",
                       encoding="utf-8")
    calls = {"n": 0}

    def complete(system, user, schema):
        calls["n"] += 1
        return json.dumps({"ticker": user.split("TICKER: ", 1)[1].split("\n", 1)[0],
                           "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    monkeypatch.setattr(runner, "measured_completer", lambda **kwargs: (complete, []))
    assert na.main(["--journal", str(journal), "--model", "m"]) == 0
    assert calls["n"] == 4
    out = capsys.readouterr()
    assert "2 context(s) x 2 = 4 calls" in out.err
    assert "THE NEWS SECTION, TAKEN AWAY" in out.out


def test_a_dry_run_asks_nothing_and_says_what_it_would_cost(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL") + "\n", encoding="utf-8")

    def explode(**kwargs):
        raise AssertionError("a dry run must not build a completer")

    monkeypatch.setattr(runner, "measured_completer", explode)
    assert na.main(["--journal", str(journal), "--model", "m", "--dry-run"]) == 0
    assert "1 context(s) x 2 = 2 calls" in capsys.readouterr().err


def test_a_journal_with_no_headlines_anywhere_says_so_rather_than_asking(tmp_path, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL", headlines=[]) + "\n", encoding="utf-8")
    assert na.main(["--journal", str(journal), "--model", "m"]) == 1
    assert "nothing to take away" in capsys.readouterr().err


def test_a_missing_journal_is_an_error_naming_it(tmp_path, capsys):
    assert na.main(["--journal", str(tmp_path / "nope.log"), "--model", "m"]) == 1
    assert "nope.log" in capsys.readouterr().err


def test_a_blank_effort_input_means_no_effort_asked(tmp_path, monkeypatch):
    """A workflow_dispatch text input left blank arrives as '', not absent."""
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL") + "\n", encoding="utf-8")
    seen = {}

    def fake(**kwargs):
        seen.update(kwargs)

        def complete(system, user, schema):
            return json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5,
                               "rationale": "r"})
        return complete, []

    monkeypatch.setattr(runner, "measured_completer", fake)
    na.main(["--journal", str(journal), "--model", "m", "--effort", ""])
    assert seen["effort"] is None


def test_claude_is_never_asked_concurrently(tmp_path, monkeypatch):
    """A rate-limited context is a lost one, where a slow one is only slow."""
    seen = {}

    def fake_replay_each(entries, prompt_for, complete, max_workers=1):
        seen["workers"] = max_workers
        return []

    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL") + "\n", encoding="utf-8")
    monkeypatch.setattr(runner, "measured_completer", lambda **kwargs: (None, []))
    monkeypatch.setattr(runner, "replay_each", fake_replay_each)
    na.main(["--journal", str(journal), "--model", "m", "--concurrency", "8"])
    assert seen["workers"] == 1


def test_the_repeat_arm_asks_each_context_a_third_time_with_the_with_news_prompt():
    """The third arm must send the WITH-news prompt again -- repeating the
    blanked one would measure the wrong arm's wobble."""
    seen: list[str] = []

    def complete(system, user, schema):
        seen.append("blank" if "- none found" in user else "news")
        ticker = user.split("TICKER: ", 1)[1].split("\n", 1)[0]
        return json.dumps({"ticker": ticker, "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    pairs, results = na.ablate([entry("AAPL"), entry("MSFT")], complete,
                               asked_model="m", repeat_with_news=True)
    assert len(results) == 6
    assert seen == ["news", "news", "blank", "blank", "news", "news"]
    assert all(p.repeated is not None for p in pairs)


def test_the_repeat_arm_is_off_unless_asked_for():
    def complete(system, user, schema):
        ticker = user.split("TICKER: ", 1)[1].split("\n", 1)[0]
        return json.dumps({"ticker": ticker, "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    pairs, results = na.ablate([entry("AAPL")], complete, asked_model="m")
    assert len(results) == 2 and pairs[0].repeated is None


def test_the_journalled_model_rides_on_the_entry():
    """Without it the report cannot tell a self-comparison from a
    cross-model one, which is the whole failure this guards against."""
    line = json.dumps({
        "ts_utc": "2026-09-12T14:00:00+00:00", "ticker": "AAPL",
        "context": TickerContext(ticker="AAPL", headlines=HEADLINES).as_dict(),
        "signal": {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.7, "rationale": "r"},
        "usage": {"model": "claude-haiku-4-5-20251001"},
    })
    assert next(iter(runner.load_entries([line]))).model == "claude-haiku-4-5-20251001"
    assert entry("AAPL").model is None, "a line with no usage block says so"


def test_main_counts_three_arms_when_repeating(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL") + "\n", encoding="utf-8")
    calls = {"n": 0}

    def complete(system, user, schema):
        calls["n"] += 1
        return json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5, "rationale": "r"})

    monkeypatch.setattr(runner, "measured_completer", lambda **kwargs: (complete, []))
    assert na.main(["--journal", str(journal), "--model", "m", "--repeat-with-news"]) == 0
    assert calls["n"] == 3
    assert "1 context(s) x 3 = 3 calls" in capsys.readouterr().err


# --- a run that mostly failed must say so, over the right denominator ----------


def test_the_failure_rate_counts_the_calls_actually_made():
    """The first gpt-oss dry run printed 'Failure rate: 286/200 calls' --
    the denominator assumed two arms while three had been asked. A rate over
    the wrong denominator is not a rate."""
    pairs = [na.Ablation("AAPL", None, None, None, None) for _ in range(100)]
    summary = na.summarise(pairs, 0.30, failures=286, calls=300,
                           errors=["timed out"] * 286)
    assert summary.calls == 300
    text = na.render(summary, pairs, 0.30, "m")
    assert "286/300 calls" in text
    assert "286/200" not in text


def test_a_run_that_mostly_failed_says_what_failed():
    """Our own timeout and the model giving up are opposite findings: one
    says raise the deadline, the other says pick another model."""
    pairs = [na.Ablation("AAPL", None, None, None, None) for _ in range(10)]
    summary = na.summarise(pairs, 0.30, failures=9, calls=30,
                           errors=["timed out after 120s"] * 8 + ["invalid output: x"])
    kinds = dict(summary.errors)
    assert sum(kinds.values()) == 9
    text = na.render(summary, pairs, 0.30, "m")
    for kind in kinds:
        assert kind in text


def test_the_denominator_falls_back_to_two_arms_when_not_told():
    summary = na.summarise([pair()], 0.30, failures=0)
    assert summary.calls == 2
