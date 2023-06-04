"""
█▀█ ▄▀█ ▀█▀ █░█ ▀
█▀▀ █▀█ ░█░ █▀█ ▄
-- -- -- -- -- --
The module contains paths to various configuration items.
Each path is stored in a constant.

The CONFIG constant contains the full path to the entire configuration.
This allows you to run a Qtile WM instance in a separate window
Xephyr for development.
If CONFIG is not set, the path will be standard
~/.config/qtile

All other constants concatenate the path from CONFIG.

Therefore icons logo and color scheme for layout
match the given color scheme.
My current color scheme for the whole system is
catppuccin_mocha
My current OS is Void Linux

In addition, I tried to save all the scripts that,
somehow used in Qtile WM inside this repository.
This means that when calling them I need to pass the full path
to the executable.
The SCRIPTS constant solves this problem.

I import the module entirely.
The reference to constants is very clear:

import path

path.LOGO
Path.SCRIPTS ...

"""
import os


theme = os.getenv('QTILE_COLOR_SCHEME', 'catppuccin_mocha')
os_id = os.getenv('QTILE_OS_ID', 'void')

# Absolute path to qtile config:
CONFIG = os.getenv('QTILE_PATH_CONFIG', os.path.expanduser('~/.config/qtile'))

# Full path to assets:
ASSETS = f'{CONFIG}/assets'

# Full path to scripts:
SCRIPTS = f'{CONFIG}/scripts'

# Get theme-specific layout icons path:
LAYOUTS = f'{ASSETS}/icons/layouts/{theme}'

# Get theme-specific logo:
LOGO = f'{ASSETS}/icons/logo/{os_id}_{theme}.png'

# Get theme-specific power-button:
POWER = f'{ASSETS}/icons/system/power_button_{theme}.png'
