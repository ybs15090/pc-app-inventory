<!-- software-count: 1 -->
# 目录 <!-- omit in toc -->
- [GitHub CLI](#-github-cli)
  - [安装](#安装)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux（Debian/Ubuntu）](#linuxdebianubuntu)
    - [本地安装包](#本地安装包)
  - [登录认证](#登录认证)
  - [常用命令](#常用命令)
  - [配置与扩展](#配置与扩展)
  - [相关链接](#相关链接)

# <img src="../../../.media/svg/github-inverted.svg" width="60" height="60" alt="GitHub CLI logo"> GitHub CLI

GitHub CLI（命令行工具 `gh`）是 GitHub 官方推出的命令行客户端，让你无需离开终端即可完成克隆仓库、创建与审查 Pull Request、管理 Issue、查看 Actions、发布 Release 等操作，是 [Git](git.md) 之外与 GitHub 协作的高效补充。

## 安装

`gh` 在各主流平台均有官方包管理器支持，也可下载独立二进制。

### Windows

```powershell
# winget（推荐）
winget install --id GitHub.cli

# 或 Scoop
scoop install gh

# 或 Chocolatey
choco install gh
```

### macOS

```bash
# Homebrew（推荐）
brew install gh

# 或 MacPorts
sudo port install gh
```

### Linux（Debian/Ubuntu）

从 GitHub 官方 apt 源安装：

```bash
sudo mkdir -p -m 755 /etc/apt/keyrings \
&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

> 其他发行版（Fedora、Arch、openSUSE 等）可用对应包管理器：`sudo dnf install gh`、`sudo pacman -S github-cli`、`sudo zypper install gh`。

### 本地安装包

在 [GitHub Releases](https://github.com/cli/cli/releases) 页面可直接下载各平台的安装包与免安装二进制（Windows 的 `.msi`/`.zip`、macOS 的 `.pkg`、Linux 的 `.deb`/`.rpm`/`.tar.gz`），适合无法联网包管理器或需要固定版本的场景。

## 登录认证

首次使用需完成一次身份认证：

```bash
gh auth login
```

按提示依次选择 **GitHub.com**（或 Enterprise）、协议（HTTPS / SSH）、认证方式（浏览器登录 / 粘贴 Token）。完成后可用以下命令查看状态：

```bash
gh auth status      # 查看当前登录账号与权限
gh auth logout      # 退出登录
```

> 登录后 `gh` 会自动为 Git 配置凭据助手，`git push/pull` 也能直接复用该认证。

## 常用命令

```bash
# 仓库
gh repo clone owner/repo        # 克隆仓库
gh repo create my-repo --public # 新建仓库
gh repo view --web              # 在浏览器打开当前仓库

# Pull Request
gh pr create                    # 基于当前分支创建 PR
gh pr list                      # 列出 PR
gh pr checkout 123              # 检出编号为 123 的 PR
gh pr view 123 --web            # 查看 PR
gh pr merge 123                 # 合并 PR

# Issue
gh issue create                 # 新建 Issue
gh issue list --label bug       # 按标签筛选

# Actions / Release
gh run list                     # 查看工作流运行记录
gh run watch                    # 实时跟踪某次运行
gh release create v1.0.0        # 发布 Release

# 直接调用 GitHub API
gh api /user
```

## 配置与扩展

```bash
# 设置默认编辑器（用于填写 PR/Issue 内容）
gh config set editor "code --wait"

# 自定义命令别名
gh alias set prc 'pr create --fill'

# 安装社区扩展（例如看板、Copilot 等）
gh extension install owner/gh-extension
gh extension list
```

## 相关链接

- [GitHub CLI 官网](https://cli.github.com/)
- [官方手册（Manual）](https://cli.github.com/manual/)
- [GitHub 仓库 cli/cli](https://github.com/cli/cli)

---

### [回到 Git](README.md)
