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
    layout.Matrix(
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        columns=2,
        margin=4
    ),
    layout.Max(
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        margin=4
    ),
    layout.MonadTall(
        align=0,
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        change_ratio=0.5,
        change_size=20,
        margin=4,
        max_ratio=0.75,
        min_ratio=0.25,
        min_secondary_size=85,  # px
        new_client_position='after_current',
        ratio=0.6,  # %
        single_border_width=1,
        single_margin=4        
    ),
    layout.MonadThreeCol(
        align=0,
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        change_ratio=0.5,
        change_size=20,
        main_centered=True,
        margin=4,
        max_ratio=0.75,
        min_ratio=0.25,
        min_secondary_size=85,
        new_client_position='top',
        ratio=0.5,
        single_border_width=1,
        single_margin=4 
    ),
    layout.MonadWide(
        align=0,
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        change_ratio=0.5,
        change_size=20,
        margin=4,
        max_ratio=0.75,
        min_ratio=0.25,
        min_secondary_size=85,
        new_client_position='after_current',
        ratio=0.5,
        single_border_width=1,
        single_margin=4       
    ),
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
