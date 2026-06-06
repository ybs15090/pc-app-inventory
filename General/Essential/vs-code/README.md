# 目录 <!-- omit in toc -->

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
