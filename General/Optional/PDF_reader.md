# 目录 <!-- omit in toc -->
- [Poppler / pdftoppm](#poppler--pdftoppm)
  - [安装](#安装)
    - [Linux](#linux)
    - [macOS](#macos)
    - [Windows](#windows)
  - [使用](#使用)
  - [相关链接](#相关链接)

# Poppler / pdftoppm

Poppler 是一个开源的 PDF 渲染库（基于 Xpdf），提供 C++ API 用于解析和渲染 PDF 文件。其中 `pdftoppm` 是其附带的命令行工具，可将 PDF 页面转换为 PPM、PNG 或 JPEG 格式的图像，在 AI 工作流中常用于将 PDF 文档转换为图片供视觉模型分析。

## 安装

### Linux

```bash
# Debian / Ubuntu
sudo apt update
sudo apt install poppler-utils -y
```

### macOS

```bash
brew install poppler
```

### Windows

从 [Poppler 官网](https://poppler.freedesktop.org/) 下载预编译的二进制包，解压后将 `bin/` 目录加入系统 PATH。

## 使用

```bash
# 将 PDF 所有页面转为 PNG（每页一个文件）
pdftoppm -png input.pdf output_prefix

# 将 PDF 所有页面转为 JPEG，指定分辨率 300 DPI
pdftoppm -jpeg -r 300 input.pdf output_prefix

# 仅转换第一页（-f 1 -l 1）
pdftoppm -png -f 1 -l 1 input.pdf output_prefix

# 单页转为单张图片（不按页拆分）
pdftoppm -png -singlefile input.pdf output_name
```

## 相关链接

- [Poppler 官网](https://poppler.freedesktop.org/)
- [Poppler 文档](https://manpages.debian.org/stable/poppler-utils/pdftoppm.1.en.html)

---

### [回到 General/Optional](README.md)
