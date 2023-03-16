#!/bin/env zsh

export QTILE_NIXGL='True'
export QTILE_TERM='alacritty'

Xephyr :5 -ac -br -noreset -screen 1366x768 -dpi 96 -zaphod -glamor &
DISPLAY=:5 dbus-run-session qtile start -c ./config.py

