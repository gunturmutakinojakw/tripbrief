# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: TripBrief
class TripBrief:
    def __init__(self):
        self.brief = {}

    def clear(self, confirmed=False):
        if confirmed:
            self.brief.clear()
            print("Trip brief cleared successfully.")
        else:
            raise PermissionError("Confirmation flag not set. Use a confirmed trip to clear.")

tripbrief = TripBrief()
