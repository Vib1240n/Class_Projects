import os
import subprocess

filen = "177.py"
search_path = "~/Library/Mobile\ Documents/com~apple~CloudDocs/Development.nosync/Class_Projects/"
# output = subprocess.check_output(f"find ~/Library/Mobile\ Documents/com~apple~CloudDocs/Development.nosync -name {filen} 2>/dev/null", shell=True)
output = subprocess.Popen(f"find {search_path} -name {filen} 2>/dev/null", shell=True, stdout=subprocess.PIPE).communicate()[0]
print(f'output before decoding: {str(output)}')
output = output.decode('utf-8')
print(f'output is {str(output)}')
print(f'output type is {type(output)}')