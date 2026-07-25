# === Stage 53: Add command help text and usage examples ===
# Project: TripBrief
def print_usage():
    """Print command help text and usage examples for TripBrief."""
    print("TripBrief - Collaborative Travel Brief")
    print("=" * 40)
    print()
    print("Commands:")
    print("  tripbrief --init              Initialize a new travel brief project")
    print("  tripbrief --itinerary         Add or view itinerary items")
    print("  tripbrief --bookings          Manage bookings and reservations")
    print("  tripbrief --budget            Track expenses and set budgets")
    print("  tripbrief --packing           Create packing lists and notes")
    print("  tripbrief --checklist         Add local checklists for destinations")
    print()
    print("Usage Examples:")
    print('  tripbrief --init "Paris Trip"')
    print('  tripbrief --itinerary add "Visit Eiffel Tower" day=1 time="9:00 AM"')
    print('  tripbrief --bookings add hotel name="Hotel Le Marais" checkin="2024-06-01" checkout="2024-06-05"')
    print('  tripbrief --budget add expense name="Lunch at Le Petit" amount=15.50 category="food"')
    print('  tripbrief --packing add item "Passport" notes="Keep in safe place"')
    print('  tripbrief --checklist add destination="Paris" items="Musee du Louvre, Seine River Cruise, Croissant at Cafe"')
    print()
    print("For more help: tripbrief --help")
