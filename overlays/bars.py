# █▄▄ ▄▀█ █▀█ █▀
# █▄█ █▀█ █▀▄ ▄█
# https://docs.qtile.org/en/latest/manual/config/screens.html#bar
# --------------

from libqtile import bar
from .ui.theme import colors
from .widgets import chadBar_widgets, separator, spacer


chadBar = bar.Bar(
    widgets=[
        # ------- left ------
        chadBar_widgets['Logo'],
        separator(linewidth=0, padding=20, size_percent=100),
        chadBar_widgets['GroupBox'],
        separator(linewidth=0, padding=20, size_percent=100),
        chadBar_widgets['CurrentLayoutIcon'],
        spacer(lenght=3),
        # ------- right ------
        chadBar_widgets['Systray'],
        separator(linewidth=0, padding=30, size_percent=100),
        chadBar_widgets['CPUlabel'],
        chadBar_widgets['CPU'],
        separator(linewidth=0, padding=10, size_percent=100),
        chadBar_widgets['RAM'],
    ],
    size=23,
    background=colors.scheme['base00'],
    border_color=colors.scheme['base00'],
    border_width=7,
    margin=4,
    opacity=1,
)
