# === Stage 63: Add relationships between records where useful ===
# Project: TripBrief
class TripBrief:
    def __init__(self):
        self.itinerary = []
        self.bookings = []
        self.budgets = []
        self.packing_notes = {}
        self.local_checklists = {}
    
    def add_itinerary(self, day, location, activities):
        self.itinerary.append({"day": day, "location": location, "activities": activities})
    
    def add_booking(self, hotel, date, price):
        self.bookings.append({"hotel": hotel, "date": date, "price": price})
    
    def add_budget(self, category, amount):
        self.budgets.append({"category": category, "amount": amount})
    
    def add_packing_note(self, item, packed=False):
        self.packing_notes[item] = packed
    
    def add_local_checklist(self, city, items):
        self.local_checklists[city] = items

    # Relationships between records
    def get_itinerary_for_day(self, day):
        return [it for it in self.itinerary if it["day"] == day]
    
    def get_bookings_by_date_range(self, start_date, end_date):
        return [b for b in self.bookings if start_date <= b["date"] <= end_date]
    
    def get_packing_status(self, item):
        return self.packing_notes.get(item, None)
    
    def get_local_checklist_for_city(self, city):
        return self.local_checklists.get(city, [])

    # Budget tracking with booking costs
    def update_budget_from_bookings(self):
        for b in self.bookings:
            category = "Accommodation"
            amount = b["price"]
            existing = next((b for b in self.budgets if b["category"] == category), None)
            if existing:
                existing["amount"] += amount
            else:
                self.budgets.append({"category": category, "amount": amount})

    def get_total_budget(self):
        return sum(b["amount"] for b in self.budgets)

trip = TripBrief()
trip.add_itinerary(1, "Paris", ["Eiffel Tower", "Louvre"])
trip.add_booking("Hotel Le Parisien", "2024-06-01", 500)
trip.add_budget("Accommodation", 300)
trip.update_budget_from_bookings()
print(f"Total budget: {trip.get_total_budget()}")
