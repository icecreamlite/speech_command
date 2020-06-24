#!/bin/bash
notify-send -t 3000 'Voice Command' $1 | nohup play -v 0.7 -r 70k $2 </dev/null &>/dev/null &
