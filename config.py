# █▀█ ▀█▀ █ █░░ █▀▀   █░█░█ █▀▄▀█
# ▀▀█ ░█░ █ █▄▄ ██▄   ▀▄▀▄▀ █░▀░█
# http://www.qtile.org/
# -------------------------------


# █▀▀ █▄░█ █░█ ▀
# ██▄ █░▀█ ▀▄▀ ▄
# ---------------
import env


# █▀█ █░█ █▀▀ █▀█ █░░ ▄▀█ █▄█ █▀ ▀
# █▄█ ▀▄▀ ██▄ █▀▄ █▄▄ █▀█ ░█░ ▄█ ▄
# --------------------------------

from overlays.groups import groups
from overlays.hooks import hooks
from overlays.keys import mod, keys
from overlays.layouts import layouts, floating_layout
from overlays.mouse import mouse
from overlays.screens import screens


# █▀█ ▀█▀ █ █░░ █▀▀   █░█ ▄▀█ █▀█ █▀ ▀
# ▀▀█ ░█░ █ █▄▄ ██▄   ▀▄▀ █▀█ █▀▄ ▄█ ▄
# https://docs.qtile.org/en/latest/manual/config/
# --------------------------------------

auto_fullscreen = True
bring_front_click = False
dgroups_key_binder = None
dgroups_app_rules = []
cursor_warp = True
focus_on_window_activation = 'urgent'
follow_mouse_focus = True
wmname = 'LG3D'
#---------------------------------------


# █░█ █▀█ █▀█ █▄▀ █▀ ▀
# █▀█ █▄█ █▄█ █░█ ▄█ ▄
# --------------------

 # just comment out the hook to disable
hooks.get('start_once', None)

