"""The HTML page: what it shows, and what it refuses to show.

Most of these pin absences rather than presences. A dashboard's failure mode is
not a crash -- it is rendering a confident number nobody can source, so the
tests that matter are the ones proving it stays quiet without the input.
"""

from __future__ import annotations

import pytest

from analysis import dashboard as db
from analysis import portfolio as pf


def book(*positions, **kw) -> pf.Book:
    return pf.Book(positions=tuple(positions), **kw)


LONG = pf.Position("LLY", "buy", 10, 100.0, 90.0, opened="2026-09-16 16:35:00")
SHORT = pf.Position("TLT", "sell", 10, 100.0, 110.0, opened="2026-09-16 16:35:00")


# --- the page holds together ---------------------------------------------


def test_the_page_carries_its_own_title():
    assert f"<title>{db.TITLE}</title>" in db.render(book(LONG))


def test_the_page_brings_no_document_skeleton():
    """The artifact host wraps the file; a second <html> would nest documents."""
    page = db.render(book(LONG)).lower()
    for tag in ("<!doctype", "<html", "<head>", "<body"):
        assert tag not in page


def test_an_empty_book_renders_a_page_rather_than_failing():
    page = db.render(book())
    assert "No open positions in the record" in page
    assert f"<title>{db.TITLE}</title>" in page


def test_every_colour_token_is_defined_before_any_dark_block():
    """The classic unreadable-artifact bug.

    A token whose only definition sits inside a media query or a [data-theme]
    block is undefined in the un-stamped "system" state, which is what most
    viewers get -- one theme's text on the other theme's ground.
    """
    style = db.STYLE
    base = style.split("@media", 1)[0]
    used = set(
        part.split(")")[0].strip()
        for part in style.split("var(")[1:]
    )
    declared = set(
        line.split(":", 1)[0].strip()
        for line in base.splitlines()
        if line.strip().startswith("--")
    )
    assert used, "the stylesheet should be built on tokens"
    assert used <= declared, f"defined only in a dark block: {sorted(used - declared)}"


def test_the_body_paints_its_own_background():
    """A transparent body borrows the host's ground and inverts on one theme."""
    assert "background: var(--ground)" in db.STYLE


def test_content_from_the_record_is_escaped():
    """Tickers come out of a file, and a file is not a trusted template."""
    nasty = pf.Position("<script>x</script>", "buy", 1, 10.0, 9.0)
    page = db.render(book(nasty))
    assert "<script>x</script>" not in page
    assert "&lt;script&gt;" in page


# --- what it refuses to show without an input ----------------------------


def test_no_price_means_no_unrealised_column():
    page = db.render(book(LONG))
    assert "Unrealised" not in page.split("Not shown yet")[0]
    assert "No live prices" in page


def test_supplying_prices_brings_the_unrealised_column_back():
    page = db.render(book(LONG, prices={"LLY": 120.0}))
    assert "Unrealised" in page
    assert "+2.00R" in page, "an R multiple is the number the ladder is written in"
    assert "No live prices" not in page


def test_without_equity_the_page_says_which_number_is_missing():
    page = db.render(book(LONG, SHORT))
    assert "Cap use needs your account equity" in page
    assert "of book" in page, "share of book is exact and should still be shown"


def test_with_equity_the_bars_become_cap_relative():
    page = db.render(book(LONG, SHORT, equity=10_000.0))
    assert "Cap use needs your account equity" not in page
    assert "of equity" in page
    assert "cap" in page


def test_a_breached_cap_is_called_out_in_words_not_only_colour():
    """Colour alone fails a colourblind reader and a printed page."""
    page = db.render(book(pf.Position("TLT", "sell", 100, 100.0, 110.0), equity=10_000.0))
    assert "over by" in page


# --- the chart floor ------------------------------------------------------


def test_a_short_history_says_so_instead_of_drawing_a_trend():
    page = db.render(book(LONG), days_of_history=2)
    assert f"Charts need about {db.CHART_MIN_DAYS} days; there are 2" in page


def test_enough_history_drops_the_chart_notice():
    page = db.render(book(LONG, prices={"LLY": 110.0}), days_of_history=40)
    assert "Charts need about" not in page
    assert "Not shown yet" not in page, "with nothing withheld the section goes away"


# --- the book table -------------------------------------------------------


def test_direction_is_carried_by_the_word_not_only_the_colour():
    page = db.render(book(LONG, SHORT))
    assert ">Long<" in page and ">Short<" in page


def test_a_protected_position_is_labelled():
    protected = pf.Position("LLY", "buy", 10, 100.0, 90.0, current_stop=105.0)
    assert "protected" in db.render(book(protected))


def test_positions_are_listed_largest_first():
    small = pf.Position("TIP", "sell", 1, 10.0, 11.0)
    page = db.render(book(small, LONG))
    assert page.index("LLY") < page.index("TIP")


def test_a_taken_rung_is_marked_on_the_ladder():
    stepped = pf.Position("LLY", "buy", 6, 100.0, 90.0, rungs_taken=1)
    page = db.render(book(stepped))
    assert '<b class="on">' in page


def test_the_wide_table_can_scroll_without_the_page_doing_so():
    assert '<div class="scroll">' in db.render(book(LONG))


# --- inputs ---------------------------------------------------------------


def test_prices_are_parsed_from_the_command_line():
    assert db._prices_from("LLY=120.5,tlt=80") == {"LLY": 120.5, "TLT": 80.0}


def test_an_unreadable_price_is_refused_rather_than_ignored():
    """Silently dropping it would show a book with one position unmarked."""
    with pytest.raises(SystemExit):
        db._prices_from("LLY=not-a-number")


def test_no_prices_is_an_empty_mapping_not_an_error():
    assert db._prices_from(None) == {} and db._prices_from("") == {}


def test_the_history_count_survives_a_missing_journal(tmp_path):
    assert db._days_of_history(tmp_path / "absent.log") == 0


def test_the_history_count_is_distinct_days(tmp_path):
    path = tmp_path / "journal.log"
    path.write_text(
        '{"ts_utc": "2026-09-15T16:00:00Z"}\n'
        '{"ts_utc": "2026-09-15T17:00:00Z"}\n'
        '{"ts_utc": "2026-09-16T16:00:00Z"}\n'
        "not json\n",
        encoding="utf-8",
    )
    assert db._days_of_history(path) == 2


def test_the_cli_prints_the_page_to_stdout(tmp_path, capsys):
    """stdout only. ``analysis/`` may read the record and may not write."""
    audit = tmp_path / "audit.log"
    audit.write_text(
        '{"ts": "2026-09-16 16:35:00", "event": "signal_processed", "result": '
        '{"ticker": "LLY", "side": "buy", "quantity": 4, "status": "ACCEPTED", '
        '"entry_price": 100.0, "stop_price": 90.0}}\n',
        encoding="utf-8",
    )
    assert db.main(["--audit", str(audit)]) == 0
    assert "Position Book" in capsys.readouterr().out


def test_the_renderer_offers_no_way_to_write_a_file():
    """Pinned, because a --out flag is the obvious thing to add back.

    ``analysis/`` is read-only by construction and CI fails the build on a
    write from this package. The redirect belongs to the caller.
    """
    import inspect

    source = inspect.getsource(db)
    assert "write_text" not in source
    assert "--out" not in source
