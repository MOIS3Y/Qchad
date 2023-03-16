# █░█ ▀█▀ █ █░░ █▀
# █▄█ ░█░ █ █▄▄ ▄█
# ----------------

import os
from libqtile.utils import guess_terminal


# nixGL apps:
def nixGL(app):
    if os.getenv('QTILE_NIXGL'):
        return "nixGL {}".format(app)
    return app


utils = {
    # Guess nixGL wrap utils:
    'browser': nixGL('firefox'),
    'terminal': nixGL(os.getenv('QTILE_TERM', guess_terminal())),
    'telegram': nixGL('telegram-desktop'),
    # Normal utils:
    'mattermost': 'matermost-desktop',
    'fmanager': 'thunar',
}
