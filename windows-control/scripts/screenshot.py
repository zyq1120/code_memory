import pyautogui
import sys
import base64

pyautogui.FAILSAFE = True

screenshot = pyautogui.screenshot()
import io
buffer = io.BytesIO()
screenshot.save(buffer, format='PNG')
print(base64.b64encode(buffer.getvalue()).decode())
