"""The owner's files (section 3): read, checked, and refused when they are not marked.

Five CSV files in the folder ``--data`` names, each with ``# SAMPLE`` or the
private marker as its first line (``investor.PRIVATE_MARKER``) and the column
names on the second:

* ``accounts.csv`` -- ``name,kind,currency``: one row per account, ``kind``
  ``taxable`` (a broker: lots in dollars) or ``tax_free`` (a keren
  hishtalmut or a kupat gemel lehashkaa: tracks in shekels).
* ``transactions.csv`` -- one row per event, in the order they happened:
  ``date,account,kind,ticker,quantity,price_usd,fee_usd,amount,currency,
  withheld_usd,fx,to_account,bought_on,note``.
* ``tax_free.csv`` -- ``date,account,track,value_ils``: a tax-free account's
  value per track on a day; the latest row of each track counts.
* ``plan.csv`` -- ``item,name,class,value,as_of``, one row per fact:
  ``target`` (a class's percent), ``fund`` (a fund's class), ``track`` (a
  tax-free track's mix, ``name`` as ``account:track``, one row per class),
  ``buy_first`` (the fund to buy for a class), ``contribution`` (an
  account's new money this month, ``value`` as an amount and a currency),
  ``carry_in`` (the loss carried in from the last assessment, ``as_of`` its
  year), ``surtax`` (``on`` or ``off``), ``other_income`` (the year's other
  taxable income, for the surtax), ``expect_gains_within_3_years`` and
  ``w8ben_filed`` (``yes`` or ``no``, dated), and ``pending`` (a track
  change already asked for: ``name`` as ``account:from>account:to``).
* ``payments.csv`` -- optional: ``date,year,half,amount_ils``: tax actually
  paid (``half`` 1 or 2 for an advance, ``annual`` for the year's balance).

An error names the file and the row, never a value (section 2.6).
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Final, Optional

from investor import PRIVATE_MARKER, REPOSITORY, SAMPLE_MARKER

TAXABLE: Final[str] = "taxable"
TAX_FREE: Final[str] = "tax_free"
KINDS: Final[tuple[str, ...]] = ("buy", "sell", "dividend", "deposit", "withdrawal", "fee", "transfer", "transfer_in")

FILES: Final[tuple[str, ...]] = ("accounts.csv", "transactions.csv", "tax_free.csv", "plan.csv")
OPTIONAL_FILES: Final[tuple[str, ...]] = ("payments.csv",)


class DataError(ValueError):
    """A file the engine refuses. Its text names a file and a row, never a value."""

    def __init__(self, file: str, row: Optional[int], kind: str) -> None:
        self.file, self.row, self.kind = file, row, kind
        where = f"{file}, row {row}" if row is not None else file
        super().__init__(f"{where}: {kind}")


@dataclass(frozen=True)
class Account:
    name: str
    kind: str
    currency: str

    @property
    def taxable(self) -> bool:
        return self.kind == TAXABLE


@dataclass(frozen=True)
class Transaction:
    row: int
    day: date
    account: str
    kind: str
    ticker: str = ""
    quantity: float = 0.0
    price_usd: float = 0.0
    fee_usd: float = 0.0
    amount: float = 0.0
    currency: str = ""
    withheld_usd: Optional[float] = None
    fx: Optional[float] = None
    to_account: str = ""
    bought_on: Optional[date] = None


@dataclass(frozen=True)
class TrackValue:
    row: int
    day: date
    account: str
    track: str
    value_ils: float


@dataclass(frozen=True)
class Payment:
    row: int
    day: date
    year: int
    half: str
    amount_ils: float


@dataclass(frozen=True)
class Dated:
    """A yes/no the owner answered on a day (the report reminds them when it is over a year old)."""

    value: bool
    as_of: Optional[date]


@dataclass
class Plan:
    targets: dict[str, float] = field(default_factory=dict)
    classes: dict[str, str] = field(default_factory=dict)
    track_mix: dict[tuple[str, str], dict[str, float]] = field(default_factory=dict)
    buy_first: dict[str, str] = field(default_factory=dict)
    #: account -> (amount, currency)
    contributions: dict[str, tuple[float, str]] = field(default_factory=dict)
    carry_in: float = 0.0
    carry_in_year: Optional[int] = None
    surtax: bool = False
    other_income_ils: float = 0.0
    other_income_year: Optional[int] = None
    expect_gains: Dated = Dated(False, None)
    w8ben: Dated = Dated(True, None)
    #: (account, from track, to track, amount in shekels, the day it was asked for)
    pending: list[tuple[str, str, str, float, Optional[date]]] = field(default_factory=list)

    def class_of(self, ticker: str) -> Optional[str]:
        return self.classes.get(ticker)


@dataclass
class Inputs:
    accounts: dict[str, Account]
    transactions: list[Transaction]
    tracks: list[TrackValue]
    plan: Plan
    payments: list[Payment]
    #: ``SAMPLE`` or ``PRIVATE``: every file carried the same marker.
    marker: str


# --------------------------------------------------------------------------- #
# Reading
# --------------------------------------------------------------------------- #


def inside_repository(path: Path) -> bool:
    try:
        path.resolve().relative_to(REPOSITORY)
    except ValueError:
        return False
    return True


def _rows(path: Path) -> tuple[str, list[dict[str, str]]]:
    """The file's marker and its rows; a file without a marker line is refused."""
    name = path.name
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise DataError(name, None, f"cannot be read ({type(exc).__name__})") from None
    lines = text.splitlines()
    if not lines or lines[0].strip() not in (SAMPLE_MARKER, PRIVATE_MARKER):
        raise DataError(name, 1, "the first line is not the sample or the private marker")
    marker = "SAMPLE" if lines[0].strip() == SAMPLE_MARKER else "PRIVATE"
    body = [line for line in lines[1:] if line.strip() and not line.lstrip().startswith("#")]
    rows = list(csv.DictReader(body))
    for number, row in enumerate(rows, start=1):
        if None in row or any(k is None for k in row):
            raise DataError(name, number, "a row has more cells than the header")
    return marker, rows


