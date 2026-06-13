# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi



# >>> fishros initialize >>>
source /opt/ros/noetic/setup.bash
# <<< fishros initialize <<<

# source ~/robot_projects/wpm2_wpv4_demo_ws/devel/setup.bash
source ~/ros_workspaces/wpm2_beifen/devel/setup.bash


# >>PATH 使用冒号分隔多个路径
export PATH="$PATH:/home/s/.local/bin"
export PATH="$PATH:/opt/blender-4.5.9-linux-x64"

# 多线程编译
export ROS_PARALLEL_JOBS='-j12'
export DISABLE_ROS1_EOL_WARNINGS=1
export PATH="$HOME/.npm-global/bin:$PATH"

# 自动获取当前主网络接口IP
# >> 配置ros分布式时启用，其他时间保持注释 >>>
# export ROS_IP=$(hostname -I | awk '{print $1}')
# export ROS_MASTER_URI=ROS_master_IP:11311

# export ROS_HOSTNAME=172.20.10.14
#  <<<  ---  <<<

# >>> IBUS config >>>
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
# <<< IBUS config <<<

# Set-Location ~ # Linux 默认就在用户目录，可视情况取消注释 cd ~
	# 询问用户是否使用代理
	read -p "是否使用代理? (是: y/Y, 否: n/N): " user_input
	# 判断用户输入并执行相应操作
	case "$user_input" in
	    [yY]|"")
	        export http_proxy="http://127.0.0.1:7897"
	        export https_proxy="http://127.0.0.1:7897"
	        echo -e "\033[32m代理已开启。\033[0m" # 绿色输出
	        ;;
	    [nN])
	        unset http_proxy
	        unset https_proxy
	        echo -e "\033[33m代理未开启。\033[0m" # 黄色输出
	        ;;
	    *)
	        echo -e "\033[31m输入无效，默认不开启代理。\033[0m" # 红色输出
	        unset http_proxy
	        unset https_proxy
	        ;;
	esac
	# 自动输出配置文件路径和代理状态
	current_http=${http_proxy:-"NONE"}
	current_https=${https_proxy:-"NONE"}
	# Cyan 颜色 \033[36m
	echo -e "\n\033[36m=========================\033[0m"
	echo "http_proxy     : $current_http"
	echo "https_proxy    : $current_https"
	echo -e "\033[36m=========================\033[0m"

