# === Stage 50: Add unit tests for import and export behavior ===
# Project: TripBrief
import pytest, json, os, tempfile, shutil
from pathlib import Path
from tripbrief.app.main import TripBriefApp

@pytest.fixture(autouse=True)
def _tmp_project(tmp_path):
    app = TripBriefApp()
    app._ensure_dir(Path("itineraries"))
    app._ensure_dir(Path("bookings"))
    app._ensure_dir(Path("budgets"))
    app._ensure_dir(Path("packing_notes"))
    app._ensure_dir(Path("local_checklists"))
    return Path(tmp_path)

def _write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f)

# --- Export tests -------------------------------------------------------

def test_export_itinerary_roundtrip(_tmp_project):
    app = TripBriefApp()
    itinerary = {
        "id": 1,
        "destination": "Paris",
        "days": [
            {"date": "2025-06-01", "activities": ["Eiffel Tower", "Louvre"], "notes": "book tickets"},
            {"date": "2025-06-02", "activities": ["Seine Cruise"], "notes": ""},
        ],
    }
    app._write_itinerary(json.dumps(itinerary))
    exported = app.export_itinerary(1)
    assert exported["id"] == 1
    assert len(exported["days"]) == 2

def test_export_booking_roundtrip(_tmp_project):
    app = TripBriefApp()
    booking = {"id": 10, "type": "hotel", "destination": "Paris", "check_in": "2025-06-01", "rooms": 1}
    app._write_booking(json.dumps(booking))
    exported = app.export_booking("h_1")
    assert exported["id"] == 10

def test_export_budget_roundtrip(_tmp_project):
    app = TripBriefApp()
    budget = {"id": 20, "destination": "Paris", "currency": "EUR"}
    app._write_budget(json.dumps(budget))
    exported = app.export_budget("b_1")
    assert exported["id"] == 20

def test_export_packing_note_roundtrip(_tmp_project):
    app = TripBriefApp()
    note = {"id": 30, "destination": "Paris", "items": ["passport", "charger"], "checked_off": [0]}
    app._write_packing_note(json.dumps(note))
    exported = app.export_packing_note("p_1")
    assert exported["id"] == 30

def test_export_local_checklist_roundtrip(_tmp_project):
    app = TripBriefApp()
    checklist = {"id": 40, "destination": "Paris", "items": ["buy metro pass"], "checked_off": [0]}
    app._write_local_checklist(json.dumps(checklist))
    exported = app.export_local_checklist("c_1")
    assert exported["id"] == 40

def test_export_unknown_resource_raises_error(_tmp_project):
    app = TripBriefApp()
    with pytest.raises(ValueError, match="not found"):
        app.export_itinerary(999)
