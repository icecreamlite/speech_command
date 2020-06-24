#!/bin/bash
(notify-send -t 3000 'Voice Command' "$1" | espeak "$2") &
