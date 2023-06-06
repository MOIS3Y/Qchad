# █▀ █▀▀ █▀█ █▀▀ █▀▀ █▄░█ █▀
# ▄█ █▄▄ █▀▄ ██▄ ██▄ █░▀█ ▄█
# https://docs.qtile.org/en/latest/manual/config/screens.html#screen
# --------------------------
from libqtile.config import Screen
from .bars import chadBar


screens = [
    # Primary monitor:
    Screen(
        top=chadBar
    )
]
