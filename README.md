# Cinema Mode

MacOS utility to automatically reduce distractions by muting other sounds
and directing only your selected media app to your speakers. Supports
multiple languages (English, Turkish).

## Features
- Silence all other applications
- Direct selected media app audio to speakers
- Multi-language support (English, Turkish)
- Easy installation and setup with integrated BlackHole virtual audio device
- Volume state management (restore previous volume when deactivating)
- Error handling during installation

## Installation

1. Clone the repository:
```bash
git clone git@github.com:DearSoftvan/CinemaMode.git
cd CinemaMode
```

2. Run the installation script (password may be required):
```bash
bash install.sh
```

## Usage

Activate Cinema Mode:
```bash
python3 src/cinema_mode.py --lang en
```

Deactivate Cinema Mode:
```bash
python3 src/cinema_mode.py --lang en --deactivate
```

- `--lang en` or `--lang tr` specifies the language (English or Turkish).
- When activating, the current system volume is stored. Deactivating restores the previous volume or defaults to 100% if unknown.
- Only the selected media app will play sound through your speakers while Cinema Mode is active.

