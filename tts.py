#!/home/b/projects/speech_command/venv/bin/python3

import pyttsx3
import sys

engine = pyttsx3.init()
engine.setProperty('volume', 1)
engine.setProperty('rate', 170)

engine.say(sys.argv[1])
engine.runAndWait()
    