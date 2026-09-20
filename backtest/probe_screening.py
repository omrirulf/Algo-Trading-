#!/usr/bin/env python3
"""Is the screening endpoint actually configured, and does it answer?

    python backtest/probe_screening.py

The screening stage is the one place in the cycle where a non-Claude model may
stand in, and it is configured by three environment variables. Every way that
goes wrong is silent:

  * the key is stored under a name nothing reads -- GEMINI_API_KEY rather than
    SCREENING_API_KEY -- and the screen stays on Haiku;
  * the key is set but SCREENING_BASE_URL is not, so nothing points at the
    endpoint the key is for, and the screen stays on Haiku;
  * all three are set but the endpoint refuses strict ``json_schema``, and
    every ticker falls through to the full model, which is the expensive
    failure rather than the dangerous one.

None of those raises. All three look exactly like "screening is off", which
is a legitimate state. So this asks out loud, and makes one real call through
the same ``OpenAICompatibleProvider`` the cycle uses, with the real signal
schema and ``reasoning=False``, because a probe that exercises a different
code path proves nothing about the one that runs.

**No key value is ever printed.** This output is meant to be safe to paste.

One request against a paid endpoint, so it costs a fraction of a cent.
Read-only. No orders, no trading, no journal written.

Exit status is 1 when the configuration is incoherent -- a key that reaches
nothing, a base URL with no model, an endpoint that will not answer -- and 0
when it is consistent, *including* all-blank, which means Haiku screens as
before.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.schemas import LLMSignal  # noqa: E402
from orchestrator.llm import (  # noqa: E402
    SCREENING_KEY_ENV_VARS,
    SCREENING_MODEL,
    LLMError,
    OpenAICompatibleProvider,
)

#: Enough of a ticker to be a fair test of the endpoint: the screen is asked
#: for a directional call over a short context, and the schema is the real
#: one, so a provider that only honours strict mode on trivial schemas fails
#: here rather than in a live cycle.
PROBE_SYSTEM = (
    "You screen equities. Answer with the JSON object the schema describes "
    "and nothing else."
)
PROBE_USER = (
    "PROBE\n\n"
    "This is a configuration check, not a real trading decision.\n"
    "Ticker PROBE. Return a valid signal object for it: bias NEUTRAL, low "
    "conviction, a one-line rationale."
)


def key_for() -> tuple[Optional[str], Optional[str]]:
    """``(name, value)`` of the first candidate spelling that is set."""
    for name in SCREENING_KEY_ENV_VARS:
        value = (os.environ.get(name) or "").strip()
        if value:
            return name, value
    return None, None


def _scrub(text: str, secret: Optional[str]) -> str:
    """An error body can echo the key back. This output is meant to be safe."""
    clean = " ".join(text.split())[:300]
    if secret and secret in clean:
        clean = clean.replace(secret, "<redacted>")
    return clean


def probe(base_url: str, model: str, key: Optional[str]) -> bool:
    """One real call. True when the endpoint answered in the schema."""
    provider = OpenAICompatibleProvider(base_url=base_url, model=model, api_key=key or "")
    started = time.monotonic()
    try:
        answer = provider.complete_detailed(
            PROBE_SYSTEM, PROBE_USER, LLMSignal.model_json_schema(),
            model=model, reasoning=False,
        )
    except LLMError as exc:
        print(f"  REFUSED  {_scrub(str(exc), key)}")
        print("  Every ticker would fall through to the full model: safe, but")
        print("  the screen would never run and nothing would be saved.")
        return False
    except Exception as exc:  # noqa: BLE001 - a probe reports, it does not raise
        print(f"  FAILED   {type(exc).__name__}: {_scrub(str(exc), key)}")
        return False

    elapsed = time.monotonic() - started
    print(f"  ANSWERED in {elapsed:.1f}s")
    try:
        signal = LLMSignal.model_validate_json(answer.text)
    except Exception as exc:  # noqa: BLE001
        print(f"  ...but not in the schema: {type(exc).__name__}")
        print(f"  raw: {_scrub(answer.text, key)}")
        return False
    print(f"  parsed: bias={signal.bias} conviction={signal.conviction}")
    usage = answer.usage
    if usage:
        print(f"  usage:  model={usage.model} in={usage.input_tokens} out={usage.output_tokens}")
        if usage.output_tokens > 2000:
            print("  NOTE: a large output for a one-line answer usually means the")
            print("  model reasoned anyway. Screening cost scales with this.")
    return True


def main() -> int:
    name, key = key_for()
    base_url = (os.environ.get("SCREENING_BASE_URL") or "").strip()
    model = (os.environ.get("SCREENING_MODEL") or "").strip()

    print("===== screening configuration =====")
    if key:
        print(f"  key found in {name} ({len(key)} characters)")
        if name != SCREENING_KEY_ENV_VARS[0]:
            print(f"  (the code reads {SCREENING_KEY_ENV_VARS[0]}; the workflow maps this onto it)")
    else:
        print(f"  no key -- looked for: {', '.join(SCREENING_KEY_ENV_VARS)}")
    print(f"  SCREENING_BASE_URL {'= ' + base_url if base_url else 'is not set'}")
    print(f"  SCREENING_MODEL    {'= ' + model if model else 'is not set'}")
    print()

    if not base_url and not model and not key:
        print(f"Screening is off. {SCREENING_MODEL} screens the watchlist, as it has been.")
        print("This is the supported default, not a fault.")
        return 0

    if not base_url:
        print("MISCONFIGURED: a key is set and nothing points at an endpoint.")
        print(f"  {SCREENING_MODEL} is still screening and the key is being paid for nothing.")
        print("  Set SCREENING_BASE_URL and SCREENING_MODEL, or remove the key.")
        return 1

    if not model:
        print("MISCONFIGURED: SCREENING_BASE_URL is set and SCREENING_MODEL is empty.")
        print("  screening_provider() raises on this, which fails the cycle.")
        return 1

    print(f"===== asking {model} =====")
    ok = probe(base_url, model, key)
    print()
    if not ok:
        print("The endpoint is configured and did not answer usably.")
        print("Do not rely on it until this passes; screening would cost more, not less.")
        return 1
    print("The endpoint answers in the schema.")
    print("That is not the same as agreeing with Haiku. Before trusting it:")
    print("  python replay/compare_screening.py \\")
    print(f"      --base-url {base_url} --model {model} --api-key <key> --limit 200")
    print("and read the escalation-recall number, not the agreement one.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
