import tkinter as tk  #
import os

window = tk.Tk()
window.title('Zoom & Captura Auto Record')

window.geometry('400x400')
l1 = tk.Label(window, text='1. Class Time (ex. 19:58)', bg='white', font=('Arial', 12), width=30, height=2)
l1.pack()
classTime = tk.Entry(window, show=None, font=('Arial', 14))
l2 = tk.Label(window, text='2. Zoom Meeting ID', bg='white', font=('Arial', 12), width=30, height=2)
l2.pack()
meetingId = tk.Entry(window, show=None, font=('Arial', 14))
l3 = tk.Label(window, text='3. Class Length', bg='white', font=('Arial', 12), width=30, height=2)
l3.pack()
meetingLengthInMins = tk.Entry(window, show=None, font=('Arial', 14))
l4 = tk.Label(window, text='4. Zoom Password (ex. T123/F)', bg='white', font=('Arial', 12), width=30, height=2)
l4.pack()
l5 = tk.Label(window, text='T***... for theres a password', bg='white', font=('Arial', 12), width=30, height=2)
l5.pack()
l6 = tk.Label(window, text='F for no password', bg='white', font=('Arial', 12), width=30, height=2)
l6.pack()
password = tk.Entry(window, show=None, font=('Arial', 14))
classTime.pack()
meetingId.pack()
meetingLengthInMins.pack()
password.pack()

def allSet():
    cT = classTime.get()
    mI = meetingId.get()
    mLIM = meetingLengthInMins.get()
    pW = password.get()

    window.destroy()
    if(pW == ""):
        os.system("python testing.py " + cT + " " + mI + " " + mLIM + " " +"F")
    else:
        os.system("python testing.py " + cT + " " + mI + " " + mLIM + " " +pW)


b = tk.Button(window, text="All Set", command=allSet)
b.pack()
window.mainloop()