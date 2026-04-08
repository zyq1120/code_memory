#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const TEMPLATES = {
  'session-state': `# SESSION-STATE.md — 活动工作内存

这个文件是助手的"RAM" — 在压缩、重启、分心后仍保留。

## 当前任务
[无]

## 关键上下文
[暂无]

## 待办操作
- [ ] 无

## 最近决策
[暂无]

---
*最后更新：${new Date().toISOString()}*
`,
  'memory-md': `# MEMORY.md — 长期记忆

## 关于用户
[添加用户偏好、沟通风格等]

## 项目
[活跃项目及其状态]

## 决策日志
[重要决策及其做出的原因]

## 经验教训
[要避免的错误、有效的模式]

## 偏好
[用户偏好的工具、框架、工作流]

---
*人工整理的记忆 — 从每日日志中提炼洞察到这里*
`,
  'daily-template': `# {{DATE}} — 每日日志

## 已完成任务
- 

## 做出的决策
- 

## 经验教训
- 

## 明天计划
- 

---
*创建时间：{{DATE}}*
`
};

const commands = {
  init: () => {
    console.log('🧠 正在初始化Elite Longterm Memory...\n');
    
    if (!fs.existsSync('SESSION-STATE.md')) {
      fs.writeFileSync('SESSION-STATE.md', TEMPLATES['session-state']);
      console.log('✓ 创建了SESSION-STATE.md（热内存）');
    } else {
      console.log('• SESSION-STATE.md已存在');
    }
    
    if (!fs.existsSync('MEMORY.md')) {
      fs.writeFileSync('MEMORY.md', TEMPLATES['memory-md']);
      console.log('✓ 创建了MEMORY.md（人工整理归档）');
    } else {
      console.log('• MEMORY.md已存在');
    }
    
    if (!fs.existsSync('memory')) {
      fs.mkdirSync('memory', { recursive: true });
      console.log('✓ 创建了memory/目录');
    } else {
      console.log('• memory/目录已存在');
    }
    
    const today = new Date().toISOString().split('T')[0];
    const todayFile = `memory/${today}.md`;
    if (!fs.existsSync(todayFile)) {
      const content = TEMPLATES['daily-template'].replace(/\{\{DATE\}\}/g, today);
      fs.writeFileSync(todayFile, content);
      console.log(`✓ 创建了${todayFile}`);
    }
    
    console.log('\n🎉 Elite Longterm Memory初始化完成！');
    console.log('\n下一步：');
    console.log('1. 将SESSION-STATE.md添加到你的代理上下文');
    console.log('2. 查看MEMORY.md获取完整设置指南');
  },
  
  today: () => {
    const today = new Date().toISOString().split('T')[0];
    const todayFile = `memory/${today}.md`;
    
    if (!fs.existsSync('memory')) {
      fs.mkdirSync('memory', { recursive: true });
    }
    
    if (!fs.existsSync(todayFile)) {
      const content = TEMPLATES['daily-template'].replace(/\{\{DATE\}\}/g, today);
      fs.writeFileSync(todayFile, content);
      console.log(`✓ 创建了${todayFile}`);
    } else {
      console.log(`• ${todayFile}已存在`);
    }
  },
  
  status: () => {
    console.log('🧠 Elite Longterm Memory状态\n');
    
    if (fs.existsSync('SESSION-STATE.md')) {
      const stat = fs.statSync('SESSION-STATE.md');
      console.log(`✓ SESSION-STATE.md（${(stat.size / 1024).toFixed(1)}KB，最后修改时间 ${stat.mtime.toLocaleString()}）`);
    } else {
      console.log('✗ SESSION-STATE.md缺失');
    }
    
    if (fs.existsSync('MEMORY.md')) {
      const stat = fs.statSync('MEMORY.md');
      const lines = fs.readFileSync('MEMORY.md', 'utf8').split('\n').length;
      console.log(`✓ MEMORY.md（${lines}行，${(stat.size / 1024).toFixed(1)}KB）`);
    } else {
      console.log('✗ MEMORY.md缺失');
    }
    
    if (fs.existsSync('memory')) {
      const files = fs.readdirSync('memory').filter(f => f.endsWith('.md'));
      console.log(`✓ memory/（${files.length}个每日日志）`);
    } else {
      console.log('✗ memory/目录缺失');
    }
  },
  
  help: () => {
    console.log(`
🧠 Elite Longterm Memory CLI

命令：
  init    在当前目录初始化记忆系统
  today   创建当天的每日日志文件
  status  检查记忆系统健康状态
  help    显示此帮助信息

使用方法：
  node elite-memory.js init
  node elite-memory.js status
`);
  }
};

const command = process.argv[2] || 'help';
if (commands[command]) {
  commands[command]();
} else {
  console.log(`未知命令：${command}`);
  commands.help();
}
