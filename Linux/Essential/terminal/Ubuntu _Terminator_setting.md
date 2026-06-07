# Ubuntu Terminator 终端配置指南

## 概述

本文档详细介绍了如何在Ubuntu系统中将Terminator设置为默认终端，解决文件管理器右键菜单"在终端打开"仍调用默认终端的问题。

## 问题背景

Ubuntu文件管理器（Nautilus）的“在终端打开”右键菜单是由内置插件提供的，该插件在底层代码中将终端硬编码为了GNOME Terminal或GNOME Console。因此，仅仅通过系统快捷键设置去修改全局默认终端，是无法影响文件管理器右键行为的。要彻底解决这个问题，需要借助第三方扩展 nautilus-open-any-terminal 来接管并覆盖默认的硬编码设置。

## 解决方案

### 方案一：设置Terminator为系统默认终端

#### 1. 验证Terminator路径

首先确认Terminator的安装路径：

```bash
which terminator
```

通常返回路径为`/usr/bin/terminator`。

#### 2. 修改右键默认终端

打开现有的终端，安装Python相关的系统依赖项以及Nautilus的Python绑定库

```bash
sudo apt update
sudo apt install python3-nautilus python3-pip gir1.2-gtk-4.0
```

验证：

```bash
dpkg -l | grep python3-nautilus
```

正常输出类似：

```text
ii  python3-nautilus
```

#### 3. 安装扩展组件

通过 pip 包管理器安装该扩展核心组件。由于不同Ubuntu版本的安全策略有所差异，请根据你的实际系统版本选择对应的安装命令。如果你使用的是Ubuntu 22.04及更早的版本，请执行以下命令：

```bash
pip3 install --user nautilus-open-any-terminal
```

如果你使用的是Ubuntu 24.04或更新的版本，由于系统引入了限制全局pip安装的安全策略，因此需要额外添加解除限制的参数：

```bash
pip3 install nautilus-open-any-terminal --break-system-packages
```

验证：

```bash
pip3 show nautilus-open-any-terminal
```

应显示版本信息。

检查扩展文件：

```bash
ls ~/.local/share/nautilus-python/extensions/
```

应看到：

```text
open_any_terminal_extension.py
```

#### 4. 使配置项生效

扩展安装完成后，系统底层暂时还无法直接读取到它，必须手动编译 GSettings Schema 配置文件

```bash
glib-compile-schemas ~/.local/share/glib-2.0/schemas/
```
确认生成：

```bash
ls ~/.local/share/glib-2.0/schemas/
```

应看到：

```text
gschemas.compiled
```

然后利用系统设置命令将文件管理器右键菜单的启动目标正式指向 Terminator：

```bash
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal terminator
```
#### 5. 重启文件管理器

最后，需要强制关闭当前正在后台运行的文件管理器进程，以加载新的插件与配置：

```bash
nautilus -q
```

重新打开文件管理器并在空白处或目标文件夹上点击右键，此时的“在终端打开”选项便会自动启动 Terminator 了。

**注意**：如果使用其他文件管理器（如Nemo、Dolphin），需替换为对应进程名（如`nemo -q`）。


## 验证与常见问题

### 1. 验证是否生效

- 右键点击任意文件夹，检查菜单中是否出现"在终端打开"（系统默认配置）或自定义名称（手动配置方案）
- 检查配置是否被正确设置：

### 2. 恢复默认设置

#### 1.方案一：仅恢复右键菜单默认行为（推荐）

删除 Open Any Terminal 的配置：

```bash
rm -rf ~/.local/share/nautilus-python/extensions/open_any_terminal_extension.py
rm -rf ~/.local/share/nautilus-python/extensions/__pycache__
```

删除用户级 Schema：

```bash
rm -f ~/.local/share/glib-2.0/schemas/com.github.stunkymonkey.nautilus-open-any-terminal.gschema.xml
rm -f ~/.local/share/glib-2.0/schemas/gschemas.compiled	
```

#### 2. 方案二：彻底卸载 Open Any Terminal

先卸载 Python 包：

```bash
pip3 uninstall nautilus-open-any-terminal
```
清理遗留文件：

```bash
rm -rf ~/.local/share/nautilus-python
rm -rf ~/.local/share/glib-2.0/schemas
```

#### 3. 最后重启 Nautilus：

```bash
nautilus -q
```

## 注意事项

- 操作前建议备份重要数据
- 修改系统配置可能需要管理员权限
- 不同Ubuntu版本可能存在细微差异，建议根据实际情况调整

**文档版本：v1.0**
**最后更新：2026-06-06**




---

### [回到 terminal](README.md)
