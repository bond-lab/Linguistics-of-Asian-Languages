#!/bin/bash
# Copy the course decks into the site, then rebuild the static site into docs/
# (what GitHub Pages serves).
set -euo pipefail
cd "$(dirname "$0")"

# Only the decks the site links to.  An explicit list, not slides/*.pdf, so
# drafts and test builds (test.pdf, politeness1.pdf, metaphor-guided.pdf, ...)
# never get published.  Add a deck here when a week page starts linking it.
decks=(
    asia-before
    englishes
    features
    languages
    metaphor
    verbal-arts
    words
    writing
)

pdfs=()
for deck in "${decks[@]}"; do
    pdf="slides/$deck.pdf"
    if [[ ! -f $pdf ]]; then
        echo "freeze.sh: $pdf is missing -- build it first" >&2
        exit 1
    fi
    pdfs+=("$pdf")
done
rsync --checksum --itemize-changes "${pdfs[@]}" web/static/pdf/

exec uv run --no-project --with-requirements requirements.txt python freeze.py
