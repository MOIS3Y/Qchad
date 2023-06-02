# █░█ █▀█ █▀█ █▄▀ █▀ 
# █▀█ █▄█ █▄█ █░█ ▄█ 
# http://docs.qtile.org/en/stable/manual/config/hooks.html
# ------------------
import os
import subprocess
from libqtile import hook
from libqtile.log_utils import logger

from overlays.helpers import path
from overlays.helpers import utils


@hook.subscribe.startup_once
def autostart():
    autostart = os.environ.get('QTILE_AUTOSTART', None)    
    if autostart:
        util_list = autostart.lower().split(',')
        for util in util_list:
            if util in utils.autostart:
                logger.warning(f"GET util: {util}: START: {utils.autostart[util]}")
                subprocess.Popen(utils.autostart[util])
    # print(path.SCRIPTS)
    # subprocess.Popen([
    #     f'{path.SCRIPTS}/xidlehook.py',
    #     f'--lockscreen={path.SCRIPTS}/i3lock.py',
    # ])
                

# @hooks.subscribe.startup_complete
# def screensaver():
#     subprocess.Popen([f'{path.SCRIPTS}/autostart.sh'])
