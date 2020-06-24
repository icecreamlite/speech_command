#!/bin/bash
notify-send -t 3000 'Voice Command' 'Exiting' | killall show_icon.py sc.py | espeak Goodbye &
