# Self-Improving-Agent 技能学习总结

## 概述

Self-Improving-Agent 是一个持续自我改进的AI代理技能，通过系统化记录学习、错误和功能请求来支持跨会话的持续改进。

## 核心功能

### 1. 三类日志文件

| 文件 | 用途 | 记录内容 |
|------|------|----------|
| `LEARNINGS.md` | 学习日志 | 纠正、洞察、知识缺口、最佳实践 |
| `ERRORS.md` | 错误日志 | 命令失败、异常、意外行为 |
| `FEATURE_REQUESTS.md` | 功能请求 | 用户请求但尚不存在的功能 |

### 2. 检测触发器

**学习触发器**：
- 用户纠正："No, that's wrong..."
- 知识过时：文档已过时
- 发现更好方法：改进原有方案

**错误触发器**：
- 命令返回非零退出码
- 异常或堆栈跟踪
- 超时或连接失败

**功能请求触发器**：
- "Can you also..."
- "I wish you could..."
- "Is there a way to..."

### 3. 提升机制

当学习广泛适用时，提升到项目记忆：

| 学习类型 | 提升目标 | 示例 |
|---------|----------|------|
| 行为模式 | `SOUL.md` | "简洁，避免免责声明" |
| 工作流程 | `AGENTS.md` | "长任务使用子代理" |
| 工具问题 | `TOOLS.md` | "Git push需要先配置auth" |
| 项目约定 | `CLAUDE.md` | "包管理器：pnpm（非npm）" |

### 4. ID格式

- 学习：`LRN-YYYYMMDD-XXX`
- 错误：`ERR-YYYYMMDD-XXX`
- 功能：`FEAT-YYYYMMDD-XXX`

### 5. 状态定义

| 状态 | 含义 |
|------|------|
| `pending` | 未处理 |
| `in_progress` | 正在处理 |
| `resolved` | 已解决 |
| `wont_fix` | 决定不处理 |
| `promoted` | 已提升到项目记忆 |
| `promoted_to_skill` | 已提取为可复用技能 |

## 工作流程

### 1. 初始化

```bash
mkdir -p .learnings
# 创建三个日志文件
```

### 2. 记录学习

```markdown
## [LRN-20260408-001] correction

**Logged**: 2026-04-08T10:00:00Z
**Priority**: high
**Status**: pending
**Area**: backend

### Summary
微信窗口标题是"WeChat"而非"微信"

### Details
在Windows上，pygetwindow查找微信窗口时需要使用"WeChat"作为标题。

### Suggested Action
更新所有窗口查找代码，优先匹配"WeChat"

### Metadata
- Source: user_feedback
- Related Files: wechat-mcp/server.py
- Tags: windows, wechat, pygetwindow

---
```

### 3. 提升学习

当学习广泛适用时：

1. **提炼**学习为简洁规则
2. **添加**到适当的目标文件
3. **更新**原始条目状态为`promoted`

### 4. 周期审查

```bash
# 统计待处理项
grep -h "Status**: pending" .learnings/*.md | wc -l

# 列出高优先级待处理项
grep -B5 "Priority**: high" .learnings/*.md | grep "^## \["
```

## 最佳实践

1. **立即记录** - 问题发生时上下文最清晰
2. **具体明确** - 未来代理需要快速理解
3. **包含复现步骤** - 特别是错误
4. **链接相关文件** - 使修复更容易
5. **建议具体修复** - 而非仅"调查"
6. **使用一致类别** - 便于过滤
7. **积极提升** - 如有疑问，添加到CLAUDE.md
8. **定期审查** - 过时学习失去价值

## 技能提取

当学习有价值成为可复用技能时：

### 提取标准

- **重复出现**：有2+个类似问题的`See Also`链接
- **已验证**：状态为`resolved`且有工作修复
- **非显而易见**：需要实际调试才能发现
- **广泛适用**：非项目特定；跨代码库有用
- **用户标记**：用户说"保存为技能"

### 提取流程

1. 识别候选学习
2. 使用辅助脚本或手动创建
3. 自定义SKILL.md
4. 更新学习状态为`promoted_to_skill`
5. 验证技能自包含

## 与OpenClaw集成

### 工作区结构

```
~/.openclaw/
├── workspace/
│   ├── AGENTS.md      # 多代理协调模式
│   ├── SOUL.md        # 行为准则和个性
│   ├── TOOLS.md       # 工具能力和问题
│   ├── MEMORY.md      # 长期记忆
│   └── memory/        # 每日记忆
│       └── YYYY-MM-DD.md
└── skills/
    └── self-improving-agent/
        └── SKILL.md
```

### Hook集成（可选）

自动提醒机制：

```bash
# 复制hook
cp -r hooks/openclaw ~/.openclaw/hooks/self-improvement

# 启用
openclaw hooks enable self-improvement
```

## Gitignore选项

**保持本地**（每开发者）：
```gitignore
.learnings/
```

**跟踪到仓库**（团队共享）：
不添加到.gitignore - 学习成为共享知识

**混合模式**（跟踪模板，忽略条目）：
```gitignore
.learnings/*.md
!.learnings/.gitkeep
```

## 总结

Self-Improving-Agent 技能通过系统化的日志记录和提升机制，使AI代理能够：

1. **从错误中学习** - 避免重复相同错误
2. **积累知识** - 构建项目特定知识库
3. **持续改进** - 跨会话传递学习
4. **团队协作** - 共享最佳实践

这是一个强大的元认知工具，使AI代理具备自我改进能力。
