# 目录 <!-- omit in toc -->
- [MacType](#mactype)
  - [简介](#简介)
  - [安装](#安装)
  - [配置与使用](#配置与使用)


# MacType

## 简介

MacType 是一款 Windows 平台上的字体渲染优化工具，通过接管 Windows 的 GDI/DirectWrite 字体渲染，模拟 macOS 的字体平滑效果。特别适合低分屏（1080P 及以下）用户改善字体显示效果。

- [官方网站](https://www.mactype.net/)

**核心功能：**
- 替换 Windows 默认字体渲染引擎，消除锯齿并加粗字形
- 支持 GDI 和 DirectWrite 两种渲染模式
- 内置多种渲染配置（如 iOS、macOS、Linux 风格），支持自定义
- 可针对特定进程排除，兼容游戏和部分应用

## 安装

1. 从[官网](https://www.mactype.net/)下载最新版安装包
2. 解压后运行 `MacTypeInstaller.exe` 或直接使用 `MacTypeTray.exe`（绿色便携版）
3. 安装时推荐选择 **MacTray** 模式（系统托盘驻留，方便随时调整）

> **注意：** 安装过程中 Windows Defender 可能弹出 SmartScreen 警告，点击"更多信息" → "仍要运行"即可。

## 配置与使用

### 基本使用

1. 启动 MacType 托盘程序
2. 右键托盘图标 → 选择渲染模式：
   - **注册表加载** — 全局生效，最稳定
   - **服务加载** — 全局生效，开机自启
   - **独立加载** — 仅对指定进程生效
3. 选择配置文件后即可看到效果

### 推荐配置

针对 1080P 屏幕，推荐以下配置组合：
- **渲染配置文件：** `XMac` 或 `Default`（中文显示更均衡）
- **加载方式：** 注册表加载（全局）+ 排除游戏进程

### 进程排除

部分应用（如杀毒软件、部分游戏）可能与 MacType 冲突，可在 `MacType.ini` 中添加排除：

```ini
[UnloadDll]
ProcessName.exe
```

常见需排除的进程：`chrome.exe`（当使用 DirectWrite 模式时）、部分反作弊游戏。

### 相关资源

- [MacType 用户手册](https://github.com/snowie2000/mactype/wiki)
- [GitHub 社区版](https://github.com/snowie2000/mactype)


---

### [回到 Windows/Optional](README.md)
