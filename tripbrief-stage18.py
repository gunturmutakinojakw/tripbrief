# === Stage 18: Add an activity log with timestamps and action names ===
# Project: TripBrief
import json
from datetime import datetime, timezone


class ActivityLog:
    """Records timestamped actions in chronological order."""

    def __init__(self):
        self._entries = []

    @staticmethod
    def _now_iso():
        return datetime.now(timezone.utc).isoformat()

    def log(self, action_name: str) -> dict:
        entry = {
            "timestamp": self._now_iso(),
            "action": action_name,
        }
        self._entries.append(entry)
        return entry.copy()

    def append_entry(self, timestamp: str, action_name: str) -> None:
        self._entries.append({"timestamp": timestamp, "action": action_name})

    def get_all(self) -> list[dict]:
        return list(self._entries)

    def summary(self) -> str:
        lines = ["Activity Log", "=" * 40]
        for i, e in enumerate(self._entries, 1):
            lines.append(f"{i}. [{e['timestamp']}] {e['action']}")
        return "\n".join(lines)

    def to_json(self) -> str:
        return json.dumps(self.get_all(), indent=2)
