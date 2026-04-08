import asyncio
import json
import sys
import time
from pathlib import Path
import pyautogui
pyautogui.FAILSAFE = False
import pygetwindow as gw
from PIL import Image, ImageGrab
import pyperclip


def get_chat_window():
    """获取聊天窗口（Dragon）"""
    windows = gw.getWindowsWithTitle("Dragon")
    for win in windows:
        if "Dragon" in win.title:
            return win
    return None


def capture_window():
    """截取窗口"""
    win = get_chat_window()
    if not win:
        windows = gw.getWindowsWithTitle("微信")
        for w in windows:
            if w.width > 500 and w.width < 2000:
                win = w
                break
    
    if not win:
        return None
    
    try:
        win.activate()
        time.sleep(0.3)
    except:
        pass
    
    bbox = (win.left, win.top, win.right, win.bottom)
    return ImageGrab.grab(bbox=bbox)


def verify_chat():
    """Step 1: 确认聊天窗口"""
    wins = gw.getWindowsWithTitle("WeChat")
    if not wins:
        wins = gw.getWindowsWithTitle("微信")
    
    if not wins:
        return False, "未找到聊天窗口"
    
    win = wins[0]
    
    print(f"聊天窗口: {win.title}")
    print(f"位置: ({win.left}, {win.top}), 大小: ({win.width}, {win.height})")
    
    img = capture_window()
    if img:
        img.save(str(Path(__file__).parent / "verify.png"))
    
    return True, None


def input_message(message):
    """Step 2-3: 输入消息并确认"""
    wins = gw.getWindowsWithTitle("WeChat")
    if not wins:
        wins = gw.getWindowsWithTitle("微信")
    
    if not wins:
        return False, "未找到聊天窗口"
    
    win = wins[0]
    
    win_left = win.left
    win_top = win.top
    win_width = win.width
    win_height = win.height
    win_right = win.left + win_width
    win_bottom = win.top + win_height
    
    input_x = win_left + win_width // 2
    input_y = win_bottom - 60
    
    pyautogui.click(input_x, input_y)
    time.sleep(0.2)
    
    pyperclip.copy(message)
    time.sleep(0.1)
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    
    input_bbox = (win_left, win_bottom - 80, win_right, win_bottom - 20)
    input_img = ImageGrab.grab(bbox=input_bbox)
    input_img.save(str(Path(__file__).parent / "input_verify.png"))
    
    return True, None


def send_message():
    """Step 4: 发送消息"""
    wins = gw.getWindowsWithTitle("WeChat")
    if not wins:
        wins = gw.getWindowsWithTitle("微信")
    
    if not wins:
        return False, "未找到聊天窗口"
    
    pyautogui.press('enter')
    time.sleep(0.3)
    
    img = capture_window()
    if img:
        img.save(str(Path(__file__).parent / "result.png"))
    
    return True, None


def send_message_to_current(message):
    """给当前聊天窗口发送消息"""
    print(f"发送消息: {message}")
    
    print("\n=== Step 1: 确认聊天窗口 ===")
    success, err = verify_chat()
    if not success:
        return False, err
    
    print("\n=== Step 2-3: 输入消息 ===")
    success, err = input_message(message)
    if not success:
        return False, err
    
    print("\n=== Step 4: 发送 ===")
    success, err = send_message()
    if not success:
        return False, err
    
    print("\n=== 发送完成! ===")
    return True, None


def search_contact(contact_name):
    """搜索联系人"""
    wins = gw.getWindowsWithTitle("WeChat")
    if not wins:
        wins = gw.getWindowsWithTitle("微信")
    
    if not wins:
        return False, "未找到微信窗口"
    
    win = wins[0]
    
    try:
        win.restore()
        time.sleep(0.3)
        win.activate()
        time.sleep(0.5)
    except:
        pass
    
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    
    pyperclip.copy(contact_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.8)
    
    pyautogui.press('enter')
    time.sleep(0.8)
    
    return True, None


def send_message_to_contact(contact_name, message):
    """给指定联系人发送消息"""
    print(f"搜索联系人: {contact_name}")
    success, err = search_contact(contact_name)
    if not success:
        return False, err
    
    print(f"发送消息: {message}")
    success, err = send_message_to_current(message)
    return success, err


def get_wechat_status():
    """获取微信状态"""
    wins = gw.getWindowsWithTitle("WeChat")
    if not wins:
        wins = gw.getWindowsWithTitle("微信")
    
    if wins:
        win = wins[0]
        return {
            "status": "running",
            "title": win.title,
            "position": {"x": win.left, "y": win.top},
            "size": {"width": win.width, "height": win.height}
        }
    
    return {"status": "not_running", "message": "微信未运行"}


TOOLS = [
    {
        "name": "wechat_get_status",
        "description": "获取微信状态",
        "inputSchema": {"type": "object", "properties": {}}
    },
    {
        "name": "wechat_send_message",
        "description": "给当前聊天窗口发送消息",
        "inputSchema": {
            "type": "object",
            "properties": {
                "message": {"type": "string", "description": "消息内容"}
            },
            "required": ["message"]
        }
    },
    {
        "name": "wechat_send_to_contact",
        "description": "给指定联系人发送消息",
        "inputSchema": {
            "type": "object",
            "properties": {
                "contact_name": {"type": "string", "description": "联系人名称"},
                "message": {"type": "string", "description": "消息内容"}
            },
            "required": ["contact_name", "message"]
        }
    }
]


async def handle_tool(name, arguments):
    """处理工具调用"""
    if name == "wechat_get_status":
        result = get_wechat_status()
        return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]}
    
    elif name == "wechat_send_message":
        message = arguments.get("message")
        if not message:
            return {"content": [{"type": "text", "text": "错误: 需要指定消息内容"}]}
        
        success, err = send_message_to_current(message)
        if success:
            return {"content": [{"type": "text", "text": f"[OK] 消息已发送\n内容: {message}"}]}
        else:
            return {"content": [{"type": "text", "text": f"[ERROR] 错误: {err}"}]}
    
    elif name == "wechat_send_to_contact":
        contact_name = arguments.get("contact_name")
        message = arguments.get("message")
        
        if not contact_name or not message:
            return {"content": [{"type": "text", "text": "错误: 需要指定联系人和消息内容"}]}
        
        success, err = send_message_to_contact(contact_name, message)
        if success:
            return {"content": [{"type": "text", "text": f"[OK] 消息已发送给 {contact_name}\n内容: {message}"}]}
        else:
            return {"content": [{"type": "text", "text": f"[ERROR] 错误: {err}"}]}
    
    return {"content": [{"type": "text", "text": "未知命令"}]}


async def main():
    """MCP 主循环"""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            request = json.loads(line)
            
            if request.get("method") == "tools/list":
                response = {"jsonrpc": "2.0", "id": request.get("id"), "result": {"tools": TOOLS}}
                print(json.dumps(response), flush=True)
            
            elif request.get("method") == "tools/call":
                tool_name = request.get("name")
                tool_args = request.get("arguments", {})
                result = await handle_tool(tool_name, tool_args)
                response = {"jsonrpc": "2.0", "id": request.get("id"), "result": result}
                print(json.dumps(response), flush=True)
        
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": str(e)}), flush=True)


if __name__ == "__main__":
    asyncio.run(main())
