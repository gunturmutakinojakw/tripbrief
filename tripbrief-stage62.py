# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: TripBrief
def score_activities(activities, budget_remaining, weather_forecast):
    """Score activities based on preferences, budget, and weather."""
    scored = []
    for act in activities:
        if "budget" in act and "cost" in act["budget"]:
            cost = act["budget"]["cost"]
            if cost > budget_remaining:
                score = 0
            else:
                score = 10 - (cost / budget_remaining) * 5
        else:
            score = 8

        for pref in act.get("preferences", []):
            if pref in weather_forecast:
                score += 3
        scored.append({"activity": act["name"], "score": round(score, 1)})

    return sorted(scored, key=lambda x: -x["score"])[:5]
