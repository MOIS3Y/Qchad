#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█░░ █▀█ █▀▀ █▄▀  █▀ █▀▀ █▀█ █▀▀ █▀▀ █▄░█ ▀
█▄▄ █▄█ █▄▄ █░█  ▄█ █▄▄ █▀▄ ██▄ ██▄ █░▀█ ▄
https://github.com/Raymo111/i3lock-color
-- -- -- -- -- -- -- -- -- -- -- -- -- --
The script is a wrapper over i3lock-color.
In the current version, it follows the Qtile WM color scheme.

It can also work standalone, for this you need to uncomment
standalone section and comment out the qtile section.
the variable font contains the font that will be used for all elements.
the variable colors contains a dictionary of colors in base16 format.

For more precise color settings, you can use my library
base16-colorlib (pip install base16-colorlib).
The library contains a collection of popular color schemes as well 
as the Color class which can help change the color tints (HSL) 
of individual elements.

Dependencies:
-- -- -- -- 
-i3lock-color
"""


# █▀▄▀█ █▀▀ ▀█▀ ▄▀█ ▀
# █░▀░█ ██▄ ░█░ █▀█ ▄
# -------------------
__author__ = "MOIS3Y"
__credits__ = ["Stepan Zhukovsky"]
__license__ = "GPL v3.0"
__version__ = "0.1.0"
__maintainer__ = "Stepan Zhukovsky"
__email__ = "stepan@zhukovsky.me"
__status__ = "Production"


import pathlib
import subprocess
import sys


# █▀ ▀█▀ ▄▀█ █▄░█ █▀▄ ▄▀█ █░░ █▀█ █▄░█ █▀▀ ▀
# ▄█ ░█░ █▀█ █░▀█ █▄▀ █▀█ █▄▄ █▄█ █░▀█ ██▄ ▄
# -- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- --

# colors = {
#     "scheme": "catppuccin_mocha",
#     "author": "https://github.com/catppuccin/catppuccin",
#     "base00": "#11111b", # crust
#     "base01": "#1e1e2e", # base
#     "base02": "#313244", # surface0
#     "base03": "#45475a", # surface1
#     "base04": "#585b70", # surface2
#     "base05": "#cdd6f4", # text
#     "base06": "#f5e0dc", # rosewater
#     "base07": "#b4befe", # lavender
#     "base08": "#f38ba8", # red
#     "base09": "#fab387", # peach
#     "base0A": "#f9e2af", # yellow
#     "base0B": "#a6e3a1", # green
#     "base0C": "#94e2d5", # teal
#     "base0D": "#89b4fa", # blue
#     "base0E": "#cba6f7", # mauve
#     "base0F": "#f2cdcd", # flamingo
# }

# font = "Sans"

# -- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- --


# █▀█ █▀▀ █░█ ▄▀█ █▀▄ ▀
# ▀▀█ █▄▄ █▀█ █▀█ █▄▀ ▄
# -- -- -- -- -- -- -- 

# require for relative imports:
qchad_dir = str(pathlib.Path(__file__).parents[1])
sys.path.append(qchad_dir)

# import current color scheme and font:
from overlays import colors
from overlays import font


colors = colors.scheme
font = font.SYSTEM
# -- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- --


def i3lock_run(colors, font):
    try:
        subprocess.run([
            # bin:
            'i3lock',
            # params:
            '--screen=1',
            '--blur=2',
            '--clock',
            '--indicator',
            '--line-uses-ring',
            '--radius=110',
            '--ring-width=9',
            '--keylayout=1',
            # colors:
            f'--insidever-color={colors["base02"]}',    # surface
            f'--insidewrong-color={colors["base02"]}',  # surface
            f'--inside-color={colors["base00"]}',       # crust
            f'--ringver-color={colors["base0B"]}',      # green
            f'--ringwrong-color={colors["base08"]}',    # red
            f'--ringver-color={colors["base0B"]}',      # green
            f'--ringwrong-color={colors["base08"]}',    # red
            f'--ring-color={colors["base02"]}',         # surface
            f'--keyhl-color={colors["base0D"]}',        # blue
            f'--bshl-color={colors["base0A"]}',         # yellow
            f'--verif-color={colors["base0B"]}',        # green
            f'--wrong-color={colors["base08"]}',        # red
            f'--layout-color={colors["base0D"]}',       # blue
            f'--separator-color={colors["base05"]}',    # text
            f'--date-color={colors["base05"]}',         # text
            f'--time-color={colors["base05"]}',         # text
            f'--modif-color={colors["base05"]}',        # text
            # font:
            f'--time-font={font}',
            f'--date-font={font}',
            f'--layout-font={font}',
            f'--verif-font={font}',
            f'--wrong-font={font}',
            # text:
            '--time-str=%T',  # %I:%M %p (am/pm)
            '--date-str=%a, %e %b %Y',
            '--verif-text=Verifying...',
            '--wrong-text=Auth Failed',
            '--noinput=No Input',
            '--lock-text=Locking...',
            '--lockfailed=Lock Failed',
            # pass keys:
            '--pass-media-keys',
            '--pass-screen-keys',
            '--pass-volume-keys',
        ])
    except FileNotFoundError as error:
        print(f"i3lock not found.\n{error}")


# entrypoint:
def main():
    i3lock_run(colors=colors, font=font)


if __name__ == "__main__":
    main()
