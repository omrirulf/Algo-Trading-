#!/usr/bin/env python3
"""Two tests that need no market outcomes, and could make the live run moot.

    python replay/signal_sanity.py plan > trials.json        # ~3 prompts per ticker
    python replay/signal_sanity.py submit --trials trials.json > batch_id
    python replay/signal_sanity.py collect --trials trials.json --batch $(cat batch_id)

The live experiment's bottleneck is calendar time: a signal needs 5-20
trading days before it can be scored. These two questions need none, and
together they bound what any later scoring could possibly find:

1. THE NULL TEST -- does the answer depend on the evidence?
   Each ticker is asked twice on real context and once on *scrambled*
   context: its own ``TICKER:`` label above another ticker's entire evidence
   (same instrument kind, so an ETF still gets the ETF prompt). If the answer
   survives having all of its evidence replaced, the model is pattern-
   completing a plausible analyst rather than reading anything. That is
   theater, and no amount of live trading rescues it.

2. SELF-CONSISTENCY -- does the model agree with itself?
   Identical context, asked twice. Whatever agreement rate comes back is a
   ceiling on any edge: a model that disagrees with itself one time in three
   on the same input is one-third noise before the market gets a say.

Both are chance-corrected. A model that answers NEUTRAL 70% of the time agrees
with anything 50% of the time by base rate alone, so raw agreement flatters it;
Cohen's kappa does not.

The verdict thresholds are constants at the top of this file, fixed before the
first call was ever made. Moving them after seeing a result is the thing this
test exists to prevent.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.schemas import Bias, LLMSignal  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import kind_for  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from orchestrator.context import TickerContext  # noqa: E402
from orchestrator.llm import BatchRequest, Completion, LLMError, batch_custom_id  # noqa: E402
from orchestrator.pricing import Usage  # noqa: E402

# --------------------------------------------------------------------------- #
# Pre-registered thresholds. Set before any call; not to be moved afterwards.
# --------------------------------------------------------------------------- #

#: Below this share of real signals clearing the conviction floor there is
#: nothing to test and nothing to trade: the model never takes a side.
SILENT_TRADE_RATE = 0.10

#: Below this bias agreement on identical input the model is arguing with
#: itself, and that disagreement caps any edge before a market is consulted.
NOISE_SELF_AGREEMENT = 0.70

#: Above this chance-corrected agreement between the real answer and the
#: scrambled one, the evidence is not what produced the answer.
THEATER_SCRAMBLE_KAPPA = 0.40


@dataclass(frozen=True)
class Verdicts:
    silent: bool
    noise: bool
    theater: bool

    @property
    def passed(self) -> bool:
        return not (self.silent or self.noise or self.theater)

    def as_list(self) -> list[str]:
        out = []
        if self.silent:
            out.append("SILENT")
        if self.noise:
            out.append("NOISE")
        if self.theater:
            out.append("THEATER")
        return out or ["PASS"]


# --------------------------------------------------------------------------- #
# Conditions
# --------------------------------------------------------------------------- #

REAL, REPEAT, SCRAMBLED = "real", "repeat", "scrambled"


@dataclass
class Trial:
    ticker: str
    condition: str
    system_prompt: str
    user_prompt: str
    donor: Optional[str] = None
    signal: Optional[LLMSignal] = None
    usage: Optional[Usage] = None
    error: Optional[str] = None

    @property
    def custom_id(self) -> str:
        return batch_custom_id(self.ticker, self.condition)


def trades(signal: Optional[LLMSignal]) -> bool:
    """Would the engine act on this? Bias plus the conviction floor."""
    return (
        signal is not None
        and signal.bias is not Bias.NEUTRAL
        and signal.conviction >= cfg.MIN_CONVICTION
    )


def scramble_prompt(target: str, donor_prompt: str, donor: str) -> str:
    """The donor's whole evidence block under the target's label.

    A plain string swap on the first line, so the scrambled prompt is
    byte-for-byte the donor's except for the ticker the model is told it is
    looking at. Anything in the headlines that names the donor is left in:
    a model that notices the mismatch and says NEUTRAL is behaving well, and
    that shows up as a higher NEUTRAL rate under scrambling.
    """
    head = f"TICKER: {donor}"
    if not donor_prompt.startswith(head):
        raise ValueError(f"donor prompt for {donor} does not start with its label")
    return f"TICKER: {target}" + donor_prompt[len(head):]


def derange(items: list[str]) -> dict[str, str]:
    """Each item mapped to a different item: a rotation by one.

    Within an instrument kind only, so the scrambled prompt is still the
    shape the system prompt expects. A group of one cannot be deranged and
    is left out of the scrambled condition.
    """
    if len(items) < 2:
        return {}
    return {items[i]: items[(i + 1) % len(items)] for i in range(len(items))}


def build_trials(
    contexts: dict[str, TickerContext],
    system_prompt_for: Callable[[str], str],
    build_user_prompt: Callable[[TickerContext], str],
) -> list[Trial]:
    prompts = {t: build_user_prompt(ctx) for t, ctx in contexts.items()}
    trials: list[Trial] = []
    for ticker in contexts:
        sp = system_prompt_for(ticker)
        trials.append(Trial(ticker, REAL, sp, prompts[ticker]))
        trials.append(Trial(ticker, REPEAT, sp, prompts[ticker]))

    by_kind: dict[str, list[str]] = {}
    for ticker in contexts:
        by_kind.setdefault(kind_for(ticker).value, []).append(ticker)
    for group in by_kind.values():
        for target, donor in derange(sorted(group)).items():
            trials.append(
                Trial(
                    target,
                    SCRAMBLED,
                    system_prompt_for(target),
                    scramble_prompt(target, prompts[donor], donor),
                    donor=donor,
                )
            )
    return trials


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #

def kappa(pairs: list[tuple[str, str]]) -> Optional[float]:
    """Cohen's kappa over paired categorical answers.

    Chance agreement is the sum over categories of p_a(c) * p_b(c); kappa
    reports how far above that the observed agreement sits. Returns None when
    chance agreement is 1.0 (every answer in both columns identical), where
    kappa is undefined -- that case is reported separately as SILENT.
    """
    if not pairs:
        return None
    n = len(pairs)
    observed = sum(1 for a, b in pairs if a == b) / n
    a_dist = Counter(a for a, _ in pairs)
    b_dist = Counter(b for _, b in pairs)
    expected = sum((a_dist[c] / n) * (b_dist[c] / n) for c in set(a_dist) | set(b_dist))
    if expected >= 1.0 - 1e-12:
        return None
    return (observed - expected) / (1.0 - expected)


@dataclass
class Report:
    tickers: int
    real: dict[str, Trial]
    repeat: dict[str, Trial]
    scrambled: dict[str, Trial]
    failed: list[Trial] = field(default_factory=list)

    # --- pairs -------------------------------------------------------------- #
    def _pairs(self, a: dict[str, Trial], b: dict[str, Trial]) -> list[tuple[str, str]]:
        return [
            (a[t].signal.bias.value, b[t].signal.bias.value)
            for t in a
            if t in b and a[t].signal is not None and b[t].signal is not None
        ]

    @property
    def self_pairs(self) -> list[tuple[str, str]]:
        return self._pairs(self.real, self.repeat)

    @property
    def scramble_pairs(self) -> list[tuple[str, str]]:
        return self._pairs(self.real, self.scrambled)

    # --- metrics ------------------------------------------------------------ #
    @staticmethod
    def _rate(pairs: list[tuple[str, str]]) -> Optional[float]:
        return None if not pairs else sum(1 for a, b in pairs if a == b) / len(pairs)

    @property
    def self_agreement(self) -> Optional[float]:
        return self._rate(self.self_pairs)

    @property
    def self_kappa(self) -> Optional[float]:
        return kappa(self.self_pairs)

    @property
    def scramble_agreement(self) -> Optional[float]:
        return self._rate(self.scramble_pairs)

    @property
    def scramble_kappa(self) -> Optional[float]:
        return kappa(self.scramble_pairs)

    def _signals(self, trials: dict[str, Trial]) -> list[LLMSignal]:
        return [t.signal for t in trials.values() if t.signal is not None]

    def trade_rate(self, condition: dict[str, Trial]) -> Optional[float]:
        sigs = self._signals(condition)
        return None if not sigs else sum(1 for s in sigs if trades(s)) / len(sigs)

    def neutral_rate(self, condition: dict[str, Trial]) -> Optional[float]:
        sigs = self._signals(condition)
        return None if not sigs else sum(1 for s in sigs if s.bias is Bias.NEUTRAL) / len(sigs)

    def mean_conviction_when_sided(self, condition: dict[str, Trial]) -> Optional[float]:
        sided = [s.conviction for s in self._signals(condition) if s.bias is not Bias.NEUTRAL]
        return None if not sided else statistics.fmean(sided)

    @property
    def self_trade_agreement(self) -> Optional[float]:
        """Do the two real runs agree on whether the engine would *act*?"""
        pairs = [
            (trades(self.real[t].signal), trades(self.repeat[t].signal))
            for t in self.real
            if t in self.repeat and self.real[t].signal and self.repeat[t].signal
        ]
        return None if not pairs else sum(1 for a, b in pairs if a == b) / len(pairs)

    @property
    def cost_usd(self) -> float:
        total = 0.0
        for cond in (self.real, self.repeat, self.scrambled):
            for t in cond.values():
                if t.usage and t.usage.cost_usd:
                    total += t.usage.cost_usd
        return total

    # --- verdict ------------------------------------------------------------ #
    @property
    def verdicts(self) -> Verdicts:
        tr = self.trade_rate(self.real)
        sa = self.self_agreement
        sk = self.scramble_kappa
        return Verdicts(
            silent=tr is not None and tr < SILENT_TRADE_RATE,
            noise=sa is not None and sa < NOISE_SELF_AGREEMENT,
            theater=sk is not None and sk > THEATER_SCRAMBLE_KAPPA,
        )

    def as_dict(self) -> dict:
        return {
            "tickers": self.tickers,
            "answered": {"real": len(self.real), "repeat": len(self.repeat),
                         "scrambled": len(self.scrambled)},
            "failed": [{"id": t.custom_id, "error": t.error} for t in self.failed],
            "self_agreement": self.self_agreement,
            "self_kappa": self.self_kappa,
            "self_trade_agreement": self.self_trade_agreement,
            "scramble_agreement": self.scramble_agreement,
            "scramble_kappa": self.scramble_kappa,
            "trade_rate_real": self.trade_rate(self.real),
            "neutral_rate_real": self.neutral_rate(self.real),
            "neutral_rate_scrambled": self.neutral_rate(self.scrambled),
            "conviction_when_sided_real": self.mean_conviction_when_sided(self.real),
            "conviction_when_sided_scrambled": self.mean_conviction_when_sided(self.scrambled),
            "cost_usd": round(self.cost_usd, 4),
            "thresholds": {
                "silent_trade_rate": SILENT_TRADE_RATE,
                "noise_self_agreement": NOISE_SELF_AGREEMENT,
                "theater_scramble_kappa": THEATER_SCRAMBLE_KAPPA,
            },
            "verdicts": self.verdicts.as_list(),
            "passed": self.verdicts.passed,
        }


def _pct(v: Optional[float]) -> str:
    return "--" if v is None else f"{v:.0%}"


def _num(v: Optional[float]) -> str:
    return "--" if v is None else f"{v:.2f}"


def render(r: Report) -> str:
    v = r.verdicts
    lines = [
        "SIGNAL SANITY",
        "",
        f"{r.tickers} tickers · answered real {len(r.real)}, repeat {len(r.repeat)}, "
        f"scrambled {len(r.scrambled)} · failed {len(r.failed)} · ${r.cost_usd:.2f}",
        "",
        "SELF-CONSISTENCY  (same context, asked twice)",
        f"  bias agreement          {_pct(r.self_agreement):>6}   kappa {_num(r.self_kappa)}",
        f"  trade/no-trade agreement{_pct(r.self_trade_agreement):>6}",
        "",
        "NULL TEST  (own label, another ticker's entire evidence)",
        f"  bias agreement          {_pct(r.scramble_agreement):>6}   kappa {_num(r.scramble_kappa)}   <- want low",
        f"  NEUTRAL rate  real {_pct(r.neutral_rate(r.real)):>5}   scrambled {_pct(r.neutral_rate(r.scrambled)):>5}   <- want scrambled higher",
        f"  conviction when sided  real {_num(r.mean_conviction_when_sided(r.real))}   "
        f"scrambled {_num(r.mean_conviction_when_sided(r.scrambled))}   <- want scrambled lower",
        "",
        "ACTIVITY",
        f"  real signals clearing the {cfg.MIN_CONVICTION:.2f} floor: {_pct(r.trade_rate(r.real))}",
        "",
        f"VERDICT: {' + '.join(v.as_list())}",
    ]
    if v.silent:
        lines.append(f"  SILENT  - under {SILENT_TRADE_RATE:.0%} of real signals would trade. Nothing to test.")
    if v.noise:
        lines.append(f"  NOISE   - self-agreement under {NOISE_SELF_AGREEMENT:.0%}. The model disagrees with itself")
        lines.append("            on identical input; that disagreement caps any edge.")
    if v.theater:
        lines.append(f"  THEATER - scramble kappa over {THEATER_SCRAMBLE_KAPPA:.2f}. The answer survives having all")
        lines.append("            of its evidence replaced, so the evidence is not producing it.")
    if v.passed:
        lines.append("  The answer changes when the evidence changes, and holds when it does not.")
        lines.append("  That is necessary for edge, not sufficient -- the live journal decides.")
    if r.failed:
        lines += ["", "FAILED:"] + [f"  {t.custom_id}: {t.error}" for t in r.failed]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Running
# --------------------------------------------------------------------------- #

def assemble(trials: list[Trial], tickers: int) -> Report:
    real = {t.ticker: t for t in trials if t.condition == REAL and t.signal}
    repeat = {t.ticker: t for t in trials if t.condition == REPEAT and t.signal}
    scrambled = {t.ticker: t for t in trials if t.condition == SCRAMBLED and t.signal}
    failed = [t for t in trials if t.signal is None]
    return Report(tickers, real, repeat, scrambled, failed)


def apply_results(
    trials: list[Trial],
    results: dict[str, "Completion | LLMError"],
    parse_signal: Callable[[str], LLMSignal],
) -> None:
    for t in trials:
        got = results.get(t.custom_id)
        if got is None:
            t.error = "no result returned"
        elif isinstance(got, LLMError):
            t.error = str(got)
        else:
            try:
                t.signal = parse_signal(got.text)
                t.usage = got.usage
            except Exception as exc:  # noqa: BLE001 - one bad answer is one row
                t.error = f"unparseable: {exc}"


def _trials_to_json(tickers: int, trials: list[Trial]) -> str:
    return json.dumps({
        "tickers": tickers,
        "trials": [{"ticker": t.ticker, "condition": t.condition,
                    "system_prompt": t.system_prompt, "user_prompt": t.user_prompt,
                    "donor": t.donor} for t in trials],
    })


def _trials_from_json(text: str) -> tuple[int, list[Trial]]:
    saved = json.loads(text)
    return saved["tickers"], [Trial(**row) for row in saved["trials"]]


def main(argv: list[str] | None = None) -> int:
    """Three stages, each a pure function of its inputs to stdout.

    Nothing under replay/ may write a file -- that guardrail is what keeps a
    replay from ever touching the journal -- so persistence between stages is
    the caller's job: redirect ``plan`` to a file, pass it to ``submit`` and
    ``collect``. It also makes resuming a batch that outlived one job trivial.
    """
    parser = argparse.ArgumentParser(description="Null test + self-consistency, no market needed.")
    sub = parser.add_subparsers(dest="stage", required=True)

    plan = sub.add_parser("plan", help="gather live context and print the trials as JSON")
    plan.add_argument("--tickers", type=int, default=len(DEFAULT_WATCHLIST),
                      help="how many of the watchlist to sample (default: all)")

    submit = sub.add_parser("submit", help="submit planned trials as a batch; prints the batch id")
    submit.add_argument("--trials", type=Path, required=True)

    collect = sub.add_parser("collect", help="collect a batch and print the report")
    collect.add_argument("--trials", type=Path, required=True)
    collect.add_argument("--batch", required=True, metavar="BATCH_ID")
    collect.add_argument("--json", action="store_true", dest="as_json")

    args = parser.parse_args(argv)

    from orchestrator.heartbeat import (
        SIGNAL_JSON_SCHEMA, build_context, build_user_prompt, parse_signal, system_prompt_for,
    )

    if args.stage == "plan":
        chosen = list(DEFAULT_WATCHLIST[: args.tickers])
        contexts: dict[str, TickerContext] = {}
        for ticker in chosen:
            try:
                contexts[ticker] = build_context(ticker)
            except Exception as exc:  # noqa: BLE001 - a ticker with no context is skipped, loudly
                print(f"{ticker}: no context ({type(exc).__name__}: {exc})", file=sys.stderr)
        if not contexts:
            print("no ticker produced a context; nothing to test", file=sys.stderr)
            return 2
        trials = build_trials(contexts, system_prompt_for, build_user_prompt)
        print(_trials_to_json(len(contexts), trials))
        print(f"planned {len(trials)} trials over {len(contexts)} tickers", file=sys.stderr)
        return 0

    from config.settings import get_settings
    from orchestrator.llm import AnthropicSignalProvider

    provider = AnthropicSignalProvider(get_settings().anthropic_api_key)
    tickers, trials = _trials_from_json(args.trials.read_text())

    if args.stage == "submit":
        prompts = [
            BatchRequest(t.custom_id, t.system_prompt, t.user_prompt, SIGNAL_JSON_SCHEMA)
            for t in trials
        ]
        batch_id = provider.submit_batch(prompts)
        print(batch_id)
        print(f"submitted {len(prompts)} requests as {batch_id}", file=sys.stderr)
        return 0

    results = provider.collect_batch(args.batch)
    apply_results(trials, results, parse_signal)
    report = assemble(trials, tickers)
    print(json.dumps(report.as_dict(), indent=2) if args.as_json else render(report))
    return 0 if report.verdicts.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
