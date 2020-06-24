#!/bin/bash
killall show_icon.py sc.py
notify-send -t 3000 'Voice Command' 'Restarting' | nohup $1sc.py </dev/null &>/dev/null &
