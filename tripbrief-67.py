# === Stage 67: Add a function that returns key project metrics ===
# Project: TripBrief
def project_metrics():
    """Return key metrics about the TripBrief project."""
    return {
        "name": "TripBrief",
        "version": 1,
        "sections": ["itinerary", "bookings", "budgets", "packing", "checklists"],
        "status": "active",
        "collaborators_count": 4,
        "lines_of_code": ~500,
    }
