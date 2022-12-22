# Нужно собрать информацию про операционную систему и версию Python

import platform
import sys

info = f"OS info is \n{platform.uname()}\n\nPython version is {sys.version}{platform.architecture()}"

print(info)
with open('os_info.txt', 'w') as ff:
    ff.write(info)
