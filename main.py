#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (at most 140 characters) for a city that does
not exist to /output/entry.txt. Deterministic: the same line every run,
standard library only, no network, no environment reads.
"""

from pathlib import Path

# One line of weather for Cloudbank City, a place that does not exist:
# named city, real forecast register, one surprising image for a bored
# commuter at a rainy bus stop.
ENTRY = (
    "Cloudbank City: 16\u00b0 with showers that only fall on the other "
    "side of the street, so half of you arrives dry. Bring a jacket anyway."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard the gate: the scorer accepts only 1-140 characters, not
    # whitespace alone. Fail loudly here rather than emit a bad entry.
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError(f"entry must be 1-140 non-blank chars, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
