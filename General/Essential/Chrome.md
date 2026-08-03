<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [Google Chrome](#google-chrome)
  - [适用场景](#适用场景)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [初次配置](#初次配置)
  - [核心功能](#核心功能)
  - [使用提示与注意事项](#使用提示与注意事项)
  - [相关链接](#相关链接)

# <img src="../../.media/png/Chrome.png" width="60" height="60" alt="Google Chrome logo"> Google Chrome

Google Chrome 是 Google 推出的跨平台 Chromium 浏览器，桌面版支持 Windows、macOS 和主流 64 位 Linux 发行版。它具有广泛的网站兼容性、成熟的 Chrome Web Store 扩展生态，并与 Google 账户、Google 密码管理工具及其他 Google 服务深度集成。

## 适用场景

- 希望获得广泛的网站兼容性和完整的 Chromium 扩展生态
- 经常使用 Gmail、Google Drive、Google Docs 等 Google 服务
- 需要在多台电脑或移动设备之间同步书签、密码、设置、历史记录和标签页
- 需要使用浏览器开发者工具进行网页调试
- 希望通过多个浏览器个人资料分隔工作、个人或不同账户环境

## 安装

建议从 [Chrome 官方下载页](https://www.google.com/chrome/)获取安装程序。安装前应检查官方页面列出的当前系统要求，避免从第三方下载站获取修改过的安装包。

### Windows

下载并运行官方安装程序，按提示完成安装。需要在无网络的目标电脑上部署时，可在官方下载页的“其他平台”入口获取离线安装程序。

安装后可进入“Windows 设置 → 应用 → 默认应用”，将 Google Chrome 设为默认浏览器。

### macOS

下载并打开 `googlechrome.dmg`，将 Chrome 拖入“应用程序”文件夹，然后从“应用程序”或 Launchpad 启动。

### Linux

官方下载页提供 Debian/Ubuntu 使用的 `.deb` 包，以及 Fedora/openSUSE 使用的 `.rpm` 包。例如：

```bash
# Debian / Ubuntu：下载 DEB 后在文件所在目录执行
sudo apt install ./google-chrome-stable_current_amd64.deb

# Fedora / openSUSE：下载 RPM 后在文件所在目录执行
sudo dnf install ./google-chrome-stable_current_x86_64.rpm
```

安装官方软件包后，Chrome 通常会将更新源接入系统的软件包管理器。实际文件名和支持的系统版本应以官方下载页为准。

## 初次配置

1. 从原浏览器导入书签、历史记录、保存的密码和其他支持的数据。
2. 根据需要登录 Google 账户；不需要跨设备同步时可以跳过登录。
3. 登录后进入“设置 → 您与 Google → 同步和 Google 服务”，只启用需要同步的数据类型。
4. 在“设置 → 隐私和安全”中运行安全检查，并检查安全浏览、Cookie、网站权限和清除浏览数据等选项。
5. 创建独立的工作与个人资料，避免书签、Cookie、扩展和登录状态混在一起。
6. 仅从可信来源安装必要的扩展，并定期检查扩展权限。

## 核心功能

| 功能 | 说明 |
|------|------|
| Chrome Web Store | 提供大量生产力、开发、内容处理和隐私类扩展 |
| Google 同步 | 通过 Google 账户在不同设备间同步所选浏览器数据 |
| 多个人资料 | 每个资料分别保存书签、扩展、Cookie、历史记录和登录状态 |
| Google 密码管理工具 | 保存、生成和检查密码，并可随账户在设备间同步 |
| 安全浏览与安全检查 | 帮助识别危险网站、下载、受影响的密码和高风险扩展或设置 |
| 内存节省模式 | 释放长时间未使用标签页占用的部分资源，再次打开时重新激活 |
| 网页翻译 | 对外语网页或选中文本提供翻译入口 |
| 开发者工具 | 提供 DOM、CSS、JavaScript、网络、性能和存储等调试工具 |
| PWA 支持 | 可将支持的网站安装为独立窗口运行的渐进式网页应用 |

## 使用提示与注意事项

- **同步隐私**：登录 Chrome 不等于必须同步全部数据。应在同步设置中确认书签、密码、历史记录等数据类型，并了解其会保存到 Google 账户。
- **无痕模式边界**：无痕模式主要是不在本机资料中保留常规历史记录和 Cookie，并不会让网站、网络管理员或互联网服务提供商无法观察访问行为。
- **扩展风险**：扩展能够申请读取网页内容、修改页面或访问浏览数据等权限。安装前应检查开发者、权限、评价和最近更新时间。
- **资源占用**：大量标签页、扩展和后台网页应用都会增加内存与 CPU 使用。可启用内存节省模式，并移除不常用扩展。
- **安全更新**：Chrome 默认自动更新。可打开“菜单 → 帮助 → 关于 Google Chrome”检查更新状态并重启完成升级。
- **Linux 显示协议**：Chrome 支持 Wayland 和 X11；若拖放、输入或窗口行为异常，可检查 `chrome://flags` 中与 Ozone 平台相关的设置。

## 相关链接

- [Google Chrome 官网](https://www.google.com/chrome/)
- [下载和安装 Chrome](https://support.google.com/chrome/answer/95346)
- [Chrome 帮助中心](https://support.google.com/chrome/)
- [Chrome 安全功能](https://www.google.com/chrome/safety/)
- [Chrome Web Store](https://chromewebstore.google.com/)
- [Chrome 隐私权声明](https://www.google.com/chrome/privacy/)

> 信息核对日期：2026-08-03。系统要求、设置入口和功能可能随版本变化，请以官方页面和当前客户端界面为准。

---

### [回到 General/Essential](README.md)
