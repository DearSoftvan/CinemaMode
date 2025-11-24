#!/usr/bin/env bash
set -e

echo "CinemaMode uninstaller"
echo "This script will attempt to revert audio changes and remove runtime 
files."

APP_DIR="$( cd "$( dirname "$0" )" && pwd )"
SRC_DIR="$APP_DIR/src"
LOCALES_DIR="$SRC_DIR/locales"

read -p "Do you want to restore the previous audio output device (if 
known)? (y/N) " restore
if [[ "$restore" =~ ^[Yy]$ ]]; then
  if command -v SwitchAudioSource >/dev/null 2>&1; then
    # read saved device
    if [[ -f "$LOCALES_DIR/output_device.json" ]]; then
      device=$(python3 - <<PY
import json, sys
p = "$LOCALES_DIR/output_device.json"
try:
    with open(p,'r') as f:
        print(json.load(f).get('device',''))
except:
    pass
PY
)
      if [[ -n "$device" ]]; then
        echo "Restoring audio output to: $device"
        SwitchAudioSource -s "$device" || echo "Failed to set $device"
      fi
    fi
  else
    echo "SwitchAudioSource not found. Cannot restore device 
automatically."
  fi
fi

# Remove runtime files
read -p "Remove runtime files (volume_state.json, output_device.json)? 
(y/N) " remove
if [[ "$remove" =~ ^[Yy]$ ]]; then
  rm -f "$LOCALES_DIR/volume_state.json"
  rm -f "$LOCALES_DIR/output_device.json"
  echo "Runtime files removed."
fi

# Offer to uninstall dependencies
read -p "Uninstall switchaudio-osx and blackhole via brew? (y/N) " 
uninstall_deps
if [[ "$uninstall_deps" =~ ^[Yy]$ ]]; then
  if command -v brew >/dev/null 2>&1; then
    echo "Uninstalling switchaudio-osx..."
    brew uninstall switchaudio-osx || true
    echo "Attempting to uninstall blackhole (may differ by cask/formula 
name)..."
    brew uninstall blackhole-2ch || brew uninstall --cask blackhole || 
true
    echo "Dependencies uninstalled (if they existed)."
  else
    echo "Homebrew not found; cannot uninstall dependencies via brew."
  fi
fi

echo "Uninstall complete."

