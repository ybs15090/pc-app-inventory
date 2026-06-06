# 目录 <!-- omit in toc -->
- [Clash Party](#clash-party)
  - [简介](#简介)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [使用](#使用)


# Clash Party

## 简介

Clash Party（原名 mihomo-party）是基于 Electron 构建的跨平台桌面 GUI 客户端，专为 Mihomo（Clash Meta）代理内核设计，被视为 Clash for Windows 停更后的最佳替代品。支持 Windows、macOS 和 Linux。

**核心特性：**

- 开箱即用 — 内置 Mihomo 稳定版和开发版双内核
- TUN 模式免管理员权限，直接开启虚拟网卡
- Sub-Store 深度集成，轻松管理订阅
- 强大的覆写功能，可任意修订配置文件
- WebDAV 备份恢复，支持 Cron 定时备份
- Smart Core 智能覆写 — AI 模型自动选择最优节点

- [GitHub](https://github.com/mihomo-party-org/clash-party)
- [官网](https://clash-party.net/)

## 安装

### Windows

从 [GitHub Releases](https://github.com/mihomo-party-org/clash-party/releases) 下载对应版本：

| 版本 | 文件 |
|------|------|
| **Windows 10/11 64 位** | `clash-party-windows-x64-setup.exe`（推荐） |
| **Windows 10/11 便携版** | `clash-party-windows-x64-portable.7z` |
| **Windows 7/8 64 位** | `clash-party-win7-x64-setup.exe` |
| **Windows 7/8 32 位** | `clash-party-win7-ia32-setup.exe` |
| **ARM64** | `clash-party-windows-arm64-setup.exe` |

安装版右键选择 **"以管理员身份运行"**，否则 TUN 模式可能报错。便携版解压后直接运行即可。

### macOS

从 [GitHub Releases](https://github.com/mihomo-party-org/clash-party/releases) 下载 `.pkg` 安装包：

| 芯片 | 文件 |
|------|------|
| **Apple M 系列** | `clash-party-macos-arm64.pkg` |
| **Intel** | `clash-party-macos-x64.pkg` |

或通过 Homebrew 安装：

```bash
brew install --cask clash-party
```

> 首次打开若提示"开发者无法验证"，终端执行：
> ```bash
> sudo xattr -r -d com.apple.quarantine /Applications/clash-party.app
> ```

### Linux

**DEB 包安装（推荐）：**

```bash
wget https://github.com/mihomo-party-org/clash-party/releases/latest/download/clash-party_amd64.deb
sudo apt install -y ./clash-party_*_amd64.deb
sudo apt --fix-broken install -y   # 如有依赖错误
```

启动：

```bash
clash-party
```

**AppImage 便携版：**

```bash
sudo apt install -y fuse libfuse2
wget https://github.com/mihomo-party-org/clash-party/releases/latest/download/clash-party-x86_64.AppImage
chmod +x clash-party-x86_64.AppImage
./clash-party-x86_64.AppImage
```

**其它发行版：**

| 发行版 | 安装方式 |
|--------|----------|
| **Fedora** | 下载 `.rpm` 包安装 |
| **Arch** | AUR: `paru -S mihomo-party-bin` |

## 使用

1. 启动 Clash Party
2. 点击 **订阅** → 添加订阅链接 → 导入
3. 点击 **代理** → 选择节点
4. 开启 **系统代理** 或 **TUN 模式**

> **注意：** Clash Party 是 Electron 应用，内存占用约 100MB+。低配设备建议使用 Clash Verge Rev（Tauri 应用，资源占用更低）。
