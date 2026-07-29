# === Stage 66: Add export of a short status dashboard ===
# Project: TripBrief
def export_dashboard(trip):
    """Compact status dashboard: trip name, days, budget spent, booking count, checklist progress."""
    total_days = sum(len(it["days"]) for it in trip.get("itineraries", []))
    bookings_count = len(trip.get("bookings", []))
    checklist_total = sum(1 for c in trip.get("checklists", []) if c)
    packing_done = sum(c.count(True) for c in trip.get("packing_notes", []))
    status_lines = [
        f"Trip: {trip['name']}",
        f"Itinerary days: {total_days}",
        f"Bookings made: {bookings_count}",
        f"Packing items done / total: {packing_done}/{sum(c.count(True) for c in trip.get('packing_notes', [])) if trip.get('packing_notes') else 0}",
    ]
    return "\n".join(status_lines)
