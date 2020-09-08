import os

import win32api


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def findInAllDrives(exe):
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        res = find(exe, drive)
        if res != None:
          return res
    return None

print("dce"[1:])