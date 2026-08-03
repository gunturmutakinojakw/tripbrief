# === Stage 81: Add final README text as a module string with usage examples ===
# Project: TripBrief
# TripBrief – Usage Examples & Quick Reference
# Append this to tripbrief.py for a self-contained module string.

def usage_example():
    """Demonstrate how to create and use a TripBrief."""
    brief = TripBrief("My European Adventure", "2024-09-15")
    
    # Add itinerary days
    day1 = ItineraryDay(
        date="2024-09-15",
        title="Arrival in Paris",
        activities=["Fly to CDG", "Hotel check-in", "Eiffel Tower"]
    )
    brief.add_day(day1)
    
    # Add bookings
    hotel = Booking("Hôtel de Luxe", "2024-09-15", 3, "$150/night")
    brief.book(hotel)
    
    # Add budget items
    budget = BudgetItem("Flights", 800)
    brief.add_budget(budget)
    
    # Add packing notes
    brief.pack("Passport", "Valid for 6 months", "Yes")
    
    # Add local checklist
    brief.checklist_add("Paris Museum Pass", "2024-09-15", True)
    
    return brief

# Quick reference: Available attributes and methods
def quick_reference(brief):
    """Return a summary of the trip."""
    return {
        "title": brief.title,
        "start_date": brief.start_date,
        "num_days": len(brief.days),
        "num_bookings": len(brief.bookings),
        "total_budget": sum(item.cost for item in brief.budget_items),
        "packing_list": brief.packing_notes,
    }

# Run the example if executed directly
if __name__ == "__main__":
    my_trip = usage_example()
    print(quick_reference(my_trip))
