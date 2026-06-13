# 目录 <!-- omit in toc -->
- [IBus 智能拼音](#ibus-智能拼音)
  - [安装](#安装)
  - [初始配置](#初始配置)
  - [使用方法](#使用方法)
  - [进阶配置](#进阶配置)
    - [模糊音](#模糊音)
    - [用户字典](#用户字典)
  - [相关链接](#相关链接)
    - [回到 输入法](#回到-输入法)

# IBus 智能拼音

`ibus-libpinyin` 是基于 [libpinyin](https://github.com/libpinyin/libpinyin) 的 IBus 中文输入法，支持全拼和注音（Bopomofo）两种输入方式，具备智能联想、云拼音、双拼、模糊音及个人用户字典等功能。适用于 Ubuntu / Debian 及其他使用 IBus 框架的 Linux 发行版。

## 安装

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install ibus ibus-libpinyin
```

安装完成后重启（或注销重新登录），确保 IBus 守护进程生效：

```bash
ibus-daemon -drx
```

> **Ubuntu 22.04+**：系统默认已集成 IBus，通常只需安装 `ibus-libpinyin` 即可。

## 初始配置

1. 打开 **IBus 首选项**：

   ```bash
   ibus-setup
   ```

2. 切换到 **输入法** 选项卡 → 点击 **添加** → 选择 **中文** → 选择 **智能拼音（Intelligent Pinyin）**。

3. 在系统设置中将默认输入法框架设为 **IBus**（Ubuntu 的路径：**设置 → 区域与语言 → 管理已安装的语言 → 键盘输入法系统**）。

## 使用方法

| 操作 | 快捷键（默认） |
|------|--------------|
| 切换输入法 | `Super + Space` / `Ctrl + Space` |
| 中英文切换 | `Shift` |
| 翻页候选词 | `Page Up` / `Page Down` |
| 选择候选词 | 数字键 `1`–`5` |
| 全角 / 半角切换 | `Shift + Space` |

## 进阶配置

右键点击任务栏输入法图标 → **首选项**，或通过 `ibus-setup` 进入拼音设置。

### 模糊音

在首选项的 **拼音** 选项卡中启用模糊音，适合有口音的用户：

| 模糊音对 | 示例 |
|---------|------|
| `z / zh` | `zi` → `zhi` |
| `c / ch` | `ci` → `chi` |
| `s / sh` | `si` → `shi` |
| `n / l`  | `nao` → `lao` |
| `f / h`  | `fei` → `hei` |
| `an / ang` | `an` → `ang` |

### 用户字典

首选项 --> 常规 --> 候选词 --> 勾选 "`将每个输入记录为新词汇`" , 即可自动生成专属字典

ibus-libpinyin 支持导入自定义词汇，以提升专业术语或个人高频词的优先级。

**字典文件格式**（每行一词）：

```
词语 pin'yin 频率权重
```

示例（参考仓库内 [用户字典.txt](用户字典.txt)）：

```
嵌入式 qian'ru'shi 15
芯片 xin'pian 5
优化 you'hua 30
```

**导入方法**：

在 IBus 拼音首选项 → **用户数据** 选项卡 → **导入** → 选择 `.txt` 文件即可。

## 相关链接

- [GitHub 仓库（ibus-libpinyin）](https://github.com/libpinyin/ibus-libpinyin)
- [libpinyin 核心库](https://github.com/libpinyin/libpinyin)
- [IBus 项目主页](https://github.com/ibus/ibus)

---

### [回到 输入法](README.md)
