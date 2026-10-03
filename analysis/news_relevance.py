"""Is a headline about the company? A code-only relevance check (the owner, 3 Oct 2026).

The rule, as the owner wrote it: a headline counts as relevant if the company
name, or the ticker as a whole word, appears in the title or the first
sentence. No model is asked. It is used two ways:

* on the shadow stock universe's news (its own query, company name plus
  ticker: ``orchestrator/universe_news.py``), to find the names whose search
  still finds something else -- the card's replacement rule (2);
* once, as a description only, on the news the main race used for its 80
  names (``logs/journal/``): how often the headlines the model read were about
  the name it scored. Nothing in production changes because of it.

How it reads the rule:

* **The text** is the title plus the first sentence of the snippet (up to the
  first ". ", "! " or "? ", or the whole snippet if it has none).
* **A name** matches as whole words, as it is written or in capitals
  (``Nvidia`` or ``NVIDIA``): a company name is a proper noun, so ``visa
  rules`` is not Visa and ``a charter flight`` is not Charter. A company may
  have more than one name (``"Southern Company", "Southern Co"``); the
  universe's names are ``config.shadow_universe.match_names``.
* **The ticker** matches as a whole word, in capitals, with ``$`` allowed in
  front (``$NVDA``, ``NYSE:T``). A hyphen or ``&`` joins it to the next
  word, so ``T-Mobile`` is not ``T`` and ``S&P`` is not ``P``. For a one- or
  two-letter ticker (``C``, ``T``, ``SO``) a capital standing alone is still
  weak evidence (``Class C``), so the report also gives the share that names
  the company by name alone.

Pure: no network, no file written. ``main`` reads a journal and prints.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Final, Iterable, Mapping, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import journal_files  # noqa: E402
from config import shadow_universe as su  # noqa: E402

#: A name with fewer relevant headlines than this share fails the check (the owner: "under 30% relevant").
FAIL_BELOW: Final[float] = 0.30

#: The names in the headlines for the race's 80 names (for the descriptive check only). A fund is named
#: by its brand as headlines write it; its ticker counts too, as for every name.
RACE_NAMES: Final[dict[str, tuple[str, ...]]] = {
    "MSFT": ("Microsoft",), "NVDA": ("Nvidia",), "ASML": ("ASML",), "GOOGL": ("Alphabet", "Google"),
    "JPM": ("JPMorgan", "JP Morgan", "J.P. Morgan"), "RY": ("Royal Bank of Canada", "RBC"),
    "HDB": ("HDFC Bank", "HDFC"), "LLY": ("Eli Lilly", "Lilly"), "NVO": ("Novo Nordisk",),
    "TEVA": ("Teva",), "CAT": ("Caterpillar",), "ESLT": ("Elbit",), "TM": ("Toyota",),
    "MELI": ("MercadoLibre", "Mercado Libre"), "PG": ("Procter & Gamble", "Procter and Gamble", "P&G"),
    "XOM": ("Exxon", "ExxonMobil"),
    "RSP": ("Equal Weight",), "IWM": ("Russell 2000",), "VGK": ("Vanguard FTSE Europe",),
    "EWJ": ("iShares MSCI Japan",), "VWO": ("Vanguard FTSE Emerging Markets",),
    "EIS": ("iShares MSCI Israel",), "VNQ": ("Vanguard Real Estate",),
    "TLT": ("20+ Year Treasury",), "DBC": ("Invesco DB Commodity",), "DBA": ("Invesco DB Agriculture",),
    "XLE": ("Energy Select Sector",), "XLF": ("Financial Select Sector",),
    "XLV": ("Health Care Select Sector",), "XLK": ("Technology Select Sector",),
    "XLI": ("Industrial Select Sector",), "XLY": ("Consumer Discretionary Select Sector",),
    "XLP": ("Consumer Staples Select Sector",), "XLU": ("Utilities Select Sector",),
    "XLB": ("Materials Select Sector",), "XLC": ("Communication Services Select Sector",),
    "SMH": ("VanEck Semiconductor",), "IGV": ("Expanded Tech-Software", "Expanded Tech Software"),
    "XBI": ("SPDR S&P Biotech",), "KRE": ("SPDR S&P Regional Banking",),
    "ITA": ("iShares U.S. Aerospace & Defense", "iShares US Aerospace"), "IYT": ("iShares Transportation",),
    "XHB": ("SPDR S&P Homebuilders",), "GDX": ("VanEck Gold Miners",),
    "EWU": ("iShares MSCI United Kingdom",), "EWG": ("iShares MSCI Germany",),
    "EWL": ("iShares MSCI Switzerland",), "EWN": ("iShares MSCI Netherlands",),
    "EWI": ("iShares MSCI Italy",), "EWP": ("iShares MSCI Spain",), "EWD": ("iShares MSCI Sweden",),
    "EWC": ("iShares MSCI Canada",), "EWA": ("iShares MSCI Australia",), "MCHI": ("iShares MSCI China",),
    "INDA": ("iShares MSCI India",), "EWY": ("iShares MSCI South Korea",), "EWT": ("iShares MSCI Taiwan",),
    "EWZ": ("iShares MSCI Brazil",), "EWW": ("iShares MSCI Mexico",), "KSA": ("iShares MSCI Saudi Arabia",),
    "TUR": ("iShares MSCI Turkey",), "EZA": ("iShares MSCI South Africa",), "EPOL": ("iShares MSCI Poland",),
    "ARGT": ("Global X MSCI Argentina",), "SHY": ("1-3 Year Treasury",), "IEF": ("7-10 Year Treasury",),
    "TIP": ("iShares TIPS",), "LQD": ("Investment Grade Corporate",), "HYG": ("High Yield Corporate",),
    "EMB": ("USD Emerging Markets Bond",), "UUP": ("US Dollar Index Bullish", "U.S. Dollar Index Bullish"),
    "GLD": ("SPDR Gold",), "SLV": ("iShares Silver",), "CPER": ("United States Copper",),
    "USO": ("United States Oil",), "UNG": ("United States Natural Gas",), "CORN": ("Teucrium Corn",),
    "WEAT": ("Teucrium Wheat",), "SOYB": ("Teucrium Soybean",), "CANE": ("Teucrium Sugar",),
}

_SENTENCE_END = re.compile(r"(?<=[.!?])\s")


def first_sentence(text: str) -> str:
    """Up to the first sentence end (". ", "! ", "? "), or the whole text."""
    text = (text or "").strip()
    found = _SENTENCE_END.search(text)
    return text[:found.start()] if found else text


def _name_pattern(name: str) -> re.Pattern:
    """The name as written, or in capitals, as whole words."""
    forms = sorted({name, name.upper()}, key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(map(re.escape, forms)) + r")(?![A-Za-z0-9])")


def _ticker_pattern(ticker: str) -> re.Pattern:
    """The ticker in capitals as a whole word; ``$`` may come first; a hyphen or ``&`` joins words."""
    return re.compile(r"(?<![A-Za-z0-9&-])\$?" + re.escape(ticker.upper()) + r"(?![A-Za-z0-9&-])")


@dataclass(frozen=True)
class Matcher:
    """The rule for one name: its company names and its ticker."""

    ticker: str
    names: tuple[str, ...]

    def by_name(self, text: str) -> bool:
        return any(_name_pattern(n).search(text) for n in self.names if n)

    def by_ticker(self, text: str) -> bool:
        return bool(_ticker_pattern(self.ticker).search(text))

    def relevant(self, title: str, snippet: str = "") -> bool:
        """The owner's rule: the company name, or the ticker as a whole word, in the title or the first sentence."""
        text = f"{title or ''} {first_sentence(snippet)}"
        return self.by_name(text) or self.by_ticker(text)

    def named(self, title: str, snippet: str = "") -> bool:
        """The company named by name alone (for reading, beside the rule)."""
        return self.by_name(f"{title or ''} {first_sentence(snippet)}")


