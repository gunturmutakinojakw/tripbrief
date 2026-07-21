# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: TripBrief
def repair_simple_integrity(trip):
    """Fix common data issues: missing currency, empty notes, invalid durations."""
    if trip.get('currency') is None:
        trip['currency'] = 'USD'
    for day in trip.get('itinerary', []):
        day.setdefault('duration_hours', 8)
        if not day.get('notes'):
            day['notes'] = ''
    budget = trip.get('budget')
    if isinstance(budget, dict) and budget:
        if budget.get('currency') is None:
            budget['currency'] = trip.get('currency', 'USD')
        for item in budget.get('items', []):
            if not item.get('cost'):
                item['cost'] = 0.0
    packing = trip.get('packing_notes', {})
    if isinstance(packing, list) and len(packing) == 0:
        trip['packing_notes'] = {'essential': [], 'optional': []}
    checks = trip.get('local_checklist', [])
    if isinstance(checks, list) and len(checks) == 0:
        trip['local_checklist'] = []
    return trip
