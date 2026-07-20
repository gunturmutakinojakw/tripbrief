# === Stage 34: Add support for multiple local user profiles ===
# Project: TripBrief
import json, os, uuid
PROFILE_DIR = "profiles"
os.makedirs(PROFILE_DIR, exist_ok=True)


def get_profile(name="default"):
    path = os.path.join(PROFILE_DIR, f"{name}.json")
    if not os.path.exists(path):
        data = {"id": str(uuid.uuid4()), "name": name, "itineraries": [], "bookings": [], "budgets": {}, "packing_notes": "", "local_checklists": []}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    return load_json(path)


def save_profile(name, data):
    path = os.path.join(PROFILE_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
