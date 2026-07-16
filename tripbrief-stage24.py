# === Stage 24: Add grouped summaries by category or status ===
# Project: TripBrief
def grouped_summary(trip):
    """Produce a compact category/status summary dict."""
    from collections import Counter
    items = []
    for section in trip.values():
        if isinstance(section, list):
            for entry in section:
                items.append(entry)
    cats = Counter()
    statuses = Counter()
    for it in items:
        if "category" in it and it["category"]:
            cats[it["category"]] += 1
        if "status" in it and it["status"]:
            statuses[it["status"]] += 1
    return {"categories": dict(cats), "statuses": dict(statuses)}
