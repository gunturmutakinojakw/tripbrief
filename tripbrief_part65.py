# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: TripBrief
def merge_imports(existing, candidate):
    """Merge two import blocks while removing exact duplicates."""
    seen = set()
    merged = []
    for line in existing:
        stripped = line.strip().lower()
        if stripped.startswith('import ') or stripped.startswith('from '):
            key = stripped.split()[1]
            if key not in seen:
                seen.add(key)
                merged.append(line)
    for line in candidate:
        stripped = line.strip().lower()
        if stripped.startswith('import ') or stripped.startswith('from '):
            key = stripped.split()[1]
            if key not in seen:
                seen.add(key)
                merged.append(line)
    return merged
