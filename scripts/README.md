# 软件计数脚本

`count-software.py` 是唯一的统计和 README 更新实现。`.ps1`、`.sh`、`.bat` 仅负责启动并转发参数，均需要 **Python 3.8 或更新版本**。

## 计数规则

只读取六个平台 `Essential/`、`Optional/` 下 Markdown 正文前 20 行中的独立 HTML 注释：

```markdown
<!-- software-count: 1 -->
```

- 单软件说明必须标记 `1`，多软件合集标记实际收录数量。
- 配置、备份、故障处理和非软件专题标记 `0`，包括名为 `config.md` 的附属文档。
- 建议把标签放在第一行；代码块中的示例、行内文字、图片和标题都不作为计数依据。
- 标签缺失的正文未计入，并逐文件提示；默认更新会被阻止，需补齐标签后重试。负数、非整数或前 20 行内重复标签直接报错。
- 排除 `README.md`、`CLAUDE.md`、`AGENTS.md`、`test.md`；不进入 `.obsidian/`、`.git/`、`test/`、`__pycache__/` 和符号链接目录，不读取符号链接文件。排除名称不区分大小写，目录名称按完整名称匹配。
- 结果是标签的合计，不执行跨文件、跨平台的软件名称去重。根模板和根级说明不在扫描范围。

## 运行方式

Windows：

```powershell
# 默认刷新中英文 README；数字已是最新时不写文件
python scripts/count-software.py

# 只看统计和逐文件明细
python scripts/count-software.py --dry-run --details

# 检查标签完整性及 README 是否需要更新
python scripts/count-software.py --check

# 明确要求刷新
python scripts/count-software.py --write
```

Linux/macOS 将 `python` 换成 `python3`，也可使用 Bash 入口：

```bash
bash scripts/count-software.sh --dry-run --details
bash scripts/count-software.sh --check
```

Windows PowerShell 入口支持相同参数，也支持 `-DryRun`、`-Check`、`-Details`、`-Write` 写法：

```powershell
pwsh.exe -NoProfile -NonInteractive -File scripts/count-software.ps1 --check
scripts/count-software.bat --dry-run --details
```

双击 BAT 时默认刷新，并在结束后暂停，方便查看结果；带参数调用时不暂停。BAT 优先从 PATH 启动 PowerShell 7，找不到时使用 Windows PowerShell 5.1，均禁用 Profile。脚本不会自动安装 Python。

## README 更新与退出码

两份根 README 的统计表放在以下标记之间；标记本身保留，数字由程序生成：

```markdown
<!-- software-stats:start -->
统计表
<!-- software-stats:end -->
```

程序先校验两份 README 的标记均存在、唯一且顺序正确，再准备写入。保留 UTF-8 BOM、原有 LF/CRLF 换行、统计区块外的内容和末尾换行状态；没有变化时不写文件。更新通过同目录临时文件替换，文件在校验后被修改时会停止，第二份写入失败时尝试恢复已经替换的第一份。

| 退出码 | 含义 |
|---|---|
| `0` | 预览完成、更新成功或检查通过。预览中的缺失标签仍会显示警告。 |
| `1` | `--check` 发现缺失标签或统计表需要更新。 |
| `2` | 无效或重复标签、读取错误、区块标记错误、更新失败，或默认更新时存在缺失标签。 |
| `130` | 用户中断。 |

## 验证脚本

```powershell
python -B -m unittest discover -s scripts -p "test_count_software.py" -v
```

测试使用临时目录和内存对象，覆盖显式标签、代码块示例、精确目录排除、编码换行、无变化时不写入、并发修改保护和部分更新失败后的回退。

---

[回到仓库入口](../README.md) · [文档编写约定](../文档编写约定.md)
