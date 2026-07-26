# === Stage 55: Add a setting to disable colorized output ===
# Project: TripBrief
def disable_color_output():
    """Disable colorized output in TripBrief CLI."""
    import os
    if os.environ.get('TRIPBRIEF_NO_COLOR'):
        os.environ['NO_COLOR'] = '1'
        os.environ['FORCE_COLOR'] = '0'
        print("Color output disabled. Set TRIPBRIEF_NO_COLOR=1 to enable.")
