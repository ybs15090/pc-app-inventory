# 目录 <!-- omit in toc -->
- [Clash Verge Rev](#clash-verge-rev)
  - [简介](#简介)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [使用](#使用)


# Clash Verge Rev

## 简介

Clash Verge Rev 是基于 Tauri 构建的跨平台 Clash Meta（Mihomo）图形客户端，原项目 [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) 已归档，现由社区维护。支持 Windows、macOS 和 Linux。

**核心特性：**

- 内置 Clash Meta（Mihomo）内核，支持切换 Alpha 版本
- 可视化节点与规则编辑，语法提示
- 系统代理 / TUN 虚拟网卡两种模式
- WebDAV 配置备份与同步
- 自定义主题、图标与 CSS

- [GitHub](https://github.com/clash-verge-rev/clash-verge-rev)

## 安装

### Windows

从 [GitHub Releases](https://github.com/clash-verge-rev/clash-verge-rev/releases) 下载对应版本：

| 版本 | 文件 |
|------|------|
| **64 位 (x64)** | `Clash.Verge.Rev_x.x.x_x64-setup.exe`（推荐） |
| **ARM64** | `arm64-setup.exe`（Surface Pro X 等 ARM 设备） |
| **64 位（自带 WebView2）** | `x64_fixed_webview2-setup.exe`（无 WebView2 环境时使用） |

双击 `.exe` 安装，安装完成后从开始菜单启动。需 Windows 10 及以上，Win7 不再支持。

### macOS

从 [GitHub Releases](https://github.com/clash-verge-rev/clash-verge-rev/releases) 下载对应 `.dmg`：

| 芯片 | 文件 |
|------|------|
| **Intel** | `Clash.Verge.Rev_x.x.x_x64.dmg` |
| **Apple M 系列** | `Clash.Verge.Rev_x.x.x_aarch64.dmg` |

双击 `.dmg` → 拖入 Applications 文件夹。若提示"无法打开未验证的开发者"，前往「系统设置 → 隐私与安全性」→ 点击「仍要打开」；或终端执行：

```bash
sudo xattr -r -d com.apple.quarantine /Applications/Clash\ Verge.app
```

### Linux

**DEB 包安装（推荐）：**

```bash
wget https://github.com/clash-verge-rev/clash-verge-rev/releases/latest/download/Clash.Verge_amd64.deb
sudo apt install -y ./Clash.Verge_*_amd64.deb
sudo apt --fix-broken install -y   # 如有依赖错误
```

> **Ubuntu 20.04 注意：** 如启动失败，需安装额外依赖：
> ```bash
> sudo apt install -y libwebkit2gtk-4.1-dev libgtk-3-dev libayatana-appindicator3-dev
> ```

**AppImage 便携版：**

```bash
sudo apt install -y fuse libfuse2
wget https://github.com/clash-verge-rev/clash-verge-rev/releases/latest/download/Clash.Verge-x86_64.AppImage
chmod +x Clash.Verge-x86_64.AppImage
./Clash.Verge-x86_64.AppImage
```

**其它发行版：**

| 发行版 | 安装方式 |
|--------|----------|
| **Fedora** | 使用 AppImage |
| **Arch** | AUR: `paru -S clash-verge-rev-bin` |

## 使用

1. 启动 Clash Verge Rev
2. 进入 **订阅** 页面 → 粘贴订阅链接 → 导入
3. 进入 **代理** 页面 → 选择节点
4. 点击 **系统代理** 或 **TUN 模式** 开启代理

> TUN 模式（虚拟网卡）可实现全局代理，包括终端流量。Linux 下 TUN 模式可能需要管理员权限。


---

### [回到 network-proxy](README.md)
