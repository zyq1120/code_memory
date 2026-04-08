import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = True

active_window = gw.getActiveWindow()
if active_window:
    print(active_window.title)
else:
    print("No active window found")
