import keyboard, time, subprocess
from datetime import datetime
import pyautogui
import argparse
import os
import win32api

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('classTime')
parser.add_argument('meetingId')
parser.add_argument('meetingLength')
parser.add_argument('password')
args = parser.parse_args()

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

def findInAllDrives(exe):
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        res = find(exe, drive)
        if res != None:
          return res
    return None

#Personal Settings
classTime = args.classTime
password = args.password
meetingId = args.meetingId
meetingLength = args.meetingLength

#Buttons
zoomExePath = findInAllDrives("Zoom.exe")
capturaExePath = findInAllDrives("captura.exe")
firstJoin = "buttons\\join_button.png"
secondJoin = "buttons\\join_button_2.png"
joinAfterPassword = "buttons\\join_after_password.png"
startRecord = "buttons\\startrecord.png"
minimizeWindow = "buttons\\captura_minimize.png"
stopRecord = "buttons\\stoprecord.png"

def locateAndClick(path):
    position = None
    while position is None:
        position = pyautogui.locateOnScreen(path, grayscale = False)
    pyautogui.moveTo(position)
    pyautogui.click()
    time.sleep(6)

def main():
    while(1):
        timestr = datetime.now().strftime("%H:%M")

        if classTime == timestr:
            subprocess.Popen(zoomExePath)
            time.sleep(2)

            #Setting up zoom
            locateAndClick(firstJoin)
            keyboard.write(meetingId)
            locateAndClick(secondJoin)
            if password[0] == 'T':
                keyboard.write(password[1:])
                locateAndClick(joinAfterPassword)
            time.sleep(10)

            #Setting up Captura
            subprocess.Popen(capturaExePath)
            time.sleep(2)
            locateAndClick(startRecord)
            locateAndClick(minimizeWindow)
            time.sleep(int(meetingLength) * 60)

            #Exits
            subprocess.Popen(capturaExePath)
            time.sleep(2)
            locateAndClick(stopRecord)
            print("disconnect time: "+ datetime.now().strftime("%H:%M"))
            break

if __name__ == '__main__':
    main()