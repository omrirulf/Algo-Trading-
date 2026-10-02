"""Every number the Israeli tax rules use, in one place.

The owner's instruction of 2 Oct 2026: the after-tax gate (pre-registration
section 5c) and the after-tax and shekel reports (section 11.9) apply the
rules below, never a flat 25%, and every number they use lives in this one
file. ``analysis.israel_tax`` reads nothing else.

The rules, as the owner wrote them (2 Oct 2026):

a. A gain or loss on a USD security is measured in shekels, with the
   exchange rate as the index (Income Tax Ordinance s.88; Tax Authority
   Circular 10/2025). cost_ILS = cost_USD x fx_buy, proceeds_ILS =
   proceeds_USD x fx_sell, nominal = proceeds_ILS - cost_ILS, inflationary
   amount = cost_ILS x (fx_sell / fx_buy - 1). A nominal gain is taxed
   after the inflationary amount, when positive, is taken off it; a nominal
   loss is allowed after the inflationary amount, when negative, is taken
   off it. So the tax is on the smaller of the shekel gain and the dollar
   gain at the sale-day rate, and a loss made only by the exchange rate is
   not deductible.
b. 25%. A surtax, as parameters: 3% on taxable income above the line, plus
   2% on capital income above the same line. Off by default at these
   account sizes.
c. FIFO lots, per account. Every reinvested dividend is a new lot.
d. Dividends: Israeli tax is 25% of the gross shekel amount, with a credit
   for the US tax withheld (25% with a W-8BEN); the extra Israeli tax is the
   difference, usually 0.
e. This year's capital losses go first against this year's capital gains.
   ``OFFSET_LOSSES_VS_DIVIDENDS`` (default on: the harsher case for an
   actively traded fund, until the accountant answers) also sets a year's
   net capital loss against that year's dividends. What is left carries
   forward against future capital gains only, nominal, with no expiry.
f. The rate is the Bank of Israel's representative rate on the trade date
   (``FX_SOURCE``); another source only for a day the Bank did not publish,
   and every such day is counted (``analysis.boi_rates``).

No personal number lives here, ever: the owner's salary is an input to the
surtax and is 0 in this file; a real figure is passed by the caller and is
never written to the repository, a log, an artifact or a phone message.
"""

from __future__ import annotations

from typing import Final

#: Rule b: capital gains, per shekel of taxable real gain.
CAPITAL_GAINS_RATE: Final[float] = 0.25

#: Rule d: Israeli tax on a dividend, per shekel of its gross amount.
DIVIDEND_RATE: Final[float] = 0.25
#: Rule d: the US tax withheld from a dividend with a W-8BEN on file (the
#: treaty rate), and without one.
US_WITHHOLDING_W8BEN: Final[float] = 0.25
US_WITHHOLDING_NO_W8BEN: Final[float] = 0.30
#: Whether a W-8BEN is on file. The funds and the paper account assume it is.
W8BEN_FILED: Final[bool] = True

#: Rule e: whether a year's net capital loss is also set against that year's
#: dividends. On by default -- the harsher case for an actively traded fund,
#: whose losses then shield dividends already credited with US tax instead
#: of carrying forward -- until the accountant answers
#: (``docs/research/cpa-questions.md``, question 1).
OFFSET_LOSSES_VS_DIVIDENDS: Final[bool] = True
#: Rule e: a loss carried forward never expires (``None``) and is used
#: against future capital gains only, at its nominal shekel amount.
CARRY_FORWARD_YEARS: Final[None] = None

#: Rule b: the surtax, as parameters. Off by default: at these account sizes
#: (a $100,000 book) it cannot apply unless the owner's other income is
#: already near the line, and that income is not the repository's to know.
SURTAX_ENABLED: Final[bool] = False
#: The line, in shekels of annual taxable income (2026).
SURTAX_THRESHOLD_ILS: Final[float] = 721_560.0
#: 3% on taxable income above the line.
SURTAX_RATE: Final[float] = 0.03
#: Plus 2% on capital income above the same line.
SURTAX_CAPITAL_RATE: Final[float] = 0.02
#: The owner's salary for the surtax: an input, 0 here. Never commit a real one.
SALARY_ILS: Final[float] = 0.0

#: Rule c: the order lots are sold in, per account.
LOT_METHOD: Final[str] = "FIFO"

#: Rule f: where the exchange rate comes from.
FX_SOURCE: Final[str] = "Bank of Israel representative rate (USD/ILS), on the trade date"
#: Only for a day the Bank of Israel did not publish: the European Central
#: Bank's reference rates, crossed through the euro (USD/ILS = EUR/ILS divided
#: by EUR/USD). Every such day is counted.
FX_FALLBACK_SOURCE: Final[str] = "European Central Bank reference rates, crossed through EUR"

#: The tax year: the calendar year.
TAX_YEAR_STARTS: Final[tuple[int, int]] = (1, 1)

__all__ = [
    "CAPITAL_GAINS_RATE", "CARRY_FORWARD_YEARS", "DIVIDEND_RATE", "FX_FALLBACK_SOURCE", "FX_SOURCE",
    "LOT_METHOD", "OFFSET_LOSSES_VS_DIVIDENDS", "SALARY_ILS", "SURTAX_CAPITAL_RATE", "SURTAX_ENABLED",
    "SURTAX_RATE", "SURTAX_THRESHOLD_ILS", "TAX_YEAR_STARTS", "US_WITHHOLDING_NO_W8BEN",
    "US_WITHHOLDING_W8BEN", "W8BEN_FILED",
]
