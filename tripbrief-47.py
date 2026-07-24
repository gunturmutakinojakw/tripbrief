# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: TripBrief
def demo_tripbrief():
    """Run a compact end-to-end demo of TripBrief."""
    from tripbrief import Itinerary, Booking, Budget, PackingNote, Checklist, Brief

    # 1. Create the brief for "Tokyo Spring"
    b = Brief(title="Tokyo Spring", travelers=2, currency="JPY")

    # 2. Add an itinerary
    itin = Itinerary(
        day=1,
        city="Shibuya",
        spots=["Meiji Shrine", "Harajuku"],
        notes="Visit Meiji Shrine early; Harajuku for street food.",
    )
    b.add_itinerary(itin)

    # 3. Add a booking
    bk = Booking(
        name="Shibuya Hotel",
        check_in="2026-04-15",
        check_out="2026-04-18",
        price=45000,
        currency="JPY",
        source="Booking.com",
    )
    b.add_booking(bk)

    # 4. Add a budget line
    bd = Budget(
        category="Transport",
        amount=3000,
        limit=5000,
        currency="JPY",
    )
    b.add_budget(bd)

    # 5. Packing note and checklist
    pn = PackingNote(item="Light jacket", reason="Evening chills")
    cl = Checklist(
        item="Bring adapter (Type A/B)", done=False,
        item="Download offline maps", done=True,
    )
    b.add_packing_note(pn)
    b.add_checklist(cl)

    # 6. Print a summary
    print("=" * 50)
    print(f"Brief: {b.title}")
    print(f"Travelers: {b.travelers} | Currency: {b.currency}")
    for i in b.itineraries:
        print(f"Day {i.day}: {', '.join(i.spots)} - {i.notes}")
    print(f"Bookings:")
    for bk in b.bookings:
        print(f"  {bk.name} | {bk.check_in} to {bk.check_out} | ¥{bk.price:,}")
    print(f"Budgets:")
    print(b.budgets)
    print(f"Packing notes:")
    for pn in b.packing_notes:
        print(f"  - {pn.item}: {pn.reason}")
    print(f"Checklist:")
    for item, done in b.checklists.items():
        status = "✓" if done else "○"
        print(f"  {status} {item}")

demo_tripbrief()