def _day(text: str, file: str, row: int, what: str = "date") -> date:
    try:
        return date.fromisoformat(text.strip())
    except ValueError:
        raise DataError(file, row, f"the {what} is not a date (YYYY-MM-DD)") from None


def _number(text: str, file: str, row: int, what: str, default: Optional[float] = 0.0) -> Optional[float]:
    text = (text or "").strip().replace(",", "")
    if not text:
        if default is None:
            return None
        return default
    try:
        return float(text)
    except ValueError:
        raise DataError(file, row, f"{what} is not a number") from None


def read_accounts(path: Path) -> tuple[str, dict[str, Account]]:
    marker, rows = _rows(path)
    out: dict[str, Account] = {}
    for number, row in enumerate(rows, start=1):
        name = (row.get("name") or "").strip()
        kind = (row.get("kind") or "").strip()
        currency = (row.get("currency") or "").strip().upper()
        if not name or kind not in (TAXABLE, TAX_FREE) or currency not in ("USD", "ILS"):
            raise DataError(path.name, number, "an account needs a name, a kind (taxable or tax_free) and a currency")
        if name in out:
            raise DataError(path.name, number, "an account is listed twice")
        out[name] = Account(name, kind, currency)
    if not out:
        raise DataError(path.name, None, "no accounts")
    return marker, out


