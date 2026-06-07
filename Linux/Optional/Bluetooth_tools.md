# 目录 <!-- omit in toc -->
- [Blueman](#blueman)
  - [安装](#安装)
  - [使用](#使用)
  - [相关链接](#相关链接)

# <img src="../../.media/svg/blueman.svg" width="60" height="60" alt="blueman logo"> Blueman

Blueman 是一款 Linux 系统的蓝牙管理工具，基于 BlueZ 协议栈开发，提供图形化界面和命令行两种操作方式。功能覆盖设备配对、文件收发、音频路由、网络共享等蓝牙应用场景。

## 安装

```bash
sudo apt update
sudo apt install blueman -y
```

## 使用

安装后在应用程序菜单中启动"Bluetooth Manager"，即可搜索、配对和管理蓝牙设备。

常用操作：
- **配对设备**：点击"搜索"扫描附近设备 → 右键 → 配对
- **发送文件**：右键已配对设备 → 发送文件
- **音频切换**：在设备属性中选择音频输出模式（A2DP / HSP/HFP）

CLI 方式：

```bash
bluetoothctl               # 进入交互式蓝牙控制台
scan on                     # 扫描设备
pair <MAC地址>              # 配对
connect <MAC地址>           # 连接
```

## 相关链接

- [Blueman GitHub](https://github.com/blueman-project/blueman)
- [蓝牙配置教程](https://geek-blogs.com/blog/bluetooth-linux-ubuntu/)

---

### [回到 Linux/Optional](README.md)
