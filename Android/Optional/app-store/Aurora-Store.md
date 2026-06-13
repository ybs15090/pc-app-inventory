# 目录 <!-- omit in toc -->
- [ Aurora Store](#-aurora-store)
  - [安装](#安装)
  - [特点](#特点)
  - [登录方式](#登录方式)
  - [使用提示](#使用提示)
  - [相关链接](#相关链接)

# <img src="../../../.media/jpg/Aurora-Store.jpg" width="60" alt="logo"> Aurora Store

**推荐与 [Gbox](Gbox.md) 搭配使用**:
- 不依赖 GMS 的应用直接使用 `Aurora Store` 下载即可
- 强依赖 GMS 的应用使用 `Gbox` 容器下载运行(会有微小性能损耗，但至少可以使用)
---

Aurora Store 是一款开源的 Google Play 第三方客户端（前身为 Yalp Store），可在不依赖 Google Play 服务（GMS）的设备上下载 Google Play 中的应用。它通过模拟 Google Play API 实现应用浏览、搜索和下载，无需 Google 账号即可使用匿名模式。

> Aurora Store 自身可从 F-Droid 获取，是去 Google 化设备（如 LineageOS、/e/OS 等）获取应用的推荐方案。

## 安装

```bash
# 从 F-Droid 安装（推荐）
# 在 F-Droid 客户端中搜索 "Aurora Store"
```

也可从 [Aurora OSS 官网](https://auroraoss.com/) 或 [GitLab Releases](https://gitlab.com/AuroraOSS/AuroraStore/-/releases) 下载 APK 安装包。

## 特点

| 特点 | 说明 |
|------|------|
| 开源透明 | 代码完全开源，可审查安全性和隐私合规性 |
| 匿名登录 | 内置匿名账号池，无需 Google 账号即可浏览和下载 |
| 无 GMS 依赖 | 不依赖 Google Play 服务，适用于自定义 ROM 和无 GMS 设备 |
| F-Droid 生态 | 可通过 F-Droid 仓库安装和获取更新 |
| 伪装设备 | 可伪装为不同设备和 DPI，下载适配特定机型的应用版本 |
| 黑名单管理 | 支持过滤不需要的应用和包含跟踪器的应用 |

## 登录方式

| 方式 | 说明 |
|------|------|
| 匿名登录 | 使用 Aurora 提供的共享账号登录，适合偶尔下载应用 |
| Google 账号 | 使用个人 Google 账号登录（建议使用备用账号，存在一定风险） |

> **安全提示：** 匿名账号由社区共享，Google 对其有速率限制。如果频繁使用匿名模式，可能遇到下载失败，等待片刻后重试即可。使用个人 Google 账号登录存在违反 Google 服务条款的风险，建议使用备用账号。

## 使用提示

- **下载失败**：匿名账号池偶尔会被 Google 限流，等待几分钟后重试或切换到其他匿名账号。
- **付费应用**：Aurora Store 无法购买付费应用，只能更新已购买的应用和下载免费应用。
- **安全性**：从 Aurora Store 下载的 APK 与 Google Play 下载的文件签名一致，均为官方版本，不会注入第三方代码。
- **系统集成**：部分 ROM 已将 Aurora Store 作为默认应用商店，可在系统设置中开启「自动更新」。
---
## 相关链接

- [Aurora OSS 官网](https://auroraoss.com/)
- [Aurora Store — GitLab](https://gitlab.com/AuroraOSS/AuroraStore)
- [F-Droid 仓库页面](https://f-droid.org/packages/com.aurora.store/)
