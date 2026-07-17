# === Stage 27: Add monthly summary calculations ===
# Project: TripBrief
from datetime import date, timedelta

def monthly_summary(trips):
    """Return a dict of month -> total cost across all trips."""
    summary = {}
    for trip in trips:
        if not trip.get("bookings") or not trip["itinerary"]:
            continue
        start = trip["itinerary"][0].get("date", date.today())
        end = trip["itinerary"][-1].get("date", start) + timedelta(days=365)
        while start < end:
            month = start.strftime("%Y-%m")
            summary[month] = summary.get(month, 0) + sum(b.get("cost", 0) for b in trip["bookings"])
            start += timedelta(days=1)
    return summary
