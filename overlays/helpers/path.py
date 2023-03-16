# █▀█ ▄▀█ ▀█▀ █░█
# █▀▀ █▀█ ░█░ █▀█
# ---------------
import os
from ..ui.theme import colors


# Absolute path to qtile config:
CONFIG = os.getenv('QTILE_PATH_CONFIG', os.path.expanduser('~/.config/qtile'))

# Relative path to assets:
ASSETS = '/overlays/assets'

# Relative path to assets:
SCRIPTS = '/overlays/scripts'

# Get theme-specific layout icons path:
LAYOUTS = CONFIG + ASSETS +'/icons/layouts/{}'.format(colors.scheme['scheme'])

# Get theme-specific logo:
LOGO = CONFIG + ASSETS + '/icons/logo/{}/{}.png'.format(
    colors.scheme['scheme'], os.getenv('QTILE_OS_ID', 'void'))
