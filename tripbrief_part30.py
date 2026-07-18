# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: TripBrief
from datetime import datetime, date

def parse_date(value):
    """Parse a date string in common formats and return a date object."""
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    formats = ("%Y-%m-%d", "%m/%d/%Y", "%d.%m.%Y")
    for fmt in formats:
        try:
            return datetime.strptime(str(value).strip(), fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {value!r}. Use YYYY-MM-DD, MM/DD/YYYY, or DD.MM.YYYY.")

def parse_datetime(value):
    """Parse a datetime string and return a datetime object."""
    formats = ("%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M", "%m/%d/%Y %H:%M")
    for fmt in formats:
        try:
            return datetime.strptime(str(value).strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unrecognized datetime format: {value!r}. Use YYYY-MM-DD HH:MM or similar.")

def today():
    """Return today's date."""
    return date.today()
