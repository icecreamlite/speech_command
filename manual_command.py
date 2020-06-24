#!/home/b/projects/speech_command/venv/bin/python3

from tkinter import *
from subprocess import Popen
import sc

comm = 'acer '
scDir = '/home/b/projects/speech_command/'

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
    
    global comm
    cSplit = comm.split()
    cLen = len(cSplit)
    if cLen == 2:
        if cSplit[1] == 'terminate':
            Popen([scDir + 'bash_scripts/terminate.sh'])
        elif cSplit[1] == 'restart':
            Popen([scDir + 'bash_scripts/restart.sh', scDir])
        else:
            Popen([scDir + 'bash_scripts/notify_tts.sh', f'Failed: "{" ".join(cSplit[1:]).title()}" command does not exist', 'Failed'])
    elif cLen > 2:
        sc.executeVoiceCommand(cSplit)

    comm = 'acer '  

if __name__ == '__main__':
    getComm()