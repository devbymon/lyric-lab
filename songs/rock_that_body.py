import sys
import time

# ANSI colors
Write = "\033[0;37m"
Red = "\033[0;91m"
Green = "\033[0;32m"
Yellow = "\033[0;93m"
Blue = "\033[0;34m"
Magenta = "\033[0;95m"
Cyan = "\033[0;36m"


def write_text(text, total_time_for_text=0.0, color=Write, jump_line=True, wait_time=0.0):
    """Print text character by character with a simple animated effect."""
    text = str(text)
    if total_time_for_text > 0 and len(text) > 0:
        delay = total_time_for_text / len(text)
    else:
        delay = wait_time

    for char in text:
        sys.stdout.write(f"{color}{char}{Write}")
        sys.stdout.flush()
        time.sleep(delay if delay > 0 else 0)

    if jump_line:
        sys.stdout.write("\n")
        sys.stdout.flush()

    if wait_time > 0:
        time.sleep(wait_time)


def printLyrics():
    lines = [
        ("I wanna da-", 0.11, 0.35),
        ("I wanna dance in the lights", 0.045, 0.75),
        ("I wanna ro-", 0.10, 0.35),
        ("I wanna rock your body", 0.055, 0.85),
        ("I wanna go", 0.09, 0.28),
        ("I wanna go for a ride", 0.05, 0.7),
        ("Hop in the music and", 0.06, 0.25),
        ("Rock your body", 0.07, 0.55),
        ("Rock that body", 0.065, 0.18),
        ("come on, come on", 0.04, 0.12),
        ("Rock that body", 0.07, 0.16),
        ("(Rock your body)", 0.032, 0.25),
        ("Rock that body", 0.065, 0.22),
        ("come on, come on", 0.04, 0.12),
        ("Rock that body", 0.07, 2.5),
    ]

    for line, char_delay, pause_after in lines:
        for char in line:
            color = Yellow if line == "(Rock your body)" else Magenta
            sys.stdout.write(f"{color}{char}{Write}")
            sys.stdout.flush()
            time.sleep(char_delay)
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(pause_after)


if __name__ == "__main__":
    printLyrics()
