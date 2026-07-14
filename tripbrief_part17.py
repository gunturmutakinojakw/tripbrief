# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: TripBrief
def dry_run_guard(cmd_name, *args):
    """Execute commands in a dry-run mode where no actual state changes occur."""
    print(f"[DRY RUN] Command: {cmd_name} -- args={args}")
    return None
