#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
▀▄▀ █ █▀▄ █░░ █▀▀ █░█ █▀█ █▀█ █▄▀ ▀
█░█ █ █▄▀ █▄▄ ██▄ █▀█ █▄█ █▄█ █░█ ▄
https://github.com/jD91mZM2/xidlehook
-- -- -- -- -- -- -- -- -- -- -- --

usage: xidlehook.py [-h] [-l LOCKSCREEN]

options:
  -h, --help            show this help message and exit
  -l LOCKSCREEN, --lockscreen LOCKSCREEN
                        Path to lockscreen exec file

xidlehook is a general-purpose replacement for xautolock.
It executes a command when the computer has been idle
for a specified amount of time.

I install this by building the xbps package with xbps-src.
The template for building xidlehook 0.10.0 
is available in my void-packages fork:
https://github.com/MOIS3Y/void-packages/tree/voidpkgs

It can also be installed from nixpkgs:
nix-env -iA nixpkgs.xidlehook

I had to create an xbps package just because none of the
autorun ways didn't work for me:
    ~/.xsession
    runit service
    qtile hook
I believe it has something to do with dbus and pulseaudio autostart.
I check the log when I tried to create a runit service.
There are certain problems with utilities using pulseaudio
if you install them from nixpkgs on a nonNixOS distribution.
Although I do not rule out that the problem only affects 
nonNixOS distributions without systemd.

Autorun executes Qtile WM.
For control and temporary suspension I use Caffeine widget.
The feature of this script is the smooth fading of the screen
and screen lock with customized i3lock-color script
which adheres to the Qtile color scheme.

Dependencies:
-- -- -- -- 
- xidlehook
- i3lock
- dunst
- elogind
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


def get_connected_displays():
    """
    returns a list of connected monitors
    to video outputs:
    ['HDMI-A-0', 'DisplayPort-2', #...]
    " connected " - spaces are important so that the evaluation 
    does not confuse with disconnected
    """
    xrandr = subprocess.run(['xrandr'],capture_output=True,encoding="utf-8")
    properties = [line for line in xrandr.stdout.splitlines()]
    return [line.split()[0] for line in properties if " connected " in line]


def dimmer(direction=None):
    """
    allows to smoothly turn the screen on and off.
    variable dim can be set to speed.
    xidlehook expects three arguments in the --timer option:
    time the command to be executed and the cancel command.
    to pass several commands in the first argument here is used
    the trick of creating a long list of commands separated by semicolons.
    """
    displays = get_connected_displays()
    primary_display= displays[0]
    
    cmd_list = []

    if direction == 'up':
        start = 1
        target = 101
        dim = 1
    elif direction == 'down':
        start = 100
        target = -1
        dim = -1
    else:
        start = 100
        target = 101
        dim = 1

    for step in range(start, target, dim):
        cmd = f'xrandr --output {primary_display} --brightness {step/100}; '
        cmd_list.append(cmd)

    return (''.join(cmd_list))


def xidlehook_run(lockscreen):
    suspend_message = "Computer will suspend very soon because of inactivity"
    try:
        subprocess.Popen([
            # bin:
            'xidlehook',
            # Don't lock when there's a fullscreen application:
            '--not-when-fullscreen',
            # Don't lock when there's audio playing:
            '--not-when-audio',
            # Send notification alert:
            '--timer',
            '600',
            f'dunstify "Power" "{suspend_message}" -u normal',
            '',
            # Dim the screen after 15 seconds & lock,
            # un dim if user becomes active:
            '--timer',
            '15',
            f'{dimmer("down")}{lockscreen}',
            f'{dimmer()}',
            # Wait 90 seconds or un dim if user becomes active:
            '--timer',
            '90',
            '',
            f'{dimmer("up")}',
            # Finally, suspend after it locks:
            '--timer',
            '10',
            'loginctl suspend',
            '',
        ])
        print("xidlehook is running")
    except FileNotFoundError as error:
        print(f"xidlehook not found.\n{error}")


# entrypoint:
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l',
        '--lockscreen',
        default='i3lock',
        help='Path to lockscreen exec file'
    )
    args = parser.parse_args()

    xidlehook_run(args.lockscreen)


if __name__ == "__main__":
    main()
