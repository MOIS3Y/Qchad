# █▀█ ▄▀█ ▀█▀ █░█
# █▀▀ █▀█ ░█░ █▀█
# ---------------
import os


theme = os.getenv('QTILE_COLOR_SCHEME', 'catppuccin_mocha')
os_id = os.getenv('QTILE_OS_ID', 'void')

# Absolute path to qtile config:
CONFIG = os.getenv('QTILE_PATH_CONFIG', os.path.expanduser('~/.config/qtile'))

# Relative path to assets:
ASSETS = f'{CONFIG}/assets'

# Relative path to assets:
SCRIPTS = f'{CONFIG}/scripts'

# Get theme-specific layout icons path:
LAYOUTS = f'{ASSETS}/icons/layouts/{theme}'

# Get theme-specific logo:
LOGO = f'{ASSETS}/icons/logo/{os_id}_{theme}.png'

# Get theme-specific power-button:
POWER = f'{ASSETS}/icons/system/power_button_{theme}.png'
