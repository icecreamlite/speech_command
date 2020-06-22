#!/home/b/projects/speech_command/venv/bin/python3

import PySimpleGUIQt as st
from os import getpid
from subprocess import Popen
import sys

pidStream = open('/home/b/projects/speech_command/show_icon_pid.txt', 'w')
pidStream.write(str(getpid()))
pidStream.close()

if sys.argv[2] == 'inactive':
    tt = 'Say "Acer" to activate'
else:
    tt = 'Waiting for command'

while True:
    tray = st.SystemTray(tooltip = tt, filename = sys.argv[1])
    tray.read()