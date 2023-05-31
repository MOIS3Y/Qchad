"""
█▄▄ ▄▀█ █▀█ █▀ ▀
█▄█ █▀█ █▀▄ ▄█ ▄
https://docs.qtile.org/en/latest/manual/config/screens.html#bar
"""
from libqtile import bar

from overlays.ui.theme import colors
from .widgets import (
    common_widgets,
    extra_widgets,
    monitoring_widgets,
    separator,
    spacer
)


separator_20px = separator(linewidth=0, padding=20, size_percent=100)

current_widgets = [
    # ------- left ------
    common_widgets['Logo'],
    separator_20px,
    common_widgets['GroupBox'],
    separator_20px,
    common_widgets['CurrentLayoutIcon'],

    # ------- center ------
    spacer(lenght=3),

    # ------- right ------
    extra_widgets['Updates'],
    separator_20px,
    monitoring_widgets['CPULabel'],
    monitoring_widgets['CPU'],
    separator_20px,
    monitoring_widgets['RAM'],
    separator_20px,
    monitoring_widgets['DFLabel'],
    monitoring_widgets['DFBox'],
    separator_20px,
    common_widgets['TrayLabel'],
    common_widgets['TrayBox'],
    separator_20px,
    extra_widgets['Caffeine'],
    extra_widgets['KeyboardLayout'],
    common_widgets['Timelabel'],
    common_widgets['Time'],
    separator_20px,
    common_widgets['Power'],
]


chadBar = bar.Bar(
    widgets=current_widgets,
    # ------- bar properties ------
    size=21,
    background=colors.scheme['base00'],
    border_color=colors.scheme['base00'],
    border_width=7,
    margin=4,  # gaps around bar
    opacity=1,
)
