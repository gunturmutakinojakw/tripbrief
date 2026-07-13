# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: TripBrief
import sys


def dispatch(text):
    """Parse a single line and route it to the right handler."""
    text = text.strip()
    if not text:
        return None

    cmd, _, arg = text.partition(" ")
    cmd = cmd.lower().strip()

    handlers = {
        "go": go_handler,
        "book": book_handler,
        "budget": budget_handler,
        "pack": pack_handler,
        "checklist": checklist_handler,
        "help": help_handler,
        "quit": quit_handler,
        "exit": quit_handler,
    }

    return handlers.get(cmd, lambda a: print(f"Unknown command: {cmd}"))(arg)


def go_handler(arg):
    if not arg:
        print("Usage: go <destination>")
    else:
        print(f"Departing to {arg}")


def book_handler(arg):
    if not arg:
        print("Usage: book <type> [details]")
    else:
        print(f"Booking {arg}")


def budget_handler(arg):
    if not arg:
        print("Usage: budget <total>")
    else:
        print(f"Budget set to ${float(arg):.2f}")


def pack_handler(arg):
    if not arg:
        print("Usage: pack <item>")
    else:
        print(f"Packing {arg}")


def checklist_handler(arg):
    if not arg:
        print("Usage: checklist <category>")
    else:
        print(f"Checking off items in {arg}")


def help_handler(_):
    print("Commands: go, book, budget, pack, checklist, help, quit")


def quit_handler(_):
    sys.exit(0)
