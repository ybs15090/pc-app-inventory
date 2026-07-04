# Terminator 用户配置备份

备份日期：2026-07-03
来源路径：`~/.config/terminator/`

## 目录结构

```
config/
├── config      # 主配置文件（快捷键、配色、字体、插件、自定义命令等）
└── plugins/    # 用户插件目录（备份时为空）
```

## 配置概览

- 快捷键：垂直分屏 `Ctrl+Shift+H`
- 配色方案：背景 `#300a24`，前景 `#ffffff`，光标 `#aaaaaa`
- 字体：Ubuntu Mono 16
- 已启用插件：Logger, LaunchpadBugURLHandler, LaunchpadCodeURLHandler, APTURLHandler, TerminalShot, ActivityWatch, InactivityWatch
- 自定义命令菜单：
  - `source ros` → `source ./devel/setup.bash`
  - `ls -a` → `ls -a`

## 恢复方法

将备份文件复制回原位置即可：

```bash
cp -av config/config ~/.config/terminator/config
cp -av config/plugins ~/.config/terminator/plugins
```

恢复后需重启 Terminator 生效。
