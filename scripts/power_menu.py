#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█▀█ █▀█ █░█░█ █▀▀ █▀█  █▀▄▀█ █▀▀ █▄░█ █░█ ▀
█▀▀ █▄█ ▀▄▀▄▀ ██▄ █▀▄  █░▀░█ ██▄ █░▀█ █▄█ ▄
-- -- -- -- -- -- -- -- -- -- -- -- - -- --
"""
import os


icons = {
    # title:
    'power_menu': '󰐦',   # nf-md-power_settings

    # commands:
    'shutdown': '󰐥',     # nf-md-power
    'reboot': '󰜉',       # nf-md-restart
    'suspend': '󰒲',      # nf-md-sleep
    'hibernate': '󰋊',    # nf-md-harddisk
    'logout': '󰍃',       # nf-md-logout
    'lock_screen': '󰌾',  # nf-md-lock

    # toggle:
    'accept': '󰄬',       #nf-md-check
    'deny': '󰅖'          #nf-md-close
}


commands = {
    'shutdown': 'loginctl poweroff',
    'reboot': 'loginctl reboot',
    'hibernate': 'loginctl hibernate',
    'logout': 'loginctl terminate-session self',
    'suspend': 'loginctl suspend',
    'lock_screen': 'dunstify "Power menu" "lock" -u normal'  
}


menu = [
    # -- -- -- -- -- shutdown -- -- -- -- -- --
    {
        'display': f'{icons["shutdown"]} Shutdown',
        'prompt': 'Are you sure?',
        'command': [
            {
                'display': f'{icons["deny"]} No, cancel',
                'command': '',
            },
            {
                'display': f'{icons["accept"]} Yes, shutdown',
                'command': commands["shutdown"]
            }
        ],
    },
    # -- -- -- -- -- reboot -- -- -- -- -- --
    {
        'display': f'{icons["reboot"]} Reboot',
        'prompt': 'Are you sure?',
        'command': [
            {
                'display': f'{icons["deny"]} No, cancel',
                'command': '',
            },
            {
                'display': f'{icons["accept"]} Yes, reboot',
                'command': commands["reboot"]
            }
        ],
    },
    # -- -- -- -- -- logout -- -- -- -- -- --
    {
        'display': f'{icons["logout"]} Logout',
        'prompt': 'Are you sure?',
        'command': [
            {
                'display': f'{icons["deny"]} No, cancel',
                'command': '',
            },
            {
                'display': f'{icons["accept"]} Yes, logout',
                'command': commands["logout"]
            }
        ],
    },
    # -- -- -- -- -- hibernate -- -- -- -- --
    {
        'display': f'{icons["hibernate"]} Hibernate',
        'prompt': 'Are you sure?',
        'command': [
            {
                'display': f'{icons["deny"]} No, cancel',
                'command': '',
            },
            {
                'display': f'{icons["accept"]} Yes, hibernate',
                'command': commands["hibernate"]
            }
        ],
    },
    # -- -- -- -- -- suspend -- -- -- -- -- --
    {
        'display': f'{icons["suspend"]} Suspend',
        'command': commands["suspend"]
    },
    # -- -- -- -- -- lock -- -- -- -- -- -- --
    {
        'display': f'{icons["lock_screen"]} Lock screen',
        'command': commands["lock_screen"]
    },
]


def call_rofi(command):
    answer = os.popen(command).read()[:-1]
    return answer


def parse_menu_fields(menu, prompt='Dmenu'):
    menu_names = []
    menu_actions = []
    menu_prompts = []

    for field in menu:
        menu_names.append(field['display'])
        menu_actions.append(field['command'])

        if 'prompt' in field:
            menu_prompts.append(field['prompt'])
        else:
            menu_prompts.append(prompt)
    return {
        'names': menu_names,
        'actions': menu_actions,
        'prompts': menu_prompts
    }


def power_menu(menu_fields, prompt=f' {icons["power_menu"]} Power Menu: '):
    menu = parse_menu_fields(menu_fields, prompt)

    sep = "\n"

    echo_cmd = f'echo "{sep.join(menu["names"])}"'
    rofi_cmd = f'rofi -dmenu -format i -i -p "{prompt}"'

    command = f'{echo_cmd} | {rofi_cmd}'

    index = call_rofi(command)

    if index != '':
        index = int(index)
        action = menu['actions'][index]

        if type(action) == list:
            power_menu(action, menu['prompts'][index])
        else:
            os.system(action)


# entrypoint:
def main():
    power_menu(menu)


if __name__ == "__main__":
    main()
