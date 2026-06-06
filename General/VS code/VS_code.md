# 目录 <!-- omit in toc -->
- [ VScode](#-vscode)
  - [安装](#安装)
    - [Windows](#windows)
    - [MacOS](#macos)
    - [Linux](#linux)
  - [更新](#更新)

# <img src="../../.media/svg/code-icon.svg" width="60" height="60" alt="code Logo"> VScode

Visual Studio Code (简称 VScode) 是一款适用于 Windows、macOS 和 Linux 的免费开源代码编辑器。它是一个面向人工智能代理的开放平台，旨在实现可扩展性，并由功能强大的编辑器提供支持，内置调试、Git 和 IntelliSense 等功能。

您可以[下载VS Code](https://code.visualstudio.com/download)并将其安装到您的桌面上，或者直接在浏览器中通过[vscode.dev](https://vscode.dev)打开它，无需任何设置

**github:** https://github.com/microsoft/vscode.git

## 安装

### Windows
1. 下载并运行安装程序，按照提示完成安装即可。

### MacOS
1. 下载.dmg安装程序。
2. 打开.dmg文件并将Visual Studio Code.app拖到“应用程序”文件夹。
3. 从“应用程序”文件夹或 Spotlight 打开 VS Code。

### Linux
1. 从下载页面下载适用于您发行版的软件包：
    Debian / Ubuntu - 下载.deb软件包并使用sudo apt install ./<file>.deb.
    Fedora / RHEL - 下载.rpm软件包并使用以下命令安装sudo dnf install ./<file>.rpm。
2. VS Code 已正式作为 Snap 软件包在Snap Store中分发。
   
    ![snap store](../../.media/png/snap-store.png)
    
    使用以下命令安装 Snap 软件包：
    ```bash
    sudo snap install --classic code # or code-insiders
    ```
    安装完成后，Snap 守护程序会在后台自动更新 VS Code。当有新版本可用时，VS Code 会显示产品内更新通知。
## 更新

VS Code 每周都会发布新版本。如果 VS Code 软件仓库安装正确，系统包管理器会像处理系统上的其他软件包一样处理自动更新。