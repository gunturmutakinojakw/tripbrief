# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: TripBrief
def update_itinerary(itin_id, updates):
    """Update itinerary fields; returns updated dict or raises KeyError if missing."""
    try:
        itin = db.get("itineraries", itin_id)
    except KeyError as e:
        raise ValueError(f"Itinerary not found: {itin_id}") from e

    for key in ("place", "dates", "notes"):
        if key in updates and key in itin:
            itype = type(itin[key])
            new_val = updates[key]
            if isinstance(new_val, str) and itype is list:
                new_val = _parse_list(new_val)
            elif not isinstance(new_val, itype):
                raise TypeError(f"Type mismatch for '{key}': expected {itype}, got {type(new_val)}")
            itin[key] = new_val

    db.put("itineraries", itin_id, itin)
    return itin
