# === Stage 43: Add CSV import for the primary record type ===
# Project: TripBrief
import csv, io


def load_csv_file(path: str) -> list[dict]:
    """Read a CSV file and return a list of dicts."""
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = []
        for row in reader:
            cleaned = {}
            for key, value in row.items():
                if value is None or value.strip() == "":
                    continue
                cleaned[key.strip()] = value.strip().strip('"')
            rows.append(cleaned)
    return rows


def load_csv_string(text: str) -> list[dict]:
    """Parse a CSV string and return a list of dicts."""
    reader = csv.DictReader(io.StringIO(text))
    rows = []
    for row in reader:
        cleaned = {}
        for key, value in row.items():
            if value is None or value.strip() == "":
                continue
            cleaned[key.strip()] = value.strip().strip('"')
        rows.append(cleaned)
    return rows
