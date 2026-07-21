# === Stage 38: Add data integrity checks for broken references ===
# Project: TripBrief
def check_references(trip):
    if "itinerary" in trip and "day_plans" not in trip.get("itinerary", {}):
        raise ValueError("Itinerary missing required 'day_plans' key")
    bookings = trip.get("bookings", [])
    for b in bookings:
        ref = b.get("booking_ref", "") or b.get("confirmation_id", "")
        if not ref:
            raise ValueError(f"Booking {b} has no reference identifier")
    return True
