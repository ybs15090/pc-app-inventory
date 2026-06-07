# PC 软件合集
[English README](README_en.md)
## 概览

本仓库收录了适用于 PC 和移动设备的推荐软件与工具清单。

## [Windows](Windows/README.md)

适用于 Windows 的必装软件和生产力工具。

## [Linux](Linux/README.md)

目前主要是 Ubuntu 相关的软件和实用 Linux 工具。

## [General](General/README.md)

跨平台通用软件与配置。

## [Android](Android/README.md)

Android 系统的工具与应用。

## [iOS](iOS/README.md)

iOS / iPadOS 系统的工具与应用。

##  收录统计 <!-- omit in toc -->
>统计仅供参考！

| 平台 | Essential | Optional | 合计 |
|------|-----------|----------|------|
| Windows | 3 | 7 | **10** |
| Linux | 11 | 5 | **16** |
| MacOS | 0 | 0 | **0** |
| General | 3 | 9 | **12** |
| Android | 0 | 1 | **1** |
| iOS | 0 | 0 | **0** |

> 运行 `bash scripts/count-software.sh` 可刷新统计。

## 使用方法

1. 克隆本仓库到本地（或者在线使用）。
2. 安装所需的软件。
3. 配置好环境。
4. 开始使用。

## 贡献

如果你对这个项目感兴趣，欢迎贡献自己的软件清单、配置建议或文档内容。

>### 仓库文件格式规范

**组织原则：**

- 软件条目应归入对应的平台目录（`Windows/`、`Linux/`、`Mac/` 或 `General/`）之下，并进一步归入 `Essential/`（必装）或 `Optional/`（选装）子目录。如果一款软件虽然支持多个平台，但其核心使用场景集中在某一平台上，也可按其主要使用平台归类。例如，Spacedesk 的主控端仅支持 Windows，因此归入 `Windows/` 目录。

- **单个独立软件**：直接在分类目录下创建 `软件名称.md` 文件，无需为其单独创建文件夹。  
  例如：`Linux/Optional/Distrobox容器软件.md`

- **单个软件，但带有附属资源**（如配置文件、截图等）：以软件名称创建文件夹，将 `.md` 主文档与附属资源文件一并放置其中。  
  例如：`General/Essential/VScode/` 目录内含 `vs-code.md`、`vscode-settings.json` 等。

- **功能相近的多款软件**（各软件篇幅较长）：以功能或用途命名创建文件夹，每款软件各自编写一份独立的 `.md` 文件。此类文件夹必须包含 `README.md`，用于列出该分类下收录的软件清单，并提供指向各软件文档的跳转链接。  
  例如：`General/Optional/network-proxy/` 目录内含 `Clash-Verge.md`、`v2rayA.md` 等，以及作为索引的 `README.md`。

- **功能相近的多款软件**（各软件篇幅较短）：可合并于一个 Markdown 文件中进行对比介绍，此时文件按功能或用途命名（如 `文件编辑.md`、`远程连接.md`），无需创建文件夹。

- 每个 Markdown 文件推荐包含以下内容：
  - 软件简介
  - 官方文档链接（如有）
  - 其他相关资源链接（如教程、社区等）
  - 安装方法
  - 使用方法（简要说明即可）

## 免责声明

本仓库收录的软件并非全部由维护者亲自使用过，部分软件的安装步骤、使用方法和相关信息来源于网络整理，**不保证完全正确或始终为最新**。在使用任何软件前，请：

- 参考官方文档确认安装方法和配置细节
- 自行评估软件的安全性和适用性
- 对重要操作做好备份

如发现错误或过时内容，欢迎通过 Issue、PR 或邮件反馈。

## 联系方式

如果你有任何问题，请通过以下方式联系我：

- Email: 
  - ybs15090@outlook.com
  - ybs15090@gmail.com

### [回到 README](README.md)
