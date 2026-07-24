# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: TripBrief
import unittest


class TestHelpers(unittest.TestCase):
    def test_create_itinerary(self):
        from src.trip import create_itinerary, validate_itinerary
        itinerary = create_itinerary(
            title="Tokyo Day 1",
            day=1,
            notes="Visit Shibuya Crossing and Harajuku."
        )
        self.assertEqual(itinerary["title"], "Tokyo Day 1")
        self.assertEqual(itinerary["day"], 1)

    def test_create_booking(self):
        from src.bookings import create_booking, validate_booking
        booking = create_booking(
            hotel="Grand Hotel",
            checkin="2025-06-01",
            checkout="2025-06-05",
            guests=3,
            currency="USD"
        )
        self.assertEqual(booking["hotel"], "Grand Hotel")
        self.assertEqual(validate_booking(booking), True)

    def test_validate_invalid_date(self):
        from src.bookings import validate_booking
        bad = create_booking(hotel="X", checkin="2025-13-01", checkout="2025-14-01", guests=1, currency="USD")
        self.assertEqual(validate_booking(bad), False)

    def test_validate_invalid_guests(self):
        from src.bookings import validate_booking
        bad = create_booking(hotel="X", checkin="2025-06-01", checkout="2025-06-02", guests=0, currency="USD")
        self.assertEqual(validate_booking(bad), False)


if __name__ == "__main__":
    unittest.main()
