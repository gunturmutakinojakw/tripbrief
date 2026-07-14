# === Stage 16: Add argparse support for the most common commands ===
# Project: TripBrief
import argparse

def main():
    parser = argparse.ArgumentParser(description="TripBrief CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # itinerary command
    it_parser = subparsers.add_parser("itinerary", help="Manage itineraries")
    it_parser.add_argument("--add", "-a", action="store_true", help="Add a new itinerary")
    it_parser.add_argument("--list", "-l", action="store_true", help="List all itineraries")

    # booking command
    bk_parser = subparsers.add_parser("booking", help="Manage bookings")
    bk_parser.add_argument("--add", "-a", action="store_true", help="Add a new booking")
    bk_parser.add_argument("--list", "-l", action="store_true", help="List all bookings")

    # budget command
    bd_parser = subparsers.add_parser("budget", help="Manage budgets")
    bd_parser.add_argument("--add", "-a", action="store_true", help="Add a new budget entry")
    bd_parser.add_argument("--list", "-l", action="store_true", help="List all budgets")

    # packing command
    pk_parser = subparsers.add_parser("packing", help="Manage packing notes")
    pk_parser.add_argument("--add", "-a", action="store_true", help="Add a new item")
    pk_parser.add_argument("--list", "-l", action="store_true", help="List all items")

    # checklist command
    ck_parser = subparsers.add_parser("checklist", help="Manage local checklists")
    ck_parser.add_argument("--add", "-a", action="store_true", help="Add a new item")
    ck_parser.add_argument("--list", "-l", action="store_true", help="List all items")

    args = parser.parse_args()
