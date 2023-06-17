"""
█▀▀ ▄▀█ █░░ █░░ █▄▄ ▄▀█ █▀▀ █▄▀ █▀ ▀
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▀█ █▄▄ █░█ ▄█ ▄
-- -- -- -- -- -- -- -- -- -- -- -- 
This module contains functions that are wrapped with a decorator.
Very handy to use as callbacks for mouse button bindings in widgets
The function must be passed as an object without a call

import callbacks


callbacks.toggle_caffeine
callbacks.toggle_notification ...
"""
import os
import subprocess

from libqtile.lazy import lazy
# from libqtile.log_utils import logger

from . import path
from . import utils


# TODO: this is prototype for realtime switch color scheme:
@lazy.function
def update_theme(qtile):
    os.environ['QTILE_COLOR_SCHEME'] = 'onedark'
    qtile.cmd_reload_config()


@lazy.function
def toggle_notification(qtile):
    subprocess.run(utils.NOTIFICATION_TOGGLE, shell=True)
    qtile.widgets_map["notification"].cmd_force_update()


@lazy.function
def switch_keyboard_layout(qtile):
    subprocess.run(utils.KEYBOARD_LAYOUT_SWITCH, shell=True)
    qtile.widgets_map['xkbswitch'].cmd_force_update()


@lazy.function
def toggle_caffeine(qtile):
    subprocess.run(utils.CAFFEINE_TOGGLE, shell=True)


@lazy.function
def toggle_power_menu(qtile):
   subprocess.run(utils.POWER_MENU, shell=True)
