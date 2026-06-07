# 目录 <!-- omit in toc -->
- [AnyDesk](#anydesk)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [快速入门](#快速入门)
  - [核心功能](#核心功能)
  - [使用提示](#使用提示)
  - [相关链接](#相关链接)

# <img src="../../../.media/png/anydesk.png" width="60" height="60" alt="anydesk logo"> AnyDesk

AnyDesk 是一款跨平台的远程桌面软件，支持 Windows、macOS、Linux、Android 和 iOS。通过自研的 DeskRT 视频编解码器，AnyDesk 在低带宽环境下也能保持流畅的画面传输和低延迟操作体验，适用于远程办公、IT 支持和无人值守访问等场景。

> 个人用户可免费使用 AnyDesk 的大部分核心功能；商业用途需要购买许可证。

## 安装

### Windows

```bash
# winget
winget install AnyDeskSoftwareGmbH.AnyDesk

# Scoop
scoop install anydesk

# Chocolatey
choco install anydesk
```

也可从[官网下载页](https://anydesk.com/download)获取 `.exe` 安装程序。

### macOS

从[官网下载页](https://anydesk.com/download)获取 `.dmg` 文件，双击挂载后将 AnyDesk 拖入"应用程序"文件夹即可。

```bash
# Homebrew
brew install --cask anydesk
```

### Linux

```bash
# Debian / Ubuntu (.deb)
wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -
echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list
sudo apt update
sudo apt install anydesk

# Fedora / RHEL (.rpm)
sudo tee /etc/yum.repos.d/anydesk.repo <<EOF
[anydesk]
name=AnyDesk
baseurl=http://rpm.anydesk.com/centos/x86_64/
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://keys.anydesk.com/repos/RPM-GPG-KEY
EOF
sudo dnf install anydesk
```

## 快速入门

1. **获取地址**：启动 AnyDesk 后，主界面会显示本机的 9 位数地址（如 `123 456 789`）。
2. **连接远程设备**：在"远程地址"输入框中输入对方的 AnyDesk 地址，点击"连接"，等对方接受请求后即可开始远程操作。
3. **设置无人值守访问**：设置 → 安全 → 勾选"允许无人值守访问"并设置密码。此后无需对方确认即可直接连接（需输入密码）。

## 核心功能

| 功能 | 说明 |
|------|------|
| 远程控制 | 实时操作远程桌面，支持剪贴板同步 |
| 文件传输 | 连接期间可双向传输文件（或通过文件管理器直接拖拽） |
| 会话录制 | 录制远程操作过程，用于培训或审计 |
| 地址簿 | 保存常用联系人，一键发起连接 |
| 白板 | 在远程屏幕上进行标注，适用于演示和协作 |
| VPN | 通过 AnyDesk 建立虚拟专用网络 |
| 隐私模式 | 使远程设备的物理屏幕变黑，保护隐私 |
| 移动端控制 | 支持 Android / iOS 客户端，可用手机远程管理电脑 |

## 使用提示

- **延迟优化**：如果连接感觉卡顿，可在 AnyDesk 设置 → 显示中降低画质或关闭"移除桌面壁纸"以外的特效。
- **安全设置**：在安全性 → 交互访问中，可限制远程端的具体权限（如禁用文件传输、剪贴板同步等）。
- **自定义别名**：为本地或远程设备设置别名（如"办公室台式机"），方便在地址簿中快速识别。
- **多显示器切换**：远程端有多屏时，使用 AnyDesk 工具栏的显示器图标在屏幕间切换。
- **移动端适配**：AnyDesk 的移动客户端提供了触摸模式、缩放和手势控制，专为小屏幕操作优化。

## 相关链接

- [AnyDesk 官网](https://anydesk.com/)
- [AnyDesk 下载页面](https://anydesk.com/download)
- [AnyDesk 帮助中心](https://support.anydesk.com/)


---

### [回到 remote-desktop](README.md)
