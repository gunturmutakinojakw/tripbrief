# === Stage 56: Add compact error classes for domain failures ===
# Project: TripBrief
class TripBriefError(Exception):
    """Base class for all TripBrief domain errors."""


class ItineraryConflict(TripBriefError):
    """A planned itinerary overlaps with an existing booking or reservation."""


class BudgetOverflow(TripBriefError):
    """The total estimated cost exceeds the allocated budget for a trip leg."""


class PackingDuplicate(TripBriefError):
    """An item is already present in a packing list and was added again."""


class LocalChecklistMissing(TripBriefError):
    """A required local checklist (e.g., permits, visas) has no entry for a destination."""


class BookingDoubleBooked(TripBriefError):
    """The same resource (hotel room, flight seat) is booked by multiple travellers."""
