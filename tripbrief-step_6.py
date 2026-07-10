# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: TripBrief
def remove_item(item_type, item_id):
    """Remove an itinerary entry, booking, budget row, packing note, or checklist by ID."""
    if item_type == "itinerary":
        for idx in range(len(trip_data["itineraries"])):
            if trip_data["itineraries"][idx]["id"] == item_id:
                del trip_data["itineraries"][idx]
                print(f"Removed itinerary {item_id}")
                return True
    elif item_type == "booking":
        bookings = trip_data.get("bookings", [])
        for idx in range(len(bookings)):
            if bookings[idx]["id"] == item_id:
                del bookings[idx]
                trip_data["bookings"] = bookings
                print(f"Removed booking {item_id}")
                return True
    elif item_type == "budget":
        rows = trip_data.get("budget", [])
        for idx in range(len(rows)):
            if rows[idx]["id"] == item_id:
                del rows[idx]
                trip_data["budget"] = rows
                print(f"Removed budget row {item_id}")
                return True
    elif item_type == "packing":
        notes = trip_data.get("packing_notes", [])
        for idx in range(len(notes)):
            if notes[idx]["id"] == item_id:
                del notes[idx]
                trip_data["packing_notes"] = notes
                print(f"Removed packing note {item_id}")
                return True
    elif item_type == "checklist":
        items = trip_data.get("local_checklists", [])
        for idx in range(len(items)):
            if items[idx]["id"] == item_id:
                del items[idx]
                trip_data["local_checklists"] = items
                print(f"Removed checklist {item_id}")
                return True
    else:
        print("Unknown item type")
        return False