def _title_snippet(item: Any) -> tuple[str, str]:
    """A ``news.Headline``, a journal ``sources`` record, or a plain prompt line."""
    if isinstance(item, Mapping):
        return str(item.get("title") or ""), str(item.get("snippet") or "")
    if not isinstance(item, str) and hasattr(item, "title"):   # a str has a .title() method too
        return str(getattr(item, "title", "") or ""), str(getattr(item, "snippet", "") or "")
    line = str(item)
    title, _, rest = line.partition(" — ")
    return title, rest


@dataclass(frozen=True)
class Share:
    """One name's headlines: how many, how many relevant by the rule, how many naming the company by name."""

    ticker: str
    headlines: int
    relevant: int
    named: int

    @property
    def share(self) -> Optional[float]:
        return self.relevant / self.headlines if self.headlines else None

    @property
    def named_share(self) -> Optional[float]:
        return self.named / self.headlines if self.headlines else None

    @property
    def fails(self) -> bool:
        """Under ``FAIL_BELOW`` relevant, or no headline at all."""
        return self.share is None or self.share < FAIL_BELOW


def share(ticker: str, names: Sequence[str], items: Iterable[Any]) -> Share:
    """Count one name's headlines by the rule."""
    matcher = Matcher(ticker, tuple(names))
    pairs = [_title_snippet(item) for item in items]
    return Share(ticker, len(pairs), sum(matcher.relevant(t, s) for t, s in pairs),
                 sum(matcher.named(t, s) for t, s in pairs))


