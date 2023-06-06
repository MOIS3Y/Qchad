#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█▀ █▀▀ ▀█▀ █░█ █▀█ ▀
▄█ ██▄ ░█░ █▄█ █▀▀ ▄
-- -- -- -- -- -- --
usage: setup.py [-h] [-l] [-i {all,deps,qchad}] [-r {all,deps,qchad}] [-v]

Installing or removing Qchad and dependencies

options:
  -h, --help            show this help message and exit
  -l, --link            Install using soft or hard links
  -i {all,deps,qchad}, --install {all,deps,qchad}
                        Install Qchad
  -r {all,deps,qchad}, --remove {all,deps,qchad}
                        Remove Qchad
  -v, --version         Show version
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
__status__ = "Development"


import os
import argparse
import platform
import pathlib
import subprocess
import shutil
import time


def pkg_mgr_cmd(flag: str | None) -> None:
    # OS:
    supported_os = ['void']
    current_os =  platform.freedesktop_os_release()

    # Packages:
    pkgs = [
        # wm:
        'qtile',
        'python3-psutil',
        # conf:
        'dunst',
        'picom',
        'rofi',
        'i3lock-color'
    ]

    # Package manager cmd for install or remove pkg:
    cmd = {
        'void': {
            'install': ['sudo', 'xbps-install', '-S'],
            'remove': ['sudo', 'xbps-remove']
        }
        # ...
    }

    # Installation:
    if current_os['ID'] in supported_os:
        for pkg in pkgs:
            cmd[current_os['ID']][flag].append(pkg)

        subprocess.run(cmd[current_os['ID']][flag])
            
    # Abort:
    else:
        os = current_os["PRETTY_NAME"]
        msg = f'Sorry, there is no automatic dependency installation for: {os}'
        print(msg)


def mv_to_backup(path: pathlib.PosixPath) -> None:
    if path.exists():
        path.rename(
            (str(path.absolute()) + f'_{time.strftime("%Y-%m-%d_%H-%M-%S")}'))



def install_qchad(soft_link: bool) -> None:
    # qchad src:
    source = pathlib.Path('./')
    # qtile config default path:
    target = pathlib.Path('~/.config/qtile')
    
    # Create backup old config if exist:
    if not target.expanduser().is_symlink() and target.expanduser().exists():
        mv_to_backup(target.expanduser())
    if target.expanduser().exists():
        target.expanduser().unlink()

    if soft_link:
        target.expanduser().symlink_to(source.absolute())
    else:
        shutil.copytree(source.absolute(), target.expanduser())


def remove_qchad(path: str = '~/.config/qtile') -> None:
    target = pathlib.Path(path)
    if target.is_symlink():
        target.unlink()
    else:
        mv_to_backup(target.expanduser())


def install(args: argparse.Namespace):
    if args.install:
        if args.install == 'qchad':
            install_qchad(args.link)

        if args.install == 'deps':
            pkg_mgr_cmd('install')

        if args.install == 'all':
            pkg_mgr_cmd('install')
            install_qchad(args.link)


def remove(args: argparse.Namespace):
    if args.remove:
        if args.remove == 'qchad':
            remove_qchad()

        if args.remove == 'deps':
            pkg_mgr_cmd('remove')

        if args.remove == 'all':
            pkg_mgr_cmd('remove')
            remove_qchad()


def main():
    parser = argparse.ArgumentParser(
        description='Installing or removing Qchad and dependencies',
    )
    parser.add_argument(
        '-l',
        '--link',
        action='store_true',
        default=False,
        help='Install using soft or hard links'
    )
    parser.add_argument(
        '-i',
        '--install',
        choices=['all', 'deps', 'qchad'],
        type=str,
        help='Install Qchad'
    )
    parser.add_argument(
        '-r',
        '--remove',
        choices=['all', 'deps', 'qchad'],
        type=str,
        help='Remove Qchad'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='Show version'
    )
    args = parser.parse_args()

    if args.install:
        install(args)
    if args.remove:
        remove(args)
    if args.version:
        print(__version__)



if __name__ == "__main__":
    main()
