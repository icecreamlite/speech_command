#!/bin/bash
notify-send -t 5000 'Voice Command' 'Restarting'
kill -9 $1
/home/b/projects/speech_command/bash_scripts/speech_command.sh
