# === Stage 41: Add plain text import for a simple line-based format ===
# Project: TripBrief
def parse_itinerary(text):
    """Parse a simple line-based itinerary text into structured data.

    Each line can be:
      - Start date/time
      - End date/time
      - Activity description (preceded by '##')
      - Notes (preceded by '>')
      - Blank lines are ignored

    Returns a list of dicts with keys: date_start, date_end, activity, notes.
    """
    entries = []
    current = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if stripped.startswith('## '):
            current['activity'] = stripped[3:]
        elif stripped.startswith('> ') and 'date_end' not in current:
            current['notes'] = stripped[2:]
        else:
            try:
                current['date_start'] = datetime.fromisoformat(stripped)
            except ValueError:
                pass
    if current:
        entries.append(current)
    return entries
