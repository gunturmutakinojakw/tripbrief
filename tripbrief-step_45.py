# === Stage 45: Add restore from backup with validation ===
# Project: TripBrief
import json, os, hashlib

def restore_from_backup(target_path, backup_path):
    """Validate a JSON backup and restore it to target (or skip if corrupted)."""
    if not os.path.isfile(backup_path):
        print(f"Backup file not found: {backup_path}")
        return False
    try:
        with open(backup_path) as f:
            data = json.load(f)
        expected = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:12]
        meta = data.get("__meta", {})
        if str(meta.get("version", "")) != "1.0":
            print("Unsupported backup version.")
            return False
        with open(target_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Restored {len(data)} entries to {target_path} (sha={expected}).")
        return True
    except Exception as e:
        print(f"Restore failed – backup is corrupted: {e}")
        return False

def init_backup(target_path):
    """Create a clean initial backup of the target file."""
    if not os.path.isfile(target_path):
        open(target_path, 'w').close()
    with open(target_path) as f:
        data = json.load(f)
    meta = {"version": "1.0", "entries": len(data)}
    backup = {**data, "__meta": meta}
    back_path = target_path + ".bak"
    with open(back_path, 'w') as f:
        json.dump(backup, f, indent=4)
    print(f"Backup saved to {back_path}")

if __name__ == '__main__':
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "init"
    path = 'trip.json'
    if cmd == "init":
        init_backup(path)
    elif cmd == "restore":
        restore_from_backup(path, path + ".bak")
