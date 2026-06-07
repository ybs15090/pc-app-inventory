# 目录 <!-- omit in toc -->
- [ripgrep (rg)](#ripgrep-rg)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [快速入门](#快速入门)
  - [常用场景](#常用场景)
  - [相关链接](#相关链接)

# ripgrep (rg)

ripgrep（命令名 `rg`）是一款基于 Rust 语言开发的跨平台文本搜索工具，支持 Linux、macOS 和 Windows 系统。它以行为单位进行搜索，能够递归遍历目录，并默认遵循 `.gitignore` 规则自动忽略不应搜索的文件（如隐藏文件、二进制文件、`node_modules/` 等），搜索速度显著优于传统的 `grep`。

官网：[https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

## 安装

### Windows

使用包管理器安装：

```bash
# winget
winget install BurntSushi.ripgrep.MSVC

# Scoop
scoop install ripgrep

# Chocolatey
choco install ripgrep
```

也可从 [GitHub Releases](https://github.com/BurntSushi/ripgrep/releases) 下载预编译的 `.msi` 安装包或独立二进制文件。

### macOS

```bash
# Homebrew
brew install ripgrep

# MacPorts
sudo port install ripgrep
```

### Linux

```bash
# Debian / Ubuntu（建议使用较新版本以获得更好的性能）
sudo apt update
sudo apt install ripgrep

# Fedora / RHEL
sudo dnf install ripgrep

# Arch Linux
sudo pacman -S ripgrep
```

部分发行版的官方源中 ripgrep 版本可能较旧，可从 [GitHub Releases](https://github.com/BurntSushi/ripgrep/releases) 下载静态链接的二进制文件或 `.deb`/`.rpm` 包安装最新版本。

## 快速入门

```bash
# 在当前目录递归搜索关键字
rg "pattern"

# 在指定目录中搜索
rg "pattern" /path/to/dir

# 搜索指定类型的文件
rg -t py "pattern"       # 仅搜索 Python 文件
rg -t md -t txt "pattern" # 搜索 Markdown 和文本文件

# 排除指定文件类型
rg -T py "pattern"        # 跳过 Python 文件

# 仅列出包含匹配内容的文件名
rg -l "pattern"

# 显示匹配行及其前后各 3 行上下文
rg -C 3 "pattern"

# 统计每个文件中的匹配次数
rg -c "pattern"

# 大小写不敏感搜索
rg -i "pattern"

# 全字匹配
rg -w "word"

# 使用正则表达式
rg "\d{4}-\d{2}-\d{2}"    # 搜索日期格式

# 替换（输出到 stdout，不修改文件）
rg "old" -r "new" path/

# 不忽略 .gitignore 中指定的文件
rg -u "pattern"            # 忽略 .gitignore，仍忽略隐藏文件和二进制文件
rg -uu "pattern"           # 仅忽略二进制文件
rg -uuu "pattern"          # 搜索所有文件，不做任何过滤
```

## 常用场景

| 场景 | 命令 |
|------|------|
| 搜索代码中的 TODO 注释 | `rg "TODO\|FIXME\|HACK"` |
| 查找使用了某个函数的文件 | `rg "function_name\("` |
| 在项目中查找特定字符串 | `rg -l "deprecated" src/` |
| 排除多个目录 | `rg "pattern" -g '!build/' -g '!dist/'` |
| 仅搜索文件名匹配模式的文件 | `rg "pattern" -g "*.go"` |
| 显示不带颜色的纯文本输出 | `rg --color never "pattern"` |

## 相关链接

- [GitHub 仓库](https://github.com/BurntSushi/ripgrep)
- [GitHub Releases（下载页面）](https://github.com/BurntSushi/ripgrep/releases)
- [ripgrep 使用指南（官方指南）](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)


---

### [回到 file-search](README.md)
