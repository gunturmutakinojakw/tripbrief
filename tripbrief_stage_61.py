# === Stage 61: Add performance timing for core list and search operations ===
# Project: TripBrief
import time

def benchmark_list_ops(trip_brief):
    """Benchmark core list and search operations on TripBrief."""
    # Simulate itinerary retrieval
    start = time.perf_counter()
    _ = trip_brief.get_itinerary("Day 1")
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[ITINERARY] Day 1 lookup: {elapsed:.2f}ms")

    # Simulate booking search by destination
    start = time.perf_counter()
    _ = trip_brief.search_bookings("Paris")
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[BOOKING SEARCH] Paris: {elapsed:.2f}ms")

    # Simulate budget aggregation
    start = time.perf_counter()
    _ = trip_brief.get_total_budget()
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[BUDGET] Total sum: {elapsed:.2f}ms")

    # Simulate packing notes retrieval
    start = time.perf_counter()
    _ = trip_brief.get_packing_notes("Clothing")
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[PACKING] Clothing: {elapsed:.2f}ms")

    # Simulate local checklist loading
    start = time.perf_counter()
    _ = trip_brief.get_local_checklist("Paris", "Day 3 Morning")
    elapsed = (time.perf_counter() - start) * 1000
    print(f"[CHECKLIST] Paris Day3AM: {elapsed:.2f}ms")

if __name__ == "__main__":
    from trip_brief import TripBrief
    tb = TripBrief(
        itinerary={"Day 1": "Arrive in Tokyo"},
        bookings=[{"dest": "Paris", "type": "flight"}],
        budget=3000,
        packing_notes={"Clothing": ["passport"]},
        local_checklists={"Paris Day 3 Morning": []}
    )
    benchmark_list_ops(tb)
