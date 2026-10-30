<!-- software-count: 0 -->
# 目录 <!-- omit in toc -->

- [Nautilus 文件管理器右键菜单添加“用 VS Code 打开”](#nautilus-文件管理器右键菜单添加用-vs-code-打开)
  - [适用环境](#适用环境)
  - [前提条件](#前提条件)
  - [方式 A：使用现成开源扩展](#方式-a使用现成开源扩展)
  - [方式 B：手动创建扩展文件](#方式-b手动创建扩展文件)
  - [备选：使用 Nautilus Scripts](#备选使用-nautilus-scripts)
  - [验证](#验证)
  - [常见问题](#常见问题)
  - [回退方法](#回退方法)
  - [相关链接](#相关链接)

# Nautilus 文件管理器右键菜单添加“用 VS Code 打开”

在 Nautilus（GNOME Files）右键菜单的**顶层**增加一个“Open in VS Code”选项，支持右键单个文件、文件夹、多选项目以及文件夹空白处，效果与系统自带的“在终端打开”一致，无需进入“打开方式”子菜单。

## 适用环境

- 系统：Ubuntu 20.04 及以上。Ubuntu 24.04 搭载 Nautilus 46（GTK 4），需要 `gir1.2-nautilus-4.0`；安装 `python3-nautilus` 时会自动带上该依赖。
- 作用范围：当前用户，扩展文件位于 `~/.local/share/nautilus-python/extensions`。
- 核对日期：2026-10-30。依赖关系与扩展加载方式已核对；扩展代码未在 Ubuntu 24.04 上实测。

## 前提条件

### 1. 安装 python3-nautilus

Nautilus 的右键菜单扩展基于 Python 编写，需要先安装 GObject Introspection 绑定：

```bash
sudo apt update
sudo apt install python3-nautilus
```

### 2. 确认 `code` 命令可用

```bash
command -v code
```

应输出类似 `/usr/bin/code` 或 `/snap/bin/code`。如果没有输出，先在 VS Code 中执行命令面板里的 **“Install 'code' command in PATH”**，或确认 VS Code 已正确安装。

## 方式 A：使用现成开源扩展

```bash
wget -qO- https://raw.githubusercontent.com/harry-cpp/code-nautilus/master/install.sh | bash
```

安装后执行：

```bash
nautilus -q
```

重新打开文件管理器，右键即可看到 “Open in VS Code”。

## 方式 B：手动创建扩展文件

如果不想运行远程脚本，可以手动创建扩展。

### 1. 创建扩展目录

```bash
mkdir -p ~/.local/share/nautilus-python/extensions
```

### 2. 创建扩展文件

```bash
nano ~/.local/share/nautilus-python/extensions/open-in-vscode.py
```

写入以下内容：

```python
from gi.repository import Nautilus, GObject
import subprocess
import shutil

CODE = shutil.which("code") or "/usr/bin/code"


class OpenInVSCode(GObject.GObject, Nautilus.MenuProvider):
    def _paths(self, files):
        paths = []
        for f in files:
            if f.get_uri_scheme() != "file":
                continue
            path = f.get_location().get_path()
            if path:
                paths.append(path)
        return paths

    def _make_item(self, name, label, paths):
        item = Nautilus.MenuItem(name=name, label=label, tip=label)
        item.connect("activate", lambda *_: subprocess.Popen([CODE, "--"] + paths))
        return item

    def get_file_items(self, *args):
        files = args[-1]
        paths = self._paths(files)
        if not paths:
            return []
        if len(paths) == 1:
            label = "Open in VS Code"
        else:
            label = f"Open {len(paths)} items in VS Code"
        return [self._make_item("OpenInVSCode::FileItems", label, paths)]

    def get_background_items(self, *args):
        folder = args[-1]
        if folder.get_uri_scheme() != "file" or not folder.is_directory():
            return []
        path = folder.get_location().get_path()
        if not path:
            return []
        return [self._make_item("OpenInVSCode::Background", "Open in VS Code", [path])]
```

保存退出。

> 如果 `command -v code` 输出不是 `/usr/bin/code`，把文件里的 `CODE = ...` 改成你的实际路径，例如 `/snap/bin/code`。

### 3. 重启 Nautilus

```bash
nautilus -q
```

重新打开文件管理器即可。

## 备选：使用 Nautilus Scripts

如果不想安装 Python 扩展，也可以用 Nautilus 脚本。缺点是菜单项会出现在右键的 **“Scripts” 子菜单**里，而不是顶层；对空白处右键打开当前目录的支持也不如扩展自然。

### 1. 创建脚本目录

```bash
mkdir -p ~/.local/share/nautilus/scripts
```

### 2. 创建脚本

```bash
nano ~/.local/share/nautilus/scripts/OpenInVSCode.sh
```

内容：

```bash
#!/bin/bash
code -n ${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS}
```

赋予执行权限：

```bash
chmod +x ~/.local/share/nautilus/scripts/OpenInVSCode.sh
```

### 3. 重启 Nautilus

```bash
nautilus -q
```

之后右键选中的文件或文件夹 → **Scripts → OpenInVSCode.sh**。

## 验证

1. 重新打开 Nautilus。
2. 右键一个文件，应看到 **Open in VS Code**。
3. 右键一个文件夹，应看到 **Open in VS Code**。
4. 进入某个文件夹，在空白处右键，应看到 **Open in VS Code**，点击后 VS Code 打开当前目录。

已有的“在终端打开”选项应保持不变，两个菜单项可以同时存在。

## 常见问题

### 1. 右键没有出现 VS Code 菜单项

检查扩展文件是否存在：

```bash
ls ~/.local/share/nautilus-python/extensions/
```

应看到 `open-in-vscode.py`。然后再次执行：

```bash
nautilus -q
```

### 2. 点击菜单项没有反应

检查 `code` 路径：

```bash
command -v code
```

如果输出不是 `/usr/bin/code`，修改扩展文件中的 `CODE` 变量为实际路径。

### 3. 想看 Nautilus 扩展报错

先从终端退出 Nautilus：

```bash
nautilus -q
```

再从终端启动：

```bash
nautilus
```

观察终端输出，常见问题是 Python 导入失败或 `Nautilus.MenuProvider` 接口不匹配。

### 4. 如何撤销“在 VS Code 中打开”

删除扩展文件：

```bash
rm ~/.local/share/nautilus-python/extensions/open-in-vscode.py
nautilus -q
```

如果用的是现成扩展的安装脚本，删除对应生成的 `.py` 文件即可。不会影响终端右键配置。

## 回退方法

- 方式 B：删除 `~/.local/share/nautilus-python/extensions/open-in-vscode.py` 后执行 `nautilus -q`。
- 方式 A：删除安装脚本生成的扩展文件（通常在 `~/.local/share/nautilus-python/extensions/` 下），再执行 `nautilus -q`。
- 备选方案：删除 `~/.local/share/nautilus/scripts/OpenInVSCode.sh` 即可。

## 相关链接

- [harry-cpp/code-nautilus](https://github.com/harry-cpp/code-nautilus)
- [Ubuntu 24.04 上配置 Terminator 右键菜单](../terminal/Ubuntu%20_Terminator_setting-v2.0.md)

最后更新：2026-10-30

---

### [回到 file-manager](README.md)
