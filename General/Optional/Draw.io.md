<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->
- [Draw.io](#-drawio)
  - [安装](#安装)
  - [功能特点](#功能特点)
  - [使用方法](#使用方法)
  - [相关链接](#相关链接)

# <img src="../../.media/svg/Draw-io.svg" width="60" height="60" alt="Draw.io logo"> Draw.io

免费开源的跨平台图表绘制工具（又名 diagrams.net），支持流程图、UML、ER 图、网络拓扑图等多种图表类型，提供网页版与桌面版。

## 安装

### Windows

```powershell
# winget
winget install JGraph.Draw
```

也可从 [GitHub Releases](https://github.com/jgraph/drawio-desktop/releases) 下载 `.exe` 安装包。

### macOS

```bash
# Homebrew
brew install --cask drawio
```

或从 [GitHub Releases](https://github.com/jgraph/drawio-desktop/releases) 下载 `.dmg`。

### Linux

从 [GitHub Releases](https://github.com/jgraph/drawio-desktop/releases) 下载对应包：
- Debian / Ubuntu：`.deb`
- Fedora / RHEL：`.rpm`
- 通用：`.AppImage`

### 网页版（免安装）

直接访问 [app.diagrams.net](https://app.diagrams.net/) 即可使用，无需注册账号。

### VS Code 扩展

在扩展市场搜索 **Draw.io Integration**（`hediet.vscode-drawio`），可在 VS Code 内直接编辑 `.drawio` 文件。

## 功能特点

- **多种图表类型**：流程图、UML 类图 / 时序图、ER 图、网络拓扑、思维导图、看板等
- **丰富图形库**：内置大量通用与专业图形（AWS、Azure、GCP、网络设备等）
- **多格式导出**：PNG、SVG、PDF、HTML、XML（`.drawio`）
- **多存储后端**：本地文件、Google Drive、OneDrive、Confluence、GitHub
- **实时协作**：网页版支持多人同时编辑
- **模板库**：提供丰富的图表模板，开箱即用
- **离线可用**：桌面版完全离线运行
- **跨平台**：Windows / macOS / Linux 桌面端 + 浏览器端

## 使用方法

| 操作 | 说明 |
|------|------|
| 新建图表 | 启动后选择模板或空白画布 |
| 插入图形 | 从左侧图形库拖入，或双击画布空白处搜索图形 |
| 连接图形 | 悬停图形边缘出现连接点，拖拽到目标图形 |
| 导出 | `文件 → 导出为` 选择 PNG / SVG / PDF 等格式 |
| 保存格式 | 默认 `.drawio`（XML），可直接提交至 Git 仓库做版本管理 |

> **技巧**：`.drawio` 文件本质是 XML，对图表内容进行版本控制时可直接 diff。

## 相关链接

- [Draw.io 官网（diagrams.net）](https://www.diagrams.net/)
- [GitHub — drawio-desktop](https://github.com/jgraph/drawio-desktop)
- [网页版入口](https://app.diagrams.net/)
- [VS Code 扩展](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)

---

### [回到 General/Optional](README.md)
