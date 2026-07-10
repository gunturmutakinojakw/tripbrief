# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: TripBrief
def sort_entries(entries, key_func):
    """Sort a list of dicts by a callable key (e.g., lambda e: e['title'])."""
    return sorted(entries, key=key_func)

def sort_by_title(entries):
    return sort_entries(entries, lambda e: e.get('title', '').lower())

def sort_by_date(entries):
    return sort_entries(entries, lambda e: e.get('date') or '')

def sort_by_priority(entries):
    return sort_entries(entries, lambda e: int(e.get('priority', 0)))

def sort_by_last_update(entries):
    return sort_entries(entries, lambda e: e.get('last_update') or '')
