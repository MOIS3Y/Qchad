"""
█░█ ▀█▀ █ █░░ █▀ ▀
█▄█ ░█░ █ █▄▄ ▄█ ▄
-- -- -- -- -- -- 
This module contains:

wrapper functions:

nixGL - checks if a utility needs to be run
as a nixGL argument to set the correct variables
environment. This is needed by applications installed from nixpkgs
that use a graphics accelerator.

check_terminal - checks if the user has installed a specific
terminal, if not then the built-in Qtile WM function is used
guess_terminal which will try to guess
which terminal is used by default

utils:

it is the dictionary from which applications are retrieved
which will be given to hotkeys.
"""
import os
from libqtile.utils import guess_terminal

from overlays.helpers import path


# nixGL apps:
def nixGL(app):
    nixgl = os.getenv('QTILE_NIXGL', 'off')
    if nixgl == 'on':
        return f"nixGL {app}"
    return app


def check_terminal():
    terminal = os.getenv('QTILE_TERM', 'default')
    if terminal == 'default':
        return guess_terminal()
    return terminal


utils = {
    # Guess nixGL wrap utils:
    'browser': nixGL('firefox'),
    'terminal': nixGL(check_terminal()),
    'telegram': nixGL('telegram-desktop'),

    # Normal utils:
    'menu': 'rofi -show drun',
    'screenshot': 'flameshot gui',
    'mattermost': 'mattermost-desktop',
    'fmanager': 'ranger',

    # Hardware utils:
    'volume_raise': 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
    'volume_lower': 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
    'volume_muted': 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
    'brightness_up': 'brightnessctl set +10%',
    'brightness_down': 'brightnessctl set 10%-',
}


autostart = {
    'nm-applet': ['nm-applet'],
    'xfce-polkit': ['/usr/libexec/xfce-polkit'],
    'cbatticon': ['cbatticon'],
    'dunst': ['dunst'],
    'picom': ['picom'],
    'xidlehook':[
        f'{path.SCRIPTS}/xidlehook.py',
        f'--lockscreen={path.SCRIPTS}/i3lock.py'],
    # 'touchegg': ['touchegg', '--client']
}
