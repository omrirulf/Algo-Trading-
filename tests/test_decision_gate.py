"""The decision gate: which lines count, when a look is read, and what it says.

The pre-registration's decision is only as good as the arithmetic that
applies it, so every branch of it is pinned here with numbers small enough
to check by hand.
"""

from __future__ import annotations

import math
from datetime import date

import numpy as np
import pytest

from analysis import decision_gate as gate
from analysis.decision_gate import LookInputs, WatchDay


# --- the bars are the O'Brien-Fleming ones, and they hold the error rate ----------


def test_the_bars_are_obrien_fleming_for_three_equal_looks():
    """2.004 x sqrt(3/k): the classic constant for K = 3 at two-sided 0.05."""
    constant = 2.004
    for k, (independent, bar) in enumerate(gate.CHECKPOINTS, start=1):
        assert independent == 20 * k
        assert bar == pytest.approx(round(constant * math.sqrt(3 / k), 2), abs=1e-9)


def test_the_bars_hold_the_overall_error_rate_at_five_percent():
    """Simulated, because nothing here should be taken on trust: under no
    effect, a statistic read at 1/3, 2/3 and all of the sample crosses one
    of the three bars about 5% of the time. Three looks at 2.0 each would
    cross about 10% of the time, which is the thing the bars exist to stop."""
    rng = np.random.default_rng(20260924)
    steps = rng.standard_normal((600_000, 3)) * math.sqrt(1 / 3)
    z = np.cumsum(steps, axis=1) / np.sqrt(np.array([1 / 3, 2 / 3, 1.0]))
    bars = np.array([bar for _, bar in gate.CHECKPOINTS])
    alpha = float(np.mean(np.any(np.abs(z) > bars, axis=1)))
    naive = float(np.mean(np.any(np.abs(z) > 2.0, axis=1)))
    assert 0.047 < alpha < 0.054
    assert naive > 0.09


# --- counting ------------------------------------------------------------------------


@pytest.mark.parametrize("entry_days, independent", [(0, 0), (2, 0), (3, 1), (59, 19), (60, 20), (180, 60)])
def test_independent_days_are_complete_blocks_of_three(entry_days, independent):
    assert gate.independent_days(entry_days) == independent


def test_the_window_starts_on_the_cutoff_day():
    assert gate.in_window(date(2026, 9, 23))
    assert not gate.in_window(date(2026, 9, 22))


# --- when a look is readable -----------------------------------------------------------


def test_the_registered_look_dates_follow_from_the_calendar():
    """24 Sep is the first entry day (from the 23 Sep cycle); the 24 Sep
    cycle produced no answer, so 25 Sep is lost and every look moves back
    one trading day. These are the dates the pre-registration prints."""
    known = gate.known_entry_days([date(2026, 9, 23)])
    assert known == [date(2026, 9, 24)]
    expected = {20: date(2026, 12, 22), 40: date(2027, 3, 22), 60: date(2027, 6, 16)}
    for independent, when in expected.items():
        assert gate.estimated_readable(gate.entry_days_needed(independent), known,
                                       last_cycle_day=date(2026, 9, 24)) == when


def test_with_no_lost_day_every_look_is_one_day_earlier():
    known = gate.known_entry_days([date(2026, 9, 23), date(2026, 9, 24)])
    assert gate.estimated_readable(60, known, last_cycle_day=date(2026, 9, 24)) == date(2026, 12, 21)
    # Not knowing the last cycle day, a lost day cannot be seen either.
    assert gate.estimated_readable(60, [date(2026, 9, 24)]) == date(2026, 12, 21)


def test_a_look_inside_the_known_days_reads_them():
    known = [date(2026, 9, 24), date(2026, 9, 28), date(2026, 9, 29)]
    # The 3rd entry day is 29 Sep; its trades close two sessions later.
    assert gate.estimated_readable(3, known) == date(2026, 10, 1)


def test_trading_days_skip_weekends_and_holidays():
    assert gate.next_trading_day(date(2026, 11, 25)) == date(2026, 11, 27)  # Thanksgiving
    assert gate.next_trading_day(date(2026, 9, 25)) == date(2026, 9, 28)   # a Friday
    assert gate.trading_days_after(date(2026, 9, 24), 0) == date(2026, 9, 24)


