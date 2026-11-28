// The desk's service worker: network first, so the pages and the snapshots
// are fresh whenever the phone is online, and the last copy of each when it
// is not. Nothing here is a credential, and nothing here writes anywhere but
// this browser's cache.
//
// Both pages are in the shell, so the four-fund page opens offline even on a
// phone that has only ever opened the desk. The cache keeps its name when the
// shell grows: a changed sw.js installs again and adds the new page to the
// same cache, and being network first, nothing older is ever served over a
// fresh copy.
//
// Each response is kept under its URL without the query string. The pages
// poll the live records with a fresh "?t=<time>" every few minutes to get
// past caches; kept under the full URL, every poll would add one more copy
// that is never read again. Kept under the bare URL, each poll replaces the
// last one, and a lookup finds it the same way.
const CACHE = "algo-desk-v1";
const bare = (url) => { const u = new URL(url); u.search = ""; u.hash = ""; return u.href; };
const SHELL = ["./", "./index.html", "./funds.html", "./manifest.webmanifest", "./icon.svg", "./icon-192.png", "./icon-512.png"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).catch(() => {}));
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(Promise.all([
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))),
    // The copies an older worker kept under their full "?t=" URLs.
    caches.open(CACHE).then((c) => c.keys().then((requests) =>
      Promise.all(requests.filter((r) => new URL(r.url).search).map((r) => c.delete(r))))),
  ]).catch(() => {}));
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const key = bare(event.request.url);
  event.respondWith(
    fetch(event.request).then((response) => {
      if (response && response.ok) {
        const copy = response.clone();
        caches.open(CACHE).then((c) => c.put(key, copy)).catch(() => {});
      }
      return response;
    }).catch(() => caches.match(key, {ignoreSearch: true}).then((hit) => hit || Response.error()))
  );
});
