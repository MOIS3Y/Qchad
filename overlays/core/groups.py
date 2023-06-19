"""
█▀▀ █▀█ █▀█ █░█ █▀█ █▀ ▀
█▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█ ▄
http://docs.qtile.org/en/stable/manual/config/groups.html
-- -- -- -- -- -- -- -- 

This module contains 7 groups.
5 main groups [WEB, TERM, CHAT, DEV, EXTRA]
2 additional [CALL, ART].
Additional groups will appear in the list and will be available after launch
applications associated with these groups.
"""
from libqtile.config import Group, Match, ScratchPad, DropDown

from overlays.helpers import utils


groups = [
    Group(
        name='WEB',  
        matches=[Match(wm_class=['Firefox'])],
        exclusive=False,
        layout='bsp',
        persist=True,
        init=True,
        label=''  # nf-fa-firefox
    ),
    Group(
        name='TERM',  
        matches=[],
        exclusive=False,
        layout='bsp',
        persist=True,
        init=True,
        label=''  # nf-fa-get_pocket
    ),
    Group(
        name='CHAT',  
        matches=[Match(wm_class=['Mattermost', 'TelegramDesktop'])],
        exclusive=False,
        layout='bsp',
        persist=True,
        init=True,
        label=""  # nf-fa-envelope
    ),
    Group(
        name='DEV',  
        matches=[Match(wm_class=["Code"])],
        exclusive=False,
        layout='bsp',
        persist=True,
        init=True,
        label=''  # nf-fa-slack
    ),
    Group(
        name='EXTRA',  
        matches=[],
        exclusive=False,
        layout='bsp',
        persist=True,
        init=True,
        label=''  # nf-fa-dollar
    ),
    Group(
        name='CALL',  
        matches=[Match(wm_class=['zoom', 'linphone'])],
        exclusive=False,
        layout='floating',
        persist=False,
        init=False,
        label=''  # nf-fa-phone
    ),
    Group(
        name='ART',  
        matches=[Match(wm_class=['Inkscape'])],
        exclusive=False,
        layout='floating',
        persist=False,
        init=False,
        label=''  # nf-fa-paint_brush
    ),
]


groups.append(
    ScratchPad(
        name='scratchpad', 
        dropdowns=[
            DropDown('terminal',
                utils.TERMINAL,
                opacity=0.9,
                x=0.24,
                y=0.3,
                width=0.5,
                height=0.5,
                on_focus_lost_hide=True
            ),
            # ...
        ]
    )
)
