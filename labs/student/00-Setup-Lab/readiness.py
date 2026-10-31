"""Run a self-contained, credential-free SQLite and JSON readiness exercise."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
import sqlite3
import sys


def check_readiness() -> dict[str, object]:
    """Check the runtime and a tiny original synthetic data contract in memory."""
    if not (3, 12) <= sys.version_info[:2] < (3, 15):
        raise ValueError("Use Python 3.12 or 3.13; trainer also tests 3.14.")
    if sys.prefix == sys.base_prefix:
        raise ValueError("Use your project .venv interpreter, not system Python.")
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE tickets (id TEXT PRIMARY KEY, hours INTEGER)")
        connection.executemany("INSERT INTO tickets VALUES (?, ?)", [("T01", 4), ("T02", 12)])
        rows = connection.execute("SELECT id, hours FROM tickets ORDER BY id").fetchall()
    if rows != [("T01", 4), ("T02", 12)]:
        raise ValueError("Synthetic SQL checkpoint failed.")
    packages: dict[str, str] = {}
    for package in ("pydantic", "pandas", "scikit-learn", "pytest", "google-genai", "boto3"):
        try:
            packages[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            packages[package] = "not installed; not required for Challenge 0"
    return {
        "challenge": "CH00",
        "status": "local_readiness_passed",
        "mode": "offline",
        "python": platform.python_version(),
        "sqlite": sqlite3.sqlite_version,
        "synthetic_rows": len(rows),
        "packages": packages,
        "cloud_calls": 0,
        "cloud_eligibility_verified": False,
    }


def create_parser() -> argparse.ArgumentParser:
    """Build the offline-only command line."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Default; no network or credentials.")
    return parser


def main() -> int:
    """Print sanitized readiness evidence without writing any files."""
    create_parser().parse_args()
    try:
        print(json.dumps(check_readiness(), indent=2))
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
