#!/usr/bin/env python3
"""Example: read sample data files and print processing results.

Run from the project root:

    python examples/process_sample_data.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Allow running without ``pip install -e .``
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from new_project.data_loader import (  # noqa: E402
    load_sales_json,
    load_users_csv,
    process_sample_data,
    summarize_sales,
    summarize_users,
)


def main() -> None:
    data_dir = Path(__file__).resolve().parents[1] / "data"

    print("=== Step 1: read files ===")
    users = load_users_csv(data_dir / "users.csv")
    sales = load_sales_json(data_dir / "sales.json")
    print(f"Loaded {len(users)} users, {len(sales)} sales lines")

    print("\n=== Step 2: process separately ===")
    print("Users summary:", json.dumps(summarize_users(users), ensure_ascii=False, indent=2))
    print("Sales summary:", json.dumps(summarize_sales(sales), ensure_ascii=False, indent=2))

    print("\n=== Step 3: one-shot pipeline ===")
    print(json.dumps(process_sample_data(data_dir), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
