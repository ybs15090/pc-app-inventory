---
name: readme-sync
description: |
  修改本仓库 pc-software-inventory 根目录 README 时，保证中英两份文件同步、并正确处理自动生成的软件统计表。

  【触发条件 — 满足其一】
  - 用户要求修改 `README.md`、`README_zh.md`、`README_en.md` 中任意一个
  - 用户说"更新 README"、"改根说明"、"改组织原则/贡献规范/目录结构"等全局性说明
  - 对仓库整体介绍、组织原则、贡献指南等根级文档的增删改

  【不触发】
  - 修改各平台目录下的软件文档或子目录 README（那是普通编辑，不涉及中英同步）
---

# 同步根 README Skill

根目录三份 README 需保持一致：`README.md`（语言入口）、`README_zh.md`（中文正文）、`README_en.md`（英文正文）。**改动正文时，中英两份必须同步。**

## 核心规则

**任何对 `README_zh.md` 或 `README_en.md` 正文的改动，都必须同步到另一份。** 用户即使只说"改 README_zh"，也要主动提醒并同步英文。

## 工作流

### 1. 同时读取两份正文

先 `Read README_zh.md` 和 `README_en.md`，定位待改段落在两份中的对应位置。

### 2. 中文优先

- 先在 `README_zh.md` 完成中文改动，与用户确认内容无误
- 确认后翻译为英文，同步到 `README_en.md`

### 3. 翻译要求

- **正式书面语**，避免口语化
- **术语一致**：`Essential/` → "必装" / "must-have"，`Optional/` → "选装" / "elective"
- **示例同步**：中文改了文件路径示例，英文用完全相同的示例
- **格式对齐**：标题层级、列表类型、代码块类型与中文版完全一致

### 4. 软件统计表 —— 勿手改，用脚本生成

两份 README 各有一张「软件收录统计」表（表头 `| 平台 | Essential | Optional | 合计 |` / `| Platform | Essential | Optional | Total |`），**由脚本自动生成，不要手工编辑数字**。

需要刷新时运行：

```bash
python scripts/count-software.py
```

脚本会重新统计 `Windows`、`Linux`、`MacOS`、`General`、`Android`、`iOS` 各平台 `Essential/` 与 `Optional/` 的软件数，并原地替换两份 README 的统计表。若无 Python 环境，可用等价的 `scripts/count-software.sh`（或 `.ps1` / `.bat`）。

> 手工改统计数字会与脚本下次运行的结果冲突。只改说明性文字，数字交给脚本。

### 5. 变更对比

改完向用户展示中英对照摘要：

| 段落 | 中文变更 | 英文变更 |
|------|---------|---------|
| 组织原则 | 新增 xxx 条目 | Added xxx entry |

确保每处中文变更都有对应英文，无遗漏。

## 注意事项

- 路径分隔符统一用正斜杠 `/`
- 平台目录名保持原始大小写：`Windows/`、`Linux/`、`MacOS/`、`General/`、`Android/`、`iOS/`
- 示例尽量引用仓库中真实存在的文件路径
