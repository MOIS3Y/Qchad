# █░█ █▀█ █▀█ █▄▀ █▀ 
# █▀█ █▄█ █▄█ █░█ ▄█ 
# http://docs.qtile.org/en/stable/manual/config/hooks.html
# ------------------
import os
import subprocess
from libqtile import hook
from .helpers import path


@hook.subscribe.startup_once
def start_once():
    autostart = f'{path.SCRIPTS}/shell/autostart.sh'
    subprocess.Popen([autostart])


hooks = {
    "start_once": start_once,
}
