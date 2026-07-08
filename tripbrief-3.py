# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: TripBrief
def _validate_id(obj):
    if not obj.get('id'):
        raise ValueError(f"{obj.__class__.__name__}: missing id")

def _validate_short_text(obj, field, max_len=200):
    val = getattr(obj, field, '') or ''
    if len(val) > max_len:
        raise ValueError(
            f"{obj.__class__.__name__}.{field} exceeds {max_len} chars "
            f"(got {len(val)})")

def _validate_required(obj, fields):
    for f in fields:
        val = getattr(obj, f, '') or ''
        if not val and obj.get(f) is None:
            raise ValueError(
                f"{obj.__class__.__name__}: required field '{f}' missing")
