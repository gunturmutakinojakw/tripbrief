# === Stage 11: Add JSON export for the current application state ===
# Project: TripBrief
def export_state_json(state: dict) -> str:
    """Compact JSON export of the current TripBrief application state."""
    import json, os
    out = {k: v for k, v in state.items() if isinstance(v, (dict, list))}
    path = "state.json"
    with open(path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"[TripBrief] State exported to {path} ({len(json.dumps(out, indent=2))} bytes)")
    return path
