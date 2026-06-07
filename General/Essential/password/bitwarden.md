# 目录 <!-- omit in toc -->
- [ Bitwarden](#-bitwarden)
  - [安装](#安装)
    - [浏览器扩展](#浏览器扩展)
    - [桌面端](#桌面端)
      - [Windows](#windows)
      - [macOS](#macos)
      - [Linux](#linux)
    - [移动端](#移动端)
  - [快速入门](#快速入门)
  - [核心功能](#核心功能)
  - [使用提示](#使用提示)
  - [相关链接](#相关链接)
    - [回到 password](#回到-password)

# <img src="../../../.media/png/bitwarden.png" width="60" height="60" alt="bitwarden-logo"> Bitwarden

Bitwarden 是一款开源的跨平台密码管理器，支持 Windows、macOS、Linux、Android、iOS 及主流浏览器。所有密码数据在本地加密后再同步至云端，用户可以自主选择官方服务器或自托管（自建服务端）。个人用户可免费使用全部核心功能，付费版提供高级两步验证、安全报告等额外特性。

## 安装

### 浏览器扩展

| 浏览器 | 获取方式 |
|--------|---------|
| Chrome / Edge / Brave | [Chrome Web Store](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb) |
| Firefox | [Firefox Add-ons](https://addons.mozilla.org/firefox/addon/bitwarden-password-manager/) |
| Safari | [Mac App Store](https://apps.apple.com/app/bitwarden/id1352778147) |

### 桌面端

#### Windows

```bash
# winget
winget install Bitwarden.Bitwarden
```

也可从[官网下载页](https://bitwarden.com/download/)获取 `.exe` 安装包。

#### macOS

```bash
# Homebrew
brew install --cask bitwarden
```

也可从 App Store 或[官网](https://bitwarden.com/download/)下载。

#### Linux

```bash
# Snap
sudo snap install bitwarden

# Flatpak
flatpak install flathub com.bitwarden.desktop
```

也可从[官网](https://bitwarden.com/download/)下载 AppImage。

### 移动端

| 平台 | 获取方式 |
|------|---------|
| Android | Google Play / F-Droid / 官网 APK |
| iOS | App Store |

## 快速入门

1. **注册账号**：在 [bitwarden.com](https://bitwarden.com/) 注册免费账号，或自行部署 [Vaultwarden](https://github.com/dani-garcia/vaultwarden) 服务端。
2. **安装客户端**：在常用设备和浏览器上安装 Bitwarden 客户端/扩展。
3. **添加密码**：手动录入或从其他密码管理器导入（支持 50+ 格式）。
4. **自动填充**：浏览网页时 Bitwarden 会自动识别登录表单并提示填充。

## 核心功能

| 功能 | 说明 |
|------|------|
| 密码生成 | 自定义长度和字符集的强密码生成器 |
| 自动填充 | 浏览器和移动端自动识别并填写登录信息 |
| 跨设备同步 | 所有设备实时同步，官方云服务或自托管 |
| 安全笔记 | 存储非密码类敏感信息（信用卡、身份证等） |
| 两步验证 | 支持 TOTP、FIDO2/WebAuthn、邮箱验证 |
| 密码库共享 | 与家人或团队成员共享密码集合 |
| 紧急访问 | 指定信任联系人，在紧急情况下获取访问权限 |
| 数据导出 | 支持 JSON、CSV 等格式导出，防止厂商锁定 |

## 使用提示

- **自托管**：如需完全掌控数据，可使用 Vaultwarden（Rust 实现的开源服务端，兼容 Bitwarden API），部署在自有服务器或 NAS 上。
- **主密码**：主密码是加密所有数据的唯一密钥，一旦丢失无法恢复。建议使用长口令并备份到安全位置。
- **浏览器 vs 桌面端**：浏览器扩展专注自动填充，桌面端适合管理密码库、导入导出等批量操作。两者可同时使用。
- **定期审计**：使用"密码库报告"功能扫描弱密码、重复密码和已知泄密账号。

## 相关链接

- [Bitwarden 官网](https://bitwarden.com/)
- [Bitwarden 下载页](https://bitwarden.com/download/)
- [Bitwarden — GitHub](https://github.com/bitwarden)
- [Vaultwarden（自托管服务端）](https://github.com/dani-garcia/vaultwarden)

---

### [回到 password](README.md)
