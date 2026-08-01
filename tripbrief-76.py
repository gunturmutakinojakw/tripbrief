# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: TripBrief
import signal
import sys


def handle_keyboard_interrupt(signum, frame):
    print("\n\nTripBrief: interrupted by user (Ctrl+C). Exiting gracefully...")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_keyboard_interrupt)
