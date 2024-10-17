import os
import subprocess as sub
from subprocess import Popen, PIPE, STDOUT
import time


def sudo(cmd):
    psswrd = "wasd"
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    p.stdin.write("{}".format(psswrd))
    output = p.communicate(input=psswrd)

def basic_commands():
    output = sub.run(["xcode-select", "--install"], capture_output=True)
    if output.returncode == 0:
        print(output.stdout)
    if output.returncode == 1:
        print(output.stderr)

def brew():

    cmd = { 1: ["brew", "--version"],
            2: ["brew", "doctor"]
    }
    brewcmd = 'sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'
    for i in cmd:
        output= sub.run(cmd.get(i), capture_output=True)
        if "homebrew-core" in str(output.stdout):
            get = sub.run(['brew', 'update'], capture_output=True)
            print("Brew Installed, continue?(y/n)")
            choice = str(input())
            if choice == 'y' or choice == 'Y':
                continue
        else:
            print("Brew not installed")
            print("Do you want to install brew?(y/n)")
            choice = str(input())
            if choice == 'y' or choice == 'Y':
                brewput = sub.run(brewcmd, capture_output=True)
    return True

def python():
    var = False
    cmds = {
        1 :["python", "--version"],
        2 :["which", "python"],
        3 :["pyenv", "--version"],
        4 :["pyenv", "update"]
    }
    for i in cmds:
        output = sub.run(cmds.get(i), capture_output=True)
        if "3" or ".pyenv" or "pyenv" or "update" in str(output.stdout):
            print(output.stdout)
            var = True
        else:
            print(output.returncode)
            print(output.stderr)
            var = False
        if(var == True):
            return
        else:
            print("do you want to intsall python?(y/n)")
            choice = str(input())
            if choice == 'y' or choice == 'Y':
                cmd = ["brew", "install", "pyenv"]
                sudo(cmd)

                

def java():
    cmds = {
        1: ['java', '--version'],
        2: ['which', 'java']
    }


if __name__ == '__main__':
    sudo()

