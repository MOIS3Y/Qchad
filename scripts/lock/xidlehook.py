#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import subprocess
"""
▀▄▀ █ █▀▄ █░░ █▀▀ █░█ █▀█ █▀█ █▄▀ ▀
█░█ █ █▄▀ █▄▄ ██▄ █▀█ █▄█ █▄█ █░█ ▄
https://github.com/jD91mZM2/xidlehook
-- -- -- -- -- -- -- -- -- -- -- --
xidlehook is a general-purpose replacement for xautolock.
It executes a command when the computer has been idle
for a specified amount of time.

I install it from nixpkgs:
nix-env -iA nixpkgs.xidlehook

Autorun executes Qtile WM.
For control and temporary suspension I use Caffeine widget.
The feature of this script is the smooth fading of the screen
and screen lock with customized i3lock-color script
which adheres to the Qtile color scheme.

It can be used standalone for this you need to change
path to screen lock executable (i3lock function)

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


def dimmer(direction):
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
        full = 0
        target = 101
        dim = 5
    else:
        full = 100
        target = -1
        dim = -1

    for step in range(full, target, dim):
        cmd = f'xrandr --output {primary_display} --brightness {step/100}; '
        cmd_list.append(cmd)

    return (''.join(cmd_list))


def i3lock():
    # qchad:
    # -- --
    cmd = str(pathlib.Path(__file__).parents[0]) + '/i3lock.py'

    # standalone:
    # -- -- -- --
    # cmd = 'i3lock'
    return cmd


def xidlehook_run():
    displays = get_connected_displays()
    primary= displays[0]
    suspend_message = "Computer will suspend very soon because of inactivity"

    try:
        subprocess.run([
            # bin:
            'xidlehook',
            # Don't lock when there's a fullscreen application:
            '--not-when-fullscreen',
            # Don't lock when there's audio playing:
            '--not-when-audio',
            # Send notification alert:
            '--timer',
            '10',
            f'dunstify "Power" "{suspend_message}" -u normal',
            '',
            # Dim the screen after 10 seconds, undim if user becomes active:
            '--timer',
            '10',
            f'{dimmer("down")}',
            f'{dimmer("up")}',
            # Un dim & lock after 10 more seconds:
            '--timer',
            '10',
            f'{i3lock()}; sleep 1; {dimmer("up")}',
            '',
            # Finally, suspend an hour after it locks:
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
    xidlehook_run()


if __name__ == "__main__":
    main()
