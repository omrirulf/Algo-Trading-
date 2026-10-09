"""TEST DATA: one printed example of each checkpoint-verdict table (the owner's Addition 2, 6 Oct 2026).

    python tests/verdict_examples.py        # from the repo root; prints plain text

The owner approved the verdict layout on 6 Oct 2026 and asked: "before the
verdict build is merged, show me one printed example of each table made
from test data, clearly marked "TEST DATA". A test must fail if any example
value can appear in a real output."

Every number here is made up. Every example table is built with
``test_data=True``, so every line it renders starts with "TEST DATA" and
``analysis.verdict.table_json`` / ``render_real`` / ``block`` refuse it;
every date is in the year 2099, which the real builders refuse
(``analysis.verdict.check_dates``). ``tests/test_verdict_examples.py``
holds the guards. Test-only: nothing outside ``tests/`` may import this
module (a guard checks that too).

The six examples: (1) the race at a checkpoint (an early stop for momentum,
not tested in a downturn); (2) the fund test at the same checkpoint (no
decision); (3) the combined line; (4) the block before the first checkpoint;
(5) the fund test's SKIPPED block; (6) the race at the final look.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import decision_gate as gate  # noqa: E402
from analysis import verdict  # noqa: E402

HEADER = "TEST DATA — every number below is made up. None is a result."
MARK = f"{verdict.TEST_DATA} · "

#: The made-up calendar, all in 2099 so an example is recognisable anywhere:
#: the race window opens, the funds start, calibration passes, and the three
#: looks fall.
RACE_START = date(2099, 3, 23)
FUND_START = date(2099, 3, 29)
CALIBRATION_PASSED = date(2099, 4, 19)
LOOK_DAYS = (date(2099, 6, 22), date(2099, 9, 22), date(2099, 12, 16))
MADE_ON = date(2099, 6, 23)


def race_early_stop() -> verdict.Table:
    """(1) Checkpoint 1: momentum, by an early stop, not tested in a downturn."""
    inputs = gate.LookInputs(
        entry_days=60, t_model_momentum=-3.62, t_model_hybrid=-1.05, t_hybrid_momentum=0.84,
        model_mean=0.00012, model_band_high=0.00071, t_vs_index={"model": -0.42, "momentum": 3.55, "hybrid": 1.30},
        index_days=60, vt_max_drawdown=0.041, window_end=LOOK_DAYS[0],
        after_tax=gate.AfterTax(gate.AFTER_TAX_READY, {"model": -0.80, "momentum": 3.52, "hybrid": 1.10},
                                window_end=LOOK_DAYS[0], window=(FUND_START, LOOK_DAYS[0]), lag=5),
    )
    look = gate.evaluate({20: inputs})[0]
    return verdict.race_table(look, 1, window_start=RACE_START, next_look=(2, LOOK_DAYS[1], 2.45),
                              test_data=True)


def fund_record_no_decision() -> dict:
    """The fund test's look record at checkpoint 1, read, deciding nothing (made-up numbers)."""
    days = {"days": 60, "from": FUND_START.isoformat(), "through": LOOK_DAYS[0].isoformat(), "lag": 5}
    ts = {"model-momentum": -2.31, "model-hybrid": -0.40, "hybrid-momentum": -1.90,
          "model-vt": -0.70, "momentum-vt": 1.12, "hybrid-vt": 0.35}
    return {
        "look": 1, "made_on": MADE_ON.isoformat(), "window_end": LOOK_DAYS[0].isoformat(), "status": "read",
        "start": FUND_START.isoformat(), "sessions": 60, "sessions_calendar": 60, "share": 60 / 180,
        "bar": 3.40, "bar_exact": 3.395, "planned_bar": 3.40, "bar_differs": False,
        "calibration_passed_on": CALIBRATION_PASSED.isoformat(),
        "tests": {pair: {**days, "t": t, "mean_daily_diff": 0.0001} for pair, t in ts.items()},
        "coin_flip": {"model_total": 0.039, "p95_total": 0.027, "funds": 1000},
        "after_tax": {"status": gate.AFTER_TAX_READY, "t": {"model": -0.80, "momentum": 3.52, "hybrid": 1.10}},
        "downturn": 0.041,
    }


def fund_no_decision() -> verdict.Table:
    """(2) The fund test at the same checkpoint: no decision."""
    return verdict.fund_test_table(fund_record_no_decision(), planned_next=(2, LOOK_DAYS[1], 2.41),
                                   test_data=True)


def combined_line() -> dict:
    """(3) The combined line on that night: the race has decided, the fund test has not."""
    race = {"decided_at": 1, "outcome": "momentum", "final_read": False, "skipped_all": False, "look": 1,
            "window_end": LOOK_DAYS[0].isoformat(), "next": None}
    fund = {"decided_at": None, "outcome": None, "final_read": False, "skipped_all": False, "look": 1,
            "window_end": LOOK_DAYS[0].isoformat(), "next": {"look": 2, "estimated": LOOK_DAYS[1].isoformat()}}
    return verdict.combined(race, fund, test_data=True)


def fund_skipped() -> verdict.Table:
    """(5) The fund test's checkpoint 1, skipped: calibration had not passed."""
    record = {"look": 1, "made_on": MADE_ON.isoformat(), "window_end": LOOK_DAYS[0].isoformat(),
              "status": verdict.FUND_SKIPPED, "reason": verdict.FUND_SKIP_REASON}
    return verdict.fund_test_table(record, test_data=True)


def race_final() -> verdict.Table:
    """(6) The final look: the hybrid, tested in a downturn; row 6 does not apply."""
    inputs = gate.LookInputs(
        entry_days=180, t_model_momentum=-1.20, t_model_hybrid=-2.60, t_hybrid_momentum=2.31,
        model_mean=0.00020, model_band_high=0.00064, t_vs_index={"model": -0.90, "momentum": 1.40, "hybrid": 2.44},
        index_days=180, vt_max_drawdown=0.124, window_end=LOOK_DAYS[2],
        after_tax=gate.AfterTax(gate.AFTER_TAX_READY, {"model": -1.00, "momentum": 1.20, "hybrid": 2.19},
                                window_end=LOOK_DAYS[2], window=(FUND_START, LOOK_DAYS[2]), lag=5),
    )
    look = gate.Look(60, 2.00, True, inputs)
    return verdict.race_table(look, 3, window_start=RACE_START, test_data=True)


def tables() -> list[verdict.Table]:
    """Every example table, all made with ``test_data=True``."""
    return [race_early_stop(), fund_no_decision(), fund_skipped(), race_final()]


def printout() -> list[str]:
    """The whole printout, line by line: every line that is not blank carries "TEST DATA"."""
    line = combined_line()
    sections = [
        ("Example 1 of 6: the race at a checkpoint", verdict.render(race_early_stop())),
        ("Example 2 of 6: the fund test at the same checkpoint", verdict.render(fund_no_decision())),
        ("Example 3 of 6: the combined line", [MARK + line["line"], MARK + line["note"]]),
        ("Example 4 of 6: before the first checkpoint",
         [MARK + text for text in verdict.block() if text]),
        ("Example 5 of 6: the fund test's checkpoint, skipped", verdict.render(fund_skipped())),
        ("Example 6 of 6: the race at the final look", verdict.render(race_final())),
    ]
    out = [HEADER]
    for title, lines in sections:
        out += ["", MARK + title, *lines]
    return out


def main() -> int:
    print("\n".join(printout()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
