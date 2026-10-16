"""The public fund table, the similar-but-not-identical pairs, and the trading-cost parameters.

Public facts only (section 2.1): a fund's ticker, ISIN, exchange, index,
provider's fund ID, domicile and whether it pays out. The owner's own funds
are listed in the private ``plan.csv``; one that is not in this table is
priced by its ticker alone.

Section 6.5: a harvest never suggests the same index or the same fund (VWRA
and VWRL are one fund; ACWI and ISAC both follow MSCI ACWI). ``SUBSTITUTES``
is the owner's table, and ``check_substitutes`` refuses any pair that shares
an index or a fund ID, so the table cannot drift into an identical pair.

Section 6.4: trading costs per side, Interactive Brokers' published prices
for a retail client in Israel (IBKR Pro: whole shares only), read from search
summaries on 4 Oct 2026 and to be checked on the broker's own page. They are
public parameters until the owner's broker is chosen (June 2027, D16).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Optional

US: Final[str] = "US"
IRELAND: Final[str] = "IE"

#: How a fund trades, for the cost table: a US-listed fund, or an Irish fund
#: in dollars on the London Stock Exchange.
US_LISTED: Final[str] = "us_listed"
LSE_USD: Final[str] = "lse_usd"


@dataclass(frozen=True)
class Fund:
    ticker: str
    name: str
    isin: str
    exchange: str
    #: The quote line the price fetch reads. Dollars only: the lines quoted in
    #: pence (SSAC, VWRL) are not used, so no unit can be mixed up.
    yahoo: str
    index: str
    #: One ID per fund across its share classes (VWRA and VWRL share one).
    fund_id: str
    domicile: str
    accumulating: bool
    venue: str
    currency: str = "USD"

    @property
    def distributing(self) -> bool:
        return not self.accumulating


#: The three Irish funds' ISINs are the plan's (section 6.5). The US-listed
#: funds' ISINs are as the provider lists them; each is to be checked on the
#: provider's page before a report is used for a filing (section 7.3), and an
#: empty ISIN prints as "n/a".
FUNDS: Final[tuple[Fund, ...]] = (
    Fund("VT", "Vanguard Total World Stock ETF", "US9220427424", "NYSE Arca", "VT",
         "FTSE Global All Cap", "VANGUARD-VT", US, False, US_LISTED),
    Fund("ACWI", "iShares MSCI ACWI ETF", "US4642882579", "Nasdaq", "ACWI",
         "MSCI ACWI", "ISHARES-ACWI-US", US, False, US_LISTED),
    Fund("VTI", "Vanguard Total Stock Market ETF", "US9229087690", "NYSE Arca", "VTI",
         "CRSP US Total Market", "VANGUARD-VTI", US, False, US_LISTED),
    Fund("ITOT", "iShares Core S&P Total U.S. Stock Market ETF", "US4642871507", "NYSE Arca", "ITOT",
         "S&P Total Market", "ISHARES-ITOT", US, False, US_LISTED),
    Fund("SCHB", "Schwab U.S. Broad Market ETF", "", "NYSE Arca", "SCHB",
         "Dow Jones U.S. Broad Stock Market", "SCHWAB-SCHB", US, False, US_LISTED),
    Fund("VXUS", "Vanguard Total International Stock ETF", "US9219097683", "Nasdaq", "VXUS",
         "FTSE Global All Cap ex US", "VANGUARD-VXUS", US, False, US_LISTED),
    Fund("IXUS", "iShares Core MSCI Total International Stock ETF", "US46434G1031", "Nasdaq", "IXUS",
         "MSCI ACWI ex USA IMI", "ISHARES-IXUS", US, False, US_LISTED),
    Fund("VWRA", "Vanguard FTSE All-World UCITS ETF (USD) Accumulating", "IE00BK5BQT80", "LSE", "VWRA.L",
         "FTSE All-World", "VANGUARD-FTSE-ALL-WORLD-UCITS", IRELAND, True, LSE_USD),
    Fund("ISAC", "iShares MSCI ACWI UCITS ETF (Acc)", "IE00B6R52259", "LSE", "ISAC.L",
         "MSCI ACWI", "ISHARES-MSCI-ACWI-UCITS", IRELAND, True, LSE_USD),
    Fund("IMID", "SPDR MSCI ACWI IMI UCITS ETF", "IE00B3YLTY66", "LSE", "IMID.L",
         "MSCI ACWI IMI", "SPDR-MSCI-ACWI-IMI-UCITS", IRELAND, True, LSE_USD),
)

BY_TICKER: Final[dict[str, Fund]] = {f.ticker: f for f in FUNDS}

#: Section 6.5: for a fund sold, the funds to suggest, in order. Each pair is
#: similar (the same broad market) and not identical (another index, or
#: another provider and index).
SUBSTITUTES: Final[dict[str, tuple[str, ...]]] = {
    "VT": ("VWRA", "IMID", "ACWI"),
    "VWRA": ("ISAC",),
    "ACWI": ("VT",),
    "VTI": ("ITOT", "SCHB"),
    "VXUS": ("IXUS",),
}

#: The first day VWRA has a price (section 7.4): money that went in before
#: it is shown as "n/a" for VWRA.
VWRA_FIRST_DAY_TEXT: Final[str] = "2019-07-23"

#: The line above which the US estate tax applies to a non-US person, in
#: dollars (a note on the report, not a rule).
US_ESTATE_TAX_LINE_USD: Final[float] = 60_000.0


def fund(ticker: str) -> Optional[Fund]:
    return BY_TICKER.get(ticker.strip().upper())


def identical(a: Fund, b: Fund) -> bool:
    """The same index or the same fund: never a harvest pair."""
    return a.index == b.index or a.fund_id == b.fund_id


def check_substitutes() -> None:
    """Refuse the table if any suggested pair is identical, or names an unknown fund."""
    for sold, suggested in SUBSTITUTES.items():
        if sold not in BY_TICKER:
            raise ValueError(f"{sold}: not in the fund table")
        for other in suggested:
            if other not in BY_TICKER:
                raise ValueError(f"{other}: not in the fund table")
            if identical(BY_TICKER[sold], BY_TICKER[other]):
                raise ValueError(f"{sold} and {other} share an index or a fund ID")


check_substitutes()


def domicile_switch(sold: Fund, bought: Fund) -> bool:
    """D12: a swap from a US-listed fund to an Irish one."""
    return sold.domicile == US and bought.domicile == IRELAND


# --------------------------------------------------------------------------- #
# Section 6.4: trading costs
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class CostTable:
    """Per side: a commission plus half the bid-ask spread, in dollars; plus the currency conversion."""

    #: A US-listed fund: $0.005 a share, at least $1.00, at most 1% of the trade; half the spread 0.01%.
    us_per_share: float = 0.005
    us_minimum: float = 1.00
    us_maximum_share: float = 0.01
    us_half_spread: float = 0.0001
    #: An Irish fund in dollars on the LSE: $4.00 up to $8,000, then 0.05% of the trade; half the spread 0.05%.
    lse_flat: float = 4.00
    lse_flat_up_to: float = 8_000.0
    lse_rate: float = 0.0005
    lse_half_spread: float = 0.0005
    #: Shekels to dollars: 0.002% of the amount, at least $2.00.
    fx_rate: float = 0.00002
    fx_minimum: float = 2.00

    def side_usd(self, fund: Optional[Fund], shares: float, price_usd: float) -> float:
        """One side (a sale or a purchase) of ``shares`` at ``price_usd``: commission plus half the spread."""
        value = shares * price_usd
        if shares <= 0 or value <= 0:
            return 0.0
        venue = fund.venue if fund is not None else US_LISTED
        if venue == LSE_USD:
            commission = self.lse_flat if value <= self.lse_flat_up_to else self.lse_rate * value
            return commission + self.lse_half_spread * value
        commission = min(max(self.us_per_share * shares, self.us_minimum), self.us_maximum_share * value)
        return commission + self.us_half_spread * value

    def conversion_usd(self, amount_usd: float) -> float:
        """Turning shekels into ``amount_usd`` dollars."""
        if amount_usd <= 0:
            return 0.0
        return max(self.fx_rate * amount_usd, self.fx_minimum)


DEFAULT_COSTS: Final[CostTable] = CostTable()
#: Fees 0 (section 8: the tests' default unless a case says otherwise).
NO_COSTS: Final[CostTable] = CostTable(us_per_share=0.0, us_minimum=0.0, us_half_spread=0.0, lse_flat=0.0,
                                       lse_rate=0.0, lse_half_spread=0.0, fx_rate=0.0, fx_minimum=0.0)

__all__ = ["BY_TICKER", "DEFAULT_COSTS", "FUNDS", "IRELAND", "LSE_USD", "NO_COSTS", "SUBSTITUTES", "US",
           "US_ESTATE_TAX_LINE_USD", "US_LISTED", "VWRA_FIRST_DAY_TEXT", "CostTable", "Fund", "check_substitutes",
           "domicile_switch", "fund", "identical"]
