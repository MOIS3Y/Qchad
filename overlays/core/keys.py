"""
█▄▀ █▀▀ █▄█ █▀ ▀
█░█ ██▄ ░█░ ▄█ ▄
https://docs.qtile.org/en/latest/manual/config/keys.html
-- -- -- -- -- -- -- -- -- -- -- -- -- --
"""
import os

from libqtile.config import Key
from libqtile.command import lazy

from .groups import groups
from overlays.helpers import utils


mod = os.getenv('QTILE_MOD_KEY', 'mod4')


keys = [
    # █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ █░░ ▀
    # █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ █▄▄ ▄

    # -- -- -- -- qtile -- -- -- --
    Key(
        [mod, 'control'], 'r',
        lazy.reload_config(),
        desc='Reload the config'
    ),
    Key(
        [mod, 'shift', 'control'], 'r',
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key(
        [mod, "control"], 'q',
        lazy.shutdown(),
        desc='Close the whole Qtile'
    ),

    # █▀▀ █▀█ █▀█ █░█ █▀█ █▀ ▀
    # █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█ ▄

    Key(
        [mod], 'Tab',
        lazy.next_layout(),
        desc='Use next layout on the actual group'
    ),
    Key(
        [mod, 'shift'], 'Tab',
        lazy.prev_layout(),
        desc='Use previous layout on the actual group'
    ),
    Key(
        [mod], 'left',
        lazy.screen.prev_group(),
        desc='Move to the group on the left'
    ),
    Key(
        [mod], 'right',
        lazy.screen.next_group(),
        desc='Move to the group on the right'
    ),

    # █░░ ▄▀█ █▄█ █▀█ █░█ ▀█▀ █▀ ▀
    # █▄▄ █▀█ ░█░ █▄█ █▄█ ░█░ ▄█ ▄

    # -- -- -- -- switch -- -- -- --
    Key(
        [mod], 'j',
        lazy.layout.down(),
        desc='Switch between windows in the current stack pane to the down'
    ),
    Key(
        [mod], 'k',
        lazy.layout.up(),
        desc='Switch between windows in the current stack pane to the up'
    ),
    Key(
        [mod], 'h',
        lazy.layout.left(),
        desc='Switch between windows in the current stack pane to the left'
    ),
    Key(
        [mod], 'l',
        lazy.layout.right(),
        desc='Switch between windows in the current stack pane to the right'
    ),
    # -- -- -- -- grow -- -- -- --
    Key(
        [mod, 'control'], 'j',
        lazy.layout.grow_down(),
        desc='Grow the focused window down'
    ),
    Key(
        [mod, 'control'], 'k',
        lazy.layout.grow_up(),
        desc='Grow the focused window up'
    ),
    Key(
        [mod, 'control'], 'h',
        lazy.layout.grow_left(),
        desc='Grow the focused window left'
    ),
    Key(
        [mod, 'control'], 'l',
        lazy.layout.grow_right(),
        desc='Grow the focused window down'
    ),
    # -- -- -- -- shuffle -- -- -- --
    Key(
        [mod, 'shift'], 'j',
        lazy.layout.shuffle_down(),
        desc='Shuffle focused window down'
    ),
    Key(
        [mod, 'shift'], 'k',
        lazy.layout.shuffle_up(),
        desc='Shuffle focused window up'
    ),
    Key(
        [mod, 'shift'], 'h',
        lazy.layout.shuffle_left(),
        desc='Shuffle focused window left'
    ),
    Key(
        [mod, 'shift'], 'l',
        lazy.layout.shuffle_right(),
        desc='Shuffle focused window right'
    ),
    # -- -- -- -- common -- -- -- --
    Key(
        [mod], 'space',
        lazy.group.next_window(),
        desc='Switch window focus to next window in group'
    ),
    Key(
        [mod, 'shift'], 'space',
        lazy.group.prev_window(),
        desc='Switch window focus to previous window in group'
    ),
    Key(
        [mod, 'shift'], 'f',
        lazy.window.toggle_floating(),
        desc='Put the focused window to/from floating mode'
    ),
    Key(
        [mod], 'w',
        lazy.window.kill(),
        desc='Close the focused window'
    ),

    # █░█ ▄▀█ █▀█ █▀▄ █░█░█ ▄▀█ █▀█ █▀▀ ▀
    # █▀█ █▀█ █▀▄ █▄▀ ▀▄▀▄▀ █▀█ █▀▄ ██▄ ▄

    # -- -- -- -- volume -- -- -- --
    Key(
        [], 'XF86AudioLowerVolume',
        lazy.spawn(utils.VOLUME_LOWER),
        desc='Volume lower'
    ),
    Key(
        [], 'XF86AudioRaiseVolume',
        lazy.spawn(utils.VOLUME_RAISE),
        desc='Volume raise'
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn(utils.VOLUME_MUTED),
        desc='Volume muted'
    ),
    # -- -- -- -- brightness -- -- -- --
    Key(
        [], 'XF86MonBrightnessUp',
        lazy.spawn(utils.BRIGHTNESS_UP),
        desc='Brightness up'
    ),
    Key(
        [], 'XF86MonBrightnessDown',
        lazy.spawn(utils.BRIGHTNESS_DOWN),
        desc='Brightness down'
    ),

    # ▄▀█ █▀█ █▀█ ▀
    # █▀█ █▀▀ █▀▀ ▄

    Key(
        [mod], 'Return',
        lazy.spawn(utils.TERMINAL),
        desc='Terminal'
    ),
    Key(
        [mod], 'm',
        lazy.spawn(utils.MENU),
        desc='Menu'
    ),
    Key(
        [mod], 'b',
        lazy.spawn(utils.BROWSER),
        desc='Browser'
    ),
    Key(
        [mod], 'f',
        lazy.spawn(utils.FMANAGER),
        desc='File manager'
    ),
    Key(
        [], 'Print',
        lazy.spawn(utils.SCREENSHOT),
        desc='Screenshot app'
    )
]

# -- -- -- -- -- -- -- -- -- -- -- -- -- --
for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key(
            [mod], actual_key,
            lazy.group[group.name].toscreen(),
            desc=f'Switch focused window to the group {group.name}'
        ),
        Key(
            [mod, "shift"], actual_key,
            lazy.window.togroup(group.name),
            desc=f'Move focused window to the group {group.name}'
        )
    ])
