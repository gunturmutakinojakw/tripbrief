# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: TripBrief
def format_trip_summary(trip):
    """Return a polished, human-readable trip briefing."""
    parts = []
    if trip["destination"]:
        parts.append(f"📍 {trip['destination']}")
    if trip["dates"]:
        parts.append(f"🗓️ {trip['dates']}")
    if trip["budget"] is not None:
        parts.append(f"💰 Budget: ${trip['budget']:.0f}")
    itinerary = trip.get("itinerary", [])
    if itinerary:
        lines = ["\n🗺️ Itinerary:\n"]
        for day in itinerary:
            lines.append(f"  • Day {day['date']} — {', '.join(day['activities'])}")
        parts.extend(lines)
    packing = trip.get("packing", [])
    if packing:
        items = [f"• {item}" for item in packing]
        parts.append("\n🎒 Pack:\n" + "\n".join(items))
    local_checklist = trip.get("local_checklist", [])
    if local_checklist:
        checklist = []
        for task, done in local_checklist.items():
            mark = "✅" if done else "⬜"
            checklist.append(f"{mark} {task}")
        parts.append("\n📋 Local checklist:\n" + "\n".join(checklist))
    return "\n\n".join(parts)
