<!-- software-count: 1 -->
# <img src="../../../.media/svg/video-x-generic.svg" width="60" height="60" alt="视频字幕工具图标"> Subtitle Edit

## 软件简介

Subtitle Edit 是免费开源的视频字幕编辑器，可用于制作字幕、修改文本、校准时间轴和转换字幕格式。

Subtitle Edit 5 提供 Windows、Linux 和 macOS 跨平台版本，适合视频字幕校对、课程录音转字幕和字幕翻译等场景。本文按 [官方跨平台文档](https://subtitleedit.github.io/subtitleedit/) 整理，核对日期：2026-09-27。

## 安装方法

统一从 [GitHub Releases](https://github.com/SubtitleEdit/subtitleedit/releases) 下载对应系统和处理器架构的发行包。日常使用优先选择正式版，注意区分标有 `Pre-release` 的测试版。

### Windows

1. 下载 Windows 安装包，按向导完成安装；如选择便携包，先完整解压再启动程序。
2. 当前官方要求 Windows 10 22H2（内部版本 19045）或更新版本。

### macOS

1. 下载适合 Intel 或 Apple Silicon 的 `.dmg` 文件并打开。
2. 将 `Subtitle Edit.app` 拖入“应用程序”文件夹，再从该文件夹启动。

官方最低要求 macOS 12，推荐 macOS 14 或更新版本；当前 `.dmg` 已包含视频播放和音视频处理所需的 libmpv、FFmpeg。

### Linux

官方提供 Flatpak 包，可从 Releases 下载。系统已安装 Flatpak 时，在下载目录执行以下命令（文件名以实际下载包为准）：

```bash
flatpak install ./SubtitleEdit-linux-x64.flatpak
flatpak run dk.nikse.subtitleedit
```

Flatpak 包包含 mpv、FFmpeg 依赖。如选择原生发行包，Debian / Ubuntu 可按官方说明补充视频功能依赖：

```bash
sudo apt update
sudo apt install mpv libmpv-dev ffmpeg
```

以上依赖命令不包含 Subtitle Edit 主程序的安装。各发行包的系统要求以对应版本说明为准，本文未实测 Ubuntu 20.04 兼容性。

安装与平台要求参见 [官方 README](https://github.com/SubtitleEdit/subtitleedit#readme)。

## 功能特点

- **字幕编辑与转换**：编辑字幕文本、拆分或合并字幕，处理 SRT、ASS/SSA、WebVTT 等格式。
- **时间轴同步**：结合视频预览、音频波形和频谱调整字幕起止时间，支持整体偏移与参考点同步。
- **语音转字幕**：通过 Whisper 等本地或云端语音识别引擎生成字幕初稿。
- **OCR 识别**：将蓝光、DVD 等图像字幕转换为可编辑文本。
- **字幕校对与翻译**：检查常见错误、拼写和显示时长，并可调用翻译服务。
- **批量处理**：批量转换字幕文件。

功能概览参见 [官方 Overview](https://subtitleedit.github.io/subtitleedit/overview.html)。

## 使用方法

### 编辑已有字幕

1. 通过 `File → Open` 打开字幕，再通过 `Video → Open video` 加载对应视频。
2. 在字幕列表中选中条目，修改文字、开始时间和结束时间。
3. 播放对应片段，结合音频波形检查字幕与声音是否一致。
4. 保存为所需字幕格式；建议另存一份，便于保留原始字幕。

### 修正字幕不同步

- **全片偏差基本固定**：使用 `Adjust All Times` 整体提前或延后字幕。
- **越往后偏差越大**：使用 `Visual Sync` 或 `Point Sync` 结合参考位置校准，并检查片源是否一致。

### 从音视频生成字幕

通过 `Video → Speech to text` 选择识别引擎与语言，按提示准备所需模型或服务配置，生成字幕后逐条校对人名、术语、标点和时间轴。自动识别结果应作为初稿使用。

菜单名称以实际版本及界面语言为准。时间轴与语音识别功能入口见 [官方文档目录](https://subtitleedit.github.io/subtitleedit/)。

## 官方文档与相关链接

- [官方文档](https://subtitleedit.github.io/subtitleedit/)
- [GitHub 源码仓库](https://github.com/SubtitleEdit/subtitleedit)
- [发行版下载](https://github.com/SubtitleEdit/subtitleedit/releases)
- [功能概览与入门](https://subtitleedit.github.io/subtitleedit/overview.html)
- [问题反馈](https://github.com/SubtitleEdit/subtitleedit/issues)

---

### [回到 Video 目录](README.md)
