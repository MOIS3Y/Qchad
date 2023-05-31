"""
▀█▀ █░█ █▀▀ █▀▄▀█ █▀▀  █▀ █░█░█ █ ▀█▀ █▀▀ █░█ █▀▀ █▀█ ▀
░█░ █▀█ ██▄ █░▀░█ ██▄  ▄█ ▀▄▀▄▀ █ ░█░ █▄▄ █▀█ ██▄ █▀▄ ▄
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
"""

import os

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.log_utils import logger


# TODO: this is prototype for realtime switch color scheme:
@lazy.function
def update_theme(qtile):
    os.environ['QTILE_COLOR_SCHEME'] = 'onedark'
    qtile.cmd_reload_config()
