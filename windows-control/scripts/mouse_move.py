import pyautogui
import sys

pyautogui.FAILSAFE = True

if len(sys.argv) < 3:
    print("Usage: python mouse_move.py <x> <y>")
    sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])
pyautogui.moveTo(x, y, duration=0.2)
