import os
import psutil as p
import win32gui

print(p.cpu_count())
print(p.cpu_times())
print(p.virtual_memory())
print(p.net_io_counters())

name="此电脑"

hwnd=win32gui.FindWindow(None,name)
if hwnd:
    print("成功找到")
else:
    print("没有找到窗口，请重试!")
    exit()

print(hwnd)
win32gui.SetForegroundWindow(hwnd)
