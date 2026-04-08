import pygetwindow as gw
import sys

if len(sys.argv) < 2:
    print("Usage: python focus_window.py \"window title\"")
    sys.exit(1)

title = sys.argv[1]
windows = gw.getWindowsWithTitle(title)

if windows:
    windows[0].activate()
    print(f"Focused: {title}")
else:
    print(f"Window not found: {title}")