# --- one look ----------------------------------------------------------------------------


def inputs(mm=0.0, mh=0.0, hm=0.0, mean=0.001, band=0.0005, **vs):
    t_vs = {"model": 0.0, "momentum": 0.0, "hybrid": 0.0}
    t_vs.update(vs)
    return LookInputs(entry_days=60, t_model_momentum=mm, t_model_hybrid=mh, t_hybrid_momentum=hm,
                      model_mean=mean, model_band_high=band, t_vs_index=t_vs)


def test_the_model_is_kept_only_if_it_also_beats_the_index():
    assert gate.decide(inputs(mm=3.0, mh=2.5, model=2.1), 2.0, final=True)[:2] == ("model", "model")
    candidate, outcome, reason = gate.decide(inputs(mm=3.0, mh=2.5, model=1.9), 2.0, final=True)
    assert (candidate, outcome) == ("model", gate.NO_ARM)
    assert "did not beat VT" in reason


def test_the_coin_flip_condition_still_has_to_hold():
    kept = gate.decide(inputs(mm=3.0, mh=3.0, mean=0.001, band=0.002, momentum=2.5), 2.0, final=True)
    assert kept[0] == "momentum"


def test_at_the_final_look_the_replacement_is_momentum_unless_the_hybrid_beat_it():
    assert gate.decide(inputs(momentum=2.5), 2.0, final=True)[:2] == ("momentum", "momentum")
    assert gate.decide(inputs(hm=2.1, hybrid=2.5), 2.0, final=True)[:2] == ("hybrid", "hybrid")
    assert gate.decide(inputs(hm=2.1, hybrid=1.0), 2.0, final=True)[:2] == ("hybrid", gate.NO_ARM)


def test_an_early_look_decides_nothing_unless_its_bar_is_met():
    candidate, outcome, reason = gate.decide(inputs(mm=3.0, mh=3.0, model=5.0), 3.47, final=False)
    assert (candidate, outcome) == (None, None)
    assert "no early stop" in reason


def test_an_early_stop_for_the_model():
    assert gate.decide(inputs(mm=3.6, mh=3.5, model=3.5), 3.47, final=False)[:2] == ("model", "model")


def test_an_early_stop_against_the_model_needs_it_worse_than_the_replacement():
    assert gate.decide(inputs(mm=-3.6, momentum=3.6), 3.47, final=False)[:2] == ("momentum", "momentum")
    # Worse than momentum, but the hybrid beat momentum, so the question is
    # the model against the hybrid -- and that one does not clear the bar.
    assert gate.decide(inputs(mm=-3.6, mh=-1.0, hm=3.5), 3.47, final=False)[:2] == (None, None)


def test_an_early_index_decision_needs_its_bar_met_in_that_direction():
    # The model is clearly better than both, but not clearly better or worse than VT.
    candidate, outcome, reason = gate.decide(inputs(mm=3.6, mh=3.6, model=1.0), 3.47, final=False)
    assert (candidate, outcome) == ("model", None)
    assert "decides nothing" in reason
    # Clearly worse than VT: no arm trades, and that is a decision.
    assert gate.decide(inputs(mm=3.6, mh=3.6, model=-3.6), 3.47, final=False)[:2] == ("model", gate.NO_ARM)


def test_a_missing_t_never_clears_a_bar():
    empty = LookInputs(entry_days=60, t_model_momentum=None, t_model_hybrid=None,
                       t_hybrid_momentum=None, model_mean=None, model_band_high=None)
    assert gate.decide(empty, 2.0, final=True)[:2] == ("momentum", gate.NO_ARM)
    assert gate.decide(empty, 3.47, final=False)[:2] == (None, None)


def test_the_first_look_that_decides_is_the_answer():
    looks = gate.evaluate({
        20: inputs(mm=3.6, mh=3.6, model=3.6),
        40: inputs(momentum=9.0),
    })
    assert [look.decided for look in looks] == [True, False, False]
    assert gate.first_decision(looks).independent == 20
    assert gate.next_look(looks).independent == 60


