# === Stage 28: Add overdue item detection based on due dates ===
# Project: TripBrief
def find_overdue_items(itinerary, today=None):
    """Return list of itinerary items past their due date."""
    if today is None:
        from datetime import date as _date
        today = _date.today()
    overdue = []
    for item in itinerary.get("items", []):
        task = item.get("task") or item.get("name", "")
        due_str = item.get("due_date", item.get("deadline"))
        if not due_str:
            continue
        try:
            from datetime import date as _date, timedelta, datetime
            due = _date.fromisoformat(due_str)
            if today > due:
                overdue.append({**item, "days_overdue": (today - due).days})
        except Exception:
            pass
    return overdue

def print_overdue_report(itinerary):
    """Print a compact overdue status report."""
    today = _date.today()
    overdue = find_overdue_items(itinerary, today)
    if not overdue:
        print("[TripBrief] All items are on schedule.")
        return
    print(f"[TripBrief] {len(overdue)} item(s) are overdue:\n")
    for idx, o in enumerate(overdue, 1):
        name = o.get("task", o.get("name", "?"))
        days = o.get("days_overdue", "unknown")
        print(f"  {idx}. [{o.get('status', 'pending')}] {name} — {days} day(s) overdue")
