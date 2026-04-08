import pyautogui
import pygetwindow as gw
from PIL import ImageGrab
import time

def capture_wechat():
    """截取微信窗口"""
    wins = gw.getWindowsWithTitle('WeChat')
    if not wins:
        wins = gw.getWindowsWithTitle('微信')
    
    if wins:
        win = wins[0]
        win.restore()
        time.sleep(0.3)
        
        bbox = (win.left, win.top, win.right, win.bottom)
        img = ImageGrab.grab(bbox=bbox)
        return img
    return None

def main():
    count = 0
    while True:
        img = capture_wechat()
        if img:
            filename = f"wechat_capture_{count:03d}.png"
            img.save(filename)
            print(f"Saved: {filename}")
            count += 1
        
        time.sleep(2)
        
        if count >= 5:
            break

if __name__ == "__main__":
    main()
