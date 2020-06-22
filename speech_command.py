import speech_recognition as sr
import pyttsx3
import pyaudio
from subprocess import call

r = sr.Recognizer()

engine = pyttsx3.init()

op = {'browser':'firefox',
    'code':'code', 'notes':['xdg-open', 'onenote.com'],
    'facebook':['xdg-open', 'facebook.com'],
    'youtube':['xdg-open', 'youtube.com'],
    'terminal':'x-terminal-emulator',}

with sr.Microphone(0) as source:
    r.energy_threshold = 3000

    print(sr.Microphone.list_microphone_names())

    while True:

        index = -1

        while index == -1:
            audio = r.listen(source)

            try:
                text = str(r.recognize_google(audio)).lower()
                index = text.find('open')
                print(text)
            
            except:
                print("Failed")

        try:
            text = text[index:].split()
            call(op[text[1]])
        except:
            print("Failed")
