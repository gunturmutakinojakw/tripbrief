# === Stage 31: Add compact table rendering for long lists ===
# Project: TripBrief
def compact_table(rows, columns):
    """Render a list of dicts as a space-separated text table."""
    if not rows:
        return ""
    widths = [max(len(str(row.get(col, ''))) for row in rows) for col in columns]
    lines = []
    header = " | ".join(col.ljust(widths[i]) for i, col in enumerate(columns))
    lines.append(header)
    for row in rows:
        line = " | ".join(str(row.get(col, '')).ljust(widths[i]) for i, col in enumerate(columns))
        lines.append(line)
    return "\n".join(lines)
