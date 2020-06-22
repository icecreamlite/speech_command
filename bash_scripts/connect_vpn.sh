#!/bin/bash
echo "sudo openvpn --config 'Installer and Configs'/OVPN/config.ovpn --auth-user-pass 'Installer and Configs'/OVPN/pass.txt" | xclip -selection c
wmctrl -s 2
konsole -p 'LocalTabTitleFormat=OpenVPN'
