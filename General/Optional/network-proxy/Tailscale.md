<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [ Tailscale](#-tailscale)
  - [软件简介](#软件简介)
  - [适用场景](#适用场景)
  - [安装方法](#安装方法)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
    - [Android / iOS](#android--ios)
  - [使用方法](#使用方法)
    - [登录并加入网络](#登录并加入网络)
    - [查看设备状态](#查看设备状态)
    - [子网路由与出口节点](#子网路由与出口节点)
  - [常见问题](#常见问题)
  - [官方文档与相关链接](#官方文档与相关链接)
    - [回到 network-proxy](#回到-network-proxy)

# <img src="../../../.media/webp/Tailscale.webp" width="60" height="60" alt="Tailscale 图标"> Tailscale

## 软件简介

Tailscale 是基于 WireGuard 的 Mesh VPN，用于把分散在各地的自有设备组成一个加密的私有网络（tailnet），实现点对点访问，无需公网 IP 或手动配置端口转发。它解决的是“设备之间如何安全互通”，而不是科学上网；与 Clash、v2rayA 等代理工具的用途不同。

- 跨平台：Windows、macOS、Linux、Android、iOS，以及 NAS、路由器等设备。
- 基于 WireGuard 加密，自动协商直连，无法直连时通过 DERP 中继。
- 提供 MagicDNS、子网路由、出口节点（Exit Node）和 ACL 访问控制。
- 个人免费计划有人数与设备数限制，以官网定价页为准。

资料核对日期：**2026-10-22**。验证范围：Tailscale 官方安装文档与各平台安装方式核对，未在本次文档整理中安装客户端或进行组网实测。

## 适用场景

| 场景 | 说明 |
|---|---|
| 远程访问家中设备 | 在外网直接访问家里的电脑、NAS、路由器管理页，不需要公网 IP。 |
| 多设备组网 | 笔记本、手机、服务器加入同一 tailnet，通过固定地址互相访问。 |
| 子网路由 | 只在一台设备安装客户端，把整个局域网（如 `192.168.1.0/24`）共享给其他设备。 |
| 出口节点 | 将其他设备的流量经由指定节点转发，用于统一出口或加密公共 Wi-Fi 流量。 |
| 团队访问控制 | 通过 ACL 管理哪些人或设备可以访问哪些服务。 |

> Tailscale 不会隐藏访问目标或绕过网络审查。需要代理上网时，应使用 [Clash Verge](Clash-Verge.md) 等代理工具；两者同时运行可能争用路由或 DNS，按需只启用其中一个。

## 安装方法

### Windows

**包管理器：**

```powershell
# winget
winget install --id Tailscale.Tailscale -e

# Chocolatey
choco install tailscale -y

# Scoop
scoop install extras/tailscale
```

**本地安装包：**

从[官方 Windows 下载页](https://tailscale.com/download/windows)获取 `.msi` 安装包，或从 [Tailscale Packages](https://pkgs.tailscale.com/stable/#windows) 下载指定版本。双击安装后，托盘会出现 Tailscale 图标。支持 Windows 10 及以上版本。

### macOS

**包管理器：**

```bash
# GUI 应用（推荐）
brew install --cask tailscale

# 仅命令行版本（适合服务器或不需要图形界面时）
brew install tailscale
```

**本地安装包：**

从[官方 macOS 下载页](https://tailscale.com/download/mac)下载安装包，或从 Mac App Store 安装。首次启动需要在“系统设置 → 隐私与安全性”中允许系统扩展，并登录账号。

### Linux

**方式一：官方安装脚本（推荐）**

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

脚本会为当前发行版添加官方软件源并安装 `tailscale` 与 `tailscaled`。

**方式二：发行版包管理器**

已添加 Tailscale 软件源后，可使用对应命令：

| 发行版 | 命令 |
|---|---|
| Debian / Ubuntu | `sudo apt update && sudo apt install tailscale` |
| Fedora | `sudo dnf install tailscale` |
| openSUSE | `sudo zypper install tailscale` |
| Arch Linux | `sudo pacman -S tailscale` |
| Alpine | `sudo apk add tailscale` |

**方式三：本地安装包**

从 [Tailscale Packages](https://pkgs.tailscale.com/stable/) 选择对应发行版与架构，下载 `.deb`、`.rpm` 或 `.tgz`，再按本地包安装。例如：

```bash
sudo apt install ./tailscale_*_amd64.deb
```

Linux 客户端需要 root 权限运行 `tailscaled`；服务由 systemd 管理，可通过 `systemctl status tailscaled` 查看状态。

### Android / iOS

- **Android**：通过 Google Play 搜索 Tailscale 安装，或从[官方 Android 下载页](https://tailscale.com/download/android)获取 APK。应用通过系统 VPN 服务建立连接，状态栏会显示 VPN 图标。
- **iOS / iPadOS**：从 App Store 安装，首次连接时按提示添加 VPN 配置。

移动端适合作为访问其他设备的客户端，但不适合承担子网路由或出口节点角色。

## 使用方法

### 登录并加入网络

1. 启动 Tailscale，选择登录方式（Google、Microsoft、GitHub 或邮箱）。
2. 在浏览器中完成授权，设备会自动加入账号对应的 tailnet。
3. Linux 命令行环境执行：

```bash
sudo tailscale up
```

如需指定账号、接受路由或使用出口节点，可在 `up` 时附加参数：

```bash
sudo tailscale up --accept-routes
sudo tailscale up --exit-node=<节点名或 IP>
```

### 查看设备状态

```bash
# 当前设备与网络状态
tailscale status

# 本机 Tailscale IPv4 地址
tailscale ip -4

# 连通性测试
tailscale ping <设备名>
```

设备名和 IP 可在[管理后台](https://login.tailscale.com/admin/machines)查看。开启 MagicDNS 后，可直接使用设备名访问，无需记 IP。

### 子网路由与出口节点

**共享局域网（子网路由）**

在作为网关的设备上执行：

```bash
sudo tailscale up --advertise-routes=192.168.1.0/24
```

随后在管理后台的 **Machines** 页面批准该路由。其他设备需要接受路由：

```bash
sudo tailscale up --accept-routes
```

**作为出口节点**

```bash
sudo tailscale up --advertise-exit-node
```

Linux 节点还需启用 IP 转发：

```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf
```

之后在管理后台批准出口节点，其他设备即可在客户端中选择使用。Windows 和 macOS 的出口节点功能可在图形界面中开启，无需手动修改内核参数。

> 子网路由和出口节点会改变目标设备的网络流量走向。配置前确认网段不与现有网络冲突，并保留本地管理通道，避免因路由或防火墙错误导致设备失联。

## 常见问题

| 问题 | 说明或处理方法 |
|---|---|
| 登录后看不到其他设备 | 确认设备属于同一 tailnet、账号一致，并执行 `tailscale status` 查看在线状态。 |
| 设备显示在线但无法访问 | 检查目标设备是否开启防火墙、服务是否监听在 Tailscale 地址上；可用 `tailscale ping` 判断连通性。 |
| 子网路由不生效 | 需在管理后台批准路由，并在客户端启用 `--accept-routes`；同时确认目标网段没有与本地网络重叠。 |
| 出口节点选项不可用 | 节点需先以 `--advertise-exit-node` 启动并在后台批准；Linux 还需启用 IP 转发。 |
| Linux 安装后连接失败 | 检查 `tailscaled` 服务状态和防火墙规则，确认允许 `tailscale0` 接口流量。 |
| 与代理软件同时使用时网络异常 | Tailscale 与代理工具都可能修改路由和 DNS。按需停用其中一个，或在代理软件中为 Tailscale 网段设置直连。 |
| Android 后台连接断开 | 在系统电池设置中允许 Tailscale 后台运行；VPN 常驻通知被清理后连接可能中断。 |
| 免费额度是否够用 | 个人免费计划有人数与设备数限制，团队或大量设备场景应查看官网定价与许可说明。 |

## 官方文档与相关链接

- [Tailscale 官网](https://tailscale.com/)
- [官方下载页](https://tailscale.com/download)
- [官方安装文档](https://tailscale.com/docs/install)
- [官方知识库](https://tailscale.com/kb/)
- [管理后台](https://login.tailscale.com/admin/)
- [软件包仓库](https://pkgs.tailscale.com/stable/)
- [源码仓库](https://github.com/tailscale/tailscale)
- [服务状态页](https://status.tailscale.com/)

---

### [回到 network-proxy](README.md)
