#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█▀▀ ▄▀█ █▀▀ █▀▀ █▀▀ █ █▄░█ █▀▀ ▀
█▄▄ █▀█ █▀░ █▀░ ██▄ █ █░▀█ ██▄ ▄
-- -- -- -- -- -- -- -- -- -- --
The script allows you to view the status of a process.
And also pause the process (kill -STOP pid)
and run it again (kill -CONT pid).

Here it monitors the work of the xidlehook process.
The script returns a process status icon.
It is mainly needed to stop the screensaver with
Qtile WM widget panel.
It's called "caffeine" after the popular widget gnome-shell

Dependencies:
-- -- -- -- 
- psutil
- xidlehook
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
import psutil


def find_process(name):
    for process in psutil.process_iter():
        if name.lower() in process.name().lower():
            return process


def toggle_process(process):
    pid = str(process.pid)
    status = process.status()
    flag = '-STOP'
    if status == 'stopped':
        flag = '-CONT'

    subprocess.run(['kill', flag, pid])


def make_caffeine_icon(process):
    if process.status() != 'stopped':
        return '󰾪 '  # nf-md-coffee_off
    else:
        return '󰅶 '  # nf-md-coffee


def caffeine(name, flag=False):
    try:
        # xidlehook:
        process = find_process(name)
        # --toggle:
        if flag:
            toggle_process(process)
            process = find_process(name)
            return make_caffeine_icon(process)
        else:
            return make_caffeine_icon(process)
    except AttributeError as error:
        return '󰾫 '  # nf-md-coffee_off_outline


def main():
    # -- -- -- -- parser -- -- -- --
    parser = argparse.ArgumentParser(
        description="caffeine app for hidlehook"
    )
    parser.add_argument(
        '--toggle',
        help='toggle hidlehook status',
        action='store_true'
    )
    args = parser.parse_args()
    # -- -- -- -- caffeine -- -- -- --
    print(caffeine('xidlehook', args.toggle), end='')


if __name__ == "__main__":
    main()
