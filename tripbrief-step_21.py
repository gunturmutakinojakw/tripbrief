# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: TripBrief
def archive_record(record, target_dir="archive"):
    """Move a completed record to an archive subdirectory."""
    import shutil
    os.makedirs(target_dir, exist_ok=True)
    fname = f"{record.get('id', 'unnamed')}_{record.get('date', '')}.json"
    dest = os.path.join(target_dir, fname)
    shutil.copy2(record_file_path(record), dest)

def restore_record(archive_dir="archive", record_id=None):
    """Restore a single archived record into the active directory."""
    import glob
    if not record_id:
        return None
    pattern = os.path.join(archive_dir, f"{record_id}_*.json")
    matches = glob.glob(pattern)
    if len(matches) != 1:
        return None
    with open(matches[0]) as fh:
        data = json.load(fh)
    shutil.copy2(matches[0], record_file_path(data))
