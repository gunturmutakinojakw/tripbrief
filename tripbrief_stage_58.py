# === Stage 58: Add bulk update behavior for selected records ===
# Project: TripBrief
def bulk_update_records(self, updates):
    """Apply a series of updates to records in batch."""
    for record_id, changes in updates.items():
        if record_id in self._records:
            rec = self._records[record_id]
            for key, value in changes.items():
                if key in rec and hasattr(rec[key], "update"):
                    rec[key].update(value)
                else:
                    rec[key] = value
    return list(self._records.values())
