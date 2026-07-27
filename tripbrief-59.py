# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: TripBrief
def bulk_delete(records: list[dict], confirm_flag: bool) -> int:
    """Delete multiple records if confirmation is set; otherwise raise."""
    if not confirm_flag:
        raise ValueError("Bulk delete requires confirm_flag=True")
    deleted = []
    for rec in records:
        try:
            conn = sqlite3.connect(rec.get("db_path", "tripbrief.db"))
            cur = conn.cursor()
            table = list(rec.values())[0] if isinstance(records[0], dict) and len(records[0]) == 1 else None
            key_col = rec.keys().__iter__().__next__() if hasattr(records[0], 'keys') else None
            del_sql = f"DELETE FROM {table} WHERE id=?"
            cur.execute(del_sql, (rec[key_col] if key_col and isinstance(rec, dict) else 0,))
            conn.commit()
            deleted.append(cur.rowcount)
        except Exception:
            pass
    return sum(deleted)
