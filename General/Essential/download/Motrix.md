<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [ Motrix](#-motrix)
  - [软件简介](#软件简介)
  - [安装方法](#安装方法)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
    - [无头服务器（Docker）](#无头服务器docker)
  - [功能特点](#功能特点)
  - [使用方法](#使用方法)
  - [常见问题](#常见问题)
  - [官方文档与相关链接](#官方文档与相关链接)
    - [回到下载工具目录](#回到下载工具目录)

# <img src="../../../.media/png/Motrix-logo.png" width="60" height="60" alt="Motrix 占位图标"> Motrix

## 软件简介

Motrix 是一款免费开源的跨平台下载管理器，支持 HTTP、HTTPS、FTP、BitTorrent 和 Magnet 链接，提供图形界面、浏览器扩展和命令行客户端。

支持 Windows 10 及以上、macOS 13 Ventura 及以上，以及 Linux（官方标注已验证 Ubuntu 18.04+、Debian 10+、Fedora 32+，需要 GNOME 或 KDE 桌面）。2.x（Motrix Turbo）基于 Electron、React 和 TypeScript 重写，下载核心为 Motrix 维护的 aria2 分支，界面与下载引擎分离；同一核心也可作为无头服务器运行在 Docker 中，适合 NAS 或家庭服务器。软件以 MIT 协议开源，官方不提供 32 位安装包。

本文依据 [Motrix 官网](https://motrix.app/)、[官方 README](https://github.com/agalwood/Motrix#readme) 和 [v2.1.1 发行说明](https://github.com/agalwood/Motrix/releases/tag/v2.1.1) 整理，核对日期：2026-10-30，当前稳定版为 **2.1.1**（发布于 2026-10-29）。验证范围：官方资料与发行包清单核对，未在本机实际安装运行。

## 安装方法

统一入口：[官网下载页](https://motrix.app/download) / [GitHub Releases](https://github.com/agalwood/Motrix/releases)。下载时选择与系统架构匹配的安装包（x64 或 ARM64）。

### Windows

官方下载页列出 WinGet、Chocolatey 和 Scoop 三种包管理器渠道：

```powershell
# WinGet
winget install --exact --id agalwood.Motrix

# Chocolatey
choco install motrix

# Scoop（需先添加 extras 仓库）
scoop install extras/motrix
```

> 包管理器清单可能滞后于官网。核对时 Scoop Extras 已是 2.1.1，而 WinGet、Chocolatey 的公开清单仍停留在 1.x；需要最新 2.x 时，请从官网或 GitHub Releases 下载安装包。

也可下载 `.exe` 安装向导（NSIS）按提示安装，或下载 `.zip` 解压后直接运行，适合便携使用。Windows 安装包未做代码签名，首次运行可能触发 SmartScreen 提示；请确认文件来自官网或官方 GitHub Release 后再继续。

### macOS

已安装 Homebrew 时：

```bash
brew install --cask motrix
```

也可下载 `.dmg`：Apple Silicon 机型选择 `arm64`，Intel 机型选择 `x64`，打开后把 Motrix 拖入“应用程序”文件夹。官方最低要求 macOS 13 Ventura，`.dmg` 与 `.zip` 包已签名并经过公证。

### Linux

官方提供 `.deb`、`.rpm`、AppImage、Flatpak、Snap 和 Arch 的 `.pacman` 包，按发行版选择一种即可。

Debian / Ubuntu 使用 `.deb`，文件名以实际下载的架构为准：

```bash
sudo apt install ./Motrix_2.1.1_amd64.deb
```

Fedora / openSUSE 使用 `.rpm`：

```bash
sudo dnf install ./Motrix-2.1.1.x86_64.rpm
```

通用发行版可使用 AppImage：

```bash
chmod +x Motrix-2.1.1-x86_64.AppImage
./Motrix-2.1.1-x86_64.AppImage
```

首次启动时，AppImage 会询问是否把桌面入口和 URL 协议处理器注册到用户目录；选择拒绝不会改动系统，之后可在“设置 → 集成”中重新启用或移除。

其他渠道：

```bash
# Snap（官方推荐 Ubuntu 用户使用）
sudo snap install motrix

# Flatpak
flatpak install flathub net.agalwood.Motrix

# Arch Linux（本地 .pacman 包）
sudo pacman -U ./Motrix-2.1.1-x64.pacman

# Arch Linux（AUR）
yay -S motrix
```

Flatpak 和 AUR 的版本可能落后于官方 Release。Flatpak 版如需浏览器接管下载，还要额外安装对应架构的 Flatpak Native Host 附加包，详见[官方 Flatpak 指南](https://github.com/agalwood/Motrix/blob/main/docs/flatpak.md)。AppImage 依赖 FUSE 2；若部分发行版提示缺少 FUSE，可先安装 `libfuse2`。

### 无头服务器（Docker）

同一套下载核心提供无头服务器镜像，可在没有桌面环境的 NAS 或服务器上通过 Web 界面管理任务：

```bash
docker pull docker.io/motrixapp/motrix-server:2.1.1
```

镜像同时发布在 Docker Hub 和 GHCR，部署方式、端口、配对与备份说明见 [官方 Docker Server 指南](https://github.com/agalwood/Motrix/blob/main/docs/docker-server.md)。

## 功能特点

| 功能 | 说明 |
|---|---|
| 多协议下载 | HTTP、HTTPS、FTP、BitTorrent 和 Magnet；可关联 `.torrent` 文件与 `magnet:`、`motrix://` 链接。 |
| 多任务与并发 | 同时下载数量可在 1–200 之间调整，默认 10；支持暂停、继续、重试和优先级调整。 |
| 会话恢复 | 使用 SQLite 保存下载会话，重启应用后恢复任务。 |
| BitTorrent | 支持按文件选择下载、Tracker 列表管理与自动更新、UPnP 和 NAT-PMP 端口映射。 |
| 速度控制 | 分别限制上传和下载速度，可保存多套限速配置。 |
| 浏览器集成 | Motrix Extension 可将 Chrome、Edge、Firefox 的下载交给 Motrix 处理。 |
| 命令行与插件 | 提供 `@motrix/cli`（需 Node.js 22+）；插件运行在 QuickJS 沙箱中，并带应用内插件市场。 |
| 界面与通知 | 深色模式、可自定义的仪表盘、下载完成系统通知、托盘常驻和开机启动。 |

## 使用方法

1. 启动 Motrix，在设置中确认默认下载目录和同时下载数量。
2. 点击界面中的新建任务按钮，粘贴 HTTP/HTTPS、FTP 或 Magnet 链接；也可以直接打开 `.torrent` 文件。确认保存路径后开始下载。
3. 在任务列表中暂停、继续、重试或调整优先级。BitTorrent 任务可在任务详情中只勾选需要的文件。
4. 需要限速时，在设置中添加或切换速度配置，分别填写上传、下载上限。
5. 可选：安装浏览器扩展接管浏览器下载，或安装 `@motrix/cli` 在终端中添加任务：

```bash
npm install -g @motrix/cli

motrix add https://example.com/file.iso --save-dir ~/Downloads
motrix list
```

界面文字和按钮位置可能随版本与语言变化，以实际界面为准。完整操作说明见[官方使用手册](https://motrix.app/manual/)。

## 常见问题

| 现象 | 排查方法 |
|---|---|
| Windows 首次运行出现 SmartScreen 警告 | 官方 Windows 安装包未签名。确认下载来源为官网或官方 GitHub Release，再选择继续运行；不要使用来路不明的安装包。 |
| 包管理器安装后仍是 1.x 版本 | WinGet、Chocolatey 等清单更新滞后。需要 2.x 时改用官网或 GitHub Releases 的安装包；升级前备份原有配置和下载文件。 |
| 从 1.x 升级后看不到旧任务 | 2.x 的迁移助手会把选中的旧任务导入为已暂停记录，不会自动续传。按[迁移指南](https://github.com/agalwood/Motrix/blob/main/docs/legacy-migration.md)操作，并保留旧配置与引擎数据库备份。 |
| 浏览器扩展无法连接 Motrix | 确认已安装并打开桌面版；Flatpak 版还需安装 Native Host 附加包。扩展与桌面端通过安全配对连接，按扩展提示完成授权。 |
| Ubuntu 等系统上 AppImage 无法启动 | 检查是否缺少 FUSE 2，可安装 `libfuse2`；也可改用 `.deb` 或 Snap 包。 |
| 下载速度不理想 | 适当提高同时下载数量，检查 Tracker 与网络状况；BT 任务可确认端口映射是否生效。限速配置或代理设置也可能限制速度。 |

## 官方文档与相关链接

- [Motrix 官网](https://motrix.app/)
- [官方下载页](https://motrix.app/download)
- [官方使用手册](https://motrix.app/manual/)
- [GitHub 源码仓库](https://github.com/agalwood/Motrix)
- [最新发行版](https://github.com/agalwood/Motrix/releases)
- [浏览器扩展](https://github.com/motrixapp/motrix-extension)
- [命令行客户端 @motrix/cli](https://github.com/motrixapp/cli)
- [Docker 无头服务器指南](https://github.com/agalwood/Motrix/blob/main/docs/docker-server.md)
- [问题反馈](https://github.com/agalwood/Motrix/issues)

---

### [回到下载工具目录](README.md)
