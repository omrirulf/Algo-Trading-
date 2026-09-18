#!/usr/bin/env bash
# Build the desk and push it to the gh-pages branch, one commit deep.
#
# Run by the pages workflow on any change to the page, and by the heartbeat
# right after the journal commit, because a push made with the workflow
# token starts no other workflow. Needs GH_TOKEN (the job's token) and
# GITHUB_REPOSITORY; nothing else, and no dependency beyond the standard
# library. The branch holds only the built site; its history is in main.
set -euo pipefail
site="$(mktemp -d)"
python dashboard/build.py --site "$site"
cd "$site"
touch .nojekyll
git init -q -b gh-pages
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A
git commit -qm "Desk built from ${GITHUB_SHA:-$(git -C "$OLDPWD" rev-parse --short HEAD)} at $(date -u +'%Y-%m-%dT%H:%MZ')"
git push -q -f "https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" gh-pages
echo "desk published to gh-pages"
