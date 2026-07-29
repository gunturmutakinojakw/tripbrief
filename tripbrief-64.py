# === Stage 64: Add validation for relationship references ===
# Project: TripBrief
def validate_references(records):
    """Check that every foreign-key reference still points to an existing record."""
    errors = []
    for rec in records:
        if "itinerary_id" in rec and "itinerary_id" not in (rec.get("bookings", []) or {}).values():
            errors.append(f"{rec['type']}: itinerary_id {rec['itinerary_id']} not found")
        if "booking_id" in rec and rec["booking_id"] not in [b["id"] for b in rec.get("bookings", [])]:
            errors.append(f"{rec['type']}: booking_id {rec['booking_id']} not found")
    return errors
