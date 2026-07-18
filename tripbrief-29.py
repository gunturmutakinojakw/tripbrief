# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: TripBrief
def upcoming_items(trip_brief):
    """Return items that occur before today, sorted by date/time."""
    from datetime import date, time, timedelta
    now = date.today() + timedelta(hours=time.now().hour)
    return [item for item in trip_brief if hasattr(item, 'date') and item.date < now]
