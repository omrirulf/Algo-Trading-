"""Insider activity — Form 4 buying and selling, as yfinance reports it.

The fourth context source, and the one where the naive reading is most often
wrong. Three things shape this module:

**Buys and sells are not symmetric.** An insider sells for reasons that have
nothing to do with the business: a scheduled 10b5-1 plan, a tax bill on
vesting shares, a house, simple diversification. An insider *buying* on the
open market is spending their own money on a view. The rendering says this
plainly so the model does not read a routine sale as a bearish signal.

**A grant is not a purchase.** Yahoo's transaction list mixes open-market
purchases with stock awards, option exercises, gifts and tax withholding.
Counting a grant as "insider buying" would turn compensation into a signal and
make the whole dimension noise, so only genuine purchases and sales are
counted; everything else is reported separately as excluded.

**Nobody trading is not the same as nobody available.** An empty transaction
list and a failed fetch look identical downstream if both render as nothing, so
they are distinguished: no activity says so, and a missing source becomes a
gap in the prompt.

Pure parsing, like its sibling modules: ``orchestrator.context`` fetches.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta
from typing import Any, Optional

from orchestrator import formatting as fmt

#: Transactions inside this window are shown individually. Matches the six
#: months yfinance's own rollup covers.
WINDOW_DAYS = 180

MAX_SHOWN_PER_SIDE = 4

#: Yahoo's ``Transaction`` values. Only these two are open-market trades; a
#: stock award, option exercise, gift or tax withholding is compensation or
#: paperwork, not a view on the price.
_BUY_TERMS = ("purchase",)
_SELL_TERMS = ("sale", "sold")

#: Row labels in the ``insider_purchases`` rollup, normalised to lowercase.
_ROLLUP_ROWS = {
    "purchases": "shares_purchased",
    "sales": "shares_sold",
    "net shares purchased (sold)": "net_shares",
    "total insider shares held": "total_shares_held",
    "% net shares purchased (sold)": "net_pct_of_held",
}

_COUNT_ROWS = {"purchases": "purchase_count", "sales": "sale_count"}


@dataclass(frozen=True)
class InsiderTrade:
    when: Optional[str]
    who: Optional[str]
    role: Optional[str]
    shares: Optional[float]
    value: Optional[float]

    def render(self) -> str:
        who = self.who or "unnamed insider"
        role = f" ({self.role})" if self.role else ""
        line = f"{self.when or 'date n/a'} {who}{role}"
        if self.shares is not None:
            line += f": {self.shares:,.0f} shares"
        if self.value is not None:
            line += f", {fmt.money(self.value)}"
        return line


@dataclass(frozen=True)
class InsiderSnapshot:
    shares_purchased: Optional[float] = None
    purchase_count: Optional[int] = None
    shares_sold: Optional[float] = None
    sale_count: Optional[int] = None
    net_shares: Optional[float] = None
    net_pct_of_held: Optional[float] = None
    total_shares_held: Optional[float] = None
    buys: list[InsiderTrade] = field(default_factory=list)
    sells: list[InsiderTrade] = field(default_factory=list)
    distinct_buyers: int = 0
    distinct_sellers: int = 0
    #: Grants, option exercises, gifts and tax withholding — excluded on purpose.
    non_market_count: int = 0
    window_days: int = WINDOW_DAYS

    @property
    def has_activity(self) -> bool:
        return bool(self.buys or self.sells) or any(
            v is not None for v in (self.shares_purchased, self.shares_sold, self.net_shares)
        )

    def as_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "InsiderSnapshot":
        """The inverse of ``as_dict``, for a snapshot read back off a journal line.

        What lets ``rules/insider_buying.py`` be recomputed over every line
        ever journalled: the arm reads the section the model was shown, and
        the journal is where that section is kept.
        """
        fields = {name: data.get(name) for name in cls.__dataclass_fields__}
        for side in ("buys", "sells"):
            fields[side] = [
                InsiderTrade(**{k: t.get(k) for k in InsiderTrade.__dataclass_fields__})
                for t in (fields.get(side) or []) if isinstance(t, dict)
            ]
        for name in ("distinct_buyers", "distinct_sellers", "non_market_count"):
            fields[name] = int(fields[name] or 0)
        fields["window_days"] = int(fields["window_days"] or WINDOW_DAYS)
        return cls(**fields)

    def as_lines(self) -> list[str]:
        if not self.has_activity:
            return [f"No insider transactions reported in the last {self.window_days} days."]

        lines = [
            f"Last {self.window_days} days: bought {_shares(self.shares_purchased)} shares "
            f"in {_count(self.purchase_count)} transaction(s) | "
            f"sold {_shares(self.shares_sold)} shares in {_count(self.sale_count)}",
            f"Net: {_shares(self.net_shares, signed=True)} shares"
            + (
                f" ({fmt.pct(self.net_pct_of_held)} of insider holdings)"
                if self.net_pct_of_held is not None
                else ""
            )
            + f" | insiders hold {_shares(self.total_shares_held)} shares",
            f"Distinct insiders: {self.distinct_buyers} buying, {self.distinct_sellers} selling",
        ]

        if self.buys:
            lines.append("Open-market purchases — insiders spending their own money:")
            lines.extend(f"  - {trade.render()}" for trade in self.buys[:MAX_SHOWN_PER_SIDE])
        if self.sells:
            lines.append(
                "Sales — weak evidence on their own; often scheduled 10b5-1 plans, "
                "tax on vesting, or diversification:"
            )
            lines.extend(f"  - {trade.render()}" for trade in self.sells[:MAX_SHOWN_PER_SIDE])
        if self.non_market_count:
            lines.append(
                f"({self.non_market_count} grant/option/gift transaction(s) excluded — "
                "compensation, not a view on the price)"
            )
        return lines


def build_snapshot(
    purchases: Any = None,
    transactions: Any = None,
    as_of: Optional[date] = None,
    window_days: int = WINDOW_DAYS,
) -> InsiderSnapshot:
    """Combine the six-month rollup with the individual transaction list."""
    rollup = parse_rollup(purchases)
    buys, sells, non_market = parse_transactions(transactions, as_of, window_days)

    return InsiderSnapshot(
        **rollup,
        buys=buys,
        sells=sells,
        distinct_buyers=len({t.who for t in buys if t.who}),
        distinct_sellers=len({t.who for t in sells if t.who}),
        non_market_count=non_market,
        window_days=window_days,
    )


def parse_rollup(purchases: Any) -> dict[str, Any]:
    """Read yfinance's ``insider_purchases`` summary frame.

    Its label column has been renamed between releases, so the label is taken
    from whichever column is not ``Shares`` or ``Trans`` rather than by name.
    """
    empty: dict[str, Any] = {
        "shares_purchased": None, "purchase_count": None,
        "shares_sold": None, "sale_count": None,
        "net_shares": None, "net_pct_of_held": None, "total_shares_held": None,
    }
    if purchases is None or not hasattr(purchases, "empty") or purchases.empty:
        return empty

    columns = list(getattr(purchases, "columns", []))
    label_columns = [c for c in columns if str(c) not in ("Shares", "Trans")]
    if not label_columns:
        return empty
    label_column = label_columns[0]

    values = dict(empty)
    for _, row in purchases.iterrows():
        label = str(row.get(label_column, "")).strip().lower()
        if label in _ROLLUP_ROWS:
            values[_ROLLUP_ROWS[label]] = fmt.clean(row.get("Shares"))
        if label in _COUNT_ROWS:
            count = fmt.clean(row.get("Trans"))
            values[_COUNT_ROWS[label]] = int(count) if count is not None else None
    return values


def parse_transactions(
    transactions: Any,
    as_of: Optional[date] = None,
    window_days: int = WINDOW_DAYS,
) -> tuple[list[InsiderTrade], list[InsiderTrade], int]:
    """Split the transaction list into open-market buys, sells, and everything else."""
    if transactions is None or not hasattr(transactions, "empty") or transactions.empty:
        return [], [], 0

    cutoff = (as_of or date.today()) - timedelta(days=window_days)
    buys: list[InsiderTrade] = []
    sells: list[InsiderTrade] = []
    non_market = 0

    for _, row in transactions.iterrows():
        when = _as_date(row.get("Start Date"))
        if when is not None and when < cutoff:
            continue

        kind = _classify(row)
        if kind is None:
            non_market += 1
            continue

        trade = InsiderTrade(
            when=when.isoformat() if when else None,
            who=_text(row.get("Insider")),
            role=_text(row.get("Position")),
            shares=fmt.clean(row.get("Shares")),
            value=fmt.clean(row.get("Value")),
        )
        (buys if kind == "buy" else sells).append(trade)

    buys.sort(key=lambda t: t.when or "", reverse=True)
    sells.sort(key=lambda t: t.when or "", reverse=True)
    return buys, sells, non_market


def _classify(row: Any) -> Optional[str]:
    """``"buy"``, ``"sell"``, or None for compensation and paperwork."""
    text = " ".join(
        str(row.get(field) or "").lower() for field in ("Transaction", "Text")
    )
    if any(term in text for term in _BUY_TERMS):
        return "buy"
    if any(term in text for term in _SELL_TERMS):
        return "sell"
    return None


def _as_date(value: Any) -> Optional[date]:
    if value is None or fmt.is_missing(value):
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str) and value.strip():
        try:
            return datetime.fromisoformat(value.strip()[:10]).date()
        except ValueError:
            return None
    try:
        import pandas as pd

        return pd.Timestamp(value).date()
    except (TypeError, ValueError):
        return None


def _text(value: Any) -> Optional[str]:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _shares(value: Optional[float], signed: bool = False) -> str:
    if value is None:
        return fmt.NA
    return f"{value:{'+' if signed else ''},.0f}"


def _count(value: Optional[int]) -> str:
    return fmt.NA if value is None else str(value)
