#!/home/b/projects/speech_command/venv/bin/python3

import PySimpleGUIQt as st
import sys, sc,  manual_command
#from os import getpid


#pidStream = open('/home/b/projects/speech_command/show_icon_pid.txt', 'w')
#pidStream.write(str(getpid()))
#pidStream.close()

if sys.argv[2] == 'inactive':
    tt = 'Say "Acer" to activate'
else:
    tt = 'Waiting for command'

#Set System Tray Icon
menu_def = ['BLANK', ['&Restart', '&Exit']]
tray = st.SystemTray(menu=menu_def, tooltip = tt, filename = sys.argv[1])

while True:

    # comm = 'acer '
    clicked = tray.read()

    if clicked == '__ACTIVATED__':

        doub_clicked = tray.read(timeout=150)

        if doub_clicked == '__ACTIVATED__':
            sc.restartProg()
        
        else:
            manual_command.getComm()

    elif clicked == 'Exit':
        sc.closeProg()
    elif clicked == 'Restart':
        sc.restartProg()
