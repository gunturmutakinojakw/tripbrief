# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: TripBrief
def get_settings():
    return {
        "default_currency": "$",
        "language": "en",
        "notifications_enabled": True,
        "auto_save": True,
        "theme": "light"
    }


def update_setting(key, value):
    settings = get_settings()
    if key not in settings:
        raise ValueError(f"Unknown setting: {key}")
    settings[key] = value
    return settings
