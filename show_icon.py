#!/home/b/projects/speech_command/venv/bin/python3

import PySimpleGUIQt as st
import sys
from tkinter import *
#from os import getpid
from subprocess import Popen
import sc


#pidStream = open('/home/b/projects/speech_command/show_icon_pid.txt', 'w')
#pidStream.write(str(getpid()))
#pidStream.close()



def getComm(): #Popup Entry widget, save typewritten and exit when <Return>
    root = Tk()
    root.title('Acer SC')
    root.resizable(0,0) #remove maximize button

    ws = root.winfo_screenwidth() #get device screeen width
    hs = root.winfo_screenheight() #get device screen height    

    root.geometry(f'+{ws//2-100}+{hs//2-50}') #initialize window position

    def saveComm(event):
        global comm
        comm += event.widget.get().lower()
        root.destroy()

    ent = Entry(root, bd=3, bg='white', fg='black')
    ent.pack()
    ent.focus_set() #focus the entry to type

    root.bind('<Return>', saveComm) #call execComm after pressing enter

    root.mainloop() 

if sys.argv[2] == 'inactive':
    tt = 'Say "Acer" to activate'
else:
    tt = 'Waiting for command'

#Set System Tray Icon
menu_def = ['BLANK', ['&Restart', '&Exit']]
tray = st.SystemTray(menu=menu_def, tooltip = tt, filename = sys.argv[1])

while True:

    comm = 'acer '
    clicked = tray.read()

    if clicked == '__ACTIVATED__':

        doub_clicked = tray.read(timeout=150)

        if doub_clicked == '__ACTIVATED__':
            sc.restartProg()
        
        else:
            getComm()
            cSplit = comm.split()
            cLen = len(cSplit)
            if cLen == 2:
                if cSplit[1] == 'terminate':
                    sc.closeProg()
                elif cSplit[1] == 'restart':
                    sc.restartProg()
                else:
                    sc.errorMessage(cSplit)
            elif cLen == 1:
                continue
            else:
                sc.executeVoiceCommand(cSplit)

    elif clicked == 'Exit':
        sc.closeProg()
    elif clicked == 'Restart':
        sc.restartProg()
