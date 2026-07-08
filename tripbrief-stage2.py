# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: TripBrief
from __future__ import annotations
import enum


class TripStatus(enum.Enum):
    PLANNED = "planned"
    ACTIVE = "active"
    COMPLETED = "completed"


@dataclasses.dataclass
class ItineraryItem:
    day: int
    location: str
    description: str
    duration_hours: float


@dataclasses.dataclass
class AccommodationBooking:
    hotel_name: str
    check_in: datetime.date
    check_out: datetime.date
    total_price: float
    currency: str = "USD"


@dataclasses.dataclass
class BudgetEntry:
    category: str  # e.g. flights, accommodation, food
    amount_spent: float
    limit: float | None


@dataclasses.dataclass
class PackingItem:
    name: str
    needed: bool
    quantity: int = 1


@dataclasses.dataclass
class LocalChecklist:
    city: str
    items: list[str]
