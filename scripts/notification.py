#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█▄░█ █▀█ ▀█▀ █ █▀▀ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀
█░▀█ █▄█ ░█░ █ █▀░ █ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
"""


# █▀▄▀█ █▀▀ ▀█▀ ▄▀█ ▀
# █░▀░█ ██▄ ░█░ █▀█ ▄
# -------------------
__author__ = "MOIS3Y"
__credits__ = ["Stepan Zhukovsky"]
__license__ = "GPL v3.0"
__version__ = "0.1.0"
__maintainer__ = "Stepan Zhukovsky"
__email__ = "stepan@zhukovsky.me"
__status__ = "Production"


import argparse
import subprocess
import sys


def check_paused():
    status =  subprocess.run(
        ['dunstctl','is-paused'],
        capture_output=True,
        encoding="utf-8"
    )
    if status.stdout.rstrip('\n') == 'true':
        return True
    else:
        return False


def make_status_icon():
    if check_paused():
        return '󱏧'  # nf-md-bell_cancel
    else:
        return '󰂚'  # nf-md-bell


def toggle_dunst():
    subprocess.run(['dunstctl', 'set-paused', 'toggle'])


def main():
    parser = argparse.ArgumentParser(
        description='Dunstctl wrapper'
    )
    parser.add_argument(
        '-s',
        '--status',
        action='store_true',
        help='show dunst status'
    )
    parser.add_argument(
        '-t',
        '--toggle',
        action='store_true',
        help='toggle dunst status'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='show version'
    )
    args = parser.parse_args()

    if args.toggle:
        toggle_dunst()
        print(make_status_icon())
    if args.status:
        print(make_status_icon())
    if args.version:
        print(__version__)

    if len(sys.argv) < 2:
        parser.print_help()


if __name__ == "__main__":
    main()
