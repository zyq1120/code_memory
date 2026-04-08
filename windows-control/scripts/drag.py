import pyautogui
import sys

pyautogui.FAILSAFE = True

if len(sys.argv) < 5:
    print("Usage: python drag.py <start_x> <start_y> <end_x> <end_y>")
    sys.exit(1)

start_x = int(sys.argv[1])
start_y = int(sys.argv[2])
end_x = int(sys.argv[3])
end_y = int(sys.argv[4])

pyautogui.moveTo(start_x, start_y)
pyautogui.drag(end_x - start_x, end_y - start_y, duration=0.5)
