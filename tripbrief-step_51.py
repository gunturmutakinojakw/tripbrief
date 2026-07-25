# === Stage 51: Add unit tests for search and filter behavior ===
# Project: TripBrief
import pytest
from tripbrief.search import SearchEngine


def test_search_by_destination_filters_results():
    engine = SearchEngine()
    results = engine.search("Paris", "destination")
    assert all(r["destination"] == "Paris" for r in results)


def test_filter_budget_range_includes_matching_items():
    engine = SearchEngine()
    budgeted = engine.filter({"budget": {"min": 100, "max": 300}})
    assert any(item.get("total_cost") and 100 <= item["total_cost"] <= 300 for item in budgeted)


def test_search_empty_query_returns_all():
    engine = SearchEngine()
    all_results = engine.search("", "")
    assert len(all_results) > 0
