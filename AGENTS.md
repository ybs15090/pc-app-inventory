# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 仓库概述

这是一个 PC 与移动设备软件清单仓库，按平台分类收录软件介绍、索引和配置专题。目前 Linux 内容主要聚焦 Ubuntu 20.04。主文档使用中文 Markdown，配置和脚本作为附属资源。

新增或调整文档前，参考根目录 [文档编写约定.md](文档编写约定.md) 和目标目录已有文档；模板是新稿起点，不要求批量改写旧文档。

## 目录结构

```
{Platform}/{Category}/{SoftwareName}.md
{Platform}/{Category}/{用途分组}/README.md
{Platform}/{Category}/{用途分组}/{SoftwareName}.md
{Platform}/{Category}/{SoftwareName}/{主说明与附属资源}
```

- **Platform**: `Linux/`, `Windows/`, `MacOS/`, `General/`（跨平台）, `Android/`, `iOS/`
- **Category**: `Essential/`（必装）或 `Optional/`（扩展/选装）
- 软件配置文件（如 VS Code 的 settings.json）作为附属资源放在软件同名目录下

覆盖多个平台的说明一般放在 `General/`；仅针对某一平台或主要使用场景集中于该平台的内容可归入对应平台，并在简介说明适用范围。

## 媒体资源

- `.media/占位图片.png` — 软件介绍默认标题图片
- `.media/svg/` — 软件图标（SVG 格式），用于 `README.md` 等页面
- `.media/png/` — 截图和演示图片
- `.media/jpg/`、`.media/ico/` — 已有 JPG 与 ICO 资源
- `.media/svg_black/` — VS Code 专用图标（深色主题适配）

引用图片时使用相对路径，如 `../../../.media/svg/example.svg`（从目标 .md 文件的相对层级计算）。

## 文档规范

根目录提供四种模板，按用途选用：

| 模板 | 适用内容 |
|---|---|
| [模板-单软件说明.md](模板-单软件说明.md) | 一款软件的完整说明；删除不支持的平台章节。 |
| [模板-多软件合集.md](模板-多软件合集.md) | 几款功能相近、篇幅较短的软件。 |
| [模板-分类索引.md](模板-分类索引.md) | 分类或软件资源文件夹的 `README.md`。 |
| [模板-配置专题.md](模板-配置专题.md) | 配置、迁移、备份或故障处理专题。 |

单软件说明通常包含以下结构（可参考 `General/Optional/File-Transfer-文件传输/LocalSend.md` 或 `General/Essential/file-search/ripgrep.md`）：

1. **目录**（默认放在开头，带 `<!-- omit in toc -->` 注释，与正文标题对应）
2. **软件简介** — 用一句话说明软件用途
3. **安装方法** — 按实际支持的平台分节，提供经来源核对的安装方式
4. **使用方法** — 简要说明即可
5. **官方文档/相关链接** — 官网、GitHub、教程链接

功能特点、常见问题等按软件实际需要增删。多软件各自篇幅较长时拆成独立说明，并建立分类索引。简短索引可省略目录；配置专题使用适用环境、操作、验证及必要的回退结构，不强加软件安装章节。

安装命令、版本和系统要求依据官网、官方仓库或包管理器资料核对；只列实际支持的渠道。支持时提供包管理器和本地安装包方案，Linux 尤其说明可用发行包及依赖。注明核对日期和实际验证范围，不把官方资料核对写成本机已安装或已测试。

Windows PowerShell 命令使用 `powershell` 代码块，Linux/macOS shell 使用 `bash`，配置使用对应语言标记。

### 命名规范

- 单软件：`软件名称.md` 或 `软件用途.md`
- 功能相关的多个软件可在同一个 `.md` 中对比介绍，此时按功能/用途命名（如 `文件编辑.md`、`远程连接.md`）
- 合集和专题优先使用中文用途名；单软件可沿用官方名称，既有文件名不为统一风格而重命名

### 图标用法

软件介绍的标题图片默认使用 `.media/占位图片.png`。模板在根目录使用下列路径；复制到目标目录后重新计算相对路径，例如两层目录用 `../../.media/占位图片.png`，三层用 `../../../.media/占位图片.png`。按需替换已确认的真实软件图标并更新 `alt`：

```markdown
# <img src=".media/占位图片.png" width="60" height="60" alt="软件名称占位图片"> 软件名称
```

带图片的多软件条目使用 `## <img ...> 软件名`。标题按此写法含前导空格时，目录锚点可能为 `#-软件名称`；重复标题按顺序使用 `-1`、`-2` 后缀。更改标题、图片写法或章节顺序后核对目录锚点，不直接照抄其他文档的锚点。

### 软件计数

根模板不在平台目录内，不计入软件统计。`scripts/count-software.py` 是唯一计数核心，`.ps1`、`.sh`、`.bat` 仅作启动入口，均需 Python 3.8 或更新版本。脚本统计六个平台的 `Essential/` 与 `Optional/`，只接受正文前 20 行内、代码块外唯一的独立 `<!-- software-count: N -->` 注释，不按图片、标题或文件名推断数量。

所有单软件说明必须标记 `<!-- software-count: 1 -->`；合集按实际数量标记，多软件模板默认计 2；配置、备份、故障处理及非软件专题标记 `<!-- software-count: 0 -->`，包括 `config.md`。建议标签放在第一行。无标签的正文不计入，且阻止默认刷新；无效或重复标签直接报错。

脚本排除 `README.md`、`CLAUDE.md`、`AGENTS.md`、`test.md`，不进入 `.obsidian/`、`.git/`、`test/`、`__pycache__/` 或符号链接目录，不读取符号链接文件。名称不区分大小写，目录按完整名称排除。统计按标签加总，不跨文件去重。

统计表由 `python scripts/count-software.py` 刷新，只更新两份 README 的 `software-stats` 标记区块，保留 BOM、换行和区块外内容，没有变化时不写文件。`--dry-run --details` 提供只读明细，`--check` 核对标签与统计表，完整说明见 [scripts/README.md](scripts/README.md)。修改计数规则时同步根 README 中英文正文、模板和本约定；未获任务授权时不批量调整旧文档标签。

## 编辑注意事项

- 使用中文撰写内容（README_en.md 除外）
- 新增软件同步所属目录索引；新增分组时同步上级 `README.md`，页面末尾提供有效返回链接
- 移动或重命名文件时，同步更新所有引用该文件的相对路径链接
- `README.md` 是语言和编写入口；根 README 正文修改同步 `README_zh.md` 与 `README_en.md`，模板无需另建英文副本
- 替换模板占位内容、检查相对链接与图片路径、核对目录锚点；按变更范围检查 Markdown 格式
- 尽量保留已有文件的编码、换行和末尾换行，不做无目的的批量格式转换
- `.gitignore` 忽略了 `*.zip`、`*.rar`、`*.log`

## 其他

- 对于所有操作,忽略`.obsidian`目录.
