# LocalSend

## 软件简介

LocalSend 是免费开源的跨平台局域网传输工具，可在电脑与手机之间直接发送文件、照片、视频和文本。

支持 Windows、macOS、Linux、Android 和 iOS。设备接入同一局域网后即可传输，无需注册账号，传输过程无需互联网连接或第三方服务器；默认通过 HTTPS 加密通信。适合手机照片导出、电脑之间交换文件，以及临时分享文档和链接。

本文根据 [LocalSend 官网](https://localsend.org/) 和 [官方 README](https://github.com/localsend/localsend#readme) 整理，核对日期：2026-10-13。

## 安装方法

统一入口：[官网下载页](https://localsend.org/download) / [GitHub 正式发行版](https://github.com/localsend/localsend/releases/latest)。下载时选择对应系统和处理器架构的安装包。

### Windows

已安装 WinGet 时，可在 PowerShell 或终端执行：

```powershell
winget install --exact --id LocalSend.LocalSend
```

包标识见 [WinGet 软件清单](https://github.com/microsoft/winget-pkgs/tree/master/manifests/l/LocalSend/LocalSend)。

也可下载 `.exe` 安装包，按向导安装；需要便携使用时，下载 `.zip` 并完整解压后启动 `localsend_app.exe`。当前官方要求 Windows 10 或更新版本。

### macOS

已安装 Homebrew 时：

```bash
brew install --cask localsend
```

命令来源：[Homebrew LocalSend 页面](https://formulae.brew.sh/cask/localsend)。

也可下载 `.dmg` 文件，打开后将 LocalSend 拖入“应用程序”文件夹，或通过官网下载页进入 App Store 安装。当前官方最低要求 macOS 11 Big Sur。

### Linux

#### Flatpak

已安装 Flatpak 并配置 Flathub 软件源时：

```bash
flatpak install flathub org.localsend.localsend_app
flatpak run org.localsend.localsend_app
```

软件页面见 [Flathub](https://flathub.org/en/apps/org.localsend.localsend_app)，命令用法见 [Flatpak 官方文档](https://docs.flatpak.org/en/latest/using-flatpak.html)。首次使用可先按 [Ubuntu 的 Flathub 设置说明](https://flathub.org/en/setup/Ubuntu) 配置环境。

#### Debian / Ubuntu 本地安装包

从 GitHub Releases 下载与处理器架构对应的 `.deb` 文件，然后在下载目录执行。以下以核对时的 x86-64 发行包为例：

```bash
sudo apt install ./LocalSend-1.18.2-linux-x86-64.deb
```

版本更新后，将命令中的文件名替换为实际下载的文件名。官方也提供 AppImage 和 `.tar.gz`，可按需要选择。

Linux 的桌面文件选择依赖 `xdg-desktop-portal` 及对应桌面后端，例如 GNOME 使用 `xdg-desktop-portal-gtk`，KDE 使用 `xdg-desktop-portal-kde`。具体依赖与系统兼容性以所选发行包为准，本文未实测 Ubuntu 20.04 的安装和运行。

### Android / iOS

- **Android**：通过官网下载页进入 Google Play、F-Droid，或从 GitHub Releases 下载对应架构的 APK。
- **iOS / iPadOS**：通过官网下载页进入 App Store 安装。

接收和发送文件时，按系统提示授予所需的本地网络、照片或文件访问权限。

## 使用方法

### 发送与接收文件

1. 在发送端和接收端安装并打开 LocalSend，将两台设备接入同一局域网。例如手机连接家中 Wi-Fi，电脑通过 Wi-Fi 或网线连接同一路由器。
2. 在接收端查看本机的设备名称；可在设置中修改名称，方便辨认。
3. 在发送端打开“发送”，选择要传输的文件、照片或文本，然后点击附近设备列表中的接收端。
4. 接收端确认发送设备和文件内容，接受传输请求。
5. 传输完成后，按接收界面的提示查看文件；接收目录可在设置中查看或调整。

菜单名称和可选内容随平台与界面语言略有差异。基本流程见 [官网使用说明](https://localsend.org/#how-it-works)。

### 常用设置

| 设置 | 用途 |
|---|---|
| 设备名称 | 为电脑和手机设置容易辨认的名称，减少选错接收端的情况。 |
| 接收目录 | 在电脑端指定接收文件的保存位置，便于整理照片和文档。 |
| 收藏设备 / 手动输入 IP | 自动发现失败时，可尝试直接输入接收端的局域网 IP；常用设备可加入收藏。 |
| Windows 便携配置 | 在 `localsend_app.exe` 同目录创建 `settings.json`，文件可为空；程序会把设置保存到该文件。 |

便携配置见 [官方 README 的 Setup 章节](https://github.com/localsend/localsend#setup)。

## 常见问题

| 现象 | 排查方法 |
|---|---|
| 附近设备列表为空 | 确认两端都已打开 LocalSend、接入同一局域网，并检查路由器是否启用了访客网络隔离或 AP 隔离。 |
| Windows 接收端不可见 | 在可信的家庭或办公网络中检查网络是否设为“专用”，并允许 LocalSend 通过该网络的防火墙。 |
| macOS / iOS 接收端不可见 | 检查系统隐私设置中的“本地网络”权限是否允许 LocalSend 访问。 |
| 使用 VPN 后无法发现设备 | 检查 VPN 是否允许局域网流量；必要时临时断开 VPN，再测试设备发现。 |
| 能访问局域网但自动发现失败 | 使用手动发送功能输入接收端 IP；若可正常传输，将该设备加入收藏。 |
| 传输速度较慢 | 优先使用信号良好的 5 GHz Wi-Fi，检查无线信号、路由器负载和接收设备的存储写入速度。 |

默认监听端口为 **53317**，官方要求允许该端口的 **TCP 和 UDP 入站流量**。如果修改了 LocalSend 的端口设置，防火墙规则也应使用对应端口。网络与防火墙排查见 [官方 Setup](https://github.com/localsend/localsend#setup) 和 [Troubleshooting](https://github.com/localsend/localsend#troubleshooting)。

## 官方文档与相关链接

- [LocalSend 官网](https://localsend.org/)
- [官网下载页](https://localsend.org/download)
- [GitHub 源码仓库与使用说明](https://github.com/localsend/localsend)
- [最新正式发行版](https://github.com/localsend/localsend/releases/latest)
- [通信协议文档](https://github.com/localsend/protocol)
- [问题反馈](https://github.com/localsend/localsend/issues)

---

### [回到文件传输目录](README.md)
