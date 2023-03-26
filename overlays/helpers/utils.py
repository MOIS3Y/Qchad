# █░█ ▀█▀ █ █░░ █▀
# █▄█ ░█░ █ █▄▄ ▄█
# ----------------
import os
from libqtile.utils import guess_terminal


# nixGL apps:
def nixGL(app):
    nixgl = os.getenv('QTILE_NIXGL', 'False')
    if nixgl == 'True':
        return "nixGL {}".format(app)
    return app

def check_terminal():
    terminal = os.getenv('QTILE_TERM', 'None')
    if terminal == 'None':
        return guess_terminal()
    return terminal


utils = {
    # Guess nixGL wrap utils:
    'browser': nixGL('firefox'),
    'terminal': nixGL(check_terminal()),
    'telegram': nixGL('telegram-desktop'),
    # Normal utils:
    'mattermost': 'matermost-desktop',
    'fmanager': 'thunar',
}
