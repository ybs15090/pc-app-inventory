# 目录 <!-- omit in toc -->
- [Poppler/pdftoppm](#popplerpdftoppm)
  - [安装](#安装)
  - [使用](#使用)


# Poppler/pdftoppm
Poppler 是一个 PDF 渲染库，基于 Xpdf-3.0 版本开发。它提供了一个 C++ API，可以用于解析和渲染 PDF 文件。
pdftoppm 是Poppler 提供的一个命令行工具, 用于将 PDF 文件转换为 PPM、PNG 或 JPEG 格式的图像。它支持多页 PDF 文件，可以指定输出图像的分辨率和质量。
## 安装
在 Linux 系统上，可以使用包管理器安装 Poppler 和 pdftoppm。例如，在 Debian/Ubuntu 上，可以运行以下命令：

```bash
sudo apt-get update
sudo apt-get install poppler-utils
```
在 macOS 上，可以使用 Homebrew 安装：

```bash
brew install poppler
```
在 Windows 上，可以从 Poppler 的官方网站下载预编译的二进制文件，并将其添加到系统路径中。

## 使用
可查阅官方文档：https://poppler.freedesktop.org/
- 一些 AI 助手可以使用 pdftoppm 将 PDF 文件转换为图像格式，以便进行进一步的处理和分析。例如，将 PDF 文件转换为 PNG 图像：

