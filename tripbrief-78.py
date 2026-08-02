# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: TripBrief
from collections import defaultdict


def group_by_destination(itinerary):
    """Split an itinerary list into per-destination sub-lists."""
    groups = defaultdict(list)
    for stop in itinerary:
        groups[stop["destination"]].append(stop)
    return dict(groups)


def sort_itinerary_by_date(itinerary, date_field="date", reverse=False):
    """Return a new itinerary sorted by the chosen date field."""
    return sorted(itinerary, key=lambda s: s.get(date_field, ""), reverse=reverse)


def extract_checklist_items(packing_notes):
    """Pull raw items from a packing-notes dict (whether it's a list or dict)."""
    if isinstance(packing_notes, list):
        return [item for item in packing_notes if item]
    if isinstance(packing_notes, dict):
        result = []
        for section, items in packing_notes.items():
            result.extend(items)
        return result
    return []


def merge_budgets(budget_list):
    """Merge a list of budget dicts by summing matching expense keys."""
    merged = {}
    for entry in budget_list:
        if isinstance(entry, dict):
            for key, value in entry.items():
                current = merged.get(key, 0)
                merged[key] = current + value if isinstance(value, (int, float)) else value
    return merged


def deduplicate_itinerary(stops):
    """Remove consecutive duplicate stops from an itinerary."""
    if not stops:
        return []
    result = [stops[0]]
    for stop in stops[1:]:
        if stop != result[-1]:
            result.append(stop)
    return result


def compute_total_budget(budgets):
    """Sum all numeric values across a list of budget dicts."""
    total = 0
    for entry in budgets:
        if isinstance(entry, dict):
            for value in entry.values():
                if isinstance(value, (int, float)):
                    total += value
    return total


def find_earliest_date(stops, date_field="date"):
    """Return the earliest non-empty date string from a list of stops."""
    candidates = [s.get(date_field, "") for s in stops]
    return next((d for d in candidates if d), None)
