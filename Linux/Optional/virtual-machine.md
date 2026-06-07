# 目录 <!-- omit in toc -->
- [GNOME Boxes](#gnome-boxes)
  - [安装](#安装)
  - [使用](#使用)
- [VirtualBox](#virtualbox)
  - [安装](#安装-1)
- [virt-manager](#virt-manager)
  - [安装](#安装-2)


# <img src="../../.media/svg/Boxes.svg" width="60" height="60" alt="Boxes logo"> GNOME Boxes

一个简单易用的 GNOME 虚拟化应用程序，适合快速创建和访问虚拟机与远程系统。基于 QEMU/KVM，集成于 GNOME 桌面环境。

- [官方网站](https://apps.gnome.org/zh-CN/Boxes/)
- [GitHub](https://gitlab.gnome.org/GNOME/gnome-boxes)

## 安装

```bash
sudo apt update
sudo apt install gnome-boxes
```

也可通过 GNOME 软件中心搜索 "Boxes" 安装。

## 使用

1. 打开 GNOME Boxes，点击左上角 "+" 按钮
2. 选择 ISO 镜像文件或输入远程连接地址
3. 按向导完成虚拟机创建
4. 双击虚拟机即可启动

> **注意：** Boxes 默认使用 KVM 加速，需确保 CPU 支持虚拟化（`egrep -c '(vmx|svm)' /proc/cpuinfo` 返回值 > 0）。


# VirtualBox

功能全面的跨平台虚拟机软件，支持 Windows、Linux、macOS 和 Solaris 等多种操作系统。提供快照、无痕模式、USB 设备直通等高级功能。

- [官方网站](https://www.virtualbox.org/)
- [官方文档](https://www.virtualbox.org/wiki/Documentation)

## 安装

```bash
# 添加 Oracle 官方仓库
echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian focal contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo apt update
sudo apt install virtualbox-7.0
```

也可直接[下载 .deb 包](https://www.virtualbox.org/wiki/Linux_Downloads)安装。

安装完成后建议安装 **VirtualBox Extension Pack** 以获得 USB 2.0/3.0、PXE 启动等支持。

> **注意：** 如果系统已启用 KVM，VirtualBox 运行时可能会冲突，需临时卸载 `kvm` 和 `kvm_intel` 模块。


# virt-manager

基于 libvirt 的虚拟机管理工具（Virtual Machine Manager），通过图形界面管理 QEMU/KVM 虚拟机。功能强大，适合需要精细化控制的用户。

- [官方网站](https://virt-manager.org/)
- [GitHub](https://github.com/virt-manager/virt-manager)

## 安装

```bash
sudo apt update
sudo apt install virt-manager qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
```

安装后将当前用户加入 `libvirt` 组以避免权限问题：

```bash
sudo adduser $USER libvirt
```

注销重新登录后生效。启动 virt-manager：

```bash
virt-manager
```


---

### [回到 Linux/Optional](README.md)
