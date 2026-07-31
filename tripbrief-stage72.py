# === Stage 72: Add Markdown report export ===
# Project: TripBrief
def export_to_markdown(report):
    """Export TripBrief report to a compact Markdown string."""
    lines = []
    for section in report:
        if section.get("type") == "itinerary":
            lines.append(f"# {section['title']}\n")
            for day in section["days"]:
                lines.append(f"## Day {day['number']} - {day['location']}\n")
                for event in day["events"]:
                    lines.append(f"- **{event.get('time', 'N/A')}**: {event['activity']}\n")
        elif section.get("type") == "booking":
            lines.append(f"## Booking: {section['destination']}\n")
            lines.append(f"- Flight: {section['flight_number']} ({section['airline']})\n")
            lines.append(f"- Hotel: {section['hotel']['name']} - ${section['hotel']['cost_per_night']} x {section['hotel']['nights']} nights\n")
        elif section.get("type") == "budget":
            lines.append(f"# Budget Summary\n")
            total = sum(item["amount"] for item in section["items"])
            lines.append(f"- Total Estimated: ${total:.2f}\n")
        elif section.get("type") == "packing":
            lines.append(f"# Packing List\n")
            for category in section["categories"]:
                lines.append(f"## {category['name']}\n")
                for item in category["items"]:
                    lines.append(f"- [ ] {item['item']} x {item['quantity']}\n")
        elif section.get("type") == "checklist":
            lines.append(f"# Local Checklist\n")
            location = section["location"]
            for task in section["tasks"]:
                lines.append(f"## {task['name']}\n")
                for item in task["items"]:
                    lines.append(f"- [ ] {item}\n")

    return "\n".join(lines)
