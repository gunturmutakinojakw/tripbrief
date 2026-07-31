# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: TripBrief
def seed_demo_data():
    """Populate TripBrief with deterministic sample data for quick testing."""
    import json, os
    base = os.path.dirname(__file__)
    demo = {
        "itinerary": [
            {"day": 1, "destination": "Paris", "activities": ["Eiffel Tower", "Louvre Museum"], "notes": "Book Eiffel tickets in advance."},
            {"day": 2, "destination": "Bordeaux", "activities": ["Wine Tasting Tour", "Cathedral of St. Andrew"], "notes": "Bring a light jacket for the evening tasting."},
        ],
        "bookings": [
            {"id": "BK-001", "type": "flight", "from": "JFK", "to": "CDG", "date": "2025-11-15", "passengers": 2, "cost": 480.0},
            {"id": "BK-002", "type": "hotel", "location": "Paris", "checkin": "2025-11-16", "checkout": "2025-11-19", "cost": 350.0},
            {"id": "BK-003", "type": "activity", "name": "Eiffel Summit", "date": "2025-11-16", "cost": 28.0},
        ],
        "budget": {
            "currency": "USD",
            "total_limit": 3000.0,
            "spent": 498.0,
            "categories": {"flights": 480.0, "accommodation": 350.0, "activities": 28.0},
        },
        "packing_notes": ["Passport", "Credit cards", "Light jacket", "Sunglasses", "Adaptor EU"],
        "local_checklist": [
            {"city": "Paris", "items": ["Get a metro card", "Learn basic French phrases", "Find nearest pharmacy"]},
            {"city": "Bordeaux", "items": ["Reserve wine tasting spot", "Check weather forecast", "Locate train station"]},
        ],
    }
    out = os.path.join(base, "data", "demo.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(demo, f, indent=2)
    print(f"[TripBrief] Demo data written to {out}")
