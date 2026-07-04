<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->
- [ Keil MDK（µVision5）](#-keil-mdkµvision5)
  - [安装](#安装)
  - [功能特点](#功能特点)
  - [授权说明](#授权说明)
  - [使用方法](#使用方法)
  - [编辑器配色美化（global.prop）](#编辑器配色美化globalprop)
  - [相关链接](#相关链接)
    - [回到 Windows/Optional/嵌入式开发](#回到-windowsoptional嵌入式开发)

# <img src="../../../../.media/jpg/keilv5.jpg" width="60" height="60" alt="Keil logo"> Keil MDK（µVision5）

Keil MDK（Microcontroller Development Kit）是 Arm 官方推出的、面向 Arm Cortex-M 微控制器的一站式嵌入式开发工具套件，核心为 **µVision5** 集成开发环境（IDE），集代码编辑、工程管理、编译与调试于一体，广泛用于 STM32、GD32、NXP、Nordic 等主流 MCU 的开发，是高校与工程界最常用的单片机开发环境之一。

> 图标为自制占位图，后续可替换为 Keil 正式 logo。

## 安装

Keil MDK **不通过 winget / Chocolatey 等包管理器分发**，需从官网注册后下载安装。

**官网下载（推荐）**：

1. 访问 [keil.arm.com](https://www.keil.arm.com/)（旧域名 [keil.com](https://www.keil.com/) 仍可用），注册 Arm 账号后进入下载页。
2. 下载 MDK-Arm 安装包（形如 `MDK5xx.exe`），运行并按向导完成安装。
3. 首次安装后自动打开 **Pack Installer**，用于安装芯片支持包。

**安装芯片支持包（Device Family Pack, DFP）**：

µVision 安装完成后本身不含具体芯片信息，需通过 Pack Installer 安装对应型号的 DFP：

- 打开 µVision → `Pack Installer`（工具栏图标或 `Project → Manage → Pack Installer`）
- 在左侧 `Devices` 中选择厂商与型号（如 `STMicroelectronics → STM32F1 Series`）
- 在右侧安装对应 Pack（如 `Keil::STM32F1xx_DFP`）

> 开发 8051 / C51 等旧架构需额外安装 **Legacy Support** 包（µVision5 默认只含 Arm 工具链）。

## 功能特点

- **µVision5 IDE**：工程管理、代码编辑、编译、下载、调试一体化，界面成熟稳定
- **Arm Compiler**：内置 Arm Compiler 6（`armclang`，基于 LLVM）与兼容旧工程的 AC5，代码优化能力强
- **CMSIS 支持**：完整支持 CMSIS-Core / DSP / RTOS 等 Arm 标准软件接口
- **软件包管理（Pack）**：按需安装芯片支持包、中间件与示例工程，工程可移植性好
- **强大的调试器**：支持 ST-Link、J-Link、ULINK 等，提供寄存器/外设（Peripheral）视图、断点、逻辑分析仪、事件记录（Event Recorder）等
- **内置 RTOS**：集成 Keil RTX5 实时操作系统，方便快速搭建多任务系统
- **广泛的 MCU 覆盖**：STM32、GD32、NXP、Nordic、TI 等主流 Cortex-M 器件

## 授权说明

Keil MDK 分为不同版本：**Community / Essential / Plus / Professional**，功能与授权范围各异。

- **MDK-Community（社区版）**：面向个人学习与非商业用途**免费**，是学生与爱好者的首选。
- **评估版（Lite/Evaluation）**：无授权时可使用，但编译生成的代码有 **32 KB** 大小限制。
- **STM32 免费授权**：Arm 与 ST 合作，为部分 STM32 入门系列（如 F0 / L0 / G0）提供免费的专属 MDK 授权。
- **商业用途**：需购买 Essential 及以上的正式授权。

> 具体版本的功能差异与授权政策以 [Keil 官网](https://www.keil.arm.com/) 最新说明为准。

## 使用方法

以新建一个 STM32 工程为例：

1. 打开 µVision，`Project → New µVision Project`，选择保存目录。
2. 在弹出的器件选择框中选择目标芯片型号（需先装好对应 DFP）。
3. 在 `Manage Run-Time Environment (RTE)` 中勾选 CMSIS、Device Startup 等组件。
4. `Target Options`（魔术棒图标）中配置时钟、编译选项、调试器（如 ST-Link）与下载算法（Flash Download）。
5. 编写代码，按 `F7` 编译（Build）。
6. 连接开发板，按 `F8` 下载（Download）到芯片。
7. 按 `Ctrl+F5` 进入调试，可单步、设断点、查看寄存器与外设状态。

## 编辑器配色美化（global.prop）

µVision 默认编辑器是白底配色，长时间使用不够护眼。编辑器的字体与语法着色统一保存在 **`global.prop`** 全局配置文件中，替换该文件即可一键切换整套配色方案。

`config/` 目录下提供了几套现成的配色备份（去掉 `.txt` 后即为 `global.prop` 内容）：

| 备份文件 | 配色风格 | 说明 |
|---------|---------|------|
| [`global.prop备份文件.txt`](config/global.prop备份文件.txt) | 默认白底 | 官方原始配色，白底黑字（Courier New 10），可作还原基准 |
| [`global.prop备份文件-深色背景.txt`](config/global.prop备份文件-深色背景.txt) | VS Code Dark+ 风 | 深灰底 `#1E1E1E` + 浅蓝字，Fixedsys 14 号 |
| [`global.prop备份文件-仿VSCode背景.txt`](config/global.prop备份文件-仿VSCode背景.txt) | 仿 VS Code / Monokai | 墨绿底 `#272822`，Courier New 11 号 |
| [`global.prop备份文件-仿VSCode背景修改版.txt`](config/global.prop备份文件-仿VSCode背景修改版.txt) | 仿 VS Code（修改版） | 深底 `#1E1F1B`，改用 Fira Code 连字字体 |

**应用方法**：

1. **完全关闭 µVision**（所有实例），否则退出时会用旧配置覆盖你的修改。
2. 找到 Keil 安装目录下的 `UV4\global.prop`，例如 `C:\Keil_v5\UV4\global.prop`；建议先**备份原文件**。
3. 打开所需的备份 `.txt`，将其内容整体覆盖写入 `global.prop`（保持文件名为 `global.prop`，无扩展名）。
4. 重新启动 µVision 即可看到新配色。

> - 若安装了 Fira Code 等连字字体，可选用「修改版」获得更佳的代码显示效果；未安装时请改用系统自带等宽字体。
> - 也可在 µVision 内 `Edit → Configuration → Colors & Fonts` 手动微调，退出时会自动写回 `global.prop`。
> - 不同 Keil 版本的 `global.prop` 字段略有差异，套用后个别项若显示异常，手动调整对应 `style.*` 即可。

## 相关链接

- [Keil 官网](https://www.keil.com/)
- [Keil MDK（Arm）](https://www.keil.arm.com/)
- [MDK 下载页](https://www.keil.arm.com/mdk-community/)
- [软件包（Pack）列表](https://www.keil.arm.com/packs/)
- [Arm 开发者文档](https://developer.arm.com/documentation)

---

### [回到 Windows/Optional/嵌入式开发](../README.md)
