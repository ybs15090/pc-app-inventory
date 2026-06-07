# 目录 <!-- omit in toc -->
- [QtScrcpy](#qtscrcpy)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [连接设备](#连接设备)
    - [USB 连接](#usb-连接)
    - [WiFi 连接](#wifi-连接)
  - [功能速览](#功能速览)
  - [使用提示](#使用提示)
  - [相关链接](#相关链接)

# QtScrcpy

QtScrcpy 是一款开源的 Android 屏幕投屏与控制工具，通过 USB 或 WiFi 连接 Android 设备，支持在桌面端实时显示并操控设备屏幕。基于 scrcpy 协议，提供图形化界面和额外功能，无需在手机上安装任何软件，无需 root 权限。

| 指标 | 表现 |
|------|------|
| 帧率 | 30~60 fps |
| 分辨率 | 最高 1920×1080+ |
| 延迟 | 35~70 ms |
| 启动速度 | 约 1 秒出首帧 |

## 安装

所有平台均可从 [GitHub Releases](https://github.com/barry-ran/QtScrcpy/releases) 下载对应安装包或便携版。

### Windows

下载 `.exe` 安装包或 `.zip` 便携版，解压后运行 `QtScrcpy.exe`。

```bash
# Scoop
scoop install qtscrcpy
```

### macOS

```bash
# Homebrew
brew install --cask qtscrcpy
```

也可下载 `.dmg` 文件手动安装。

### Linux

从 GitHub Releases 下载 AppImage，给予执行权限后运行：

```bash
chmod +x QtScrcpy-*.AppImage
./QtScrcpy-*.AppImage
```

## 连接设备

### USB 连接

1. 在 Android 设备上开启**开发者选项** → **USB 调试**。
2. 用 USB 数据线连接手机与电脑。
3. 手机上弹出的"允许 USB 调试"对话框中点击"允许"。
4. 在 QtScrcpy 中点击"USB 连接"，选择设备即可。

### WiFi 连接

1. 先用 USB 连接设备，在 QtScrcpy 中记录设备 IP。
2. 点击"无线连接" → 输入设备 IP，或直接使用"一键 WiFi"功能。
3. 连接成功后即可拔掉 USB 线，后续可纯无线使用。

> WiFi 模式下延迟和画质受路由器性能影响，建议使用 5GHz 频段。

## 功能速览

| 功能 | 说明 |
|------|------|
| 屏幕镜像 | 实时投屏 Android 设备画面到桌面 |
| 键鼠控制 | 用电脑键盘和鼠标操作手机 |
| 多设备连接 | 同时连接并投屏多台 Android 设备 |
| 录屏 | 录制设备屏幕操作，保存为视频文件 |
| 截图 | 一键截取设备当前画面 |
| 全屏模式 | 投屏窗口全屏显示，适合演示 |
| 剪贴板同步 | 电脑与手机剪贴板双向同步 |
| 拖拽安装 APK | 直接将 APK 文件拖入窗口即可安装 |
| 文件传输 | 支持从电脑向手机传输文件 |
| 按键映射 | 自定义键盘按键映射到屏幕触控位置（适合游戏） |

## 使用提示

- **开发者选项**：部分手机（如小米、vivo）的开发者选项默认隐藏，需在"设置 → 关于手机"中连续点击"版本号" 7 次才能解锁。
- **分辨率调整**：在设置中降低投屏分辨率可减少延迟和 CPU 占用。
- **游戏场景**：使用按键映射功能，可将 WASD 等键位映射到屏幕虚拟摇杆区域，实现 PC 操控手游。
- **多设备管理**：适合需要同时操作多台手机的测试场景，所有设备在同一窗口分屏显示。

## 相关链接

- [QtScrcpy — GitHub](https://github.com/barry-ran/QtScrcpy)
- [QtScrcpy — 下载页](https://github.com/barry-ran/QtScrcpy/releases)
- [第三方文档站](https://qtscrcpy.org/)（独立网站，非官方，仅供参考）

---

### [回到 remote-desktop](README.md)
