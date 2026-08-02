#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-https://github.com/sr-maximus/CSPTF.git}"
BRANCH="${2:-agent/publish-csptf-v0.1}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

command -v git >/dev/null || { echo "git is required" >&2; exit 1; }

echo "Cloning $REPO_URL..."
git clone "$REPO_URL" "$TMP_DIR/repo"
cd "$TMP_DIR/repo"
git checkout -b "$BRANCH"

# Copy the complete CSPTF tree while preserving the cloned .git directory.
rsync -a --delete --exclude='.git/' "$ROOT_DIR/" "$TMP_DIR/repo/"

git config user.name "Sr. Maximus"
git config user.email "47902444+sr-maximus@users.noreply.github.com"
git add -A

if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git commit -m "Publish CSPTF v0.1.0 draft"
git push -u origin "$BRANCH"

echo
echo "Published branch: $BRANCH"
echo "Open a pull request into main from the GitHub interface."
