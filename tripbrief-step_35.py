# === Stage 35: Add active user switching and user-specific records ===
# Project: TripBrief
class TripBrief:
    def __init__(self, itinerary=None, bookings=None, budgets=None):
        self.itinerary = itinerary or []
        self.bookings = bookings or []
        self.budgets = budgets or []

    def add_itinerary(self, date, location, activities):
        self.itinerary.append({"date": date, "location": location, "activities": activities})

    def add_booking(self, service, details):
        self.bookings.append({"service": service, **details})

    def add_budget(self, category, amount):
        self.budgets.append({"category": category, "amount": amount})
