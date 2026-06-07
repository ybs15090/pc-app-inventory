# 目录 <!-- omit in toc -->
- [Microsoft Defender](#microsoft-defender)
  - [各平台说明](#各平台说明)
    - [Windows](#windows)
    - [macOS / iOS](#macos--ios)
    - [Android](#android)
  - [核心功能](#核心功能)
  - [使用提示](#使用提示)
  - [相关链接](#相关链接)

# Microsoft Defender

Microsoft Defender 是微软提供的安全防护解决方案。在 Windows 上以系统内置的防病毒和防火墙组件形态提供免费基础防护；在 macOS、iOS 和 Android 上则通过 Microsoft 365 订阅附带的 Defender 应用提供反恶意软件扫描和钓鱼防护。

> Windows 版本的 Defender 防病毒和防火墙完全免费且已内置，无需额外安装。macOS / Android / iOS 版本的完整功能需 Microsoft 365 订阅。

## 各平台说明

### Windows

Windows 10/11 已内置 Microsoft Defender 防病毒，默认启用，通过"Windows 安全"应用管理。无需安装任何额外软件。

**核心组件：**

| 组件 | 说明 |
|------|------|
| 病毒和威胁防护 | 实时扫描、云提交、勒索软件防护（受控文件夹访问） |
| 防火墙和网络保护 | 入站/出站流量过滤，公共/专用网络配置 |
| 应用和浏览器控制 | 基于信誉的应用阻止（SmartScreen） |
| 设备安全性 | 内核隔离、安全启动、TPM 等硬件安全特性 |

### macOS / iOS

从 App Store 下载"Microsoft Defender"应用，登录 Microsoft 365 账号后开启保护：

- 反恶意软件扫描（macOS）
- 钓鱼网站防护（Safari 扩展）
- 网络威胁通知

### Android

从 Google Play 下载"Microsoft Defender"，登录 Microsoft 365 账号后使用：

- 应用扫描（检测恶意 APK）
- 钓鱼链接防护
- 设备安全状态概览

## 核心功能

| 功能 | 说明 |
|------|------|
| 实时防护 | 持续监控文件活动和下载内容 |
| 云提交保护 | 可疑文件自动上传云端分析，几秒内返回判定 |
| 勒索软件防护 | 受控文件夹访问，阻止未知应用修改受保护目录 |
| SmartScreen | 拦截恶意网站和下载的未签名/低信誉应用 |
| 跨设备仪表板 | 在任意设备上查看所有关联设备的安全状态（需 Microsoft 365） |
| 身份盗窃监控 | 监控暗网中的个人数据泄露（部分区域提供） |

## 使用提示

- **排除项**：如果某些开发工具、编译产物被误报，可在"病毒和威胁防护 → 排除项"中添加文件夹或进程。
- **受控文件夹**：将重要工作目录加入受控文件夹保护列表，可有效防御勒索软件。
- **性能影响**：Windows Defender 对系统性能影响极小，日常使用无感知。全盘扫描时可暂时关闭以释放 I/O。
- **第三方杀软共存**：安装第三方杀毒软件后 Windows Defender 会自动进入被动模式，卸载第三方后自动恢复。
- **macOS 用户**：macOS 版 Defender 与 macOS 自带的 Gatekeeper / XProtect 互补，不冲突。

## 相关链接

- [Microsoft Defender 官网](https://www.microsoft.com/microsoft-365/microsoft-defender-for-individuals)
- [Windows 安全中心文档](https://support.microsoft.com/windows/windows-security)
- [Microsoft 365 订阅](https://www.microsoft.com/microsoft-365)

---

### [回到 security](README.md)
