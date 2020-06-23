#!/bin/bash
notify-send -t 3000 'Voice Command' 'Exiting' | killall show_icon.py sc.py | /home/b/projects/speech_command/tts.py Goodbye &
