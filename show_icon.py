#!/home/b/projects/speech_command/venv/bin/python3

import PySimpleGUIQt as st
import sys, manual_command
from subprocess import Popen

scDir = '/home/b/projects/speech_command/'

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
            Popen([scDir + 'bash_scripts/restart.sh', scDir])
        
        else:
            manual_command.getComm()

    elif clicked == 'Exit':
        Popen([scDir + 'bash_scripts/terminate.sh'])
    elif clicked == 'Restart':
        Popen([scDir + 'bash_scripts/restart.sh', scDir])
