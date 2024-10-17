import subprocess

pwd = subprocess.PIPE("pwd")
print("pwd: %s"%pwd.stdout)