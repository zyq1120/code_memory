import pyautogui
import sys

pyautogui.FAILSAFE = True

screenshot = pyautogui.screenshot()
output_path = sys.argv[1] if len(sys.argv) > 1 else 'screenshot.png'
screenshot.save(output_path)
print(f"Screenshot saved to: {output_path}")
