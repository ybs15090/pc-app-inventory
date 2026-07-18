# 目录 <!-- omit in toc -->
- [vscode扩展](#vscode扩展)
  - [导出vscdoe扩展](#导出vscdoe扩展)
  - [导入vscdoe扩展](#导入vscdoe扩展)
  - [直接备份扩展目录](#直接备份扩展目录)
  - [必装扩展](#必装扩展)
  - [推荐扩展](#推荐扩展)
  - [字体设置](#字体设置)
    - [回到 General/Essential](#回到-generalessential)

# vscode扩展

## 导出vscdoe扩展
```bash 
code --list-extensions --show-versions > vscode-extensions.txt
```

## 导入vscdoe扩展
1. Windows powershell
```bash
Get-Content vscode-extensions.txt | ForEach-Object { code --install-extension $_ }
```
2. Linux/MacOS
```bash
cat vscode-extensions.txt | xargs -L 1 code --install-extension
```

## 直接备份扩展目录

扩展实际存放位置：

**Windows：**
```
%USERPROFILE%\.vscode\extensions
```
**Linux：**
```
~/.vscode/extensions
```
直接复制整个目录也可以迁移，但不如 CLI 方法干净。

## 必装扩展
- [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): 不同文件夹显示不同图标
- [Chinese (Simplified) (简体中文) Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-ceintl.vscode-language-pack-zh-hans)
- [Folder Colors](https://marketplace.visualstudio.com/items?itemName=SergeyEgorov.folder-color): 自定义文件夹及文件的颜色,便于区分
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph): git可视化

## 推荐扩展
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
- [Outline Map](https://marketplace.visualstudio.com/items?itemName=Gerrnperl.outline-map): 一个可视化的交互式大纲地图，它结合了大纲地图的清晰度和迷你地图的直观概览。它是 VS Code 内置大纲地图的增强版。
  推荐勾选:"Outline-map>Find Ref: Enabled",点击时自动寻找所有引用
- [Window Colors](https://marketplace.visualstudio.com/items?itemName=stuart.unique-window-colors):为每个 VSCode 窗口自动赋予独特的颜色

## 字体设置

`General\Essential\VScode\settings - 2026-07-18-字体优化.json`中有一些常用字体配置,按需取用,记得检查系统中是否已经安装相应字体

---

### [回到 General/Essential](../README.md)
