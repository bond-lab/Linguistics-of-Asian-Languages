#!/bin/bash
# Serve the site locally for preview on http://127.0.0.1:5000
set -euo pipefail
cd "$(dirname "$0")"

exec uv run --no-project --with-requirements requirements.txt python wsgi.py
