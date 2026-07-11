# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: TripBrief
import json


def safe_load(path, default=None):
    """Load JSON from *path* with friendly error handling."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError(f"Expected an object at {path}, got {type(data).__name__}")
        return data
    except FileNotFoundError:
        if default is not None:
            return default
        raise
    except json.JSONDecodeError as exc:
        print(f"[TripBrief] Malformed JSON in {path}: {exc.msg} (line {exc.lineno}, col {exc.colno})")
        if default is not None:
            return default
        raise
