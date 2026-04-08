import pyautogui
import sys

pyautogui.FAILSAFE = True

if len(sys.argv) < 2:
    print("Usage: python type_text.py \"text to type\"")
    sys.exit(1)

text = sys.argv[1]
pyautogui.write(text, interval=0.01)
