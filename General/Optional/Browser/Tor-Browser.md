<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [Tor Browser](#tor-browser)
  - [适用场景](#适用场景)
  - [工作原理与边界](#工作原理与边界)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
    - [移动端](#移动端)
  - [首次连接](#首次连接)
  - [核心功能](#核心功能)
  - [安全等级](#安全等级)
  - [重要安全建议](#重要安全建议)
  - [相关链接](#相关链接)

# <img src="../../../.media/png/Tor_Browser.png" width="60" height="60" alt="Tor Browser logo"> Tor Browser

Tor Browser 是 Tor Project 维护的隐私浏览器，基于 Firefox ESR 并针对 Tor 网络、抗浏览器指纹和会话隔离进行了专门配置。它将 Tor Browser 自身的网页流量通过多个 Tor 中继转发，使目标网站通常看不到用户的直接公网 IP，并可访问 `.onion` 服务。

Tor Browser 的目标是降低网站、网络观察者和广告跟踪者关联用户活动的能力，但它不能保证绝对匿名，也不会自动保护电脑中其他应用的网络流量。

## 适用场景

- 希望隐藏访问网站时直接暴露的公网 IP 地址
- 需要降低跨网站跟踪和浏览器指纹识别风险
- 在公共网络上需要更强的流量路径隐私保护
- 需要访问 Tor 网络中的 `.onion` 服务
- 在 Tor 连接受限制的网络环境中使用网桥
- 进行对身份隔离有明确需求的研究、新闻或敏感信息检索

## 工作原理与边界

Tor Browser 通常通过入口、中间和出口等多个 Tor 中继转发连接。网站看到的通常是出口中继 IP，而不是用户直接连接时的 IP。Tor 网络内部的多跳转发不意味着从出口到普通网站的最后一段一定加密，因此仍应优先使用 HTTPS 网站。

Tor 只保护已正确配置为使用它的应用。仅启动 Tor Browser 不会让下载工具、聊天软件、游戏或其他浏览器自动通过 Tor。登录实名账户、提交姓名或电话号码等个人信息，也会直接向对应网站暴露身份。

## 安装

只应从 [Tor Project 官方下载页](https://www.torproject.org/download/)或官方列出的可信渠道下载。高风险使用场景建议进一步[验证安装包签名](https://support.torproject.org/tor-browser/getting-started/verifying-tor-browser/)。

### Windows

官方支持 Windows 10 和 Windows 11。下载 `.exe` 安装程序，验证签名后运行安装向导，并记住选择的安装目录。

### macOS

下载官方 `.dmg` 文件，验证签名后打开并完成安装。安装前应查看官方页面标注的最低 macOS 版本要求。

### Linux

建议使用 64 位 Linux，从官方下载页获取 `.tar.xz` 压缩包：

```bash
# 解压下载的压缩包
tar -xf tor-browser-linux-*.tar.xz

# 进入解压后的 Tor Browser 目录后启动
./start-tor-browser.desktop

# 可选：注册到桌面应用菜单
./start-tor-browser.desktop --register-app
```

如果启动文件没有执行权限，可在目录中执行：

```bash
chmod +x start-tor-browser.desktop
```

压缩包名称和解压目录会随版本、语言及架构变化，应以实际文件名为准。Tor Project 已宣布将在 Tor Browser 16.0 停止支持 32 位 x86 Linux，因此应优先使用 64 位系统。

### 移动端

Tor Project 提供 Android 版 Tor Browser，可通过 Google Play、Tor Project 官网或官方说明指定的 F-Droid 仓库安装。

Tor Project **没有官方 iOS 版 Tor Browser**。其推荐的 Onion Browser 受 iOS WebKit 限制，无法提供与 Tor Browser 完全相同的隐私保护，不能简单视为等价版本。

## 首次连接

1. 启动 Tor Browser 后，普通网络环境可直接选择“连接”。
2. 如果 Tor 连接被网络阻止，打开连接设置并配置 Tor Project 提供的内置网桥，或通过官方渠道获取网桥地址。
3. 连接成功后再开始浏览，不要把普通浏览器代理设置误认为 Tor Browser 已经连接。
4. 需要切断当前网站关联并更换 Tor 路径时，可使用“为此站点使用新线路”；需要清除全部会话状态时使用“新身份”。

## 核心功能

| 功能 | 说明 |
|------|------|
| Tor 多跳路由 | 通过多个中继转发 Tor Browser 的网页连接，隐藏直接来源 IP |
| 抗浏览器指纹 | 尽量让不同用户的浏览器特征相似，降低通过配置差异识别用户的能力 |
| 会话与站点隔离 | 降低 Cookie、缓存和其他站点数据被用于跨站关联的风险 |
| NoScript | 内置脚本控制扩展，并配合安全等级限制高风险网页功能 |
| HTTPS-Only | 优先请求 HTTPS 连接，减少出口到普通网站之间的明文传输风险 |
| 网桥 | 在直接连接 Tor 受阻时，通过不公开或伪装的入口连接网络 |
| 新线路与新身份 | 为网站更换 Tor 路径，或清除会话状态并重新建立浏览身份 |
| Onion 服务 | 访问使用 `.onion` 地址、连接保持在 Tor 网络内部的服务 |

## 安全等级

点击地址栏旁的盾牌图标可以调整安全等级：

| 等级 | 适用情况 | 影响 |
|------|----------|------|
| 标准 | 日常使用和网站兼容性优先 | 启用大多数网页功能，包括 JavaScript |
| 较安全 | 风险较高，希望减少可利用的动态网页功能 | 禁用非 HTTPS 网站的 JavaScript，并限制部分字体和媒体 |
| 最安全 | 高风险浏览，安全性优先 | 默认对所有网站禁用 JavaScript，并进一步限制图片、字体和媒体等功能 |

提高安全等级会导致部分网站无法登录、播放视频或正常显示，应根据风险和可用性权衡，而不是随意修改 NoScript 的细节设置。

## 重要安全建议

- **不要安装额外扩展或主题**：它们可能绕过 Tor、扩大攻击面或形成独特浏览器指纹。Tor Project 只测试随浏览器附带的扩展配置。
- **不要使用 Tor 下载 BT**：BT 客户端可能绕过代理或在协议中暴露真实 IP，同时会严重占用 Tor 网络资源。
- **不要把 Tor 当成全局 VPN**：Tor Browser 只保护自身网页流量；其他软件需要单独评估和配置。
- **谨慎登录和填写表单**：网站可能看不到直接 IP，但登录实名账户或提交个人资料后仍然知道用户身份。
- **谨慎打开下载文件**：DOC、PDF 等文件若在外部应用联网打开，可能绕过 Tor 直接连接网络。优先在 Tor Browser 内查看，并在必要时离线处理。
- **优先使用 HTTPS**：Tor 会保护用户到出口中继之间的路径，但普通网站的最后一段连接仍取决于 HTTPS。
- **不要随意调整默认配置**：自定义窗口、字体、语言、扩展和其他浏览器特征可能降低抗指纹效果。
- **及时更新**：浏览器漏洞可能直接破坏隐私保护。收到更新提示后应尽快完成更新并重启。
- **接受速度与兼容性代价**：多跳路由通常比直接连接慢，部分网站可能显示验证码、限制出口节点或完全拒绝访问。

## 相关链接

- [Tor Project 官网](https://www.torproject.org/)
- [Tor Browser 官方下载页](https://www.torproject.org/download/)
- [Tor Browser 安装说明](https://support.torproject.org/tor-browser/getting-started/installing/)
- [Tor Browser 用户手册](https://tb-manual.torproject.org/)
- [安全使用 Tor Browser](https://support.torproject.org/tor-browser/security/using-tb-safely/)
- [安全等级说明](https://support.torproject.org/tor-browser/features/security-levels/)
- [扩展和插件风险](https://support.torproject.org/tor-browser/features/plugins/)
- [验证安装包签名](https://support.torproject.org/tor-browser/getting-started/verifying-tor-browser/)
- [Tor 网络状态](https://status.torproject.org/)

> 信息核对日期：2026-08-03。系统支持、下载渠道和安全建议可能随 Tor Browser 版本变化，请以 Tor Project 官方页面为准。

---

### [回到 Browser](README.md)
