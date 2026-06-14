# 目录 <!-- omit in toc -->
- [Claude Code](#claude-code)
  - [安装](#安装)
    - [Linux / macOS](#linux--macos)
    - [Windows](#windows)
  - [快速入门](#快速入门)
  - [核心特性](#核心特性)
  - [常用命令](#常用命令)
  - [配置](#配置)
  - [相关链接](#相关链接)

# Claude Code

Claude Code 是 Anthropic 推出的终端原生 AI 编程助手。与浏览器聊天不同，它直接在终端中运行，能够读取项目文件、编写代码、执行 shell 命令、操作 Git，并与 MCP 工具服务器集成，适合日常开发、代码审查、调试等场景。

> 支持 Claude Pro、Max 订阅或 API Key 付费。可通过 OAuth 登录或设置 API Key 使用。

## 安装

### Linux / macOS

```bash
# npm（全局安装）
npm install -g @anthropic-ai/claude-code
```

安装完成后在终端输入 `claude` 即可启动。

### Windows

```bash
npm install -g @anthropic-ai/claude-code
```

也可通过 Scoop 或直接下载安装包。

> 要求 Node.js ≥ 18。如果系统没有 Node.js，可先通过 [`nvm`](https://github.com/nvm-sh/nvm) 安装。

## 快速入门

1. 在终端中进入你的项目目录。
2. 输入 `claude` 启动交互式会话。
3. 用自然语言描述需求，例如：
   - "帮我找出这个项目中的所有 TODO 注释"
   - "解释 src/utils.js 中的这段代码"
   - "为这个函数写单元测试"
4. Claude Code 会读取文件、分析代码并给出回复，经你许可后可直接修改文件或执行命令。

启动时加上 `-p` 参数可直接用一句话执行（非交互模式）：

```bash
claude -p "总结这个项目的目录结构"
```

## 核心特性

| 特性 | 说明 |
|------|------|
| 文件操作 | 读取、创建、编辑项目文件，支持 apply_patch 精确修改 |
| Shell 执行 | 运行测试、构建、安装依赖等 shell 命令 |
| Git 集成 | 查看 diff、提交代码、切换分支 |
| MCP 工具 | 连接 MCP 服务器扩展能力（如数据库查询、外部 API） |
| 上下文感知 | 自动读取项目结构和关键文件，理解代码库全貌 |
| 权限控制 | 修改文件、执行命令前需确认，可配置信任级别 |
| 会话管理 | 支持恢复历史会话、多项目同时工作 |
| IDE 集成 | 可通过 VS Code / JetBrains 扩展配合使用 |

## 常用命令

```bash
# 启动交互式会话
claude

# 非交互模式，直接提问
claude -p "你的问题"

# 指定模型
claude --model claude-sonnet-4-20250514

# 从文件读取输入
claude -p < prompt.md

# 恢复上次会话
claude --resume

# 查看帮助
claude --help
```

## 配置

首次运行 `claude` 时会引导登录。配置信息存储在 `~/.claude/` 下：

- `settings.json` — 全局设置（模型、权限级别等）
- 项目级配置文件（`.claude/settings.json`）可覆盖全局设置

也可通过环境变量配置：

```bash
# 使用 API Key（可选，OAuth 登录无需设置）
export ANTHROPIC_API_KEY="sk-ant-..."

# 指定模型
export ANTHROPIC_MODEL="claude-sonnet-4-20250514"
```

## 相关链接

- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Anthropic 官网](https://www.anthropic.com/)

---

### [回到 AI-agent](README.md)
