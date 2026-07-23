# === Stage 44: Add backup creation for the data file ===
# Project: TripBrief
import json, os

def backup_data():
    src = "tripbrief.json"
    dst = f"{src}.backup"
    if not os.path.exists(src):
        print("No data file found.")
        return
    with open(src) as f:
        content = f.read()
    with open(dst, 'w') as f:
        f.write(content)
    print(f"Backup saved to {dst}")

if __name__ == "__main__":
    backup_data()
