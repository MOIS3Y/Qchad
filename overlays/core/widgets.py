"""
█░█░█ █ █▀▄ █▀▀ █▀▀ ▀█▀ █▀ ▀
▀▄▀▄▀ █ █▄▀ █▄█ ██▄ ░█░ ▄█ ▄
https://docs.qtile.org/en/latest/manual/ref/widgets.html
"""

import os
import subprocess
from libqtile import qtile, widget
from libqtile.lazy import lazy

from overlays.helpers import path, font, custom_widgets
from overlays.ui.theme import colors
from overlays.ui.switcher import update_theme



# █▀▀ █▀▄▀█ █▀█ ▀█▀ █▄█ ▀
# ██▄ █░▀░█ █▀▀ ░█░ ░█░ ▄
# -- -- -- -- -- -- -- --
def spacer(**config):
    return widget.Spacer(
        background=config.get('background', None),
        lenght=config.get('lenght', 50),
        mouse_callbacks=config.get('mouse_callbacks', {}),
    )

def separator(**config):
    return widget.Sep(
        background=config.get('background', None),
        foreground=config.get('foreground', colors.scheme['base05']),
        linewidth=config.get('linewidth', 1),
        mouse_callbacks=config.get('mouse_callbacks', {}),
        padding=config.get('padding', 2),
        size_percent=config.get('size_percent', 2),
    )


