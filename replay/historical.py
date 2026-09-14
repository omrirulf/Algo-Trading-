#!/usr/bin/env python3
"""An early read on the signal, from history, on the two dimensions that are honest there.

    python replay/historical.py plan --samples 200 --seed 7 > hist_trials.json
    python replay/historical.py submit --trials hist_trials.json > batch_id
    python replay/historical.py collect --trials hist_trials.json --batch $(cat batch_id)

Why only two of five dimensions
-------------------------------
A live signal sees news, technicals, fundamentals, the analyst view and
insider filings. Two of those can be rebuilt as they stood on a past date:

- TECHNICALS rebuild exactly. Every indicator is a function of the bars up to
  the signal date, so slicing the OHLC frame at that date and calling the
  same ``build_snapshot`` the live path uses gives the number the model would
  have seen, with no way for a later bar to leak in.
- NEWS rebuilds approximately. Google's index accepts a custom date range, so
  the query asks for stories dated on or just before the signal date. What it
  returns is what is *still indexed* -- sparser than the day's real coverage,
  and biased towards stories that lasted. Samples that come back with no
  headlines are kept and counted separately, because "technicals only" is a
  different and weaker strategy than "technicals plus news".

The other three cannot be rebuilt honestly. yfinance reports fundamentals,
analyst targets and insider filings as they stand *today*; handing the model
today's numbers under a past date would leak the future through the side door.
They are withheld and named as gaps, so the model is told to score them 0.0
rather than guess -- exactly what the live prompt tells it to do with a gap.

So this tests a strategy with less to go on than the live one. A signal that
shows something here has something; one that shows nothing here has not been
given its full inputs, and the live journal is still the arbiter.

Scoring is the engine's own arithmetic: every sided signal that clears the
conviction floor is put through ``backtest.simulate.simulate_trade`` -- next-bar
entry, the real ATR stop, the real position cap -- so "hit" means the trade
the system would actually have taken made money, not that the close was
higher some days later. The unconditional forward return of every sample is
reported alongside as the base rate a BULLISH call has to beat.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Callable, Optional

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.schemas import Bias, LLMSignal  # noqa: E402
from backtest.simulate import DEFAULT_HORIZON_DAYS, Trade, simulate_trade  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import is_fund  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from orchestrator import technicals  # noqa: E402
from orchestrator.context import TickerContext  # noqa: E402
from orchestrator.llm import BatchRequest, Completion, LLMError, batch_custom_id  # noqa: E402
from orchestrator.pricing import Usage  # noqa: E402

#: Bars of history a sample must have behind it. The 52-week range and the
#: 200-day average both need a year, and a thinner snapshot would not be the
#: one the live path produces.
MIN_HISTORY_BARS = 252

#: How much OHLC to fetch. Three years leaves a full year behind the oldest
#: two-year-old sample.
OHLC_PERIOD = "3y"

#: Gaps named the way the live prompt names a gap, so the model treats them
#: identically: score 0.0, do not infer.
WITHHELD = {
    "fundamentals": "fundamentals withheld: not available point-in-time in this replay",
    "analysts": "analyst view withheld: not available point-in-time in this replay",
    "insiders": "insider activity withheld: not available point-in-time in this replay",
}


@dataclass
class Sample:
    ticker: str
    day: str                 # ISO date of the signal bar
    index: int               # position of that bar in the fetched frame
    system_prompt: str
    user_prompt: str
    headlines: int
    signal: Optional[LLMSignal] = None
    usage: Optional[Usage] = None
    error: Optional[str] = None
    trade: Optional[Trade] = None
    raw_forward: Optional[float] = None   # unconditional next-bar-to-horizon return

    @property
    def custom_id(self) -> str:
        return batch_custom_id(self.ticker, self.day)


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #

def fetch_ohlc(ticker: str, period: str = OHLC_PERIOD) -> Optional[pd.DataFrame]:
    """Daily bars, or None. Never raises: a ticker with no history is skipped."""
    try:
        import yfinance as yf

        frame = yf.Ticker(ticker).history(period=period, interval="1d", auto_adjust=False)
    except Exception:  # noqa: BLE001
        return None
    if frame is None or frame.empty or not isinstance(frame.index, pd.DatetimeIndex):
        return None
    return frame.dropna(subset=["Open", "High", "Low", "Close"])


def technicals_as_of(frame: pd.DataFrame, index: int) -> Optional[technicals.TechnicalSnapshot]:
    """The snapshot the live path would have built on that bar.

    ``iloc[: index + 1]`` is the whole guarantee: nothing after the signal bar
    is in the frame the indicators are computed from.
    """
    try:
        return technicals.build_snapshot(frame.iloc[: index + 1])
    except (ValueError, KeyError):
        return None


def raw_forward_return(frame: pd.DataFrame, index: int, horizon: int) -> Optional[float]:
    """Next-bar open to horizon-bar close, the same span simulate_trade covers."""
    entry = index + 1
    exit_ = entry + horizon - 1
    if exit_ >= len(frame):
        return None
    entry_px = float(frame["Open"].iloc[entry])
    exit_px = float(frame["Close"].iloc[exit_])
    if entry_px <= 0:
        return None
    return exit_px / entry_px - 1.0


def build_sample_context(
    ticker: str, headlines: list[str], snapshot: Optional[technicals.TechnicalSnapshot]
) -> TickerContext:
    gaps = [WITHHELD["fundamentals"]]
    if not is_fund(ticker):
        gaps += [WITHHELD["analysts"], WITHHELD["insiders"]]
    if snapshot is None:
        gaps.append("technicals could not be computed for this bar")
    return TickerContext(
        ticker=ticker, headlines=list(headlines), technicals=snapshot,
        fundamentals=None, analysts=None, insiders=None, gaps=gaps,
    )


def draw_samples(
    frames: dict[str, pd.DataFrame],
    n: int,
    horizon: int,
    rng: random.Random,
) -> list[tuple[str, int]]:
    """(ticker, bar index) pairs with a year behind and the horizon ahead.

    Uniform over tickers, then uniform over eligible bars, so the sample is
    not dominated by whichever ticker has the longest history.
    """
    eligible = {
        t: (MIN_HISTORY_BARS, len(f) - horizon - 2)
        for t, f in frames.items()
        if len(f) - horizon - 2 > MIN_HISTORY_BARS
    }
    if not eligible:
        return []
    tickers = sorted(eligible)
    out: list[tuple[str, int]] = []
    seen: set[tuple[str, int]] = set()
    attempts = 0
    while len(out) < n and attempts < n * 20:
        attempts += 1
        t = rng.choice(tickers)
        lo, hi = eligible[t]
        i = rng.randint(lo, hi)
        if (t, i) in seen:
            continue
        seen.add((t, i))
        out.append((t, i))
    return out


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #

def trades(signal: Optional[LLMSignal]) -> bool:
    return (
        signal is not None
        and signal.bias is not Bias.NEUTRAL
        and signal.conviction >= cfg.MIN_CONVICTION
    )


def side_of(signal: LLMSignal) -> str:
    return "buy" if signal.bias is Bias.BULLISH else "sell"


def score(samples: list[Sample], frames: dict[str, pd.DataFrame], horizon: int) -> None:
    """Attach the raw forward return to every sample and a Trade to every traded one."""
    for s in samples:
        frame = frames.get(s.ticker)
        if frame is None:
            continue
        s.raw_forward = raw_forward_return(frame, s.index, horizon)
        if trades(s.signal):
            s.trade = simulate_trade(frame, s.index, side=side_of(s.signal), horizon_days=horizon)


def _se(p: float, n: int) -> float:
    return math.sqrt(p * (1 - p) / n) if n else 0.0


@dataclass
class Report:
    samples: list[Sample]
    horizon: int
    failed: list[Sample] = field(default_factory=list)

    @property
    def answered(self) -> list[Sample]:
        return [s for s in self.samples if s.signal is not None]

    @property
    def with_news(self) -> int:
        return sum(1 for s in self.samples if s.headlines > 0)

    def by_bias(self, bias: Bias) -> list[Sample]:
        return [s for s in self.answered if s.signal.bias is bias]

    @property
    def traded(self) -> list[Sample]:
        return [s for s in self.answered if s.trade is not None]

    # --- base rate ---------------------------------------------------------- #
    @property
    def base_rate_up(self) -> Optional[float]:
        raws = [s.raw_forward for s in self.samples if s.raw_forward is not None]
        return None if not raws else sum(1 for r in raws if r > 0) / len(raws)

    @property
    def base_mean_forward(self) -> Optional[float]:
        raws = [s.raw_forward for s in self.samples if s.raw_forward is not None]
        return None if not raws else statistics.fmean(raws)

    # --- directional read --------------------------------------------------- #
    def hit_rate(self, bias: Bias) -> tuple[Optional[float], int]:
        rows = [s for s in self.by_bias(bias) if s.raw_forward is not None]
        if not rows:
            return None, 0
        if bias is Bias.BULLISH:
            hits = sum(1 for s in rows if s.raw_forward > 0)
        elif bias is Bias.BEARISH:
            hits = sum(1 for s in rows if s.raw_forward < 0)
        else:
            return None, len(rows)
        return hits / len(rows), len(rows)

    def mean_forward(self, bias: Bias) -> Optional[float]:
        rows = [s.raw_forward for s in self.by_bias(bias) if s.raw_forward is not None]
        return None if not rows else statistics.fmean(rows)

    # --- the engine's trades ------------------------------------------------ #
    @property
    def traded_hit_rate(self) -> Optional[float]:
        t = self.traded
        return None if not t else sum(1 for s in t if s.trade.return_pct > 0) / len(t)

    @property
    def traded_mean_realised_pct(self) -> Optional[float]:
        t = self.traded
        return None if not t else statistics.fmean(s.trade.realised_pct_of_equity for s in t)

    @property
    def traded_stop_rate(self) -> Optional[float]:
        t = self.traded
        return None if not t else sum(1 for s in t if s.trade.stopped_out) / len(t)

    @property
    def cost_usd(self) -> float:
        return sum(s.usage.cost_usd or 0.0 for s in self.samples if s.usage)

    def as_dict(self) -> dict:
        bull, nb = self.hit_rate(Bias.BULLISH)
        bear, ns = self.hit_rate(Bias.BEARISH)
        return {
            "samples": len(self.samples), "answered": len(self.answered),
            "failed": len(self.failed), "with_news": self.with_news, "horizon": self.horizon,
            "base_rate_up": self.base_rate_up, "base_mean_forward": self.base_mean_forward,
            "bullish": {"n": nb, "hit_rate": bull, "mean_forward": self.mean_forward(Bias.BULLISH)},
            "bearish": {"n": ns, "hit_rate": bear, "mean_forward": self.mean_forward(Bias.BEARISH)},
            "neutral": {"n": len(self.by_bias(Bias.NEUTRAL))},
            "traded": {"n": len(self.traded), "hit_rate": self.traded_hit_rate,
                       "mean_realised_pct_of_equity": self.traded_mean_realised_pct,
                       "stop_rate": self.traded_stop_rate},
            "cost_usd": round(self.cost_usd, 4),
        }


def _pct(v: Optional[float], d: int = 1) -> str:
    return "--" if v is None else f"{v * 100:.{d}f}%"


def render(r: Report) -> str:
    bull, nb = r.hit_rate(Bias.BULLISH)
    bear, ns = r.hit_rate(Bias.BEARISH)
    nn = len(r.by_bias(Bias.NEUTRAL))
    lines = [
        "HISTORICAL REPLAY -- technicals + dated news only",
        "",
        f"{len(r.samples)} samples · answered {len(r.answered)} · failed {len(r.failed)} · "
        f"with news {r.with_news} ({_pct(r.with_news / len(r.samples) if r.samples else None, 0)}) · "
        f"horizon {r.horizon} bars · ${r.cost_usd:.2f}",
        "",
        "BASE RATE (every sample, no signal)",
        f"  share of {r.horizon}-bar forward returns > 0   {_pct(r.base_rate_up)}",
        f"  mean forward return                     {_pct(r.base_mean_forward, 2)}",
        "",
        "DIRECTIONAL READ (raw forward return, by the model's bias)",
        f"  BULLISH  n={nb:<4} hit {_pct(bull)} ± {_pct(_se(bull or 0, nb))}   mean {_pct(r.mean_forward(Bias.BULLISH), 2)}"
        f"   <- must beat the base rate, not 50%",
        f"  BEARISH  n={ns:<4} hit {_pct(bear)} ± {_pct(_se(bear or 0, ns))}   mean {_pct(r.mean_forward(Bias.BEARISH), 2)}"
        f"   <- 'hit' = return < 0",
        f"  NEUTRAL  n={nn}",
        "",
        "THE ENGINE'S TRADES (sided, over the floor, real stop and cap)",
        f"  traded {len(r.traded)} · hit {_pct(r.traded_hit_rate)} · "
        f"mean realised {_pct(r.traded_mean_realised_pct, 3)} of equity · stopped out {_pct(r.traded_stop_rate)}",
        "",
        "Reading it:",
        "- Two of five dimensions. Fundamentals, analyst view and insider filings",
        "  were withheld because they cannot be rebuilt point-in-time. This is a",
        "  weaker strategy than the live one; a signal here is evidence, silence is not.",
        "- Historical news is what Google still indexes: sparser and survivor-biased.",
        "  Samples with no headlines are technicals-only and are counted above.",
        f"- ± is one standard error. With n this size, a hit rate within about",
        f"  two of them of the base rate is indistinguishable from it.",
    ]
    if r.failed:
        lines += ["", "FAILED:"] + [f"  {s.custom_id}: {s.error}" for s in r.failed[:20]]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Stages
# --------------------------------------------------------------------------- #

def _samples_to_json(samples: list[Sample], horizon: int, seed: int) -> str:
    return json.dumps({
        "horizon": horizon, "seed": seed,
        "samples": [{"ticker": s.ticker, "day": s.day, "index": s.index,
                     "system_prompt": s.system_prompt, "user_prompt": s.user_prompt,
                     "headlines": s.headlines} for s in samples],
    })


def _samples_from_json(text: str) -> tuple[list[Sample], int]:
    saved = json.loads(text)
    return [Sample(**row) for row in saved["samples"]], int(saved["horizon"])


def apply_results(
    samples: list[Sample],
    results: dict[str, "Completion | LLMError"],
    parse_signal: Callable[[str], LLMSignal],
) -> list[Sample]:
    failed = []
    for s in samples:
        got = results.get(s.custom_id)
        if got is None:
            s.error = "no result returned"
        elif isinstance(got, LLMError):
            s.error = str(got)
        else:
            try:
                s.signal = parse_signal(got.text)
                s.usage = got.usage
            except Exception as exc:  # noqa: BLE001
                s.error = f"unparseable: {exc}"
        if s.signal is None:
            failed.append(s)
    return failed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Historical replay on the two honest dimensions.")
    sub = parser.add_subparsers(dest="stage", required=True)

    plan = sub.add_parser("plan")
    plan.add_argument("--samples", type=int, default=200)
    plan.add_argument("--seed", type=int, default=7)
    plan.add_argument("--horizon", type=int, default=DEFAULT_HORIZON_DAYS)
    plan.add_argument("--tickers", type=int, default=len(DEFAULT_WATCHLIST))

    submit = sub.add_parser("submit")
    submit.add_argument("--trials", type=Path, required=True)

    collect = sub.add_parser("collect")
    collect.add_argument("--trials", type=Path, required=True)
    collect.add_argument("--batch", required=True)
    collect.add_argument("--json", action="store_true", dest="as_json")

    args = parser.parse_args(argv)

    from orchestrator.heartbeat import (
        SIGNAL_JSON_SCHEMA, build_user_prompt, parse_signal, system_prompt_for,
    )

    if args.stage == "plan":
        from config.settings import get_settings
        from orchestrator.news import BrightDataNewsProvider

        settings = get_settings()
        news = BrightDataNewsProvider(
            settings.brightdata_api_token, settings.brightdata_serp_zone,
            unlocker_zone=settings.brightdata_unlocker_zone,
        )
        universe = list(DEFAULT_WATCHLIST[: args.tickers])
        frames = {t: f for t in universe if (f := fetch_ohlc(t)) is not None}
        for t in universe:
            if t not in frames:
                print(f"{t}: no bars; skipped", file=sys.stderr)
        rng = random.Random(args.seed)
        drawn = draw_samples(frames, args.samples, args.horizon, rng)
        samples: list[Sample] = []
        for ticker, index in drawn:
            frame = frames[ticker]
            day = frame.index[index].date()
            snap = technicals_as_of(frame, index)
            try:
                headlines = news.fetch_on(ticker, day)
            except Exception as exc:  # noqa: BLE001 - no news is a counted condition, not a crash
                print(f"{ticker} {day}: news failed ({type(exc).__name__}); technicals only",
                      file=sys.stderr)
                headlines = []
            ctx = build_sample_context(ticker, headlines, snap)
            samples.append(Sample(
                ticker=ticker, day=day.isoformat(), index=index,
                system_prompt=system_prompt_for(ticker), user_prompt=build_user_prompt(ctx),
                headlines=len(headlines),
            ))
        print(_samples_to_json(samples, args.horizon, args.seed))
        print(f"planned {len(samples)} samples over {len(frames)} tickers; "
              f"{sum(1 for s in samples if s.headlines)} with news", file=sys.stderr)
        return 0 if samples else 2

    from config.settings import get_settings
    from orchestrator.llm import AnthropicSignalProvider

    provider = AnthropicSignalProvider(get_settings().anthropic_api_key)
    samples, horizon = _samples_from_json(args.trials.read_text())

    if args.stage == "submit":
        prompts = [BatchRequest(s.custom_id, s.system_prompt, s.user_prompt, SIGNAL_JSON_SCHEMA)
                   for s in samples]
        batch_id = provider.submit_batch(prompts)
        print(batch_id)
        print(f"submitted {len(prompts)} as {batch_id}", file=sys.stderr)
        return 0

    results = provider.collect_batch(args.batch)
    failed = apply_results(samples, results, parse_signal)
    frames = {t: f for t in {s.ticker for s in samples} if (f := fetch_ohlc(t)) is not None}
    score(samples, frames, horizon)
    report = Report(samples, horizon, failed)
    print(json.dumps(report.as_dict(), indent=2) if args.as_json else render(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
