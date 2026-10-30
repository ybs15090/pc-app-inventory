<!-- software-count: 0 -->
# 目录 <!-- omit in toc -->

- [Ubuntu 24.04 上配置 Terminator 右键菜单](#ubuntu-2404-上配置-terminator-右键菜单)
  - [适用环境](#适用环境)
  - [初版文档在 24.04 上的问题](#初版文档在-2404-上的问题)
  - [沿用 pip 流程：补装依赖](#沿用-pip-流程补装依赖)
  - [推荐方案：使用 .deb 包](#推荐方案使用-deb-包)
  - [彻底替换系统自带的“在终端打开”](#彻底替换系统自带的在终端打开)
  - [在 VS Code 中打开（可选）](#在-vs-code-中打开可选)
  - [回退方法](#回退方法)
  - [相关链接](#相关链接)

# Ubuntu 24.04 上配置 Terminator 右键菜单

[初版文档](Ubuntu%20_Terminator_setting.md)中的方法在 Ubuntu 24.04 上**核心思路是适用的，但需要一处关键补充**。同时，存在比文档中“pip 安装 + 手动编译 Schema”更简单的 **`.deb` 包安装法**。

## 适用环境

- 系统：Ubuntu 24.04（Nautilus 46，GTK 4）；初版文档以 Ubuntu 20.04 为主。
- 作用范围：当前用户的 Nautilus 右键菜单。
- 核对日期：2026-10-30。依赖关系与 `.deb` 文件名依据 Ubuntu 24.04 官方软件包和 GitHub Releases 核对，未在全新 24.04 上完整实测。

## 初版文档在 24.04 上的问题

文档通过 `nautilus-open-any-terminal` 扩展来接管右键菜单，这是解决 Ubuntu 24.04 下 Nautilus 右键“在终端打开”硬编码问题的正确方向。Ubuntu 24.04 搭载的 Nautilus 46 使用 GTK 4，而官方 `.deb` 包最初缺少 GTK 4 的内省数据依赖，导致直接安装会失败。

文档中的方法使用 `pip` 安装，并包含了 `gir1.2-gtk-4.0`，但**遗漏了另一个关键依赖 `gir1.2-nautilus-4.0`**。这是 Nautilus 4.0 扩展接口的 GObject 内省数据，缺少它同样可能导致扩展无法正常工作。

## 沿用 pip 流程：补装依赖

如果沿用初版文档的 pip 流程，只需在依赖安装步骤中补上它：

```bash
sudo apt install python3-nautilus python3-pip gir1.2-gtk-4.0 gir1.2-nautilus-4.0
```

后续的 `pip install --break-system-packages` 和 `gsettings` 配置步骤可以继续沿用。

## 推荐方案：使用 `.deb` 包

**直接下载 `.deb` 包安装是更理想的选择**，因为它可以自动处理扩展文件的部署和 Schema 注册，省去手动编译的步骤。

**步骤 1：安装缺失的依赖**

这是让 `.deb` 包能在 Ubuntu 24.04 上顺利安装的关键。

```bash
sudo apt update
sudo apt install python3-nautilus gir1.2-gtk-4.0 gir1.2-nautilus-4.0
# sudo apt install -s python3-nautilus gir1.2-gtk-4.0 gir1.2-nautilus-4.0 #模拟安装
```

**步骤 2：下载并安装 `.deb` 包**

前往 `nautilus-open-any-terminal` 的 [GitHub Releases](https://github.com/Stunkymonkey/nautilus-open-any-terminal) 页面，下载最新的 `.deb` 文件（文件名类似 `nautilus-extension-any-terminal_x.x.x-x_all.deb`），然后用 `apt` 安装：

```bash
sudo apt install ./下载的包名.deb
```

执行后，扩展会自动部署，无需再手动运行 `glib-compile-schemas`。

**步骤 3：将右键菜单指向 Terminator**

```bash
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal terminator
```

**步骤 4：重启 Nautilus**

```bash
nautilus -q
```

重新打开文件管理器，右键菜单就会调用 Terminator 了。

## 彻底替换系统自带的“在终端打开”

文档的方法是“增加”一个打开 Terminator 的右键选项。如果你希望**彻底替换**掉系统自带的“在终端打开”（它仍然指向 GNOME Terminal），可以额外执行：

```bash
sudo apt remove nautilus-extension-gnome-terminal
```

这样可以避免右键菜单中出现两个相似的选项。

## 在 VS Code 中打开（可选）

本专题只处理终端右键菜单。如果还需要在右键菜单中用 VS Code 打开文件或目录，见 [Nautilus 文件管理器右键菜单添加“用 VS Code 打开”](../file-manager/Nautilus添加VSCode右键菜单.md)。两个扩展互不冲突，可以同时安装。

## 回退方法

- 若执行过“彻底替换”步骤，先恢复系统插件：`sudo apt install nautilus-extension-gnome-terminal`。
- 卸载扩展：`.deb` 安装的使用 `sudo apt remove nautilus-extension-any-terminal`；`pip` 安装的使用 `python3 -m pip uninstall nautilus-open-any-terminal --break-system-packages`。
- 可选：重置扩展配置项 `gsettings reset com.github.stunkymonkey.nautilus-open-any-terminal terminal`。
- 每次改动后执行 `nautilus -q`，让文件管理器重新加载扩展。

## 相关链接

- [nautilus-open-any-terminal（GitHub）](https://github.com/Stunkymonkey/nautilus-open-any-terminal)
- [初版文档：Ubuntu Terminator 终端配置指南](Ubuntu%20_Terminator_setting.md)
- [Nautilus 文件管理器右键菜单添加“用 VS Code 打开”](../file-manager/Nautilus添加VSCode右键菜单.md)

---

### [回到 terminal](README.md)
