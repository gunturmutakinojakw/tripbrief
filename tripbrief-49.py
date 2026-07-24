# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: TripBrief
import unittest
from tripbrief import TripBrief


class TestTripBrief(unittest.TestCase):
    def setUp(self):
        self.tb = TripBrief()
        self.tb.add_destination("Paris", 3, "2025-10-01")
        self.tb.add_destination("Rome", 3, "2025-10-10")

    def test_update_nonexistent_returns_none(self):
        result = self.tb.update_destination("Berlin", "Paris", "2025-10-01")
        self.assertIsNone(result)

    def test_delete_nonexistent_returns_false(self):
        result = self.tb.delete_destination("Tokyo")
        self.assertFalse(result)

    def test_update_empty_itinerary(self):
        self.tb.update_destination("Berlin", "Paris", "2025-10-01")
        paris = self.tb.get_destination("Paris")
        self.assertEqual(paris["days"], 3)
        self.assertEqual(paris["cities"][0]["name"], "Berlin")

    def test_delete_and_recreate(self):
        self.assertTrue(self.tb.delete_destination("Rome"))
        self.assertIsNone(self.tb.get_destination("Rome"))
