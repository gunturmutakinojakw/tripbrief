# === Stage 25: Add daily summary calculations ===
# Project: TripBrief
def daily_summary(trip):
    """Compute per-day totals: meals, transport, accommodation, activities, notes."""
    summary = {}
    for day in trip.get("days", []):
        date = day["date"]
        if date not in summary:
            summary[date] = {"meals": 0, "transport": 0, "accommodation": 0, "activities": 0}
        for item in day.get("items", []):
            cat = item.get("category")
            cost = item.get("cost", 0)
            if cat == "meal":
                summary[date]["meals"] += cost
            elif cat == "transport":
                summary[date]["transport"] += cost
            elif cat == "accommodation":
                summary[date]["accommodation"] += cost
            else:
                summary[date]["activities"] += cost
    return summary

def print_daily_summary(trip):
    """Pretty-print the daily summaries."""
    s = daily_summary(trip)
    if not s:
        print("No days found in itinerary.")
        return
    total = sum(v["meals"] + v["transport"] + v["accommodation"] + v["activities"] for v in s.values())
    print(f"{'Date':<12} {'Meals':>8} {'Transport':>10} {'Accommodation':>14} {'Activities':>10} {'Total':>7}")
    print("-" * 63)
    for date, costs in s.items():
        total_day = sum(costs.values())
        print(f"{date:<12} {costs['meals']:>8.2f} {costs['transport']:>10.2f} {costs['accommodation']:>14.2f} {costs['activities']:>10.2f} {total_day:>7.2f}")
    print("-" * 63)
    print(f"{'TOTAL':<12} {sum(v['meals'] for v in s.values()):>8.2f} {sum(v['transport'] for v in s.values()):>10.2f} {sum(v['accommodation'] for v in s.values()):>14.2f} {sum(v['activities'] for v in s.values()):>10.2f} {total:>7.2f}")
