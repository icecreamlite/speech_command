#!/home/b/projects/speech_command/venv/bin/python3

"""
To modify dictionary:
Add words to train.txt in venv/lib/python3.6/site-packages/pocketsphinx/model
Upload to http://www.speech.cs.cmu.edu/tools/lmtool-new.html
Download generated .tgz file
Copy .dic and .lm file to model and rename .dic file to cmudict-en-us.dict
    and .lm file to en-us.lm.bin while saving the previus one
"""

if __name__ == '__main__':
    from pocketsphinx import LiveSpeech    
from subprocess import Popen
import pyttsx3
import sys

isOpen = False #check if icon is open

engine = pyttsx3.init() #initialize text to speech
engine.setProperty('volume', 1)
engine.setProperty('rate', 170)

scDir = '/home/b/projects/speech_command/'

#Dictionaries of commands
bt = {'on': ['rfkill', 'unblock', 'bluetooth'],
      'off': ['rfkill', 'block', 'bluetooth'],}

con = {'vpn': scDir + 'bash_scripts/connect_vpn.sh'}

deskt = {'one': ['wmctrl', '-s', '0'],
         'two': ['wmctrl', '-s', '1'],
         'three': ['wmctrl', '-s', '2'],
         'show': ['wmctrl', '-k', 'on']}

op = {'browser':'firefox',
      'calcu': 'kcalc',
      'code':'code',
      'downloads': ['dolphin', '/home/b/Downloads'],
      'facebook': ['firefox', 'facebook.com'],
      'idle': ['idle-python3.6'],
      'messenger': ['firefox', 'messenger.com'],
      'model': ['dolphin', scDir + 'venv/lib/python3.6/site-packages/pocketsphinx/model'],
      'notes':['firefox', 'https://onedrive.live.com/redir?resid=BB111DB5197D5585%21338&page=Edit&wd=target%28Quick%20Notes.one%7Cfa9043aa-1386-9546-a932-5aa0da199f45%2FCoins.ph%20Load%20Promo%20Codes%7C15398123-b4a1-4d1c-8c44-73b967d39df1%2F%29&wdorigin=703'],
      'store': '/home/b/projects/sari_store_prices/ssp.sh',
      'terminal': ['konsole'],
      'trainer': ['firefox', 'http://www.speech.cs.cmu.edu/tools/lmtool-new.html'],
      'youtube':['firefox', 'youtube.com']}

ping = {'google': ['konsole', '-p LocalTabTitleFormat=Ping Google', '-p TerminalColumns=103', '-e', 'ping google.com']}

syst = {'shutdown': 'poweroff',
        'reboot': 'reboot'}

trig = {'desktop': deskt,
        'open':op,
        'system': syst,
        'bluetooth': bt,
        'ping': ping,
        'connect': con}   

def closeProg():
    #killTrayIcon()
    Popen(['notify-send', '-t', '5000', 'Voice Command', 'Exiting'])
    engine.say('Goodbye')
    engine.runAndWait()
    Popen([scDir + 'bash_scripts/terminate.sh'])

def restartProg():
    Popen(['notify-send', '-t', '5000', 'Voice Command', 'Restarting'])
    engine.say('Restarting')
    engine.runAndWait()   
    Popen([scDir + 'bash_scripts/restart.sh'])

def errorMessage(pArr):
    Popen(['notify-send', '-t', '5000', 'Voice Command', f'Failed: "{" ".join(pArr[1:]).title()}" command does not exist'])
    engine.say("Failed")
    engine.runAndWait()

def trayIconStatus(status):
    if status == 'inactive':
        filename = scDir + "icons/inactive.ico"
    elif status == 'active':
        filename = scDir + "icons/active.ico"

    global isOpen

    if isOpen:
        Popen(['killall', 'show_icon.py'])
    else:
        isOpen = True

    Popen([scDir + 'bash_scripts/show_icon.sh', f'{filename} {status}'])

def executeVoiceCommand(pArr):     
    try:
        Popen(trig[pArr[1]][pArr[2]])
        Popen(['notify-send', '-t', '5000', 'Voice Command', \
              f'"{" ".join(pArr[1:]).title()}"'])        
        engine.say(' '.join(pArr[1:]))
        engine.runAndWait()   
    except:
        errorMessage(pArr)

def runMain():

    pSplit = [] #initialize command list
    newActivate = True #check if Acer is active

    Popen(['notify-send', '-t', '5000', 'Voice Command', "I'm up!"])
    trayIconStatus('inactive')
    engine.say("I'm up!")
    engine.runAndWait()

    for phrase in LiveSpeech(): #listen to mic
        if len(pSplit) != 0 and pSplit[0] == 'acer':
            pSplit = pSplit[:1] + str(phrase).lower().split()
        else:
            pSplit = str(phrase).lower().split()

        pSplitLen = len(pSplit)

        if pSplitLen > 0 and pSplit[0] == 'acer' and newActivate: #activates voice command when hearing "Acer"
            Popen(['play', '-v 0.7', '-r 70k', scDir + 'audio/activate.wav'])
            Popen(['notify-send', '-t', '5000', 'Voice Command', 'Activated'])
            trayIconStatus('active')
            newActivate = False
                
        if pSplitLen == 2 and pSplit[0] == 'acer':
            if pSplit[1] == 'terminate': #exit/kill/terminate program
                closeProg()
            elif pSplit[1] == 'deactivate': #stop listening for commands
                Popen(['play', '-v 0.7', scDir + 'audio/deactivate.wav'])
                Popen(['notify-send', '-t', '5000', 'Voice Command', 'Deactivated'])
                trayIconStatus('inactive')
                newActivate = True
                pSplit = []
            elif pSplit[1] == 'restart': #restarts the program. Useful for restarting if there are changes in script
                restartProg()

        if pSplitLen == 3 and pSplit[0] == 'acer' and pSplit[1] in trig.keys(): #execute command after hearing valid command
            executeVoiceCommand(pSplit)


if __name__ == '__main__':
    runMain()