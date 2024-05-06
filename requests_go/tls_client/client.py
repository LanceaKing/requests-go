import os
import ctypes
from sys import platform
from platform import machine

if platform == 'darwin':
    file_ext = '-darwin_arm64.dylib' if machine() == "arm64" else '-darwin_amd64.dylib'
elif platform in ('win32', 'cygwin'):
    file_ext = '-windows_amd64.dll' if 8 == ctypes.sizeof(ctypes.c_voidp) else '-windows_386.dll'
else:
    if machine() == "aarch64":
        file_ext = '-linux_arm64.so'
    elif machine() == "x86_64":
        file_ext = '-linux_amd64.so'
    else:
        file_ext = '-linux_386.so'

root_dir = os.path.abspath(os.path.dirname(__file__))
library = ctypes.cdll.LoadLibrary(f'{root_dir}/dependencies/requests-go{file_ext}')

request = library.request
request.argtypes = [ctypes.c_char_p]
request.restype = ctypes.c_char_p

freeMemory = library.freeMemory
request.argtypes = [ctypes.c_char_p]
