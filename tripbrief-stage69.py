# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: TripBrief
def reset_demo_data():
    """Reset all TripBrief data to demo state and write back."""
    import json, os
    base = "data"
    files = {"itinerary.json": ITINERARY, "bookings.json": BOOKINGS,
             "budget.json": BUDGET, "packing_notes.json": PACKING_NOTES,
             "local_checklists.json": LOCAL_CHECKLISTS}
    for name, data in files.items():
        path = os.path.join(base, name)
        if os.path.exists(path):
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
            print(f"[OK] {name} reset.")
    else:
        print("[WARN] data dir missing; skipping write.")

if __name__ == "__main__":
    print("TripBrief — resetting demo data...")
    reset_demo_data()
