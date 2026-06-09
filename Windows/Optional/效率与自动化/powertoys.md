<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->
- [Microsoft PowerToys](#-microsoft-powertoys)
  - [安装](#安装)
  - [主要功能模块](#主要功能模块)
  - [常用快捷键速览](#常用快捷键速览)
  - [相关链接](#相关链接)


<p align="center">
    <img src="../../../.media/png/powertoys-light.png" />
</p>

# <img src="../../../.media/png/powertoys.png" width="60" height="60" alt="Logo" /> Microsoft PowerToys

Microsoft PowerToys 是微软官方出品的 Windows 系统增强工具集，包含多个实用小工具，覆盖窗口管理、快速启动、文件批量处理、键鼠增强等场景，适合追求效率的 Windows 用户。

## 安装

```powershell
# winget（推荐）
winget install Microsoft.PowerToys

# Scoop
scoop install powertoys

# Chocolatey
choco install powertoys
```

也可从 [GitHub Releases](https://github.com/microsoft/PowerToys/releases) 或 [Microsoft Store](https://apps.microsoft.com/detail/xp89dcgq3k6vld) 下载安装包。

安装完成后，PowerToys 在系统托盘运行，通过托盘图标打开设置面板，可按需启用/禁用各模块。

## 主要功能模块

| 模块 | 功能说明 | 默认快捷键 |
|------|----------|------------|
| **PowerToys Run** | 快速启动器，搜索应用、文件、计算、网页等 | `Alt + Space` |
| **FancyZones** | 自定义窗口布局，将屏幕划分为多个区域并吸附窗口 | `Win + Shift + \`` |
| **Color Picker** | 屏幕取色工具，支持 HEX / RGB / HSL 等格式 | `Win + Shift + C` |
| **Text Extractor** | 屏幕 OCR 识别，截图区域后复制识别文字 | `Win + Shift + T` |
| **Peek** | 文件快速预览（类似 macOS 空格预览），无需打开应用 | `Ctrl + Space` |
| **Image Resizer** | 右键菜单批量调整图片尺寸 | 右键菜单 |
| **PowerRename** | 文件批量重命名，支持正则表达式 | 右键菜单 |
| **Keyboard Manager** | 重映射按键与快捷键，无需第三方软件 | — |
| **Mouse Without Borders** | 用一套键鼠控制多台 Windows 电脑（局域网） | — |
| **Always on Top** | 将任意窗口置于所有窗口之上 | `Win + Ctrl + T` |
| **Awake** | 临时阻止电脑进入休眠，可设定时间 | 托盘菜单 |
| **File Locksmith** | 查找占用指定文件的进程并释放 | 右键菜单 |
| **Hosts File Editor** | 图形化编辑 `hosts` 文件 | — |
| **Workspaces** | 保存并一键恢复多窗口工作布局 | — |

## 常用快捷键速览

| 操作 | 快捷键 |
|------|--------|
| 启动 PowerToys Run | `Alt + Space` |
| 取色器 | `Win + Shift + C` |
| 文字识别 (OCR) | `Win + Shift + T` |
| 文件快速预览 | `Ctrl + Space`（文件资源管理器中选中文件后） |
| 窗口置顶 | `Win + Ctrl + T` |
| FancyZones 编辑布局 | `Win + Shift + \`` |

> 所有快捷键均可在 PowerToys 设置面板中自定义。

## 相关链接

- [PowerToys — GitHub](https://github.com/microsoft/PowerToys)
- [PowerToys — 官方文档](https://learn.microsoft.com/zh-cn/windows/powertoys/)
- [PowerToys — Microsoft Store](https://apps.microsoft.com/detail/xp89dcgq3k6vld)

---

### [回到 Windows/Optional](../README.md)
