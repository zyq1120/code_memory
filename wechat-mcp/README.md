# WeChat MCP

Windows 电脑端微信消息监控与发送 MCP。

## 功能

- 📸 截取微信窗口截图
- 👤 搜索并打开联系人聊天窗口
- ✉️ 给指定联系人发送消息
- 🔍 支持独立聊天窗口识别和消息发送

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 给指定联系人发送消息

```python
from server import send_message_to_contact

send_message_to_contact("联系人名称", "消息内容")
```

### 2. 给当前聊天窗口发送消息

```python
from server import send_message_to_current

send_message_to_current("消息内容")
```

### 3. 获取微信状态

```python
from server import get_wechat_status

status = get_wechat_status()
print(status)
```

### 4. 命令行测试

```bash
# 给当前聊天窗口发送消息
python test_wechat.py send -m "测试消息"

# 给指定联系人发送消息
python test_wechat.py send-to -c "杨思雨" -m "测试消息"

# 获取微信状态
python test_wechat.py status
```

## MCP 工具

```json
{
  "tools": [
    {
      "name": "wechat_get_status",
      "description": "获取微信窗口状态"
    },
    {
      "name": "wechat_send_message",
      "description": "给当前聊天窗口发送消息"
    },
    {
      "name": "wechat_send_to_contact",
      "description": "给指定联系人发送消息"
    }
  ]
}
```

## 注意事项

1. 微信窗口需要保持打开状态
2. 发送消息时会自动激活微信窗口
3. 使用剪贴板输入，避免输入法问题
4. 支持独立聊天窗口（Dragon）和主窗口

## 文件结构

```
wechat-mcp/
├── server.py         # MCP 服务器主程序
├── test_wechat.py    # 测试工具
├── requirements.txt  # Python 依赖
└── README.md         # 说明文档
```
