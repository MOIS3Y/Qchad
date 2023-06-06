"""
█▀▀ █▀█ █▄░█ ▀█▀ ▀
█▀░ █▄█ █░▀█ ░█░ ▄
-- -- -- -- -- --
This module contains constants for setting fonts.
Constants get their value from environment variables.
In case the variable is not set by the user or
missing from env.py will be set to default

When importing in the right places in the configuration,
I import the module entirely.
The reference to constants is very clear:

import font

font.FAMILY
font.SIZE ...
"""
import os


FAMILY = os.getenv('QTILE_FONT_STYLE', 'JetBrainsMono Nerd Font Regular')
SIZE_GROUPS = int(os.getenv('QTILE_FONT_SIZE_GROUPS', 26,))
SIZE_WIDGETS = int(os.getenv('FONT_SIZE_WIDGETS', 14))

SYSTEM = os.getenv('QTILE_FONT_SYSTEM', 'Sans')
