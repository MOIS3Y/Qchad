# █▀▀ █▀█ █▄░█ ▀█▀ 
# █▀░ █▄█ █░▀█ ░█░ 
# ----------------
import os


FAMILY = os.getenv('QTILE_FONT_STYLE', 'JetBrainsMono Nerd Font Regular')
SIZE_GROUPS = int(os.getenv('QTILE_FONT_SIZE_GROUPS', 26,))
SIZE_WIDGETS = int(os.getenv('FONT_SIZE_WIDGETS', 14))
