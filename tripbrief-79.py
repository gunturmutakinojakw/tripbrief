# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: TripBrief
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from trip import run_demo

if __name__ == "__main__":
    try:
        run_demo()
        print("\n✅ All validations and demo operations passed.")
    except Exception as e:
        print(f"\n❌ Validation failed: {e}")
