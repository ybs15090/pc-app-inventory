# 目录 <!-- omit in toc -->
- [Bitwarden Authenticator](#bitwarden-authenticator)
  - [安装](#安装)
    - [移动端](#移动端)
    - [浏览器扩展](#浏览器扩展)
    - [桌面端](#桌面端)
  - [快速入门](#快速入门)
  - [与密码管理器内置 2FA 的区别](#与密码管理器内置-2fa-的区别)
  - [相关链接](#相关链接)
    - [回到 password](#回到-password)


<img src="../../../.media/png/bitwarden-authenticator.png" width="60" height="60" alt="bitwarden-authenticator logo">

# Bitwarden Authenticator

Bitwarden Authenticator 是 Bitwarden 推出的独立两步验证（2FA）应用，用于生成和管理 TOTP 一次性验证码。与 Bitwarden 密码管理器分开使用，专注提供登录时的二次验证。支持跨设备同步（需登录 Bitwarden 账号），免费、开源。

> 无需使用 Bitwarden 密码管理器也能独立运行——只需注册免费的 Bitwarden 账号即可同步验证码。

## 安装

### 移动端

| 平台 | 获取方式 |
|------|---------|
| Android | [Google Play](https://play.google.com/store/apps/details?id=com.bitwarden.authenticator) / F-Droid |
| iOS | [App Store](https://apps.apple.com/app/bitwarden-authenticator/id6476331021) |

### 浏览器扩展

| 浏览器 | 获取方式 |
|--------|---------|
| Chrome / Edge | [Chrome Web Store](https://chromewebstore.google.com/detail/bitwarden-authenticator/begfocpgfinckfkmofgfgnmpdlghhfif) |
| Firefox | [Firefox Add-ons](https://addons.mozilla.org/firefox/addon/bitwarden-authenticator/) |

### 桌面端

从 [GitHub Releases](https://github.com/bitwarden/authenticator/releases) 下载各平台安装包：

- Windows：`.exe` 安装包
- macOS：`.dmg`
- Linux：AppImage / Snap

```bash
# Snap
sudo snap install bitwarden-authenticator
```

## 快速入门

1. **安装应用**：在手机上安装 Bitwarden Authenticator。
2. **登录账号**：使用 Bitwarden 账号登录（免费注册即可）。
3. **添加验证码**：扫描网站提供的 QR 码，或手动输入密钥。
4. **自动同步**：登录同一账号的所有设备自动同步验证码，更换手机无需重新配置。

## 与密码管理器内置 2FA 的区别

| | Bitwarden Authenticator | 密码管理器内置 2FA |
|------|------|------|
| 定位 | 独立 2FA 应用 | 密码管理器附加功能 |
| 安全隔离 | 密码与 2FA 分开存储 | 密码和 2FA 在同一应用 |
| 适用场景 | 高安全要求、合规场景 | 日常便捷使用 |
| 是否需要订阅 | 免费 | 免费（Bitwarden）/ 部分竞品需付费 |

> **安全建议**：将密码和 2FA 分开存储可避免"单点故障"——即使密码管理器被攻破，攻击者仍缺少第二因素。

## 相关链接

- [Bitwarden Authenticator 官网](https://bitwarden.com/products/authenticator/)
- [GitHub 仓库](https://github.com/bitwarden/authenticator)

---

### [回到 password](README.md)
