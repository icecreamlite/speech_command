#!/bin/bash
killall show_icon.py sc.py
notify-send -t 3000 'Voice Command' 'Restarting' | /home/b/projects/speech_command/bash_scripts/speech_command.sh
