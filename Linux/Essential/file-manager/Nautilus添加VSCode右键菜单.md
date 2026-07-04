# Nautilus 文件管理器右键菜单添加"用 VS Code 打开"

## 概述

本文档介绍如何在 Ubuntu 默认文件管理器 Nautilus（GNOME Files）的右键菜单中，添加一个**顶层菜单项**"用 VS Code 打开"，效果与系统自带的"在终端打开"一致——右键即可直接点击，无需进入"打开方式"子菜单。

实现原理与 [Nautilus Terminator 配置](../terminal/Ubuntu%20_Terminator_setting.md) 相同：都是基于 `nautilus-python` 编写一个 `Nautilus.MenuProvider` 扩展来接管右键菜单，本方案在此基础上做了简化（不依赖 GSettings，纯本地脚本，无需编译 Schema）。

## 效果说明

- 右键点击**一个或多个文件/文件夹** → 菜单中出现「用 VS Code 打开」，点击后用 `code` 命令打开所有选中项
- 在文件夹**空白处右键**（未选中任何项）→ 菜单中出现「在此文件夹中用 VS Code 打开」，点击后以当前文件夹为工作区打开 VS Code

## 前置条件

### 1. 安装 python3-nautilus

Nautilus 的右键菜单扩展基于 Python 编写，需要先安装 GObject Introspection 绑定：

```bash
sudo apt update
sudo apt install python3-nautilus
```

> 如果已经按照 [Terminator 终端配置指南](../terminal/Ubuntu%20_Terminator_setting.md) 装过 `nautilus-open-any-terminal`，这一步已完成，可跳过。

验证：

```bash
dpkg -l | grep python3-nautilus
```

### 2. 确认 code 命令可用

VS Code 通过官方 .deb / apt 源安装后会自动把 `code` 命令加入 PATH：

```bash
which code
```

应返回类似 `/usr/bin/code` 的路径。若无输出，说明 VS Code 未正确安装或未加入 PATH。

## 实现步骤

### 1. 创建扩展目录

```bash
mkdir -p ~/.local/share/nautilus-python/extensions
```

### 2. 编写扩展脚本

创建文件 `~/.local/share/nautilus-python/extensions/open_with_code.py`，内容如下：

<details>
<summary>点击展开 open_with_code.py 完整代码</summary>

```python
# -*- coding: UTF-8 -*-
"""Nautilus 右键菜单扩展：为文件/文件夹添加"用 VS Code 打开"选项。"""

from subprocess import Popen

from gi import require_version

try:
    require_version("Gtk", "4.0")
    require_version("Nautilus", "4.0")
except ValueError:
    require_version("Gtk", "3.0")
    require_version("Nautilus", "3.0")

from gi.repository import Gio, GObject, Nautilus  # noqa: E402

CODE_CMD = "code"


def _uri_to_path(uri):
    return Gio.File.new_for_uri(uri).get_path()


def _open_with_code(paths):
    paths = [p for p in paths if p]
    if paths:
        Popen([CODE_CMD] + paths)


class OpenWithCodeExtension(GObject.GObject, Nautilus.MenuProvider):
    def _menu_activate_cb(self, menu, files):
        _open_with_code([_uri_to_path(f.get_uri()) for f in files])

    def _menu_background_activate_cb(self, menu, file_):
        _open_with_code([_uri_to_path(file_.get_uri())])

    def get_file_items(self, *args):
        # `args` 在 Nautilus 4.0 API 中为 [files]
        # 在 Nautilus 3.0 API 中为 [window, files]
        files = args[-1]
        if not files:
            return []

        item = Nautilus.MenuItem(
            name="OpenWithCode::open_file_item",
            label="用 VS Code 打开",
            tip="使用 Visual Studio Code 打开选中的文件/文件夹",
        )
        item.connect("activate", self._menu_activate_cb, files)
        return [item]

    def get_background_items(self, *args):
        # `args` 在 Nautilus 4.0 API 中为 [folder]
        # 在 Nautilus 3.0 API 中为 [window, folder]
        file_ = args[-1]

        item = Nautilus.MenuItem(
            name="OpenWithCode::open_bg_item",
            label="在此文件夹中用 VS Code 打开",
            tip="使用 Visual Studio Code 打开当前文件夹",
        )
        item.connect("activate", self._menu_background_activate_cb, file_)
        return [item]
```

</details>

`get_file_items` / `get_background_items` 均使用 `*args` 接收参数，是为了同时兼容新旧两代 Nautilus 扩展接口：Ubuntu 20.04/22.04 自带的 Nautilus 3.x 传入 `(window, files)`，而较新发行版（Ubuntu 23.04+）的 Nautilus 4.x 只传入 `(files)`，取 `args[-1]` 即可兼容两种情况。

### 3. 重启文件管理器

```bash
nautilus -q
```

重新打开文件管理器，右键点击任意文件/文件夹，即可看到「用 VS Code 打开」菜单项。

**注意**：本方案基于 `nautilus-python`，仅对 Nautilus 有效。如果使用其他文件管理器（如 Nemo、Dolphin），需要使用对应文件管理器各自的插件机制，不能直接复用此脚本。

## 验证与常见问题

### 1. 验证是否生效

- 右键点击任意文件或文件夹，检查是否出现「用 VS Code 打开」
- 在文件夹空白处右键，检查是否出现「在此文件夹中用 VS Code 打开」
- 点击后应能正常拉起 VS Code 并打开对应路径

### 2. 菜单项没有出现

依次排查：

```bash
# 1. 检查脚本语法是否正确
python3 -c "compile(open('$HOME/.local/share/nautilus-python/extensions/open_with_code.py').read(), 'x', 'exec')"

# 2. 退出所有 nautilus 进程后，在终端以调试模式前台启动，观察报错输出
nautilus -q
NAUTILUS_PYTHON_DEBUG=misc nautilus --no-desktop
```

若终端输出 Python Traceback，说明扩展加载失败，可根据报错信息排查（常见原因是 GTK/Nautilus 绑定版本不匹配）。调试结束后按 `Ctrl-C` 退出，再正常运行一次 `nautilus -q` 即可让文件管理器恢复正常（桌面图标）模式。

### 3. 恢复默认设置（卸载）

删除扩展脚本即可：

```bash
rm -f ~/.local/share/nautilus-python/extensions/open_with_code.py
rm -rf ~/.local/share/nautilus-python/extensions/__pycache__
nautilus -q
```

## 注意事项

- 本方案不依赖 GSettings，纯本地脚本，删除文件即可完全卸载，不影响其他用户
- 多选文件/文件夹时会一并作为参数传给 `code` 命令，具体如何在窗口中排布由 VS Code 自身决定
- 实测环境：Ubuntu 20.04，Nautilus 3.36.3，`python3-nautilus` 1.2.3

**文档版本：v1.0**
**最后更新：2026-07-03**

---

### [回到 file-manager](README.md)
