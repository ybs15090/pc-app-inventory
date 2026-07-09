# 目录 <!-- omit in toc -->
- [ KeePassXC](#-keepassxc)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
    - [浏览器扩展](#浏览器扩展)
  - [快速入门](#快速入门)
  - [核心功能](#核心功能)
  - [常用配置](#常用配置)
    - [数据库保存位置](#数据库保存位置)
    - [浏览器集成](#浏览器集成)
    - [自动输入](#自动输入)
    - [TOTP 与通行密钥](#totp-与通行密钥)
    - [SSH Agent](#ssh-agent)
  - [与 KeePass 的关系](#与-keepass-的关系)
  - [安全建议](#安全建议)
  - [相关链接](#相关链接)
    - [回到 password](#回到-password)

# <img src="../../../.media/svg/keepassxc.svg" width="60" height="60" alt="keepassxc-logo"> KeePassXC

KeePassXC 是一款免费、开源、跨平台的本地密码管理器，支持 Windows、macOS 和 Linux。它以 KeePass 兼容的 KDBX 数据库为核心，将用户名、密码、URL、附件、备注等信息保存在离线加密文件中，不依赖官方云服务，适合希望自己掌控密码数据库和同步方式的用户。

> 如果你主要在 Linux 或 macOS 上使用 KeePass 系列数据库，KeePassXC 通常比 KeePass 2.x + Mono 更原生；如果你依赖 KeePass 2.x 插件生态，则应优先考虑 KeePass。

## 安装

### Windows

```bash
# WinGet
winget install -e --id KeePassXCTeam.KeePassXC

# Chocolatey
choco install keepassxc
```

也可从 [KeePassXC 下载页](https://keepassxc.org/download/) 获取 Windows 安装包或便携版 ZIP。

### macOS

```bash
# Homebrew
brew install --cask keepassxc
```

也可从 [KeePassXC 下载页](https://keepassxc.org/download/) 下载 Apple Silicon 或 Intel 版本。

### Linux

KeePassXC 官方推荐 Linux 桌面优先使用 Flatpak，也提供 AppImage、Snap、PPA 和各发行版软件包。

```bash
# Flatpak
flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install --user flathub org.keepassxc.KeePassXC

# Snap
sudo snap install keepassxc

# Ubuntu / Debian 发行版仓库
sudo apt install keepassxc

# Fedora
sudo dnf install keepassxc

# Arch Linux
sudo pacman -S keepassxc
```

### 浏览器扩展

KeePassXC Browser 可配合桌面端在浏览器中自动填充密码。

| 浏览器 | 获取方式 |
|--------|---------|
| Firefox | Firefox Add-ons |
| Chrome / Chromium / Brave / Vivaldi | Chrome Web Store |
| Microsoft Edge | Microsoft Edge Add-ons |

> 浏览器扩展需要本机 KeePassXC 桌面端配合使用，不能单独作为云端密码库运行。

## 快速入门

1. **创建数据库**：打开 KeePassXC，选择 `Create new database`，生成 `.kdbx` 数据库。
2. **设置主密码**：使用足够长的主密码；如需要更高安全性，可叠加密钥文件或硬件密钥挑战响应。
3. **建立分组**：按用途建立 `个人`、`工作`、`服务器`、`银行卡` 等分组。
4. **添加条目**：为每个网站或应用单独保存用户名、密码、URL、备注和附件。
5. **启用浏览器集成**：安装 KeePassXC Browser，在 KeePassXC 设置中启用对应浏览器。
6. **备份数据库**：定期备份 `.kdbx`，尤其是在迁移设备、升级版本和调整同步方式之前。

## 核心功能

| 功能 | 说明 |
|------|------|
| KDBX 数据库 | 原生创建、打开和保存 KeePass 兼容的 KDBX 文件 |
| 本地加密 | 数据保存在本地离线加密文件中，可自行选择保存位置 |
| 密码生成器 | 生成随机密码或更容易记忆的口令短语 |
| 自动输入 | 可向桌面应用或网页登录框输入用户名和密码 |
| 浏览器集成 | 支持主流浏览器扩展，提供网页自动填充 |
| 导入导出 | 支持从 CSV、1Password、Bitwarden、Proton Pass、KeePass 1 等格式导入 |
| 数据库报告 | 检查密码健康度、重复密码和泄露风险 |
| TOTP | 存储并生成一次性验证码 |
| SSH Agent | 管理 SSH 密钥并与系统 SSH Agent 集成 |
| Secret Service | 在 Linux 上可作为 FreeDesktop.org Secret Service 使用 |

## 常用配置

### 数据库保存位置

- 单机使用：将 `.kdbx` 放在固定目录，并启用自动备份。
- 多设备同步：可将 `.kdbx` 放入 OneDrive、Dropbox、Syncthing、坚果云等同步目录。
- 高安全要求：数据库可放同步目录，密钥文件放在单独位置，如 U 盘或只在本机保存。
- 团队共享：优先评估 KeeShare 或专门的团队密码管理方案，避免多人直接同时编辑同一数据库文件。

### 浏览器集成

1. 在 KeePassXC 中打开 `Tools` → `Settings` → `Browser Integration`。
2. 勾选 `Enable browser integration`。
3. 选择要连接的浏览器。
4. 安装 KeePassXC Browser 扩展。
5. 在浏览器扩展中与当前数据库配对。

配对后，浏览器扩展会根据 URL 匹配条目，提示填充用户名、密码，也可在保存新账号时写回数据库。

### 自动输入

KeePassXC 也支持 Auto-Type，适合不方便使用浏览器扩展的软件登录窗口。

- 默认使用条目中的用户名、密码和窗口匹配规则。
- 可以为特殊登录流程自定义 Auto-Type 序列。
- 在多个相似窗口之间使用时，应先确认窗口标题匹配是否准确。

### TOTP 与通行密钥

KeePassXC 支持保存 TOTP 一次性验证码，并可通过浏览器集成支持通行密钥相关功能。

安全取舍：

- 将密码和 TOTP 放在同一个数据库中更方便，但会增加单点失守风险。
- 对银行、邮箱、主账号等高价值账号，建议把二次验证放在独立验证器或硬件密钥中。

### SSH Agent

KeePassXC 可保存 SSH 私钥，并将其加载到 SSH Agent。适合希望统一管理服务器密码、密钥和备注的用户。

配置思路：

1. 将 SSH 私钥作为条目附件保存。
2. 在条目中启用 SSH Agent。
3. 解锁数据库后，按需把密钥加入 Agent。
4. 数据库锁定或关闭时，确认密钥是否自动移除。

## 与 KeePass 的关系

KeePassXC 和 [KeePass](keepass.md) 都围绕 KeePass 系列数据库工作，常见 `.kdbx` 数据库可以在两者之间迁移或共用，但它们不是同一个项目。

| 对比项 | KeePass | KeePassXC |
|--------|---------|-----------|
| 项目定位 | 原始 KeePass 项目，插件生态丰富 | 社区维护的跨平台原生客户端 |
| 桌面平台 | 官方主要面向 Windows，其他平台可通过 Mono 或兼容客户端使用 | 官方支持 Windows、macOS、Linux |
| 数据格式 | KeePass 2.x 使用 KDBX | 创建、打开和保存 KeePass 兼容 KDBX |
| 插件 | 支持 KeePass 2.x 插件 | 不兼容 KeePass 2.x 插件，更多功能内置 |
| 浏览器集成 | 通常依赖插件或第三方方案 | 官方提供 KeePassXC Browser 配套扩展 |
| 推荐场景 | 需要 KeePass 插件、使用 Windows 或偏好原项目 | 需要原生跨平台体验、浏览器集成、Linux/macOS 桌面使用 |

如果已经在使用 KeePass 数据库，迁移到 KeePassXC 前建议复制一份 `.kdbx` 测试打开、编辑、保存和同步流程，确认所有客户端都能正常使用。

## 安全建议

- 使用长主密码，避免只用短密码保护整个数据库。
- 开启空闲自动锁定、系统锁屏时锁定和剪贴板自动清空。
- 多设备同步时保留数据库历史版本，防止误同步导致文件损坏。
- 使用密钥文件时，单独备份密钥文件，不要与数据库放在同一同步目录。
- 浏览器集成只连接可信浏览器，定期检查已授权的浏览器连接。
- 导出 CSV、HTML 等明文文件后，及时删除并清理备份。

## 相关链接

- [KeePassXC 官网](https://keepassxc.org/)
- [KeePassXC 下载页](https://keepassxc.org/download/)
- [KeePassXC 入门指南](https://keepassxc.org/docs/KeePassXC_GettingStarted)
- [KeePassXC 用户指南](https://keepassxc.org/docs/KeePassXC_UserGuide)
- [KeePassXC GitHub](https://github.com/keepassxreboot/keepassxc)
- [KeePass](keepass.md)

---

### [回到 password](README.md)
