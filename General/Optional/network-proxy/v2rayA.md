# 目录 <!-- omit in toc -->
- [v2rayA](#v2raya)
  - [简介](#简介)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
      - [Snap 安装（最简单）](#snap-安装最简单)
      - [APT 源安装（推荐）](#apt-源安装推荐)
      - [手动 DEB 安装](#手动-deb-安装)
      - [Docker 部署](#docker-部署)
  - [配置与使用](#配置与使用)
  - [常见问题](#常见问题)


# v2rayA

## 简介

v2rayA 是一个基于 Web GUI 的 V2Ray 客户端，使用 Go + Vue.js 开发。支持 VMess、VLESS、Shadowsocks、SSR、Trojan、Tuic、Juicity 等多种协议，可在浏览器中通过 `http://localhost:2017` 管理。

**适用场景：** 桌面系统代理、路由器旁路由部署、NAS/家庭网关全局透明代理。

- [GitHub](https://github.com/v2rayA/v2rayA)
- [官方文档](https://v2raya.org/)

## 安装

### Windows

推荐使用 winget 一键安装：

```powershell
winget install --id=v2rayA.v2rayA -e
```

也可通过 Scoop 安装，或从 [GitHub Releases](https://github.com/v2rayA/v2rayA/releases) 下载 `.exe` 安装包手动安装。

> Windows 版 v2rayA 同样通过 Web UI（`http://localhost:2017`）管理，安装后从开始菜单启动或设为开机自启。

### macOS

v2rayA 在 macOS 上的适配较简单，无原生图形界面，需通过终端运行。

通过 Homebrew 安装：

```bash
brew tap v2raya/v2raya
brew install v2raya
```

或从 [GitHub Releases](https://github.com/v2rayA/v2rayA/releases) 下载 macOS 二进制文件，手动 `chmod +x` 后运行。

启动后在浏览器访问 `http://localhost:2017` 进行管理。

### Linux

#### Snap 安装（最简单）

```bash
sudo snap install v2raya
```

> Snap 会自动打包内核，无需额外配置。安装后直接跳到 [配置与使用](#配置与使用)。

#### APT 源安装（推荐）

适合 Ubuntu 20.04 及更新版本，支持自动更新：

```bash
# 添加官方 GPG 密钥和 APT 源
curl -Ls https://mirrors.v2raya.org/go.sh | sudo bash

# 安装
sudo apt update
sudo apt install v2raya
```

安装 Xray 内核（推荐，支持更多协议）：

```bash
wget -qO- https://github.com/XTLS/Xray-install/raw/main/install-release.sh | sudo bash
```

或安装 v2ray 内核：

```bash
wget -qO- https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh | sudo bash
```

#### 手动 DEB 安装

```bash
wget -O /tmp/v2raya.deb \
  https://github.com/v2rayA/v2rayA/releases/latest/download/installer_debian_amd64.deb
sudo apt install /tmp/v2raya.deb
```

#### Docker 部署

```bash
docker run -d \
  --name v2raya \
  --restart always \
  --privileged \
  --network host \
  -e V2RAYA_ADDRESS=0.0.0.0:2017 \
  -v /etc/v2raya:/etc/v2raya \
  mzz2017/v2raya
```

**其它发行版：**

| 发行版 | 安装方式 |
|--------|----------|
| **Fedora** | `sudo dnf install v2raya`（添加官方源后） |
| **Arch** | AUR: `paru -S v2raya` |
| **openSUSE** | 使用 Docker 或手动 DEB 转 RPM |

## 配置与使用

### 1. 关联内核（APT/DEB 安装后）

编辑 `/etc/default/v2raya`，确保内核路径正确：

```bash
V2RAYA_V2RAY_BIN=/usr/local/bin/xray
V2RAYA_V2RAY_CONFDIR=/usr/local/etc/xray
```

### 2. 启动服务（Linux）

```bash
sudo systemctl enable --now v2raya
sudo systemctl status v2raya
```

### 3. 访问 Web UI

浏览器打开 **`http://localhost:2017`**，首次访问需创建管理员账户。

### 4. 添加节点

- 导入订阅链接（支持 Base64/SIP008 等多种格式）
- 或手动添加单个节点

### 5. 启用代理

- **Linux：** Web UI 中选择节点后，开启透明代理（自动配置 iptables 规则）
- **Windows / macOS：** 开启系统代理模式

## 常见问题

| 问题 | 解决方法 |
|------|----------|
| 无法访问 Web UI | 检查服务状态 `sudo systemctl status v2raya`（Linux）；检查端口 `ss -tlnp \| grep 2017` |
| 忘记管理员密码 | `sudo v2raya --reset-password` |
| Linux 透明代理无效 | 确保以 root 权限运行：`sudo systemctl start v2raya` |
| IPv6 无法连接 | `sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=0` |
| Snap 版无法透明代理 | Snap 沙箱限制，改用 APT 方式安装 |
| Windows 开机自启 | 安装时勾选"开机自启"，或手动将快捷方式放入启动文件夹 |
