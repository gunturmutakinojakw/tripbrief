# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: TripBrief
def parse_itinerary_date(raw: str) -> datetime.date | None:
    """Return a date parsed from common itinerary formats, else None."""
    try:
        return datetime.date.fromisoformat(raw.strip())
    except ValueError:
        for fmt in ("%b %d", "%B %d", "%Y-%m-%d"):
            try:
                return datetime.date.strptime(raw.strip(), fmt)
            except ValueError:
                continue
        return None


def format_budget_currency(amount: float, currency: str = "USD") -> str:
    """Format a monetary amount with its currency symbol."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    sym = symbols.get(currency.upper(), f"{currency} ")
    return f"{sym}{amount:,.2f}"


def sanitize_packing_note(text: str) -> str:
    """Lowercase and strip whitespace from packing notes."""
    return text.strip().lower()


def validate_local_checklist(item: dict[str, Any]) -> bool:
    """Ensure each checklist item has a name (str) and done flag (bool)."""
    if not isinstance(item.get("name"), str):
        return False
    try:
        _ = item["done"] is True or item["done"] is False
    except KeyError:
        return False
    return True


def group_by_day(itinerary: list[dict]) -> dict[str, list]:
    """Group itinerary entries by their date (ISO string key)."""
    groups: dict[str, list] = {}
    for entry in itinerary:
        d = parse_itinerary_date(entry.get("date", ""))
        if d is None:
            continue
        groups.setdefault(d.isoformat(), []).append(entry)
    return groups


def calculate_total_budget(items: list[dict]) -> float:
    """Sum the estimated_cost across all budget items."""
    total = 0.0
    for item in items:
        try:
            cost = float(item.get("estimated_cost", 0))
        except (TypeError, ValueError):
            continue
        total += cost
    return round(total, 2)


def merge_packing_notes(source: list[dict], target: list[dict]) -> dict[str, bool]:
    """Merge source notes into target and return the resulting note map."""
    result = {n["item"]: n["done"] for n in target}
    for n in source:
        key = sanitize_packing_note(n.get("item", ""))
        if not key:
            continue
        result[key] = True
    return result


def format_local_checklist(chk: list[dict]) -> str:
    """Return a readable string of checklist items, e.g. '✓ item1\n✗ item2'."""
    lines = []
    for item in chk:
        if validate_local_checklist(item):
            done = "✓" if item["done"] else "✗"
            lines.append(f"{done} {item['name']}")
    return "\n".join(lines)


def merge_itineraries(a: list[dict], b: list[dict]) -> dict[str, list]:
    """Combine two itinerary lists into a single grouped structure."""
    combined = a + b
    return group_by_day(combined)


def filter_valid_budget_items(items: list[dict]) -> list[dict]:
    """Return only items whose name is non-empty and cost is numeric."""
    valid = []
    for item in items:
        if not isinstance(item.get("name"), str) or not item["name"].strip():
            continue
        try:
            float(item.get("estimated_cost", 0))
            valid.append(item)
        except (TypeError, ValueError):
            pass
    return valid


def summary_report(itinerary: list[dict], budget: list[dict]) -> dict[str, Any]:
    """Produce a compact summary of the trip plan."""
    days = len(group_by_day(itinerary))
    total_cost = calculate_total_budget(budget)
    packing = merge_packing_notes([], [])
    return {
        "total_days": days,
        "estimated_total": format_budget_currency(total_cost),
        "packing_summary": sanitize_packing_note("all items reviewed"),
    }
