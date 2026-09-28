<!-- software-count: 1 -->
# <img src="../../../.media/png/Shutter-Encoder.png" width="60" height="60" alt="Shutter Encoder 图标"> Shutter Encoder

## 软件简介

Shutter Encoder 是面向音视频制作的免费转换工具，使用 FFmpeg 处理媒体文件。除格式转换外，还可用于压缩、裁切、提取音轨、重新封装和处理字幕。

本文依据[官方网站](https://www.shutterencoder.com/)与[官方文档](https://www.shutterencoder.com/documentation/)整理，核对日期：2026-09-28。

## 安装方法

在[官方下载区](https://www.shutterencoder.com/)选择对应平台的包：

- **Windows**：提供安装版 `.exe` 和便携版 `.zip`；完整解压便携版后再运行。
- **macOS**：分别提供 Intel 与 Apple Silicon 版本。
- **Linux**：提供 `.deb` 和 `.AppImage`。选择与发行版、处理器架构相符的包，并参考官网的当前说明。

官网列出的平台要求以下载时的版本为准。

## 功能特点

- **格式转换与压缩**：将音频或视频转换为所需编码和容器，并调整输出设置。
- **音频处理**：从视频导出 WAV 等音频文件，或转换常见音频格式。
- **不重新编码的操作**：在条件允许时裁切、提取或重新封装媒体流；具体限制取决于源文件和目标容器。
- **字幕处理**：编辑、嵌入或烧录字幕；输出方式需按交付需求选择。
- **队列与预设**：批量添加任务，保存常用设置。

## 使用方法

以从视频导出 WAV 为例：

1. 把视频文件拖入文件列表，确认选中的源文件和音轨。
2. 在功能列表中选择 `WAV`，按用途设置采样率、声道等参数。
3. 检查输出目录，点击 `Start function` 开始处理。
4. 完成后核对音频时长，并试听开头、中间和结尾。

若使用“无需转换”类功能，先确认输出容器支持源编码；裁切高度压缩的视频时，切点可能落在相邻关键帧。以上操作入口和选项以当前版本界面为准。

## 官方文档与相关链接

- [官方网站与下载](https://www.shutterencoder.com/)
- [功能文档](https://www.shutterencoder.com/documentation/)
- [源代码](https://github.com/paulpacifico/shutter-encoder)

---

### [回到音视频软件索引](README.md)