def universe_share(ticker: str, items: Iterable[Any]) -> Share:
    """One shadow-universe name's headlines, counted with its names from ``config.shadow_universe``."""
    return share(ticker, su.match_names(ticker), items)


def overall(shares: Sequence[Share]) -> Optional[float]:
    """Relevant headlines over all headlines, every name together."""
    total = sum(s.headlines for s in shares)
    return sum(s.relevant for s in shares) / total if total else None


def report(shares: Sequence[Share], title: str) -> str:
    """The table the owner asked for: the share per name, the names under 30%, and the overall share."""
    def pct(value: Optional[float]) -> str:
        return "n/a" if value is None else f"{value * 100:.0f}%"

    failing = [s for s in shares if s.fails]
    lines = [f"# {title}", "",
             f"Rule: a headline is relevant if the company name, or the ticker as a whole word, is in its title or "
             f"first sentence (code only, no model). A name fails under {FAIL_BELOW:.0%} relevant or with no "
             "headline.", "",
             f"**Overall: {pct(overall(shares))} relevant** ({sum(s.relevant for s in shares)} of "
             f"{sum(s.headlines for s in shares)} headlines, {len(shares)} names).", "",
             f"**Under {FAIL_BELOW:.0%} (or no headline): {len(failing)} name(s)**"
             + (": " + ", ".join(f"{s.ticker} ({pct(s.share)})" for s in failing) if failing else "."), "",
             "| Name | Headlines | Relevant | Share | By name alone |", "| --- | ---: | ---: | ---: | ---: |"]
    lines += [f"| {s.ticker} | {s.headlines} | {s.relevant} | {pct(s.share)} | {pct(s.named_share)} |"
              for s in shares]
    return "\n".join(lines) + "\n"


def journal_headlines(directory: Path, since: date, until: Optional[date] = None) -> dict[str, list[dict]]:
    """Every answered line's news records in a production journal, per ticker, from ``since`` (UTC days)."""
    out: dict[str, list[dict]] = defaultdict(list)
    files = sorted(Path(directory).glob("*.log")) if Path(directory).is_dir() else [Path(directory)]
    for path in files:
        for raw in journal_files.iter_lines(path):
            try:
                line = json.loads(raw)
            except ValueError:
                continue
            if not isinstance(line, dict) or not isinstance(line.get("ticker"), str):
                continue
            try:
                day = datetime.fromisoformat(str(line.get("ts_utc"))).astimezone(timezone.utc).date()
            except ValueError:
                continue
            if day < since or (until is not None and day > until):
                continue
            ctx = line.get("context") if isinstance(line.get("context"), dict) else {}
            records = ctx.get("sources") or ctx.get("headlines") or []
            out[line["ticker"]].extend(r if isinstance(r, dict) else {"title": _title_snippet(r)[0],
                                                                       "snippet": _title_snippet(r)[1]}
                                       for r in records)
    return dict(out)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """``python -m analysis.news_relevance``: the descriptive check on the race's news, printed as Markdown."""
    parser = argparse.ArgumentParser(prog="python -m analysis.news_relevance",
                                     description="Relevance of the race's news headlines (descriptive only).")
    parser.add_argument("--journal", type=Path, default=Path(__file__).resolve().parent.parent / "logs" / "journal")
    parser.add_argument("--since", default="2026-09-23", help="first UTC day (default: the full model's first day)")
    parser.add_argument("--until", default=None)
    args = parser.parse_args(argv)
    found = journal_headlines(args.journal, date.fromisoformat(args.since),
                              date.fromisoformat(args.until) if args.until else None)
    shares = [share(t, RACE_NAMES.get(t, ()), found.get(t, [])) for t in RACE_NAMES]
    print(report(shares, f"News relevance: the race's 80 names, lines from {args.since} (descriptive only)"))
    return 0


__all__ = ["FAIL_BELOW", "Matcher", "RACE_NAMES", "Share", "first_sentence", "journal_headlines", "main",
           "overall", "report", "share", "universe_share"]


if __name__ == "__main__":
    raise SystemExit(main())
