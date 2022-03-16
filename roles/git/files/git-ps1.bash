#!/bin/bash
# Provide a custom Bash prompt for Git
export PS1='`if [ $? = 0 ]; then echo "\[\e[32m\] ✔ "; else echo "\[\e[31m\] ✘ "; fi`\[\e[00;37m\]\u\[\e[01;37m\]@\[\e[00;37m\]\h\[\e[01;37m\]:\[\e[01;34m\]\w\[\e[00;34m\] `[[ $(git status 2> /dev/null | head -n4 | tail -n1) != "Changes to be committed:" ]] && echo "\[\e[01;31m\]" || echo "\[\e[01;33m\]"``[[ $(git status 2> /dev/null | tail -n1) != "nothing to commit, working tree clean" ]] || echo "\[\e[01;32m\]"`$(__git_ps1 "(%s)")`echo "\[\e[00m\]"`\$ '
