-- The Supabase starter: the day's MAIN start for the trading heartbeat.
--
-- Run once, by hand, in the SQL editor of the Supabase project
-- "algo-trading-archive" (as the postgres role). Nothing in this repository
-- applies it, and it is safe to run again: every statement is idempotent.
--
-- WHY THIS EXISTS
--
-- GitHub's cron is best-effort, and on this repository it has been far worse
-- than "a few minutes late": the heartbeat's cron arrived 4.5 to 5.7 hours
-- late on every day of the week of 21 Sep 2026, and on 16 Sep it never
-- arrived at all. A workflow_dispatch, by contrast, is created the moment it
-- is asked for. So the owner decided (26 Sep 2026) that the day's run is
-- started from here: a pg_cron job at 14:40 UTC, Monday to Friday, asks
-- GitHub to dispatch .github/workflows/heartbeat.yml. GitHub's own cron, the
-- Claude Routines, a temporary Claude "bridge" Routine at 14:42 and the
-- watchdog stay as backups. Every one of them is only a request to run: the
-- workflow's guard (analysis/cycle_day.py) lets exactly one of them run the
-- day, and the journal's run block records which one did (source =
-- "supabase-cron" for this one), so the daily brief can say when a backup
-- had to step in.
--
-- pg_cron runs in UTC on Supabase, so '40 14 * * 1-5' is 14:40 UTC: 10:40 New
-- York in summer and 09:40 in winter, after the 09:30 open in both seasons.
-- It fires on market holidays too; the heartbeat stands down on those by
-- itself (orchestrator/heartbeat.py, skip_for_non_trading_day) and writes
-- nothing.
--
-- WHERE THE TOKEN LIVES
--
-- The GitHub token this sends is NOT in this file, NOT in the repository, NOT
-- in a GitHub secret and NOT in any log. It lives only in Supabase Vault, as
-- the secret named exactly
--
--     github_heartbeat_dispatch
--
-- Make it once, in the Supabase dashboard (Project Settings, Vault, or with
-- select vault.create_secret('<the token>', 'github_heartbeat_dispatch');
-- typed into the SQL editor and never saved anywhere). A fine-grained token
-- limited to this one repository with "Actions: Read and write" is enough; a
-- classic token needs the "workflow" scope. GitHub makes it expire: write its
-- expiry date in config/settings.py (GITHUB_DISPATCH_TOKEN_EXPIRES), and the
-- daily health check warns 14 days before and raises a critical alarm once it
-- has expired. To replace it, update the same Vault secret (same name) and
-- the date.
--
-- The token is read from vault.decrypted_secrets inside start_heartbeat()
-- only, and handed straight to net.http_post as a header. It is never written
-- to public.starter_log, never returned, never logged by this file. One thing
-- to know: pg_net keeps each request, headers included, in its own queue
-- table (net.http_request_queue) for the second or two until its worker sends
-- it, and deletes it then. That table is readable only by the database's own
-- roles, not by the API keys.
--
-- HOW TO SEE WHAT IT DID
--
-- Every request writes one row to public.starter_log (requested_at, source,
-- request_id). Three minutes later, record_starter_status() copies the status
-- code of GitHub's answer onto that row (and pg_net's own error text, such as
-- a timeout, when there was no answer) -- never the response body, never a
-- header. GitHub answers a dispatch it accepted with 204 (No Content). A 401
-- is an expired or revoked token; a 403 or 404 a token that may not start
-- workflows on this repository; a 422 a dispatch whose inputs or branch do
-- not match the workflow.
--
--     select * from public.starter_log order by requested_at desc limit 10;
--     select * from cron.job_run_details order by start_time desc limit 10;
--
-- The heartbeat reads today's row read-only (store/starter_status.py, with
-- the SUPABASE_URL / SUPABASE_SERVICE_KEY secrets), commits it as
-- logs/starter_status.json, and the daily brief shows the status code.
--
-- KEEPING THE PROJECT AWAKE
--
-- A free Supabase project that has no activity for about a week is paused,
-- and a paused project runs no cron job: the main starter would stop in
-- silence (the backups would still start the day). Do not count on these jobs
-- to keep the project awake -- Supabase judges inactivity by its own measure.
-- What does is the heartbeat's own traffic through the API every trading day:
-- the archive push (store/push_remote.py) and the starter-log read, which
-- both need the two GitHub secrets above. Without them the brief warns every
-- day ("archive not configured: the Supabase project will pause"), and a
-- failed push pages the owner the same day. If the project is paused anyway,
-- restore it from the Supabase dashboard; the jobs resume with it.


