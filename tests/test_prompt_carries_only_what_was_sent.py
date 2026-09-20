"""The fund prompt teaches only the sections the context actually carried.

Two properties, and the second is the one that pays for the first.

*Correctness*: a paragraph appears exactly when its section does. The model is
never told how to read a block it was not given, and never given a block
nothing told it how to read.

*Price*: the guidance is the cached prefix, so it has to stay byte-stable for
tickers that carry the same sections. A prompt assembled in a different order
per ticker would be a cache miss every call, which costs more than the
paragraphs save.
"""

from __future__ import annotations

import pytest

from orchestrator import heartbeat as hb
from orchestrator.context import (
    ENRICHMENT_SECTIONS,
    FUND_ONLY_SECTIONS,
    OPTIONAL_SECTIONS,
    TickerContext,
)

#: A fund, per config.instruments, and a single name.
FUND = "GLD"
COMPANY = "AAPL"


def _context(ticker: str = FUND, **sections) -> TickerContext:
    """A context carrying only the named sections; the rest are absent."""
    return TickerContext(ticker=ticker, headlines=[], **sections)


# --- correctness -----------------------------------------------------------


#: The paragraph itself is the marker. A section *name* is no good here: the
#: tail names them too, when it says which ones feed which score "whichever of
#: them are present" -- which stays true and is why the tail is not
#: conditional.
GUIDANCE = dict(hb.ETF_SECTION_GUIDANCE)


def test_a_section_the_context_lacks_takes_its_guidance_with_it():
    bare = hb.system_prompt_for(FUND, _context())
    for attr in ("crops", "energy", "flows", "outlook"):
        assert GUIDANCE[attr] not in bare


def test_a_section_the_context_carries_keeps_its_guidance():
    with_crops = hb.system_prompt_for(FUND, _context(crops=object()))
    assert GUIDANCE["crops"] in with_crops
    # ...and only that one.
    assert GUIDANCE["energy"] not in with_crops


@pytest.mark.parametrize("attr", sorted(GUIDANCE))
def test_each_paragraph_tracks_exactly_its_own_section(attr):
    assert GUIDANCE[attr] not in hb.system_prompt_for(FUND, _context())
    assert GUIDANCE[attr] in hb.system_prompt_for(FUND, _context(**{attr: object()}))


def test_the_head_and_tail_are_sent_whatever_the_context_carried():
    bare = hb.system_prompt_for(FUND, _context())
    assert "This is a fund holding many underlying positions" in bare
    assert "Setting conviction" in bare
    assert "are not read by the risk system" in bare
    # The conviction bar and the scoring rules are not optional.
    assert "Most cycles deserve NEUTRAL" in bare


def test_a_context_free_call_still_sends_everything():
    """What a caller holding only a symbol gets, and what the cycle sent before."""
    assert hb.system_prompt_for(FUND) == hb.ETF_SYSTEM_PROMPT
    assert hb.etf_system_prompt(None) == hb.ETF_SYSTEM_PROMPT


def test_a_single_name_is_unaffected():
    assert hb.system_prompt_for(COMPANY, _context(COMPANY)) == hb.SYSTEM_PROMPT
    assert hb.system_prompt_for(COMPANY) == hb.SYSTEM_PROMPT


# --- price -----------------------------------------------------------------


def test_two_tickers_with_the_same_sections_get_a_byte_identical_prefix():
    """Otherwise every ticker writes its own cache and none of them reads one."""
    a = hb.system_prompt_for(FUND, _context("GLD", macro=object(), carry=object()))
    b = hb.system_prompt_for("SLV", _context("SLV", carry=object(), macro=object()))
    assert a == b


def test_dropping_a_section_only_ever_shortens_the_prompt():
    full = hb.system_prompt_for(FUND, _context(**{a: object() for a, _ in hb.ETF_SECTION_GUIDANCE}))
    assert full == hb.ETF_SYSTEM_PROMPT
    for attr, _ in hb.ETF_SECTION_GUIDANCE:
        others = {a: object() for a, _ in hb.ETF_SECTION_GUIDANCE if a != attr}
        assert len(hb.system_prompt_for(FUND, _context(**others))) < len(full)


def test_the_paragraphs_a_bare_fund_sheds_are_worth_shedding():
    """The four sections no fund context has ever carried are most of the saving."""
    bare = hb.system_prompt_for(FUND, _context())
    assert len(hb.ETF_SYSTEM_PROMPT) - len(bare) > 4000


# --- drift -----------------------------------------------------------------


def test_every_guided_attribute_is_a_real_optional_section():
    """A paragraph keyed to a field that does not exist would never render."""
    fields = set(TickerContext.__dataclass_fields__)
    for attr, _ in hb.ETF_SECTION_GUIDANCE:
        assert attr in fields, attr
        assert attr in OPTIONAL_SECTIONS, f"{attr} is always sent; its guidance cannot be conditional"


def test_every_fund_section_that_can_be_absent_is_accounted_for():
    """A new fund section must arrive with guidance, or be a deliberate omission.

    Without this, adding a section to ``context.py`` would quietly send the
    model data no paragraph explains -- the exact failure this file exists to
    prevent, one release later.
    """
    guided = {attr for attr, _ in hb.ETF_SECTION_GUIDANCE}
    rendered_for_funds = {
        attr for _, attr in ENRICHMENT_SECTIONS if attr in FUND_ONLY_SECTIONS
    }
    assert rendered_for_funds == guided, (
        "fund sections with no guidance paragraph: "
        f"{sorted(rendered_for_funds - guided)}"
    )
