# 目录 <!-- omit in toc -->
- [OpenAI Codex CLI](#openai-codex-cli)
  - [安装](#安装)
    - [Linux / macOS](#linux--macos)
    - [Windows](#windows)
  - [快速入门](#快速入门)
  - [核心特性](#核心特性)
  - [常用命令](#常用命令)
  - [配置](#配置)
  - [与 Claude Code 的对比](#与-claude-code-的对比)
  - [相关链接](#相关链接)
    - [回到 AI-agent](#回到-ai-agent)

# OpenAI Codex CLI

Codex CLI 是 OpenAI 推出的终端 AI 编程助手。它运行在本地终端中，可调用 OpenAI 模型完成代码生成、文件编辑、命令执行等任务，并将每次操作的结果作为下一步推理的上下文。

> 需要 OpenAI API Key。
## 安装

### Linux / macOS

```bash
npm install -g @openai/codex
```

安装后执行 `codex` 即可进入会话。首次运行会提示输入 API Key，也可提前设置环境变量。

### Windows

```bash
npm install -g @openai/codex
```

> 要求 Node.js ≥ 18。

## 快速入门

1. 在终端中进入项目目录。
2. 输入 `codex` 启动交互式会话。
3. 用自然语言描述任务。
4. Codex 会读取文件、分析代码、执行操作，并在每个步骤后等待你的确认。

非交互模式（一次性任务）：

```bash
codex exec "解释这个函数的作用"
```

## 核心特性

| 特性 | 说明 |
|------|------|
| 多模型支持 | 可切换 GPT-4o、o4-mini、o3 等 OpenAI 模型 |
| 文件操作 | 读取、写入、编辑项目文件 |
| Shell 执行 | 运行命令、执行脚本 |
| 会话记忆 | 在同一会话中保持上下文，逐步完成复杂任务 |
| 沙箱模式 | 可在受限环境中运行，限制文件系统和网络访问 |
| 多会话 | 同时开启多个独立会话处理不同任务 |
| 自定义规则 | 通过 `AGENTS.md` 或 `CODEAX.md` 配置文件定义项目级行为 |
| MCP 支持 | 可连接 MCP 服务器扩展工具能力 |

## 常用命令

```bash
# 进入交互式会话
codex

# 执行一次性任务
codex exec "用 Python 写一个 HTTP 服务器"

# 指定模型
codex --model o4-mini

# 以受限沙箱模式运行（不修改文件）
codex --sandbox

# 查看帮助
codex --help
```

## 配置

配置文件位于 `~/.codex/` 或项目下的 `.codex/` 目录。

```bash
# 设置 API Key（推荐在 ~/.bashrc 或 ~/.zshrc 中设置）
export OPENAI_API_KEY="sk-..."

# 指定默认模型
export OPENAI_MODEL="gpt-4o"
```

也可通过 `codex config` 命令交互式配置。

## 与 Claude Code 的对比

| 维度 | Claude Code | Codex CLI |
|------|-------------|-----------|
| 开发方 | Anthropic | OpenAI |
| 底层模型 | Claude 系列 | GPT / o 系列 |
| 安装方式 | npm | npm |
| MCP 支持 | ✅ | ✅ |
| 安全确认 | 默认确认 | 默认确认 |
| 多会话 | ✅ | ✅ |
| 项目规则文件 | `CLAUDE.md` | `AGENTS.md` / `CODEAX.md` |
| 沙箱模式 | — | ✅ 内置沙箱 |

两者在功能上高度重叠，选择主要取决于：
- 你偏好哪个模型生态（Claude vs GPT）
- 已有的 API 订阅情况
- 特定场景下的模型能力差异（如长上下文、代码生成精确度等）

## 相关链接

- [Codex CLI GitHub](https://github.com/openai/codex)
- [OpenAI API 文档](https://platform.openai.com/docs)
- [OpenAI 官网](https://openai.com/)

---

### [回到 AI-agent](README.md)
