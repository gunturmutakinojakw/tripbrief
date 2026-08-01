# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: TripBrief
class ValidationError:
    severity = "warning"
    message = ""
    section = ""


def validate_trip(trip):
    errors = []
    warnings = []

    if not trip.get("itinerary") or not trip["itinerary"].get("days"):
        errors.append(ValidationError("No itinerary days defined", "itinerary"))

    for day in trip.get("itinerary", {}).get("days", []):
        missing = [k for k in ["date", "activities"] if not day.get(k)]
        if missing:
            errors.append(ValidationError(f"Day {day.get('name', '?')}: missing {missing}", "itinerary"))

    if trip.get("bookings") and not any(b.get("confirmed") or b.get("pending") for b in trip["bookings"]):
        warnings.append(ValidationError("No confirmed or pending bookings", "bookings"))

    if trip.get("budget") and (trip["budget"].get("total") is None or trip["budget"]["total"] <= 0):
        errors.append(ValidationError("Budget total must be positive", "budget"))

    for note in trip.get("packing_notes", []):
        if not note.get("items"):
            warnings.append(ValidationError(f"Packing note '{note.get('title', '?')}' has no items", "packing_notes"))

    return errors, warnings
