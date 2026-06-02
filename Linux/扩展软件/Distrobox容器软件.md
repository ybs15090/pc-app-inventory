# 目录 <!-- omit in toc -->
- [Distrobox](#distrobox)
  - [安装 distrobox（依赖 Docker 或 Podman）](#安装-distrobox依赖-docker-或-podman)
  - [Ubuntu 20.04 官方源不含 Podman，需要先添加第三方源：](#ubuntu-2004-官方源不含-podman需要先添加第三方源)
    - [添加 Kubic 项目的软件源（专门为旧版 Ubuntu 提供 Podman）](#添加-kubic-项目的软件源专门为旧版-ubuntu-提供-podman)
    - [导入 GPG 签名密钥](#导入-gpg-签名密钥)
    - [更新软件源并安装](#更新软件源并安装)
  - [第二步：安装 Distrobox 软件本体](#第二步安装-distrobox-软件本体)
    - [安装脚本默认将二进制文件放在 ~/.local/bin，需要确认该路径在 PATH 中](#安装脚本默认将二进制文件放在-localbin需要确认该路径在-path-中)
    - [验证安装](#验证安装)
  - [创建一个 Ubuntu 22.04 容器](#创建一个-ubuntu-2204-容器)
    - [进入容器](#进入容器)
    - [在容器内安装依赖并运行 AppImage](#在容器内安装依赖并运行-appimage)
  - [第六步：将 CC Switch 导出到宿主桌面（可选但推荐）](#第六步将-cc-switch-导出到宿主桌面可选但推荐)
    - [仍在容器内执行](#仍在容器内执行)
    - [在容器内手动创建 .desktop 文件](#在容器内手动创建-desktop-文件)
    - [然后导出到宿主](#然后导出到宿主)
    - [然后推出容器](#然后推出容器)
- [==========================================](#)
- [常用管理命令备忘](#常用管理命令备忘)
  - [查看所有容器状态](#查看所有容器状态)
  - [停止容器](#停止容器)
  - [删除容器（镜像保留，下次 create 更快）](#删除容器镜像保留下次-create-更快)
  - [在容器内执行单条命令而不进入交互模式](#在容器内执行单条命令而不进入交互模式)
  - [确定当前终端身处何处](#确定当前终端身处何处)

# Distrobox
在容器内运行不兼容的应用：
Distrobox 能创建一个与宿主桌面深度集成的容器，GUI 应用可以直接显示在宿主桌面上，体验接近原生。

[Distrobox 官方网站](https://distrobox.it/)
[常用管理命令](#常用管理命令备忘)

## 安装 distrobox（依赖 Docker 或 Podman）
```bash
sudo apt install podman   # 推荐用 podman，无需 root 守护进程
curl -s https://raw.githubusercontent.com/89luca89/distrobox/main/install | sudo sh
```

## Ubuntu 20.04 官方源不含 Podman，需要先添加第三方源：
### 添加 Kubic 项目的软件源（专门为旧版 Ubuntu 提供 Podman）
```bash
echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04/ /" \
  | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
```
### 导入 GPG 签名密钥
```bash
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04/Release.key \
  | sudo apt-key add -
```
### 更新软件源并安装
```bash
sudo apt update
sudo apt install podman -y

# 验证
podman --version
```
## 第二步：安装 Distrobox 软件本体
Ubuntu 20.04 官方源中的 Distrobox 版本较旧，建议用官方脚本安装最新版：
```bash
curl -s https://raw.githubusercontent.com/89luca89/distrobox/main/install | sh
```

### 安装脚本默认将二进制文件放在 ~/.local/bin，需要确认该路径在 PATH 中
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 验证安装
```bash
distrobox --version
```

## 创建一个 Ubuntu 22.04 容器
```bash
distrobox create --name ubuntu22 --image ubuntu:22.04
```

### 进入容器
```bash
distrobox enter ubuntu22
```

### 在容器内安装依赖并运行 AppImage
```bash
sudo apt update
sudo apt install libfuse2 -y
chmod +x ~/CC-Switch-v3.14.0-Linux-x86_64.AppImage
~/CC-Switch-v3.14.0-Linux-x86_64.AppImage
```

## 第六步：将 CC Switch 导出到宿主桌面（可选但推荐）
这一步完成后，你无需每次手动进入容器，可以像普通应用一样从启动器打开 CC Switch。
### 仍在容器内执行
 先让 AppImage 在容器内完成一次集成，生成 .desktop 文件
 如果之前已安装 AppImageLauncher 则自动完成，否则手动指定
```bash
distrobox-export --app cc-switch
```

### 在容器内手动创建 .desktop 文件
如果 distrobox-export --app 找不到应用（因为 AppImage 未注册），则手动创建后再导出：
```bash
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/cc-switch.desktop << 'EOF'
[Desktop Entry]
Name=CC Switch
Exec=/home/你的用户名/App/cc_switch/CC-Switch-v3.14.0-Linux-x86_64.AppImage
Icon=cc-switch
Type=Application
Categories=Utility;
EOF
```

### 然后导出到宿主
```bash
distrobox-export --app cc-switch
```

如果仍然报错，说明 distrobox-export 匹配名称时大小写敏感，改用完整文件名指定：
```bash
distrobox-export --app "CC Switch"
```
### 然后推出容器
```bash 
distrobox exit # Ctrl+D
```

# ==========================================
# 常用管理命令备忘

## 查看所有容器状态
distrobox list

## 停止容器
distrobox stop ubuntu22

## 删除容器（镜像保留，下次 create 更快）
distrobox rm ubuntu22

## 在容器内执行单条命令而不进入交互模式
distrobox enter ubuntu22 -- ./CC-Switch-v3.14.0-Linux-x86_64.AppImage

## 确定当前终端身处何处
cat /etc/os-release | grep VERSION
