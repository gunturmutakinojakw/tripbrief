# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: TripBrief
def snapshot_compare(before, after, key="state"):
    if before is None and after is None:
        return {"status": "unchanged", "value": None}
    if before is None or after is None:
        return {"status": "changed", "before": before, "after": after}
    if isinstance(before, dict) and isinstance(after, dict):
        changes = {k: (v1, v2) for k, v1 in before.items() if v1 != after.get(k)}
        new_keys = set(after.keys()) - set(before.keys())
        removed_keys = set(before.keys()) - set(after.keys())
        return {"status": "changed", "changes": changes, "new_keys_added": list(new_keys), "keys_removed": list(removed_keys)}
    if isinstance(before, (list, tuple)) and isinstance(after, (list, tuple)):
        before_set = set(before)
        after_set = set(after)
        return {"status": "changed", "only_in_before": before_set - after_set, "only_in_after": after_set - before_set}
    if before == after:
        return {"status": "unchanged", "value": before}
    return {"status": "changed", "before": str(before), "after": str(after)}
