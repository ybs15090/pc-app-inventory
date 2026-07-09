<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->
- [VB-CABLE](#-vb-cable)
  - [简介](#简介)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
  - [功能特点](#功能特点)
  - [使用方法](#使用方法)
    - [基础设置](#基础设置)
    - [常见场景](#常见场景)
  - [其他平台替代方案](#其他平台替代方案)
  - [相关链接](#相关链接)

# <img src="../../.media/svg/VB-CABLE.svg" width="60" height="60" alt="VB-CABLE logo"> VB-CABLE

最轻量、易用的虚拟音频线，一进一出，适合将电脑播放的声音转为麦克风输入。

## 简介

VB-CABLE 是由 [VB-Audio Software](https://vb-audio.com/) 开发的跨平台虚拟音频驱动。它在系统中创建一条"虚拟音频线"——一个播放设备（CABLE Input）和一个录音设备（CABLE Output），发送到播放设备的音频会直接出现在录音设备中，实现应用程序之间的音频路由。

**典型场景**：将电脑播放的音乐 / 视频声音作为麦克风信号输入到语音软件（QQ、微信、Discord、OBS 等），或在不同应用间传递音频流。

VB-CABLE 基础版可免费使用（Donationware），另有捐赠版（VB-CABLE A+B / C+D）可提供额外的虚拟线路。

## 安装

### Windows

```powershell
# winget
winget install "VB-Audio Virtual Cable"
```

也可从官网下载安装包：

1. 访问 [VB-Audio Cable 页面](https://vb-audio.com/Cable/)
2. 下载 **VBCABLE_Setup_x64.exe**（64 位系统）或 **VBCABLE_Setup.exe**（32 位系统）
3. 右键以管理员身份运行安装程序
4. 点击 **Install Driver**，安装完成后建议重启系统

> **注意**：安装过程会短暂中断音频（正常现象），重启后即可正常使用。

### macOS

从 [VB-Audio 官网](https://shop.vb-audio.com/zh/mac-/29-vb-cable-mac.html) 下载对应版本的驱动包：

| 版本 | 包名 | 说明 |
|------|------|------|
| 基础版 | `VBCable_MACDriver_Pack108.zip` | 1 条虚拟音频线（Donationware） |
| A+B | `VBCableAB_MACDriver_Pack108.zip` | 2 条独立虚拟音频线 |
| C+D | `VBCableCD_MACDriver_Pack108.zip` | 另外 2 条独立虚拟音频线 |

安装步骤：

1. 下载对应 ZIP 包并解压
2. 运行安装程序，按提示完成驱动安装
3. 安装后在 `/Applications/VB-Audio/` 中可找到 **VB-CABLE Control Panel**，用于管理延迟和监控状态

> **系统要求**：macOS 10.10 及以上，同时支持 Intel 和 Apple Silicon 芯片。

卸载方法：

```bash
# 需手动删除以下文件
sudo rm -rf /Library/Audio/Plug-Ins/HAL/VBCable.Driver
sudo rm -rf /Applications/VB-Audio
sudo rm -f /Library/Preferences/com.vbaudio.vbcable.plist
sudo rm -f /Library/LaunchDaemons/com.vbaudio.vbcableagent.plist
```

## 功能特点

- **零延迟**：内核级驱动，音频传输无感知延迟
- **轻量级**：安装包仅 ~2 MB，资源占用极低
- **位精确**：PCM 音频逐位传输，无损音质
- **即装即用**：安装后自动出现在系统音频设备列表中，无需额外配置
- **采样率兼容**：支持 44.1kHz ~ 192kHz 采样率，自动匹配
- **多通道**：macOS 版支持 1~8 通道配置
- **多应用并发**：多个应用可同时读取同一个录音端点

## 使用方法

### 基础设置

**Windows：**

1. **将音频路由到虚拟线**：在 `声音设置 → 应用音量和设备首选项` 中，将特定应用的输出设备设为 `CABLE Input (VB-Audio Virtual Cable)`
2. **在另一应用中接收**：将目标应用的麦克风输入设备设为 `CABLE Output (VB-Audio Virtual Cable)`

**macOS：**

1. **将音频路由到虚拟线**：在 `系统设置 → 声音 → 输出` 中选择 `VB-CABLE` 作为输出设备；或在特定应用（如音乐播放器）的音频设置中切换
2. **在另一应用中接收**：将目标应用的输入设备设为 `VB-CABLE`
3. 使用 **VB-CABLE Control Panel** 调整内部延迟和查看驱动状态（绿色 LED = 正常运行）

> **macOS 技巧**：如需同时听到本机声音和路由后的声音，可使用 `音频 MIDI 设置` 创建聚合设备（Aggregate Device），将 VB-CABLE 与实体音箱/耳机合并。

**Windows 技巧：**

> 如需同时听到本机声音和路由后的声音，可在 `声音设置 → 录制 → CABLE Output → 属性 → 侦听` 中勾选"侦听此设备"，将播放设备设为你实际使用的音箱/耳机。

### 常见场景

| 场景 | 输出端（播放） | 输入端（录音） |
|------|---------------|---------------|
| 播放背景音乐到语音聊天 | 音乐播放器 → `CABLE Input` | 语音软件麦克风 → `CABLE Output` |
| 录制系统音频 | 系统声音 → `CABLE Input` | OBS / Audacity 音频源 → `CABLE Output` |
| 应用间音频传递 | App A 输出 → `CABLE Input` | App B 输入 → `CABLE Output` |

## 其他平台替代方案

Linux 平台的虚拟音频方案：

| 工具 | 说明 |
|------|------|
| PulseAudio `module-null-sink` | 系统内置，创建虚拟音频 sink |
| PipeWire `loopback` | 现代 Linux 音频方案，原生支持虚拟路由 |

## 相关链接

- [VB-Audio 官网](https://vb-audio.com/)
- [VB-CABLE Windows 下载页](https://vb-audio.com/Cable/)
- [VB-CABLE macOS 下载页](https://shop.vb-audio.com/zh/mac-/29-vb-cable-mac.html)
- [VB-Audio 产品对比](https://vb-audio.com/Cable/#ComparisonTable)
- [VB-CABLE for MAC 论坛](https://forum.vb-audio.com/viewtopic.php?t=1063)

---

### [回到 General/Optional](README.md)