# █▀▀ █▀█ █▀▄▀█ █▀▄▀█ █▀█ █▄░█ ▀
# █▄▄ █▄█ █░▀░█ █░▀░█ █▄█ █░▀█ ▄
# -- -- -- -- -- -- -- -- -- -- 
common_widgets = {
    'Logo': widget.Image(
        background=None,
        filename=path.LOGO,
        margin=3,
        margin_x=None,
        margin_y=None,
        mouse_callbacks={},
        rotate=0.0,
        scale=1.0
    ),
    'GroupBox': widget.GroupBox(
        active=colors.scheme['base0D'],
        background=None,
        block_highlight_text_color=colors.scheme['base0B'],
        borderwidth=2,
        center_aligned=True,
        disable_drag=False,
        fmt='{}',
        font=font.FAMILY,
        fontsize=font.SIZE_GROUPS,
        foreground=colors.scheme['base05'],
        hide_unused=False,
        highlight_color=[colors.scheme['base00']],
        highlight_method='text',
        inactive=colors.scheme['base04'],
        invert_mouse_wheel=False,
        margin=3,
        margin_x=None,
        margin_y=None,
        markup=True,
        max_chars=0,
        mouse_callbacks={},
        other_current_screen_border='404040',
        other_screen_border='404040',
        # padding=None,
        padding_x=None,
        padding_y=None,
        rounded=True,
        spacing=19,
        this_current_screen_border=colors.scheme['base0B'],
        this_screen_border=colors.scheme['base0D'],
        toggle=True,
        urgent_alert_method='text',
        urgent_border=colors.scheme['base08'],
        urgent_text=colors.scheme['base08'],
        use_mouse_wheel=True,
        visible_groups=None
    ),
    'CurrentLayoutIcon': widget.CurrentLayoutIcon(
        custom_icon_paths=[path.LAYOUTS],
        scale=0.8
    ),
    'Timelabel': widget.TextBox(
        background=colors.lightness(colors.scheme['base0D'], -4),
        foreground=colors.scheme['base00'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        padding=None,
        text=' 󰥔 ',  # nf-md-clock
    ),
    'Time': widget.Clock(
        background=colors.scheme['base0D'],
        foreground=colors.scheme['base00'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        fmt='{}',
        format='%H:%M',
        markup=True,
        max_chars=0,
        mouse_callbacks={},
        padding=None,
        timezone=None,  # default system TZ
        update_interval=1.0,
    ),
    'DateBox': widget.WidgetBox(
        background=colors.scheme['base0D'],
        foreground=colors.scheme['base00'],
        close_button_location='right',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        start_opened=True,
        text_closed='  ',
        text_open='  ',
        widgets=[
            widget.Clock(
                background=colors.scheme['base0D'],
                foreground=colors.scheme['base00'],
                font=font.FAMILY,
                fontsize=font.SIZE_WIDGETS,
                fmt='{}',
                format='%d-%m-%y %a',
                markup=True,
                max_chars=0,
                mouse_callbacks={},
                padding=None,
                timezone=None,  # default system TZ
                update_interval=1.0,
            ),
        ]
    ),
    'TrayLabel': widget.TextBox(
        background=colors.scheme['base0E'],
        foreground=colors.scheme['base00'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        padding=None,
        text=' 󰳾 '
    ),
    'TrayBox': widget.WidgetBox(
        background=colors.scheme['base01'],
        foreground=colors.scheme['base05'],
        close_button_location='right',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        start_opened=True,
        text_closed='     ',
        text_open='     ',
        widgets=[
            widget.Systray(
            background=colors.scheme['base01'],
            icon_size=16,
            mouse_callbacks={},
            padding=15
            ),
            # separator(
            #     background=colors.scheme['base02'],
            #     linewidth=0,
            #     padding=10,
            #     size_percent=100)
        ]
    ),
    'Power': widget.Image(
        background=None,
        filename=path.POWER,
        margin=3,
        margin_x=None,
        margin_y=None,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                path.SCRIPTS + "/power_menu.py"
            )
        },
        rotate=0.0,
        scale=0.8
    )
}


# █▀▄▀█ █▀█ █▄░█ █ ▀█▀ █▀█ █▀█ █ █▄░█ █▀▀ ▀
# █░▀░█ █▄█ █░▀█ █ ░█░ █▄█ █▀▄ █ █░▀█ █▄█ ▄
# -- -- -- -- -- -- -- -- -- -- -- -- -- --
monitoring_widgets = {
    'CPULabel': widget.TextBox(
        background=colors.scheme['base0B'],
        foreground=colors.scheme['base00'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        padding=None,
        text='CPU'
    ),
    'CPU': widget.CPU(
        background=colors.scheme['base02'],
        foreground=colors.scheme['base05'],
        fmt=' {} ',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        format='{load_percent}',
        update_interval=1.0
    ),
    'RAM': widget.Memory(
        background=None,
        fmt=' {}',  # nf-fae-chip
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        foreground=colors.scheme['base0D'],
        format='{MemUsed: .1f}{mm}',
        markup=True,
        max_chars=0,
        measure_mem='G',
        measure_swap='G',
        mouse_callbacks={},
        padding=None,
        update_interval=1.0
    ),
    'DFLabel': widget.TextBox(
        background=colors.scheme['base00'],
        foreground=colors.scheme['base0D'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        padding=None,
        text='󰋊 '  # nf-md-harddisk
    ),
    'DFRoot': widget.DF(
        background=colors.scheme['base00'],
        foreground=colors.scheme['base0D'],
        fmt='{} ',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        format='ROOT: {uf:.0f}{m}|{r:.0f}%',
        measure='G',
        mouse_callbacks={},
        padding=None,
        partition='/',
        update_interval=60,
        visible_on_warn=True,
        warn_color=colors.scheme['base08'],
        warn_space=3
    ),
    'DFHome': widget.DF(
        background=colors.scheme['base00'],
        foreground=colors.scheme['base0D'],
        fmt='{} ',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        format='HOME: {uf:.0f}{m}|{r:.0f}%',
        measure='G',
        mouse_callbacks={},
        padding=None,
        partition='/home',
        update_interval=60,
        visible_on_warn=True,
        warn_color=colors.scheme['base08'],
        warn_space=10
    ),
    'DFNix':widget.DF(
        background=colors.scheme['base00'],
        foreground=colors.scheme['base0D'],
        fmt='{} ',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        format='NIX: {uf:.0f}{m}|{r:.0f}%',
        measure='G',
        mouse_callbacks={},
        padding=None,
        partition='/nix',
        update_interval=60,
        visible_on_warn=True,
        warn_color=colors.scheme['base08'],
        warn_space=10
    ),
}


# █▀ █▀█ █░█ █▄░█ █▀▄ ▀
# ▄█ █▄█ █▄█ █░▀█ █▄▀ ▄
# -- -- -- -- -- -- --
sound_widgets = {
    'PulseVolume': widget.PulseVolume(
        background=None,
        cardid=None,
        channel='Master',
        check_mute_command='None',
        check_mute_string='[off]',
        device='default',
        emoji=False,
        fmt='  {}',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        foreground=colors.scheme['base0A'],
        get_volume_command=None,
        limit_max_volume=True,
        markup=True,
        max_chars=0,
        mouse_callbacks={},
        padding=3,
        step=5,
        theme_path=None,
        volume_app=None,
        volume_down_command=None,
        volume_up_command=None
    ),
    'Volume': widget.Volume(
        background=None,
        cardid=None,
        channel='Master',
        check_mute_command='None',
        check_mute_string='[off]',
        device='default',
        emoji=False,
        fmt='  {}',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        foreground=colors.scheme['base0A'],
        get_volume_command=None,
        limit_max_volume=True,
        markup=True,
        max_chars=0,
        mouse_callbacks={},
        padding=3,
        step=5,
        theme_path=None,
        volume_app=None,
        volume_down_command=None,
        volume_up_command=None     
    ),
}


# █░░ ▄▀█ █▀█ ▀█▀ █▀█ █▀█ ▀
# █▄▄ █▀█ █▀▀ ░█░ █▄█ █▀▀ ▄
# -- -- -- -- -- -- -- --
laptop_widgets = {
    'Backlight': widget.Backlight(
        background=None,
        backlight_name='intel_backlight',
        change_command='brightnessctl set {}%',
        fmt='  {}',  # nf-fa-adjust
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        foreground=colors.scheme['base08'],
        step=5,
    ),
    'BatteryIcon': widget.BatteryIcon(
        background=None,
        # battery=0,
        scale=1,
        theme_path=path.BATTERY,
        update_interval=60
    )
}


# █▀▀ ▀▄▀ ▀█▀ █▀█ ▄▀█ ▀
# ██▄ █░█ ░█░ █▀▄ █▀█ ▄
# -- -- -- -- -- -- --
extra_widgets = {
    'KeyboardLayout': custom_widgets.KeyboardLayout(
        background=colors.scheme['base00'],
        foreground=colors.scheme['base0D'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        text='UNK',
        update_interval=0.1,
        padding=20
    ),
    'Caffeine': widget.GenPollText(
        background=None,
        foreground=colors.scheme['base0C'],        
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        func=lambda: subprocess.check_output(
            path.SCRIPTS + "/caffeine.py"
        ).decode("utf-8"),
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                path.SCRIPTS + "/caffeine.py --toggle"
            )
        },
        update_interval=1
    ),
    'Switcher': widget.TextBox(
        background=colors.scheme['base0B'],
        foreground=colors.scheme['base00'],
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        mouse_callbacks={'Button1': update_theme},
        padding=None,
        text='SWT ',
    ),
    'Updates': widget.CheckUpdates(
        background=None,
        colour_have_updates=colors.scheme['base0B'],
        colour_no_updates=colors.scheme['base0B'],
        custom_command='xbps-install -Mun',
        display_format='  {updates} pkgs',
        font=font.FAMILY,
        fontsize=font.SIZE_WIDGETS,
        fmt='{}',
        no_update_string='',
        update_interval=60
    )
}
