# █░█░█ █ █▀▄ █▀▀ █▀▀ ▀█▀ █▀
# ▀▄▀▄▀ █ █▄▀ █▄█ ██▄ ░█░ ▄█
# https://docs.qtile.org/en/latest/manual/ref/widgets.html
# --------------------------
import os
from libqtile import widget
from .helpers import custom_widgets, path
from .ui.theme import colors


default_params = {
    'font': '{} {}'.format(
        os.getenv('QTILE_FONT_FAMILY', 'RobotoMono Nerd Font'),
        os.getenv('QTILE_FONT_STYLE', 'Regular')
        ),
    'size': int(os.getenv('QTILE_FONT_SIZE', 14)), 
}

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


chadBar_widgets = {
    'Logo': widget.Image(
        background=None,
        filename=path.LOGO,
        margin=3,
        margin_x=None,
        margin_y=None,
        mouse_callbacks={},
        rotate=0.0,
        scale=0.8
    ),
    'GroupBox': widget.GroupBox(
        active=colors.scheme['base0D'],
        background=None,
        block_highlight_text_color=colors.scheme['base0B'],
        borderwidth=2,
        center_aligned=True,
        disable_drag=False,
        fmt='{}',
        font=default_params['font'],
        fontsize=default_params['size'],
        foreground=colors.scheme['base05'],
        hide_unused=False,
        highlight_color=[colors.scheme['base00']],
        highlight_method='line',
        inactive=colors.scheme['base04'],
        invert_mouse_wheel=True,
        margin=3,
        margin_x=None,
        margin_y=4,
        markup=True,
        max_chars=0,
        mouse_callbacks={},
        other_current_screen_border='404040',
        other_screen_border='404040',
        # padding=None,
        padding_x=None,
        padding_y=None,
        rounded=True,
        scroll=False,
        scroll_clear=False,
        scroll_delay=2,
        scroll_fixed_width=False,
        scroll_hide=False,
        scroll_interval=0.1,
        scroll_repeat=True,
        scroll_step=1,
        spacing=19,
        this_current_screen_border=colors.scheme['base0B'],
        this_screen_border=colors.scheme['base0D'],
        toggle=True,
        urgent_alert_method='line',
        urgent_border=colors.scheme['base08'],
        urgent_text=colors.scheme['base08'],
        use_mouse_wheel=True,
        visible_groups=None
    ),
    'CurrentLayout': custom_widgets.CurrentLayout(
        background=None,
        fmt='{}',
        font='RobotoMono Nerd Font Bold',
        fontshadow=None,
        fontsize=14,
        foreground=colors.scheme['base0A'],
        markup=True,
        max_chars=0,
        mouse_callbacks={},
        padding=None,
        scroll=False,
        scroll_clear=False,
        scroll_delay=2,
        scroll_fixed_width=False,
        scroll_hide=False,
        scroll_interval=0.1,
        scroll_repeat=True,
        scroll_step=1
    ),
    'CurrentLayoutIcon': widget.CurrentLayoutIcon(
        custom_icon_paths=[path.LAYOUTS],
        scale=0.8
    ),
    'CPUlabel': widget.TextBox(
        background=colors.scheme['base0B'],
        foreground=colors.scheme['base00'],
        font='RobotoMono Nerd Font Regular',
        fontsize=14,
        padding=None,
        text='CPU',
    ),
    'CPU': widget.CPU(
        background=colors.scheme['base02'],
        foreground=colors.scheme['base05'],
        fmt=' {} ',
        font='RobotoMono Nerd Font Regular',
        fontsize=14,
        format='{load_percent}',
        update_interval=1.0,
    ),
    'Systray': widget.Systray(
        background=colors.scheme['base00'],
        icon_size=20,
        mouse_callbacks={},
        padding=25
    ),
}
