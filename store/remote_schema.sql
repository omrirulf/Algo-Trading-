-- Postgres / Supabase schema for the remote archive.
--
-- Paste this into the Supabase SQL editor once, or let
-- `python store/push_remote.py --print-schema` hand it to you.
--
-- This is the same shape as store/schema.py, with three deliberate differences.
--
-- 1. `line_hash` is the primary key rather than a surrogate id. The content
--    hash is the natural key, and making it the PK is what makes the push
--    idempotent: `on conflict do nothing` absorbs a re-send of lines the
--    remote already has, so a push that overlaps the previous one is free.
--
-- 2. `raw` stays `text`, byte-exact, exactly as in SQLite -- and a generated
--    `raw_json` column carries the parsed form beside it. Storing only jsonb
--    would silently reformat the line (key order, whitespace, number
--    rendering), and the archive's whole claim is that it kept what was
--    written. This way the record is verbatim AND queryable:
--
--        select raw_json -> 'context' -> 'technicals' ->> 'rsi14' from signals;
--
-- 3. `ts_exact` is smallint rather than boolean, so one row builder in
--    store/loader.py serves both backends with no per-backend coercion.
--    Postgres will not implicitly cast 0/1 to boolean, and a translation layer
--    that exists only to satisfy a type is a place for the two archives to
--    drift apart.

create table if not exists public.signals (
    line_hash          text primary key,
    ingested_at        timestamptz not null,

    ts_utc             timestamptz,
    ts_exact           smallint not null default 0,
    trade_date         date,

    ticker             text not null,
    bias               text,
    conviction         double precision,
    rationale          text,

    news_score         double precision,
    technical_score    double precision,
    fundamental_score  double precision,
    analyst_score      double precision,
    insider_score      double precision,

    outcome_status     text,
    outcome_reason     text,
    outcome_quantity   integer,
    order_id           text,
    error              text,

    gap_count          integer not null default 0,

    model              text,
    input_tokens       bigint,
    output_tokens      bigint,
    cost_usd           double precision,

    fx_rate            double precision,

    raw                text not null,
    raw_json           jsonb generated always as (raw::jsonb) stored
);

create table if not exists public.executions (
    line_hash    text primary key,
    ingested_at  timestamptz not null,

    ts_utc       timestamptz,
    ts_exact     smallint not null default 0,
    trade_date   date,

    ticker       text not null,
    status       text,
    reason       text,
    bias         text,
    conviction   double precision,

    quantity     integer,
    side         text,
    entry_price  double precision,
    stop_price   double precision,
    atr          double precision,
    order_id     text,

    level        text,
    raw          text not null,
    raw_json     jsonb generated always as (raw::jsonb) stored
);

create index if not exists signals_ticker_ts on public.signals (ticker, ts_utc);
create index if not exists signals_ts on public.signals (ts_utc desc);
create index if not exists signals_date on public.signals (trade_date);
create index if not exists signals_order on public.signals (order_id);
create index if not exists executions_ticker_ts on public.executions (ticker, ts_utc);
create index if not exists executions_order on public.executions (order_id);

-- The same join the local index exposes: a signal beside the order it became.
-- LEFT JOIN because most signals never become orders, and a rejection is data.
create or replace view public.decisions as
select
    s.ts_utc, s.trade_date, s.ticker, s.bias, s.conviction,
    s.news_score, s.technical_score, s.fundamental_score,
    s.analyst_score, s.insider_score,
    s.outcome_status, s.outcome_reason, s.gap_count, s.cost_usd, s.fx_rate,
    e.quantity, e.side, e.entry_price, e.stop_price, e.atr, e.order_id
from public.signals s
left join public.executions e
       on e.order_id = s.order_id and s.order_id is not null;

-- NOT optional, and not a detail. A Postgres view runs with the permissions of
-- whoever CREATED it unless told otherwise, so without this line `decisions`
-- reads straight through the row-level security below it: the signals table is
-- closed to the publishable key and a view over it is wide open.
--
-- That is not hypothetical. The first version of this file omitted it, and a
-- probe with the anon role read 0 rows from `signals` and 1 row from
-- `decisions` -- the security lint caught it before the schema carried any
-- real data. security_invoker makes the view enforce the permissions of
-- whoever queries it, which is the whole point of the RLS below.
alter view public.decisions set (security_invoker = on);

-- Row-level security on, and deliberately NO policies.
--
-- That combination denies every request carrying the publishable (anon) key,
-- which is the key that is safe to leak precisely because it should be able to
-- do nothing here. The push uses the service-role key, which bypasses RLS and
-- lives only in a GitHub Actions secret.
--
-- The alternative -- an insert-only policy for anon -- would let anyone who
-- read the publishable key append rows to the record of what this system
-- decided. A journal that strangers can write to is not a journal.
alter table public.signals enable row level security;
alter table public.executions enable row level security;
