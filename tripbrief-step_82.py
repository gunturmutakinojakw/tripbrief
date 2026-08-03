# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: TripBrief
def demo():
    print("=== TripBrief Demo ===")
    itinerary = {
        "destination": "Tokyo",
        "dates": ["2025-08-10", "2025-08-17"],
        "days": [
            {"day": 1, "plan": "Arrive Narita, check in hotel"},
            {"day": 2, "plan": "Shibuya crossing, Meiji Shrine"},
            {"day": 3, "plan": "TeamLab Borderless, Senso-ji Temple"},
        ]
    }
    bookings = [
        {"type": "flight", "to": "Narita", "price": 250},
        {"type": "hotel", "nights": 7, "price_per_night": 120},
        {"type": "train", "route": "Tokaido Shinkansen", "price": 8000},
    ]
    budget = {"total": 5000, "spent": 9340}

    packing = ["passport", "power adapter", "light jacket", "sunscreen"]
    local_checklist = [
        ("Senso-ji Temple", True),
        ("Tsukiji Outer Market", False),
        ("Shibuya Sky observation deck", True),
    ]

    print(f"Destination: {itinerary['destination']}")
    for day in itinerary["days"]:
        print(f"  Day {day['day']}: {day['plan']}")
    total_cost = sum(b["price"] * b["nights"] if "nights" in b else b["price"] for b in bookings)
    print(f"Total cost: ${total_cost}")
    print("Packing list:")
    for item in packing:
        print(f"  ✓ {item}")
    print("Local checklist:")
    for place, done in local_checklist:
        status = "✓ Done" if done else "○ Not yet"
        print(f"  {status} - {place}")

demo()
