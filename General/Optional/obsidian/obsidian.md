# 目录 <!-- omit in toc -->
- [ Obsidian](#-obsidian)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [快速入门](#快速入门)
  - [核心特性](#核心特性)
  - [推荐插件](#推荐插件)
  - [使用提示](#使用提示)
  - [相关链接](#相关链接)
    - [回到 General/Optional](#回到-generaloptional)

# <img src="../../.media/png/Obsidian.png" width="60" height="60" alt="obsidian logo"/> Obsidian

Obsidian 是一款基于本地 Markdown 文件的知识管理工具，以"笔记库"（Vault）为核心概念——只需选择一个本地文件夹，即可将其中的所有 Markdown 文件作为笔记进行浏览、搜索和关联。支持双向链接、关系图谱、反向链接面板、Canvas 画布以及丰富的第三方插件生态，适合个人知识管理、项目文档整理、笔记写作等多种场景。

> 个人用户免费使用，数据完全存储在本地，无需注册账号即可使用全部核心功能。官方提供付费的 Obsidian Sync 和 Obsidian Publish 作为可选的云同步与发布服务。

## 安装

### Windows

```bash
# winget
winget install Obsidian.Obsidian

# Scoop
scoop install obsidian

# Chocolatey
choco install obsidian
```

也可从[官网](https://obsidian.md/download)下载 `.exe` 安装包。

### macOS

```bash
# Homebrew
brew install --cask obsidian
```

也可从[官网](https://obsidian.md/download)下载 `.dmg` 文件。

### Linux

```bash
# Snap
sudo snap install obsidian

# AppImage
# 从 GitHub Releases 下载 AppImage，给予执行权限后直接运行
```

也可通过 Flatpak 安装：

```bash
flatpak install flathub md.obsidian.Obsidian
```

## 快速入门

1. **创建 Vault**：首次启动时点击"创建新库"，选择一个文件夹作为 Vault 的根目录（例如指向本仓库路径）。
2. **浏览文件**：左侧文件列表显示文件夹中的所有 Markdown 文件，点击即可编辑或阅读。
3. **链接笔记**：输入 `[[文件名]]` 即可创建指向其他笔记的链接，点击链接可直接跳转。
4. **查看图谱**：点击左侧"关系图谱"图标，可全局查看所有笔记之间的引用关系。

## 核心特性

| 特性 | 说明 |
|------|------|
| 本地优先 | 所有笔记以纯 Markdown 文件存储在本地，无格式锁定 |
| 双向链接 | `[[wikilink]]` 语法链接笔记，自动追踪引用与提及 |
| 反向链接 | 每篇笔记底部显示"哪些笔记链接了本文" |
| 关系图谱 | 可视化展示 Vault 中所有笔记的引用网络 |
| Canvas | 无限画布，可拖入笔记、图片、卡片进行可视化整理 |
| 全文搜索 | 支持正则表达式、模糊匹配、路径过滤等高级搜索 |
| 标签系统 | `#tag` 和嵌套标签 `#parent/child` 用于分类 |
| 插件生态 | 2000+ 第三方插件，覆盖主题、工作流、格式扩展等 |

## 推荐插件

| 插件 | 用途 |
|------|------|
| Obsidian Git | 自动定时提交 Vault 到 Git，适合配合本仓库使用 |
| Dataview | 将 Vault 视为数据库进行查询，生成动态列表与统计 |
| Calendar | 按日期组织日记笔记，提供日历视图 |
| Excalidraw | 内置手绘风格的绘图工具 |
| Templater | 高级模板引擎，支持动态脚本模板 |
| Kanban | 看板视图，适合任务管理与项目追踪 |

## 使用提示

- **用于浏览本仓库**：直接用 Obsidian 打开项目根目录，文件树结构与目录一致，`[[ ]]]` 和 Markdown 链接均支持跳转。
- **同步方案**：可搭配 Obsidian Sync（官方）、Syncthing、OneDrive 或 [[../Essential/Git/git|Git]] 实现跨设备同步。
- **忽略文件**：在设置 → 文件和链接中配置排除规则，可隐藏 `.git/`、`.media/` 等非笔记文件夹。
- **中文搜索**：Obsidian 内置搜索已支持中文分词，无需额外配置。
- **移动端**：Obsidian 提供 iOS 和 Android 客户端，可免费使用。

## 相关链接

- [Obsidian 官网](https://obsidian.md/)
- [Obsidian 下载页](https://obsidian.md/download)
- [Obsidian 帮助文档](https://help.obsidian.md/)
- [Obsidian 中文论坛](https://forum-zh.obsidian.md/)
- [社区插件市场](https://obsidian.md/plugins)
- [GitHub](https://github.com/obsidianmd/obsidian-releases) 非开源


---

### [回到 General/Optional](README.md)
