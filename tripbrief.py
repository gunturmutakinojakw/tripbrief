# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: TripBrief
import json, os

DATA_DIR = "data"

def _ensure_dir():
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR)

_ensure_dir()

itinerary = {
    "day": 1,
    "city": "Kyoto",
    "stops": [
        {"time": "09:00", "place": "Fushimi Inari Taisha", "duration_min": 240},
        {"time": "13:00", "place": "Pontocho Alley", "duration_min": 60},
    ]
}

bookings = [
    {"id": "BK-001", "type": "flight", "airline": "ANA", "route": "NRT-KIX", "date": "2025-07-14"},
    {"id": "BK-002", "type": "hotel", "name": "Hotel Granvia KIX", "checkin": "2025-07-14", "checkout": "2025-07-16"},
]

budget = {
    "currency": "USD",
    "total_limit": 3000,
    "spent": {"flights": 850, "hotels": 420, "meals": 0},
}

packing_notes = [
    {"item": "Passport", "status": "packed"},
    {"item": "Sunscreen SPF30+", "status": "packed"},
    {"item": "Light rain jacket", "status": "to pack"},
]

local_checklist = {
    "city": "Kyoto",
    "items": [
        {"task": "Buy Fushimi Inari ticket (if needed)", "done": True},
        {"task": "Reserve Pontocho dinner spot", "done": False},
    ]
}

demo_data = {
    "itineraries": {"day_1": itinerary},
    "bookings": bookings,
    "budget": budget,
    "packing_notes": packing_notes,
    "local_checklists": {"kyoto": local_checklist},
}

print(json.dumps(demo_data, indent=2))
