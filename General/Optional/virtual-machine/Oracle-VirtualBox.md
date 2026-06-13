# 目录 <!-- omit in toc -->
- [Oracle VirtualBox](#oracle-virtualbox)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [使用方法](#使用方法)
  - [核心功能](#核心功能)
  - [Extension Pack](#extension-pack)
  - [相关链接](#相关链接)

# <img src="../../../.media/png/VirtualBox.png" width="60" alt="VirtualBox logo"> Oracle VirtualBox

Oracle VM VirtualBox 是一款开源、跨平台的桌面虚拟化软件，由 Oracle 开发维护。基础包基于 GPLv2 协议免费使用，支持在单台物理机上同时运行 Windows、Linux、macOS、Solaris 等多种操作系统。

VirtualBox 支持快照、无缝模式、USB 设备直通、共享文件夹等功能，并可通过安装 Extension Pack 获得更多高级特性。

**支持的平台：**
- Windows、macOS、Linux、Solaris

## 安装

### Windows

```bash
# winget
winget install Oracle.VirtualBox
```

也可从 [VirtualBox 官网](https://www.virtualbox.org/wiki/Downloads) 下载 `.exe` 安装包。

### macOS

```bash
# Homebrew
brew install --cask virtualbox
```

也可从 [VirtualBox 官网](https://www.virtualbox.org/wiki/Downloads) 下载 `.dmg` 安装包。

> **注意：** macOS 版本依赖系统内核扩展，安装时需在「系统设置」中允许 Oracle 的软件扩展。

### Linux

```bash
# Debian/Ubuntu
sudo apt install virtualbox virtualbox-ext-pack

# Fedora
sudo dnf install VirtualBox
```

也可从 [VirtualBox Linux 下载页](https://www.virtualbox.org/wiki/Linux_Downloads) 获取对应发行版的 `.deb` 或 `.rpm` 包安装。

## 使用方法

1. **创建虚拟机**：点击「新建」，输入名称、选择操作系统类型和版本，按向导分配内存、创建虚拟硬盘。
2. **安装操作系统**：选择 ISO 镜像文件作为启动盘，启动虚拟机后按正常流程安装。
3. **安装 Guest Additions**：虚拟机启动后，在菜单栏选择「设备」→「安装增强功能」，以获得分辨率自适应、无缝模式、剪贴板共享等增强体验。
4. **管理快照**：在虚拟机管理器中点击「生成备份」→「生成快照」，保存当前状态以便随时恢复。

## 核心功能

| 功能 | 说明 |
|------|------|
| 多系统运行 | 在物理机上同时运行 Windows、Linux、macOS、Solaris 等系统 |
| 快照与还原 | 保存虚拟机当前状态，出问题时一键恢复到快照点 |
| 无缝模式 | 虚拟机中的应用程序窗口直接显示在宿主机桌面上 |
| 虚拟网络 | 支持 NAT、桥接、仅主机、内部网络等多种网络模式 |
| 共享文件夹 | 宿主机与虚拟机之间共享文件夹，方便文件交换 |
| 剪贴板共享 | 支持双向剪贴板共享和拖放操作 |
| 3D 加速 | 支持 OpenGL 和 Direct3D，可运行部分 3D 应用 |
| VM 组管理 | 将多个虚拟机编组，支持批量启动和管理 |

## Extension Pack

VirtualBox Extension Pack 是 Oracle 提供的扩展包（免费用于个人和评测用途），为 VirtualBox 增加以下功能：

| 功能 | 说明 |
|------|------|
| USB 2.0/3.0 直通 | 将宿主机 USB 设备高速直通给虚拟机 |
| VirtualBox RDP | 通过 RDP 协议远程访问虚拟机 |
| 磁盘加密 | 对虚拟磁盘进行 AES 加密保护 |
| PXE 启动 | 支持通过网络启动虚拟机 |
| NVMe 支持 | 模拟 NVMe 控制器用于现代操作系统 |

```bash
# 安装 Extension Pack（版本号需与 VirtualBox 一致）
VBOX_VER=$(vboxmanage --version | cut -d'r' -f1)
curl -O "https://download.virtualbox.org/virtualbox/${VBOX_VER}/Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VER}.vbox-extpack"
sudo vboxmanage extpack install Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VER}.vbox-extpack
```

也可从 [VirtualBox 下载页](https://www.virtualbox.org/wiki/Downloads) 手动下载 `.vbox-extpack` 文件，双击自动安装。

## 相关链接

- [VirtualBox 官网](https://www.virtualbox.org/)
- [官方文档](https://www.virtualbox.org/wiki/Documentation)
- [下载页面](https://www.virtualbox.org/wiki/Downloads)
- [VirtualBox — GitLab](https://www.virtualbox.org/browser)
- [Extension Pack 许可说明](https://www.virtualbox.org/wiki/Licensing_FAQ)

---

### [回到 virtual-machine](README.md)
