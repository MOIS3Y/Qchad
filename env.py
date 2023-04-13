# █▀▀ █▄░█ █░█ ▀
# ██▄ █░▀█ ▀▄▀ ▄
# ---------------
import os
import platform
from libqtile.log_utils import logger
# ----------------------------------------------------------
# NOTE:
# Because I also use nixpkgs on non nixOS distr (Void Linux)
# some apps need stat like nixGL arg (nixGL alacritty)
# https://github.com/guibou/nixGL
# I set QTILE_NIXGL = True by default in home-manager .xsession
# or from testq.sh when develop. 
# -----------------------------------------------------------

environment = {
    # Set current OS id from /etc/os-release, default "void":
    'QTILE_OS_ID': platform.freedesktop_os_release()['ID'],

    # Set qtile config path:
    'QTILE_PATH_CONFIG': os.path.expanduser('~/.config/qtile'),

    # Set terminal, if 'None' default - guess_terminal():
    'QTILE_TERM': 'None',

    # Set nixGL for some GL apps from nixpkgs:
    'QTILE_NIXGL': 'False',

    # Set default keys:
    'QTILE_MOD_KEY': 'mod4',
    
    # Set interface properties:
    'QTILE_COLOR_SCHEME': 'catppuccin_mocha',
    'QTILE_FONT_FAMILY': 'JetBrainsMono Nerd Font Regular',
    'QTILE_FONT_SIZE_GROUPS': '30',
    'QTILE_FONT_SIZE_WIDGETS': '18',
}


def set_env(**environment_vars):
    for env_key, env_var in environment_vars.items():
        get_env = os.getenv(env_key)
        logger.info("Set env by userenv: {}: {}".format(env_key, env_var))
        if not get_env:
            os.environ[env_key] = env_var
            logger.warning(
                "Set env by default: {}: {}".format(env_key, env_var)
            )


set_env(**environment)
