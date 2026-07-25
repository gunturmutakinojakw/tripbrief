# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: TripBrief
import re


def sanitize_filename(name: str) -> str:
    """Return a filesystem-safe filename derived from *name*.

    Strips path separators, control characters, and replaces other
    unsafe characters with underscores to prevent errors on Windows,
    macOS, and Linux.
    """
    return re.sub(r'[\\/:*?"<>|]', '_', name).strip()
