# === Stage 20: Add duplicate detection for newly created records ===
# Project: TripBrief
class DuplicateRecordError(Exception):
    pass


def check_existing_records(records, record_id):
    if any(r.get("id") == record_id for r in records):
        raise DuplicateRecordError(f"Duplicate record with id={record_id}")
