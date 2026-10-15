<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [ HandBrake](#-handbrake)
  - [软件简介](#软件简介)
  - [安装方法](#安装方法)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
      - [Flathub](#flathub)
      - [本地 Flatpak 安装包](#本地-flatpak-安装包)
  - [功能特点](#功能特点)
  - [使用方法](#使用方法)
    - [转为 MP4 视频](#转为-mp4-视频)
    - [调整画质与体积](#调整画质与体积)
    - [处理音轨与字幕](#处理音轨与字幕)
    - [批量转码](#批量转码)
  - [常见问题与使用边界](#常见问题与使用边界)
  - [官方文档与相关链接](#官方文档与相关链接)
    - [回到音视频软件索引](#回到音视频软件索引)

# <img src="../../../.media/png/HandBrake.png" width="60" height="60" alt="HandBrake 图标"> HandBrake

## 软件简介

HandBrake 是免费开源的跨平台视频转码工具，可将多种来源的视频转换为 MP4、MKV 或 WebM，用于压缩体积、调整分辨率、适配播放设备，以及批量处理视频。

软件支持 Windows、macOS 和 Linux，提供图形界面与独立的 HandBrakeCLI 命令行工具。常见用途包括压缩录屏和课程视频、转换手机或相机素材，以及为电视、平板等设备制作合适的播放版本。

HandBrake 导出时会重新编码视频，部分音频格式可在条件允许时直接保留。需要保留原有音视频编码、仅封装字幕或调整 MKV 轨道时，可参考 [MKVToolNix](MKVToolNix.md)；更多音视频转换与处理任务可参考 [Shutter Encoder](Shutter-Encoder.md)。功能范围见[官方介绍](https://handbrake.fr/docs/en/latest/introduction/about.html)。

资料核对日期：2026-10-15。核对时[官网下载页](https://handbrake.fr/downloads.php)列出的正式版本为 **1.11.2**。验证范围：官网、官方文档、发行说明及包管理器清单核对；未在本机安装、启动或进行视频转码测试。

## 安装方法

统一入口：[官网下载页](https://handbrake.fr/downloads.php) / [GitHub 正式发行版](https://github.com/HandBrake/HandBrake/releases/latest)。下载时区分图形界面版与 HandBrakeCLI，并选择对应系统和处理器架构的发行包。

### Windows

已安装 WinGet 时，可在 PowerShell 或终端执行：

```powershell
winget install --exact --id HandBrake.HandBrake
```

包标识、架构与依赖见 [WinGet 软件清单](https://github.com/microsoft/winget-pkgs/tree/master/manifests/h/HandBrake/HandBrake)。

也可从官网下载 `.exe` 安装包并按向导安装；便携使用时，下载 `.zip`，完整解压后启动 `HandBrake.exe`。官方分别提供 **x64** 和 **ARM64** 版本，按电脑的处理器架构选择。

核对时，Windows 图形界面版依赖 **Microsoft .NET Desktop Runtime 10.0.x**。若启动时提示缺少运行环境，从 [Microsoft .NET 10 下载页](https://dotnet.microsoft.com/en-us/download/dotnet/10.0)选择与程序架构对应的 **.NET Desktop Runtime**。该依赖见 [1.11.2 发行说明](https://github.com/HandBrake/HandBrake/releases/tag/1.11.2)。

官方下载页列出 Windows 10 及更新版本；当前[系统支持表](https://handbrake.fr/docs/en/latest/technical/system-requirements.html)将 Windows 11 列为受支持，Windows 10 列为已弃用（Deprecated），并注明需 1909 或更新版本。系统支持等级、CPU 与内存要求以所选版本的官方说明为准。

### macOS

已安装 Homebrew 时：

```bash
brew install --cask handbrake-app
```

图形界面版的包名见 [Homebrew HandBrake 页面](https://formulae.brew.sh/cask/handbrake-app)。需要 HandBrakeCLI 时，可查看单独的 [Homebrew 命令行版页面](https://formulae.brew.sh/formula/handbrake)。

也可从官网下载 `.dmg`，打开后将 `HandBrake.app` 拖入“应用程序”文件夹。官方提供兼容 Intel 与 Apple Silicon 的 Universal 版本。

下载页标注最低为 macOS 10.13，但当前[系统支持表](https://handbrake.fr/docs/en/latest/technical/system-requirements.html)对旧版 macOS 的支持等级另有区分；旧系统用户应结合该表选择版本。

### Linux

#### Flathub

官方提供 Flatpak，可通过 [Flathub](https://flathub.org/en/apps/fr.handbrake.ghb)安装并更新。已安装 Flatpak 且配置好 Flathub 软件源时：

```bash
flatpak install flathub fr.handbrake.ghb
flatpak run fr.handbrake.ghb
```

安装方法及应用标识见[官方安装文档](https://handbrake.fr/docs/en/latest/get-handbrake/download-and-install.html)。首次使用可先按 [Flathub 的发行版设置说明](https://flathub.org/en/setup)配置环境。

#### 本地 Flatpak 安装包

从官网下载页或 GitHub Releases 下载 `.flatpak` 后，在下载目录执行。以下以核对时的 x86-64 图形界面包为例：

```bash
flatpak --user install ./HandBrake-1.11.2-x86_64.flatpak
flatpak run fr.handbrake.ghb
```

版本更新后，将文件名替换为实际下载的名称。安装需要系统已提供 Flatpak，以及能够获取对应运行时；本地包的安装方法见[官方 Flatpak Bundles 说明](https://handbrake.fr/docs/en/latest/get-handbrake/download-and-install.html#flatpak-bundles)。官网下载页的 Linux 二进制渠道为 Flatpak；发行版仓库中的 `.deb`、`.rpm` 软件包由各发行版维护，版本与功能应另行核对。

**Ubuntu 20.04 兼容性：** 当前[官方系统要求](https://handbrake.fr/docs/en/latest/technical/system-requirements.html)将 Ubuntu 20.04 列为不支持，表中最后兼容版本为 **1.9.2**。本文未实测 Ubuntu 20.04 上的安装或运行，使用旧系统前应先核对对应版本与 Flatpak 运行时的兼容性。

## 功能特点

| 功能 | 用途或限制 |
|---|---|
| 视频转码 | 将来源视频编码为 H.264、H.265、AV1 等格式，并输出到 MP4、MKV 或 WebM；可选组合受编码器与容器限制。 |
| 设备与通用预设 | 快速载入一组视频、音频和容器设置，再按播放设备或交付要求调整。 |
| 质量与码率控制 | 使用恒定质量或平均码率控制输出，在画质与体积之间取舍。 |
| 画面与滤镜 | 调整分辨率、裁剪边缘、处理隔行扫描和降噪等；先预览再确认处理效果。 |
| 音轨处理 | 选择语言与声道、转码音频；符合条件的音频可使用 Passthru 直通。 |
| 字幕处理 | 选择源文件字幕或导入 SRT，按字幕格式和容器选择保留字幕轨或烧录字幕。 |
| 批量队列 | 为不同源文件设置输出参数，加入队列后连续编码。 |
| 硬件编码 | 可使用受支持的 Intel QSV、NVIDIA NVENC、AMD 或 Apple VideoToolbox 编码器；具体选项取决于硬件、驱动、系统及发行包。 |

功能依据：[官方功能列表](https://handbrake.fr/features.php)与[官方文档](https://handbrake.fr/docs/)。

## 使用方法

### 转为 MP4 视频

以下以普通视频转为 H.264 + AAC 的 MP4 为入门示例：

1. 打开 HandBrake，点击 **Open Source（打开源文件）**，或把视频拖入主窗口；多标题来源需确认选中的 `Title`。
2. 选择通用预设，例如 **Fast 1080p30**。检查该预设的分辨率和帧率是否符合需求；需要保留 60 fps 等源特性时，调整相应设置并预览。
3. 在 **Summary（摘要）**中确认容器为 **MP4**，在 **Video（视频）**中确认视频编码器为 **H.264 (x264)**，在 **Audio（音频）**中检查所需音轨与 AAC 编码设置。
4. 在 **Dimensions（尺寸）**中检查输出尺寸与裁剪范围，在 **Subtitles（字幕）**中确认需要的字幕及烧录选项。
5. 设置输出目录与文件名，例如 `课程录屏-压缩.mp4`，使用与源文件不同的路径或名称，保留原件。
6. 先用 **Preview（预览）**生成短片检查画面、声音和字幕，再点击 **Start Encode / Start（开始编码）**处理完整视频。
7. 完成后在输出目录查看文件，核对时长、分辨率、音轨和字幕，并抽查开头、中间及结尾。

基础流程见[官方快速入门](https://handbrake.fr/docs/en/latest/introduction/quick-start.html)。各平台菜单名称可能略有差异。

### 调整画质与体积

首次使用可从预设默认的 **Constant Quality（恒定质量）**开始。以下是 x264、x265 常用 RF 设置的理解方式：

| 设置 | 影响 |
|---|---|
| 降低 RF | 提高目标质量，通常增加输出体积。 |
| 提高 RF | 降低目标质量，通常减小输出体积。 |
| 调整 Encoder Preset | 改变编码速度与压缩效率的取舍；与整套视频预设是两个不同层级的设置。 |
| 降低输出分辨率 | 减少画面细节与编码工作量，适合观看需求较低的副本。 |

官方对 **1080p 的 x264、x265**给出的 RF 参考范围为 **20–24**。例如，可先用 x264、RF 22 编码短片，再根据实际观看效果微调。RF 数值不能直接用于比较不同编码器的画质，部分硬件编码器的质量刻度方向也不同，详见[官方质量调整说明](https://handbrake.fr/docs/en/latest/workflow/adjust-quality.html)。

恒定质量模式下，最终体积随素材复杂程度变化。编码速度、画质和体积的关系见[官方性能说明](https://handbrake.fr/docs/en/latest/technical/performance.html)；需要控制目标体积时，可评估平均码率模式，并预留音轨等内容所占的空间。

### 处理音轨与字幕

- **音轨**：保留所需语言与声道。选择 `Passthru` 时，应确认源音频格式和目标容器均支持；转为 AAC 等格式时会重新编码音频。
- **可切换字幕**：保留为独立字幕轨时，播放器可按需开关；支持范围取决于字幕类型、容器和播放器。
- **烧录字幕（Burn In）**：将字幕写入视频画面，播放时始终显示，导出后无法作为独立字幕轨关闭。
- **外部字幕**：导入 SRT 后，先预览中文字幕显示与时间同步，再确认输出容器和烧录选项。

具体支持组合见[官方字幕说明](https://handbrake.fr/docs/en/latest/advanced/subtitles.html)。仅需把字幕封装进 MKV 并保留原视频编码时，可使用 [MKVToolNix](MKVToolNix.md)。

### 批量转码

1. 打开一个源文件，确认标题、预设、音轨、字幕及输出位置。
2. 点击 **Add to Queue（加入队列）**，保存该任务的参数。
3. 继续添加其他文件，检查各任务的输出文件名，避免多个任务使用同一路径。
4. 打开队列列表复核任务，再启动队列；完成后检查任务状态与输出文件。

操作说明见[官方队列文档](https://handbrake.fr/docs/en/latest/advanced/queue.html)。

## 常见问题与使用边界

| 问题 | 说明或处理方法 |
|---|---|
| 转码后文件反而更大 | 检查质量、码率、分辨率和音轨设置。对已经充分压缩的视频再次转码，不能保证继续缩小；先用短片测试。 |
| Windows 启动提示缺少 .NET | 按当前版本要求安装架构匹配的 .NET Desktop Runtime；核对时 1.11.2 使用 10.0.x。 |
| 找不到硬件编码器 | 核对 GPU 支持、驱动、系统及发行包，查看对应编码器的官方要求；拥有独立显卡不代表所有编码格式均受支持。 |
| 字幕无法关闭 | 检查是否勾选了 Burn In。需要可切换字幕时，选择支持字幕轨的格式与容器，并重新从源文件导出。 |
| 只想更换容器或加入字幕 | HandBrake 会重新编码视频；保留原编码封装到 MKV 可参考 [MKVToolNix](MKVToolNix.md)。 |
| 需要拼接多个片段或时间线剪辑 | 可先用 [Premiere Pro](Adobe-Premiere-Pro.md)等剪辑工具完成编辑；HandBrake 主要用于后续转码。 |
| 来源视频无法打开 | 先核对来源格式和文件完整性，再查看 Activity Log；官方说明 HandBrake 不处理带 DRM 或复制保护的来源。 |

功能边界见[官方介绍](https://handbrake.fr/docs/en/latest/introduction/about.html)，排查时可参考[官方帮助文档](https://handbrake.fr/docs/)。

## 官方文档与相关链接

- [HandBrake 官网](https://handbrake.fr/)
- [官网下载页](https://handbrake.fr/downloads.php)
- [GitHub 源码仓库](https://github.com/HandBrake/HandBrake)
- [最新正式发行版](https://github.com/HandBrake/HandBrake/releases/latest)
- [官方文档](https://handbrake.fr/docs/)
- [官方系统要求](https://handbrake.fr/docs/en/latest/technical/system-requirements.html)
- [官方质量调整说明](https://handbrake.fr/docs/en/latest/workflow/adjust-quality.html)
- [官方字幕说明](https://handbrake.fr/docs/en/latest/advanced/subtitles.html)

---

### [回到音视频软件索引](README.md)
