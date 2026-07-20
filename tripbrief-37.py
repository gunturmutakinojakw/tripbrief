# === Stage 37: Add recommendations for the next useful action ===
# Project: TripBrief
class PackingOptimizer:
    """Packing suggestions based on trip details and weather."""

    def __init__(self):
        self.clothing_rules = [
            "If destination is tropical, pack light cotton clothing.",
            "If destination has cold winters, bring thermal layers and a heavy jacket.",
            "For beach destinations, include swimwear and sandals.",
            "Mountain trips need sturdy hiking boots and rain gear.",
        ]
        self.essential_items = [
            "Toiletries", "Travel documents", "Phone charger", "Reusable water bottle", "Sunscreen"
        ]
        self.weather = {"destination": None, "temperature": None}

    def get_suggestions(self):
        """Generate packing list based on current trip context."""
        suggestions = []
        for item in self.essential_items:
            suggestions.append(item)
        if self.weather["temperature"] and self.weather["temperature"] < 10:
            for rule in self.clothing_rules:
                if "cold" in rule.lower() or "thermal" in rule.lower():
                    suggestions.append(rule.split(".")[0].strip())
        return suggestions

    def update_weather(self, temperature):
        """Update weather data and refresh packing list."""
        self.weather["temperature"] = temperature
        updated_list = self.get_suggestions()
        print(f"Packing suggestions for temp {temperature}°C: {updated_list}")
