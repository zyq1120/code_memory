import pyautogui
import sys

pyautogui.FAILSAFE = True

if len(sys.argv) < 3:
    print("Usage: python scroll.py [up|down] <amount>")
    sys.exit(1)

direction = sys.argv[1]
amount = int(sys.argv[2])

if direction == 'up':
    pyautogui.scroll(amount)
else:
    pyautogui.scroll(-amount)
