# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: TripBrief
def format_itinerary(itinerary):
    """Format a single itinerary entry for console display."""
    print(f"📅 {itinerary['date']} | 🕐 {itinerary['time']}")
    if 'location' in itinerary:
        print(f"   📍 {itinerary['location']}")
    if 'activities' in itinerary:
        for act in itinerary['activities']:
            print(f"   • {act}")
    return

def format_budget(budget, currency_symbol="$"):
    """Format budget summary with totals."""
    total = sum(budget.values())
    print(f"\n💰 Budget Summary")
    for category, amount in budget.items():
        print(f"   {category}: {currency_symbol}{amount:.2f}")
    print(f"   ────────────────")
    print(f"   Total: {currency_symbol}{total:.2f}")
