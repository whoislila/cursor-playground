"""Read and process sample data files under the project ``data/`` directory."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

# Project root: src/cursor_demo_project/ -> src/ -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_DIR = PROJECT_ROOT / "data"


def load_users_csv(path: Path | None = None) -> list[dict[str, str]]:
    """Load user rows from a CSV file."""
    file_path = path or DEFAULT_DATA_DIR / "users.csv"
    with file_path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load_sales_json(path: Path | None = None) -> list[dict[str, Any]]:
    """Load sales records from a JSON file."""
    file_path = path or DEFAULT_DATA_DIR / "sales.json"
    with file_path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {file_path}")
    return data


def summarize_users(users: list[dict[str, str]], min_age: int = 18) -> dict[str, Any]:
    """Filter adults and count how many users live in each city."""
    adults = [u for u in users if int(u["age"]) >= min_age]
    city_counts = Counter(u["city"] for u in adults)
    return {
        "total": len(users),
        "adults": len(adults),
        "minors": len(users) - len(adults),
        "by_city": dict(sorted(city_counts.items())),
    }


def summarize_sales(sales: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute total revenue and units sold per product."""
    revenue_by_product: dict[str, float] = defaultdict(float)
    units_by_product: dict[str, int] = defaultdict(int)

    for row in sales:
        product = row["product"]
        quantity = int(row["quantity"])
        line_total = float(row["amount"]) * quantity
        revenue_by_product[product] += line_total
        units_by_product[product] += quantity

    return {
        "order_lines": len(sales),
        "total_revenue": sum(revenue_by_product.values()),
        "revenue_by_product": dict(sorted(revenue_by_product.items())),
        "units_by_product": dict(sorted(units_by_product.items())),
    }


def process_sample_data(data_dir: Path | None = None) -> dict[str, Any]:
    """Load default sample files and return both summaries."""
    base = data_dir or DEFAULT_DATA_DIR
    users = load_users_csv(base / "users.csv")
    sales = load_sales_json(base / "sales.json")
    return {
        "users": summarize_users(users),
        "sales": summarize_sales(sales),
    }
