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

сonstants that contain commands to run utilities or custom wrapper scripts

import utils


utils.TERMINAL
utils.BROWSER ...
"""
import os
from libqtile.utils import guess_terminal

from . import path
from . import font


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


def check_updates():
    os_id = os.getenv('QTILE_OS_ID', None)
    if os_id == 'void':
        return 'xbps-install -Mun'


color_scheme = os.getenv("QTILE_COLOR_SCHEME", "catppuccin_mocha")


# Guess nixGL wrap utils:
BROWSER = nixGL('firefox')
TERMINAL = nixGL(check_terminal())
TELEGRAM = nixGL('telegram-desktop')

# Normal utils:
MENU = 'rofi -show drun'
SCREENSHOT = 'flameshot gui'
MATTERMOST = 'mattermost-desktop'
FMANAGER = f'{TERMINAL} -e ranger'
VOLUME_CONTROL = 'pavucontrol'

# Custom utils:
CAFFEINE_STATUS = f'{path.SCRIPTS}/caffeine.py'
CAFFEINE_TOGGLE = f'{path.SCRIPTS}/caffeine.py --toggle'
LOCKSCREEN = f'{path.SCRIPTS}/lockscreen.py -s {color_scheme} -f {font.SYSTEM}'
NOTIFICATION_STATUS = f'{path.SCRIPTS}/notification.py --status'
NOTIFICATION_TOGGLE = f'{path.SCRIPTS}/notification.py --toggle'
NOTIFICATION_HISTORY = 'dunstctl history-pop'
POWER_MENU = f'{path.SCRIPTS}/power_menu.py'
CHECK_UPDATES = check_updates()
KEYBOARD_LAYOUT_SWITCH = 'xkb-switch -n'
KEYBOARD_LAYOUT_SHOW = 'xkb-switch'

# Hardware utils:
VOLUME_RAISE = 'pactl set-sink-volume @DEFAULT_SINK@ +5%'
VOLUME_LOWER = 'pactl set-sink-volume @DEFAULT_SINK@ -5%'
VOLUME_MUTED = 'pactl set-sink-mute @DEFAULT_SINK@ toggle'

BRIGHTNESS_UP = 'brightnessctl set +10%'
BRIGHTNESS_DOWN = 'brightnessctl set 10%-'
BRIGHTNESS_SCROLL= 'brightnessctl set {}%'
