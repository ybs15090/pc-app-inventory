# 目录 <!-- omit in toc -->
- [ Git](#-git)
  - [安装](#安装)
  - [Git 的核心概念包括：](#git-的核心概念包括)
  - [Git 的常用命令包括：](#git-的常用命令包括)
  - [ GitHub](#-github)

# <img src="../../../.media/svg_black/terminal-git-bash.svg" width="60" height="60" alt="code-Logo"> Git
Git 是一个分布式版本控制系统，广泛用于软件开发和其他版本控制任务。它允许多个开发者协同工作，跟踪文件的更改历史，并管理项目的不同版本。

## 安装
在 **Linux** 系统上，可以使用包管理器安装 Git。
```bash
sudo apt-get update
sudo apt-get install git
``` 
**Windows** 用户可以从 Git 的官方网站下载预编译的安装程序，并按照提示进行安装。
也可以使用 wget 等命令直接下载 Git 安装程序：


## Git 的核心概念包括：
- **仓库（Repository）**：存储项目文件和历史记录的地方。
- **提交（Commit）**：记录文件更改的快照。
- **分支（Branch）**：项目的独立开发线，可以并行开发不同的功能。
- **合并（Merge）**：将不同分支的更改合并到一起。
- **远程仓库（Remote Repository）**：托管在服务器上的仓库，可以与本地仓库进行同步。
## Git 的常用命令包括：    
- `git init`：初始化一个新的 Git 仓库。
- `git clone`：从远程仓库克隆一个本地副本。 
- `git add`：将文件添加到暂存区，准备提交。
- `git commit`：提交更改并记录历史。    
- `git push`：将本地提交推送到远程仓库。
- `git pull`：从远程仓库拉取最新更改并合并到本地。
- `git branch`：列出、创建或删除分支。
- `git merge`：合并分支。
- `git status`：查看当前仓库状态。
- `git log`：查看提交历史。
- `git diff`：查看文件更改的差异。
Git 还支持更多高级功能，如标签（Tag）、子模块（Submodule）和钩子（Hook）等，使其成为一个强大且灵活的版本控制工具。

## <img src="../../../.media/svg/github-inverted.svg" width="60" height="60" alt="github-Logo"> [GitHub](https://github.com)

GitHub是一个在线软件源代码托管服务平台，用于公开程序或软件的代码。使用Git作为版本控制软件，由开发者克里斯·汪斯崔斯、P·J·海特和汤姆·普雷斯顿·沃纳使用Ruby on Rails编写而成。在2018年，GitHub被微软公司收购。

GitHub同时提供付费账户和免费账户。这两种账户都可以建立公开或私有的代码仓库，但付费用户拥有更多功能。
