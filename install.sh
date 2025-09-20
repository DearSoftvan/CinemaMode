#!/bin/bash
# CinemaMode Installer with error handling and user guidance

echo "Starting CinemaMode installation..."

# 1. Homebrew kontrolü ve kurulumu
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL 
https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    if [ $? -ne 0 ]; then
        echo "Error: Homebrew installation failed. Please check your 
internet connection and try again."
        exit 1
    fi
else
    echo "Homebrew found."
fi

# 2. BlackHole kurulumu
echo "Installing BlackHole 2ch..."
brew install blackhole-2ch
if [ $? -ne 0 ]; then
    echo "Error: BlackHole installation failed. Please ensure Homebrew is 
working and try again."
    exit 1
fi

# 3. Proje dosyalarını kopyalama
echo "Copying CinemaMode files to ~/Projects/CinemaMode..."
mkdir -p ~/Projects/CinemaMode
cp -r src/* ~/Projects/CinemaMode/
if [ $? -ne 0 ]; then
    echo "Error: Failed to copy project files. Check file permissions."
    exit 1
fi

echo "CinemaMode and BlackHole installed successfully!"
echo "Note: During installation, you may be asked for your computer 
password or SSH key passphrase. Please provide it when prompted."
echo "Run 'python3 ~/Projects/CinemaMode/cinema_mode.py' to activate 
Cinema Mode."

