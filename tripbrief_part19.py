# === Stage 19: Add undo support for the last simple mutation ===
# Project: TripBrief
class UndoStack:
    def __init__(self):
        self.history = []
        self.max_undo = 10

    def push(self, state):
        if len(self.history) >= self.max_undo:
            del self.history[0]
        self.history.append(state.copy())

    def undo(self):
        if not self.history:
            return None
        last = self.history.pop()
        return last
