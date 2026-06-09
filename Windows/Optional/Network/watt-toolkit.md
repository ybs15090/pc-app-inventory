<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->
- [ Watt Toolkit](#-watt-toolkit)
  - [安装](#安装)
  - [主要功能](#主要功能)
    - [网络加速](#网络加速)
    - [Steam 工具](#steam-工具)
  - [加速原理](#加速原理)
  - [使用方法](#使用方法)
  - [相关链接](#相关链接)
    - [回到 Windows/Optional/Network](#回到-windowsoptionalnetwork)


# <img src="../../../.media/png/watt-toolkit.png" width="70" height="70" alt="Logo" /> Watt Toolkit

Watt Toolkit（原名 Steam++）是一款开源跨平台网络工具箱，支持 Windows、macOS、Linux、Android 和 iOS，以 Windows 平台使用最为广泛。核心功能是通过 SNI 代理免科学上网访问 Steam、GitHub、OneDrive 等平台，同时提供 Steam 本地令牌、账号切换等辅助工具。

## 安装

从官网下载安装包（推荐，含自动更新）：

1. 访问 [官方下载页面](https://steampp.net/download)
2. 选择对应系统架构（x64 / ARM64）的安装版（Setup）或便携版（Portable）
3. 安装完成后以**管理员身份运行**，部分加速功能需要管理员权限

```powershell
# winget
winget install Watt-Toolkit
```

## 主要功能

### 网络加速

通过修改本地 hosts 或 SNI 代理对以下平台加速，**无需代理工具**：

| 平台 | 说明 |
|------|------|
| Steam | 商店、下载、社区、创意工坊加速 |
| GitHub | 访问、克隆、Release 下载加速 |
| OneDrive | 文件同步与下载加速 |
| Epic Games | 商店与游戏下载加速 |
| Discord | 国内直连访问 |
| Twitch | 直播与视频加速 |

> 流量不经过第三方服务器，加速原理见下方「[加速原理](#加速原理)」。

### Steam 工具

| 功能 | 说明 |
|------|------|
| 本地令牌 | 替代 Steam 手机令牌，管理二步验证码 |
| 账号切换 | 快速切换多个 Steam 账号，无需重新登录 |
| 库存管理 | 查看 Steam 库存与交易历史 |

## 加速原理

国内访问 Steam 等平台失败，通常有两种原因：

- **DNS 污染**：查询域名时被返回错误 IP，导致根本连不上目标服务器
- **SNI 封锁**：HTTPS 握手时客户端会明文发送目标域名（SNI 字段），防火墙识别后切断连接

Watt Toolkit 的处理方式：

1. 修改本机 `hosts`，将目标域名指向 `127.0.0.1`，绕过 DNS 污染
2. 在本机启动 HTTPS 服务接管流量，转发时**替换或隐藏 SNI 字段**，防火墙无法识别目标域名，放行数据包
3. 数据包直连目标服务器真实 IP，服务器正常响应

整个过程流量只经过本机软件，不经过任何第三方服务器。

> **局限性**：此方案只能绕过域名层面的封锁。若目标平台的 IP 本身已被封（如 Google），则无效，这种情况需要使用 VPN。

## 使用方法

1. **启用加速**：打开软件 → 选择「网络加速」→ 勾选需要加速的平台 → 点击「一键加速」
2. **添加令牌**：进入「本地令牌」→ 扫码或手动导入 Steam 令牌
3. **切换账号**：进入「账号切换」→ 添加已登录过的账号 → 一键切换
4. **停止加速**：点击「停止加速」或直接退出程序，hosts 修改会自动还原

> 加速 Steam 下载时，建议在 Steam 设置 → 下载 → 下载地区中选择「中国 — 上海」或「中国 — 武汉」配合使用。

## 相关链接

- [官方网站](https://steampp.net/)
- [下载页面](https://steampp.net/download)
- [GitHub](https://github.com/BeyondDimension/SteamTools)

---

### [回到 Windows/Optional/Network](README.md)
