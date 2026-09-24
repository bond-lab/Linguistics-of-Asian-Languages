#!/bin/bash
# Rebuild the static site into docs/ (what GitHub Pages serves).
set -euo pipefail
cd "$(dirname "$0")"

exec uv run --no-project --with-requirements requirements.txt python freeze.py
