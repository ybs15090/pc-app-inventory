<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [Microsoft Edge](#microsoft-edge)
  - [适用场景](#适用场景)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [初次配置](#初次配置)
  - [核心功能](#核心功能)
  - [使用提示与注意事项](#使用提示与注意事项)
  - [相关链接](#相关链接)

# <img src="../../.media/png/Edge.png" width="60" height="60" alt="Microsoft Edge logo"> Microsoft Edge

Microsoft Edge 是 Microsoft 推出的跨平台 Chromium 浏览器，支持 Windows、macOS、Linux、Android 和 iOS。它与 Windows、Microsoft 账户和 Microsoft 365 服务结合紧密，并提供垂直标签页、分屏、休眠标签页、PDF 阅读器、沉浸式阅读器及 Copilot 等功能。

## 适用场景

- 主要使用 Windows，希望减少额外安装并获得较好的系统集成
- 经常使用 Microsoft 365、Outlook、OneDrive 或组织提供的工作账户
- 需要垂直标签页、标签页分组、工作区或单标签分屏
- 经常阅读、批注 PDF，或者使用朗读和沉浸式阅读工具
- 需要通过个人资料分隔个人账户、工作账户和访客环境
- 需要企业策略、Microsoft Defender SmartScreen 或旧版企业网站兼容能力

## 安装

建议从 [Microsoft Edge 官方下载页](https://www.microsoft.com/edge/download)获取安装程序。功能可用性可能因设备类型、市场和浏览器版本而不同。

### Windows

Windows 10 和 Windows 11 通常已经预装 Edge，并通过 Microsoft Edge Update 自动更新。若浏览器缺失或安装损坏，可从官方下载页重新下载安装程序。

可打开“设置及其他 → 帮助和反馈 → 关于 Microsoft Edge”，检查当前版本和更新状态。

### macOS

从官方下载页选择适用于 Mac 的安装程序，确认 Intel 或 Apple 芯片架构后完成安装。首次启动时可从 Safari、Chrome 或其他支持的浏览器导入数据。

### Linux

官方下载页提供适用于 Debian/Ubuntu 的 `.deb` 包，并可按页面入口选择适合 RPM 系发行版的软件包。例如：

```bash
# Debian / Ubuntu：下载 DEB 后在文件所在目录执行
sudo apt install ./microsoft-edge-stable_*.deb

# Fedora / RHEL：下载 RPM 后在文件所在目录执行
sudo dnf install ./microsoft-edge-stable-*.rpm
```

动态文件名中的版本号和架构标记会随发布版本变化，执行前应确认实际文件名。

## 初次配置

1. 从原浏览器导入收藏夹、密码、历史记录和其他支持的数据。
2. 根据需要登录 Microsoft 账户或工作/学校账户；不需要同步时可以跳过。
3. 在“设置 → 个人资料 → 同步”中只启用需要跨设备同步的数据类型。
4. 在“设置 → 隐私、搜索和服务”中选择跟踪防护级别，并检查 Microsoft Defender SmartScreen 等安全选项。
5. 在“设置 → 系统和性能”中检查效率模式、休眠标签页和启动增强等选项。
6. 根据屏幕比例选择水平或垂直标签页，并把分屏等常用按钮固定到工具栏。

## 核心功能

| 功能 | 说明 |
|------|------|
| 垂直标签页 | 将标签页显示在窗口侧面，标题更容易辨认，适合宽屏和大量标签页 |
| 分屏 | 在同一个标签页中并排显示两个网页，支持调整比例和交换位置 |
| 标签页分组与工作区 | 按任务组织标签页；工作区可保存项目相关的标签页和收藏内容 |
| 休眠标签页与效率模式 | 暂停不活跃的后台标签页，降低部分 CPU、内存和能耗使用 |
| PDF 阅读器 | 直接打开 PDF，并提供搜索、朗读、标注、添加文字等功能 |
| 沉浸式阅读与朗读 | 简化网页排版，并使用语音朗读页面内容 |
| Copilot | 在浏览器中提供 AI 辅助；具体能力和数据处理方式取决于账户、地区、版本及组织策略 |
| Microsoft 同步 | 同步收藏夹、密码、历史记录、设置、打开的标签页等所选数据 |
| Microsoft Defender SmartScreen | 帮助识别已知恶意网站、诈骗页面和危险下载 |
| 扩展与网页应用 | 支持 Microsoft Edge 加载项，并兼容大量 Chromium 扩展和 PWA |

## 使用提示与注意事项

- **账户与同步**：个人 Microsoft 账户和工作/学校账户可能采用不同的同步与管理策略。使用组织账户时，应留意管理员下发的浏览器策略。
- **Copilot 数据边界**：向 Copilot 提交问题或允许其参考页面内容前，应检查当前账户、隐私设置和组织要求，不要发送敏感资料。
- **侧边栏变化**：Microsoft 正在逐步停用传统侧边栏的应用列表，不再允许新增侧边栏应用；Copilot 和普通侧窗不受该调整影响。不要依赖即将退役的应用入口构建长期工作流。
- **InPrivate 边界**：InPrivate 主要减少浏览数据在本机资料中的保存，不代表网站、组织网络或互联网服务提供商无法看到访问行为。
- **扩展风险**：优先从 Microsoft Edge 加载项或可信的 Chrome Web Store 页面安装扩展，并检查扩展请求的站点访问权限。
- **Windows 集成**：部分 Windows 小组件、PWA 和系统功能依赖 Edge/WebView2。即使使用其他默认浏览器，也不建议通过非官方方式强制删除 Edge。
- **安全更新**：保持自动更新开启，并定期访问 `edge://settings/help` 检查更新状态。

## 相关链接

- [Microsoft Edge 官网](https://www.microsoft.com/edge/)
- [Microsoft Edge 官方下载页](https://www.microsoft.com/edge/download)
- [Microsoft Edge 支持中心](https://support.microsoft.com/microsoft-edge)
- [Microsoft Edge 功能列表](https://www.microsoft.com/edge/features)
- [Edge 生产力功能](https://www.microsoft.com/edge/features/productivity)
- [Edge 性能功能说明](https://support.microsoft.com/edge/learn-about-performance-features-in-microsoft-edge)
- [Edge 安全浏览建议](https://support.microsoft.com/edge/securely-browse-the-web-in-microsoft-edge)
- [Microsoft Edge 加载项](https://microsoftedge.microsoft.com/addons/)

> 信息核对日期：2026-08-03。系统要求、功能名称和设置入口可能随版本、地区或组织策略变化，请以官方页面和当前客户端界面为准。

---

### [回到 General/Essential](README.md)