-- 1. The two extensions. pg_cron runs the schedule; pg_net sends the request
--    from inside the database, asynchronously (it returns a request id at
--    once, and a background worker sends the request and stores the answer
--    in net._http_response, where it is kept for six hours).
create extension if not exists pg_cron;
create extension if not exists pg_net with schema extensions;


-- 2. The starter's log. One row per request. Row-level security on and no
--    policy at all, so only the service role (which bypasses RLS) can read
--    it: the publishable key reads nothing. The token is never a column.
create table if not exists public.starter_log (
    id           bigint generated always as identity primary key,
    requested_at timestamptz not null default now(),
    source       text not null default 'supabase-cron',
    request_id   bigint,
    status_code  int,
    error        text
);

alter table public.starter_log enable row level security;
revoke all on table public.starter_log from anon, authenticated;


-- 3. Ask GitHub to start the day's run.
--
--    security definer, so the cron job can read Vault through it without
--    being given Vault itself; search_path set to empty, so every name below
--    is the one written (a security definer function must not look names up
--    in a schema someone else could write to).
create or replace function public.start_heartbeat()
returns bigint
language plpgsql
security definer
set search_path = ''
as $$
declare
    dispatch_token text;
    request        bigint;
begin
    select secret.decrypted_secret
      into dispatch_token
      from vault.decrypted_secrets as secret
     where secret.name = 'github_heartbeat_dispatch'
     limit 1;

    if dispatch_token is null or dispatch_token = '' then
        insert into public.starter_log (source, error)
        values ('supabase-cron', 'no token in vault');
        return null;
    end if;

    -- The same inputs a person would give on the Run workflow page: a cycle,
    -- started by an outside scheduler (not the watchdog's backup, so it never
    -- counts against the watchdog's own limit), named supabase-cron for the
    -- journal. Never `rerun`: the workflow's guard must decide.
    request := net.http_post(
        url := 'https://api.github.com/repos/omrirulf/Algo-Trading-/actions/workflows/heartbeat.yml/dispatches',
        body := jsonb_build_object(
            'ref', 'main',
            'inputs', jsonb_build_object(
                'mode', 'cycle',
                'started_by', 'scheduler',
                'source', 'supabase-cron'
            )
        ),
        headers := jsonb_build_object(
            'Authorization', 'Bearer ' || dispatch_token,
            'Accept', 'application/vnd.github+json',
            'X-GitHub-Api-Version', '2022-11-28',
            'User-Agent', 'algo-trading-supabase-cron',
            'Content-Type', 'application/json'
        ),
        timeout_milliseconds := 10000
    );

    insert into public.starter_log (requested_at, source, request_id)
    values (now(), 'supabase-cron', request);
    return request;
end;
$$;


-- 4. Copy GitHub's answer onto the log: the status code, or pg_net's own
--    error text when no answer came (a timeout, a name that did not
--    resolve). Only those two -- never the response body or its headers.
--    Rows already answered are left alone, so running it again is harmless.
create or replace function public.record_starter_status()
returns integer
language plpgsql
security definer
set search_path = ''
as $$
declare
    updated integer;
begin
    update public.starter_log as log
       set status_code = response.status_code,
           error       = coalesce(left(response.error_msg, 200), log.error)
      from net._http_response as response
     where response.id = log.request_id
       and log.status_code is null
       and (response.status_code is not null or response.error_msg is not null);
    get diagnostics updated = row_count;
    return updated;
end;
$$;


-- 5. Nobody but the database's own roles may call either function: not the
--    publishable key, not a signed-in user. (Supabase grants execute on new
--    functions to anon and authenticated by default, so revoking from public
--    alone would not be enough.)
revoke execute on function public.start_heartbeat() from public, anon, authenticated;
revoke execute on function public.record_starter_status() from public, anon, authenticated;


-- 6. The schedule, Monday to Friday, UTC. Unscheduled first, so running this
--    file again replaces the jobs rather than adding a second copy.
select cron.unschedule(jobid)
  from cron.job
 where jobname in ('heartbeat-start', 'heartbeat-start-status');

select cron.schedule('heartbeat-start', '40 14 * * 1-5', 'select public.start_heartbeat()');
select cron.schedule('heartbeat-start-status', '43 14 * * 1-5', 'select public.record_starter_status()');
