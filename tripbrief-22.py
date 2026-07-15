# === Stage 22: Add favorite records and quick favorite listing ===
# Project: TripBrief
def quick_favorites(trip_id, db):
    """Return favorite records for a trip as compact dicts."""
    cur = db.cursor()
    cur.execute(
        "SELECT id, item_type, description, notes FROM favorites WHERE trip_id=%s",
        (trip_id,),
    )
    favs = [dict(zip([c[0] for c in cur.description], row)) for row in cur.fetchall()]
    return favs


def add_favorite(trip_id, item_type="note", description="", notes="", db=None):
    """Insert a new favorite record and return its id."""
    if db is None:
        import sqlite3
        db = sqlite3.connect("tripbrief.db")
    cur = db.cursor()
    cur.execute(
        "INSERT INTO favorites (trip_id, item_type, description, notes) VALUES (?, ?, ?, ?)",
        (trip_id, item_type, description, notes),
    )
    return cur.lastrowid


def remove_favorite(fav_id, db=None):
    """Delete a favorite record by its id."""
    if db is None:
        import sqlite3
        db = sqlite3.connect("tripbrief.db")
    db.execute("DELETE FROM favorites WHERE id=?", (fav_id,))