def test_the_header_line_is_the_owners_words_until_a_decision():
    looks = gate.evaluate({})
    assert gate.status_line(7, looks) == (
        "independent days since 2026-09-23: 7 of 60 (= 180 trading days) — NO DECISION YET"
    )
    decided = gate.evaluate({20: inputs(mm=3.6, mh=3.6, model=3.6)})
    assert gate.status_line(20, decided).endswith("EARLY STOP AT 20: KEEP THE MODEL")
    final = gate.evaluate({20: inputs(), 40: inputs(), 60: inputs(momentum=1.0)})
    assert gate.status_line(61, final) == (
        "independent days since 2026-09-23: 60 of 60 (= 180 trading days) — FINAL: "
        + gate.OUTCOME_TEXT[gate.NO_ARM].upper()
    )


# --- the index's own window ----------------------------------------------------------------


BARS = [
    (date(2026, 9, 24), 100.0, 101.0, 0.0),
    (date(2026, 9, 25), 101.0, 102.0, 0.5),   # ex-dividend inside the window
    (date(2026, 9, 28), 102.0, 103.0, 0.0),
    (date(2026, 9, 29), 103.0, 104.0, 0.0),
]


def test_the_index_window_is_open_to_close_with_the_dividend_added_back():
    assert gate.index_window_return(BARS, date(2026, 9, 24), 3) == pytest.approx((103.0 + 0.5) / 100.0 - 1)


def test_a_dividend_ex_on_the_entry_day_is_not_added():
    assert gate.index_window_return(BARS, date(2026, 9, 25), 3) == pytest.approx(104.0 / 101.0 - 1)


def test_an_unfinished_or_unpriced_window_is_none():
    assert gate.index_window_return(BARS, date(2026, 9, 28), 3) is None
    assert gate.index_window_return(BARS, date(2026, 9, 30), 3) is None


# --- the owner's model-watch triggers -----------------------------------------------------


def day(d, asked=60, failed=0, shorts=1, setup=0):
    return WatchDay(day=d, asked=asked, failed=failed, shorts=shorts, setup_failed=setup)


DAYS = [date(2026, 10, d) for d in (1, 2, 5, 6, 7, 8, 9)]


def test_failures_above_five_percent_over_five_days_trip():
    days = [day(d) for d in DAYS[:5]]
    assert gate.failure_trips(days) == []
    days[2] = day(DAYS[2], failed=16)  # 16 of 300 = 5.3%
    (trip,) = gate.failure_trips(days)
    assert (trip.first, trip.last) == (DAYS[0], DAYS[4])
    days[2] = day(DAYS[2], failed=15)  # exactly 5% is not above it
    assert gate.failure_trips(days) == []


def test_fewer_than_five_days_are_never_judged():
    assert gate.failure_trips([day(DAYS[0], failed=60)]) == []


def test_five_days_without_a_short_trip_only_when_spy_fell():
    days = [day(d, shorts=0) for d in DAYS[:5]]
    falling = {date(2026, 9, 30): 500.0, DAYS[4]: 490.0}
    rising = {date(2026, 9, 30): 500.0, DAYS[4]: 510.0}
    assert len(gate.no_short_trips(days, falling)) == 1
    assert gate.no_short_trips(days, rising) == []
    days[3] = day(DAYS[3], shorts=1)
    assert gate.no_short_trips(days, falling) == []


def test_a_lost_day_neither_extends_nor_breaks_a_no_short_run():
    days = [day(d, shorts=0) for d in DAYS[:3]] + [day(DAYS[3], failed=60, shorts=0)] + \
           [day(d, shorts=0) for d in DAYS[4:6]]
    falling = {date(2026, 9, 30): 500.0, DAYS[5]: 480.0}
    (trip,) = gate.no_short_trips(days, falling)
    assert (trip.first, trip.last) == (DAYS[0], DAYS[5])


def test_a_run_whose_last_close_is_not_final_is_not_judged():
    days = [day(d, shorts=0) for d in DAYS[:5]]
    assert gate.no_short_trips(days, {date(2026, 9, 30): 500.0}) == []


# --- a look that cannot be read decides nothing ----------------------------------


def test_an_unpriced_index_is_never_read_as_a_result():
    """A VT outage on the night of the final look must not become 'no arm trades'."""
    from dataclasses import replace

    kept = inputs(mm=3.0, mh=2.6, model=2.4)
    assert gate.decide(kept, 2.0, final=True)[1] == "model"
    outage = replace(kept, index_missing=3)
    candidate, outcome, reason = gate.decide(outage, 2.0, final=True)
    assert (candidate, outcome) == (None, None)
    assert "cannot be read tonight" in reason and "VT" in reason


