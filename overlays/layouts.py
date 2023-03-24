# █░░ ▄▀█ █▄█ █▀█ █░█ ▀█▀ █▀
# █▄▄ █▀█ ░█░ █▄█ █▄█ ░█░ ▄█
# https://docs.qtile.org/en/latest/manual/ref/layouts.html
# --------------------------
import os
from libqtile import layout
from libqtile.config import Match

from .helpers import font
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
        columns=3,
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
    layout.RatioTile(
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        fancy=False,
        margin=4,
        ratio=1.618,
        ratio_increment=0.1
    ),
    layout.Slice(
        # fallback=layout.max.Max(),  #  set non-slice area
        # match=Match(wm_class='telegram-desktop'),  # check xprop
        # side='left',  # left,right,top,bottom
        # width=360
    ),
    layout.Spiral(
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        clockwise=True,
        main_pane='left',  # left,right,top,bottom
        main_pane_ratio=None,
        margin=4,
        new_client_position='top',  # after_current,before_current,top,bottom
        ratio=0.6180469715698392,
        ratio_increment=0.1
    ),
    layout.Stack(
        autosplit=False,
        border_focus=colors.scheme['base0D'],
        border_focus_stack=colors.scheme['base0C'],
        border_normal=colors.scheme['base00'],
        border_normal_stack=colors.scheme['base00'],
        border_width=1,
        fair=None,
        margin=4,
        num_stacks=2
    ),
    layout.Tile(
        add_after_last=False,
        add_on_top=True,
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_on_single=True,
        border_width=1,
        expand=True,
        margin=4,
        margin_on_single=True,
        master_length=1,
        master_match=None,  # or Match()
        max_ratio=0.85,
        min_ratio=0.15,
        ratio=0.618,
        ratio_increment=0.05,
        shift_windows=False
    ),
    layout.TreeTab(
        active_bg=colors.scheme['base0D'],
        active_fg=colors.scheme['base00'],
        bg_color=colors.scheme['base01'],
        border_width=1,
        font=font.FAMILY,
        fontshadow=None,
        fontsize=font.SIZE_WIDGETS,
        inactive_bg=colors.scheme['base02'],
        inactive_fg=colors.scheme['base05'],
        level_shift=90,
        margin_left=6,
        margin_y=90,
        padding_left=6,
        padding_x=6,
        padding_y=2,
        panel_width=150,
        place_right=False,
        previous_on_rm=True,
        section_bottom=6,
        section_fg=colors.scheme['base0D'],
        section_fontsize=font.SIZE_WIDGETS,
        section_left=6,
        section_padding=4,
        section_top=4,
        sections=['Main', 'Extra'],
        urgent_bg=colors.scheme['base08'],
        urgent_fg=colors.scheme['base00'],
        vspace=4
    ),
    layout.VerticalTile(
        border_focus=colors.scheme['base0D'],
        border_normal=colors.scheme['base00'],
        border_width=1,
        margin=4,
        single_border_width=1,
        single_margin=4
    ),
    layout.Zoomy(
        columnwidth=150,
        margin=4,
        property_big='1.0',
        property_name='ZOOM',
        property_small='0.1'
    )
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
    border_focus=colors.scheme['base0C']
)
