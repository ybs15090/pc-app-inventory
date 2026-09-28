<!-- software-count: 1 -->
# <img src="../../../.media/png/MKVToolNix.png" width="60" height="60" alt="MKVToolNix 图标"> MKVToolNix

## 软件简介

MKVToolNix 是一组创建、修改和检查 Matroska（MKV）文件的工具。常用的 MKVToolNix GUI 可以把视频、音频和字幕轨封装进一个 MKV 文件，也能调整轨道语言、名称和标记。

本文依据[官方网站](https://mkvtoolnix.download/)、[下载页](https://mkvtoolnix.download/downloads.html)和[官方文档](https://mkvtoolnix.download/docs.html)整理，核对日期：2026-09-28。

## 安装方法

从[官方下载页](https://mkvtoolnix.download/downloads.html)选择对应系统的包：

- **Windows**：提供安装包和便携压缩包；当前下载页要求 Windows 10 / Windows Server 2016 或更新版本。
- **macOS**：当前提供适用于 macOS 13 或更新版本的 DMG。下载页也列出 MacPorts 和 Homebrew 途径；Homebrew 的 `mkvtoolnix` formula 仅含命令行工具，`mkvtoolnix-app` cask 才提供 GUI。
- **Linux**：按发行版使用下载页列出的软件包或仓库。官方当前为 Ubuntu 24.04、26.04 提供新版本仓库；Ubuntu 20.04 的官方仓库只保留至 v81.0，不能照搬新版仓库配置。

安装后启动 **MKVToolNix GUI**；命令行处理可使用 `mkvmerge` 等组件。

## 功能特点

- **混流封装**：从多个源文件选择视频、音频、字幕等轨道，生成 MKV。
- **轨道属性**：设置字幕或音轨的语言、名称、默认轨道标记等元数据。
- **查看与提取**：检查容器内容，提取已有轨道；另有章节和头部编辑功能。

只添加字幕轨通常属于重新封装，不需要重新编码原视频和音频。MKVToolNix 不负责把对白识别为文字，也不会自动翻译字幕；若需要永久烧录到画面，应使用支持视频重新编码的工具。

## 使用方法

以把已校对的 SRT 字幕封装进原视频为例：

1. 在 MKVToolNix GUI 的混流器中添加原视频，再添加 SRT 字幕文件。
2. 在轨道列表中保留需要的视频和音频轨，选中字幕轨并设置语言、名称；按需要设置默认轨道标记，普通完整字幕不要误设为强制显示。
3. 指定新的 `.mkv` 输出路径，开始混流，保留原始文件。
4. 用播放器抽查字幕是否可切换、中文是否正常显示，以及开头、中段、结尾是否同步。

默认轨道标记会参与播放器的轨道选择，实际自动显示行为还受播放器语言偏好影响。输入字幕建议采用 UTF-8 编码，并在封装前完成文本和时间轴校对。

## 官方文档与相关链接

- [官方网站与下载](https://mkvtoolnix.download/downloads.html)
- [MKVToolNix GUI 文档](https://mkvtoolnix.download/doc/mkvtoolnix-gui.html)
- [mkvmerge 文档](https://mkvtoolnix.download/doc/mkvmerge.html)

---

### [回到音视频软件索引](README.md)
