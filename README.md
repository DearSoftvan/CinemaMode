cat > README.md << 'EOF'
# Cinema Mode

MacOS utility to automatically reduce distractions by muting other sounds
and directing only your selected media app to your speakers. Supports
multiple languages (English, Turkish).

## Features
- Silence all other applications
- Direct selected media app audio to speakers
- Multi-language support (English, Turkish)
- Easy installation and setup with integrated BlackHole virtual audio device
- Error handling during installation
- Deactivate Cinema Mode and restore previous volume

## Installation

1. Clone the repository:
```bash
git clone git@github.com:DearSoftvan/CinemaMode.git
cd CinemaMode

2. Install required components:
bash install.sh

3.Ensure BlackHole virtual audio device is installed (script handles installation).
Usage
Activate Cinema Mode
# Default English
python3 src/cinema_mode.py

# Turkish
python3 src/cinema_mode.py --lang tr

This will set your speakers volume to 50%
Only the selected media app will play sound through your speakers
Current volume is saved to volume_state.json for later restoration
Deactivate Cinema Mode
# Default English
python3 src/cinema_mode.py --deactivate

# Turkish
python3 src/cinema_mode.py --lang tr --deactivate

Restores the previous volume saved during activation
If previous volume is not found, defaults to 100%
Confirms with a localized message
License
This project is licensed under the MIT License. See LICENSE for details.
