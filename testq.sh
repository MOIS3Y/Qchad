#!/bin/env bash

qchad_path="." 

export QTILE_OS_ID='void'
export QTILE_PATH_CONFIG="${qchad_path}"

export QTILE_NIXGL='off'
export QTILE_TERM='wezterm'
export QTILE_AUTOSTART='test'


export QTILE_COLOR_SCHEME='catppuccin_mocha'
export QTILE_FONT_FAMILY='JetBrainsMono Nerd Font Regular'
export QTILE_FONT_SIZE_GROUPS='16'
export QTILE_FONT_SIZE_WIDGETS='16'

Xephyr :5 -ac -br -noreset -screen 1366x768 -dpi 96 -zaphod -glamor &
DISPLAY=:5 dbus-run-session qtile start -c "${qchad_path}/config.py"
