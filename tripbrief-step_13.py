# === Stage 13: Add file save support using a configurable path ===
# Project: TripBrief
import os, json, pathlib

class TripBrief:
    def __init__(self):
        self._itineraries = []
        self._bookings = []
        self._budgets = []
        self._packing_notes = []
        self._local_checklists = []
        self._config_path = os.environ.get("TRIPBRIEF_CONFIG", "tripbrief.json")

    @classmethod
    def load(cls, path=None):
        if path is None:
            obj = cls()
            try:
                with open(obj._config_path) as f:
                    data = json.load(f)
                obj._itineraries = data.get("itineraries", [])
                obj._bookings = data.get("bookings", [])
                obj._budgets = data.get("budgets", [])
                obj._packing_notes = data.get("packing_notes", [])
                obj._local_checklists = data.get("checklists", [])
            except FileNotFoundError:
                pass
            return obj

    def save(self, path=None):
        if path is None:
            path = self._config_path
        data = {
            "itineraries": self._itineraries,
            "bookings": self._bookings,
            "budgets": self._budgets,
            "packing_notes": self._packing_notes,
            "checklists": self._local_checklists,
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def append_itinerary(self, itinerary):
        self._itineraries.append(itinerary)

    def append_booking(self, booking):
        self._bookings.append(booking)

    def append_budget(self, budget):
        self._budgets.append(budget)

    def append_packing_note(self, note):
        self._packing_notes.append(note)

    def append_local_checklist(self, checklist):
        self._local_checklists.append(checklist)

if __name__ == "__main__":
    trip = TripBrief.load()
    trip.append_itinerary({"day": 1, "location": "Paris"})
    trip.save("my_trip.json")
