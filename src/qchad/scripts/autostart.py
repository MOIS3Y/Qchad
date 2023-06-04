#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
▄▀█ █░█ ▀█▀ █▀█ █▀ ▀█▀ ▄▀█ █▀█ ▀█▀ ▀
█▀█ █▄█ ░█░ █▄█ ▄█ ░█░ █▀█ █▀▄ ░█░ ▄
-- -- -- -- -- -- -- -- -- -- -- -- 
"""
import os
import argparse
import subprocess


def autostart(utils, path=''):
    # Set your autostart utils here
    # name : ['exec', 'args', ...]
    autostart_utils = {
        'test': ['dunstify', 'Test', 'autostart work good'],
        'nm-applet': ['nm-applet'],
        'xfce-polkit': ['/usr/libexec/xfce-polkit'],
        'cbatticon': ['cbatticon'],
        'dunst': ['dunst'],
        'picom': ['picom'],
        'touchegg': ['touchegg', '--client'],
        'xidlehook':[
            f'{path}xidlehook.py',
            f'--lockscreen={path}lockscreen.py'
        ],
        # ...
    }

    util_list = utils.lower().split(',')
    for util in util_list:
        if util in autostart_utils:
            subprocess.Popen(autostart_utils[util])


def main():
    parser = argparse.ArgumentParser(description='Autorun utilities')
    parser.add_argument(
        '-u',
        '--utils',
        required=True,
        help='comma-separated utility names'
    )
    parser.add_argument(
        '-p',
        '--path',
        help="If the path to the executable is not set in $PATH"
    ),
    args: Namespace = parser.parse_args()

    autostart(utils=args.utils, path=args.path)


if __name__ == "__main__":
    main()
