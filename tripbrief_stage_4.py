# === Stage 4: Implement create operations for the primary records ===
# Project: TripBrief
from datetime import date, timedelta

def create_itinerary(trip_id, day_num, activities):
    """Register a single-day itinerary."""
    trip = _lookup_trip(trip_id)
    record = {
        "trip_id": trip_id,
        "day": day_num,
        "activities": [a for a in activities if isinstance(a, str)],
        "created_at": date.today().isoformat(),
    }
    trip["itineraries"].append(record)
    return record

def create_booking(trip_id, provider, details):
    """Register a booking (flight / hotel / car)."""
    trip = _lookup_trip(trip_id)
    booking = {
        "trip_id": trip_id,
        "type": provider.lower(),  # flight | hotel | car
        "details": dict(details),
        "created_at": date.today().isoformat(),
    }
    trip["bookings"].append(booking)
    return booking

def create_budget(trip_id, currency="USD", items=None):
    """Register a budget record."""
    trip = _lookup_trip(trip_id)
    budget = {
        "trip_id": trip_id,
        "currency": currency,
        "items": [] if items is None else [dict(i) for i in items],
        "created_at": date.today().isoformat(),
    }
    trip["budgets"].append(budget)
    return budget

def create_packing_list(trip_id):
    """Register an empty packing list."""
    trip = _lookup_trip(trip_id)
    record = {
        "trip_id": trip_id,
        "items": [],
        "created_at": date.today().isoformat(),
    }
    trip["packing_lists"].append(record)
    return record

def create_local_checklist(trip_id, location):
    """Register a local checklist for a destination."""
    trip = _lookup_trip(trip_id)
    record = {
        "trip_id": trip_id,
        "location": location,
        "items": [],
        "created_at": date.today().isoformat(),
    }
    trip["local_checklists"].append(record)
    return record
