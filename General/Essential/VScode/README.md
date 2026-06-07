# 目录 <!-- omit in toc -->
- [vscode扩展](#vscode扩展)
  - [导出vscdoe扩展](#导出vscdoe扩展)
  - [导入vscdoe扩展](#导入vscdoe扩展)
  - [直接备份扩展目录](#直接备份扩展目录)
  - [必装扩展](#必装扩展)
  - [推荐扩展](#推荐扩展)

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
- [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)
- [Chinese (Simplified) (简体中文) Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-ceintl.vscode-language-pack-zh-hans)

## 推荐扩展
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
