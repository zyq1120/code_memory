# OpenCode Memory & Skills

This repository contains my AI agent skills, memory systems, and automation tools.

## Structure

```
├── .opencode/
│   └── skills/
│       └── skills/
│           └── skills/
│               ├── self-improving-agent/    # Self-improvement skill
│               └── ... (other skills)
├── elite-memory/                            # Long-term memory system
│   ├── SESSION-STATE.md                     # Hot memory
│   ├── MEMORY.md                            # Curated memory
│   ├── memory/                              # Daily logs
│   └── elite-memory.js                      # CLI tool
├── windows-control/                         # Windows automation scripts
│   └── scripts/
│       ├── screenshot.py
│       ├── click.py
│       ├── type_text.py
│       └── ... (other scripts)
└── wechat-mcp/                              # WeChat automation MCP
    ├── server.py
    ├── test_wechat.py
    └── README.md
```

## Skills

### Self-Improving Agent
Captures learnings, errors, and corrections for continuous improvement.

### Elite Longterm Memory
Multi-layer memory system for AI agents (hot/warm/cold/archive).

### Windows Control
Desktop automation using pyautogui (screenshots, clicks, typing).

### WeChat MCP
WeChat message automation via MCP protocol.

## Setup

```bash
# Clone repository
git clone https://github.com/zyq1120/code_memory.git

# Install dependencies
pip install pyautogui pygetwindow pillow pyperclip
```

## Usage

```bash
# Initialize memory system
node elite-memory/elite-memory.js init

# Send WeChat message
python wechat-mcp/test_wechat.py send-to -c "联系人" -m "消息"

# Take screenshot
python windows-control/scripts/screenshot_file.py screenshot.png
```

## License

MIT
