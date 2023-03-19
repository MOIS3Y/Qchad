import os
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.log_utils import logger


@lazy.function
def update_theme(qtile):
    new_theme = os.environ['QTILE_COLOR_SCHEME'] = 'onedark'
    qtile.cmd_reload_config()
