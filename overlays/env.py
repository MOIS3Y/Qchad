"""
█▀▀ █▄░█ █░█ ▀
██▄ █░▀█ ▀▄▀ ▄
-- -- -- -- --
This module reads environment variables and uses them as priority settings
in the configuration.

If the environment variable is not set, the default value will be used
from the environment dictionary. This will be reflected in the log:
~/.local/share/qtile/qtile.log

I find this configuration method very convenient, because if I need
fix the color scheme, font, modifier, switch to another OS, etc.
no need to fix the source code.

I set environment variables in ~/.xsession file.
The DM sets these variables before creating a graphics session.
Each exported environment variable is prefixed with QTILE_*

NOTE:
Because I also use nixpkgs on non nixOS distr (Void Linux)
some apps need stat like nixGL arg ($ nixGL alacritty)
https://github.com/guibou/nixGL

I set QTILE_NIXGL=on by default in home-manager .xsession
or from testq.sh when develop. 
"""

import os
import platform
from libqtile.log_utils import logger


environment = {
    # Set current OS id from /etc/os-release, default "void":
    'QTILE_OS_ID': platform.freedesktop_os_release()['ID'],

    # Set qtile config path:
    'QTILE_PATH_CONFIG': os.path.expanduser('~/.config/qtile'),

    # Set terminal, if default - guess_terminal():
    'QTILE_TERM': 'default',

    # Set nixGL for some GL apps from nixpkgs:
    'QTILE_NIXGL': 'off',

    # Set default keys:
    'QTILE_MOD_KEY': 'mod4',

    # Autostart apps:
    'QTILE_AUTOSTART': 'nm-applet,picom,dunst,xfce-polkit,cbatticon,xidlehook',
    
    # Set interface properties:
    'QTILE_COLOR_SCHEME': 'catppuccin_mocha',
    'QTILE_FONT_FAMILY': 'JetBrainsMono Nerd Font Regular',
    'QTILE_FONT_SIZE_GROUPS': '16',
    'QTILE_FONT_SIZE_WIDGETS': '16',
}


def set_env(**environment_vars):
    for env_key, env_var in environment_vars.items():
        get_env = os.getenv(env_key)
        logger.info(f"Set env by user env: {env_key}: {env_var}")

        if not get_env:
            os.environ[env_key] = env_var
            logger.warning(f"Set env by default: {env_key}: {env_var}")


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
set_env(**environment)
