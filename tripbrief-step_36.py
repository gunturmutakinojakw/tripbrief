# === Stage 36: Add templates for quickly creating common records ===
# Project: TripBrief
class Template:
    def __init__(self, name, model, fields):
        self.name = name
        self.model = model
        self.fields = fields

    def fill(self, **kwargs):
        data = {}
        for f in self.fields:
            if f in kwargs:
                data[f] = kwargs[f]
            elif hasattr(f, 'default') and f.default is not None:
                data[f] = f.default()
        return self.model(**data)

class ItineraryTemplate(Template):
    def __init__(self):
        super().__init__("itinerary", Itinerary, ["date", "city"])

class BookingTemplate(Template):
    def __init__(self):
        super().__init__("booking", Booking, ["destination", "check_in", "check_out", "guests"])

class BudgetItemTemplate(Template):
    def __init__(self):
        super().__init__("budget_item", BudgetItem, ["category", "amount", "currency"])

class PackingItemTemplate(Template):
    def __init__(self):
        super().__init__("packing_item", PackingItem, ["item", "quantity"])

class LocalChecklistTemplate(Template):
    def __init__(self):
        super().__init__("local_checklist", LocalChecklist, ["city", "tasks"])
