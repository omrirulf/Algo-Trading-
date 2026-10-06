"""Production's model request and answer parsing, pinned byte for byte.

The owner's instruction of 6 Oct 2026 (item 3), for PR #142: that PR added
one read-only method to the production model-call code
(``OpenAICompatibleProvider.request_body``, for the voting arm). These tests
show that the request production sends is byte-identical before and after
it, for a fixed input, and that production's answer parsing gives the same
results.

``observe()`` sends fixed contexts through the production path
(``heartbeat.call_llm``, the provider, httpx) to a fake server, and hashes:

- every request body exactly as it went on the wire (the key is in a header,
  never in the body; the header is checked, not hashed);
- the method, URL and content type of every request;
- what production parsed out of fixed answers: the completion and its token
  counts, ``parse_signal``, ``repair_transparency`` and
  ``scores_without_a_source``.

``GOLDEN`` holds the values ``observe()`` gave on the base commit 1ac931f
(main before PR #142), computed there and copied here. A failure means that
production's request or parsing changed: change ``GOLDEN`` only with the
owner's knowledge, and write the change down.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

import httpx

from orchestrator import heartbeat as hb
from orchestrator import llm, technicals
from orchestrator.context import NEWS_GAP_PREFIX, TickerContext

#: ``heartbeat.prompt_fingerprint()`` on main before PR #142, and on every
#: production cycle line since 27 Sep 2026 (``model_setup.prompt``).
FINGERPRINT = "6c59e07de87e"

#: ``observe()`` on the base commit 1ac931f.
GOLDEN: dict[str, str] = {
    "MSFT.invalid_values_then_valid.1.body":
        "a65cdd28b9f4bb1388b9cdf7d258b997982904b25a216b5e61b6c0072b6d6345",
    "MSFT.invalid_values_then_valid.1.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "MSFT.invalid_values_then_valid.2.body":
        "c8f53afed54f36c3e71da3546975f25a5ef2cd637ed4611aba8305d93a7f6300",
    "MSFT.invalid_values_then_valid.2.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "MSFT.invalid_values_then_valid.completion":
        "261df4e219bdadb98a432e4048fdc17ff9b5860be9ccdc06c3de83fb0c12c4a4",
    "MSFT.invalid_values_then_valid.parsed":
        "be5cba4370e5835e106852d3120949f208b5dabb7d9ceebec880541df6efca30",
    "MSFT.invalid_values_then_valid.requests": "2",
    "MSFT.off_schema_then_valid.1.body":
        "a65cdd28b9f4bb1388b9cdf7d258b997982904b25a216b5e61b6c0072b6d6345",
    "MSFT.off_schema_then_valid.1.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "MSFT.off_schema_then_valid.2.body":
        "f21710fb747df459cc34874a9b5e9cc8078ad0f13c146c48c254e6cddbda4812",
    "MSFT.off_schema_then_valid.2.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "MSFT.off_schema_then_valid.completion":
        "13e52b487fe54b62adeea8b458c1c7b775bc2b428f3783a6ba5a63d15819f598",
    "MSFT.off_schema_then_valid.parsed":
        "be5cba4370e5835e106852d3120949f208b5dabb7d9ceebec880541df6efca30",
    "MSFT.off_schema_then_valid.requests": "2",
    "MSFT.scores_without_a_source":
        "15846cbf0fc597a284bfc85f01915832b3ab903b60238eb8137c81412714f879",
    "MSFT.system_prompt":
        "1f15d7ba43cefc850eb7d703d3ffe6b8484addf6dbfb128dbda78665bf90772c",
    "MSFT.user_prompt": "b64a21870bc85a44362cd4494c032ffa25f2dcd7a6922465f4887fffc15478cc",
    "MSFT.valid.1.body":
        "a65cdd28b9f4bb1388b9cdf7d258b997982904b25a216b5e61b6c0072b6d6345",
    "MSFT.valid.1.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "MSFT.valid.completion":
        "2e15b803098ae21f8f11cb10a206ea787c96836f85227ad75d372c6576879782",
    "MSFT.valid.parsed":
        "be5cba4370e5835e106852d3120949f208b5dabb7d9ceebec880541df6efca30",
    "MSFT.valid.requests": "1",
    "TLT.invalid_values_then_valid.1.body":
        "744f8215abf4acf065f8eb9bf40441be92432a63db7820a5fc72979485ecc8a4",
    "TLT.invalid_values_then_valid.1.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "TLT.invalid_values_then_valid.2.body":
        "5a3ed931785de8b73d5aae6a4951aecc8dee14b21956858052ea3e4491beb81f",
    "TLT.invalid_values_then_valid.2.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "TLT.invalid_values_then_valid.completion":
        "5e792c59e818434085d732eeaae4272ae4e9f99573250770bc4dd6ecd91b2554",
    "TLT.invalid_values_then_valid.parsed":
        "0368d09691c6f24742248005b5b3d8838942d251f7b7bb6dbb20f5c24ab45187",
    "TLT.invalid_values_then_valid.requests": "2",
    "TLT.off_schema_then_valid.1.body":
        "744f8215abf4acf065f8eb9bf40441be92432a63db7820a5fc72979485ecc8a4",
    "TLT.off_schema_then_valid.1.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "TLT.off_schema_then_valid.2.body":
        "2b19c032499985bd1812a4d8da9506672e22d8db3bf76ec97806bb2ee3c33ceb",
    "TLT.off_schema_then_valid.2.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "TLT.off_schema_then_valid.completion":
        "9aec4cfec0b038526705ccb8b7e26496819b3e41490ea3e10f1ed00560a82850",
    "TLT.off_schema_then_valid.parsed":
        "0368d09691c6f24742248005b5b3d8838942d251f7b7bb6dbb20f5c24ab45187",
    "TLT.off_schema_then_valid.requests": "2",
    "TLT.scores_without_a_source":
        "0413abc7e685241ec9013f70fdc0ddac0085a8bdf8c4a70fada0fcd696e30d3f",
    "TLT.system_prompt":
        "01c4402c78d5b42db7cc6a3b19ebe66d57fb25805a028e00222b64abb813713c",
    "TLT.user_prompt": "f4f925b949c97f456c95e030c912fcddfe9bcc963b21a12316dda8cedb282467",
    "TLT.valid.1.body": "744f8215abf4acf065f8eb9bf40441be92432a63db7820a5fc72979485ecc8a4",
    "TLT.valid.1.target":
        "3e612970d3ab84c8d20c3803059368908d778c4b266198a6cd84dcda112b1ec9",
    "TLT.valid.completion":
        "7707b0e39e7362aab6600f59482b68ec595ce63112cf0fa6aaba9ba856b31ffe",
    "TLT.valid.parsed": "0368d09691c6f24742248005b5b3d8838942d251f7b7bb6dbb20f5c24ab45187",
    "TLT.valid.requests": "1",
    "parse.conviction_out_of_range":
        "e314971209099a0776821d532674db71b2aaa24a025568b54d670fd199a091a6",
    "parse.mended": "3ea564de110e04d56cf379adbd9f3f251d81ba038bdec27dad412729d99a5293",
    "parse.not_json": "f686204310518840db7245d78452f5a9a26a9a7fd068918bd4ac073c2e47f050",
    "parse.unknown_field":
        "5af0d23b65287c45f47878ab3ac5160c61d6a21b565fe242350ccc4891832706",
    "parse.valid": "be5cba4370e5835e106852d3120949f208b5dabb7d9ceebec880541df6efca30",
    "prompt_fingerprint": "6c59e07de87e",
    "repair.conviction_out_of_range":
        "3c674a07688681419723c7990960c6e6273c380272709a2d777cf8cffffe80ae",
    "repair.mended": "8a9476d75c618500da8c6d9ea1b0bde151b98d67ab57cec5b06ea07df4762bb5",
    "repair.not_json": "f686204310518840db7245d78452f5a9a26a9a7fd068918bd4ac073c2e47f050",
    "repair.unknown_field":
        "72d4871021a872bb81b6c98486221c61a9df8fa22f5a903f1be5a394a451a474",
    "repair.valid": "be5cba4370e5835e106852d3120949f208b5dabb7d9ceebec880541df6efca30",
}

KEY = "test-full-model-key"

SNAPSHOT = technicals.TechnicalSnapshot(
    last_close=184.55, as_of="2026-09-14", bars=250, sma20=179.1, sma50=171.4, sma200=163.7,
    macd=2.14, macd_signal=1.82, macd_histogram=0.32,
    distance_sma20=0.03, distance_sma50=0.077, distance_sma200=0.128,
    rsi14=61.2, return_1d=0.008, return_5d=0.021, return_21d=0.064, return_63d=0.11,
    low_52w=121.3, high_52w=190.2, position_in_52w_range=0.92,
    atr14=4.26, atr_pct_of_price=0.023, annualised_volatility=0.31, relative_volume=1.4,
)

#: A company with headlines and a gap, and a fund whose news lookup failed.
CONTEXTS = (
    TickerContext(
        ticker="MSFT",
        headlines=["Microsoft wins a cloud contract (Reuters, 2026-09-14)",
                   "Azure growth beats estimates — €2bn deal (FT)"],
        technicals=SNAPSHOT,
        gaps=["fundamentals: the provider returned nothing"],
    ),
    TickerContext(
        ticker="TLT",
        technicals=SNAPSHOT,
        gaps=[f"{NEWS_GAP_PREFIX}: Bright Data answered with an empty body"],
    ),
)


def _signal(ticker: str, **change: Any) -> dict:
    signal = {
        "ticker": ticker, "bias": "BULLISH", "conviction": 0.62,
        "rationale": "Trend above all three averages; news supportive.",
        "news_score": 0.4, "technical_score": 0.5, "fundamental_score": None,
        "analyst_score": None, "insider_score": None,
        "key_factors": ["Price 12.8% above the 200-day average", "RSI 61"],
    }
    signal.update(change)
    return signal


def _reply(content: str, prompt_tokens: int = 3210, completion_tokens: int = 456) -> dict:
    return {
        "id": "fixed", "object": "chat.completion", "model": llm.MODEL,
        "choices": [{"index": 0, "message": {"role": "assistant", "content": content},
                     "finish_reason": "stop"}],
        "usage": {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens},
    }


def _scenarios(ticker: str) -> dict[str, list[dict]]:
    """What the fake server answers, in order, per scenario."""
    good = json.dumps(_signal(ticker))
    return {
        "valid": [_reply(good)],
        "off_schema_then_valid": [_reply("I think it is bullish."), _reply(good, 3300, 410)],
        "invalid_values_then_valid": [
            _reply(json.dumps(_signal(ticker, conviction=-0.35))), _reply(good, 3350, 420),
        ],
    }


#: Fixed raw answers for production's parsing on its own.
RAW_ANSWERS = {
    "valid": json.dumps(_signal("MSFT")),
    "mended": json.dumps(_signal(
        "msft", analyst_score=10.0, insider_score=-999, rationale="x" * 2105,
        key_factors=["a", "b", "c", "d", "e", "f", "g", 7, "  ", "y" * 230],
    )),
    "conviction_out_of_range": json.dumps(_signal("MSFT", conviction=-0.35)),
    "unknown_field": json.dumps(_signal("MSFT", smuggled="yes")),
    "not_json": "I think it is bullish.",
}


def _sha(data: bytes | str) -> str:
    raw = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(raw).hexdigest()


def _jsonish(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)


def _outcome(fn: Any) -> Any:
    try:
        return {"ok": fn()}
    except Exception as exc:  # noqa: BLE001 - the error is the outcome
        errors = getattr(exc, "errors", None)
        if callable(errors):
            return {"error": type(exc).__name__,
                    "where": sorted([list(map(str, e["loc"])), e["type"]] for e in errors())}
        return {"error": type(exc).__name__}


def observe(sent: list[dict] | None = None) -> dict[str, str]:
    """Hashes of everything production sends and parses, for the fixed inputs above.

    Runs on any commit that has ``heartbeat.call_llm``: it touches only what
    main had before PR #142. ``sent``, when given, receives every request
    (method, URL, headers, body bytes) for the tests below.
    """
    out: dict[str, str] = {"prompt_fingerprint": hb.prompt_fingerprint()}
    real = llm.new_http_client
    try:
        for ctx in CONTEXTS:
            system, user = hb.system_prompt_for(ctx.ticker, ctx), hb.build_user_prompt(ctx)
            out[f"{ctx.ticker}.system_prompt"] = _sha(system)
            out[f"{ctx.ticker}.user_prompt"] = _sha(user)
            for name, replies in _scenarios(ctx.ticker).items():
                queue = list(replies)
                requests: list[dict] = []

                def handler(request: httpx.Request, queue=queue, requests=requests) -> httpx.Response:
                    requests.append({
                        "method": request.method, "url": str(request.url),
                        "headers": dict(request.headers), "body": request.content,
                    })
                    return httpx.Response(200, json=queue.pop(0))

                llm.new_http_client = lambda timeout, handler=handler: httpx.Client(
                    transport=httpx.MockTransport(handler), timeout=timeout)
                completion = hb.call_llm(system, user, hb.SIGNAL_JSON_SCHEMA)
                prefix = f"{ctx.ticker}.{name}"
                out[f"{prefix}.requests"] = str(len(requests))
                for n, request in enumerate(requests, 1):
                    out[f"{prefix}.{n}.body"] = _sha(request["body"])
                    out[f"{prefix}.{n}.target"] = _sha(_jsonish([
                        request["method"], request["url"], request["headers"].get("content-type"),
                    ]))
                usage = completion.usage
                out[f"{prefix}.completion"] = _sha(_jsonish([
                    completion.text, usage.model, usage.input_tokens, usage.output_tokens,
                ]))
                out[f"{prefix}.parsed"] = _sha(_jsonish(
                    _outcome(lambda: hb.parse_signal(completion.text).model_dump(mode="json"))))
                if sent is not None:
                    sent.extend({"scenario": prefix, **r} for r in requests)
    finally:
        llm.new_http_client = real
    for name, raw in RAW_ANSWERS.items():
        out[f"parse.{name}"] = _sha(_jsonish(
            _outcome(lambda raw=raw: hb.parse_signal(raw).model_dump(mode="json"))))
        out[f"repair.{name}"] = _sha(_jsonish(
            _outcome(lambda raw=raw: hb.repair_transparency(json.loads(raw)))))
    for ctx in CONTEXTS:
        signal = hb.parse_signal(json.dumps(_signal(ctx.ticker, fundamental_score=0.3,
                                                    analyst_score=0.2, insider_score=-0.1)))
        out[f"{ctx.ticker}.scores_without_a_source"] = _sha(_jsonish(
            hb.scores_without_a_source(signal, ctx).model_dump(mode="json")))
    return out


def test_the_prompt_fingerprint_is_production_s():
    assert hb.prompt_fingerprint() == FINGERPRINT


def test_production_s_requests_and_parsing_match_main_before_pr_142():
    seen = observe()
    assert seen["prompt_fingerprint"] == FINGERPRINT
    assert seen == GOLDEN


def test_every_request_carries_the_key_in_its_header_and_nowhere_else():
    sent: list[dict] = []
    observe(sent)
    assert len(sent) == 10
    for request in sent:
        assert request["method"] == "POST"
        assert request["url"] == llm.MODEL_BASE_URL.rstrip("/") + "/chat/completions"
        assert request["headers"]["authorization"] == f"Bearer {KEY}"
        assert KEY.encode() not in request["body"]


def test_request_body_is_what_the_first_ask_sends():
    """The voting arm's rebuild (``request_body``) equals the body production sent first."""
    sent: list[dict] = []
    observe(sent)
    provider = hb.full_model_provider()
    for ctx in CONTEXTS:
        system, user = hb.system_prompt_for(ctx.ticker, ctx), hb.build_user_prompt(ctx)
        rebuilt = provider.request_body(system, user, hb.SIGNAL_JSON_SCHEMA,
                                        model=llm.MODEL, effort=hb.full_model_effort())
        firsts = [r for r in sent if r["scenario"].startswith(f"{ctx.ticker}.")
                  and r is next(s for s in sent if s["scenario"] == r["scenario"])]
        assert len(firsts) == 3
        for request in firsts:
            assert json.loads(request["body"]) == rebuilt
