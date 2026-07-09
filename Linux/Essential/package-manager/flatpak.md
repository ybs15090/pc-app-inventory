# 目录 <!-- omit in toc -->
- [Flatpak](#flatpak)
  - [简介](#简介)
  - [安装](#安装)
    - [Ubuntu / Debian 系](#ubuntu--debian-系)
    - [其它发行版速查](#其它发行版速查)
  - [Flathub 仓库](#flathub-仓库)
    - [添加 Flathub](#添加-flathub)
    - [Flathub Beta 频道](#flathub-beta-频道)
  - [常用命令](#常用命令)
  - [桌面集成与权限管理](#桌面集成与权限管理)
    - [返回keepassxc](#返回keepassxc)
    - [回到 package-manager](#回到-package-manager)



# Flatpak

## 简介

Flatpak 是一个面向 Linux 的通用软件包管理框架，采用沙箱隔离技术，使应用与系统库解耦，同一软件可在不同发行版上运行。截至 2025 年，Flatpak 已被 **38+ 个 Linux 发行版** 官方支持，是桌面 GUI 应用分发的事实标准。

核心优势：

- 📦 **跨发行版** — 一套打包，处处运行
- 🔒 **沙箱隔离** — 应用运行在受限环境中，更安全
- 🚀 **版本更新及时** — 由应用开发者直接发布，不受发行版仓库延迟影响
- 🧩 **运行时（Runtime）机制** — 共享底层库，避免重复打包

> **与 Snap 的关系：** Ubuntu 预装 Snap，Flatpak 为可选替代方案。二者可以共存，无冲突。一般建议：桌面 GUI 应用优先用 Flatpak；系统工具和开发库用 APT/Snap。

- [官方网站](https://flatpak.org/)
- [Flathub 应用商店](https://flathub.org/)

## 安装

部分发行版（Fedora、Linux Mint、Pop!_OS、elementary OS、Endless OS）已预装 Flatpak，可直接跳到 [Flathub 仓库](#flathub-仓库) 章节。

### Ubuntu / Debian 系

**Ubuntu 20.04 及更新版本（22.04 / 24.04）** 均可从官方仓库直接安装：

```bash
sudo apt update
sudo apt install flatpak
```

**获取更新版本（推荐）：** 官方 PPA 提供的版本通常比系统仓库更新，适合所有 Ubuntu 版本：

```bash
sudo add-apt-repository ppa:flatpak/stable -y
sudo apt update
sudo apt install flatpak
```

**GNOME 桌面用户** 建议安装软件中心插件，方便图形化浏览和安装：

```bash
sudo apt install gnome-software-plugin-flatpak
```

**KDE 桌面用户：**

```bash
sudo apt install plasma-discover-backend-flatpak
```

### 其它发行版速查

| 发行版 | 安装命令 |
|--------|----------|
| **Debian** | `sudo apt install flatpak` |
| **Fedora / RHEL / CentOS / Rocky** | `sudo dnf install flatpak`（Fedora 预装） |
| **Arch / Manjaro / EndeavourOS** | `sudo pacman -S flatpak` |
| **openSUSE Leap / Tumbleweed** | `sudo zypper install flatpak` |
| **Alpine Linux** | `sudo apk add flatpak` |
| **Gentoo** | `emerge --ask sys-apps/flatpak` |
| **Solus** | `sudo eopkg install flatpak` |
| **Void Linux** | `sudo xbps-install -S flatpak` |

安装完成后建议重启系统，确保所有 Flatpak 集成全部生效：

```bash
sudo reboot
```

## Flathub 仓库

Flathub 是 Flatpak 的官方应用商店，托管了数千款应用，是安装 Flatpak 软件的主要来源。

### 添加 Flathub

```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

验证是否添加成功：

```bash
flatpak remotes
# 应看到 flathub 在列表中
```

### Flathub Beta 频道

获取尚未正式发布的测试版应用：

```bash
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
```

安装 Beta 版本时需显式指定仓库：

```bash
flatpak install flathub-beta <应用ID>
```

## 常用命令

| 操作 | 命令 |
|------|------|
| 搜索软件 | `flatpak search <关键词>` |
| 安装软件（用户级） | `flatpak install --user flathub <应用ID>` |
| 安装软件（系统级） | `sudo flatpak install flathub <应用ID>` |
| 运行软件 | `flatpak run <应用ID>` |
| 卸载软件 | `flatpak uninstall <应用ID>` |
| 列出已安装应用 | `flatpak list --app` |
| 更新全部 | `flatpak update` |
| 更新单个应用 | `flatpak update <应用ID>` |
| 清理未使用的运行时 | `flatpak uninstall --unused` |
| 查看应用详情 | `flatpak info <应用ID>` |
| 查看远程仓库 | `flatpak remotes` |
| 删除远程仓库 | `flatpak remote-delete <仓库名>` |

**示例：**

```bash
# 搜索 Firefox
flatpak search firefox

# 以用户身份安装（推荐，无需 sudo）
flatpak install --user flathub org.mozilla.firefox

# 运行
flatpak run org.mozilla.firefox

# 从 .flatpakref 文件安装（从 Flathub 网站下载）
flatpak install ./com.example.App.flatpakref
```

## 桌面集成与权限管理

Flatpak 应用安装后会自动出现在桌面菜单中。如果应用未显示：

- **Xorg 下：** `Alt + F2` → 输入 `r` → 回车（重启 GNOME Shell）
- **Wayland 或其它桌面：** 注销后重新登录

**权限管理：** Flatpak 的沙箱机制会限制应用对宿主文件系统的访问。推荐使用 **Flatseal** 图形化工具管理每个应用的沙箱权限：

```bash
flatpak install flathub com.github.tchx84.Flatseal
```

**应用存储路径：**

| 范围 | 路径 |
|------|------|
| 系统级安装 | `/var/lib/flatpak/` |
| 用户级安装 | `~/.local/share/flatpak/` |

> **最佳实践（2025）：** 桌面 GUI 应用优先使用 Flatpak（或 Snap）安装；系统工具、驱动和开发库使用原生包管理器（APT/DNF/Pacman）。


---

### [返回keepassxc](../../../General/Essential/password/keepassxc.md)

### [回到 package-manager](README.md)
