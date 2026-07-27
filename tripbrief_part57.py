# === Stage 57: Add structured result objects for command handlers ===
# Project: TripBrief
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TripBriefResult:
    """Structured result returned by command handlers."""
    status: str = "ok"
    message: str = ""
    itinerary: dict = field(default_factory=dict)
    bookings: list[dict] = field(default_factory=list)
    budget: dict = field(default_factory=dict)
    packing_notes: list[str] = field(default_factory=list)
    local_checklist: list[dict] = field(default_factory=list)


@dataclass
class BookingResult(TripBriefResult):
    """Extended result when a booking is created or confirmed."""
    provider: str = ""
    reference_id: Optional[str] = None
