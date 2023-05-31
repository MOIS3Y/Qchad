"""
█▀█ ▀█▀ █ █░░ █▀▀   █░█░█ █▀▄▀█ ▀
▀▀█ ░█░ █ █▄▄ ██▄   ▀▄▀▄▀ █░▀░█ ▄
http://www.qtile.org/
-- -- -- -- -- -- -- -- -- -- --
"""
# NOTE: require before other imports
from overlays import env

# wm configuration parts
from overlays import (
    groups,
    hooks,
    keys,
    mod,
    layouts,
    mouse,
    screens
)

# qtile config fields
from overlays.variables import (
    auto_fullscreen,
    bring_front_click,
    dgroups_key_binder,
    dgroups_app_rules,
    cursor_warp,
    focus_on_window_activation,
    follow_mouse_focus,
    wmname
)
