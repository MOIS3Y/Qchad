"""
▀█▀ █░█ █▀▀ █▀▄▀█ █▀▀ ▀ 
░█░ █▀█ ██▄ █░▀░█ ██▄ ▄
-- -- -- -- -- -- -- --
"""

import os

from .color import Color
from .colors import color_schemes


scheme = color_schemes[os.getenv('QTILE_COLOR_SCHEME', 'catppuccin_mocha')] 

# export var for set current color scheme:
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
colors = Color(**scheme)
