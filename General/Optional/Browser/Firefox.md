<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [Mozilla Firefox](#mozilla-firefox)
  - [适用场景](#适用场景)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [初次配置](#初次配置)
  - [核心功能](#核心功能)
  - [侧边栏与垂直标签页](#侧边栏与垂直标签页)
  - [使用提示与注意事项](#使用提示与注意事项)
  - [相关链接](#相关链接)

# <img src="../../../.media/png/Firefox.png" width="60" height="60" alt="Mozilla Firefox logo"> Mozilla Firefox

Mozilla Firefox 是由 Mozilla 开发的免费开源跨平台浏览器，使用 Gecko 浏览器引擎，而不是 Chromium。桌面版支持 Windows、macOS 和 Linux，并提供增强型跟踪保护、Cookie 隔离、Mozilla 账户同步、扩展、阅读模式、画中画以及开发者工具等功能。

## 适用场景

- 希望使用 Chromium 之外的独立浏览器引擎
- 重视跟踪器拦截、Cookie 隔离和细粒度网站权限管理
- 需要在多台设备之间端到端加密同步书签、密码、历史记录和标签页
- 希望使用垂直标签页、侧边栏或自定义工具栏
- 需要 Firefox Add-ons 扩展生态和完善的网页开发工具
- 希望通过不同个人资料或容器分隔工作、个人及多账户登录状态

## 安装

建议从 [Firefox 官方下载页](https://www.mozilla.org/firefox/new/)或操作系统的可信软件源安装。使用 Mozilla 官方页面可以自动匹配操作系统和语言版本。

### Windows

从官方下载页运行在线安装程序，也可以在 Microsoft Store 中安装 Mozilla Firefox。需要离线安装或指定语言、架构、发布通道时，可使用 Mozilla 的完整安装包下载入口。

### macOS

下载并打开 Firefox 的 `.dmg` 文件，将 Firefox 拖入“应用程序”文件夹。首次启动时根据系统提示确认打开，并可从 Safari、Chrome 等浏览器导入数据。

### Linux

许多 Linux 发行版已预装 Firefox，或可从发行版软件源安装：

```bash
# Debian / Ubuntu 系发行版的软件源版本
sudo apt install firefox

# Fedora / RHEL 系发行版的软件源版本
sudo dnf install firefox

# Flatpak
flatpak install flathub org.mozilla.firefox

# Snap
sudo snap install firefox
```

发行版软件源可能提供 ESR 版本，或比 Mozilla 正式版稍晚更新。需要 Mozilla 直接维护的 DEB/RPM 软件包、ARM64 构建或压缩包安装时，应按 [Mozilla Linux 安装指南](https://support.mozilla.org/kb/install-firefox-linux)配置官方软件源或选择对应安装方式。

## 初次配置

1. 从原浏览器导入书签、历史记录、密码和其他支持的数据。
2. 根据需要将 Firefox 设置为默认浏览器。
3. 打开“设置 → 隐私与安全”，选择标准、严格或自定义增强型跟踪保护，并检查 Cookie、网站权限和数据收集选项。
4. 如需跨设备同步，登录 Mozilla 账户，并只选择需要同步的数据类型。
5. 打开“设置 → 常规 → 浏览器布局”，按需启用侧边栏和垂直标签页。
6. 仅从可信来源安装必要扩展，并检查扩展请求的站点访问权限。

## 核心功能

| 功能 | 说明 |
|------|------|
| Gecko 引擎 | 独立于 Chromium 的网页渲染与 JavaScript 运行环境 |
| 增强型跟踪保护 | 拦截多类已知跟踪器、跨站跟踪 Cookie 和部分指纹跟踪脚本 |
| Total Cookie Protection | 按网站隔离 Cookie，减少第三方跨站关联浏览活动的能力 |
| Firefox Sync | 通过 Mozilla 账户同步所选数据，并在离开浏览器前完成端到端加密 |
| 密码管理器 | 保存、生成和检查登录密码，可配合主密码保护本地登录数据 |
| Firefox Add-ons | 提供内容处理、开发、生产力和隐私等扩展及主题 |
| 阅读模式与画中画 | 简化文章排版，或将网页视频显示为浮动窗口 |
| 多个人资料 | 使用独立资料分隔书签、Cookie、扩展、历史记录和设置 |
| 开发者工具 | 提供检查器、控制台、网络、性能、存储和响应式设计等工具 |

## 侧边栏与垂直标签页

Firefox 136 起引入更新后的侧边栏，可从主页面旁快速访问：

- 书签、历史记录和保存的密码
- Mozilla 账户同步的其他设备标签页
- 用户选择的 AI 聊天服务
- 垂直排列的固定标签页和普通标签页

进入“设置 → 常规 → 浏览器布局”启用侧边栏，或右键工具栏/标签栏选择“启用垂直标签页”。侧边栏可以放在窗口左侧或右侧，支持拖动调整宽度，并可在折叠图标模式与显示完整标签标题的展开模式之间切换。

Firefox 的侧边栏以浏览器工具和标签页管理为主，不像 Opera 那样预设大量社交网站，也不像 Vivaldi 那样直接把任意网址作为网页面板。需要固定网站时，可评估可信的侧边栏扩展，但应同时检查扩展权限。

## 使用提示与注意事项

- **同步并非备份**：Firefox Sync 采用端到端加密，但主要用途是保持设备数据一致，不能代替独立的书签、密码和个人资料备份。
- **隐私浏览边界**：隐私窗口主要减少本地历史、Cookie 和表单数据的保留，并不会对网站、组织网络或互联网服务提供商隐藏访问行为。
- **兼容性**：少数只针对 Chromium 测试的网站可能出现功能或排版问题。遇到异常时，先排除扩展和严格跟踪保护的影响，再向网站或 Mozilla 报告。
- **扩展安全**：扩展可能读取网页内容、浏览历史或剪贴板。即使来自 Firefox Add-ons，也应检查权限、开发者和更新记录。
- **同步密码安全**：Mozilla 无法解密同步数据；应使用强账户密码、启用多重验证，并保存账户恢复方式。
- **更新**：Firefox 默认自动更新。可打开“菜单 → 帮助 → 关于 Firefox”检查状态；Linux 软件源版本通常随系统包管理器更新。

## 相关链接

- [Firefox 官网](https://www.mozilla.org/firefox/)
- [Firefox 官方下载页](https://www.mozilla.org/firefox/new/)
- [Firefox 帮助中心](https://support.mozilla.org/products/firefox)
- [Windows 安装说明](https://support.mozilla.org/kb/how-install-firefox-windows)
- [macOS 安装说明](https://support.mozilla.org/kb/how-download-and-install-firefox-mac)
- [Linux 安装说明](https://support.mozilla.org/kb/install-firefox-linux)
- [侧边栏和垂直标签页](https://support.mozilla.org/kb/use-sidebar-access-tools-and-vertical-tabs)
- [Firefox Sync 说明](https://support.mozilla.org/kb/sync)
- [Firefox Add-ons](https://addons.mozilla.org/firefox/)

> 信息核对日期：2026-08-03。安装方式、界面名称和功能可能随版本或发行版打包方式变化，请以 Mozilla 官方页面和当前客户端界面为准。

---

### [回到 Browser](README.md)
