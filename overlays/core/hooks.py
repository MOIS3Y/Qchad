"""
█░█ █▀█ █▀█ █▄▀ █▀ ▀
█▀█ █▄█ █▄█ █░█ ▄█ ▄
# http://docs.qtile.org/en/stable/manual/config/hooks.html
-- -- -- -- -- -- -- 
"""
import os
import subprocess
from libqtile import hook
from libqtile.log_utils import logger

from overlays.helpers import path


@hook.subscribe.startup_once
def autostart():
    autostart = os.environ.get('QTILE_AUTOSTART', None)    
    if autostart:
        try:
            subprocess.Popen([
                f"{path.SCRIPTS}/autostart.py",
                '--utils',
                autostart,
                '--path',
                f"{path.SCRIPTS}/"
            ])
        except FileNotFoundError as error:
            logger.warning(f"Check path.SCRIPTS, {error}")
    else:
        logger.warning("No utils to autostart... skip")
