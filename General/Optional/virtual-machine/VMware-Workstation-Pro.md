

# 目录 <!-- omit in toc -->
- [ VMware Workstation Pro](#-vmware-workstation-pro)
  - [安装](#安装)
    - [Windows](#windows)
    - [Linux](#linux)
    - [macOS (VMware Fusion Pro)](#macos-vmware-fusion-pro)
  - [使用方法](#使用方法)
  - [核心功能](#核心功能)
  - [历史](#历史)
  - [下载](#下载)
  - [相关链接](#相关链接)

# <img src="../../../.media/png/Vmware_workstation.png" width="60" height="60" alt="Logo"> VMware Workstation Pro

VMware Workstation Pro（曾用名VMware Workstation）是VMware公司推出的一款桌面虚拟计算软件，具有Windows、Linux 版本。此软件可以提供虚拟机功能，使计算机可以同时运行多个不同操作系统。

VMware Workstation支持桥接现有主机网卡，并与虚拟机共享实体磁盘驱动器和USB设备。它也可模拟磁盘驱动器、将ISO映像档挂载为虚拟光盘驱动器，并将虚拟硬盘实现为.vmdk文件。

**支持的平台:**
- Windows、Linux
- macOS  (VMware Fusion Pro)

## 安装

### Windows

```bash
# winget
winget install VMware.WorkstationPro
```

也可从 [Broadcom 下载门户](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true) 获取 `.exe` 安装包（需注册 Broadcom 账号）。

### Linux

```bash
# 从 Broadcom 下载 .bundle 安装包后
chmod +x VMware-Workstation-Full-*.x86_64.bundle
sudo ./VMware-Workstation-Full-*.x86_64.bundle
```

> **注意：** 安装过程中需按提示接受许可协议，按 Enter 滚动阅读条款，输入 `yes` 接受。

也可从 [Broadcom 下载门户](https://support.broadcom.com/group/ecx/free-downloads) 获取最新 `.bundle` 包。

### macOS (VMware Fusion Pro)

VMware Workstation Pro 不直接支持 macOS，macOS 用户可使用 VMware Fusion Pro：

```bash
# Homebrew
brew install --cask vmware-fusion
```

也可从 [Broadcom 下载门户](https://support.broadcom.com/group/ecx/free-downloads) 获取 `.dmg` 安装包。

## 使用方法

1. **创建虚拟机**：点击「创建新的虚拟机」，选择 ISO 镜像文件，按向导完成 CPU、内存、磁盘等配置。
2. **安装操作系统**：启动虚拟机，按正常流程在虚拟机中安装操作系统。
3. **安装 VMware Tools**：虚拟机启动后，在菜单栏选择「虚拟机」→「安装 VMware Tools」，以获得分辨率自适应、剪贴板共享、文件拖放等增强功能。
4. **管理快照**：在虚拟机运行期间，可通过「虚拟机」→「快照」保存当前状态，随时回滚。

## 核心功能

| 功能 | 说明 |
|------|------|
| 多系统运行 | 在同一台物理机上同时运行 Windows、Linux 等操作系统 |
| 快照与克隆 | 保存虚拟机状态并可随时回滚；支持完整克隆和链接克隆 |
| 虚拟网络 | 提供 NAT、桥接、仅主机三种网络模式，支持自定义虚拟网络配置 |
| 文件共享 | 主机与虚拟机之间支持拖放文件、共享文件夹和剪贴板共享 |
| USB 直通 | 将主机的 USB 设备直接连接到虚拟机中使用 |
| 3D 加速 | 支持 DirectX 11 和 OpenGL 4.3，可运行轻量 3D 应用 |
| 虚拟机加密 | 对虚拟机进行全盘加密，防止未授权访问 |
| 远程连接 | 可连接远程 ESXi 或 vCenter 服务器，管理企业级虚拟化环境 |

## 历史

2015年，VMware Workstation 发表12版，VMware Player 转型为 VMware Workstation 的免费版并改名为 VMware Workstation Player，VMware Workstation 的付费版定名为 VMware Workstation Pro。

2023年11月22日，博通收购VMware，VMware 官方名称变更为 VMware by Broadcom，成为博通软件集团 (Broadcom Software Group) 业务单元。

2024年5月14日，博通宣布 VMware Workstation Pro 改为个人免费使用，并宣布 VMware Workstation Player 停产，同年11月13日，博通宣布VMware Workstation Pro改为全面免费使用。

## 下载

VMware Workstation Pro 现为免费软件，需通过 Broadcom 下载门户获取：

1. 访问 [Broadcom 下载门户](https://support.broadcom.com/group/ecx/free-downloads)
2. 注册或登录 Broadcom 账号
3. 搜索 workstation, 选择所需版本和平台，下载对应安装包

> 具体步骤可参考 [官方下载教程](https://knowledge.broadcom.com/external/article/368734)。

## 相关链接

- [VMware Workstation Pro 产品页面](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)
- [官方文档](https://docs.vmware.com/en/VMware-Workstation-Pro/index.html)
- [官方下载教程](https://knowledge.broadcom.com/external/article/368734)
- [Broadcom 下载门户](https://support.broadcom.com/group/ecx/free-downloads)
- [VMware Fusion (macOS)](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)

---

### [回到 virtual-machine](README.md)