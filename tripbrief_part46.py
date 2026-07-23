# === Stage 46: Add a schema version field and migration helper ===
# Project: TripBrief
SCHEMA_VERSION = "1.4"


def migrate_data(data):
    """Bumps schema version and normalizes legacy fields."""
    if data.get("schema_version") != SCHEMA_VERSION:
        data["schema_version"] = SCHEMA_VERSION
    if "itinerary_items" not in data and "items" in data.get("itineraries", []):
        for it in data["itineraries"]:
            if isinstance(it.get("items"), list):
                it["itinerary_items"] = it.pop("items")
    if "budget_total" not in data:
        data.setdefault("budgets", {"total": 0, "currency": "USD"})
    return data
