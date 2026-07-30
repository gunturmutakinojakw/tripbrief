# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: TripBrief
# TripBrief — Compact Changelog Generator
# Usage: python changelog.py --log activity_log.json --out CHANGELOG.md

import argparse, json, sys
from datetime import datetime

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--log", required=True)
    p.add_argument("--out", default="CHANGELOG.md")
    return p.parse_args()

def main():
    args = parse_args()
    with open(args.log, "r") as f:
        log = json.load(f)

    # Group entries by date (most recent first), then by category order.
    category_order = {
        "feat": 1, "fix": 2, "improvement": 3, "other": 4
    }

    def sort_key(entry):
        ts = entry.get("timestamp", "")[:10]
        cat = entry.get("category", "other")
        return (ts, category_order.get(cat, 9))

    log.sort(key=sort_key)

    lines = ["# TripBrief Changelog\n"]
    current_date = None
    for entry in log:
        ts = entry.get("timestamp", "")[:10]
        if ts != current_date:
            lines.append(f"\n## {ts}\n")
            current_date = ts

        emoji = {"feat": "✨", "fix": "🐛", "improvement": "💡", "other": "➕"}.get(
            entry.get("category", ""), "➕"
        )
        desc = entry.get("description", "")[:120]
        lines.append(f"- {emoji} {desc}")

    with open(args.out, "w") as f:
        f.write("\n".join(lines))

    print(f"Changelog written to {args.out}")

if __name__ == "__main__":
    main()
