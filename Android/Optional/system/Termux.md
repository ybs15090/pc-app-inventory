<!-- software-count: 2 -->
# 目录 <!-- omit in toc -->

- [ Termux 与 Termux:API](#-termux-与-termuxapi)
  - [软件简介](#软件简介)
  - [组件关系](#组件关系)
  - [安装方法](#安装方法)
    - [Termux 主程序](#termux-主程序)
    - [Termux:API 附加组件](#termuxapi-附加组件)
    - [安装来源一致性](#安装来源一致性)
  - [使用方法](#使用方法)
  - [常用命令](#常用命令)
  - [常见问题](#常见问题)
  - [官方文档与相关链接](#官方文档与相关链接)
    - [回到 system 目录](#回到-system-目录)

# <img src="../../../.media/svg/Termux.svg" width="60" height="60" alt="Termux 图标"> Termux 与 Termux:API

## 软件简介

Termux 是 Android 平台上的终端模拟器和 Linux 环境，无需 Root 即可安装软件包、运行脚本和常用命令行工具。Termux:API 是它的附加组件，为 Termux 增加电池、剪贴板、通知、位置、相机、短信等系统接口的命令行调用能力。

两者面向不同需求：只用 SSH、Git、Python 或命令行工具时，安装 Termux 即可；需要让脚本读取手机状态或调用系统功能时，再安装 Termux:API。二者仅支持 Android，且必须来自同一安装来源。

资料核对日期：**2026-10-22**。验证范围：官方 GitHub Releases、Termux Wiki 与 F-Droid 资料核对，未在本次文档整理中安装应用或进行手机功能实测。

## 组件关系

| 组件 | 包名 | 作用 | 是否必须 |
|---|---|---|---|
| Termux | `com.termux` | 提供终端、包管理器和 Linux 用户空间 | 是 |
| Termux:API（应用） | `com.termux.api` | 提供系统接口的权限与桥接服务 | 使用 API 时安装 |
| `termux-api`（软件包） | — | 提供 `termux-*` 命令行工具，在 Termux 内安装 | 使用 API 时安装 |

只安装 Termux:API 应用而没有在 Termux 内安装 `termux-api` 包，或反过来，都无法调用系统接口。两个组件缺一不可。

## 安装方法

### Termux 主程序

**方式一：GitHub Releases（推荐，版本最新）**

1. 打开 [Termux Releases](https://github.com/termux/termux-app/releases)，在最新正式版的 Assets 中下载 APK。核对时最新正式版为 **v0.118.3**（2025-05-22）。
2. 按设备架构选择文件。多数手机使用 `arm64-v8a`，较旧的 32 位设备使用 `armeabi-v7a`，模拟器使用 `x86` 或 `x86_64`；不确定时可选 `universal`，体积更大。文件名形如 `termux-app_v0.118.3+github-debug_arm64-v8a.apk`。
3. 在浏览器或文件管理器中打开 APK，按系统提示允许“安装未知应用”，完成安装。
4. 首次启动后等待终端初始化完成，再执行 `pkg update && pkg upgrade` 更新软件包索引。

> GitHub 构建使用公开测试密钥签名，仅从官方 Releases 下载。不要安装来自论坛、网盘或聊天群转发的 APK。

**方式二：F-Droid**

在 F-Droid 客户端中搜索 **Termux** 安装。F-Droid 构建的版本通常比 GitHub 晚数天到数周，但升级由 F-Droid 统一管理。F-Droid 同时提供 Termux:API，适合希望一个来源管理全部组件的用户。

**关于 Google Play**

官方已将 Google Play 版本标记为弃用，另设实验性仓库 `termux-play-store`，不再作为推荐渠道。不要把它与 F-Droid 或 GitHub 版本混用。

系统要求：**Android 7.0 及以上**。更旧的 Android 5/6 仅有停止维护的 `apt-android-5` 构建，无法继续获取软件包更新。

### Termux:API 附加组件

**方式一：GitHub Releases**

1. 从 [Termux:API Releases](https://github.com/termux/termux-api/releases) 下载最新 APK。核对时为 **v0.53.0**（2025-09-01），文件名形如 `termux-api-app_v0.53.0+github.debug.apk`。
2. 安装后先启动一次 Termux:API，按提示授予需要的运行时权限。
3. 回到 Termux，安装命令行工具：

```bash
pkg update
pkg install termux-api
```

**方式二：F-Droid**

在 F-Droid 中搜索 **Termux:API** 安装，然后在 Termux 内执行同样的 `pkg install termux-api`。如果 Termux 主程序来自 F-Droid，附加组件也应从 F-Droid 安装。

**验证安装**

```bash
termux-battery-status
```

首次调用时，如果系统弹出权限请求，按提示允许。能返回 JSON 格式的电池信息即表示组件工作正常。

### 安装来源一致性

Termux、Termux:API 以及从 F-Droid 安装的插件共用 `com.termux` 的共享用户标识，但 **GitHub、F-Droid、Google Play 三者的签名密钥不同**。混装会导致附加组件无法调用主程序，或安装时直接报签名冲突。

- 所有组件固定使用同一个来源。
- 从 GitHub 切换到 F-Droid（或反向）时，必须先卸载 Termux 和全部插件。卸载会删除 Termux 家目录中的数据，操作前先备份需要保留的文件。
- 系统提示“应用未安装”或“签名不一致”时，优先检查来源是否混用，而不是反复重装单个应用。

## 使用方法

1. 打开 Termux，执行 `pkg update && pkg upgrade` 更新基础环境。
2. 用 `pkg install <包名>` 安装需要的工具，例如 `pkg install git python openssh`。
3. 需要访问手机共享存储时执行 `termux-setup-storage`，按提示授予存储权限。文件通常位于 `~/storage/shared`。
4. 需要让 Termux:API 的调用生效时，直接在 Termux 中执行对应命令，例如：

```bash
termux-toast "来自 Termux 的提示"
termux-clipboard-set "Hello from Termux"
termux-clipboard-get
termux-notification --title "Termux" --content "API 调用成功"
termux-location
```

5. 需要长时间运行任务时执行 `termux-wake-lock` 获取唤醒锁，任务结束后用 `termux-wake-unlock` 释放。Android 的电池优化仍可能终止后台进程，可在系统设置中为 Termux 关闭电池优化。

> Termux 的文件系统位于应用私有目录，卸载应用会一并删除。重要脚本和配置应定期备份到共享存储或其他设备。

## 常用命令

| 命令 | 作用 | 常见权限要求 |
|---|---|---|
| `termux-battery-status` | 读取电量、充电状态与温度 | 无 |
| `termux-toast` | 显示短时提示 | 无 |
| `termux-notification` | 发送系统通知 | 通知权限 |
| `termux-clipboard-get` / `termux-clipboard-set` | 读写剪贴板 | Android 10 及以上对后台读取有限制 |
| `termux-location` | 获取当前位置 | 位置权限 |
| `termux-camera-photo` | 调用相机拍照 | 相机权限 |
| `termux-sms-list` | 读取短信列表 | 短信权限 |
| `termux-wifi-connectioninfo` | 读取 Wi-Fi 连接信息 | 部分系统要求位置权限 |
| `termux-setup-storage` | 在 `~/storage` 下建立共享存储链接 | 存储权限 |

部分接口还需要额外授权：修改亮度等设置需要“修改系统设置”，读取通知需要手动开启“通知使用权”，安装或卸载应用需要“安装未知应用”权限。按实际使用的命令授予即可，不需要一次开放全部权限。

## 常见问题

| 问题 | 说明或处理方法 |
|---|---|
| `termux-battery-status` 一直无输出或卡住 | 确认 Termux:API 应用已安装并启动过；在系统设置中将 Termux 和 Termux:API 加入电池优化白名单或“受保护应用”，部分厂商系统会限制后台调用。 |
| 提示 `termux-api` 命令不存在 | 只安装了 Termux:API 应用，尚未在 Termux 内执行 `pkg install termux-api`。 |
| 附加组件提示签名冲突或无法调用 | 主程序与附加组件来源不一致。统一来源，必要时卸载后重装，操作前备份数据。 |
| 安装 Termux:API 后仍无权限 | 打开 Termux:API 应用检查运行时权限；修改系统设置、通知使用权等特殊权限需要在系统设置中单独开启。 |
| `Android/data` 或共享目录无法访问 | Android 11 及后续系统限制应用访问其他应用的私有目录，能否访问取决于系统版本与厂商实现，不能仅凭存储权限判断。 |
| 后台任务被系统终止 | 执行 `termux-wake-lock`，并在系统电池设置中允许 Termux 后台运行；不同厂商的限制差异较大。 |
| 从外部应用调用 Termux 命令失败 | 需要在 `~/.termux/termux.properties` 中设置 `allow-external-apps = true`，再执行 `termux-reload-settings`。 |

## 官方文档与相关链接

- [Termux 官网](https://termux.dev/)
- [Termux 源码仓库](https://github.com/termux/termux-app)
- [Termux Releases](https://github.com/termux/termux-app/releases)
- [Termux Wiki](https://wiki.termux.com/)
- [Termux:API 说明](https://wiki.termux.com/wiki/Termux:API)
- [Termux:API 源码仓库](https://github.com/termux/termux-api)
- [Termux:API Releases](https://github.com/termux/termux-api/releases)
- [F-Droid 上的 Termux](https://f-droid.org/packages/com.termux/)

---

### [回到 system 目录](README.md)