def read_transactions(path: Path, accounts: dict[str, Account]) -> tuple[str, list[Transaction]]:
    marker, rows = _rows(path)
    out: list[Transaction] = []
    file = path.name
    for number, row in enumerate(rows, start=1):
        kind = (row.get("kind") or "").strip()
        if kind not in KINDS:
            raise DataError(file, number, "an unknown kind of event")
        account = (row.get("account") or "").strip()
        if account not in accounts:
            raise DataError(file, number, "an account that is not in accounts.csv")
        day = _day(row.get("date") or "", file, number)
        ticker = (row.get("ticker") or "").strip().upper()
        quantity = _number(row.get("quantity") or "", file, number, "the quantity")
        price = _number(row.get("price_usd") or "", file, number, "the price")
        fee = _number(row.get("fee_usd") or "", file, number, "the fee")
        amount = _number(row.get("amount") or "", file, number, "the amount")
        currency = (row.get("currency") or "").strip().upper()
        withheld = _number(row.get("withheld_usd") or "", file, number, "the US tax withheld", default=None)
        fx = _number(row.get("fx") or "", file, number, "the rate", default=None)
        to_account = (row.get("to_account") or "").strip()
        bought_text = (row.get("bought_on") or "").strip()
        bought_on = _day(bought_text, file, number, "bought_on") if bought_text else None
        if kind in ("buy", "sell", "transfer_in"):
            if not ticker or quantity <= 0 or price <= 0:
                raise DataError(file, number, "a trade needs a ticker, a positive quantity and a positive price")
            if fee < 0:
                raise DataError(file, number, "a fee is not negative")
            if kind == "transfer_in" and bought_on is None:
                raise DataError(file, number, "a transfer_in needs the lot's purchase day in bought_on")
        if kind == "dividend":
            if not ticker or amount <= 0:
                raise DataError(file, number, "a dividend needs a ticker and a positive gross amount")
            if currency and currency != "USD":
                raise DataError(file, number, "a dividend of a fund not quoted in dollars is refused")
            currency = "USD"
            if withheld is not None and not 0 <= withheld <= amount:
                raise DataError(file, number, "the US tax withheld is between 0 and the gross dividend")
        if kind in ("deposit", "withdrawal", "fee"):
            if amount <= 0 or currency not in ("USD", "ILS"):
                raise DataError(file, number, "a cash event needs a positive amount and a currency (USD or ILS)")
        if kind == "transfer":
            if to_account not in accounts or to_account == account:
                raise DataError(file, number, "a transfer needs another of the owner's accounts in to_account")
            if ticker:
                if quantity <= 0:
                    raise DataError(file, number, "a transfer of shares needs a positive quantity")
            elif amount <= 0 or currency not in ("USD", "ILS"):
                raise DataError(file, number, "a transfer of cash needs a positive amount and a currency")
        if fx is not None and fx <= 0:
            raise DataError(file, number, "a rate override must be positive")
        if out and day < out[-1].day:
            raise DataError(file, number, "the events are not in the order they happened")
        out.append(Transaction(number, day, account, kind, ticker, quantity, price, fee, amount, currency,
                               withheld, fx, to_account, bought_on))
    return marker, out


def read_tracks(path: Path, accounts: dict[str, Account]) -> tuple[str, list[TrackValue]]:
    marker, rows = _rows(path)
    out: list[TrackValue] = []
    for number, row in enumerate(rows, start=1):
        account = (row.get("account") or "").strip()
        if account not in accounts or accounts[account].taxable:
            raise DataError(path.name, number, "a track belongs to a tax_free account of accounts.csv")
        track = (row.get("track") or "").strip()
        value = _number(row.get("value_ils") or "", path.name, number, "the value")
        if not track or value < 0:
            raise DataError(path.name, number, "a track needs a name and a value that is not negative")
        out.append(TrackValue(number, _day(row.get("date") or "", path.name, number), account, track, value))
    return marker, out


def _yes_no(text: str, file: str, row: int) -> bool:
    value = (text or "").strip().lower()
    if value in ("yes", "on", "true", "1"):
        return True
    if value in ("no", "off", "false", "0"):
        return False
    raise DataError(file, row, "expected yes or no")


