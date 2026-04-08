import pyautogui
import sys

pyautogui.FAILSAFE = True

if len(sys.argv) < 2:
    print("Usage: python key_press.py \"key\" (e.g., 'enter', 'ctrl+s', 'alt+tab')")
    sys.exit(1)

keys = sys.argv[1].split('+')
pyautogui.hotkey(*keys)
