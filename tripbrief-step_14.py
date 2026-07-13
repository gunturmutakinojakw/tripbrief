# === Stage 14: Add file load support with fallback demo data ===
# Project: TripBrief
def load_demo_data():
    return {
        "itinerary": [
            {"day": 1, "city": "Paris", "activities": ["Eiffel Tower", "Louvre Museum"], "notes": "Book tickets in advance"},
            {"day": 2, "city": "Paris", "activities": ["Seine River Cruise", "Notre-Dame"], "notes": ""},
        ],
        "bookings": [
            {"type": "flight", "from": "NYC", "to": "CDG", "date": "2024-03-15", "cost": 600.00, "status": "confirmed"},
            {"type": "hotel", "location": "Paris", "checkin": "2024-03-15", "checkout": "2024-03-20", "cost": 500.00, "status": "confirmed"},
        ],
        "budget": {"total_budget": 2000.00, "spent": 1100.00, "remaining": 900.00},
        "packing_notes": ["Passport", "Comfortable shoes", "Light jacket"],
        "local_checklist": [
            {"day": 1, "city": "Paris", "items": ["Buy metro pass", "Find pharmacy"]},
            {"day": 2, "city": "Paris", "items": []},
        ]
    }
