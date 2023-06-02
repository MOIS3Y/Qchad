#!/bin/env bash

export QTILE_NIXGL='off'
export QTILE_TERM='wezterm'
export QTILE_PATH_CONFIG='.'

Xephyr :5 -ac -br -noreset -screen 1366x768 -dpi 96 -zaphod -glamor &
DISPLAY=:5 dbus-run-session qtile start -c ./config.py
