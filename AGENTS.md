# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 仓库概述

这是一个 PC 软件清单文档仓库，按平台分类收录推荐软件与配置。目前主要聚焦 Ubuntu 20.04。所有内容均为 Markdown 格式。

## 目录结构

```
{Platform}/{Category}/{SoftwareName}.md
```

- **Platform**: `Linux/`, `Windows/`, `MacOS/`, `General/`（跨平台）
- **Category**: `Essential/`（必装）或 `Optional/`（扩展/选装）
- 软件配置文件（如 VS Code 的 settings.json）作为附属资源放在软件同名目录下

`General/` 中的内容适用于所有平台；非通用的内容应放入对应平台目录。

## 媒体资源

- `.media/svg/` — 软件图标（SVG 格式），用于 `README.md` 等页面
- `.media/png/` — 截图和演示图片
- `.media/svg_black/` — VS Code 专用图标（深色主题适配）

引用图片时使用相对路径，如 `../../../.media/svg/example.svg`（从目标 .md 文件的相对层级计算）。

## 文档规范

新软件文档遵循以下结构（参考 `Linux/Essential/效率软件.md` 或 `General/Essential/vs-code/vs-code.md`）：

1. **目录**（可选，带 `<!-- omit in toc -->` 注释）
2. **软件简介** — 用一句话说明软件用途
3. **安装方法** — 使用 bash 代码块等格式提供安装命令
4. **使用方法** — 简要说明即可
5. **官方文档/相关链接** — 官网、GitHub、教程链接

### 命名规范

- 单软件：`软件名称.md` 或 `软件用途.md`
- 功能相关的多个软件可在同一个 `.md` 中对比介绍，此时按功能/用途命名（如 `文件编辑.md`、`远程连接.md`）
- 文件名使用中文描述（当前惯例）

### 图标用法

在标题中使用 HTML `<img>` 标签嵌入图标：

```markdown
## <img src="../../.media/svg/example.svg" width="60" height="60" alt="logo"> 软件名
```

## 编辑注意事项

- 使用中文撰写内容（README_en.md 除外）
- 移动或重命名文件时，同步更新所有引用该文件的相对路径链接
- `.gitignore` 忽略了 `*.zip`、`*.rar`、`*.log`
