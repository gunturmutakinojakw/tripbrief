# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: TripBrief
def filter_items(items, **kwargs):
    """Filter items by status, category, owner, tag, and/or include_deleted."""
    result = list(items)
    if "status" in kwargs:
        result = [i for i in result if getattr(i, "status", None) == kwargs["status"]]
    if "category" in kwargs:
        result = [i for i in result if getattr(i, "category", None) == kwargs["category"]]
    if "owner" in kwargs:
        result = [i for i in result if getattr(i, "owner", None) == kwargs["owner"]]
    if "tag" in kwargs:
        tags = set(kwargs["tag"]) if not isinstance(kwargs["tag"], str) else {kwargs["tag"]}
        result = [i for i in result if any(t in getattr(i, "tags", []) for t in tags)]
    return result
