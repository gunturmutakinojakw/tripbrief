# === Stage 40: Add plain text report export ===
# Project: TripBrief
def export_itinerary_to_txt(itinerary):
    """Export a TripBrief itinerary to plain text."""
    lines = [f"Trip: {itinerary.get('destination', 'Unknown')}", f"Date: {itinerary.get('date_range', 'TBD')}"]
    for day in itinerary.get("days", []):
        lines.append(f"\nDay {day['number']} - {day.get('location', 'Unknown')}")
        for time, activity in day.get("activities", {}).items():
            lines.append(f"{time}: {activity}")
    return "\n".join(lines)
