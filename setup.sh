#!/bin/bash

# Detect the operating system
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)
        # Check the distribution
        if command -v apt-get >/dev/null 2>&1; then
            # Debian-based distribution (Ubuntu, Linux Mint, etc.)
            sudo apt-get update
            sudo apt-get install -y python3 python3-venv
        elif command -v dnf >/dev/null 2>&1; then
            # Red Hat-based distribution (CentOS, Fedora, etc.)
            sudo dnf install -y python3
        elif command -v pacman >/dev/null 2>&1; then
            # Arch Linux
            sudo pacman -Sy python3
        else
            echo "Unsupported Linux distribution. Please install Python 3 manually."
            exit 1
        fi
        ;;
    Darwin*)
        # macOS
        if command -v brew >/dev/null 2>&1; then
            # Install using Homebrew
            brew install python3
        else
            echo "Homebrew not found. Please install Python 3 manually."
            exit 1
        fi
        ;;
    *)
        echo "Unsupported operating system. Please install Python 3 manually."
        exit 1
        ;;
esac

# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Install pytest
pip install pytest

echo "Virtual environment setup complete with Python 3 and pytest installed. Use 'source myenv/bin/activate' to activate."