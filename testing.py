import keyboard, time, subprocess
from datetime import datetime
import pyautogui
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('classTime')
parser.add_argument('meetingId')
parser.add_argument('meetingLength')
parser.add_argument('password')
args = parser.parse_args()

#Personal Settings
classTime = args.classTime
password = args.password
meetingId = args.meetingId
meetingLength = args.meetingLength

#Buttons
zoomExePath = "C:\\Users\\29469\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
capturaExePath = "C:\\Program Files (x86)\\Captura\\captura.exe"
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
    time.sleep(5)

def main():
    while(1):
        timestr = datetime.now().strftime("%H:%M")

        if classTime == timestr:
            subprocess.Popen(zoomExePath)
            time.sleep(5)

            #Setting up zoom
            locateAndClick(firstJoin)
            keyboard.write(meetingId)
            locateAndClick(secondJoin)
            if password[0] == 'T':
                keyboard.write(password[2:])
            time.sleep(3)
            locateAndClick(joinAfterPassword)
            time.sleep(2)
            
            #Setting up Captura
            subprocess.Popen(capturaExePath)
            locateAndClick(startRecord)
            locateAndClick(minimizeWindow)
            time.sleep(int(meetingLength) * 60)

            #Exits
            subprocess.Popen(capturaExePath)
            locateAndClick(stopRecord)
            print("disconnect time: "+ datetime.now().strftime("%H:%M"))
            break

if __name__ == '__main__':
    main()