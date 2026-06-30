# 目录 <!-- omit in toc -->
- [MacType](#mactype)
  - [简介](#简介)
  - [安装](#安装)
  - [配置与使用](#配置与使用)
    - [基本使用](#基本使用)
    - [推荐配置](#推荐配置)
    - [进程排除](#进程排除)
    - [MacType 与文字大小 120% 失效修复](#mactype-与文字大小-120-失效修复)
    - [相关资源](#相关资源)
    - [回到 Windows/Optional](#回到-windowsoptional)


# MacType

## 简介

MacType 是一款 Windows 平台上的字体渲染优化工具，通过接管 Windows 的 GDI/DirectWrite 字体渲染，模拟 macOS 的字体平滑效果。特别适合低分屏（1080P 及以下）用户改善字体显示效果。

- [官方网站](https://www.mactype.net/)

**核心功能：**
- 替换 Windows 默认字体渲染引擎，消除锯齿并加粗字形
- 支持 GDI 和 DirectWrite 两种渲染模式
- 内置多种渲染配置（如 iOS、macOS、Linux 风格），支持自定义
- 可针对特定进程排除，兼容游戏和部分应用

## 安装

1. 从[官网](https://www.mactype.net/)下载最新版安装包
2. 解压后运行 `MacTypeInstaller.exe` 或直接使用 `MacTypeTray.exe`（绿色便携版）
3. 安装时推荐选择 **MacTray** 模式（系统托盘驻留，方便随时调整）

> **注意：** 安装过程中 Windows Defender 可能弹出 SmartScreen 警告，点击"更多信息" → "仍要运行"即可。

## 配置与使用

### 基本使用

1. 启动 MacType 托盘程序
2. 右键托盘图标 → 选择渲染模式：
   - **注册表加载** — 全局生效，最稳定
   - **服务加载** — 全局生效，开机自启
   - **独立加载** — 仅对指定进程生效
3. 选择配置文件后即可看到效果

### 推荐配置

针对 1080P 屏幕，推荐以下配置组合：
- **渲染配置文件：** `XMac` 或 `Default`（中文显示更均衡）
- **加载方式：** 注册表加载（全局）+ 排除游戏进程

### 进程排除

部分应用（如杀毒软件、部分游戏）可能与 MacType 冲突，可在 `MacType.ini` 中添加排除：

```ini
[UnloadDll]
ProcessName.exe
```

常见需排除的进程：`chrome.exe`（当使用 DirectWrite 模式时）、部分反作弊游戏。

---

### MacType 与文字大小 120% 失效修复

> **问题**：冷启动（长时间断电后第一次开机）后，"设置 → 辅助功能 → 文字大小"的 120% 不生效，需手动拖一次滑块才恢复。快速重启通常不复现。

**真根因**：Windows 传统桌面字体缩放由 `Control Panel\Desktop\WindowMetrics` 的 LOGFONT 控制（与 UWP 的 `TextScaleFactor` 是两套机制）。冷启动时磁盘服务慢，MacType 的 GDI 钩子与 Windows 下发非客户区字体度量**抢时序**，MacType 先行缓存了未缩放字体，导致设置正确但渲染仍为 100%。热重启磁盘有缓存，抢赢几率低，所以通常正常。

**修复思路**：用登录计划任务，等 MacType 服务稳定后，通过 `SPI_SETNONCLIENTMETRICS` 强制重新下发一次当前非客户区字体度量（用 ±1px 微扰触发真实变更再还原），让 MacType 在已起来的状态下重新接收正确度量。

**第一步**：创建脚本 [`~\.scripts\reapply-textscale.ps1`](../../scripts/MacType-setting/reapply-textscale.ps1)

**第二步**：以管理员身份运行 PowerShell，注册登录触发任务（路径和用户名替换为实际值）：

```powershell
Register-ScheduledTask -TaskName "ReapplyTextScale-MacType" `
  -Action (New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -WindowStyle Hidden -NonInteractive -ExecutionPolicy Bypass -File `"C:\Users\<用户名>\.scripts\reapply-textscale.ps1`"") `
  -Trigger (New-ScheduledTaskTrigger -AtLogOn -User "<用户名>") `
  -Settings (New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 2) `
    -MultipleInstances IgnoreNew `
    -DisallowStartIfOnBatteries $false -StopIfGoingOnBatteries $false) `
  -Description "MacType 初始化后重新应用文字大小 120%" -Force
```

**效果**：登录后约 8 秒自动修复，无需手动操作。日志记录在 `~\.scripts\textscale-boot-probe.log`。

**排查方法**：

```powershell
# 查看上次任务结果，非 0 表示脚本崩溃
Get-ScheduledTaskInfo -TaskName ReapplyTextScale-MacType
```

若 `LastTaskResult` 非 0，用 **PowerShell 5.1**（而非 pwsh 7）直接跑脚本看报错。

**维护注意事项**：

- 脚本只能用**英文注释，保持纯 ASCII**——PS 5.1 在无 BOM 的 UTF-8 文件中遇到中文字节会解析错乱，导致脚本崩溃、缩放不生效
- 计划任务命令行必须带 **`-NoProfile`**，否则用户配置文件中的交互式菜单会在非交互模式下报错
- 调试时用 `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` 复现，和任务实际运行环境一致

### 相关资源

- [MacType 用户手册](https://github.com/snowie2000/mactype/wiki)
- [GitHub 社区版](https://github.com/snowie2000/mactype)


---

### [回到 Windows/Optional](README.md)
