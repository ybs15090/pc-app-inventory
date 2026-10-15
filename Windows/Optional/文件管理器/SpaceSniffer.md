<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->

- [ SpaceSniffer](#-spacesniffer)
  - [软件简介](#软件简介)
  - [安装方法](#安装方法)
    - [Windows 便携版](#windows-便携版)
    - [Scoop](#scoop)
    - [通过图吧工具箱使用](#通过图吧工具箱使用)
  - [功能特点](#功能特点)
  - [使用方法](#使用方法)
    - [定位占用空间的文件](#定位占用空间的文件)
    - [常用筛选条件](#常用筛选条件)
  - [使用注意事项](#使用注意事项)
  - [官方文档与相关链接](#官方文档与相关链接)
    - [回到文件管理器目录](#回到文件管理器目录)

# <img src="../../../.media/png/spacesniffer.png" width="60" height="60" alt="SpaceSniffer 图标"> SpaceSniffer

## 软件简介

SpaceSniffer 是 Uderzo Software 开发的免费 Windows 磁盘空间分析工具，使用矩形树状图（Treemap）展示文件和文件夹的大小，便于找出占用空间较多的目录与文件。

软件可便携运行，无需安装。适合排查磁盘空间去向、整理下载目录、查找大型视频素材与游戏文件。矩形面积越大，代表对应文件或目录占用越多；可以逐层展开目录并筛选结果。

**SpaceSniffer 也被[图吧工具箱](../图吧工具箱.md)收录。** 已经使用图吧工具箱时，可直接查找并启动其内置版本；需要独立使用或更新版本时，可从作者官网下载便携包。

资料核对日期：2026-10-15。验证范围：作者官网、下载页、更新记录与 Scoop 清单核对；未在本机安装、运行或测试磁盘扫描。图吧工具箱的内置版本以实际发行包为准。

## 安装方法

### Windows 便携版

1. 打开[作者官方下载页](https://www.uderzo.it/main_products/space_sniffer/download.html)，从页面链接的官方镜像下载；镜像无法使用时，可进入[作者备用下载页](https://www.uderzo.it/main_products/space_sniffer/download_alt.html)。
2. 下载适合系统架构的 ZIP 压缩包，并完整解压到固定目录，例如 `D:\Tools\SpaceSniffer\`。
3. 双击解压后的 `SpaceSniffer.exe` 启动，无需安装向导。

核对时，作者列出的当前版本为 **2.2.0.27 x64**，发布日期为 **2026-03-25**。该版本面向 64 位 Windows；作者页面标注 x64 版本在 Windows 7、8、10、11 上测试过。版本与系统兼容性以[作者发布信息](https://www.uderzo.it/main_products/space_sniffer/download_alt.html)为准，本文未做上述系统的运行验证。

### Scoop

已安装 [Scoop](https://scoop.sh/) 时，可在 PowerShell 中执行：

```powershell
scoop bucket add extras
scoop install extras/spacesniffer
```

如果已经添加 `extras`，可直接执行第二条命令。包名与下载来源见 [Scoop Extras 清单](https://github.com/ScoopInstaller/Extras/blob/master/bucket/spacesniffer.json)，添加软件源的方法见 [Scoop 官方说明](https://github.com/ScoopInstaller/Scoop#known-application-buckets)。核对时该清单提供 64 位版本。

### 通过图吧工具箱使用

1. 按[图吧工具箱说明](../图吧工具箱.md)下载并打开工具箱。
2. 在硬盘相关工具分类中查找 **SpaceSniffer**，点击对应条目启动。
3. 按需要选择要分析的磁盘或目录。

工具分类名称和所含版本可能随图吧工具箱发行版变化。内置版与作者独立发布版不一定同步，需要新版功能或修复时，先核对作者的[更新记录](https://www.uderzo.it/main_products/space_sniffer/release_notes.html)。

## 功能特点

| 功能 | 用途 |
|---|---|
| 矩形树状图 | 用面积表示文件与目录的大小，快速查看空间分布。 |
| 逐层浏览与缩放 | 单击目录块查看内部内容，双击目录块将其放大为当前视图。 |
| 条件筛选 | 按文件类型、大小和时间等条件缩小查看范围，也可排除指定类型。 |
| 动态更新 | 响应文件系统变化，在视图中更新相关文件或目录。 |
| 临时颜色标记 | 使用四种颜色标记已检查的项目，并按标记筛选。 |
| 文本报告导出 | 通过内置导出模块生成报告，可自定义报告布局。 |
| Windows 右键菜单 | 在图中对文件或目录打开系统右键菜单，进一步查看或管理。 |

功能依据：[作者产品介绍](https://www.uderzo.it/main_products/space_sniffer/)与[功能说明](https://www.uderzo.it/main_products/space_sniffer/features.html)。

## 使用方法

### 定位占用空间的文件

1. 启动 SpaceSniffer，在选择窗口中选择要分析的盘符或文件夹，例如下载目录、素材目录或某个磁盘。
2. 开始扫描后，先查看整体分布；扫描期间也能浏览结果，判断总量时应等待扫描完成并查看是否有读取错误。
3. 从面积较大的矩形开始检查。单击目录块展开其内容，双击目录块放大查看，再通过导航按钮返回上级视图。
4. 将鼠标移到项目上查看提示信息，确认文件名、路径和大小；需要进一步查看时，右键打开 Windows 文件或文件夹菜单。
5. 需要保存分析结果时，使用内置导出模块生成文本报告；后续复查时可重新扫描对应目录。

### 常用筛选条件

在筛选框中输入条件后按 Enter。以下示例来自[作者产品介绍](https://www.uderzo.it/main_products/space_sniffer/)：

| 条件 | 含义 |
|---|---|
| `*.jpg` | 只显示 JPEG 文件。 |
| `\|*.jpg` | 排除 JPEG 文件。 |
| `>1mb` | 按大小筛选大于 1 MB 的文件。 |
| `>2years` | 按文件时间筛选超过两年的文件。 |
| `*.jpg;>1mb;<3months` | 组合文件类型、大小和时间条件。 |

## 使用注意事项

- **先确认文件用途再处理。** SpaceSniffer 用于分析空间分布，文件较大并不能说明它可以删除。需要整理软件数据时，优先使用对应软件的卸载、缓存清理或迁移功能。
- **读取失败会影响扫描完整性。** 遇到拒绝访问或无法读取的目录时，查看错误信息；确有权限需求时可尝试以管理员身份重新运行，但管理员权限也不保证能读取所有受保护或被占用的文件。
- **筛选会改变当前显示范围。** 查看整个磁盘或目录的分布前，先清空筛选条件，并确认当前视图所在的目录层级。
- **扫描大小不等于可释放空间。** 判断整理效果时，应在实际处理后重新扫描，并查看 Windows 显示的磁盘可用空间。

## 官方文档与相关链接

- [作者官网：Uderzo Software SpaceSniffer](https://www.uderzo.it/main_products/space_sniffer/)
- [作者官方下载页](https://www.uderzo.it/main_products/space_sniffer/download.html)
- [作者备用下载页](https://www.uderzo.it/main_products/space_sniffer/download_alt.html)
- [官方功能说明](https://www.uderzo.it/main_products/space_sniffer/features.html)
- [官方更新记录](https://www.uderzo.it/main_products/space_sniffer/release_notes.html)
- [SpaceSniffer 中文介绍页（用户提供）](https://www.space-sniffer.cn/index.html)
- [图吧工具箱官网](https://www.tbtool.cn/)
- [仓库内的图吧工具箱说明](../图吧工具箱.md)

---

### [回到文件管理器目录](README.md)
