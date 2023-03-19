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
    'border_normal': colors.scheme['base00'],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Bsp(
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_on_single=False,
        border_width=1,
        fair=False,
        grow_amount=10,
        margin=4,
        margin_on_single=None,
        lower_right=True,
        ratio=1.6,
        warp_clients=False,
    ),
    layout.Columns(
        border_focus=colors.scheme['base0D'],
        border_focus_stack=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_normal_stack=colors.scheme['base00'],
        border_on_single=False,
        border_width=1,
        fair=False,
        grow_amount=10,
        insert_position=1,  # 0 or 1
        margin=4,
        margin_on_single=None,
        num_columns=2,
        split=True,
        wrap_focus_columns=True,
        wrap_focus_rows=True,
        wrap_focus_stacks=True
    ),
    layout.Floating(
        **layout_conf,
        fullscreen_border_width = 0,
        max_border_width = 0
    ),
    layout.Matrix(),
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