def test_a_missing_index_bar_waits_while_recent_and_is_left_out_once_settled():
    """The price source had no VT bar for 22 Sep 2026 while it had SPY's. A
    missing day is an outage -- the look waits -- until the source has
    printed five later sessions without it; then it is a gap that will not
    be filled, and waiting for it would hold every look unreadable for good."""
    assert gate.INDEX_GAP_SETTLE_SESSIONS == 5
    days = [date(2026, 9, 21), date(2026, 9, 22), date(2026, 9, 23), date(2026, 9, 24), date(2026, 9, 25),
            date(2026, 9, 28), date(2026, 9, 29), date(2026, 9, 30)]
    bar = lambda d: (d, 100.0, 101.0, 0.0)
    four_after = [bar(d) for d in days[:6] if d != days[1]]            # 23..28 Sep: four later bars
    assert gate.index_gaps(four_after, days[:3]) == set()
    five_after = [bar(d) for d in days[:7] if d != days[1]]            # 23..29 Sep: five
    assert gate.index_gaps(five_after, days[:3]) == {days[1]}
    assert gate.index_gaps(five_after, days[5:7]) == set()             # days it has are no gap

    from dataclasses import replace

    kept = inputs(mm=3.0, mh=2.6, model=2.4)
    settled = replace(kept, index_gaps=1)
    assert gate.decide(settled, 2.0, final=True)[1] == "model"


def test_a_look_with_missing_prices_waits_for_them():
    from dataclasses import replace

    missing = replace(inputs(mm=3.6, mh=3.6, model=3.6), unreadable="no final prices for NVDA")
    looks = gate.evaluate({20: missing})
    assert not looks[0].decided and "no final prices for NVDA" in looks[0].reason
    assert gate.status_line(20, looks).endswith("NO DECISION YET")


def test_after_a_decision_later_looks_are_shown_but_decide_nothing():
    looks = gate.evaluate({20: inputs(mm=3.6, mh=3.6, model=3.6), 40: inputs(momentum=9.0),
                           60: inputs(momentum=9.0)})
    assert [look.outcome for look in looks] == ["model", None, None]
    assert all("already decided at the 20-day look" in look.reason for look in looks[1:])
    assert gate.first_decision(looks).independent == 20


def test_trigger_c_trips_early_when_the_outcome_is_already_certain():
    """Two days with 61 model errors in 123 calls: any 5-day window holding
    them can ask at most 123 + 3 x 80 names, and 5% of that is 18."""
    first, second = date(2026, 9, 28), date(2026, 9, 29)
    days = [day(first, asked=65, failed=3), day(second, asked=58, failed=58)]
    assert gate.failure_trips(days) == []            # without a ceiling it waits
    (trip,) = gate.failure_trips(days, max_names_per_day=80)
    assert (trip.first, trip.last) == (first, second)
    calm = [day(first, asked=65, failed=3)]
    assert gate.failure_trips(calm, max_names_per_day=80) == []


def test_trigger_c_counts_model_errors_only_and_from_25_september():
    """The owner's decision of 24 Sep 2026: the 23-24 Sep failures were a key
    problem, not the model. Setup errors are shown, never counted, and the
    count restarts on 25 Sep."""
    assert gate.FAILURE_WATCH_START == date(2026, 9, 25)
    assert gate.RUN_ALERT_FAILED_SHARE == 0.20
    outage = [day(date(2026, 9, 23), asked=65, failed=3), day(date(2026, 9, 24), asked=58, setup=58)]
    assert gate.failure_trips(outage, max_names_per_day=80) == []
    # The same 58 setup errors after the restart still count for nothing.
    later = [day(d, asked=60, setup=58 if i == 0 else 0) for i, d in enumerate(DAYS[:5])]
    assert gate.failure_trips(later, max_names_per_day=80) == []
    # 16 model errors of the 242 calls that reached the model is 6.6%: tripped.
    later[1] = day(DAYS[1], failed=16)
    (trip,) = gate.failure_trips(later, max_names_per_day=80)
    assert "16 of 242" in trip.detail
