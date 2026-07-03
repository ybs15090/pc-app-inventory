# 目录 <!-- omit in toc -->
- [终端配置文件](#终端配置文件)
  - [.bashrc](#bashrc)
    - [应用方法](#应用方法)
    - [自定义配置说明](#自定义配置说明)
      - [IBus 输入法环境变量](#ibus-输入法环境变量)
      - [PATH 扩展](#path-扩展)
      - [代理切换脚本](#代理切换脚本)
      - [ROS 环境（机器人开发专用）](#ros-环境机器人开发专用)
  - [Terminator 配置备份](#terminator-配置备份)

# 终端配置文件

本目录存放终端相关的用户配置文件，包括 Shell（`.bashrc`）及 Terminator 终端模拟器的配置备份。

## .bashrc

[`.bashrc`](.bashrc) 是 Bash 的用户级配置文件，每次打开非登录交互式终端时自动加载。

文件前半段为 Ubuntu 默认内容（历史记录、彩色提示符、`ll` / `la` 等常用别名），后半段为个人自定义扩展。

### 应用方法

**方式一：追加到现有 `.bashrc`**（推荐，避免覆盖系统默认配置）

```bash
cat ~/path/to/this/.bashrc >> ~/.bashrc
source ~/.bashrc
```

**方式二：直接替换**

```bash
cp ~/.bashrc ~/.bashrc.bak   # 先备份
cp .bashrc ~/.bashrc
source ~/.bashrc
```

### 自定义配置说明

#### IBus 输入法环境变量

```bash
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
```

使 GTK / Qt 应用正确识别 IBus 输入框架，解决 Electron 类应用（VS Code、Obsidian 等）无法输入中文的问题。详见 [中文输入法故障与解决](../../输入法/中文输入法故障与解决.md#问题-3electron-类应用无法输入中文)。

#### PATH 扩展

```bash
export PATH="$PATH:/home/s/.local/bin"
export PATH="$PATH:/opt/blender-4.5.9-linux-x64"
export PATH="$HOME/.npm-global/bin:$PATH"
```

| 路径 | 用途 |
|------|------|
| `~/.local/bin` | pip 用户级安装的命令行工具（如 `pipx`） |
| `/opt/blender-*/` | Blender 解压安装后的启动命令 |
| `~/.npm-global/bin` | npm 全局包安装路径（避免 sudo） |

按需保留或替换为实际路径。

#### 代理切换脚本

每次打开终端时询问是否启用 HTTP 代理，并在最后显示当前代理状态：

```
是否使用代理? (是: y/Y, 否: n/N):
```

- 输入 `y` / 回车：设置 `http_proxy` 和 `https_proxy` 为 `http://127.0.0.1:7897`（Clash 默认端口）
- 输入 `n`：清除代理环境变量
- 最终打印当前代理状态（青色高亮）

> 端口 `7897` 对应 Clash 系列代理客户端的默认混合代理端口，如使用其他客户端请修改。

#### ROS 环境（机器人开发专用）

```bash
source /opt/ros/noetic/setup.bash          # ROS Noetic 基础环境
source ~/ros_workspaces/wpm2_beifen/devel/setup.bash  # 工作空间
export ROS_PARALLEL_JOBS='-j12'            # 多线程编译
export DISABLE_ROS1_EOL_WARNINGS=1        # 屏蔽 EOL 警告
```

不使用 ROS 的用户可删除这几行。分布式 ROS 配置（`ROS_IP`、`ROS_MASTER_URI`）已注释，按需启用。

## Terminator 配置备份

[`config/`](config/) 子目录备份了 Terminator 的用户配置（对应 `~/.config/terminator/`），包含快捷键、配色方案、字体及自定义命令菜单等设置，可直接复制回原路径以恢复。

详见 [Terminator-用户配置备份.md](config/Terminator-用户配置备份.md)。

---

### [回到 terminal](../README.md)
