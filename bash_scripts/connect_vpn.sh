#!/bin/bash
wmctrl -s 2 | echo "sudo openvpn --config 'Installer and Configs'/OVPN/config.ovpn --auth-user-pass 'Installer and Configs'/OVPN/pass.txt" | xclip -selection c
konsole -p 'LocalTabTitleFormat=OpenVPN'
