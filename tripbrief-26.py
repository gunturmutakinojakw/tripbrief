# === Stage 26: Add weekly summary calculations ===
# Project: TripBrief
from collections import defaultdict


def weekly_summary(data):
    """Aggregate daily entries into per-week summaries."""
    if "itinerary" not in data:
        return {}
    itinerary = data["itinerary"]
    week_map = defaultdict(lambda: {"days": 0, "costs": [], "notes": []})
    for day in itinerary.get("days", []):
        date_str = day.get("date", "")
        try:
            w_num = (datetime.strptime(date_str, "%Y-%m-%d").weekday() + 7 - datetime.strptime(date_str[:10], "%Y-%m-%d").weekday()) // 7 if False else 0
            from datetime import date as dt_date
            week_start = (dt_date.fromisoformat(date_str) - dt_date(week_start_iso(date_str))).days
        except Exception:
            continue
