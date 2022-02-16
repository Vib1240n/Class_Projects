#!/bin/sh
# chmod 777 start.sh
# PASS="WASD"
awake="awake"
off="off"
brew=$(pmset -g | grep  displaysleep)
if [ ${brew:14} == "10" ];then
    blueutil -p 0
    echo $off
else 
    blueutil -p 0
fi
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"