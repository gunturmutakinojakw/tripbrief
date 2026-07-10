# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: TripBrief
def search_trips(query, **kwargs):
    results = []
    for trip in get_all_trips():
        text = (trip.get('title', '') + ' ' + trip.get('destination', '') + ' ' + 
                trip.get('summary', '')).lower()
        if query.lower() in text:
            results.append(trip)
    return results

def search_bookings(query, **kwargs):
    results = []
    for booking in get_all_bookings():
        fields = (booking.get('airline', '') + ' ' + booking.get('flight_number', '') + 
                  booking.get('hotel_name', '') + ' ' + booking.get('location', '')).lower()
        if query.lower() in fields:
            results.append(booking)
    return results

def search_budgets(query, **kwargs):
    results = []
    for budget in get_all_budgets():
        text = (budget.get('category', '') + ' ' + str(budget.get('amount', 0)) + 
                ' ' + budget.get('notes', '')).lower()
        if query.lower() in text:
            results.append(budget)
    return results

def search_packing(query, **kwargs):
    results = []
    for item in get_all_packing_items():
        text = (item.get('name', '') + ' ' + item.get('category', '')).lower()
        if query.lower() in text:
            results.append(item)
    return results

def search_local(query, **kwargs):
    results = []
    for local in get_all_locals():
        text = (local.get('name', '') + ' ' + local.get('description', '')).lower()
        if query.lower() in text:
            results.append(local)
    return results

def search_all(query, **kwargs):
    return {
        'trips': search_trips(query, **kwargs),
        'bookings': search_bookings(query, **kwargs),
        'budgets': search_budgets(query, **kwargs),
        'packing': search_packing(query, **kwargs),
        'locals': search_local(query, **kwargs)
    }
