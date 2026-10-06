"""The voting arm ``model_vote`` in the funds and the race: its signal, its comparator, its race arm.

Pre-registration section 13.11 (the owner's instruction of 4 Oct 2026,
item 1; registered at the 2026-12-22 checkpoint). The vote is evaluated
twice, with the machinery the model arm already has:

* **The fund** (``vote_signal``): the model fund's own books, engine,
  manager, costs and rules, with the vote's answer on each line in place
  of the single call's. A line the vote has no answer for (fewer than 3
  of the 5 votes succeeded, or no vote line at all) is not dispatched.
* **The comparator fund** (``comparator_signal``): the model's single call
  on exactly the same lines -- the journal's own answer, dispatched only
  where the vote has an answer. So the two funds differ in one thing only,
  and the four registered funds are untouched.
* **The race arm** (``race``): the vote's answers against the model's on
  the same lines, scored as the race scores every arm, and the daily
  difference read with a Newey-West t at the race's horizon (lag 3).

The main metric is the mean daily net return, vote minus model. "Acting
differently" (section 13.7) is a line where the two signals differ after
the conviction floor (``analysis.vote.acted_differently``); fewer than 20
by the final checkpoint and the idea is "not tested".

Nothing here is computed before ``config.model_vote.START``: the funds
program builds these only on a checkpoint night from that date
(``analysis.vote.due``), and the answers themselves exist only from it.
Simulation only, like every shadow fund: CI keeps ``shadow/`` from a
broker, a key and a file write.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Mapping, Optional, Sequence

from analysis.reader import JournalEntry
from analysis.vote import Answer, Key, acted_differently, key_of
from app.schemas import Bias, LLMSignal
from config import model_vote as mv
from config import settings as cfg
from shadow.fund import Line, SignalFor, model_signal


def _answer_for(found: Mapping[Key, Answer], entry: JournalEntry) -> Optional[Answer]:
    key = key_of(entry)
    return found.get(key) if key is not None else None


def vote_signal(found: Mapping[Key, Answer]) -> SignalFor:
    """The vote fund's signal maker: each line's vote answer, bias and conviction only; None without one."""

    def signal(line: Line) -> Optional[LLMSignal]:
        answer = _answer_for(found, line.entry)
        if answer is None:
            return None
        try:
            return LLMSignal(ticker=line.entry.ticker, bias=Bias(answer.bias), conviction=float(answer.conviction),
                             rationale="vote")
        except (ValueError, TypeError):
            return None

    return signal


def comparator_signal(found: Mapping[Key, Answer]) -> SignalFor:
    """The comparator fund's signal maker: the model's single call, only on the lines the vote answered."""

    def signal(line: Line) -> Optional[LLMSignal]:
        if _answer_for(found, line.entry) is None:
            return None
        return model_signal(line)

    return signal


def lines_with_an_answer(lines: Sequence[JournalEntry], found: Mapping[Key, Answer]) -> list[JournalEntry]:
    """The answered production lines from ``START`` that have a vote answer: the lines both arms are raced on."""
    return [e for e in lines
            if e.timestamp is not None and e.model_answered and not e.held
            and e.timestamp.date() >= mv.START and _answer_for(found, e) is not None]


def acted(lines: Sequence[JournalEntry], found: Mapping[Key, Answer]) -> int:
    """Section 13.7 for the vote: lines where its signal and the single call's differ, after production's floor."""
    return acted_differently(lines, found, cfg.MIN_CONVICTION)


def race(lines: Sequence[JournalEntry], found: Mapping[Key, Answer], how) -> dict:
    """The vote's race arm against the model's single call on the same lines (section 13.11).

    ``lines`` are the race's answered lines; ``found`` the vote's answers
    (``analysis.vote.answers``); ``how`` the race's own settings
    (``shadow.exploratory.race_settings``). The vote's entries are the
    lines with the vote's side and conviction in place of the model's,
    every other field as journalled, so the scorer joins both arms to
    exactly the same forward return. Each arm is scored as the race scores
    every arm (``shadow.exploratory.arm_trades``); the daily difference,
    vote minus model, on the entry days either traded (no trade is 0), is
    read with a Newey-West t at lag ``how.horizon`` (3).
    """
    from analysis.horse_race import daily_net, entries_for_arm, on_grid
    from shadow import exploratory as xp

    kept = lines_with_an_answer(lines, found)
    voted = []
    for e in kept:
        answer = _answer_for(found, e)
        voted.append(replace(e, bias=answer.bias, conviction=answer.conviction, scores={}, blend={}))
    vote_trades = xp.arm_trades(mv.ARM, voted, how)
    model_trades = xp.arm_trades("model", entries_for_arm("model", kept), how)
    grid = sorted(set(daily_net(vote_trades)) | set(daily_net(model_trades)))
    diffs = [a - b for a, b in zip(on_grid(daily_net(vote_trades), grid), on_grid(daily_net(model_trades), grid))]
    return xp._test(diffs, how.horizon) | {"compare_to": "model", "trades": len(vote_trades),
                                           "model_trades": len(model_trades), "lines": len(kept),
                                           "acted": acted(kept, found)}


__all__ = ["acted", "comparator_signal", "lines_with_an_answer", "race", "vote_signal"]
