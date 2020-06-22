#!/home/b/projects/speech_command/venv/bin/python3
from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print(phrase)