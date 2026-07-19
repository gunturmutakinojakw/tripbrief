# === Stage 32: Add pagination helpers for long console output ===
# Project: TripBrief
def paginate(lines, chunk=8):
    """Yield line-chunks for scrolling in a terminal."""
    import sys
    width = 80
    while lines:
        n = min(chunk, len(lines))
        block = "\n".join(lines[:n])
        lines = lines[n:]
        if block.count("\n") > 1 and width - 4 < _est_w(block):
            block += "\r" + "─" * (width - 2) + "\r\n"
        sys.stdout.write(block + "\n")
        sys.stdout.flush()

def _est_w(text):
    """Rough estimate of terminal width for a wrapped line."""
    try:
        from wcwidth import wcswidth as _w
        return _w(text) or len(text)
    except ImportError:
        return len(text.replace("\t", " "))
