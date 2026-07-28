# === Stage 60: Add saved views for frequently used filters ===
# Project: TripBrief
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}
    
    def apply(self, records):
        result = []
        for r in records:
            match = True
            for key, value in self.filters.items():
                if not self._match_field(r, key, value):
                    match = False
                    break
            if match:
                result.append(r)
        return result
    
    def _match_field(self, record, field, value):
        try:
            return str(record.get(field)) == str(value)
        except Exception:
            return False

class ViewManager:
    def __init__(self):
        self.views = {}
    
    def add_view(self, name, filters=None):
        if not name or len(name) > 50:
            raise ValueError("Name must be between 1 and 50 characters")
        view = SavedView(name, filters)
        self.views[name] = view
        return view
    
    def get_view(self, name):
        return self.views.get(name)
    
    def remove_view(self, name):
        if name in self.views:
            del self.views[name]
            return True
        return False
    
    def list_views(self):
        return list(self.views.keys())

def load_saved_views(data_file="saved_views.json"):
    import json
    try:
        with open(data_file, "r") as f:
            data = json.load(f)
        manager = ViewManager()
        for name in data.get("views", []):
            manager.add_view(name)
        return manager
    except Exception:
        return ViewManager()

def save_views(manager, data_file="saved_views.json"):
    import json
    data = {"views": list(manager.views.keys())}
    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)
