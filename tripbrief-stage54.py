# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: TripBrief
class Color:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    @classmethod
    def apply(cls, fg=None, bg=None):
        """Return ANSI string for given foreground/background."""
        if not cls._enabled:
            return ""
        code = ""
        if fg is not None:
            code += f"\033[{fg+30}m"
        if bg is not None:
            code += f"\033[{bg+40}m"
        return code + cls.RESET

    @classmethod
    def enabled(cls):
        """Check if stdout supports ANSI."""
        import sys
        cls._enabled = hasattr(sys.stdout, "isatty") and sys.stdout.isatty()
        return cls._enabled


def _c(fg=None, bg=None):
    """Shortcut for colorize."""
    return Color.apply(fg=fg, bg=bg) if Color.enabled() else ""


def cprint(*args, fg=None, bg=None, **kwargs):
    """Print colored or plain text depending on terminal support."""
    prefix = _c(fg, bg)
    print(prefix + "".join(str(a) for a in args), end=prefix + "\n" if not kwargs else "")


def cprint_ok(text, fg="GREEN", bg=None):
    """Print success message with green color."""
    return cprint(_c("GREEN"), text, _c())


def cprint_warn(text, fg="YELLOW", bg=None):
    """Print warning message with yellow color."""
    return cprint(_c(fg), f"[{text}]", _c())


def cprint_error(text, fg="RED", bg=None):
    """Print error message with red color."""
    return cprint(_c(fg), f"ERROR: {text}", _c())


if __name__ == "__main__":
    print("Color enabled:", Color.enabled())