def read_plan(path: Path, accounts: dict[str, Account]) -> tuple[str, Plan]:
    marker, rows = _rows(path)
    plan = Plan()
    file = path.name
    for number, row in enumerate(rows, start=1):
        item = (row.get("item") or "").strip()
        name = (row.get("name") or "").strip()
        klass = (row.get("class") or "").strip()
        value = (row.get("value") or "").strip()
        as_of_text = (row.get("as_of") or "").strip()
        as_of = _day(as_of_text, file, number, "as_of") if as_of_text and item not in ("carry_in", "other_income") else None
        if item == "target":
            if not klass:
                raise DataError(file, number, "a target needs a class")
            plan.targets[klass] = _number(value, file, number, "the target")
        elif item == "fund":
            if not name or not klass:
                raise DataError(file, number, "a fund row needs the ticker and its class")
            plan.classes[name.upper()] = klass
        elif item == "track":
            if ":" not in name or not klass:
                raise DataError(file, number, "a track row needs account:track and a class")
            account, track = (part.strip() for part in name.split(":", 1))
            if account not in accounts or accounts[account].taxable:
                raise DataError(file, number, "a track belongs to a tax_free account of accounts.csv")
            plan.track_mix.setdefault((account, track), {})[klass] = _number(value, file, number, "the mix")
        elif item == "buy_first":
            if not klass or not value:
                raise DataError(file, number, "buy_first needs a class and a ticker")
            plan.buy_first[klass] = value.upper()
        elif item == "contribution":
            if name not in accounts:
                raise DataError(file, number, "a contribution names an account of accounts.csv")
            parts = value.split()
            amount = _number(parts[0] if parts else "", file, number, "the contribution")
            currency = parts[1].upper() if len(parts) > 1 else accounts[name].currency
            if amount < 0 or currency not in ("USD", "ILS"):
                raise DataError(file, number, "a contribution is an amount that is not negative, and a currency")
            plan.contributions[name] = (amount, currency)
        elif item == "carry_in":
            plan.carry_in = _number(value, file, number, "the loss carried in")
            if plan.carry_in > 0:
                raise DataError(file, number, "a loss carried in is 0 or negative")
            if not as_of_text.isdigit():
                raise DataError(file, number, "carry_in needs the year it was carried out of in as_of")
            plan.carry_in_year = int(as_of_text)
        elif item == "surtax":
            plan.surtax = _yes_no(value, file, number)
        elif item == "other_income":
            plan.other_income_ils = _number(value, file, number, "the other income")
            plan.other_income_year = int(as_of_text) if as_of_text.isdigit() else None
        elif item == "expect_gains_within_3_years":
            plan.expect_gains = Dated(_yes_no(value, file, number), as_of)
        elif item == "w8ben_filed":
            plan.w8ben = Dated(_yes_no(value, file, number), as_of)
        elif item == "pending":
            if ">" not in name:
                raise DataError(file, number, "a pending move is written account:from>account:to")
            left, right = (part.strip() for part in name.split(">", 1))
            if ":" not in left or ":" not in right:
                raise DataError(file, number, "a pending move is written account:from>account:to")
            account, from_track = (p.strip() for p in left.split(":", 1))
            account_to, to_track = (p.strip() for p in right.split(":", 1))
            if account != account_to or account not in accounts or accounts[account].taxable:
                raise DataError(file, number, "a pending move stays inside one tax_free account")
            plan.pending.append((account, from_track, to_track, _number(value, file, number, "the amount"), as_of))
        else:
            raise DataError(file, number, "an unknown plan item")
    for (account, track), mix in plan.track_mix.items():
        if abs(sum(mix.values()) - 100.0) > 1e-6:
            raise DataError(file, None, "a track's mix does not add up to 100")
    return marker, plan


def read_payments(path: Path) -> tuple[str, list[Payment]]:
    marker, rows = _rows(path)
    out: list[Payment] = []
    for number, row in enumerate(rows, start=1):
        half = (row.get("half") or "").strip().lower()
        year_text = (row.get("year") or "").strip()
        if half not in ("1", "2", "annual") or not year_text.isdigit():
            raise DataError(path.name, number, "a payment needs a year and a half (1, 2 or annual)")
        amount = _number(row.get("amount_ils") or "", path.name, number, "the amount")
        out.append(Payment(number, _day(row.get("date") or "", path.name, number), int(year_text), half, amount))
    return marker, out


def read_folder(data: Path) -> Inputs:
    """Every file of the folder, checked. Refuses a folder inside this repository (section 2.6)."""
    data = Path(data)
    if inside_repository(data):
        raise DataError(str(data.name), None, "the data folder is inside the repository; real numbers never live here")
    if not data.is_dir():
        raise DataError(str(data.name), None, "the data folder does not exist")
    markers: set[str] = set()
    marker, accounts = read_accounts(data / "accounts.csv")
    markers.add(marker)
    marker, transactions = read_transactions(data / "transactions.csv", accounts)
    markers.add(marker)
    marker, tracks = read_tracks(data / "tax_free.csv", accounts)
    markers.add(marker)
    marker, plan = read_plan(data / "plan.csv", accounts)
    markers.add(marker)
    payments: list[Payment] = []
    if (data / "payments.csv").exists():
        marker, payments = read_payments(data / "payments.csv")
        markers.add(marker)
    if len(markers) != 1:
        raise DataError("the folder", None, "the files do not all carry the same marker")
    return Inputs(accounts, transactions, tracks, plan, payments, markers.pop())


__all__ = ["Account", "DataError", "Dated", "FILES", "Inputs", "KINDS", "OPTIONAL_FILES", "Payment", "Plan",
           "TAXABLE", "TAX_FREE", "TrackValue", "Transaction", "inside_repository", "read_accounts", "read_folder",
           "read_payments", "read_plan", "read_tracks", "read_transactions"]
