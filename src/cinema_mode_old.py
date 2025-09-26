#!/usr/bin/env python3
import json
import subprocess
import argparse
import sys

def load_language(lang='en'):
    """Load language JSON file."""
    try:
        with open(f'locales/{lang}.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Language file not found, defaulting to English.")
        with open('locales/en.json', 'r') as f:
            return json.load(f)

def activate_blackhole():
    """Set system audio output to BlackHole (2ch)."""
    try:
        subprocess.run([
            "osascript", "-e",
            'set volume output volume 100',
        ])
        # Buraya ileride CoreAudio veya AppleScript ile BlackHole seçimi eklenebilir
        print("BlackHole audio device should now be active for selected app.")
    except Exception as e:
        print(f"Error activating BlackHole: {e}")

def activate_cinema_mode(lang='en'):
    messages = load_language(lang)
    print(messages['activate'])
    activate_blackhole()
    print(messages['tip'])

def deactivate_cinema_mode(lang='en'):
    messages = load_language(lang)
    print(messages['deactivate'])
    # Buraya default hoparlörü geri almak için kod eklenebilir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cinema Mode for MacOS")
    parser.add_argument('--lang', default='en', help='Language: en or tr')
    parser.add_argument('--deactivate', action='store_true', 
help='Deactivate Cinema Mode')
    args = parser.parse_args()

    if args.deactivate:
        deactivate_cinema_mode(args.lang)
    else:
        activate_cinema_mode(args.lang)

