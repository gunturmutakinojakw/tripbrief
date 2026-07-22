# === Stage 42: Add CSV export without external dependencies ===
# Project: TripBrief
def export_csv(trip):
    """Export trip data to CSV format without external dependencies."""
    import csv
    output = []
    for section in ['itinerary', 'bookings', 'budgets', 'packing_notes']:
        items = getattr(trip, section, [])
        if not items:
            continue
        headers = list(items[0].keys()) if isinstance(items[0], dict) else None
        if headers is None:
            for item in items:
                output.append([str(item)])
            return '\n'.join('\t'.join(row) for row in output) + '\n'
        for item in items:
            row = [item.get(h, '') for h in headers]
            output.append(row)
    return csv.writer(output).writerow(
        list(zip(*output)) if len(output) > 1 else output[0]
    )
