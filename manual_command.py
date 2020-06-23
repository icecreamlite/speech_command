#!/home/b/projects/speech_command/venv/bin/python3

from tkinter import *
import sc

comm = 'acer '

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
            sc.closeProg()
        elif cSplit[1] == 'restart':
            sc.restartProg()
        else:
            sc.errorMessage(cSplit)
    elif cLen > 2:
        sc.executeVoiceCommand(cSplit)

    comm = 'acer '  

if __name__ == '__main__':
    getComm()