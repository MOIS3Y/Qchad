# █░░ ▄▀█ █▄█ █▀█ █░█ ▀█▀ █▀
# █▄▄ █▀█ ░█░ █▄█ █▄█ ░█░ ▄█
# https://docs.qtile.org/en/latest/manual/ref/layouts.html
# --------------------------
import os
from libqtile import layout
from libqtile.config import Match
from .ui.theme import colors

# Layouts and layout rules
layout_conf = {
    'border_focus': colors.scheme['base0D'],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Bsp(
        **layout_conf,
        fair =False,
        grow_amount = 10,
        lower_right = True,
        margin_on_single = 4,
        ratio = 1.6,
        warp_clients = False
    ),
    # layout.Columns(),
    layout.Floating(
        **layout_conf,
        fullscreen_border_width = 0,
        max_border_width = 0
    ),
    # layout.Matrix(),
    # layout.Max(),
    # layout.MonadTall(),
    # layout.MonadThreeCol(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Slice(),
    # layout.Spiral(),
    # layout.Stack(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors.scheme['base0D']
)
